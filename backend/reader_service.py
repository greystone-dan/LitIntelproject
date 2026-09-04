"""Case reader, citation-pass, and metadata formatting service for AI CaseLibrary.

Owns reader payload assembly, metadata extraction formatting,
HTML source sanitization and citation markup wrapping, and citation-pass details.
"""

from __future__ import annotations

import re
from typing import Any

from bs4 import BeautifulSoup, NavigableString
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .citations import (
	RawCitationMatch,
	extract_case_citation_matches,
	extract_raw_citation_matches,
	extract_statute_reference_matches,
	is_self_case_name_match,
	parse_legislation_citation,
)
from .database import (
	Case,
	CaseChunk,
	CaseSource,
	CaseTag,
	Citation,
	CitationMetrics,
	StatuteReference,
)
from .metadata import extract_metadata_observations
from .models import (
	CaseReaderChunkResponse,
	CaseReaderCitationResponse,
	CaseReaderDataResponse,
	CaseReaderMetadataFieldResponse,
	CaseReaderTagResponse,
	CaseResponse,
	CaseSourceResponse,
	CitationMetricsResponse,
)

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


def _build_reader_inferred_tags(case: Case, chunks: list[CaseChunk]) -> list[CaseReaderTagResponse]:
	text_parts: list[str] = []
	if case.full_text:
		text_parts.append(case.full_text)
	if case.summary:
		text_parts.append(case.summary)
	for chunk in chunks:
		if chunk.text:
			text_parts.append(chunk.text)
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
	seen_values: set[str] = set()
	for category, value, pattern in catalog:
		match = re.search(pattern, content, flags=re.IGNORECASE)
		if match is None:
			continue
		key = f"{category}:{value}"
		if key in seen_values:
			continue
		seen_values.add(key)
		evidence = content[max(0, match.start() - 80) : min(len(content), match.end() + 80)].strip()
		tags.append(
			CaseReaderTagResponse(
				category=category,
				value=value,
				score=0.9,
				evidence=evidence,
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


def _format_reader_html(
	source_html: str | None, citations: list[CaseReaderCitationResponse]
) -> str | None:
	if not source_html:
		return None
	soup = BeautifulSoup(source_html, "html.parser")
	for citation in sorted(
		citations,
		key=lambda row: len(row.citation_text or row.normalized_citation or ""),
		reverse=True,
	):
		original_label = (citation.citation_text or citation.normalized_citation or "").strip()
		labels = []
		for value in (original_label, citation.normalized_citation, citation.target_title):
			candidate = (value or "").strip()
			if not candidate:
				continue
			candidate = re.sub(r"\]\s*at\s+paras?\b.*$", "", candidate, flags=re.IGNORECASE).strip(" []")
			candidate = re.sub(r"\s+at\s+paras?\b.*$", "", candidate, flags=re.IGNORECASE).strip()
			if candidate and candidate not in labels:
				labels.append(candidate)
		labels.sort(key=len, reverse=True)
		if not labels:
			continue
		for node in list(soup.find_all(string=lambda value: isinstance(value, NavigableString))):
			if node.parent.name in {"mark", "button"}:
				continue
			label = next((candidate for candidate in labels if candidate in str(node)), "")
			if not label:
				continue
			before, after = str(node).split(label, 1)
			replacement = []
			if before:
				replacement.append(NavigableString(before))
			if citation.target_case_id:
				wrapped = soup.new_tag(
					"button",
					attrs={
						"class": "citation-link",
						"type": "button",
						"data-target-case-id": str(citation.target_case_id),
						"data-target-title": citation.target_title or "Linked case",
						"data-authority": citation.target_chunk_text or citation.target_title or label,
					},
				)
			else:
				statute = citation.citation_kind == "statute" or _is_irpa_irpr_reference(original_label)
				wrapped = soup.new_tag(
					"mark",
					attrs={
						"class": "chunk-statute" if statute else "chunk-citation",
						"data-authority": citation.target_chunk_text or label,
					},
				)
			wrapped.string = label
			replacement.append(wrapped)
			if after:
				replacement.append(NavigableString(after))
			node.replace_with(*replacement)
			break
	return soup.decode_contents()


def build_case_reader_data(case_id: int, db: Session) -> CaseReaderDataResponse:
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
	chunks = list(
		db.scalars(
			select(CaseChunk)
			.where(
				CaseChunk.case_id == case_id,
				CaseChunk.chunk_set.in_(["paragraph", "section", "legacy"]),
			)
			.order_by(CaseChunk.chunk_index)
		)
	)
	if any((chunk.chunk_set or "") == "paragraph" for chunk in chunks):
		chunks = [chunk for chunk in chunks if (chunk.chunk_set or "") == "paragraph"]
	elif chunks:
		if any((chunk.chunk_set or "") == "section" for chunk in chunks):
			chunks = [chunk for chunk in chunks if (chunk.chunk_set or "") == "section"]
		elif any((chunk.chunk_set or "") == "legacy" for chunk in chunks):
			chunks = [chunk for chunk in chunks if (chunk.chunk_set or "") == "legacy"]
	tags = list(
		db.scalars(
			select(CaseTag).where(CaseTag.case_id == case_id).order_by(CaseTag.category, CaseTag.value)
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

	def target_paragraph(citation: Citation) -> int | None:
		match = re.search(
			r"(?:at\s+)?(?:para(?:s|graph(?:s)?)?\.?|paragraph(?:s)?)\s+(\d+)",
			citation.citation_text or citation.normalized_citation or "",
			re.IGNORECASE,
		)
		return int(match.group(1)) if match is not None else None

	target_pinpoints = {
		(target_case_id, paragraph)
		for citation, target_case_id, _, _ in stored_citations
		if target_case_id is not None and (paragraph := target_paragraph(citation)) is not None
	}
	target_chunks: dict[tuple[int, int], str] = {}
	if target_pinpoints:
		target_case_ids = {target_case_id for target_case_id, _ in target_pinpoints}
		for chunk in db.scalars(
			select(CaseChunk).where(
				CaseChunk.case_id.in_(target_case_ids),
				CaseChunk.chunk_set == "paragraph",
				CaseChunk.paragraph_start.is_not(None),
				CaseChunk.paragraph_end.is_not(None),
			)
		):
			chunk_start = chunk.paragraph_start
			chunk_end = chunk.paragraph_end
			if chunk_start is None or chunk_end is None:
				continue
			for target_case_id, paragraph in target_pinpoints:
				if chunk.case_id == target_case_id and chunk_start <= paragraph <= chunk_end:
					target_chunks[(target_case_id, paragraph)] = chunk.text
					break

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

	statute_rows = list(
		db.scalars(
			select(StatuteReference)
			.where(StatuteReference.source_case_id == case_id)
			.order_by(StatuteReference.chunk_id, StatuteReference.offset_start, StatuteReference.id)
		)
	)
	statute_responses = [
		CaseReaderCitationResponse(
			id=-1000000 - reference.id,
			citation_kind=reference.reference_kind,
			chunk_id=reference.chunk_id,
			offset_start=reference.offset_start,
			offset_end=reference.offset_end,
			citation_text=reference.reference_text,
			normalized_citation=reference.normalized_reference,
			instrument_key=reference.instrument_key,
			pinpoint=reference.pinpoint,
			provenance="statute_references",
			legislation_url=reference.legislation_url
			or _legislation_url_for_reference(
				reference.normalized_reference or reference.reference_text
			),
			unresolved=False,
		)
		for reference in statute_rows
	]
	citation_responses.extend(statute_responses)

	selected_chunk_ids = {chunk.id for chunk in chunks if chunk.id is not None}
	if selected_chunk_ids:
		citation_responses = [
			row
			for row in citation_responses
			if row.chunk_id is None or row.chunk_id in selected_chunk_ids
		]

	has_statute_like = any(
		_is_statute_like_label(row.target_citation)
		or _is_statute_like_label(row.normalized_citation)
		or _is_statute_like_label(row.citation_text)
		for row in citation_responses
	)

	chunk_ids_with_rows = {
		row.chunk_id for row in citation_responses if row.chunk_id in selected_chunk_ids
	}
	if selected_chunk_ids:
		seen_live: set[tuple[int, int, int, str]] = set()
		for row in citation_responses:
			if row.chunk_id is None or row.offset_start is None or row.offset_end is None:
				continue
			seen_live.add(
				(
					row.chunk_id,
					int(row.offset_start),
					int(row.offset_end),
					str(row.normalized_citation or row.citation_text or "").strip().lower(),
				)
			)

		next_live_id = -1
		process_all_chunks = (not chunk_ids_with_rows) or (not has_statute_like)
		for chunk in chunks:
			if chunk.id is None:
				continue
			if not process_all_chunks and chunk.id in chunk_ids_with_rows:
				pass
			chunk_text = chunk.text or ""
			if not chunk_text.strip():
				continue
			for raw in extract_raw_citation_matches(chunk_text):
				if raw.kind not in {"case", "case_short", "case_name", "neutral"}:
					continue
				if is_self_case_name_match(case.title, raw):
					continue
				normalized_key = str(raw.normalized_citation or raw.citation_text or "").strip().lower()
				key = (chunk.id, raw.offset_start, raw.offset_end, normalized_key)
				if key in seen_live:
					continue
				seen_live.add(key)
				citation_responses.append(
					CaseReaderCitationResponse(
						id=next_live_id,
						citation_kind=raw.kind,
						chunk_id=chunk.id,
						offset_start=raw.offset_start,
						offset_end=raw.offset_end,
						citation_text=raw.citation_text,
						normalized_citation=raw.normalized_citation,
						target_case_id=None,
						target_title=None,
						target_citation=None,
						provenance="reader_live_extract",
						unresolved=True,
					)
				)
				next_live_id -= 1
			for raw in extract_statute_reference_matches(chunk_text):
				normalized_key = str(raw.normalized_citation or raw.citation_text or "").strip().lower()
				key = (chunk.id, raw.offset_start, raw.offset_end, normalized_key)
				if key in seen_live:
					continue
				seen_live.add(key)
				citation_responses.append(
					CaseReaderCitationResponse(
						id=next_live_id,
						citation_kind=raw.kind,
						chunk_id=chunk.id,
						offset_start=raw.offset_start,
						offset_end=raw.offset_end,
						citation_text=raw.citation_text,
						normalized_citation=raw.normalized_citation,
						instrument_key=(
							parsed.instrument_key
							if (parsed := parse_legislation_citation(raw.normalized_citation or raw.citation_text))
							else None
						),
						pinpoint=(parsed.pinpoint if parsed else None),
						provenance="reader_live_statute_extract",
						legislation_url=(
							parsed.legislation_url
							if parsed
							else _legislation_url_for_reference(raw.normalized_citation or raw.citation_text)
						),
						unresolved=False,
					)
				)
				next_live_id -= 1

	metrics = db.scalar(select(CitationMetrics).where(CitationMetrics.case_id == case_id))
	formatted_html = _format_reader_html(case.source_html, citation_responses)

	return CaseReaderDataResponse(
		case=CaseResponse.model_validate(case, from_attributes=True),
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
	)


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
