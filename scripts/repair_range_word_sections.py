"""Repair statute_references.provision_section values like "34t" that came from "34 to 37".

The first backfill read the "t" of "to" (or the "a" of "and") as a section suffix, so a range or
list pinpoint such as "34 to 37" was stored with provision_section "34t". This re-derives only the
rows whose section ends in a letter and whose pinpoint runs the section straight into "to", "and"
or "th"; it changes a row only when the corrected section is the old one minus that letter.
Dry run by default; --apply writes. Safe to run twice.
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
    "SELECT id, pinpoint, provision_section FROM statute_references "
    "WHERE provision_section ~ '^[0-9]{1,3}([.][0-9]+)?[a-z]$' AND pinpoint ~* '^[[:space:]]*[0-9]{1,3}([.][0-9]+)?[[:space:]]*(to|and|th)' "
    "AND id > :after ORDER BY id LIMIT :limit"
)
UPDATE_SQL = text(
    "UPDATE statute_references SET provision_section = :section WHERE id = :id AND provision_section = :old"
)


def corrected_section(pinpoint: str, old_section: str) -> str | None:
    """Return the repaired section, or None when the row should be left alone."""
    section = parse_provision_identity(pinpoint)[0]
    if section and section == old_section[:-1]:
        return section
    return None


def run(apply: bool, batch_size: int) -> dict[str, Any]:
    stats: Counter[str] = Counter()
    samples: list[tuple[str, str, str]] = []
    after = 0
    with SessionLocal() as db:
        while True:
            rows = db.execute(SELECT_SQL, {"after": after, "limit": batch_size}).all()
            if not rows:
                break
            after = rows[-1][0]
            updates = []
            for row_id, pinpoint, old in rows:
                stats["seen"] += 1
                new = corrected_section(pinpoint, old)
                if new is None:
                    stats["left_alone"] += 1
                    continue
                stats["to_fix"] += 1
                if len(samples) < 25:
                    samples.append((pinpoint, old, new))
                updates.append({"id": row_id, "section": new, "old": old})
            if apply and updates:
                db.execute(UPDATE_SQL, updates)
                db.commit()
                stats["updated"] += len(updates)
    return {"stats": dict(stats), "samples": samples}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the repairs (default is a dry run)")
    parser.add_argument("--batch-size", type=int, default=20000)
    args = parser.parse_args()
    result = run(args.apply, args.batch_size)
    print("mode:", "APPLY" if args.apply else "dry run (no writes)")
    print("stats:", result["stats"])
    for pinpoint, old, new in result["samples"]:
        print(f"  {pinpoint!r:28} {old} -> {new}")


if __name__ == "__main__":
    main()
