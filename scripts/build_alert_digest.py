"""Build an offline saved-search digest from enriched JSON on stdin or --input."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.alert_digest import (
	build_alert_digest,
	parse_timestamp,
	partition_matches,
	render_digest_html,
	render_digest_text,
)


def main(argv: list[str] | None = None) -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--input", type=Path, help="Enriched JSON snapshot; default: stdin")
	parser.add_argument("--since", type=parse_timestamp, help="ISO timestamp overriding saved-search last checks")
	parser.add_argument("--out", type=Path, help="Output file; default: stdout")
	parser.add_argument("--format", choices=("html", "text", "json"), default="html")
	args = parser.parse_args(argv)
	try:
		payload = json.loads(args.input.read_text(encoding="utf-8") if args.input else sys.stdin.read())
		searches = payload["saved_searches"]
		new, earlier = partition_matches(searches, payload["matches"], since=args.since)
		digest = build_alert_digest(searches, new, earlier)
		output = (
			render_digest_html(digest) if args.format == "html" else
			render_digest_text(digest) if args.format == "text" else
			json.dumps(digest, ensure_ascii=False, indent=2) + "\n"
		)
		if args.out:
			args.out.write_text(output, encoding="utf-8")
		else:
			print(output, end="")
	except (OSError, ValueError, KeyError, TypeError) as exc:
		parser.error(f"Invalid digest input/output: {exc}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
