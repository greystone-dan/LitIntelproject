from types import SimpleNamespace

from backend.citations import extract_statute_reference_matches
from scripts.build_statute_demand_report import occurrence_record, paragraph_location


def test_paragraph_location_starts_at_zero():
    assert paragraph_location("First paragraph.", 0, 5)["paragraph_offset_start"] == 0


def test_occurrence_record_contains_ui_ready_location_and_context():
    text = "The tribunal applied paragraph 34(1)(f) of IRPA.\n\nThe claim continued."
    match = extract_statute_reference_matches(text)[0]
    row = SimpleNamespace(
        id=42,
        title="Example v. Canada",
        court="Federal Court",
        citation="2024 FC 1",
        full_text_hash="abc123",
    )

    record = occurrence_record(row, text, match, 0, 20)

    assert record["occurrence_id"] == "42:0"
    assert record["instrument_key"] == "canada.irpa"
    assert record["pinpoint"] == "34(1)(f)"
    assert record["offset_start"] < record["offset_end"]
    assert text[record["offset_start"] : record["offset_end"]] == record["reference_text"]
    assert record["exact_span_valid"] is True
    assert record["location"]["paragraph_index"] == 1
    assert "34(1)(f)" in record["context_excerpt"]
    assert record["resolution_status"] == "identified_unresolved"
