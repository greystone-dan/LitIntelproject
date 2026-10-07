"""Refugee Appeal Division (RAD) cover page, outcome and government-role rules, checked on full-length RAD layouts."""
from backend.metadata import _rad_header_fields, extract_case_metadata
from backend.metadata_outcomes import build_case_outcome

COVER_LABEL_BEFORE_VALUE = """
Immigration and
Refugee Board of Canada
Refugee Appeal Division
RAD File No. / No de dossier de la SAR : MB5-00902
MB5-00904
Private Proceeding / Huis clos
Reasons and Decision - Motifs et décision
Appeal considered at
Montréal, Quebec
Appel instruit à
Date of decision
September 17, 2015
Date de la décision
Panel
Me Normand Leduc
Tribunal
Counsel for the Minister
N/A
"""

COVER_VALUE_BEFORE_LABEL = """
N° de dossier de la SAR/RAD File No.: MB3-03199
Huis clos/Private Proceeding
Appel instruit à
Montréal, Québec
Appeal considered at
Date de la décision
January 6, 2014
Date of Decision
Tribunal
Stephen J. Gallagher
Panel
"""


def _decision(cover: str, body: str) -> str:
	return cover + "\nREASONS FOR DECISION\n" + body


def test_rad_cover_label_before_value():
	assert _rad_header_fields(COVER_LABEL_BEFORE_VALUE) == {
		"docket": "MB5-00902",
		"date": "September 17, 2015",
		"place of hearing": "Montréal, Quebec",
		"judge": "Normand Leduc",
	}


def test_rad_cover_value_before_label():
	assert _rad_header_fields(COVER_VALUE_BEFORE_LABEL) == {
		"docket": "MB3-03199",
		"date": "January 6, 2014",
		"place of hearing": "Montréal, Québec",
		"judge": "Stephen J. Gallagher",
	}


def test_court_judgment_that_mentions_the_rad_is_left_alone():
	text = "Federal Court\nJudgment\nReview of a Refugee Appeal Division decision\nPanel\nJohn Smith\n"
	assert _rad_header_fields(text) == {}


def test_rad_cover_fields_clear_review_flags():
	payload = extract_case_metadata(_decision(COVER_LABEL_BEFORE_VALUE, "[1] I dismiss the appeal and confirm the decision of the RPD."))
	assert payload["docket"] == "MB5-00902"
	assert payload["date"] == "September 17, 2015"
	assert payload["_needs_review"] is False
	assert not [flag for flag in payload["_quality_flags"] if flag.startswith("missing_critical")]


def test_confirmed_decision_is_dismissed_even_with_a_reopen_application_in_the_annex():
	body = (
		"INTRODUCTION\n[1] The Appellant applied to reopen an earlier appeal.\nCONCLUSION\n"
		"[177] Pursuant to paragraph 111(1)(a) of the IRPA, I confirm the decision of the RPD. The appeal is denied.\n"
		"(signed) Member\nANNEX 1: PROCEDURAL HISTORY\n[1] Application to Reopen allowed, extension of time granted.\n"
	)
	assert build_case_outcome(_decision(COVER_LABEL_BEFORE_VALUE, body), {})["decision_outcome"] == "dismissed"


def test_set_aside_and_substitute_is_allowed():
	body = "REMEDY\n[27] For these reasons, I set aside the determination of the RPD and substitute a determination that the appellant is a Convention refugee."
	assert build_case_outcome(_decision(COVER_LABEL_BEFORE_VALUE, body), {})["decision_outcome"] == "allowed"


def test_referral_is_allowed_even_when_the_rpd_finding_is_quoted():
	body = (
		"[3] The RPD found that the claimant is neither a Convention refugee nor a person in need of protection.\n"
		"CONCLUSION\n[14] Pursuant to Section 111(1)(c) of the IRPA, the Refugee Appeal Division refers the matter to the "
		"Refugee Protection Division for re-determination by a differently-constituted panel."
	)
	assert build_case_outcome(_decision(COVER_LABEL_BEFORE_VALUE, body), {})["decision_outcome"] == "allowed"


def test_different_results_for_different_appellants_are_mixed():
	body = (
		"CONCLUSION\n[24] I confirm the determination of the RPD for the principal appellant. Her appeal is dismissed.\n"
		"[25] However, I set aside the determination of the RPD and substitute the determination that the minor appellants are persons in need of protection."
	)
	assert build_case_outcome(_decision(COVER_LABEL_BEFORE_VALUE, body), {})["decision_outcome"] == "mixed"


def test_recited_section_111_options_are_not_a_ruling():
	body = (
		"REMEDY\n[53] Section 111(1) of IRPA allows the RAD to: (a) confirm the determination of the RPD; (b) set aside a decision "
		"of the RPD and substitute a determination that should have been made; (c) refer the matter back to the RPD.\n"
		"[54] I allow the appeal. I set aside the determination of the RPD and substitute my own decision that the appellant is a Convention refugee."
	)
	assert build_case_outcome(_decision(COVER_LABEL_BEFORE_VALUE, body), {})["decision_outcome"] == "allowed"


def test_dismissal_for_failure_to_perfect_stays_dismissed():
	body = (
		"[1] No Appellant's Record or application for an extension of time has been received.\n"
		"[2] The appeal is dismissed because the Appellant failed to perfect the appeal within the time limit."
	)
	assert build_case_outcome(_decision(COVER_LABEL_BEFORE_VALUE, body), {})["decision_outcome"] == "dismissed"


def test_extension_of_time_decision_alone_is_procedural():
	body = "[11] For reasons of procedural fairness, the application for an extension of time is allowed, and the appeal record is accepted."
	assert build_case_outcome(_decision(COVER_LABEL_BEFORE_VALUE, body), {})["decision_outcome"] == "procedural"


def test_claimant_appeal_has_no_government_side():
	body = "CONCLUSION\n[30] I dismiss the appeal and confirm the decision of the RPD that the Appellant is neither a Convention refugee nor a person in need of protection."
	outcome = build_case_outcome(_decision(COVER_LABEL_BEFORE_VALUE, body), {})
	assert outcome["decision_outcome"] == "dismissed"
	assert outcome["government_role"] is None
	assert outcome["government_outcome"] is None


def test_ministers_appeal_allowed_means_the_government_won():
	body = (
		"[1] The Minister's appeal is from the RPD decision that the Respondent is a Convention refugee.\n"
		"CONCLUSION\n[49] The Minister's appeal is allowed. I set aside the determination of the RPD and substitute my own decision that the "
		"Respondent is neither a Convention refugee nor a person in need of protection."
	)
	outcome = build_case_outcome(_decision(COVER_LABEL_BEFORE_VALUE, body), {})
	assert outcome["decision_outcome"] == "allowed"
	assert outcome["government_role"] == "applicant"
	assert outcome["government_outcome"] == "won"


def test_ministers_appeal_dismissed_means_the_government_lost():
	body = "[1] These are my reasons for dismissing the Minister's appeal.\nCONCLUSION\n[47] I dismiss the Minister's appeal. The RPD was correct."
	outcome = build_case_outcome(_decision(COVER_LABEL_BEFORE_VALUE, body), {})
	assert outcome["decision_outcome"] == "dismissed"
	assert outcome["government_outcome"] == "lost"
