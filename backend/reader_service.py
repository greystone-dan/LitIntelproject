"""Case reader, citation-pass, and metadata formatting service for AI CaseLibrary.

Owns reader payload assembly, metadata extraction formatting,
HTML source sanitization and citation markup wrapping, and citation-pass details.
"""

from __future__ import annotations

import re
import time
from collections import OrderedDict
from itertools import islice
from threading import RLock
from types import SimpleNamespace
from typing import Any

from fastapi import HTTPException, status
from sqlalchemy import Integer, and_, cast, func, or_, select
from sqlalchemy.orm import Session

from .citations import (
	RawCitationMatch,
	extract_case_citation_matches,
	extract_raw_citation_matches,
	extract_statute_reference_matches,
	is_self_case_name_match,
	parse_legislation_citation,
	resolve_legislation_reference,
)
from .case_formatter import format_decision
from .document_structure import locate_chunk_layers, map_span_to_located_layers
from .database import (
	Case,
	CaseChunk,
	CaseOutcome,
	CaseSource,
	CaseTag,
	Citation,
	CitationMetrics,
	StatuteReference,
)
from .statute_versioning import get_statute_version_label
from .citation_refine.pinpoints import target_paragraphs
from .paragraph_cited_by_db import load_paragraph_cited_by, load_pinpoint_cited_by
from .metadata import extract_metadata_observations
from .legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION
from .models import (
	CaseDiscussionUnitSummaryResponse,
	CaseEvidenceSpanResponse,
	CaseEvidenceSummaryResponse,
	CaseReaderChunkResponse,
	CaseReaderCitationResponse,
	CaseReaderDataResponse,
	CaseReaderExtractedSummaryItemResponse,
	CaseReaderMetadataFieldResponse,
	CaseReaderTagResponse,
	CaseSummaryResponse,
	CaseSummarySectionItemResponse,
	CaseSummarySectionResponse,
	CaseSubThemeSummaryResponse,
	CaseResponse,
	CaseSourceResponse,
	CitationMetricsResponse,
)
from scripts.inspect_discussion_units import inspect_case

_STATUTE_LIKE_RE = re.compile(
	r"\b(IRPA|IRPR|Charter|Act|Code|Regulations?|Convention|art\.)\b", re.IGNORECASE
)


def _normalize_whitespace(value: str) -> str:
	return " ".join((value or "").split()).strip()


def _is_statute_like_label(value: str | None) -> bool:
	text = (value or "").strip()
	return bool(_STATUTE_LIKE_RE.search(text))


def _is_irpa_irpr_reference(value: str | None) -> bool:
	return bool(
		re.search(
			r"\b(?:IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations?)\b",
			value or "",
			re.IGNORECASE,
		)
	)


_INSPECT_CACHE: "OrderedDict[tuple, tuple[float, dict[str, Any]]]" = OrderedDict()
_INSPECT_CACHE_MAX = 64
_INSPECT_CACHE_TTL_SECONDS = 3600
_INSPECT_CACHE_LOCK = RLock()


def _cached_inspect_case(db: Session, case_id: int, chunks: list[CaseChunk] | None) -> dict[str, Any]:
	"""Discussion-unit segmentation is pure compute (seconds per case), so reuse it per case until its chunks change."""
	key = None
	if chunks is not None:
		key = (case_id, tuple((chunk.id, chunk.text_hash) for chunk in chunks if (chunk.chunk_set or "") == "paragraph"))
		with _INSPECT_CACHE_LOCK:
			hit = _INSPECT_CACHE.get(key)
			if hit is not None and time.monotonic() - hit[0] < _INSPECT_CACHE_TTL_SECONDS:
				_INSPECT_CACHE.move_to_end(key)
				return hit[1]
	report = inspect_case(db, case_id, "paragraph", 0.35, 2)
	if key is not None:
		with _INSPECT_CACHE_LOCK:
			_INSPECT_CACHE[key] = (time.monotonic(), report)
			while len(_INSPECT_CACHE) > _INSPECT_CACHE_MAX:
				_INSPECT_CACHE.popitem(last=False)
	return report


def _build_evidence_summary(
	case_id: int,
	db: Session,
	*,
	has_paragraph_chunks: bool,
	chunks: list[CaseChunk] | None = None,
	citations: list[CaseReaderCitationResponse] | None = None,
) -> CaseEvidenceSummaryResponse | None:
	if not has_paragraph_chunks:
		return None
	report = _cached_inspect_case(db, case_id, chunks)
	units = []
	for unit in report["discussion_units"]:
		subthemes = []
		for subtheme in unit.get("subthemes", []):
			evidence = [
				CaseEvidenceSpanResponse(
					role=item["role"],
					text=item["text"],
					chunk_id=item["chunk_id"],
					start_offset=item["start_offset"],
					end_offset=item["end_offset"],
					paragraph_index=item["paragraph_index"],
					context_text=item["context_text"],
					source_text_hash=item["source_text_hash"],
				)
				for item in subtheme.get("argument_evidence", [])
			]
			subthemes.append(
				CaseSubThemeSummaryResponse(
					subtheme_id=subtheme["subtheme_id"],
					paragraph_indices=subtheme["paragraph_indices"],
					key_terms=subtheme["key_terms"],
					display_key_terms=subtheme.get("display_key_terms", subtheme["key_terms"]),
					argument_roles=subtheme["argument_roles"],
					explanation=subtheme["explanation"],
					evidence=evidence,
				)
			)
		units.append(
			CaseDiscussionUnitSummaryResponse(
				discussion_unit_id=unit["discussion_unit_id"],
				unit_index=int(unit["discussion_unit_id"].rsplit(":", 1)[-1]),
				start_paragraph=unit["start_paragraph"],
				end_paragraph=unit["end_paragraph"],
				paragraph_count=unit["paragraph_count"],
				subthemes=subthemes,
			)
		)

	# Build citation-to-subtheme mapping
	citation_mappings = {}
	if chunks and citations:
		chunks_by_id = {chunk.id: chunk for chunk in chunks if chunk.id is not None}

		for citation in citations:
			if citation.chunk_id is None or citation.id is None:
				continue

			chunk = chunks_by_id.get(citation.chunk_id)
			if chunk is None or chunk.paragraph_start is None:
				continue

			# Find subtheme(s) that contain this citation's paragraph
			citation_para = chunk.paragraph_start
			for unit in units:
				for subtheme in unit.subthemes:
					if citation_para in subtheme.paragraph_indices:
						citation_mappings[citation.id] = {
							"unit_index": unit.unit_index,
							"subtheme_id": subtheme.subtheme_id,
							"key_terms": subtheme.key_terms,
							"explanation": subtheme.explanation,
						}
						break

	return CaseEvidenceSummaryResponse(
		method="discussion_unit_v1",
		version="1.4",
		total_units=len(units),
		total_subthemes=sum(len(unit.subthemes) for unit in units),
		note="Evidence-based structural summary; not a legal conclusion. Each evidence span maps to canonical source text and a source hash.",
		units=units,
		citation_mappings=citation_mappings,
	)


def _build_case_summary(evidence_summary: CaseEvidenceSummaryResponse | None) -> CaseSummaryResponse | None:
	if evidence_summary is None:
		return None
	section_definitions = (
		("issue", "Issue", "issue"),
		("party_positions", "Party positions", "party_position"),
		("facts", "Facts and evidence", "evidence_fact"),
		("governing_law", "Governing law", "governing_rule"),
		("reasoning", "Court reasoning", "reasoning_application"),
		("limitations", "Limitations and counterarguments", "counterargument_limitation"),
		("disposition", "Disposition", "disposition"),
	)
	sections = []
	for section_id, title, role in section_definitions:
		items = []
		for unit in evidence_summary.units:
			for subtheme in unit.subthemes:
				if role not in subtheme.argument_roles:
					continue
				items.append(
					CaseSummarySectionItemResponse(
						section_role=role,
						subtheme_id=subtheme.subtheme_id,
						text=subtheme.explanation,
						paragraph_indices=list(subtheme.paragraph_indices),
						evidence=subtheme.evidence,
					)
				)
		sections.append(
			CaseSummarySectionResponse(
				section_id=section_id,
				title=title,
				available=bool(items),
				unavailable_reason=None if items else "Not detected in available evidence.",
				items=items,
			)
		)
	return CaseSummaryResponse(
		method="discussion_unit_brief_v1",
		version="1.0",
		disclaimer="Deterministic case brief from structured evidence; not a legal conclusion.",
		sections=sections,
		total_available_sections=sum(section.available for section in sections),
		total_unavailable_sections=sum(not section.available for section in sections),
	)


