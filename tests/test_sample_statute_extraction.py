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


def test_refugee_division_bare_sections_default_to_the_irpa():
    text = "The claim is made under section 96 and subsection 97(1) of the Act. The Charter s. 7 applies. Section 3.2 of the report states x."
    board = {(e["instrument_key"], e["pinpoint"]) for e in analyze_text(text, "RPD")["extracted"]}
    assert ("canada.irpa", "96") in board and ("canada.irpa", "97(1)") in board
    assert ("canada.charter", "7") in board
    assert not [e for e in analyze_text(text, "RPD")["extracted"] if e["pinpoint"] == "3.2"]
    court = {(e["instrument_key"], e["pinpoint"]) for e in analyze_text(text, "FC")["extracted"]}
    assert ("canada.irpa", "96") not in court


def test_bare_section_96_is_never_tied_to_the_charter():
    text = "The Charter applies to this hearing. The risk assessment under section 96 and sections 97 and 98 was reasonable."
    assert not [e for e in analyze_text(text)["extracted"] if e["instrument_key"] == "canada.charter" and e["pinpoint"]]


def test_federal_court_immigration_decision_ties_bare_96_to_irpa_not_charter():
    text = (
        "This is an application under the Immigration and Refugee Protection Act (the \"Act\"). "
        "The applicant argues that section 7 of the Charter is engaged. "
        "He says the denial of a section 96 risk assessment breaches section 7. Under section 97 of the Act it fails."
    )
    keyed = {(e["text"], e["instrument_key"], e["pinpoint"]) for e in analyze_text(text, "FC")["extracted"]}
    assert ("section 96", "canada.irpa", "96") in keyed
    assert ("section 97", "canada.irpa", "97") in keyed
    assert not [k for k in keyed if k[1] == "canada.charter" and k[2] == "96"]


def test_non_immigration_decision_does_not_default_to_irpa():
    text = "The Patent Act (the \"Act\") applies. See section 96 of the Act and section 97."
    assert not [e for e in analyze_text(text, "FC")["extracted"] if e["instrument_key"] == "canada.irpa"]


_CASE_35113_TEXT = (
    "Docket: IMM-20375-24 "
    "The Applicant relies on subsection 108(4) of the IRPA and says denial of an abeyance would be contrary to his section 7 rights under the "
    "Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982, being Schedule B to the Canada Act 1982 (UK), 1982, c 11 [Charter]. "
    "He asks for a remedy under subsection 24(1) of the Charter. The Officer limited the analysis to section 97 of the IRPA as the Applicant did not fall within "
    "subparagraphs 113(e)(i) or (ii) of the IRPA. Under the compelling reasons exception in subsection 108(4) of the IRPA, paragraph 108(1)(e) does not apply. "
    "As the PRRA will not be assessed under Section 96, 1 note that pursuant to section 97(1)(b)(iv) of the IRPA the Officer is precluded. "
    "The first requirement for the application of section 108(4) is met. It is at the removal stage where the section 7 interests are engaged. "
    "The IRPA, the IRPA and the IRPA again; the IRPA once more."
)


def _keyed(text, court="FC"):
    return {(e["text"], e["instrument_key"], e["pinpoint"]) for e in analyze_text(text, court)["extracted"]}


def test_case_35113_charter_rights_and_interests_stay_with_the_charter():
    keyed = _keyed(_CASE_35113_TEXT)
    assert ("section 7", "canada.charter", "7") in keyed
    assert ("subsection 24(1) of the Charter", "canada.charter", "24(1)") in keyed
    assert not [k for k in keyed if k[1] == "canada.irpa" and k[2] == "7"]


def test_case_35113_bare_irpa_provisions_follow_the_dominant_act():
    keyed = _keyed(_CASE_35113_TEXT)
    assert ("section 108(4)", "canada.irpa", "108(4)") in keyed
    assert ("paragraph 108(1)(e)", "canada.irpa", "108(1)(e)") in keyed


def test_case_35113_bracket_continuation_stray_digit_and_canada_act():
    result = analyze_text(_CASE_35113_TEXT, "FC")["extracted"]
    assert ("subparagraphs 113(e)(i) or (ii) of the IRPA", "canada.irpa", "113(e)(i),113(e)(ii)") in {
        (e["text"], e["instrument_key"], e["pinpoint"]) for e in result
    }
    assert not [e for e in result if e["text"].strip().lower() == "canada act"]
    assert ("Section 96", "canada.irpa", "96") in {(e["text"], e["instrument_key"], e["pinpoint"]) for e in result}


def test_the_act_defined_in_the_decision_is_used_for_bare_provisions():
    text = (
        'The Customs Act R.S.C. 1985 c-1 (2nd Supp.) (the "Act") applies. ' + "x " * 400 +
        "A Notice pursuant to subsection 124(1) of the Act was issued. " + "y " * 400 +
        "The Federal Court Act applies. " + "zz. " * 300 + "Section 135 of the Act provides an appeal."
    )
    keyed = {(e["text"], e["instrument_key"], e["pinpoint"]) for e in analyze_text(text)["extracted"]}
    assert ("subsection 124(1)", "canada.customs_act", "124(1)") in keyed
    assert ("Section 135", "canada.customs_act", "135") in keyed


def test_bare_of_the_act_with_unregistered_nearest_act_keeps_a_row_without_instrument():
    text = "The Radiocommunication Act applies. Subsection 140(1) of the Act provides for reviews."
    rows = [e for e in analyze_text(text)["extracted"] if e["text"].lower().startswith("subsection")]
    assert rows and rows[0]["instrument_key"] is None
