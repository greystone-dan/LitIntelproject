from scripts.compare_pipeline_case import compare_snapshots


def test_compare_snapshots_reports_layer_deltas_and_outcome_change():
    before = {
        "case_id": 7,
        "source_html_present": False,
        "text_length": 100,
        "chunks": [{"chunk_set": "paragraph", "chunk_index": 0, "text_hash": "old"}],
        "citations": [{"kind": "case", "normalized": "Old v. Canada", "text": "Old v Canada", "offset_start": 1, "offset_end": 13}],
        "statutes": [{"kind": "irpa", "normalized": "IRPA s. 7", "instrument_key": "irpa", "pinpoint": "7", "offset_start": 20, "offset_end": 29}],
        "tags_v3": [{"category": "agency", "value": "ircc", "offset_start": 30, "offset_end": 34}],
        "outcome": {"outcome_status": "undetermined"},
    }
    after = {
        "case_id": 7,
        "source_html_present": True,
        "text_length": 100,
        "chunks": [{"chunk_set": "paragraph", "chunk_index": 0, "text_hash": "new"}],
        "citations": [{"kind": "case", "normalized": "New v. Canada", "text": "New v Canada", "offset_start": 1, "offset_end": 13}],
        "statutes": [],
        "tags_v3": [
            {"category": "agency", "value": "ircc", "offset_start": 30, "offset_end": 34},
            {"category": "agency", "value": "cbsa", "offset_start": 40, "offset_end": 44},
        ],
        "outcome": {"outcome_status": "won"},
    }

    result = compare_snapshots(before, after)

    assert result["after_source_html_present"] is True
    assert result["chunks"]["delta"] == 0
    assert result["citations"]["delta"] == 0
    assert result["statutes"]["delta"] == -1
    assert result["statutes"]["major_delta"] is False
    assert result["tags_v3"]["delta"] == 1
    assert result["outcome_before"]["outcome_status"] == "undetermined"
    assert result["outcome_after"]["outcome_status"] == "won"
