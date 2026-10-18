"""Re-split stored paragraph rows with the reader's paragraph numbering (dry run by default).

Only the "paragraph" chunk set of each chosen decision is replaced; full_case and section rows are left alone.
References that point at an old paragraph row are moved to the new row that holds the same text, so citations,
refined citations, statute references and tags keep their ids and their resolved targets (nothing is rebuilt):
  - rows in the same decision (citations, citations_refined, statute_references, statute_references_refined,
    case_tags) are moved by character position and their offsets re-based;
  - rows in other decisions that point at this decision's paragraphs (citations.target_chunk_id,
    citations_refined.target_chunk_id) are moved by their stated paragraph number, or cleared when no single new
    row holds that paragraph.

A new row whose text is identical to an old row keeps that row's stored embedding; embeddings of rows whose text
changes are dropped (the report counts both). The dry run does the whole change inside a transaction and rolls it
back, so its reference and embedding counts are exact.

Every applied decision first writes a JSON undo record (old rows with their original ids and embeddings, and the old values of
every reference changed). `--undo FILE` puts the old rows back and restores the references.

Examples:
  python scripts/resplit_paragraph_chunks.py --case-ids-csv ids.csv --report report.csv
  python scripts/resplit_paragraph_chunks.py --court SCC --year-from 2005 --apply --undo-dir undo_resplit
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import date
from pathlib import Path

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import (
    Case,
    CaseChunk,
    CaseTag,
    Citation,
    CitationRefined,
    SessionLocal,
    StatuteReference,
    StatuteReferenceRefined,
)
from scripts.chunk_cases import build_case_chunk_layers, load_case_ids_from_csv

# Tables whose chunk_id points into the same decision, with the offset columns stored relative to that chunk.
OWN_REFERENCE_MODELS = (Citation, CitationRefined, StatuteReference, StatuteReferenceRefined, CaseTag)
# Tables whose target_chunk_id points into another decision's paragraph rows.
TARGET_REFERENCE_MODELS = (Citation, CitationRefined)

ROW_COLUMNS = (
    "id", "case_id", "chunk_set", "chunk_index", "chunk_label", "paragraph_start", "paragraph_end",
    "text", "text_hash", "token_estimate", "embedding_model",
)


def row_signature(rows) -> list[tuple]:
    return [(row.chunk_label, row.paragraph_start, row.paragraph_end, row.text_hash) for row in rows]


def locate_rows(case_text: str, rows) -> list[tuple[object, int, int]]:
    """Character span of each row inside the decision text, walking forward like rebuild_citations_for_case."""
    located = []
    cursor = 0
    for row in rows:
        body = row.text or ""
        if not body:
            continue
        start = case_text.find(body, cursor)
        if start < 0:
            start = case_text.find(body)
        if start < 0:
            continue
        located.append((row, start, start + len(body)))
        cursor = max(cursor, start + len(body))
    return located


def row_for_position(located, position: int):
    for row, start, end in located:
        if start <= position < end:
            return row, start
    return None, 0


def row_for_paragraph(rows, paragraph: int | None):
    if paragraph is None:
        return None
    hits = [
        row for row in rows
        if row.paragraph_start is not None and row.paragraph_end is not None
        and row.paragraph_start <= paragraph <= row.paragraph_end
    ]
    return hits[0] if len(hits) == 1 else None


def row_to_dict(row) -> dict:
    data = {name: getattr(row, name) for name in ROW_COLUMNS}
    embedding = getattr(row, "embedding", None)
    data["embedding"] = None if embedding is None else [float(value) for value in embedding]
    return data


def carry_over_embeddings(old_rows, new_rows) -> tuple[int, int]:
    """Copy an old row's stored embedding to a new row with identical text. Returns (carried, lost)."""
    available: dict[str, list] = {}
    for row in old_rows:
        if row.embedding is not None:
            available.setdefault(row.text_hash, []).append(row)
    carried = 0
    for row in new_rows:
        donors = available.get(row.text_hash)
        if donors and getattr(row, "embedding", None) is None:
            donor = donors.pop(0)
            if donor.text == row.text:
                row.embedding = donor.embedding
                row.embedding_model = donor.embedding_model
                carried += 1
            else:
                donors.insert(0, donor)
    embedded_old = sum(1 for row in old_rows if row.embedding is not None)
    return carried, embedded_old - carried


def paragraph_rows(session: Session, case_id: int) -> list[CaseChunk]:
    return list(
        session.scalars(
            select(CaseChunk)
            .where(CaseChunk.case_id == case_id, CaseChunk.chunk_set == "paragraph")
            .order_by(CaseChunk.chunk_index, CaseChunk.id)
        )
    )