def _verified_reader_evidence_location(
	text: str, evidence: str | None, start: int | None, end: int | None,
	blocks: list[dict[str, Any]],
) -> tuple[dict[str, Any], int] | None:
	"""Verify an absolute excerpt, then map it by containment, never text search."""
	if not evidence or type(start) is not int or type(end) is not int:
		return None
	if not (0 <= start < end <= len(text)) or text[start:end] != evidence:
		return None
	for index, block in enumerate(blocks):
		if block["type"] != "para":
			continue
		paragraph_end = block["end"]
		for continuation in blocks[index + 1:]:
			if continuation["type"] not in {"text", "quote", "listitem"}:
				break
			paragraph_end = continuation["end"]
		if block["start"] <= start < end <= paragraph_end:
			return block, paragraph_end
	for block in blocks:
		if block["start"] <= start < end <= block["end"]:
			return block, block["end"]
	return None


def _build_reader_outcome_metadata(
	case: Case, outcome: CaseOutcome | None, blocks: list[dict[str, Any]]
) -> list[CaseReaderMetadataFieldResponse]:
	"""Project stored outcome evidence into existing reader metadata, without reclassification.

	The paragraph number is the formatter identity, not a chunk index. Only
	verified evidence inside one formatter paragraph can supply a quotation.
	"""
	if outcome is None:
		return []
	rows = []
	source = outcome.source or ""
	if outcome.decision_outcome and outcome.decision_outcome != "unclear":
		rows.append(CaseReaderMetadataFieldResponse(
			key="decision_outcome", value=outcome.decision_outcome, source=source,
		))
	text = case.full_text or ""
	evidence = outcome.disposition_evidence
	start, end = outcome.evidence_offset_start, outcome.evidence_offset_end
	location = _verified_reader_evidence_location(text, evidence, start, end, blocks)
	if location is None or location[0]["type"] != "para":
		return rows
	block, paragraph_end = location
	quote = text[block["start"]:paragraph_end]
	rows.extend([
		CaseReaderMetadataFieldResponse(
			key="disposition_paragraph", value=quote, source=source, evidence=quote,
		),
		CaseReaderMetadataFieldResponse(
			key="disposition_paragraph_number", value=str(block["num"]), source="formatter",
		),
	])
	return rows


def _build_reader_extracted_summary(
	case: Case, outcome: CaseOutcome | None, blocks: list[dict[str, Any]],
	tags: list[CaseTag], metadata: list[CaseReaderMetadataFieldResponse],
) -> list[CaseReaderExtractedSummaryItemResponse]:
	"""Read-only short projection; no prose, fallback summary text or inferred tags.

	Header values must match explicit source-header facts. Stored tags/outcomes
	require exact evidence at their stored document offsets; stale or unmappable
	evidence is omitted, never relocated to a coincidental occurrence.
	"""
	text = case.full_text or ""
	items: list[CaseReaderExtractedSummaryItemResponse] = []

	def add(
		key: str, label: str, value: str, source: str,
		evidence: str | None, start: int | None, end: int | None, *, paragraph_only: bool = False,
	) -> bool:
		location = _verified_reader_evidence_location(text, evidence, start, end, blocks)
		if not value or location is None:
			return False
		block, _ = location
		if paragraph_only and block["type"] != "para":
			return False
		items.append(CaseReaderExtractedSummaryItemResponse(
			key=key, label=label, value=value, source=source, evidence=evidence,
			start=start, end=end, block_start=block["start"], block_type=block["type"],
			paragraph_number=block.get("num") if block["type"] == "para" else None,
		))
		return True

	# Only the pre-reasons header is eligible for metadata. In particular, a
	# quoted case's date/judge/court in the reasons must not become this case's.
	header_end = next(
		(block["start"] for block in blocks if block["type"] in {"para", "doctitle"}),
		blocks[0]["end"] if blocks and blocks[0]["type"] == "meta" else 0,
	)
	header = text[:header_end]
	court = _normalize_whitespace(case.court or "")
	if court:
		match = re.search(r"(?mi)^[ \t]*(" + re.escape(court) + r")[ \t]*$", header)
		if match:
			add("court", "Court", court, "canonical_case",
				match.group(0), match.start(), match.end())
	if case.date is not None and hasattr(case.date, "strftime"):
		date_values = (
			str(case.date), case.date.strftime("%Y/%m/%d"), case.date.strftime("%Y%m%d"),
			f"{case.date.strftime('%B')} {case.date.day}, {case.date.year}",
		)
		match = re.search(
			r"(?mi)^[ \t]*(?:Date|Decision date|Date du jugement)[ \t]*:[ \t]*"
			r"(?:\n[ \t]*)?(" + "|".join(re.escape(value) for value in date_values) + r")[ \t]*$",
			header,
		)
		if match:
			add("date", "Decision date", match.group(1), "canonical_case",
				match.group(1), match.start(1), match.end(1))

	judge_candidates = [
		(row.value, row.source) for row in metadata
		if row.key == "judge" and row.evidence
		and _normalize_whitespace(row.evidence).casefold() == row.value.casefold()
	]
	stored = (getattr(case, "metadata_json", None) or {}).get("reader_extracted")
	if isinstance(stored, dict):
		field_sources = stored.get("_field_sources")
		judge_sources = field_sources.get("judge") if isinstance(field_sources, dict) else None
		value = stored.get("judge")
		if isinstance(value, str) and isinstance(judge_sources, dict):
			source_value = judge_sources.get("text")
			if isinstance(source_value, str) and (
				_normalize_whitespace(source_value).casefold()
				== _normalize_whitespace(value).casefold()
			):
				judge_candidates.append((_normalize_whitespace(value), "reader_extracted"))
	for value, source in judge_candidates:
		# Reuse the extracted value only in a judge-labelled header capture,
		# not by searching for the name in the body or a party caption.
		name = r"[ \t]+".join(re.escape(part) for part in value.split())
		if not name:
			continue
		match = re.search(
			r"(?mi)^[ \t]*(?:Judge|Judges|Present|Coram|Before|"
			r"Reasons for judgment(?: and judgment)? by|Judgment delivered by)"
			r"[ \t]*:[ \t]*(?:\n[ \t]*)?"
			# Only prefixes stripped by the metadata judge normalizer are eligible.
			# Keep them outside the capture so evidence offsets cover the name only.
			r"(?:(?:The[ \t]+)?(?:(?:Right[ \t]+)?Honourable|Honorable|L['’]honorable)[ \t]+)?"
			r"(?:(?:(?:monsieur|madame)[ \t]+)?(?:le|la)[ \t]+juge"
			r"(?:[ \t]+en[ \t]+chef(?:[ \t]+par[ \t]+int[ée]rim)?)?[ \t]+)?"
			r"(?:(?:Madame|Mme|M\.|Mme\.|Mr\.?|Mrs\.?|Madam|Mr\.?[ \t]+Justice|"
			r"Madame[ \t]+Justice|madame[ \t]+la[ \t]+juge[ \t]+en[ \t]+chef"
			r"[ \t]+par[ \t]+intérim)[ \t]+)?(" + name + r")[ \t]*$",
			header,
		)
		if match:
			if add("judge", "Judge", match.group(1), source,
				match.group(1), match.start(1), match.end(1)):
				break

	seen_tags: set[tuple[str, str]] = set()
	for tag in sorted(tags, key=lambda row: (-(row.score or 0), row.category, row.value)):
		pair = (tag.category, tag.value)
		if pair in seen_tags:
			continue
		if add(f"tag:{tag.category}", f"Tag ({tag.category})", tag.value, tag.source,
			tag.evidence, tag.offset_start, tag.offset_end, paragraph_only=True):
			seen_tags.add(pair)
		if len(seen_tags) >= 3:
			break

	if outcome is not None:
		location = _verified_reader_evidence_location(
			text, outcome.disposition_evidence, outcome.evidence_offset_start,
			outcome.evidence_offset_end, blocks,
		)
		if location and location[0]["type"] == "para":
			block, end = location
			quote = text[block["start"]:end]
			add("disposition", "Disposition · verbatim", quote, outcome.source or "",
				quote, block["start"], end, paragraph_only=True)
		if outcome.decision_outcome and outcome.decision_outcome != "unclear" and add("outcome", "Outcome", outcome.decision_outcome, outcome.source or "",
			outcome.disposition_evidence, outcome.evidence_offset_start,
			outcome.evidence_offset_end, paragraph_only=True):
			if outcome.source:
				add("outcome_source", "Outcome source", outcome.source, outcome.source,
					outcome.disposition_evidence, outcome.evidence_offset_start,
					outcome.evidence_offset_end, paragraph_only=True)
	return items



