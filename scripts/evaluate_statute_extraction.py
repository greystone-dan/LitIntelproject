"""Evaluate deterministic statute extraction against exact-span fixtures."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import extract_statute_reference_matches

DEFAULT_FIXTURES = PROJECT_ROOT / "data" / "eval" / "statute_extraction_fixtures.json"


def evaluate_fixtures(fixtures: list[dict[str, Any]]) -> dict[str, Any]:
    expected_total = actual_total = exact_matches = false_positives = false_negatives = 0
    results = []
    for fixture in fixtures:
        expected = fixture.get("expected", [])
        actual = [
            {
                "kind": match.kind,
                "citation_text": match.citation_text,
                "normalized_citation": match.normalized_citation,
                "offset_start": match.offset_start,
                "offset_end": match.offset_end,
            }
            for match in extract_statute_reference_matches(fixture["text"])
        ]
        expected_total += len(expected)
        actual_total += len(actual)
        expected_keys = {(row["kind"], row["normalized_citation"], row["offset_start"], row["offset_end"]) for row in expected}
        actual_keys = {(row["kind"], row["normalized_citation"], row["offset_start"], row["offset_end"]) for row in actual}
        exact = len(expected_keys & actual_keys)
        missing = sorted(expected_keys - actual_keys)
        extra = sorted(actual_keys - expected_keys)
        exact_matches += exact
        false_negatives += len(missing)
        false_positives += len(extra)
        results.append({"id": fixture["id"], "expected": len(expected), "actual": len(actual), "exact_matches": exact, "missing": missing, "extra": extra, "passed": not missing and not extra})
    precision = exact_matches / actual_total if actual_total else 1.0 if expected_total == 0 else 0.0
    recall = exact_matches / expected_total if expected_total else 1.0
    return {"fixture_count": len(fixtures), "expected_total": expected_total, "actual_total": actual_total, "exact_matches": exact_matches, "false_positives": false_positives, "false_negatives": false_negatives, "precision_pct": round(precision * 100, 2), "recall_pct": round(recall * 100, 2), "exact_span_accuracy_pct": round(exact_matches / expected_total * 100, 2) if expected_total else 100.0, "passed": false_positives == 0 and false_negatives == 0, "results": results}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixtures", type=Path, default=DEFAULT_FIXTURES)
    parser.add_argument("--output-file", type=Path)
    args = parser.parse_args()
    report = evaluate_fixtures(json.loads(args.fixtures.read_text(encoding="utf-8")))
    if args.output_file:
        args.output_file.parent.mkdir(parents=True, exist_ok=True)
        args.output_file.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "results"}, indent=2))
    if not report["passed"]:
        for result in report["results"]:
            if not result["passed"]:
                print(json.dumps(result, indent=2), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
