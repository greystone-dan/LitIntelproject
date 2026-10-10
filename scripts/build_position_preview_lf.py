"""Build "whose position" preview files from the proof-of-concept labelling runs (arm LF, one JSON per decision).

Input: folders of ``case_<id>_LF_<model>.json`` files (paragraphs with propositions: holder, layer, kind, text, quote).
Output: ``data/position_preview/case_<id>.json`` in the format the reader already loads (see ``build_position_preview.py``),
plus a paragraph level ``l`` derived the way the proof of concept found most reliable: a rule-of-law point about the law
is the legal framework, otherwise the level follows the holder (the model's own layer answers were less reliable).
Offline: no database, no model, no network. Decisions that already have a file are left alone.

    python scripts/build_position_preview_lf.py --src ai_poc_wide/out/LF --src ai_poc_wide/out_wave2/LF --src ai_poc_wide/out_wave3_300/LF
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parents[1] / "data" / "position_preview"
SOURCE = {"model": "gpt-4.1-mini", "prompt": "prop_v4+layer", "run": "wide_lf"}
_LAYER_KEY = {1: "judge", 2: "jr_party", 3: "earlier_decision", 4: "first_instance", 5: "source", 6: "framework"}


def point_layer(point: dict) -> int:
	"""Level of one point: law commentary is 6, a first-instance position reported inside the earlier decision is 4, else by holder."""
	holder, kind = point.get("holder") or "other", point.get("kind")
	if kind == "rule_of_law" and holder in ("court", "prior_court_or_authority", "earlier_decision_maker"):
		return 6
	if point.get("layer") == 4:
		return 4
	return {"court": 1, "applicant": 2, "respondent": 2, "earlier_decision_maker": 3, "witness_or_document": 5, "prior_court_or_authority": 5}.get(holder, 1)


def compact_case(raw: dict) -> dict:
	paragraphs: dict[str, dict] = {}
	for row in raw.get("paragraphs", []):
		points = row.get("propositions", [])
		if not points:
			continue
		holders = Counter(p.get("holder") or "other" for p in points)
		kinds = Counter(p.get("kind") for p in points if p.get("kind"))
		layers = Counter(point_layer(p) for p in points)
		top = max(layers.items(), key=lambda kv: (kv[1], -kv[0]))[0]
		paragraphs[str(row["para"])] = {
			"h": [name for name, _ in holders.most_common()],
			"k": [name for name, _ in kinds.most_common()],
			"s": (row.get("summary") or "").strip(),
			"r": row.get("role") or "other",
			"l": _LAYER_KEY[top],
		}
	return {"case_id": raw["case_id"], "source": SOURCE, "paragraphs": paragraphs}


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--src", required=True, type=Path, action="append", help="folder of arm-LF JSON files (repeatable)")
	parser.add_argument("--out", type=Path, default=OUT_DIR)
	args = parser.parse_args()
	args.out.mkdir(parents=True, exist_ok=True)
	written = skipped = 0
	for src in args.src:
		for path in sorted(src.glob("case_*.json")):
			case = compact_case(json.loads(path.read_text(encoding="utf-8")))
			target = args.out / f"case_{case['case_id']}.json"
			if target.exists() or not case["paragraphs"]:
				skipped += 1
				continue
			target.write_text(json.dumps(case, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n", encoding="utf-8")
			written += 1
	print(f"wrote {written} files to {args.out}, skipped {skipped} (already present or empty)")


if __name__ == "__main__":
	main()
