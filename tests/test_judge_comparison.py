"""SQLite fixtures mirror the exact stored issue/outcome sources used by comparison."""

import json

import pytest
from sqlalchemy import create_engine, event, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import Session

from backend import analytics_service, judge_issue_record
from backend.analytics_service import (
	fetch_judge_comparison,
	fetch_judge_profile_by_slug,
	fetch_judge_profile_issues,
)
from backend.database import JudgeProfile


@pytest.fixture
def db():
	engine = create_engine(
		"sqlite://",
		connect_args={"check_same_thread": False},
		poolclass=StaticPool,
	)
	with engine.begin() as connection:
		for ddl in (
			"CREATE TABLE judge_profiles (id INTEGER PRIMARY KEY, slug TEXT, display_name TEXT, "
			"normalized_name TEXT, primary_court TEXT, aliases JSON, created_at DATETIME, updated_at DATETIME)",
			"CREATE TABLE cases (id INTEGER PRIMARY KEY, date DATE, issues JSON, metadata_json JSON, "
			"citation TEXT, title TEXT, court TEXT)",
			"CREATE TABLE case_judge_profiles (id INTEGER PRIMARY KEY, case_id INTEGER, judge_profile_id INTEGER, "
			"raw_name TEXT, created_at DATETIME)",
			"CREATE TABLE case_tags (id INTEGER PRIMARY KEY, case_id INTEGER, category TEXT, value TEXT)",
			"CREATE TABLE citations (id INTEGER PRIMARY KEY, source_case_id INTEGER, target_case_id INTEGER, "
			"normalized_citation TEXT, citation_text TEXT)",
		):
			connection.execute(text(ddl))
		connection.execute(text(
			"INSERT INTO judge_profiles (id, slug, display_name, normalized_name, primary_court) VALUES "
			"(1, 'judge-a', 'Judge A', 'judge a', 'FC'), "
			"(2, 'judge-b', 'Judge B', 'judge b', 'FC'), "
			"(3, 'empty', 'Empty Judge', 'empty judge', 'FC')"
		))
		for case_id in range(1, 15):
			side_index = (case_id - 1) % 7
			issues = ["  Procedural   FAIRNESS ", "procedural fairness"]
			if side_index < 4:
				issues += ["four only"] * 8
			if side_index < 5 or (case_id <= 7 and side_index == 5):
				issues += ["five boundary"]
			outcome = ("won", "lost", "mixed", None, "won", "lost", "unknown")[side_index]
			connection.execute(text(
				"INSERT INTO cases VALUES (:id, :date, :issues, :metadata, :citation, :title, 'FC')"
			), {
				"id": case_id, "date": "2020-01-01" if side_index < 4 else "2021-02-02",
				"issues": json.dumps(issues),
				"metadata": json.dumps({"reader_extracted": {
					"government outcome": outcome, "judge": "Wrong metadata judge",
					"challenged issues": ["metadata only"],
				}}),
				"citation": f"2020 FC {case_id}", "title": f"Decision {case_id}",
			})
			connection.execute(text(
				"INSERT INTO case_judge_profiles (case_id, judge_profile_id) VALUES (:id, :judge)"
			), {"id": case_id, "judge": 1 if case_id <= 7 else 2})
		# Duplicate links/occurrences must never inflate decision counts.
		connection.execute(text("INSERT INTO case_judge_profiles (case_id, judge_profile_id) VALUES (1, 1)"))
		connection.execute(text(
			"INSERT INTO cases VALUES (100, '2019-01-01', '[]', '{}', '2019 SCC 65', 'Vavilov', 'SCC')"
		))
		connection.execute(text(
			"INSERT INTO case_tags (case_id, category, value) VALUES "
			"(1, 'issue', 'fairness'), (1, 'issue', 'fairness'), (2, 'issue', 'fairness'), "
			"(1, 'type', 'JR'), (8, 'issue', 'fairness'), (100, 'issue', 'excluded')"
		))
		connection.execute(text(
			"INSERT INTO citations (source_case_id, target_case_id, normalized_citation, citation_text) VALUES "
			"(1, 100, 'short alias', 'Vavilov at para 1'), (1, 100, 'other alias', 'para 2'), "
			"(2, 100, NULL, 'Vavilov'), (8, 100, '2019 SCC 65', 'Vavilov'), "
			"(1, NULL, '2000 FC 9', 'first mention'), (1, NULL, '2000 FC 9', 'repeat'), "
			"(2, NULL, NULL, ' 2000 FC 9 '), (3, NULL, NULL, NULL), "
			"(100, NULL, 'outside cohort', 'outside cohort')"
		))
	with Session(engine) as session:
		yield session
	engine.dispose()


