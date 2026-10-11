"""Plain-language search over the paragraph keyword index (table paragraph_search); no model or AI call.

The index is built outside the app (scripts or a one-off SQL file) so the search degrades safely: when the table
is missing or empty, `search_paragraph_cases` returns None and the caller keeps the older matching.
A query becomes one slot per content word (the word or any of its curated synonyms). Cases are looked up
from strict to loose: all slots, then all but one, then all but two, stopping once enough paragraphs match.
Paragraphs are ranked by tsvector proximity, with a bonus when the exact phrase appears, and rolled up per case.
"""

from __future__ import annotations

import itertools
import os
import re
import time
from typing import Any

from sqlalchemy import text as sql_text

from .search_matching import sentence_words
from .search_thesaurus import synonyms_for

TS_CONFIG = "english"
MIN_PARAGRAPHS = 20  # stop loosening once this many paragraphs match
MAX_PARAGRAPHS = 2000  # ranked paragraphs kept per search
MAX_CASES = 300
MAX_LOOSEN = 2
_TABLE_CACHE: dict[str, float | bool] = {"checked": 0.0, "ready": False}
_TABLE_TTL_SECONDS = 60.0


def _enabled() -> bool:
	return os.getenv("ILIT_PARAGRAPH_SEARCH", "1").strip().lower() not in {"0", "false", "no", "off"}


def _term(phrase: str) -> str:
	tokens = re.findall(r"[a-z0-9]+", phrase.lower())
	tokens = [token for token in tokens if len(token) > 1]
	if not tokens:
		return ""
	if len(tokens) == 1:
		return tokens[0]
	return "(" + " <-> ".join(tokens) + ")"


def query_slots(query: str) -> list[str]:
	"""One OR-group string per content word: the word plus its synonyms."""
	slots: list[str] = []
	for word in sentence_words(query):
		terms = [_term(word)] + [_term(synonym) for synonym in synonyms_for(word)]
		unique = list(dict.fromkeys(term for term in terms if term))
		if unique:
			slots.append("(" + " | ".join(unique) + ")")
	return slots


def tier_queries(slots: list[str]) -> list[str]:
	"""tsquery strings from strict (all slots) to loose (all but MAX_LOOSEN)."""
	count = len(slots)
	tiers = []
	for missing in range(0, MAX_LOOSEN + 1):
		keep = count - missing
		if keep < 2:
			break
		combos = itertools.combinations(slots, keep)
		tiers.append(" | ".join("(" + " & ".join(combo) + ")" for combo in combos))
	return tiers


def _index_ready(db: Any) -> bool:
	now = time.monotonic()
	if now - float(_TABLE_CACHE["checked"]) < _TABLE_TTL_SECONDS and _TABLE_CACHE["checked"]:
		return bool(_TABLE_CACHE["ready"])
	try:
		ready = bool(
			db.execute(
				sql_text(
					"SELECT to_regclass('public.paragraph_search') IS NOT NULL "
					"AND EXISTS (SELECT 1 FROM paragraph_search LIMIT 1)"
				)
			).scalar()
		)
	except Exception:
		_rollback(db)
		ready = False
	_TABLE_CACHE.update(checked=now, ready=ready)
	return ready


def _rollback(db: Any) -> None:
	try:
		db.rollback()
	except Exception:
		pass


def _ranked_sql(restrict_courts: bool):
	"""The ranking query; with restrict_courts the court filter is applied before the paragraph cut-off."""
	court_join = "JOIN cases c ON c.id = p.case_id AND lower(c.court) = ANY(:courts)" if restrict_courts else ""
	return sql_text(
		f"""
	WITH q AS (
		SELECT to_tsquery('{TS_CONFIG}', :match_query) AS match_q,
		       to_tsquery('{TS_CONFIG}', :rank_query) AS rank_q,
		       phraseto_tsquery('{TS_CONFIG}', :phrase_text) AS phrase_q
	), hits AS (
		SELECT p.chunk_id, p.case_id,
		       ts_rank_cd(p.tsv, q.rank_q, 32)
		       + CASE WHEN p.tsv @@ q.phrase_q THEN 1.0 ELSE 0.0 END AS score
		FROM paragraph_search p {court_join}, q
		WHERE p.tsv @@ q.match_q
		ORDER BY score DESC
		LIMIT :max_paragraphs
	)
	SELECT case_id,
	       max(score) AS best_score,
	       count(*) AS paragraphs,
	       (array_agg(chunk_id ORDER BY score DESC))[1] AS best_chunk_id
	FROM hits
	GROUP BY case_id
	ORDER BY max(score) + 0.05 * least(count(*), 10) DESC, case_id DESC
	LIMIT :max_cases
	"""
	)


_RANKED_SQL = _ranked_sql(False)
_RANKED_COURT_SQL = _ranked_sql(True)


def search_paragraph_cases(db: Any, query: str, courts: list[str] | None = None) -> list[dict[str, Any]] | None:
	"""Cases ranked by their best paragraph; None when the index or query is unusable (use older matching).

	`courts` (lower-case names as stored in cases.court) keeps only those courts before the paragraph cut-off, so a
	small court is not crowded out of the top results by larger ones."""
	if not _enabled():
		return None
	slots = query_slots(query)
	if len(slots) < 2:
		return None
	if not _index_ready(db):
		return None
	rank_query = " | ".join(slots)
	rows: list[Any] = []
	try:
		for match_query in tier_queries(slots):
			params = {
				"match_query": match_query,
				"rank_query": rank_query,
				"phrase_text": " ".join(query.split()),
				"max_paragraphs": MAX_PARAGRAPHS,
				"max_cases": MAX_CASES,
			}
			if courts:
				params["courts"] = [court.lower() for court in courts]
			result = db.execute(_RANKED_COURT_SQL if courts else _RANKED_SQL, params)
			rows = list(result.mappings().all())
			if sum(int(row["paragraphs"]) for row in rows) >= MIN_PARAGRAPHS:
				break
	except Exception:
		_rollback(db)
		return None
	return [
		{
			"case_id": int(row["case_id"]),
			"score": float(row["best_score"]),
			"paragraphs": int(row["paragraphs"]),
			"best_chunk_id": int(row["best_chunk_id"]),
		}
		for row in rows
	] or None
