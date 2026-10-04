"""Pure fixtures and query compilation only: no engine, DB or environment files."""

import ast
from contextlib import contextmanager
from datetime import UTC, date, datetime
from pathlib import Path
from types import SimpleNamespace

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import JSON, Column, Integer, MetaData, String, Table
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import registry

from backend import decision_timing as timing
from backend import decision_timing_routes as routes


@pytest.mark.parametrize("value, expected", [
    ("20260102", date(2026, 1, 2)), ("2026/01/02", date(2026, 1, 2)),
    ("2026-01-02", date(2026, 1, 2)), (" January  2, 2026 ", date(2026, 1, 2)),
    ("2 février 2026", date(2026, 2, 2)), (date(2026, 1, 2), date(2026, 1, 2)),
    ("2026-02-30", None), ("Jan 2, 26", None), ("02/01/2026", None),
    ("January 2 and 3, 2026", None), ("2026-01-02T00:00:00", None),
    (datetime(2026, 1, 2, tzinfo=UTC), None), ([], None), ({}, None), ("unknown", None),
])
def test_explicit_dates(value, expected):
    assert timing.explicit_date(value) == expected


def test_threshold_and_linear_quantiles():
    assert timing.timing_stats(range(9)) == {
        "n": 9, "suppressed": True, "median_days": None,
        "p25_days": None, "p75_days": None,
    }
    assert timing.timing_stats(range(10)) == {
        "n": 10, "suppressed": False, "median_days": 4.5,
        "p25_days": 2.25, "p75_days": 6.75,
    }
    assert timing.timing_stats([])["median_days"] is None


def samples(n, year=2026):
    return [(i, year, "2026-01-01", f"2026-01-{i + 1:02d}") for i in range(n)]


def test_dedup_exclusions_and_private_groups():
    rows = samples(10) + samples(10) + [
        (20, 1999, "2026-01-01", "2026-01-01"),
        (21, 2000, None, "2026-01-02"),
        (22, 2001, "nonsense", "2026-01-02"),
        (23, 2002, "2026-01-03", "2026-01-02"),
        (24, 2003, [], "2026-01-02"),
    ]
    result = timing.aggregate_timing(rows)
    assert result["overall"]["n"] == 11
    assert result["by_year"] == [{"year": 2026, **timing.timing_stats(range(10))}]
    assert result["hidden_groups"]["by_year"] == {"groups": 1, "samples": 1}
    assert result["excluded"] == {
        "missing_dates": 1, "invalid_dates": 2, "reversed_dates": 1,
        "duplicate_records": 10,
    }
    assert "1999" not in repr(result)
    assert timing.aggregate_timing(samples(9))["by_year"] == []
    assert timing.aggregate_timing([])["hidden_groups"]["by_year"]["samples"] == 0


def test_group_thresholds_deduplication_and_missing_metadata():
    rows = [(*row, [" Refugee  Protection ", "refugee protection", None],
             ["detention", " DETENTION ", {}]) for row in samples(10)]
    rows += [(20, None, "2026-01-01", "2026-01-02", ["hidden issue"], ["hidden tag"]),
             (21, None, "  ", "2026-01-02", ["hidden issue"], ["hidden tag"]),
             (22, None, "2026-01-01", "2026-01-02", "not a list", {"bad": "tag"}),
             (23, None, 20260101, "2026-01-02", ["refugee protection"], ["detention"])]
    result = timing.aggregate_timing(rows + rows[:10])
    assert result["by_issue"] == [{"issue": "refugee protection", **timing.timing_stats(range(10))}]
    assert result["by_tag"] == [{"tag": "detention", **timing.timing_stats(range(10))}]
    assert result["hidden_groups"]["by_issue"] == {"groups": 1, "samples": 1}
    assert result["hidden_groups"]["by_tag"] == {"groups": 1, "samples": 1}
    assert "hidden issue" not in repr(result) and "hidden tag" not in repr(result)
    assert result["overall"]["n"] == 12
    assert result["excluded"]["missing_dates"] == result["excluded"]["invalid_dates"] == 1
    assert result["excluded"]["duplicate_records"] == 10
    assert timing.aggregate_timing([(*r, ["tiny"], ["tiny"]) for r in samples(9)])["by_tag"] == []
    assert timing.aggregate_timing([])["by_issue"] == timing.aggregate_timing([])["by_tag"] == []


