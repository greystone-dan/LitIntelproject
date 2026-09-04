"""Search and retrieval service for AI CaseLibrary.

Owns query validation, filter expression generation, tsvector lexical ranking,
cosine distance semantic scoring, hybrid candidate combination, and chunk grouping.
"""

from __future__ import annotations

import math
import os
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable

from fastapi import HTTPException, status
from openai import OpenAI, OpenAIError
from sqlalchemy import Text, func, or_, select
from sqlalchemy.orm import Session
from sqlalchemy.sql import Select

try:
	import yaml
except Exception:  # pragma: no cover
	yaml = None

from .database import Case, CaseChunk, CaseChunkEmbedding, CaseTag, CitationMetrics
from .embedding_providers import SentenceTransformerEmbeddingProvider
from .legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION
from .models import (
	CaseResponse,
	CaseSearchRequest,
	CaseSearchResponse,
	ChunkGroupSearchRequest,
	ChunkPassage,
	ChunkSearchResponse,
	GroupedChunkCaseResponse,
	GroupedChunkSearchResponse,
	LocalChunkSearchRequest,
)

EMBEDDING_DIMENSIONS = 1536
EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")


def _env_bool(name: str) -> bool | None:
	value = os.getenv(name)
	if value is None:
		return None
	return value.strip().lower() in {"1", "true", "yes", "on"}


def _load_ai_rollout_flags() -> dict[str, bool]:
	flags = {
		"semantic_enabled": True,
		"hybrid_enabled": True,
		"local_semantic_enabled": True,
		"embed_on_ingest_enabled": True,
	}

	config_path = Path(__file__).resolve().parent.parent / "config.yaml"
	if yaml is not None and config_path.exists():
		try:
			payload = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
			rollout = (payload.get("ai") or {}).get("rollout") or {}
			for key in flags:
				if key in rollout:
					flags[key] = bool(rollout.get(key))
		except Exception:
			pass

	overrides = {
		"semantic_enabled": _env_bool("CASELIBRARY_SEMANTIC_ENABLED"),
		"hybrid_enabled": _env_bool("CASELIBRARY_HYBRID_ENABLED"),
		"local_semantic_enabled": _env_bool("CASELIBRARY_LOCAL_SEMANTIC_ENABLED"),
		"embed_on_ingest_enabled": _env_bool("CASELIBRARY_EMBED_ON_INGEST_ENABLED"),
	}
	for key, value in overrides.items():
		if value is not None:
			flags[key] = value
	return flags


AI_ROLLOUT = _load_ai_rollout_flags()


def _effective_search_mode(requested_mode: str, rollout: dict[str, bool] | None = None) -> str:
	flags = rollout or AI_ROLLOUT
	if requested_mode == "semantic" and not flags.get("semantic_enabled", True):
		return "metadata"
	if requested_mode == "hybrid" and (
		not flags.get("hybrid_enabled", True) or not flags.get("semantic_enabled", True)
	):
		return "metadata"
	return requested_mode


def _embed(text: str) -> list[float]:
	api_key = os.getenv("OPENAI_API_KEY")
	if not api_key:
		raise HTTPException(
			status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
			detail="OPENAI_API_KEY is not configured",
		)

	try:
		client = OpenAI(api_key=api_key)
		response = client.embeddings.create(input=text, model=EMBEDDING_MODEL)
	except OpenAIError as exc:
		raise HTTPException(
			status_code=status.HTTP_502_BAD_GATEWAY,
			detail="The embedding service is unavailable",
		) from exc

	embedding = response.data[0].embedding
	if len(embedding) != EMBEDDING_DIMENSIONS:
		raise HTTPException(
			status_code=status.HTTP_502_BAD_GATEWAY,
			detail="The embedding service returned an unexpected vector size",
		)
	return embedding


