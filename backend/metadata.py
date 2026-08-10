from __future__ import annotations

import re
from dataclasses import dataclass

from fc_ingest.document_scraper import _extract_metadata_with_quality


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


@dataclass(frozen=True)
class MetadataMatch:
	field: str
	text: str
	value: str
	offset_start: int
	offset_end: int
	confidence: float
	source: str


def _find_value_span(text: str, value: str) -> tuple[int, int] | None:
	parts = value.split()
	if not parts:
		return None
	pattern = r"\s+".join(re.escape(part) for part in parts)
	match = re.search(pattern, text, re.IGNORECASE)
	if not match:
		return None
	return match.start(), match.end()


def extract_metadata_matches(text: str | None) -> list[MetadataMatch]:
	"""Return deterministic metadata fields that map to exact source spans."""
	content = text or ""
	if not content.strip():
		return []

	metadata = _extract_metadata_with_quality(content)
	confidence = metadata.get("_field_confidence") or {}
	sources = metadata.get("_field_sources") or {}
	matches: list[MetadataMatch] = []
	for field in METADATA_FIELDS:
		value = str(metadata.get(field) or "").strip()
		if not value:
			continue
		field_sources = sources.get(field) or {}
		source_value = str(field_sources.get("text") or value).strip()
		span = _find_value_span(content, source_value)
		if not span:
			continue
		start, end = span
		matches.append(
			MetadataMatch(
				field=field,
				text=content[start:end],
				value=value,
				offset_start=start,
				offset_end=end,
				confidence=float(confidence.get(field) or 0.0),
				source="text",
			)
		)

	return matches