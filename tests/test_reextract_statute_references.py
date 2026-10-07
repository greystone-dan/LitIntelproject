from scripts.reextract_statute_references import diff_case, new_rows_for_texts, summarize


def test_new_extraction_keeps_decimal_sections_and_lists():
    rows = new_rows_for_texts(["Under section 18.1 of the Federal Courts Act and sections 96 and 97 of IRPA."])
    stats = summarize(rows)
    assert stats["decimal_sections"] == 1
    assert stats["list_rows"] == 1
    assert stats["instrument:canada.federal_courts_act"] == 1


def test_diff_counts_changed_references():
    old = [{"instrument_key": "canada.federal_courts_act", "pinpoint": "18"}]
    new = [{"instrument_key": "canada.federal_courts_act", "pinpoint": "18.1"}]
    assert diff_case(old, new) == {"added": 1, "removed": 1, "unchanged": 0}


def test_detail_record_lists_removed_and_added_rows_with_context():
    from scripts.reextract_statute_references import detail_record

    old = [
        {"instrument_key": "canada.irpa", "pinpoint": "96", "reference_text": "s. 96", "offset_start": 4, "offset_end": 9},
        {"instrument_key": None, "pinpoint": "7", "reference_text": "s. 7", "offset_start": 20, "offset_end": 24},
    ]
    new = [
        {"instrument_key": "canada.irpa", "pinpoint": "96", "reference_text": "s. 96", "offset_start": 4, "offset_end": 9},
        {"instrument_key": "canada.charter", "pinpoint": "7", "reference_text": "s. 7", "offset_start": 20, "offset_end": 24},
    ]
    text = "See s. 96 of the Act and then s. 7 of the Charter."
    record = detail_record(12, text, old, new)
    assert record["case_id"] == 12
    assert [r["instrument_key"] for r in record["removed"]] == [None]
    assert [r["instrument_key"] for r in record["added"]] == ["canada.charter"]
    assert "s. 7" in record["added"][0]["context"]


def test_read_backup_keeps_first_entry_per_case(tmp_path):
    import json

    from scripts.reextract_statute_references import read_backup

    path = tmp_path / "backup.jsonl"
    path.write_text(
        json.dumps({"case_id": 5, "rows": [{"id": 1, "pinpoint": "18"}]}) + "\n"
        + "\n"
        + json.dumps({"case_id": 5, "rows": [{"id": 9, "pinpoint": "18.1"}]}) + "\n"
        + json.dumps({"case_id": 6, "rows": []}) + "\n",
        encoding="utf-8",
    )
    saved = read_backup(path)
    assert saved == {5: [{"id": 1, "pinpoint": "18"}], 6: []}
