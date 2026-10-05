from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO
import logging
import re
from typing import Any

from docx import Document
from sqlalchemy import func, or_, select, text, tuple_
from sqlalchemy.orm import Session

from .citations import (
	extract_case_citation_matches,
	extract_statute_reference_matches,
	parse_legislation_citation,
	resolve_legislation_reference,
)
from .database import Case
from . import resource_limits

logger = logging.getLogger(__name__)

MAX_DOCX_BYTES = resource_limits.MAX_UPLOAD_BYTES
LIVE_ANALYSIS_CONTENT_TYPES = {
	"application/pdf",
	"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
	"application/octet-stream",
}


@dataclass(frozen=True)
class LiveParagraph:
	index: int
	text: str
	offset_start: int
	offset_end: int
	page_number: int | None = None


def _paragraphs_from_docx(content: bytes) -> tuple[str, list[LiveParagraph]]:
	resource_limits.validate_docx_archive(content)
	document = Document(BytesIO(content))
	paragraphs: list[LiveParagraph] = []
	parts: list[str] = []
	offset = 0
	for index, paragraph in enumerate(document.paragraphs):
		text = paragraph.text
		resource_limits.validate_extracted_text_length(offset + len(text))
		start = offset
		end = start + len(text)
		paragraphs.append(LiveParagraph(index, text, start, end))
		parts.append(text)
		offset = end + 2
	return "\n\n".join(parts), paragraphs


def _paragraphs_from_pdf(content: bytes) -> tuple[str, list[LiveParagraph]]:
	page_texts = resource_limits.extract_pdf_pages(content)
	paragraphs: list[LiveParagraph] = []
	parts: list[str] = []
	offset = 0
	for index, text in enumerate(page_texts):
		start = offset
		end = start + len(text)
		paragraphs.append(LiveParagraph(index, text, start, end, page_number=index + 1))
		parts.append(text)
		offset = end + 2
	return "\n\n".join(parts), paragraphs


def _context(text: str, start: int, end: int, radius: int = 120) -> str:
	return text[max(0, start - radius) : min(len(text), end + radius)].replace("\n", " ").strip()


def _paragraph_for_offset(paragraphs: list[LiveParagraph], offset: int) -> LiveParagraph | None:
	for paragraph in paragraphs:
		if paragraph.offset_start <= offset <= paragraph.offset_end:
			return paragraph
	return None


def validate_live_analysis_upload(filename: str | None, content_type: str | None, content: bytes) -> None:
	if not filename or not filename.lower().endswith((".docx", ".pdf")):
		raise ValueError("Only .docx and text-based .pdf files are supported")
	if content_type and content_type.lower() not in LIVE_ANALYSIS_CONTENT_TYPES:
		raise ValueError("The uploaded file must be a DOCX or PDF document")
	if not content:
		raise ValueError("The uploaded file is empty")
	if len(content) > resource_limits.MAX_UPLOAD_BYTES:
		raise resource_limits.ResourceLimitError(resource_limits.upload_limit_message())


def validate_docx_upload(filename: str | None, content_type: str | None, content: bytes) -> None:
	if not filename or not filename.lower().endswith(".docx"):
		raise ValueError("Only .docx files are supported")
	if content_type and content_type.lower() not in {
		"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
		"application/octet-stream",
	}:
		raise ValueError("The uploaded file must be a DOCX document")
	validate_live_analysis_upload(filename, content_type, content)


