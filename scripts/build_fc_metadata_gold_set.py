from __future__ import annotations

import argparse
import csv
import random
from pathlib import Path
import sys

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal
from fc_ingest.document_scraper import _extract_metadata_with_quality


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a real-case FC metadata gold annotation template")
    parser.add_argument("--out", type=Path, default=Path("data/eval/fc_metadata_gold_template.csv"))
    parser.add_argument("--limit", type=int, default=400, help="Maximum total rows")
    parser.add_argument("--per-court", type=int, default=120, help="Rows per court bucket")
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def _bucket(court: str | None, citation: str | None) -> str:
    c = (court or "").upper()
    cited = (citation or "").upper()
    if "SCC" in c or " SCC " in cited:
        return "SCC"
    if "FCA" in c or " FCA " in cited:
        return "FCA"
    if "FC" in c or " FC " in cited:
        return "FC"
    return "OTHER"


def main() -> None:
    args = parse_args()
    if args.limit < 1:
        raise SystemExit("--limit must be at least 1")

    rng = random.Random(args.seed)

    with SessionLocal() as session:
        query = (
            select(Case.id, Case.title, Case.court, Case.date, Case.citation, Case.full_text)
            .where(Case.full_text.is_not(None))
            .where(Case.full_text != "")
            .where((Case.court == "FC") | (Case.citation.ilike("% FC %")) | (Case.citation.ilike("% FCA %")) | (Case.citation.ilike("% SCC %")))
            .order_by(Case.id.desc())
        )
        rows = list(session.execute(query))

    buckets: dict[str, list[tuple[int, str, str, object, str | None, str]]] = {"FC": [], "FCA": [], "SCC": [], "OTHER": []}
    for case_id, title, court, decision_date, citation, full_text in rows:
        b = _bucket(court, citation)
        buckets.setdefault(b, []).append((int(case_id), str(title), str(court), decision_date, citation, str(full_text)))

    selected: list[tuple[int, str, str, object, str | None, str]] = []
    for bucket in ("FC", "FCA", "SCC", "OTHER"):
        candidates = buckets.get(bucket, [])
        rng.shuffle(candidates)
        selected.extend(candidates[: args.per_court])

    if len(selected) > args.limit:
        rng.shuffle(selected)
        selected = selected[: args.limit]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "case_id",
                "court",
                "date",
                "citation",
                "title",
                "bucket",
                "extracted_date",
                "extracted_docket",
                "extracted_neutral_citation",
                "extracted_judge",
                "extracted_style_of_cause",
                "extracted_place_of_hearing",
                "extracted_date_of_hearing",
                "extracted_counsel",
                "extracted_confidence_date",
                "extracted_confidence_docket",
                "extracted_confidence_neutral_citation",
                "extracted_confidence_judge",
                "extracted_confidence_style_of_cause",
                "gold_date",
                "gold_docket",
                "gold_neutral_citation",
                "gold_judge",
                "gold_style_of_cause",
                "gold_place_of_hearing",
                "gold_date_of_hearing",
                "gold_counsel",
                "annotator_notes",
            ],
        )
        writer.writeheader()

        for case_id, title, court, decision_date, citation, full_text in selected:
            metadata = _extract_metadata_with_quality(full_text)
            confidence = metadata.get("_field_confidence") or {}
            writer.writerow(
                {
                    "case_id": case_id,
                    "court": court,
                    "date": decision_date,
                    "citation": citation,
                    "title": title,
                    "bucket": _bucket(court, citation),
                    "extracted_date": metadata.get("date", ""),
                    "extracted_docket": metadata.get("docket", ""),
                    "extracted_neutral_citation": metadata.get("neutral citation", ""),
                    "extracted_judge": metadata.get("judge", ""),
                    "extracted_style_of_cause": metadata.get("style of cause", ""),
                    "extracted_place_of_hearing": metadata.get("place of hearing", ""),
                    "extracted_date_of_hearing": metadata.get("date of hearing", ""),
                    "extracted_counsel": metadata.get("counsel", ""),
                    "extracted_confidence_date": confidence.get("date", ""),
                    "extracted_confidence_docket": confidence.get("docket", ""),
                    "extracted_confidence_neutral_citation": confidence.get("neutral citation", ""),
                    "extracted_confidence_judge": confidence.get("judge", ""),
                    "extracted_confidence_style_of_cause": confidence.get("style of cause", ""),
                    "gold_date": "",
                    "gold_docket": "",
                    "gold_neutral_citation": "",
                    "gold_judge": "",
                    "gold_style_of_cause": "",
                    "gold_place_of_hearing": "",
                    "gold_date_of_hearing": "",
                    "gold_counsel": "",
                    "annotator_notes": "",
                }
            )

    print({"output": str(args.out), "rows": len(selected)})


if __name__ == "__main__":
    main()
