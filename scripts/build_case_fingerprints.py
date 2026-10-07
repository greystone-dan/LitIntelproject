"""Compute stored case fingerprints for cases that have none (batch job; not run by the live site).

Dry run by default: it reports how many cases would be fingerprinted. Use --apply to write.
Cheap and read-mostly: it reads cases.full_text and writes only case_fingerprints.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from backend.batch_safety import lower_process_priority
from backend.case_fingerprint import FINGERPRINT_VERSION
from backend.case_fingerprint_store import rebuild_missing
from backend.batch_safety import make_limited_engine
from backend.database import Case, CaseFingerprintRecord, engine


def main() -> int:
    print("priority:", lower_process_priority())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write fingerprints (default: dry run)")
    parser.add_argument("--limit", type=int, default=None, help="stop after this many cases")
    parser.add_argument("--court", default=None, help="only this court label")
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--workers", type=int, default=1, help="processes computing at once (default 1)")
    parser.add_argument("--max-duty", type=float, default=0.7, help="share of time the job may spend working (0-1)")
    parser.add_argument("--max-chars", type=int, default=250_000, help="read at most this many characters of each decision")
    args = parser.parse_args()

    limited = make_limited_engine(engine.url, statement_timeout_ms=120_000, application_name="ilit-fingerprint-build")
    with Session(limited) as session:
        total = session.scalar(select(func.count(Case.id)).where(Case.full_text.is_not(None)))
        current = session.scalar(
            select(func.count(CaseFingerprintRecord.case_id)).where(CaseFingerprintRecord.version == FINGERPRINT_VERSION)
        )
        by_court = session.execute(
            select(func.upper(Case.court), func.count(Case.id)).where(Case.full_text.is_not(None)).group_by(func.upper(Case.court))
        ).all()
        session.rollback()
        print(f"cases with text: {total}; fingerprints at {FINGERPRINT_VERSION}: {current}")
        print("cases with text by court:", {court: count for court, count in by_court})
        if not args.apply:
            print("dry run: nothing written (use --apply)")
            return 0
        started = time.time()
        done = rebuild_missing(
            session, batch_size=args.batch_size, limit=args.limit, court=args.court,
            max_chars=args.max_chars, workers=args.workers, max_duty=args.max_duty,
        )
        print(f"fingerprinted {done} cases in {time.time() - started:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
