from datetime import date
from types import SimpleNamespace

import pytest
from fastapi import HTTPException
from pydantic import ValidationError

from backend import routes
from backend.models import (
    CaseIngestRequest,
    CaseReaderMetadataFieldResponse,
    CaseSearchRequest,
    ChunkGroupSearchRequest,
    LocalChunkSearchRequest,
)


@pytest.fixture(autouse=True)
def _enable_ai_rollout_defaults(monkeypatch):
    monkeypatch.setitem(routes.AI_ROLLOUT, "semantic_enabled", True)
    monkeypatch.setitem(routes.AI_ROLLOUT, "hybrid_enabled", True)
    monkeypatch.setitem(routes.AI_ROLLOUT, "local_semantic_enabled", True)
    monkeypatch.setitem(routes.AI_ROLLOUT, "embed_on_ingest_enabled", True)


class FakeDatabase:
    def __init__(self, rows=(), scalar_value=None):
        self.rows = list(rows)
        self.scalar_value = scalar_value
        self.scalars_values = []
        self.added = []
        self.committed = False

    def add(self, value):
        self.added.append(value)

    def commit(self):
        self.committed = True

    def rollback(self):
        self.committed = False

    def refresh(self, value):
        value.id = 1

    def execute(self, statement):
        self.statement = statement
        return self.rows

    def scalar(self, statement):
        self.statement = statement
        return self.scalar_value

    def scalars(self, statement):
        self.statement = statement
        return iter(self.scalars_values)


def test_ingest_stores_metadata_and_embedding(monkeypatch):
    monkeypatch.setattr(routes, "_embed", lambda text: [0.1] * routes.EMBEDDING_DIMENSIONS)
    database = FakeDatabase()
    request = CaseIngestRequest(
        title="Example v. Jones",
        court="Ontario Court of Appeal",
        jurisdiction="Ontario",
        source_type="test_source",
        date=date(2026, 7, 31),
        citation="2026 ONCA 1",
        summary="A contract dispute.",
        issues=["contract interpretation"],
        source_name="Court website",
    )

    result = routes.ingest_case(request, database)

    assert database.committed is True
    assert database.added[0] is result
    assert len(database.added) == 3
    assert result.id == 1
    assert result.citation == "2026 ONCA 1"
    assert result.embedding == [0.1] * routes.EMBEDDING_DIMENSIONS


def test_search_returns_similarity_and_applies_filters(monkeypatch):
    monkeypatch.setattr(routes, "_embed", lambda text: [0.2] * routes.EMBEDDING_DIMENSIONS)
    case = SimpleNamespace(
        id=1,
        title="Example v. Jones",
        court="Ontario Court of Appeal",
        jurisdiction="Ontario",
        date=date(2026, 7, 31),
        citation="2026 ONCA 1",
        summary="A contract dispute.",
        full_text=None,
        issues=["contract interpretation"],
        metadata_json=None,
        source_url=None,
        source_name="Court website",
    )
    database = FakeDatabase(rows=[(case, 0.2, 0.4)])
    request = CaseSearchRequest(
        query="contract interpretation",
        search_mode="hybrid",
        semantic_weight=0.8,
        lexical_weight=0.2,
        court="Ontario Court of Appeal",
        jurisdiction="Ontario",
        source_type="test_source",
        cited_case="2026 ONCA 1",
        citation_contains="ONCA",
        date_from=date(2020, 1, 1),
        date_to=date(2026, 12, 31),
    )

    results = routes.search_cases(request, database)

    assert results[0].title == "Example v. Jones"
    assert results[0].similarity == pytest.approx(0.84)
    params = database.statement.compile().params
    assert any("Ontario Court of Appeal" in str(value) for value in params.values())
    assert "Ontario" in params.values()
    assert "test_source" in params.values()
    assert "%2026 ONCA 1%" in params.values()
    assert "%ONCA%" in params.values()


def test_search_metadata_mode_uses_basic_identifiers(monkeypatch):
    monkeypatch.setattr(routes, "_embed", lambda text: [0.2] * routes.EMBEDDING_DIMENSIONS)
    case = SimpleNamespace(
        id=2,
        title="Doe v. Canada",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2024, 6, 1),
        citation="2024 FC 100",
        summary="Immigration review.",
        full_text=None,
        issues=None,
        metadata_json={"court_number": "IMM-1234-24"},
        source_url=None,
        source_name="Federal Court portal collector",
    )
    database = FakeDatabase(rows=[(case, 0.9)])
    request = CaseSearchRequest(
        query="IMM-1234-24",
        search_mode="metadata",
        court="Federal Court",
        jurisdiction="Canada",
        citation_contains="2024 FC",
    )

    results = routes.search_cases(request, database)

    assert results[0].title == "Doe v. Canada"
    assert results[0].citation == "2024 FC 100"
    assert results[0].similarity == pytest.approx(1.0)
    params = database.statement.compile().params
    assert any("Federal Court" in str(value) for value in params.values())
    assert "Canada" in params.values()
    assert "%2024 FC%" in params.values()


