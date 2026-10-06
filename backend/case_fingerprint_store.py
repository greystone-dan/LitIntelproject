"""Stored case fingerprints: compute at ingest/batch time, read back into a similarity index.

Nothing here is called by the live site. Fingerprints are computed from the stored decision text
only (no network, no model), so they can be rebuilt any time and a version bump simply reselects
every row.
"""

from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from .case_fingerprint import FINGERPRINT_VERSION, CaseFingerprint, FingerprintIndex, compute_fingerprint
from .database import Case, CaseFingerprintRecord


def _record_to_fingerprint(record: CaseFingerprintRecord) -> CaseFingerprint:
    return CaseFingerprint(
        version=record.version,
        terms=dict(record.terms or {}),
        authorities=dict(record.authorities or {}),
        length=record.text_length or 0,
        role_chars=dict(record.role_chars or {}),
    )


def store_fingerprint(session: Session, case_id: int, fingerprint: CaseFingerprint) -> CaseFingerprintRecord:
    """Insert or replace the stored fingerprint for one case (caller commits)."""
    record = session.get(CaseFingerprintRecord, case_id)
    if record is None:
        record = CaseFingerprintRecord(case_id=case_id)
        session.add(record)
    record.version = fingerprint.version
    record.terms = fingerprint.terms
    record.authorities = fingerprint.authorities
    record.role_chars = fingerprint.role_chars
    record.text_length = fingerprint.length
    record.computed_at = datetime.now(timezone.utc)
    return record


def rebuild_case_fingerprint(session: Session, case: Case) -> CaseFingerprintRecord:
    """Compute and store one case's fingerprint from its full text."""
    return store_fingerprint(session, case.id, compute_fingerprint(case.full_text, own_citation=case.citation))


def rebuild_missing(session: Session, batch_size: int = 200, limit: int | None = None, court: str | None = None) -> int:
    """Fingerprint every case that has none (or an older version); commits per batch. Returns the count."""
    done = 0
    while limit is None or done < limit:
        stmt = (
            select(Case)
            .outerjoin(CaseFingerprintRecord, CaseFingerprintRecord.case_id == Case.id)
            .where(Case.full_text.is_not(None))
            .where((CaseFingerprintRecord.case_id.is_(None)) | (CaseFingerprintRecord.version != FINGERPRINT_VERSION))
            .order_by(Case.id)
            .limit(min(batch_size, limit - done) if limit is not None else batch_size)
        )
        if court:
            stmt = stmt.where(Case.court == court)
        cases = list(session.scalars(stmt))
        if not cases:
            break
        for case in cases:
            rebuild_case_fingerprint(session, case)
        session.commit()
        done += len(cases)
    return done


def load_index(session: Session, court: str | None = None) -> FingerprintIndex:
    """Read every current-version fingerprint into an in-memory index (optionally one court)."""
    stmt = select(CaseFingerprintRecord).where(CaseFingerprintRecord.version == FINGERPRINT_VERSION)
    if court:
        stmt = stmt.join(Case, Case.id == CaseFingerprintRecord.case_id).where(Case.court == court)
    stmt = stmt.order_by(CaseFingerprintRecord.case_id)
    return FingerprintIndex((record.case_id, _record_to_fingerprint(record)) for record in session.scalars(stmt))
