from scripts.sample_statute_extraction import analyze_text


def test_analyze_text_reports_extracted_and_loose_mentions():
    text = "See paragraph 3(b) of the policy. The officer applied subsection 24(1) of the Charter."
    result = analyze_text(text)
    assert any(row["instrument_key"] == "canada.charter" and row["pinpoint"] == "24(1)" for row in result["extracted"])
    assert any("paragraph 3(b)" in row["text"] for row in result["loose_unmatched"])


def test_bare_section_of_the_act_is_not_anchored_to_nearest_instrument():
    from backend.citations import extract_statute_reference_matches

    text = "The Charter was raised. Regarding section 18 of the Act, the Tribunal ruled."
    assert not [m for m in extract_statute_reference_matches(text) if "18" in (m.normalized_citation or "")]


def test_provision_with_letter_subparagraph_takes_named_regulations():
    result = analyze_text(
        "See subsection 108(2) of IRPA and paragraph 228(1)(b.1) of the Immigration and Refugee Protection Regulations, SOR/2002-227 apply."
    )
    keyed = {(e["instrument_key"], e["pinpoint"]) for e in result["extracted"]}
    assert ("canada.irpr", "228(1)") in keyed