@pytest.mark.parametrize(
    "court_filter,court_value,expected_fragment",
    [
        ("FC", "Federal Court", "%Federal Court%"),
        ("FCA", "Federal Court of Appeal", "%Federal Court of Appeal%"),
        ("SCC", "Supreme Court of Canada", "%Supreme Court of Canada%"),
    ],
)
def test_search_expands_court_abbreviations(monkeypatch, court_filter, court_value, expected_fragment):
    monkeypatch.setattr(routes, "_embed", lambda text: [0.2] * routes.EMBEDDING_DIMENSIONS)
    case = SimpleNamespace(
        id=3,
        title="Example v. Canada",
        court=court_value,
        jurisdiction="Canada",
        date=date(2024, 6, 1),
        citation="2024 FC 200",
        summary="A summary mentioning related citations.",
        full_text=None,
        issues=None,
        metadata_json=None,
        source_url=None,
        source_name="A2AJ Canadian Legal Data",
    )
    database = FakeDatabase(rows=[(case, 0.9, 0.9)])
    request = CaseSearchRequest(
        query="Example",
        search_mode="metadata",
        court=court_filter,
    )

    routes.search_cases(request, database)

    params = database.statement.compile().params
    assert expected_fragment in params.values()


def test_search_applies_extended_metadata_filters(monkeypatch):
    monkeypatch.setattr(routes, "_embed", lambda text: [0.2] * routes.EMBEDDING_DIMENSIONS)
    case = SimpleNamespace(
        id=20,
        title="Example v. Canada",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2024, 6, 1),
        citation="2024 FC 200",
        secondary_citation="2024 FCA 20",
        summary="A summary mentioning related citations.",
        full_text="Minister and IRCC and CBSA appear in the full text.",
        issues=None,
        metadata_json={"court_number": "IMM-1234-24"},
        source_url=None,
        source_name="A2AJ Canadian Legal Data",
        source_id="IMM-1234-24",
        source_type="a2aj_curated",
        language="en",
        processing_status="embedded",
        scraped_at=date(2024, 7, 1),
        citing_cases_count=7,
    )
    database = FakeDatabase(rows=[(case, 0.9)])
    request = CaseSearchRequest(
        query="Example",
        search_mode="metadata",
        title_contains="Example",
        source_name_contains="A2AJ",
        source_url_contains="canlii.org",
        source_id_contains="IMM-1234-24",
        dataset_version_contains="2024",
        upstream_license_contains="Open Government",
        secondary_citation_contains="2024 FCA",
        cases_cited_contains="2024 FC 1",
        cases_citing_contains="2024 FCA 2",
        scraped_from=date(2024, 1, 1),
        scraped_to=date(2024, 12, 31),
        language="en",
        processing_status="embedded",
        citing_cases_min=1,
        citing_cases_max=10,
    )

    routes.search_cases(request, database)
    params = database.statement.compile().params

    assert "%Example%" in params.values()
    assert "%A2AJ%" in params.values()
    assert "%canlii.org%" in params.values()
    assert "%IMM-1234-24%" in params.values()
    assert "%2024%" in params.values()
    assert "%Open Government%" in params.values()
    assert "%2024 FCA%" in params.values()
    assert "%2024 FC 1%" in params.values()
    assert "%2024 FCA 2%" in params.values()
    assert date(2024, 1, 1) in params.values()
    assert date(2024, 12, 31) in params.values()
    assert "en" in params.values()
    assert "embedded" in params.values()
    assert 1 in params.values()


