from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO
import re
from typing import Any

from docx import Document
from pypdf import PdfReader
from sqlalchemy import func, or_, select, tuple_
from sqlalchemy.orm import Session

from .citations import (
	extract_case_citation_matches,
	extract_statute_reference_matches,
	parse_legislation_citation,
)
from .database import Case, LegislationDocument, LegislationSection

MAX_DOCX_BYTES = 10 * 1024 * 1024
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
	document = Document(BytesIO(content))
	paragraphs: list[LiveParagraph] = []
	parts: list[str] = []
	offset = 0
	for index, paragraph in enumerate(document.paragraphs):
		text = paragraph.text
		start = offset
		end = start + len(text)
		paragraphs.append(LiveParagraph(index, text, start, end))
		parts.append(text)
		offset = end + 2
	return "\n\n".join(parts), paragraphs


def _paragraphs_from_pdf(content: bytes) -> tuple[str, list[LiveParagraph]]:
	reader = PdfReader(BytesIO(content))
	paragraphs: list[LiveParagraph] = []
	parts: list[str] = []
	offset = 0
	for index, page in enumerate(reader.pages):
		text = page.extract_text() or ""
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
	if len(content) > MAX_DOCX_BYTES:
		raise ValueError("The uploaded file exceeds the 10 MB limit")


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
	legislation_source: tuple[LegislationDocument, LegislationSection] | None = None,
) -> dict[str, Any]:
	paragraph = _paragraph_for_offset(paragraphs, match.offset_start)
	parsed = parse_legislation_citation(match.normalized_citation or match.citation_text)
	document, section = legislation_source or (None, None)
	section_number = None
	provision_text = None
	resolution_status = "unresolved"
	if document and section:
		section_number = section.section_number
		resolution_status = "resolved_section"
		pinpoint = parsed.pinpoint if parsed else ""
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
		"instrument_key": parsed.instrument_key if parsed else None,
		"pinpoint": parsed.pinpoint if parsed else None,
		"legislation_url": (parsed.legislation_url if parsed else None) or (document.source_url if document else None),
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


def _resolve_local_cases(session: Session, matches: list[Any]) -> dict[str, Case]:
	variants = {variant for match in matches if match.kind == "neutral" for variant in _citation_variants(match.normalized_citation)}
	alias_terms = {term for match in matches if match.kind in {"case", "case_short", "case_name"} for term in _case_alias_terms(match)}
	if not variants and not alias_terms:
		return {}
	normalized_citation = func.upper(func.regexp_replace(func.coalesce(Case.citation, ""), r"\s+", " ", "g"))
	normalized_secondary = func.upper(
		func.regexp_replace(func.coalesce(Case.secondary_citation, ""), r"\s+", " ", "g")
	)
	conditions = [normalized_citation.in_(variants), normalized_secondary.in_(variants)] if variants else []
	for term in alias_terms:
		pattern = f"%{term}%"
		conditions.extend([Case.title.ilike(pattern), Case.citation.ilike(pattern), Case.secondary_citation.ilike(pattern)])
	cases = session.scalars(select(Case).where(or_(*conditions)).order_by(Case.id)).all()
	resolved: dict[str, Case] = {}
	for case in cases:
		for value in (case.citation, case.secondary_citation):
			if value:
				resolved.setdefault(" ".join(value.upper().split()), case)
		if case.title:
			for term in alias_terms:
				if term in case.title.lower():
					resolved.setdefault(term, case)
		for term in alias_terms:
			if any(term in (value or "").lower() for value in (case.citation, case.secondary_citation)):
				resolved.setdefault(term, case)
	return resolved


def _resolve_local_statutes(
	session: Session,
	matches: list[Any],
) -> dict[tuple[str, str], tuple[LegislationDocument, LegislationSection]]:
	requested: set[tuple[str, str]] = set()
	for match in matches:
		parsed = parse_legislation_citation(match.normalized_citation or match.citation_text)
		if not parsed:
			continue
		section_match = re.match(r"(\d{1,3}(?:\.\d+)?[A-Za-z]?)", parsed.pinpoint)
		if section_match:
			requested.add((parsed.instrument_key, section_match.group(1)))
	if not requested:
		return {}
	rows = session.execute(
		select(LegislationDocument, LegislationSection)
		.join(LegislationSection, LegislationSection.document_id == LegislationDocument.id)
		.where(tuple_(LegislationDocument.instrument_key, LegislationSection.section_number).in_(requested))
	).all()
	return {
		(document.instrument_key, section.section_number): (document, section)
		for document, section in rows
	}


def _statute_source_for_match(
	match: Any,
	sources: dict[tuple[str, str], tuple[LegislationDocument, LegislationSection]],
) -> tuple[LegislationDocument, LegislationSection] | None:
	parsed = parse_legislation_citation(match.normalized_citation or match.citation_text)
	if not parsed:
		return None
	section_match = re.match(r"(\d{1,3}(?:\.\d+)?[A-Za-z]?)", parsed.pinpoint)
	if not section_match:
		return None
	return sources.get((parsed.instrument_key, section_match.group(1)))


def _analyze_text(text: str, paragraphs: list[LiveParagraph], filename: str, session: Session | None = None) -> dict[str, Any]:
	case_matches = extract_case_citation_matches(text)
	statute_matches = extract_statute_reference_matches(text)
	resolved_cases = _resolve_local_cases(session, case_matches) if session is not None else {}
	statute_sources = _resolve_local_statutes(session, statute_matches) if session is not None else {}
	case_rows: list[dict[str, Any]] = []
	for match in case_matches:
		resolved_case = next(
			(resolved_cases.get(variant) for variant in sorted(_citation_variants(match.normalized_citation)) if variant in resolved_cases),
			None,
		)
		if resolved_case is None:
			resolved_case = next((resolved_cases.get(term) for term in _case_alias_terms(match) if term in resolved_cases), None)
		case_rows.append(_row(text, paragraphs, match, resolved_case=resolved_case))

	return {
		"filename": filename,
		"text": text,
		"text_length": len(text),
		"paragraph_count": len(paragraphs),
		"case_citations": case_rows,
		"statute_references": [
			_row(text, paragraphs, match, legislation_source=_statute_source_for_match(match, statute_sources))
			for match in statute_matches
		],
		"summary": {
			"case_citations": len(case_rows),
			"resolved_case_citations": sum(row["resolved_case_id"] is not None for row in case_rows),
			"unresolved_case_citations": sum(row["resolved_case_id"] is None for row in case_rows),
			"statute_references": len(statute_matches),
		},
	}


def analyze_docx(content: bytes, filename: str, session: Session | None = None) -> dict[str, Any]:
	if len(content) > MAX_DOCX_BYTES:
		raise ValueError("The uploaded file exceeds the 10 MB limit")
	text, paragraphs = _paragraphs_from_docx(content)
	return _analyze_text(text, paragraphs, filename, session)


def analyze_pdf(content: bytes, filename: str, session: Session | None = None) -> dict[str, Any]:
	if len(content) > MAX_DOCX_BYTES:
		raise ValueError("The uploaded file exceeds the 10 MB limit")
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
