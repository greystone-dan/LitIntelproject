"""List or delete the 20 placeholder "TEST CASE" decisions (ids 61264 to 61283) from the library. Dry run by default.

  python scripts/remove_test_cases.py            # dry run: show the exact rows and what hangs off them
  python scripts/remove_test_cases.py --apply    # delete them (needs Daniel's go for the live database)

Only ids 61264-61283 can ever be touched, and only if every one still looks like a test row (title starts with
"TEST CASE", citation contains "TEST" and a number). The script refuses to delete anything if another decision
cites one of them, or if a row does not look like a test row.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import func, select

from backend.database import Case, CaseChunk, Citation, SessionLocal

TEST_IDS = tuple(range(61264, 61284))
TEST_CITATION_RE = re.compile(r"TEST\d+", re.IGNORECASE)


def looks_like_test_row(case: Case) -> bool:
	return (case.title or "").startswith("TEST CASE") and bool(TEST_CITATION_RE.search(case.citation or ""))


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Delete the rows (after all checks pass).")
	args = parser.parse_args()

	with SessionLocal() as session:
		cases = list(session.scalars(select(Case).where(Case.id.in_(TEST_IDS)).order_by(Case.id)))
		print(f"Found {len(cases)} of {len(TEST_IDS)} expected rows (ids {TEST_IDS[0]}-{TEST_IDS[-1]}):")
		problems: list[str] = []
		for case in cases:
			cited_by_others = session.scalar(
				select(func.count()).select_from(Citation).where(
					Citation.target_case_id == case.id, Citation.source_case_id != case.id
				)
			)
			own_citations = session.scalar(
				select(func.count()).select_from(Citation).where(Citation.source_case_id == case.id)
			)
			chunks = session.scalar(select(func.count()).select_from(CaseChunk).where(CaseChunk.case_id == case.id))
			print(
				f"  {case.id}  {case.court!r}  {case.date}  {case.citation!r}  {(case.title or '')[:50]!r}"
				f"  chunks={chunks} own_citations={own_citations} cited_by_others={cited_by_others}"
			)
			if not looks_like_test_row(case):
				problems.append(f"{case.id} does not look like a test row")
			if cited_by_others:
				problems.append(f"{case.id} is cited by {cited_by_others} other citation rows")
		if problems:
			print("\nRefusing to delete:")
			for problem in problems:
				print("  -", problem)
			sys.exit(1)
		if not args.apply:
			print("\nDry run: nothing deleted. Add --apply to delete these rows.")
			return
		for case in cases:
			session.delete(case)
		session.commit()
		print(f"\nDeleted {len(cases)} rows.")


if __name__ == "__main__":
	main()
