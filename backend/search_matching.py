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
