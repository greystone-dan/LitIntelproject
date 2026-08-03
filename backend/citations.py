from __future__ import annotations

import hashlib
import re
from collections import defaultdict
from datetime import date, datetime

from sqlalchemy import delete, func, select
from sqlalchemy.orm import Session

from .database import A2AJCase, A2AJCaseMap, A2AJCitationEdge, Case, CaseChunk, Citation, CitationMetrics

NEUTRAL_CIT_RE = re.compile(r"\b(\d{4})\s+(FC|FCA|SCC|IRB|RPD|RAD|IAD|ID)\s+(\d+)\b")
CASE_CIT_RE = re.compile(r"\b([A-Z][A-Za-z]+ v\. [A-Z][A-Za-z]+),?\s+(\d{4})\s+([A-Z]{2,})\s+(\d+)\b")
STATUTE_CIT_RE = re.compile(r"\b(IRPA|IRPR)\s+s\.\s*\d+(?:\(\d+\))*")


def _normalize_whitespace(value: str) -> str:
	return " ".join(value.split()).strip()


def normalize_neutral_citation(match: re.Match[str]) -> str:
	year, court, number = match.groups()
	return f"{year} {court} {number}".strip()


def normalize_case_citation(match: re.Match[str]) -> str:
	parties, year, reporter, number = match.groups()
	return f"{parties.strip()}, {year} {reporter.strip().upper()} {number}".strip()


def resolve_neutral_to_case_id(session: Session, neutral_citation: str) -> int | None:
	normalized = _normalize_whitespace(neutral_citation).upper()
	case = session.scalar(
		select(Case).where(
			func.upper(func.regexp_replace(func.coalesce(Case.citation, ""), r"\s+", " ", "g"))
			== normalized
		)
	)
	return case.id if case is not None else None


def extract_citations_from_text(
	session: Session,
	source_case_id: int,
	text: str | None,
	chunk_id: int | None = None,
) -> list[Citation]:
	content = text or ""
	if not content.strip():
		return []

	candidates: list[tuple[int, int, Citation]] = []
	for match in NEUTRAL_CIT_RE.finditer(content):
		normalized = normalize_neutral_citation(match)
		target_case_id = resolve_neutral_to_case_id(session, normalized)
		candidates.append(
			(
				match.start(),
				match.end(),
				Citation(
					source_case_id=source_case_id,
					target_case_id=target_case_id,
					citation_text=match.group(0),
					normalized_citation=normalized,
					chunk_id=chunk_id,
					offset_start=match.start(),
					offset_end=match.end(),
					unresolved=target_case_id is None,
				),
			)
		)

	for match in CASE_CIT_RE.finditer(content):
		normalized = normalize_case_citation(match)
		candidates.append(
			(
				match.start(),
				match.end(),
				Citation(
					source_case_id=source_case_id,
					target_case_id=None,
					citation_text=match.group(0),
					normalized_citation=normalized,
					chunk_id=chunk_id,
					offset_start=match.start(),
					offset_end=match.end(),
					unresolved=True,
				),
			)
		)

	for match in STATUTE_CIT_RE.finditer(content):
		normalized = _normalize_whitespace(match.group(0))
		candidates.append(
			(
				match.start(),
				match.end(),
				Citation(
					source_case_id=source_case_id,
					target_case_id=None,
					citation_text=match.group(0),
					normalized_citation=normalized,
					chunk_id=chunk_id,
					offset_start=match.start(),
					offset_end=match.end(),
					unresolved=True,
				),
			)
		)

	selected: list[Citation] = []
	occupied: list[tuple[int, int]] = []
	for start, end, citation in sorted(candidates, key=lambda item: (-(item[1] - item[0]), item[0])):
		if any(not (end <= occupied_start or start >= occupied_end) for occupied_start, occupied_end in occupied):
			continue
		occupied.append((start, end))
		selected.append(citation)

	selected.sort(key=lambda citation: (citation.offset_start or 0, citation.offset_end or 0))

	if selected:
		session.add_all(selected)
	return selected


def rebuild_citations_for_case(session: Session, case: Case, chunks: list[CaseChunk] | None = None) -> int:
	session.execute(delete(Citation).where(Citation.source_case_id == case.id))
	inserted = 0
	if chunks:
		for chunk in chunks:
			inserted += len(extract_citations_from_text(session, case.id, chunk.text, chunk.id))
	else:
		inserted += len(extract_citations_from_text(session, case.id, case.full_text or case.summary, None))
	return inserted