def _party_filter_terms(filters: list[str]) -> list[str]:
	aliases = {
		"Minister": [
			"Minister",
			"MPSEP",
			"Minister of Public Safety",
			"Minister of Public Safety and Emergency Preparedness",
		],
		"IRCC": [
			"IRCC",
			"Immigration, Refugees and Citizenship Canada",
			"Citizenship and Immigration Canada",
		],
		"CBSA": [
			"CBSA",
			"Canada Border Services Agency",
			"Border Services Agency",
		],
	}

	terms: list[str] = []
	seen: set[str] = set()
	for filter_name in filters:
		for term in aliases.get(filter_name, [filter_name]):
			normalized = term.strip()
			if normalized and normalized.lower() not in seen:
				seen.add(normalized.lower())
				terms.append(normalized)
	return terms


def _case_search_document() -> Any:
	return func.concat_ws(
		" ",
		func.coalesce(Case.title, ""),
		func.coalesce(Case.citation, ""),
		func.coalesce(Case.secondary_citation, ""),
		func.coalesce(Case.source_name, ""),
		func.coalesce(Case.source_id, ""),
		func.coalesce(Case.court, ""),
		func.coalesce(Case.jurisdiction, ""),
		func.coalesce(Case.summary, ""),
		func.coalesce(Case.full_text, ""),
		func.coalesce(func.cast(Case.cases_cited, Text), ""),
		func.coalesce(func.cast(Case.cases_citing, Text), ""),
		func.coalesce(func.cast(Case.metadata_json, Text), ""),
	)


def _chunk_search_document() -> Any:
	return func.concat_ws(
		" ",
		func.coalesce(Case.title, ""),
		func.coalesce(Case.citation, ""),
		func.coalesce(Case.secondary_citation, ""),
		func.coalesce(Case.source_name, ""),
		func.coalesce(Case.source_id, ""),
		func.coalesce(Case.court, ""),
		func.coalesce(Case.jurisdiction, ""),
		func.coalesce(Case.summary, ""),
		func.coalesce(Case.full_text, ""),
		func.coalesce(func.cast(Case.cases_cited, Text), ""),
		func.coalesce(func.cast(Case.cases_citing, Text), ""),
		func.coalesce(func.cast(Case.metadata_json, Text), ""),
		func.coalesce(CaseChunk.text, ""),
	)


