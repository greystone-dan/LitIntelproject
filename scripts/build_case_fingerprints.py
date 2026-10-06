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

from backend.case_fingerprint import FINGERPRINT_VERSION
from backend.case_fingerprint_store import rebuild_missing
from backend.database import Case, CaseFingerprintRecord, SessionLocal


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write fingerprints (default: dry run)")
    parser.add_argument("--limit", type=int, default=None, help="stop after this many cases")
    parser.add_argument("--court", default=None, help="only this court label")
    parser.add_argument("--batch-size", type=int, default=200)
    args = parser.parse_args()

    with SessionLocal() as session:
        total = session.scalar(select(func.count(Case.id)).where(Case.full_text.is_not(None)))
        current = session.scalar(
            select(func.count(CaseFingerprintRecord.case_id)).where(CaseFingerprintRecord.version == FINGERPRINT_VERSION)
        )
        print(f"cases with text: {total}; fingerprints at {FINGERPRINT_VERSION}: {current}")
        if not args.apply:
            print("dry run: nothing written (use --apply)")
            return 0
        started = time.time()
        done = rebuild_missing(session, batch_size=args.batch_size, limit=args.limit, court=args.court)
        print(f"fingerprinted {done} cases in {time.time() - started:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
