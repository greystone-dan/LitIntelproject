import csv
from datetime import date

import pytest
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine, select
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.database import Base, Case, Citation


@compiles(Vector, "sqlite")
def _sqlite_vector_type(_type, _compiler, **_kw):
	return "JSON"


@pytest.fixture
def session():
	engine = create_engine("sqlite://", poolclass=StaticPool, connect_args={"check_same_thread": False})
	Base.metadata.create_all(engine)
	with Session(engine) as db:
		for case_id, title in [(1, "Source v. Case"), (2, "Canada v. Oxford Properties Group Inc."), (3, "Pro-Sys Consultants Ltd. v. Microsoft Corporation"),
			(4, "Ontario (Public Safety and Security) v. Criminal Lawyers' Association")]:
			db.add(Case(id=case_id, title=title, court="FC", date=date(2020, 1, 1), full_text="x"))
		db.flush()
		rows = [
			("group", "Canada v. Oxford Properties Group Inc., 2018 FCA 30", 2),
			("Pro-Sys at para 103", "Pro-Sys Consultants Ltd. v. Microsoft Corporation, 2013 SCC 57", 3),
			("(Criminal Lawyers Association at paras 5-6)", "Ontario (Public Safety and Security) v. Criminal Lawyers' Association, 2010 SCC 23", 4),
		]
		for text, normalized, target in rows:
			db.add(Citation(source_case_id=1, target_case_id=target, citation_kind="case_short", citation_text=text, normalized_citation=normalized, unresolved=False))
		db.add(Citation(source_case_id=1, target_case_id=None, citation_kind="case_short", citation_text="Bank", normalized_citation="X v. Y", unresolved=True))
		db.commit()
		yield db


def run(session, monkeypatch, *args):
	import scripts.flag_weak_short_form_links as script

	monkeypatch.setattr(script, "SessionLocal", lambda: session)
	monkeypatch.setattr(session, "close", lambda: None)
	script.main(list(args))


def targets(session):
	session.expire_all()
	return {c.citation_text: c.target_case_id for c in session.scalars(select(Citation))}


def test_dry_run_flags_only_the_weak_link_and_writes_nothing(session, monkeypatch, tmp_path, capsys):
	backup = tmp_path / "weak.csv"
	run(session, monkeypatch, "--backup", str(backup))
	assert "suspects_to_act_on=1" in capsys.readouterr().out
	assert [row["citation_text"] for row in csv.DictReader(backup.open(encoding="utf-8"))] == ["group"]
	assert targets(session)["group"] == 2


def test_apply_unlinks_and_revert_restores(session, monkeypatch, tmp_path):
	backup = tmp_path / "weak.csv"
	run(session, monkeypatch, "--backup", str(backup), "--apply")
	assert targets(session)["group"] is None and targets(session)["Pro-Sys at para 103"] == 3
	run(session, monkeypatch, "--revert-from", str(backup), "--apply")
	assert targets(session)["group"] == 2


def test_apply_requires_a_backup(session, monkeypatch):
	with pytest.raises(SystemExit):
		run(session, monkeypatch, "--apply")
	assert targets(session)["group"] == 2


def test_judge_handles_non_breaking_hyphen_in_party_name() -> None:
	from scripts.flag_weak_short_form_links import judge

	assert judge("Pro-Sys at para 103", "Pro-Sys Consultants Ltd. v. Microsoft Corporation, 2013 SCC 57, at para. 103", "Pro‑Sys Consultants Ltd. v. Microsoft Corporation") is None
