"""Apply the current metadata and outcome extractor to every case with full text."""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal
from backend.metadata import extract_case_metadata


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=500)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.batch_size < 1:
        raise SystemExit("--batch-size must be at least 1")

    scanned = changed = outcome_recovered = government_recovered = errors = 0
    started = time.monotonic()
    with SessionLocal() as session:
        cases = session.scalars(
            select(Case)
            .where(Case.full_text.is_not(None), Case.full_text != "")
            .order_by(Case.id)
        ).yield_per(args.batch_size)
        for case in cases:
            scanned += 1
            try:
                before = dict((case.metadata_json or {}).get("reader_extracted") or {})
                extracted = extract_case_metadata(case.full_text or case.summary or "")
                payload = dict(case.metadata_json or {})
                if payload.get("reader_extracted") != extracted:
                    payload["reader_extracted"] = extracted
                    case.metadata_json = payload
                    session.add(case)
                    changed += 1
                if not before.get("decision outcome") and extracted.get("decision outcome"):
                    outcome_recovered += 1
                if extracted.get("government outcome") in {"won", "lost"} and before.get("government outcome") not in {"won", "lost"}:
                    government_recovered += 1
            except Exception as error:
                errors += 1
                session.rollback()
                print(f"case_error id={case.id} error={type(error).__name__}: {error}", flush=True)
            if scanned % args.batch_size == 0:
                session.commit()
                elapsed = time.monotonic() - started
                print(
                    f"progress scanned={scanned} changed={changed} "
                    f"decision_outcomes_recovered={outcome_recovered} "
                    f"government_outcomes_recovered={government_recovered} "
                    f"errors={errors} elapsed_seconds={elapsed:.1f}",
                    flush=True,
                )
        session.commit()
    print(
        f"finished scanned={scanned} changed={changed} "
        f"decision_outcomes_recovered={outcome_recovered} "
        f"government_outcomes_recovered={government_recovered} errors={errors}",
        flush=True,
    )


if __name__ == "__main__":
    main()