def test_get_case_citation_pass_returns_live_rows(monkeypatch):
    case = SimpleNamespace(
        id=77,
        title="Example v. Canada",
        court="FC",
        citation="2024 FC 100",
        date=date(2024, 1, 1),
        summary=None,
        full_text="See Example v. Canada, 2024 FC 100 under IRPA s. 72(1).",
    )
    class EmptyDB:
        def scalars(self, statement):
            return iter([])

    database = EmptyDB()

    monkeypatch.setattr(routes, "_get_case_or_404", lambda case_id, db: case)
    monkeypatch.setattr(
        routes,
        "extract_case_citation_matches",
        lambda text: [
            SimpleNamespace(
                kind="case",
                citation_text="Example v. Canada, 2024 FC 100",
                normalized_citation="Example v. Canada, 2024 FC 100",
                offset_start=4,
                offset_end=33,
            )
        ],
    )
    monkeypatch.setattr(
        routes,
        "extract_statute_reference_matches",
        lambda text: [
            SimpleNamespace(
                kind="statute",
                citation_text="IRPA s. 72(1)",
                normalized_citation="Immigration and Refugee Protection Act, S.C. 2001, c. 27 s. 72(1)",
                offset_start=41,
                offset_end=54,
            )
        ],
    )
    monkeypatch.setattr(
        routes,
        "extract_metadata_matches",
        lambda text: [
            SimpleNamespace(
                field="docket",
                text="IMM-123-24",
                value="IMM-123-24",
                offset_start=0,
                offset_end=10,
                confidence=0.97,
                source="text",
            )
        ],
    )

    payload = routes.get_case_citation_pass(77, database)

    assert payload["summary"]["live_total"] == 1
    assert payload["summary"]["statute_total"] == 1
    assert payload["summary"]["metadata_total"] == 1
    assert payload["live_extracted"][0]["kind"] == "case"
    assert payload["live_statutes"][0]["kind"] == "statute"
    assert payload["live_metadata"][0]["field"] == "docket"
    assert all(row["kind"] not in {"statute", "instrument"} for row in payload["live_extracted"])
    assert "Example v. Canada" in payload["live_extracted"][0]["context"]


def test_get_case_citation_pass_detail_returns_passage_and_chunk_locations(monkeypatch):
    full_text = "Header\n[1] The Court considered Vavilov, 2019 SCC 65 in context.\nTail"
    case = SimpleNamespace(
        id=77,
        title="Example v. Canada",
        court="FC",
        citation="2024 FC 100",
        date=date(2024, 1, 1),
        summary=None,
        full_text=full_text,
    )
    citation_text = "Vavilov, 2019 SCC 65"
    offset_start = full_text.index(citation_text)
    offset_end = offset_start + len(citation_text)
    chunk_text = full_text[7:-5]
    chunk = SimpleNamespace(
        id=900,
        case_id=77,
        chunk_set="paragraph",
        chunk_index=0,
        chunk_label="Paragraph 1",
        paragraph_start=1,
        paragraph_end=1,
        text=chunk_text,
        token_estimate=14,
    )

    class DetailDB:
        def scalars(self, statement):
            return iter([chunk])

    monkeypatch.setattr(routes, "_get_case_or_404", lambda case_id, db: case)
    monkeypatch.setattr(
        routes,
        "extract_case_citation_matches",
        lambda text: [
            SimpleNamespace(
                kind="case_short",
                citation_text=citation_text,
                normalized_citation="Vavilov, 2019 SCC 65",
                offset_start=offset_start,
                offset_end=offset_end,
            )
        ],
    )
    monkeypatch.setattr(routes, "_stored_case_citation_details", lambda *args: [])

    payload = routes.get_case_citation_pass_detail(
        77,
        layer="case",
        offset_start=offset_start,
        offset_end=offset_end,
        db=DetailDB(),
    )

    assert payload["layer"] == "case"
    assert payload["citation_text"] == citation_text
    assert payload["location"]["line_number"] == 2
    assert payload["location"]["paragraph_number"] == 1
    assert payload["passage"]["text"] == "[1] The Court considered Vavilov, 2019 SCC 65 in context."
    assert payload["chunks"][0]["chunk_id"] == 900
    assert payload["chunks"][0]["chunk_set"] == "paragraph"
    assert payload["chunks"][0]["paragraph_start"] == 1
    assert payload["chunks"][0]["citation_text"] == citation_text


def test_stored_case_citation_details_matches_document_relative_offsets():
    selected = SimpleNamespace(
        citation_text="2014 SCC 68",
        normalized_citation="2014 SCC 68",
        offset_start=115,
        offset_end=126,
    )
    citation = SimpleNamespace(
        id=619679,
        chunk_id=None,
        offset_start=115,
        offset_end=126,
        citation_text="2014 SCC 68",
        normalized_citation="2014 SCC 68",
        provenance="local",
        unresolved=False,
        target_case_id=35868,
    )
    target = SimpleNamespace(
        id=35868,
        title="Febles v. Canada",
        citation="2014 SCC 68",
        court="SCC",
        date=date(2014, 10, 30),
    )

    class StoredCitationDB:
        def scalars(self, statement):
            return iter([citation])

        def get(self, model, record_id):
            return target

    details = routes._stored_case_citation_details(StoredCitationDB(), 35868, selected, [])

    assert details[0]["record_id"] == 619679
    assert details[0]["provenance"] == "local"
    assert details[0]["target"]["case_id"] == 35868