def case_selection(args) -> list[int]:
    ids: set[int] = set(args.case_id or [])
    if args.case_ids_csv:
        ids.update(load_case_ids_from_csv(args.case_ids_csv))
    with SessionLocal() as session:
        if ids:
            return sorted(ids)
        query = select(Case.id).where(Case.full_text.is_not(None), Case.full_text != "")
        if args.court:
            query = query.where(Case.court == args.court)
        if args.year_from:
            query = query.where(Case.date >= date(args.year_from, 1, 1))
        return list(session.scalars(query.order_by(Case.id)))


def plan_case(session: Session, case: Case) -> dict:
    """What re-splitting this decision would change, without writing anything."""
    old_rows = paragraph_rows(session, case.id)
    new_rows = [row for row in build_case_chunk_layers(case) if row.chunk_set == "paragraph"]
    old_numbered = [r for r in old_rows if (r.chunk_label or "").isdigit()]
    new_numbered = [r for r in new_rows if (r.chunk_label or "").isdigit()]
    return {
        "old_rows": old_rows,
        "new_rows": new_rows,
        "old_total": len(old_rows),
        "new_total": len(new_rows),
        "old_numbered": len(old_numbered),
        "new_numbered": len(new_numbered),
        "same": row_signature(old_rows) == row_signature(new_rows),
        "old_embedded": sum(1 for r in old_rows if r.embedding is not None),
        "embeddings_carried": 0,
        "embeddings_lost": 0,
    }


def apply_case(session: Session, case: Case, plan: dict, undo_dir: Path | None) -> dict:
    old_rows, new_rows = plan["old_rows"], plan["new_rows"]
    text = case.full_text or case.summary or ""
    old_ids = [row.id for row in old_rows]
    undo = {
        "case_id": case.id,
        "old_rows": [row_to_dict(row) for row in old_rows],
        "own": [],
        "target": [],
    }

    # New rows exist before anything moves, so every reference always has a valid chunk to point at.
    plan["embeddings_carried"], plan["embeddings_lost"] = carry_over_embeddings(old_rows, new_rows)
    session.add_all(new_rows)
    session.flush()
    old_located = locate_rows(text, old_rows)
    new_located = locate_rows(text, new_rows)
    moved = cleared = 0

    if old_ids:
        for model in OWN_REFERENCE_MODELS:
            refs = list(session.scalars(select(model).where(model.chunk_id.in_(old_ids))))
            old_by_id = {row.id: (row, start) for row, start, _ in old_located}
            for ref in refs:
                old_row, old_start = old_by_id.get(ref.chunk_id, (None, 0))
                undo["own"].append({
                    "table": model.__tablename__, "id": ref.id, "chunk_id": ref.chunk_id,
                    "offset_start": ref.offset_start, "offset_end": ref.offset_end,
                })
                if old_row is None or ref.offset_start is None:
                    ref.chunk_id = None
                    cleared += 1
                    continue
                absolute = old_start + ref.offset_start
                new_row, new_start = row_for_position(new_located, absolute)
                if new_row is None:
                    ref.chunk_id = None
                    cleared += 1
                    continue
                length = (ref.offset_end - ref.offset_start) if ref.offset_end is not None else None
                ref.chunk_id = new_row.id
                ref.offset_start = absolute - new_start
                if length is not None:
                    ref.offset_end = ref.offset_start + length
                moved += 1
        for model in TARGET_REFERENCE_MODELS:
            refs = list(session.scalars(select(model).where(model.target_chunk_id.in_(old_ids))))
            for ref in refs:
                undo["target"].append({"table": model.__tablename__, "id": ref.id, "target_chunk_id": ref.target_chunk_id})
                new_row = row_for_paragraph(new_rows, ref.target_paragraph)
                ref.target_chunk_id = new_row.id if new_row is not None else None
                moved += 1 if new_row is not None else 0
                cleared += 0 if new_row is not None else 1
        session.flush()

    if undo_dir is not None:
        undo_dir.mkdir(parents=True, exist_ok=True)
        path = undo_dir / f"case_{case.id}.json"
        path.write_text(json.dumps(undo, default=str), encoding="utf-8")

    if old_ids:
        session.execute(delete(CaseChunk).where(CaseChunk.id.in_(old_ids)))
    return {
        "moved": moved, "cleared": cleared, "own": len(undo["own"]), "target": len(undo["target"]),
        "embeddings_carried": plan["embeddings_carried"], "embeddings_lost": plan["embeddings_lost"],
    }


