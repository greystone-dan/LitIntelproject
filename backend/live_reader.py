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
import types
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Case
from .live_analysis import LiveParagraph, analyze_extracted
from .contextual_authority.case_structure import structure_outline
from .live_decision import decision_details, decision_format_blocks, looks_like_decision
from .paragraph_cited_by_db import load_pinpoint_cited_by
from .citation_refine import refine_case_citations
from .citation_refine.pinpoints import target_paragraphs
from .citations import extract_case_citation_matches
from .reader_service import (
	_compute_reader_inferred_tags,
	MAX_PINPOINT_TEXT_CASES,
	MAX_PINPOINT_TEXT_PARAGRAPHS,
	_pinpoint_response_fields,
	paragraph_text_from_decision,
)

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


_LEAD_WORDS_RE = re.compile(r"^(?:(?:and|or|but|see|also|compare|cf\.?|in|e\.g\.,?|per|accord|contra)\s+)+", re.IGNORECASE)


def _trim_lead_words(row: dict[str, Any]) -> dict[str, Any]:
	"""\"and in Canada v Huruglica, ...\" or \"Compare Suresh ...\": the signal words are not part of the citation."""
	if row["kind"] not in {"case", "case_short", "case_name"}:
		return row
	match = _LEAD_WORDS_RE.match(row["reference_text"])
	if not match or match.end() >= len(row["reference_text"]):
		return row
	return {**row, "reference_text": row["reference_text"][match.end():], "offset_start": row["offset_start"] + match.end()}


def _add_back_references(text: str, rows: list[dict[str, Any]], case_matches: list[Any]) -> list[dict[str, Any]]:
	"""Link "Vavilov, above at para 99" and "Ibid at para 20" to the earlier citation they point back to.

	Uses only the back-reference step of ``citation_refine`` over this document, so the shared extractor and
	stored data are untouched. Every such link is a guess about which earlier citation is meant, and is marked so.
	"""
	by_span = {(r["offset_start"], r["offset_end"]): r for r in rows if r["kind"] in {"case", "neutral"}}
	refined = refine_case_citations(text, pass_one_rows=case_matches, steps=("C2_backrefs",))
	out = list(rows)
	for ref in refined.rows:
		if ref.kind != "case_short" or ref.anchor_offset_start is None:
			continue
		target = by_span.get((ref.anchor_offset_start, ref.anchor_offset_end or 0))
		if target is None:
			continue
		span = (ref.offset_start, ref.offset_end)
		label = target.get("resolved_case_title") or target["reference_text"]
		note = f"Back-reference (heuristic): taken to mean the earlier citation of {label[:60]}"
		existing = next((r for r in out if (r["offset_start"], r["offset_end"]) == span), None)
		for start, end, _ in ref.replaces:
			out = [r for r in out if (r["offset_start"], r["offset_end"]) != (start, end)]
		if existing is not None and existing.get("resolved_case_id") is not None:
			continue
		row = {
			**(existing or {}),
			"kind": "case_short",
			"reference_text": text[ref.offset_start : ref.offset_end],
			"normalized_reference": ref.normalized_citation,
			"offset_start": ref.offset_start,
			"offset_end": ref.offset_end,
			"resolved_case_id": target.get("resolved_case_id"),
			"resolved_case_title": target.get("resolved_case_title"),
			"resolved_case_citation": target.get("resolved_case_citation"),
			"heuristic_note": note,
			"library_status": target.get("library_status"),
		}
		out = [r for r in out if (r["offset_start"], r["offset_end"]) != span]
		out.append(row)
	return sorted(out, key=lambda r: (r["offset_start"], -r["offset_end"]))


