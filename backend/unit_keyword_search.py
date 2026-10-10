"""Find the discussion unit, not just the case (no model, no AI call).

Runs the paragraph keyword search, then places the best matching paragraph of each case inside the discussion unit
that contains it. Each result names the case, judge, outcome, the unit's rule-based role (experimental) and its
printed paragraph range, plus the matching passage. Off unless ILIT_UNIT_SEARCH is set.
"""

from __future__ import annotations

import os
import re
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Case, CaseChunk
from .paragraph_search import search_paragraph_cases
from .reader_service import _cached_inspect_case, _printed_numbers, _unit_number_range, _unit_roles
from .search_matching import sentence_words
from .search_thesaurus import synonyms_for

MAX_CASES = 12
MAX_QUERY_CHARS = 300
SNIPPET_CHARS = 420
UNIT_SEARCH_NOTE = "Experimental: units and roles come from fixed text rules; the match is by words, not meaning."


def unit_search_enabled() -> bool:
	return os.getenv("ILIT_UNIT_SEARCH", "").strip().lower() in {"1", "true", "yes", "on"}


def _term_sets(query: str) -> list[set[str]]:
	"""One set of lower-case words per content word: the word and its curated synonyms (single words only)."""
	sets = []
	for word in sentence_words(query):
		words = {word} | {s.lower() for s in synonyms_for(word) if s and " " not in s}
		sets.append(words)
	return sets


def _piece_score(text: str, term_sets: list[set[str]]) -> int:
	"""How many query words (or a synonym, matched on a shared start so plurals count) appear in the text."""
	tokens = set(re.findall(r"[a-z0-9]+", text.lower()))
	score = 0
	for words in term_sets:
		if any(tok == w or (len(w) >= 5 and tok.startswith(w[:5])) for w in words for tok in tokens):
			score += 1
	return score


def snippet_around(text: str, term_sets: list[set[str]], limit: int = SNIPPET_CHARS) -> str:
	text = " ".join((text or "").split())
	if len(text) <= limit:
		return text
	lowered = text.lower()
	positions = [lowered.find(w) for words in term_sets for w in words]
	positions = [p for p in positions if p >= 0]
	centre = min(positions) if positions else 0
	start = max(0, min(centre - limit // 4, len(text) - limit))
	return ("…" if start else "") + text[start : start + limit].strip() + ("…" if start + limit < len(text) else "")


def locate_unit(report: dict[str, Any], chunk_index: int, term_sets: list[set[str]]) -> dict[str, Any] | None:
	"""The unit holding the best-matching piece of the given paragraph chunk, with that piece, or None."""
	pieces = [p for p in report.get("paragraphs", []) if p.get("source_paragraph_index") == chunk_index]
	if not pieces:
		return None
	best = max(pieces, key=lambda p: (_piece_score(p.get("text") or "", term_sets), -p["paragraph_index"]))
	index = best["paragraph_index"]
	for position, unit in enumerate(report.get("discussion_units", [])):
		if unit["start_paragraph"] <= index <= unit["end_paragraph"]:
			return {"position": position, "unit": unit, "piece": best}
	return None


def build_unit_result(report: dict[str, Any], chunk_index: int, term_sets: list[set[str]]) -> dict[str, Any] | None:
	found = locate_unit(report, chunk_index, term_sets)
	if found is None:
		return None
	unit, piece = found["unit"], found["piece"]
	roles = _unit_roles(report)
	numbers = _printed_numbers(report)
	first, last = _unit_number_range(numbers, unit["start_paragraph"], unit["end_paragraph"])
	return {
		"unit_index": int(unit["discussion_unit_id"].rsplit(":", 1)[-1]),
		"role": roles[found["position"]] if found["position"] < len(roles) else None,
		"start_number": first,
		"end_number": last,
		"paragraph_number": numbers.get(piece["paragraph_index"]),
		"paragraph_count": unit["paragraph_count"],
		"snippet": snippet_around(piece.get("text") or "", term_sets),
		"match_score": _piece_score(piece.get("text") or "", term_sets),
	}


def _case_meta(case: Case) -> dict[str, Any]:
	extracted = (case.metadata_json or {}).get("reader_extracted") or {}
	return {
		"title": case.title,
		"citation": case.citation,
		"court": case.court,
		"date": case.date.isoformat() if case.date else None,
		"judge": extracted.get("judge") if isinstance(extracted, dict) else None,
		"outcome": extracted.get("decision outcome") if isinstance(extracted, dict) else None,
	}


def search_units(db: Session, query: str, *, max_cases: int = MAX_CASES) -> dict[str, Any] | None:
	"""Results ordered by the case ranking of the paragraph search; None when that search cannot run."""
	query = " ".join((query or "").split())[:MAX_QUERY_CHARS]
	hits = search_paragraph_cases(db, query)
	if not hits:
		return None
	term_sets = _term_sets(query)
	results = []
	for hit in hits[:max_cases]:
		case = db.get(Case, hit["case_id"])
		chunk = db.get(CaseChunk, hit["best_chunk_id"])
		if case is None or chunk is None:
			continue
		chunks = list(db.scalars(select(CaseChunk).where(CaseChunk.case_id == case.id, CaseChunk.chunk_set == "paragraph")))
		unit = build_unit_result(_cached_inspect_case(db, case.id, chunks), chunk.chunk_index, term_sets)
		if unit is None:
			continue
		results.append({"case_id": case.id, **_case_meta(case), **unit, "case_score": hit["score"]})
	return {"query": query, "note": UNIT_SEARCH_NOTE, "results": results}
