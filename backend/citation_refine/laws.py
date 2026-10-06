"""Second-pass refinement for statute and treaty references.

Steps (each can be switched off by name):
  L1_definitions  work out what "the Act", "the Regulations", "[IRPA]" mean from the
                  whole decision; replace pass-one junk rows such as "of the Act".
  L2_gap_scan     new patterns: "s. 112 of the Act", "r. 117(9)(d) IRPR",
                  "Rule 9 of the ... Rules", French "article 25 de la LIPR", "art 1E".
  L3_expand       split lists and ranges ("ss. 96, 97", "ss. 112 to 114",
                  "36(1)(a) and (b)") into one row per provision.
  L4_registry     identify instruments with the extended registry (more laws,
                  French names) instead of pass one's registry alone.
  L5_validate     drop rows with no instrument and no provision; flag provision
                  numbers outside the instrument's known range; score confidence.
"""

from __future__ import annotations

import re
import string
from collections.abc import Iterable
from dataclasses import replace

from ..citations import RawCitationMatch, extract_statute_reference_matches
from ..statutes import LEGISLATION_REGISTRY
from .context import DocumentContext, normalize_term
from .instruments import INSTRUMENT_ALIAS_PATTERN, REGISTRY, Instrument, identify_instrument, lookup_alias
from .models import (
	ACTION_ADDED,
	ACTION_CORRECTED,
	ACTION_DROPPED,
	ACTION_EXPANDED,
	ACTION_KEPT,
	LayerResult,
	RefinedStatuteReference,
)

LAW_STEPS = ("L1_definitions", "L2_gap_scan", "L3_expand", "L4_registry", "L5_validate")

MAX_RANGE_EXPANSION = 30

# Highest provision number per instrument, for sanity checks (decimals like 25.1 allowed).
KNOWN_MAX_PROVISION = {
	"canada.irpa": 275,
	"canada.irpr": 365,
	"canada.charter": 34,
	"international.refugee_convention": 46,
	"canada.fc_cirp_rules": 22,
	"canada.rpd_rules": 74,
	"canada.rad_rules": 53,
	"canada.federal_courts_act": 61,
	"canada.citizenship_act": 46,
}

# French drafting writes paragraphs as "36(1)a)" and subparagraphs as "a)(i)".
_PROVISION = r"\d{1,3}(?:\.\d{1,3})?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9.]{1,6}\s*\))*(?:[a-z]{1,4}\)(?:\([ivx]{1,5}\))?)?"
_SIBLING = r"(?:\(\s*[A-Za-z0-9.]{1,6}\s*\)(?:\s*\(\s*[A-Za-z0-9.]{1,6}\s*\))*|[a-z]{1,4}\)(?!\w))"
_SEPARATOR = r"(?:\s*,\s*(?:and|or|et|ou)?\s*|\s+(?:and|or|to|through|et|ou|à)\s+|\s*[-–]\s*)"
_PROVISION_LIST = rf"{_PROVISION}(?:{_SEPARATOR}(?:{_PROVISION}|{_SIBLING}))*+"

_EN_LABEL = (
	r"(?:sub-?sections?|subss?\.|subs\.|sub-?paragraphs?|subparas?\.|paragraphs?|paras?\.|"
	r"sections?|ss\.?|s\.|s(?=\s+\d)|rules?|rr?\.|r(?=\s+\d)|articles?|arts?\.?|clauses?|cl\.)"
)
_FR_LABEL = r"(?:articles?|art\.?|paragraphes?|par\.|alinéas?|al\.|sous-alinéas?|ss-al\.)"
_GENERIC_EN = r"(?-i:Act|Regulations|Rules|Convention|Charter)"
_GENERIC_FR = r"(?-i:Loi|Règlement|Règles|Convention|Charte)"
_INSTRUMENT_TAIL = (
	r"(?:,?\s*(?:S\.?C\.?|R\.?S\.?C\.?|L\.?C\.?|L\.?R\.?C\.?)\s*,?\s*\d{4}\s*,?\s*c\.?\s*[A-Z0-9.\-]+(?:\s*\([^)]{0,20}\))?"
	r"|,?\s*(?:SOR|DORS)\s*/\s*\d{2,4}-\d+)?"
)
_NOT_A_NAME_CONTINUATION = r"(?![\w-])(?!\s+(?:to|respecting|for|of\s+\d{4})\b)"

