"""Export the current bounded V3 canary rows as a human-review snapshot."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseTag, SessionLocal
from backend.legal_tagger_v3 import TAXONOMY_VERSION


OUTPUT_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "eval"
    / "reports"
    / "tagging-v3-canary-review.md"
)


def _cell(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def export_review() -> int:
    statement = (
        select(Case.id, Case.court, CaseTag)
        .join(CaseTag, CaseTag.case_id == Case.id)
        .where(CaseTag.taxonomy_version == TAXONOMY_VERSION)
        .order_by(Case.court, Case.id, CaseTag.offset_start, CaseTag.id)
    )
    with SessionLocal() as db:
        rows = db.execute(statement).all()

    lines = [
        "# V3 Canary Review",
        "",
        "Status: proposed human review",
        f"Taxonomy: `{TAXONOMY_VERSION}`",
        "",
        "Review every occurrence for exact evidence, canonical category/value, and whether `mention` is the correct evidence role. This is a review snapshot, not activation approval.",
        "",
        "## Review checklist",
        "",
        "- Confirm the evidence is an exact source span.",
        "- Confirm the canonical category and value are appropriate.",
        "- Confirm the match is a mention only, not an inferred finding.",
        "- Record false positives or alias decisions before expanding the canary.",
        "",
        f"## Occurrences ({len(rows)})",
        "",
        "| Case | Court | Category | Value | Evidence | Start | End | Rule | Language | Role | Source |",
        "| ---: | --- | --- | --- | --- | ---: | ---: | --- | --- | --- | --- |",
    ]
    for case_id, court, tag in rows:
        lines.append(
            "| "
            + " | ".join(
                _cell(value)
                for value in (
                    case_id,
                    court,
                    tag.category,
                    tag.value,
                    tag.evidence,
                    tag.offset_start,
                    tag.offset_end,
                    tag.rule_id,
                    tag.language,
                    tag.evidence_role,
                    tag.source,
                )
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Review decision",
            "",
            "Pending human review. Do not activate corpus-wide V3 tagging until reviewed precision and corrections are recorded.",
            "",
        ]
    )
    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    return len(rows)


if __name__ == "__main__":
    print(f"exported_occurrences={export_review()} output={OUTPUT_PATH}")