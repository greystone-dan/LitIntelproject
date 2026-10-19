"""Remove citation rows where a decision cites itself (site review R5). Dry run by default, reversible.

A row in `citations` with source_case_id = target_case_id makes a decision list its own caption as an authority
and adds one to its own "Cited by" count. This is the exact-match cleanup (same test as
scripts/audit_self_citations.py); the older scripts/remove_self_citations.py has no restore step and
recomputes all metrics.

  python scripts/fix_self_citations.py                          # dry run: counts by court and a sample
  python scripts/fix_self_citations.py --apply --expected-count N   # save every row to an undo file, then delete in batches
  python scripts/fix_self_citations.py --undo data/db_fix_backups/self_citations_<stamp>.jsonl   # put them back

Take a database backup first if you can (pg_dump of the citations table); the undo file is a second safety net.
After --apply nothing needs recomputing for citation_metrics (compute_citation_metrics already ignores self
links); the live "Cited by" numbers drop on their own. If the dry run reports paragraph_citation_edges self
rows, rebuild them with scripts/build_paragraph_cited_by.py (see docs/PARAGRAPH_CITED_BY.md).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import delete, text
from sqlalchemy.dialects.postgresql import insert as pg_insert

from backend.database import Citation, SessionLocal
from scripts.fix_common import chunked, count_lines, default_undo_path, read_undo_file, write_undo_file

COUNT_SQL = text("SELECT COUNT(*) FROM citations WHERE source_case_id = target_case_id")
BY_COURT_SQL = text(
	"SELECT coalesce(s.court, '(unknown)') AS court, COUNT(*) AS n FROM citations c "
	"JOIN cases s ON s.id = c.source_case_id WHERE c.source_case_id = c.target_case_id "
	"GROUP BY 1 ORDER BY n DESC, 1"
)
SAMPLE_SQL = text(
	"SELECT c.id, c.source_case_id, s.court, s.citation AS source_citation, c.citation_kind, c.citation_text "
	"FROM citations c JOIN cases s ON s.id = c.source_case_id "
	"WHERE c.source_case_id = c.target_case_id ORDER BY c.id LIMIT :limit"
)
FETCH_SQL = text(
	"SELECT * FROM citations WHERE source_case_id = target_case_id AND id > :after ORDER BY id LIMIT :limit"
)
EDGE_SQL = text("SELECT COUNT(*) FROM paragraph_citation_edges WHERE source_case_id = target_case_id")


def dry_run_report(db, sample: int) -> dict[str, Any]:
	total = int(db.execute(COUNT_SQL).scalar() or 0)
	by_court = [(row["court"], int(row["n"])) for row in db.execute(BY_COURT_SQL).mappings().all()]
	rows = [dict(row) for row in db.execute(SAMPLE_SQL, {"limit": sample}).mappings().all()]
	try:
		edges = int(db.execute(EDGE_SQL).scalar() or 0)
	except Exception:  # noqa: BLE001 - table may not exist on an old database
		db.rollback()
		edges = None
	return {"total": total, "by_court": by_court, "sample": rows, "self_paragraph_edges": edges}


def save_rows(db, undo_path: Path, batch_size: int) -> list[int]:
	"""Phase 1: copy every self-citation row (all columns) to the undo file. Returns the saved ids."""
	ids: list[int] = []

	def rows():
		after = 0
		while True:
			batch = [dict(r) for r in db.execute(FETCH_SQL, {"after": after, "limit": batch_size}).mappings().all()]
			if not batch:
				return
			after = batch[-1]["id"]
			ids.extend(r["id"] for r in batch)
			yield from batch

	written = write_undo_file(undo_path, rows())
	if written != len(ids) or count_lines(undo_path) != len(ids):
		raise RuntimeError(f"undo file check failed ({written} written, {len(ids)} read); nothing deleted")
	return ids


def delete_rows(db, ids: list[int], batch_size: int) -> int:
	"""Phase 2: delete the saved ids in batches, committing each batch. The WHERE re-checks the self link."""
	deleted = 0
	for batch in chunked(ids, batch_size):
		result = db.execute(
			delete(Citation).where(Citation.id.in_(list(batch)), Citation.source_case_id == Citation.target_case_id)
		)
		db.commit()
		deleted += result.rowcount or 0
	return deleted


def restore_rows(db, undo_path: Path, batch_size: int) -> int:
	"""Re-insert the saved rows with their original ids; rows whose id already exists are left alone."""
	restored = 0
	batch: list[dict[str, Any]] = []
	for row in read_undo_file(undo_path):
		batch.append(row)
		if len(batch) >= batch_size:
			restored += _insert(db, batch)
			batch = []
	if batch:
		restored += _insert(db, batch)
	return restored


def _insert(db, batch: list[dict[str, Any]]) -> int:
	result = db.execute(pg_insert(Citation.__table__).on_conflict_do_nothing(index_elements=["id"]), batch)
	db.commit()
	return result.rowcount or 0


def main(argv: list[str] | None = None) -> int:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Save the rows to an undo file, then delete them (default is a dry run).")
	parser.add_argument("--undo", type=Path, help="Restore the rows saved in this undo file.")
	parser.add_argument("--undo-file", type=Path, help="Where --apply writes the undo file (default data/db_fix_backups/, timestamped).")
	parser.add_argument("--expected-count", type=int, help="With --apply: stop unless exactly this many self-citations exist.")
	parser.add_argument("--batch-size", type=int, default=5000)
	parser.add_argument("--sample", type=int, default=15, help="Rows to show in the dry run.")
	args = parser.parse_args(argv)
	if args.batch_size < 1:
		parser.error("--batch-size must be at least 1")

	with SessionLocal() as db:
		if args.undo:
			print(f"restored={restore_rows(db, args.undo, args.batch_size)} from {args.undo}")
			print("Note: put-back rows count again in the live 'Cited by' numbers; citation_metrics ignores self links.")
			return 0
		report = dry_run_report(db, args.sample)
		print(f"self_citations={report['total']}")
		for court, count in report["by_court"]:
			print(f"  {count:8d}  {court}")
		for row in report["sample"]:
			print(f"  sample id={row['id']} case={row['source_case_id']} {row['court']} {row['source_citation']} "
			      f"[{row['citation_kind']}] {str(row['citation_text'])[:80]!r}")
		if report["self_paragraph_edges"]:
			print(f"paragraph_citation_edges self rows={report['self_paragraph_edges']}: rebuild with "
			      "scripts/build_paragraph_cited_by.py after the cleanup")
		if not args.apply:
			print("Dry run: nothing written. Add --apply (and --expected-count) to delete.")
			return 0
		if args.expected_count is not None and args.expected_count != report["total"]:
			print(f"Expected {args.expected_count} but found {report['total']}; nothing changed.")
			return 1
		undo_path = args.undo_file or default_undo_path("self_citations")
		ids = save_rows(db, undo_path, args.batch_size)
		print(f"undo file written: {undo_path} ({len(ids)} rows)")
		deleted = delete_rows(db, ids, args.batch_size)
		remaining = int(db.execute(COUNT_SQL).scalar() or 0)
		print(f"deleted={deleted} remaining_self_citations={remaining}")
		print("citation_metrics: no recompute needed (compute_citation_metrics already ignores self links).")
		print("Undo with: python scripts/fix_self_citations.py --undo", undo_path)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