# "s. 112 of the Act", "paragraph 36(1)(a) of IRPA", "Rule 9 of the Federal Courts ... Rules"
PROVISION_OF_INSTRUMENT_RE = re.compile(
	rf"(?<![\w.])(?P<label>{_EN_LABEL})\s*(?P<prov>{_PROVISION_LIST})\s+(?:of|under|in)\s+(?:the\s+)?"
	rf"(?:(?P<inst>{INSTRUMENT_ALIAS_PATTERN})(?![\w'’])|(?P<generic>{_GENERIC_EN}){_NOT_A_NAME_CONTINUATION})",
	re.IGNORECASE,
)
# "IRPA, s 97", "the Act, s. 25(1)", "Immigration and Refugee Protection Act, S.C. 2001, c. 27, s. 96"
INSTRUMENT_THEN_PROVISION_RE = re.compile(
	rf"(?:(?P<inst>{INSTRUMENT_ALIAS_PATTERN})(?![\w'’])|\bthe\s+(?P<generic>{_GENERIC_EN})(?![\w-]))"
	rf"{_INSTRUMENT_TAIL}\s*,?\s*(?P<label>{_EN_LABEL})\s*(?P<prov>{_PROVISION_LIST})",
	re.IGNORECASE,
)
# "r. 117(9)(d) IRPR", "s. 97 IRPA"
PROVISION_THEN_ACRONYM_RE = re.compile(
	rf"(?<![\w.])(?P<label>{_EN_LABEL}|{_FR_LABEL})\s*(?P<prov>{_PROVISION_LIST})\s*,?\s+(?P<inst>(?-i:IRPA|IRPR|LIPR|RIPR))\b",
	re.IGNORECASE,
)
# "l'article 25 de la LIPR", "alinéa 36(1)a) du Règlement"
FRENCH_PROVISION_RE = re.compile(
	rf"(?<![\w.])(?P<label>{_FR_LABEL})\s*(?P<prov>{_PROVISION_LIST})\s+"
	rf"(?:de\s+la\s+|du\s+|de\s+l['’]\s*|des\s+|de\s+)"
	rf"(?:(?P<inst>{INSTRUMENT_ALIAS_PATTERN})(?![\w'’])|(?P<generic>{_GENERIC_FR})(?![\w-]))",
	re.IGNORECASE,
)
# "art 1E", "Article 1F(b)", "article 33(1)" with no instrument named.
REFUGEE_ARTICLE_RE = re.compile(
	r"(?<![\w.])(?:art\.?|article)\s*(?P<prov>1\s*[EF](?:\s*\(\s*[a-cA-C]\s*\)|[a-cA-C](?![a-z]))?|33(?:\s*\(\s*[12]\s*\))?)(?![\w(])",
	re.IGNORECASE,
)

_GAP_PATTERNS: tuple[tuple[str, re.Pattern[str], int], ...] = (
	("provision_of_instrument", PROVISION_OF_INSTRUMENT_RE, 4),
	("french_provision", FRENCH_PROVISION_RE, 4),
	("instrument_then_provision", INSTRUMENT_THEN_PROVISION_RE, 3),
	("provision_then_acronym", PROVISION_THEN_ACRONYM_RE, 3),
	("refugee_article", REFUGEE_ARTICLE_RE, 1),
)

