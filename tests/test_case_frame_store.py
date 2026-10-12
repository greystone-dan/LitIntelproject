import datetime
import json

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend import case_frame_store
from backend.database import Base, Case, CaseFrame, CaseOutcome, get_db
from backend.main import app
from scripts.load_case_frames import load, read_frames

TEXT = "[1] Mr Rahman Jones applied for judicial review of the 2019 decision of the Refugee Appeal Division. [2] Reasons follow."
FRAME = {"id": "FC_7", "parties": {"applicant": "Rahman Jones", "applicant_role": "applicant", "respondent": "Minister", "respondent_role": "respondent"},
	"levels": [{"body": "Refugee Appeal Division", "date": "2019-12-05", "outcome": "dismissed", "para": 1},
		{"body": "Federal Court", "date": "2020-12-21", "outcome": "application dismissed", "para": 0}],
	"subject": "Judicial review of a refugee appeal decision.", "issues": [{"text": "Was the IFA finding reasonable?", "para": 2}],
	"arguments": [{"side": "applicant", "text": "The IFA was unreasonable.", "para": 2, "main": True}], "challenged": [], "arg_paras": {}}


@pytest.fixture
def db():
	engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
	Base.metadata.create_all(engine, tables=[Base.metadata.tables[n] for n in ("cases", "case_frames", "case_outcomes")])
	with Session(engine) as session:
		session.add(Case(id=7, title="Jones v. Canada", citation="2020 FC 1172", court="FC", full_text=TEXT, date=datetime.date(2020, 12, 21)))
		session.commit()
		yield session


def _folder(tmp_path, files):
	for name, frame in files.items():
		(tmp_path / f"{name}.json").write_text(json.dumps(frame), encoding="utf-8")
	return tmp_path


def test_loader_dry_run_then_apply_is_idempotent(db, tmp_path):
	rows = read_frames(_folder(tmp_path, {"FC_7": FRAME}))
	assert load(db, rows, "t")["to_add"] == 1
	assert db.scalar(select(CaseFrame.id)) is None
	assert load(db, rows, "t", apply=True)["after"] == 1
	again = load(db, rows, "t", apply=True)
	assert again["to_add"] == 0 and again["skipped_present"] == 1 and again["after"] == 1


def test_loader_skips_bad_files_missing_cases_and_frames_for_another_decision(db, tmp_path):
	other = dict(FRAME, id="FC_8", parties={"applicant": "Zxqwvbn Pplmkj", "respondent": "Minister"}, levels=[{"body": "RAD", "date": "1999-01-01", "para": 40}])
	folder = _folder(tmp_path, {"FC_7": other | {"id": "FC_7"}, "FC_8": FRAME, "FC_99": dict(FRAME, id="FC_99")})
	stats = load(db, read_frames(folder), "t")
	assert stats["skipped_guard"] == 1 and stats["skipped_bad_file"] == 1 and stats["skipped_no_case"] == 1 and stats["to_add"] == 0


def test_route_is_off_unless_flagged_and_returns_clean_frame(db, monkeypatch):
	db.add(CaseFrame(case_id=7, version=1, frame=dict(FRAME, issues="oops", extra="x"), source="t"))
	db.commit()
	app.dependency_overrides[get_db] = lambda: db
	try:
		client = TestClient(app)
		monkeypatch.delenv(case_frame_store.ENABLED_ENV, raising=False)
		assert client.get("/cases/7/case-frame").json() == {"available": False}
		monkeypatch.setenv(case_frame_store.ENABLED_ENV, "1")
		data = client.get("/cases/7/case-frame").json()
		assert data["available"] and data["frame"]["issues"] == [] and "extra" not in data["frame"]
		assert data["frame"]["arguments"][0]["text"].startswith("The IFA")
		assert client.get("/cases/8/case-frame").json()["available"] is False
	finally:
		app.dependency_overrides.clear()


def test_card_data_leaves_out_this_decision_and_gives_a_result_line(db, monkeypatch):
	db.add(CaseFrame(case_id=7, version=1, frame=FRAME, source="t"))
	db.add(CaseOutcome(case_id=7, classifier_version="deterministic_outcome_v2", decision_outcome="dismissed", outcome_status="lost",
		confidence=0.78, disposition_evidence="the application is dismissed"))
	db.commit()
	monkeypatch.setenv(case_frame_store.ENABLED_ENV, "1")
	data = case_frame_store.case_frame(7, db)
	assert [l["body"] for l in data["frame"]["levels"]] == ["Refugee Appeal Division"]  # the decision itself is not an "earlier decision"
	assert data["result"]["text"] == "Dismissed" and "clear ruling" in data["result"]["reliability"] and "rules" in data["result"]["source"]


def test_result_line_is_cautious_or_absent():
	class Row:
		decision_outcome, confidence, disposition_evidence = "mixed", 0.7, None

	assert "check the decision" in case_frame_store.result_line(Row)["reliability"]
	Row.decision_outcome = "procedural"
	assert case_frame_store.result_line(Row) is None and case_frame_store.result_line(None) is None


def test_card_script_has_no_internal_role_labels_and_shows_the_result():
	from pathlib import Path

	js = (Path(__file__).resolve().parents[1] / "backend" / "pages" / "reader_frame.js").read_text(encoding="utf-8")
	assert "_role" not in js and "frame-result" in js
