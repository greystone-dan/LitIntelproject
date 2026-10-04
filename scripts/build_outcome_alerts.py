#!/usr/bin/env python3
"""Offline builder for saved-search outcome alerts.

Usage: python scripts/build_outcome_alerts.py input.json --output output.json

Input JSON should contain: {"saved_search": {...}, "cases": [...], "outcomes": [...], "since": optional iso str }

This script is intentionally offline and uses only the pure fixture helper.
"""
import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.outcome_alerts import compute_alerts_from_fixture


def main(argv=None):
    parser = argparse.ArgumentParser(description="Offline builder for saved-search outcome alerts")
    parser.add_argument("input", help="Path to input JSON file")
    parser.add_argument("--output", "-o", help="Path to output JSON file (defaults to stdout)")
    parser.add_argument("--as-of", help="ISO datetime to use as 'now' for windowing (optional)")
    args = parser.parse_args(argv)

    try:
        with open(args.input, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except Exception as e:
        print(f"Error reading input JSON: {e}", file=sys.stderr)
        return 2

    saved = data.get("saved_search") or {}
    cases = data.get("cases") or []
    outcomes = data.get("outcomes") or []
    since = data.get("since")
    out = compute_alerts_from_fixture(saved, cases, outcomes, since=since, as_of=args.as_of)

    try:
        if args.output:
            with open(args.output, "w", encoding="utf-8") as oh:
                json.dump(out, oh, default=str, indent=2)
        else:
            print(json.dumps(out, default=str, indent=2))
    except Exception as e:
        print(f"Error writing output JSON: {e}", file=sys.stderr)
        return 3

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