def batch_extract_citations_from_cases(
	session: Session,
	batch_size: int = 500,
	start_after_case_id: int = 0,
) -> int:
	inserted = 0
	last_case_id = start_after_case_id
	while True:
		cases = list(
			session.scalars(
				select(Case)
				.where(Case.id > last_case_id)
				.order_by(Case.id)
				.limit(batch_size)
			)
		)
		if not cases:
			break
		for case in cases:
			inserted += rebuild_citations_for_case(session, case)
		last_case_id = cases[-1].id
		session.commit()
	return inserted


def batch_extract_citations_from_chunks(session: Session, batch_size: int = 1000) -> int:
	inserted = 0
	last_case_id = 0
	while True:
		case_ids = list(
			session.scalars(
				select(CaseChunk.case_id)
				.where(CaseChunk.case_id > last_case_id)
				.distinct()
				.order_by(CaseChunk.case_id)
				.limit(batch_size)
			)
		)
		if not case_ids:
			break
		chunks = list(
			session.scalars(
				select(CaseChunk)
				.where(CaseChunk.case_id.in_(case_ids))
				.order_by(CaseChunk.case_id, CaseChunk.chunk_index)
			)
		)
		cases_by_id = {
			case.id: case
			for case in session.scalars(select(Case).where(Case.id.in_(case_ids)))
		}
		chunks_by_case: dict[int, list[CaseChunk]] = defaultdict(list)
		for chunk in chunks:
			chunks_by_case[chunk.case_id].append(chunk)
		for case_id, chunk_rows in chunks_by_case.items():
			case = cases_by_id.get(case_id)
			if case is None:
				continue
			inserted += rebuild_citations_for_case(session, case, chunk_rows)
		last_case_id = case_ids[-1]
		session.commit()
	return inserted


def compute_citation_metrics(session: Session) -> int:
	resolved_edges = list(
		session.execute(
			select(Citation.source_case_id, Citation.target_case_id).where(Citation.target_case_id.is_not(None))
		)
	)
	out_degree: dict[int, int] = defaultdict(int)
	in_degree: dict[int, int] = defaultdict(int)
	for source_case_id, target_case_id in resolved_edges:
		if source_case_id is None or target_case_id is None:
			continue
		out_degree[int(source_case_id)] += 1
		in_degree[int(target_case_id)] += 1

	updated = 0
	for case_id, in session.execute(select(Case.id)):
		metrics = session.get(CitationMetrics, case_id)
		if metrics is None:
			metrics = CitationMetrics(case_id=case_id)
			session.add(metrics)
		metrics.in_degree = in_degree.get(case_id, 0)
		metrics.out_degree = out_degree.get(case_id, 0)
		updated += 1

	session.commit()
	return updated


def _a2aj_value(record: dict, *names: str):
	for name in names:
		value = record.get(name)
		if value not in (None, ""):
			return value
	return None


def _as_date(value: object) -> date | None:
	if isinstance(value, datetime):
		return value.date()
	if isinstance(value, date):
		return value
	if value:
		return date.fromisoformat(str(value)[:10])
	return None


def _a2aj_case_key(record: dict) -> str:
	neutral = _a2aj_value(record, "neutral_citation", "citation_en", "citation_fr")
	title = _a2aj_value(record, "name_en", "name_fr")
	document_date = _a2aj_value(record, "document_date_en", "document_date_fr")
	raw_id = _a2aj_value(record, "id", "case_id", "a2aj_case_id")
	if raw_id:
		return str(raw_id)
	parts = [str(neutral or ""), str(title or ""), str(document_date or "")]
	return hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()[:24]


