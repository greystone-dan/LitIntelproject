"""Refresh the stored "cited by" numbers (citation_metrics). Dry run by default.

The stored in_degree was last computed before many citation links were added or cleaned (Baker showed 0 with
about 2,900 citing cases), and counted citation rows. It now counts distinct citing cases, as search does.

  python scripts/recompute_citation_metrics.py            # dry run: stored vs live for sample cases and totals
  python scripts/recompute_citation_metrics.py --apply    # recompute and write all rows (needs Daniel's go)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import func, select

from backend.citations import compute_citation_metrics
from backend.database import Case, Citation, CitationMetrics, SessionLocal

SAMPLE_IDS = (35874, 35899, 35862, 35870, 10643, 38474, 61426)  # Vavilov, Baker, Chieu, Ezokola, FC/FCA/new FC


def live_in_degree(session, case_id: int) -> int:
	return int(
		session.scalar(
			select(func.count(func.distinct(Citation.source_case_id))).where(
				Citation.target_case_id == case_id, Citation.source_case_id != case_id
			)
		)
		or 0
	)


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Recompute and write citation_metrics.")
	args = parser.parse_args()

	with SessionLocal() as session:
		print("case_id  citation            stored in_degree -> live distinct citing cases")
		for case_id in SAMPLE_IDS:
			case = session.get(Case, case_id)
			if case is None:
				continue
			stored = session.scalar(select(CitationMetrics.in_degree).where(CitationMetrics.case_id == case_id))
			print(f"{case_id:<8} {str(case.citation)[:18]:<19} {stored!s:>8} -> {live_in_degree(session, case_id)}")
		total = session.scalar(select(func.count()).select_from(CitationMetrics))
		print(f"citation_metrics rows: {total}")
		if not args.apply:
			print("Dry run: nothing written. Add --apply to recompute all rows.")
			return
		updated = compute_citation_metrics(session)
		print(f"Recomputed {updated} cases.")


if __name__ == "__main__":
	main()
