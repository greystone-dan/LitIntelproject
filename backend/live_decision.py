"""Header details for an uploaded document that is itself a court decision.

Uses the same deterministic extractors as the stored-case reader (header metadata, outcome rules, case-type
rules, decision formatter) on text held in memory. Nothing is stored, no model is called. Every value is the
output of fixed rules on the text, so the page labels it as such; a memo is not a decision and gets none of it.
"""

from __future__ import annotations

import re
from typing import Any

from . import metadata_outcomes
from .case_formatter import format_decision
from .case_types.classifier import STATUS_CLASSIFIED, classify_text
from .case_types.display import provision_text
from .case_types.taxonomy import TYPES_BY_KEY
from .metadata import extract_case_metadata

# The case-type rules run the citation pipeline several times; past this length they take seconds, so a very long
# document is shown without a case type rather than making the page wait.
MAX_CASE_TYPE_CHARS = 100_000
_COURT_BY_NEUTRAL = {"SCC": "Supreme Court of Canada", "FCA": "Federal Court of Appeal", "FC": "Federal Court", "FCT": "Federal Court"}
_MARKED_PARA_RE = re.compile(r"^\[?(\d{1,3})\]?[ \t]+(?=[A-Z“\"\[(])", re.MULTILINE)


def looks_like_decision(text: str) -> bool:
	"""A court decision numbers its paragraphs in brackets, in order, starting at the top: [1], [2], [3]..."""
	numbers = [int(m.group(1)) for m in _MARKED_PARA_RE.finditer(text)]
	if len(numbers) < 6:
		return False
	run = sum(1 for earlier, later in zip(numbers, numbers[1:]) if later == earlier + 1)
	return numbers[0] <= 2 and run >= 0.7 * (len(numbers) - 1)


def decision_format_blocks(text: str) -> list[dict[str, Any]]:
	return format_decision(text)


def _judges(value: object) -> str | None:
	names = [n.strip() for n in str(value or "").split(";") if n.strip()]
	if not names:
		return None
	return names[0] if len(names) == 1 else f"{names[0]} and {len(names) - 1} other judge{'s' if len(names) > 2 else ''}"


def decision_details(text: str) -> dict[str, Any]:
	"""Header facts, outcome and case type for a decision, each as the rules found them (``None`` when not found)."""
	metadata = extract_case_metadata(text)
	outcome = metadata_outcomes.build_case_outcome(text, metadata)
	case_type = None
	if len(text) <= MAX_CASE_TYPE_CHARS:
		result = classify_text(text)
		entry = TYPES_BY_KEY.get(result.primary_type or "")
		if result.status == STATUS_CLASSIFIED and entry is not None:
			case_type = {"label": entry.label, "provision": provision_text(result.primary_detail)}
	decision_outcome = outcome.get("decision_outcome") or metadata.get("decision outcome")
	neutral = str(metadata.get("neutral citation") or "")
	court_match = re.match(r"^\d{4}\s+([A-Z]+)\s+\d+$", neutral)
	return {
		"citation": metadata.get("neutral citation"),
		"court": _COURT_BY_NEUTRAL.get(court_match.group(1)) if court_match else None,
		"docket": metadata.get("docket"),
		"date": metadata.get("date"),
		"judge": _judges(metadata.get("judge")),
		"style_of_cause": metadata.get("style of cause"),
		"outcome": None if decision_outcome in (None, "", "unclear") else str(decision_outcome),
		"outcome_evidence": outcome.get("disposition_evidence"),
		"case_type": case_type,
	}
