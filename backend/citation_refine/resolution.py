"""Link refined rows to cases, paragraphs and statute provisions.

The core functions take plain lookups (dicts / callables), so they are testable
without a database. ``load_*`` helpers build those lookups from a session with
read-only queries. Nothing here writes to the database.

Case statuses:      resolved, ambiguous, conflict, not_in_database, no_identifier
Pinpoint statuses:  none, resolved, partial, beyond_target, page_unmapped,
                    no_paragraph_index, not_attempted
Statute statuses:   resolved_provision, partial_provision, resolved_section,
                    section_not_indexed, document_not_indexed, missing_section,
                    instrument_unidentified
"""

from __future__ import annotations

import re
from collections import defaultdict
from collections.abc import Callable, Iterable
from dataclasses import dataclass, field

from .cases import identifier_keys
from .models import PINPOINT_PAGE, PINPOINT_PARAGRAPH, RefinedCitation, RefinedStatuteReference

# --------------------------------------------------------------------------- cases


@dataclass(frozen=True)
class ParagraphLink:
	paragraph: int
	chunk_id: int | None


@dataclass(frozen=True)
class CaseResolution:
	row: RefinedCitation
	target_case_id: int | None
	status: str
	method: str | None = None
	matched_key: str | None = None
	paragraphs: tuple[ParagraphLink, ...] = ()
	pinpoint_status: str = "none"
	unmatched_paragraphs: tuple[int, ...] = ()


def _title_key(value: str | None) -> str:
	text = re.sub(r"\s+(?:v\.?|vs\.?|c\.)\s+", " v ", (value or "").casefold())
	text = re.sub(r"[^a-z0-9 ]+", " ", text)
	return " ".join(text.split())


@dataclass
class CaseIndex:
	"""Lookup keys -> case id (None when two cases share a key)."""

	by_key: dict[str, int | None] = field(default_factory=dict)
	by_title_year: dict[tuple[str, int], set[int]] = field(default_factory=lambda: defaultdict(set))
	by_docket: dict[str, int | None] = field(default_factory=dict)

	def add(self, case_id: int, citations: Iterable[str | None], title: str | None = None, year: int | None = None, docket: str | None = None) -> None:
		for value in citations:
			for key in identifier_keys(value):
				if key not in self.by_key:
					self.by_key[key] = case_id
				elif self.by_key[key] != case_id:
					self.by_key[key] = None
		if title and year:
			self.by_title_year[(_title_key(title), year)].add(case_id)
		for value in re.findall(r"(?:IMM|DES|A|T)-\d{1,6}-\d{2}", docket or ""):
			if value not in self.by_docket:
				self.by_docket[value] = case_id
			elif self.by_docket[value] != case_id:
				self.by_docket[value] = None


def build_case_index(records: Iterable[tuple[int, str | None, str | None, str | None, int | None, str | None]]) -> CaseIndex:
	"""Build from (case_id, citation, secondary_citation, title, year, docket_number) tuples."""
	index = CaseIndex()
	for case_id, citation, secondary, title, year, docket in records:
		index.add(case_id, (citation, secondary), title, year, docket)
	return index


ParagraphLookup = Callable[[int], list[tuple[int | None, int, int]] | None]


def _years(row: RefinedCitation) -> set[int]:
	return {int(value) for value in re.findall(r"\b((?:19|20)\d{2})\b", " ".join(row.identifiers))}


def _resolve_by_identifiers(row: RefinedCitation, index: CaseIndex) -> tuple[int | None, str, str | None, str | None]:
	if row.kind == "docket":
		target = index.by_docket.get(row.normalized_citation)
		if row.normalized_citation not in index.by_docket:
			return None, "not_in_database", None, None
		return (target, "resolved", "docket", row.normalized_citation) if target else (None, "ambiguous", None, None)
	if not row.identifiers:
		if row.case_name:
			return _resolve_by_name(row, index)
		return None, "no_identifier", None, None
	found: dict[int, str] = {}
	ambiguous = False
	for key in row.identifiers:
		if key not in index.by_key:
			continue
		target = index.by_key[key]
		if target is None:
			ambiguous = True
		else:
			found.setdefault(target, key)
	if len(found) == 1:
		target, key = next(iter(found.items()))
		return target, "resolved", "identifier", key
	if len(found) > 1:
		return None, "conflict", None, None
	if ambiguous:
		return None, "ambiguous", None, None
	if row.case_name:
		target, status, method, key = _resolve_by_name(row, index)
		if target is not None:
			return target, status, method, key
	return None, "not_in_database", None, None


