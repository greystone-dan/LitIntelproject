from datetime import datetime, timezone

from scripts.ingest_a2aj_parquet import build_case


def test_build_case_preserves_rich_source_metadata_without_duplicating_text():
    record = {
        "dataset": "FCA",
        "citation_en": "2024 FCA 12",
        "citation_fr": "2024 CAF 12",
        "name_en": "Example v Canada",
        "name_fr": "Exemple c Canada",
        "document_date_en": "2024-02-03",
        "url_en": "https://example.test/en",
        "url_fr": "https://example.test/fr",
        "unofficial_text_en": "Reasons for decision",
        "cases_cited_en": ["2020 SCC 1"],
        "cases_citing_en": ["2025 FCA 2"],
        "citing_cases_count": 1,
        "scraped_timestamp_en": datetime(2026, 1, 2, tzinfo=timezone.utc),
        "upstream_license": "Open Government Licence",
    }

    case = build_case(record)

    assert case is not None
    assert case.court == "FCA"
    assert case.cases_cited == ["2020 SCC 1"]
    assert case.metadata_json["citation_fr"] == "2024 CAF 12"
    assert case.metadata_json["name_fr"] == "Exemple c Canada"
    assert case.metadata_json["scraped_timestamp_en"] == "2026-01-02T00:00:00+00:00"
    assert "unofficial_text_en" not in case.metadata_json