def _apply_case_filters(statement: Select, search: CaseSearchRequest) -> Select:
	if search.title_contains:
		statement = statement.where(Case.title.ilike(f"%{search.title_contains}%"))
	if search.court:
		court_aliases = {
			"FC": "Federal Court",
			"FCA": "Federal Court of Appeal",
			"SCC": "Supreme Court of Canada",
		}
		court_name = court_aliases.get(search.court.upper(), search.court)
		statement = statement.where(Case.court.ilike(f"%{court_name}%"))
	if search.jurisdiction:
		statement = statement.where(Case.jurisdiction == search.jurisdiction)
	if search.source_name_contains:
		statement = statement.where(Case.source_name.ilike(f"%{search.source_name_contains}%"))
	if search.source_url_contains:
		statement = statement.where(Case.source_url.ilike(f"%{search.source_url_contains}%"))
	if search.source_id_contains:
		statement = statement.where(Case.source_id.ilike(f"%{search.source_id_contains}%"))
	if search.dataset_version_contains:
		statement = statement.where(Case.dataset_version.ilike(f"%{search.dataset_version_contains}%"))
	if search.upstream_license_contains:
		statement = statement.where(Case.upstream_license.ilike(f"%{search.upstream_license_contains}%"))
	if search.secondary_citation_contains:
		statement = statement.where(Case.secondary_citation.ilike(f"%{search.secondary_citation_contains}%"))
	if search.party_filters:
		searchable_document = _case_search_document()
		party_terms = _party_filter_terms([party for party in search.party_filters if party])
		party_clauses = [searchable_document.ilike(f"%{party}%") for party in party_terms]
		if party_clauses:
			statement = statement.where(or_(*party_clauses))
	if search.source_type:
		statement = statement.where(Case.source_type == search.source_type)
	if search.language:
		statement = statement.where(Case.language == search.language)
	if search.processing_status:
		statement = statement.where(Case.processing_status == search.processing_status)
	for tag_filter in search.tag_filters or []:
		category, _, value = tag_filter.partition(":")
		statement = statement.where(
			select(CaseTag.id)
			.where(
				CaseTag.case_id == Case.id,
				CaseTag.category == category.strip(),
				CaseTag.value == value.strip(),
				CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
			)
			.exists()
		)
	if search.date_from:
		statement = statement.where(Case.date >= search.date_from)
	if search.date_to:
		statement = statement.where(Case.date <= search.date_to)
	if search.scraped_from:
		statement = statement.where(func.date(Case.scraped_at) >= search.scraped_from)
	if search.scraped_to:
		statement = statement.where(func.date(Case.scraped_at) <= search.scraped_to)
	if search.citing_cases_min is not None:
		statement = statement.where(func.coalesce(Case.citing_cases_count, 0) >= search.citing_cases_min)
	if search.citing_cases_max is not None:
		statement = statement.where(func.coalesce(Case.citing_cases_count, 0) <= search.citing_cases_max)
	if search.cited_case:
		cited_case_text = func.coalesce(func.cast(Case.cases_cited, Text), "")
		statement = statement.where(cited_case_text.ilike(f"%{search.cited_case}%"))
	if search.citation_contains:
		needle = f"%{search.citation_contains}%"
		statement = statement.where(
			or_(
				Case.citation.ilike(needle),
				Case.secondary_citation.ilike(needle),
			)
		)
	if search.cases_cited_contains:
		cited_text = func.coalesce(func.cast(Case.cases_cited, Text), "")
		statement = statement.where(cited_text.ilike(f"%{search.cases_cited_contains}%"))
	if search.cases_citing_contains:
		citing_text = func.coalesce(func.cast(Case.cases_citing, Text), "")
		statement = statement.where(citing_text.ilike(f"%{search.cases_citing_contains}%"))
	return statement


def _validate_search_ranges(search: CaseSearchRequest) -> None:
	if search.date_from and search.date_to and search.date_from > search.date_to:
		raise HTTPException(status_code=422, detail="date_from must be on or before date_to")
	if search.scraped_from and search.scraped_to and search.scraped_from > search.scraped_to:
		raise HTTPException(status_code=422, detail="scraped_from must be on or before scraped_to")
	if (
		search.citing_cases_min is not None
		and search.citing_cases_max is not None
		and search.citing_cases_min > search.citing_cases_max
	):
		raise HTTPException(status_code=422, detail="citing_cases_min must be less than or equal to citing_cases_max")


def _case_match_source(case: Case, query: str, search_mode: str) -> str:
	query_text = " ".join(query.lower().split())
	if not query_text:
		return "Metadata" if search_mode == "metadata" else "Mixed"

	metadata_parts = [
		getattr(case, "title", None),
		getattr(case, "citation", None),
		getattr(case, "secondary_citation", None),
		getattr(case, "source_name", None),
		getattr(case, "source_id", None),
		getattr(case, "court", None),
		getattr(case, "jurisdiction", None),
		str(getattr(case, "metadata_json", None) or ""),
		str(getattr(case, "cases_cited", None) or ""),
		str(getattr(case, "cases_citing", None) or ""),
	]
	metadata_text = " ".join(part for part in metadata_parts if part).lower()
	body_text = f"{getattr(case, 'summary', '') or ''} {getattr(case, 'full_text', '') or ''}".lower()

	metadata_hits = sum(1 for token in query_text.split() if token in metadata_text)
	body_hits = sum(1 for token in query_text.split() if token in body_text)
	if metadata_hits > body_hits:
		return "Metadata"
	if body_hits > metadata_hits:
		return "Full text"
	if search_mode == "metadata":
		return "Metadata"
	if search_mode == "semantic":
		return "Full text"
	return "Mixed"