def _row(
	text: str,
	paragraphs: list[LiveParagraph],
	match: Any,
	*,
	resolved_case: Case | None = None,
	legislation_resolution: Any | None = None,
) -> dict[str, Any]:
	paragraph = _paragraph_for_offset(paragraphs, match.offset_start)
	parsed = parse_legislation_citation(match.normalized_citation or match.citation_text)
	document = legislation_resolution.document if legislation_resolution is not None else None
	section = legislation_resolution.section if legislation_resolution is not None else None
	section_number = None
	provision_text = None
	resolution_status = legislation_resolution.resolution_status if legislation_resolution is not None else "unresolved"
	if section is not None:
		section_number = section.section_number
		pinpoint = legislation_resolution.pinpoint if legislation_resolution is not None else (parsed.pinpoint if parsed else "")
		section_match = re.match(r"(\d{1,3}(?:\.\d+)?[A-Za-z]?)(.*)", pinpoint)
		if section_match and section_match.group(2).strip():
			provision_text = _provision_excerpt(section.text, section_match.group(2).strip())
			if provision_text:
				resolution_status = "resolved_provision"
	return {
		"kind": match.kind,
		"reference_text": match.citation_text,
		"normalized_reference": match.normalized_citation,
		"offset_start": match.offset_start,
		"offset_end": match.offset_end,
		"paragraph_index": paragraph.index if paragraph else None,
		"paragraph_text": paragraph.text if paragraph else None,
		"page_number": paragraph.page_number if paragraph else None,
		"context": _context(text, match.offset_start, match.offset_end),
		"resolved_case_id": resolved_case.id if resolved_case else None,
		"resolved_case_title": resolved_case.title if resolved_case else None,
		"resolved_case_citation": resolved_case.citation if resolved_case else None,
		"instrument_key": legislation_resolution.instrument_key if legislation_resolution is not None else (parsed.instrument_key if parsed else None),
		"pinpoint": legislation_resolution.pinpoint if legislation_resolution is not None else (parsed.pinpoint if parsed else None),
		"legislation_url": (parsed.legislation_url if parsed else None) or (document.source_url if document else None),
		"authority_document_title": document.title if document else None,
		"authority_document_url": document.source_url if document else None,
		"authority_section_number": section.section_number if section else None,
		"authority_section_text": section.text if section else None,
		"source_title": document.title if document else None,
		"source_text": section.text if section else None,
		"source_url": document.source_url if document else (parsed.legislation_url if parsed else None),
		"resolution_status": resolution_status,
		"section_number": section_number,
		"provision_text": provision_text,
	}


def _provision_excerpt(section_text: str, suffix: str) -> str | None:
	"""Return the containing subsection text from a flattened authority section."""
	labels = re.findall(r"(?<!\w)(\([0-9]+\))", suffix)
	if not labels:
		return None
	label = labels[0]
	start_match = re.search(rf"(?<!\w){re.escape(label)}\s+", section_text)
	if not start_match:
		return None
	remainder = section_text[start_match.end() :]
	next_match = re.search(r"\s+\([0-9]+\)\s+", remainder)
	end = start_match.end() + (next_match.start() if next_match else len(remainder))
	excerpt = section_text[start_match.start() : end].strip()
	excerpt = re.sub(r"\.\s+[A-Z][^.!?]{1,80}$", ".", excerpt)
	return excerpt


def _citation_variants(value: str) -> set[str]:
	normalized = " ".join(value.upper().split())
	variants = {normalized}
	if " FC " in f" {normalized} ":
		variants.add(normalized.replace(" FC ", " FCT "))
	if " FCT " in f" {normalized} ":
		variants.add(normalized.replace(" FCT ", " FC "))
	return variants


_EMBEDDED_IDENTIFIER_RE = re.compile(
	r"\b\d{4}\s+(?:SCC|FCA|FC|FCT|CAF|CF|CSC|ONCA|BCCA|ABCA)\s+\d{1,4}\b|\[\d{4}\]\s+\d+\s+S\.?C\.?R\.?\s+\d+",
	re.IGNORECASE,
)


def _embedded_identifiers(match: Any) -> set[str]:
	"""Neutral or SCR citations written inside a case-name citation, without any pinpoint after them."""
	return {" ".join(found.upper().split()) for found in _EMBEDDED_IDENTIFIER_RE.findall(match.citation_text or "")}