MAX_PINPOINT_TEXT_CASES = 12
# A pinpoint such as "paras 45-60" shows text for its first few paragraphs only, to keep the payload small.
MAX_PINPOINT_TEXT_PARAGRAPHS = 6


def _starts_with_paragraph(text: str | None, paragraph: int) -> bool:
	return bool(text) and re.match(rf"^\s*\[{int(paragraph)}\]", text) is not None


def paragraph_text_from_decision(full_text: str | None, paragraph: int) -> str | None:
	"""The stored text of one numbered paragraph, as the reader's formatter delimits it; ``None`` when absent."""
	for block in format_decision(full_text):
		if block.get("type") == "para" and block.get("num") == paragraph:
			return full_text[block["start"] : block["end"]].strip() or None
	return None


def _citation_target_paragraph(
	citation_text: str | None,
	normalized_citation: str | None,
	stored_target_paragraph: int | None = None,
) -> int | None:
	"""The first cited paragraph (``target_paragraphs`` has all of them)."""
	pins = target_paragraphs(citation_text, normalized_citation, stored_target_paragraph)
	return pins.first if pins is not None else None


def _pinpoint_response_fields(pins: Any, target_case_id: int | None, target_chunks: dict[tuple[int, int], str]) -> dict[str, Any]:
	"""Every paragraph the pinpoint names, the label, and stored text for the leading ones."""
	if pins is None or target_case_id is None:
		return {}
	texts = {
		str(paragraph): target_chunks[(target_case_id, paragraph)]
		for paragraph in pins.paragraphs[:MAX_PINPOINT_TEXT_PARAGRAPHS]
		if (target_case_id, paragraph) in target_chunks
	}
	return {
		"target_paragraphs": list(pins.paragraphs),
		"target_pinpoint_label": pins.label,
		"target_pinpoint_open_ended": pins.open_ended,
		"target_pinpoint_capped": pins.capped,
		"target_chunk_texts": texts,
	}


def _match_pinpoint_chunks(pinpoints_by_case: dict[int, list[int]], chunks: Any) -> dict[tuple[int, int], str]:
	"""Map (cited case, paragraph) to the text of the chunk covering it; one pass over the chunks."""
	matched: dict[tuple[int, int], str] = {}
	for chunk in chunks:
		for paragraph in pinpoints_by_case.get(chunk.case_id, ()):
			if chunk.paragraph_start <= paragraph <= chunk.paragraph_end:
				matched[(chunk.case_id, paragraph)] = chunk.text
	return matched


_PINPOINT_SQL_PATTERN = r"(?i)(?:para(?:s|graph(?:s)?)?\.?|paragraph(?:s)?)\s+(\d+)"


def _incoming_cited_case_counts(db: Session, case_id: int) -> dict[int, int]:
	"""Distinct citing cases per cited paragraph, aggregated in SQL (a heavily cited case has tens of thousands of rows)."""
	paragraph = func.coalesce(
		Citation.target_paragraph,
		cast(
			func.substring(
				func.coalesce(func.nullif(Citation.citation_text, ""), func.nullif(Citation.normalized_citation, ""), ""),
				_PINPOINT_SQL_PATTERN,
			),
			Integer,
		),
	)
	rows = db.execute(
		select(paragraph.label("paragraph"), func.count(func.distinct(Citation.source_case_id)).label("n"))
		.where(Citation.target_case_id == case_id, Citation.source_case_id != case_id)
		.group_by(paragraph)
	).all()
	return {int(row.paragraph): int(row.n) for row in rows if row.paragraph is not None}


def _cited_case_counts_by_paragraph(rows: Any, case_id: int) -> dict[int, int]:
	sources_by_paragraph: dict[int, set[int]] = {}
	for source_case_id, paragraph in rows:
		if source_case_id is None or source_case_id == case_id or paragraph is None:
			continue
		sources_by_paragraph.setdefault(int(paragraph), set()).add(int(source_case_id))
	return {paragraph: len(sources) for paragraph, sources in sources_by_paragraph.items()}


def _legislation_url_for_reference(value: str | None) -> str | None:
	"""Return the official Justice Laws section page for an IRPA/IRPR reference."""
	text = value or ""
	if not _is_irpa_irpr_reference(text):
		return None
	section = re.search(r"\b(?:s|ss)\.?\s*(\d{1,3}(?:\.\d+)?)", text, re.IGNORECASE)
	if section is None:
		section = re.search(r"\bsections?\s*(\d{1,3}(?:\.\d+)?)", text, re.IGNORECASE)
	if section is None:
		return None
	section_number = section.group(1)
	if re.search(r"\b(?:IRPR|Immigration and Refugee Protection Regulations?)\b", text, re.IGNORECASE):
		return f"https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-227/section-{section_number}.html"
	return f"https://laws-lois.justice.gc.ca/eng/acts/I-2.5/section-{section_number}.html"


_INFERRED_TAG_CACHE: "OrderedDict[tuple, list[CaseReaderTagResponse]]" = OrderedDict()
_INFERRED_TAG_CACHE_MAX = 128


def _build_reader_inferred_tags(case: Case, chunks: list[CaseChunk]) -> list[CaseReaderTagResponse]:
	"""Keyword tags over the whole decision (a few hundred ms on long ones), cached per case text."""
	key = (getattr(case, "id", None), hash(case.full_text or ""), hash(case.summary or ""), len(chunks))
	with _INSPECT_CACHE_LOCK:
		cached = _INFERRED_TAG_CACHE.get(key)
		if cached is not None:
			_INFERRED_TAG_CACHE.move_to_end(key)
			return list(cached)
	tags = _compute_reader_inferred_tags(case, chunks)
	with _INSPECT_CACHE_LOCK:
		_INFERRED_TAG_CACHE[key] = tags
		while len(_INFERRED_TAG_CACHE) > _INFERRED_TAG_CACHE_MAX:
			_INFERRED_TAG_CACHE.popitem(last=False)
	return list(tags)


