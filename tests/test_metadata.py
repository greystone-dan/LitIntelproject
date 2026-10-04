from hashlib import sha256
from types import SimpleNamespace

from backend.case_processing import _run_metadata_layer
from backend.metadata import extract_case_metadata, extract_metadata_matches, extract_metadata_observations
from backend.metadata_outcomes import build_case_outcome


class FakeSession:
	def __init__(self):
		self.added = []

	def add(self, value):
		self.added.append(value)


def test_extract_metadata_matches_returns_exact_canonical_spans():
	text = (
		"Court File No.: IMM-123-24\n"
		"Date: 2024-01-10\n"
		"Neutral Citation: 2024 FC 100\n"
		"Present: Justice Example\n"
		"Place of Hearing: Toronto, Ontario\n"
		"Date of Hearing: January 8, 2024\n"
	)

	matches = extract_metadata_matches(text)

	assert {match.field for match in matches} >= {
		"date",
		"docket",
		"neutral citation",
		"judge",
		"place of hearing",
		"date of hearing",
	}
	assert "place_of_hearing" not in {match.field for match in matches}
	assert all(text[match.offset_start:match.offset_end] == match.text for match in matches)
	assert all(match.confidence > 0 for match in matches)


def test_metadata_observations_derive_government_loss_when_minister_applicant_and_dismissed():
	text = (
		"Between:\n"
		"The Minister of Citizenship and Immigration Applicant\n"
		"and\n"
		"Jane Doe Respondent\n"
		"The application is dismissed.\n"
	)

	rows = extract_metadata_observations(text)
	by_field = {row.field: row for row in rows}

	assert by_field["decision outcome"].value == "dismissed"
	assert by_field["government role"].value == "applicant"
	assert by_field["government outcome"].value == "lost"
	assert by_field["government outcome"].span_matched is False


def test_metadata_observations_derive_government_win_when_individual_applicant_and_dismissed():
	text = (
		"Between:\n"
		"Jane Doe Applicant\n"
		"and\n"
		"The Minister of Citizenship and Immigration Respondent\n"
		"The application is dismissed.\n"
	)

	rows = extract_metadata_observations(text)
	by_field = {row.field: row for row in rows}

	assert by_field["decision outcome"].value == "dismissed"
	assert by_field["government role"].value == "respondent"
	assert by_field["government outcome"].value == "won"


def test_metadata_stage_persists_case_level_extraction_and_preserves_source_metadata():
	text = (
		"Between:\n"
		"The Minister of Citizenship and Immigration Applicant\n"
		"and\n"
		"Jane Doe Respondent\n"
		"The application is dismissed.\n"
	)
	case = SimpleNamespace(
		id=1,
		full_text=text,
		summary=None,
		full_text_hash=None,
		metadata_json={"source": "unit-test"},
	)
	session = FakeSession()

	changed = _run_metadata_layer(session, case)

	extracted = case.metadata_json["reader_extracted"]
	assert changed == 2
	assert case.metadata_json["source"] == "unit-test"
	assert extracted["decision outcome"] == "dismissed"
	assert extracted["government role"] == "applicant"
	assert extracted["government outcome"] == "lost"
	assert extracted["_field_sources"]["government outcome"] == {"derived": "lost"}
	assert case.full_text_hash == sha256(text.encode("utf-8")).hexdigest()
	assert session.added == [case]


def test_metadata_outcome_prefers_final_order_over_quoted_prior_decision():
	text = (
		'The Court discussed an earlier decision where the application was allowed.\n'
		'Some reasons and procedural history.\n'
		'ORDER\nThe application is dismissed.'
	)

	rows = extract_metadata_observations(text)
	by_field = {row.field: row for row in rows}

	assert by_field["decision outcome"].value == "dismissed"


def test_metadata_outcome_derives_individual_win_from_set_aside_and_remittal():
	text = (
		"Between:\n"
		"Jane Doe Applicant\n"
		"and\n"
		"The Minister of Citizenship and Immigration Respondent\n"
		"JUDGMENT\nThe decision is set aside and the matter is referred back.\n"
	)

	rows = extract_metadata_observations(text)
	by_field = {row.field: row for row in rows}

	assert by_field["decision outcome"].value == "remitted"
	assert by_field["government outcome"].value == "lost"