# Provisions inside a pass-one normalized citation ("... ss. 96, 97", "art. 1F(b) of ...").
_NORMALIZED_PROVISION_RE = re.compile(
	rf"(?<![\w.])(?:ss?\.?|sections?|subsections?|paragraphs?|subparas?\.?|paras?\.?|arts?\.?|articles?|rr?\.|rules?)\s*"
	rf"(?P<prov>{_PROVISION_LIST})",
	re.IGNORECASE,
)
_JUNK_NORMALIZED_RE = re.compile(
	r"^(?:of|in|under|and|or)?\s*(?:the\s+)?(?:Act|Regulations|Rules|Code|Order|Convention)\.?$",
	re.IGNORECASE,
)
_ROMAN = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv"]


# --------------------------------------------------------------------------- provisions
def _normalize_provision(value: str) -> str:
	normalized = re.sub(r"\s+", "", value)
	normalized = re.sub(r"(?<=\))([a-z]{1,4})\)", r"(\1)", normalized)
	normalized = re.sub(r"\(([A-Za-z0-9.]+)\)", lambda match: f"({match.group(1).lower()})", normalized)
	normalized = re.sub(r"(?<=\d)([A-Z])(?=(?:\(|$))", lambda match: match.group(1).lower(), normalized)
	return normalized


def _provision_parts(provision: str) -> tuple[str, ...]:
	match = re.match(r"(?P<section>\d{1,3}(?:\.\d{1,3})?[A-Za-z]?)(?P<tail>(?:\([^()]+\))*)$", provision)
	if match is None:
		return ()
	return (match.group("section"), *re.findall(r"\(([^()]+)\)", match.group("tail")))


def _join_parts(parts: Iterable[str]) -> str:
	parts = list(parts)
	return parts[0] + "".join(f"({part})" for part in parts[1:]) if parts else ""


def _expand_label_range(start: str, end: str) -> list[str] | None:
	if start.isdigit() and end.isdigit():
		low, high = int(start), int(end)
		if low < high and high - low <= MAX_RANGE_EXPANSION:
			return [str(value) for value in range(low, high + 1)]
		return None
	if start in _ROMAN and end in _ROMAN and _ROMAN.index(start) < _ROMAN.index(end):
		return _ROMAN[_ROMAN.index(start) : _ROMAN.index(end) + 1]
	letters = string.ascii_lowercase
	if len(start) == 1 and len(end) == 1 and start in letters and end in letters and start < end:
		return list(letters[letters.index(start) : letters.index(end) + 1])
	return None


def split_provision_list(value: str, expand: bool = True) -> list[str]:
	"""Split "96, 97", "112 to 114" or "36(1)(a) and (b)" into single provisions.

	Bare siblings like "(b)" inherit the parent path of the previous provision.
	With ``expand=False`` the whole list is returned as one normalized string.
	"""
	compact = " ".join(value.split())
	if not expand:
		return [_normalize_provision(compact)]
	tokens = re.split(rf"({_SEPARATOR})", compact, flags=re.IGNORECASE)
	items: list[str] = []
	pending_range = False
	previous_parts: tuple[str, ...] = ()
	for token in tokens:
		if not token or not token.strip():
			continue
		if re.fullmatch(_SEPARATOR, token, flags=re.IGNORECASE):
			pending_range = bool(re.search(r"\b(?:to|through|à)\b|[-–]", token, flags=re.IGNORECASE))
			continue
		normalized = _normalize_provision(token)
		if re.fullmatch(r"[a-z]{1,4}\)", normalized):
			normalized = f"({normalized}"
		if normalized.startswith("("):
			siblings = re.findall(r"\(([^()]+)\)", normalized)
			if not previous_parts or len(siblings) >= len(previous_parts):
				continue
			parts = (*previous_parts[: len(previous_parts) - len(siblings)], *siblings)
		else:
			parts = _provision_parts(normalized)
			if not parts:
				continue
		if pending_range and items and previous_parts and len(parts) == len(previous_parts) and parts[:-1] == previous_parts[:-1]:
			expanded = _expand_label_range(previous_parts[-1], parts[-1])
			if expanded is not None:
				for label in expanded[1:]:
					items.append(_join_parts((*parts[:-1], label)))
				previous_parts = parts
				pending_range = False
				continue
			# Too wide to expand: keep both ends so neither is lost.
		items.append(_join_parts(parts))
		previous_parts = parts
		pending_range = False
	return list(dict.fromkeys(items)) or [_normalize_provision(compact)]


