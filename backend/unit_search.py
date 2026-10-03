"""Unit-level search service with semantic embeddings and keyword fallback."""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from typing import Any

from sqlalchemy import and_, select, text
from sqlalchemy.orm import Session

from .database import CaseChunk, CaseChunkEmbedding, Case, CaseJudgeProfile, CaseOutcome
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


def search_units_by_embedding(
	query: str,
	db: Session,
	limit: int = 20,
	embedding_model: str = "bge-m3",
	similarity_threshold: float = 0.5,
) -> list[UnitSearchResult]:
	"""
	Search units using semantic embeddings with keyword fallback.

	Args:
		query: Search query text
		db: Database session
		limit: Maximum results to return
		embedding_model: Embedding model name (default: bge-m3 from PR 30)
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
	# Note: In a real system, we'd embed the query using the same model
	# For now, we return an empty list to demonstrate the fallback flow
	# Production implementation would:
	# 1. Embed the query using bge-m3
	# 2. Query <=> operator on pgvector for similarity
	# 3. Join with discussion_unit_cache to get unit metadata
	logger.debug(f"Semantic search not yet implemented for: {query}")
	return []


def _keyword_search(query: str, db: Session, limit: int) -> list[UnitSearchResult]:
	"""Search units using keyword matching."""
	# Split query into words for keyword search
	keywords = query.lower().split()

	# Query case_chunks for matching text
	# Join with discussion_unit_cache to get unit info
	# This is a simplified implementation; production would:
	# 1. Use full-text search (FTS) for better performance
	# 2. Match against subtheme key_terms
	# 3. Weight matches by relevance (title matches > content matches)

	results = []

	# For now, return empty to prevent errors in development
	# TODO: Implement full keyword search across units

	return results


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

	judge_names = [j.judge_name for j in judges] if judges else []
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