def test_metadata_outcome_exposes_winner_and_structured_evidence():
	text = (
		"Between:\n"
		"Jane Doe Applicant\n"
		"and\n"
		"The Minister of Citizenship and Immigration Respondent\n"
		"JUDGMENT\nThe application is dismissed."
	)

	payload = extract_case_metadata(text)

	assert payload["case winner"] == "respondent"
	assert payload["case loser"] == "applicant"
	assert payload["outcome status"] == "won"
	assert payload["outcome detail"]["disposition"] == "dismissed"
	evidence = payload["outcome detail"]["evidence"]
	assert text[evidence["offset_start"]:evidence["offset_end"]] == evidence["text"]


def test_metadata_outcome_marks_partial_relief_as_mixed():
	text = (
		"Between:\n"
		"Jane Doe Applicant\n"
		"and\n"
		"The Minister of Citizenship and Immigration Respondent\n"
		"ORDER\nThe application is allowed in part and dismissed in part."
	)

	payload = extract_case_metadata(text)

	assert payload["decision outcome"] == "mixed"
	assert payload["government outcome"] == "mixed"
	assert payload["case winner"] == "mixed"
	assert payload["outcome detail"]["status"] == "mixed"


def test_metadata_exposes_multiple_challenged_issues_without_replacing_legacy_issue():
	text = (
		"This application for judicial review challenges an RPD decision. "
		"The applicant alleges credibility and procedural fairness issues."
	)

	payload = extract_case_metadata(text)

	assert payload["case issue"] in {"credibility", "procedural_fairness"}
	assert payload["challenged issue"] == payload["case issue"]
	assert set(payload["challenged issues"].split(", ")) >= {"credibility", "procedural_fairness"}


def test_build_case_outcome_returns_dedicated_normalized_record():
	text = "Between:\nJane Doe Applicant\nand\nThe Minister Respondent\nORDER\nThe application is allowed."
	record = build_case_outcome(text, {})

	assert record["classifier_version"] == "deterministic_outcome_v2"
	assert record["decision_outcome"] == "allowed"
	assert record["outcome_status"] == "won"
	assert record["winner_side"] == "applicant"
	assert record["disposition_evidence"] == "application is allowed"
	assert record["evidence_offset_end"] > record["evidence_offset_start"]


def test_extract_case_metadata_derives_case_type_and_challenge_from_legal_signals():
	text = (
		"This application for judicial review challenges a Refugee Protection Division decision. "
		"The applicant alleges credibility and procedural fairness issues under sections 96 and "
		"97 of the IRPA and the Refugee Convention."
	)
	payload = extract_case_metadata(text)

	assert payload["case type"] == "judicial_review"
	assert payload["case challenge"] == "refugee_protection_decision"
	assert payload["case issue"] in {"credibility", "procedural_fairness", "refugee_protection"}
	assert "judicial_review" in payload["case topic"]


def test_extract_case_metadata_returns_empty_payload_for_empty_text():
	assert extract_case_metadata("  ") == {}


def test_judge_signature_block_captures_signature_name_not_court_label():
	text = (
		"Date: 20260123\n"
		"Docket: IMM-13884-24\n"
		"Citation: 2026 FC 103\n"
		"Ottawa, Ontario, January 23, 2026\n"
		"PRESENT: The Honourable Mr. Justice Zinn\n"
		"BETWEEN:\n"
		"OBINNA NWAOKONKO\n"
		"Applicant\n"
		"and\n"
		"THE MINISTER OF CITIZENSHIP AND IMMIGRATION\n"
		"Respondent\n"
		"JUDGMENT AND REASONS\n"
		"[1] The application is dismissed.\n"
		'"Russel W. Zinn"\n'
		"Judge\n"
		"FEDERAL COURT\n"
		"SOLICITORS OF RECORD\n"
	)

	payload = extract_case_metadata(text)

	assert payload["judge"] == "Russel W. Zinn"
	assert payload["_field_confidence"]["judge"] >= 0.9
	assert "invalid_shape:judge" not in payload["_quality_flags"]


def test_judge_court_name_capture_is_dropped_for_present_fallback():
	text = (
		"Date: 20260203\n"
		"Docket: IMM-999-25\n"
		"Citation: 2026 FC 200\n"
		"PRESENT: The Honourable Mr. Justice Brown\n"
		"BETWEEN:\n"
		"JANE DOE\n"
		"Applicant\n"
		"and\n"
		"THE MINISTER OF CITIZENSHIP AND IMMIGRATION\n"
		"Respondent\n"
		"JUDGMENT AND REASONS\n"
		"[1] The application is dismissed.\n"
		"Judge\n"
		"FEDERAL COURT\n"
		"SOLICITORS OF RECORD\n"
	)

	payload = extract_case_metadata(text)

	assert payload["judge"] == "Justice Brown"
	assert "invalid_shape:judge" not in payload["_quality_flags"]