def models():
    metadata = MetaData()

    def table(name, ints=(), strings=(), jsons=()):
        return Table(name, metadata,
                     *(Column(k, Integer, primary_key=(i == 0))
                       for i, k in enumerate(ints)),
                     *(Column(k, String) for k in strings),
                     *(Column(k, JSON) for k in jsons))

    c = table("fc_activity_classifications", ("source_case_id",), jsons=("classification_json",))
    s = table("fc_activity_summaries", ("source_case_id", "year"), (
        "city_filed", "decision_body", "application_type", "representation",
        "proceeding_language", "office_location", "resolution", "applicant_counsel_key",
        "leave_judge_key", "merits_judge_key",
    ))
    case = table("cases", ("id",), ("date", "court"), ("metadata_json",))
    j = table("judge_profiles", ("id",), ("slug",))
    link = table("case_judge_profiles", ("case_id", "judge_profile_id"))

    mapper = registry()
    return SimpleNamespace(**{
        name: mapper.mapped(type(name, (), {"__table__": tab}))
        for name, tab in [("FCActivityClassification", c), ("FCActivitySummary", s),
                          ("Case", case), ("JudgeProfile", j), ("CaseJudgeProfile", link)]
    }), s, link


class FakeSession:
    def __init__(self, *results):
        self.results = iter(results)
        self.statements = []
        self.protected = False

    @property
    @contextmanager
    def no_autoflush(self):
        self.protected = True
        try:
            yield
        finally:
            self.protected = False

    def execute(self, statement):
        assert self.protected
        self.statements.append(statement)
        rows = next(self.results)
        return SimpleNamespace(all=lambda: rows, first=lambda: rows[0] if rows else None)


@pytest.fixture
def query_models(monkeypatch):
    m, _summary, _link = models()
    monkeypatch.setattr(timing, "_models", lambda: m)
    return m


def sql(statement):
    return str(statement.compile(dialect=postgresql.dialect(),
                                 compile_kwargs={"literal_binds": True}))


def test_stage_query_and_stored_taxonomy_only(query_models):
    rows = [(*row, "refugee_protection", [" Refugee_protection ", "refugee_protection"])
            for row in samples(10)]
    db = FakeSession(rows + rows)
    result = timing.fetch_fc_activity_timing(
        db, city=" Toronto ", year_from=2020, year_to=2026, decision_body="rpd",
        application_type="leave", representation="represented", language="en",
        office="Ottawa", resolution="judicial_review_granted",
        judge="judge-key", counsel="counsel-key",
    )
    text = sql(db.statements[0])
    assert result["overall"]["n"] == 10
    assert result["by_issue"][0]["issue"] == "refugee_protection"
    assert result["by_tag"][0]["n"] == 10
    assert "decision_subject" in text and "challenge_categories" in text
    assert "judicial_review_heard" in text and "judicial_review_decided" in text
    assert "judicial_review_decision'" not in text
    assert "JOIN fc_activity_summaries" in text
    for column in ("city_filed", "year", "decision_body", "application_type",
                   "representation", "proceeding_language", "office_location",
                   "resolution", "applicant_counsel_key", "leave_judge_key", "merits_judge_key"):
        assert f"fc_activity_summaries.{column}" in text
    assert " OR " in text and "'Toronto'" in text
    assert "full_text" not in text and "docket" not in text and "JOIN cases" not in text


