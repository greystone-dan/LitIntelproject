"""Second-pass refinement for case citations.

Steps (each can be switched off by name):
  C1_gap_scan     find citation "cores" pass one misses: all Canadian neutral court
                  codes (incl. French CSC/CAF/CF), older reporters (Imm. L.R., F.C.R.,
                  D.L.R., F.T.R., N.R. ...), Quicklaw numbers ([2003] F.C.J. No. 123),
                  R v. / Re / (Re) / French "c." case names, and court docket numbers.
  C2_backrefs     resolve Ibid / Id. / "Name, supra (note 4)" / "Name, above" /
                  "précité" to the case they point back to.
  C3_parallel     join a case name with all of its parallel citations
                  (neutral + S.C.R. + D.L.R. + CanLII) into one row; every citation
                  becomes an identifier for database lookup.
  C4_pinpoints    parse pinpoints into lists ("paras 85-87 and 99" -> 85, 86, 87, 99;
                  "at p. 841"/"at 841" -> page 841).
  C5_validate     check years against each court's neutral-citation start, flag
                  implausible pinpoints, drop self-citations, score confidence.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import dataclass, replace
from datetime import date

from ..citations import CASE_CITATION_KINDS, RawCitationMatch, _extract_short_aliases, extract_raw_citation_matches
from .models import (
	ACTION_ADDED,
	ACTION_CORRECTED,
	ACTION_DROPPED,
	ACTION_KEPT,
	PINPOINT_PARAGRAPH,
	LayerResult,
	Pinpoint,
	RefinedCitation,
)
from .pinpoints import BARE_PAGE_RE, TRAILING_PINPOINT_RE, parse_all_pinpoints, parse_bare_page_pinpoint, parse_pinpoint, pinpoint_phrase

CASE_STEPS = ("C1_gap_scan", "C2_backrefs", "C3_parallel", "C4_pinpoints", "C5_validate")

# --------------------------------------------------------------------------- courts and reporters
# Neutral citation court codes -> first year the code was used (None = no check).
NEUTRAL_COURTS: dict[str, int | None] = {
	"SCC": 2000, "CSC": 2000, "FCA": 2001, "CAF": 2001, "FC": 2001, "CF": 2001, "FCT": 2001, "CFPI": 2001,
	"TCC": 2003, "CCI": 2003, "CMAC": 2001, "CACM": 2001,
	"ABCA": 1998, "ABKB": 2022, "ABQB": 1998, "ABPC": 1998, "ABCJ": 2022,
	"BCCA": 1999, "BCSC": 2000, "BCPC": 1998,
	"MBCA": 2000, "MBKB": 2022, "MBQB": 2000, "MBPC": 2007,
	"NBCA": 2001, "NBKB": 2022, "NBQB": 2001, "NBBR": 2001, "NBPC": 2002,
	"NLCA": 2001, "NLSC": 2018, "NLTD": 2001, "NLPC": 2002,
	"NSCA": 1999, "NSSC": 2000, "NSPC": 2001,
	"NWTCA": 1999, "NWTSC": 1999, "NUCA": 2001, "NUCJ": 2001,
	"ONCA": 2007, "ONSC": 2009, "ONCJ": 2003,
	"PECA": 2000, "PESC": 2000,
	"QCCA": 2001, "QCCS": 2001, "QCCQ": 2001,
	"SKCA": 2000, "SKKB": 2022, "SKQB": 1999, "SKPC": 2002,
	"YKCA": 2000, "YKSC": 2000,
	# Immigration and Refugee Board divisions (pass one already accepts these).
	"IRB": None, "RPD": None, "RAD": None, "IAD": None, "ID": None,
}
FRENCH_TO_ENGLISH_COURT = {"CSC": "SCC", "CAF": "FCA", "CF": "FC", "CFPI": "FCT", "CCI": "TCC", "CACM": "CMAC"}
_FRENCH_COURTS = set(FRENCH_TO_ENGLISH_COURT)

_COURT_ALTERNATION = "|".join(sorted(NEUTRAL_COURTS, key=len, reverse=True))
NEUTRAL_RE = re.compile(rf"(?<![\w/\[(])(?P<year>(?:19|20)\d{{2}})\s+(?P<court>{_COURT_ALTERNATION})\s+(?P<number>\d{{1,5}})\b")
CANLII_RE = re.compile(
	r"(?<![\w/])(?P<year>(?:19|20)\d{2})\s+CanLII\s+(?P<number>\d{1,9})(?:\s*\((?P<court>[A-Za-z][A-Za-z .]{1,20})\))?",
	re.IGNORECASE,
)


@dataclass(frozen=True)
class _Reporter:
	canonical: str
	key: str
	needs_year: bool  # volume numbers restart each year
	french: bool = False


_REPORTERS: tuple[_Reporter, ...] = (
	_Reporter("S.C.R.", "SCR", True),
	_Reporter("R.C.S.", "SCR", True, french=True),
	_Reporter("F.C.R.", "FCR", True),
	_Reporter("F.C.", "FC", True),
	_Reporter("C.F.", "FC", True, french=True),
	_Reporter("Imm. L.R.", "IMMLR", False),
	_Reporter("D.L.R.", "DLR", False),
	_Reporter("F.T.R.", "FTR", False),
	_Reporter("N.R.", "NR", False),
	_Reporter("C.R.R.", "CRR", False),
	_Reporter("Admin. L.R.", "ADMINLR", False),
	_Reporter("C.C.C.", "CCC", False),
	_Reporter("C.R.", "CR", False),
	_Reporter("O.R.", "OR", False),
	_Reporter("A.C.W.S.", "ACWS", False),
	_Reporter("W.C.B.", "WCB", False),
	_Reporter("B.C.L.R.", "BCLR", False),
	_Reporter("A.C.", "AC", True),
	_Reporter("Q.B.", "QB", True),
	_Reporter("W.L.R.", "WLR", False),
	_Reporter("All E.R.", "ALLER", True),
	_Reporter("U.S.", "US", False),
)


def _reporter_fragment(canonical: str) -> str:
	parts: list[str] = []
	for char in canonical:
		if char == ".":
			parts.append(r"\.?\s?")
		elif char == " ":
			parts.append(r"\s*")
		else:
			parts.append(re.escape(char))
	return "".join(parts)


_REPORTER_BY_KEY = {}
_REPORTER_ALTERNATION_PARTS = []
for _index, _reporter in enumerate(sorted(_REPORTERS, key=lambda item: -len(item.canonical))):
	_REPORTER_BY_KEY[f"r{_index}"] = _reporter
	_REPORTER_ALTERNATION_PARTS.append(f"(?P<r{_index}>{_reporter_fragment(_reporter.canonical)})")
_SERIES = r"(?:\(\s*(?P<series>\d{1,2}\s*(?:d|nd|rd|th|st|e)|2d|3d)\s*\))"
REPORTED_RE = re.compile(
	r"(?<![\w/])(?:\[(?P<bracket_year>(?:18|19|20)\d{2})\]|\((?P<paren_year>(?:18|19|20)\d{2})\)\s*,?)?\s*"
	rf"(?P<volume>\d{{1,4}})\s+(?:{'|'.join(_REPORTER_ALTERNATION_PARTS)})\s*{_SERIES}?\s*(?P<page>\d{{1,5}})\b"
)
# Quicklaw / Lexis numbers: [2003] F.C.J. No. 123 (QL), [2003] A.C.F. no 123
_DATABASES = {
	"FCJ": "F.C.J.", "SCJ": "S.C.J.", "ACF": "A.C.F.", "ACS": "A.C.S.", "IADD": "I.A.D.D.", "RPDD": "R.P.D.D.",
	"RADD": "R.A.D.D.", "IDD": "I.D.D.", "CRDD": "C.R.D.D.", "OJ": "O.J.", "BCJ": "B.C.J.", "AJ": "A.J.", "QJ": "Q.J.",
}
_DATABASE_ALTERNATION = "|".join(
	_reporter_fragment(value).rstrip(r"\s?") for value in sorted(_DATABASES.values(), key=len, reverse=True)
)
DATABASE_RE = re.compile(
	rf"\[(?P<year>(?:19|20)\d{{2}})\]\s*(?P<db>{_DATABASE_ALTERNATION})\s*(?:No|no|n[°o])\.?\s*(?P<number>\d{{1,6}})"
	r"(?:\s*\((?:QL|Lexis|QuickLaw)\))?"
)
DOCKET_RE = re.compile(r"(?<![\w-])(?P<docket>(?:IMM|DES|A|T)-\d{1,6}-\d{2})(?![\w-])")

# What may sit between two parallel citations or after the last one.
_TAG = r"\((?:CanLII|QL|Lexis|QuickLaw|[A-Z][A-Za-z.&]{0,6}(?:\s?[A-Z][A-Za-z.&]{0,6}){0,3})\)"
_GAP_PINPOINT = (
	r"(?:,?\s*(?:at|aux?|à)\s+(?:paragraphs?|paras?\.?|par\.?|pp?\.)\s*"
	r"\d{1,5}(?:\s*(?:[-–]|to)\s*\d{1,5})?(?:\s*(?:,|and)\s*\d{1,5}(?:\s*(?:[-–]|to)\s*\d{1,5})?)*?)"
)
# Between parallel citations: a comma, optional court/database tags, optional pinpoint
# ("2004 FC 303 at para 22, 131 A.C.W.S. (3d) 508").
_CHAIN_GAP_RE = re.compile(rf"^\s*(?:{_TAG}\s*)?{_GAP_PINPOINT}?\s*,\s*(?:{_TAG}\s*,?\s*)?$")
_TRAILING_TAG_RE = re.compile(rf"^\s*{_TAG}")
_DECLARED_ALIAS_RE = re.compile(r"^\s*(?:\[\s*(?P<a>[A-Z][A-Za-z .'’\-]{1,60}?)\s*\]|\(\s*[\"“](?P<b>[A-Z][A-Za-z .'’\-]{1,60}?)\s*[\"”]\s*\))")

# --------------------------------------------------------------------------- case names
_CONNECTORS = {"of", "and", "the", "for", "de", "du", "des", "la", "le", "les", "et", "&", "in", "on", "to"}
_NARRATIVE = {
	"see", "in", "cf", "citing", "quoting", "applying", "following", "per", "also", "contra", "compare", "accord",
	"but", "as", "under", "from", "unlike", "like", "distinguishing", "approved", "adopted", "affirmed", "considering",
	"eg", "where", "when", "while", "since", "after", "before", "that", "this", "these", "then", "thus", "however",
	"moreover", "further", "finally", "indeed", "here", "there", "although", "because", "if", "both", "dans", "voir",
	"aussi", "selon", "arrêt", "affaire", "decision", "judgment", "case", "court", "justice", "judge", "held", "found",
}
_ABBREVIATIONS = {"ltd", "inc", "co", "corp", "st", "ste", "mr", "mrs", "ms", "dr", "jr", "sr", "no", "bros"}
_SEPARATOR_RE = re.compile(r"\s(?P<sep>v\.?|vs\.?|c\.)\s")


def _left_party(prefix: str) -> str | None:
	tokens: list[str] = []
	pos = len(prefix)
	while pos > 0 and len(tokens) < 14:
		end = pos
		while end > 0 and prefix[end - 1].isspace():
			end -= 1
		if end == 0:
			break
		if prefix[end - 1] == ")":
			opening = prefix.rfind("(", 0, end - 1)
			if opening < 0 or end - opening > 80:
				break
			tokens.append(prefix[opening:end])
			pos = opening
			continue
		match = re.search(r"[\w'’.&\-]+$", prefix[:end])
		if match is None:
			break
		word = match.group(0)
		stripped = word.strip(".").casefold()
		if word.endswith(".") and tokens and stripped not in _ABBREVIATIONS and len(stripped) > 1:
			break  # "... the Court. Baker v. Canada" -- sentence boundary
		if stripped in _NARRATIVE:
			break
		if word[:1].isupper() or stripped in _CONNECTORS or word == "&":
			tokens.append(word)
			pos = match.start()
			continue
		break
	while tokens and tokens[-1].casefold() in _CONNECTORS:
		tokens.pop()
	if not tokens:
		return None
	return " ".join(reversed(tokens))


def _right_party(value: str) -> str | None:
	value = value.strip().rstrip(",").strip()
	if not value or len(value) > 200 or not value[:1].isupper():
		return None
	if re.search(r"[;\[\]]|\.\s+[A-Z][a-z]+\s+[a-z]", value):
		return None
	# A year, a citation or a narrative word means we ran into an earlier citation:
	# "Jones v. Great Western Railway Co. (1930), 47 T.L.R. 39 ... See also Re Jaballah".
	if re.search(r"\b(?:18|19|20)\d{2}\b|\bat\s+(?:paras?|p{1,2}\.|\d)", value):
		return None
	if any(word.casefold() in {"see", "cf", "also", "citing", "quoting", "voir"} for word in re.findall(r"[A-Za-z]+", value)):
		return None
	if value.count("(") != value.count(")"):
		return None
	return value


@dataclass(frozen=True)
class _Name:
	start: int
	text: str
	normalized: str
	style: str  # "v", "re", "short"
	language: str


# "Re Sheehan and Criminal Injuries Compensation Board", "Singh (Re)"
_RE_PARTY = r"[A-Z][\w'’\-.]*(?:\s+(?:(?:and|of|the|for|de|du|des|la|le|et|&)\s+)?[A-Z][\w'’\-.]*){0,7}"


def _find_case_name(content: str, chain_start: int) -> _Name | None:
	window_start = max(0, chain_start - 260)
	prelude = content[window_start:chain_start]
	if not re.search(r"(?:,|\s)\s*$", prelude) and prelude:
		return None
	separators = list(_SEPARATOR_RE.finditer(prelude))
	for separator in reversed(separators[-2:]):
		right = _right_party(prelude[separator.end() :])
		if right is None:
			continue
		left = _left_party(prelude[: separator.start()])
		if left is None:
			continue
		left_start = prelude.rfind(left.split(" ")[0], 0, separator.start())
		if left_start < 0:
			continue
		sep = separator.group("sep")
		language = "fr" if sep == "c." else "en"
		normalized = f"{' '.join(left.split())} {'c.' if language == 'fr' else 'v.'} {' '.join(right.split())}"
		return _Name(window_start + left_start, prelude[left_start:].rstrip(" ,"), normalized, "v", language)
	re_style = re.search(
		rf"(?:(?<![\w])Re\s+(?P<a>{_RE_PARTY})|(?P<b>{_RE_PARTY})\s*\((?:Re)\)|(?P<c>{_RE_PARTY}),\s+Re)\s*,?\s*$",
		prelude,
	)
	if re_style is not None:
		party = re_style.group("a") or re_style.group("b") or re_style.group("c")
		first = party.split(" ")[0].casefold()
		if first not in _NARRATIVE:
			return _Name(window_start + re_style.start(), re_style.group(0).rstrip(" ,"), f"{party} (Re)", "re", "en")
	short = re.search(r"(?:^|[;(]\s*|(?:See|see|In|in|also|Cf\.?|cf\.?)\s+)(?P<name>[A-Z][\w'’\-]+(?:\s+[A-Z][\w'’\-]+){0,2})\s*,\s*$", prelude)
	if short is not None:
		name = short.group("name")
		if name.split(" ")[0].casefold() not in _NARRATIVE:
			return _Name(window_start + short.start("name"), name, name, "short", "en")
	return None


# --------------------------------------------------------------------------- cores
@dataclass(frozen=True)
class _Core:
	start: int
	end: int
	kind: str  # neutral, canlii, reported, database
	normalized: str
	keys: tuple[str, ...]
	year: int | None
	court: str | None
	language: str
	reporter_needs_year: bool = False


def _neutral_keys(year: str, court: str, number: str) -> tuple[str, ...]:
	english = FRENCH_TO_ENGLISH_COURT.get(court, court)
	keys = [f"{year} {english} {int(number)}"]
	if english == "FC":
		keys.append(f"{year} FCT {int(number)}")
	if english == "FCT":
		keys.append(f"{year} FC {int(number)}")
	return tuple(dict.fromkeys(keys))


def _find_cores(content: str) -> list[_Core]:
	cores: list[_Core] = []
	for match in NEUTRAL_RE.finditer(content):
		year, court, number = match.group("year"), match.group("court"), match.group("number")
		cores.append(
			_Core(
				match.start(),
				match.end(),
				"neutral",
				f"{year} {court} {int(number)}",
				_neutral_keys(year, court, number),
				int(year),
				court,
				"fr" if court in _FRENCH_COURTS else "en",
			)
		)
	for match in CANLII_RE.finditer(content):
		year, number, court = match.group("year"), match.group("number"), match.group("court")
		normalized = f"{year} CanLII {int(number)}" + (f" ({' '.join(court.split())})" if court else "")
		cores.append(_Core(match.start(), match.end(), "canlii", normalized, (f"{year} CANLII {int(number)}",), int(year), "CanLII", "en"))
	for match in REPORTED_RE.finditer(content):
		reporter = next(_REPORTER_BY_KEY[name] for name, value in match.groupdict().items() if name in _REPORTER_BY_KEY and value)
		year = match.group("bracket_year") or match.group("paren_year")
		if reporter.needs_year and not match.group("bracket_year"):
			continue
		volume, page = int(match.group("volume")), int(match.group("page"))
		series = re.sub(r"\s+", "", match.group("series") or "")
		series_text = f" ({series})" if series else ""
		if match.group("bracket_year"):
			normalized = f"[{year}] {volume} {reporter.canonical}{series_text} {page}"
		elif year:
			normalized = f"({year}), {volume} {reporter.canonical}{series_text} {page}"
		else:
			normalized = f"{volume} {reporter.canonical}{series_text} {page}"
		keys = [f"{volume} {reporter.key}{series.upper()} {page}"]
		if year:
			keys.insert(0, f"{year} {volume} {reporter.key}{series.upper()} {page}")
		start = match.start() + (len(match.group(0)) - len(match.group(0).lstrip()))
		cores.append(
			_Core(
				start,
				match.end(),
				"reported",
				normalized,
				tuple(keys),
				int(year) if year else None,
				reporter.canonical,
				"fr" if reporter.french else "en",
				reporter.needs_year,
			)
		)
	for match in DATABASE_RE.finditer(content):
		db_key = re.sub(r"[^A-Z]", "", match.group("db").upper())
		canonical = _DATABASES.get(db_key, match.group("db"))
		number = int(match.group("number"))
		normalized = f"[{match.group('year')}] {canonical} No. {number}"
		cores.append(
			_Core(
				match.start(),
				match.end(),
				"database",
				normalized,
				(f"{match.group('year')} {db_key} {number}",),
				int(match.group("year")),
				canonical,
				"fr" if db_key in {"ACF", "ACS"} else "en",
			)
		)
	# Drop cores contained in a longer core (e.g. "2013 CanLII 1 (FC)" vs "2013 ... FC").
	cores.sort(key=lambda core: (core.start, -(core.end - core.start)))
	kept: list[_Core] = []
	for core in cores:
		if kept and core.start < kept[-1].end:
			continue
		kept.append(core)
	return kept


def _chains(content: str, cores: list[_Core]) -> list[list[_Core]]:
	chains: list[list[_Core]] = []
	for core in cores:
		if chains and _CHAIN_GAP_RE.match(content[chains[-1][-1].end : core.start]):
			chains[-1].append(core)
		else:
			chains.append([core])
	return chains


def identifier_keys(value: str | None) -> tuple[str, ...]:
	"""Lookup keys for every citation core in ``value``.

	Used on both sides of resolution: on refined rows and on ``cases.citation`` /
	``cases.secondary_citation`` when building the lookup index, so keys always match.
	"""
	keys: list[str] = []
	for core in _find_cores(value or ""):
		keys.extend(core.keys)
	return tuple(dict.fromkeys(keys))


# --------------------------------------------------------------------------- building entries
def _trailing_extras(content: str, end: int, last_core: _Core) -> tuple[int, list[Pinpoint], str | None]:
	pinpoints: list[Pinpoint] = []
	alias: str | None = None
	for _ in range(4):
		window = content[end : end + 160]
		tag = _TRAILING_TAG_RE.match(window)
		if tag is not None and not re.match(r"^\s*\(\s*[\"“]", window):
			end += tag.end()
			continue
		pin = TRAILING_PINPOINT_RE.match(window)
		if pin is not None:
			parsed = parse_pinpoint(pin.group("pinpoint"))
			if parsed is not None:
				pinpoints.append(parsed)
				end += pin.end()
				continue
		if last_core.kind == "reported" and not pinpoints:
			bare = BARE_PAGE_RE.match(window)
			parsed_bare = parse_bare_page_pinpoint(window)
			if bare is not None and parsed_bare is not None:
				end += bare.end()
				pinpoints.append(parsed_bare)
				continue
		declared = _DECLARED_ALIAS_RE.match(content[end : end + 96])
		if declared is not None and alias is None:
			alias = " ".join((declared.group("a") or declared.group("b")).split())
			end += declared.end()
			continue
		break
	return end, pinpoints, alias


def _entry_from_chain(content: str, chain: list[_Core], steps: frozenset[str]) -> RefinedCitation:
	first = chain[0]
	name = _find_case_name(content, first.start)
	start = name.start if name is not None else first.start
	cores = chain if "C3_parallel" in steps else chain[:1]
	end, pinpoints, alias = _trailing_extras(content, cores[-1].end, cores[-1])
	for left, right in zip(cores, cores[1:]):
		pinpoints = [*parse_all_pinpoints(content[left.end : right.start]), *pinpoints]
	if "C3_parallel" not in steps and len(chain) > 1:
		end = cores[-1].end
	normalized = name.normalized if name is not None else ""
	for core in cores:
		# "(1995), 30 Imm. L.R. (2d) 1" follows the name without a comma.
		joiner = " " if core.normalized.startswith("(") else ", "
		normalized = f"{normalized}{joiner}{core.normalized}" if normalized else core.normalized
	if pinpoints and "C4_pinpoints" in steps:
		normalized = f"{normalized}, {pinpoint_phrase(pinpoints[0])}"
	notes: list[str] = []
	if name is None:
		kind = "neutral"
		if all(core.kind != "neutral" and core.kind != "canlii" for core in cores):
			notes.append("reporter_only")
		confidence = 0.85
	else:
		kind = "case"
		confidence = 0.95 if name.style != "short" else 0.8
		if name.style == "short":
			notes.append("short_name")
	language = name.language if name is not None and name.language == "fr" else ("fr" if any(core.language == "fr" for core in cores) else "en")
	keys = tuple(dict.fromkeys(key for core in cores for key in core.keys))
	return RefinedCitation(
		kind=kind,
		citation_text=content[start:end],
		normalized_citation=normalized,
		offset_start=start,
		offset_end=end,
		step="C1_gap_scan",
		action=ACTION_ADDED,
		confidence=confidence,
		pinpoint=pinpoint_phrase(pinpoints[0]) if pinpoints else None,
		pinpoints=tuple(pinpoints) if "C4_pinpoints" in steps else (),
		declared_alias=alias,
		case_name=name.normalized if name is not None else None,
		identifiers=keys,
		language=language,
		notes=tuple(notes),
	)


def _from_pass_one(row: RawCitationMatch) -> RefinedCitation:
	confidence = {"case": 0.9, "neutral": 0.9, "case_short": 0.8, "case_name": 0.4}.get(row.kind, 0.5)
	notes = ("name_only",) if row.kind == "case_name" else ()
	return RefinedCitation(
		kind=row.kind,
		citation_text=row.citation_text,
		normalized_citation=row.normalized_citation,
		offset_start=row.offset_start,
		offset_end=row.offset_end,
		step="pass1",
		action=ACTION_KEPT,
		confidence=confidence,
		pinpoint=row.pinpoint,
		anchor_citation_text=row.anchor_citation_text,
		anchor_offset_start=row.anchor_offset_start,
		anchor_offset_end=row.anchor_offset_end,
		declared_alias=row.declared_alias,
		identifiers=identifier_keys(row.normalized_citation) or identifier_keys(row.citation_text),
		notes=notes,
	)


def _base_citation(normalized: str) -> str:
	"""Strip a trailing pinpoint from a normalized citation."""
	return re.sub(r",?\s*(?:at|aux?|à)\s+(?:paras?\.|para\.|pp?\.|par\.|note)\s.*$", "", normalized, flags=re.IGNORECASE).strip()


def _overlap(a: RefinedCitation, b: RefinedCitation) -> bool:
	return not (a.offset_end <= b.offset_start or b.offset_end <= a.offset_start)


def _is_malformed(row: RefinedCitation, cores: list[_Core]) -> bool:
	"""Pass-one rows that a full citation found by this layer may replace even if they stick out.

	Bare names ("Kane v. Board"), and spans that start in the middle of another
	citation ("S.C.R. 1105. Vavilov v. Canada, 2019 CSC 65").
	"""
	if row.kind == "case_name":
		return True
	if not re.match(r"[A-Za-z0-9\[(]", row.citation_text):
		return True
	return any(core.start < row.offset_start < core.end for core in cores)


def _reconcile(entries: list[RefinedCitation], pass_one: list[RefinedCitation], cores: list[_Core] | None = None) -> list[RefinedCitation]:
	cores = cores or []
	result: list[RefinedCitation] = []
	consumed: set[int] = set()
	malformed = {index for index, row in enumerate(pass_one) if _is_malformed(row, cores)}
	for entry in entries:
		overlapping = [index for index, row in enumerate(pass_one) if _overlap(entry, row)]
		if not overlapping:
			result.append(entry)
			continue
		rows = [pass_one[index] for index in overlapping]
		covers = all(
			index in malformed or (entry.offset_start <= pass_one[index].offset_start and pass_one[index].offset_end <= entry.offset_end)
			for index in overlapping
		)
		if not covers:
			# Pass one found a longer span (e.g. a name we did not): keep it, add our identifiers.
			for index in overlapping:
				if index in consumed:
					continue
				row = pass_one[index]
				if row.offset_start <= entry.offset_start and entry.offset_end <= row.offset_end:
					pass_one[index] = replace(
						row,
						identifiers=tuple(dict.fromkeys((*row.identifiers, *entry.identifiers))),
						pinpoints=row.pinpoints or entry.pinpoints,
						language=entry.language,
					)
			continue
		consumed.update(overlapping)
		same_span = len(rows) == 1 and rows[0].offset_start == entry.offset_start and rows[0].offset_end == entry.offset_end
		if same_span and rows[0].kind == entry.kind:
			row = rows[0]
			result.append(
				replace(
					row,
					identifiers=tuple(dict.fromkeys((*row.identifiers, *entry.identifiers))),
					pinpoints=entry.pinpoints,
					case_name=entry.case_name,
					language=entry.language,
					declared_alias=row.declared_alias or entry.declared_alias,
				)
			)
			continue
		step = "C3_parallel" if len(entry.identifiers) > max(len(row.identifiers) for row in rows) else "C1_gap_scan"
		alias = entry.declared_alias or next((row.declared_alias for row in rows if row.declared_alias), None)
		result.append(
			replace(
				entry,
				step=step,
				action=ACTION_CORRECTED,
				declared_alias=alias,
				replaces=tuple((row.offset_start, row.offset_end, row.normalized_citation) for row in rows),
			)
		)
	result.extend(row for index, row in enumerate(pass_one) if index not in consumed)
	result.sort(key=lambda row: (row.offset_start, row.offset_end))
	return result


# --------------------------------------------------------------------------- back-references
_PIN_RANGE = r"\d{1,5}(?!\d|\s+(?-i:[A-Z]))(?:\s*(?:[-–]|to|à)\s*\d{1,5}(?!\d|\s+(?-i:[A-Z])))?"
_PINPOINT_TAIL = (
	r"(?:\s*,?\s*(?:at\s+|aux?\s+|à\s+)?(?:paragraphs?|paras?\.?|par\.?|pp?\.)\s*"
	rf"{_PIN_RANGE}(?:\s*(?:,|and|et|&)\s*{_PIN_RANGE})*)?"
)
IBID_RE = re.compile(rf"(?<![\w.])(?P<word>Ibid(?:em)?\.?|Id\.)(?P<tail>{_PINPOINT_TAIL})", re.UNICODE)
SUPRA_RE = re.compile(
	rf"(?P<name>[A-Z][\w'’\-]+(?:\s+(?:v\.?\s+)?[A-Z][\w'’\-]+){{0,3}})\s*,?\s+"
	rf"(?P<word>supra|above|précitée?s?|ci-dessus)(?P<note>\s*(?:,\s*)?(?:note|n\.)\s*\d{{1,4}})?(?P<tail>{_PINPOINT_TAIL})",
)


def _alias_table(rows: list[RefinedCitation]) -> list[tuple[str, RefinedCitation]]:
	table: list[tuple[str, RefinedCitation]] = []
	for row in rows:
		if row.kind != "case" or not row.case_name:
			continue
		aliases = set(alias.casefold() for alias in _extract_short_aliases(row.case_name))
		if row.declared_alias:
			aliases.add(row.declared_alias.casefold())
		first = re.split(r"\s+(?:v\.|c\.)\s+|\s+\(Re\)", row.case_name)[0]
		aliases.add(first.casefold())
		for alias in aliases:
			if len(alias) >= 3:
				table.append((alias, row))
	return table


def _anchor_for(row: RefinedCitation, rows_by_span: dict[tuple[int, int], RefinedCitation]) -> RefinedCitation:
	"""Follow a short form back to the full citation it points at."""
	if row.kind == "case_short" and row.anchor_offset_start is not None:
		target = rows_by_span.get((row.anchor_offset_start, row.anchor_offset_end or 0))
		if target is not None:
			return target
	return row


def _backref_row(
	content: str, match: re.Match[str], target: RefinedCitation, word: str, step: str
) -> RefinedCitation:
	text = match.group(0).rstrip(" ,")
	end = match.start() + len(text)
	pinpoint = parse_pinpoint(match.group("tail")) if match.group("tail") else None
	base = _base_citation(target.normalized_citation)
	normalized = f"{base}, {pinpoint_phrase(pinpoint)}" if pinpoint else base
	return RefinedCitation(
		kind="case_short",
		citation_text=content[match.start() : end],
		normalized_citation=normalized,
		offset_start=match.start(),
		offset_end=end,
		step=step,
		action=ACTION_ADDED,
		confidence=0.8 if word.lower().startswith(("ibid", "id")) else 0.85,
		pinpoint=pinpoint_phrase(pinpoint) if pinpoint else None,
		pinpoints=(pinpoint,) if pinpoint else (),
		anchor_citation_text=target.citation_text,
		anchor_offset_start=target.offset_start,
		anchor_offset_end=target.offset_end,
		case_name=target.case_name,
		identifiers=target.identifiers,
		notes=(f"backref:{word.strip('.').lower()}",),
	)


_NOTE_MARKER_RE = re.compile(r"\[\d{1,3}\]")
_IBID_RUNNING_TEXT_GAP = 400


def _ibid_follows(content: str, match: re.Match[str], latest: RefinedCitation) -> bool:
	"""True when "Ibid" really refers to ``latest``: that citation is in the note or sentence right before it.

	In an endnote list ("[10] See the record [11] Ibid") the note just before must hold the citation; otherwise
	"Ibid" means whatever that note cites (often a record or an exhibit), not an earlier case. In running text the
	citation must be close behind.
	"""
	markers = list(_NOTE_MARKER_RE.finditer(content, latest.offset_end, match.start()))
	own_marker = bool(markers) and not content[markers[-1].end() : match.start()].strip()
	if own_marker:
		return len(markers) == 1
	return not markers and match.start() - latest.offset_end <= _IBID_RUNNING_TEXT_GAP


def _apply_backrefs(content: str, rows: list[RefinedCitation]) -> list[RefinedCitation]:
	rows_by_span = {(row.offset_start, row.offset_end): row for row in rows}
	table = _alias_table(rows)
	added: list[RefinedCitation] = []
	removed: set[tuple[int, int]] = set()

	def free(start: int, end: int, allow_inside_short: bool) -> tuple[bool, list[RefinedCitation]]:
		inside: list[RefinedCitation] = []
		for row in rows:
			if row.offset_end <= start or end <= row.offset_start:
				continue
			if allow_inside_short and row.kind in {"case_short", "case_name"} and start <= row.offset_start and row.offset_end <= end:
				inside.append(row)
				continue
			return False, []
		for row in added:
			if not (row.offset_end <= start or end <= row.offset_start):
				return False, []
		return True, inside

	ordered = sorted(rows, key=lambda row: row.offset_start)
	for match in IBID_RE.finditer(content):
		ok, _inside = free(match.start(), match.end(), allow_inside_short=False)
		if not ok:
			continue
		previous = [row for row in ordered if row.offset_end <= match.start() and row.kind in CASE_CITATION_KINDS and row.kind != "case_name"]
		previous += [row for row in added if row.offset_end <= match.start()]
		if not previous:
			continue
		latest = max(previous, key=lambda row: row.offset_end)
		if not _ibid_follows(content, match, latest):
			continue
		target = _anchor_for(latest, rows_by_span)
		added.append(_backref_row(content, match, target, match.group("word"), "C2_backrefs"))

	for match in SUPRA_RE.finditer(content):
		name = match.group("name")
		words = name.split()
		# Allow "See Vavilov, supra": drop leading narrative words.
		while words and words[0].casefold() in {"see", "in", "also", "cf", "per", "voir"}:
			words = words[1:]
		if not words:
			continue
		key = " ".join(words).casefold()
		candidates = [
			(alias, row)
			for alias, row in table
			if row.offset_end <= match.start() and (alias == key or alias == words[-1].casefold() or key.startswith(alias))
		]
		if not candidates:
			continue
		target = max(candidates, key=lambda item: item[1].offset_end)[1]
		start = match.start("name") + len(name) - len(" ".join(words))
		ok, inside = free(start, match.end(), allow_inside_short=True)
		if not ok:
			continue
		# Re-match from the first kept word so the span excludes "See".
		synthetic = SUPRA_RE.match(content, start)
		if synthetic is None:
			continue
		row = _backref_row(content, synthetic, target, match.group("word"), "C2_backrefs")
		if inside:
			removed.update((item.offset_start, item.offset_end) for item in inside)
			row = replace(
				row,
				action=ACTION_CORRECTED,
				replaces=tuple((item.offset_start, item.offset_end, item.normalized_citation) for item in inside),
			)
		added.append(row)

	result = [row for row in rows if (row.offset_start, row.offset_end) not in removed]
	result.extend(added)
	result.sort(key=lambda row: (row.offset_start, row.offset_end))
	return result


# --------------------------------------------------------------------------- pinpoints and validation
def _with_pinpoints(content: str, row: RefinedCitation) -> RefinedCitation:
	if row.pinpoints:
		return row
	pinpoints = list(parse_all_pinpoints(row.citation_text))
	if not pinpoints and row.identifiers:
		bare = parse_bare_page_pinpoint(content[row.offset_end : row.offset_end + 40])
		if bare is not None and re.search(r"\b(?:SCR|FCR|FC|DLR|IMMLR)\b", " ".join(row.identifiers)):
			pinpoints.append(bare)
	if not pinpoints:
		return row
	return replace(row, pinpoints=tuple(pinpoints), pinpoint=row.pinpoint or pinpoint_phrase(pinpoints[0]))


def _validate(row: RefinedCitation, current_year: int, self_keys: set[str]) -> RefinedCitation | None:
	if self_keys and row.kind in {"case", "neutral"} and set(row.identifiers) & self_keys:
		return None
	notes = list(row.notes)
	confidence = row.confidence
	for match in NEUTRAL_RE.finditer(row.normalized_citation):
		year, court = int(match.group("year")), match.group("court")
		first_year = NEUTRAL_COURTS.get(court)
		if year > current_year or (first_year is not None and year < first_year):
			notes.append(f"implausible_year:{year} {court}")
			confidence = min(confidence, 0.4)
		if court == "FCT" and year > 2003:
			notes.append("fct_after_2003")
			confidence = min(confidence, 0.5)
	for pinpoint in row.pinpoints:
		if pinpoint.kind == PINPOINT_PARAGRAPH and max(pinpoint.values) > 1500:
			notes.append("pinpoint_suspicious")
			confidence = min(confidence, 0.5)
		if pinpoint.truncated:
			notes.append("pinpoint_truncated")
	if row.kind == "case_name" and re.search(r"\n", row.citation_text):
		return None
	if tuple(notes) == row.notes and confidence == row.confidence:
		return row
	return replace(row, notes=tuple(dict.fromkeys(notes)), confidence=confidence)


# --------------------------------------------------------------------------- own dockets
_DOCKET_PART_RE = re.compile(r"(?<![\w-])(?P<court>IMM|DES|A|T)-(?P<number>\d{1,6})(?:-(?P<year>\d{2}))?(?![\w-])")
_DOCKET_LIST_GAP_RE = re.compile(r"[\s,;]*(?:(?:and|et|&)[\s,;]*)?")


def _own_docket_keys(source_dockets: Iterable[str | None]) -> list[tuple[str, str, str | None]]:
	"""Own docket numbers as (court, number, year). The stored year is optional ("T-1053" or "T-1053-02")."""
	return [
		(match.group("court"), match.group("number"), match.group("year"))
		for value in source_dockets
		for match in _DOCKET_PART_RE.finditer(value or "")
	]


def _own_docket_matches(content: str, source_dockets: Iterable[str | None]) -> set[int]:
	"""Start offsets of docket numbers in ``content`` that belong to the decision itself.

	Stored dockets are missing for some courts (Federal Court of Appeal and tribunal decisions), so a number printed
	after a docket label in the decision's header also counts. A match is the decision's own when it equals a stored docket (ignoring the year when the stored one has none) or
	sits in the same unbroken list of docket numbers as such a match, as in the header of a consolidated decision. Every other
	occurrence of those numbers in the text (the per-party "Docket:" blocks) is the decision's own as well.
	"""
	keys = _own_docket_keys(source_dockets)
	matches = list(DOCKET_RE.finditer(content))
	if not matches:
		return set()
	owned = [
		any(
			(court, number) == (key[0], key[1]) and (key[2] is None or key[2] == year)
			for key in keys
			for court, number, year in [_docket_parts(match.group("docket"))]
		)
		or _labelled_header_docket(content, match)
		for match in matches
	]
	runs: list[list[int]] = [[0]] if matches else []
	for index in range(1, len(matches)):
		gap = content[matches[index - 1].end() : matches[index].start()]
		if _DOCKET_LIST_GAP_RE.fullmatch(gap):
			runs[-1].append(index)
		else:
			runs.append([index])
	own_numbers: set[str] = set()
	for run in runs:
		if any(owned[index] for index in run):
			own_numbers.update(matches[index].group("docket") for index in run)
	# A consolidated decision repeats each of its dockets in a per-party "Docket:" block further down.
	return {match.start() for match in matches if match.group("docket") in own_numbers}


_DOCKET_LABEL_BEFORE_RE = re.compile(
	r"(?:dockets?|file\s+numbers?|file\s+nos?\.?|court\s+file(?:\s+nos?\.?)?|consolidated\s+files)\s*[:.]?\s*(?:\(consolidated\s+files\s*)?[:.]?\s*$",
	re.IGNORECASE,
)
_HEADER_WORD_AFTER_RE = re.compile(r"\s*(?:neutral\s+citation|citation|coram|between|style\s+of\s+cause|place\s+of\s+hearing)", re.IGNORECASE)
_HEADER_CHARS = 4000


def _labelled_header_docket(content: str, match: re.Match[str]) -> bool:
	"""A docket printed right after "Docket:" / "File numbers" / "Court File No." in the decision's header block."""
	label = _DOCKET_LABEL_BEFORE_RE.search(content[max(0, match.start() - 45) : match.start()])
	if label is None:
		return False
	# "..., and in Court File No. T-1747-00, we rely on" is a reference in running text; a header label starts a line or
	# follows a capitalised word.
	before_label = content[max(0, match.start() - 45) : match.start()][: label.start()].rstrip(" \t")
	if before_label and before_label[-1].islower():
		return False
	if match.start() < _HEADER_CHARS:
		return True
	# Counsel-page layout at the end ("DOCKET: A-413-00  STYLE OF CAUSE: ...") or a header-less text window.
	return bool(_HEADER_WORD_AFTER_RE.match(content, match.end()))