def test_judge_honourable_name_without_title_token_is_normalized_and_valid():
	text = (
		"Date: 20060914\n"
		"Docket: IMM-123-05\n"
		"Citation: 2006 FC 1160\n"
		"PRESENT: The Honourable Paul U.C. Rouleau\n"
		"BETWEEN:\n"
		"FADILA KHARCHI\n"
		"Applicant\n"
		"and\n"
		"THE MINISTER OF CITIZENSHIP AND IMMIGRATION\n"
		"Respondent\n"
		"REASONS FOR JUDGMENT\n"
		"[1] The application is dismissed.\n"
	)

	payload = extract_case_metadata(text)

	assert payload["judge"] == "Paul U.C. Rouleau"
	assert payload["_field_confidence"]["judge"] >= 0.9
	assert "invalid_shape:judge" not in payload["_quality_flags"]


def test_judge_document_labels_and_locations_are_rejected():
	for label in ("Certified true translation", "Ottawa, Ontario"):
		text = (
			"Date: 20260203\n"
			"Docket: IMM-999-25\n"
			"Citation: 2026 FC 200\n"
			f"PRESENT: {label}\n"
			"BETWEEN:\n"
			"JANE DOE\n"
			"Applicant\n"
			"and\n"
			"THE MINISTER OF CITIZENSHIP AND IMMIGRATION\n"
			"Respondent\n"
			"JUDGMENT AND REASONS\n"
			"[1] The application is dismissed.\n"
		)

		payload = extract_case_metadata(text)

		assert payload.get("judge") is None


def test_judge_inline_coram_header_is_extracted():
	metadata = extract_case_metadata(
		"DATE OF DECISION January 3, 2006\nCORAM CORAM James V. Railton\nFOR THE CLAIMANT(S) Mary C. Tatham"
	)

	assert metadata["judge"] == "James V. Railton"


def test_judge_reasons_heading_is_extracted():
	metadata = extract_case_metadata(
		"REASONS FOR ORDER BLANCHARD J.\n[1] This is the order."
	)

	assert metadata["judge"] == "BLANCHARD J."


def test_style_of_cause_recovers_versus_form_from_between_when_capture_truncated():
	text = (
		"Date: 20060928\n"
		"Docket: IMM-5883-05\n"
		"Citation: 2006 FC 1154\n"
		"Ottawa, Ontario, September 28, 2006\n"
		"PRESENT: The Honourable Mr. Justice Phelan\n"
		"BETWEEN:\n"
		"OLGA VAKRUCHEV\n"
		"VITA VAKRUCHEV\n"
		"Applicants\n"
		"and\n"
		"THE MINISTER OF CITIZENSHIP\n"
		"AND IMMIGRATION\n"
		"Respondent\n"
		"REASONS FOR JUDGMENT AND JUDGMENT\n"
		"[1] The application is dismissed.\n"
		"STYLE OF CAUSE:\n"
		"OLGA VAKRUCHEV\n"
		"VITA VAKRUCHEV\n"
		"AND OTHERS\n"
	)

	payload = extract_case_metadata(text)

	assert payload["style of cause"] == "OLGA VAKRUCHEV VITA VAKRUCHEV v. THE MINISTER OF CITIZENSHIP AND IMMIGRATION"
	assert "invalid_shape:style of cause" not in payload["_quality_flags"]


def test_french_title_page_labels_reach_critical_confidence():
	text = (
		"Date\n"
		"2026-02-02\n"
		"Référence neutre\n"
		"2026 CF 148\n"
		"Numéro de dossier\n"
		"T-1012-24\n"
		"Contenu de la décision\n"
		"Date : 20260202\n"
		"Dossier : T-1012-24\n"
		"Référence : 2026 CF 148\n"
		"Ottawa (Ontario), le 2 février 2026\n"
		"En présence de monsieur le juge McHaffie\n"
		"ENTRE :\n"
		"MARIE DUPONT\n"
		"Demanderesse\n"
		"et\n"
		"LE MINISTRE DE LA CITOYENNETÉ ET DE L'IMMIGRATION\n"
		"Défendeur\n"
		"JUGEMENT ET MOTIFS\n"
		"[1] La demande est rejetée.\n"
	)

	payload = extract_case_metadata(text)

	assert payload["_field_confidence"]["date"] >= 0.9
	assert payload["_field_confidence"]["docket"] >= 0.9
	assert payload["_field_confidence"]["neutral citation"] >= 0.9


