"""Outcome and government-role derivation for case metadata.

These helpers inspect the operative tail of a decision (ORDER / JUDGMENT /
DISPOSITION blocks) to label the decision outcome, then combine the caption
parties with that outcome to derive the government role and result. They are
imported by `backend.metadata`; nothing else should depend on them.
"""

from __future__ import annotations

import re

OUTCOME_CLASSIFIER_VERSION = "deterministic_outcome_v2"
_GOVERNMENT_PARTY_RE = re.compile(
	r"\b(?:minister|attorney\s+general|public\s+safety|citizenship\s+and\s+immigration|canada\s+border\s+services\s+agency|\bcbsa\b|\bircc\b|government\s+of\s+canada)\b",
	re.IGNORECASE,
)

_OUTCOME_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
	(
		"dismissed",
		re.compile(
			r"\b(?:application|appeal|judicial\s+review|motion|proceeding|claim|complaint|action)\b[^\n\.]{0,140}\b(?:is|are|be|hereby)?\s*(?:dismissed|denied|refused)\b",
			re.IGNORECASE,
		),
	),
	(
		"allowed",
		re.compile(
			r"\b(?:application|appeal|judicial\s+review|motion|proceeding|claim|complaint|action)\b[^\n\.]{0,140}\b(?:is|are|be|hereby)?\s*(?:allowed|granted)\b",
			re.IGNORECASE,
		),
	),
	(
		"granted",
		re.compile(
			r"\b(?:application|appeal|judicial\s+review|motion|proceeding|claim|complaint|action)\b[^\n\.]{0,140}\b(?:is|are|be|hereby)?\s*granted\b",
			re.IGNORECASE,
		),
	),
	(
		"set_aside",
		re.compile(r"\b(?:is|are|be|hereby)?\s*(?:set aside|quashed|annulled|vacated)\b", re.IGNORECASE),
	),
	(
		"remitted",
		re.compile(r"\b(?:is|are|be|hereby)?\s*(?:remitted|referred back|sent back)\b", re.IGNORECASE),
	),
)


_TAIL_CHARS = 12000
_MARKER_RE = re.compile(
	r"\b(?:ORDERS?|JUDGMENT|DISPOSITION|CONCLUSION)\b|^[ \t]*(?:Order|Judgment|Disposition|Conclusion)\b",
	re.MULTILINE,
)
_SUBJECT = (
	r"(?:application|appeal|cross-appeal|judicial\s+review|petition|proceeding|claim|complaint|action|"
	r"request|motion|stay|leave(?:\s+to\s+\w+)?)"
)
_DISMISS_WORDS = r"(?:dismissed|denied|refused|rejected)"
_ALLOW_WORDS = r"(?:allowed|granted|upheld)"
_SUBJECT_VERB_RE = re.compile(
	rf"\b(?P<subject>{_SUBJECT})\b(?P<span>[^\n\.;]{{0,140}}?)\b(?P<verb>{_DISMISS_WORDS}|{_ALLOW_WORDS}|withdrawn|discontinued)\b",
	re.IGNORECASE,
)
_ACTOR_VERB_RE = re.compile(
	r"\b(?P<actor>court|tribunal|panel|I\s+would|we\s+would|I\s+hereby)\s+(?:hereby\s+)?"
	r"(?P<verb>allows?|dismisses|dismiss|grants?|denies|deny|refuses|refuse)\b(?P<object>[^\n\.;]{0,100})",
	re.IGNORECASE,
)
_BARE_VERDICT_RE = re.compile(
	r"^[ \t]*(?:\d+\.[ \t]*)?(?:the[ \t]+)?(?:(?:appeal|application|motion)[ \t]+)?"
	r"(?P<verb>dismissed|allowed|granted|denied)\b[ \t]*\.?[ \t]*$",
	re.IGNORECASE | re.MULTILINE,
)
_CONSEQUENCE_RE = re.compile(
	r"\b(?:set aside|quashed|annulled|vacated|remitted|referred back|sent back)\b", re.IGNORECASE
)
_NEGATION_BEFORE_VERB_RE = re.compile(
	r"(?:\bnot\b|n't|\bcannot\b|\bnever\b|\bunless\b|\bif\b|\bwhether\b|\bshould\b|\bwould\b|\bmust\b)"
	r"\s*(?:[\w-]+\s+){0,2}$",
	re.IGNORECASE,
)
_PARTIAL_RE = re.compile(r"\b(?:in\s+part|partly|partially)\b", re.IGNORECASE)
_SIDE_ORDER_RE = re.compile(r"\b(?:leave|stay|extension|motion|request)\b", re.IGNORECASE)
_VERB_LABELS = {
	"allowed": "allowed", "allow": "allowed", "allows": "allowed", "upheld": "allowed",
	"granted": "granted", "grant": "granted", "grants": "granted",
	"dismissed": "dismissed", "dismiss": "dismissed", "dismisses": "dismissed",
	"denied": "dismissed", "deny": "dismissed", "denies": "dismissed",
	"refused": "dismissed", "refuse": "dismissed", "refuses": "dismissed", "rejected": "dismissed",
	"withdrawn": "withdrawn", "discontinued": "withdrawn",
}


