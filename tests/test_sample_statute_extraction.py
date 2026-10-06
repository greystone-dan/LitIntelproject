from scripts.sample_statute_extraction import analyze_text


def test_analyze_text_reports_extracted_and_loose_mentions():
    text = "See paragraph 3(b) of the policy. The officer applied subsection 24(1) of the Charter."
    result = analyze_text(text)
    assert any(row["instrument_key"] == "canada.charter" and row["pinpoint"] == "24(1)" for row in result["extracted"])
    assert any("paragraph 3(b)" in row["text"] for row in result["loose_unmatched"])