def test_french_dossier_space_colon_label_reaches_critical_confidence():
	text = (
		"Date\n"
		"2026-03-15\n"
		"Référence neutre\n"
		"2026 CF 220\n"
		"Numéro de dossier\n"
		"IMM-555-25\n"
		"Contenu de la décision\n"
		"Date : 20260315\n"
		"Dossier : IMM-555-25\n"
		"Référence : 2026 CF 220\n"
		"En présence de madame la juge Fothergill\n"
		"ENTRE :\n"
		"JEAN TREMBLAY\n"
		"Demandeur\n"
		"et\n"
		"LE MINISTRE DE LA CITOYENNETÉ ET DE L'IMMIGRATION\n"
		"Défendeur\n"
		"JUGEMENT ET MOTIFS\n"
		"[1] La demande est accueillie.\n"
	)

	payload = extract_case_metadata(text)

	assert payload["_field_confidence"]["docket"] >= 0.9


def test_french_reference_space_colon_label_reaches_critical_confidence():
	text = (
		"Date\n"
		"2026-04-20\n"
		"Référence neutre\n"
		"2026 CF 305\n"
		"Numéro de dossier\n"
		"T-777-25\n"
		"Contenu de la décision\n"
		"Date : 20260420\n"
		"Dossier : T-777-25\n"
		"Référence : 2026 CF 305\n"
		"En présence de monsieur le juge Roy\n"
		"ENTRE :\n"
		"FATIMA BENALI\n"
		"Demanderesse\n"
		"et\n"
		"LE MINISTRE DE LA CITOYENNETÉ ET DE L'IMMIGRATION\n"
		"Défendeur\n"
		"JUGEMENT ET MOTIFS\n"
		"[1] La demande est rejetée.\n"
	)

	payload = extract_case_metadata(text)

	assert payload["_field_confidence"]["neutral citation"] >= 0.9


def test_scc_numeric_docket_reaches_critical_confidence():
	text = (
		"Citation: 2008 SCC 48\n"
		"Docket: 31516\n"
		"Present: McLachlin C.J. and Bastarache, Binnie, LeBel, Deschamps, Fish and Abella JJ.\n"
		"BETWEEN:\n"
		"HER MAJESTY THE QUEEN\n"
		"Appellant\n"
		"and\n"
		"C.B.\n"
		"Respondent\n"
		"REASONS FOR JUDGMENT\n"
		"[1] The appeal is dismissed.\n"
	)

	payload = extract_case_metadata(text)

	assert payload["docket"] == "31516"
	assert payload["_field_confidence"]["docket"] >= 0.9
	assert "invalid_shape:docket" not in payload["_quality_flags"]


def test_fc_docket_shape_still_valid_after_numeric_acceptance():
	text = (
		"Date: 20260123\n"
		"Docket: IMM-13884-24\n"
		"Citation: 2026 FC 103\n"
		"PRESENT: The Honourable Mr. Justice Zinn\n"
		"BETWEEN:\n"
		"OBINNA NWAOKONKO\n"
		"Applicant\n"
		"and\n"
		"THE MINISTER OF CITIZENSHIP AND IMMIGRATION\n"
		"Respondent\n"
		"JUDGMENT AND REASONS\n"
		"[1] The application is dismissed.\n"
	)

	payload = extract_case_metadata(text)

	assert payload["docket"] == "IMM-13884-24"
	assert payload["_field_confidence"]["docket"] >= 0.9
	assert "invalid_shape:docket" not in payload["_quality_flags"]


def test_short_numeric_docket_fails_shape_validation():
	text = (
		"Date: 20260123\n"
		"Docket: 42\n"
		"Citation: 2026 FC 999\n"
		"PRESENT: The Honourable Mr. Justice Brown\n"
		"BETWEEN:\n"
		"JANE DOE\n"
		"Applicant\n"
		"and\n"
		"THE MINISTER OF CITIZENSHIP AND IMMIGRATION\n"
		"Respondent\n"
		"JUDGMENT AND REASONS\n"
		"[1] The application is dismissed.\n"
	)

	payload = extract_case_metadata(text)

	assert "invalid_shape:docket" in payload["_quality_flags"]
	assert payload["_field_confidence"]["docket"] < 0.9


