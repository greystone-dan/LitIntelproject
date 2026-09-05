"""Backfill the dedicated deterministic outcome table in bounded batches."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from sqlalchemy import exists, select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseOutcome, SessionLocal
from backend.metadata_outcomes import OUTCOME_CLASSIFIER_VERSION, build_case_outcome


def backfill(*, limit: int | None = None, batch_size: int = 100, dry_run: bool = False) -> tuple[int, int]:
	if batch_size < 1:
		raise ValueError("batch_size must be at least 1")
	if limit is not None and limit < 1:
		raise ValueError("limit must be at least 1")
	with SessionLocal() as db:
		completed = exists(
			select(CaseOutcome.id).where(
				CaseOutcome.case_id == Case.id,
				CaseOutcome.classifier_version == OUTCOME_CLASSIFIER_VERSION,
			)
		)
		cases = db.scalars(select(Case).where(~completed).order_by(Case.id).limit(limit or 1000000)).all()
		if dry_run:
			count = sum(
				1
				for case in cases
				if build_case_outcome(
					case.full_text or case.summary or "",
					dict((case.metadata_json or {}).get("reader_extracted") or {}),
				)
			)
			return len(cases), count
		processed = 0
		for start in range(0, len(cases), batch_size):
			batch = cases[start : start + batch_size]
			for case in batch:
				metadata = dict(case.metadata_json or {})
				extracted = dict(metadata.get("reader_extracted") or {})
				db.add(CaseOutcome(case_id=case.id, **build_case_outcome(case.full_text or case.summary or "", extracted)))
			db.commit()
			processed += len(batch)
		return processed, processed


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--limit", type=int)
	parser.add_argument("--batch-size", type=int, default=100)
	parser.add_argument("--dry-run", action="store_true")
	args = parser.parse_args()
	cases, rows = backfill(limit=args.limit, batch_size=args.batch_size, dry_run=args.dry_run)
	print(f"cases={cases} outcome_rows={rows} dry_run={args.dry_run} classifier={OUTCOME_CLASSIFIER_VERSION}")


if __name__ == "__main__":
	main()