"""paragraph_positions: loader (dry run, additive, idempotent), database reader, 0.7 confidence rule, Live Analysis."""

import datetime
import json

import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend import position_tags
from backend.database import Base, Case, ParagraphPosition
from backend.live_reader import format_blocks_for_text
from scripts.load_position_tags import load, read_file


@pytest.fixture
def db():
	engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
	Base.metadata.create_all(engine, tables=[Base.metadata.tables[n] for n in ("cases", "paragraph_positions")])
	with Session(engine) as session:
		session.add(Case(id=7, title="Singh v. Canada", citation="2025 FC 1210", court="FC", full_text="x", date=datetime.date(2025, 7, 8)))
		session.commit()
		yield session


def _write(directory, case_id, paragraphs=None):
	directory.mkdir(parents=True, exist_ok=True)
	paragraphs = {"1": {"h": "applicant", "p": 0.91}, "2": {"h": "court", "p": 0.42}} if paragraphs is None else paragraphs
	(directory / f"case_{case_id}.json").write_text(json.dumps({"case_id": case_id, "source": {"tagger": "positions_learned_v1"}, "paragraphs": paragraphs}))


def test_loader_is_dry_by_default_additive_and_idempotent(db, tmp_path):
	_write(tmp_path, 7)
	_write(tmp_path, 999)  # not in the library
	_write(tmp_path, 8, {})  # no paragraphs
	dry = load(db, tmp_path)
	assert dry["to_add"] == 1 and dry["not_in_library"] == 1 and dry["unreadable"] == 1 and dry["paragraphs_to_add"] == 2
	assert db.scalar(select(ParagraphPosition.id)) is None
	done = load(db, tmp_path, apply=True)
	assert (done["before"], done["after"]) == (0, 1)
	again = load(db, tmp_path, apply=True)
	assert again["to_add"] == 0 and again["already_loaded"] == 1 and again["after"] == 1
	row = db.scalars(select(ParagraphPosition)).one()
	assert row.tagger == "positions_learned_v1" and row.paragraph_count == 2


def test_read_file_rejects_garbage(tmp_path):
	(tmp_path / "case_5.json").write_text("not json")
	assert read_file(tmp_path / "case_5.json") is None


def test_low_confidence_paragraphs_say_unsure():
	sure = position_tags._learned_row("applicant", 0.9)
	unsure = position_tags._learned_row("court", 0.69)
	assert sure["unsure"] is False and sure["positions"][0]["key"] == "applicant"
	assert unsure["unsure"] is True and unsure["positions"][0]["key"] == "unsure" and unsure["layer"]["key"] == "unknown"
	assert position_tags._learned_row("applicant", 0.7)["unsure"] is False


def test_reader_reads_the_table_only_when_flag_is_on(db, tmp_path, monkeypatch):
	stored = {"1": {"h": "respondent", "p": 0.8}, "2": {"h": "court", "p": 0.5}}
	_write(tmp_path / "files", 7, stored)
	load(db, tmp_path / "files", apply=True)
	monkeypatch.setattr(position_tags, "_database_rows", lambda cid: {n: position_tags._learned_row(r["h"], r["p"]) for n, r in db.scalar(select(ParagraphPosition.paragraphs).where(ParagraphPosition.case_id == cid)).items()})
	empty = tmp_path / "empty"
	empty.mkdir()
	source = position_tags.FilePositionSource(empty, None, empty)
	monkeypatch.delenv(position_tags.LEARNED_FLAG, raising=False)
	assert position_tags.case_positions(7, source)["available"] is False
	monkeypatch.setenv(position_tags.LEARNED_FLAG, "1")
	data = position_tags.case_positions(7, source)
	assert data["available"] and data["source"] == "learned"
	assert data["paragraphs"]["1"]["positions"][0]["key"] == "respondent"
	assert data["paragraphs"]["2"]["unsure"] is True


def test_database_failure_falls_back_to_files(tmp_path, monkeypatch):
	monkeypatch.setenv(position_tags.LEARNED_FLAG, "1")
	monkeypatch.setattr(position_tags, "_database_rows", lambda cid: None)
	_write(tmp_path / "learned", 777002)
	empty = tmp_path / "empty"
	empty.mkdir()
	data = position_tags.case_positions(777002, position_tags.FilePositionSource(empty, None, tmp_path / "learned"))
	assert data["available"] and data["paragraphs"]["1"]["positions"][0]["key"] == "applicant"


def test_live_analysis_uses_learned_tags_only_behind_the_flag(monkeypatch):
	text = "[1] The applicant submits that the officer erred in law.\n\n[2] I am not persuaded by that argument. The application is dismissed."
	blocks = format_blocks_for_text(text)
	monkeypatch.delenv(position_tags.LEARNED_FLAG, raising=False)
	assert position_tags.live_positions(text, blocks)["mode"] == "rules"
	monkeypatch.setenv(position_tags.LEARNED_FLAG, "1")
	live = position_tags.live_positions(text, blocks)
	assert live["mode"] == "learned" and live["available"]
	assert all("unsure" in r for r in live["paragraphs"].values())
