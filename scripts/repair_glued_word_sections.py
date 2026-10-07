"""Repair statute_references.provision_section values like "25s" or "2d" that came from a word glued to the number.

The stored pinpoint has its spaces removed, so "s. 25 ss. 3" or "S. 2(d)" read as section "25s" or "2d" in the first
backfill. Real lettered sections are uppercase ("224A", "83A", "1F", "39B") or lowercase before a bracket
("224a(1)"), so this touches only rows whose stored pinpoint has LOWERCASE letters straight after the digits and no
bracket, never rows of the Criminal Code or Income Tax Act (old lettered sections), and only when the section can be
read again from the cited text itself (reference_text: "section 20.1" -> 20.1, "S. 2d" -> 2). Rows where the
text gives no section are left alone. Dry run by default; --apply first writes an undo CSV (id, old section, new
section); --undo FILE restores the old values where the row still holds the new one.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text

from backend.database import SessionLocal

EXCLUDED_INSTRUMENTS = ("canada.criminal_code", "canada.income_tax_act")
SELECT_SQL = text(
    "SELECT id, instrument_key, pinpoint, coalesce(reference_text, normalized_reference, ''), provision_section "
    "FROM statute_references "
    "WHERE provision_section ~ '^[0-9]{1,3}([.][0-9]+)?[a-z]$' "
    "AND pinpoint ~ '^[0-9]{1,3}([.][0-9]+)?[a-z]+([.]|[0-9]|$)' "
    "AND (instrument_key IS NULL OR instrument_key NOT IN ('canada.criminal_code', 'canada.income_tax_act')) "
    "AND id > :after ORDER BY id LIMIT :limit"
)
UPDATE_SQL = text("UPDATE statute_references SET provision_section = :new WHERE id = :id AND provision_section = :old")
UNDO_SQL = text("UPDATE statute_references SET provision_section = :old WHERE id = :id AND provision_section = :new")
DEFAULT_UNDO = PROJECT_ROOT / "data" / "statute_glued_sections_undo.csv"

_SECTION_IN_TEXT = re.compile(
    r"\b(?:ss?|secs?|sections?|subsections?|paragraphs?|paras?)\b\.?\s*(\d{1,3}(?:\.\d+)?)(?![0-9])",
    re.IGNORECASE,
)


def section_from_reference(reference: str | None) -> str | None:
    """The first plain section number in the cited text, or None. A trailing lowercase letter is a word, not a suffix."""
    match = _SECTION_IN_TEXT.search(reference or "")
    return match.group(1) if match else None


def corrected_section(pinpoint: str, reference: str | None, old: str) -> str | None:
    """Return the repaired section, or None when the row should be left alone."""
    if not re.match(r"^[0-9]{1,3}(?:\.[0-9]+)?[a-z]+(?:[.]|[0-9]|$)", pinpoint or ""):
        return None
    new = section_from_reference(reference)
    if new is None or new == old:
        return None
    return new


def run(apply: bool, batch_size: int, undo_path: Path) -> dict[str, Any]:
    stats: Counter[str] = Counter()
    samples: list[tuple[str, str, str, str]] = []
    after = 0
    undo_file = writer = None
    if apply:
        undo_path.parent.mkdir(parents=True, exist_ok=True)
        undo_file = open(undo_path, "w", newline="", encoding="utf-8")
        writer = csv.writer(undo_file)
        writer.writerow(["id", "old_section", "new_section"])
    try:
        with SessionLocal() as db:
            while True:
                rows = db.execute(SELECT_SQL, {"after": after, "limit": batch_size}).all()
                if not rows:
                    break
                after = rows[-1][0]
                updates = []
                for row_id, instrument, pinpoint, reference, old in rows:
                    stats["seen"] += 1
                    new = corrected_section(pinpoint, reference, old)
                    if new is None:
                        stats["left_alone"] += 1
                        continue
                    stats["to_fix"] += 1
                    stats["agrees_with_pinpoint_digits" if new == old[:-1] else "text_differs_from_pinpoint"] += 1
                    if len(samples) < 30:
                        samples.append((str(reference)[:40], pinpoint, old, new))
                    updates.append({"id": row_id, "old": old, "new": new})
                if apply and updates:
                    assert writer is not None and undo_file is not None
                    writer.writerows([[u["id"], u["old"], u["new"]] for u in updates])
                    undo_file.flush()
                    db.execute(UPDATE_SQL, updates)
                    db.commit()
                    stats["updated"] += len(updates)
    finally:
        if undo_file is not None:
            undo_file.close()
    return {"stats": dict(stats), "samples": samples}


def undo(path: Path) -> int:
    restored = 0
    with open(path, newline="", encoding="utf-8") as handle, SessionLocal() as db:
        rows = [{"id": int(r["id"]), "old": r["old_section"], "new": r["new_section"]} for r in csv.DictReader(handle)]
        for start in range(0, len(rows), 5000):
            restored += db.execute(UNDO_SQL, rows[start : start + 5000]).rowcount or 0
        db.commit()
    return restored


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the repairs (default is a dry run)")
    parser.add_argument("--undo", type=Path, help="restore the old sections listed in this undo file")
    parser.add_argument("--undo-file", type=Path, default=DEFAULT_UNDO)
    parser.add_argument("--batch-size", type=int, default=20000)
    args = parser.parse_args()
    if args.undo:
        print("restored:", undo(args.undo))
        return
    result = run(args.apply, args.batch_size, args.undo_file)
    print("mode:", "APPLY" if args.apply else "dry run (no writes)")
    print("stats:", result["stats"])
    for reference, pinpoint, old, new in result["samples"]:
        print(f"  {reference!r:44} pinpoint={pinpoint!r:12} {old} -> {new}")


if __name__ == "__main__":
    main()
