"""Find the discussion unit, not just the case (no model, no AI call).

Runs the paragraph keyword search, then places the best matching paragraph of each case inside the discussion unit
that contains it. Each result names the case, judge, outcome, the unit's rule-based role (experimental) and its
printed paragraph range, plus the matching passage. Off unless ILIT_UNIT_SEARCH is set.
"""

from __future__ import annotations

import os
import re
import time
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Case, CaseChunk
from .paragraph_search import search_paragraph_cases
from .reader_service import _cached_inspect_case, _printed_numbers, _unit_number_range, _unit_roles
from .search_matching import sentence_words
from .search_thesaurus import synonyms_for

DEFAULT_LIMIT = 8
MAX_LIMIT = 20
POOL_EXTRA = 2  # extra cases looked at so the final order can be re-ranked before cutting to the limit
TIME_BUDGET_SECONDS = 2.5  # unit segmentation is seconds per cold case; stop looking at more cases after this
MAX_QUERY_CHARS = 300
SNIPPET_CHARS = 420
UNIT_SEARCH_NOTE = "Experimental: units and roles come from fixed text rules; the match is by words, not meaning."


def unit_search_enabled() -> bool:
	return os.getenv("ILIT_UNIT_SEARCH", "").strip().lower() in {"1", "true", "yes", "on"}


_NUMBERED_RE = re.compile(r"^[^\[\n]{0,80}\[\d{1,3}\]")


def _tokens(text: str) -> list[str]:
	return re.findall(r"[a-z0-9]+", (text or "").lower())


def _same_word(token: str, word: str) -> bool:
	"""Equal, or long words sharing their first six letters (reason / reasonable, bias / biased need no stem list)."""
	return token == word or (len(token) >= 6 and len(word) >= 6 and token[:6] == word[:6])


def _term_sets(query: str) -> list[set[str]]:
	"""One set of lower-case words per content word: the word and its curated synonyms (single words only)."""
	sets = []
	for word in sentence_words(query):
		sets.append({word} | {s.lower() for s in synonyms_for(word) if s and " " not in s})
	return sets


def _query_pairs(query: str, term_sets: list[set[str]]) -> list[tuple[set[str], set[str]]]:
	"""Neighbouring content words in the order the user typed them (the user's own phrase, e.g. 'internal flight')."""
	by_original = dict(zip(sentence_words(query), term_sets))
	ordered = [by_original[t] for t in _tokens(query) if t in by_original]
	return [(ordered[i], ordered[i + 1]) for i in range(len(ordered) - 1)]


def _piece_score(text: str, term_sets: list[set[str]], pairs: list[tuple[set[str], set[str]]] | None = None) -> float:
	"""Query words found in the text, plus one for each neighbouring pair of query words that sit next to each other."""
	tokens = _tokens(text)
	present = [any(_same_word(tok, w) for w in words for tok in tokens) for words in term_sets]
	score = float(sum(present))
	for first, second in pairs or []:
		for i in range(len(tokens) - 1):
			if any(_same_word(tokens[i], w) for w in first) and any(_same_word(tokens[i + 1], w) for w in second):
				score += 1
				break
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


def locate_unit(report: dict[str, Any], chunk_index: int, term_sets: list[set[str]], pairs=None) -> dict[str, Any] | None:
	"""The unit holding the best-matching piece of the given paragraph chunk, with that piece, or None.

	Pieces that carry a printed paragraph number win ties, so a hit lands on a numbered paragraph rather than a heading.
	"""
	pieces = [p for p in report.get("paragraphs", []) if p.get("source_paragraph_index") == chunk_index]
	if not pieces:
		return None
	best = max(
		pieces,
		key=lambda p: (_piece_score(p.get("text") or "", term_sets, pairs), bool(_NUMBERED_RE.match(p.get("text") or "")), -p["paragraph_index"]),
	)
	index = best["paragraph_index"]
	for position, unit in enumerate(report.get("discussion_units", [])):
		if unit["start_paragraph"] <= index <= unit["end_paragraph"]:
			return {"position": position, "unit": unit, "piece": best}
	return None


def build_unit_result(report: dict[str, Any], chunk_index: int, term_sets: list[set[str]], pairs=None) -> dict[str, Any] | None:
	found = locate_unit(report, chunk_index, term_sets, pairs)
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
		"match_score": _piece_score(piece.get("text") or "", term_sets, pairs),
	}


def rank_results(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
	"""Numbered paragraphs before headnote and cover-page hits, then more query words and phrases, then case rank."""
	return sorted(results, key=lambda r: (r["paragraph_number"] is None, -r["match_score"], -r["case_score"]))


COURT_NAMES = {
	"FC": "FEDERAL COURT",
	"FCA": "FEDERAL COURT OF APPEAL",
	"SCC": "SUPREME COURT OF CANADA",
	"RAD": "REFUGEE APPEAL DIVISION",
	"RPD": "REFUGEE PROTECTION DIVISION",
}


def _court_filter(court: str) -> set[str]:
	"""Courts asked for, as the short code and the full name (the library stores either spelling)."""
	wanted: set[str] = set()
	for value in (court or "").split(","):
		code = value.strip().upper()
		if code:
			wanted.update({code, COURT_NAMES.get(code, code)})
	return wanted


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


def search_units(
	db: Session, query: str, *, limit: int = DEFAULT_LIMIT, court: str = "", budget_seconds: float = TIME_BUDGET_SECONDS
) -> dict[str, Any] | None:
	"""Best unit per case, re-ranked; None when the paragraph search cannot run. `court` is a comma list (FC,FCA,RAD)."""
	query = " ".join((query or "").split())[:MAX_QUERY_CHARS]
	limit = max(1, min(int(limit), MAX_LIMIT))
	hits = search_paragraph_cases(db, query)
	if not hits:
		return None
	term_sets = _term_sets(query)
	pairs = _query_pairs(query, term_sets)
	courts = _court_filter(court)
	started = time.monotonic()
	results: list[dict[str, Any]] = []
	truncated = False
	for hit in hits:
		if len(results) >= limit + POOL_EXTRA:
			break
		if results and time.monotonic() - started > budget_seconds:
			truncated = True
			break
		case = db.get(Case, hit["case_id"])
		if case is None or (courts and (case.court or "").upper() not in courts):
			continue
		chunk = db.get(CaseChunk, hit["best_chunk_id"])
		if chunk is None:
			continue
		chunks = list(db.scalars(select(CaseChunk).where(CaseChunk.case_id == case.id, CaseChunk.chunk_set == "paragraph")))
		unit = build_unit_result(_cached_inspect_case(db, case.id, chunks), chunk.chunk_index, term_sets, pairs)
		if unit is None:
			continue
		results.append({"case_id": case.id, **_case_meta(case), **unit, "case_score": hit["score"]})
	return {"query": query, "note": UNIT_SEARCH_NOTE, "truncated": truncated, "results": rank_results(results)[:limit]}