def _compute_reader_inferred_tags(case: Case, chunks: list[CaseChunk]) -> list[CaseReaderTagResponse]:
	if case.full_text and case.full_text.strip():
		content = case.full_text
	else:
		text_parts: list[str] = [case.summary] if case.summary else []
		text_parts.extend(chunk.text for chunk in chunks if chunk.text)
		content = "\n".join(text_parts)
	if not content.strip():
		return []

	catalog: list[tuple[str, str, str]] = [
		("forum", "federal_court", r"\bFederal Court\b|\bFC\b"),
		("forum", "rad", r"\bRAD\b|Refugee Appeal Division"),
		("forum", "rpd", r"\bRPD\b|Refugee Protection Division"),
		("forum", "iad", r"\bIAD\b|Immigration Appeal Division"),
		("forum", "id", r"\bID\b|Immigration Division"),
		("forum", "irb", r"\bIRB\b|Immigration and Refugee Board"),
		("statute", "irpa", r"\b(?:IRPA|Immigration and Refugee Protection Act)\b"),
		("statute", "irpr", r"\b(?:IRPR|Immigration and Refugee Protection Regulations?)\b"),
		("issue", "procedural_fairness", r"procedural fairness|natural justice|right to be heard|fair hearing"),
		("issue", "reasonableness", r"\breasonableness\b|unreasonable decision|reasonable decision"),
		("issue", "standard_of_review", r"standard of review|palpable and overriding error|correctness standard"),
		("issue", "credibility", r"\bcredibility\b|credible evidence|credibility finding"),
		("issue", "jurisdiction", r"\bjurisdiction\b|jurisdictional error"),
		("issue", "delay", r"\bdelay\b|unreasonable delay|mandamus"),
		("issue", "detention", r"\bdetention\b|detained|detention review"),
		("issue", "removal", r"\bremoval\b|removal order|pre-removal risk assessment|\bPRRA\b"),
		("issue", "inadmissibility", r"inadmissib|security certificate|organized criminality|misrepresentation"),
		("issue", "refugee_protection", r"refugee protection|Convention refugee|person in need of protection|\bclaimant\b"),
		("issue", "humanitarian_compassionate", r"humanitarian and compassionate|\bH&C\b|\bH[.]\s*&\s*C[.]\b"),
		("issue", "family_reunification", r"family reunification|family class|spousal sponsorship|sponsorship application"),
		("issue", "temporary_residence", r"temporary resident|study permit|work permit|visitor visa|temporary foreign worker"),
		("issue", "citizenship", r"\bcitizenship\b|citizenship application|citizenship revocation"),
		("analysis", "ifa", r"\bIFA\b|internal flight alternative|alternative of internal flight"),
		("analysis", "charter", r"\bCharter\b|Canadian Charter of Rights and Freedoms|section 7 of the Charter"),
		("analysis", "statutory_interpretation", r"statutory interpretation|purposive interpretation|modern principle of interpretation"),
		("analysis", "adr", r"\bADR\b|\bAdministrative\s+Deferral\s+of\s+Removal\b"),
	]

	tags: list[CaseReaderTagResponse] = []
	max_occurrences_per_tag = 50
	for category, value, pattern in catalog:
		for match in islice(re.finditer(pattern, content, flags=re.IGNORECASE), max_occurrences_per_tag):
			evidence = content[max(0, match.start() - 80) : min(len(content), match.end() + 80)].strip()
			tags.append(
				CaseReaderTagResponse(
					category=category,
					value=value,
					score=0.9,
					evidence=evidence,
						offset_start=match.start(),
						offset_end=match.end(),
					source="reader_keyword",
					taxonomy_version="reader_v1",
				)
			)

	section_hits: dict[str, str] = {}

	def add_section_tag(tag_value: str, evidence: str) -> None:
		if not tag_value or tag_value in section_hits:
			return
		section_hits[tag_value] = evidence

	for match in re.finditer(
		r"\b(?:IRPA|IRPR)\s+(?:s\.|section)\s*(\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)",
		content,
		flags=re.IGNORECASE,
	):
		section = _normalize_whitespace(match.group(1))
		prefix = "irpr" if re.search(r"\bIRPR\b", match.group(0), flags=re.IGNORECASE) else "irpa"
		add_section_tag(
			f"{prefix}_s_{section}",
			content[max(0, match.start() - 80) : min(len(content), match.end() + 80)].strip(),
		)
		if len(section_hits) >= 20:
			break

	for match in re.finditer(
		r"\b(?:ss?\.|sections?|subsections?|paragraphs?)\s*(\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*(?:\s*(?:to|-|and|or)\s*\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)*)\s+of\s+(?:the\s+)?(IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations|Canadian Charter of Rights and Freedoms|Charter|Criminal Code)\b",
		content,
		flags=re.IGNORECASE,
	):
		sections = match.group(1)
		law = match.group(2)
		prefix = (
			"irpr"
			if re.search(r"\bIRPR\b", law, flags=re.IGNORECASE)
			else "charter"
			if re.search(r"\bCharter\b", law, flags=re.IGNORECASE)
			else "criminal_code"
			if re.search(r"\bCriminal Code\b", law, flags=re.IGNORECASE)
			else "irpa"
		)
		for section_match in re.finditer(r"\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*", sections):
			section = _normalize_whitespace(section_match.group(0))
			add_section_tag(
				f"{prefix}_s_{section}",
				content[max(0, match.start() - 80) : min(len(content), match.end() + 80)].strip(),
			)
		if len(section_hits) >= 20:
			break

	for section, evidence in section_hits.items():
		tags.append(
			CaseReaderTagResponse(
				category="statute_section",
				value=section,
				score=0.85,
				evidence=evidence,
					offset_start=None,
					offset_end=None,
				source="reader_keyword",
				taxonomy_version="reader_v1",
			)
		)

	return tags


def _build_reader_extracted_metadata(
	case: Case,
	chunks: list[CaseChunk],
	*,
	include_canonical_fields: bool = True,
) -> list[CaseReaderMetadataFieldResponse]:
	text_parts: list[str] = []
	if case.full_text:
		text_parts.append(case.full_text)
	if case.summary:
		text_parts.append(case.summary)
	for chunk in chunks[:2]:
		if chunk.text:
			text_parts.append(chunk.text)
	content = "\n".join(text_parts)

	rows: list[CaseReaderMetadataFieldResponse] = []
	seen: set[tuple[str, str]] = set()

	def add_row(
		key: str, value: str | None, evidence: str | None = None, source: str = "reader_extracted"
	) -> None:
		if value is None:
			return
		clean = _normalize_whitespace(value)
		if not clean:
			return
		pair = (key, clean)
		if pair in seen:
			return
		seen.add(pair)
		rows.append(CaseReaderMetadataFieldResponse(key=key, value=clean, source=source, evidence=evidence))

	if include_canonical_fields:
		add_row("decision_date", str(case.date), source="canonical_case")
		if hasattr(case.date, "day") and hasattr(case.date, "strftime"):
			add_row(
				"decision_date_written",
				f"{case.date.strftime('%B')} {case.date.day}, {case.date.strftime('%Y')}",
				source="canonical_case",
			)

	court = str(case.court or "")
	court_type = (
		"SC"
		if re.search(r"Supreme Court of Canada|\bSCC\b", court, flags=re.IGNORECASE)
		else "FCA"
		if re.search(r"Federal Court of Appeal|\bFCA\b", court, flags=re.IGNORECASE)
		else "FC"
		if re.search(r"Federal Court|\bFC\b", court, flags=re.IGNORECASE)
		else None
	)
	if court_type:
		add_row("court_type", court_type, evidence=court, source="reader_derived")
	case_number_match = re.search(
		r"\b(?:Docket|Case\s+number|File\s+number)\s*[:#-]?\s*([A-Z][A-Z0-9]{0,5}[- ]?\d{1,6}(?:[-/]\d{1,4})?|\d{1,6})\b",
		content,
		flags=re.IGNORECASE,
	)
	if case_number_match is not None:
		case_number = _normalize_whitespace(case_number_match.group(1)).replace(" ", "-").upper()
		add_row("case_number", case_number, evidence=case_number_match.group(0), source="reader_extracted")
		add_row("docket", case_number, evidence=case_number_match.group(0), source="reader_extracted")

	for match in re.finditer(r"\bIMM[- ]?\d{1,6}-\d{2}\b", content, flags=re.IGNORECASE):
		add_row("imm_number", match.group(0).upper().replace(" ", "-"), evidence=match.group(0))

	match = re.search(r"\b([A-Z][a-z]+,\s+[A-Z][A-Za-z ]+),\s+[A-Z][a-z]+\s+\d{1,2},\s+\d{4}\b", content)
	if match is not None:
		add_row("location", match.group(1), evidence=match.group(0))

	match = re.search(
		r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(?:19|20)\d{2}\b",
		content,
		flags=re.IGNORECASE,
	)
	if match is not None:
		add_row("decision_date_written", match.group(0), evidence=match.group(0))

	match = re.search(
		r"\bDate\s*[:\-]?\s*((?:19|20)\d{2}[-/](?:0[1-9]|1[0-2])[-/](?:0[1-9]|[12]\d|3[01]))",
		content,
		flags=re.IGNORECASE,
	)
	if match is not None:
		add_row("decision_date_text", match.group(1).replace("/", "-"), evidence=match.group(0))

	match = re.search(
		r"(The\s+Honourable[^\n\r]{0,100}?Justice\s+[A-Z][A-Za-z'\-]+)", content, flags=re.IGNORECASE
	)
	if match is not None:
		add_row("judge", match.group(1), evidence=match.group(0))

	match = re.search(r"\bApplicants\s+and\s+(.{8,180}?)\s+Respondent\b", content, flags=re.IGNORECASE | re.DOTALL)
	if match is None:
		match = re.search(r"\band\s+(.{8,180}?)\s+Respondent\b", content, flags=re.IGNORECASE | re.DOTALL)
	if match is not None:
		candidate = _normalize_whitespace(match.group(1))
		candidate = re.sub(r"^[^A-Za-z]+", "", candidate)
		candidate = re.sub(r"[^A-Za-z)\]'.\- ]+$", "", candidate)
		if candidate.isupper():
			candidate = candidate.title()
		add_row("respondent", candidate, evidence=_normalize_whitespace(match.group(0)))

	minister_match = re.search(
		r"\bThe\s+Minister\s+of\s+Citizenship\s+and\s+Immigration\b",
		content,
		flags=re.IGNORECASE,
	)
	if minister_match is not None:
		add_row(
			"respondent",
			"The Minister of Citizenship and Immigration",
			evidence=minister_match.group(0),
		)

	match = re.search(r"\bcitizens\s+of\s+([A-Z][A-Za-z'\- ]{2,60})\b", content, flags=re.IGNORECASE)
	if match is not None:
		add_row("country", match.group(1).title(), evidence=match.group(0))

	preferred_order = {
		"imm_number": 0,
		"decision_date": 1,
		"decision_date_written": 2,
		"decision_date_text": 3,
		"location": 4,
		"judge": 5,
		"respondent": 6,
		"country": 7,
	}
	return sorted(rows, key=lambda row: (preferred_order.get(row.key, 99), row.key, row.value))


