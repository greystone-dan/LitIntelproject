from __future__ import annotations

import csv
import os
from collections import defaultdict
from functools import lru_cache
from math import ceil
from math import log1p
from pathlib import Path
from typing import Any

from sqlalchemy import case as sql_case, false, func, or_, select, union
from sqlalchemy.orm import Session, aliased

from .database import Case, CaseChunk, CaseTag, Citation, CitationMetrics, StatuteReference


_STANDARD_TEST_PHRASES = (
	"standard of review",
	"procedural fairness",
	"reasonableness",
	"palpable and overriding error",
	"natural justice",
	"duty of fairness",
	"test for",
	"framework",
)

_MASTER_300_CASE_MAP_CSV = Path(__file__).resolve().parent.parent / "data" / "eval" / "fc_priority_seed_case_map.csv"


def _focus_master_300_enabled() -> bool:
	value = (os.getenv("CASELIBRARY_FOCUS_MASTER_300") or "false").strip().lower()
	return value in {"1", "true", "yes", "on"}


@lru_cache(maxsize=1)
def _focused_case_ids() -> tuple[int, ...]:
	if not _focus_master_300_enabled():
		return tuple()
	if not _MASTER_300_CASE_MAP_CSV.exists():
		return tuple()
	ids: list[int] = []
	seen: set[int] = set()
	with _MASTER_300_CASE_MAP_CSV.open("r", encoding="utf-8-sig", newline="") as file_obj:
		reader = csv.DictReader(file_obj)
		for row in reader:
			if str(row.get("status") or "") != "matched":
				continue
			raw = str(row.get("local_case_id") or "").strip()
			if not raw.isdigit():
				continue
			case_id = int(raw)
			if case_id in seen:
				continue
			seen.add(case_id)
			ids.append(case_id)
	return tuple(ids)


def _aggregated_edges():
	focus_ids = _focused_case_ids()
	statement = select(
		Citation.source_case_id.label("source_case_id"),
		Citation.target_case_id.label("target_case_id"),
		func.count(Citation.id).label("occurrence_count"),
	).where(Citation.target_case_id.is_not(None))
	if _focus_master_300_enabled():
		if not focus_ids:
			statement = statement.where(false())
		else:
			statement = statement.where(
				Citation.source_case_id.in_(focus_ids),
				Citation.target_case_id.in_(focus_ids),
			)
	return statement.group_by(Citation.source_case_id, Citation.target_case_id).cte("aggregated_citation_edges")


def _case_node(case: Case, metrics: CitationMetrics | None = None) -> dict[str, Any]:
	return {
		"case_id": case.id,
		"title": case.title,
		"citation": case.citation,
		"court": case.court,
		"date": case.date,
		"in_degree": int(metrics.in_degree or 0) if metrics else 0,
		"out_degree": int(metrics.out_degree or 0) if metrics else 0,
		"pagerank": metrics.pagerank if metrics else None,
	}


def citation_map_summary(session: Session) -> dict[str, int]:
	edges = _aggregated_edges()
	focus_ids = _focused_case_ids()
	connected = union(
		select(edges.c.source_case_id.label("case_id")),
		select(edges.c.target_case_id.label("case_id")),
	).subquery()
	case_count_statement = select(func.count(Case.id))
	resolved_statement = select(func.count(Citation.id)).where(Citation.target_case_id.is_not(None))
	unresolved_statement = select(func.count(Citation.id)).where(Citation.target_case_id.is_(None))
	metrics_statement = select(func.count(CitationMetrics.case_id))
	if _focus_master_300_enabled():
		if not focus_ids:
			case_count_statement = case_count_statement.where(false())
			resolved_statement = resolved_statement.where(false())
			unresolved_statement = unresolved_statement.where(false())
			metrics_statement = metrics_statement.where(false())
		else:
			case_count_statement = case_count_statement.where(Case.id.in_(focus_ids))
			resolved_statement = resolved_statement.where(
				Citation.source_case_id.in_(focus_ids),
				Citation.target_case_id.in_(focus_ids),
			)
			unresolved_statement = unresolved_statement.where(Citation.source_case_id.in_(focus_ids))
			metrics_statement = metrics_statement.where(CitationMetrics.case_id.in_(focus_ids))
	return {
		"total_cases": int(session.scalar(case_count_statement) or 0),
		"resolved_occurrences": int(session.scalar(resolved_statement) or 0),
		"unresolved_occurrences": int(session.scalar(unresolved_statement) or 0),
		"aggregated_edges": int(session.scalar(select(func.count()).select_from(edges)) or 0),
		"connected_cases": int(session.scalar(select(func.count()).select_from(connected)) or 0),
		"metrics_cases": int(session.scalar(metrics_statement) or 0),
	}


def top_authorities(session: Session, limit: int = 50) -> list[dict[str, Any]]:
	edges = _aggregated_edges()
	rows = session.execute(
		select(
			Case,
			CitationMetrics,
			func.count(edges.c.source_case_id).label("citing_cases"),
			func.sum(edges.c.occurrence_count).label("citation_occurrences"),
		)
		.join(edges, edges.c.target_case_id == Case.id)
		.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
		.group_by(Case.id, CitationMetrics.case_id)
		.order_by(func.count(edges.c.source_case_id).desc(), func.sum(edges.c.occurrence_count).desc(), Case.id)
		.limit(limit)
	)
	return [
		{
			**_case_node(case, metrics),
			"citing_cases": int(citing_cases),
			"citation_occurrences": int(citation_occurrences),
		}
		for case, metrics, citing_cases, citation_occurrences in rows
	]


def search_citation_cases(session: Session, query: str, limit: int = 12) -> list[dict[str, Any]]:
	term = query.strip()
	if not term:
		return []
	pattern = f"%{term}%"
	focus_ids = _focused_case_ids()
	statement = select(Case, CitationMetrics).outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
	if _focus_master_300_enabled():
		if not focus_ids:
			return []
		statement = statement.where(Case.id.in_(focus_ids))
	rows = session.execute(
		statement.where(or_(Case.citation.ilike(pattern), Case.title.ilike(pattern)))
		.order_by(
			(Case.citation == term).desc(),
			Case.date.desc(),
			Case.id.desc(),
		)
		.limit(limit)
	)
	return [_case_node(case, metrics) for case, metrics in rows]


def case_authority_map(session: Session, case: Case, limit: int = 5) -> dict[str, Any]:
	edges = _aggregated_edges()
	authority_frequency = (
		select(
			edges.c.target_case_id,
			func.count(edges.c.source_case_id).label("citing_cases"),
		)
		.group_by(edges.c.target_case_id)
		.cte("authority_map_frequency")
	)
	rows = list(
		session.execute(
			select(
				Case,
				CitationMetrics,
				edges.c.occurrence_count,
				authority_frequency.c.citing_cases,
			)
			.join(edges, edges.c.target_case_id == Case.id)
			.join(authority_frequency, authority_frequency.c.target_case_id == Case.id)
			.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
			.where(edges.c.source_case_id == case.id, edges.c.target_case_id != case.id)
			.order_by(
				authority_frequency.c.citing_cases.desc(),
				edges.c.occurrence_count.desc(),
				Case.id,
			)
			.limit(limit)
		)
	)
	focus_metrics = session.get(CitationMetrics, case.id)
	nodes = [_case_node(case, focus_metrics)]
	map_edges = []
	for authority, metrics, occurrence_count, citing_cases in rows:
		node = _case_node(authority, metrics)
		node["in_degree"] = int(citing_cases)
		nodes.append(node)
		map_edges.append(
			{
				"source_case_id": case.id,
				"target_case_id": authority.id,
				"occurrence_count": int(occurrence_count),
			}
		)
	return {
		"focus": nodes[0],
		"nodes": nodes,
		"edges": map_edges,
	}


def common_citing_cases(
	session: Session,
	authority_ids: list[int],
	limit: int = 50,
) -> list[dict[str, Any]]:
	unique_ids = list(dict.fromkeys(authority_ids))
	if len(unique_ids) < 2 or len(unique_ids) > 3:
		raise ValueError("Select two or three distinct cases")
	edges = _aggregated_edges()
	rows = session.execute(
		select(
			Case,
			CitationMetrics,
			func.count(edges.c.target_case_id).label("matched_authority_count"),
			func.sum(edges.c.occurrence_count).label("citation_occurrences"),
		)
		.join(edges, edges.c.source_case_id == Case.id)
		.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
		.where(edges.c.target_case_id.in_(unique_ids))
		.group_by(Case.id, CitationMetrics.case_id)
		.having(func.count(edges.c.target_case_id) == len(unique_ids))
		.order_by(func.sum(edges.c.occurrence_count).desc(), Case.date.desc(), Case.id)
		.limit(limit)
	)
	return [
		{
			"case": _case_node(case, metrics),
			"matched_authority_count": int(matched_count),
			"citation_occurrences": int(occurrences),
		}
		for case, metrics, matched_count, occurrences in rows
	]


