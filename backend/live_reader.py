"""Reader-shaped payload for an uploaded or pasted document (Live Analysis markup view).

Everything here is deterministic and held in memory: nothing is stored and no model is called. The
payload has the same shape the case reader loads for a stored decision (``item``, ``citations`` and
``readerData``), so the reader's own components (formatted text, citation hover, markup mode) draw it.

What a document can honestly have is limited to what can be read from its text and from the library:
citations (with the cited paragraph's stored text and cited-by counts where the library has them),
statute references (with stored provision text) and paragraph structure. It has no discussion units,
outcome, judge or tags: those are computed per library decision, not per upload.
"""

from __future__ import annotations

import re
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Case
from .live_analysis import LiveParagraph, analyze_extracted
from .paragraph_cited_by_db import load_target_cited_by
from .reader_service import MAX_PINPOINT_TEXT_CASES, _citation_target_paragraph, paragraph_text_from_decision

_SEGMENT_RE = re.compile(r"\S(?:.*?\S)?(?=\n[ \t]*\n|\s*\Z)", re.DOTALL)
_NUMBERED_HEADING_RE = re.compile(r"^(?:[IVX]+|[A-Z]|\d{1,2}(?:\.\d{1,2})*)[.)]\s+\S")
_ROMAN = {"I", "V", "X"}


def _heading_level(segment: str) -> int | None:
	"""Heuristic: a short line with no closing punctuation is a heading. Returns ``None`` for body text."""
	line = segment.strip()
	if "\n" in line or len(line) > 110 or line.endswith((".", ",", ";", ":", "?")):
		return None
	if _NUMBERED_HEADING_RE.match(line):
		label = re.split(r"[.)]", line, maxsplit=1)[0]
		return 1 if label in _ROMAN else (3 if label[:1].isdigit() else 2)
	letters = [c for c in line if c.isalpha()]
	if letters and all(c.isupper() for c in letters) and len(line.split()) <= 10:
		return 1
	if len(line.split()) <= 8 and line[:1].isupper():
		return 2
	return None


def format_blocks_for_text(text: str) -> list[dict[str, Any]]:
	"""Typed ``[start, end)`` blocks over ``text``: paragraphs numbered in reading order, plus headings."""
	blocks: list[dict[str, Any]] = []
	number = 0
	for match in _SEGMENT_RE.finditer(text):
		segment = match.group(0)
		level = _heading_level(segment)
		if level is not None:
			blocks.append({"type": "heading", "start": match.start(), "end": match.end(), "level": level})
			continue
		number += 1
		blocks.append({"type": "para", "start": match.start(), "end": match.end(), "num": number, "mark_end": match.start()})
	return blocks


def _reader_citation(row: dict[str, Any], row_id: int, *, statute: bool) -> dict[str, Any]:
	resolved = row.get("resolved_case_id")
	out: dict[str, Any] = {
		"id": row_id,
		"citation_kind": "statute" if statute else row["kind"],
		"offset_start": row["offset_start"],
		"offset_end": row["offset_end"],
		"citation_text": row["reference_text"],
		"normalized_citation": row.get("normalized_reference"),
		"target_case_id": resolved,
		"target_title": row.get("resolved_case_title"),
		"target_citation": row.get("resolved_case_citation"),
		"unresolved": resolved is None if not statute else row.get("resolution_status") == "unresolved",
		"provenance": "live_analysis",
	}
	if statute:
		for key in (
			"instrument_key", "pinpoint", "legislation_url", "authority_document_title", "authority_document_url",
			"authority_section_number", "authority_section_text", "source_url", "section_number", "provision_text",
		):
			out[key] = row.get(key)
	return out


def _attach_pinpoint_text(session: Session, rows: list[dict[str, Any]]) -> None:
	"""Cited paragraph number, its stored text and its cited-by counts, from the library only."""
	pinpoints: dict[tuple[int, int], dict[str, Any]] = {}
	for row in rows:
		if row["target_case_id"] is None or row["citation_kind"] == "statute":
			continue
		paragraph = _citation_target_paragraph(row["citation_text"], row["normalized_citation"])
		if paragraph is not None:
			row["target_paragraph"] = paragraph
			pinpoints[(row["target_case_id"], paragraph)] = row
	if not pinpoints:
		return
	wanted: dict[int, set[int]] = {}
	for case_id, paragraph in sorted(pinpoints):
		if len(wanted) >= MAX_PINPOINT_TEXT_CASES and case_id not in wanted:
			continue
		wanted.setdefault(case_id, set()).add(paragraph)
	texts: dict[tuple[int, int], str] = {}
	for case_id, full_text in session.execute(select(Case.id, Case.full_text).where(Case.id.in_(wanted))):
		for paragraph in wanted[case_id]:
			text = paragraph_text_from_decision(full_text, paragraph)
			if text:
				# Modern SCC reasons number paragraphs without brackets; the reader's note code looks for "[N]".
				text = re.sub(rf"^\s*{paragraph}\s+(?=\S)", f"[{paragraph}] ", text) if not text.lstrip().startswith("[") else text
				texts[(case_id, paragraph)] = text
	cited_by: dict[tuple[int, int], dict] = {}
	try:
		with session.begin_nested():
			cited_by = load_target_cited_by(session, pinpoints)
	except Exception:  # noqa: BLE001 - optional stored data; a missing table must not break the page
		cited_by = {}
	for key, row in pinpoints.items():
		if key in texts:
			row["target_chunk_text"] = texts[key]
		if key in cited_by:
			row["target_cited_by"] = cited_by[key]


def build_live_reader_payload(
	text: str,
	paragraphs: list[LiveParagraph],
	filename: str,
	session: Session | None = None,
) -> dict[str, Any]:
	"""The reader payload for one document. ``session`` is read-only and optional (no library: nothing resolves)."""
	analysis = analyze_extracted(text, paragraphs, filename, session)
	rows: list[dict[str, Any]] = []
	for source, statute in ((analysis["case_citations"], False), (analysis["statute_references"], True)):
		for row in source:
			rows.append(_reader_citation(row, len(rows) + 1, statute=statute))
	if session is not None:
		_attach_pinpoint_text(session, rows)
	rows.sort(key=lambda r: (r["offset_start"], -r["offset_end"]))
	item = {
		"id": None,
		"title": filename,
		"full_text": text,
		"citation": None,
		"court": None,
		"date": None,
		"judge": None,
		"source_url": None,
	}
	return {
		"item": item,
		"citations": rows,
		"readerData": {
			"case": item,
			"format_blocks": format_blocks_for_text(text),
			"chunks": [],
			"citations": rows,
			"tags": [],
			"extracted_metadata": [],
			"evidence_summary": None,
		},
		"summary": {
			**analysis["summary"],
			"paragraphs": analysis["paragraph_count"],
			"characters": analysis["text_length"],
		},
		"filename": filename,
	}
