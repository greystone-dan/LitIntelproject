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


def _best_match(text: str, others: Sequence[Mapping], similarity, threshold: float) -> tuple[int, float] | None:
	best = None
	for i, o in enumerate(others):
		score = similarity(text, str(o.get("text") or ""))
		if score >= threshold and (best is None or score > best[1]):
			best = (i, score)
	return best


def adopt_full_text_sides(full_text: Sequence[Mapping], notes: Sequence[Mapping], similarity, threshold: float = 0.8) -> list[dict]:
	"""Notes-only arguments that restate a full-text argument take that argument's side label.

	The full-text list sees the whole decision and its labels were right in all 191 true arguments of a held-out set; the notes
	list labelled 81% of the matching ones right, 95% after this. ``similarity(a, b)`` gives 0-1 (an embedding cosine in the
	tests). Notes arguments with no match keep their label and are marked ``side_adopted: False``.
	"""
	out = []
	for n in notes:
		hit = _best_match(str(n.get("text") or ""), full_text, similarity, threshold)
		if hit is None:
			out.append({**n, "side_adopted": False})
		else:
			out.append({**n, "side": full_text[hit[0]].get("side"), "side_adopted": True})
	return out


def count_votes(argument: Mapping, repeat_runs: Sequence[Sequence[Mapping]], similarity, threshold: float = 0.8) -> int:
	"""How many independent extra full-text reads contain a matching argument."""
	text = str(argument.get("text") or "")
	return sum(1 for run in repeat_runs if _best_match(text, run, similarity, threshold) is not None)


def merge_by_votes(full_text: Sequence[Mapping], notes: Sequence[Mapping], repeat_runs: Sequence[Sequence[Mapping]], similarity, threshold: float = 0.8, min_votes: int = 1) -> list[dict]:
	"""Every full-text argument, plus the notes-only arguments at least ``min_votes`` extra reads also found.

	Held-out (90 decisions, two sets): 93-95% right and 89-93% of true arguments found, against 90-93% right for keeping both lists
	unchecked and 96% right but only 81-88% found for the full-text list alone. Notes arguments get the full-text side label when
	they match one (``adopt_full_text_sides``).
	"""
	out = [{**a, "src": "full_text", "votes": count_votes(a, repeat_runs, similarity, threshold)} for a in full_text]
	for n in adopt_full_text_sides(full_text, notes, similarity, threshold):
		votes = count_votes(n, repeat_runs, similarity, threshold)
		if votes >= min_votes:
			out.append({**n, "src": "notes", "votes": votes})
	return out
