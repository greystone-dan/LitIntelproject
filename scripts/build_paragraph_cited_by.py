"""Build the paragraph-level "cited by" tables from stored citation occurrences.

For every case that cites another library case by paragraph, store which paragraph it
cites, how often, and the signal phrase written next to the citation ("see also",
"followed in", "distinguished", ...). The reader's Markup view reads these rows.

Safe by default: with no flags it only reports what it would do. Nothing is written
without --apply. No AI and no network. It only reads the citing case's own text.

  python scripts/build_paragraph_cited_by.py                       # plan only
  python scripts/build_paragraph_cited_by.py --apply --max-minutes 60
  python scripts/build_paragraph_cited_by.py --apply --case-ids 12 34 56
  python scripts/build_paragraph_cited_by.py --report-cited 1292  # show what is stored for a case

Resumable: a citing case counts as done once its status row is written, so stopping with
Ctrl+C (or --max-minutes) and running the same command again carries on. Each citing case is
rewritten in one transaction, so re-running is harmless. To redo everything after changing the
classifier, raise ALGO_VERSION in backend/paragraph_cited_by.py.

Light on the machine: small batches, a pause between them, lower process priority, and a
per-statement time limit. Run it off-battery and off-peak (see docs/PARAGRAPH_CITED_BY.md).
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text  # noqa: E402

from backend.database import SessionLocal  # noqa: E402
from backend.paragraph_cited_by import ALGO_VERSION  # noqa: E402
from backend.paragraph_cited_by_db import (  # noqa: E402
    compute_source_edges,
    count_pending_sources,
    load_paragraph_cited_by,
    pending_source_ids,
    write_source_edges,
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apply", action="store_true", help="write results (default: report only)")
    parser.add_argument("--batch-size", type=int, default=25, help="citing cases per transaction batch (default 25)")
    parser.add_argument("--sleep", type=float, default=0.5, help="seconds to pause between batches (default 0.5)")
    parser.add_argument("--max-minutes", type=float, default=None, help="stop cleanly after this many minutes")
    parser.add_argument("--limit", type=int, default=None, help="stop after this many citing cases")
    parser.add_argument("--after-id", type=int, default=0, help="only citing cases with an id above this")
    parser.add_argument("--case-ids", type=int, nargs="*", help="process exactly these citing case ids")
    parser.add_argument("--statement-timeout-ms", type=int, default=60000, help="per-statement limit (default 60000)")
    parser.add_argument("--report-cited", type=int, metavar="CASE_ID", help="print stored cited-by for this cited case and exit")
    return parser.parse_args(argv)


def lower_priority() -> None:
    try:
        os.nice(10)
    except (AttributeError, OSError):
        pass  # Windows has no os.nice; the scheduled task / start /low handles priority there


def report_cited(case_id: int) -> int:
    with SessionLocal() as db:
        data = load_paragraph_cited_by(db, case_id)
    if data is None:
        print(f"Nothing stored for case {case_id} (batch not run for its citing cases, or no pinpoint citations).")
        return 0
    cov = data["coverage"]
    print(f"Case {case_id}: {cov['sources_processed']}/{cov['sources_total']} citing cases processed"
          f"{'' if cov['complete'] else ' (partial)'}")
    for item in data["paragraphs"]:
        purposes = ", ".join(f"{label} {n}" for label, n in item["purposes"].items())
        print(f"  ¶[{item['paragraph']}] cited by {item['citer_count']} case(s), {item['mention_count']} mention(s): {purposes}")
        for citer in item["citers"][:3]:
            print(f"      {citer['citation'] or citer['title']} x{citer['mentions']} {citer['purpose']}"
                  f"{' (' + citer['signal'] + ')' if citer['signal'] else ''}")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.report_cited is not None:
        return report_cited(args.report_cited)
    if args.batch_size < 1:
        raise SystemExit("--batch-size must be at least 1")
    lower_priority()
    started = time.monotonic()
    deadline = started + args.max_minutes * 60 if args.max_minutes else None
    processed = edges_total = occurrences_total = 0
    failed: list[int] = []
    mode = "APPLY" if args.apply else "PLAN ONLY (no --apply: nothing is written)"
    with SessionLocal() as db:
        if db.get_bind().dialect.name == "postgresql":
            db.execute(text(f"SET statement_timeout = {int(args.statement_timeout_ms)}"))
        total, done = count_pending_sources(db)
        print(f"Paragraph cited-by, algorithm v{ALGO_VERSION}, {mode}")
        print(f"Citing cases with resolved citations: {total}; already processed: {done}; to do: {max(total - done, 0)}")
        after = args.after_id
        explicit = list(args.case_ids) if args.case_ids else None
        try:
            while True:
                if explicit is not None:
                    batch, explicit = explicit[: args.batch_size], explicit[args.batch_size:]
                else:
                    batch = pending_source_ids(db, after, args.batch_size)
                if not batch:
                    break
                for source_id in batch:
                    try:
                        with db.begin_nested():  # a failure only undoes this one citing case
                            edges, used = compute_source_edges(db, source_id)
                            if args.apply:
                                write_source_edges(db, source_id, edges)
                    except Exception as error:  # noqa: BLE001 - report and carry on with the next case
                        failed.append(source_id)
                        print(f"  skipped case {source_id}: {type(error).__name__}: {str(error)[:120]}", flush=True)
                        after = max(after, source_id)
                        continue
                    processed += 1
                    edges_total += len(edges)
                    occurrences_total += used
                    after = max(after, source_id)
                    if args.limit and processed >= args.limit:
                        break
                if args.apply:
                    db.commit()
                else:
                    db.rollback()
                print(f"  {processed} citing cases, {edges_total} paragraph edges, {occurrences_total} citations read "
                      f"({time.monotonic() - started:.0f}s)", flush=True)
                if args.limit and processed >= args.limit:
                    break
                if deadline and time.monotonic() >= deadline:
                    print("Time limit reached; run the same command again to resume.")
                    break
                time.sleep(max(args.sleep, 0))
        except KeyboardInterrupt:
            db.rollback()
            print("Interrupted; finished batches are saved. Run the same command again to resume.")
    if failed:
        print(f"Skipped {len(failed)} case(s) that errored (they stay pending): {failed[:20]}")
    print(f"Done: {processed} citing cases, {edges_total} paragraph edges, {occurrences_total} citations read.")
    if not args.apply:
        print("Nothing was written. Add --apply to store these.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
