from backend.metadata import extract_metadata_matches


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