def _docket_parts(docket: str) -> tuple[str, str, str]:
	court, number, year = docket.split("-")
	return court, number, year


# --------------------------------------------------------------------------- entry point
def refine_case_citations(
	text: str | None,
	pass_one_rows: list[RawCitationMatch] | None = None,
	steps: Iterable[str] | None = None,
	source_citations: Iterable[str | None] = (),
	include_dockets: bool = True,
	current_year: int | None = None,
	source_dockets: Iterable[str | None] | None = None,
) -> LayerResult:
	"""Run the case refinement layer over a whole decision.

	``pass_one_rows`` defaults to ``extract_raw_citation_matches(text)`` (only the
	case kinds and S.C.R. "secondary" rows are used). ``source_citations`` are the
	decision's own citations; matching rows are dropped as self-citations.
	``source_dockets`` are the decision's own docket numbers (pass it, even empty, to skip own dockets); docket rows that are
	one of them, or sit in the same header list of consolidated dockets, are skipped.
	"""
	content = text or ""
	enabled = frozenset(CASE_STEPS if steps is None else steps)
	if not content.strip():
		return LayerResult(rows=[], steps_run=tuple(step for step in CASE_STEPS if step in enabled))
	if pass_one_rows is None:
		pass_one_rows = extract_raw_citation_matches(content)
	year_limit = current_year or date.today().year

	pass_one = [_from_pass_one(row) for row in pass_one_rows if row.kind in CASE_CITATION_KINDS or row.kind == "secondary"]
	# S.C.R. pinpoint "secondary" rows are case citations without a name; treat as neutral-like.
	pass_one = [replace(row, kind="neutral", notes=(*row.notes, "reporter_only")) if row.kind == "secondary" else row for row in pass_one]

	rows = pass_one
	if "C1_gap_scan" in enabled or "C3_parallel" in enabled:
		cores = _find_cores(content)
		chains = _chains(content, cores)
		entries = [_entry_from_chain(content, chain, enabled) for chain in chains]
		if "C1_gap_scan" not in enabled:
			# Parallel joining only: improve rows pass one already found.
			entries = [entry for entry in entries if any(_overlap(entry, row) for row in pass_one)]
		rows = _reconcile(entries, list(pass_one), cores)
	if include_dockets and "C1_gap_scan" in enabled:
		# Passing ``source_dockets`` (even empty) opts in to own-docket skipping; without it every docket is a row.
		own_dockets = _own_docket_matches(content, source_dockets) if source_dockets is not None else set()
		for match in DOCKET_RE.finditer(content):
			if match.start() in own_dockets:
				continue
			if any(not (match.end() <= row.offset_start or row.offset_end <= match.start()) for row in rows):
				continue
			rows.append(
				RefinedCitation(
					kind="docket",
					citation_text=match.group(0),
					normalized_citation=match.group("docket"),
					offset_start=match.start(),
					offset_end=match.end(),
					step="C1_gap_scan",
					action=ACTION_ADDED,
					confidence=0.9,
					identifiers=(match.group("docket"),),
				)
			)
		rows.sort(key=lambda row: (row.offset_start, row.offset_end))

	if "C2_backrefs" in enabled:
		rows = _apply_backrefs(content, rows)
	if "C4_pinpoints" in enabled:
		rows = [_with_pinpoints(content, row) for row in rows]

	dropped: list[RefinedCitation] = []
	if "C5_validate" in enabled:
		self_keys: set[str] = set()
		for value in source_citations:
			self_keys.update(identifier_keys(value))
		validated: list[RefinedCitation] = []
		for row in rows:
			checked = _validate(row, year_limit, self_keys)
			if checked is None:
				reason = "self_citation" if set(row.identifiers) & self_keys else "noise"
				dropped.append(replace(row, step="C5_validate", action=ACTION_DROPPED, confidence=0.0, notes=(*row.notes, reason)))
			else:
				validated.append(checked)
		rows = validated
	return LayerResult(rows=rows, dropped=dropped, steps_run=tuple(step for step in CASE_STEPS if step in enabled))


__all__ = ["CASE_STEPS", "identifier_keys", "refine_case_citations"]
