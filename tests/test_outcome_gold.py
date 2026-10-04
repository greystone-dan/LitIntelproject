"""Regression guard: the outcome reader against hand-read decisions.

tests/fixtures/outcome_gold.json.gz holds 587 decisions (FC, FCA, SCC, RAD, RPD) whose outcome was read by hand from the
ruling itself: A = allowed/granted, D = dismissed/rejected, M = mixed, P = procedural order. Each entry has the citation,
the (trimmed) decision text and, where the reader agrees with the hand label, the quoted disposition sentence. The set
includes the landmark and tricky patterns found in the outcome audit. It was used while tuning the rules, so treat it as
a regression floor, not as a fresh accuracy measure.
"""
import gzip
import json
from pathlib import Path

import pytest

from backend.metadata_outcomes import build_case_outcome

FIXTURE = Path(__file__).parent / "fixtures" / "outcome_gold.json.gz"
_CLASS = {
	"allowed": "A", "granted": "A", "set_aside": "A", "remitted": "A",
	"dismissed": "D", "mixed": "M", "procedural": "P", "unclear": "?",
}


@pytest.fixture(scope="module")
def results():
	with gzip.open(FIXTURE, "rt", encoding="utf-8") as handle:
		gold = json.load(handle)
	rows = []
	for case in gold:
		outcome = build_case_outcome(case["text"], {})
		rows.append((case, _CLASS.get(outcome["decision_outcome"], "?")))
	return rows


def test_gold_set_is_large_and_covers_every_court(results):
	assert len(results) >= 580
	assert {case["court"] for case, _ in results} == {"FC", "FCA", "SCC", "RAD", "RPD"}


def test_asserted_outcomes_are_almost_never_wrong(results):
	asserted = [(case, pred) for case, pred in results if pred != "?"]
	wrong = [(case["id"], case["citation"], case["truth"], pred) for case, pred in asserted if pred != case["truth"]]
	assert len(wrong) <= 1, wrong
	assert len(asserted) - len(wrong) >= 0.995 * len(asserted)


def test_the_reader_still_answers_most_cases(results):
	decided = [(case, pred) for case, pred in results if case["truth"] in {"A", "D"}]
	abstained = [case["id"] for case, pred in decided if pred == "?"]
	assert len(abstained) <= 0.02 * len(decided), abstained