def test_search_party_filters_apply_to_search_document(monkeypatch):
    monkeypatch.setattr(routes, "_embed", lambda text: [0.2] * routes.EMBEDDING_DIMENSIONS)
    case = SimpleNamespace(
        id=3,
        title="Example v. Canada",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2024, 1, 1),
        citation="2024 FC 300",
        summary="Minister review",
        full_text="IRCC and CBSA referenced in the full text.",
        issues=None,
        metadata_json={"party": "IRCC"},
        source_url=None,
        source_name="source",
    )
    database = FakeDatabase(rows=[(case, 0.9)])
    request = CaseSearchRequest(
        query="review",
        search_mode="metadata",
        party_filters=["IRCC", "CBSA", "Minister"],
    )

    routes.search_cases(request, database)
    params = database.statement.compile().params

    assert "%IRCC%" in params.values()
    assert "%CBSA%" in params.values()
    assert "%Minister%" in params.values()


def test_search_party_filters_expand_common_aliases(monkeypatch):
    monkeypatch.setattr(routes, "_embed", lambda text: [0.2] * routes.EMBEDDING_DIMENSIONS)
    case = SimpleNamespace(
        id=4,
        title="Example v. Canada",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2024, 1, 1),
        citation="2024 FC 400",
        summary="MPSEP and Canada Border Services Agency referenced in the decision.",
        full_text="Immigration, Refugees and Citizenship Canada appears in the full text.",
        issues=None,
        metadata_json={"party": "Minister of Public Safety and Emergency Preparedness"},
        source_url=None,
        source_name="source",
    )
    database = FakeDatabase(rows=[(case, 0.9)])
    request = CaseSearchRequest(
        query="review",
        search_mode="metadata",
        party_filters=["Minister", "IRCC", "CBSA"],
    )

    routes.search_cases(request, database)
    params = database.statement.compile().params
    values = list(params.values())

    assert any("%MPSEP%" in value for value in values if isinstance(value, str))
    assert any("%Minister of Public Safety%" in value for value in values if isinstance(value, str))
    assert any("%Immigration, Refugees and Citizenship Canada%" in value for value in values if isinstance(value, str))
    assert any("%Canada Border Services Agency%" in value for value in values if isinstance(value, str))


def test_search_applies_all_exact_legal_tag_filters(monkeypatch):
    monkeypatch.setattr(routes, "_embed", lambda text: [0.2] * routes.EMBEDDING_DIMENSIONS)
    case = SimpleNamespace(
        id=5,
        title="Tagged case",
        court="FC",
        jurisdiction="Canada",
        date=date(2024, 1, 1),
        citation="2024 FC 5",
        summary="Removal decision",
        full_text=None,
        issues=None,
        metadata_json=None,
        source_url=None,
        source_name="source",
    )
    database = FakeDatabase(rows=[(case, 0.9)])
    request = CaseSearchRequest(
        query="removal",
        search_mode="metadata",
        tag_filters=["agency:cbsa", "enforcement_impediment:judicial_stay"],
    )

    routes.search_cases(request, database)
    values = list(database.statement.compile().params.values())

    assert "agency" in values
    assert "cbsa" in values
    assert "enforcement_impediment" in values
    assert "judicial_stay" in values


def test_search_rejects_malformed_legal_tag_filter():
    with pytest.raises(ValidationError):
        CaseSearchRequest(query="removal", tag_filters=["cbsa"])


def test_search_rejects_reversed_date_range():
    request = CaseSearchRequest(
        query="contract",
        date_from=date(2026, 12, 31),
        date_to=date(2026, 1, 1),
    )

    with pytest.raises(HTTPException) as error:
        routes.search_cases(request, FakeDatabase())

    assert error.value.status_code == 422
    assert "date_from" in error.value.detail


def test_search_rejects_reversed_scraped_range():
    request = CaseSearchRequest(
        query="contract",
        scraped_from=date(2026, 12, 31),
        scraped_to=date(2026, 1, 1),
    )

    with pytest.raises(HTTPException) as error:
        routes.search_cases(request, FakeDatabase())

    assert error.value.status_code == 422
    assert "scraped_from" in error.value.detail


def test_search_rejects_invalid_citing_case_bounds():
    request = CaseSearchRequest(
        query="contract",
        citing_cases_min=10,
        citing_cases_max=2,
    )

    with pytest.raises(HTTPException) as error:
        routes.search_cases(request, FakeDatabase())

    assert error.value.status_code == 422
    assert "citing_cases_min" in error.value.detail


def test_embedding_requires_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(HTTPException) as error:
        routes._embed("contract")

    assert error.value.status_code == 503