def _label_for(instrument: Instrument | None, raw_label: str | None, plural: bool) -> str:
	base = instrument.provision_label if instrument is not None else "s."
	if raw_label and re.match(r"(?:art|article)", raw_label, re.IGNORECASE) and (instrument is None or instrument.kind == "instrument"):
		# French "article" of a statute is a section; only treaties use "art.".
		base = "art."
	if raw_label and re.match(r"(?:rule|r\.|rr\.|r$)", raw_label.strip(), re.IGNORECASE):
		base = "r."
	if not plural:
		return base
	return {"s.": "ss.", "r.": "rr.", "art.": "arts."}.get(base, base)


def _normalized_citation(instrument: Instrument | None, fallback_name: str | None, label: str, provision: str | None) -> str:
	name = instrument.citation if instrument is not None else (fallback_name or "").strip()
	if not provision:
		return name
	if instrument is not None and instrument.kind == "instrument":
		short = "Refugee Convention" if instrument.key == "international.refugee_convention" else instrument.aliases[0]
		return f"{label} {provision} of {short}"
	return f"{name} {label} {provision}".strip()


# --------------------------------------------------------------------------- row building
def _build_row(
	*,
	text: str,
	start: int,
	end: int,
	instrument: Instrument | None,
	fallback_name: str | None,
	raw_label: str | None,
	provisions: list[str],
	step: str,
	action: str,
	confidence: float,
	language: str,
	notes: tuple[str, ...] = (),
	replaces: tuple[tuple[int, int, str], ...] = (),
) -> list[RefinedStatuteReference]:
	kind = instrument.kind if instrument is not None else "statute"
	citation_text = text[start:end]
	if not provisions:
		return [
			RefinedStatuteReference(
				kind=kind,
				citation_text=citation_text,
				normalized_citation=_normalized_citation(instrument, fallback_name, "", None),
				offset_start=start,
				offset_end=end,
				step=step,
				action=action,
				confidence=confidence,
				instrument_key=instrument.key if instrument else None,
				instrument_citation=instrument.citation if instrument else None,
				language=language,
				notes=notes,
				replaces=replaces,
			)
		]
	rows: list[RefinedStatuteReference] = []
	group = len(provisions) > 1
	for index, provision in enumerate(provisions):
		if kind == "instrument":
			# Treaty articles keep their capital letter: art. 1F(b), not 1f(b).
			provision = re.sub(r"^(\d+)([a-z])(?=\(|$)", lambda m: m.group(1) + m.group(2).upper(), provision)
		parts = _provision_parts(provision)
		label = _label_for(instrument, raw_label, plural=False)
		rows.append(
			RefinedStatuteReference(
				kind=kind,
				citation_text=citation_text,
				normalized_citation=_normalized_citation(instrument, fallback_name, label, provision),
				offset_start=start,
				offset_end=end,
				step=step,
				action=ACTION_EXPANDED if group and action == ACTION_KEPT else action,
				confidence=confidence,
				instrument_key=instrument.key if instrument else None,
				instrument_citation=instrument.citation if instrument else None,
				provision=provision,
				section=parts[0] if parts else None,
				subsection=parts[1] if len(parts) > 1 else None,
				paragraph=parts[2] if len(parts) > 2 else None,
				subparagraph=parts[3] if len(parts) > 3 else None,
				nested_depth=max(len(parts) - 1, 0) if parts else None,
				legislation_url=instrument.url_for(parts[0]) if instrument and parts else None,
				group_start=start if group else None,
				group_end=end if group else None,
				group_index=index if group else None,
				group_size=len(provisions) if group else None,
				language=language,
				notes=notes,
				replaces=replaces,
			)
		)
	return rows


def _registry_allowed(instrument: Instrument | None, steps: frozenset[str]) -> Instrument | None:
	if instrument is None:
		return None
	if "L4_registry" in steps or instrument.key in LEGISLATION_REGISTRY:
		return instrument
	return None