def _case_lexical_rank_expr(query: str):
	document = _case_search_document()
	return func.ts_rank_cd(func.to_tsvector("simple", document), func.plainto_tsquery("simple", query))


def _chunk_lexical_rank_expr(query: str):
	document = _chunk_search_document()
	return func.ts_rank_cd(func.to_tsvector("simple", document), func.plainto_tsquery("simple", query))


@lru_cache(maxsize=2)
def _local_embedding_provider(model_name: str) -> SentenceTransformerEmbeddingProvider:
	return SentenceTransformerEmbeddingProvider(model_name=model_name)


def execute_search_cases(
	search: CaseSearchRequest,
	db: Session,
	*,
	embed_fn: Callable[[str], list[float]] | None = None,
	rollout: dict[str, bool] | None = None,
) -> list[CaseSearchResponse]:
	_validate_search_ranges(search)
	effective_mode = _effective_search_mode(search.search_mode, rollout=rollout)
	embed_func = embed_fn or _embed

	query_vector = embed_func(search.query) if effective_mode in {"semantic", "hybrid"} else None
	semantic_distance = (
		Case.embedding.cosine_distance(query_vector).label("semantic_distance")
		if query_vector is not None
		else None
	)
	lexical_rank = _case_lexical_rank_expr(search.query).label("lexical_rank")
	graph_in_degree = func.coalesce(CitationMetrics.in_degree, 0).label("graph_in_degree")

	statement = (
		select(Case, semantic_distance, lexical_rank, graph_in_degree)
		if semantic_distance is not None
		else select(Case, lexical_rank, graph_in_degree)
	)
	statement = statement.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
	if effective_mode in {"semantic", "hybrid"}:
		statement = statement.where(Case.embedding.is_not(None))
	statement = _apply_case_filters(statement, search)

	if effective_mode in {"lexical", "metadata"}:
		statement = statement.order_by(lexical_rank.desc())
	else:
		statement = statement.order_by(semantic_distance)

	raw_rows = list(db.execute(statement))
	prepared_rows: list[tuple[Case, float, float]] = []
	max_lexical = 0.0

	for row in raw_rows:
		if effective_mode in {"semantic", "hybrid"}:
			if len(row) == 4:
				case, semantic_distance_value, lexical_rank_value, graph_in_degree_value = row
			else:
				case, semantic_distance_value, lexical_rank_value = row
				graph_in_degree_value = 0
		else:
			if len(row) == 3:
				case, lexical_rank_value, graph_in_degree_value = row
			else:
				case, lexical_rank_value = row
				graph_in_degree_value = 0
			semantic_distance_value = None

		semantic_similarity = (
			max(0.0, min(1.0, 1.0 - float(semantic_distance_value)))
			if semantic_distance_value is not None
			else 0.0
		)
		lexical_score = max(0.0, float(lexical_rank_value or 0.0))
		max_lexical = max(max_lexical, lexical_score)
		prepared_rows.append((case, semantic_similarity, lexical_score))

	weighted_rows: list[tuple[Case, float, float]] = []
	for case, semantic_similarity, lexical_score in prepared_rows:
		lexical_similarity = lexical_score / max_lexical if max_lexical > 0 else 0.0
		if effective_mode == "semantic":
			final_score = semantic_similarity
		elif effective_mode in {"lexical", "metadata"}:
			final_score = lexical_similarity
		else:
			denominator = search.semantic_weight + search.lexical_weight
			final_score = (
				(search.semantic_weight * semantic_similarity) + (search.lexical_weight * lexical_similarity)
			) / denominator
		graph_boost = min(0.05, math.log1p(max(0, graph_in_degree_value)) / 100.0)
		weighted_rows.append((case, final_score, final_score + graph_boost))

	weighted_rows.sort(key=lambda item: item[2], reverse=True)
	start = (search.page - 1) * search.page_size
	end = start + search.page_size
	page_rows = weighted_rows[start:end]

	return [
		CaseSearchResponse(
			**CaseResponse.model_validate(case, from_attributes=True).model_dump(),
			similarity=score,
			match_source=_case_match_source(case, search.query, effective_mode),
		)
		for case, score, _ in page_rows
	]