def test_search_semantic_falls_back_to_metadata_when_rollout_disabled(monkeypatch):
    def fail_if_called(_text):
        raise AssertionError("semantic embeddings should be skipped when rollout disables semantic mode")

    monkeypatch.setattr(routes, "_embed", fail_if_called)
    monkeypatch.setitem(routes.AI_ROLLOUT, "semantic_enabled", False)

    case = SimpleNamespace(
        id=11,
        title="Fallback Case",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2026, 7, 31),
        citation="2026 FC 11",
        summary="fallback summary",
        full_text=None,
        issues=None,
        metadata_json=None,
        source_url=None,
        source_name="source",
    )
    database = FakeDatabase(rows=[(case, 0.4, 0)])
    request = CaseSearchRequest(query="fallback", search_mode="semantic")

    results = routes.search_cases(request, database)

    assert results[0].title == "Fallback Case"


def test_ingest_skips_embedding_when_rollout_embed_disabled(monkeypatch):
    def fail_if_called(_text):
        raise AssertionError("ingest embedding should be disabled by rollout flag")

    monkeypatch.setattr(routes, "_embed", fail_if_called)
    monkeypatch.setitem(routes.AI_ROLLOUT, "embed_on_ingest_enabled", False)

    request = CaseIngestRequest(
        title="No embed rollout",
        court="Federal Court",
        date=date(2026, 7, 31),
        summary="summary",
    )

    result = routes.ingest_case(request, FakeDatabase())

    assert result.embedding is None
    assert result.processing_status == "raw"


def test_local_chunk_search_respects_rollout_disable(monkeypatch):
    monkeypatch.setitem(routes.AI_ROLLOUT, "local_semantic_enabled", False)

    with pytest.raises(HTTPException) as error:
        routes.search_chunks_local(
            LocalChunkSearchRequest(query="fairness", model_name="BAAI/bge-m3"),
            FakeDatabase(),
        )

    assert error.value.status_code == 503



def test_raw_ingest_skips_embedding(monkeypatch):
    def fail_if_called(text):
        raise AssertionError("raw ingestion must not call OpenAI")

    monkeypatch.setattr(routes, "_embed", fail_if_called)
    database = FakeDatabase()
    request = CaseIngestRequest(
        title="A2AJ Raw Record",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2024, 1, 1),
        citation="2024 FC RAW001",
        full_text="Unofficial source text retained for later processing.",
        source_name="A2AJ Canadian Legal Data",
        source_type="a2aj_parquet",
    processing_status="embedded",
    )

    result = routes.ingest_case(request, database)

    assert result.summary is None
    assert result.embedding is None
    assert result.full_text_hash is not None
    assert result.processing_status == "raw"


def test_ingest_hashes_server_text_and_derives_status(monkeypatch):
    monkeypatch.setattr(routes, "_embed", lambda text: [0.1] * routes.EMBEDDING_DIMENSIONS)
    request = CaseIngestRequest(
        title="Hash test",
        court="Federal Court",
        date=date(2024, 1, 1),
        summary="A summary",
        full_text="Authoritative full text",
        full_text_hash="0" * 64,
        processing_status="raw",
    )

    result = routes.ingest_case(request, FakeDatabase())

    assert result.processing_status == "embedded"
    assert result.full_text_hash == __import__("hashlib").sha256(
        b"Authoritative full text"
    ).hexdigest()


def test_get_case_returns_existing_record():
    case = SimpleNamespace(id=22, title="Calixto v. Canada")

    result = routes.get_case(22, FakeDatabase(scalar_value=case))

    assert result is case


def test_get_case_returns_not_found():
    with pytest.raises(HTTPException) as error:
        routes.get_case(999999, FakeDatabase())

    assert error.value.status_code == 404


def test_testing_interface_returns_html_page():
    response = routes.testing_interface()
    html = response.body.decode("utf-8")

    assert response.status_code == 200
    assert "text/html" in response.media_type
    assert "AI CaseLibrary API Tester" in html
    assert "Run grouped chunk search" in html
    assert "Group by case" in html
    assert "Document text query" in html
    assert "Payload preview / advanced override" in html
    assert "Secondary citation" in html
    assert "Source name" in html
    assert "Source URL contains" in html
    assert "Dataset version contains" in html
    assert "Upstream license contains" in html
    assert "Source type" in html
    assert "Language" in html
    assert "Processing status" in html
    assert "Scraped from" in html
    assert "Cases cited contains" in html
    assert "Cases citing contains" in html
    assert "Court type" in html
    assert "Year filter" in html
    assert "Minister" in html
    assert "IRCC" in html
    assert "CBSA" in html
    assert "File number / source ID (identifier)" in html
    assert "Start a search" in html
    assert "Reset your search" in html
    assert "Open text" in html
    assert "caseTextResult" in html
    assert "/search/chunks/grouped" in html
    assert '"cited_case": "2007 FC 1262"' in html


