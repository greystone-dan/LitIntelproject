"""Regression tests from the 2026-10-17 grading of the v2 outcome dry run (docs: outcomes/outcome_v2_grading_2026-10-17.md).

The fixture rows are the last 1,500 characters of real FC/FCA/SCC decisions, graded by a model reader (not a lawyer).
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from backend.metadata_outcomes import build_case_outcome

_ROWS = json.loads((Path(__file__).parent / "fixtures" / "outcome_v2_graded_rows.json").read_text(encoding="utf-8"))
_FAMILY = {
	"allowed": "A", "granted": "A", "set_aside": "A", "remitted": "A",
	"dismissed": "D", "mixed": "M", "procedural": "P", "unclear": "U",
}


@pytest.mark.parametrize("row", _ROWS, ids=lambda row: f"{row['kind']}-{row['citation']}")
def test_graded_row(row):
	outcome = build_case_outcome(row["text"], {})
	assert _FAMILY[outcome["decision_outcome"]] == _FAMILY[row["gold_disposition"]]
	if outcome["winner_side"] in {"applicant", "respondent"} and row["gold_winner"] in {"applicant", "respondent"}:
		assert outcome["winner_side"] == row["gold_winner"]


def test_appeal_allowed_then_application_dismissed_is_an_allowed_appeal():
	text = (
		"[20] Accordingly, I would allow the appeal with costs, and set aside the decision of the Tribunal. "
		"Proceeding to render the decision that should have been rendered, I would dismiss the respondents' appeals with costs.\n"
	)
	assert build_case_outcome(text, {})["decision_outcome"] == "allowed"


def test_motion_headline_is_procedural():
	outcome = build_case_outcome("Reasons.\nMotion granted, Major J. dissenting.\nSolicitors for the appellant: X, Ottawa.", {})
	assert outcome["decision_outcome"] == "procedural"
	assert outcome["winner_side"] is None


def test_split_headline_in_different_appeals_is_mixed():
	outcome = build_case_outcome("Reasons.\nAppeal dismissed in Orbanski. Appeal allowed in Elias with costs, LeBel J. dissenting.\n", {})
	assert outcome["decision_outcome"] == "mixed"


def test_appeal_and_cross_appeal_allowed_dismissed_stays_allowed():
	assert build_case_outcome("Reasons.\nAppeal allowed and cross-appeal dismissed.\nSolicitors for the appellant: X.", {})["decision_outcome"] == "allowed"


def test_dismiss_all_other_aspects_is_mixed():
	text = "I would allow the application in respect of the first issue and dismiss all other aspects of the application.\n"
	assert build_case_outcome(text, {})["decision_outcome"] == "mixed"


def test_crown_appellant_in_solicitor_block_sets_government_role():
	text = (
		"Appeal allowed.\nSolicitor for the appellant: Attorney General of Ontario, Toronto. "
		"Solicitors for the respondents: Wilton & Associate, Toronto.\n"
	)
	outcome = build_case_outcome(text, {"style of cause": "R.D. v. Ontario"})
	assert outcome["government_role"] == "applicant"
	assert outcome["government_outcome"] == "won"


def test_crown_respondent_and_appellant_on_same_line():
	text = "Appeal dismissed with costs.\nSolicitors for the appellant: Nelligan & Power, Ottawa. Solicitor for the respondent: The Attorney General of Canada, Ottawa.\n"
	assert build_case_outcome(text, {})["government_role"] == "respondent"
