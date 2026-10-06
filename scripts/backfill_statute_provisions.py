"""Fill statute_references.provision_section/subsection/paragraph from the stored pinpoint.

The provision_* columns were added after most references were stored, so about 99.9% of
rows have a pinpoint such as "36(1)(a)" but an empty provision_section. Statute-consideration
queries filter on provision_section and so find almost nothing. This derives the columns from
the pinpoint with the same parser the extractor uses. It never changes the pinpoint, the
instrument or any other column, and only touches rows whose provision_section is still NULL.

Dry run by default (counts and samples only). Use --apply to write.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text

from backend.database import SessionLocal
from backend.statutes import parse_provision_identity

SELECT_SQL = text(
    "SELECT id, pinpoint FROM statute_references "
    "WHERE provision_section IS NULL AND pinpoint IS NOT NULL AND pinpoint <> '' AND id > :after "
    "ORDER BY id LIMIT :limit"
)
UPDATE_SQL = text(
    "UPDATE statute_references SET provision_section = :section, provision_subsection = :subsection, "
    "provision_paragraph = :paragraph, provision_nested_depth = :depth, provision_is_range_or_list = :is_list "
    "WHERE id = :id AND provision_section IS NULL"
)


def derive_provision_fields(row_id: int, pinpoint: str) -> dict[str, Any] | None:
    """Return the column values for one row, or None when the pinpoint has no usable section."""
    section, subsection, paragraph, depth, is_list = parse_provision_identity(pinpoint)
    if not section:
        return None
    return {
        "id": row_id,
        "section": section,
        "subsection": subsection,
        "paragraph": paragraph,
        "depth": depth,
        "is_list": is_list,
    }


def run(apply: bool, batch_size: int, max_rows: int | None) -> dict[str, Any]:
    stats: Counter[str] = Counter()
    samples: list[tuple[str, str | None, str | None, str | None]] = []
    after = 0
    with SessionLocal() as db:
        while max_rows is None or stats["seen"] < max_rows:
            rows = db.execute(SELECT_SQL, {"after": after, "limit": batch_size}).all()
            if not rows:
                break
            after = rows[-1][0]
            updates = []
            for row_id, pinpoint in rows:
                stats["seen"] += 1
                fields = derive_provision_fields(row_id, pinpoint)
                if fields is None:
                    stats["unparseable"] += 1
                    continue
                stats["parseable"] += 1
                if fields["is_list"]:
                    stats["range_or_list"] += 1
                if len(samples) < 25 and stats["parseable"] % 997 == 1:
                    samples.append((pinpoint, fields["section"], fields["subsection"], fields["paragraph"]))
                updates.append(fields)
            if apply and updates:
                db.execute(UPDATE_SQL, updates)
                db.commit()
                stats["updated"] += len(updates)
    return {"stats": dict(stats), "samples": samples}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the updates (default is a dry run)")
    parser.add_argument("--batch-size", type=int, default=20000)
    parser.add_argument("--max-rows", type=int, default=None, help="stop after this many candidate rows")
    args = parser.parse_args()
    result = run(args.apply, args.batch_size, args.max_rows)
    print("mode:", "APPLY" if args.apply else "dry run (no writes)")
    print("stats:", result["stats"])
    for pinpoint, section, subsection, paragraph in result["samples"]:
        print(f"  {pinpoint!r:28} -> section={section} subsection={subsection} paragraph={paragraph}")


if __name__ == "__main__":
    main()
