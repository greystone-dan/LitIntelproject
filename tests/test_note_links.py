import datetime

import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.database import Base, Case, ParagraphNote, ParagraphNoteLink
from scripts import load_note_links as loader


@pytest.fixture
def db():
	engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
	names = ("cases", "paragraph_notes", "paragraph_note_links")
	Base.metadata.create_all(engine, tables=[Base.metadata.tables[n] for n in names])
	with Session(engine) as session:
		for i, cite in ((1, "2020 FC 1"), (2, "2021 FC 2")):
			session.add(Case(id=i, title=f"A v. B {i}", citation=cite, court="FC", full_text="x", date=datetime.date(2020, 1, 1)))
			session.add(ParagraphNote(case_id=i, para=5, version=1, note="n", source="t"))
		session.commit()
		yield session


ROW = {"citation_key": "2020_FC_1", "para": 5, "other_citation_key": "2021_FC_2", "other_para": 5, "score": 9}


def test_dry_run_then_apply_is_idempotent_and_undo_removes_only_its_label(db):
	rows = [ROW, dict(ROW, other_para=6), dict(ROW, other_citation_key="2099_FC_9"), dict(ROW, citation_key="2021_FC_2", other_citation_key="2021_FC_2"), {"citation_key": "bad"}]
	first = loader.load(db, rows, False)
	assert (first["to_add"], first["skipped_no_note"], first["skipped_no_case"], first["skipped_bad_row"]) == (1, 1, 2, 1)
	assert db.scalar(select(ParagraphNoteLink.id)) is None
	loader.load(db, rows, True)
	again = loader.load(db, rows, True)
	assert again["to_add"] == 0 and again["skipped_present"] == 1 and again["after"] == 1
	db.add(ParagraphNoteLink(case_id=2, para=5, other_case_id=1, other_para=5, score=9, source="other"))
	db.commit()
	assert loader.undo(db, False)["to_remove"] == 1
	assert loader.undo(db, True)["after"] == 1
	assert db.scalar(select(ParagraphNoteLink.source)) == "other"