def ingest_a2aj_cases_from_rows(session: Session, rows: list[dict]) -> int:
	inserted = 0
	for record in rows:
		a2aj_case_id = _a2aj_case_key(record)
		neutral_citation = _a2aj_value(record, "neutral_citation", "citation_en", "citation_fr")
		court = _a2aj_value(record, "court", "dataset")
		decision_date = _as_date(_a2aj_value(record, "decision_date", "document_date_en", "document_date_fr"))
		cases_cited = _a2aj_value(record, "cases_cited", "cases_cited_en", "cases_cited_fr")
		cases_citing = _a2aj_value(record, "cases_citing", "cases_citing_en", "cases_citing_fr")
		citing_cases_count = _a2aj_value(record, "citing_cases_count")
		existing = session.scalar(select(A2AJCase).where(A2AJCase.a2aj_case_id == a2aj_case_id))
		if existing is None:
			session.add(
				A2AJCase(
					a2aj_case_id=a2aj_case_id,
					neutral_citation=neutral_citation,
					court=court,
					decision_date=decision_date,
					cases_cited=cases_cited,
					cases_citing=cases_citing,
					citing_cases_count=citing_cases_count if isinstance(citing_cases_count, int) else None,
				)
			)
			inserted += 1
		else:
			existing.neutral_citation = neutral_citation
			existing.court = court
			existing.decision_date = decision_date
			existing.cases_cited = cases_cited
			existing.cases_citing = cases_citing
			existing.citing_cases_count = citing_cases_count if isinstance(citing_cases_count, int) else existing.citing_cases_count
	session.commit()
	return inserted


def build_a2aj_case_map(session: Session) -> int:
	inserted = 0
	for a2aj_case in session.scalars(select(A2AJCase).where(A2AJCase.neutral_citation.is_not(None))):
		local_case = session.scalar(select(Case).where(Case.citation == a2aj_case.neutral_citation))
		if local_case is None:
			continue
		mapping = session.get(A2AJCaseMap, a2aj_case.a2aj_case_id)
		if mapping is None:
			session.add(A2AJCaseMap(a2aj_case_id=a2aj_case.a2aj_case_id, local_case_id=local_case.id))
			inserted += 1
		else:
			mapping.local_case_id = local_case.id
	session.commit()
	return inserted


def ingest_a2aj_citation_edges_from_rows(session: Session, rows: list[dict]) -> int:
	inserted = 0
	for record in rows:
		source_a2aj_case_id = _a2aj_case_key(record)
		cases_cited = _a2aj_value(record, "cases_cited", "cases_cited_en", "cases_cited_fr") or []
		if isinstance(cases_cited, str):
			cases_cited = [cases_cited]
		for cited in cases_cited:
			if cited in (None, ""):
				continue
			existing = session.scalar(
				select(A2AJCitationEdge).where(
					A2AJCitationEdge.source_a2aj_case_id == source_a2aj_case_id,
					A2AJCitationEdge.normalized_citation == str(cited),
				)
			)
			if existing is None:
				session.add(
					A2AJCitationEdge(
						source_a2aj_case_id=source_a2aj_case_id,
						target_a2aj_case_id=None,
						normalized_citation=str(cited),
					)
				)
				inserted += 1
	session.commit()
	return inserted


def convert_a2aj_edges_to_local(session: Session, dedupe: bool = True) -> int:
	maps = {mapping.a2aj_case_id: mapping.local_case_id for mapping in session.scalars(select(A2AJCaseMap))}
	inserted = 0
	for edge in session.scalars(select(A2AJCitationEdge)):
		source_local = maps.get(edge.source_a2aj_case_id)
		if source_local is None:
			continue
		target_local = maps.get(edge.target_a2aj_case_id) if edge.target_a2aj_case_id else None
		if target_local is None and edge.normalized_citation:
			target_local = resolve_neutral_to_case_id(session, edge.normalized_citation)
		if target_local is None:
			continue
		if dedupe:
			existing = session.scalar(
				select(Citation).where(
					Citation.source_case_id == source_local,
					Citation.target_case_id == target_local,
					Citation.normalized_citation == edge.normalized_citation,
					Citation.provenance == "a2aj",
				)
			)
			if existing is not None:
				continue
		session.add(
			Citation(
				source_case_id=source_local,
				target_case_id=target_local,
				citation_text=edge.normalized_citation,
				normalized_citation=edge.normalized_citation,
				chunk_id=None,
				offset_start=None,
				offset_end=None,
				unresolved=False,
				provenance="a2aj",
			)
		)
		inserted += 1
	session.commit()
	return inserted


def merge_local_and_a2aj_graph(session: Session) -> dict[str, int]:
	"""Recompute local graph metrics after any A2AJ merge pass."""
	return {
		"citation_metrics_updated": compute_citation_metrics(session),
	}