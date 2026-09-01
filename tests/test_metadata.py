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