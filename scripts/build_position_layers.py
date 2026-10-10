"""Build per-paragraph rule-based holder and layer files for the reader preview.

Offline: reads two folders of JSON (propositions files for the paragraph numbers, case reports for the text),
no database, no model, no network. Output ``data/position_layers/case_<id>.json``:

    {"case_id": 28105, "source": {...}, "frame": "...",
     "paragraphs": {"13": {"l": 2, "h": ["respondent"], "law": false, "mixed": false, "c": "explicit"}}}

``l`` is the one layer the reader shows (1 judge, 2 submissions to the court, 3 earlier decision maker,
4 first-instance party as reported, 5 witness or document, 6 legal framework / precedent commentary), the same
field name the reader preview uses for a stored layer. ``h`` are the rules' holders, ``law`` marks a paragraph with
any layer-6 sentence, ``mixed`` marks two or more of layers 1-4 in the paragraph, ``c`` is how the paragraph layer
was decided (explicit cue, lead_in, carried, default).

    python scripts/build_position_layers.py --props ai_poc_data/bundle5/props --reports ai_poc_data/bundle4/recent/reports
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from backend.case_frame import build_frame  # noqa: E402
from backend.opinion_parts import opinion_parts, part_of  # noqa: E402
from backend.position_holder import RULES_VERSION, parties_from_frame, split_numbered_paragraphs, tag_paragraph  # noqa: E402

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "position_layers")


def paragraph_layer(res) -> tuple[int, str]:
	"""One layer per paragraph: the most common layer among explicit cues (first sentence wins a tie);
	with no explicit cue, the most common among all sentences."""
	explicit = [c for c in res.cues if c.confidence in ("explicit", "lead_in")]
	pool = explicit or res.cues
	if not pool:
		return 1, "default"
	counts = Counter(c.layer for c in pool)
	best = max(counts.values())
	for c in pool:
		if counts[c.layer] == best:
			return c.layer, ("explicit" if explicit else pool[0].confidence)
	return 1, "default"


def build_case(props: dict, report: dict) -> dict:
	header = report["paragraphs"][0]["text"] if report["paragraphs"] else ""
	frame = build_frame(header, "\n".join(p["text"] for p in report["paragraphs"][1:]))
	parties = parties_from_frame(frame, header.splitlines()[0] if header else "")
	texts = split_numbered_paragraphs("\n".join(p["text"] for p in report["paragraphs"]))
	parts = opinion_parts("\n".join(p["text"] for p in report["paragraphs"]))["parts"]
	out: dict[str, dict] = {}
	lead = None
	for num in sorted(int(k["para"]) for k in props["paragraphs"]):
		text = texts.get(num)
		if not text:
			continue
		res = tag_paragraph(text, parties, lead=lead)
		lead = res.lead_out
		layer, how = paragraph_layer(res)
		out[str(num)] = {"l": layer, "h": res.holders, "law": res.has_framework, "mixed": res.mixed_layers, "c": how}
		kind = part_of(parts, num)
		if kind != "majority":
			out[str(num)]["o"] = kind  # a dissenting or concurring paragraph: the judges' own view, not the Court's holding
	return {"case_id": props["case_id"], "source": {"rules": RULES_VERSION}, "frame": frame.text(), "paragraphs": out}


def main() -> None:
	ap = argparse.ArgumentParser(description=__doc__)
	ap.add_argument("--props", required=True)
	ap.add_argument("--reports", required=True)
	ap.add_argument("--out", default=OUT_DIR)
	a = ap.parse_args()
	os.makedirs(a.out, exist_ok=True)
	n = 0
	for pf in sorted(glob.glob(os.path.join(a.props, "case_*.json"))):
		props = json.load(open(pf, encoding="utf-8"))
		rp = os.path.join(a.reports, f"case_{props['case_id']}_deterministic.json")
		if not os.path.exists(rp):
			continue
		case = build_case(props, json.load(open(rp, encoding="utf-8")))
		with open(os.path.join(a.out, f"case_{case['case_id']}.json"), "w", encoding="utf-8") as fh:
			fh.write(json.dumps(case, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n")
		n += 1
	print(f"wrote {n} files to {a.out}")


if __name__ == "__main__":
	main()
