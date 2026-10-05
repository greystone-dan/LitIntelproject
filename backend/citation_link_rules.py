"""Exact-key rules for linking stored citation rows to library cases.

Every key is built the same way for the cited text and for the library case's
own citation fields, so a link needs both sides to agree on the full key (year,
volume, reporter, page or court, number). Nothing here guesses from names alone:
a name is only used to break a tie between cases that share a key, or to reject
a new-rule link whose target title shares nothing with the cited name.

This module is pure (no database access); the scripts feed it rows.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Iterable

LIBRARY_COURTS = frozenset({"FC", "FCT", "FCA", "SCC"})
FRENCH_COURT_MAP = {"CSC": "SCC", "CAF": "FCA", "CF": "FC", "CFPI": "FCT"}
REPORTER_ALIASES = {"RCS": "SCR", "RCF": "FC", "FCR": "FC"}
YEAR_ONLY_SCR_LAST_YEAR = 1984
NOT_A_COURT = frozenset({"SCR", "RCS", "FCR", "RCF", "NR", "DLR", "CCC", "FTR", "CPR", "ACWS", "WWR", "BCLR", "CRR", "OR", "AR", "SR", "CR", "QB", "KB"})

NEUTRAL_RE = re.compile(
	r"(?<![A-Za-z0-9])(?:\[)?((?:19|20)\d{2})(?:\])?\s+(CanLII|[A-Z]{1,8})\s+(\d{1,7})\b"
)
REPORTER_RE = re.compile(
	r"(?:\[((?:19|20)\d{2})\]|\(((?:19|20)\d{2})\)|(?<![\d\w])((?:19|20)\d{2}))\s*,?\s*"
	r"(?:(\d{1,3})\s+)?"
	r"((?:[A-Z]\.?){2,6})\s*"
	r"(?:\((\d)(?:st|nd|rd|th|d)\)\s*)?"
	r"(\d{1,7})\b"
)
DOCKET_RE = re.compile(r"\b(?:IMM|IAD|T|A|DES|ITA)-\d{1,6}-\d{2,4}\b|\bTB\d-\d{4,6}\b|\bMB\d-\d{4,6}\b", re.IGNORECASE)
BACK_REFERENCE_RE = re.compile(r"\b(?:ibid|ibidem|idem|supra|above|ci-dessus|précité)\b", re.IGNORECASE)
UNKEYABLE_REPORTER_RE = re.compile(r"\b\d{1,3}\s+[A-Z]{2,6}\s*(?:\(\d(?:st|nd|rd|th|d|e)\)\s*)?\d{1,5}\b")
CONNECTOR_RE = re.compile(r"\s+(?:v\.?|vs\.?|c\.?|versus)\s+", re.IGNORECASE)
_TITLE_STOPWORDS = frozenset(
	{
		"canada", "minister", "citizenship", "immigration", "attorney", "general", "the", "and", "des", "du",
		"for", "of", "ministre", "procureur", "general", "her", "his", "majesty", "queen", "king", "regina",
	}
)


@dataclass(frozen=True)
class Key:
	value: str
	family: str  # neutral_en | neutral_fr | reporter | reporter_alias | reporter_year_only | reporter_series


@dataclass
class Resolution:
	target_case_id: int | None = None
	rule: str | None = None
	reason: str | None = None  # why not: self | ambiguous | conflict | name_mismatch | no_hit | no_key
	keys: list[Key] = field(default_factory=list)


def _clean_reporter(value: str) -> str:
	return re.sub(r"[^A-Z0-9]", "", value.upper())


def keys_for(text: str | None) -> list[Key]:
	"""All lookup keys a citation string offers, strongest family first."""
	if not text:
		return []
	keys: list[Key] = []
	seen: set[str] = set()

	def add(value: str, family: str) -> None:
		if value not in seen:
			seen.add(value)
			keys.append(Key(value, family))

	for match in NEUTRAL_RE.finditer(text):
		year, court, number = match.group(1), match.group(2).upper(), int(match.group(3))
		if court in NOT_A_COURT:
			continue
		family = "neutral_en"
		if court in FRENCH_COURT_MAP:
			court, family = FRENCH_COURT_MAP[court], "neutral_fr"
		add(f"{year} {court} {number}", family)
		if court == "FCT":
			add(f"{year} FC {number}", family)
		elif court == "FC":
			add(f"{year} FCT {number}", family)

	for match in REPORTER_RE.finditer(text):
		year = match.group(1) or match.group(2) or match.group(3)
		volume, raw_reporter, series, page = match.group(4), match.group(5), match.group(6), int(match.group(7))
		reporter = _clean_reporter(raw_reporter)
		family = "reporter"
		if reporter in REPORTER_ALIASES:
			reporter, family = REPORTER_ALIASES[reporter], "reporter_alias"
		if reporter == "SCR" and volume is None:
			if int(year) > YEAR_ONLY_SCR_LAST_YEAR:
				continue
			add(f"{year} SCR {page}", "reporter_year_only")
			continue
		if volume is None:
			continue
		suffix = f"{series}" if series else ""
		add(f"{year} {int(volume)} {reporter}{suffix} {page}", "reporter_series" if series else family)
	return keys


class CaseKeyIndex:
	"""key -> case ids, built from each case's own citation fields."""

	def __init__(self) -> None:
		self.by_key: dict[str, set[int]] = {}
		self.titles: dict[int, str] = {}

	def add_case(self, case_id: int, title: str | None, *citations: str | None) -> None:
		self.titles[case_id] = title_key(title)
		for citation in citations:
			for key in keys_for(citation):
				self.by_key.setdefault(key.value, set()).add(case_id)


