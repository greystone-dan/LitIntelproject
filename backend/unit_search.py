"""Unit-level search service with semantic embeddings and keyword fallback."""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from typing import Any

from sqlalchemy import and_, select, text, func
from sqlalchemy.orm import Session

from .embedding_providers import DEFAULT_LOCAL_EMBEDDING_MODEL
from .database import (
	CaseChunk,
	CaseChunkEmbedding,
	Case,
	CaseJudgeProfile,
	CaseOutcome,
	DiscussionUnitCache,
)
from .contextual_authority.discussion_units import DISCUSSION_UNIT_METHOD, DISCUSSION_UNIT_VERSION

logger = logging.getLogger(__name__)


@dataclass
class UnitSearchResult:
	"""Result from unit search."""
	case_id: int
	unit_index: int
	start_paragraph: int
	end_paragraph: int
	subtheme_id: str
	key_terms: list[str]
	judges: list[str]
	disposition: str | None
	score: float
	match_type: str  # 'semantic' or 'keyword'


# Deprecated: retained for compatibility; no backend or script callers exist.
def search_units_by_embedding(
	query: str,
	db: Session,
	limit: int = 20,
	embedding_model: str = DEFAULT_LOCAL_EMBEDDING_MODEL,
	similarity_threshold: float = 0.5,
) -> list[UnitSearchResult]:
	"""
	Search units using semantic embeddings with keyword fallback.

	Args:
		query: Search query text
		db: Database session
		limit: Maximum results to return
		embedding_model: Embedding model name (default: BAAI/bge-m3)
		similarity_threshold: Minimum similarity score (0-1)

	Returns:
		List of UnitSearchResult objects sorted by score
	"""
	# First try semantic search if embeddings are available
	semantic_results = _semantic_search(
		query, db, limit, embedding_model, similarity_threshold
	)

	if semantic_results:
		return semantic_results

	# Fall back to keyword search
	logger.info(f"Semantic search returned no results, falling back to keyword search")
	return _keyword_search(query, db, limit)


def _semantic_search(
	query: str,
	db: Session,
	limit: int,
	embedding_model: str,
	threshold: float,
) -> list[UnitSearchResult]:
	"""Search units using semantic similarity on embeddings."""
	try:
		from .embedding_providers import SentenceTransformerEmbeddingProvider
		from sqlalchemy import func
	except ImportError:
		logger.warning(f"Embedding provider not available, falling back to keyword search")
		return []

	try:
		# Get query embedding
		provider = SentenceTransformerEmbeddingProvider(model_name=embedding_model)
		query_embedding = provider.embed_query(query)

		# Search for similar chunks using cosine similarity
		# This uses pgvector's <=> operator for efficient similarity search
		similarity_results = db.execute(
			select(
				CaseChunk.case_id,
				CaseChunk.id.label("chunk_id"),
				CaseChunk.text,
				func.cosine_distance(
					CaseChunkEmbedding.embedding,
					query_embedding
				).label("distance"),
			)
			.join(
				CaseChunkEmbedding,
				and_(
					CaseChunk.id == CaseChunkEmbedding.chunk_id,
					CaseChunkEmbedding.model_name == embedding_model,
				),
			)
			.where(
				func.cosine_distance(
					CaseChunkEmbedding.embedding,
					query_embedding,
				) < (1.0 - threshold)  # Convert threshold to distance
			)
			.order_by("distance")
			.limit(limit * 2)  # Get extra to account for deduplication
		).all()

		if not similarity_results:
			logger.debug(f"No semantic matches for: {query}")
			return []

		# Convert to UnitSearchResult with judge enrichment
		results = []
		seen_units = set()

		for chunk in similarity_results:
			if len(results) >= limit:
				break

			# Get judge and outcome info for case
			judge_analytics = get_unit_judge_analytics(chunk.case_id, 0, db)

			# Map chunk to unit using discussion_unit_cache
			unit_index, start_para, end_para, subtheme_id = _map_chunk_to_unit(
				chunk.case_id, None, db  # TODO: Get paragraph indices from chunk
			)

			# Use unit as key to avoid duplicate results
			unit_key = (chunk.case_id, unit_index, subtheme_id)
			if unit_key in seen_units:
				continue

			seen_units.add(unit_key)

			# Extract key terms from chunk text (top content words)
			key_terms = _extract_key_terms(chunk.text, max_terms=3)

			result = UnitSearchResult(
				case_id=chunk.case_id,
				unit_index=unit_index,
				start_paragraph=start_para,
				end_paragraph=end_para,
				subtheme_id=subtheme_id,
				key_terms=key_terms,
				judges=judge_analytics.get("judges", []),
				disposition=judge_analytics.get("disposition"),
				score=1.0 - chunk.distance,  # Convert distance to similarity
				match_type="semantic",
			)
			results.append(result)

		return results

	except Exception as e:
		logger.error(f"Semantic search failed: {e}", exc_info=True)
		return []


