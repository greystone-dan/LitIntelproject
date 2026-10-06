"""Deterministic source-metadata facade.

Composes the deterministic scraper extractor (`fc_ingest.document_scraper`)
with the derived intelligence layer in `backend.intelligence` (decision
outcome, government role/result, case type/challenge/issue/topic), and
exposes the public payload plus span-matched observations and matches.
Downstream callers should import from this module only; the stored payload
shape in `metadata_json->'reader_extracted'` is unchanged.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from fc_ingest.document_scraper import _extract_metadata_with_quality

from .intelligence import INTELLIGENCE_FIELDS, derive_intelligence_fields, derive_outcome_payload


METADATA_FIELDS = (
	"date",
	"docket",
	"neutral citation",
	"judge",
	"style of cause",
	"place of hearing",
	"date of hearing",
	"dated",
	"counsel",
	"present",
	"between",
	"solicitors of record",
)

# Combined emission order: the 12 deterministic source fields followed by the
# derived intelligence fields, so payloads, observations, and matches keep
# surfacing outcome/subject values in exactly the same order as before.
ALL_FIELDS = METADATA_FIELDS + INTELLIGENCE_FIELDS


@dataclass(frozen=True)
class MetadataMatch:
	field: str
	text: str
	value: str
	offset_start: int
	offset_end: int
	confidence: float
	source: str


@dataclass(frozen=True)
class MetadataObservation:
	field: str
	text: str
	value: str
	offset_start: int | None
	offset_end: int | None
	confidence: float
	source: str
	span_matched: bool


def _find_value_span(text: str, value: str) -> tuple[int, int] | None:
	parts = value.split()
	if not parts:
		return None
	pattern = r"\s+".join(re.escape(part) for part in parts)
	match = re.search(pattern, text, re.IGNORECASE)
	if not match:
		return None
	return match.start(), match.end()


def _field_source_label(field_sources: dict[str, str]) -> str:
	has_text = bool(str(field_sources.get("text") or "").strip())
	has_table = bool(str(field_sources.get("table") or "").strip())
	if has_text and has_table:
		return "text+table"
	if has_table:
		return "table"
	if has_text:
		return "text"
	return "derived"


_RPD_MARKER_RE = re.compile(r"Refugee Protection Division|Section de la protection des r[ée]fugi[ée]s|\bRPD File\b", re.IGNORECASE)
_RPD_NOT_A_NAME_RE = re.compile(r"counsel|claimant|conseil|demandeur|representative|minister|tribunal officer", re.IGNORECASE)


def _rpd_header_fields(content: str) -> dict[str, str]:
	"""Panel member and one-line place of hearing for Refugee Protection Division decisions.

	The generic label extractor lets "place of hearing" run on through the rest of the RPD cover page
	and finds no judge, so this reads the two fields from the cover page lines instead.
	"""
	head = content[:3000]
	if not _RPD_MARKER_RE.search(head):
		return {}
	lines = [line.strip() for line in head.splitlines()]
	found: dict[str, str] = {}
	for index, line in enumerate(lines):
		if re.fullmatch(r"Panel(?:\s+Tribunal)?", line, re.IGNORECASE):
			for candidate in lines[index + 1 : index + 4]:
				if not candidate or candidate.lower() == "tribunal":
					continue
				name = re.sub(r"^(?:Me|Mme|Mr\.?|Ms\.?|Mrs\.?)\s+", "", candidate)
				if (
					len(name) <= 60
					and 1 < len(name.split()) <= 5
					and not re.search(r"\d", name)
					and not _RPD_NOT_A_NAME_RE.search(name)
				):
					found["judge"] = name
				break
			break
	for index, line in enumerate(lines):
		if re.match(r"Place\s*\(?s?\)?\s*of hearing", line, re.IGNORECASE):
			for candidate in lines[index + 1 : index + 3]:
				if candidate and not re.match(r"Lieu", candidate, re.IGNORECASE):
					place = candidate
					if re.search(r"\b(?:in|at)$", place, re.IGNORECASE) and index + 2 < len(lines):
						place += " " + lines[lines.index(candidate, index) + 1]
					if len(place) <= 80 and not re.search(r"\bdate\b", place, re.IGNORECASE):
						found["place of hearing"] = place
					break
			break
	return found


def extract_case_metadata(text: str | None) -> dict[str, object]:
	"""Extract the complete metadata payload stored once on a case."""
	content = text or ""
	if not content.strip():
		return {}

	extracted = dict(_extract_metadata_with_quality(content))
	confidence = dict(extracted.get("_field_confidence") or {})
	sources = dict(extracted.get("_field_sources") or {})
	for field, value in _rpd_header_fields(content).items():
		extracted[field] = value
		confidence[field] = 0.9
		sources[field] = {"text": value}
	for field, (value, score) in derive_intelligence_fields(content, extracted).items():
		extracted[field] = value
		confidence[field] = score
		sources[field] = {"derived": value}
	outcome_detail = derive_outcome_payload(content, extracted)

	payload = {
		field: extracted[field]
		for field in ALL_FIELDS
		if extracted.get(field)
	}
	payload["_field_confidence"] = confidence
	payload["_field_sources"] = sources
	payload["_quality_flags"] = list(extracted.get("_quality_flags") or [])
	payload["_needs_review"] = bool(extracted.get("_needs_review"))
	payload["outcome detail"] = outcome_detail
	return payload


def extract_metadata_observations(text: str | None) -> list[MetadataObservation]:
	"""Return metadata captures, including fields without exact text-span matches."""
	content = text or ""
	if not content.strip():
		return []

	metadata = extract_case_metadata(content)
	confidence = dict(metadata.get("_field_confidence") or {})
	sources = dict(metadata.get("_field_sources") or {})
	rows: list[MetadataObservation] = []
	for field in ALL_FIELDS:
		value = str(metadata.get(field) or "").strip()
		if not value:
			continue
		field_sources = sources.get(field) or {}
		source_value = str(field_sources.get("text") or value).strip()
		span = _find_value_span(content, source_value) if source_value else None
		source_label = _field_source_label(field_sources)
		if span:
			start, end = span
			rows.append(
				MetadataObservation(
					field=field,
					text=content[start:end],
					value=value,
					offset_start=start,
					offset_end=end,
					confidence=float(confidence.get(field) or 0.0),
					source=source_label,
					span_matched=True,
				)
			)
			continue
		rows.append(
			MetadataObservation(
				field=field,
				text=source_value or value,
				value=value,
				offset_start=None,
				offset_end=None,
				confidence=float(confidence.get(field) or 0.0),
				source=source_label,
				span_matched=False,
			)
		)

	return rows


def extract_metadata_matches(text: str | None) -> list[MetadataMatch]:
	"""Return deterministic metadata fields that map to exact source spans."""
	matches: list[MetadataMatch] = []
	for row in extract_metadata_observations(text):
		if not row.span_matched or row.offset_start is None or row.offset_end is None:
			continue
		matches.append(
			MetadataMatch(
				field=row.field,
				text=row.text,
				value=row.value,
				offset_start=row.offset_start,
				offset_end=row.offset_end,
				confidence=row.confidence,
				source=row.source,
			)
		)
	return matches
