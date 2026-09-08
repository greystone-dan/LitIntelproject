"""Run a bounded citation rebuild in 10-case progress batches and print compact extraction counts."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from sqlalchemy import func, select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, Citation, SessionLocal


def _select_case_ids(*, case_ids: list[int] | None, limit: int | None, offset: int = 0) -> list[int]:
    if case_ids:
        return sorted(set(case_ids))
    if limit is None:
        raise ValueError("--limit is required unless --case-id is provided")
    with SessionLocal() as session:
        return list(
            session.scalars(
                select(Case.id)
                .where(Case.full_text.is_not(None), Case.full_text != "")
                .order_by(Case.id)
                .offset(offset)
                .limit(limit)
            ).all()
        )


def _batch_case_ids(case_ids: list[int], batch_size: int) -> list[list[int]]:
    if batch_size < 1:
        raise ValueError("--batch-size must be at least 1")
    return [case_ids[i : i + batch_size] for i in range(0, len(case_ids), batch_size)]


def _count_batch_citations(case_ids: list[int]) -> int:
    with SessionLocal() as session:
        total = session.scalar(
            select(func.count(Citation.id)).where(Citation.source_case_id.in_(case_ids))
        )
        return int(total or 0)


def _write_skipped_batch(run_dir: Path, batch_number: int, case_ids: list[int], reason: str) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)
    skip_path = run_dir / "skipped_batches.jsonl"
    entry = {
        "batch_number": batch_number,
        "case_ids": case_ids,
        "reason": reason,
    }
    with skip_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=True) + "\n")


def run_progress_batches(*, case_ids: list[int], batch_size: int, run_dir: Path, apply: bool, timeout_seconds: int) -> None:
    batches = _batch_case_ids(case_ids, batch_size)
    processed_total = 0
    citation_total = 0
    for batch_index, batch in enumerate(batches, start=1):
        batch_dir = run_dir / f"batch-{batch_index:02d}"
        command = [
            sys.executable,
            str(PROJECT_ROOT / "scripts" / "rebuild_citations_controlled.py"),
        ]
        for case_id in batch:
            command.extend(["--case-id", str(case_id)])
        command.extend([
            "--limit",
            str(len(batch)),
            "--run-dir",
            str(batch_dir),
        ])
        if apply:
            command.extend(["--apply", "--confirm-citation-rebuild"])

        try:
            result = subprocess.run(command, cwd=PROJECT_ROOT, capture_output=True, text=True, timeout=timeout_seconds)
        except subprocess.TimeoutExpired:
            _write_skipped_batch(run_dir, batch_index, batch, "timeout")
            print(f"Cases Processed [{processed_total}] - Citations Extracted [{citation_total}] - Batch {batch_index} Skipped (timeout)", flush=True)
            continue

        if result.returncode != 0:
            error_tail = "\n".join(result.stderr.strip().splitlines()[-10:])
            reason = f"exit_code={result.returncode}; stderr={error_tail}"
            _write_skipped_batch(run_dir, batch_index, batch, reason)
            print(f"Cases Processed [{processed_total}] - Citations Extracted [{citation_total}] - Batch {batch_index} Skipped (exit {result.returncode})", flush=True)
            continue

        batch_citations = _count_batch_citations(batch)
        processed_total += len(batch)
        citation_total += batch_citations
        print(f"Cases Processed [{processed_total}] - Citations Extracted [{citation_total}]", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-id", type=int, action="append", default=[], help="Explicit case ID. Repeat for a bounded cohort.")
    parser.add_argument("--all", action="store_true", help="Select all text-bearing cases up to --limit.")
    parser.add_argument("--limit", type=int, help="Max number of text-bearing cases to include when --all is used.")
    parser.add_argument("--offset", type=int, default=0, help="Skip this many text-bearing cases before applying --limit.")
    parser.add_argument("--batch-size", type=int, default=10, help="Cases per progress batch; default 10.")
    parser.add_argument("--timeout-seconds", type=int, default=240, help="Per-batch timeout; default 240 seconds (4 minutes).")
    parser.add_argument("--run-dir", type=Path, default=PROJECT_ROOT / "data" / "overnight_runs" / "citation-progress-run")
    parser.add_argument("--dry-run", action="store_true", help="Not currently used; batches are explicit apply mode by default.")
    parser.add_argument("--apply", action="store_true", help="Run the extraction-only case rebuild for each batch.")
    parser.add_argument("--confirm-citation-rebuild", action="store_true", help="Required when --apply is used.")
    args = parser.parse_args()

    if args.dry_run and args.apply:
        raise SystemExit("--dry-run and --apply cannot be combined")
    if not args.apply and not args.dry_run:
        args.apply = True
    if args.apply and not args.confirm_citation_rebuild:
        raise SystemExit("--apply requires --confirm-citation-rebuild")

    if args.case_id and args.all:
        raise SystemExit("--case-id and --all cannot be combined")

    selected_ids = args.case_id if args.case_id else []
    if not selected_ids and args.all:
        if args.limit is None:
            raise SystemExit("--limit is required with --all")
        selected_ids = _select_case_ids(case_ids=None, limit=args.limit, offset=args.offset)
    elif not selected_ids:
        if args.limit is None:
            raise SystemExit("Provide --case-id or --all with --limit")
        selected_ids = _select_case_ids(case_ids=None, limit=args.limit, offset=args.offset)

    run_progress_batches(
        case_ids=selected_ids,
        batch_size=args.batch_size,
        run_dir=args.run_dir,
        apply=args.apply,
        timeout_seconds=args.timeout_seconds,
    )


if __name__ == "__main__":
    main()