def _disposition(text: str) -> str | None:
	return build_case_outcome(text, {})["decision_outcome"]


def test_outcome_judicial_review_allowed_with_remittal_stays_allowed():
	text = (
		"JUDGMENT\nTHIS COURT'S JUDGMENT is that:\n"
		"1. The application for judicial review is allowed.\n"
		"2. The decision is set aside and the matter is remitted to a different officer.\n"
		"3. There is no question to certify."
	)
	assert _disposition(text) == "allowed"


def test_outcome_main_ruling_beats_ancillary_leave_and_stay():
	text = (
		"JUDGMENT\n1. Leave is granted.\n2. The application for judicial review is dismissed.\n"
		"3. The motion for a stay is granted."
	)
	assert _disposition(text) == "dismissed"


def test_outcome_ignores_negated_and_conditional_cues():
	text = (
		"The applicant argues the application should not be allowed. If the appeal were allowed, "
		"the matter would be remitted.\nORDER\nTHIS COURT ORDERS that the application is dismissed."
	)
	assert _disposition(text) == "dismissed"


def test_outcome_allowed_in_part_is_mixed():
	assert _disposition("ORDER\nThe application is allowed in part.") == "mixed"


def test_outcome_actor_and_bare_verdict_forms():
	assert _disposition("Reasons.\nFor these reasons, the Court dismisses the application.") == "dismissed"
	assert _disposition("Reasons.\nORDER\n1. ALLOWED.") == "allowed"
	assert _disposition("Reasons.\nI would allow the appeal.") == "allowed"


def test_outcome_not_confused_by_in_order_to_text():
	text = "In order to decide, the Court notes the application is allowed only if x.\nORDER\nThe appeal is dismissed."
	assert _disposition(text) == "dismissed"


# --- Outcome audit regressions (2026-10-04) ---------------------------------------------------------
# Each case is a shortened real disposition pattern that the earlier rules got wrong.


def test_outcome_rad_dismisses_appeal_despite_set_aside_in_footnote_text():
	text = (
		"CONCLUSION\n[53] The RAD dismisses the appeal and confirms the decision of the RPD that the Appellants are "
		"neither Convention refugees nor persons in need of protection.\n"
		"1 Huruglica v. Canada, 2016 FCA 93; the decision was set aside on judicial review."
	)
	assert _disposition(text) == "dismissed"


def test_outcome_rpd_rejected_and_accepted_claims():
	header = "RPD File No. / N° de dossier de la SPR : TB2-05345\nReasons and Decision\n"
	assert _disposition(header + "[17] The panel finds that the claimant is neither a Convention refugee nor a person in need of protection. "
		"The Refugee Protection Division, therefore, rejects her claim.") == "dismissed"
	assert _disposition(header + "[21] For these reasons, the claim for refugee protection is rejected.") == "dismissed"
	assert _disposition(header + "[25] The panel determines that the claimant, XXXX, is not a \"Convention refugee\" "
		"nor a \"person in need of protection\".") == "dismissed"
	assert _disposition(header + "The panel determines that the claimant is a person in need of protection; "
		"consequently, his claim for refugee protection is accepted.") == "allowed"


def test_outcome_appeal_court_concluding_sentences_without_judgment_block():
	allowed = (
		"[32] The appeal should therefore be allowed, the order of the judge should be set aside, the application "
		"for judicial review should be dismissed and the decision of the officer restored."
	)
	assert _disposition(allowed) == "allowed"
	assert _disposition("[11] Accordingly, we will dismiss the appeal. Costs are fixed at $4,000.") == "dismissed"
	assert _disposition("[38] For these reasons, I would allow the appeal and set aside the decision.") == "allowed"
	assert _disposition("[28] I would grant the motion and dismiss the appeal for mootness.") == "dismissed"


def test_outcome_ignores_leave_to_appeal_in_subsequent_history_citations():
	text = (
		"The test is well settled (Doe v. Canada, [1996] 3 F.C. 83 (C.A.), leave to appeal refused, [1997] S.C.C.A. No. 1).\n"
		"[9] For these reasons, the appeal is allowed."
	)
	assert _disposition(text) == "allowed"
	assert _disposition("Reasons cite Roe v. Canada (2001), 1 Imm. L.R. 1; leave to appeal dismissed, [2002] 1 S.C.R. v.\n"
		"[9] The appeal will be dismissed.") == "dismissed"


