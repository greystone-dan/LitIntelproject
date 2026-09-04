from types import SimpleNamespace

from scripts.benchmark_case_citations import citation_metrics, is_exact_span_valid


def test_exact_span_validation_requires_exact_offsets_and_text():
	text = "See 2019 SCC 65 here."
	match = SimpleNamespace(citation_text="2019 SCC 65", offset_start=4, offset_end=15)
	invalid = SimpleNamespace(citation_text="2019 SCC 66", offset_start=4, offset_end=15)

	assert is_exact_span_valid(text, match)
	assert not is_exact_span_valid(text, invalid)


def test_metrics_use_case_layer_matches_without_statute_leakage():
	text = "Vavilov v. Canada, 2019 SCC 65 applied IRPA s. 34(1)(f)."
	case = SimpleNamespace(
		title="Other v. Canada",
		citation="2024 FC 10",
		secondary_citation=None,
	)
	case_match = SimpleNamespace(
		kind="case",
		citation_text="Vavilov v. Canada, 2019 SCC 65",
		normalized_citation="Vavilov v. Canada, 2019 SCC 65",
		offset_start=0,
		offset_end=len("Vavilov v. Canada, 2019 SCC 65"),
	)

	metrics = citation_metrics(case, text, [case_match])

	assert metrics["extracted_citations"] == 1
	assert metrics["exact_span_valid_count"] == 1
	assert metrics["invalid_span_count"] == 0
	assert metrics["pinpoint_available_count"] == 0
	assert metrics["resolution_status"] == "not_measured"