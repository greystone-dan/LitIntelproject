"""Fill blank FCA headline outcomes from the stored deterministic_outcome_v2 result (dry run by default).

Only decisions whose headline ("decision outcome" in metadata_json.reader_extracted) is blank are touched, and only
when v2 says allowed, dismissed or mixed. Undetermined, unclear and procedural v2 results are left blank, and any
headline that already has a value is never changed. --apply writes an undo file with the old value of every row.

Examples:
  python scripts/fill_fca_headline_outcomes.py --case-ids-csv fca_ids.csv
  python scripts/fill_fca_headline_outcomes.py --apply --undo-file undo_fca_headlines.json
  python scripts/fill_fca_headline_outcomes.py --undo undo_fca_headlines.json
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

from sqlalchemy import text

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import SessionLocal
from scripts.chunk_cases import load_case_ids_from_csv

FILLABLE = ("allowed", "dismissed", "mixed")
COURT = "FCA"

SELECT_SQL = """
    SELECT c.id, c.metadata_json->'reader_extracted'->>'decision outcome' AS headline,
           o.decision_outcome AS v2
    FROM cases AS c
    LEFT JOIN case_outcomes AS o
      ON o.case_id = c.id AND o.classifier_version = 'deterministic_outcome_v2'
    WHERE c.court = :court
      AND (CAST(:ids AS integer[]) IS NULL OR c.id = ANY(CAST(:ids AS integer[])))
    ORDER BY c.id
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--court", default=COURT)
    parser.add_argument("--case-ids-csv", default=None)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--undo-file", default="undo_fca_headlines.json")
    parser.add_argument("--undo", default=None, help="restore headlines from an undo file")
    return parser.parse_args()


def classify(headline: str | None, v2: str | None) -> str:
    if (headline or "").strip():
        return "kept_existing"
    if v2 in FILLABLE:
        return "fill"
    return "left_blank"


def summarise(rows: list[tuple[int, str | None, str | None]]) -> dict:
    counts = Counter(classify(headline, v2) for _, headline, v2 in rows)
    filled_by = Counter(v2 for _, headline, v2 in rows if classify(headline, v2) == "fill")
    blank_before = sum(1 for _, headline, _ in rows if not (headline or "").strip())
    return {
        "decisions": len(rows),
        "blank_before": blank_before,
        "blank_after": blank_before - counts["fill"],
        "fill": counts["fill"],
        "left_blank": counts["left_blank"],
        "kept_existing": counts["kept_existing"],
        "filled_by_value": dict(filled_by),
    }


def main() -> None:
    args = parse_args()

    if args.undo:
        old = json.loads(Path(args.undo).read_text(encoding="utf-8"))
        with SessionLocal() as session:
            for case_id, value in old.items():
                session.execute(
                    text(
                        "UPDATE cases SET metadata_json = jsonb_set(metadata_json::jsonb, "
                        "'{reader_extracted}', (metadata_json::jsonb->'reader_extracted') - 'decision outcome')::json "
                        "WHERE id = :id AND metadata_json->'reader_extracted'->>'decision outcome' = :value"
                    ),
                    {"id": int(case_id), "value": value},
                )
            session.commit()
        print(f"restored={len(old)}")
        return

    ids = load_case_ids_from_csv(args.case_ids_csv) if args.case_ids_csv else None
    with SessionLocal() as session:
        rows = [
            (row.id, row.headline, row.v2)
            for row in session.execute(text(SELECT_SQL), {"court": args.court, "ids": ids})
        ]
        summary = summarise(rows)
        to_fill = [(case_id, v2) for case_id, headline, v2 in rows if classify(headline, v2) == "fill"]
        print(("APPLY" if args.apply else "DRY RUN (nothing written)"), json.dumps(summary))
        if not args.apply:
            return
        # Blank headlines have no value to restore: the undo file lists the ids so undo removes the filled key.
        Path(args.undo_file).write_text(json.dumps({str(case_id): v2 for case_id, v2 in to_fill}), encoding="utf-8")
        for case_id, value in to_fill:
            session.execute(
                text(
                    "UPDATE cases SET metadata_json = jsonb_set(COALESCE(metadata_json::jsonb, '{}'::jsonb), "
                    "'{reader_extracted}', COALESCE(metadata_json::jsonb->'reader_extracted', '{}'::jsonb) "
                    "|| jsonb_build_object('decision outcome', CAST(:value AS text)))::json "
                    "WHERE id = :id AND COALESCE(metadata_json->'reader_extracted'->>'decision outcome', '') = ''"
                ),
                {"id": case_id, "value": value},
            )
        session.commit()
        print(f"filled={len(to_fill)} undo_file={args.undo_file}")


if __name__ == "__main__":
    main()
