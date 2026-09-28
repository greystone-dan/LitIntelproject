"""Report recurring evidence patterns among unknown FC Activity motions."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
from typing import Any


def _phrase_family(text: str) -> str:
    lowered = text.casefold()
    if re.search(r"motion record|motion doc\.?\s*(?:no\.?|number)|in support of doc\.?", lowered):
        return "motion_record_reference"
    if re.search(r"result of hearing|matter (?:dismissed|granted|refused)|minutes of hearing", lowered):
        return "hearing_motion_reference"
    if re.search(r"\bstay motion\b|urgent stay|motion to stay", lowered):
        return "generic_stay_reference"
    if re.search(r"order (?:on|rendered on) the motion|decision on the motion|motion .* granted|motion .* refused", lowered):
        return "motion_order_without_subject"
    return "unresolved_motion"


def build_report(report: dict[str, Any], candidate_limit: int = 30) -> dict[str, Any]:
    if candidate_limit < 1:
        raise ValueError("candidate_limit must be positive")
    unknown_events: list[dict[str, Any]] = []
    for case in report.get("cases", []):
        classification = case.get("classification", {})
        for event in classification.get("procedural_events", []):
            if not str(event.get("event_type", "")).startswith("motion") or event.get("subtype") != "unknown":
                continue
            text = str(event.get("text") or "")
            unknown_events.append(
                {
                    "activity_case_id": case.get("activity_case_id"),
                    "doc_id": event.get("doc_id"),
                    "event_type": event.get("event_type"),
                    "outcome": event.get("outcome"),
                    "source_document_date": event.get("source_document_date"),
                    "phrase_family": _phrase_family(text),
                    "review_status": "unknown",
                    "suggested_subtype": None,
                    "evidence": text[:240],
                }
            )
    family_counts = Counter(item["phrase_family"] for item in unknown_events)
    outcome_counts = Counter(str(item["outcome"] or "unknown") for item in unknown_events)
    candidates = sorted(
        unknown_events,
        key=lambda item: (
            item["phrase_family"],
            item["event_type"] or "",
            item["activity_case_id"] or 0,
            item["doc_id"] or 0,
        ),
    )[:candidate_limit]
    return {
        "report_version": "fc_activity_motion_unknowns_v1",
        "source_report": report.get("report_version"),
        "source_sample_size": report.get("sample_size_actual"),
        "unknown_motion_event_count": len(unknown_events),
        "phrase_family_counts": dict(sorted(family_counts.items())),
        "outcome_counts": dict(sorted(outcome_counts.items())),
        "candidate_limit": candidate_limit,
        "candidate_matrix": candidates,
        "rules_promoted": False,
        "database_written": False,
        "network_called": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--candidate-limit", type=int, default=30)
    args = parser.parse_args()
    report = build_report(json.loads(args.input.read_text(encoding="utf-8")), args.candidate_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("unknown_motion_event_count", "phrase_family_counts", "rules_promoted")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())