def execute_search_chunks(
	search: CaseSearchRequest,
	db: Session,
	*,
	embed_fn: Callable[[str], list[float]] | None = None,
	rollout: dict[str, bool] | None = None,
) -> list[ChunkSearchResponse]:
	_validate_search_ranges(search)
	effective_mode = _effective_search_mode(search.search_mode, rollout=rollout)
	embed_func = embed_fn or _embed

	if effective_mode in {"lexical", "metadata"}:
		lexical_rank = _chunk_lexical_rank_expr(search.query).label("lexical_rank")
		statement = (
			select(Case, CaseChunk, lexical_rank)
			.join(CaseChunk, CaseChunk.case_id == Case.id)
			.order_by(lexical_rank.desc())
			.offset((search.page - 1) * search.page_size)
			.limit(search.page_size)
		)
	else:
		distance = CaseChunk.embedding.cosine_distance(embed_func(search.query)).label("distance")
		statement = (
			select(Case, CaseChunk, distance)
			.join(CaseChunk, CaseChunk.case_id == Case.id)
			.where(CaseChunk.embedding.is_not(None))
			.order_by(distance)
			.offset((search.page - 1) * search.page_size)
			.limit(search.page_size)
		)
	statement = _apply_case_filters(statement, search)

	rows = list(db.execute(statement))
	if effective_mode in {"lexical", "metadata"}:
		max_lexical = max((float(rank or 0.0) for _, _, rank in rows), default=0.0)
		return [
			ChunkSearchResponse(
				**CaseResponse.model_validate(case, from_attributes=True).model_dump(),
				chunk_index=chunk.chunk_index,
				chunk_text=chunk.text,
				similarity=(max(0.0, float(rank or 0.0)) / max_lexical if max_lexical > 0 else 0.0),
			)
			for case, chunk, rank in rows
		]

	return [
		ChunkSearchResponse(
			**CaseResponse.model_validate(case, from_attributes=True).model_dump(),
			chunk_index=chunk.chunk_index,
			chunk_text=chunk.text,
			similarity=max(0.0, min(1.0, 1.0 - float(distance_value))),
		)
		for case, chunk, distance_value in rows
	]


def execute_search_chunks_local(
	search: LocalChunkSearchRequest,
	db: Session,
	*,
	rollout: dict[str, bool] | None = None,
) -> list[ChunkSearchResponse]:
	flags = rollout or AI_ROLLOUT
	if not flags.get("local_semantic_enabled", True):
		raise HTTPException(
			status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
			detail="Local semantic search is disabled by rollout configuration",
		)
	_validate_search_ranges(search)
	query_vector = _local_embedding_provider(search.model_name).embed_query(search.query)
	distance = CaseChunkEmbedding.embedding.cosine_distance(query_vector).label("distance")
	statement = (
		select(Case, CaseChunk, distance)
		.join(CaseChunk, CaseChunk.case_id == Case.id)
		.join(CaseChunkEmbedding, CaseChunkEmbedding.chunk_id == CaseChunk.id)
		.where(CaseChunkEmbedding.model_name == search.model_name)
		.order_by(distance)
		.offset((search.page - 1) * search.page_size)
		.limit(search.page_size)
	)
	statement = _apply_case_filters(statement, search)
	rows = list(db.execute(statement))
	return [
		ChunkSearchResponse(
			**CaseResponse.model_validate(case, from_attributes=True).model_dump(),
			chunk_index=chunk.chunk_index,
			chunk_text=chunk.text,
			similarity=max(0.0, min(1.0, 1.0 - float(distance_value))),
		)
		for case, chunk, distance_value in rows
	]