def _citation_context(text: str, start: int, end: int, radius: int = 500) -> tuple[str, int, int]:
	window_start = max(0, start - radius)
	window_end = min(len(text), end + radius)
	line_start = text.rfind("\n", window_start, start)
	line_end = text.find("\n", end, window_end)
	context_start = line_start + 1 if line_start >= window_start else window_start
	context_end = line_end if line_end >= 0 else window_end
	return text[context_start:context_end].strip(), context_start, context_end


def citation_contexts(
	session: Session,
	source_case_id: int,
	target_case_id: int,
	limit: int = 50,
) -> list[dict[str, Any]]:
	target_case = aliased(Case, name="target_case")
	rows = session.execute(
		select(Citation, CaseChunk, Case, target_case)
		.join(CaseChunk, CaseChunk.id == Citation.chunk_id)
		.join(Case, Case.id == Citation.source_case_id)
		.join(target_case, target_case.id == Citation.target_case_id)
		.where(
			Citation.source_case_id == source_case_id,
			Citation.target_case_id == target_case_id,
			Citation.offset_start.is_not(None),
			Citation.offset_end.is_not(None),
		)
		.order_by(CaseChunk.chunk_index, Citation.offset_start, Citation.id)
		.limit(limit)
	)
	contexts: list[dict[str, Any]] = []
	seen: set[tuple[str, str]] = set()
	for citation, chunk, source_case, target_row in rows:
		start = int(citation.offset_start or 0)
		end = int(citation.offset_end or start)
		context, context_start, context_end = _citation_context(chunk.text, start, end)
		key = (citation.normalized_citation or "", " ".join(context.split()))
		if key in seen:
			continue
		seen.add(key)
		contexts.append(
			{
				"citation_id": citation.id,
				"source_case_id": source_case.id,
				"source_title": source_case.title,
				"source_citation": source_case.citation,
				"target_case_id": target_row.id,
				"target_title": target_row.title,
				"target_citation": target_row.citation,
				"chunk_id": chunk.id,
				"chunk_index": chunk.chunk_index,
				"citation_text": citation.citation_text,
				"normalized_citation": citation.normalized_citation,
				"offset_start": start,
				"offset_end": end,
				"context_start": context_start,
				"context_end": context_end,
				"context": context,
			}
		)
	return contexts


def case_legal_tags(session: Session, case_id: int, limit: int = 100) -> list[dict[str, Any]]:
	priority = {"statute": 0, "issue": 1, "legal_area": 2, "outcome": 3}
	rows = session.scalars(
		select(CaseTag)
		.where(
			CaseTag.case_id == case_id,
			CaseTag.category.in_(priority),
		)
		.order_by(CaseTag.score.desc(), CaseTag.category, CaseTag.value)
		.limit(limit)
	)
	return [
		{
			"category": tag.category,
			"value": tag.value,
			"score": tag.score,
			"evidence": tag.evidence,
			"source": tag.source,
			"taxonomy_version": tag.taxonomy_version,
		}
		for tag in sorted(rows, key=lambda tag: (priority.get(tag.category, 9), -tag.score, tag.value))
	]


def citation_map_topics(
	session: Session,
	query: str = "",
	limit: int = 100,
) -> list[dict[str, Any]]:
	term = query.strip()
	focus_ids = _focused_case_ids()
	statement = (
		select(
			CaseTag.category,
			CaseTag.value,
			func.count(func.distinct(CaseTag.case_id)).label("case_count"),
		)
		.where(CaseTag.category.in_(("issue", "statute", "legal_area")))
		.group_by(CaseTag.category, CaseTag.value)
	)
	if _focus_master_300_enabled():
		if not focus_ids:
			return []
		statement = statement.where(CaseTag.case_id.in_(focus_ids))
	if term:
		statement = statement.where(CaseTag.value.ilike(f"%{term}%"))
	rows = session.execute(
		statement.order_by(func.count(func.distinct(CaseTag.case_id)).desc(), CaseTag.category, CaseTag.value).limit(limit)
	)
	return [
		{
			"category": category,
			"value": value,
			"case_count": int(case_count),
		}
		for category, value, case_count in rows
	]


def citation_issue_map(
	session: Session,
	category: str,
	value: str,
	limit: int = 50,
) -> dict[str, Any]:
	edges = _aggregated_edges()
	focus_ids = _focused_case_ids()
	influence = (
		select(
			edges.c.target_case_id.label("case_id"),
			func.count(edges.c.source_case_id).label("in_degree"),
		)
		.group_by(edges.c.target_case_id)
		.cte("issue_map_influence")
	)
	outgoing = (
		select(
			edges.c.source_case_id.label("case_id"),
			func.count(edges.c.target_case_id).label("out_degree"),
		)
		.group_by(edges.c.source_case_id)
		.cte("issue_map_outgoing")
	)
	case_rows = list(
		session.execute(
			select(
				Case,
				func.coalesce(influence.c.in_degree, 0),
				func.coalesce(outgoing.c.out_degree, 0),
			)
			.join(CaseTag, CaseTag.case_id == Case.id)
			.outerjoin(influence, influence.c.case_id == Case.id)
			.outerjoin(outgoing, outgoing.c.case_id == Case.id)
			.where(CaseTag.category == category, CaseTag.value == value)
			.order_by(func.coalesce(influence.c.in_degree, 0).desc(), Case.date.desc(), Case.id)
			.limit(limit)
		)
	)
	if _focus_master_300_enabled():
		if not focus_ids:
			case_rows = []
		else:
			case_rows = [row for row in case_rows if row[0].id in focus_ids]
	case_ids = [case.id for case, _, _ in case_rows]
	issue_edges = list(
		session.execute(
			select(edges.c.source_case_id, edges.c.target_case_id, edges.c.occurrence_count)
			.where(edges.c.source_case_id.in_(case_ids), edges.c.target_case_id.in_(case_ids))
			.order_by(edges.c.occurrence_count.desc(), edges.c.source_case_id, edges.c.target_case_id)
		)
	) if case_ids else []
	nodes = []
	for case, in_degree, out_degree in case_rows:
		node = _case_node(case)
		node["in_degree"] = int(in_degree)
		node["out_degree"] = int(out_degree)
		nodes.append(node)
	available_statement = select(func.count(func.distinct(CaseTag.case_id))).where(
		CaseTag.category == category,
		CaseTag.value == value,
	)
	if _focus_master_300_enabled():
		if not focus_ids:
			available_statement = available_statement.where(false())
		else:
			available_statement = available_statement.where(CaseTag.case_id.in_(focus_ids))

	return {
		"category": category,
		"value": value,
		"available_cases": int(session.scalar(available_statement) or 0),
		"nodes": nodes,
		"edges": [
			{
				"source_case_id": int(source_case_id),
				"target_case_id": int(target_case_id),
				"occurrence_count": int(occurrence_count),
			}
			for source_case_id, target_case_id, occurrence_count in issue_edges
		],
	}


def citation_neighborhood(session: Session, case: Case, limit: int = 100) -> dict[str, Any]:
	edges = _aggregated_edges()
	incident_edges = list(
		session.execute(
			select(edges.c.source_case_id, edges.c.target_case_id, edges.c.occurrence_count)
			.where((edges.c.source_case_id == case.id) | (edges.c.target_case_id == case.id))
			.order_by(edges.c.occurrence_count.desc())
			.limit(limit)
		)
	)
	node_ids = {
		int(node_id)
		for source_case_id, target_case_id, _ in incident_edges
		for node_id in (source_case_id, target_case_id)
	}
	case_rows = session.execute(
		select(Case, CitationMetrics)
		.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
		.where(Case.id.in_(node_ids))
	)
	nodes_by_id = {row.id: _case_node(row, metrics) for row, metrics in case_rows}
	focus = nodes_by_id.get(case.id, _case_node(case))
	return {
		"focus": focus,
		"nodes": list(nodes_by_id.values()),
		"edges": [
			{
				"source_case_id": int(source_case_id),
				"target_case_id": int(target_case_id),
				"occurrence_count": int(occurrence_count),
			}
			for source_case_id, target_case_id, occurrence_count in incident_edges
		],
	}


