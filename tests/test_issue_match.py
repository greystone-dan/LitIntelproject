import datetime
import json
import gzip

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend import issue_match, routes
from backend.database import Base, Case, IssueMap, IssueMapQuestion, get_db
from backend.main import app
from backend.pages.live_analysis import live_analysis_page_html
from scripts.load_issue_maps import DEFAULT_FILE, load, read_rows


@pytest.fixture
def db():
	engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
	Base.metadata.create_all(engine, tables=[Base.metadata.tables[n] for n in ("cases", "issue_maps", "issue_map_questions")])
	with Session(engine) as session:
		session.add(Case(id=7, title="Singh v. Canada", citation="2025 FC 1210", court="FC", full_text="x", date=datetime.date(2025, 7, 8)))
		session.commit()
		issue_match.reset_index()
		yield session
	issue_match.reset_index()


def _rows():
	return [
		{"source_key": "a", "issue_no": 1, "live_case_id": 7, "citation": "2025 FC 1210", "court": "FC", "issue": "Was the work permit refusal unreasonable because the officer ignored dual intent?",
		 "text": "Was the work permit refusal unreasonable because the officer ignored dual intent? Officer overlooked the LMIA permanent resident stream.", "result": "allowed_for_applicant", "result_para": 9,
		 "soften": None, "result_paragraph": "The Officer failed to recognize the LMIA's express reference.", "questions": ["Can an officer refuse a work permit when the LMIA shows the worker intends to apply for permanent residence?"]},
		{"source_key": "b", "issue_no": 1, "live_case_id": None, "citation": "2010 FC 1", "court": "FC", "issue": "Did the Board breach fairness by refusing an adjournment?",
		 "text": "Did the Board breach fairness by refusing an adjournment? Counsel was unavailable.", "result": "dismissed_for_applicant", "result_para": 0,
		 "soften": None, "result_paragraph": None, "questions": ["Is refusing an adjournment a breach of procedural fairness?"]},
	]


def test_loader_is_dry_by_default_and_idempotent(db):
	rows = _rows()
	stats = load(db, rows)
	assert stats["to_add"] == 2 and stats["to_add_linked"] == 1
	assert db.scalar(select(IssueMap.id)) is None
	applied = load(db, rows, apply=True)
	assert applied["after_issues"] == 2 and applied["after_questions"] == 2
	again = load(db, rows, apply=True)
	assert again["to_add"] == 0 and again["after_issues"] == 2
	linked = {m.source_key: m.case_id for m in db.scalars(select(IssueMap))}
	assert linked == {"a": 7, "b": None}


def test_matches_use_questions_and_return_cards(db):
	load(db, _rows(), apply=True)
	result = issue_match.find_issue_matches(db, "The LMIA showed the worker wants permanent residence, so refusing the work permit was unreasonable.")
	first = result["matches"][0]
	assert first["citation"] == "2025 FC 1210" and first["case_url"] == "/data-explorer?case_id=7"
	assert first["result_label"].startswith("The applicant won") and first["result_paragraph_number"] == 9
	assert "Keyword match to check" in result["basis"] and result["library_issues"] == 2
	adjourn = issue_match.find_issue_matches(db, "Refusing an adjournment breached procedural fairness for the applicant.")
	assert adjourn["matches"][0]["citation"] == "2010 FC 1"
	assert adjourn["matches"][0]["note"] == "No paragraph states a result for this issue."
	assert issue_match.find_issue_matches(db, "zzzz qqqq")["matches"] == []


def test_index_rebuilds_when_rows_change(db):
	rows = _rows()
	load(db, rows[:1], apply=True)
	assert issue_match.find_issue_matches(db, "refusing an adjournment breached fairness")["matches"] == []
	load(db, rows, apply=True)
	assert issue_match.find_issue_matches(db, "refusing an adjournment breached fairness")["matches"][0]["citation"] == "2010 FC 1"


def test_route_is_404_when_off_and_stateless_when_on(db, monkeypatch):
	load(db, _rows(), apply=True)
	monkeypatch.setitem(app.dependency_overrides, get_db, lambda: db)
	client = TestClient(app)
	body = {"text": "Refusing an adjournment breached procedural fairness for the applicant."}
	monkeypatch.delenv(issue_match.ENABLED_ENV, raising=False)
	assert client.post("/live-analysis/issue-matches", json=body).status_code == 404
	monkeypatch.setenv(issue_match.ENABLED_ENV, "1")
	response = client.post("/live-analysis/issue-matches", json=body)
	assert response.status_code == 200
	assert "no-store" in response.headers["cache-control"]
	assert response.json()["matches"][0]["citation"] == "2010 FC 1"
	assert client.post("/live-analysis/issue-matches", json={"text": "short"}).status_code == 422
	assert client.post("/live-analysis/issue-matches", json={"text": "x" * 4001}).status_code == 422


def test_page_block_only_when_enabled(monkeypatch):
	monkeypatch.delenv(issue_match.ENABLED_ENV, raising=False)
	off = live_analysis_page_html()
	assert "laMatchesBox" not in off and "/live-analysis/issue-matches" not in off
	monkeypatch.setenv(issue_match.ENABLED_ENV, "1")
	on = live_analysis_page_html()
	assert "laMatchesBox" in on and "/live-analysis/issue-matches" in on and "not stored" in on


def test_shipped_issue_map_file_is_well_formed():
	rows = read_rows(DEFAULT_FILE)
	assert len(rows) > 2000
	allowed = set(issue_match.RESULT_LABELS)
	assert all(r["result"] in allowed and r["issue"] and r["text"] for r in rows)
	assert len({(r["source_key"], r["issue_no"]) for r in rows}) == len(rows)