def _resolve_by_name(row: RefinedCitation, index: CaseIndex) -> tuple[int | None, str, str | None, str | None]:
	"""Name + year match, only when exactly one case has that title and year."""
	name = _title_key(row.case_name)
	if " v " not in f" {name} " and "re" not in name.split():
		return None, "no_identifier", None, None
	candidates: set[int] = set()
	for year in _years(row):
		candidates |= index.by_title_year.get((name, year), set())
	if len(candidates) == 1:
		return next(iter(candidates)), "resolved", "name_year", name
	if len(candidates) > 1:
		return None, "ambiguous", None, None
	return None, "no_identifier" if not row.identifiers else "not_in_database", None, None


def link_paragraphs(row: RefinedCitation, target_case_id: int | None, paragraph_lookup: ParagraphLookup | None) -> tuple[str, tuple[ParagraphLink, ...], tuple[int, ...]]:
	if not row.pinpoints:
		return "none", (), ()
	if target_case_id is None or paragraph_lookup is None:
		return "not_attempted", (), ()
	paragraph_pins = [pin for pin in row.pinpoints if pin.kind == PINPOINT_PARAGRAPH]
	if not paragraph_pins:
		return ("page_unmapped" if any(pin.kind == PINPOINT_PAGE for pin in row.pinpoints) else "none"), (), ()
	chunks = paragraph_lookup(target_case_id)
	if not chunks:
		return "no_paragraph_index", (), ()
	last_paragraph = max(end for _chunk, _start, end in chunks)
	links: list[ParagraphLink] = []
	unmatched: list[int] = []
	for pin in paragraph_pins:
		for value in pin.values:
			chunk_id = next((chunk for chunk, start, end in chunks if start <= value <= end), None)
			if chunk_id is None and not any(start <= value <= end for _chunk, start, end in chunks):
				unmatched.append(value)
			else:
				links.append(ParagraphLink(value, chunk_id))
	if not links:
		return ("beyond_target" if unmatched and min(unmatched) > last_paragraph else "partial"), (), tuple(unmatched)
	if unmatched:
		return "partial", tuple(links), tuple(unmatched)
	return "resolved", tuple(links), ()


def resolve_case_rows(
	rows: Iterable[RefinedCitation],
	index: CaseIndex,
	paragraph_lookup: ParagraphLookup | None = None,
) -> list[CaseResolution]:
	"""Resolve full citations first, then let short forms inherit their anchor's target."""
	rows = list(rows)
	by_span: dict[tuple[int, int], CaseResolution] = {}
	results: list[CaseResolution | None] = [None] * len(rows)

	def finish(position: int, row: RefinedCitation, target: int | None, status: str, method: str | None, key: str | None) -> None:
		pin_status, links, unmatched = link_paragraphs(row, target, paragraph_lookup)
		resolution = CaseResolution(row, target, status, method, key, links, pin_status, unmatched)
		results[position] = resolution
		by_span[(row.offset_start, row.offset_end)] = resolution

	for position, row in enumerate(rows):
		if row.kind == "case_short" and row.anchor_offset_start is not None:
			continue
		finish(position, row, *_resolve_by_identifiers(row, index))
	for position, row in enumerate(rows):
		if results[position] is not None:
			continue
		anchor = by_span.get((row.anchor_offset_start or -1, row.anchor_offset_end or -1))
		if anchor is not None and anchor.target_case_id is not None:
			finish(position, row, anchor.target_case_id, "resolved", "anchor", anchor.matched_key)
		elif anchor is not None:
			finish(position, row, None, anchor.status, None, None)
		else:
			finish(position, row, *_resolve_by_identifiers(row, index))
	return [result for result in results if result is not None]


