from hashlib import sha256
from types import SimpleNamespace

from backend.case_processing import _run_metadata_layer
from backend.metadata import extract_case_metadata, extract_metadata_matches, extract_metadata_observations


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