def test_comparison_counts_distinct_decisions_and_explicit_denominators(db):
	result = fetch_judge_comparison(db, "judge-a", "judge-b")
	assert list(result)[:3] == ["status", "shared_issues", "outcomes"]
	assert result["status"] == "ok"
	assert result["metadata"]["issue_source"] == "cases.issues"
	assert result["metadata"]["outcome_source"] == "cases.metadata_json.reader_extracted.government outcome"
	a = result["judges"]["a"]
	assert a["profile"]["slug"] == "judge-a"
	assert a["decisions"] == {"count": 7, "denominator": 7}
	assert a["outcomes"] == {
		"government_won": {"count": 2, "denominator": 7},
		"government_lost": {"count": 2, "denominator": 7},
		"unclassified": {"count": 3, "denominator": 7},
		"classified": {"count": 4, "denominator": 7},
		"government_win_rate": {"percent": 50.0, "denominator": 4},
	}
	assert a["yearly_decisions"] == [
		{"year": "2020", "decisions": {"count": 4, "denominator": 7}},
		{"year": "2021", "decisions": {"count": 3, "denominator": 7}},
	]
	assert a["undated_decisions"] == {"count": 0, "denominator": 7}
	assert a["top_tags"] == [
		{"category": "issue", "value": "fairness", "decisions": {"count": 2, "denominator": 7}},
		{"category": "type", "value": "JR", "decisions": {"count": 1, "denominator": 7}},
	]
	authorities = {row["citation"]: row for row in a["top_authorities"]}
	assert set(authorities) == {"2019 SCC 65", "2000 FC 9"}
	assert authorities["2019 SCC 65"] == {
		"target_case_id": 100, "citation": "2019 SCC 65", "title": "Vavilov",
		"decisions": {"count": 2, "denominator": 7},
	}
	assert authorities["2000 FC 9"]["target_case_id"] is None
	assert authorities["2000 FC 9"]["decisions"] == {"count": 2, "denominator": 7}


def test_shared_issues_require_five_each_and_issue_outcome_denominators(db):
	result = fetch_judge_comparison(db, "judge-a", "judge-b")
	shared = {row["issue"]: row for row in result["shared_issues"]}
	assert set(shared) == {"five boundary", "procedural fairness"}
	assert shared["five boundary"]["a"]["decisions"] == {"count": 6, "denominator": 7}
	assert shared["five boundary"]["b"]["decisions"] == {"count": 5, "denominator": 7}
	assert shared["five boundary"]["b"]["outcomes"]["unclassified"] == {"count": 2, "denominator": 5}
	assert shared["five boundary"]["b"]["outcomes"]["government_win_rate"] == {
		"percent": 66.7, "denominator": 3,
	}
	assert shared["procedural fairness"]["a"]["decisions"] == {"count": 7, "denominator": 7}
	db.execute(text("UPDATE cases SET issues = '[]' WHERE id = 12"))
	result = fetch_judge_comparison(db, "judge-a", "judge-b")
	assert [row["issue"] for row in result["shared_issues"]] == ["procedural fairness"]


