from datetime import date
from types import SimpleNamespace

from fastapi.testclient import TestClient

from backend.database import get_db
from backend.main import app
from backend.overruling_risk import (
    OVERRULING_RISK_SEEDS,
    build_overruling_risk_result,
)


def _case(case_id, title, citation, decision_date):
    return SimpleNamespace(
        id=case_id,
        title=title,
        citation=citation,
        date=date.fromisoformat(decision_date),
    )


def _vavilov(case_id=65):
    seed = OVERRULING_RISK_SEEDS[0]
    return _case(case_id, seed["case_name"], seed["citation"], seed["date"])


def test_direct_flag_includes_source_rationale_date_notice_and_assignment():
    subject = _vavilov()

    result = build_overruling_risk_result(subject, [])

    assert result["counts"] == {"direct": 1, "indirect": 0, "total": 1}
    flag = result["flags"][0]
    assert flag["assignment"] == "direct"
    assert flag["event_date"] == "2019-12-19"
    assert flag["decision_date"] == "2019-12-19"
    assert flag["source"] == OVERRULING_RISK_SEEDS[0]["source"]
    assert flag["rationale"] == OVERRULING_RISK_SEEDS[0]["rationale"]
    assert flag["notice"] == "seed list, needs lawyer review."
    assert "how_assigned" in flag
    assert "other cases may be affected" in flag["assessment"]
    assert "this case may be affected" not in flag["assessment"]


def test_indirect_flag_identifies_stored_resolved_relationship_and_is_cautious():
    subject = _case(12, "Example v Example", "2020 FC 12", "2020-01-02")
    authority = _vavilov()
    citation = SimpleNamespace(
        id=987,
        source_case_id=12,
        target_case_id=authority.id,
        citation_text="Vavilov, 2019 SCC 65",
        normalized_citation="2019 SCC 65",
    )

    result = build_overruling_risk_result(subject, [(citation, authority)])

    assert result["counts"] == {"direct": 0, "indirect": 1, "total": 1}
    flag = result["flags"][0]
    assert flag["assignment"] == "indirect"
    assert flag["citation_relationship"]["citation_id"] == 987
    assert flag["citation_relationship"]["source_case_id"] == 12
    assert flag["citation_relationship"]["target_case_id"] == authority.id
    assert "indicator, not a legal conclusion" in flag["how_assigned"]
    assert flag["decision_date"] == "2020-01-02"
    assert flag["event_date"] == "2019-12-19"
    assert flag["authority_decision_date"] == "2019-12-19"


def test_counts_and_dates_make_pre_vavilov_decision_identifiable():
    subject = _case(5, "Earlier case", "1990 FC 1", "2018-04-03")
    authority = _vavilov()
    citation = SimpleNamespace(
        id=1,
        source_case_id=subject.id,
        target_case_id=authority.id,
        citation_text="2019 SCC 65",
        normalized_citation="2019 SCC 65",
    )

    result = build_overruling_risk_result(subject, [(citation, authority)])

    assert result["counts"] == {"direct": 0, "indirect": 1, "total": 1}
    assert result["case"]["decision_date"] == "2018-04-03"
    assert result["flags"][0]["event_date"] > result["case"]["decision_date"]


def test_no_flag_result_has_zero_counts_and_no_speculative_events():
    subject = _case(6, "Unlisted case", "2024 SCC 1", "2024-01-01")

    result = build_overruling_risk_result(subject, [])

    assert result["counts"] == {"direct": 0, "indirect": 0, "total": 0}
    assert result["flags"] == []
    assert len(OVERRULING_RISK_SEEDS) == 1
    assert "No seeded indicator matched" in result["assessment"]


class _FixtureSession:
    def __init__(self, requested_case, citation_rows=()):
        self.requested_case = requested_case
        self.citation_rows = list(citation_rows)

    def scalar(self, statement):
        return self.requested_case

    def execute(self, statement):
        return self.citation_rows


def test_api_route_returns_read_only_fixture_result_and_404_for_missing_case():
    requested = _case(65, "Canada (Minister of Citizenship and Immigration) v. Vavilov", "2019 SCC 65", "2019-12-19")
    session = _FixtureSession(requested)

    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    try:
        client = TestClient(app)
        response = client.get("/api/overruling-risk/65")
        assert response.status_code == 200
        assert response.json()["counts"] == {"direct": 1, "indirect": 0, "total": 1}
        assert "may be affected" in response.json()["assessment"]

        def missing_db():
            yield _FixtureSession(None)

        app.dependency_overrides[get_db] = missing_db
        missing = client.get("/api/overruling-risk/999")
        assert missing.status_code == 404
        assert missing.json()["detail"] == "Case not found"
        client.close()
    finally:
        app.dependency_overrides.pop(get_db, None)


def test_route_query_uses_only_stored_resolved_citation_fixture():
    requested = _case(12, "Example v Example", "2020 FC 12", "2020-01-02")
    authority = _vavilov()
    citation = SimpleNamespace(
        id=4,
        source_case_id=12,
        target_case_id=authority.id,
        citation_text="2019 SCC 65",
        normalized_citation="2019 SCC 65",
    )
    session = _FixtureSession(requested, [(citation, authority)])

    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    try:
        client = TestClient(app)
        response = client.get("/api/overruling-risk/12")
        client.close()
        assert response.status_code == 200
        payload = response.json()
        assert payload["counts"] == {"direct": 0, "indirect": 1, "total": 1}
        assert payload["flags"][0]["citation_relationship"]["relationship"].startswith(
            "stored resolved Citation"
        )
    finally:
        app.dependency_overrides.pop(get_db, None)
