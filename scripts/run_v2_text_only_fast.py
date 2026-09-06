"""Fast text-only V2 Pipeline runner for non-SCC cases."""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.case_processing import process_case_in_five_layers  # noqa: E402
from backend.database import Case, SessionLocal  # noqa: E402
from scripts.acquire_case_html import ALLOWED_HOSTS  # noqa: E402

STAGE_ORDER = ("full_case", "heading_chunks", "metadata", "outcome", "case_citations", "statutes", "tags_v3")


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def run(*, limit: int, batch_size: int, run_dir: Path, start_after_id: int = 0, dry_run: bool = False) -> dict[str, object]:
    if limit < 1 or batch_size < 1:
        raise ValueError("limit and batch-size must be positive")
    run_dir.mkdir(parents=True, exist_ok=True)
    state_path = run_dir / "state.json"
    state = {"status": "running", "created_at": now(), "updated_at": now(), "stages": list(STAGE_ORDER), "cases": {}}
    processed = 0
    started = time.monotonic()
    with SessionLocal() as db:
        statement = (
            select(Case)
            .where(
                Case.id > start_after_id,
                Case.full_text.is_not(None),
                Case.full_text != "",
                Case.court != "SCC",
            )
            .order_by(Case.id)
            .limit(limit)
        )
        for case in db.scalars(statement).yield_per(batch_size):
            host = urlparse((case.source_url or "").strip()).hostname
            if not host or host not in ALLOWED_HOSTS:
                state["cases"][str(case.id)] = {"status": "excluded_source", "source_host": host}
                processed += 1
                continue
            if dry_run:
                state["cases"][str(case.id)] = {"status": "planned"}
            else:
                try:
                    report = process_case_in_five_layers(db, case.id, stage_order=list(STAGE_ORDER))
                    state["cases"][str(case.id)] = {"status": "completed", "report": report}
                except Exception as error:
                    db.rollback()
                    state["cases"][str(case.id)] = {"status": "quarantined", "error": f"{type(error).__name__}: {error}"}
            processed += 1
            if processed % batch_size == 0:
                if not dry_run:
                    db.commit()
                state["updated_at"] = now()
                state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
                print(f"processed={processed} elapsed_seconds={time.monotonic()-started:.1f}", flush=True)
        if not dry_run:
            db.commit()
    state["status"] = "dry_run" if dry_run else "completed"
    state["updated_at"] = now()
    state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    completed = sum(item.get("status") == "completed" for item in state["cases"].values())
    quarantined = sum(item.get("status") == "quarantined" for item in state["cases"].values())
    excluded = sum(item.get("status") == "excluded_source" for item in state["cases"].values())
    print(f"status={state['status']} processed={processed} completed={completed} quarantined={quarantined} excluded={excluded} elapsed_seconds={time.monotonic()-started:.1f}")
    return state


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=500)
    parser.add_argument("--batch-size", type=int, default=50)
    parser.add_argument("--start-after-id", type=int, default=0)
    parser.add_argument("--run-dir", type=Path, default=Path("data/eval/reports/v2-fast-benchmark"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run(limit=args.limit, batch_size=args.batch_size, start_after_id=args.start_after_id, run_dir=args.run_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
