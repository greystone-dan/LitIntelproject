"""
Batch job service for computing and caching discussion units across all cases.
Can be run periodically to update the cache, or on-demand for specific cases.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Case, DiscussionUnitCache
from .contextual_authority.discussion_units import DISCUSSION_UNIT_METHOD, DISCUSSION_UNIT_VERSION
from .reader_service import build_case_reader_data


logger = logging.getLogger(__name__)


def get_cached_evidence_summary(case_id: int, db: Session) -> dict[str, Any] | None:
	"""Get cached evidence summary for a case, or None if not cached."""
	row = db.execute(
		select(DiscussionUnitCache)
		.where(DiscussionUnitCache.case_id == case_id)
		.where(DiscussionUnitCache.method_version == f"{DISCUSSION_UNIT_METHOD}:{DISCUSSION_UNIT_VERSION}")
	).scalar_one_or_none()

	if not row:
		return None

	try:
		return json.loads(row.units_json)
	except json.JSONDecodeError:
		logger.warning(f"Failed to parse cached units JSON for case {case_id}")
		return None


def cache_evidence_summary(case_id: int, evidence_summary: dict[str, Any], db: Session) -> None:
	"""Cache evidence summary for a case."""
	method_version = f"{DISCUSSION_UNIT_METHOD}:{DISCUSSION_UNIT_VERSION}"

	# Check if cache already exists
	existing = db.execute(
		select(DiscussionUnitCache)
		.where(DiscussionUnitCache.case_id == case_id)
		.where(DiscussionUnitCache.method_version == method_version)
	).scalar_one_or_none()

	units_json = json.dumps(evidence_summary, default=str)
	total_units = len(evidence_summary.get("units", []))
	total_subthemes = evidence_summary.get("total_subthemes", 0)

	if existing:
		# Update existing cache
		existing.units_json = units_json
		existing.total_units = total_units
		existing.total_subthemes = total_subthemes
		existing.updated_at = datetime.utcnow()
	else:
		# Create new cache entry
		cache_entry = DiscussionUnitCache(
			case_id=case_id,
			method_version=method_version,
			units_json=units_json,
			total_units=total_units,
			total_subthemes=total_subthemes,
		)
		db.add(cache_entry)

	db.commit()


def compute_case_units(case_id: int, db: Session) -> dict[str, Any] | None:
	"""
	Compute discussion units for a case and cache the result.
	Returns the cached evidence summary.
	"""
	try:
		# Build reader data (which triggers unit computation)
		reader_data = build_case_reader_data(case_id, db)

		if not reader_data.evidence_summary:
			logger.warning(f"No evidence summary generated for case {case_id}")
			return None

		# Convert to dict for caching
		evidence_dict = reader_data.evidence_summary.model_dump()

		# Cache it
		cache_evidence_summary(case_id, evidence_dict, db)

		return evidence_dict
	except Exception as e:
		logger.error(f"Failed to compute units for case {case_id}: {e}")
		return None


def batch_compute_all_units(db: Session, start_case_id: int = 1, end_case_id: int | None = None) -> dict[str, Any]:
	"""
	Batch compute discussion units for all cases in range.

	Args:
		db: Database session
		start_case_id: First case ID to process (default 1)
		end_case_id: Last case ID to process (default: max case ID in database)

	Returns:
		Statistics dict with counts of successes, failures, skipped
	"""
	# Get max case ID if not specified
	if end_case_id is None:
		max_case = db.execute(select(Case.id).order_by(Case.id.desc()).limit(1)).scalar()
		end_case_id = max_case or 1

	stats = {
		"total_cases": end_case_id - start_case_id + 1,
		"processed": 0,
		"successful": 0,
		"failed": 0,
		"skipped": 0,
		"start_time": datetime.utcnow().isoformat(),
	}

	logger.info(f"Starting batch compute for cases {start_case_id}-{end_case_id}")

	for case_id in range(start_case_id, end_case_id + 1):
		# Check if case exists
		case = db.execute(select(Case).where(Case.id == case_id)).scalar_one_or_none()
		if not case:
			stats["skipped"] += 1
			continue

		stats["processed"] += 1

		try:
			result = compute_case_units(case_id, db)
			if result:
				stats["successful"] += 1
			else:
				stats["failed"] += 1
		except Exception as e:
			logger.error(f"Error processing case {case_id}: {e}")
			stats["failed"] += 1

		# Log progress every 50 cases
		if stats["processed"] % 50 == 0:
			logger.info(f"Progress: {stats['processed']}/{stats['total_cases']} cases processed")

	stats["end_time"] = datetime.utcnow().isoformat()
	logger.info(f"Batch compute complete: {stats}")

	return stats


def clear_cache(db: Session, case_id: int | None = None) -> int:
	"""
	Clear cached discussion units.

	Args:
		db: Database session
		case_id: If specified, clear only this case's cache; otherwise clear all

	Returns:
		Number of cache entries deleted
	"""
	if case_id:
		deleted = db.execute(
			select(DiscussionUnitCache).where(DiscussionUnitCache.case_id == case_id)
		).rowcount
		db.query(DiscussionUnitCache).filter(DiscussionUnitCache.case_id == case_id).delete()
	else:
		deleted = db.query(DiscussionUnitCache).delete()

	db.commit()
	logger.info(f"Cleared {deleted} cache entries")

	return deleted