def test_grouped_chunk_search_groups_by_case(monkeypatch):
    monkeypatch.setattr(routes, "_embed", lambda text: [0.2] * routes.EMBEDDING_DIMENSIONS)
    case_a = SimpleNamespace(
        id=101,
        title="Case A",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2026, 1, 1),
        citation="2026 FC 101",
        summary="A",
        full_text=None,
        issues=None,
        metadata_json=None,
        source_url=None,
        source_name="source",
    )
    case_b = SimpleNamespace(
        id=202,
        title="Case B",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2026, 1, 2),
        citation="2026 FC 202",
        summary="B",
        full_text=None,
        issues=None,
        metadata_json=None,
        source_url=None,
        source_name="source",
    )
    chunk_a1 = SimpleNamespace(chunk_index=0, text="Best passage A")
    chunk_b1 = SimpleNamespace(chunk_index=1, text="Best passage B")
    chunk_a2 = SimpleNamespace(chunk_index=2, text="Second passage A")

    database = FakeDatabase(
        rows=[
            (case_a, chunk_a1, 0.10, 0.9),
            (case_b, chunk_b1, 0.15, 0.8),
            (case_a, chunk_a2, 0.20, 0.7),
        ]
    )
    request = ChunkGroupSearchRequest(
        query="risk",
        source_type="a2aj_curated",
        page=1,
        page_size=5,
        max_chunks_per_case=1,
    )

    result = routes.search_chunks_grouped(request, database)

    assert result.result_type == "grouped_by_case"
    assert result.total_chunks == 3
    assert result.total_cases == 2
    assert len(result.cases) == 2
    assert result.cases[0].id == 101
    assert result.cases[0].chunks[0].chunk_text == "Best passage A"
    assert len(result.cases[0].chunks) == 1
    assert result.cases[1].id == 202


def test_grouped_chunk_search_lexical_mode_skips_embedding(monkeypatch):
    def fail_if_called(text):
        raise AssertionError("lexical grouped mode should not call embeddings")

    monkeypatch.setattr(routes, "_embed", fail_if_called)
    case = SimpleNamespace(
        id=301,
        title="Lexical grouped case",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2026, 7, 31),
        citation="2026 FC 301",
        summary="A",
        full_text=None,
        issues=None,
        metadata_json=None,
        source_url=None,
        source_name="source",
    )
    chunk = SimpleNamespace(chunk_index=0, text="state protection discussion")
    database = FakeDatabase(rows=[(case, chunk, 0.5)])
    request = ChunkGroupSearchRequest(
        query="state protection",
        search_mode="lexical",
        page=1,
        page_size=5,
        max_chunks_per_case=2,
    )

    result = routes.search_chunks_grouped(request, database)

    assert result.total_cases == 1
    assert result.cases[0].id == 301


def test_chunk_search_applies_citation_filters(monkeypatch):
    monkeypatch.setattr(routes, "_embed", lambda text: [0.2] * routes.EMBEDDING_DIMENSIONS)
    case = SimpleNamespace(
        id=1,
        title="Example v. Jones",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2026, 7, 31),
        citation="2026 FC 1",
        summary="A",
        full_text=None,
        issues=None,
        metadata_json=None,
        source_url=None,
        source_name="source",
    )
    chunk = SimpleNamespace(chunk_index=1, text="Passage")
    database = FakeDatabase(rows=[(case, chunk, 0.2)])
    request = CaseSearchRequest(
        query="risk",
        cited_case="2026 FC 1",
        citation_contains="FC",
    )

    routes.search_chunks(request, database)
    params = database.statement.compile().params

    assert "%2026 FC 1%" in params.values()
    assert "%FC%" in params.values()


def test_local_chunk_search_uses_requested_model(monkeypatch):
    provider = SimpleNamespace(embed_query=lambda text: [0.3] * 1024)
    monkeypatch.setattr(routes, "_local_embedding_provider", lambda model_name: provider)
    case = SimpleNamespace(
        id=701,
        title="Local vector case",
        court="FC",
        jurisdiction="Canada",
        date=date(2026, 1, 1),
        citation="2026 FC 701",
        summary=None,
        full_text="Reasons",
        issues=None,
        metadata_json=None,
        source_url=None,
        source_name="A2AJ",
    )
    chunk = SimpleNamespace(chunk_index=2, text="Relevant local passage")
    database = FakeDatabase(rows=[(case, chunk, 0.12)])

    result = routes.search_chunks_local(
        LocalChunkSearchRequest(query="procedural fairness", model_name="BAAI/bge-m3"),
        database,
    )

    assert result[0].id == 701
    assert result[0].chunk_text == "Relevant local passage"
    assert result[0].similarity == pytest.approx(0.88)
    assert "BAAI/bge-m3" in database.statement.compile().params.values()


