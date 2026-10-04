#!/usr/bin/env python3
"""Offline, read-only CLI tool for phrase association analysis.

Analyzes 2-4 word phrases in allowed (applicant win) vs. dismissed
(minister win) decisions for a specific legal tag. Results are printed
to stdout. Uses the existing database access layer.

Usage:
    python scripts/phrase_analysis.py --tag "procedural fairness"
    python scripts/phrase_analysis.py --tag "due process" --judge judge_slug

Output: JSON with phrase counts and group denominators. Caveats describe
wording patterns, not causes of outcomes.
"""

import argparse
import json
import sys
from pathlib import Path

# Add backend to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.database import SessionLocal
from backend.language_analytics import MAX_DECISIONS, analyze_phrases_for_tag


def main():
	"""Parse arguments and run phrase analysis."""
	parser = argparse.ArgumentParser(
		description="Analyze phrase associations in case decisions by tag.",
		formatter_class=argparse.RawDescriptionHelpFormatter,
	)
	parser.add_argument(
		"--tag",
		required=True,
		type=str,
		help="Legal tag to analyze (required). Example: 'procedural fairness'",
	)
	parser.add_argument(
		"--judge",
		type=str,
		default=None,
		help="Optional judge profile slug to filter decisions. Example: 'judge_slug'",
	)
	parser.add_argument(
		"--max-decisions",
		type=int,
		default=MAX_DECISIONS,
		help=f"Maximum decisions to scan (default and hard maximum: {MAX_DECISIONS}).",
	)

	args = parser.parse_args()

	db = None
	try:
		db = SessionLocal()
		result = analyze_phrases_for_tag(
			db,
			tag=args.tag.strip(),
			judge_slug=args.judge.strip() if args.judge else None,
			max_decisions=args.max_decisions,
			min_phrase_frequency=5,
			top_phrases_per_side=25,
		)

		print(json.dumps(result.to_dict(), indent=2))
	except Exception:
		print("Phrase analysis failed. Check the input and local database configuration.", file=sys.stderr)
		sys.exit(1)
	finally:
		if db is not None:
			db.close()


if __name__ == "__main__":
	main()
