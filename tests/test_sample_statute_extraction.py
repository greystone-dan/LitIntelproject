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


def test_bare_rule_ties_to_federal_courts_rules_only_after_they_are_named():
    named = analyze_text("Under the Federal Courts Rules, SOR/98-106, see Rule 53(1) and Rule 5 of the Tax Court Rules.")
    keyed = {(e["instrument_key"], e["pinpoint"]) for e in named["extracted"]}
    assert ("canada.federal_courts_rules", "53(1)") in keyed
    assert ("canada.federal_courts_rules", "5") not in keyed
    assert not [e for e in analyze_text("See Rule 53(1).")["extracted"] if e["instrument_key"]]


def test_fc_citizenship_immigration_rules_are_registered():
    result = analyze_text("Rule 9 of the Federal Courts Citizenship, Immigration and Refugee Protection Rules, SOR/93-22 applies.")
    keyed = {(e["instrument_key"], e["pinpoint"]) for e in result["extracted"]}
    assert ("canada.fc_cirp_rules", "9") in keyed


def test_anchored_provision_guards():
    text = "The Charter applies. The pre-trial order under s. 515(10)(c) and the Year Book 19 E. 3 R.S. 346 were cited."
    found = [e for e in analyze_text(text)["extracted"] if e["instrument_key"] == "canada.charter" and e["pinpoint"]]
    assert not found


def test_provision_identity_does_not_read_a_range_word_as_a_section_suffix():
    from backend.statutes import parse_provision_identity

    assert parse_provision_identity("34 to 37")[0] == "34"
    assert parse_provision_identity("7 and 8")[0] == "7"
    assert parse_provision_identity("31A(1)")[0] == "31a"