def test_search_lexical_mode_skips_embedding_call(monkeypatch):
    def fail_if_called(text):
        raise AssertionError("lexical mode should not call embeddings")

    monkeypatch.setattr(routes, "_embed", fail_if_called)
    case = SimpleNamespace(
        id=1,
        title="Lexical Case",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2026, 7, 31),
        citation="2026 FC 55",
        summary="state protection analysis",
        full_text=None,
        issues=None,
        metadata_json=None,
        source_url=None,
        source_name="source",
    )
    database = FakeDatabase(rows=[(case, 0.3)])
    request = CaseSearchRequest(query="state protection", search_mode="lexical")

    results = routes.search_cases(request, database)

    assert results[0].title == "Lexical Case"


def test_hybrid_mode_requires_non_zero_weight_sum():
    with pytest.raises(ValidationError):
        CaseSearchRequest(
            query="risk",
            search_mode="hybrid",
            semantic_weight=0.0,
            lexical_weight=0.0,
        )


def test_ingest_adds_extracted_citations_to_metadata(monkeypatch):
    monkeypatch.setattr(routes, "_embed", lambda text: [0.1] * routes.EMBEDDING_DIMENSIONS)
    monkeypatch.setattr(routes, "_extract_legal_citations", lambda text: ["2007 FC 1262", "2026 ONCA 1"])

    request = CaseIngestRequest(
        title="Citation extraction test",
        court="Federal Court",
        date=date(2026, 7, 31),
        summary="Cites 2007 FC 1262 and 2026 ONCA 1.",
        metadata_json={"source": "unit-test"},
    )

    result = routes.ingest_case(request, FakeDatabase())

    assert result.metadata_json["source"] == "unit-test"
    assert result.metadata_json["extracted_citations"] == ["2007 FC 1262", "2026 ONCA 1"]
    assert result.cases_cited == ["2007 FC 1262", "2026 ONCA 1"]


def test_ingest_preserves_cases_cited_when_provided(monkeypatch):
    monkeypatch.setattr(routes, "_embed", lambda text: [0.1] * routes.EMBEDDING_DIMENSIONS)
    monkeypatch.setattr(routes, "_extract_legal_citations", lambda text: ["2007 FC 1262"])

    request = CaseIngestRequest(
        title="Explicit cited list",
        court="Federal Court",
        date=date(2026, 7, 31),
        summary="Citation text",
        cases_cited=["manual-citation"],
    )

    result = routes.ingest_case(request, FakeDatabase())

    assert result.cases_cited == ["manual-citation"]


@pytest.mark.parametrize(
    "court,citation,full_text,expected_court_type,expected_case_number",
    [
        (
            "Federal Court",
            "2024 FC 1",
            "Date: 2024-01-02\nDocket: IMM-123-24\nCitation: 2024 FC 1\nBETWEEN:\nJane Doe v. Canada",
            "FC",
            "IMM-123-24",
        ),
        (
            "Federal Court of Appeal",
            "2024 FCA 2",
            "Case number: A-123-24\nCitation: 2024 FCA 2\nSTYLE OF CAUSE: Smith v. Canada",
            "FCA",
            "A-123-24",
        ),
        (
            "Supreme Court of Canada",
            "2024 SCC 3",
            "Case number: 40000\nCitation: 2024 SCC 3\nSTYLE OF CAUSE: Roe v. Canada",
            "SC",
            "40000",
        ),
    ],
)
def test_reader_metadata_derives_court_type_and_case_number(court, citation, full_text, expected_court_type, expected_case_number):
    case = SimpleNamespace(
        id=1,
        title="Sample v. Canada",
        court=court,
        jurisdiction="Canada",
        date=date(2024, 1, 2),
        citation=citation,
        summary=None,
        full_text=full_text,
    )

    rows = routes._build_reader_extracted_metadata(case, [], include_canonical_fields=False)
    metadata = {row.key: row.value for row in rows}

    assert metadata["court_type"] == expected_court_type
    assert metadata["case_number"] == expected_case_number
    assert metadata["docket"] == expected_case_number


