import json
from pathlib import Path

from scripts.import_fc_decisions import dedupe_key, load_records, to_ingest_payload


def test_load_records_jsonl(tmp_path: Path):
    sample = tmp_path / "fc.jsonl"
    sample.write_text('{"style_of_cause":"A v B","decision_date":"2025-01-01","summary":"x"}\n', encoding="utf-8")

    rows = load_records(sample)

    assert len(rows) == 1
    assert rows[0]["style_of_cause"] == "A v B"


def test_to_ingest_payload_maps_fc_fields():
    record = {
        "style_of_cause": "Doe v Canada",
        "neutral_citation": "2025 FC 123",
        "decision_date": "2025-01-02",
        "full_text": "Long decision text",
        "docket_number": "IMM-1234-24",
    }

    payload = to_ingest_payload(record, source_name="FC Bulk")

    assert payload["title"] == "Doe v Canada"
    assert payload["citation"] == "2025 FC 123"
    assert payload["source_type"] == "federal_court"
    assert payload["source_name"] == "FC Bulk"
    assert payload["metadata_json"]["docket_number"] == "IMM-1234-24"


def test_dedupe_key_prefers_source_id_then_citation():
    payload = {
        "source_id": "IMM-1",
        "citation": "2024 FC 1",
        "title": "X",
    }

    key = dedupe_key(payload)

    assert key == "imm-1"


def test_load_records_jsonl_skips_non_import_stages(tmp_path: Path):
    sample = tmp_path / "collector.jsonl"
    sample.write_text(
        "\n".join(
            [
                '{"stage":"listing","file_number":"IMM-1"}',
                '{"stage":"detail","file_number":"IMM-1"}',
                '{"stage":"import_ready","style_of_cause":"Doe v Canada","neutral_citation":"2025 FC 12","decision_date":"2025-01-01","full_text":"Decision text","docket_number":"IMM-1","url":"https://example.com/f/1"}',
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    rows = load_records(sample)

    assert len(rows) == 1
    assert rows[0]["style_of_cause"] == "Doe v Canada"
    assert rows[0]["decision_date"] == "2025-01-01"