def _build_metadata_pass_normalized_rows(
	case: Case, extracted: list[CaseReaderMetadataFieldResponse]
) -> list[dict[str, str]]:
	values = {row.key: row.value for row in extracted}
	style = values.get("style_of_cause_text") or case.title
	style = str(style or "").title()
	style = re.sub(r"\s+V\.?\s+", " v. ", style, flags=re.IGNORECASE)
	style = re.sub(
		r"\b(Of|And|The)\b",
		lambda match: match.group(1).lower() if match.group(1) in {"Of", "And"} else "The",
		style,
	)
	rows = [
		{"key": "tribunal", "value": case.court or ""},
		{"key": "court_type", "value": values.get("court_type", "")},
		{"key": "case_number", "value": values.get("case_number", case.source_id or "")},
		{"key": "style_of_cause", "value": style},
	]
	if values.get("respondent"):
		respondent = re.sub(
			r"\b(Of|And|The)\b",
			lambda match: match.group(1).lower() if match.group(1) in {"Of", "And"} else "The",
			str(values["respondent"]).title(),
		)
		rows.append({"key": "respondent", "value": respondent})
	if getattr(case, "language", None):
		rows.append({"key": "language", "value": str(case.language).lower()})
	return [row for row in rows if row["value"]]


def get_case_metadata_pass(
	case_id: int,
	db: Session,
	*,
	get_case_fn: Any | None = None,
	build_extracted_fn: Any | None = None,
	build_normalized_fn: Any | None = None,
) -> dict[str, object]:
	get_case = get_case_fn or (lambda cid, session: session.scalar(select(Case).where(Case.id == cid)))
	case = get_case(case_id, db)
	if case is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
	chunks = list(
		db.scalars(
			select(CaseChunk).where(CaseChunk.case_id == case.id).order_by(CaseChunk.chunk_index)
		)
	)
	build_extracted = build_extracted_fn or _build_reader_extracted_metadata
	build_normalized = build_normalized_fn or _build_metadata_pass_normalized_rows
	extracted = build_extracted(case, chunks, include_canonical_fields=False)
	return {
		"case_id": case.id,
		"extracted": [row.model_dump() for row in extracted],
		"normalized_display": build_normalized(case, extracted),
	}


def get_case_statute_references(case_id: int, db: Session) -> list[CaseReaderCitationResponse]:
	if db.scalar(select(Case.id).where(Case.id == case_id)) is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
	rows = db.scalars(
		select(StatuteReference)
		.where(StatuteReference.source_case_id == case_id)
		.order_by(StatuteReference.chunk_id, StatuteReference.offset_start, StatuteReference.id)
	)

	def build_raw_match(reference: StatuteReference) -> RawCitationMatch:
		citation_text = reference.reference_text or reference.normalized_reference or ""
		normalized_citation = reference.normalized_reference or citation_text
		offset_start = reference.offset_start if reference.offset_start is not None else 0
		offset_end = reference.offset_end if reference.offset_end is not None else offset_start
		return RawCitationMatch(
			reference.reference_kind,
			citation_text,
			normalized_citation,
			offset_start,
			offset_end,
		)

	def build_response(reference: StatuteReference) -> CaseReaderCitationResponse:
		resolution = resolve_legislation_reference(db, build_raw_match(reference))
		authority_document = resolution.document
		authority_section = resolution.section
		legislation_url = reference.legislation_url or (
			authority_document.source_url if authority_document is not None else None
		)
		version_label = get_statute_version_label(getattr(reference, "statute_version", None))
		return CaseReaderCitationResponse(
			id=-1000000 - reference.id,
			citation_kind=reference.reference_kind,
			chunk_id=reference.chunk_id,
			offset_start=reference.offset_start,
			offset_end=reference.offset_end,
			citation_text=reference.reference_text,
			normalized_citation=reference.normalized_reference,
			instrument_key=resolution.instrument_key or reference.instrument_key,
			pinpoint=resolution.pinpoint or reference.pinpoint,
			target_case_id=None,
			target_title=None,
			target_citation=None,
			provenance="statute_references",
			legislation_url=legislation_url,
			authority_document_title=authority_document.title if authority_document is not None else None,
			authority_document_url=authority_document.source_url if authority_document is not None else None,
			authority_section_number=authority_section.section_number if authority_section is not None else None,
			authority_section_text=authority_section.text if authority_section is not None else None,
			source_title=authority_document.title if authority_document is not None else None,
			source_text=authority_section.text if authority_section is not None else None,
			source_url=legislation_url,
			resolution_status=resolution.resolution_status,
			section_number=resolution.provision_section or reference.provision_section,
			provision_text=authority_section.text if authority_section is not None else None,
			provision_section=resolution.provision_section or reference.provision_section,
			provision_subsection=resolution.provision_subsection or reference.provision_subsection,
			provision_paragraph=resolution.provision_paragraph or reference.provision_paragraph,
			provision_nested_depth=resolution.provision_nested_depth,
			provision_is_range_or_list=resolution.is_range_or_list or reference.provision_is_range_or_list,
			unresolved=resolution.resolution_status != "resolved_section",
			statute_version_label=version_label,
		)
	return [
		build_response(reference)
		for reference in rows
	]


