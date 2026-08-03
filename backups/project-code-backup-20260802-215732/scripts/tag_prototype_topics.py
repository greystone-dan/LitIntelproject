"""Tag prototype cohort cases with topic-keyword metadata.

Writes `topic_keywords` and `topic_scores` into each case metadata_json.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import pandas as pd
from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal

DEFAULT_IDS_CSV = Path("data/eval/prototype_case_ids_v1.csv")

TOPIC_PATTERNS: dict[str, tuple[str, ...]] = {
    "refugee_protection": (
        r"\brefugee\b",
        r"\basylum\b",
        r"\bconvention refugee\b",
        r"\bprotected person\b",
        r"\bnon[- ]?refoulement\b",
        r"\bRPD\b",
        r"\bRAD\b",
    ),
    "removal_detention": (
        r"\bremoval order\b",
        r"\bstay of removal\b",
        r"\bdeport\w*\b",
        r"\bdetention\b",
        r"\bPRRA\b",
        r"\bpre[- ]?removal risk assessment\b",
    ),
    "inadmissibility_security": (
        r"\binadmissib\w*\b",
        r"\bsecurity\b",
        r"\bserious criminality\b",
        r"\bmisrepresentation\b",
        r"\borganized criminality\b",
        r"\bIRPA s\.?\s*34\b",
    ),
    "family_hc": (
        r"\bfamily class\b",
        r"\bsponsorship\b",
        r"\bspouse\b",
        r"\bcommon[- ]law\b",
        r"\bhumanitarian and compassionate\b",
        r"\bH&?C\b",
        r"\bbest interests of the child\b",
    ),
    "citizenship_status": (
        r"\bcitizenship\b",
        r"\bpermanent resident\b",
        r"\bresidency obligation\b",
        r"\bcertificate of citizenship\b",
    ),
    "judicial_review_procedure": (
        r"\bjudicial review\b",
        r"\bprocedural fairness\b",
        r"\bnatural justice\b",
        r"\breasonableness\b",
        r"\bcorrectness\b",
        r"\bVavilov\b",
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ids-csv", type=Path, default=DEFAULT_IDS_CSV)
    parser.add_argument("--min-score", type=int, default=1)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def score_topics(text: str) -> tuple[list[str], dict[str, int]]:
    scores: dict[str, int] = {}
    for topic, patterns in TOPIC_PATTERNS.items():
        score = 0
        for pattern in patterns:
            score += len(re.findall(pattern, text, flags=re.IGNORECASE))
        scores[topic] = score
    keywords = [topic for topic, score in scores.items() if score > 0]
    return keywords, scores


def main() -> None:
    args = parse_args()
    if not args.ids_csv.exists():
        raise SystemExit(f"Prototype ids file not found: {args.ids_csv}")

    ids = pd.read_csv(args.ids_csv)["case_id"].dropna().astype(int).tolist()
    updated = 0

    with SessionLocal() as session:
        rows = list(session.scalars(select(Case).where(Case.id.in_(ids)).order_by(Case.id)))
        for case in rows:
            text = "\n".join(
                [
                    case.title or "",
                    case.summary or "",
                    case.full_text or "",
                    " ".join(case.cases_cited or []),
                ]
            )
            topic_keywords, topic_scores = score_topics(text)

            metadata = dict(case.metadata_json or {})
            metadata["prototype_v1"] = True
            metadata["prototype_set"] = "immigration_334_v1"
            metadata["topic_keywords"] = topic_keywords
            metadata["topic_scores"] = topic_scores
            case.metadata_json = metadata
            updated += 1

        if not args.dry_run:
            session.commit()

    print(f"cases_scanned={len(ids)}")
    print(f"cases_updated={updated}")
    print(f"dry_run={args.dry_run}")


if __name__ == "__main__":
    main()
