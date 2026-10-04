"""Utilities for statute versioning and decision-to-statute-version linking."""

from datetime import date
import logging
from sqlalchemy.orm import Session
from sqlalchemy import and_

from backend.database import Statute, StatuteVersion, StatuteSection, Case, StatuteReference

logger = logging.getLogger(__name__)


def find_statute_version_at_date(
    db: Session, instrument_key: str, decision_date: date | None
) -> StatuteVersion | None:
    """
    Find the statute version in force on a given decision date.

    Args:
        db: Database session
        instrument_key: Statute code (e.g., "IRPA", "IRPR")
        decision_date: Decision date to match against in_force_date

    Returns:
        StatuteVersion in effect on that date, or None if not found
    """
    if not decision_date:
        return None

    try:
        statute = db.query(Statute).filter(Statute.instrument_key == instrument_key).first()
        if not statute:
            return None

        version = (
            db.query(StatuteVersion)
            .filter(
                StatuteVersion.statute_id == statute.id,
                StatuteVersion.in_force_date <= decision_date,
            )
            .order_by(StatuteVersion.in_force_date.desc())
            .first()
        )

        return version
    except Exception as e:
        logger.warning(f"Error finding statute version for {instrument_key} at {decision_date}: {e}")
        return None


def get_statute_version_label(statute_version: StatuteVersion | None) -> str:
    """Generate a label for statute version display."""
    if not statute_version:
        return "Version unknown"
    return f"In force {statute_version.in_force_date.strftime('%Y-%m-%d')}"


def link_statute_reference_to_version(
    db: Session, statute_ref, case_date: date | None
) -> bool:
    """
    Link a statute reference to the appropriate statute version based on case date.

    Args:
        db: Database session
        statute_ref: StatuteReference object with instrument_key set
        case_date: Date of the decision

    Returns:
        True if successfully linked, False otherwise
    """
    if not statute_ref.instrument_key or not case_date:
        return False

    try:
        version = find_statute_version_at_date(db, statute_ref.instrument_key, case_date)
        if version:
            statute_ref.statute_version_id = version.id
            return True
        return False
    except Exception as e:
        logger.warning(f"Error linking statute reference: {e}")
        return False


def link_case_statute_references_to_versions(db: Session, case_id: int) -> int:
    """
    Link all statute references in a case to their appropriate statute versions.

    Args:
        db: Database session
        case_id: ID of the case

    Returns:
        Number of references successfully linked
    """
    try:
        case = db.query(Case).filter(Case.id == case_id).first()
        if not case or not case.date:
            return 0

        linked_count = 0
        for statute_ref in case.statute_references:
            if link_statute_reference_to_version(db, statute_ref, case.date):
                linked_count += 1

        if linked_count > 0:
            db.commit()
            logger.info(f"Linked {linked_count} statute references for case {case_id}")

        return linked_count
    except Exception as e:
        logger.error(f"Error linking case references: {e}")
        db.rollback()
        return 0


def batch_link_statute_references(db: Session, batch_size: int = 100) -> int:
    """
    Link statute references to versions for all cases that have unlinked references.

    Args:
        db: Database session
        batch_size: Number of cases to process per batch

    Returns:
        Total number of references linked
    """
    try:
        # Find cases with statute references that have no statute_version_id
        cases_with_unlinked = db.query(Case.id).filter(
            Case.id.in_(
                db.query(StatuteReference.source_case_id).filter(
                    and_(
                        StatuteReference.statute_version_id.is_(None),
                        StatuteReference.instrument_key.isnot(None),
                    )
                ).distinct()
            )
        ).limit(batch_size)

        total_linked = 0
        for case_row in cases_with_unlinked:
            case_id = case_row[0]
            linked = link_case_statute_references_to_versions(db, case_id)
            total_linked += linked

        logger.info(f"Batch linked {total_linked} statute references across {batch_size} cases")
        return total_linked
    except Exception as e:
        logger.error(f"Error in batch linking: {e}")
        db.rollback()
        return 0
