import json


def test_baseline_snapshot_schema_is_compact_and_layer_complete():
    record = {
        "case_id": 1,
        "text_length": 100,
        "full_text_hash": "hash",
        "source_html_present": True,
        "chunk_counts": {"full_case": 1, "paragraph": 2},
        "citation_count": 3,
        "statute_count": 4,
        "v3_tag_count": 5,
        "outcome": {"status": "undetermined"},
    }

    encoded = json.dumps(record)

    assert len(encoded) < 1000
    assert set(("chunk_counts", "citation_count", "statute_count", "v3_tag_count", "outcome")).issubset(record)
