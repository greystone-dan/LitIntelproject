"""Structured pinpoint parsing for case citations.

Turns "at paras 85-87 and 99" into paragraphs (85, 86, 87, 99) and
"at pp. 841-42" into pages (841, 842), so a pinpoint can be linked to every
paragraph it names, not only the first one.
"""

from __future__ import annotations

import re

from .models import PINPOINT_FOOTNOTE, PINPOINT_PAGE, PINPOINT_PARAGRAPH, Pinpoint

MAX_EXPANDED_VALUES = 200

# A number followed by a capitalized word is the next citation's volume
# ("at para 22, 131 A.C.W.S. (3d) 508"), not part of the pinpoint.
_NUMBER = r"\d{1,5}(?!\d|\s+(?-i:[A-Z]))"
_RANGE = rf"{_NUMBER}(?:\s*(?:[-–—]|to|à|au)\s*{_NUMBER})?"
_LIST = rf"{_RANGE}(?:\s*(?:,|;|and|or|et|&)\s*{_RANGE})*"

# Paragraph pinpoints in English and French.
_PARAGRAPH_LABEL = (
	r"(?:paragraphs?|paras?\.?|para\.?|¶¶?|"
	r"paragraphes?|par\.?|parag\.?)"
)
# Page pinpoints.
_PAGE_LABEL = r"(?:pages?|pp\.?|p\.)"

PINPOINT_RE = re.compile(
	rf"(?:\b(?:at|aux?|à|in)\s+)?"
	rf"(?<![A-Za-z])(?:(?P<para_label>{_PARAGRAPH_LABEL})\s*(?P<para_values>{_LIST})"
	rf"|(?P<page_label>{_PAGE_LABEL})\s*(?P<page_values>{_LIST}))",
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


def parse_footnote_reference(text: str) -> Pinpoint | None:
	match = FOOTNOTE_RE.search(text)
	if match is None:
		return None
	return Pinpoint(PINPOINT_FOOTNOTE, " ".join(match.group(0).split()), (int(match.group("values")),))


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
