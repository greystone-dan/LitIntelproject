"""Structured pinpoint parsing for case citations.

Turns "at paras 85-87 and 99" into paragraphs (85, 86, 87, 99) and
"at pp. 841-42" into pages (841, 842), so a pinpoint can be linked to every
paragraph it names, not only the first one.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .models import PINPOINT_FOOTNOTE, PINPOINT_PAGE, PINPOINT_PARAGRAPH, Pinpoint

MAX_EXPANDED_VALUES = 200

# A number followed by a capitalized word is the next citation's volume
# ("at para 22, 131 A.C.W.S. (3d) 508"), not part of the pinpoint.
_NUMBER = r"\d{1,5}(?!\d|\s+(?-i:[A-Z]))"
_RANGE = rf"{_NUMBER}(?:\s*(?:[-–—]|to|à|au)\s*{_NUMBER})?"
_LIST = rf"{_RANGE}(?:\s*(?:,|;|and|or|et|&)\s*{_RANGE})*"

# Paragraph pinpoints in English and French.
_PARAGRAPH_LABEL = (
	r"(?:paragraphes?|paragraphs?|paras?\.?|para\.?|¶¶?|"
	r"par\.?|parag\.?)"
)
# Page pinpoints.
_PAGE_LABEL = r"(?:pages?|pp\.?|p\.)"

# "para 45 ff", "paras 45 et seq", "para 45 and following": open-ended, the extent is not stated.
_OPEN_ENDED = r"(?:\s*(?:ff\b\.?|et\s+seq\b\.?|and\s+following\b|et\s+suiv(?:ants?)?\b\.?))"

PINPOINT_RE = re.compile(
	rf"(?:\b(?:at|aux?|à|in)\s+)?"
	rf"(?<![A-Za-z])(?:(?P<para_label>{_PARAGRAPH_LABEL})\s*(?P<para_values>{_LIST})(?P<para_ff>{_OPEN_ENDED})?"
	rf"|(?P<page_label>{_PAGE_LABEL})\s*(?P<page_values>{_LIST})(?P<page_ff>{_OPEN_ENDED})?)",
	re.IGNORECASE,
)
# A bare "at 841" directly after a reported citation is a page pinpoint.
BARE_PAGE_RE = re.compile(rf"^\s*,?\s*at\s+(?P<values>{_LIST})\b(?!\s*(?:CanLII|[A-Z]{{2,}}))")
FOOTNOTE_RE = re.compile(r"\b(?:supra\s+)?(?:note|n\.)\s*(?P<values>\d{1,4})\b", re.IGNORECASE)

# What may sit between a citation and its trailing pinpoint.
TRAILING_PINPOINT_RE = re.compile(
	rf"^\s*(?:\((?:CanLII|QL|Lexis|F\.?C\.?A?\.?|F\.?C\.?T\.?D\.?|C\.?A\.?|SCC)\)\s*)?[,;:]?\s*\[?\s*"
	rf"(?P<pinpoint>(?:(?:at|aux?|à)\s+)?(?:{_PARAGRAPH_LABEL}\s*{_LIST}|{_PAGE_LABEL}\s*{_LIST}))\s*\]?",
	re.IGNORECASE,
)


def _expand_range(start: int, end: int) -> list[int]:
	if end < start:
		# Abbreviated page ranges, e.g. 841-42 means 841 to 842.
		digits = len(str(end))
		candidate = int(str(start)[: -digits] + str(end)) if len(str(start)) > digits else end
		end = candidate
	if end < start:
		return [start]
	return list(range(start, end + 1))


def _expand_values(raw: str) -> tuple[tuple[int, ...], bool, bool]:
	values: list[int] = []
	is_range_or_list = False
	truncated = False
	parts = re.split(r"\s*(?:,|;|\band\b|\bor\b|\bet\b|&)\s*", raw.strip(), flags=re.IGNORECASE)
	if len([part for part in parts if part]) > 1:
		is_range_or_list = True
	for part in parts:
		if not part:
			continue
		bounds = re.split(r"\s*(?:[-–—]|\bto\b|\bà\b|\bau\b)\s*", part, flags=re.IGNORECASE)
		numbers = [int(value) for value in bounds if value.isdigit()]
		if not numbers:
			continue
		if len(numbers) >= 2:
			is_range_or_list = True
			expanded = _expand_range(numbers[0], numbers[-1])
		else:
			expanded = [numbers[0]]
		for value in expanded:
			if len(values) >= MAX_EXPANDED_VALUES:
				truncated = True
				break
			if value not in values:
				values.append(value)
	return tuple(values), is_range_or_list, truncated


def parse_pinpoint(text: str | None) -> Pinpoint | None:
	"""Parse the first paragraph or page pinpoint found in ``text``."""
	if not text:
		return None
	match = PINPOINT_RE.search(text)
	if match is None:
		return None
	if match.group("para_values"):
		kind, raw_values = PINPOINT_PARAGRAPH, match.group("para_values")
	else:
		kind, raw_values = PINPOINT_PAGE, match.group("page_values")
	values, is_range_or_list, truncated = _expand_values(raw_values)
	if not values:
		return None
	return Pinpoint(
		kind=kind,
		raw=" ".join(match.group(0).split()),
		values=values,
		is_range_or_list=is_range_or_list,
		truncated=truncated,
		open_ended=bool(match.group("para_ff") or match.group("page_ff")),
	)


def parse_all_pinpoints(text: str | None) -> tuple[Pinpoint, ...]:
	"""Parse every pinpoint in ``text`` (e.g. "at para 4 and at p. 12")."""
	if not text:
		return ()
	found: list[Pinpoint] = []
	for match in PINPOINT_RE.finditer(text):
		pinpoint = parse_pinpoint(match.group(0))
		if pinpoint is not None:
			found.append(pinpoint)
	return tuple(found)


def parse_bare_page_pinpoint(text_after_citation: str) -> Pinpoint | None:
	"""Parse "at 841" immediately after a reported citation."""
	match = BARE_PAGE_RE.match(text_after_citation)
	if match is None:
		return None
	values, is_range_or_list, truncated = _expand_values(match.group("values"))
	if not values:
		return None
	label = "pp." if is_range_or_list else "p."
	return Pinpoint(PINPOINT_PAGE, f"at {label} {' '.join(match.group('values').split())}", values, is_range_or_list, truncated)


def pinpoint_phrase(pinpoint: Pinpoint) -> str:
	"""Render a pinpoint in the "at para. N" style used by pass-one normalization."""
	raw_numbers = re.sub(
		rf"^(?:(?:at|aux?|à|in)\s+)?(?:{_PARAGRAPH_LABEL}|{_PAGE_LABEL})\s*",
		"",
		pinpoint.raw,
		flags=re.IGNORECASE,
	)
	raw_numbers = re.sub(r"\s*[–—]\s*", "-", raw_numbers)
	raw_numbers = re.sub(r"\s*\bà\b\s*", "-", raw_numbers)
	raw_numbers = re.sub(r"\s+et\s+", " and ", raw_numbers)
	if pinpoint.kind == PINPOINT_PAGE:
		label = "pp." if pinpoint.is_range_or_list else "p."
	elif pinpoint.kind == PINPOINT_FOOTNOTE:
		label = "note"
	else:
		label = "paras." if pinpoint.is_range_or_list else "para."
	return f"at {label} {raw_numbers.strip()}"


MAX_LINKED_PARAGRAPHS = 30


@dataclass(frozen=True)
class ParagraphPinpoints:
	"""Every paragraph a citation's pinpoint text names, in the order written."""

	paragraphs: tuple[int, ...]
	label: str  # e.g. "paras 45-48, 52"
	open_ended: bool = False
	capped: bool = False  # a very long range was cut at MAX_LINKED_PARAGRAPHS (heuristic)

	@property
	def first(self) -> int:
		return self.paragraphs[0]


