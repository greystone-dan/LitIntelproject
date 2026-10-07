"""Whole-token identity matches shared by case search and analytics SQL.

Identity queries use match hierarchy; non-identity topic scores are untouched.
SQL fragments contain only fixed expressions; all query values are bound parameters.
"""

from __future__ import annotations

import re
from typing import Any


CAPTION_SEPARATOR = r" (v|vs|versus) "
BETWEEN_SEPARATOR = r" (and|applicant|applicants|respondent|respondents) "


def normalized_tokens(value: Any) -> str:
	return " ".join(re.findall(r"[^\W_]+", str(value or "").lower()))


def citation_query(query: str) -> str:
	normalized = _citation_tokens(query)
	# Neutral or reported citation, not a topic/year-only query.
	return normalized if re.fullmatch(r"[12][0-9]{3} (?:[0-9]+ )?[a-z]+ [0-9]+", normalized) else ""


def _citation_tokens(value: Any) -> str:
	return re.sub(r"(?<!\S)s c r(?!\S)", "scr", normalized_tokens(value))


def _contains_tokens(value: Any, query: str) -> bool:
	return bool(query) and f" {query} " in f" {normalized_tokens(value)} "


def _caption_parties(value: Any) -> list[str]:
	caption = normalized_tokens(value)
	return re.split(CAPTION_SEPARATOR, caption)[::2] if re.search(CAPTION_SEPARATOR, caption) else []


def identity_tier(case: Any, query: str) -> int:
	citation = citation_query(query)
	if citation and any(
		f" {citation} " in f" {_citation_tokens(getattr(case, field, None))} "
		for field in ("citation", "secondary_citation")
	):
		return 2
	tokens = normalized_tokens(query)
	metadata = getattr(case, "metadata_json", None)
	metadata = metadata if isinstance(metadata, dict) else {}
	reader = metadata.get("reader_extracted")
	reader = reader if isinstance(reader, dict) else {}
	parties = _caption_parties(getattr(case, "title", None)) + _caption_parties(reader.get("style of cause"))
	between = normalized_tokens(reader.get("between"))
	if between:
		parties += re.split(BETWEEN_SEPARATOR, f" {between} ")[::2]
	return 1 if any(_contains_tokens(party, tokens) for party in parties) else 0


def match_details(case: Any, query: str, mode: str) -> tuple[str, int]:
	"""Calculate label and hierarchy once (4 citation, 3 party, 2 title, 1 body)."""
	tier = identity_tier(case, query)
	if tier:
		return ("Citation", 4) if tier == 2 else ("Party name", 3)
	tokens = normalized_tokens(query)
	if tokens and tokens in normalized_tokens(getattr(case, "title", None)):
		return "Title", 2
	if tokens and any(tokens in normalized_tokens(getattr(case, field, None)) for field in ("full_text", "summary")):
		return "Full text", 1
	return ("Semantic" if mode in {"semantic", "hybrid"} else "Metadata"), 0


def matched_on(case: Any, query: str, mode: str) -> str:
	return match_details(case, query, mode)[0]


def _normalized_sql(expression: str) -> str:
	# Bind the POSIX regex so text() cannot mistake its colon for a bind name.
	return f"TRIM(REGEXP_REPLACE(LOWER(COALESCE({expression}, '')), :match_normalization, ' ', 'g'))"


