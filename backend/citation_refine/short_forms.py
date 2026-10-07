"""Reject pass-one short forms whose alias cannot be a name of the case they were anchored to.

Pass one turns a capitalised word near an earlier full citation into a short form of that citation. On real decisions
this produced rows such as "Lake" -> "Lake City Casinos", "Nation" -> "Standingready v. Ocean Man First Nation", "Bank" ->
"Royal Bank of Canada v. Radius Credit Union" or "connection" -> "Venngo Inc v. Concierge Connection", and a footnote note
("actuellement disponible seulement en anglais") anchored to a case. A short form is only kept when its alias appears as whole words in one of the anchor's party names (or of a parenthetical alias in it), is capitalised, and is not a generic word.
Short forms the decision defines itself ("[Vavilov]") are always kept.
"""

from __future__ import annotations

import re

from .models import RefinedCitation

_GENERIC = frozenset(
	{
		"bank", "estate", "nation", "home", "investments", "investment", "company", "corporation", "corp", "trust", "fund", "group",
		"holdings", "society", "association", "minister", "canada", "court", "crown", "queen", "king", "city", "county",
		"commission", "council", "authority", "services", "industries", "limited", "ltd", "inc", "co", "national", "general",
		"attorney", "citizenship", "immigration", "refugee", "province", "state", "united", "the", "la", "le", "les", "de", "du", "service", "services", "band", "companies", "associated", "judgment", "international",
		"refugees", "employment", "marine", "revenue", "public", "commissioner", "ontario", "alberta", "quebec", "board", "union", "school", "centre", "center",
	}
)
_NAME_END_RE = re.compile(r",\s*(?:\[|\(|(?:19|20)\d\d|\d+\s+[A-Z]|at\s|à\s|au\s|aux\s)")
_PARTY_SPLIT_RE = re.compile(r"\s+(?:v\.?|c\.?|vs\.?)\s+", re.IGNORECASE)
_PINPOINT_START_RE = re.compile(r"\s*,?\s*(?:\(|\[|at\s|à\s|au\s|aux\s|,|;|supra\b|above\b|précité)", re.IGNORECASE)


def _words(value: str) -> list[str]:
	value = value.replace("\u2010", "-").replace("\u2011", "-").replace("\u2012", "-")
	return [word.strip("'’-") for word in re.findall(r"[\w'’-]+", value.casefold()) if word.strip("'’-")]


def _without_article(tokens: list[str]) -> list[str]:
	return tokens[1:] if tokens and tokens[0] in {"the", "le", "la", "les", "l"} else tokens


def alias_of(row: RefinedCitation) -> str:
	text = " ".join((row.citation_text or "").replace("\n", " ").split())
	text = re.sub(r"^\(\s*(?:(?:see|voir|cf\.?)\s+)?", "", text, flags=re.IGNORECASE)
	match = _PINPOINT_START_RE.search(text)
	alias = (text[: match.start()] if match else text).strip(" ,;:()[]")
	return re.sub(r"\s+(?:FCA|FC|FCT|SCC|CAF|CF|CSC)$", "", alias)


_TITLE_BLOCK_RE = re.compile(r"^[A-Z][A-Z .,'’-]+(?:\s+et al\.?)?\s+v\.?\s+(?:THE|ATTORNEY|MCI|M\.C\.?I?\.?|MINISTER|SECRETARY)\b", re.UNICODE)
_FOOTNOTE_ARTIFACT_RE = re.compile(r"\[\d+\s*$")


def _weak_case_name(row: RefinedCitation) -> bool:
	"""Name-only rows that are a title block party line ("JUNIOR HERMAN v. THE") or a footnote artifact ("Hall v. Hill[3")."""
	text = " ".join((row.citation_text or "").split())
	return bool(_FOOTNOTE_ARTIFACT_RE.search(text) or _TITLE_BLOCK_RE.match(text))


def is_weak_short_form(row: RefinedCitation) -> bool:
	if row.kind == "case_name" and row.step == "pass1":
		return _weak_case_name(row)
	if row.kind != "case_short" or row.step != "pass1" or row.declared_alias:
		return False
	alias = alias_of(row)
	words = _words(alias)
	if not words:
		return True
	if not any(char.isupper() for char in alias):
		return True
	if len(words) == 1 and words[0] in _GENERIC:
		return True
	name = _NAME_END_RE.split(row.normalized_citation or "", maxsplit=1)[0]
	parties = [part.strip() for part in _PARTY_SPLIT_RE.split(name) if part.strip()]
	if len(parties) < 2:
		return False  # not enough structure to judge; keep
	candidates = [_without_article(_words(party)) for party in parties]
	for party in parties:
		for inner in re.findall(r"\(([^)]*)\)", party):
			candidates.append(_words(inner))
	size = len(words)
	return not any(
		tokens[start : start + size] == words for tokens in candidates for start in range(max(len(tokens) - size + 1, 0))
	)