def _keyword_search(query: str, db: Session, limit: int) -> list[UnitSearchResult]:
	"""Search units using keyword matching."""
	keywords = query.lower().split()
	if not keywords:
		return []

	results = []
	seen_units = set()

	try:
		# Search case chunks by keyword matching
		# Join with discussion_unit_cache to map chunks to units
		for keyword in keywords:
			pattern = f"%{keyword}%"
			chunks = db.execute(
				select(
					CaseChunk.case_id,
					CaseChunk.text,
				)
				.where(CaseChunk.text.ilike(pattern))
				.limit(limit * 3)
			).all()

			for chunk in chunks:
				if len(results) >= limit:
					break

				# Get judge and outcome info for case
				judge_analytics = get_unit_judge_analytics(chunk.case_id, 0, db)

				# Map chunk to unit using discussion_unit_cache
				unit_index, start_para, end_para, subtheme_id = _map_chunk_to_unit(
					chunk.case_id, None, db
				)

				# Use unit as key to avoid duplicate results
				unit_key = (chunk.case_id, unit_index, subtheme_id)
				if unit_key in seen_units:
					continue

				seen_units.add(unit_key)

				# Extract key terms from chunk text
				key_terms = _extract_key_terms(chunk.text, max_terms=3)

				result = UnitSearchResult(
					case_id=chunk.case_id,
					unit_index=unit_index,
					start_paragraph=start_para,
					end_paragraph=end_para,
					subtheme_id=subtheme_id,
					key_terms=key_terms,
					judges=judge_analytics.get("judges", []),
					disposition=judge_analytics.get("disposition"),
					score=0.5,  # Default score for keyword matches
					match_type="keyword",
				)
				results.append(result)

			if len(results) >= limit:
				break

	except Exception as e:
		logger.warning(f"Keyword search failed: {e}")
		return []

	return results[:limit]


def _map_chunk_to_unit(
	case_id: int,
	chunk_paragraph_indices: tuple[int, ...] | None,
	db: Session,
) -> tuple[int, int, int, str]:
	"""
	Map a chunk to its discussion unit and subtheme.

	Args:
		case_id: Case ID
		chunk_paragraph_indices: Paragraph indices in chunk (if available)
		db: Database session

	Returns:
		Tuple of (unit_index, start_paragraph, end_paragraph, subtheme_id)
	"""
	if not chunk_paragraph_indices:
		return (0, 0, 0, "")

	try:
		# Get cached units for case
		cache_entry = db.execute(
			select(DiscussionUnitCache)
			.where(DiscussionUnitCache.case_id == case_id)
			.where(
				DiscussionUnitCache.method_version
				== f"{DISCUSSION_UNIT_METHOD}:{DISCUSSION_UNIT_VERSION}"
			)
		).scalar_one_or_none()

		if not cache_entry:
			return (0, 0, 0, "")

		# Parse units JSON
		units_data = json.loads(cache_entry.units_json)

		# Find unit containing first paragraph of chunk
		first_para = chunk_paragraph_indices[0]

		for unit in units_data.get("units", []):
			unit_start = unit.get("start_paragraph", 0)
			unit_end = unit.get("end_paragraph", 0)

			if unit_start <= first_para <= unit_end:
				# Found the unit, now find the subtheme
				unit_index = unit.get("unit_index", 0)
				subtheme_id = ""

				for subtheme in unit.get("subthemes", []):
					para_indices = subtheme.get("paragraph_indices", [])
					if first_para in para_indices:
						subtheme_id = subtheme.get("subtheme_id", "")
						break

				return (unit_index, unit_start, unit_end, subtheme_id)

		return (0, 0, 0, "")

	except Exception as e:
		logger.warning(f"Failed to map chunk to unit: {e}")
		return (0, 0, 0, "")