def title_key(value: str | None) -> str:
	text = (value or "").casefold().replace("’", "'").replace("–", "-")
	text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
	return " ".join(text.split())


def cited_name_key(text: str | None) -> str:
	"""The case-name part of a citation string (text before the first year/reporter), normalised."""
	raw = " ".join((text or "").split())
	cut = re.search(r"(?:\[|\()?(?:19|20)\d{2}(?:\]|\))?\s*,?\s*(?:\d{1,3}\s+)?[A-Z]", raw)
	name = raw[: cut.start()] if cut else raw
	name = re.sub(r"[,;:\s]+$", "", name)
	return title_key(name) if CONNECTOR_RE.search(name) else ""


def _name_tokens(value: str) -> set[str]:
	return {token for token in value.split() if len(token) >= 4 and token not in _TITLE_STOPWORDS and not token.isdigit()}


def names_compatible(cited_name: str, target_title: str) -> bool:
	"""True when there is no cited name to check, or it shares a distinctive word with the title."""
	if not cited_name or not target_title:
		return True
	cited, target = _name_tokens(cited_name), _name_tokens(target_title)
	if not cited or not target:
		return True
	return bool(cited & target)


def resolve_row(text: str | None, source_case_id: int | None, index: CaseKeyIndex) -> Resolution:
	keys = keys_for(text)
	if not keys:
		return Resolution(reason="no_key")
	hits: dict[int, list[Key]] = {}
	self_hit = False
	for key in keys:
		for case_id in index.by_key.get(key.value, ()):
			if case_id == source_case_id:
				self_hit = True
				continue
			hits.setdefault(case_id, []).append(key)
	if not hits:
		return Resolution(reason="self" if self_hit else "no_hit", keys=keys)
	cited_name = cited_name_key(text)
	if len(hits) > 1:
		confirmed = [case_id for case_id in hits if cited_name and index.titles.get(case_id) == cited_name]
		if len(confirmed) == 1:
			return Resolution(confirmed[0], "ambiguous_title_confirmed", keys=keys)
		return Resolution(reason="ambiguous", keys=keys)
	(case_id, matched), = hits.items()
	rule = matched[0].family
	if rule != "neutral_en" and not names_compatible(cited_name, index.titles.get(case_id, "")):
		return Resolution(reason="name_mismatch", keys=keys)
	return Resolution(case_id, rule, keys=keys)


def classify_unresolved(
	text: str | None,
	kind: str | None,
	source_case_id: int | None,
	index: CaseKeyIndex,
	title_counts: dict[str, int] | None = None,
) -> tuple[str, str | None]:
	"""Return (bucket, detail) explaining one unresolved row. Buckets starting 'would_link:' are gains."""
	resolution = resolve_row(text, source_case_id, index)
	if resolution.target_case_id is not None:
		return f"would_link:{resolution.rule}", None
	if resolution.reason in {"ambiguous", "self", "name_mismatch"}:
		return {"ambiguous": "ambiguous_key", "self": "self_citation", "name_mismatch": "name_mismatch_rejected"}[resolution.reason], None
	raw = text or ""
	if resolution.keys:
		neutral = [key for key in resolution.keys if key.family.startswith("neutral")]
		if neutral:
			court = neutral[0].value.split()[1]
			if court in LIBRARY_COURTS:
				return "neutral_library_court_not_in_library", court
			if court == "CANLII":
				return "canlii_cite_not_in_library", court
			return "neutral_other_court", court
		return "reporter_cite_not_in_library", resolution.keys[0].value.split()[-2]
	if BACK_REFERENCE_RE.search(raw):
		return "back_reference", None
	if DOCKET_RE.search(raw):
		return "docket_only", None
	if UNKEYABLE_REPORTER_RE.search(raw):
		return "reporter_unkeyable", None
	name = cited_name_key(raw) or (title_key(raw) if kind in {"case_name", "case_short"} else "")
	if name:
		count = (title_counts or {}).get(name, 0)
		if count == 0:
			return "name_only_not_in_library", None
		return ("name_only_title_unique" if count == 1 else "name_only_ambiguous"), None
	return "other", None


def title_counts_for(index: CaseKeyIndex) -> dict[str, int]:
	counts: dict[str, int] = {}
	for value in index.titles.values():
		if value:
			counts[value] = counts.get(value, 0) + 1
	return counts


def build_index(rows: Iterable[tuple[int, str | None, str | None, str | None]]) -> CaseKeyIndex:
	index = CaseKeyIndex()
	for case_id, title, citation, secondary in rows:
		index.add_case(case_id, title, citation, secondary)
	return index
