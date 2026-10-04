"""Second-opinion reader for case outcomes.

Batch use only, on open case law: a small model reads the end of a decision and says what the ruling was, quoting
the sentence it relied on. The answer is advisory data kept apart from the rule engine's answer; it never
overwrites it, and an answer whose quote is not found verbatim in the text sent is discarded. User text never
goes through here.
"""

from __future__ import annotations

import json
import re
from typing import Any

from .metadata_outcomes import _is_tribunal_document, _strip_footnotes, _TRAILER_RE

CHECKER_VERSION = "outcome_checker_v1"
MODEL = "gpt-4.1-nano"
# List prices per million tokens as recorded in scripts/audit_fc_activity_motion_unknowns_openai.py; verify before a run.
INPUT_COST_PER_MILLION = 0.10
OUTPUT_COST_PER_MILLION = 0.40
EXCERPT_CHARS = 2800
LABELS = ("allowed", "dismissed", "mixed", "procedural", "unclear")

_SYSTEM = (
	"You read the end of a Canadian court or tribunal decision and report what the decision-maker ordered on the "
	"proceeding itself. Labels: allowed (application, appeal or claim succeeds, including granted, set aside and "
	"returned for redetermination, claim accepted), dismissed (dismissed, rejected, denied, claimant is not a "
	"Convention refugee), mixed (partly allowed, or several appeals with different results), procedural (the order "
	"only decides a motion, stay, extension, costs, intervention or similar, not the merits), unclear (the excerpt "
	"does not show the ruling). Use only the excerpt. Do not guess: answer unclear when the ruling is not stated. "
	"Ignore quoted statutes, footnotes, case law quoted from other courts and the lower decision being reviewed. "
	'Return JSON only: {"outcome": "<label>", "quote": "<the exact sentence from the excerpt that states the ruling, '
	'copied word for word, or an empty string>"}.'
)


def select_excerpt(text: str, chars: int = EXCERPT_CHARS) -> str:
	"""The end of the reasons, without footnotes or the counsel trailer, cut at a paragraph boundary."""
	if not text:
		return ""
	if _is_tribunal_document(text):
		text = _strip_footnotes(text)
	trailer = _TRAILER_RE.search(text, max(0, len(text) - 4000))
	if trailer:
		text = text[: trailer.start()]
	text = text.rstrip()
	if len(text) <= chars:
		return text.strip()
	cut = text[-chars:]
	newline = cut.find("\n")
	if 0 <= newline < chars // 3:
		cut = cut[newline + 1 :]
	return cut.strip()


def build_messages(excerpt: str) -> list[dict[str, str]]:
	return [{"role": "system", "content": _SYSTEM}, {"role": "user", "content": f"Excerpt:\n{excerpt}"}]


def _squash(value: str) -> str:
	return re.sub(r"\s+", " ", value.replace("’", "'").replace("“", '"').replace("”", '"')).strip().lower()


def parse_answer(raw: str, excerpt: str) -> dict[str, Any]:
	"""Validate the model's JSON. Returns {outcome, quote, valid, reason}; invalid answers become "unclear"."""
	try:
		data = json.loads(raw)
		outcome = str(data.get("outcome", "")).strip().lower()
		quote = str(data.get("quote") or "").strip()
	except (ValueError, TypeError, AttributeError):
		return {"outcome": "unclear", "quote": "", "valid": False, "reason": "bad_json"}
	if outcome not in LABELS:
		return {"outcome": "unclear", "quote": "", "valid": False, "reason": "bad_label"}
	if outcome == "unclear":
		return {"outcome": "unclear", "quote": "", "valid": True, "reason": "model_unclear"}
	if not quote or _squash(quote) not in _squash(excerpt):
		return {"outcome": "unclear", "quote": quote, "valid": False, "reason": "quote_not_in_text"}
	return {"outcome": outcome, "quote": quote, "valid": True, "reason": "ok"}


_CLASS = {"allowed": "A", "granted": "A", "set_aside": "A", "remitted": "A", "dismissed": "D", "mixed": "M", "procedural": "P", "unclear": "?"}


def short_label(label: str | None) -> str:
	return _CLASS.get(label or "", "?")


def compare(rule_label: str | None, checker_label: str | None) -> str:
	"""agree / disagree / checker_only (rules abstained, model answered) / both_unclear / rules_only."""
	rule, checker = short_label(rule_label), short_label(checker_label)
	if rule == "?" and checker == "?":
		return "both_unclear"
	if rule == "?":
		return "checker_only"
	if checker == "?":
		return "rules_only"
	return "agree" if rule == checker else "disagree"


def usage_cost(prompt_tokens: int, completion_tokens: int) -> float:
	return (prompt_tokens * INPUT_COST_PER_MILLION + completion_tokens * OUTPUT_COST_PER_MILLION) / 1_000_000


def estimate_tokens(text: str) -> int:
	"""Rough token count (4 characters per token) plus the fixed prompt."""
	return (len(text) + 3) // 4 + (len(_SYSTEM) + 3) // 4 + 10
