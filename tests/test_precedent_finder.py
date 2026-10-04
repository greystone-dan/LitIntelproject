"""Offline contracts for ephemeral proposition research (SQLite fixtures only)."""

from datetime import date
from types import SimpleNamespace

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend import precedent_finder as service
from backend.database import Case, CaseTag, Citation, get_db
from backend.legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION


@pytest.fixture
def db():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False},
                           poolclass=StaticPool)
    for model in (Case, CaseTag, Citation):
        model.__table__.create(engine)
    with Session(engine) as session:
        yield session
    engine.dispose()


def case(db, number, *, day=date(2020, 1, 1), outcome=None, **kwargs):
    metadata = {"reader_extracted": {"government outcome": outcome}} if outcome else {}
    db.add(Case(id=number, title=f"Decision {number}", court="FC", date=day,
                citation=f"2020 FC {number}", metadata_json=metadata, **kwargs))
    db.flush()


def tag(db, owner, value="fairness", *, taxonomy=ACTIVE_TAG_TAXONOMY_VERSION, offset=0):
    db.add(CaseTag(case_id=owner, category="issue", value=value, score=1,
                   evidence=value, offset_start=offset, offset_end=offset + len(value),
                   source="core_whitelist", taxonomy_version=taxonomy))
    db.flush()


def cite(db, source, target, kind="neutral"):
    db.add(Citation(source_case_id=source, target_case_id=target,
                    citation_kind=kind, normalized_citation="2020 FC 100"))
    db.flush()


@pytest.fixture
def fixed_tagger(monkeypatch):
    class Tagger:
        def tag(self, text):
            return [SimpleNamespace(category="issue", value=value)
                    for value in ("fairness", "reasons") if value in text]
    monkeypatch.setattr(service, "CoreLegalTaggerV3", Tagger)


def test_lexicographic_counts_duplicates_and_outcome_denominator(db, fixed_tagger):
    for number, outcome in ((1, "won"), (2, "lost"), (3, None), (4, "mixed")):
        case(db, number, outcome=outcome)
        tag(db, number)
    tag(db, 2, offset=20)  # A second occurrence is not a second decision/tag.
    tag(db, 3, "reasons")
    tag(db, 4, "reasons")
    for number, day in ((100, date(2000, 1, 1)), (101, date(2025, 1, 1)),
                        (102, date(2024, 1, 2)), (103, date(2024, 1, 1)),
                        (104, date(2024, 1, 1))):
        case(db, number, day=day, full_text="Authority source excerpt.")
    for owner in (1, 2, 3):
        cite(db, owner, 100)
    cite(db, 1, 100)  # Occurrence duplication must not inflate denominator.
    cite(db, 1, 101)
    cite(db, 2, 101)
    for target in (104, 103, 102):
        cite(db, 3, target)
        cite(db, 4, target)
    payload = service.find_precedents("fairness reasons fairness", db)
    rows = payload["authorities"]
    assert [row["case_id"] for row in rows] == [100, 102, 103, 104, 101]
    assert rows[0]["rank_numbers"] == [3, 2, 20000101]
    assert rows[0]["matched_tags"] == ["issue:fairness", "issue:reasons"]
    assert rows[0]["matching_citing_decisions"] == 3
    assert rows[0]["outcome_mix"] == {
        "government_won": 1, "government_lost": 1, "mixed": 0, "unclassified": 1,
        "denominator": 3,
        "basis": "Stored reader_extracted government outcomes of matching "
                 "citing decisions; not outcomes of the authority.",
    }
    assert rows[1]["outcome_mix"]["mixed"] == 1
    assert rows[0]["excerpt"] == "Authority source excerpt."
    assert rows[0]["court"] == "FC"
    assert rows[0]["date"] == "2000-01-01"
    assert not payload["coverage"]["partial"]
    assert "proposition" not in payload
    assert not db.new and not db.dirty and not db.deleted


def test_citation_tie_and_missing_excerpt(db, fixed_tagger):
    case(db, 1)
    tag(db, 1)
    for number, citation in ((100, "2020 FC Z"), (101, "2020 FC A")):
        case(db, number)
        db.get(Case, number).citation = citation
        cite(db, 1, number)
    db.flush()
    rows = service.find_precedents("fairness", db)["authorities"]
    assert [row["case_id"] for row in rows] == [101, 100]
    assert rows[0]["excerpt"] is None
    assert rows[0]["outcome_mix"]["unclassified"] == 1


@pytest.mark.parametrize("source", ["synthetic", "staged", "discovered", "activity",
                                   "reference_library", "side_project"])
