"""Extract case-to-case citations for RPD/SCC A2AJ cases with per-case timeouts."""

from __future__ import annotations

import argparse
import multiprocessing as mp
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import select

from backend.case_processing import _run_case_citation_layer
from backend.database import Case, SessionLocal

PROCESSED_KEY = "case_citations_processed"
SKIPPED_KEY = "case_citations_skipped"
SKIP_REASON_KEY = "case_citations_skip_reason"


def pending_case_ids() -> list[int]:
    with SessionLocal() as session:
        rows = session.execute(
            select(Case.id, Case.metadata_json)
            .where(Case.source_type == "a2aj_parquet", Case.court.in_(["RPD", "SCC"]))
            .order_by(Case.id)
        ).all()
    return [
        case_id
        for case_id, metadata in rows
        if not (isinstance(metadata, dict) and metadata.get(PROCESSED_KEY) is True)
    ]


def process_case(case_id: int, result_queue: mp.Queue) -> None:
    try:
        with SessionLocal() as session:
            case = session.scalar(select(Case).where(Case.id == case_id))
            if case is None:
                result_queue.put(("error", "case not found"))
                return
            inserted = _run_case_citation_layer(session, case)
            session.commit()
            result_queue.put(("processed", inserted))
    except Exception as exc:  # pragma: no cover - exercised by worker failures
        result_queue.put(("error", f"{type(exc).__name__}: {exc}"))


def mark_case(case_id: int, *, skipped: bool, reason: str | None = None) -> None:
    with SessionLocal() as session:
        case = session.scalar(select(Case).where(Case.id == case_id))
        if case is None:
            return
        metadata = dict(case.metadata_json or {})
        metadata[PROCESSED_KEY] = True
        if skipped:
            metadata[SKIPPED_KEY] = True
            metadata[SKIP_REASON_KEY] = reason or "Case worker did not complete within the configured timeout."
        case.metadata_json = metadata
        session.commit()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-timeout-seconds", type=int, default=120)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.case_timeout_seconds < 1:
        raise SystemExit("--case-timeout-seconds must be at least 1")

    case_ids = pending_case_ids()
    print(f"pending_cases={len(case_ids)}", flush=True)
    processed = skipped = citations = 0
    context = mp.get_context("spawn")

    for case_id in case_ids:
        result_queue = context.Queue()
        worker = context.Process(target=process_case, args=(case_id, result_queue))
        worker.start()
        worker.join(args.case_timeout_seconds)

        if worker.is_alive():
            worker.terminate()
            worker.join()
            mark_case(case_id, skipped=True)
            skipped += 1
            print(f"skipped case_id={case_id} reason=timeout", flush=True)
            continue

        result = result_queue.get() if not result_queue.empty() else ("error", "worker exited without a result")
        if result[0] == "processed":
            processed += 1
            citations += int(result[1])
            if processed % 10 == 0:
                print(
                    f"processed={processed} skipped={skipped} citations_inserted={citations}",
                    flush=True,
                )
        else:
            mark_case(case_id, skipped=True, reason=str(result[1]))
            skipped += 1
            print(f"skipped case_id={case_id} reason={result[1]}", flush=True)

    print(
        f"cases_processed={processed} cases_skipped={skipped} "
        f"case_citations_inserted={citations}",
        flush=True,
    )


if __name__ == "__main__":
    main()