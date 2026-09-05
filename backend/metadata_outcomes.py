"""Outcome and government-role derivation for case metadata.

These helpers inspect the operative tail of a decision (ORDER / JUDGMENT /
DISPOSITION blocks) to label the decision outcome, then combine the caption
parties with that outcome to derive the government role and result. They are
imported by `backend.metadata`; nothing else should depend on them.
"""

from __future__ import annotations

import re

OUTCOME_CLASSIFIER_VERSION = "deterministic_outcome_v1"
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


def _operative_blocks(content: str) -> list[str]:
	if not content:
		return []
	tail = content[-12000:]
	markers = list(re.finditer(r"\b(?:ORDER|JUDGMENT|DISPOSITION|CONCLUSION)\b", tail, re.IGNORECASE))
	if not markers:
		return [tail]
	blocks: list[str] = []
	for index, marker in enumerate(markers):
		end = markers[index + 1].start() if index + 1 < len(markers) else len(tail)
		block = tail[marker.start() : end].strip()
		if block:
			blocks.append(block)
	return blocks


def _outcome_window(content: str) -> str:
	blocks = _operative_blocks(content)
	if not blocks:
		return ""
	best_block = max(
		blocks,
		key=lambda block: (
			sum(bool(pattern.search(block)) for _label, pattern in _OUTCOME_PATTERNS),
			len(block),
		),
	)
	return best_block


def _latest_outcome_label(content: str) -> str | None:
	latest: tuple[int, str] | None = None
	search_content = _outcome_window(content)
	for label, pattern in _OUTCOME_PATTERNS:
		for match in pattern.finditer(search_content):
			if latest is None or match.start() > latest[0]:
				latest = (match.start(), label)
	if latest is None:
		return None
	return latest[1]


def _latest_outcome_match(content: str) -> tuple[str, re.Match[str]] | None:
	search_content = _outcome_window(content)
	latest: tuple[int, str, re.Match[str]] | None = None
	for label, pattern in _OUTCOME_PATTERNS:
		for match in pattern.finditer(search_content):
			if latest is None or match.start() > latest[0]:
				latest = (match.start(), label, match)
	if latest is None:
		return None
	return latest[1], latest[2]


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
	outcome = _latest_outcome_label(content)
	outcome_match = _latest_outcome_match(content)
	partial = bool(
		outcome_match
		and re.search(r"\b(?:in\s+part|partly|partially)\b", outcome_match[1].group(0), re.IGNORECASE)
	)
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
	match_result = _latest_outcome_match(content)
	if match_result is None:
		return {"status": "undetermined", "disposition": None, "evidence": None}

	label, match = match_result
	window = _outcome_window(content)
	window_start = content.rfind(window) if window else -1
	evidence = {
		"text": match.group(0),
		"offset_start": window_start + match.start() if window_start >= 0 else None,
		"offset_end": window_start + match.end() if window_start >= 0 else None,
	}
	partial = bool(re.search(r"\b(?:in\s+part|partly|partially)\b", match.group(0), re.IGNORECASE))
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