def test_outcome_supreme_court_headline_beats_dissent_and_quoted_text():
	text = (
		"Held (Moldaver and Wagner JJ. dissenting in part): The appeal should be allowed.\n"
		"Appeal allowed with costs, Moldaver and Wagner JJ. dissenting in part.\n"
		"[200] In dissent: I would dismiss the appeal and affirm the Officer's decision.\n"
		"Solicitors for the appellant: Counsel, Toronto."
	)
	assert _disposition(text) == "allowed"
	assert build_case_outcome(text, {})["decision_outcome"] == "allowed"  # not "mixed": the "in part" is the dissent


def test_government_role_follows_style_of_cause_for_minister_appeals():
	text = (
		"Appellant\nand\nAlexander Vavilov\nRespondent\nHeld: The appeal should be dismissed.\n"
		"Appeal dismissed with costs throughout.\nSolicitors for the appellant: Attorney General of Canada, Ottawa."
	)
	record = build_case_outcome(text, {"style of cause": "Minister of Citizenship and Immigration v. Alexander Vavilov"})
	assert record["decision_outcome"] == "dismissed"
	assert record["government_role"] == "applicant"
	assert record["government_outcome"] == "lost"
	record = build_case_outcome(text, {"style of cause": "Alexander Vavilov v. Minister of Citizenship and Immigration"})
	assert record["government_role"] == "respondent"
	assert record["government_outcome"] == "won"


def test_government_role_ignores_counsel_for_the_minister_caption_line():
	text = (
		"RAD File No. : MB9-02333\nPerson who is the subject of the appeal\nXXXX\nAppellant\n"
		"Counsel for the Minister\nN/A\nREASONS FOR DECISION\n[18] I dismiss the appeal and confirm the RPD's determination."
	)
	record = build_case_outcome(text, {})
	assert record["decision_outcome"] == "dismissed"
	assert record["government_role"] is None


def test_outcome_abstains_instead_of_guessing():
	assert _disposition("Some reasons that never state a ruling. The officer considered the file.") == "unclear"
	# Only a weak consequence cue outside any operative block: say nothing rather than guess.
	assert _disposition("The matter was discussed at length. The earlier order was set aside last year in another case.") == "unclear"


def test_outcome_procedural_orders_are_not_merits_outcomes():
	assert _disposition("Foo v. Canada\nJUDGMENT\nTHIS COURT ORDERS that the motion for an extension of time is granted.") == "procedural"
	assert _disposition("STYLE OF CAUSE\nMOTION DEALT WITH IN WRITING WITHOUT APPEARANCE OF PARTIES\n[6] I would therefore dismiss the appeal.") == "procedural"


def test_outcome_appendix_statutes_and_footnotes_do_not_decide():
	statute = "\nAppeal allowed\nFondement de l'appel\n67 (1) To allow an appeal, the Division must be satisfied that\n"
	assert _disposition("[33] For these reasons, I would dismiss the appeal without costs." + statute * 2 + "x" * 9000) == "dismissed"
	rad = (
		"Refugee Appeal Division\n[19] Pursuant to section 111(1)(a), I dismiss the appeal and confirm the decision of the RPD.\n"
		"1 Statistics on the number of applications for relocation that are granted and refused.\n"
	)
	assert _disposition(rad) == "dismissed"


def test_outcome_judgment_the_lower_court_should_have_given_follows_the_ruling():
	text = (
		"[31] For these reasons, I would allow the appeal and set aside the judgment of the Federal Court. "
		"Pronouncing the judgment that the Federal Court ought to have pronounced, I would dismiss the application for judicial review."
	)
	assert _disposition(text) == "allowed"


def test_outcome_rpd_positive_and_exclusion_findings():
	assert _disposition("Refugee Protection Division\n[9] The panel determines that A and B are Convention refugees as defined in IRPA, section 96 and accepts their claims.") == "allowed"
	assert _disposition("Refugee Protection Division\n[32] Accordingly, this claimant is excludable under article 1F(b) of the Refugee Convention.") == "dismissed"


def test_outcome_rad_panel_is_the_rpd_not_the_decision_maker():
	text = (
		"Refugee Appeal Division\n[22] The panel dismisses just about everything the claimant said. The RAD finds this wrong.\n"
		"[34] Pursuant to Section 111(1)(b) of the IRPA, the RAD sets aside the determination of the RPD and substitutes its own. The appeal is allowed."
	)
	assert _disposition(text) == "allowed"