def test_noncanonical_sources_and_targets_excluded(db, fixed_tagger, source):
    case(db, 1)
    case(db, 2, source_type=source)
    case(db, 100)
    case(db, 101, source_type=source)
    tag(db, 1)
    tag(db, 2)
    cite(db, 1, 100)
    cite(db, 2, 100)
    cite(db, 1, 101)
    rows = service.find_precedents("fairness", db)["authorities"]
    assert [row["case_id"] for row in rows] == [100]
    assert rows[0]["matching_citing_decisions"] == 1


def test_old_tags_statutes_unresolved_self_and_noncanonical_datasets(db, fixed_tagger):
    for number in (1, 2, 100, 101, 102, 103):
        case(db, number)
    case(db, 3, dataset_version="synthetic-fixture")
    case(db, 104, dataset_version="reference-library-v1")
    tag(db, 1)
    tag(db, 2, taxonomy="old")
    tag(db, 3)
    cite(db, 1, 100)
    cite(db, 2, 101)
    cite(db, 3, 102)
    cite(db, 1, 103, kind="statute")
    cite(db, 1, 104)
    cite(db, 1, None)
    cite(db, 1, 1)
    assert [row["case_id"] for row in service.find_precedents("fairness", db)["authorities"]] == [100]


def test_posting_budget_charges_duplicates_and_every_query_bounded(db, fixed_tagger, monkeypatch):
    monkeypatch.setattr(service, "POSTINGS_PER_TAG", 2)
    for number in (1, 2, 100):
        case(db, number)
    tag(db, 1)
    tag(db, 1, offset=20)
    tag(db, 2)
    cite(db, 1, 100)
    cite(db, 2, 100)
    statements = []
    event.listen(db.bind, "before_cursor_execute",
                 lambda conn, cursor, statement, params, context, many: statements.append(statement))
    payload = service.find_precedents("fairness", db)
    assert payload["coverage"]["partial"]
    assert payload["authorities"][0]["matching_citing_decisions"] == 1
    assert all("LIMIT" in sql for sql in statements if sql.lstrip().startswith("SELECT"))
    assert not any("SELECT cases.full_text" in sql for sql in statements)
    assert "ORDER BY case_tags.case_id, case_tags.id" in statements[0]
    assert not any(sql.lstrip().startswith(("INSERT", "UPDATE", "DELETE")) for sql in statements)


@pytest.mark.parametrize("budget", ["CITING_DECISIONS", "CITATIONS_PER_DECISION", "AUTHORITIES"])
def test_each_discovery_budget_reports_partial(db, fixed_tagger, monkeypatch, budget):
    monkeypatch.setattr(service, budget, 1)
    for number in (1, 2, 100, 101):
        case(db, number)
    for owner in (1, 2):
        tag(db, owner)
        cite(db, owner, 100)
        cite(db, owner, 101)
    assert service.find_precedents("fairness", db)["coverage"]["partial"]


def test_empty_tagless_and_real_extractors():
    class NoDatabase:
        def execute(self, *_):
            raise AssertionError("Tagless inputs must not query the database")
    assert "Enter" in service.find_precedents("", NoDatabase())["message"]
    payload = service.find_precedents("hello", NoDatabase())
    assert payload["authorities"] == []
    assert "No V3 legal tags" in payload["message"]
    # Use the real V3 engine, but empty postings for the real recognized phrase.
    class EmptyDatabase:
        def execute(self, *_):
            return []
    payload = service.find_precedents("IRPA s. 34(1)(f)", EmptyDatabase())
    assert payload["statutes"]
    assert "34(1)(f)" in " ".join(payload["statutes"])
    payload = service.find_precedents("procedural fairness", EmptyDatabase())
    assert payload["tags"]
    assert "No resolved canonical authorities" in payload["message"]


@pytest.fixture
def client(monkeypatch):
    from backend import routes
    app = FastAPI()
    app.include_router(routes.router)
    app.dependency_overrides[get_db] = lambda: object()
    monkeypatch.setattr(routes, "find_precedents", lambda proposition, db: {
        "tags": [], "statutes": [], "authorities": [], "message": "No matches",
        "coverage": {"partial": False, "note": "Bounded"},
    })
    return TestClient(app)


@pytest.mark.parametrize("body", [
    {}, {"proposition": 12}, {"proposition": None}, {"proposition": ["private-secret"]},
    {"proposition": {"private-secret": "value"}}, ["private-secret"],
    {"other": "private-secret"}, {"proposition": "ok", "other": "private-secret"},
])
def test_validation_never_echoes_input(client, body, caplog):
    response = client.post("/precedent-finder", json=body)
    assert response.status_code == 422
    assert "private-secret" not in response.text
    assert "private-secret" not in caplog.text
    assert response.headers["cache-control"] == "no-store"


