import datetime
import gzip
import json

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.database import Base, Case, CaseFrame, IssueMap, ParagraphNote, get_db
from backend.main import app
from scripts import load_core150_layers as loader

TEXT = (
	"[1] Mr Rahman Jones applied for judicial review of the 2019 decision of the Refugee Appeal Division.\n"
	"[2] The officer did not give reasons for the refusal. [3] The application is allowed."
)
FRAME = {"id": "2020_FC_1172", "parties": {"applicant": "Rahman Jones", "respondent": "Minister"},
	"levels": [{"body": "Refugee Appeal Division", "date": "2019-12-05", "outcome": "dismissed", "para": 1}, {"body": "Federal Court", "date": "2020-12-21", "outcome": "allowed", "para": 3}],
	"subject": "Judicial review of a refugee appeal decision.", "issues": [{"text": "Were the reasons adequate?", "para": 2}],
	"arguments": [{"side": "applicant", "text": "No reasons were given.", "para": 2, "main": True}], "challenged": [], "arg_paras": {}}
ISSUE = {"source_key": "2020_FC_1172", "issue_no": 1, "citation_key": "2020_FC_1172", "court": "FC", "issue": "Were the reasons adequate?",
	"applicant_position": "No.", "respondent_position": "Yes.", "result": "allowed_for_applicant", "result_para": 3,
	"result_quote": "The application is allowed.", "paras": "2-3", "review_flags": ["order_para_only", "minister_applicant"], "order_para": 3}
NOTES = [
	{"citation_key": "2020_FC_1172", "para": 1, "note": "The applicant seeks review of the RAD decision.", "para_start": "Mr Rahman Jones applied for judicial review of the 2019 decis"},
	{"citation_key": "2020_FC_1172", "para": 2, "note": "The officer gave no reasons.", "para_start": "The officer did not give reasons for the refusal."},
]


@pytest.fixture
def db():
	engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
	names = ("cases", "case_frames", "case_outcomes", "issue_maps", "issue_map_questions", "paragraph_notes")
	Base.metadata.create_all(engine, tables=[Base.metadata.tables[n] for n in names])
	with Session(engine) as session:
		session.add(Case(id=7, title="Jones v. Canada", citation="2020 FC 1172", court="FC", full_text=TEXT, date=datetime.date(2020, 12, 21)))
		session.commit()
		yield session


def _run(db, apply, notes=NOTES):
	ids = loader.resolve(db, ["2020_FC_1172", "2021_FC_9"])
	return (
		loader.load_frames(db, [{"citation_key": "2020_FC_1172", "frame": FRAME}, {"citation_key": "2021_FC_9", "frame": FRAME}], ids, apply),
		loader.load_issue_maps(db, [ISSUE], ids, apply),
		loader.load_notes(db, notes, ids, apply, 0.9),
	)


def test_dry_run_writes_nothing_then_apply_is_idempotent(db):
	frames, issues, notes = _run(db, False)
	assert (frames["to_add"], frames["skipped_no_case"], issues["to_add"], notes["to_add"]) == (1, 1, 1, 2)
	assert db.scalar(select(ParagraphNote.id)) is None and db.scalar(select(IssueMap.id)) is None and db.scalar(select(CaseFrame.id)) is None
	_run(db, True)
	frames, issues, notes = _run(db, True)
	assert (frames["to_add"], issues["to_add"], notes["to_add"]) == (0, 0, 0)
	assert frames["after"] == 1 and issues["after"] == 1 and notes["after"] == 2


def test_misaligned_notes_are_skipped(db):
	bad = [dict(n, para_start="Completely different words that are not in the stored decision text") for n in NOTES]
	assert _run(db, False, bad)[2]["cases_skipped_misaligned"] == 1


def test_case_with_an_older_issue_map_is_left_alone(db):
	db.add(IssueMap(source_key="7", issue_no=1, case_id=7, issue="x", text="x", result="dismissed_for_applicant"))
	db.commit()
	assert _run(db, False)[1]["skipped_case_has_map"] == 1


def test_undo_removes_only_what_the_loader_added(db):
	db.add(IssueMap(source_key="7", issue_no=1, case_id=7, issue="x", text="x", result="dismissed_for_applicant"))
	db.commit()
	_run(db, True)
	assert loader.undo(db, {"2020_FC_1172"}, False) == {"case_frames": 1, "paragraph_notes": 2, "issue_maps": 0}
	db.add(IssueMap(source_key="2020_FC_1172", issue_no=1, case_id=7, issue="y", text="y", result="allowed_for_applicant"))
	db.commit()
	assert loader.undo(db, {"2020_FC_1172"}, True)["issue_maps"] == 1
	assert len(db.scalars(select(IssueMap)).all()) == 1 and db.scalar(select(ParagraphNote.id)) is None


def test_routes_return_stored_layers(db):
	_run(db, True)
	app.dependency_overrides[get_db] = lambda: db
	try:
		client = TestClient(app)
		issues = client.get("/cases/7/issue-map").json()
		assert issues["available"] and issues["issues"][0]["result_para"] == 3
		assert issues["issues"][0]["result_label"].startswith("The applicant won")
		assert [c["code"] for c in issues["issues"][0]["checks"]] == ["order_para_only", "minister_applicant"] and issues["issues"][0]["respondent_position"] == "Yes."
		notes = client.get("/cases/7/paragraph-notes").json()
		assert notes["available"] and notes["paragraphs"]["2"] == "The officer gave no reasons."
		assert client.get("/cases/8/issue-map").json() == {"available": False}
		assert client.get("/cases/8/paragraph-notes").json() == {"available": False}
	finally:
		app.dependency_overrides.clear()


def test_shipped_data_files_are_consistent():
	frames, issues, notes = (loader.read_jsonl(loader.DATA / f"{n}.jsonl.gz") for n in ("frames", "issue_maps", "paragraph_notes"))
	keys = {r["citation_key"] for r in frames}
	assert len(keys) == 150 and all(loader.KEY.match(k) for k in keys)
	assert {r["citation_key"] for r in issues} <= keys and {r["citation_key"] for r in notes} <= keys
	assert all(r["note"].strip() and not r["note"].upper().startswith("NONE") for r in notes)
	assert len({(r["source_key"], r["issue_no"]) for r in issues}) == len(issues)
