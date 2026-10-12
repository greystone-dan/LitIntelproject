"""Stored case frames for the reader: read one decision's frame from case_frames.

Behind CASELIBRARY_CASE_FRAME_ENABLED=1. Stored data only; no model runs when a page loads.
"""

from __future__ import annotations

import os
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import CaseFrame, CaseOutcome

ENABLED_ENV = "CASELIBRARY_CASE_FRAME_ENABLED"
NOTE = (
	"A short summary written ahead of time from the decision text. It can contain mistakes: "
	"check it against the decision before relying on it."
)
LISTS = ("levels", "issues", "arguments", "challenged")

# What the stored ruling word means in plain words, for the "Result" line.
RESULT_WORDS = {
	"allowed": "Allowed",
	"granted": "Granted",
	"dismissed": "Dismissed",
	"set_aside": "Set aside",
	"remitted": "Sent back to be decided again",
	"mixed": "Partly allowed",
	"withdrawn": "Withdrawn",
}


def is_enabled() -> bool:
	return os.getenv(ENABLED_ENV) == "1"


def clean_frame(frame: dict[str, Any]) -> dict[str, Any]:
	"""Keep only the fields the reader draws, with the right shapes, so a malformed stored row cannot break the page."""
	out: dict[str, Any] = {
		"parties": frame.get("parties") if isinstance(frame.get("parties"), dict) else {},
		"subject": str(frame.get("subject") or ""),
	}
	for key in LISTS:
		rows = frame.get(key)
		out[key] = [r for r in rows if isinstance(r, dict)] if isinstance(rows, list) else []
	return out


def drop_own_decision(levels: list[dict[str, Any]]) -> list[dict[str, Any]]:
	"""Stored frames end the levels list with this decision itself; the card lists only the earlier ones."""
	return levels[:-1]


def result_line(outcome: Any) -> dict[str, str] | None:
	"""The ruling of this decision as read by the outcome rules, with a plain reliability label. None when unknown."""
	word = RESULT_WORDS.get(getattr(outcome, "decision_outcome", None) or "")
	if not word:
		return None
	clear = (getattr(outcome, "confidence", 0) or 0) >= 0.75 and bool(getattr(outcome, "disposition_evidence", None))
	return {
		"text": word,
		"reliability": "Matched a clear ruling in the text" if clear else "Less certain: check the decision",
		"source": "Read by fixed rules, not by AI",
	}


def case_frame(case_id: int, db: Session) -> dict[str, Any]:
	if not is_enabled():
		return {"available": False}
	row = db.execute(
		select(CaseFrame).where(CaseFrame.case_id == case_id).order_by(CaseFrame.version.desc()).limit(1)
	).scalar_one_or_none()
	if row is None:
		return {"available": False, "empty_note": "No summary has been prepared for this decision yet."}
	frame = clean_frame(row.frame or {})
	frame["levels"] = drop_own_decision(frame["levels"])
	outcome = db.execute(
		select(CaseOutcome).where(CaseOutcome.case_id == case_id).order_by(CaseOutcome.updated_at.desc(), CaseOutcome.id.desc()).limit(1)
	).scalars().first()
	return {"available": True, "note": NOTE, "version": row.version, "frame": frame, "result": result_line(outcome)}
