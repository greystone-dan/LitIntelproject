"""Tag decisions with the rules + learned whose-position tagger and write one compact file per decision.

Offline: reads decision texts from a folder of <id>.json files (title, full_text; ``scripts/fetch_position_texts.py``
writes them) and writes ``<out>/case_<id>.json`` in the shape ``backend/position_tags.py`` reads when
ILIT_LEARNED_POSITIONS=1. No database, no network, no model call. Nothing is loaded anywhere by this script.

    python scripts/build_position_tags.py --texts position_texts --out data/position_learned [--limit 100]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
	sys.path.insert(0, str(REPO_ROOT))

from backend import learned_positions as lp  # noqa: E402

VERSION = "positions_learned_v1"


def tag_case(stored: dict) -> dict | None:
	full = stored.get("full_text") or ""
	numbers, tags = lp.tag_decision_text(full, stored.get("title") or "")
	if not numbers:
		return None
	return {
		"case_id": stored.get("id"),
		"source": {"tagger": VERSION, "learned": lp.available()},
		"paragraphs": {str(n): {"h": t["holder"], "p": t["p"]} for n, t in zip(numbers, tags)},
	}


def main(argv=None) -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--texts", type=Path, required=True)
	parser.add_argument("--out", type=Path, required=True)
	parser.add_argument("--limit", type=int, default=0)
	args = parser.parse_args(argv)
	args.out.mkdir(parents=True, exist_ok=True)
	written = skipped = 0
	for path in sorted(args.texts.glob("*.json")):
		if args.limit and written >= args.limit:
			break
		case = tag_case(json.loads(path.read_text(encoding="utf-8")))
		if case is None:
			skipped += 1
			continue
		case["case_id"] = case["case_id"] or int(path.stem)
		(args.out / f"case_{case['case_id']}.json").write_text(json.dumps(case, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
		written += 1
	print(f"wrote {written} files to {args.out}; {skipped} had no numbered paragraphs")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