def _case_alias_terms(match: Any) -> set[str]:
	clean = re.split(r"\s*,\s*(?:at\s+)?para", match.citation_text or "", maxsplit=1, flags=re.IGNORECASE)[0]
	clean = " ".join(clean.split())
	parts = re.split(r"\s+(?:v\.?|vs\.?|c\.?|versus)\s+", clean, maxsplit=1, flags=re.IGNORECASE)
	choices = [clean, *parts]
	terms = set()
	for choice in choices:
		term = re.sub(r"[^A-Za-z0-9\s]", " ", choice).strip()
		term = " ".join(term.split()).lower()
		if len(term) >= 3:
			terms.add(term)
	return terms


@dataclass(frozen=True)
class _LibraryCase:
	"""The few columns a citation row needs; the (very large) decision text is never loaded here."""

	id: int
	title: str | None
	citation: str | None
	secondary_citation: str | None


_LOOKUP_TIMEOUT_MS = 10000
_MAX_ALIAS_TERMS = 40


def _identifier_in(value: str | None, identifier: str) -> bool:
	"""``identifier`` appears in ``value`` as a whole citation (so ``2019 SCC 6`` does not match ``2019 SCC 65``)."""
	return bool(value) and re.search(rf"(?<!\w){re.escape(identifier)}(?!\w)", " ".join(value.upper().split())) is not None


def _lookup_cases(session: Session, matches: list[Any]) -> dict[str, _LibraryCase]:
	variants = {variant for match in matches if match.kind == "neutral" for variant in _citation_variants(match.normalized_citation)}
	variants |= {variant for match in matches for found in _embedded_identifiers(match) for variant in _citation_variants(found)}
	alias_terms = {term for match in matches if match.kind in {"case", "case_short", "case_name"} for term in _case_alias_terms(match)}
	resolved: dict[str, _LibraryCase] = {}
	columns = (Case.id, Case.title, Case.citation, Case.secondary_citation)
	if variants:
		# The stored citation is not always the bare neutral citation (it may carry the case name or a reporter
		# after it), so match containing it, then confirm the whole citation is there. The trigram index serves this.
		conditions = []
		for variant in sorted(variants):
			pattern = f"%{variant}%"
			conditions.extend([Case.citation.ilike(pattern), Case.secondary_citation.ilike(pattern)])
		for row in session.execute(select(*columns).where(or_(*conditions)).order_by(Case.id).limit(20 * len(variants))):
			case = _LibraryCase(*row)
			for variant in variants:
				if _identifier_in(case.citation, variant) or _identifier_in(case.secondary_citation, variant):
					resolved.setdefault(variant, case)
	# A case name alone is ambiguous ("Baker" is in many titles): accept it only when exactly one decision matches.
	for term in sorted(alias_terms)[:_MAX_ALIAS_TERMS]:
		if term in resolved:
			continue
		rows = session.execute(select(*columns).where(Case.title.ilike(f"%{term}%")).order_by(Case.id).limit(2)).all()
		if len(rows) == 1:
			resolved[term] = _LibraryCase(*rows[0])
	return resolved


def _resolve_local_cases(session: Session, matches: list[Any]) -> tuple[dict[str, _LibraryCase], bool]:
	"""``(resolved, lookup_failed)``. A database error or timeout must not read as "not in the library"."""
	if not any(match.kind in {"neutral", "case", "case_short", "case_name"} for match in matches):
		return {}, False
	try:
		with session.begin_nested():
			if session.get_bind().dialect.name == "postgresql":
				session.execute(text(f"SET LOCAL statement_timeout = {_LOOKUP_TIMEOUT_MS}"))
			return _lookup_cases(session, matches), False
	except Exception:  # noqa: BLE001 - reported per row as a failed lookup, not a missing case
		logger.exception("live analysis library lookup failed")
		return {}, True


def analyze_extracted(text: str, paragraphs: list[LiveParagraph], filename: str, session: Session | None = None) -> dict[str, Any]:
	return _analyze_text(text, paragraphs, filename, session)


