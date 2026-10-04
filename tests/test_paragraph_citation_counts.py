"""Synthetic stored-citation fixtures: no database, extraction or application startup."""

from datetime import date
from types import SimpleNamespace

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.dialects import postgresql

from backend.case_formatter import format_decision
from backend.database import get_db
from backend.paragraph_citation_counts import (
    aggregate_paragraph_citations, get_paragraph_citation_counts, router, usable_pinpoints,
)

TEXT = "Decision Content\n[1] First 😀.\n[3] Third.\n[4] Fourth.\n[7] Seventh."
BLOCKS = format_decision(TEXT)
TARGET_DATE = date(2020, 1, 1)
LATER = date(2021, 1, 1)


def test_distinct_later_decisions_and_occurrence_coverage_have_separate_denominators():
    rows = [
        (10, LATER, 1, None, None),
        (10, LATER, 1, None, None),  # duplicate does not inflate a paragraph
        (10, LATER, None, "Case at paras. 3–4 and 7", None),
        (11, LATER, None, "Case at paras. 1, 3 to 4", None),
        (11, LATER, None, "Case at pp. 1-7", None),
        (12, LATER, None, "Case without pinpoint", None),
        (13, LATER, 2, None, None),  # missing actual number, not index two
        (14, LATER, None, "Case at paras. 99-100", None),
        (42, LATER, 1, None, None),  # self
        (15, date(2019, 1, 1), 1, None, None),
        (16, TARGET_DATE, 1, None, None),  # same day is not proven later
        (17, None, 1, None, None),
        (None, LATER, 1, None, None),
    ]
    result = aggregate_paragraph_citations(42, TARGET_DATE, BLOCKS, rows)
    assert result.counts == {1: 2, 3: 2, 4: 2, 7: 1}
    assert result.total_citing_decisions == 5
    assert result.citing_decisions_with_usable_pinpoint == 2
    assert result.citing_decisions_without_usable_pinpoint == 3
    assert result.total_citations == 8
    assert result.citations_without_usable_pinpoint == 4
    assert result.chronology_known


@pytest.mark.parametrize("text,expected", [
    ("Case at paras. 1, 3-4 and 7", {1, 3, 4, 7}),
    ("Case at paragraphs 1; 3 to 7", {1, 3, 4, 7}),
    ("Case at paras. 1, 1, 3 or 7", {1, 3, 7}),
    ("Case at paras. 2-4, 99", {3, 4}),
    ("Case at paras. 1-999999999999", {1, 3, 4, 7}),
    ("Case at para. 7", {7}),
    ("Case at p. 3", set()),
    ("Case at pp. 1-7", set()),
    ("IRPA s. 34(1)(f)", set()),
    ("Case at para. 3(1)", set()),
    ("Case at para. 3.1", set()),
    ("Case at paras. 7-3", set()),
    ("Case at paras. 0-7", set()),
    ("Case at paras. 3-unknown", set()),
    ("Case at paras. 3 and unknown", set()),
    ("Case at para. 99", set()),
    ("Case, 2024 FC 3", set()),
])
def test_stored_paragraph_lists_ranges_and_unusable_forms(text, expected):
    assert usable_pinpoints(None, text, None, {1, 3, 4, 7}) == expected


def test_stored_scalar_precedence_and_normalized_fallback():
    actual = {1, 3, 4, 7}
    assert usable_pinpoints(3, "Case at paras. 3-4", None, actual) == {3, 4}
    assert usable_pinpoints(2, "Case at paras. 2-4", None, actual) == {3, 4}
    assert usable_pinpoints(2, "Case at paras. 2, 7", None, actual) == {7}
    assert usable_pinpoints(7, "Case at paras. 3-4", None, actual) == {7}
    assert usable_pinpoints(99, "Case at para. 3", None, actual) == set()
    assert usable_pinpoints(None, "Case", "Case at para. 4", actual) == {4}
    assert usable_pinpoints(None, "Case at paras. 4-3", "Case at para. 4", actual) == set()
    assert usable_pinpoints(None, "Case at para. " + "9" * 5000, None, actual) == set()
    assert usable_pinpoints(0, "Case at para. 3", None, actual) == set()
    assert usable_pinpoints(-1, None, None, actual) == set()


def test_empty_unnumbered_unknown_date_and_zero_counts():
    assert aggregate_paragraph_citations(42, TARGET_DATE, BLOCKS, ()).counts == {1: 0, 3: 0, 4: 0, 7: 0}
    result = aggregate_paragraph_citations(42, TARGET_DATE, format_decision("Unnumbered text"), [(10, LATER, 1, None, None)])
    assert result.counts == {} and result.total_citing_decisions == 1
    assert result.citations_without_usable_pinpoint == 1
    result = aggregate_paragraph_citations(42, None, BLOCKS, [(10, LATER, 1, None, None)])
    assert result.total_citations == 0 and not result.chronology_known


class FixtureSession:
    def __init__(self, target, rows=()):
        self.target, self.rows, self.queries = target, rows, []

    def execute(self, query):
        self.queries.append(str(query.compile(dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True})))
        if len(self.queries) == 1:
            return SimpleNamespace(first=lambda: self.target)
        return iter(self.rows)


def test_http_contract_and_query_are_read_only_resolved_strictly_later():
    db = FixtureSession(SimpleNamespace(date=TARGET_DATE, full_text=TEXT), [(10, LATER, 3, None, None)])
    app = FastAPI()  # no main app, startup, lifespan or database connection
    app.include_router(router)
    app.dependency_overrides[get_db] = lambda: db
    with TestClient(app) as client:
        response = client.get("/api/cases/42/paragraph-citation-counts")
    assert response.status_code == 200
    assert response.json() == {
        "case_id": 42, "counts": {"1": 0, "3": 1, "4": 0, "7": 0},
        "chronology_known": True, "total_citing_decisions": 1,
        "citing_decisions_with_usable_pinpoint": 1,
        "citing_decisions_without_usable_pinpoint": 0,
        "total_citations": 1, "citations_without_usable_pinpoint": 0,
    }
    assert len(db.queries) == 2
    sql = db.queries[1]
    assert "citations.target_case_id = 42" in sql
    assert "cases.date > '2020-01-01'" in sql and "citations.source_case_id != 42" in sql
    assert "JOIN cases ON cases.id = citations.source_case_id" in sql
    assert all(query.startswith("SELECT ") for query in db.queries)
    assert "statute" not in sql and "chunk" not in sql


def test_unknown_case_404_and_unknown_date_avoids_incoming_query():
    db = FixtureSession(None)
    with pytest.raises(Exception) as error:
        get_paragraph_citation_counts(42, db)
    assert error.value.status_code == 404
    db = FixtureSession(SimpleNamespace(date=None, full_text=TEXT))
    assert not get_paragraph_citation_counts(42, db).chronology_known
    assert len(db.queries) == 1


def test_registration_is_additive_and_legacy_reader_count_semantics_unchanged():
    from backend import routes
    from backend.reader_service import _cited_case_counts_by_paragraph
    assert any(route.path == "/api/cases/{case_id}/paragraph-citation-counts" for route in routes.router.routes)
    assert _cited_case_counts_by_paragraph([(10, 1), (10, 1), (11, 1), (42, 1), (11, 99)], 42) == {1: 2, 99: 1}
    assert format_decision(TEXT, {1: 9})[1]["cited_by_count"] == 9
