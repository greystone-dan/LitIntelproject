"""Run the complete V2 Pipeline with durable state and per-case quarantine."""

from __future__ import annotations

import argparse
import json
import multiprocessing
import sys
import time
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.case_processing import process_case_in_five_layers
from backend.database import Case, SessionLocal
from scripts.acquire_case_html import acquire_case, apply_result
from scripts.acquire_case_html import ALLOWED_HOSTS
from scripts.chunk_cases import rebuild_case_chunks
from scripts.reacquire_source_html import validate_snapshot, decision_content_url
from scripts.compare_pipeline_case import snapshot_case, compare_snapshots
import requests

STAGES = ("source_html", "chunks", "metadata", "outcome", "citations", "statutes", "tags_v3")
PROCESSING_STAGE_NAMES = {"citations": "case_citations", "statutes": "statutes"}
TEXT_ONLY_DEFAULT_EXCLUDED_COURTS = {"SCC"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _stage_worker(case_id: int, stage: str, timeout: float, retries: int, result_pipe) -> None:
    """Run one mutating stage in an isolated process with its own session."""
    try:
        import requests
        from sqlalchemy import select

        from backend.database import Case, SessionLocal
        from scripts.acquire_case_html import acquire_case, apply_result
        from scripts.chunk_cases import rebuild_case_chunks

        with SessionLocal() as db:
            case = db.scalar(select(Case).where(Case.id == case_id))
            if case is None:
                raise ValueError(f"Case {case_id} not found")
            client = requests.Session()
            client.headers.update({"User-Agent": "AI-CaseLibrary/2.0 (V2 Pipeline)", "Accept": "text/html,application/xhtml+xml;q=0.9"})
            if stage == "source_html":
                result = acquire_case(case, client, timeout, retries)
                if result["status"] != "ready":
                    raise RuntimeError(str(result.get("reason", "source HTML quarantined")))
                apply_result(db, case, result)
            elif stage == "chunks":
                if (case.court or "").upper() != "SCC":
                    case.source_html = None
                rebuild_case_chunks(db, case_ids=[case_id], replace_existing=True)
            else:
                from backend.case_processing import process_case_in_five_layers
                process_case_in_five_layers(db, case_id, stage_order=[PROCESSING_STAGE_NAMES.get(stage, stage)])
            db.commit()
        result_pipe.send({"ok": True})
    except Exception as error:
        result_pipe.send({"ok": False, "error": f"{type(error).__name__}: {error}"})
    finally:
        result_pipe.close()


def _run_stage_with_watchdog(case_id: int, stage: str, timeout: float, retries: int) -> dict[str, object]:
    context = multiprocessing.get_context("spawn")
    parent_pipe, child_pipe = context.Pipe(duplex=False)
    process = context.Process(target=_stage_worker, args=(case_id, stage, timeout, retries, child_pipe))
    process.start()
    child_pipe.close()
    started = time.monotonic()
    result = None
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
        return {"ok": False, "error": f"stage-timeout:{timeout}s", "timed_out": True}
    process.join(5)
    return result


def run(*, limit: int | None, case_ids: list[int] | None, batch_size: int, timeout: float, retries: int, stage_timeout: float, run_dir: Path, dry_run: bool, excluded_courts: set[str] | None = None, text_only: bool = True, detailed_snapshots: bool = False, checkpoint_interval: int = 100) -> dict:
    run_dir.mkdir(parents=True, exist_ok=True)
    state_path = run_dir / "state.json"
    quarantine_path = run_dir / "quarantine.jsonl"
    if state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))
    else:
        state = {"run_id": run_dir.name, "created_at": now(), "updated_at": now(), "status": "running", "selected_stages": list(STAGES), "cases": {}}
    interrupted = False
    try:
        with SessionLocal() as db:
            statement = select(Case).where(Case.full_text.is_not(None), Case.full_text != "").order_by(Case.id)
            if case_ids:
                statement = select(Case).where(Case.id.in_(case_ids)).order_by(Case.id)
            else:
                statement = statement.limit(limit or 1000000)
            cases = db.scalars(statement).yield_per(batch_size)
            for case in cases:
                if (case.court or "").upper() in (excluded_courts or TEXT_ONLY_DEFAULT_EXCLUDED_COURTS):
                    continue
                source_host = urlparse((case.source_url or "").strip()).hostname
                if not source_host or source_host not in ALLOWED_HOSTS:
                    state["cases"].setdefault(str(case.id), {"case_id": case.id, "stages": {}, "errors": []})["stages"]["source_html"] = "excluded_source"
                    continue
                case_state = state["cases"].setdefault(str(case.id), {"case_id": case.id, "stages": {}, "errors": []})
                before_snapshot = snapshot_case(case.id) if detailed_snapshots and not dry_run else None
                for stage in STAGES:
                    if case_state["stages"].get(stage) == "completed":
                        continue
                    if stage == "source_html" and text_only and (case.court or "").upper() != "SCC":
                        case_state["stages"][stage] = "skipped_text_only"
                        continue
                    try:
                        if dry_run:
                            case_state["stages"][stage] = "planned"
                            continue
                        result = _run_stage_with_watchdog(case.id, stage, stage_timeout, retries)
                        if not result.get("ok"):
                            raise RuntimeError(str(result.get("error", "stage failed")))
                        case_state["stages"][stage] = "completed"
                    except Exception as error:
                        db.rollback()
                        detail = {"case_id": case.id, "stage": stage, "error": f"{type(error).__name__}: {error}", "at": now()}
                        case_state["errors"].append(detail)
                        with quarantine_path.open("a", encoding="utf-8") as handle:
                            handle.write(json.dumps(detail) + "\n")
                        case_state["stages"][stage] = "quarantined"
                        break
                if len(state["cases"]) % checkpoint_interval == 0:
                    state["updated_at"] = now()
                    state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
                if detailed_snapshots and not dry_run and not case_state["errors"]:
                    after_snapshot = snapshot_case(case.id)
                    comparison = compare_snapshots(before_snapshot, after_snapshot)
                    report_path = run_dir / f"case-{case.id}-comparison.json"
                    report_path.write_text(json.dumps(comparison, indent=2) + "\n", encoding="utf-8")
                    major_layers = [
                        layer for layer in ("chunks", "citations", "statutes")
                        if comparison.get(layer, {}).get("major_delta")
                    ]
                    if major_layers:
                        detail = {"case_id": case.id, "stage": "quality_gate", "error": f"major_delta:{','.join(major_layers)}", "at": now()}
                        case_state["errors"].append(detail)
                        with quarantine_path.open("a", encoding="utf-8") as handle:
                            handle.write(json.dumps(detail) + "\n")
    except KeyboardInterrupt:
        interrupted = True
    has_errors = any(item["errors"] for item in state["cases"].values())
    state["status"] = "interrupted" if interrupted else "dry_run" if dry_run else "completed_with_quarantine" if has_errors else "completed"
    state["updated_at"] = now()
    state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    return state


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--case-id", type=int, action="append", default=[])
    parser.add_argument("--batch-size", type=int, default=25)
    parser.add_argument("--timeout", type=float, default=30)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--stage-timeout", type=float, default=900, help="Maximum seconds per local case stage")
    parser.add_argument("--run-dir", type=Path, default=Path("data/overnight_runs/v2-pipeline"))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--include-court", action="append", default=[], help="Court codes to include; SCC remains excluded unless explicitly selected")
    parser.add_argument("--allow-scc", action="store_true", help="Allow SCC in this run; intended only for the separate SCC path")
    parser.add_argument("--detailed-snapshots", action="store_true", help="Write per-case before/after reports; disabled for bulk runs")
    args = parser.parse_args()
    if args.batch_size < 1 or args.timeout <= 0 or args.retries < 1:
        raise SystemExit("batch-size, timeout, and retries must be positive")
    if args.stage_timeout <= 0:
        raise SystemExit("stage-timeout must be positive")
    excluded = set() if args.allow_scc else TEXT_ONLY_DEFAULT_EXCLUDED_COURTS
    state = run(limit=args.limit, case_ids=sorted(set(args.case_id)), batch_size=args.batch_size, timeout=args.timeout, retries=args.retries, stage_timeout=args.stage_timeout, run_dir=args.run_dir, dry_run=args.dry_run, excluded_courts=excluded, detailed_snapshots=args.detailed_snapshots)
    completed = sum(all(value == "completed" for value in item["stages"].values()) for item in state["cases"].values())
    quarantined = sum(bool(item["errors"]) for item in state["cases"].values())
    print(f"status={state['status']} cases={len(state['cases'])} complete={completed} quarantined={quarantined} embeddings=False")


if __name__ == "__main__":
    main()
