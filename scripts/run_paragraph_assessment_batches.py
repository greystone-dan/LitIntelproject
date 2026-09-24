"""Run paragraph-level assessments in visible, resumable batches."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime, timezone

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.discussion_units_ledger import read_ledger, record_case


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _write_progress(run_dir: Path, case_ids: list[int], stage: int, total_stages: int) -> None:
    ledger = read_ledger(run_dir / "ledger.json")
    rows = []
    for case_id in case_ids:
        entry = ledger["cases"].get(str(case_id), {})
        status = entry.get("status", "pending")
        cost = entry.get("spent_usd", "")
        duration = entry.get("elapsed_seconds", "")
        review = f"reviews/case_{case_id}_paragraph_assessment.md"
        review_cell = f"[review]({review})" if status == "complete" else ""
        rows.append(f"| {case_id} | {status} | {entry.get('unit_count', '')} | {cost} | {duration} | {review_cell} |")
    complete = sum(ledger["cases"].get(str(case_id), {}).get("status") == "complete" for case_id in case_ids)
    failed = sum(ledger["cases"].get(str(case_id), {}).get("status") == "failed" for case_id in case_ids)
    started = sum(ledger["cases"].get(str(case_id), {}).get("status") == "started" for case_id in case_ids)
    total_cost = sum(float(ledger["cases"].get(str(case_id), {}).get("spent_usd", 0) or 0) for case_id in case_ids)
    lines = [
        "# Paragraph-level 300-case run progress",
        "",
        f"Last updated: `{_now()}`",
        f"Current stage: `{stage}/{total_stages}`",
        f"Progress: `{complete}/{len(case_ids)}` complete, `{failed}` failed, `{started}` active",
        f"Estimated spend recorded: `${total_cost:.6f}`",
        "",
        "Generated outputs are local and report-only. No database writes are performed.",
        "",
        "| Case | Status | Paragraph assessments | Cost (USD) | Elapsed (s) | Review |",
        "| ---: | --- | ---: | ---: | ---: | --- |",
        *rows,
        "",
    ]
    (run_dir / "progress.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=Path("data/eval/llm_discussion_units_pilot/core_300_run/reports"))
    parser.add_argument("--run-dir", type=Path, default=Path("data/eval/llm_discussion_units_pilot/paragraph_level_300_run"))
    parser.add_argument("--batch-size", type=int, default=25)
    parser.add_argument("--budget-usd", type=float, default=1.0)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--case-ids", help="Comma-separated case IDs to process instead of the full cohort")
    parser.add_argument("--exclude-case-ids", help="Comma-separated case IDs to leave untouched")
    args = parser.parse_args()
    if args.batch_size < 1:
        parser.error("--batch-size must be positive")
    if args.workers < 1:
        parser.error("--workers must be positive")
    reports = sorted(args.source_dir.glob("case_*_deterministic.json"), key=lambda path: int(path.stem.split("_")[1]))
    if len(reports) != 300:
        parser.error(f"expected 300 deterministic reports, found {len(reports)}")
    all_case_ids = [int(path.stem.split("_")[1]) for path in reports]
    if args.case_ids:
        try:
            case_ids = [int(value.strip()) for value in args.case_ids.split(",") if value.strip()]
        except ValueError as exc:
            parser.error(f"--case-ids must contain comma-separated integers: {exc}")
        unknown_ids = sorted(set(case_ids) - set(all_case_ids))
        if unknown_ids:
            parser.error(f"--case-ids contains unknown IDs: {unknown_ids}")
        if not case_ids:
            parser.error("--case-ids must contain at least one ID")
        case_ids = list(dict.fromkeys(case_ids))
    else:
        case_ids = all_case_ids
    excluded_ids = set()
    if args.exclude_case_ids:
        try:
            excluded_ids = {int(value.strip()) for value in args.exclude_case_ids.split(",") if value.strip()}
        except ValueError as exc:
            parser.error(f"--exclude-case-ids must contain comma-separated integers: {exc}")
        unknown_excluded_ids = sorted(excluded_ids - set(all_case_ids))
        if unknown_excluded_ids:
            parser.error(f"--exclude-case-ids contains unknown IDs: {unknown_excluded_ids}")
        case_ids = [case_id for case_id in case_ids if case_id not in excluded_ids]
        if not case_ids:
            parser.error("case selection is empty after applying --exclude-case-ids")
    run_dir = args.run_dir
    (run_dir / "requests").mkdir(parents=True, exist_ok=True)
    (run_dir / "reviews").mkdir(parents=True, exist_ok=True)
    ledger_path = run_dir / "ledger.json"
    if not ledger_path.exists():
        ledger_path.write_text(json.dumps({"ledger_version": 1, "cases": {}}, indent=2) + "\n", encoding="utf-8")
    stages = [case_ids[:10]]
    remaining = case_ids[10:]
    stages.extend(remaining[index:index + args.batch_size] for index in range(0, len(remaining), args.batch_size))
    stages = [stage for stage in stages if stage]
    total_stages = len(stages)
    _write_progress(run_dir, all_case_ids, 0, total_stages)
    package_script = Path("scripts/package_discussion_units_llm.py")
    for stage_number, stage_case_ids in enumerate(stages, 1):
        pending_case_ids = [
            case_id for case_id in stage_case_ids
            if read_ledger(ledger_path)["cases"].get(str(case_id), {}).get("status") != "complete"
        ]
        for case_id in pending_case_ids:
            record_case(ledger_path, case_id, "started", network_requested=True)

        def run_case(case_id: int) -> tuple[int, subprocess.CompletedProcess[str] | None, str | None]:
            started_at = datetime.now(timezone.utc).isoformat()
            started_clock = time.monotonic()
            input_path = args.source_dir / f"case_{case_id}_deterministic.json"
            request_path = run_dir / "requests" / f"case_{case_id}_paragraph_assessment.json"
            review_path = run_dir / "reviews" / f"case_{case_id}_paragraph_assessment.md"
            command = [
                sys.executable,
                str(package_script),
                "--input-json", str(input_path),
                "--output-request", str(request_path),
                "--output-markdown", str(review_path),
                "--paragraph-level",
                "--send",
                "--budget-usd", str(args.budget_usd),
            ]
            try:
                result = subprocess.run(command, capture_output=True, text=True, timeout=240)
                result.elapsed_seconds = round(time.monotonic() - started_clock, 3)  # type: ignore[attr-defined]
                result.started_at = started_at  # type: ignore[attr-defined]
                result.finished_at = datetime.now(timezone.utc).isoformat()  # type: ignore[attr-defined]
                return case_id, result, None
            except subprocess.TimeoutExpired as exc:
                return case_id, None, f"runner timeout after 240 seconds: {exc}"

        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = [executor.submit(run_case, case_id) for case_id in pending_case_ids]
            for future in as_completed(futures):
                case_id, result, timeout_error = future.result()
                if timeout_error:
                    record_case(ledger_path, case_id, "failed", error=timeout_error)
                elif result is not None and result.returncode != 0:
                    record_case(
                        ledger_path,
                        case_id,
                        "failed",
                        error=f"package runner exited {result.returncode}",
                        stdout=result.stdout[-2000:],
                        stderr=result.stderr[-2000:],
                        elapsed_seconds=result.elapsed_seconds,
                        started_at=result.started_at,
                        finished_at=result.finished_at,
                    )
                else:
                    request_path = run_dir / "requests" / f"case_{case_id}_paragraph_assessment.json"
                    output = json.loads(request_path.read_text(encoding="utf-8"))
                    usage = output["response"]["usage"]
                    record_case(
                        ledger_path,
                        case_id,
                        "complete",
                        mode="network",
                        unit_count=len(output["response"]["result"]["assessments"]),
                        spent_usd=usage["estimated_cost_usd"],
                        usage=usage,
                        elapsed_seconds=result.elapsed_seconds,
                        started_at=result.started_at,
                        finished_at=result.finished_at,
                        returned_assessment_count=output["response"]["result"].get("returned_assessment_count", 0),
                        missing_count=len(output["response"]["result"].get("missing_paragraph_indices", [])),
                        response_complete=output["response"]["result"].get("response_complete", True),
                    )
                _write_progress(run_dir, all_case_ids, stage_number, total_stages)
                entry = read_ledger(ledger_path)["cases"].get(str(case_id), {})
                print(
                    f"[{stage_number}/{total_stages}] case {case_id}: {entry.get('status', 'unknown')} "
                    f"({entry.get('unit_count', 0)} assessments, ${entry.get('spent_usd', 0) or 0})",
                    flush=True,
                )
    _write_progress(run_dir, all_case_ids, total_stages, total_stages)
    return 1 if any(read_ledger(ledger_path)["cases"].get(str(case_id), {}).get("status") == "failed" for case_id in case_ids) else 0


if __name__ == "__main__":
    raise SystemExit(main())