def _sentence_bounds(text: str, start: int, end: int) -> tuple[int, int]:
	"""Expand [start, end) to the enclosing sentence/list item."""
	left = max(text.rfind("\n", 0, start), text.rfind(". ", 0, start))
	right_candidates = [i for i in (text.find("\n", end), text.find(". ", end)) if i != -1]
	right = min(right_candidates) + 1 if right_candidates else len(text)
	return left + 1, right


def _disposition_candidates(tail: str) -> list[tuple[int, int, str, re.Match[str]]]:
	"""Every disposition cue in `tail` as (rank, start, label, match).

	Rank 3 is a ruling on the proceeding itself, 2 is a consequence of it (set
	aside / remitted), 1 is an ancillary ruling (leave, stay, motion) or a
	"would" opinion. Negated or conditional cues are dropped.
	"""
	found: list[tuple[int, int, str, re.Match[str]]] = []
	for match in _SUBJECT_VERB_RE.finditer(tail):
		prefix = tail[match.start("span") : match.start("verb")]
		if _NEGATION_BEFORE_VERB_RE.search(prefix):
			continue
		label = _VERB_LABELS[match.group("verb").lower()]
		subject = match.group("subject").lower()
		side = subject.startswith(("leave", "stay", "motion", "request"))
		rank = 1 if side and label in {"allowed", "granted"} else 3 if not side or label == "dismissed" else 1
		if subject.startswith(("motion", "request", "stay")) and label == "dismissed":
			rank = 1
		found.append((rank, match.start(), label, match))
	for match in _ACTOR_VERB_RE.finditer(tail):
		label = _VERB_LABELS[match.group("verb").lower()]
		conditional = match.group("actor").lower().endswith("would")
		rank = 1 if conditional or _SIDE_ORDER_RE.search(match.group("object")) else 3
		found.append((rank, match.start(), label, match))
	for match in _BARE_VERDICT_RE.finditer(tail):
		found.append((2, match.start(), _VERB_LABELS[match.group("verb").lower()], match))
	for match in _CONSEQUENCE_RE.finditer(tail):
		prefix = tail[max(0, match.start() - 30) : match.start()]
		if _NEGATION_BEFORE_VERB_RE.search(prefix):
			continue
		label = "set_aside" if match.group(0).lower() in {"set aside", "quashed", "annulled", "vacated"} else "remitted"
		found.append((2, match.start(), label, match))
	return found


def _best_outcome(content: str) -> tuple[str, re.Match[str], int, str] | None:
	"""Pick the operative disposition: (label, match, tail_offset, tail_text)."""
	if not content:
		return None
	offset = max(0, len(content) - _TAIL_CHARS)
	tail = content[offset:]
	candidates = _disposition_candidates(tail)
	if not candidates:
		# Long trailing annexes can push the ruling out of the tail; fall back to the whole text.
		offset, tail = 0, content
		candidates = _disposition_candidates(tail)
	if not candidates:
		return None
	operative_start = 0
	for marker in _MARKER_RE.finditer(tail):
		if any(start >= marker.start() for _rank, start, _label, _m in candidates):
			operative_start = marker.start()
	rank, _start, label, match = max(
		candidates, key=lambda item: (item[1] >= operative_start, item[0], item[1])
	)
	return label, match, offset, tail


def _is_partial(tail: str, match: re.Match[str]) -> bool:
	left, right = _sentence_bounds(tail, match.start(), match.end())
	return bool(_PARTIAL_RE.search(tail[left:right]))


def _government_role(style_or_between: str) -> str | None:
	if not style_or_between:
		return None
	text = " ".join(style_or_between.split())
	lower = text.lower()
	if not _GOVERNMENT_PARTY_RE.search(lower):
		return None

	applicant_matches = list(re.finditer(r"\bapplicants?\b", lower))
	respondent_matches = list(re.finditer(r"\brespondents?\b", lower))
	gov_matches = list(_GOVERNMENT_PARTY_RE.finditer(lower))
	if not gov_matches:
		return None

	def nearest_distance(a: int, positions: list[re.Match[str]]) -> int:
		if not positions:
			return 10**9
		best = 10**9
		for pos in positions:
			distance = abs(a - pos.start())
			# In captions, the role token commonly appears after the party name.
			if pos.start() < a:
				distance += 40
			if distance < best:
				best = distance
		return best

	best_role: str | None = None
	best_distance = 10**9
	for match in gov_matches:
		idx = match.start()
		d_app = nearest_distance(idx, applicant_matches)
		d_res = nearest_distance(idx, respondent_matches)
		if min(d_app, d_res) > 120:
			continue
		if d_app < d_res and d_app < best_distance:
			best_distance = d_app
			best_role = "applicant"
		elif d_res < d_app and d_res < best_distance:
			best_distance = d_res
			best_role = "respondent"

	if best_role is not None:
		return best_role

	vs_split = re.split(r"\bv\.?\b", lower, maxsplit=1)
	if len(vs_split) == 2:
		left, right = vs_split
		if _GOVERNMENT_PARTY_RE.search(left):
			return "applicant"
		if _GOVERNMENT_PARTY_RE.search(right):
			return "respondent"
	return None


