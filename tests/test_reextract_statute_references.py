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
