"""Which paragraphs report a party's argument (no AI).

Runs the fixed position rules (``backend/position_holder.py``) over the whole decision and keeps the paragraphs
whose main voice is the applicant's or the respondent's, so a discussion unit can point at the party arguments
inside it. The unit boundaries are not changed: party-position changes were tested as a boundary signal and did
not help. On hand-read paragraphs about 6 in 10 of the flagged ones really were a party's argument, and some
party arguments are not flagged, so callers must label this as experimental.
"""

from __future__ import annotations

from typing import Sequence

from ..position_holder import tag_decision

PARTY_VOICES = ("applicant", "respondent")


def party_argument_voices(paragraphs: Sequence[str], title: str = "") -> dict[int, str]:
	"""Position in ``paragraphs`` -> 'applicant' or 'respondent' for each paragraph whose main voice is a party."""
	if not paragraphs:
		return {}
	results = tag_decision(list(paragraphs), title)
	return {index: result.primary for index, result in enumerate(results) if result.primary in PARTY_VOICES}