def _derive_outcome_fields(content: str, metadata: dict[str, object]) -> dict[str, tuple[str, float]]:
	derived: dict[str, tuple[str, float]] = {}
	best = _best_outcome(content)
	outcome = best[0] if best else None
	partial = bool(best and _is_partial(best[3], best[1]))
	if outcome:
		derived["decision outcome"] = ("mixed" if partial else outcome, 0.70 if partial else 0.78)

	style_text = str(metadata.get("style of cause") or "").strip()
	between_text = str(metadata.get("between") or "").strip()
	role_source_text = "\n".join(part for part in (style_text, between_text, content[:1200]) if part)
	gov_role = _government_role(role_source_text)
	if gov_role:
		derived["government role"] = (gov_role, 0.74)

	if outcome and gov_role:
		if partial:
			government_outcome = "mixed"
		elif outcome == "dismissed":
			government_outcome = "lost" if gov_role == "applicant" else "won"
		elif outcome in {"allowed", "granted", "set_aside", "remitted"}:
			government_outcome = "won" if gov_role == "applicant" else "lost"
		else:
			government_outcome = "undetermined"
		derived["government outcome"] = (government_outcome, 0.70 if partial else 0.76)
		winner = gov_role if government_outcome == "won" else "applicant" if gov_role == "respondent" else "respondent"
		loser = "respondent" if winner == "applicant" else "applicant"
		if government_outcome == "mixed":
			winner = loser = "mixed"
		derived["case winner"] = (winner, 0.70 if partial else 0.76)
		derived["case loser"] = (loser, 0.70 if partial else 0.76)
		derived["outcome status"] = (government_outcome, 0.70 if partial else 0.76)
	elif outcome:
		derived["outcome status"] = ("mixed" if partial else "undetermined", 0.60 if partial else 0.50)

	return derived


def derive_outcome_detail(content: str, metadata: dict[str, object]) -> dict[str, object]:
	"""Return structured disposition evidence without replacing legacy fields."""
	best = _best_outcome(content)
	if best is None:
		return {"status": "undetermined", "disposition": None, "evidence": None}

	label, match, tail_offset, tail = best
	evidence = {
		"text": match.group(0),
		"offset_start": tail_offset + match.start(),
		"offset_end": tail_offset + match.end(),
	}
	partial = _is_partial(tail, match)
	role = _government_role(
		"\n".join(
			[
				*(
					str(metadata.get(key) or "").strip()
					for key in ("style of cause", "between")
					if metadata.get(key)
				),
				content[:1200],
			]
		)
	)
	status = "mixed" if partial else "undetermined"
	winner = loser = None
	if role and not partial:
		applicant_won = (label in {"allowed", "granted", "set_aside", "remitted"}) == (role == "respondent")
		status = "won" if applicant_won else "lost"
		winner = "applicant" if applicant_won else "respondent"
		loser = "respondent" if winner == "applicant" else "applicant"
	return {
		"status": status,
		"disposition": "mixed" if partial else label,
		"winner": winner,
		"loser": loser,
		"government_role": role,
		"evidence": evidence,
	}


def build_case_outcome(content: str, metadata: dict[str, object]) -> dict[str, object]:
	"""Build the normalized dedicated outcome record for one case."""
	fields = _derive_outcome_fields(content, metadata)
	detail = derive_outcome_detail(content, metadata)
	confidence_values = [score for _value, score in fields.values()]
	evidence = detail.get("evidence") or {}
	return {
		"classifier_version": OUTCOME_CLASSIFIER_VERSION,
		"decision_outcome": fields.get("decision outcome", (None, 0.0))[0],
		"outcome_status": detail.get("status") or "undetermined",
		"winner_side": detail.get("winner") or fields.get("case winner", (None, 0.0))[0],
		"loser_side": detail.get("loser") or fields.get("case loser", (None, 0.0))[0],
		"government_role": fields.get("government role", (detail.get("government_role"), 0.0))[0],
		"government_outcome": fields.get("government outcome", (None, 0.0))[0],
		"challenged_issue": metadata.get("challenged issue"),
		"challenged_issues": [
			item for item in str(metadata.get("challenged issues") or "").split(", ") if item
		],
		"disposition_evidence": evidence.get("text"),
		"evidence_offset_start": evidence.get("offset_start"),
		"evidence_offset_end": evidence.get("offset_end"),
		"confidence": max(confidence_values, default=0.0),
		"source": "deterministic_outcome",
	}