# --------------------------------------------------------------------------- statutes


@dataclass(frozen=True)
class ProvisionUnit:
	"""One subsection / paragraph / subparagraph / clause inside a section's text."""

	path: tuple[str, ...]
	start: int
	end: int
	text: str


_LEVEL_SUBSECTION, _LEVEL_PARAGRAPH, _LEVEL_SUBPARAGRAPH, _LEVEL_CLAUSE = 1, 2, 3, 4
_MARKER_RE = re.compile(r"\((?P<label>\d{1,3}(?:\.\d{1,2})?|[a-z](?:\.\d{1,2})?|[ivx]{1,6}|[A-Z](?:\.\d{1,2})?)\)")
_CROSS_REFERENCE_BEFORE = re.compile(
	r"(?:sub-?sections?|paragraphs?|sub-?paragraphs?|sections?|clauses?|under|of|in|to|par\.|s\.|ss\.)\s*$",
	re.IGNORECASE,
)
_ROMAN_VALUES = {"i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5, "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10, "xi": 11, "xii": 12}


def _marker_level(label: str, previous_paragraph: str | None, previous_subparagraph: str | None) -> int:
	if label[0].isdigit():
		return _LEVEL_SUBSECTION
	if label[0].isupper():
		return _LEVEL_CLAUSE
	if label in _ROMAN_VALUES:
		# "(i)" after "(h)" is a paragraph; after "(a)" it starts subparagraphs.
		if previous_subparagraph is not None and _ROMAN_VALUES.get(previous_subparagraph, 0) + 1 == _ROMAN_VALUES[label]:
			return _LEVEL_SUBPARAGRAPH
		if label in {"i", "v", "x"} and previous_paragraph and ord(label) == ord(previous_paragraph[0]) + 1:
			return _LEVEL_PARAGRAPH
		if label == "i" or previous_subparagraph is not None:
			return _LEVEL_SUBPARAGRAPH
	return _LEVEL_PARAGRAPH


def split_section_text(section_number: str, text: str) -> list[ProvisionUnit]:
	"""Split a section's flat text into its numbered parts.

	"36 (1) A permanent resident is inadmissible ... (a) having been convicted ..."
	gives units for ("36", "1"), ("36", "1", "a"), ... Cross-references such as
	"under subsection (2)" are not treated as new parts.
	"""
	markers: list[tuple[int, int, str, int]] = []
	previous_paragraph: str | None = None
	previous_subparagraph: str | None = None
	for match in _MARKER_RE.finditer(text):
		before = text[max(0, match.start() - 24) : match.start()]
		if before[-1:].isalnum() or before[-1:] == ")":
			continue  # inline reference such as "36(1)(a)"
		if _CROSS_REFERENCE_BEFORE.search(before) or re.search(r"\)\s+(?:and|or|to)\s*$", before):
			continue  # "under subsection (2)", "subsections (1) and (2)"
		label = match.group("label")
		level = _marker_level(label, previous_paragraph, previous_subparagraph)
		if level == _LEVEL_SUBSECTION:
			previous_paragraph = previous_subparagraph = None
		elif level == _LEVEL_PARAGRAPH:
			previous_paragraph, previous_subparagraph = label, None
		elif level == _LEVEL_SUBPARAGRAPH:
			previous_subparagraph = label
		markers.append((match.start(), match.end(), label, level))

	units: list[ProvisionUnit] = []
	stack: list[tuple[int, str]] = []
	for index, (start, _end, label, level) in enumerate(markers):
		while stack and stack[-1][0] >= level:
			stack.pop()
		stack.append((level, label))
		finish = len(text)
		for later_start, _later_end, _later_label, later_level in markers[index + 1 :]:
			if later_level <= level:
				finish = later_start
				break
		path = (section_number, *(item[1] for item in stack))
		units.append(ProvisionUnit(path, start, finish, text[start:finish].strip()))
	return units


@dataclass(frozen=True)
class StatuteResolution:
	row: RefinedStatuteReference
	status: str
	section_id: int | None = None
	matched_path: tuple[str, ...] = ()
	unit_start: int | None = None
	unit_end: int | None = None