def build_case_reader_data(case_id: int, db: Session, include_evidence: bool = True) -> CaseReaderDataResponse:
	case = db.scalar(select(Case).where(Case.id == case_id))
	if case is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")

	sources = list(
		db.scalars(
			select(CaseSource)
			.where(CaseSource.case_id == case_id)
			.order_by(CaseSource.is_primary.desc(), CaseSource.id)
		)
	)
	all_chunks = list(
		db.scalars(
			select(CaseChunk)
			.where(
				CaseChunk.case_id == case_id,
				CaseChunk.chunk_set.in_(["paragraph", "section", "full_case", "legacy"]),
			)
			.order_by(CaseChunk.chunk_index)
		)
	)
	chunks = list(all_chunks)
	if any((chunk.chunk_set or "") == "paragraph" for chunk in chunks):
		chunks = [chunk for chunk in chunks if (chunk.chunk_set or "") == "paragraph"]
	elif chunks:
		if any((chunk.chunk_set or "") == "section" for chunk in chunks):
			chunks = [chunk for chunk in chunks if (chunk.chunk_set or "") == "section"]
		elif any((chunk.chunk_set or "") == "full_case" for chunk in chunks):
			chunks = [chunk for chunk in chunks if (chunk.chunk_set or "") == "full_case"]
		elif any((chunk.chunk_set or "") == "legacy" for chunk in chunks):
			chunks = [chunk for chunk in chunks if (chunk.chunk_set or "") == "legacy"]
	tags = list(
		db.scalars(
			select(CaseTag)
			.where(
				CaseTag.case_id == case_id,
				CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
			)
			.order_by(CaseTag.category, CaseTag.value)
		)
	)
	inferred_tags = _build_reader_inferred_tags(case, chunks)
	extracted_metadata = _build_reader_extracted_metadata(case, chunks)

	target_case = Case.__table__.alias("target_case")
	citation_rows = db.execute(
		select(
			Citation,
			target_case.c.id,
			target_case.c.title,
			target_case.c.citation,
		)
		.outerjoin(target_case, target_case.c.id == Citation.target_case_id)
		.where(Citation.source_case_id == case_id)
		.order_by(Citation.chunk_id, Citation.offset_start, Citation.id)
	)
	stored_citations = list(citation_rows)

	pins_by_citation = {
		citation.id: target_paragraphs(citation.citation_text, citation.normalized_citation)
		for citation, target_case_id, _, _ in stored_citations
		if target_case_id is not None
	}

	def target_paragraph(citation: Citation) -> int | None:
		pins = pins_by_citation.get(citation.id)
		return pins.first if pins is not None else None

	# Every paragraph a pinpoint names (cited-by), and the leading ones whose text is shown.
	target_pinpoints = {
		(target_case_id, paragraph)
		for citation, target_case_id, _, _ in stored_citations
		if target_case_id is not None and pins_by_citation.get(citation.id) is not None
		for paragraph in pins_by_citation[citation.id].paragraphs[:MAX_PINPOINT_TEXT_PARAGRAPHS]
	}
	target_chunks: dict[tuple[int, int], str] = {}
	if target_pinpoints:
		# Fetch only the paragraph chunks that cover a cited pinpoint (not every paragraph of every cited case).
		pinpoints_by_case: dict[int, list[int]] = {}
		for target_case_id, paragraph in target_pinpoints:
			pinpoints_by_case.setdefault(target_case_id, []).append(paragraph)
		target_paragraph_chunks = db.scalars(
			select(CaseChunk)
			.where(
				CaseChunk.chunk_set == "paragraph",
				CaseChunk.paragraph_start.is_not(None),
				CaseChunk.paragraph_end.is_not(None),
				or_(
					*(
						and_(
							CaseChunk.case_id == target_case_id,
							CaseChunk.paragraph_start <= max(paragraphs),
							CaseChunk.paragraph_end >= min(paragraphs),
						)
						for target_case_id, paragraphs in pinpoints_by_case.items()
					)
				),
			)
		)
		best_span: dict[tuple[int, int], int] = {}
		for chunk in target_paragraph_chunks:
			for target_case_id, paragraph in target_pinpoints:
				if (
					chunk.case_id == target_case_id
					and chunk.paragraph_start <= paragraph <= chunk.paragraph_end
				):
					key = (target_case_id, paragraph)
					# The narrowest chunk that holds the paragraph wins, not whichever is read last.
					span = chunk.paragraph_end - chunk.paragraph_start
					if key not in best_span or span < best_span[key]:
						best_span[key] = span
						target_chunks[key] = chunk.text
		# Paragraph text from the stored decision itself where no chunk starts at that paragraph (large cases are
		# chunked coarsely). Bounded, and stored text only.
		missing = sorted(
			key for key in target_pinpoints
			if not _starts_with_paragraph(target_chunks.get(key), key[1])
		)
		if missing:
			wanted: dict[int, set[int]] = {}
			for target_case_id, paragraph in missing:
				if len(wanted) >= MAX_PINPOINT_TEXT_CASES and target_case_id not in wanted:
					continue
				wanted.setdefault(target_case_id, set()).add(paragraph)
			for target_case_id, full_text in db.execute(
				select(Case.id, Case.full_text).where(Case.id.in_(wanted))
			):
				for paragraph in wanted[target_case_id]:
					text = paragraph_text_from_decision(full_text, paragraph)
					if text:
						target_chunks[(target_case_id, paragraph)] = text
					else:
						target_chunks.pop((target_case_id, paragraph), None)

	citation_responses = [
		CaseReaderCitationResponse(
			id=citation.id,
			citation_kind=citation.citation_kind,
			chunk_id=citation.chunk_id,
			offset_start=citation.offset_start,
			offset_end=citation.offset_end,
			citation_text=citation.citation_text,
			normalized_citation=citation.normalized_citation,
			target_case_id=target_case_id,
			target_title=target_title,
			target_citation=target_citation,
			target_paragraph=target_paragraph(citation),
			target_chunk_text=target_chunks.get((target_case_id, paragraph))
			if target_case_id is not None and (paragraph := target_paragraph(citation)) is not None
			else None,
			**_pinpoint_response_fields(pins_by_citation.get(citation.id), target_case_id, target_chunks),
			provenance=citation.provenance,
			unresolved=citation.unresolved,
		)
		for citation, target_case_id, target_title, target_citation in stored_citations
	]
	citation_responses = [
		row
		for row in citation_responses
		if not is_self_case_name_match(
			case.title,
			RawCitationMatch(
				kind=row.citation_kind,
				citation_text=row.citation_text or "",
				normalized_citation=row.normalized_citation or "",
				offset_start=row.offset_start or 0,
				offset_end=row.offset_end or 0,
			),
		)
	]

	selected_chunk_ids = {chunk.id for chunk in chunks if chunk.id is not None}

	case_text = case.full_text or case.summary or ""
	chunks_by_id = {chunk.id: chunk for chunk in all_chunks if chunk.id is not None}
	located_chunks = locate_chunk_layers(case_text, all_chunks)
	chunk_starts: dict[int, int] = {}
	for citation in citation_responses:
		if citation.offset_start is None or citation.offset_end is None:
			continue
		absolute_start = citation.offset_start
		absolute_end = citation.offset_end
		if citation.chunk_id is not None:
			chunk = chunks_by_id.get(citation.chunk_id)
			if chunk is None:
				continue
			if citation.chunk_id not in chunk_starts:
				chunk_starts[citation.chunk_id] = case_text.find(chunk.text)
			chunk_start = chunk_starts[citation.chunk_id]
			if chunk_start < 0:
				continue
			absolute_start = chunk_start + citation.offset_start
			absolute_end = chunk_start + citation.offset_end
		layer_spans = map_span_to_located_layers(len(case_text), absolute_start, absolute_end, located_chunks)
		citation.layer_spans = {
			layer: {
				"chunk_id": span.chunk_id,
				"absolute_start": span.absolute_start,
				"absolute_end": span.absolute_end,
				"local_start": span.local_start,
				"local_end": span.local_end,
			}
			for layer, span in layer_spans.items()
		}
		paragraph_span = layer_spans.get("paragraph")
		if citation.chunk_id not in selected_chunk_ids and paragraph_span is not None:
			citation.chunk_id = paragraph_span.chunk_id
			citation.offset_start = paragraph_span.local_start
			citation.offset_end = paragraph_span.local_end

	metrics = db.scalar(select(CitationMetrics).where(CitationMetrics.case_id == case_id))
	formatted_html = None
	evidence_summary = (
		_build_evidence_summary(
			case_id,
			db,
			has_paragraph_chunks=any((chunk.chunk_set or "") == "paragraph" for chunk in all_chunks),
			chunks=all_chunks,
			citations=citation_responses,
		)
		if include_evidence
		else None
	)
	case_summary = _build_case_summary(evidence_summary)
	cited_paragraph_counts = _incoming_cited_case_counts(db, case_id)

	format_blocks = format_decision(case.full_text, cited_paragraph_counts)
	# Optional stored data: a missing table (migration not applied yet) must never break the reader.
	try:
		with db.begin_nested():
			paragraph_cited_by = load_paragraph_cited_by(db, case_id)
			target_cited_by = load_pinpoint_cited_by(
				db,
				{
					(row.target_case_id, tuple(row.target_paragraphs or ()))
					for row in citation_responses
					if row.target_case_id is not None and row.target_paragraphs
				},
			)
	except Exception:  # noqa: BLE001
		paragraph_cited_by, target_cited_by = None, {}
	for row in citation_responses:
		if row.target_case_id is not None and row.target_paragraphs:
			row.target_cited_by = target_cited_by.get((row.target_case_id, tuple(row.target_paragraphs)))
	outcome = db.scalar(
		select(CaseOutcome).where(CaseOutcome.case_id == case_id)
		.order_by(CaseOutcome.updated_at.desc(), CaseOutcome.id.desc()).limit(1)
	)
	extracted_metadata += _build_reader_outcome_metadata(case, outcome, format_blocks)

	return CaseReaderDataResponse(
		case=CaseResponse.model_validate(case, from_attributes=True),
		paragraph_cited_by=paragraph_cited_by,
		format_blocks=format_blocks,
		extracted_summary=_build_reader_extracted_summary(
			case, outcome, format_blocks, tags, extracted_metadata,
		),
		sources=[CaseSourceResponse.model_validate(row, from_attributes=True) for row in sources],
		chunks=[
			CaseReaderChunkResponse(
				id=chunk.id,
				chunk_set=chunk.chunk_set,
				chunk_index=chunk.chunk_index,
				chunk_label=chunk.chunk_label,
				paragraph_start=chunk.paragraph_start,
				paragraph_end=chunk.paragraph_end,
				text=chunk.text or "",
				text_length=len(chunk.text or ""),
				token_estimate=int(chunk.token_estimate or 0),
				created_at=chunk.created_at,
			)
			for chunk in chunks
		],
		citations=citation_responses,
		tags=[CaseReaderTagResponse.model_validate(tag, from_attributes=True) for tag in tags]
		+ inferred_tags,
		extracted_metadata=extracted_metadata,
		metrics=CitationMetricsResponse.model_validate(metrics, from_attributes=True)
		if metrics is not None
		else None,
		formatted_html=formatted_html,
		evidence_summary=evidence_summary,
		case_summary=case_summary,
	)


