"""Re-extract statute references with the current rules; dry run compares, apply replaces.

Why: older extraction dropped decimal sections ("18.1" stored as "18") and mis-handled lists. This
reads the same text the original build used (the preferred chunk set, else full text), runs the
current extractor, and compares with the stored rows of the same cases.

Dry run (default) writes nothing: it reports counts before and after (rows, rows with an
instrument, decimal sections, list rows, rows per instrument) and sample changes.
--apply with --confirm-statute-reextract first writes every old row of each case to a JSONL
backup file, then replaces that case's rows (one transaction per batch). Restore: scripts that
read the backup file, or re-insert rows from it; the backup holds every column.
Cases are chosen by --case-id, or by a seeded random sample (--sample N --seed S), or --all.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import delete, select

from backend.citations import (
    court_defaults_to_irpa,
    _preferred_case_chunks,
    extract_statute_reference_matches,
    rebuild_statute_references_for_case,
)
from backend.database import Case, CaseChunk, SessionLocal, StatuteReference
from backend.statutes import parse_legislation_citation

BACKUP_COLUMNS = [column.name for column in StatuteReference.__table__.columns]


def new_rows_for_texts(texts: list[str], court: str | None = None) -> list[dict[str, Any]]:
    """Run the current extractor over each text and return plain row dicts."""
    rows: list[dict[str, Any]] = []
    for text in texts:
        for match in extract_statute_reference_matches(text, default_irpa=court_defaults_to_irpa(court)):
            parsed = parse_legislation_citation(match.normalized_citation or match.citation_text)
            rows.append(
                {
                    "instrument_key": parsed.instrument_key if parsed else None,
                    "pinpoint": parsed.pinpoint if parsed else None,
                    "provision_section": parsed.section if parsed else None,
                    "provision_is_range_or_list": bool(parsed.is_range_or_list) if parsed else False,
                }
            )
    return rows


def summarize(rows: list[dict[str, Any]]) -> Counter[str]:
    stats: Counter[str] = Counter()
    for row in rows:
        stats["rows"] += 1
        if row.get("instrument_key"):
            stats["with_instrument"] += 1
            stats[f"instrument:{row['instrument_key']}"] += 1
        section = row.get("provision_section") or ""
        if "." in section:
            stats["decimal_sections"] += 1
        if row.get("provision_is_range_or_list"):
            stats["list_rows"] += 1
    return stats


def row_key(row: dict[str, Any]) -> tuple[Any, ...]:
    return (row.get("instrument_key"), (row.get("pinpoint") or "").lower())


def diff_case(old: list[dict[str, Any]], new: list[dict[str, Any]]) -> dict[str, int]:
    old_keys, new_keys = Counter(row_key(r) for r in old), Counter(row_key(r) for r in new)
    return {
        "added": sum((new_keys - old_keys).values()),
        "removed": sum((old_keys - new_keys).values()),
        "unchanged": sum((old_keys & new_keys).values()),
    }


def select_case_ids(db, case_ids: list[int], sample: int | None, seed: int, include_all: bool, limit: int) -> list[int]:
    if case_ids:
        return sorted(case_ids)
    ids = list(db.scalars(select(Case.id).where(Case.full_text.is_not(None)).order_by(Case.id)))
    if include_all:
        return ids[:limit]
    ids.sort(key=lambda cid: hashlib.md5(f"{seed}:{cid}".encode()).hexdigest())
    return sorted(ids[: sample or 0])


def case_texts(db, case: Case) -> list[str]:
    chunks = list(db.scalars(select(CaseChunk).where(CaseChunk.case_id == case.id)))
    selected = _preferred_case_chunks(chunks)
    if selected:
        return [chunk.text or "" for chunk in selected]
    return [case.full_text or case.summary or ""]


def stored_rows(db, case_id: int) -> list[dict[str, Any]]:
    result = db.execute(select(StatuteReference).where(StatuteReference.source_case_id == case_id)).scalars()
    return [{name: getattr(row, name) for name in BACKUP_COLUMNS} for row in result]


def run(case_ids: list[int], apply: bool, backup_path: Path | None, batch_size: int) -> dict[str, Any]:
    before: Counter[str] = Counter()
    after: Counter[str] = Counter()
    changes: Counter[str] = Counter()
    samples: list[dict[str, Any]] = []
    with SessionLocal() as db:
        backup = backup_path.open("a", encoding="utf-8") if apply and backup_path else None
        try:
            for index, case_id in enumerate(case_ids, 1):
                case = db.get(Case, case_id)
                if case is None:
                    changes["case_missing"] += 1
                    continue
                old = stored_rows(db, case_id)
                new = new_rows_for_texts(case_texts(db, case), case.court)
                before.update(summarize(old))
                after.update(summarize(new))
                diff = diff_case(old, new)
                changes.update(diff)
                if (diff["added"] or diff["removed"]) and len(samples) < 20:
                    samples.append({"case_id": case_id, **diff})
                if apply:
                    if backup is not None:
                        backup.write(json.dumps({"case_id": case_id, "rows": old}, default=str) + "\n")
                        backup.flush()
                    rebuild_statute_references_for_case(db, case)
                    changes["cases_rebuilt"] += 1
                    if index % batch_size == 0:
                        db.commit()
            if apply:
                db.commit()
        finally:
            if backup is not None:
                backup.close()
    return {"before": dict(before), "after": dict(after), "changes": dict(changes), "samples": samples}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-id", type=int, action="append", default=[])
    parser.add_argument("--sample", type=int, default=None, help="seeded random sample of this many cases")
    parser.add_argument("--seed", type=int, default=20261006)
    parser.add_argument("--all", action="store_true", help="every case with text, up to --limit")
    parser.add_argument("--limit", type=int, default=100000)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--confirm-statute-reextract", action="store_true", help="required with --apply")
    parser.add_argument("--backup", type=Path, default=PROJECT_ROOT / "data" / "statute_references_backup.jsonl")
    parser.add_argument("--batch-size", type=int, default=50)
    args = parser.parse_args()
    if not (args.case_id or args.sample or args.all):
        parser.error("choose --case-id, --sample N or --all")
    if args.apply and not args.confirm_statute_reextract:
        parser.error("--apply needs --confirm-statute-reextract")
    with SessionLocal() as db:
        case_ids = select_case_ids(db, args.case_id, args.sample, args.seed, args.all, args.limit)
    if args.apply:
        args.backup.parent.mkdir(parents=True, exist_ok=True)
    result = run(case_ids, args.apply, args.backup if args.apply else None, args.batch_size)
    print("mode:", "APPLY" if args.apply else "dry run (no writes)", "cases:", len(case_ids))
    for key in ("before", "after", "changes"):
        print(key + ":", json.dumps(result[key], sort_keys=True))
    for sample in result["samples"]:
        print("  changed:", sample)


if __name__ == "__main__":
    main()
