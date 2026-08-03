from datetime import date

from backend.database import Case
from backend.ingestion import merge_case_fields, merge_metadata, source_priority
from backend.models import CaseIngestRequest


def test_source_priority_prefers_official_without_discarding_a2aj():
    assert source_priority("federal_court") > source_priority("canlii_html_seed")
    assert source_priority("canlii_html_seed") > source_priority("a2aj_parquet")
    assert source_priority("a2aj_parquet") > source_priority(None)


def test_merge_metadata_preserves_existing_values_and_records_conflicts():
    merged = merge_metadata(
        {"judge": "Existing Judge", "nested": {"language": "en"}},
        {"judge": "Incoming Judge", "nested": {"language": "fr", "panel": 3}},
        source_type="a2aj_parquet",
    )

    assert merged["judge"] == "Existing Judge"
    assert merged["nested"] == {"language": "en", "panel": 3}
    assert {conflict["path"] for conflict in merged["_source_conflicts"]} == {
        "judge",
        "nested.language",
    }


def test_lower_priority_merge_fills_gaps_and_unions_citations():
    existing = Case(
        title="Official title",
        court="FC",
        jurisdiction="Canada",
        date=date(2024, 1, 1),
        citation="2024 FC 1",
        full_text="Official reasons",
        source_type="federal_court",
        source_url=None,
        metadata_json={"judge": "Official Judge"},
        cases_cited=["2020 SCC 1"],
        cases_citing=None,
        citing_cases_count=1,
        processing_status="raw",
    )
    incoming = CaseIngestRequest(
        title="A2AJ title",
        court="FC",
        jurisdiction="Canada",
        date=date(2024, 1, 1),
        citation="2024 FC 1",
        full_text="Unofficial reasons",
        source_type="a2aj_parquet",
        source_url="https://example.test/a2aj",
        metadata_json={"judge": "A2AJ Judge", "citation_fr": "2024 CF 1"},
        cases_cited=["2020 SCC 1", "2021 FCA 2"],
        cases_citing=["2025 FC 2"],
        citing_cases_count=3,
    )

    changed = merge_case_fields(existing, incoming)

    assert existing.title == "Official title"
    assert existing.full_text == "Official reasons"
    assert existing.source_url == "https://example.test/a2aj"
    assert existing.cases_cited == ["2020 SCC 1", "2021 FCA 2"]
    assert existing.cases_citing == ["2025 FC 2"]
    assert existing.citing_cases_count == 3
    assert existing.metadata_json["judge"] == "Official Judge"
    assert existing.metadata_json["citation_fr"] == "2024 CF 1"
    assert "source_url" in changed
    assert "full_text" not in changed


def test_higher_priority_merge_updates_canonical_fields():
    existing = Case(
        title="Unofficial title",
        court="FC",
        jurisdiction="Canada",
        date=date(2024, 1, 1),
        citation="2024 FC 1",
        full_text="Unofficial reasons",
        source_type="a2aj_parquet",
        processing_status="raw",
    )
    incoming = CaseIngestRequest(
        title="Official title",
        court="FC",
        jurisdiction="Canada",
        date=date(2024, 1, 2),
        citation="2024 FC 1",
        full_text="Official reasons",
        source_type="federal_court",
    )

    changed = merge_case_fields(existing, incoming)

    assert existing.title == "Official title"
    assert existing.date == date(2024, 1, 2)
    assert existing.full_text == "Official reasons"
    assert existing.source_type == "federal_court"
    assert {"title", "date", "full_text", "source_type"}.issubset(changed)
