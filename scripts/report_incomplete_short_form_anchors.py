"""Report stored short-form anchors that can be lengthened from source text."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from sqlalchemy import func, select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import _extend_case_anchor_span
from backend.database import Case, Citation, SessionLocal


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--progress-every", type=int, default=500)
    parser.add_argument("--source-batch-size", type=int, default=250)
    parser.add_argument("--output", type=Path, default=None)
    return parser.parse_args()


def _complete_anchor(row) -> bool:
    return (
        row.anchor_citation_text is not None
        and row.anchor_offset_start is not None
        and row.anchor_offset_end is not None
    )


def _process_case(
    rows,
    text: str,
    counts: Counter,
    examples: list[dict[str, object]],
    count_population: bool = True,
) -> None:
    for row in rows:
        if count_population:
            counts["complete_anchor_rows"] += 1
            if row.target_case_id is None:
                counts["complete_anchor_unresolved_rows"] += 1

        stored_start = row.anchor_offset_start
        stored_end = row.anchor_offset_end
        if not (0 <= stored_start < stored_end <= len(text)):
            counts["stored_anchor_conflicts"] += 1
            continue
        if text[stored_start:stored_end] != row.anchor_citation_text:
            counts["stored_anchor_conflicts"] += 1
            continue
        counts["validated_stored_anchor_rows"] += 1
        if re.search(r"[0-9]{4}", row.anchor_citation_text):
            counts["validated_stored_anchors_with_year"] += 1
        else:
            counts["validated_stored_anchors_without_year"] += 1

        expected_start, expected_end, expected_text = _extend_case_anchor_span(text, stored_start, stored_end)

        if (
            stored_start == expected_start
            and stored_end == expected_end
            and row.anchor_citation_text == expected_text
        ):
            counts["no_local_extension_evidence"] += 1
            continue

        if expected_start == stored_start and expected_end > stored_end:
            repair_type = "safe_right_edge_extension"
        elif expected_start > stored_start and expected_end >= stored_end:
            repair_type = "start_correction_candidate"
        else:
            counts["local_anchor_conflicts"] += 1
            continue

        counts["candidate_anchor_repairs"] += 1
        counts[f"{repair_type}s"] += 1
        if repair_type == "safe_right_edge_extension" and row.target_case_id is None:
            counts["safe_right_edge_unresolved_rows"] += 1
        if repair_type == "start_correction_candidate" and row.target_case_id is None:
            counts["start_correction_unresolved_rows"] += 1
        if len(examples) < 20:
            examples.append(
                {
                    "repair_type": repair_type,
                    "citation_id": row.id,
                    "source_case_id": row.source_case_id,
                    "citation_text": row.citation_text,
                    "old_anchor": row.anchor_citation_text,
                    "new_anchor": expected_text,
                    "old_span": [stored_start, stored_end],
                    "new_span": [expected_start, expected_end],
                }
            )


def build_report(session, case_session, progress_every: int, source_batch_size: int) -> dict[str, object]:
    if progress_every < 1:
        raise ValueError("progress_every must be at least 1")
    if source_batch_size < 1:
        raise ValueError("source_batch_size must be at least 1")

    all_short = session.scalar(
        select(func.count())
        .select_from(Citation)
        .where(Citation.citation_kind == "case_short")
    ) or 0
    complete_short = session.scalar(
        select(func.count())
        .select_from(Citation)
        .where(
            Citation.citation_kind == "case_short",
            Citation.anchor_citation_text.is_not(None),
            Citation.anchor_offset_start.is_not(None),
            Citation.anchor_offset_end.is_not(None),
        )
    ) or 0
    unresolved_complete_short = session.scalar(
        select(func.count())
        .select_from(Citation)
        .where(
            Citation.citation_kind == "case_short",
            Citation.target_case_id.is_(None),
            Citation.anchor_citation_text.is_not(None),
            Citation.anchor_offset_start.is_not(None),
            Citation.anchor_offset_end.is_not(None),
        )
    ) or 0

    counts = Counter(
        {
            "all_case_short_rows": int(all_short),
            "rows_with_existing_anchor_fields": int(complete_short),
            "unresolved_rows_with_existing_anchor_fields": int(unresolved_complete_short),
        }
    )
    examples: list[dict[str, object]] = []
    source_case_ids = list(
        session.scalars(
            select(Citation.source_case_id)
            .where(
                Citation.citation_kind == "case_short",
                Citation.target_case_id.is_(None),
                Citation.anchor_citation_text.is_not(None),
                Citation.anchor_offset_start.is_not(None),
                Citation.anchor_offset_end.is_not(None),
            )
            .distinct()
            .order_by(Citation.source_case_id)
        )
    )
    processed_cases = 0
    row_columns = (
        Citation.id,
        Citation.source_case_id,
        Citation.citation_text,
        Citation.target_case_id,
        Citation.offset_start,
        Citation.offset_end,
        Citation.anchor_citation_text,
        Citation.anchor_offset_start,
        Citation.anchor_offset_end,
    )
    for batch_start in range(0, len(source_case_ids), source_batch_size):
        batch_ids = source_case_ids[batch_start : batch_start + source_batch_size]
        case_texts = dict(
            case_session.execute(
                select(Case.id, Case.full_text).where(Case.id.in_(batch_ids))
            ).all()
        )
        rows_by_case: dict[int, list[object]] = defaultdict(list)
        for row in session.execute(
            select(*row_columns)
            .where(
                Citation.citation_kind == "case_short",
                Citation.target_case_id.is_(None),
                Citation.source_case_id.in_(batch_ids),
                Citation.anchor_citation_text.is_not(None),
                Citation.anchor_offset_start.is_not(None),
                Citation.anchor_offset_end.is_not(None),
            )
            .order_by(Citation.source_case_id, Citation.id)
        ):
            rows_by_case[row.source_case_id].append(row)
        for source_case_id in batch_ids:
            source_text = case_texts.get(source_case_id) or ""
            _process_case(rows_by_case[source_case_id], source_text, counts, examples)
        processed_cases += len(batch_ids)
        if processed_cases % progress_every < source_batch_size or processed_cases == len(source_case_ids):
            print(f"processed_source_cases={processed_cases}", file=sys.stderr, flush=True)

    counts["processed_source_cases"] = processed_cases
    counts["no_anchor_rows_excluded"] = counts["all_case_short_rows"] - counts["rows_with_existing_anchor_fields"]
    counts["resolved_rows_with_existing_anchor_fields"] = (
        counts["rows_with_existing_anchor_fields"]
        - counts["unresolved_rows_with_existing_anchor_fields"]
    )
    return {"counts": dict(counts), "examples": examples}


def main() -> None:
    args = parse_args()
    with SessionLocal() as session, SessionLocal() as case_session:
        report = build_report(session, case_session, args.progress_every, args.source_batch_size)
    serialized = json.dumps(report, indent=2, ensure_ascii=True)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized + "\n", encoding="utf-8")
    print(serialized)


if __name__ == "__main__":
    main()