@pytest.mark.parametrize("issues", [None, '"not a list"', '{"issue": "procedural fairness"}', '[null, 1, "", " "]'])
def test_missing_or_malformed_issues_never_infer_metadata_fallback(db, issues):
	db.execute(text("UPDATE cases SET issues = :issues WHERE id <= 7"), {"issues": issues})
	result = fetch_judge_comparison(db, "judge-a", "judge-b")
	assert result["shared_issues"] == []
	assert result["judges"]["a"]["issues"] == []
	assert result["judges"]["a"]["decisions_with_issues"] == {"count": 0, "denominator": 7}


def test_unknown_slugs_are_explicit_and_not_partial_or_fuzzy(db):
	assert fetch_judge_comparison(db, "missing", "judge-a") == {
		"status": "unknown_judge", "unknown_slugs": ["missing"],
	}
	assert fetch_judge_comparison(db, "Judge A", "absent") == {
		"status": "unknown_judge", "unknown_slugs": ["Judge A", "absent"],
	}
	assert fetch_judge_comparison(db, "missing", "missing")["unknown_slugs"] == ["missing"]


def test_empty_same_judge_swapped_and_unclassified_comparisons(db):
	empty = fetch_judge_comparison(db, "empty", "empty")
	assert empty["shared_issues"] == []
	assert empty["judges"]["a"]["decisions"] == {"count": 0, "denominator": 0}
	assert empty["outcomes"]["a"]["government_win_rate"] == {"percent": None, "denominator": 0}
	assert empty["judges"]["a"]["top_tags"] == empty["judges"]["a"]["top_authorities"] == []
	same = fetch_judge_comparison(db, "judge-a", "judge-a")
	assert same["judges"]["a"] == same["judges"]["b"]
	swapped = fetch_judge_comparison(db, " judge-b ", "judge-a")
	assert swapped["judges"]["a"]["profile"]["slug"] == "judge-b"
	db.execute(text("UPDATE cases SET metadata_json = '{}' WHERE id <= 7"))
	unclassified = fetch_judge_comparison(db, "judge-a", "judge-b")
	assert unclassified["outcomes"]["a"]["unclassified"] == {"count": 7, "denominator": 7}
	assert unclassified["outcomes"]["a"]["government_win_rate"] == {"percent": None, "denominator": 0}


def test_comparison_executes_only_selects_and_preserves_existing_empty_profile(db):
	statements = []

	def capture(connection, cursor, statement, parameters, context, executemany):
		statements.append(statement)

	event.listen(db.bind, "before_cursor_execute", capture)
	try:
		fetch_judge_comparison(db, "judge-a", "judge-b")
	finally:
		event.remove(db.bind, "before_cursor_execute", capture)
	assert statements and all(statement.lstrip().upper().startswith("SELECT") for statement in statements)
	assert not db.new and not db.dirty and not db.deleted
	legacy = fetch_judge_profile_by_slug(db, "empty")
	assert legacy["profile"]["slug"] == "empty"
	assert legacy["outcomes"]["all_linked"] == 0
	assert legacy["outcomes"]["government_win_rate"] is None
	assert legacy["yearly_decisions"] == legacy["decisions"] == []


def test_pending_changes_are_not_autoflushed(db):
	pending = JudgeProfile(slug="pending", display_name="Pending Judge", normalized_name="pending judge")
	db.add(pending)
	assert fetch_judge_comparison(db, "pending", "judge-a") == {
		"status": "unknown_judge", "unknown_slugs": ["pending"],
	}
	assert pending in db.new
	assert pending.id is None


