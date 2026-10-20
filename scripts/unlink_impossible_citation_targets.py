"""Unlink citations whose target decision is dated after the citing decision (impossible links).

Dry run by default: SELECTs in a READ ONLY transaction, prints counts by citing court, kind and
wrong target, and writes a sample. Nothing is written without --apply, and --apply refuses to run
without --change-log and --expected-count, and prints linked-citation and wrong-target counts before and after.

    python scripts/unlink_impossible_citation_targets.py --sample-csv C:\\ilit_backups\\unlink_sample.csv
    python scripts/unlink_impossible_citation_targets.py --apply --expected-count N --change-log C:\\ilit_backups\\unlink_changes.csv
    python scripts/unlink_impossible_citation_targets.py --undo C:\\ilit_backups\\unlink_changes.csv --apply

What --apply does: for rows whose target is dated more than --min-days after the citing decision,
set target_case_id = NULL and unresolved = true. The change log (written and flushed before each
batch is updated) holds citation id, previous target, previous unresolved value and the dates, so
--undo can restore both columns. A row whose cite text already contains the target's own citation
is skipped: there the library date, not the link, is wrong.
"""

from __future__ import annotations

import argparse
import csv
import random
import sys
from collections import Counter
from pathlib import Path

from sqlalchemy import text

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import _citation_variants  # noqa: E402

DEFAULT_SOURCE_COURTS = r"^(FC|FCA|SCC|Federal Court|Federal Court of Appeal|Supreme Court of Canada)$"
CASE_KINDS = ("case", "case_name", "case_short", "neutral")
LOG_FIELDS = [
	"citation_id", "source_case_id", "source_court", "kind", "previous_target_case_id",
	"previous_unresolved", "source_date", "target_date", "cite_text",
]


def holds_own_citation(cite_text: str | None, target_citation: str | None, target_secondary: str | None) -> bool:
	"""True when the cite text names the target by its own citation (the link is right, the date is wrong)."""
	wanted = {v for v in _citation_variants(cite_text or "") if " CANLII " not in f" {v} "}
	if not wanted:
		return False
	have: set[str] = set()
	for value in (target_citation, target_secondary):
		have.update(_citation_variants(value or ""))
	return bool(wanted & have)


def read_undo_rows(path: Path) -> list[dict]:
	with path.open(newline="", encoding="utf-8") as handle:
		return list(csv.DictReader(handle))


CANDIDATE_SQL = """SELECT ci.id, ci.source_case_id, s.court, ci.citation_kind, ci.target_case_id, ci.unresolved,
	coalesce(ci.citation_text, ci.normalized_citation, ''), s.date, t.date, t.citation, t.secondary_citation, t.title
	FROM citations ci JOIN cases s ON s.id = ci.source_case_id JOIN cases t ON t.id = ci.target_case_id
	WHERE s.court ~* :src AND ci.citation_kind IN ('case','case_name','case_short','neutral')
	AND ci.target_case_id IS NOT NULL AND t.date > s.date + :days * interval '1 day'
	ORDER BY ci.id"""
LINKED_SQL = """SELECT count(*) FROM citations ci JOIN cases s ON s.id = ci.source_case_id
	WHERE s.court ~* :src AND ci.citation_kind IN ('case','case_name','case_short','neutral')
	AND ci.target_case_id IS NOT NULL"""


def find_candidates(session, source_courts: str, min_days: int) -> tuple[list[tuple], int]:
	"""Impossible links to unlink, and how many were skipped because the cite text holds the target's own cite."""
	rows = session.execute(text(CANDIDATE_SQL), {"src": source_courts, "days": min_days}).all()
	candidates = [r for r in rows if not holds_own_citation(r[6], r[9], r[10])]
	return candidates, len(rows) - len(candidates)


def state_counts(session, source_courts: str, min_days: int) -> dict:
	"""Linked citations (in scope) and the impossible links still present, for before/after reporting."""
	candidates, _ = find_candidates(session, source_courts, min_days)
	return {
		"linked_citations": session.execute(text(LINKED_SQL), {"src": source_courts}).scalar(),
		"impossible_links": len(candidates),
		"distinct_wrong_targets": len({r[4] for r in candidates}),
	}