def test_canonical_query_known_and_unknown_slug(query_models):
    rows = [(i, date(2026, 1, i + 1), "2026-01-01") for i in range(10)]
    db = FakeSession([(7, "exact-slug")], rows + rows, rows[:9])
    result = timing.fetch_judge_timing(db, "exact-slug")
    assert result["judge"]["n"] == 10
    assert result["judge"]["median_days"] == 4.5
    assert result["baseline"]["n"] == 9 and result["baseline"]["median_days"] is None
    assert result["minister_filter_applied"] is False
    assert "judge_profiles.slug = 'exact-slug'" in sql(db.statements[0])
    judge_sql, baseline_sql = map(sql, db.statements[1:])
    assert "case_judge_profiles.case_id = cases.id" in judge_sql
    assert "case_judge_profiles.judge_profile_id = 7" in judge_sql
    for text in (judge_sql, baseline_sql):
        assert "date of hearing" in text and "reader_extracted" in text
        assert "'federal court of canada'" in text and "'fc'" in text
        assert "lower(trim(cases.court))" in text
        assert "'FCA'" not in text and "full_text" not in text and "fc_activity" not in text
    assert "case_judge_profiles" not in baseline_sql
    empty = FakeSession([])
    assert timing.fetch_judge_timing(empty, "Exact-Slug") == {"status": "unknown_judge"}
    assert len(empty.statements) == 1
    zero = timing.fetch_judge_timing(FakeSession([(7, "exact-slug")], [], []), "exact-slug")
    assert zero["judge"]["n"] == zero["baseline"]["n"] == 0
    assert zero["judge"]["p75_days"] is None


def test_routes_params_contract_and_errors(monkeypatch):
    app = FastAPI()
    app.include_router(routes.router)
    sentinel = object()
    app.dependency_overrides[routes.get_timing_db] = lambda: sentinel
    calls = []

    def activity(db, **filters):
        assert db is sentinel
        calls.append(filters)
        return {**timing.aggregate_timing([]), "by_issue": {"status": "unavailable"},
                "by_tag": {"status": "unavailable"}}

    monkeypatch.setattr(routes, "fetch_fc_activity_timing", activity)
    monkeypatch.setattr(routes, "fetch_judge_timing",
                        lambda db, slug: {"status": "unknown_judge"} if slug == "unknown"
                        else {"status": "ok", "minister_filter_applied": False})
    with TestClient(app) as client:
        response = client.get("/api/fc-activity/timing", params={
            "city": "Toronto", "year_from": "2020", "year_to": "2026",
            "decision_body": "rpd", "application_type": "leave", "representation": "represented",
            "language": "en", "office": "Ottawa", "resolution": "open",
            "judge": "a", "counsel": "b",
        })
        assert response.status_code == 200
        assert response.json()["overall"]["median_days"] is None
        assert calls[0]["year_from"] == 2020 and calls[0]["counsel"] == "b"
        assert len(calls[0]) == 11
        assert client.get("/api/fc-activity/timing?year_from=bad").status_code == 422
        assert client.get("/api/fc-activity/timing?year_from=2026&year_to=2020").status_code == 422
        assert client.get("/api/judge-profiles/unknown/timing").json() == {
            "detail": {"code": "unknown_judge"}}
        assert client.get("/api/judge-profiles/unknown/timing").status_code == 404
        known = client.get("/api/judge-profiles/exact/timing?minister=A&minister=B")
        assert known.status_code == 200 and known.json()["minister_filter_applied"] is False


def test_application_registration_and_generated_api_contract():
    root = Path(__file__).resolve().parents[1]
    tree = ast.parse((root / "backend/main.py").read_text(encoding="utf-8"))
    assert any(isinstance(node, ast.ImportFrom) and node.module == "decision_timing_routes"
               and any(alias.name == "router" and alias.asname == "decision_timing_router"
                       for alias in node.names) for node in ast.walk(tree))
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
               and node.func.attr == "include_router"
               and any(isinstance(arg, ast.Name) and arg.id == "decision_timing_router"
                       for arg in node.args) for node in ast.walk(tree))
    reference = (root / "docs/API_REFERENCE.generated.md").read_text(encoding="utf-8")
    assert "### `GET /api/fc-activity/timing`" in reference
    assert "### `GET /api/judge-profiles/{slug}/timing`" in reference