def test_malformed_json_and_body_byte_limit(client, caplog):
    for body, status in ((b'{"proposition":"private-secret"', 422),
                         (b"\xffprivate-secret", 422),
                         (b"private-secret" * 4000, 413)):
        response = client.post("/precedent-finder", content=body,
                               headers={"Content-Type": "application/json"})
        assert response.status_code == status
        assert "private-secret" not in response.text
        assert response.headers["cache-control"] == "no-store"
    assert "private-secret" not in caplog.text


def test_character_limit_and_json_unicode(client, monkeypatch, caplog):
    from backend import routes
    calls = []
    def analyze(proposition, db):
        calls.append(len(proposition))
        return {"authorities": []}
    monkeypatch.setattr(routes, "find_precedents", analyze)
    for text in ("x" * 3000, "😀" * 3000):
        assert client.post("/precedent-finder", json={"proposition": text}).status_code == 200
    rejected = "private-secret" + "x" * 3000
    response = client.post("/precedent-finder", json={"proposition": rejected})
    assert response.status_code == 413
    assert "private-secret" not in response.text + caplog.text
    assert calls == [3000, 3000]
    with pytest.raises(ValueError, match="at most 3000"):
        service.find_precedents(rejected, object())


def test_success_failure_and_media_type_privacy(client, monkeypatch, caplog):
    from backend import routes
    response = client.post("/precedent-finder", json={"proposition": "private-secret"})
    assert response.status_code == 200
    assert "private-secret" not in response.text + caplog.text
    assert response.headers["pragma"] == "no-cache"
    def fail(proposition, db):
        raise ValueError(proposition)
    monkeypatch.setattr(routes, "find_precedents", fail)
    response = client.post("/precedent-finder", json={"proposition": "private-secret"})
    assert response.status_code == 500
    assert "private-secret" not in response.text + caplog.text
    response = client.post("/precedent-finder", content="private-secret")
    assert response.status_code == 422
    assert "private-secret" not in response.text + caplog.text


def test_page_contract_preserves_existing_research_links(client):
    response = client.get("/precedent-finder")
    assert response.status_code == 200
    assert response.headers["cache-control"] == "no-store"
    html = response.text
    for expected in ('maxlength="3000"', 'method:\'POST\'', "JSON.stringify({proposition:input.value})",
                     "textContent=value", 'href="/data-explorer"', "rank", "unclassified",
                     "denominator", "recency", "pagehide", "No embeddings"):
        assert expected in html
    assert "localStorage" not in html and "sessionStorage" not in html
    assert "innerHTML" not in html and "console." not in html
    assert "alert(" not in html


def test_real_endpoint_fixture_and_audit_never_record_proposition(db, fixed_tagger, caplog):
    from backend import routes
    from backend.audit import RequestAuditMiddleware
    case(db, 1)
    case(db, 100)
    tag(db, 1)
    cite(db, 1, 100)
    app = FastAPI()
    app.include_router(routes.router)
    app.dependency_overrides[get_db] = lambda: db
    records = []
    audit = RequestAuditMiddleware.__new__(RequestAuditMiddleware)
    audit.app = app
    audit.address_key = b"fixture-only"
    audit.raw_address = False
    audit.handler = SimpleNamespace(handle=lambda record: records.append(record.getMessage()))
    client = TestClient(audit)
    proposition = "private-secret fairness"
    response = client.post("/precedent-finder", json={"proposition": proposition})
    assert response.status_code == 200
    row = response.json()["authorities"][0]
    assert row["case_id"] == 100
    assert row["rank_numbers"] == [1, 1, 20200101]
    assert row["outcome_mix"]["denominator"] == 1
    response = client.post("/precedent-finder", json={"proposition": [proposition]})
    assert response.status_code == 422
    assert len(records) == 2
    assert all('"path": "/precedent-finder"' in record for record in records)
    assert "private-secret" not in response.text + caplog.text + "".join(records)
    assert not db.new and not db.dirty and not db.deleted


def test_deep_invalid_json_and_openapi_contract(client):
    response = client.post("/precedent-finder", content="[" * 2000 + "private-secret",
                           headers={"Content-Type": "application/json"})
    assert response.status_code == 422
    assert "private-secret" not in response.text
    operation = client.app.openapi()["paths"]["/precedent-finder"]["post"]
    schema = operation["requestBody"]["content"]["application/json"]["schema"]
    assert schema["properties"]["proposition"]["maxLength"] == 3000
    assert schema["required"] == ["proposition"]
    assert schema["additionalProperties"] is False
    assert {"200", "413", "422", "500"} <= set(operation["responses"])
