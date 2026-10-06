"""Measure section-level statute extraction against the frozen gold set.

Gold file: data/eval/statute_section_gold.json (synthetic CBSA-style sentences with the
instrument and pinpoint a careful reader would extract; lists are expected one pair per
section). Cases with "holdout": true are frozen for before/after comparison: never tune
extraction rules on them. Pure measurement, no database, no network.

Usage: python scripts/evaluate_statute_sections.py [--split dev|holdout|all] [--misses] [--json out.json]
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import extract_statute_reference_matches
from backend.statutes import normalize_provision_pinpoint, parse_legislation_citation

DEFAULT_GOLD = PROJECT_ROOT / "data" / "eval" / "statute_section_gold.json"


def extracted_pairs(text: str) -> set[tuple[str, str]]:
    pairs: set[tuple[str, str]] = set()
    for match in extract_statute_reference_matches(text):
        parsed = parse_legislation_citation(match.normalized_citation or match.citation_text)
        if parsed is not None and parsed.instrument_key and parsed.pinpoint:
            pairs.add((parsed.instrument_key, normalize_provision_pinpoint(parsed.pinpoint)))
    return pairs


def evaluate(cases: list[dict[str, Any]], split: str = "all") -> dict[str, Any]:
    selected = [c for c in cases if split == "all" or (split == "holdout") == bool(c.get("holdout"))]
    tp = fp = fn = 0
    by_tag: dict[str, list[int]] = defaultdict(lambda: [0, 0])  # tag -> [found, expected]
    misses: list[dict[str, Any]] = []
    extras: list[dict[str, Any]] = []
    for case in selected:
        expected = {(e["instrument_key"], normalize_provision_pinpoint(e["pinpoint"])) for e in case["expected"]}
        found = extracted_pairs(case["text"])
        hit = expected & found
        tp += len(hit)
        fn += len(expected - found)
        fp += len(found - expected)
        for tag in case.get("tags", []):
            by_tag[tag][0] += len(hit)
            by_tag[tag][1] += len(expected)
        if expected - found:
            misses.append({"id": case["id"], "text": case["text"], "missing": sorted(expected - found), "found": sorted(found)})
        if found - expected:
            extras.append({"id": case["id"], "text": case["text"], "extra": sorted(found - expected)})
    expected_total = tp + fn
    return {
        "split": split,
        "cases": len(selected),
        "expected_pairs": expected_total,
        "recall_pct": round(tp * 100 / expected_total, 1) if expected_total else 100.0,
        "precision_pct": round(tp * 100 / (tp + fp), 1) if tp + fp else 100.0,
        "false_positive_pairs": fp,
        "by_tag_recall_pct": {t: round(v[0] * 100 / v[1], 1) if v[1] else None for t, v in sorted(by_tag.items())},
        "misses": misses,
        "extras": extras,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gold", type=Path, default=DEFAULT_GOLD)
    parser.add_argument("--split", choices=["dev", "holdout", "all"], default="all")
    parser.add_argument("--misses", action="store_true", help="print every miss and false positive")
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()
    result = evaluate(json.loads(args.gold.read_text(encoding="utf-8")), args.split)
    summary = {k: v for k, v in result.items() if k not in {"misses", "extras"}}
    print(json.dumps(summary, indent=2))
    if args.misses:
        for row in result["misses"]:
            print("MISS", row["id"], row["text"][:90], "missing", row["missing"], "found", row["found"])
        for row in result["extras"]:
            print("EXTRA", row["id"], row["text"][:90], row["extra"])
    if args.json:
        args.json.write_text(json.dumps(result, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
