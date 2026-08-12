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


def test_extract_case_metadata_returns_empty_payload_for_empty_text():
	assert extract_case_metadata("  ") == {}