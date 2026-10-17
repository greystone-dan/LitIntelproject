"""Free check for wrongly listed arguments, and the side-label fix for appeals brought by the Minister.

An argument list says which side made each argument and cites a paragraph. This module scores how well the cited
paragraph (plus one on each side) reads like that side being reported as making a point. Regular expressions
only: no model, no network, no database. Off unless ILIT_ARGUMENT_CHECKER is set; nothing in the site calls it.

In an appeal the "applicant" is the appellant, who can be the Minister. The party words that go with each label
must then be swapped (``applicant_is_minister == "yes"``), otherwise every argument in such a decision scores as
if it were on the wrong side. ``normalise_side`` gives the role-based label used for that.
"""

from __future__ import annotations

import os
import re
from typing import Mapping, Sequence

CHECKER_VERSION = "arg_checker_v1"

_VERBS = (r"(?:submits?|submitted|argues?|argued|contends?|contended|says?|said|alleges?|alleged|claims?|claimed|maintains?|"
	r"asserts?|asserted|take the position|position is|according to|counsel for|states|stated|points? out|pointed out|"
	r"suggests?|relies|relied|objects?)")
_INDIVIDUAL = (r"\b(?:applicants?|appellants?|claimants?|plaintiff|he|she|they|counsel for the applicant|his counsel|her counsel)")
_MINISTER = (r"\b(?:respondents?|minister|attorney general|crown|the government|counsel for the respondent)")
_MINISTER_APPELLANT_INDIVIDUAL = (r"\b(?:respondents?|claimants?|he|she|they|counsel for the respondent|his counsel|her counsel)")
_MINISTER_APPELLANT_MINISTER = (r"\b(?:applicants?|appellants?|minister|attorney general|crown|the government|counsel for the applicant)")


def enabled() -> bool:
	return os.environ.get("ILIT_ARGUMENT_CHECKER", "").strip().lower() in ("1", "true", "yes", "on")


def normalise_side(side: str, applicant_is_minister: str | None) -> str:
	"""Role-based label: ``minister`` or ``individual`` (``other`` for an intervener or unknown side)."""
	s = (side or "").lower()
	if s not in ("applicant", "respondent"):
		return "other"
	minister_side = (s == "respondent") != (applicant_is_minister == "yes")
	return "minister" if minister_side else "individual"


def _party_patterns(side: str, applicant_is_minister: str | None) -> tuple[str, str]:
	"""(own side's words, other side's words) for the given label."""
	role = normalise_side(side, applicant_is_minister)
	if role == "other":
		return _INDIVIDUAL, _MINISTER
	if applicant_is_minister == "yes":
		return ((_MINISTER_APPELLANT_MINISTER, _MINISTER_APPELLANT_INDIVIDUAL) if role == "minister"
			else (_MINISTER_APPELLANT_INDIVIDUAL, _MINISTER_APPELLANT_MINISTER))
	return (_MINISTER, _INDIVIDUAL) if role == "minister" else (_INDIVIDUAL, _MINISTER)


def own_side_reporting(side: str, para: int, paragraphs: Mapping[int, str], applicant_is_minister: str | None = None) -> int:
	"""How many times the cited paragraph and its neighbours show this side's words close to a reporting verb."""
	own, _ = _party_patterns(side, applicant_is_minister)
	text = " ".join(paragraphs.get(k, "") for k in (para - 1, para, para + 1)).lower()
	return len(re.findall(own + r"[^.]{0,80}" + _VERBS, text)) + len(re.findall(_VERBS + r"[^.]{0,40}" + own, text))


def score_arguments(arguments: Sequence[Mapping], paragraphs: Mapping[int, str], applicant_is_minister: str | None = None) -> list[dict]:
	"""Score each argument (keys ``side``, ``para``); higher means the cited paragraph supports it more."""
	out = []
	for a in arguments:
		para = int(a.get("para") or 0)
		own = own_side_reporting(str(a.get("side") or ""), para, paragraphs, applicant_is_minister) if para else 0
		out.append({**a, "side_role": normalise_side(str(a.get("side") or ""), applicant_is_minister), "own_side_reporting": own,
			"checker": CHECKER_VERSION})
	return out


def flag_lowest(scored: Sequence[Mapping], share: float = 0.2) -> list[dict]:
	"""Mark the lowest ``share`` of arguments as ``flagged`` (kept, not removed). Ties at the cut are not flagged."""
	if not scored:
		return []
	ordered = sorted(m["own_side_reporting"] for m in scored)
	cut = ordered[int(len(ordered) * share)]
	return [{**m, "flagged": m["own_side_reporting"] < cut} for m in scored]
