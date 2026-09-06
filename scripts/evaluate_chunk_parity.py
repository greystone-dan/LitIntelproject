"""Compare HTML-enabled and text-only chunking on a bounded sample."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal  # noqa: E402
from scripts.chunk_cases import build_case_chunk_layers  # noqa: E402


def rows_for(case: Case, html_enabled: bool) -> list:
    original = case.source_html
    try:
        if not html_enabled:
            case.source_html = None
        return build_case_chunk_layers(case)
    finally:
        case.source_html = original


def containment(source: list[str], target: list[str]) -> float:
    if not source:
        return 1.0
    return sum(any(text in candidate or candidate in text for candidate in target) for text in source) / len(source)


def metrics(case: Case) -> dict[str, object]:
    html_rows = rows_for(case, True)
    text_rows = rows_for(case, False)
    html_sections = [row for row in html_rows if row.chunk_set == "section"]
    text_sections = [row for row in text_rows if row.chunk_set == "section"]
    html_paragraphs = [row for row in html_rows if row.chunk_set == "paragraph"]
    text_paragraphs = [row for row in text_rows if row.chunk_set == "paragraph"]
    html_tokens = sum(row.token_estimate for row in html_rows)
    text_tokens = sum(row.token_estimate for row in text_rows)
    return {
        "case_id": case.id,
        "court": case.court,
        "citation": case.citation,
        "text_length": len(case.full_text or ""),
        "html_sections": len(html_sections),
        "text_sections": len(text_sections),
        "section_relative_delta": abs(len(html_sections) - len(text_sections)) / max(1, len(html_sections)),
        "html_paragraphs": len(html_paragraphs),
        "text_paragraphs": len(text_paragraphs),
        "paragraph_relative_delta": abs(len(html_paragraphs) - len(text_paragraphs)) / max(1, len(html_paragraphs)),
        "paragraph_containment": containment([row.text for row in html_paragraphs], [row.text for row in text_paragraphs]),
        "html_tokens": html_tokens,
        "text_tokens": text_tokens,
        "token_relative_delta": abs(html_tokens - text_tokens) / max(1, html_tokens),
        "html_chunk_count": len(html_rows),
        "text_chunk_count": len(text_rows),
        "canonical_text_preserved": all((row.text or "") in (case.full_text or "") for row in text_rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-id", type=int, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    with SessionLocal() as db:
        cases = list(db.scalars(select(Case).where(Case.id.in_(args.case_id)).order_by(Case.id)))
    report = {"gates": {"section_relative_delta": 0.20, "paragraph_relative_delta": 0.10, "paragraph_containment": 0.90, "token_relative_delta": 0.05}, "cases": [metrics(case) for case in cases]}
    for item in report["cases"]:
        item["passes"] = {
            "section": item["section_relative_delta"] <= report["gates"]["section_relative_delta"],
            "paragraph": item["paragraph_relative_delta"] <= report["gates"]["paragraph_relative_delta"],
            "containment": item["paragraph_containment"] >= report["gates"]["paragraph_containment"],
            "tokens": item["token_relative_delta"] <= report["gates"]["token_relative_delta"],
            "canonical_text": item["canonical_text_preserved"],
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"cases={len(report['cases'])} output={args.output}")


if __name__ == "__main__":
    main()
