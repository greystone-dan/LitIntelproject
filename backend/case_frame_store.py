"""Stored case frames for the reader: read one decision's frame from case_frames.

Behind CASELIBRARY_CASE_FRAME_ENABLED=1. Stored data only; no model runs when a page loads.
"""

from __future__ import annotations

import os
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import CaseFrame

ENABLED_ENV = "CASELIBRARY_CASE_FRAME_ENABLED"
NOTE = (
	"A short summary written ahead of time from the decision text. It can contain mistakes: "
	"check it against the decision before relying on it."
)
LISTS = ("levels", "issues", "arguments", "challenged")


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


def case_frame(case_id: int, db: Session) -> dict[str, Any]:
	if not is_enabled():
		return {"available": False}
	row = db.execute(
		select(CaseFrame).where(CaseFrame.case_id == case_id).order_by(CaseFrame.version.desc()).limit(1)
	).scalar_one_or_none()
	if row is None:
		return {"available": False, "empty_note": "No summary has been prepared for this decision yet."}
	return {"available": True, "note": NOTE, "version": row.version, "frame": clean_frame(row.frame or {})}