def _analyze_text(text: str, paragraphs: list[LiveParagraph], filename: str, session: Session | None = None) -> dict[str, Any]:
	case_matches = extract_case_citation_matches(text)
	statute_matches = extract_statute_reference_matches(text)
	resolved_cases, lookup_failed = _resolve_local_cases(session, case_matches) if session is not None else ({}, False)
	case_rows: list[dict[str, Any]] = []
	for match in case_matches:
		resolved_case = next(
			(resolved_cases.get(variant) for variant in sorted(_citation_variants(match.normalized_citation)) if variant in resolved_cases),
			None,
		)
		if resolved_case is None:
			resolved_case = next(
				(resolved_cases.get(variant) for found in sorted(_embedded_identifiers(match)) for variant in sorted(_citation_variants(found)) if variant in resolved_cases),
				None,
			)
		if resolved_case is None:
			resolved_case = next((resolved_cases.get(term) for term in _case_alias_terms(match) if term in resolved_cases), None)
		row = _row(text, paragraphs, match, resolved_case=resolved_case)
		row["library_status"] = "in_library" if resolved_case else ("lookup_failed" if lookup_failed else ("not_checked" if session is None else "not_found"))
		case_rows.append(row)

	return {
		"filename": filename,
		"text": text,
		"text_length": len(text),
		"paragraph_count": len(paragraphs),
		"case_citations": case_rows,
		"statute_references": [
			_row(
				text,
				paragraphs,
				match,
				legislation_resolution=resolve_legislation_reference(session, match)
				if session is not None
				else None,
			)
			for match in statute_matches
		],
		"summary": {
			"case_citations": len(case_rows),
			"resolved_case_citations": sum(row["resolved_case_id"] is not None for row in case_rows),
			"unresolved_case_citations": sum(row["resolved_case_id"] is None for row in case_rows),
			"library_lookup_failed": lookup_failed,
			"statute_references": len(statute_matches),
		},
	}


def extract_document(content: bytes, filename: str, content_type: str | None = None) -> tuple[str, list[LiveParagraph]]:
	"""Text and paragraphs of an uploaded DOCX or text PDF, held in memory only."""
	validate_live_analysis_upload(filename, content_type, content)
	if filename.lower().endswith(".pdf") or (content_type or "").lower() == "application/pdf":
		return _paragraphs_from_pdf(content)
	return _paragraphs_from_docx(content)


def paragraphs_from_pasted_text(text: str) -> tuple[str, list[LiveParagraph]]:
	"""Pasted text as paragraphs: one per blank-line-separated block (single line breaks stay inside a paragraph)."""
	resource_limits.validate_pasted_text_length(len(text))
	text = text.replace("\r\n", "\n").replace("\r", "\n")
	paragraphs: list[LiveParagraph] = []
	parts: list[str] = []
	offset = 0
	for index, block in enumerate(re.split(r"\n[ \t]*\n", text)):
		start = offset
		end = start + len(block)
		paragraphs.append(LiveParagraph(index, block, start, end))
		parts.append(block)
		offset = end + 2
	return "\n\n".join(parts), paragraphs


def analyze_docx(content: bytes, filename: str, session: Session | None = None) -> dict[str, Any]:
	if len(content) > resource_limits.MAX_UPLOAD_BYTES:
		raise resource_limits.ResourceLimitError(resource_limits.upload_limit_message())
	text, paragraphs = _paragraphs_from_docx(content)
	return _analyze_text(text, paragraphs, filename, session)


def analyze_pdf(content: bytes, filename: str, session: Session | None = None) -> dict[str, Any]:
	if len(content) > resource_limits.MAX_UPLOAD_BYTES:
		raise resource_limits.ResourceLimitError(resource_limits.upload_limit_message())
	text, paragraphs = _paragraphs_from_pdf(content)
	return _analyze_text(text, paragraphs, filename, session)


def analyze_document(
	content: bytes,
	filename: str,
	content_type: str | None = None,
	session: Session | None = None,
) -> dict[str, Any]:
	validate_live_analysis_upload(filename, content_type, content)
	if filename.lower().endswith(".pdf") or (content_type or "").lower() == "application/pdf":
		return analyze_pdf(content, filename, session)
	return analyze_docx(content, filename, session)