def test_judge_issue_aggregation_remains_reexported_from_analytics_service():
	assert analytics_service.fetch_judge_profile_issues is judge_issue_record.fetch_judge_profile_issues
	assert analytics_service._stored_issue_labels is judge_issue_record._stored_issue_labels
	assert analytics_service._issue_outcome_category is judge_issue_record._issue_outcome_category
	assert analytics_service._issue_outcome_summary is judge_issue_record._issue_outcome_summary
	assert analytics_service._JUDGE_ISSUE_MINIMUM_DECISIONS == judge_issue_record._JUDGE_ISSUE_MINIMUM_DECISIONS
	assert analytics_service.fetch_judge_profile_issues.__module__ == "backend.judge_issue_record"


def test_judge_issue_outcomes_threshold_mapping_and_federal_court_baseline(db):
	db.execute(text("UPDATE cases SET issues = '[]'"))
	outcomes = {
		1: "won", 2: "lost", 3: "mixed", 4: None, 5: "undetermined",
		6: "unexpected", 7: "won",
	}
	for case_id, outcome in outcomes.items():
		db.execute(text(
			"UPDATE cases SET issues = :issues, metadata_json = :metadata WHERE id = :id"
		), {
			"id": case_id,
			"issues": json.dumps(["  Procedural   FAIRNESS ", "procedural fairness"]),
			"metadata": json.dumps({"reader_extracted": {
				"government outcome": outcome,
				"decision outcome": "allowed",
			}}),
		})
	for case_id, outcome in ((15, "lost"), (16, "mixed"), (17, None)):
		db.execute(text(
			"INSERT INTO cases VALUES (:id, '2022-01-01', :issues, :metadata, :citation, :title, 'FC')"
		), {
			"id": case_id,
			"issues": json.dumps(["procedural fairness"]),
			"metadata": json.dumps({"reader_extracted": {"government outcome": outcome}}),
			"citation": f"2022 FC {case_id}",
			"title": f"Linked decision {case_id}",
		})
		db.execute(text(
			"INSERT INTO case_judge_profiles (case_id, judge_profile_id, raw_name) "
			"VALUES (:id, 1, 'Judge A')"
		), {"id": case_id})

	# Nine distinct decisions remain hidden, including duplicate issue occurrences.
	for case_id in range(40, 49):
		db.execute(text(
			"INSERT INTO cases VALUES (:id, '2022-01-01', :issues, '{}', :citation, :title, 'FC')"
		), {
			"id": case_id,
			"issues": json.dumps(["hidden issue", "hidden issue"]),
			"citation": f"2022 FC {case_id}",
			"title": f"Hidden decision {case_id}",
		})
		db.execute(text(
			"INSERT INTO case_judge_profiles (case_id, judge_profile_id, raw_name) "
			"VALUES (:id, 1, 'Judge A')"
		), {"id": case_id})

	for case_id in range(20, 30):
		db.execute(text(
			"INSERT INTO cases VALUES (:id, '2022-01-01', :issues, :metadata, :citation, :title, 'Federal Court')"
		), {
			"id": case_id,
			"issues": json.dumps(["PROCEDURAL FAIRNESS"]),
			"metadata": json.dumps({"reader_extracted": {
				"government outcome": ("won", "lost", "mixed", None, "undetermined")[case_id % 5],
			}}),
			"citation": f"2022 FC {case_id}",
			"title": f"Baseline decision {case_id}",
		})
	db.execute(text(
		"INSERT INTO cases VALUES (101, '2022-01-01', :issues, :metadata, '2022 FCA 1', 'Appeal', "
		"'Federal Court of Appeal')"
	), {
		"issues": json.dumps(["procedural fairness"]),
		"metadata": json.dumps({"reader_extracted": {"government outcome": "won"}}),
	})

	result = fetch_judge_profile_issues(db, " judge-a ")
	assert result["status"] == "ok"
	assert result["profile"]["slug"] == "judge-a"
	assert result["hidden_issue_count"] == 1
	assert [row["issue"] for row in result["issues"]] == ["procedural fairness"]
	row = result["issues"][0]
	assert row["judge"]["decisions"] == {"count": 10, "denominator": 19}
	assert row["judge"]["outcomes"] == {
		"minister_win": {"count": 2, "denominator": 10, "percent": 20.0},
		"applicant_win": {"count": 2, "denominator": 10, "percent": 20.0},
		"other": {"count": 2, "denominator": 10, "percent": 20.0},
		"unclassified": {"count": 4, "denominator": 10, "percent": 40.0},
	}
	baseline = row["federal_court_baseline"]
	assert baseline["decisions"] == {"count": 20, "denominator": 36}
	assert baseline["outcomes"] == {
		"minister_win": {"count": 4, "denominator": 20, "percent": 20.0},
		"applicant_win": {"count": 4, "denominator": 20, "percent": 20.0},
		"other": {"count": 4, "denominator": 20, "percent": 20.0},
		"unclassified": {"count": 8, "denominator": 20, "percent": 40.0},
	}
	assert result["metadata"]["outcome_source"] == (
		"cases.metadata_json.reader_extracted.government outcome"
	)
	assert "ranking" in result["metadata"]["interpretation"]


