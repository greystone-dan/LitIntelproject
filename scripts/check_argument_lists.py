"""Score the arguments in an exported case-frame list and flag the least supported ones (files only).

Reads a JSON list of decisions ``{"id", "applicant_is_minister", "paragraphs": {"12": "text"}, "arguments": [{"side", "para", "text"}]}``
and writes the same list with a score on every argument and the weakest marked ``flagged``. Nothing is deleted and the
database is not touched. Off unless ILIT_ARGUMENT_CHECKER is set.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from backend.argument_checker import enabled, flag_lowest, score_arguments  # noqa: E402


def main() -> int:
	p = argparse.ArgumentParser(description=__doc__)
	p.add_argument("input")
	p.add_argument("output")
	p.add_argument("--share", type=float, default=0.2, help="Share of arguments per decision to flag (default 0.2).")
	args = p.parse_args()
	if not enabled():
		print("ILIT_ARGUMENT_CHECKER is not set; nothing done.")
		return 0
	data = json.loads(Path(args.input).read_text(encoding="utf-8"))
	flagged = 0
	for d in data:
		paras = {int(k): v for k, v in d.get("paragraphs", {}).items()}
		scored = flag_lowest(score_arguments(d.get("arguments", []), paras, d.get("applicant_is_minister")), args.share)
		flagged += sum(1 for s in scored if s["flagged"])
		d["arguments"] = scored
	Path(args.output).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
	print(f"{len(data)} decisions, {flagged} arguments flagged -> {args.output}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