SectionLookup = Callable[[str, str], tuple[int, str] | None]
DocumentLookup = Callable[[str], bool]


def _normalize_label(value: str) -> str:
	return value.casefold()


def resolve_statute_row(row: RefinedStatuteReference, has_document: DocumentLookup, get_section: SectionLookup) -> StatuteResolution:
	if not row.instrument_key:
		return StatuteResolution(row, "instrument_unidentified")
	if not row.section:
		return StatuteResolution(row, "missing_section")
	if not has_document(row.instrument_key):
		return StatuteResolution(row, "document_not_indexed")
	section = get_section(row.instrument_key, row.section)
	if section is None:
		return StatuteResolution(row, "section_not_indexed")
	section_id, section_text = section
	wanted = row.provision_path
	if len(wanted) <= 1:
		return StatuteResolution(row, "resolved_section", section_id, wanted[:1])
	units = split_section_text(row.section, section_text)
	wanted_key = tuple(_normalize_label(part) for part in wanted)
	best: ProvisionUnit | None = None
	for unit in units:
		unit_key = tuple(_normalize_label(part) for part in unit.path)
		if unit_key == wanted_key:
			return StatuteResolution(row, "resolved_provision", section_id, unit.path, unit.start, unit.end)
		if wanted_key[: len(unit_key)] == unit_key and (best is None or len(unit.path) > len(best.path)):
			best = unit
	if best is not None:
		return StatuteResolution(row, "partial_provision", section_id, best.path, best.start, best.end)
	return StatuteResolution(row, "partial_provision", section_id, wanted[:1])


def resolve_statute_rows(rows: Iterable[RefinedStatuteReference], has_document: DocumentLookup, get_section: SectionLookup) -> list[StatuteResolution]:
	return [resolve_statute_row(row, has_document, get_section) for row in rows]


# --------------------------------------------------------------------------- read-only database adapters


def load_case_index(session) -> CaseIndex:  # pragma: no cover - needs Postgres
	from sqlalchemy import select

	from ..database import Case

	records = (
		(case_id, citation, secondary, title, decided.year if decided else None, docket)
		for case_id, citation, secondary, title, decided, docket in session.execute(
			select(Case.id, Case.citation, Case.secondary_citation, Case.title, Case.date, Case.docket_number)
		)
	)
	return build_case_index(records)


def paragraph_lookup_from_session(session) -> ParagraphLookup:  # pragma: no cover - needs Postgres
	from sqlalchemy import select

	from ..database import CaseChunk

	cache: dict[int, list[tuple[int | None, int, int]]] = {}

	def lookup(case_id: int) -> list[tuple[int | None, int, int]]:
		if case_id not in cache:
			cache[case_id] = [
				(chunk_id, start, end)
				for chunk_id, start, end in session.execute(
					select(CaseChunk.id, CaseChunk.paragraph_start, CaseChunk.paragraph_end).where(
						CaseChunk.case_id == case_id,
						CaseChunk.chunk_set == "paragraph",
						CaseChunk.paragraph_start.is_not(None),
						CaseChunk.paragraph_end.is_not(None),
					)
				)
			]
		return cache[case_id]

	return lookup


def statute_lookups_from_session(session) -> tuple[DocumentLookup, SectionLookup]:  # pragma: no cover - needs Postgres
	from sqlalchemy import select

	from ..database import LegislationDocument, LegislationSection

	documents = {key: doc_id for doc_id, key in session.execute(select(LegislationDocument.id, LegislationDocument.instrument_key))}
	cache: dict[tuple[str, str], tuple[int, str] | None] = {}

	def has_document(key: str) -> bool:
		return key in documents

	def get_section(key: str, section: str) -> tuple[int, str] | None:
		if (key, section) not in cache:
			row = session.execute(
				select(LegislationSection.id, LegislationSection.text).where(
					LegislationSection.document_id == documents.get(key),
					LegislationSection.section_number == section,
				)
			).first()
			cache[(key, section)] = (row[0], row[1]) if row else None
		return cache[(key, section)]

	return has_document, get_section
