import json

import pytest

from backend import outcome_checker as oc


def test_excerpt_drops_footnotes_and_counsel_trailer():
	text = "Refugee Appeal Division\n[1] a\n" * 3 + "[19] I dismiss the appeal.\n1 Footnote: appeal allowed in another case.\n"
	assert "Footnote" not in oc.select_excerpt(text)
	court = "[5] The application is dismissed.\nFEDERAL COURT\nSOLICITORS OF RECORD\nDOCKET: IMM-1-22\n"
	assert "DOCKET" not in oc.select_excerpt(court)


def test_excerpt_is_bounded_and_starts_on_a_line():
	text = "\n".join(f"[{n}] " + "word " * 40 for n in range(200)) + "\n[201] The appeal is allowed."
	excerpt = oc.select_excerpt(text)
	assert len(excerpt) <= oc.EXCERPT_CHARS
	assert excerpt.startswith("[") and excerpt.endswith("allowed.")


def test_answer_needs_a_quote_found_in_the_text():
	excerpt = "[9] For these reasons, the application for judicial review is dismissed."
	good = json.dumps({"outcome": "dismissed", "quote": "the application for judicial review is dismissed."})
	assert oc.parse_answer(good, excerpt)["valid"] is True
	invented = json.dumps({"outcome": "allowed", "quote": "The application is allowed."})
	result = oc.parse_answer(invented, excerpt)
	assert (result["outcome"], result["valid"], result["reason"]) == ("unclear", False, "quote_not_in_text")


def test_bad_json_and_bad_labels_become_unclear():
	assert oc.parse_answer("not json", "x")["reason"] == "bad_json"
	assert oc.parse_answer('{"outcome": "won", "quote": "x"}', "x")["reason"] == "bad_label"
	assert oc.parse_answer('{"outcome": "unclear", "quote": ""}', "x")["valid"] is True


def test_compare_flags_disagreement_without_overwriting():
	assert oc.compare("dismissed", "dismissed") == "agree"
	assert oc.compare("dismissed", "allowed") == "disagree"
	assert oc.compare("unclear", "allowed") == "checker_only"
	assert oc.compare("allowed", "unclear") == "rules_only"
	assert oc.compare("unclear", "unclear") == "both_unclear"
	assert oc.compare("granted", "allowed") == "agree"


def test_cost_arithmetic_and_hundred_thousand_token_check():
	assert oc.usage_cost(1_000_000, 0) == pytest.approx(oc.INPUT_COST_PER_MILLION)
	assert oc.usage_cost(0, 1_000_000) == pytest.approx(oc.OUTPUT_COST_PER_MILLION)
	assert oc.estimate_tokens("x" * 2800) > 700