def _label(paragraphs: tuple[int, ...]) -> str:
	runs: list[list[int]] = []
	for value in paragraphs:
		if runs and value == runs[-1][-1] + 1:
			runs[-1].append(value)
		else:
			runs.append([value])
	text = ", ".join(str(r[0]) if len(r) == 1 else f"{r[0]}-{r[-1]}" for r in runs)
	return ("paras " if len(paragraphs) > 1 else "para ") + text


def paragraph_pinpoints(text: str | None) -> ParagraphPinpoints | None:
	"""All paragraph pinpoints in ``text`` merged ("paras 45-48 and 52", "at para 3 and at para 9").

	Page and footnote pinpoints are ignored. A range longer than ``MAX_LINKED_PARAGRAPHS`` keeps
	only its first paragraphs, since a sweep like "paras 20-120" is not a pinpoint at any one of them.
	"""
	merged: list[int] = []
	open_ended = capped = False
	for pin in parse_all_pinpoints(text):
		if pin.kind != PINPOINT_PARAGRAPH:
			continue
		open_ended = open_ended or pin.open_ended
		for value in pin.values:
			if value not in merged:
				merged.append(value)
	if len(merged) > MAX_LINKED_PARAGRAPHS:
		merged, capped = merged[:MAX_LINKED_PARAGRAPHS], True
	if not merged:
		return None
	paragraphs = tuple(merged)
	return ParagraphPinpoints(paragraphs, _label(paragraphs) + (" ff" if open_ended else ""), open_ended, capped)


def target_paragraphs(
	citation_text: str | None,
	normalized_citation: str | None = None,
	stored_target_paragraph: int | None = None,
) -> ParagraphPinpoints | None:
	"""Cited paragraphs of one stored citation: the stored first paragraph, plus the rest written in its text."""
	written = paragraph_pinpoints(citation_text or normalized_citation or "")
	if stored_target_paragraph is None:
		return written
	stored = int(stored_target_paragraph)
	if written is None or stored != written.first:
		return ParagraphPinpoints((stored,), _label((stored,)))
	return written
