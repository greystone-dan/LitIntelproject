"""Which citation table the read paths use: the live one (default) or the refined side table.

``CITATIONS_SOURCE=legacy`` (default) changes nothing. ``CITATIONS_SOURCE=refined`` reads refined rows for every source
decision that has a finished refinement status and falls back to the live rows for all other decisions, so a partly
refined library never loses citations.
"""

from __future__ import annotations

import os

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Citation, CitationRefined, CitationRefineStatus

VALID_CITATION_SOURCES = frozenset({"legacy", "refined"})


def citations_source() -> str:
	value = os.getenv("CITATIONS_SOURCE", "legacy").strip().lower() or "legacy"
	if value not in VALID_CITATION_SOURCES:
		raise ValueError("CITATIONS_SOURCE must be one of: legacy, refined")
	return value


def _refined_source_ids():
	return select(CitationRefineStatus.source_case_id).where(CitationRefineStatus.status == "done")


def outgoing_citations(db: Session, case_id: int) -> list:
	if citations_source() == "refined" and db.scalar(select(CitationRefineStatus.source_case_id).where(CitationRefineStatus.source_case_id == case_id, CitationRefineStatus.status == "done")) is not None:
		return list(db.scalars(select(CitationRefined).where(CitationRefined.source_case_id == case_id).order_by(CitationRefined.id)))
	return list(db.scalars(select(Citation).where(Citation.source_case_id == case_id).order_by(Citation.id)))


def incoming_citations(db: Session, case_id: int) -> list:
	if citations_source() != "refined":
		return list(db.scalars(select(Citation).where(Citation.target_case_id == case_id).order_by(Citation.id)))
	refined = list(db.scalars(select(CitationRefined).where(CitationRefined.target_case_id == case_id).order_by(CitationRefined.id)))
	legacy = list(
		db.scalars(
			select(Citation)
			.where(Citation.target_case_id == case_id, Citation.source_case_id.not_in(_refined_source_ids()))
			.order_by(Citation.id)
		)
	)
	return [*refined, *legacy]