def test_judge_issue_route_unknown_canonical_judge_contract(db):
	from fastapi import FastAPI
	from fastapi.testclient import TestClient
	from backend import routes

	app = FastAPI()
	app.include_router(routes.router)
	app.dependency_overrides[routes.get_db] = lambda: db
	with TestClient(app) as client:
		unknown = client.get("/api/judge-profiles/not-a-canonical-judge/issues")
		assert unknown.status_code == 404
		assert unknown.json()["detail"]["code"] == "unknown_judge"
		assert client.get("/api/judge-profiles/judge-a/issues").status_code == 200


def test_undated_and_malformed_outcome_metadata_remain_in_denominator(db):
	db.execute(text("UPDATE cases SET date = NULL, metadata_json = '[]' WHERE id = 1"))
	db.execute(text("UPDATE cases SET metadata_json = '{\"reader_extracted\": []}' WHERE id = 2"))
	result = fetch_judge_comparison(db, "judge-a", "judge-b")
	a = result["judges"]["a"]
	assert a["decisions"] == {"count": 7, "denominator": 7}
	assert a["undated_decisions"] == {"count": 1, "denominator": 7}
	assert a["yearly_decisions"][0]["decisions"] == {"count": 3, "denominator": 7}
	assert a["outcomes"]["unclassified"] == {"count": 5, "denominator": 7}


def test_all_numeric_statistics_carry_denominators(db):
	result = fetch_judge_comparison(db, "judge-a", "judge-b")

	def check(value):
		if isinstance(value, dict):
			for key, child in value.items():
				if key in {"count", "percent"}:
					assert "denominator" in value
				elif isinstance(child, (int, float)):
					# IDs are identity, not statistics.
					assert key in {"denominator", "target_case_id"}
				else:
					check(child)
		elif isinstance(value, list):
			for child in value:
				check(child)

	for section in ("shared_issues", "outcomes", "judges"):
		check(result[section])


def test_comparison_http_contract_and_route_precedence(db, monkeypatch):
	from fastapi import FastAPI
	from fastapi.testclient import TestClient
	from backend import routes

	expected = fetch_judge_comparison(db, "judge-a", "judge-b")
	calls = []

	def compare(database, a, b):
		calls.append((a, b))
		if a == "missing":
			return {"status": "unknown_judge", "unknown_slugs": [a]}
		return expected

	monkeypatch.setattr(routes, "fetch_judge_comparison", compare)
	app = FastAPI()
	app.include_router(routes.router)
	app.dependency_overrides[routes.get_db] = lambda: object()
	with TestClient(app) as client:
		response = client.get("/judges/compare?a=judge-a&b=judge-b")
		assert response.status_code == 200
		assert response.json() == expected
		assert calls == [("judge-a", "judge-b")]
		unknown = client.get("/judges/compare?a=missing&b=judge-b")
		assert unknown.status_code == 404
		assert unknown.json()["detail"]["code"] == "unknown_judge"
		assert unknown.json()["detail"]["unknown_slugs"] == ["missing"]
		assert client.get("/judges/compare?a=judge-a").status_code == 422
		assert client.get("/judges/compare?a=&b=judge-b").status_code == 422
		assert client.get("/judges/judge-a", follow_redirects=False).status_code == 307


