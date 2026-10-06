"""Stored case fingerprints: compute at ingest/batch time, read back into a similarity index.

Nothing here is called by the live site. Fingerprints are computed from the stored decision text
only (no network, no model), so they can be rebuilt any time and a version bump simply reselects
every row.
"""

from __future__ import annotations

import time
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .batch_safety import throttle_sleep
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


COURT_LABELS = {
    "FC": ("FC", "FEDERAL COURT"),
    "FCA": ("FCA", "FEDERAL COURT OF APPEAL"),
    "SCC": ("SCC", "SUPREME COURT OF CANADA"),
}


def _compute_job(job: tuple[int, str | None, str | None]) -> tuple[int, CaseFingerprint, float]:
    """Pool worker: one case's fingerprint and the seconds it took (module level so it can be pickled)."""
    case_id, citation, text = job
    started = time.time()
    return case_id, compute_fingerprint(text, own_citation=citation), time.time() - started


def rebuild_missing(
    session: Session,
    batch_size: int = 200,
    limit: int | None = None,
    court: str | None = None,
    max_chars: int = 250_000,
    workers: int = 1,
    max_duty: float | None = None,
) -> int:
    """Fingerprint every case that has none (or an older version); commits per batch. Returns the count.

    Safe for a long run against the live database: each batch is read in one short query (id,
    citation and the first ``max_chars`` of the text only, never the whole row), the transaction is
    ended before any computing so it never sits idle, and results are written in one short
    transaction. ``workers`` > 1 computes in that many processes; ``max_duty`` (0-1) rests between
    batches so the job never works more than that share of the time.
    """
    pool = ProcessPoolExecutor(max_workers=workers) if workers > 1 else None
    done = 0
    try:
        while limit is None or done < limit:
            stmt = (
                select(Case.id, Case.citation, func.substr(Case.full_text, 1, max_chars))
                .outerjoin(CaseFingerprintRecord, CaseFingerprintRecord.case_id == Case.id)
                .where(Case.full_text.is_not(None))
                .where((CaseFingerprintRecord.case_id.is_(None)) | (CaseFingerprintRecord.version != FINGERPRINT_VERSION))
                .order_by(Case.id)
                .limit(min(batch_size, limit - done) if limit is not None else batch_size)
            )
            if court:
                stmt = stmt.where(func.upper(Case.court).in_(COURT_LABELS.get(court.upper(), (court.upper(),))))
            jobs = [tuple(row) for row in session.execute(stmt)]
            session.rollback()  # no open transaction while computing
            if not jobs:
                break
            batch_started = time.time()
            results = list(pool.map(_compute_job, jobs, chunksize=1)) if pool else [_compute_job(job) for job in jobs]
            for case_id, fingerprint, _seconds in results:
                store_fingerprint(session, case_id, fingerprint)
            session.commit()
            done += len(jobs)
            if max_duty and 0 < max_duty < 1:
                time.sleep(throttle_sleep(time.time() - batch_started, 0.0, max_duty))
    finally:
        if pool:
            pool.shutdown()
    return done


def load_index(session: Session, court: str | None = None) -> FingerprintIndex:
    """Read every current-version fingerprint into an in-memory index (optionally one court)."""
    stmt = select(CaseFingerprintRecord).where(CaseFingerprintRecord.version == FINGERPRINT_VERSION)
    if court:
        stmt = stmt.join(Case, Case.id == CaseFingerprintRecord.case_id).where(Case.court == court)
    stmt = stmt.order_by(CaseFingerprintRecord.case_id)
    return FingerprintIndex((record.case_id, _record_to_fingerprint(record)) for record in session.scalars(stmt))