def test_metadata_pass_normalized_display_formats_human_fields():
    case = SimpleNamespace(
        id=6617,
        title="A.B. v THE MINISTER OF CITIZENSHIP AND IMMIGRATION",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2021, 1, 1),
        citation="2021 FC 1",
        summary=None,
        full_text=None,
        language="EN",
        source_id="IMM-111-20",
    )

    extracted = [
        CaseReaderMetadataFieldResponse(key="court_type", value="FC", source="reader_derived", evidence="FC"),
        CaseReaderMetadataFieldResponse(key="case_number", value="IMM-111-20", source="reader_extracted", evidence="Docket: IMM-111-20"),
        CaseReaderMetadataFieldResponse(key="style_of_cause_text", value="A.B. V THE MINISTER OF CITIZENSHIP AND IMMIGRATION", source="reader_extracted", evidence="style"),
        CaseReaderMetadataFieldResponse(key="applicant", value="A.B.", source="reader_derived", evidence="caption"),
        CaseReaderMetadataFieldResponse(key="respondent", value="THE MINISTER OF CITIZENSHIP AND IMMIGRATION", source="reader_derived", evidence="caption"),
    ]

    normalized = routes._build_metadata_pass_normalized_rows(case, extracted)
    values = {row["key"]: row["value"] for row in normalized}

    assert values["tribunal"] == "Federal Court"
    assert values["court_type"] == "FC"
    assert values["case_number"] == "IMM-111-20"
    assert values["style_of_cause"] == "A.B. v. The Minister of Citizenship and Immigration"
    assert values["respondent"] == "The Minister of Citizenship and Immigration"
    assert values["language"] == "en"


def test_metadata_pass_response_includes_normalized_display(monkeypatch):
    case = SimpleNamespace(
        id=1,
        title="Sample",
        citation="2024 SCC 1",
        court="Supreme Court of Canada",
        date=date(2024, 1, 1),
        language="EN",
        source_id="40000",
    )

    extracted = [
        CaseReaderMetadataFieldResponse(key="court_type", value="SC", source="reader_derived", evidence="SC"),
        CaseReaderMetadataFieldResponse(key="case_number", value="40000", source="reader_derived", evidence="40000"),
        CaseReaderMetadataFieldResponse(key="style_of_cause_text", value="ROE V. CANADA", source="reader_extracted", evidence="style"),
    ]

    monkeypatch.setattr(routes, "_get_case_or_404", lambda case_id, db: case)
    monkeypatch.setattr(routes, "_build_reader_extracted_metadata", lambda _case, _chunks, include_canonical_fields=False: extracted)

    payload = routes.get_case_metadata_pass(1, FakeDatabase())

    assert "normalized_display" in payload
    normalized = {row["key"]: row["value"] for row in payload["normalized_display"]}
    assert normalized["tribunal"] == "Supreme Court of Canada"
    assert normalized["style_of_cause"] == "Roe v. Canada"


def test_prototype_graph_returns_subgraph_payload(monkeypatch):
    case_a = SimpleNamespace(
        id=10,
        title="A v. Canada",
        citation="2020 FC 10",
        court="FC",
        date=date(2020, 1, 10),
        summary="",
        full_text="",
        metadata_json={"topic_keywords": ["refugee_protection"]},
        cases_cited=[],
    )
    case_b = SimpleNamespace(
        id=20,
        title="B v. Canada",
        citation="2021 FC 20",
        court="FC",
        date=date(2021, 2, 20),
        summary="",
        full_text="",
        metadata_json={"topic_keywords": ["refugee_protection"]},
        cases_cited=[],
    )
    case_c = SimpleNamespace(
        id=30,
        title="C v. Canada",
        citation="2022 FC 30",
        court="FC",
        date=date(2022, 3, 30),
        summary="",
        full_text="",
        metadata_json={"topic_keywords": ["family_hc"]},
        cases_cited=[],
    )

    database = FakeDatabase()
    database.scalars_values = [case_a, case_b, case_c]
    monkeypatch.setattr(routes, "_prototype_case_ids", lambda: [10, 20, 30])
    monkeypatch.setattr(
        routes,
        "_prototype_edges",
        lambda: [(10, 20, "2021 FC 20"), (20, 30, "2022 FC 30")],
    )

    payload = routes.prototype_graph(max_nodes=100, topic="refugee_protection", db=database)

    assert payload["meta"]["returned_nodes"] == 3
    assert payload["meta"]["returned_edges"] == 2
    assert len(payload["nodes"]) == 3
    assert len(payload["edges"]) == 2


def test_prototype_cases_clamps_to_first_page_when_out_of_range(monkeypatch):
    case = SimpleNamespace(
        id=99,
        title="Single match",
        citation="2024 FC 99",
        court="FC",
        date=date(2024, 1, 1),
        summary="",
        full_text="",
        processing_status="embedded",
        metadata_json={"topic_keywords": ["refugee_protection"]},
        cases_cited=[],
    )
    database = FakeDatabase(rows=[(99, 3)])
    database.scalars_values = [case]
    monkeypatch.setattr(routes, "_prototype_case_ids", lambda: [99])

    payload = routes.prototype_cases(q="single", page=5, page_size=20, db=database)

    assert payload["total"] == 1
    assert payload["page"] == 1
    assert len(payload["items"]) == 1