def similar_cases_by_authority(
	session: Session,
	case_id: int,
	limit: int = 20,
	min_shared: int = 2,
) -> list[dict[str, Any]]:
	edges = _aggregated_edges()
	base_authorities = (
		select(edges.c.target_case_id)
		.where(edges.c.source_case_id == case_id)
		.cte("base_authorities")
	)
	authority_frequency = (
		select(
			edges.c.target_case_id,
			func.count(edges.c.source_case_id).label("citing_cases"),
		)
		.group_by(edges.c.target_case_id)
		.cte("authority_frequency")
	)
	candidates = (
		select(
			edges.c.source_case_id.label("case_id"),
			func.count(edges.c.target_case_id).label("shared_authority_count"),
			func.sum(1.0 / authority_frequency.c.citing_cases).label("rarity_weighted_score"),
		)
		.join(base_authorities, base_authorities.c.target_case_id == edges.c.target_case_id)
		.join(authority_frequency, authority_frequency.c.target_case_id == edges.c.target_case_id)
		.where(edges.c.source_case_id != case_id)
		.group_by(edges.c.source_case_id)
		.having(func.count(edges.c.target_case_id) >= min_shared)
		.order_by(func.sum(1.0 / authority_frequency.c.citing_cases).desc(), func.count(edges.c.target_case_id).desc())
		.limit(limit)
		.cte("similar_cases")
	)
	candidate_rows = list(
		session.execute(
			select(Case, CitationMetrics, candidates.c.shared_authority_count, candidates.c.rarity_weighted_score)
			.join(candidates, candidates.c.case_id == Case.id)
			.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
			.order_by(candidates.c.rarity_weighted_score.desc(), candidates.c.shared_authority_count.desc())
		)
	)
	if not candidate_rows:
		return []

	candidate_ids = [row.id for row, _, _, _ in candidate_rows]
	shared_rows = session.execute(
		select(
			edges.c.source_case_id,
			Case,
			authority_frequency.c.citing_cases,
		)
		.join(base_authorities, base_authorities.c.target_case_id == edges.c.target_case_id)
		.join(Case, Case.id == edges.c.target_case_id)
		.join(authority_frequency, authority_frequency.c.target_case_id == edges.c.target_case_id)
		.where(edges.c.source_case_id.in_(candidate_ids))
		.order_by(edges.c.source_case_id, authority_frequency.c.citing_cases, Case.id)
	)
	shared_by_candidate: dict[int, list[dict[str, Any]]] = defaultdict(list)
	for candidate_id, authority, citing_cases in shared_rows:
		shared_by_candidate[int(candidate_id)].append(
			{
				"case_id": authority.id,
				"title": authority.title,
				"citation": authority.citation,
				"citing_cases": int(citing_cases),
			}
		)

	return [
		{
			"case": _case_node(candidate, metrics),
			"shared_authority_count": int(shared_count),
			"rarity_weighted_score": float(score),
			"shared_authorities": shared_by_candidate[candidate.id],
		}
		for candidate, metrics, shared_count, score in candidate_rows
	]


def co_cited_authorities(session: Session, authority_id: int, limit: int = 30) -> list[dict[str, Any]]:
	edges = _aggregated_edges()
	base_sources = (
		select(edges.c.source_case_id)
		.where(edges.c.target_case_id == authority_id)
		.cte("base_authority_sources")
	)
	rows = session.execute(
		select(
			Case,
			CitationMetrics,
			func.count(edges.c.source_case_id).label("shared_citing_cases"),
			func.sum(edges.c.occurrence_count).label("citation_occurrences"),
		)
		.join(edges, edges.c.target_case_id == Case.id)
		.join(base_sources, base_sources.c.source_case_id == edges.c.source_case_id)
		.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
		.where(Case.id != authority_id)
		.group_by(Case.id, CitationMetrics.case_id)
		.order_by(func.count(edges.c.source_case_id).desc(), func.sum(edges.c.occurrence_count).desc(), Case.id)
		.limit(limit)
	)
	return [
		{
			"authority": _case_node(authority, metrics),
			"shared_citing_cases": int(shared_citing_cases),
			"citation_occurrences": int(citation_occurrences),
		}
		for authority, metrics, shared_citing_cases, citation_occurrences in rows
	]


def citation_authority_signals(
	session: Session,
	case_id: int,
	*,
	limit: int = 20,
	context_limit: int = 3,
) -> list[dict[str, Any]]:
	edges = _aggregated_edges()
	authority_frequency = (
		select(
			edges.c.target_case_id,
			func.count(edges.c.source_case_id).label("citing_cases"),
		)
		.group_by(edges.c.target_case_id)
		.cte("authority_signal_frequency")
	)
	rows = list(
		session.execute(
			select(
				Case,
				CitationMetrics,
				edges.c.occurrence_count,
				authority_frequency.c.citing_cases,
			)
			.join(edges, edges.c.target_case_id == Case.id)
			.join(authority_frequency, authority_frequency.c.target_case_id == Case.id)
			.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
			.where(edges.c.source_case_id == case_id, edges.c.target_case_id != case_id)
			.order_by(edges.c.occurrence_count.desc(), authority_frequency.c.citing_cases, Case.id)
			.limit(limit)
		)
	)
	if not rows:
		return []

	total_occurrences = max(1, sum(int(occurrence_count) for _, _, occurrence_count, _ in rows))
	results: list[dict[str, Any]] = []
	for authority, metrics, occurrence_count, global_citing_cases in rows:
		stats = session.execute(
			select(
				func.count(Citation.id),
				func.count(func.distinct(Citation.chunk_id)),
				func.min(CaseChunk.chunk_index),
				func.max(CaseChunk.chunk_index),
			)
			.outerjoin(CaseChunk, CaseChunk.id == Citation.chunk_id)
			.where(
				Citation.source_case_id == case_id,
				Citation.target_case_id == authority.id,
			)
		).first()
		occurrences = int(stats[0] or 0) if stats else int(occurrence_count)
		distinct_chunks = int(stats[1] or 0) if stats else 0
		first_chunk_index = int(stats[2]) if stats and stats[2] is not None else None
		last_chunk_index = int(stats[3]) if stats and stats[3] is not None else None

		contexts = citation_contexts(session, case_id, authority.id, limit=max(1, context_limit))
		boilerplate_hits = 0
		for context in contexts:
			lowered = context["context"].lower()
			if any(phrase in lowered for phrase in _STANDARD_TEST_PHRASES):
				boilerplate_hits += 1

		global_count = int(global_citing_cases or 0)
		gravity_share = occurrences / total_occurrences
		surprise_score = log1p(occurrences) / (1.0 + log1p(max(1, global_count)))
		originality_score = surprise_score * (distinct_chunks / max(1, occurrences))

		results.append(
			{
				"authority": _case_node(authority, metrics),
				"occurrence_count": occurrences,
				"distinct_chunks": distinct_chunks,
				"gravity_share": gravity_share,
				"global_citing_cases": global_count,
				"surprise_score": float(surprise_score),
				"originality_score": float(originality_score),
				"boilerplate_hits": boilerplate_hits,
				"first_chunk_index": first_chunk_index,
				"last_chunk_index": last_chunk_index,
				"sample_contexts": contexts,
			}
		)

	return sorted(results, key=lambda row: (row["surprise_score"], row["occurrence_count"]), reverse=True)


def citation_paths(
	session: Session,
	source_case_id: int,
	target_case_id: int,
	*,
	max_hops: int = 3,
	limit: int = 5,
	per_node_limit: int = 40,
) -> list[dict[str, Any]]:
	if max_hops < 1:
		return []
	if source_case_id == target_case_id:
		case = session.get(Case, source_case_id)
		metrics = session.get(CitationMetrics, source_case_id)
		if case is None:
			return []
		node = _case_node(case, metrics)
		return [{"path_case_ids": [source_case_id], "hop_count": 0, "total_occurrences": 0, "nodes": [node], "edge_occurrences": []}]

	edges = _aggregated_edges()
	frontier_paths: list[list[int]] = [[source_case_id]]
	found_paths: list[tuple[list[int], list[int]]] = []

	for _depth in range(1, max_hops + 1):
		frontier_nodes = {path[-1] for path in frontier_paths}
		if not frontier_nodes:
			break

		raw_rows = list(
			session.execute(
				select(edges.c.source_case_id, edges.c.target_case_id, edges.c.occurrence_count)
				.where(edges.c.source_case_id.in_(frontier_nodes))
				.order_by(edges.c.source_case_id, edges.c.occurrence_count.desc(), edges.c.target_case_id)
			)
		)
		neighbors: dict[int, list[tuple[int, int]]] = defaultdict(list)
		for src, tgt, occ in raw_rows:
			src_id = int(src)
			if len(neighbors[src_id]) >= per_node_limit:
				continue
			neighbors[src_id].append((int(tgt), int(occ)))

		next_frontier: list[list[int]] = []
		for path in frontier_paths:
			for next_case_id, occurrence_count in neighbors.get(path[-1], []):
				if next_case_id in path:
					continue
				next_path = [*path, next_case_id]
				if next_case_id == target_case_id:
					edge_weights = []
					for index in range(len(next_path) - 1):
						src = next_path[index]
						dst = next_path[index + 1]
						weight = next((occ for candidate, occ in neighbors.get(src, []) if candidate == dst), occurrence_count)
						edge_weights.append(int(weight))
					found_paths.append((next_path, edge_weights))
					if len(found_paths) >= limit:
						break
				else:
					next_frontier.append(next_path)
			if len(found_paths) >= limit:
				break
		if len(found_paths) >= limit:
			break

		frontier_paths = next_frontier[:1500]

	if not found_paths:
		return []

	node_ids = {case_id for path, _ in found_paths for case_id in path}
	rows = session.execute(
		select(Case, CitationMetrics)
		.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
		.where(Case.id.in_(node_ids))
	)
	nodes_by_id = {case.id: _case_node(case, metrics) for case, metrics in rows}

	def sort_key(item: tuple[list[int], list[int]]) -> tuple[int, int]:
		path, weights = item
		return (len(path), -sum(weights))

	result = []
	for path, edge_weights in sorted(found_paths, key=sort_key)[:limit]:
		result.append(
			{
				"path_case_ids": path,
				"hop_count": len(path) - 1,
				"total_occurrences": int(sum(edge_weights)),
				"nodes": [nodes_by_id[case_id] for case_id in path if case_id in nodes_by_id],
				"edge_occurrences": edge_weights,
			}
		)
	return result


