"""Build the compact per-decision "whose position" files the reader preview reads.

Input: the propositions run (batch 4) JSON files, one per decision, e.g. ``case_28105_prop_prop_v4_gpt-4.1-mini.json``.
Output: ``data/position_preview/case_<id>.json``. Offline and read-only against the database: no AI calls.

    python scripts/build_position_preview.py --src path/to/bundle5/props
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parents[1] / "data" / "position_preview"


def compact_case(raw: dict) -> dict:
	"""One decision: per paragraph the holders (most frequent first), statement kinds, one-line summary and role."""
	paragraphs: dict[str, dict] = {}
	for row in raw.get("paragraphs", []):
		holders = Counter(p.get("holder") or "other" for p in row.get("propositions", []))
		kinds = Counter(p.get("kind") for p in row.get("propositions", []) if p.get("kind"))
		if not holders:
			continue
		paragraphs[str(row["para"])] = {
			"h": [name for name, _ in holders.most_common()],
			"k": [name for name, _ in kinds.most_common()],
			"s": (row.get("summary") or "").strip(),
			"r": row.get("role") or "other",
		}
		if row.get("layer"):  # optional: set once layer detection exists
			paragraphs[str(row["para"])]["l"] = row["layer"]
	return {
		"case_id": raw["case_id"],
		"source": {"model": raw.get("model"), "prompt": raw.get("prompt_version"), "run": raw.get("run")},
		"paragraphs": paragraphs,
	}


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--src", required=True, type=Path, help="folder of propositions-run JSON files")
	parser.add_argument("--out", type=Path, default=OUT_DIR)
	args = parser.parse_args()
	args.out.mkdir(parents=True, exist_ok=True)
	count = 0
	for path in sorted(args.src.glob("case_*.json")):
		case = compact_case(json.loads(path.read_text(encoding="utf-8")))
		target = args.out / f"case_{case['case_id']}.json"
		target.write_text(json.dumps(case, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n", encoding="utf-8")
		count += 1
	print(f"wrote {count} files to {args.out}")


if __name__ == "__main__":
	main()