def test_comparison_ui_is_sibling_and_renderer_preserves_denominators(db):
	import re
	import shutil
	import subprocess
	from html.parser import HTMLParser
	from backend.pages.data_explorer import data_explorer_page_html

	html = data_explorer_page_html()

	class Ancestors(HTMLParser):
		def __init__(self):
			super().__init__()
			self.stack = []
			self.form_ancestors = None

		def handle_starttag(self, tag, attrs):
			attrs = dict(attrs)
			if attrs.get("id") == "judgeComparisonForm":
				self.form_ancestors = list(self.stack)
			if tag not in {"input", "br", "hr", "meta", "link", "img"}:
				self.stack.append((tag, attrs.get("id")))

		def handle_endtag(self, tag):
			for i in range(len(self.stack) - 1, -1, -1):
				if self.stack[i][0] == tag:
					del self.stack[i:]
					break

	parser = Ancestors()
	parser.feed(html)
	assert ("section", "judgeProfilePanel") in parser.form_ancestors
	assert not any(identity == "judgeProfileContent" for _, identity in parser.form_ancestors)
	assert 'id="judgeCompareA"' in html and 'id="judgeCompareB"' in html
	assert "Unknown canonical judge:" in html
	assert "#judgeComparisonResult .judge-comparison-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}" in html
	assert "#judgeComparisonResult .judge-comparison-grid>*{min-width:0}" in html
	assert "@media(max-width:760px){#judgeComparisonResult .judge-comparison-grid{grid-template-columns:minmax(0,1fr)}}" in html
	node = shutil.which("node")
	if not node:
		pytest.skip("Node unavailable for rendered comparison checks")
	functions = re.search(r"(function judgeComparisonCount[\s\S]+?)let judgeComparisonRequest;", html).group(1)
	data = fetch_judge_comparison(db, "judge-a", "judge-b")
	data["shared_issues"][0]["issue"] = "<img src=x onerror=alert(1)>"
	result = subprocess.run([node, "-e", """
const num=value=>String(value);
const esc=value=>String(value).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
""" + functions + "\nconsole.log(renderJudgeComparison(" + json.dumps(data) + "));"],
		text=True, capture_output=True, check=True).stdout
	assert "7 / 7 linked decisions" in result
	assert "4 / 7 linked decisions" in result  # year denominator
	assert "2 / 7 linked decisions" in result  # deduplicated tags/authorities
	assert "3 / 7 decisions in this set" in result  # unclassified
	assert result.index("Shared recorded issues") < result.index("Overall outcomes") < result.index("— coverage")
	assert "&lt;img" in result and "<img" not in result
	assert 'class="ci-table"' not in result

	class Grids(HTMLParser):
		def __init__(self):
			super().__init__()
			self.stack = []
			self.children = {}

		def handle_starttag(self, tag, attrs):
			classes = dict(attrs).get("class", "").split()
			grid = next((name for name in classes if name in {
				"judge-comparison-outcomes", "judge-comparison-coverage",
			}), None)
			if self.stack and self.stack[-1]:
				self.children[self.stack[-1]].append(tag)
			if grid:
				assert "judge-comparison-grid" in classes
				self.children[grid] = []
			if tag not in {"br", "input", "hr", "img"}:
				self.stack.append(grid)

		def handle_endtag(self, tag):
			self.stack.pop()

	grids = Grids()
	grids.feed(result)
	assert grids.children == {
		"judge-comparison-outcomes": ["p", "p"],
		"judge-comparison-coverage": ["section", "section"],
	}