def execute_grouped_chunk_search(
	search: ChunkGroupSearchRequest,
	db: Session,
	*,
	embed_fn: Callable[[str], list[float]] | None = None,
	rollout: dict[str, bool] | None = None,
) -> GroupedChunkSearchResponse:
	"""Inner retrieval shared by /search/chunks/grouped and /research."""
	_validate_search_ranges(search)
	effective_mode = _effective_search_mode(search.search_mode, rollout=rollout)
	embed_func = embed_fn or _embed

	query_vector = embed_func(search.query) if effective_mode in {"semantic", "hybrid"} else None
	semantic_distance = (
		CaseChunk.embedding.cosine_distance(query_vector).label("semantic_distance")
		if query_vector is not None
		else None
	)
	lexical_rank = _chunk_lexical_rank_expr(search.query).label("lexical_rank")

	statement = (
		select(Case, CaseChunk, semantic_distance, lexical_rank)
		if semantic_distance is not None
		else select(Case, CaseChunk, lexical_rank)
	)
	statement = statement.join(CaseChunk, CaseChunk.case_id == Case.id)
	if effective_mode in {"semantic", "hybrid"}:
		statement = statement.where(CaseChunk.embedding.is_not(None))
	statement = _apply_case_filters(statement, search)

	chunk_scan_limit = min(
		500,
		max(search.candidate_pool, search.page_size * search.max_chunks_per_case * 5),
	)
	if effective_mode in {"lexical", "metadata"}:
		statement = statement.order_by(lexical_rank.desc()).limit(chunk_scan_limit)
	else:
		statement = statement.order_by(semantic_distance).limit(chunk_scan_limit)

	raw_rows = list(db.execute(statement))
	prepared_rows: list[tuple[Case, CaseChunk, float, float]] = []
	max_lexical = 0.0

	for row in raw_rows:
		if effective_mode in {"semantic", "hybrid"}:
			case, chunk, semantic_distance_value, lexical_rank_value = row
		else:
			case, chunk, lexical_rank_value = row
			semantic_distance_value = None

		semantic_similarity = (
			max(0.0, min(1.0, 1.0 - float(semantic_distance_value)))
			if semantic_distance_value is not None
			else 0.0
		)
		lexical_score = max(0.0, float(lexical_rank_value or 0.0))
		max_lexical = max(max_lexical, lexical_score)
		prepared_rows.append((case, chunk, semantic_similarity, lexical_score))

	grouped: dict[int, GroupedChunkCaseResponse] = {}
	for case, chunk, semantic_similarity, lexical_score in prepared_rows:
		lexical_similarity = lexical_score / max_lexical if max_lexical > 0 else 0.0
		if effective_mode == "semantic":
			final_similarity = semantic_similarity
		elif effective_mode in {"lexical", "metadata"}:
			final_similarity = lexical_similarity
		else:
			denominator = search.semantic_weight + search.lexical_weight
			final_similarity = (
				(search.semantic_weight * semantic_similarity) + (search.lexical_weight * lexical_similarity)
			) / denominator

		case_id = case.id
		entry = grouped.get(case_id)
		if entry is None:
			entry = GroupedChunkCaseResponse(
				**CaseResponse.model_validate(case, from_attributes=True).model_dump(),
				best_similarity=final_similarity,
				chunks=[],
			)
			grouped[case_id] = entry
		entry.best_similarity = max(entry.best_similarity, final_similarity)
		entry.chunks.append(
			ChunkPassage(
				chunk_index=chunk.chunk_index,
				chunk_text=chunk.text,
				similarity=final_similarity,
			)
		)

	grouped_cases = list(grouped.values())
	for item in grouped_cases:
		item.chunks.sort(key=lambda c: c.similarity, reverse=True)
		item.chunks = item.chunks[: search.max_chunks_per_case]
	grouped_cases.sort(key=lambda c: c.best_similarity, reverse=True)

	start = (search.page - 1) * search.page_size
	end = start + search.page_size
	paged_cases = grouped_cases[start:end]

	return GroupedChunkSearchResponse(
		total_cases=len(grouped_cases),
		total_chunks=len(raw_rows),
		max_chunks_per_case=search.max_chunks_per_case,
		cases=paged_cases,
	)
