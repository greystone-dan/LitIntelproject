"""Measure pinpoints on refined citations, read-only (nothing is written).

The refined table does not store the pinpoint yet, so this re-runs the refiner on decisions that already have
refined rows and counts the rows that carry a pinpoint. It also counts the same for the first pass alone
(pass-one rows, pinpoints read only from the row's own text), which is the "before".

    python scripts/measure_refined_pinpoints.py --sample 500 --random-seed 7
    python scripts/measure_refined_pinpoints.py --sample 500 --csv pinpoint_measure.csv

Also checks that the stored refined row count for each decision matches a fresh run (a mismatch means the table
was built with older rules).
"""

from __future__ import annotations

import argparse
import csv
import random
import sys
from pathlib import Path

from sqlalchemy import func, select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citation_refine.cases import refine_case_citations
from backend.database import Case, CitationRefined, CitationRefineStatus, SessionLocal

CASE_KINDS = {"case", "neutral", "case_short"}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--sample", type=int, default=500, help="Decisions to measure (default 500).")
	parser.add_argument("--random-seed", type=int, default=7)
	parser.add_argument("--refine-version", type=int, default=1)
	parser.add_argument("--csv", type=Path, default=None, help="Write one line per decision here.")
	return parser.parse_args(argv)


def count_pinpoints(rows) -> tuple[int, int]:
	cited = [row for row in rows if row.kind in CASE_KINDS]
	return len(cited), sum(1 for row in cited if row.pinpoints)


def main(argv: list[str] | None = None) -> None:
	args = parse_args(argv)
	with SessionLocal() as session:
		ids = list(session.scalars(select(CitationRefineStatus.source_case_id).where(CitationRefineStatus.refine_version == args.refine_version)))
		random.Random(args.random_seed).shuffle(ids)
		ids = ids[: args.sample]
		totals = dict(decisions=0, first_rows=0, first_pin=0, new_rows=0, new_pin=0, stored_equal=0)
		lines = []
		for case_id in ids:
			case = session.get(Case, case_id)
			if case is None or not case.full_text:
				continue
			kwargs = dict(source_citations=[case.citation, case.secondary_citation], include_dockets=False, source_dockets=[case.docket_number])
			first = refine_case_citations(case.full_text, steps=["C4_pinpoints"], **kwargs).rows
			fresh = refine_case_citations(case.full_text, **kwargs).rows
			stored = session.scalar(
				select(func.count(CitationRefined.id)).where(CitationRefined.source_case_id == case_id, CitationRefined.refine_version == args.refine_version)
			) or 0
			first_rows, first_pin = count_pinpoints(first)
			new_rows, new_pin = count_pinpoints(fresh)
			totals["decisions"] += 1
			totals["first_rows"] += first_rows
			totals["first_pin"] += first_pin
			totals["new_rows"] += new_rows
			totals["new_pin"] += new_pin
			totals["stored_equal"] += stored == len(fresh)
			lines.append((case_id, case.citation, first_rows, first_pin, new_rows, new_pin, stored, len(fresh)))
			session.expire_all()
	if args.csv:
		with args.csv.open("w", newline="", encoding="utf-8") as handle:
			writer = csv.writer(handle)
			writer.writerow(["case_id", "citation", "first_pass_rows", "first_pass_with_pinpoint", "refined_rows", "refined_with_pinpoint", "stored_rows", "fresh_rows"])
			writer.writerows(lines)
	print(
		f"decisions={totals['decisions']} first_pass: rows={totals['first_rows']} with_pinpoint={totals['first_pin']} | "
		f"refined (current rules): rows={totals['new_rows']} with_pinpoint={totals['new_pin']} | "
		f"stored_row_count_matches_fresh_run={totals['stored_equal']}/{totals['decisions']}"
	)
	print("READ ONLY: nothing was written.")


if __name__ == "__main__":
	main()