def _score(row: RefinedStatuteReference) -> int:
	return (2 if row.instrument_key else 0) + (2 if row.provision else 0) + (1 if row.nested_depth else 0)


def _overlaps(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
	return not (a_end <= b_start or b_end <= a_start)


# --------------------------------------------------------------------------- pass-one rows
def _refine_pass_one_row(
	text: str,
	row: RawCitationMatch,
	context: DocumentContext,
	steps: frozenset[str],
) -> tuple[list[RefinedStatuteReference], RefinedStatuteReference | None]:
	"""Return (kept rows, dropped row)."""
	normalized = " ".join((row.normalized_citation or row.citation_text or "").split())
	if "L1_definitions" in steps and _JUNK_NORMALIZED_RE.match(normalized):
		dropped = RefinedStatuteReference(
			kind=row.kind,
			citation_text=row.citation_text,
			normalized_citation=normalized,
			offset_start=row.offset_start,
			offset_end=row.offset_end,
			step="L1_definitions",
			action=ACTION_DROPPED,
			confidence=0.0,
			notes=("generic_name_without_provision",),
		)
		return [], dropped

	found = identify_instrument(normalized) or identify_instrument(row.citation_text)
	instrument = _registry_allowed(found[0] if found else None, steps)
	language = found[1] if found else "en"
	# Prefer a provision after the instrument name ("<Act>, S.C. 2001, c. 27 s. 96");
	# treaties put it first ("art. 1F(b) of Refugee Convention").
	alias_match = identify_instrument(normalized)
	provision_match = None
	if alias_match is not None:
		provision_match = _NORMALIZED_PROVISION_RE.search(normalized, alias_match[2].end())
	if provision_match is None:
		provision_match = _NORMALIZED_PROVISION_RE.search(normalized)
	provisions: list[str] = []
	raw_label = None
	if provision_match is not None:
		raw_label = re.match(r"\S+", provision_match.group(0)).group(0)  # type: ignore[union-attr]
		provisions = split_provision_list(provision_match.group("prov"), expand="L3_expand" in steps)
	fallback_name = None
	if instrument is None:
		fallback_name = re.split(r"\s+(?:ss?|arts?|rr?)\.\s+", normalized, maxsplit=1)[0]
	confidence = 0.95 if instrument and provisions else 0.85 if instrument else 0.5
	notes = () if instrument else ("instrument_not_in_registry",)
	rows = _build_row(
		text=text,
		start=row.offset_start,
		end=row.offset_end,
		instrument=instrument,
		fallback_name=fallback_name,
		raw_label=raw_label,
		provisions=provisions,
		step="pass1",
		action=ACTION_KEPT,
		confidence=confidence,
		language=language,
		notes=notes,
	)
	if len(rows) > 1:
		rows = [replace(item, step="L3_expand") for item in rows]
	return rows, None


# --------------------------------------------------------------------------- gap scan
def _gap_candidates(text: str, context: DocumentContext, steps: frozenset[str]) -> list[tuple[int, list[RefinedStatuteReference]]]:
	candidates: list[tuple[int, list[RefinedStatuteReference]]] = []
	for name, pattern, priority in _GAP_PATTERNS:
		if name == "refugee_article" and "L2_gap_scan" not in steps:
			continue
		for match in pattern.finditer(text):
			groups = match.groupdict()
			instrument: Instrument | None = None
			language = "fr" if name == "french_provision" else "en"
			explicit = True
			if name == "refugee_article":
				instrument = REGISTRY["international.refugee_convention"]
			elif groups.get("inst"):
				found = lookup_alias(groups["inst"])
				if found is None:
					continue
				instrument = REGISTRY[found[0]]
				language = found[1]
			elif groups.get("generic"):
				if "L1_definitions" not in steps:
					continue
				resolved = context.resolve_term(groups["generic"], match.start())
				if resolved is None:
					continue
				instrument = REGISTRY[resolved[0]]
				explicit = resolved[1]
			if name != "refugee_article" and "L2_gap_scan" not in steps and not groups.get("generic"):
				continue
			instrument = _registry_allowed(instrument, steps)
			if instrument is None:
				continue
			provisions = split_provision_list(groups["prov"], expand="L3_expand" in steps)
			if name == "refugee_article":
				provisions = [_normalize_provision(re.sub(r"(?<=[EF])([a-cA-C])$", r"(\1)", groups["prov"].replace(" ", "")))]
			step = "L1_definitions" if groups.get("generic") else "L2_gap_scan"
			confidence = 0.92 if explicit else 0.75
			notes = () if explicit else ("instrument_from_default_reading",)
			rows = _build_row(
				text=text,
				start=match.start(),
				end=match.end(),
				instrument=instrument,
				fallback_name=None,
				raw_label=groups.get("label") or "art.",
				provisions=provisions,
				step=step,
				action=ACTION_ADDED,
				confidence=confidence,
				language=language,
				notes=notes,
			)
			# "s. 216 of the Regulations" names its instrument outright, so it beats a
			# neighbouring prefix match such as "IRPA, section 216".
			candidates.append((priority, [replace(row, notes=(*row.notes, "explicit_of")) if name in {"provision_of_instrument", "french_provision"} else row for row in rows]))
	return candidates


# --------------------------------------------------------------------------- validation
# Pass-one "generic statute" rows that are sentence fragments, not law names:
# "Does the Act", "Should the Minister's Order", "Statutes and Regulations Cited Act".
_FRAGMENT_FIRST_WORDS = {
	"does", "do", "did", "should", "would", "could", "is", "are", "was", "were", "has", "have", "had", "will",
	"may", "can", "must", "new", "statutes", "under", "whether", "if", "when", "while", "each", "every", "any",
	"all", "no", "not", "this", "that", "these", "those", "how", "why", "what", "which", "where",
}


def _validate(row: RefinedStatuteReference) -> RefinedStatuteReference | None:
	notes = list(row.notes)
	confidence = row.confidence
	if not row.instrument_key and not row.provision:
		first_word = (re.findall(r"[A-Za-z]+", row.normalized_citation) or [""])[0].casefold()
		if first_word in _FRAGMENT_FIRST_WORDS or not re.search(r"[A-Za-z]{3,}", row.normalized_citation):
			return None
		# A real law name we cannot identify yet: keep it, at low confidence.
		confidence = min(confidence, 0.4)
	maximum = KNOWN_MAX_PROVISION.get(row.instrument_key or "")
	if maximum and row.section:
		number = re.match(r"\d+", row.section)
		if number and int(number.group(0)) > maximum:
			notes.append("provision_out_of_range")
			confidence = round(confidence * 0.5, 3)
	if row.instrument_key == "international.refugee_convention" and row.section and not re.match(r"^\d{1,2}[A-Za-z]?$", row.section):
		notes.append("unusual_article_number")
	if tuple(notes) == row.notes and confidence == row.confidence:
		return row
	return replace(row, notes=tuple(notes), confidence=confidence)


# --------------------------------------------------------------------------- entry point
PASS_ONE_WINDOW = 6000


def pass_one_statutes_by_window(text: str, window: int = PASS_ONE_WINDOW) -> list[RawCitationMatch]:
	"""Run pass-one statute extraction in paragraph-aligned windows.

	Pass one's anchored-provision step re-scans the text from the start for every
	match, so it slows down sharply on whole decisions. Production already runs it
	per chunk; this mirrors that and shifts offsets back to whole-text positions.
	"""
	rows: list[RawCitationMatch] = []
	start = 0
	while start < len(text):
		end = min(len(text), start + window)
		if end < len(text):
			newline = text.rfind("\n", start + window // 2, end)
			end = newline + 1 if newline > 0 else end
		for row in extract_statute_reference_matches(text[start:end]):
			rows.append(replace(row, offset_start=row.offset_start + start, offset_end=row.offset_end + start))
		start = end
	return rows

def refine_statute_references(
	text: str | None,
	pass_one_rows: list[RawCitationMatch] | None = None,
	steps: Iterable[str] | None = None,
	context: DocumentContext | None = None,
) -> LayerResult:
	"""Run the law refinement layer over a whole decision.

	``pass_one_rows`` defaults to ``extract_statute_reference_matches(text)``.
	Offsets are relative to ``text`` (run it on the full decision so "the Act"
	definitions near the top are visible, then map rows to chunks by offset).
	"""
	content = text or ""
	enabled = frozenset(LAW_STEPS if steps is None else steps)
	if not content.strip():
		return LayerResult(rows=[], steps_run=tuple(sorted(enabled)))
	if pass_one_rows is None:
		pass_one_rows = pass_one_statutes_by_window(content)
	context = context or DocumentContext.build(content)

	kept: list[RefinedStatuteReference] = []
	dropped: list[RefinedStatuteReference] = []
	for raw in pass_one_rows:
		rows, junk = _refine_pass_one_row(content, raw, context, enabled)
		kept.extend(rows)
		if junk is not None:
			dropped.append(junk)

	# Gap candidates: best first, no overlaps among themselves.
	candidates = _gap_candidates(content, context, enabled)
	candidates.sort(key=lambda item: (-item[0], -_score(item[1][0]), -(item[1][0].offset_end - item[1][0].offset_start), item[1][0].offset_start))
	accepted_spans: list[tuple[int, int]] = []
	for _priority, rows in candidates:
		start, end = rows[0].offset_start, rows[0].offset_end
		if any(_overlaps(start, end, a, b) for a, b in accepted_spans):
			continue
		gap_score = _score(rows[0])
		overlapping = [row for row in kept if _overlaps(start, end, row.offset_start, row.offset_end)]
		dropped_overlap = [row for row in dropped if _overlaps(start, end, row.offset_start, row.offset_end)]
		if overlapping:
			best_existing = max(_score(row) for row in overlapping)
			covers_all = all(start <= row.offset_start and row.offset_end <= end for row in overlapping)
			same_instrument = {row.instrument_key for row in overlapping} == {rows[0].instrument_key}
			explicit_of = "explicit_of" in rows[0].notes
			better = gap_score > best_existing or (
				gap_score == best_existing and (covers_all or explicit_of) and not same_instrument
			)
			if not better:
				continue
			replaced_spans = tuple(
				dict.fromkeys((row.offset_start, row.offset_end, row.normalized_citation) for row in overlapping)
			)
			kept = [row for row in kept if row not in overlapping]
			rows = [replace(row, action=ACTION_CORRECTED, replaces=replaced_spans) for row in rows]
		elif dropped_overlap:
			replaced_spans = tuple((row.offset_start, row.offset_end, row.normalized_citation) for row in dropped_overlap)
			rows = [replace(row, action=ACTION_CORRECTED, replaces=replaced_spans) for row in rows]
		accepted_spans.append((start, end))
		kept.extend(rows)

	if "L5_validate" in enabled:
		validated: list[RefinedStatuteReference] = []
		for row in kept:
			checked = _validate(row)
			if checked is None:
				dropped.append(replace(row, step="L5_validate", action=ACTION_DROPPED, confidence=0.0, notes=(*row.notes, "sentence_fragment")))
			else:
				validated.append(checked)
		kept = validated

	kept = [replace(row, notes=tuple(note for note in row.notes if note != "explicit_of")) if "explicit_of" in row.notes else row for row in kept]
	kept.sort(key=lambda row: (row.offset_start, row.offset_end, row.group_index or 0))
	dropped.sort(key=lambda row: (row.offset_start, row.offset_end))
	return LayerResult(rows=kept, dropped=dropped, steps_run=tuple(step for step in LAW_STEPS if step in enabled))


__all__ = [
	"LAW_STEPS",
	"refine_statute_references",
	"split_provision_list",
	"normalize_term",
]
