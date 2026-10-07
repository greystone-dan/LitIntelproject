"""Re-extract statute references with the current rules; dry run compares, apply replaces.

Why: older extraction dropped decimal sections ("18.1" stored as "18") and mis-handled lists. This
reads the same text the original build used (the preferred chunk set, else full text), runs the
current extractor, and compares with the stored rows of the same cases.

Dry run (default) writes nothing: it reports counts before and after (rows, rows with an
instrument, decimal sections, list rows, rows per instrument) and sample changes.
--apply with --confirm-statute-reextract first writes every old row of each case to a JSONL
backup file, then replaces that case's rows (one transaction per batch).
--restore BACKUP puts the backed-up rows back (every column, original ids): for each case in the
file it deletes the case's current rows and re-inserts the saved ones. If a case appears more than
once in the file (re-runs append), the first entry, the oldest rows, is used. --restore-dry-run
reports what it would do.
Cases are chosen by --case-id, or by a seeded random sample (--sample N --seed S), or --all;
--skip-cases-in BACKUP drops cases a previous apply already backed up (the rest after a first tranche).
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
    irpa_mode_for,
    extract_statute_reference_matches,
    rebuild_statute_references_for_case,
)
from backend.database import Case, SessionLocal, StatuteReference
from backend.statutes import parse_legislation_citation

BACKUP_COLUMNS = [column.name for column in StatuteReference.__table__.columns]


def new_rows_for_texts(texts: list[str], court: str | None = None) -> list[dict[str, Any]]:
    """Run the current extractor over each text and return plain row dicts."""
    rows: list[dict[str, Any]] = []
    for text in texts:
        for match in extract_statute_reference_matches(text, default_irpa=irpa_mode_for(court, text)):
            parsed = parse_legislation_citation(match.normalized_citation or match.citation_text)
            rows.append(
                {
                    "instrument_key": parsed.instrument_key if parsed else None,
                    "pinpoint": parsed.pinpoint if parsed else None,
                    "provision_section": parsed.section if parsed else None,
                    "provision_is_range_or_list": bool(parsed.is_range_or_list) if parsed else False,
                    "reference_text": match.citation_text,
                    "normalized_reference": match.normalized_citation,
                    "offset_start": match.offset_start,
                    "offset_end": match.offset_end,
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


def diff_rows(old: list[dict[str, Any]], new: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """The old rows the new run no longer produces, and the new rows the old run lacked (same key rule as diff_case)."""
    def leftovers(rows: list[dict[str, Any]], other: list[dict[str, Any]]) -> list[dict[str, Any]]:
        budget = Counter(row_key(r) for r in other)
        left: list[dict[str, Any]] = []
        for row in rows:
            key = row_key(row)
            if budget[key] > 0:
                budget[key] -= 1
            else:
                left.append(row)
        return left

    return leftovers(old, new), leftovers(new, old)


def context_of(text: str, start: Any, end: Any, width: int = 110) -> str:
    if not isinstance(start, int) or not isinstance(end, int):
        return ""
    return " ".join(text[max(0, start - width) : end + width].split())


def detail_record(case_id: int, text: str, old: list[dict[str, Any]], new: list[dict[str, Any]]) -> dict[str, Any]:
    removed, added = diff_rows(old, new)

    def shape(row: dict[str, Any]) -> dict[str, Any]:
        return {
            "text": row.get("reference_text"),
            "normalized": row.get("normalized_reference"),
            "instrument_key": row.get("instrument_key"),
            "pinpoint": row.get("pinpoint"),
            "context": context_of(text, row.get("offset_start"), row.get("offset_end")),
        }

    return {"case_id": case_id, "removed": [shape(r) for r in removed], "added": [shape(r) for r in added]}


def select_case_ids(db, case_ids: list[int], sample: int | None, seed: int, include_all: bool, limit: int) -> list[int]:
    if case_ids:
        return sorted(case_ids)
    ids = list(db.scalars(select(Case.id).where(Case.full_text.is_not(None)).order_by(Case.id)))
    if include_all:
        return ids[:limit]
    ids.sort(key=lambda cid: hashlib.md5(f"{seed}:{cid}".encode()).hexdigest())
    return sorted(ids[: sample or 0])


def case_texts(db, case: Case) -> list[str]:
    """The text the stored rows were built from: the full text (their chunk_id is NULL).

    The "section" chunk set holds only headings for many decisions, so extracting from chunks would
    miss nearly every reference; the apply step also rebuilds from the full text.
    """
    return [case.full_text or case.summary or ""]


def stored_rows(db, case_id: int) -> list[dict[str, Any]]:
    result = db.execute(select(StatuteReference).where(StatuteReference.source_case_id == case_id)).scalars()
    return [{name: getattr(row, name) for name in BACKUP_COLUMNS} for row in result]


def read_backup(path: Path) -> dict[int, list[dict[str, Any]]]:
    """case_id -> saved rows; the first entry per case wins (it holds the pre-re-extraction rows)."""
    saved: dict[int, list[dict[str, Any]]] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            saved.setdefault(int(record["case_id"]), record["rows"])
    return saved


def restore(backup_path: Path, apply: bool, case_ids: list[int] | None = None, batch_size: int = 50) -> dict[str, int]:
    """Replace each backed-up case's current rows with the saved rows. Writes only when apply is true."""
    saved = read_backup(backup_path)
    wanted = sorted(saved) if not case_ids else [cid for cid in sorted(case_ids) if cid in saved]
    counts: Counter[str] = Counter()
    counts["cases_not_in_backup"] = len(set(case_ids or []) - set(saved))
    with SessionLocal() as db:
        for index, case_id in enumerate(wanted, 1):
            if db.get(Case, case_id) is None:
                counts["case_missing"] += 1
                continue
            rows = saved[case_id]
            counts["current_rows_replaced"] += len(stored_rows(db, case_id))
            counts["rows_restored"] += len(rows)
            counts["cases_restored"] += 1
            if apply:
                db.execute(delete(StatuteReference).where(StatuteReference.source_case_id == case_id))
                db.flush()
                for row in rows:
                    db.add(StatuteReference(**{name: row.get(name) for name in BACKUP_COLUMNS}))
                if index % batch_size == 0:
                    db.commit()
        if apply:
            db.commit()
    return dict(counts)