def build_case_evidence(case_id: int, db: Session) -> dict[str, Any]:
	"""Discussion-unit evidence and case summary alone, so the reader can load them after the decision text."""
	if db.scalar(select(Case.id).where(Case.id == case_id)) is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
	all_chunks = list(
		db.scalars(
			select(CaseChunk)
			.where(
				CaseChunk.case_id == case_id,
				CaseChunk.chunk_set.in_(["paragraph", "section", "full_case", "legacy"]),
			)
			.order_by(CaseChunk.chunk_index)
		)
	)
	citation_rows = db.execute(
		select(Citation.id, Citation.chunk_id).where(Citation.source_case_id == case_id)
	).all()
	citations = [SimpleNamespace(id=row.id, chunk_id=row.chunk_id) for row in citation_rows]
	evidence_summary = _build_evidence_summary(
		case_id,
		db,
		has_paragraph_chunks=any((chunk.chunk_set or "") == "paragraph" for chunk in all_chunks),
		chunks=all_chunks,
		citations=citations,
	)
	case_summary = _build_case_summary(evidence_summary)
	return {
		"evidence_summary": evidence_summary.model_dump(mode="json") if evidence_summary else None,
		"case_summary": case_summary.model_dump(mode="json") if case_summary else None,
	}


def build_case_citation_pass(
	case_id: int,
	db: Session,
	*,
	get_case_fn: Any | None = None,
	extract_case_fn: Any | None = None,
	extract_statute_fn: Any | None = None,
	extract_metadata_fn: Any | None = None,
) -> dict[str, Any]:
	get_case = get_case_fn or (lambda cid, session: session.scalar(select(Case).where(Case.id == cid)))
	case = get_case(case_id, db)
	if case is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")

	full_text = case.full_text or case.summary or ""
	extract_case = extract_case_fn or extract_case_citation_matches
	extract_statute = extract_statute_fn or extract_statute_reference_matches
	extract_metadata = extract_metadata_fn or extract_metadata_observations

	live_rows = extract_case(full_text)
	statute_rows = extract_statute(full_text)
	metadata_rows = extract_metadata(full_text)
	live_payload = [
		{
			"kind": match.kind,
			"citation_text": match.citation_text,
			"normalized_citation": match.normalized_citation,
			"offset_start": match.offset_start,
			"offset_end": match.offset_end,
			"context": full_text[
				max(0, (match.offset_start or 0) - 40) : min(len(full_text), (match.offset_end or 0) + 40)
			]

			.replace("\n", " ")
			.strip(),
		}
		for match in live_rows
	]
	statute_payload = [
		{
			"kind": match.kind,
			"citation_text": match.citation_text,
			"normalized_citation": match.normalized_citation,
			"offset_start": match.offset_start,
			"offset_end": match.offset_end,
			"context": full_text[
				max(0, match.offset_start - 40) : min(len(full_text), match.offset_end + 40)
			]
			.replace("\n", " ")
			.strip(),
		}
		for match in statute_rows
	]
	metadata_payload = [
		{
			"field": match.field,
			"text": match.text,
			"value": match.value,
			"offset_start": match.offset_start,
			"offset_end": match.offset_end,
			"confidence": match.confidence,
			"source": match.source,
			"span_matched": match.span_matched,
			"context": (
				full_text[
					max(0, match.offset_start - 40) : min(len(full_text), match.offset_end + 40)
				]
				.replace("\n", " ")
				.strip()
				if match.span_matched and match.offset_start is not None and match.offset_end is not None
				else ""
			),
		}
		for match in metadata_rows
	]

	return {
		"case": {
			"id": case.id,
			"title": case.title,
			"citation": case.citation,
			"court": case.court,
			"date": case.date,
			"summary": case.summary,
			"full_text": case.full_text,
		},
		"summary": {
			"live_total": len(live_payload),
			"statute_total": len(statute_payload),
			"metadata_total": len(metadata_payload),
		},
		"live_extracted": live_payload,
		"live_statutes": statute_payload,
		"live_metadata": metadata_payload,
	}


