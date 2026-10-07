"""Read-only "similar cases" for the reader: same subject and shares authorities, from stored fingerprints.

No model, no network, nothing computed from the decision text at request time. The stored
``case_fingerprints`` rows are read into one in-memory index the first time they are needed and
kept for a while; a case with no stored fingerprint (or an empty table) simply returns nothing.
"""

from __future__ import annotations

import threading
import time
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .case_fingerprint import FINGERPRINT_VERSION, FingerprintIndex
from .case_fingerprint_store import load_index
from .database import Case, CaseFingerprintRecord, get_db

router = APIRouter()

LIST_SIZE = 8
RECHECK_SECONDS = 600
MIN_SUBJECT_SCORE = 0.15
MIN_AUTHORITY_SCORE = 0.10

_lock = threading.Lock()
_cache: dict[str, Any] = {"stamp": None, "index": None, "checked": 0.0}


def _stamp(db: Session) -> tuple[int, Any]:
    row = db.execute(
        select(func.count(CaseFingerprintRecord.case_id), func.max(CaseFingerprintRecord.computed_at)).where(
            CaseFingerprintRecord.version == FINGERPRINT_VERSION
        )
    ).one()
    db.rollback()  # no transaction left open while the index is built
    return int(row[0] or 0), row[1]


def get_index(db: Session) -> FingerprintIndex | None:
    """The shared index, rebuilt only when the stored fingerprints changed (checked every few minutes)."""
    now = time.time()
    with _lock:
        if _cache["checked"] and now - _cache["checked"] < RECHECK_SECONDS:
            return _cache["index"]
        stamp = _stamp(db)
        if stamp != _cache["stamp"]:
            _cache["index"] = load_index(db) if stamp[0] else None
            db.rollback()
            _cache["stamp"] = stamp
        _cache["checked"] = now
        return _cache["index"]


def reset_cache() -> None:
    with _lock:
        _cache.update(stamp=None, index=None, checked=0.0)


def _label(term: str) -> str:
    return term.split(":", 1)[1] if term[:2] in ("t:", "s:") else term


def build_similar_cases(db: Session, case_id: int, index: FingerprintIndex | None = None) -> dict[str, Any]:
    index = index if index is not None else get_index(db)
    empty = {"available": False, "case_id": case_id, "similar": [], "shares_authorities": []}
    if index is None or not index.has(case_id):
        return empty
    subject = index.similar_by_subject(case_id, k=LIST_SIZE, min_score=MIN_SUBJECT_SCORE)
    shared = index.shares_authorities(case_id, k=LIST_SIZE, min_score=MIN_AUTHORITY_SCORE)
    ids = {other for other, _ in subject} | {other for other, _ in shared}
    cases = {
        row.id: row
        for row in db.execute(select(Case.id, Case.title, Case.citation, Case.court, Case.date).where(Case.id.in_(ids))).all()
    } if ids else {}
    db.rollback()

    def item(other: int, score: float, why: list[str] | None = None) -> dict[str, Any] | None:
        row = cases.get(other)
        if row is None:
            return None
        return {
            "case_id": other,
            "title": row.title,
            "citation": row.citation,
            "court": row.court,
            "date": row.date.isoformat() if row.date else None,
            "score": round(float(score), 3),
            "shared": why or [],
        }

    similar = [
        item(other, score, [_label(term) for term, _ in index.explain_subject(case_id, other, 3)]) for other, score in subject
    ]
    authorities = [item(other, score) for other, score in shared]
    return {
        "available": True,
        "case_id": case_id,
        "similar": [row for row in similar if row],
        "shares_authorities": [row for row in authorities if row],
    }


@router.get("/api/cases/{case_id}/similar-cases", include_in_schema=False)
def similar_cases(case_id: int, db: Session = Depends(get_db)) -> dict[str, Any]:
    return build_similar_cases(db, case_id)