def citation_contextual_paths(
	session: Session,
	source_case_id: int,
	target_case_id: int,
	*,
	max_hops: int = 3,
	limit: int = 5,
	per_node_limit: int = 40,
	hop_context_limit: int = 1,
) -> list[dict[str, Any]]:
	paths = citation_paths(
		session,
		source_case_id,
		target_case_id,
		max_hops=max_hops,
		limit=limit,
		per_node_limit=per_node_limit,
	)
	results: list[dict[str, Any]] = []
	for path in paths:
		hops = []
		for index in range(len(path["path_case_ids"]) - 1):
			source_id = int(path["path_case_ids"][index])
			step_target_id = int(path["path_case_ids"][index + 1])
			contexts = citation_contexts(
				session,
				source_id,
				step_target_id,
				limit=max(1, hop_context_limit),
			)
			hops.append(
				{
					"source_case_id": source_id,
					"target_case_id": step_target_id,
					"occurrence_count": int(path["edge_occurrences"][index]),
					"contexts": contexts,
				}
			)
		results.append({**path, "hops": hops})
	return results


def citation_replacement_trend(
	session: Session,
	old_case_id: int,
	new_case_id: int,
	*,
	start_year: int | None = None,
	end_year: int | None = None,
) -> dict[str, Any]:
	edges = _aggregated_edges()
	year_expr = func.extract("year", Case.date)
	statement = (
		select(
			year_expr.label("year"),
			func.sum(sql_case((edges.c.target_case_id == old_case_id, 1), else_=0)).label("old_citing_cases"),
			func.sum(sql_case((edges.c.target_case_id == new_case_id, 1), else_=0)).label("new_citing_cases"),
		)
		.join(edges, edges.c.source_case_id == Case.id)
		.where(edges.c.target_case_id.in_([old_case_id, new_case_id]))
	)
	if start_year is not None:
		statement = statement.where(year_expr >= start_year)
	if end_year is not None:
		statement = statement.where(year_expr <= end_year)
	rows = list(session.execute(statement.group_by(year_expr).order_by(year_expr)))

	series = []
	for year, old_count, new_count in rows:
		y = int(year)
		old_value = int(old_count or 0)
		new_value = int(new_count or 0)
		total = old_value + new_value
		series.append(
			{
				"year": y,
				"old_citing_cases": old_value,
				"new_citing_cases": new_value,
				"new_share": (new_value / total) if total else 0.0,
			}
		)

	if series:
		half = max(1, len(series) // 2)
		early = series[:half]
		late = series[half:]
		if not late:
			late = early
		old_early = sum(item["old_citing_cases"] for item in early) / len(early)
		old_late = sum(item["old_citing_cases"] for item in late) / len(late)
		new_early = sum(item["new_citing_cases"] for item in early) / len(early)
		new_late = sum(item["new_citing_cases"] for item in late) / len(late)
		replacement_score = (new_late - new_early) - (old_late - old_early)
		status = "replacement_likely" if (new_late > old_late and old_early >= new_early and replacement_score > 0) else "no_clear_replacement"
	else:
		replacement_score = 0.0
		status = "insufficient_data"

	old_case = session.get(Case, old_case_id)
	new_case = session.get(Case, new_case_id)
	old_metrics = session.get(CitationMetrics, old_case_id)
	new_metrics = session.get(CitationMetrics, new_case_id)

	return {
		"old_authority": _case_node(old_case, old_metrics) if old_case else None,
		"new_authority": _case_node(new_case, new_metrics) if new_case else None,
		"replacement_score": float(replacement_score),
		"status": status,
		"series": series,
	}


def citation_landmark_candidates(
	session: Session,
	*,
	limit: int = 20,
	recent_years: int = 3,
	baseline_years: int = 5,
	min_recent: int = 20,
) -> list[dict[str, Any]]:
	edges = _aggregated_edges()
	max_year_value = session.scalar(select(func.extract("year", func.max(Case.date))))
	if max_year_value is None:
		return []
	max_year = int(max_year_value)
	recent_start = max_year - recent_years + 1
	baseline_start = recent_start - baseline_years
	baseline_end = recent_start - 1
	year_expr = func.extract("year", Case.date)
	growth_rows = list(
		session.execute(
			select(
				edges.c.target_case_id,
				func.sum(sql_case((year_expr >= recent_start, 1), else_=0)).label("recent_citing_cases"),
				func.sum(
					sql_case(
						((year_expr >= baseline_start) & (year_expr <= baseline_end), 1),
						else_=0,
					)
				).label("baseline_citing_cases"),
			)
			.join(Case, Case.id == edges.c.source_case_id)
			.group_by(edges.c.target_case_id)
			.having(func.sum(sql_case((year_expr >= recent_start, 1), else_=0)) >= min_recent)
		)
	)
	if not growth_rows:
		return []

	case_ids = [int(case_id) for case_id, _, _ in growth_rows]
	case_rows = session.execute(
		select(Case, CitationMetrics)
		.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
		.where(Case.id.in_(case_ids))
	)
	case_by_id = {case.id: _case_node(case, metrics) for case, metrics in case_rows}

	results = []
	for case_id, recent_count, baseline_count in growth_rows:
		recent_value = int(recent_count or 0)
		baseline_value = int(baseline_count or 0)
		baseline_expected_recent = baseline_value * (recent_years / max(1, baseline_years))
		emergence_score = float(recent_value - baseline_expected_recent)
		baseline_per_year = baseline_value / max(1, baseline_years)
		recent_per_year = recent_value / max(1, recent_years)
		lift_ratio = float(recent_per_year / baseline_per_year) if baseline_per_year > 0 else float(recent_per_year)
		results.append(
			{
				"case": case_by_id.get(int(case_id)),
				"recent_citing_cases": recent_value,
				"baseline_citing_cases": baseline_value,
				"emergence_score": emergence_score,
				"lift_ratio": lift_ratio,
				"recent_window": {"start_year": recent_start, "end_year": max_year},
				"baseline_window": {"start_year": baseline_start, "end_year": baseline_end},
			}
		)

	results.sort(key=lambda item: (item["emergence_score"], item["recent_citing_cases"]), reverse=True)
	return [item for item in results if item["case"] is not None][:limit]


def citation_surprise_feed(
	session: Session,
	*,
	category: str | None = None,
	value: str | None = None,
	start_year: int | None = None,
	end_year: int | None = None,
	limit: int = 50,
	min_occurrences: int = 1,
) -> list[dict[str, Any]]:
	edges = _aggregated_edges()
	source_case = aliased(Case, name="surprise_source_case")
	target_case = aliased(Case, name="surprise_target_case")
	date_year = func.extract("year", source_case.date)
	authority_frequency = (
		select(
			edges.c.target_case_id,
			func.count(edges.c.source_case_id).label("global_citing_cases"),
		)
		.group_by(edges.c.target_case_id)
		.cte("surprise_authority_frequency")
	)
	outgoing_totals = (
		select(
			edges.c.source_case_id,
			func.sum(edges.c.occurrence_count).label("source_occurrences"),
		)
		.group_by(edges.c.source_case_id)
		.cte("surprise_source_totals")
	)

	statement = (
		select(
			source_case,
			target_case,
			edges.c.occurrence_count,
			authority_frequency.c.global_citing_cases,
			func.coalesce(outgoing_totals.c.source_occurrences, edges.c.occurrence_count),
		)
		.join(source_case, source_case.id == edges.c.source_case_id)
		.join(target_case, target_case.id == edges.c.target_case_id)
		.join(authority_frequency, authority_frequency.c.target_case_id == edges.c.target_case_id)
		.outerjoin(outgoing_totals, outgoing_totals.c.source_case_id == edges.c.source_case_id)
		.where(edges.c.occurrence_count >= min_occurrences)
	)
	if category and value:
		statement = statement.join(
			CaseTag,
			(CaseTag.case_id == source_case.id) & (CaseTag.category == category) & (CaseTag.value == value),
		)
	if start_year is not None:
		statement = statement.where(date_year >= start_year)
	if end_year is not None:
		statement = statement.where(date_year <= end_year)

	rows = list(
		session.execute(
			statement.order_by(edges.c.occurrence_count.desc(), authority_frequency.c.global_citing_cases, source_case.id).limit(
				max(limit * 5, 200)
			)
		)
	)

	results = []
	for src, tgt, occurrences, global_citing_cases, source_occurrences in rows:
		occ = int(occurrences or 0)
		global_count = int(global_citing_cases or 0)
		source_total = max(1, int(source_occurrences or 0))
		surprise_score = log1p(occ) / (1.0 + log1p(max(1, global_count)))
		gravity_share = occ / source_total
		results.append(
			{
				"source_case": _case_node(src, session.get(CitationMetrics, src.id)),
				"authority": _case_node(tgt, session.get(CitationMetrics, tgt.id)),
				"occurrence_count": occ,
				"global_citing_cases": global_count,
				"gravity_share": gravity_share,
				"surprise_score": float(surprise_score),
			}
		)

	results.sort(key=lambda item: (item["surprise_score"], item["occurrence_count"]), reverse=True)
	return results[:limit]


def citation_doctrine_shifts(
	session: Session,
	*,
	category: str,
	value: str,
	limit: int = 10,
	candidate_limit: int = 12,
	start_year: int | None = None,
	end_year: int | None = None,
) -> list[dict[str, Any]]:
	edges = _aggregated_edges()
	source_case = aliased(Case, name="shift_source_case")
	year_expr = func.extract("year", source_case.date)

	statement = (
		select(
			edges.c.target_case_id,
			year_expr.label("year"),
			func.count(edges.c.source_case_id).label("citing_cases"),
		)
		.join(source_case, source_case.id == edges.c.source_case_id)
		.join(CaseTag, (CaseTag.case_id == source_case.id) & (CaseTag.category == category) & (CaseTag.value == value))
	)
	if start_year is not None:
		statement = statement.where(year_expr >= start_year)
	if end_year is not None:
		statement = statement.where(year_expr <= end_year)

	rows = list(session.execute(statement.group_by(edges.c.target_case_id, year_expr).order_by(year_expr)))
	if not rows:
		return []

	by_authority: dict[int, dict[int, int]] = defaultdict(dict)
	totals: dict[int, int] = defaultdict(int)
	years: set[int] = set()
	for target_case_id, year, citing_cases in rows:
		case_id = int(target_case_id)
		y = int(year)
		count = int(citing_cases or 0)
		by_authority[case_id][y] = count
		totals[case_id] += count
		years.add(y)

	ordered_years = sorted(years)
	if len(ordered_years) < 2:
		return []

	candidate_ids = [case_id for case_id, _ in sorted(totals.items(), key=lambda item: item[1], reverse=True)[:candidate_limit]]
	case_rows = session.execute(
		select(Case, CitationMetrics)
		.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
		.where(Case.id.in_(candidate_ids))
	)
	nodes = {case.id: _case_node(case, metrics) for case, metrics in case_rows}

	half = max(1, len(ordered_years) // 2)
	early_years = ordered_years[:half]
	late_years = ordered_years[half:]
	if not late_years:
		late_years = early_years

	def avg(series: dict[int, int], years_slice: list[int]) -> float:
		return sum(series.get(year, 0) for year in years_slice) / max(1, len(years_slice))

	shifts: list[dict[str, Any]] = []
	for old_id in candidate_ids:
		for new_id in candidate_ids:
			if old_id == new_id:
				continue
			old_node = nodes.get(old_id)
			new_node = nodes.get(new_id)
			if old_node is None or new_node is None:
				continue
			old_series = by_authority.get(old_id, {})
			new_series = by_authority.get(new_id, {})
			old_early = avg(old_series, early_years)
			old_late = avg(old_series, late_years)
			new_early = avg(new_series, early_years)
			new_late = avg(new_series, late_years)
			replacement_score = (new_late - new_early) - (old_late - old_early)
			if new_late <= old_late or old_early < new_early:
				continue
			if replacement_score <= 0:
				continue
			series = []
			for year in ordered_years:
				old_count = int(old_series.get(year, 0))
				new_count = int(new_series.get(year, 0))
				total = old_count + new_count
				series.append(
					{
						"year": year,
						"old_citing_cases": old_count,
						"new_citing_cases": new_count,
						"new_share": (new_count / total) if total else 0.0,
					}
				)
			shifts.append(
				{
					"old_authority": old_node,
					"new_authority": new_node,
					"replacement_score": float(replacement_score),
					"status": "replacement_likely",
					"series": series,
				}
			)

	shifts.sort(key=lambda item: item["replacement_score"], reverse=True)
	return shifts[:limit]


def citation_hidden_bridges(
	session: Session,
	source_case_id: int,
	target_case_id: int,
	*,
	max_hops: int = 4,
	path_limit: int = 20,
	per_node_limit: int = 60,
	bridge_limit: int = 15,
) -> list[dict[str, Any]]:
	paths = citation_paths(
		session,
		source_case_id,
		target_case_id,
		max_hops=max_hops,
		limit=path_limit,
		per_node_limit=per_node_limit,
	)
	if not paths:
		return []

	stats: dict[int, dict[str, float]] = {}
	for path in paths:
		path_case_ids = [int(case_id) for case_id in path["path_case_ids"]]
		edge_occurrences = [int(value) for value in path["edge_occurrences"]]
		hop_count = max(1, len(path_case_ids) - 1)
		for index, bridge_case_id in enumerate(path_case_ids[1:-1], start=1):
			state = stats.setdefault(
				bridge_case_id,
				{
					"path_count": 0.0,
					"weighted_support": 0.0,
					"position_sum": 0.0,
					"hop_sum": 0.0,
				},
			)
			state["path_count"] += 1.0
			left_occ = edge_occurrences[index - 1] if index - 1 < len(edge_occurrences) else 0
			right_occ = edge_occurrences[index] if index < len(edge_occurrences) else left_occ
			state["weighted_support"] += (left_occ + right_occ) / 2.0
			state["position_sum"] += index / hop_count
			state["hop_sum"] += hop_count

	bridge_ids = list(stats.keys())
	rows = session.execute(
		select(Case, CitationMetrics)
		.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
		.where(Case.id.in_(bridge_ids))
	)
	nodes = {case.id: _case_node(case, metrics) for case, metrics in rows}

	results = []
	for bridge_id, state in stats.items():
		path_count = int(state["path_count"])
		if path_count <= 0:
			continue
		node = nodes.get(bridge_id)
		if node is None:
			continue
		results.append(
			{
				"bridge_case": node,
				"path_count": path_count,
				"weighted_support": float(state["weighted_support"]),
				"average_relative_position": float(state["position_sum"] / path_count),
				"average_path_hops": float(state["hop_sum"] / path_count),
			}
		)

	results.sort(key=lambda item: (item["weighted_support"], item["path_count"]), reverse=True)
	return results[:bridge_limit]


def citation_inheritance_chains(
	session: Session,
	authority_case_id: int,
	*,
	max_depth: int = 3,
	limit: int = 20,
	per_node_limit: int = 20,
	min_occurrences: int = 1,
) -> list[dict[str, Any]]:
	if max_depth < 1:
		return []

	edges = _aggregated_edges()
	frontier: list[tuple[list[int], list[int]]] = [([authority_case_id], [])]
	found: list[tuple[list[int], list[int]]] = []

	for _depth in range(1, max_depth + 1):
		frontier_targets = {path[-1] for path, _ in frontier}
		if not frontier_targets:
			break

		raw_rows = list(
			session.execute(
				select(edges.c.target_case_id, edges.c.source_case_id, edges.c.occurrence_count)
				.where(edges.c.target_case_id.in_(frontier_targets), edges.c.occurrence_count >= min_occurrences)
				.order_by(edges.c.target_case_id, edges.c.occurrence_count.desc(), edges.c.source_case_id)
			)
		)
		children: dict[int, list[tuple[int, int]]] = defaultdict(list)
		for tgt, src, occ in raw_rows:
			target_id = int(tgt)
			if len(children[target_id]) >= per_node_limit:
				continue
			children[target_id].append((int(src), int(occ)))

		next_frontier: list[tuple[list[int], list[int]]] = []
		for path, edge_weights in frontier:
			for child_id, occurrence_count in children.get(path[-1], []):
				if child_id in path:
					continue
				next_path = [*path, child_id]
				next_weights = [*edge_weights, occurrence_count]
				found.append((next_path, next_weights))
				next_frontier.append((next_path, next_weights))
				if len(found) >= limit:
					break
			if len(found) >= limit:
				break
		if len(found) >= limit:
			break

		frontier = next_frontier[:1500]

	if not found:
		return []

	node_ids = {case_id for path, _ in found for case_id in path}
	rows = session.execute(
		select(Case, CitationMetrics)
		.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
		.where(Case.id.in_(node_ids))
	)
	nodes_by_id = {case.id: _case_node(case, metrics) for case, metrics in rows}

	def sort_key(item: tuple[list[int], list[int]]) -> tuple[int, int]:
		path, weights = item
		return (sum(weights), len(path))

	results = []
	for path, edge_weights in sorted(found, key=sort_key, reverse=True)[:limit]:
		results.append(
			{
				"chain_case_ids": path,
				"depth": len(path) - 1,
				"total_occurrences": int(sum(edge_weights)),
				"nodes": [nodes_by_id[case_id] for case_id in path if case_id in nodes_by_id],
				"edge_occurrences": edge_weights,
			}
		)
	return results


def citation_missing_authorities(
	session: Session,
	case_id: int,
	*,
	peer_limit: int = 40,
	result_limit: int = 20,
	min_peer_share: float = 0.2,
	min_peer_citations: int = 2,
) -> list[dict[str, Any]]:
	edges = _aggregated_edges()
	peer_rows = similar_cases_by_authority(session, case_id, limit=peer_limit, min_shared=2)
	peer_ids = [int(row["case"]["case_id"]) for row in peer_rows if row.get("case") and row["case"].get("case_id") is not None]
	if not peer_ids:
		return []

	base_authority_ids = {
		int(authority_id)
		for authority_id in session.scalars(select(edges.c.target_case_id).where(edges.c.source_case_id == case_id))
	}

	authority_frequency = (
		select(
			edges.c.target_case_id,
			func.count(edges.c.source_case_id).label("global_citing_cases"),
		)
		.group_by(edges.c.target_case_id)
		.cte("missing_authority_frequency")
	)

	statement = (
		select(
			edges.c.target_case_id,
			func.count(edges.c.source_case_id).label("peer_citing_cases"),
			func.sum(edges.c.occurrence_count).label("peer_occurrences"),
			authority_frequency.c.global_citing_cases,
		)
		.join(authority_frequency, authority_frequency.c.target_case_id == edges.c.target_case_id)
		.where(edges.c.source_case_id.in_(peer_ids))
	)
	if base_authority_ids:
		statement = statement.where(~edges.c.target_case_id.in_(base_authority_ids))
	rows = list(
		session.execute(
			statement.group_by(edges.c.target_case_id, authority_frequency.c.global_citing_cases).order_by(
				func.count(edges.c.source_case_id).desc(),
				func.sum(edges.c.occurrence_count).desc(),
				edges.c.target_case_id,
			)
		)
	)
	if not rows:
		return []

	min_peer_hits = max(min_peer_citations, ceil(len(peer_ids) * max(0.0, min_peer_share)))
	candidate_ids = [int(authority_id) for authority_id, peer_hits, *_rest in rows if int(peer_hits or 0) >= min_peer_hits]
	if not candidate_ids:
		return []

	case_rows = session.execute(
		select(Case, CitationMetrics)
		.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
		.where(Case.id.in_(candidate_ids))
	)
	nodes = {case.id: _case_node(case, metrics) for case, metrics in case_rows}

	results = []
	peer_count = max(1, len(peer_ids))
	for authority_id, peer_hits, peer_occurrences, global_citing in rows:
		authority_case_id = int(authority_id)
		if authority_case_id not in nodes:
			continue
		hits = int(peer_hits or 0)
		if hits < min_peer_hits:
			continue
		occurrences = int(peer_occurrences or 0)
		global_count = int(global_citing or 0)
		coverage = hits / peer_count
		rarity_boost = 1.0 / (1.0 + log1p(max(1, global_count)))
		priority_score = coverage * log1p(max(1, occurrences)) * (1.0 + rarity_boost)
		results.append(
			{
				"authority": nodes[authority_case_id],
				"peer_citing_cases": hits,
				"peer_coverage": float(coverage),
				"peer_occurrences": occurrences,
				"rarity_boost": float(rarity_boost),
				"priority_score": float(priority_score),
			}
		)

	results.sort(key=lambda item: (item["priority_score"], item["peer_citing_cases"]), reverse=True)
	return results[:result_limit]


def citation_authority_lifecycle(
	session: Session,
	*,
	category: str | None = None,
	value: str | None = None,
	start_year: int | None = None,
	end_year: int | None = None,
	limit: int = 25,
	recent_years: int = 3,
	prior_years: int = 3,
) -> list[dict[str, Any]]:
	edges = _aggregated_edges()
	source_case = aliased(Case, name="lifecycle_source_case")
	year_expr = func.extract("year", source_case.date)
	statement = (
		select(
			edges.c.target_case_id,
			year_expr.label("year"),
			func.count(edges.c.source_case_id).label("citing_cases"),
		)
		.join(source_case, source_case.id == edges.c.source_case_id)
	)
	if category and value:
		statement = statement.join(
			CaseTag,
			(CaseTag.case_id == source_case.id) & (CaseTag.category == category) & (CaseTag.value == value),
		)
	if start_year is not None:
		statement = statement.where(year_expr >= start_year)
	if end_year is not None:
		statement = statement.where(year_expr <= end_year)

	rows = list(session.execute(statement.group_by(edges.c.target_case_id, year_expr).order_by(year_expr)))
	if not rows:
		return []

	by_authority: dict[int, dict[int, int]] = defaultdict(dict)
	all_years: set[int] = set()
	for authority_id, year, citing_cases in rows:
		case_id = int(authority_id)
		y = int(year)
		count = int(citing_cases or 0)
		by_authority[case_id][y] = count
		all_years.add(y)

	max_year = max(all_years)
	recent_start = max_year - recent_years + 1
	prior_end = recent_start - 1
	prior_start = prior_end - prior_years + 1

	candidate_ids = list(by_authority.keys())
	case_rows = session.execute(
		select(Case, CitationMetrics)
		.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
		.where(Case.id.in_(candidate_ids))
	)
	nodes = {case.id: _case_node(case, metrics) for case, metrics in case_rows}

	results = []
	for authority_id, series in by_authority.items():
		node = nodes.get(authority_id)
		if node is None:
			continue
		total = int(sum(series.values()))
		recent = int(sum(value_count for year, value_count in series.items() if year >= recent_start))
		prior = int(sum(value_count for year, value_count in series.items() if prior_start <= year <= prior_end))
		older = max(0, total - recent - prior)
		velocity = float(recent - prior)
		decay = float(max(0, prior - recent))

		if recent >= max(10, int(prior * 1.5)) and recent > prior:
			stage = "emerging"
		elif total >= 25 and recent >= max(8, int(prior * 0.9)):
			stage = "dominant"
		elif prior > 0 and recent <= int(prior * 0.6):
			stage = "declining"
		elif older >= (recent + prior) and total >= 20:
			stage = "foundational"
		else:
			stage = "transitional"

		results.append(
			{
				"authority": node,
				"recent_citing_cases": recent,
				"prior_citing_cases": prior,
				"total_citing_cases": total,
				"velocity": velocity,
				"decay": decay,
				"lifecycle_stage": stage,
			}
		)

	results.sort(key=lambda item: (item["recent_citing_cases"], item["total_citing_cases"], item["velocity"]), reverse=True)
	return results[:limit]


def citation_cross_court_flow(
	session: Session,
	*,
	start_year: int | None = None,
	end_year: int | None = None,
	limit: int = 40,
) -> list[dict[str, Any]]:
	edges = _aggregated_edges()
	source_case = aliased(Case, name="court_flow_source_case")
	target_case = aliased(Case, name="court_flow_target_case")
	year_expr = func.extract("year", source_case.date)
	statement = (
		select(
			source_case.court,
			target_case.court,
			func.count(edges.c.source_case_id).label("citing_case_count"),
			func.sum(edges.c.occurrence_count).label("citation_occurrences"),
		)
		.join(source_case, source_case.id == edges.c.source_case_id)
		.join(target_case, target_case.id == edges.c.target_case_id)
	)
	if start_year is not None:
		statement = statement.where(year_expr >= start_year)
	if end_year is not None:
		statement = statement.where(year_expr <= end_year)

	rows = list(
		session.execute(
			statement.group_by(source_case.court, target_case.court)
			.order_by(func.sum(edges.c.occurrence_count).desc(), func.count(edges.c.source_case_id).desc())
			.limit(limit)
		)
	)
	return [
		{
			"source_court": source_court,
			"target_court": target_court,
			"citing_case_count": int(citing_case_count or 0),
			"citation_occurrences": int(citation_occurrences or 0),
		}
		for source_court, target_court, citing_case_count, citation_occurrences in rows
	]


def citation_position_profiles(
	session: Session,
	case_id: int,
	*,
	limit: int = 30,
	min_occurrences: int = 1,
) -> list[dict[str, Any]]:
	max_chunk_index_value = session.scalar(select(func.max(CaseChunk.chunk_index)).where(CaseChunk.case_id == case_id))
	half_threshold = int(max_chunk_index_value // 2) if max_chunk_index_value is not None else 0

	rows = list(
		session.execute(
			select(
				Citation.target_case_id,
				func.count(Citation.id).label("occurrence_count"),
				func.avg(CaseChunk.chunk_index).label("avg_chunk_index"),
				func.min(CaseChunk.chunk_index).label("first_chunk_index"),
				func.max(CaseChunk.chunk_index).label("last_chunk_index"),
				func.sum(sql_case((CaseChunk.chunk_index <= half_threshold, 1), else_=0)).label("first_half_hits"),
				func.sum(sql_case((CaseChunk.chunk_index > half_threshold, 1), else_=0)).label("second_half_hits"),
			)
			.join(CaseChunk, CaseChunk.id == Citation.chunk_id)
			.where(Citation.source_case_id == case_id, Citation.target_case_id.is_not(None))
			.group_by(Citation.target_case_id)
			.having(func.count(Citation.id) >= min_occurrences)
			.order_by(func.count(Citation.id).desc(), func.avg(CaseChunk.chunk_index), Citation.target_case_id)
			.limit(limit)
		)
	)
	if not rows:
		return []

	authority_ids = [int(target_case_id) for target_case_id, *_ in rows]
	case_rows = session.execute(
		select(Case, CitationMetrics)
		.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
		.where(Case.id.in_(authority_ids))
	)
	nodes = {case.id: _case_node(case, metrics) for case, metrics in case_rows}

	results = []
	for target_case_id, occurrence_count, avg_chunk_index, first_chunk_index, last_chunk_index, first_half_hits, second_half_hits in rows:
		authority_id = int(target_case_id)
		node = nodes.get(authority_id)
		if node is None:
			continue
		results.append(
			{
				"authority": node,
				"occurrence_count": int(occurrence_count or 0),
				"avg_chunk_index": float(avg_chunk_index or 0.0),
				"first_chunk_index": int(first_chunk_index) if first_chunk_index is not None else None,
				"last_chunk_index": int(last_chunk_index) if last_chunk_index is not None else None,
				"first_half_hits": int(first_half_hits or 0),
				"second_half_hits": int(second_half_hits or 0),
			}
		)
	return results


def citation_completion_suggestions(
	session: Session,
	case_id: int,
	*,
	peer_limit: int = 40,
	limit: int = 20,
	min_peer_share: float = 0.2,
	min_peer_citations: int = 2,
) -> list[dict[str, Any]]:
	candidates = citation_missing_authorities(
		session,
		case_id,
		peer_limit=peer_limit,
		result_limit=max(limit * 3, limit),
		min_peer_share=min_peer_share,
		min_peer_citations=min_peer_citations,
	)
	if not candidates:
		return []

	results = []
	for row in candidates:
		peer_coverage = float(row.get("peer_coverage") or 0.0)
		rarity_boost = float(row.get("rarity_boost") or 0.0)
		expected_occurrences = int(row.get("peer_occurrences") or 0)
		recommendation_score = peer_coverage * (1.0 + rarity_boost) * log1p(max(1, expected_occurrences))
		results.append(
			{
				"authority": row.get("authority"),
				"peer_citing_cases": int(row.get("peer_citing_cases") or 0),
				"peer_coverage": peer_coverage,
				"rarity_boost": rarity_boost,
				"expected_occurrences": expected_occurrences,
				"recommendation_score": float(recommendation_score),
			}
		)

	results.sort(key=lambda item: (item["recommendation_score"], item["peer_citing_cases"]), reverse=True)
	return results[:limit]


def citation_shift_dashboard(
	session: Session,
	*,
	category: str,
	value: str,
	start_year: int | None = None,
	end_year: int | None = None,
	replacement_limit: int = 8,
	lifecycle_limit: int = 40,
	surprise_limit: int = 25,
) -> dict[str, Any]:
	replacements = citation_doctrine_shifts(
		session,
		category=category,
		value=value,
		limit=replacement_limit,
		candidate_limit=max(10, replacement_limit * 2),
		start_year=start_year,
		end_year=end_year,
	)
	lifecycle = citation_authority_lifecycle(
		session,
		category=category,
		value=value,
		start_year=start_year,
		end_year=end_year,
		limit=lifecycle_limit,
	)
	surprises = citation_surprise_feed(
		session,
		category=category,
		value=value,
		start_year=start_year,
		end_year=end_year,
		limit=surprise_limit,
		min_occurrences=1,
	)

	emerging = [row for row in lifecycle if row.get("lifecycle_stage") == "emerging"][: max(1, replacement_limit)]
	declining = [row for row in lifecycle if row.get("lifecycle_stage") == "declining"][: max(1, replacement_limit)]

	return {
		"category": category,
		"value": value,
		"replacement_candidates": replacements,
		"emerging_authorities": emerging,
		"declining_authorities": declining,
		"surprises": surprises,
	}


def citation_edge_summary(
	session: Session,
	source_case_id: int,
	target_case_id: int,
	*,
	context_limit: int = 3,
	variant_limit: int = 5,
) -> dict[str, Any]:
	source_case = session.get(Case, source_case_id)
	target_case = session.get(Case, target_case_id)
	if source_case is None or target_case is None:
		return {
			"source_case": None,
			"target_case": None,
			"occurrence_count": 0,
			"distinct_chunks": 0,
			"first_chunk_index": None,
			"last_chunk_index": None,
			"top_normalized_citations": [],
			"sample_contexts": [],
		}

	source_metrics = session.get(CitationMetrics, source_case_id)
	target_metrics = session.get(CitationMetrics, target_case_id)

	occurrence_count = int(
		session.scalar(
			select(func.count(Citation.id)).where(
				Citation.source_case_id == source_case_id,
				Citation.target_case_id == target_case_id,
			)
		)
		or 0
	)
	distinct_chunks = int(
		session.scalar(
			select(func.count(func.distinct(Citation.chunk_id))).where(
				Citation.source_case_id == source_case_id,
				Citation.target_case_id == target_case_id,
			)
		)
		or 0
	)
	chunk_bounds = session.execute(
		select(func.min(CaseChunk.chunk_index), func.max(CaseChunk.chunk_index))
		.join(Citation, Citation.chunk_id == CaseChunk.id)
		.where(Citation.source_case_id == source_case_id, Citation.target_case_id == target_case_id)
	).first()
	first_chunk_index = int(chunk_bounds[0]) if chunk_bounds and chunk_bounds[0] is not None else None
	last_chunk_index = int(chunk_bounds[1]) if chunk_bounds and chunk_bounds[1] is not None else None

	variant_rows = session.execute(
		select(Citation.normalized_citation, func.count(Citation.id).label("occurrences"))
		.where(Citation.source_case_id == source_case_id, Citation.target_case_id == target_case_id)
		.group_by(Citation.normalized_citation)
		.order_by(func.count(Citation.id).desc(), Citation.normalized_citation)
		.limit(variant_limit)
	)

	return {
		"source_case": _case_node(source_case, source_metrics),
		"target_case": _case_node(target_case, target_metrics),
		"occurrence_count": occurrence_count,
		"distinct_chunks": distinct_chunks,
		"first_chunk_index": first_chunk_index,
		"last_chunk_index": last_chunk_index,
		"top_normalized_citations": [
			{"normalized_citation": normalized_citation, "occurrences": int(occurrences)}
			for normalized_citation, occurrences in variant_rows
		],
		"sample_contexts": citation_contexts(session, source_case_id, target_case_id, limit=context_limit),
	}


def citation_intelligence_overview(session: Session, case_id: int) -> dict[str, Any]:
	"""Core metrics for a single authority: citing case counts, occurrences, date range."""
	row = session.execute(
		select(
			func.count(func.distinct(Citation.source_case_id)).label("unique_citing_cases"),
			func.count(Citation.id).label("total_occurrences"),
			func.min(Case.date).label("first_citation_date"),
			func.max(Case.date).label("most_recent_date"),
		)
		.join(Case, Case.id == Citation.source_case_id)
		.where(Citation.target_case_id == case_id)
	).first()
	unique_citing = int(row[0] or 0)
	total_occ = int(row[1] or 0)
	first_date = row[2]
	latest_date = row[3]

	# Two-level aggregation: count per case first, then avg/max across cases
	per_case_cte = (
		select(
			Citation.source_case_id,
			func.count(Citation.id).label("mention_count"),
		)
		.where(Citation.target_case_id == case_id)
		.group_by(Citation.source_case_id)
		.cte("ci_per_case")
	)
	stats = session.execute(
		select(
			func.avg(per_case_cte.c.mention_count),
			func.max(per_case_cte.c.mention_count),
		)
	).first()
	avg_mentions = round(float(stats[0] or 0), 2)
	max_mentions = int(stats[1] or 0)

	# Case with the most mentions
	top_case_row = session.execute(
		select(Case, func.count(Citation.id).label("mention_count"))
		.join(Citation, Citation.source_case_id == Case.id)
		.where(Citation.target_case_id == case_id)
		.group_by(Case.id)
		.order_by(func.count(Citation.id).desc())
		.limit(1)
	).first()
	top_citing_case = None
	if top_case_row:
		top_case, top_count = top_case_row
		top_citing_case = {"case_id": top_case.id, "title": top_case.title, "citation": top_case.citation, "mention_count": int(top_count)}

	# Authority case details
	authority = session.get(Case, case_id)
	metrics = session.get(CitationMetrics, case_id)

	return {
		"case_id": case_id,
		"title": authority.title if authority else None,
		"citation": authority.citation if authority else None,
		"court": authority.court if authority else None,
		"date": str(authority.date) if authority and authority.date else None,
		"in_degree": int(metrics.in_degree or 0) if metrics else 0,
		"pagerank": float(metrics.pagerank) if metrics and metrics.pagerank else None,
		"unique_citing_cases": unique_citing,
		"total_occurrences": total_occ,
		"avg_mentions_per_case": avg_mentions,
		"max_mentions_in_single_case": max_mentions,
		"top_citing_case": top_citing_case,
		"first_citation_date": str(first_date) if first_date else None,
		"most_recent_citation_date": str(latest_date) if latest_date else None,
	}


def citation_intelligence_timeline(session: Session, case_id: int) -> list[dict[str, Any]]:
	"""Citing-case counts and total occurrences grouped by year."""
	rows = session.execute(
		select(
			func.extract("year", Case.date).label("year"),
			func.count(func.distinct(Citation.source_case_id)).label("citing_cases"),
			func.count(Citation.id).label("occurrences"),
		)
		.join(Case, Case.id == Citation.source_case_id)
		.where(Citation.target_case_id == case_id)
		.group_by(func.extract("year", Case.date))
		.order_by(func.extract("year", Case.date))
	)
	return [
		{"year": int(year), "citing_cases": int(citing_cases), "occurrences": int(occurrences)}
		for year, citing_cases, occurrences in rows
	]


def citation_intelligence_outcomes(session: Session, case_id: int) -> dict[str, Any]:
	"""Government outcome breakdown across all cases citing this authority."""
	rows = session.execute(
		select(
			func.coalesce(
				func.lower(Case.metadata_json["reader_extracted"]["government outcome"].as_string()),
				"unknown",
			).label("outcome"),
			func.count(func.distinct(Citation.source_case_id)).label("case_count"),
		)
		.join(Case, Case.id == Citation.source_case_id)
		.where(Citation.target_case_id == case_id)
		.group_by(
			func.coalesce(
				func.lower(Case.metadata_json["reader_extracted"]["government outcome"].as_string()),
				"unknown",
			)
		)
	).all()
	totals: dict[str, int] = {}
	for outcome, count in rows:
		label = outcome.strip() if outcome else "unknown"
		if label in {"won", "government won"}:
			label = "government_win"
		elif label in {"lost", "government lost"}:
			label = "government_loss"
		elif label in {"mixed"}:
			label = "mixed"
		else:
			label = "unknown"
		totals[label] = totals.get(label, 0) + int(count)
	total_cases = sum(totals.values())
	return {
		"government_win": totals.get("government_win", 0),
		"government_loss": totals.get("government_loss", 0),
		"mixed": totals.get("mixed", 0),
		"unknown": totals.get("unknown", 0),
		"total_cases": total_cases,
		"government_win_pct": round(100 * totals.get("government_win", 0) / total_cases, 1) if total_cases else 0.0,
		"government_loss_pct": round(100 * totals.get("government_loss", 0) / total_cases, 1) if total_cases else 0.0,
		"mixed_pct": round(100 * totals.get("mixed", 0) / total_cases, 1) if total_cases else 0.0,
		"unknown_pct": round(100 * totals.get("unknown", 0) / total_cases, 1) if total_cases else 0.0,
	}


def citation_intelligence_courts(session: Session, case_id: int) -> list[dict[str, Any]]:
	"""Citation counts broken down by citing-case court."""
	rows = session.execute(
		select(
			Case.court.label("court"),
			func.count(func.distinct(Citation.source_case_id)).label("case_count"),
			func.count(Citation.id).label("occurrences"),
		)
		.join(Case, Case.id == Citation.source_case_id)
		.where(Citation.target_case_id == case_id)
		.group_by(Case.court)
		.order_by(func.count(func.distinct(Citation.source_case_id)).desc())
	).all()
	total_cases = sum(int(r[1]) for r in rows)
	return [
		{
			"court": court,
			"case_count": int(case_count),
			"occurrences": int(occurrences),
			"pct": round(100 * int(case_count) / total_cases, 1) if total_cases else 0.0,
		}
		for court, case_count, occurrences in rows
	]


def citation_intelligence_judges(session: Session, case_id: int, limit: int = 30) -> list[dict[str, Any]]:
	"""Top judges citing this authority, via raw name in metadata_json."""
	rows = session.execute(
		select(
			func.coalesce(
				Case.metadata_json["reader_extracted"]["judge"].as_string(),
				"Unknown",
			).label("judge"),
			func.count(func.distinct(Citation.source_case_id)).label("case_count"),
			func.count(Citation.id).label("occurrences"),
			func.min(Case.date).label("first_use"),
			func.max(Case.date).label("latest_use"),
		)
		.join(Case, Case.id == Citation.source_case_id)
		.where(
			Citation.target_case_id == case_id,
			Case.metadata_json["reader_extracted"]["judge"].as_string().is_not(None),
			Case.metadata_json["reader_extracted"]["judge"].as_string() != "",
		)
		.group_by(
			func.coalesce(
				Case.metadata_json["reader_extracted"]["judge"].as_string(),
				"Unknown",
			)
		)
		.order_by(func.count(func.distinct(Citation.source_case_id)).desc())
		.limit(limit)
	).all()
	return [
		{
			"judge": judge,
			"case_count": int(case_count),
			"occurrences": int(occurrences),
			"first_use": str(first_use) if first_use else None,
			"latest_use": str(latest_use) if latest_use else None,
		}
		for judge, case_count, occurrences, first_use, latest_use in rows
	]


def citation_intelligence_statutes(session: Session, case_id: int, limit: int = 20) -> list[dict[str, Any]]:
	"""Statute provisions most frequently co-cited alongside this authority."""
	# Source cases that cite this authority
	citing_sources = (
		select(Citation.source_case_id)
		.where(Citation.target_case_id == case_id)
		.distinct()
		.cte("ci_citing_sources")
	)
	rows = session.execute(
		select(
			StatuteReference.normalized_reference,
			func.count(func.distinct(StatuteReference.source_case_id)).label("case_count"),
			func.count(StatuteReference.id).label("occurrences"),
		)
		.join(citing_sources, citing_sources.c.source_case_id == StatuteReference.source_case_id)
		.where(StatuteReference.normalized_reference.is_not(None))
		.group_by(StatuteReference.normalized_reference)
		.order_by(func.count(func.distinct(StatuteReference.source_case_id)).desc())
		.limit(limit)
	).all()
	return [
		{
			"provision": normalized_reference,
			"case_count": int(case_count),
			"occurrences": int(occurrences),
		}
		for normalized_reference, case_count, occurrences in rows
	]


def citation_intelligence_table(
	self_or_session: Session,
	case_id: int,
	*,
	page: int = 1,
	page_size: int = 50,
	year: int | None = None,
	court: str | None = None,
	judge: str | None = None,
	gov_outcome: str | None = None,
	min_mentions: int = 1,
) -> dict[str, Any]:
	"""Paginated evidence table: one row per citation where target is this authority."""
	session = self_or_session
	per_case_counts = (
		select(
			Citation.source_case_id,
			func.count(Citation.id).label("mention_count"),
		)
		.where(Citation.target_case_id == case_id)
		.group_by(Citation.source_case_id)
		.having(func.count(Citation.id) >= min_mentions)
		.cte("ci_per_case_counts")
	)
	base = (
		select(
			Citation,
			Case,
			CaseChunk,
			per_case_counts.c.mention_count,
		)
		.join(Case, Case.id == Citation.source_case_id)
		.outerjoin(CaseChunk, CaseChunk.id == Citation.chunk_id)
		.join(per_case_counts, per_case_counts.c.source_case_id == Citation.source_case_id)
		.where(Citation.target_case_id == case_id)
	)
	if year:
		base = base.where(func.extract("year", Case.date) == year)
	if court:
		base = base.where(Case.court.ilike(f"%{court}%"))
	if judge:
		base = base.where(
			Case.metadata_json["reader_extracted"]["judge"].as_string().ilike(f"%{judge}%")
		)
	if gov_outcome:
		base = base.where(
			func.lower(Case.metadata_json["reader_extracted"]["government outcome"].as_string()) == gov_outcome.lower()
		)

	total = session.scalar(select(func.count()).select_from(base.subquery())) or 0
	rows = session.execute(
		base.order_by(Case.date.desc(), Citation.source_case_id, Citation.id)
		.offset((page - 1) * page_size)
		.limit(page_size)
	).all()

	results = []
	for citation, source_case, chunk, mention_count in rows:
		judge_val = None
		gov_outcome_val = None
		if source_case.metadata_json and "reader_extracted" in source_case.metadata_json:
			re_data = source_case.metadata_json["reader_extracted"]
			judge_val = re_data.get("judge")
			gov_outcome_val = re_data.get("government outcome")
		results.append({
			"citation_id": citation.id,
			"case_id": source_case.id,
			"case_title": source_case.title,
			"case_citation": source_case.citation,
			"court": source_case.court,
			"date": str(source_case.date) if source_case.date else None,
			"judge": judge_val,
			"gov_outcome": gov_outcome_val,
			"mention_count": int(mention_count or 0),
			"chunk_id": chunk.id if chunk else None,
			"chunk_index": chunk.chunk_index if chunk else None,
			"citation_text": citation.citation_text,
			"chunk_text": chunk.text if chunk else None,
		})
	return {
		"total": int(total),
		"page": page,
		"page_size": page_size,
		"total_pages": max(1, -(-int(total) // page_size)),
		"rows": results,
	}