def run(
    case_ids: list[int],
    apply: bool,
    backup_path: Path | None,
    batch_size: int,
    detail_path: Path | None = None,
) -> dict[str, Any]:
    before: Counter[str] = Counter()
    after: Counter[str] = Counter()
    changes: Counter[str] = Counter()
    samples: list[dict[str, Any]] = []
    with SessionLocal() as db:
        backup = backup_path.open("a", encoding="utf-8") if apply and backup_path else None
        detail = detail_path.open("w", encoding="utf-8") if detail_path else None
        try:
            for index, case_id in enumerate(case_ids, 1):
                case = db.get(Case, case_id)
                if case is None:
                    changes["case_missing"] += 1
                    continue
                old = stored_rows(db, case_id)
                texts = case_texts(db, case)
                new = new_rows_for_texts(texts, case.court)
                before.update(summarize(old))
                after.update(summarize(new))
                diff = diff_case(old, new)
                changes.update(diff)
                if (diff["added"] or diff["removed"]) and len(samples) < 20:
                    samples.append({"case_id": case_id, **diff})
                if detail is not None and (diff["added"] or diff["removed"]):
                    detail.write(json.dumps(detail_record(case_id, texts[0], old, new), default=str) + "\n")
                if apply:
                    if backup is not None:
                        backup.write(json.dumps({"case_id": case_id, "rows": old}, default=str) + "\n")
                        backup.flush()
                    rebuild_statute_references_for_case(db, case, [])
                    changes["cases_rebuilt"] += 1
                    if index % batch_size == 0:
                        db.commit()
            if apply:
                db.commit()
        finally:
            if backup is not None:
                backup.close()
            if detail is not None:
                detail.close()
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
    parser.add_argument(
        "--detail-file",
        type=Path,
        default=None,
        help="write every removed and added row with its surrounding text, one JSON line per changed case (read-only)",
    )
    parser.add_argument(
        "--skip-cases-in",
        type=Path,
        default=None,
        help="leave out cases already present in this backup file (use for the rest after a first tranche)",
    )
    parser.add_argument("--restore", type=Path, default=None, help="put the rows saved in this backup file back")
    parser.add_argument("--restore-dry-run", action="store_true", help="with --restore: report only, write nothing")
    args = parser.parse_args()
    if args.restore:
        if not args.restore.exists():
            parser.error(f"backup file not found: {args.restore}")
        if not args.restore_dry_run and not args.confirm_statute_reextract:
            parser.error("--restore writes to the database; add --confirm-statute-reextract (or --restore-dry-run)")
        result = restore(args.restore, apply=not args.restore_dry_run, case_ids=args.case_id or None, batch_size=args.batch_size)
        print("mode:", "restore dry run (no writes)" if args.restore_dry_run else "RESTORE", json.dumps(result, sort_keys=True))
        return
    if not (args.case_id or args.sample or args.all):
        parser.error("choose --case-id, --sample N or --all")
    if args.apply and not args.confirm_statute_reextract:
        parser.error("--apply needs --confirm-statute-reextract")
    with SessionLocal() as db:
        case_ids = select_case_ids(db, args.case_id, args.sample, args.seed, args.all, args.limit)
    if args.skip_cases_in:
        done = set(read_backup(args.skip_cases_in))
        case_ids = [cid for cid in case_ids if cid not in done]
    if args.apply:
        args.backup.parent.mkdir(parents=True, exist_ok=True)
    result = run(case_ids, args.apply, args.backup if args.apply else None, args.batch_size, args.detail_file)
    print("mode:", "APPLY" if args.apply else "dry run (no writes)", "cases:", len(case_ids))
    for key in ("before", "after", "changes"):
        print(key + ":", json.dumps(result[key], sort_keys=True))
    for sample in result["samples"]:
        print("  changed:", sample)


if __name__ == "__main__":
    main()
