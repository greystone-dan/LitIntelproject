"""Audit retained Discussion Unit reports for review-only structural risks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DEFAULT_REPORTS_DIR = Path("data/eval/llm_discussion_units_pilot/core_300_run/reports")
DEFAULT_OUTPUT = Path("data/eval/llm_discussion_units_pilot/core_300_run/discussion_unit_structural_audit.json")
DEFAULT_MIN_PARAGRAPHS = 12
DEFAULT_MAX_UNIT_PARAGRAPHS = 20
DEFAULT_MAX_SUBTHEME_PARAGRAPHS = 12


def _span_size(item: dict[str, Any]) -> int:
    paragraph_indices = item.get("paragraph_indices")
    if isinstance(paragraph_indices, list):
        return len(paragraph_indices)
    return int(item.get("paragraph_count") or 0)


def audit_report(
    report: dict[str, Any],
    *,
    min_paragraphs: int,
    max_unit_paragraphs: int,
    max_subtheme_paragraphs: int,
) -> dict[str, Any]:
    case_id = int(report["case_id"])
    paragraph_count = int(report["paragraph_count"])
    units = report.get("discussion_units") or []
    unit_sizes = [_span_size(unit) for unit in units]
    subthemes = [subtheme for unit in units for subtheme in unit.get("subthemes") or []]
    subtheme_sizes = [_span_size(subtheme) for subtheme in subthemes]
    collapsed_top_level = paragraph_count >= min_paragraphs and len(units) == 1
    collapsed_subthemes = paragraph_count >= min_paragraphs and len(subthemes) <= 1
    oversized_unit_count = sum(size >= max_unit_paragraphs for size in unit_sizes)
    oversized_subtheme_count = sum(size >= max_subtheme_paragraphs for size in subtheme_sizes)
    flags = []
    if collapsed_top_level:
        flags.append("collapsed_top_level")
    if collapsed_subthemes:
        flags.append("collapsed_subthemes")
    if oversized_unit_count:
        flags.append("oversized_unit")
    if oversized_subtheme_count:
        flags.append("oversized_subtheme")
    return {
        "case_id": case_id,
        "paragraph_count": paragraph_count,
        "discussion_unit_count": len(units),
        "subtheme_count": len(subthemes),
        "max_unit_paragraph_count": max(unit_sizes, default=0),
        "max_subtheme_paragraph_count": max(subtheme_sizes, default=0),
        "oversized_unit_count": oversized_unit_count,
        "oversized_subtheme_count": oversized_subtheme_count,
        "flags": flags,
    }


def audit_reports(
    reports_dir: Path,
    *,
    min_paragraphs: int = DEFAULT_MIN_PARAGRAPHS,
    max_unit_paragraphs: int = DEFAULT_MAX_UNIT_PARAGRAPHS,
    max_subtheme_paragraphs: int = DEFAULT_MAX_SUBTHEME_PARAGRAPHS,
) -> dict[str, Any]:
    paths = sorted(reports_dir.glob("case_*_deterministic.json"))
    if not paths:
        raise ValueError(f"No deterministic reports found in {reports_dir}")
    cases = [
        audit_report(
            json.loads(path.read_text(encoding="utf-8")),
            min_paragraphs=min_paragraphs,
            max_unit_paragraphs=max_unit_paragraphs,
            max_subtheme_paragraphs=max_subtheme_paragraphs,
        )
        for path in paths
    ]
    return {
        "schema_version": 1,
        "source": str(reports_dir).replace("\\", "/"),
        "thresholds": {
            "min_paragraphs_for_collapse": min_paragraphs,
            "max_unit_paragraphs": max_unit_paragraphs,
            "max_subtheme_paragraphs": max_subtheme_paragraphs,
        },
        "case_count": len(cases),
        "cases": cases,
        "summary": {
            "collapsed_top_level_case_count": sum("collapsed_top_level" in case["flags"] for case in cases),
            "collapsed_subthemes_case_count": sum("collapsed_subthemes" in case["flags"] for case in cases),
            "cases_with_oversized_units": sum("oversized_unit" in case["flags"] for case in cases),
            "cases_with_oversized_subthemes": sum("oversized_subtheme" in case["flags"] for case in cases),
            "flagged_case_ids": [case["case_id"] for case in cases if case["flags"]],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reports-dir", type=Path, default=DEFAULT_REPORTS_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--min-paragraphs", type=int, default=DEFAULT_MIN_PARAGRAPHS)
    parser.add_argument("--max-unit-paragraphs", type=int, default=DEFAULT_MAX_UNIT_PARAGRAPHS)
    parser.add_argument("--max-subtheme-paragraphs", type=int, default=DEFAULT_MAX_SUBTHEME_PARAGRAPHS)
    args = parser.parse_args()
    report = audit_reports(
        args.reports_dir,
        min_paragraphs=args.min_paragraphs,
        max_unit_paragraphs=args.max_unit_paragraphs,
        max_subtheme_paragraphs=args.max_subtheme_paragraphs,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "case_count": report["case_count"], **report["summary"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())