"""Build side-by-side refined case citations (second-pass extraction) for decisions.

Writes only to the new tables `citations_refined` and `citation_refine_status`;
the live `citations` table is never touched, so the site keeps reading pass-one
data. DRY RUN BY DEFAULT: nothing is written without `--apply`.

    python scripts/build_refined_citations.py --limit 500            # dry run: counts and a compare to pass one
    python scripts/build_refined_citations.py --limit 500 --apply    # write the first 500 decisions
    python scripts/build_refined_citations.py --language fr --random-seed 1 --limit 500   # random French sample, dry run
    python scripts/build_refined_citations.py --apply --court FC     # continue (resumable; skips done decisions)
    python scripts/build_refined_citations.py --revert --yes         # delete all refined rows and status rows for this version

One decision per transaction, resumable (decisions with a status row for the
same refine version are skipped), capped by --limit, with an optional stop file
checked between decisions. Docket rows are not stored (no column for them yet).
Statute references and paragraph links are a later step.
"""

from __future__ import annotations

import argparse
import random
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import delete, func, select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citation_refine.cases import refine_case_citations
from backend.database import Case, Citation, CitationRefined, CitationRefineStatus, SessionLocal

REFINE_VERSION = 1
PROVENANCE = "refine_v1"
CASE_KINDS = ("neutral", "case", "case_short", "case_name")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Write rows. Without it nothing is written.")
	parser.add_argument("--limit", type=int, default=500, help="Maximum decisions to process this run (default 500).")
	parser.add_argument("--court", default=None, help="Only this court (FC, FCA, SCC, RPD ...).")
	parser.add_argument("--case-id", type=int, action="append", default=None, help="Only these decision ids (repeatable).")
	parser.add_argument("--language", choices=("en", "fr"), default=None, help="Only decisions tagged with this language.")
	parser.add_argument("--random-seed", type=int, default=None, help="Pick decisions in a seeded random order instead of lowest id first.")
	parser.add_argument("--start-after-id", type=int, default=0)
	parser.add_argument("--sleep", type=float, default=0.0, help="Seconds to pause between decisions.")
	parser.add_argument("--stop-file", type=Path, default=None, help="Stop cleanly when this file exists.")
	parser.add_argument("--refine-version", type=int, default=REFINE_VERSION)
	parser.add_argument("--revert", action="store_true", help="Delete refined rows and status rows for the version.")
	parser.add_argument("--yes", action="store_true", help="Confirm --revert.")
	return parser.parse_args(argv)


def refined_rows_for(case: Case):
	"""Case-layer refinement for one decision, without docket rows."""
	result = refine_case_citations(
		case.full_text,
		source_citations=[case.citation, case.secondary_citation],
		include_dockets=False,
		source_dockets=[case.docket_number],
	)
	return result.rows


def build_for_case(session, case: Case, version: int, apply: bool) -> tuple[int, int]:
	"""Return (refined row count, pass-one row count). Writes only when apply is true."""
	rows = refined_rows_for(case)
	first_pass = session.scalar(
		select(func.count(Citation.id)).where(Citation.source_case_id == case.id, Citation.citation_kind.in_(CASE_KINDS))
	) or 0
	if apply:
		session.execute(delete(CitationRefined).where(CitationRefined.source_case_id == case.id, CitationRefined.refine_version == version))
		for row in rows:
			session.add(
				CitationRefined(
					source_case_id=case.id,
					citation_kind=row.kind,
					citation_text=row.citation_text,
					normalized_citation=row.normalized_citation,
					anchor_citation_text=row.anchor_citation_text,
					anchor_offset_start=row.anchor_offset_start,
					anchor_offset_end=row.anchor_offset_end,
					declared_alias=(row.declared_alias or None) and row.declared_alias[:255],
					provenance=PROVENANCE,
					offset_start=row.offset_start,
					offset_end=row.offset_end,
					unresolved=True,
					refine_step=row.step,
					confidence=row.confidence,
					refine_version=version,
				)
			)
		status = session.get(CitationRefineStatus, case.id)
		if status is None:
			status = CitationRefineStatus(source_case_id=case.id, refine_version=version, status="done", case_rows=0, statute_rows=0)
			session.add(status)
		status.refine_version, status.status = version, "done"
		status.case_rows, status.statute_rows = len(rows), 0
		status.processed_at = datetime.now(timezone.utc)
		session.commit()
	return len(rows), first_pass


def revert(session, version: int) -> tuple[int, int]:
	rows = session.execute(delete(CitationRefined).where(CitationRefined.refine_version == version)).rowcount
	statuses = session.execute(delete(CitationRefineStatus).where(CitationRefineStatus.refine_version == version)).rowcount
	session.commit()
	return rows or 0, statuses or 0


def main(argv: list[str] | None = None) -> None:
	args = parse_args(argv)
	if args.limit < 1:
		raise SystemExit("--limit must be at least 1")
	with SessionLocal() as session:
		if args.revert:
			if not args.yes:
				raise SystemExit("--revert deletes refined rows; add --yes to confirm")
			rows, statuses = revert(session, args.refine_version)
			print(f"reverted refine_version={args.refine_version} rows_deleted={rows} status_rows_deleted={statuses}")
			return
		done = select(CitationRefineStatus.source_case_id).where(CitationRefineStatus.refine_version == args.refine_version)
		query = select(Case.id).where(Case.id > args.start_after_id, Case.full_text.is_not(None), Case.id.not_in(done)).order_by(Case.id)
		if args.court:
			query = query.where(Case.court == args.court)
		if args.language:
			query = query.where(Case.language == args.language)
		if args.case_id:
			query = query.where(Case.id.in_(args.case_id))
		if args.random_seed is None:
			case_ids = list(session.scalars(query.limit(args.limit)))
		else:
			candidates = list(session.scalars(query))
			random.Random(args.random_seed).shuffle(candidates)
			case_ids = candidates[: args.limit]
		processed = refined_total = first_total = zero_before = zero_after = 0
		for case_id in case_ids:
			if args.stop_file is not None and args.stop_file.exists():
				print(f"stop file found, stopping after {processed} decisions")
				break
			case = session.get(Case, case_id)
			refined, first_pass = build_for_case(session, case, args.refine_version, args.apply)
			processed += 1
			refined_total += refined
			first_total += first_pass
			zero_before += first_pass == 0
			zero_after += refined == 0
			session.expire_all()
			if processed % 100 == 0:
				print(f"processed={processed} refined_rows={refined_total} first_pass_rows={first_total} last_id={case_id}")
			if args.sleep:
				time.sleep(args.sleep)
		print(
			f"{'APPLIED' if args.apply else 'DRY RUN (nothing written)'} decisions={processed} refined_rows={refined_total} "
			f"first_pass_rows={first_total} decisions_with_no_rows_first_pass={zero_before} decisions_with_no_rows_refined={zero_after}"
		)


if __name__ == "__main__":
	main()