def _extract_key_terms(text: str, max_terms: int = 3) -> list[str]:
	"""Extract key terms from text (top content words)."""
	import re
	from collections import Counter

	# Simple extraction: content words (3+ chars, not stopwords)
	stopwords = {
		"the", "and", "for", "that", "this", "with", "from", "have", "has",
		"been", "are", "were", "was", "is", "be", "by", "or", "an", "a",
		"of", "to", "in", "on", "at", "as", "if", "it", "but", "not",
	}

	words = re.findall(r'\b[a-z]+\b', text.lower())
	content_words = [w for w in words if len(w) >= 3 and w not in stopwords]

	if not content_words:
		return []

	# Return most common words
	counter = Counter(content_words)
	return [word for word, count in counter.most_common(max_terms)]


def get_unit_judge_analytics(
	case_id: int,
	unit_index: int,
	db: Session,
) -> dict[str, Any]:
	"""
	Get judge and outcome information for a unit in a case.

	Args:
		case_id: Case ID
		unit_index: Unit index
		db: Database session

	Returns:
		Dict with judges, outcomes, and citation patterns
	"""
	# Get judges for the case
	judges = db.execute(
		select(CaseJudgeProfile).where(CaseJudgeProfile.case_id == case_id)
	).scalars().all()

	# Get outcomes for the case
	outcomes = db.execute(
		select(CaseOutcome).where(CaseOutcome.case_id == case_id)
	).scalars().all()

	judge_names = [j.raw_name for j in judges] if judges else []
	outcome_disposition = outcomes[0].decision_outcome if outcomes else None

	return {
		"judges": judge_names,
		"disposition": outcome_disposition,
		"outcome_status": outcomes[0].outcome_status if outcomes else None,
		"winner_side": outcomes[0].winner_side if outcomes else None,
	}


def enrich_theme_with_judge_analytics(
	theme_data: dict[str, Any],
	db: Session,
) -> dict[str, Any]:
	"""
	Enrich theme data with judge/outcome analytics for each occurrence.

	Args:
		theme_data: Theme discovery data
		db: Database session

	Returns:
		Enhanced theme data with judge analytics
	"""
	# For each occurrence, fetch judge and outcome information
	for occurrence in theme_data.get("occurrences", []):
		analytics = get_unit_judge_analytics(
			occurrence["case_id"],
			occurrence["unit_index"],
			db,
		)
		occurrence.update(analytics)

	# Aggregate judge patterns across all occurrences
	judge_counts = {}
	disposition_counts = {}

	for occurrence in theme_data.get("occurrences", []):
		for judge in occurrence.get("judges", []):
			judge_counts[judge] = judge_counts.get(judge, 0) + 1

		disposition = occurrence.get("disposition")
		if disposition:
			disposition_counts[disposition] = disposition_counts.get(disposition, 0) + 1

	theme_data["judge_patterns"] = {
		"top_judges": sorted(
			judge_counts.items(),
			key=lambda x: x[1],
			reverse=True
		)[:5],
		"disposition_split": disposition_counts,
	}

	return theme_data