def undo_case(session: Session, path: Path) -> None:
    record = json.loads(path.read_text(encoding="utf-8"))
    case_id = record["case_id"]
    models = {model.__tablename__: model for model in OWN_REFERENCE_MODELS + TARGET_REFERENCE_MODELS}
    # Restore the old rows with their original ids, point the references back, then drop the new rows.
    current_ids = [row.id for row in paragraph_rows(session, case_id)]
    for data in record["old_rows"]:
        values = {name: data[name] for name in ROW_COLUMNS}
        session.add(CaseChunk(**values, embedding=data.get("embedding")))
    session.flush()
    for ref in record["own"]:
        session.execute(
            update(models[ref["table"]]).where(models[ref["table"]].id == ref["id"]).values(
                chunk_id=ref["chunk_id"], offset_start=ref["offset_start"], offset_end=ref["offset_end"]
            )
        )
    for ref in record["target"]:
        session.execute(
            update(models[ref["table"]]).where(models[ref["table"]].id == ref["id"]).values(target_chunk_id=ref["target_chunk_id"])
        )
    if current_ids:
        session.execute(delete(CaseChunk).where(CaseChunk.id.in_(current_ids)))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--case-id", type=int, action="append", default=[])
    parser.add_argument("--case-ids-csv", default=None, help="CSV with an id or case_id column")
    parser.add_argument("--court", default=None, help="e.g. SCC, FC, FCA")
    parser.add_argument("--year-from", type=int, default=None, help="only decisions dated on or after this year")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--apply", action="store_true", help="write the changes (default is a dry run)")
    parser.add_argument("--undo-dir", default="undo_resplit", help="where --apply writes one undo file per decision")
    parser.add_argument("--undo", nargs="+", metavar="FILE", help="restore decisions from undo files")
    parser.add_argument("--report", default=None, help="write a per-decision CSV of before/after counts")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.undo:
        with SessionLocal() as session:
            for name in args.undo:
                undo_case(session, Path(name))
                session.commit()
                print(f"restored {name}", flush=True)
        return

    case_ids = case_selection(args)
    if args.limit:
        case_ids = case_ids[: args.limit]
    totals = {"decisions": 0, "changed": 0, "unchanged": 0, "old_rows": 0, "new_rows": 0,
              "old_numbered": 0, "new_numbered": 0, "moved": 0, "cleared": 0, "embeddings_carried": 0, "embeddings_lost": 0}
    report_rows = []
    undo_dir = Path(args.undo_dir) if args.apply else None

    with SessionLocal() as session:
        for case_id in case_ids:
            case = session.get(Case, case_id)
            if case is None or not (case.full_text or "").strip():
                continue
            court = case.court
            plan = plan_case(session, case)
            totals["decisions"] += 1
            result = {"moved": 0, "cleared": 0, "embeddings_carried": 0, "embeddings_lost": 0}
            if plan["same"]:
                totals["unchanged"] += 1
                session.rollback()
            else:
                totals["changed"] += 1
                totals["old_rows"] += plan["old_total"]
                totals["new_rows"] += plan["new_total"]
                totals["old_numbered"] += plan["old_numbered"]
                totals["new_numbered"] += plan["new_numbered"]
                # A dry run does the whole change inside a transaction and rolls it back, so its counts are exact.
                try:
                    result = apply_case(session, case, plan, undo_dir)
                    if args.apply:
                        session.commit()
                    else:
                        session.rollback()
                except Exception as error:
                    session.rollback()
                    print(f"case_error id={case_id} error={type(error).__name__}: {error}", flush=True)
                    continue
                for key in ("moved", "cleared", "embeddings_carried", "embeddings_lost"):
                    totals[key] += result[key]
            report_rows.append({
                "case_id": case_id, "court": court, "changed": not plan["same"],
                "old_rows": plan["old_total"], "new_rows": plan["new_total"],
                "old_numbered": plan["old_numbered"], "new_numbered": plan["new_numbered"],
                "moved_refs": result["moved"], "cleared_refs": result["cleared"],
                "embeddings_carried": result["embeddings_carried"], "embeddings_lost": result["embeddings_lost"],
            })

    if args.report and report_rows:
        with open(args.report, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(report_rows[0]))
            writer.writeheader()
            writer.writerows(report_rows)
    mode = "APPLIED" if args.apply else "DRY RUN (nothing written)"
    print(mode)
    for key, value in totals.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