def _reader_citation(row: dict[str, Any], row_id: int, *, statute: bool) -> dict[str, Any]:
	if not statute:
		row = _trim_lead_words(row)
	resolved = row.get("resolved_case_id")
	out: dict[str, Any] = {
		"heuristic_note": row.get("heuristic_note"),
		"library_status": row.get("library_status"),
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
	"""Cited paragraph(s), their stored text and cited-by counts, from the library only (same parser as the reader)."""
	pins_by_row: dict[int, Any] = {}
	for row in rows:
		if row["target_case_id"] is None or row["citation_kind"] == "statute":
			continue
		pins = target_paragraphs(row["citation_text"], row["normalized_citation"])
		if pins is not None:
			pins_by_row[row["id"]] = pins
			row["target_paragraph"] = pins.first
	if not pins_by_row:
		return
	by_id = {row["id"]: row for row in rows}
	wanted: dict[int, set[int]] = {}
	for row_id in sorted(pins_by_row):
		case_id = by_id[row_id]["target_case_id"]
		if len(wanted) >= MAX_PINPOINT_TEXT_CASES and case_id not in wanted:
			continue
		wanted.setdefault(case_id, set()).update(pins_by_row[row_id].paragraphs[:MAX_PINPOINT_TEXT_PARAGRAPHS])
	texts: dict[tuple[int, int], str] = {}
	for case_id, full_text in session.execute(select(Case.id, Case.full_text).where(Case.id.in_(wanted))):
		for paragraph in wanted[case_id]:
			text = paragraph_text_from_decision(full_text, paragraph)
			if text:
				# Modern SCC reasons number paragraphs without brackets; the reader's note code looks for "[N]".
				text = text if text.lstrip().startswith("[") else re.sub(rf"^\s*{paragraph}\s+(?=\S)", f"[{paragraph}] ", text)
				texts[(case_id, paragraph)] = text
	for row_id, pins in pins_by_row.items():
		row = by_id[row_id]
		case_id = row["target_case_id"]
		if case_id not in wanted:
			continue
		if (case_id, pins.first) in texts:
			row["target_chunk_text"] = texts[(case_id, pins.first)]
		row.update(_pinpoint_response_fields(pins, case_id, texts))
	try:
		with session.begin_nested():
			cited_by = load_pinpoint_cited_by(
				session, {(by_id[i]["target_case_id"], tuple(p.paragraphs)) for i, p in pins_by_row.items()}
			)
	except Exception:  # noqa: BLE001 - optional stored data; a missing table must not break the page
		cited_by = {}
	for row_id, pins in pins_by_row.items():
		found = cited_by.get((by_id[row_id]["target_case_id"], tuple(pins.paragraphs)))
		if found:
			by_id[row_id]["target_cited_by"] = found


def document_tags(text: str) -> list[dict[str, Any]]:
	"""The reader's keyword tags (forum, statute, issue, analysis) found in this text by the same fixed rules, never stored."""
	holder = types.SimpleNamespace(id=None, full_text=text, summary=None)
	return [tag.model_dump() for tag in _compute_reader_inferred_tags(holder, [])]


def _outline(text: str, blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
	try:
		return structure_outline(text, blocks)
	except Exception:  # noqa: BLE001 - an outline problem must never break the reader
		return []


def build_live_reader_payload(
	text: str,
	paragraphs: list[LiveParagraph],
	filename: str,
	session: Session | None = None,
) -> dict[str, Any]:
	"""The reader payload for one document. ``session`` is read-only and optional (no library: nothing resolves)."""
	case_matches = extract_case_citation_matches(text)
	analysis = analyze_extracted(text, paragraphs, filename, session, case_matches)
	rows: list[dict[str, Any]] = []
	case_rows = _add_back_references(text, analysis["case_citations"], case_matches)
	for source, statute in ((case_rows, False), (analysis["statute_references"], True)):
		for row in source:
			rows.append(_reader_citation(row, len(rows) + 1, statute=statute))
	if session is not None:
		_attach_pinpoint_text(session, rows)
	rows.sort(key=lambda r: (r["offset_start"], -r["offset_end"]))
	is_decision = looks_like_decision(text)
	details = decision_details(text) if is_decision else None
	item = {
		"id": None,
		"title": filename,
		"full_text": text,
		"citation": (details or {}).get("citation"),
		"court": (details or {}).get("court"),
		"date": (details or {}).get("date"),
		"judge": (details or {}).get("judge"),
		"source_url": None,
		"rule_outcome": (details or {}).get("outcome"),
	}
	format_blocks = decision_format_blocks(text) if is_decision else format_blocks_for_text(text)
	return {
		"item": item,
		"citations": rows,
		"readerData": {
			"case": item,
			"format_blocks": format_blocks,
			"chunks": [],
			"citations": rows,
			"tags": document_tags(text),
			"extracted_metadata": [],
			"evidence_summary": None,
			"structure_outline": _outline(text, format_blocks),
			"case_type": {"primary": details["case_type"]} if details and details.get("case_type") else None,
		},
		"summary": {
			**analysis["summary"],
			"paragraphs": sum(b["type"] == "para" for b in format_blocks) if is_decision else analysis["paragraph_count"],
			"characters": analysis["text_length"],
		},
		"filename": filename,
		"decision": details,
	}
