import datetime

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.database import Base, Case, ParagraphNote, ParagraphNoteLink, get_db
from backend.main import app
from backend.reader_layers import LINKS_LABEL, case_note_links


@pytest.fixture
def db():
	engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
	Base.metadata.create_all(engine, tables=[Base.metadata.tables[n] for n in ("cases", "paragraph_notes", "paragraph_note_links")])
	with Session(engine) as session:
		for i in (1, 2, 3, 4):
			session.add(Case(id=i, title=f"Party {i} v. Canada", citation=f"2020 FC {i}", court="FC", full_text="x", date=datetime.date(2020, 1, 1)))
			for para in (5, 6):
				session.add(ParagraphNote(case_id=i, para=para, version=1, note=f"note {i}.{para}", source="t"))
		for other, score in ((2, 8), (3, 10), (4, 9)):
			session.add(ParagraphNoteLink(case_id=1, para=5, other_case_id=other, other_para=6, score=score, source="links-v1"))
		session.add(ParagraphNoteLink(case_id=1, para=6, other_case_id=2, other_para=5, score=9, source="links-v1"))
		# a link whose far-end note was never stored is not shown
		session.add(ParagraphNoteLink(case_id=1, para=6, other_case_id=3, other_para=99, score=10, source="links-v1"))
		session.commit()
		yield session


def test_links_are_grouped_by_paragraph_best_two_first_with_far_end_note(db):
	out = case_note_links(1, db)
	assert out["available"] and out["label"] == LINKS_LABEL and "same point" not in out["label"].lower()
	first, second = out["items"]
	assert (first["para"], first["note"]) == (5, "note 1.5")
	assert [(l["case_id"], l["score"]) for l in first["links"]] == [(3, 10), (4, 9)]
	assert first["links"][0]["citation"] == "2020 FC 3" and first["links"][0]["note"] == "note 3.6"
	assert [l["para"] for l in second["links"]] == [5]
	assert "60%" in out["note"] and "92 to 98%" in out["note"]


def test_decision_without_links_is_unavailable_and_route_reads_stored_rows(db):
	assert case_note_links(2, db) == {"available": False}
	app.dependency_overrides[get_db] = lambda: db
	try:
		client = TestClient(app)
		assert client.get("/cases/1/note-links").json()["available"] is True
		assert client.get("/cases/9/note-links").json() == {"available": False}
	finally:
		app.dependency_overrides.clear()
