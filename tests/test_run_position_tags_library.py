import datetime
import json

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.database import Base, Case
from scripts.run_position_tags_library import run, wanted

TEXT = (
	"Singh v. Canada (Citizenship and Immigration)\nDate: 20200101\n"
	"[1] The applicant is a citizen of India.\n[2] The applicant submits that the Officer erred.\n[3] I am not persuaded. The application is dismissed.\n"
)


@pytest.fixture
def db():
	engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
	Base.metadata.create_all(engine, tables=[Base.metadata.tables["cases"]])
	with Session(engine) as session:
		rows = [
			(1, "Singh v. Canada (Citizenship and Immigration)", "FC", datetime.date(2020, 1, 1), "en", TEXT),
			(2, "Singh v. Canada (Citizenship and Immigration)", "FC", datetime.date(2001, 1, 1), "en", TEXT),  # before 2005
			(3, "Acme v. Revenue", "FC", datetime.date(2020, 1, 1), "en", "Acme v. Revenue\n[1] Tax.\n[2] More tax."),  # not immigration
			(4, "Singh c. Canada (Citoyenneté et Immigration)", "FC", datetime.date(2020, 1, 1), "fr", TEXT),  # French
			(5, "Singh v. Canada (Citizenship and Immigration)", "SCC", datetime.date(2020, 1, 1), "en", TEXT),  # other court
			(6, "Singh v. Canada (Citizenship and Immigration)", "FC", datetime.date(2020, 1, 1), "en", "No numbers here at all."),
		]
		for i, title, court, day, language, text in rows:
			session.add(Case(id=i, title=title, court=court, date=day, language=language, full_text=text, citation=f"c{i}"))
		session.commit()
		yield session


def test_only_in_scope_decisions_are_written_and_the_database_is_untouched(db, tmp_path):
	stats = run(db, tmp_path)
	assert stats["candidates"] == 4 and stats["written"] == 1
	assert stats["not_immigration_or_french"] == 2 and stats["no_numbered_paragraphs"] == 1
	written = json.loads((tmp_path / "case_1.json").read_text())
	assert sorted(written["paragraphs"]) == ["1", "2", "3"]
	assert not db.dirty and not db.new and not db.deleted


def test_rerun_skips_existing_files(db, tmp_path):
	run(db, tmp_path)
	again = run(db, tmp_path)
	assert again["written"] == 0 and again["skipped_existing"] == 1


def test_wanted():
	assert wanted("Singh v. Canada (Citizenship and Immigration)", "FC", "en", TEXT)
	assert not wanted("Singh", "FC", "fr", TEXT) and not wanted("Singh", "FC", "en", None)
