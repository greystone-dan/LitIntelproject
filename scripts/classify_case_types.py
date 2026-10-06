"""Label every decision with its case type (deterministic rules, no AI). Dry run by default.

  python scripts/classify_case_types.py --limit 200                 # dry run: print counts only
  python scripts/classify_case_types.py --court FC --apply          # write rows to case_type_labels
  python scripts/classify_case_types.py --revert                    # delete rows of this taxonomy version

Only reads `cases` and writes `case_type_labels`. Resumable: decisions that already have a row for the
current taxonomy version are skipped.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import delete, select

from backend.case_types import TAXONOMY_VERSION, classify_text
from backend.database import Case, CaseTypeLabel, SessionLocal


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Write rows (needs Daniel's go for the live database).")
	parser.add_argument("--revert", action="store_true", help="Delete rows for the current taxonomy version.")
	parser.add_argument("--court", help="Only decisions whose court column equals this value (for example FC).")
	parser.add_argument("--limit", type=int, default=0, help="Stop after this many decisions (0 = all).")
	parser.add_argument("--batch", type=int, default=200)
	parser.add_argument("--sample", type=int, default=0, help="Pick this many decisions at random (use with --seed) instead of the lowest ids.")
	parser.add_argument("--seed", type=int, default=1, help="Random seed for --sample.")
	parser.add_argument("--show-reasons", action="store_true", help="Also print why decisions were not_immigration or unclear.")
	args = parser.parse_args()

	with SessionLocal() as session:
		if args.revert:
			removed = session.execute(delete(CaseTypeLabel).where(CaseTypeLabel.taxonomy_version == TAXONOMY_VERSION)).rowcount
			session.commit()
			print(f"Removed {removed} rows for {TAXONOMY_VERSION}.")
			return
		done = select(CaseTypeLabel.case_id).where(CaseTypeLabel.taxonomy_version == TAXONOMY_VERSION)
		query = select(Case.id).where(Case.id.not_in(done)).order_by(Case.id)
		if args.court:
			query = query.where(Case.court == args.court)
		ids = list(session.scalars(query))
		if args.sample:
			import random
			ids = random.Random(args.seed).sample(ids, min(args.sample, len(ids)))
		elif args.limit:
			ids = ids[: args.limit]
		counts: Counter = Counter()
		reasons: Counter = Counter()
		for start in range(0, len(ids), args.batch):
			for case in session.scalars(select(Case).where(Case.id.in_(ids[start:start + args.batch]))):
				result = classify_text(case.full_text, court=case.court, title=case.title, docket=case.docket_number,
				                       source_citations=[case.citation])
				counts[result.primary_type or result.status] += 1
				if args.show_reasons and not result.primary_type:
					reasons[f"{case.court} {result.status}: {result.reason[:70]}"] += 1
				if args.apply:
					session.add(CaseTypeLabel(
						case_id=case.id, taxonomy_version=TAXONOMY_VERSION, status=result.status,
						primary_type=result.primary_type, primary_detail=result.primary_detail,
						secondary_types=result.secondary_types, second_type=result.second_type, second_detail=result.second_detail, proceeding=result.proceeding, issues=result.issues,
						confidence=result.confidence, scores=result.scores, evidence=result.evidence,
					))
			if args.apply:
				session.commit()
			session.expire_all()
		print(("Applied" if args.apply else "Dry run (nothing written)") + f": {len(ids)} decisions")
		for label, count in counts.most_common():
			print(f"{count:7d}  {label}")
		for label, count in reasons.most_common(12):
			print(f"{count:7d}  [{label}]")


if __name__ == "__main__":
	main()
