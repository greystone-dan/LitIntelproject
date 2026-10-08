"""Score a tagging run's roles against role_reference_60.json (60 paragraphs in 4 cases, one reader, so a rough guide only)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REFERENCE = json.loads((Path(__file__).parent / "role_reference_60.json").read_text(encoding="utf-8"))["roles"]


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("dirs", nargs="+", type=Path)
	args = parser.parse_args()
	for directory in args.dirs:
		right = total = 0
		for case_id, labels in REFERENCE.items():
			path = directory / f"case_{case_id}_tags.json"
			if not path.exists():
				continue
			by_index = {str(a["paragraph_index"]): a["role"] for a in json.loads(path.read_text(encoding="utf-8"))["assessments"]}
			for index, role in labels.items():
				total += 1
				right += by_index.get(index) == role
		print(json.dumps({"run_dir": str(directory), "right": right, "of": total, "accuracy": round(right / total, 3) if total else None}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
