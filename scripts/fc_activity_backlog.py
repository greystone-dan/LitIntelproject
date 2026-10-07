#!/usr/bin/env python3
"""Overnight FC Activity backlog: fetch docket activity for IMM files that are not resolved yet.

"Known" IMM numbers are the union of: fc_activity_cases (citation or raw_payload.imm_number),
fc_procedural_history rows with a style of cause, and IMM docket numbers on FC decisions in `cases`.

A known number is "resolved" when its fc_activity file has docket entries AND the stored
classification says lifecycle_status.status = 'closed'. Everything else is unresolved:
  not_in_activity   known only from decisions / procedural history, no fc_activity file
  no_documents      fc_activity file exists but holds zero docket entries
  open_or_unknown   has entries, lifecycle not 'closed' (or not classified yet)

Subcommands (all read-only except `run` without --dry-run/--out-file, `import` and `undo --yes`):
  counts              totals and a by-year breakdown, plus a runtime estimate
  export-list FILE    write the ordered unresolved list (for a machine with no database)
  run --dry-run       fetch and parse the first N unresolved numbers (default 20), write nothing;
                      use --limit 200 to see the speed before a full night
  run                 the real run: additive writes only, resumable, stop file, progress file
  run --list-file F --out-file R.jsonl [--shard i/n]
                      second-machine mode: no database; fetched results go to a JSONL file
  import R.jsonl      add a results file to the database (additive, ledgered, safe to repeat)
  undo                list (default) or remove (--yes) the rows a run added, from its ledger

Writes are additive: new fc_activity_cases / fc_activity_documents rows only. Existing files only
gain missing docket entries (and a blank case name/date is filled); nothing is overwritten or deleted.
No AI calls. Two requests per file, one file at a time. Pace follows the earlier live sweep
(2026-09-25/26, 98,301 files at 2,300-11,500 files/hour, no blocks): start at 100 ms between files with a 2 s pause per 20 files
(sub-2 s is the fetcher's explicit opt-in, approved by Daniel on 2026-10-07 with back-off), double the
delay after any failure up to 2 s, speed up again after 50 clean files. Any HTTP 403/429 stops the run
at once; it is never retried around.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text  # noqa: E402

from backend.database import FCActivityCase, FCActivityDocument, SessionLocal  # noqa: E402

IMM_RE = re.compile(r"^IMM-(\d+)-(\d{2})$")
ADVISORY_LOCK_KEY = 74_100_262
CATEGORIES = ("not_in_activity", "no_documents", "open_or_unknown")
SECONDS_PER_FILE = 0.5  # 2026-09-25/26 sweep: 100 ms delay, ~0.3-0.4 s per file, plus a 2 s pause per 20 files
DEFAULT_RUN_DIR = PROJECT_ROOT / "data" / "fc_activity_overnight"

UNRESOLVED_SQL = """
WITH acase AS (
    SELECT c.id,
           upper(COALESCE(NULLIF(c.citation, ''), c.raw_payload->>'imm_number')) AS imm
    FROM fc_activity_cases c
),
acase_imm AS (
    SELECT a.imm,
           bool_or(EXISTS (SELECT 1 FROM fc_activity_documents d WHERE d.case_id = a.id)) AS has_docs,
           bool_or(k.classification_json::jsonb #>> '{lifecycle_status,status}' = 'closed') AS closed
    FROM acase a
    LEFT JOIN fc_activity_classifications k ON k.source_case_id = a.id
    WHERE a.imm ~ '^IMM-[0-9]+-[0-9]{2}$'
    GROUP BY a.imm
),
known AS (
    SELECT imm FROM acase_imm
    UNION
    SELECT upper(imm_number) FROM fc_procedural_history
      WHERE coalesce(style_of_cause, '') <> '' AND upper(imm_number) ~ '^IMM-[0-9]+-[0-9]{2}$'
    UNION
    SELECT m[1] FROM cases cs,
      LATERAL regexp_matches(upper(coalesce(cs.docket_number, '') || ' ' || coalesce(cs.source_id, '')),
                             '(IMM-[0-9]+-[0-9]{2})', 'g') AS m
      WHERE cs.court = 'FC'
)
SELECT k.imm,
       CASE WHEN a.imm IS NULL THEN 'not_in_activity'
            WHEN NOT coalesce(a.has_docs, false) THEN 'no_documents'
            WHEN coalesce(a.closed, false) THEN 'resolved'
            ELSE 'open_or_unknown' END AS category
FROM known k LEFT JOIN acase_imm a ON a.imm = k.imm
"""


def imm_sort_key(imm: str, newest_first: bool = False) -> tuple[int, int]:
    """Year then sequence; two-digit years 00-50 are 2000s. Oldest first unless newest_first."""
    match = IMM_RE.match(imm)
    if not match:
        return (9999, 0)
    seq, yy = int(match.group(1)), int(match.group(2))
    year = 2000 + yy if yy <= 50 else 1900 + yy
    return (-year, -seq) if newest_first else (year, seq)


def run_order_key(row: tuple[str, str], oldest_first: bool = False) -> tuple[int, tuple[int, int]]:
    """Never-fetched files first (not_in_activity, no_documents), then open_or_unknown; newest year first within each."""
    imm, category = row
    rank = CATEGORIES.index(category) if category in CATEGORIES else len(CATEGORIES)
    return (rank, imm_sort_key(imm, newest_first=not oldest_first))


def load_unresolved(db, categories: tuple[str, ...] = CATEGORIES) -> list[tuple[str, str]]:
    rows = db.execute(text(UNRESOLVED_SQL)).all()
    return [(imm, cat) for imm, cat in rows if cat in categories and IMM_RE.match(imm)]


def parse_shard(value: str | None) -> tuple[int, int]:
    """'2/3' -> (2, 3), 1-based. None -> (1, 1)."""
    if not value:
        return (1, 1)
    match = re.fullmatch(r"(\d+)/(\d+)", value.strip())
    if not match or not (1 <= int(match.group(1)) <= int(match.group(2))):
        raise ValueError("--shard must look like i/n with 1 <= i <= n, e.g. 2/2")
    return int(match.group(1)), int(match.group(2))


def in_shard(imm: str, index: int, count: int) -> bool:
    """Deterministic split by hash of the IMM number, so machines with different lists still never overlap."""
    return int(hashlib.sha256(imm.encode("utf-8")).hexdigest(), 16) % count == index - 1


def read_list_file(path: Path) -> list[str]:
    return [line.split("\t", 1)[0].strip().upper() for line in path.read_text(encoding="utf-8").splitlines()
            if IMM_RE.match(line.split("\t", 1)[0].strip().upper())]


def read_done(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {line.split("\t", 1)[0].strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def stop_requested(stop_file: Path | None) -> bool:
    return bool(stop_file and stop_file.exists())


def estimate_hours(count: int, seconds_per_file: float = SECONDS_PER_FILE) -> float:
    return count * seconds_per_file / 3600


class Logger:
    def __init__(self, path: Path | None) -> None:
        self.handle = path.open("a", encoding="utf-8", buffering=1) if path else None

    def __call__(self, message: str) -> None:
        line = f"{datetime.now(timezone.utc):%Y-%m-%d %H:%M:%S}Z {message}"
        print(line, flush=True)
        if self.handle:
            self.handle.write(line + "\n")


def cmd_counts(args: argparse.Namespace) -> int:
    with SessionLocal() as db:
        rows = db.execute(text(UNRESOLVED_SQL)).all()
    by_cat: dict[str, int] = {}
    by_year: dict[str, dict[str, int]] = {}
    for imm, cat in rows:
        by_cat[cat] = by_cat.get(cat, 0) + 1
        year = imm_sort_key(imm)[0]
        by_year.setdefault(str(year), {}).setdefault(cat, 0)
        by_year[str(year)][cat] += 1
    total = len(rows)
    unresolved = sum(by_cat.get(c, 0) for c in CATEGORIES)
    print(f"Total known IMM numbers: {total:,}")
    print(f"Resolved (closed): {by_cat.get('resolved', 0):,}")
    print(f"Unresolved: {unresolved:,}")
    for cat in CATEGORIES:
        print(f"  {cat}: {by_cat.get(cat, 0):,}")
    print("\nBy year (resolved / not_in_activity / no_documents / open_or_unknown):")
    for year in sorted(by_year):
        c = by_year[year]
        print(f"  {year}: {c.get('resolved', 0):,} / {c.get('not_in_activity', 0):,} / "
              f"{c.get('no_documents', 0):,} / {c.get('open_or_unknown', 0):,}")
    print(f"\nEstimate at ~{SECONDS_PER_FILE:.0f} s per file: {estimate_hours(unresolved):.1f} hours "
          f"for all unresolved ({estimate_hours(unresolved) / 10:.1f} ten-hour nights).")
    if args.json_out:
        Path(args.json_out).write_text(json.dumps({"total": total, "by_category": by_cat, "by_year": by_year}, indent=2), encoding="utf-8")
    return 0


def store_additive(db, imm: str, result: dict[str, Any], run_label: str) -> tuple[int, bool, list[int]]:
    """Add the file/entries that are missing. Never overwrites or deletes. Returns (case_id, case_created, new_doc_ids)."""
    from scripts.fetch_fc_procedural_history import _activity_hash, _activity_year, _json_safe, _parse_date

    case = db.query(FCActivityCase).filter(FCActivityCase.citation == imm).first()
    if case is None:
        case = db.query(FCActivityCase).filter(
            FCActivityCase.source_key.in_([_activity_hash("fc-procedural-endpoint", imm), _activity_hash("fc-daily-intake", imm)])
        ).first()
    entry_dates = [d for d in (_parse_date(str(e.get("date") or "")) for e in result.get("entries_json") or []) if d]
    created = False
    if case is None:
        case = FCActivityCase(
            source_key=_activity_hash("fc-overnight-backlog", imm),
            citation=imm,
            year=_activity_year(imm),
            case_name=result.get("style_of_cause"),
            date_filed=min(entry_dates) if entry_dates else None,
            source_type="fc_registry_overnight",
            source_name=run_label,
            source_id=imm,
            scraped_timestamp=result.get("fetched_at"),
            raw_payload=_json_safe({**result, "imm_number": imm}),
        )
        db.add(case)
        db.flush()
        created = True
    else:
        if not case.case_name and result.get("style_of_cause"):
            case.case_name = result["style_of_cause"]
        if case.date_filed is None and entry_dates:
            case.date_filed = min(entry_dates)

    new_ids: list[int] = []
    seen: set[tuple[str, str]] = set()
    for entry in result.get("entries_json") or []:
        entry_text = str(entry.get("entry") or "").strip()
        entry_date = entry.get("date") or None
        re_no = str(entry.get("re_no") or "").strip() or None
        docno = str(entry.get("docno") or "").strip() or None
        if not entry_text and not entry_date:
            continue
        entry_hash = _activity_hash(imm, re_no, docno, entry_date, entry_text)
        if re_no is not None and docno is not None:
            if (re_no, docno) in seen:
                continue
            seen.add((re_no, docno))
            if db.query(FCActivityDocument.id).filter(
                FCActivityDocument.case_id == case.id, FCActivityDocument.re_no == re_no, FCActivityDocument.docno == docno
            ).first():
                continue
        if db.query(FCActivityDocument.id).filter(
            FCActivityDocument.case_id == case.id, FCActivityDocument.entry_hash == entry_hash
        ).first():
            continue
        doc = FCActivityDocument(
            case_id=case.id, re_no=re_no, docno=docno,
            doc_dt=_parse_date(str(entry_date)) if entry_date else None,
            recorded_entry=entry_text or None, entry_hash=entry_hash,
            raw_document={"imm_number": imm, **entry},
        )
        db.add(doc)
        db.flush()
        new_ids.append(doc.id)
    db.commit()
    return case.id, created, new_ids


def cmd_export_list(args: argparse.Namespace) -> int:
    with SessionLocal() as db:
        candidates = load_unresolved(db, tuple(args.categories.split(",")))
    candidates.sort(key=lambda row: run_order_key(row, args.oldest_first))
    Path(args.file).write_text("".join(f"{imm}\t{cat}\n" for imm, cat in candidates), encoding="utf-8")
    print(f"Wrote {len(candidates):,} unresolved IMM numbers to {args.file}")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    import random

    from scripts.daily_intake import build_fc_client, is_missing_file
    from scripts.fetch_fc_procedural_history import RequestBudget, _json_safe, process_imm

    shard_index, shard_count = parse_shard(args.shard)
    offline = bool(args.out_file)
    if offline and not args.list_file:
        print("--out-file needs --list-file (the second machine has no database).")
        return 1
    run_dir = Path(args.run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    stop_file = Path(args.stop_file) if args.stop_file else run_dir / "stop.txt"
    done_path = run_dir / "done.tsv"          # IMM <tab> outcome; the resume list
    ledger_path = run_dir / "ledger.jsonl"    # what was added, for undo
    progress_path = run_dir / "progress.json"
    log = Logger(None if args.dry_run else run_dir / "run.log")
    run_label = f"FC Activity overnight backlog {datetime.now(timezone.utc):%Y-%m-%d}"

    if stop_requested(stop_file) and not args.dry_run:
        log(f"Stop file exists ({stop_file}); delete it to run. Nothing done.")
        return 1

    lock_db = None
    if args.list_file:
        candidates = [(imm, "listed") for imm in read_list_file(Path(args.list_file))]
    else:
        lock_db = SessionLocal()  # held open for the whole run: the advisory lock lives on this connection
        with SessionLocal() as db:
            candidates = load_unresolved(db, tuple(args.categories.split(",")))
        candidates.sort(key=lambda row: run_order_key(row, args.oldest_first))
        if not args.dry_run and not offline:
            if not lock_db.execute(text("SELECT pg_try_advisory_lock(:k)"), {"k": ADVISORY_LOCK_KEY}).scalar():
                log("Another backlog run holds the lock; exiting.")
                lock_db.close()
                return 1
    done = set() if args.dry_run or args.ignore_done else read_done(done_path)
    todo = [imm for imm, _cat in candidates if imm not in done and in_shard(imm, shard_index, shard_count)]
    limit = 20 if args.dry_run and not args.limit else args.limit
    if limit:
        todo = todo[:limit]
    log(f"{'DRY RUN: ' if args.dry_run else ''}shard {shard_index}/{shard_count}: {len(candidates):,} listed, "
        f"{len(done):,} already done, {len(todo):,} to process (~{estimate_hours(len(todo)):.1f} h)")

    started = time.monotonic()
    request_budget = RequestBudget(max(args.max_requests, 2 * len(todo) * 3))
    stats = {"processed": 0, "files_added": 0, "docs_added": 0, "missing": 0, "failed": 0}
    consecutive_failures = 0
    pause_s = args.issue_pause_s
    current_delay_ms = args.delay_ms
    clean_streak = 0
    stopped_by = "finished"
    writes = not args.dry_run
    done_handle = done_path.open("a", encoding="utf-8", buffering=1) if writes else None
    ledger_handle = ledger_path.open("a", encoding="utf-8", buffering=1) if writes and not offline else None
    out_handle = Path(args.out_file).open("a", encoding="utf-8", buffering=1) if offline and writes else None

    def write_progress() -> None:
        if not writes:
            return
        progress_path.write_text(json.dumps({
            **stats, "shard": f"{shard_index}/{shard_count}", "remaining": len(todo) - stats["processed"],
            "stopped_by": stopped_by, "delay_ms": current_delay_ms,
            "elapsed_minutes": round((time.monotonic() - started) / 60, 1),
            "updated": datetime.now(timezone.utc).isoformat(),
        }, indent=2), encoding="utf-8")

    block_seen: list[int] = []

    def watch_status(response) -> None:  # httpx response hook: a 403/429 means the site is refusing us
        if response.status_code in (403, 429):
            block_seen.append(response.status_code)

    try:
        with build_fc_client() as client:
            client.event_hooks["response"].append(watch_status)
            for i, imm in enumerate(todo, 1):
                if stop_requested(stop_file):
                    stopped_by = "stop file"
                    break
                if args.max_minutes and (time.monotonic() - started) > args.max_minutes * 60:
                    stopped_by = "time limit"
                    break
                if i > 1:
                    time.sleep((current_delay_ms + random.randint(0, args.jitter_ms)) / 1000)
                try:
                    result = process_imm(client, imm, request_budget=request_budget)
                except Exception as exc:  # budget or unexpected
                    result = {"error": str(exc)}
                if block_seen:
                    stopped_by = f"HTTP {block_seen[0]} from the Court site: stopped, not retried"
                    log(f"[BLOCK] {imm}: {stopped_by}")
                    break
                if result.get("error"):
                    stats["failed"] += 1
                    consecutive_failures += 1
                    clean_streak = 0
                    current_delay_ms = min(args.max_delay_ms, max(current_delay_ms * 2, 250))
                    log(f"[fail] {imm}: {result['error']} (consecutive={consecutive_failures}, delay now {current_delay_ms} ms, pausing {pause_s:.0f}s)")
                    time.sleep(pause_s)
                    pause_s = min(pause_s * 2, 300)
                    if consecutive_failures >= args.max_consecutive_failures:
                        stopped_by = f"{consecutive_failures} failures in a row (source may be blocking)"
                        break
                    continue
                consecutive_failures, pause_s = 0, args.issue_pause_s
                clean_streak += 1
                if clean_streak >= 50 and current_delay_ms > args.delay_ms:
                    current_delay_ms = max(args.delay_ms, int(current_delay_ms * 0.75))
                    clean_streak = 0
                    log(f"[adaptive] 50 clean files; delay back to {current_delay_ms} ms")
                stats["processed"] += 1
                if is_missing_file(result):
                    stats["missing"] += 1
                    outcome = "missing"
                    log(f"[{i}/{len(todo)}] {imm}: no file at registry")
                elif args.dry_run:
                    outcome = "dry"
                    log(f"[{i}/{len(todo)}] {imm}: {len(result.get('entries_json') or [])} entries, "
                        f"status={result.get('case_status')}, would write")
                elif offline:
                    outcome = f"fetched:{len(result.get('entries_json') or [])}"
                    out_handle.write(json.dumps({"imm": imm, "result": _json_safe(result)}) + "\n")
                    log(f"[{i}/{len(todo)}] {imm}: {len(result.get('entries_json') or [])} entries saved to file")
                else:
                    with SessionLocal() as db:
                        case_id, created, new_ids = store_additive(db, imm, result, run_label)
                    stats["files_added"] += int(created)
                    stats["docs_added"] += len(new_ids)
                    outcome = f"ok:{len(new_ids)}"
                    if created or new_ids:
                        ledger_handle.write(json.dumps({"imm": imm, "case_id": case_id, "case_created": created, "doc_ids": new_ids}) + "\n")
                    log(f"[{i}/{len(todo)}] {imm}: {'new file, ' if created else ''}{len(new_ids)} new entries")
                if done_handle:
                    done_handle.write(f"{imm}\t{outcome}\n")
                if i % 25 == 0:
                    write_progress()
                if i % args.batch_size == 0:
                    time.sleep(args.batch_pause_ms / 1000)
    finally:
        write_progress()
        if lock_db is not None:
            lock_db.close()
        for handle in (done_handle, ledger_handle, out_handle):
            if handle:
                handle.close()
    elapsed = max(time.monotonic() - started, 0.001)
    log(f"Stopped: {stopped_by}. {stats}")
    log(f"Speed: {stats['processed']} files in {elapsed / 60:.1f} min = {stats['processed'] / elapsed * 3600:,.0f} files/hour")
    return 0 if stopped_by in ("finished", "stop file", "time limit") else 2


def cmd_import(args: argparse.Namespace) -> int:
    """Add a second machine's results file to the database: additive, ledgered, safe to run twice."""
    run_dir = Path(args.run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    ledger_path = run_dir / "ledger.jsonl"
    done_path = run_dir / "done.tsv"
    run_label = f"FC Activity overnight backlog (import) {datetime.now(timezone.utc):%Y-%m-%d}"
    lines = [line for line in Path(args.file).read_text(encoding="utf-8").splitlines() if line.strip()]
    done = read_done(done_path)
    todo = [json.loads(line) for line in lines]
    todo = [row for row in todo if row["imm"] not in done or args.ignore_done]
    print(f"{len(lines):,} results in file, {len(todo):,} not imported yet.")
    if args.dry_run:
        print("Dry run: nothing written.")
        return 0
    files = docs = 0
    with SessionLocal() as db, ledger_path.open("a", encoding="utf-8", buffering=1) as ledger, done_path.open("a", encoding="utf-8", buffering=1) as done_out:
        for row in todo:
            result = row["result"]
            if not result.get("entries_json") and not result.get("style_of_cause"):
                done_out.write(f"{row['imm']}\tmissing\n")
                continue
            fetched = result.get("fetched_at")
            if isinstance(fetched, str):
                result["fetched_at"] = datetime.fromisoformat(fetched)
            case_id, created, new_ids = store_additive(db, row["imm"], result, run_label)
            files += int(created)
            docs += len(new_ids)
            if created or new_ids:
                ledger.write(json.dumps({"imm": row["imm"], "case_id": case_id, "case_created": created, "doc_ids": new_ids}) + "\n")
            done_out.write(f"{row['imm']}\tok:{len(new_ids)}\n")
    print(f"Imported: {files:,} new files, {docs:,} new docket entries.")
    return 0


def cmd_undo(args: argparse.Namespace) -> int:
    ledger = Path(args.run_dir) / "ledger.jsonl"
    if not ledger.exists():
        print("No ledger; nothing to undo.")
        return 0
    entries = [json.loads(line) for line in ledger.read_text(encoding="utf-8").splitlines() if line.strip()]
    doc_ids = [d for e in entries for d in e["doc_ids"]]
    case_ids = [e["case_id"] for e in entries if e["case_created"]]
    print(f"Ledger: {len(case_ids):,} files created, {len(doc_ids):,} docket entries added.")
    if not args.yes:
        print("Dry run. Re-run with --yes to delete exactly these rows.")
        return 0
    with SessionLocal() as db:
        db.execute(text("DELETE FROM fc_activity_documents WHERE id = ANY(:ids)"), {"ids": doc_ids})
        db.execute(text("DELETE FROM fc_activity_cases WHERE id = ANY(:ids) AND source_type = 'fc_registry_overnight'"), {"ids": case_ids})
        db.commit()
    ledger.rename(ledger.with_suffix(".undone.jsonl"))
    print("Removed.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    counts = sub.add_parser("counts", help="read-only counts and runtime estimate")
    counts.add_argument("--json-out")
    counts.set_defaults(func=cmd_counts)
    export = sub.add_parser("export-list", help="write the ordered unresolved list to a file")
    export.add_argument("file")
    export.add_argument("--categories", default=",".join(CATEGORIES))
    export.add_argument("--oldest-first", action="store_true")
    export.set_defaults(func=cmd_export_list)
    imp = sub.add_parser("import", help="add a second machine's results file to the database")
    imp.add_argument("file")
    imp.add_argument("--run-dir", default=str(DEFAULT_RUN_DIR))
    imp.add_argument("--dry-run", action="store_true")
    imp.add_argument("--ignore-done", action="store_true")
    imp.set_defaults(func=cmd_import)
    run = sub.add_parser("run", help="fetch unresolved IMM files")
    run.add_argument("--dry-run", action="store_true", help="fetch and parse 20 numbers (or --limit), write nothing")
    run.add_argument("--limit", type=int)
    run.add_argument("--max-minutes", type=float, help="stop after this long (e.g. 600 for ten hours)")
    run.add_argument("--categories", default=",".join(CATEGORIES))
    run.add_argument("--oldest-first", action="store_true", help="never-fetched first, then newest year first within each category (default is newest first)")
    run.add_argument("--ignore-done", action="store_true", help="re-fetch numbers already in done.tsv")
    run.add_argument("--run-dir", default=str(DEFAULT_RUN_DIR))
    run.add_argument("--stop-file", help="default: <run-dir>/stop.txt")
    run.add_argument("--delay-ms", type=int, default=100, help="starting delay between files; backs off after failures")
    run.add_argument("--max-delay-ms", type=int, default=2000, help="ceiling for automatic back-off")
    run.add_argument("--jitter-ms", type=int, default=0, help="as in the 2026-09 sweep")
    run.add_argument("--batch-size", type=int, default=20)
    run.add_argument("--batch-pause-ms", type=int, default=2000, help="pause after every batch of files")
    run.add_argument("--issue-pause-s", type=float, default=10, help="pause after a failed fetch; doubles up to 300")
    run.add_argument("--max-consecutive-failures", type=int, default=10)
    run.add_argument("--max-requests", type=int, default=100000)
    run.set_defaults(func=cmd_run)
    undo = sub.add_parser("undo", help="remove the rows a run added (dry run unless --yes)")
    undo.add_argument("--run-dir", default=str(DEFAULT_RUN_DIR))
    undo.add_argument("--yes", action="store_true")
    undo.set_defaults(func=cmd_undo)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
