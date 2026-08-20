"""Remove false-positive self-case short-form citation rows.

Dry-run is the default. Use --apply only after reviewing the reported count.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from sqlalchemy import delete, select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import RawCitationMatch, is_self_case_name_match
from backend.database import Case, Citation, SessionLocal


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Delete matching rows and commit changes")
    parser.add_argument("--batch-size", type=int, default=1000, help="Cases to scan per batch")
    return parser.parse_args()


def find_matching_ids(session, batch_size: int) -> list[int]:
    matching_ids: list[int] = []
    last_case_id = 0
    while True:
        cases = list(
            session.scalars(
                select(Case)
                .where(Case.id > last_case_id)
                .order_by(Case.id)
                .limit(batch_size)
            )
        )
        if not cases:
            break
        case_ids = [case.id for case in cases]
        titles = {case.id: case.title for case in cases}
        rows = session.execute(
            select(Citation.id, Citation.citation_kind, Citation.citation_text, Citation.normalized_citation, Citation.offset_start, Citation.offset_end, Citation.source_case_id)
            .where(Citation.source_case_id.in_(case_ids), Citation.citation_kind.in_(["case_short", "case_name"]))
        )
        for row in rows:
            match = RawCitationMatch(
                kind=row.citation_kind,
                citation_text=row.citation_text or "",
                normalized_citation=row.normalized_citation or "",
                offset_start=row.offset_start or 0,
                offset_end=row.offset_end or 0,
            )
            if is_self_case_name_match(titles.get(row.source_case_id), match):
                matching_ids.append(row.id)
        last_case_id = cases[-1].id
    return matching_ids


def main() -> None:
    args = parse_args()
    if args.batch_size < 1:
        raise SystemExit("--batch-size must be at least 1")
    with SessionLocal() as session:
        matching_ids = find_matching_ids(session, args.batch_size)
        print(f"matching_rows={len(matching_ids)}")
        if not args.apply:
            print("dry_run=true; no rows changed")
            return
        deleted = 0
        for start in range(0, len(matching_ids), 5000):
            chunk = matching_ids[start : start + 5000]
            session.execute(delete(Citation).where(Citation.id.in_(chunk)))
            session.commit()
            deleted += len(chunk)
        print(f"deleted_rows={deleted}")


if __name__ == "__main__":
    main()