def identity_sql(query: str) -> tuple[str, str, dict[str, str]]:
	"""Return identical citation/party predicates for filtering, ranking and labels."""
	params = {
		"match_tokens": normalized_tokens(query),
		"match_citation": citation_query(query),
		"match_normalization": "[^[:alnum:]]+",
	}
	citation_fields = [
		f"REGEXP_REPLACE({_normalized_sql(f'c.{field}')}, '(^| )s c r( |$)', '\\1scr\\2', 'g')"
		for field in ("citation", "secondary_citation")
	]
	citation = "(:match_citation <> '' AND (" + " OR ".join(
		f"POSITION(' ' || :match_citation || ' ' IN ' ' || {field} || ' ') > 0" for field in citation_fields
	) + "))"
	captions = [_normalized_sql(expression) for expression in (
		"c.title", "c.metadata_json->'reader_extracted'->>'style of cause'",
	)]
	party_checks = [
		f"({caption} ~ '{CAPTION_SEPARATOR}' AND EXISTS "
		f"(SELECT 1 FROM REGEXP_SPLIT_TO_TABLE({caption}, '{CAPTION_SEPARATOR}') AS party(name) "
		"WHERE POSITION(' ' || :match_tokens || ' ' IN ' ' || party.name || ' ') > 0))"
		for caption in captions
	]
	between = _normalized_sql("c.metadata_json->'reader_extracted'->>'between'")
	party_checks.append(
		f"EXISTS (SELECT 1 FROM REGEXP_SPLIT_TO_TABLE(' ' || {between} || ' ', '{BETWEEN_SEPARATOR}') AS party(name) "
		"WHERE POSITION(' ' || :match_tokens || ' ' IN ' ' || TRIM(party.name) || ' ') > 0)"
	)
	party = "(:match_tokens <> '' AND (" + " OR ".join(party_checks) + "))"
	return citation, party, params


def matched_on_sql(query: str, *, search_full_text: bool) -> tuple[str, dict[str, str]]:
	citation, party, params = identity_sql(query)
	params["match_like"] = f"%{' '.join(query.split())}%"
	label = f"CASE WHEN {citation} THEN 'Citation' WHEN {party} THEN 'Party name' "
	# Title/body labels use precisely the legacy ranking predicates (including
	# substring matches); only identity matches require whole-token boundaries.
	label += "WHEN :match_tokens <> '' AND c.title ILIKE :match_like THEN 'Title' "
	if search_full_text:
		label += "WHEN :match_tokens <> '' AND (c.full_text ILIKE :match_like OR c.summary ILIKE :match_like) THEN 'Full text' "
	return label + "ELSE 'Metadata' END", params


# Plain-language (sentence) queries: match cases that contain most of the content words, not only the exact phrase.
SENTENCE_STOPWORDS = frozenset(
	"a an the of to in is was were are be been being for on and or my me i he she it they them his her their "
	"its that this these those by with as at from not did do does done if because after before when who which "
	"whom what where why how into than then so out up has have had would could should can may might about over "
	"under against between through during without within also but any all some no our we you your us".split()
)
SENTENCE_MIN_WORDS = 3
SENTENCE_MAX_WORDS = 6


def sentence_words(query: str) -> list[str]:
	"""Distinct content words of a plain-language query, longest first; [] unless it reads like a sentence."""
	seen: list[str] = []
	for word in re.findall(r"[^\W_]+", str(query or "").lower()):
		if len(word) >= 3 and word not in SENTENCE_STOPWORDS and word not in seen:
			seen.append(word)
	if len(seen) < SENTENCE_MIN_WORDS:
		return []
	return sorted(seen, key=lambda value: (-len(value), seen.index(value)))[:SENTENCE_MAX_WORDS]


def sentence_hits_sql(query: str, *, search_full_text: bool) -> tuple[str, str, dict[str, str]]:
	"""Return (hit_count_sql, filter_sql, params) for most-of-the-words matching, or empty strings.

	Needs at least 60% of the content words (min 2) in the title, citation and, when body search is on, the
	summary and full text. Values are bound parameters; no schema or index change.
	"""
	words = sentence_words(query)
	if not words:
		return "", "", {}
	columns = ["c.title", "c.citation"] + (["c.summary", "c.full_text"] if search_full_text else [])
	params: dict[str, str] = {}
	parts = []
	for index, word in enumerate(words):
		name = f"sentence_word_{index}"
		params[name] = f"%{word}%"
		clause = " OR ".join(f"COALESCE({column}, '') ILIKE :{name}" for column in columns)
		parts.append(f"(CASE WHEN {clause} THEN 1 ELSE 0 END)")
	hits = "(" + " + ".join(parts) + ")"
	needed = max(2, -(-len(words) * 3 // 5))
	return hits, f"{hits} >= {needed}", params