def _citation_pass_chunks(
	db: Session,
	case_id: int,
	full_text: str,
	offset_start: int,
	offset_end: int,
) -> list[dict[str, Any]]:
	def _is_paragraph_chunk(chunk_set: str | None) -> bool:
		value = (chunk_set or "").strip().lower()
		return value == "paragraph" or value.startswith("paragraph_")

	chunks = list(
		db.scalars(
			select(CaseChunk)
			.where(CaseChunk.case_id == case_id)
			.order_by(CaseChunk.chunk_set, CaseChunk.chunk_index, CaseChunk.id)
		)
	)
	locations: list[dict[str, Any]] = []
	for chunk in chunks:
		chunk_text = chunk.text or ""
		search_start = 0
		while chunk_text:
			chunk_start = full_text.find(chunk_text, search_start)
			if chunk_start < 0:
				break
			chunk_end = chunk_start + len(chunk_text)
			if chunk_start <= offset_start and offset_end <= chunk_end:
				relative_start = offset_start - chunk_start
				relative_end = offset_end - chunk_start
				locations.append(
					{
						"chunk_id": chunk.id,
						"chunk_set": chunk.chunk_set,
						"chunk_index": chunk.chunk_index,
						"chunk_label": chunk.chunk_label,
						"paragraph_start": chunk.paragraph_start,
						"paragraph_end": chunk.paragraph_end,
						"document_start": chunk_start,
						"document_end": chunk_end,
						"offset_start": relative_start,
						"offset_end": relative_end,
						"citation_text": chunk_text[relative_start:relative_end],
						"text": chunk_text,
						"text_length": len(chunk_text),
						"token_estimate": chunk.token_estimate,
						"is_paragraph_chunk": _is_paragraph_chunk(chunk.chunk_set),
					}
				)
				break
			search_start = chunk_start + 1
	locations.sort(
		key=lambda row: (
			0 if row.get("is_paragraph_chunk") else 1,
			abs((row.get("text_length") or 0) - (offset_end - offset_start)),
			str(row.get("chunk_set") or ""),
			int(row.get("chunk_index") or 0),
		)
	)
	return locations


def _stored_case_citation_details(
	db: Session,
	case_id: int,
	selected: Any,
	chunks: list[dict[str, Any]],
) -> list[dict[str, Any]]:
	chunk_locations = {int(chunk["chunk_id"]): chunk for chunk in chunks}
	rows = list(
		db.scalars(select(Citation).where(Citation.source_case_id == case_id).order_by(Citation.id))
	)
	details: list[dict[str, Any]] = []
	for citation in rows:
		chunk = chunk_locations.get(citation.chunk_id) if citation.chunk_id is not None else None
		identity_matches = (
			citation.normalized_citation == selected.normalized_citation
			or citation.citation_text == selected.citation_text
		)
		if citation.chunk_id is None:
			location_matches = (
				citation.offset_start == selected.offset_start
				and citation.offset_end == selected.offset_end
			)
		else:
			location_matches = chunk is not None and (
				citation.offset_start is None
				or (
					citation.offset_start == chunk["offset_start"]
					and citation.offset_end == chunk["offset_end"]
				)
			)
		if not identity_matches or not location_matches:
			continue
		target = db.get(Case, citation.target_case_id) if citation.target_case_id is not None else None
		details.append(
			{
				"record_id": citation.id,
				"citation_kind": getattr(citation, "citation_kind", "unknown"),
				"chunk_id": citation.chunk_id,
				"offset_start": citation.offset_start,
				"offset_end": citation.offset_end,
				"citation_text": citation.citation_text,
				"normalized_citation": citation.normalized_citation,
				"provenance": citation.provenance,
				"unresolved": citation.unresolved,
				"target": {
					"case_id": target.id,
					"title": target.title,
					"citation": target.citation,
					"court": target.court,
					"date": target.date,
				}
				if target is not None
				else None,
			}
		)
	return details


def _stored_statute_reference_details(
	db: Session,
	case_id: int,
	selected: Any,
	chunks: list[dict[str, Any]],
) -> list[dict[str, Any]]:
	chunk_locations = {int(chunk["chunk_id"]): chunk for chunk in chunks}
	rows = list(
		db.scalars(
			select(StatuteReference)
			.where(StatuteReference.source_case_id == case_id)
			.order_by(StatuteReference.id)
		)
	)
	details: list[dict[str, Any]] = []
	for reference in rows:
		chunk = chunk_locations.get(reference.chunk_id) if reference.chunk_id is not None else None
		identity_matches = (
			reference.normalized_reference == selected.normalized_citation
			or reference.reference_text == selected.citation_text
		)
		if reference.chunk_id is None:
			location_matches = (
				reference.offset_start == selected.offset_start
				and reference.offset_end == selected.offset_end
			)
		else:
			location_matches = chunk is not None and (
				reference.offset_start is None
				or (
					reference.offset_start == chunk["offset_start"]
					and reference.offset_end == chunk["offset_end"]
				)
			)
		if identity_matches and location_matches:
			details.append(
				{
					"record_id": reference.id,
					"chunk_id": reference.chunk_id,
					"offset_start": reference.offset_start,
					"offset_end": reference.offset_end,
					"reference_text": reference.reference_text,
					"normalized_reference": reference.normalized_reference,
					"reference_kind": reference.reference_kind,
				}
			)
	return details


def build_case_citation_pass_detail(
	case_id: int,
	layer: str,
	offset_start: int,
	offset_end: int,
	db: Session,
	*,
	get_case_fn: Any | None = None,
	extract_case_fn: Any | None = None,
	extract_statute_fn: Any | None = None,
	stored_case_fn: Any | None = None,
	stored_statute_fn: Any | None = None,
) -> dict[str, Any]:
	get_case = get_case_fn or (lambda cid, session: session.scalar(select(Case).where(Case.id == cid)))
	case = get_case(case_id, db)
	if case is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
	full_text = case.full_text or case.summary or ""
	if layer not in {"case", "law", "metadata"}:
		raise HTTPException(
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unsupported citation layer"
		)
	if offset_start < 0 or offset_end <= offset_start or offset_end > len(full_text):
		raise HTTPException(
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid citation offsets"
		)

	extract_case = extract_case_fn or extract_case_citation_matches
	extract_statute = extract_statute_fn or extract_statute_reference_matches
	stored_case = stored_case_fn or _stored_case_citation_details
	stored_statute = stored_statute_fn or _stored_statute_reference_details

	if layer == "case":
		matches = extract_case(full_text)
	elif layer == "law":
		matches = extract_statute(full_text)
	else:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Metadata layer not supported in this endpoint",
		)
	selected = next(
		(
			match
			for match in matches
			if match.offset_start == offset_start and match.offset_end == offset_end
		),
		None,
	)
	if selected is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND, detail="Extracted reference not found"
		)

	line_start = full_text.rfind("\n", 0, offset_start) + 1
	line_end = full_text.find("\n", offset_end)
	if line_end < 0:
		line_end = len(full_text)
	line_text = full_text[line_start:line_end]
	paragraph_match = re.match(r"\s*\[(\d+)\]", line_text)
	chunks = _citation_pass_chunks(db, case_id, full_text, offset_start, offset_end)
	stored_records: list[dict[str, Any]] = []
	if layer == "case":
		stored_records = stored_case(db, case_id, selected, chunks)
	elif layer == "law":
		stored_records = stored_statute(db, case_id, selected, chunks)
	primary_paragraph_chunk = next(
		(chunk for chunk in chunks if chunk.get("is_paragraph_chunk")), None
	)

	citation_text = selected.citation_text
	normalized = selected.normalized_citation
	kind = selected.kind
	return {
		"layer": layer,
		"kind": kind,
		"citation_text": citation_text,
		"normalized_value": normalized,
		"offset_start": offset_start,
		"offset_end": offset_end,
		"span_length": offset_end - offset_start,
		"location": {
			"line_number": full_text.count("\n", 0, offset_start) + 1,
			"column_number": offset_start - line_start + 1,
			"paragraph_number": int(paragraph_match.group(1)) if paragraph_match else None,
			"document_length": len(full_text),
			"position_percent": round((offset_start / len(full_text)) * 100, 2)
			if full_text
			else 0.0,
		},
		"passage": {
			"text": line_text,
			"offset_start": line_start,
			"offset_end": line_end,
		},
		"chunks": chunks,
		"primary_paragraph_chunk": primary_paragraph_chunk,
		"stored_records": stored_records,
	}