def apply_unlink(session, candidates: list[tuple], change_log: Path, batch_size: int) -> int:
	"""Write the change log for each batch (flushed), then unlink it. A row changed since the scan is skipped."""
	change_log.parent.mkdir(parents=True, exist_ok=True)
	changed = 0
	with change_log.open("a", newline="", encoding="utf-8") as handle:
		writer = csv.writer(handle)
		if handle.tell() == 0:
			writer.writerow(LOG_FIELDS)
		for start in range(0, len(candidates), batch_size):
			batch = candidates[start : start + batch_size]
			for r in batch:
				writer.writerow([r[0], r[1], r[2], r[3], r[4], r[5], r[7], r[8], r[6][:200]])
			handle.flush()
			for r in batch:
				res = session.execute(
					text("UPDATE citations SET target_case_id = NULL, unresolved = true WHERE id = :id AND target_case_id = :t"),
					{"id": r[0], "t": r[4]},
				)
				changed += res.rowcount
			session.commit()
	return changed


def undo_unlink(session, rows: list[dict]) -> tuple[int, int]:
	"""Restore previous target and unresolved, only where the row is still unlinked."""
	restored = skipped = 0
	for row in rows:
		result = session.execute(
			text("UPDATE citations SET target_case_id = :t, unresolved = :u WHERE id = :id AND target_case_id IS NULL"),
			{"t": int(row["previous_target_case_id"]), "u": row["previous_unresolved"] in ("True", "true", "1", "t"), "id": int(row["citation_id"])},
		)
		restored += result.rowcount
		skipped += 1 - result.rowcount
	session.commit()
	return restored, skipped


def main(argv: list[str] | None = None) -> int:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Write changes (default is a dry run).")
	parser.add_argument("--change-log", type=Path, help="CSV of every changed row; required with --apply.")
	parser.add_argument("--expected-count", type=int, help="With --apply: stop unless exactly this many links would be unlinked.")
	parser.add_argument("--undo", type=Path, help="Restore rows from a change-log CSV (dry run unless --apply).")
	parser.add_argument("--min-days", type=int, default=30)
	parser.add_argument("--source-courts", default=DEFAULT_SOURCE_COURTS)
	parser.add_argument("--sample-csv", type=Path, default=None)
	parser.add_argument("--sample-size", type=int, default=50)
	parser.add_argument("--batch-size", type=int, default=1000)
	parser.add_argument("--seed", type=int, default=7)
	args = parser.parse_args(argv)
	if args.apply and not args.undo and (args.change_log is None or args.expected_count is None):
		raise SystemExit("--apply needs --change-log and --expected-count (the dry-run to_unlink number)")

	from backend.database import SessionLocal

	with SessionLocal() as session:
		if args.undo:
			rows = read_undo_rows(args.undo)
			print(f"undo rows in file: {len(rows)}")
			if not args.apply:
				print("dry run: pass --apply to restore")
				return 0
			restored, skipped = undo_unlink(session, rows)
			print(f"restored={restored} skipped_already_changed={skipped}")
			return 0

		if not args.apply:
			session.execute(text("SET TRANSACTION READ ONLY"))
		candidates, skipped_own = find_candidates(session, args.source_courts, args.min_days)
		by_court = Counter(r[2] for r in candidates)
		by_kind = Counter(r[3] for r in candidates)
		by_target = Counter((r[4], r[11]) for r in candidates)
		print(f"to_unlink={len(candidates)} skipped_cite_holds_targets_own_citation={skipped_own}")
		print("by citing court:", dict(by_court))
		print("by kind:", dict(by_kind))
		print(f"distinct wrong targets: {len(by_target)}")
		for (target_id, title), n in by_target.most_common(20):
			print(f"  target {target_id} ({title}): {n}")

		if args.sample_csv:
			rng = random.Random(args.seed)
			sample = rng.sample(candidates, min(args.sample_size, len(candidates)))
			with args.sample_csv.open("w", newline="", encoding="utf-8") as handle:
				writer = csv.writer(handle)
				writer.writerow(LOG_FIELDS + ["target_title"])
				for r in sample:
					writer.writerow([r[0], r[1], r[2], r[3], r[4], r[5], r[7], r[8], r[6][:200], r[11]])

		if not args.apply:
			print("dry run: nothing written. Re-run with --apply --change-log FILE --expected-count N")
			return 0
		if args.expected_count != len(candidates):
			print(f"Expected {args.expected_count} but found {len(candidates)}; nothing changed.")
			return 1
		before = state_counts(session, args.source_courts, args.min_days)
		print("before:", before)
		changed = apply_unlink(session, candidates, args.change_log, args.batch_size)
		after = state_counts(session, args.source_courts, args.min_days)
		print("after: ", after)
		print(f"unlinked={changed} of {len(candidates)}; change log: {args.change_log}")
		return 0


if __name__ == "__main__":
	sys.exit(main())
