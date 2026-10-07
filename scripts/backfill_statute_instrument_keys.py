"""Fill statute_references.instrument_key for rows that name a registered act but were stored without a key.

About 59% of statute_references have no instrument_key, and most of those name an act the registry already
knows ("Patent Act", "Federal Court Rules", "Immigration and Refugee Protection Act, S.C. 2001, c. 27").
This resolves the act name with backend/instrument_resolver.py (exact normalized names only, court-aware for
names shared with provincial acts) and writes only the instrument_key column, only where it is still NULL.

Dry run by default (counts per instrument and samples). --apply first writes an undo file of every id and key
it is about to set; --undo FILE puts those rows back to NULL, only where the key is still the one written.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text

from backend.database import SessionLocal
from backend.instrument_resolver import resolve_instrument_key

SELECT_SQL = text(
    "SELECT r.id, coalesce(r.normalized_reference, r.reference_text), c.court "
    "FROM statute_references r LEFT JOIN cases c ON c.id = r.source_case_id "
    "WHERE r.instrument_key IS NULL AND r.id > :after ORDER BY r.id LIMIT :limit"
)
UPDATE_SQL = text("UPDATE statute_references SET instrument_key = :key WHERE id = :id AND instrument_key IS NULL")
UNDO_SQL = text("UPDATE statute_references SET instrument_key = NULL WHERE id = :id AND instrument_key = :key")
DEFAULT_UNDO = PROJECT_ROOT / "data" / "statute_instrument_backfill_undo.csv"


def run(apply: bool, batch_size: int, max_rows: int | None, undo_path: Path) -> dict[str, Any]:
    stats: Counter[str] = Counter()
    per_key: Counter[str] = Counter()
    samples: dict[str, str] = {}
    after = 0
    undo_file = None
    writer = None
    if apply:
        undo_path.parent.mkdir(parents=True, exist_ok=True)
        undo_file = open(undo_path, "w", newline="", encoding="utf-8")
        writer = csv.writer(undo_file)
        writer.writerow(["id", "instrument_key"])
    try:
        with SessionLocal() as db:
            while max_rows is None or stats["seen"] < max_rows:
                rows = db.execute(SELECT_SQL, {"after": after, "limit": batch_size}).all()
                if not rows:
                    break
                after = rows[-1][0]
                updates = []
                for row_id, reference, court in rows:
                    stats["seen"] += 1
                    key = resolve_instrument_key(reference, court)
                    if key is None:
                        stats["unresolved"] += 1
                        continue
                    stats["resolved"] += 1
                    per_key[key] += 1
                    samples.setdefault(key, str(reference)[:90])
                    updates.append({"id": row_id, "key": key})
                if apply and updates:
                    assert writer is not None and undo_file is not None
                    writer.writerows([[u["id"], u["key"]] for u in updates])
                    undo_file.flush()
                    db.execute(UPDATE_SQL, updates)
                    db.commit()
                    stats["updated"] += len(updates)
    finally:
        if undo_file is not None:
            undo_file.close()
    return {"stats": dict(stats), "per_key": per_key, "samples": samples}


def undo(path: Path) -> int:
    restored = 0
    with open(path, newline="", encoding="utf-8") as handle, SessionLocal() as db:
        batch: list[dict[str, Any]] = []
        for row in csv.DictReader(handle):
            batch.append({"id": int(row["id"]), "key": row["instrument_key"]})
            if len(batch) >= 5000:
                restored += db.execute(UNDO_SQL, batch).rowcount or 0
                batch = []
        if batch:
            restored += db.execute(UNDO_SQL, batch).rowcount or 0
        db.commit()
    return restored


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the keys (default is a dry run)")
    parser.add_argument("--undo", type=Path, help="restore NULL for the rows listed in this undo file")
    parser.add_argument("--undo-file", type=Path, default=DEFAULT_UNDO, help="where --apply writes the undo list")
    parser.add_argument("--batch-size", type=int, default=20000)
    parser.add_argument("--max-rows", type=int, default=None)
    args = parser.parse_args()
    if args.undo:
        print("restored to NULL:", undo(args.undo))
        return
    result = run(args.apply, args.batch_size, args.max_rows, args.undo_file)
    print("mode:", "APPLY" if args.apply else "dry run (no writes)")
    print("stats:", result["stats"])
    if args.apply:
        print("undo file:", args.undo_file)
    for key, count in result["per_key"].most_common():
        print(f"  {count:8d} {key:48s} e.g. {result['samples'][key]!r}")


if __name__ == "__main__":
    main()
