"""Run the SCC-specific text-only enrichment pipeline."""

from __future__ import annotations

import argparse
import json
import multiprocessing
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.case_processing import process_case_in_five_layers  # noqa: E402
from backend.database import Case, SessionLocal  # noqa: E402

STAGE_ORDER = ("full_case", "heading_chunks", "metadata", "outcome", "case_citations", "statutes", "tags_v3")


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _case_worker(case_id: int, result_pipe) -> None:
    try:
        from backend.case_processing import process_case_in_five_layers
        from backend.database import SessionLocal

        with SessionLocal() as db:
            report = process_case_in_five_layers(db, case_id, stage_order=list(STAGE_ORDER))
            db.commit()
        result_pipe.send({"status": "completed", "report": report})
    except Exception as error:
        result_pipe.send({"status": "quarantined", "error": f"{type(error).__name__}: {error}"})
    finally:
        result_pipe.close()


def _run_case_with_watchdog(case_id: int, timeout: float) -> dict[str, object]:
    context = multiprocessing.get_context("spawn")
    parent_pipe, child_pipe = context.Pipe(duplex=False)
    process = context.Process(target=_case_worker, args=(case_id, child_pipe))
    process.start()
    child_pipe.close()
    started = time.monotonic()
    result: dict[str, object] | None = None
    while time.monotonic() - started < timeout:
        if parent_pipe.poll(0.25):
            result = parent_pipe.recv()
            break
        if not process.is_alive():
            break
    if result is None:
        if process.is_alive():
            process.terminate()
        process.join(5)
        return {"status": "quarantined", "error": f"stage-timeout:{timeout}s", "timed_out": True}
    process.join(5)
    return result


def run(*, limit: int, batch_size: int, run_dir: Path, start_after_id: int = 0, case_ids: list[int] | None = None, from_date: date | None = None, resume: bool = False, case_timeout: float = 600, dry_run: bool = False) -> dict[str, object]:
    if limit < 1 or batch_size < 1:
        raise ValueError("limit and batch-size must be positive")
    if case_timeout <= 0:
        raise ValueError("case-timeout must be positive")
    run_dir.mkdir(parents=True, exist_ok=True)
    state_path = run_dir / "state.json"
    if resume and state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))
        state["status"] = "running"
    else:
        state = {"status": "running", "created_at": now(), "updated_at": now(), "court": "SCC", "from_date": from_date.isoformat() if from_date else None, "stages": list(STAGE_ORDER), "cases": {}}
    processed = 0
    started = time.monotonic()
    with SessionLocal() as db:
        if case_ids:
            statement = select(Case).where(Case.id.in_(sorted(set(case_ids))), Case.court == "SCC").order_by(Case.id)
        else:
            statement = (
                select(Case)
                .where(Case.id > start_after_id, Case.court == "SCC", Case.full_text.is_not(None), Case.full_text != "")
                .order_by(Case.id)
                .limit(limit)
            )
        if from_date:
            statement = statement.where(Case.date >= from_date)
        for case in db.scalars(statement).yield_per(batch_size):
            prior = state["cases"].get(str(case.id))
            if resume and prior and prior.get("status") == "completed":
                continue
            if dry_run:
                state["cases"][str(case.id)] = {"status": "planned"}
            else:
                try:
                    result = _run_case_with_watchdog(case.id, case_timeout)
                    state["cases"][str(case.id)] = result
                    if result.get("status") == "quarantined":
                        db.rollback()
                except Exception as error:
                    db.rollback()
                    state["cases"][str(case.id)] = {"status": "quarantined", "error": f"{type(error).__name__}: {error}"}
            processed += 1
            if processed % batch_size == 0:
                if not dry_run:
                    db.commit()
                state["updated_at"] = now()
                state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
                print(f"processed={processed} elapsed_seconds={time.monotonic() - started:.1f}", flush=True)
        if not dry_run:
            db.commit()
    state["status"] = "dry_run" if dry_run else "completed"
    state["updated_at"] = now()
    state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    completed = sum(item.get("status") == "completed" for item in state["cases"].values())
    quarantined = sum(item.get("status") == "quarantined" for item in state["cases"].values())
    print(f"status={state['status']} processed={processed} completed={completed} quarantined={quarantined} elapsed_seconds={time.monotonic() - started:.1f}")
    return state


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=1000000, help="Maximum selected cases; date/case filters still apply")
    parser.add_argument("--batch-size", type=int, default=25)
    parser.add_argument("--start-after-id", type=int, default=0)
    parser.add_argument("--case-id", type=int, action="append", default=[])
    parser.add_argument("--from-date", type=date.fromisoformat, help="Include cases on or after YYYY-MM-DD")
    parser.add_argument("--run-dir", type=Path, default=Path("data/overnight_runs/scc-text-only"))
    parser.add_argument("--resume", action="store_true", help="Resume from an existing state file and skip completed cases")
    parser.add_argument("--case-timeout", type=float, default=600, help="Quarantine a case after this many seconds")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run(limit=args.limit, batch_size=args.batch_size, start_after_id=args.start_after_id, case_ids=args.case_id, from_date=args.from_date, resume=args.resume, case_timeout=args.case_timeout, run_dir=args.run_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
