from datetime import date, datetime, timezone
from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend import statute_consideration as consideration
from backend.database import Case, CaseOutcome, Statute, StatuteReference


class _Query:
    def __init__(self, rows):
        self.rows = list(rows)

    def all(self):
        return self.rows

    def join(self, *_args):
        return self

    def filter(self, *_args):
        return self

    def order_by(self, *_args):
        return self


class _Session:
    def __init__(self, references=(), outcomes=(), statutes=None):
        self.references = list(references)
        self.outcomes = list(outcomes)
        self.statutes = list(statutes or [
            SimpleNamespace(
                instrument_key="canada.irpa",
                title="Immigration and Refugee Protection Act",
                short_title="IRPA",
            )
        ])

    def query(self, *models):
        if models == (Statute,):
            return _Query(self.statutes)
        if models == (StatuteReference, Case):
            return _Query(self.references)
        if models == (CaseOutcome,):
            return _Query(sorted(
                self.outcomes,
                key=lambda row: (row.updated_at or datetime.min.replace(tzinfo=timezone.utc), row.id),
                reverse=True,
            ))
        raise AssertionError(f"Unexpected query: {models}")


def _decision(case_id, decision_date, court="Federal Court"):
    return SimpleNamespace(
        id=case_id,
        title=f"Decision {case_id}",
        citation=f"202{decision_date.year % 10} FC {case_id}",
        court=court,
        date=decision_date,
    )


def _reference(case_id):
    return SimpleNamespace(source_case_id=case_id)


def _outcome(case_id, outcome, outcome_id=1, updated_at=None):
    return SimpleNamespace(
        case_id=case_id,
        decision_outcome=outcome,
        id=outcome_id,
        updated_at=updated_at,
    )


def _client(session):
    app = FastAPI()
    app.include_router(consideration.router)
    app.dependency_overrides[consideration.get_db] = lambda: session
    return TestClient(app)


def test_aggregation_counts_distinct_decisions_and_reference_occurrences_separately():
    cases = {
        1: _decision(1, date(2022, 1, 1), "Federal Court"),
        2: _decision(2, date(2024, 1, 1), "Federal Court of Appeal"),
        3: _decision(3, date(2024, 2, 1), "Federal Court"),
    }
    rows = [
        (_reference(1), cases[1]),
        (_reference(1), cases[1]),
        (_reference(2), cases[2]),
        (_reference(3), cases[3]),
    ]
    result = consideration.aggregate_consideration(
        rows,
        [
            _outcome(1, "dismissed", outcome_id=2),
            _outcome(1, "allowed", outcome_id=1),
            _outcome(2, ""),
            _outcome(3, "allowed"),
        ],
    )

    assert result["summary"]["decision_count"] == 3
    assert result["summary"]["denominator"] == 3
    assert result["summary"]["reference_occurrences"] == 4
    assert {
        row["value"]: row["decision_count"] for row in result["by_court"]
    } == {"Federal Court": 2, "Federal Court of Appeal": 1}
    assert {
        row["value"]: row["decision_count"] for row in result["by_year"]
    } == {"2022": 1, "2024": 2}
    assert {row["denominator"] for row in result["by_year"]} == {3}
    outcomes = {row["value"]: row for row in result["by_outcome"]}
    assert set(outcomes) == {"allowed", "dismissed", "unclassified"}
    assert all(row["denominator"] == 3 for row in outcomes.values())
    assert outcomes["unclassified"]["decision_count"] == 1
    assert next(row for row in result["decisions"] if row["case_id"] == 1)["outcome"] == "dismissed"


def test_decision_ranking_uses_within_decision_references_then_recency():
    older = _decision(1, date(2020, 1, 1))
    recent_a = _decision(2, date(2024, 1, 1))
    recent_b = _decision(3, date(2025, 1, 1))
    rows = [
        (_reference(1), older),
        (_reference(2), recent_a),
        (_reference(2), recent_a),
        (_reference(3), recent_b),
        (_reference(3), recent_b),
    ]

    result = consideration.aggregate_consideration(rows, [])

    assert [row["case_id"] for row in result["decisions"]] == [3, 2, 1]
    assert [row["reference_count"] for row in result["decisions"]] == [2, 2, 1]


def test_api_caps_page_size_at_50_and_paginates_decision_rows(monkeypatch):
    monkeypatch.setattr(
        consideration,
        "find_statute_version_at_date",
        lambda *_args: None,
    )
    cases = [_decision(i, date(2020 + i, 1, 1)) for i in range(1, 61)]
    refs = [(SimpleNamespace(), case) for case in cases]
    response = _client(_Session(references=refs)).get(
        "/api/statutes/IRPA/34/consideration?page=2&page_size=500"
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["pagination"]["page_size"] == 50
    assert payload["pagination"]["total_decisions"] == 60
    assert payload["pagination"]["total_pages"] == 2
    assert len(payload["decisions"]) == 10


def test_unknown_act_and_section_return_actionable_404_hints():
    client = _client(_Session())
    unknown_act = client.get("/api/statutes/Nope/34/consideration")
    unknown_section = client.get("/api/statutes/IRPA/999/consideration")

    assert unknown_act.status_code == 404
    assert "Hint:" in unknown_act.json()["detail"]
    assert unknown_section.status_code == 404
    assert "Hint:" in unknown_section.json()["detail"]


def test_page_and_statute_viewer_link_to_consideration_form():
    client = _client(_Session())
    page = client.get("/statute-consideration")

    assert page.status_code == 200
    assert 'id="act"' in page.text
    assert 'id="section"' in page.text
    assert 'case-reader-ui/${encodeURIComponent(d.case_id)}' in page.text
    from backend.pages.statute_viewer import statute_viewer_page_html

    assert 'href="/statute-consideration"' in statute_viewer_page_html()
