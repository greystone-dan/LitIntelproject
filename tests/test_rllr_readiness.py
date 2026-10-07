"""Refugee Law Lab Reporter copies of Refugee Protection Division decisions: header block and claim ruling."""
from backend.metadata import extract_case_metadata
from backend.metadata_outcomes import build_case_outcome

HEADER = """2023 RLLR 85

Citation: 2023 RLLR 85
Tribunal: Refugee Protection Division
Date of Decision: July 6, 2023
Panel: Osehise Odigie
Counsel for the Claimant(s): N/A
Country: Fiji
RPD Number: VC2-09277
Associated RPD Number(s): N/A
ATIP Number: A-2023-01721
ATIP Pages: N/A

DECISION

[1] MEMBER: This is the decision of the Refugee Protection Division in the claim of XXXX.
"""
FOOTNOTES = "\n1 Exhibit 2, Basis of Claim Form.\n2 Thirunavukkarasu v. Canada, [1994] 1 F.C. 589 (C.A.).\n"


def _text(body: str) -> str:
	return HEADER + body


def test_header_block_gives_date_panel_and_file_number():
	payload = extract_case_metadata(_text("[2] I find you are a Convention refugee and I accept your claim.\n"))
	assert payload["docket"] == "VC2-09277"
	assert payload["date"] == "July 6, 2023"
	assert payload["judge"] == "Osehise Odigie"
	assert payload["_needs_review"] is False


def test_accepted_claim_is_allowed_even_with_transcript_sign_off_and_footnotes():
	body = (
		"CONCLUSION\n[13] I find that you are a Convention refugee, and your claim is, therefore, accepted.\n"
		"[14] Thank you. This hearing is now concluded.\n\n——— REASONS CONCLUDED ———\n" + FOOTNOTES
	)
	outcome = build_case_outcome(_text(body), {})
	assert outcome["decision_outcome"] == "allowed"
	assert outcome["government_role"] is None


def test_footnotes_after_a_signature_do_not_hide_the_ruling():
	body = "[13] I accept both of your claims.\n(signed) MEMBER\nMarch 29, 2019\n" + FOOTNOTES
	assert build_case_outcome(_text(body), {})["decision_outcome"] == "allowed"


def test_rejected_claim_is_dismissed():
	body = "[20] I find that you are neither a Convention refugee nor a person in need of protection. Your claim is rejected.\n"
	assert build_case_outcome(_text(body), {})["decision_outcome"] == "dismissed"


def test_adults_accepted_and_minor_rejected_is_mixed():
	body = (
		"CONCLUSION\n[37] The adult claimants are Convention refugees. I accept their claims.\n"
		"[38] The child claimant is not a Convention refugee. Her claim is rejected.\n"
	)
	assert build_case_outcome(_text(body), {})["decision_outcome"] == "mixed"


def test_person_in_need_of_protection_instead_of_refugee_is_allowed():
	body = "[24] The claimant is not a Convention refugee under section 96, but is a person in need of protection under section 97(1)(b).\n"
	assert build_case_outcome(_text(body), {})["decision_outcome"] == "allowed"


def test_a_modal_reject_is_not_a_ruling():
	body = "[99] It would be inexcusable to reject their claim by hiding behind the IFA. I determine that the claimants are Convention refugees and the Board accepts their claims.\n"
	assert build_case_outcome(_text(body), {})["decision_outcome"] == "allowed"


def test_reporter_decisions_are_filed_under_rpd():
	from scripts.ingest_a2aj_parquet import build_case

	record = {
		"dataset": "RLLR", "citation_en": "2023 RLLR 85", "name_en": "", "document_date_en": "2023-07-06 00:00:00+00:00",
		"unofficial_text_en": _text("[2] I accept your claim."), "url_en": "https://refugeelab.ca/rllr/2023rllr85",
	}
	case = build_case(record)
	assert case.court == "RPD"
	assert case.citation == "2023 RLLR 85"
