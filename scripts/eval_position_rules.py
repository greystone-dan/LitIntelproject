"""Score the deterministic whose-position rules against graded labels, with a fixed train / held-out split.

Offline, no model. Inputs:
  --gold   one or more JSON files {case_id: {para: {"h": [holders], "l": [layers], "src": ...}}}
           (reader grades: data/eval/position_gold_reader.json; AI tags: data/eval/position_gold_ai.json; both hold labels only)
  --texts  folder of case_<id>.json or <id>.json files holding {"title", "court", "full_text"}
           (``scripts/fetch_position_texts.py`` writes them from the public pages; nothing is stored in the database)

The split is by decision (sha1 of the case id), so a decision is never in both sets. Develop on ``train``; ``test``
is the held-out set and is reported, never tuned on.

Metrics are per paragraph: the set of holders the rules found against the set the label says. Layers are compared
with the one layer the reader shows for the paragraph (``paragraph_layer``) and count as right when it is among the
labelled layers.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from backend.case_frame import build_frame  # noqa: E402
from backend.position_holder import (  # noqa: E402
	HOLDERS, parties_from_frame, split_numbered_paragraphs, tag_paragraph,
)
from scripts.build_position_layers import paragraph_layer  # noqa: E402

TEST_SHARE = 30  # percent of decisions held out


def split_of(case_id: int | str) -> str:
	h = int(hashlib.sha1(f"position-split-{case_id}".encode()).hexdigest(), 16) % 100
	return "test" if h < TEST_SHARE else "train"


def load_text(texts_dir: str, case_id: int) -> dict | None:
	for name in (f"{case_id}.json", f"case_{case_id}.json"):
		p = os.path.join(texts_dir, name)
		if os.path.exists(p):
			return json.load(open(p, encoding="utf-8"))
	return None


def tag_case(rec: dict) -> dict[int, dict]:
	"""Run the rules over one decision exactly as the layer builder does. Returns {para: {holders, layer, cues}}."""
	text = rec["full_text"] or ""
	paras = split_numbered_paragraphs(text)
	if not paras:
		return {}
	first = min(paras)
	start = text.find(paras[first][:40])
	header = text[:start] if start > 0 else text[:1500]
	body = text[start:] if start > 0 else text
	frame = build_frame(header, body)
	title = header.splitlines()[0] if header.strip() else (rec.get("title") or "")
	parties = parties_from_frame(frame, title)
	out: dict[int, dict] = {}
	prev = None
	lead = None
	for num in sorted(paras):
		res = tag_paragraph(paras[num], parties, previous=prev, lead=lead)
		lead = res.lead_out
		last_any = res.sentence_holders[-1] if res.sentence_holders else None
		if last_any in (parties.author, None) or re.match(r"^\s*(?:\[\d+\]\s*)?(?:I\b|In my\b)", paras[num]):
			prev = None
		else:
			prev = last_any
		layer, conf = paragraph_layer(res)
		out[num] = {"holders": list(res.holders), "layer": layer, "conf": conf,
			"sent": list(res.sentence_holders), "layers": list(res.layers)}
	return out


def prf(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
	p = tp / (tp + fp) if tp + fp else 0.0
	r = tp / (tp + fn) if tp + fn else 0.0
	f = 2 * p * r / (p + r) if p + r else 0.0
	return round(p, 3), round(r, 3), round(f, 3)


def evaluate(gold: dict, texts_dir: str, which: str, rules=tag_case) -> dict:
	cache: dict[int, dict] = {}
	holder_counts = {h: [0, 0, 0] for h in HOLDERS}  # tp fp fn
	exact = n = 0
	by_court: dict[str, list[int]] = defaultdict(lambda: [0, 0])
	layer_n = layer_ok = 0
	layer_by_gold: dict[int, list[int]] = defaultdict(lambda: [0, 0])
	confusion: Counter = Counter()
	missing = 0
	decisions = 0
	per_decision: dict[str, list[int]] = {}  # case id -> [tp, fp, fn, tp_non_court, fp_non_court, fn_non_court]
	for cid_s, paras in gold.items():
		if which != "all" and split_of(cid_s) != which:
			continue
		rec = load_text(texts_dir, int(cid_s))
		if not rec:
			missing += 1
			continue
		pred = cache.get(int(cid_s))
		if pred is None:
			pred = cache[int(cid_s)] = rules(rec)
		decisions += 1
		court = rec.get("court") or "?"
		for p_s, lab in paras.items():
			pr = pred.get(int(p_s))
			if pr is None:
				continue
			g = {h for h in lab["h"] if h in HOLDERS}
			if not g:
				continue
			r = set(pr["holders"])
			n += 1
			ok = g == r
			exact += ok
			by_court[court][0] += ok
			by_court[court][1] += 1
			dc = per_decision.setdefault(cid_s, [0, 0, 0, 0, 0, 0])
			for h in HOLDERS:
				k = None
				if h in g and h in r:
					k = 0
				elif h in r:
					k = 1
				elif h in g:
					k = 2
				if k is not None:
					holder_counts[h][k] += 1
					dc[k] += 1
					if h != "court":
						dc[3 + k] += 1
			if not ok:
				for gh in g - r:
					for rh in (r - g) or {"none"}:
						confusion[(gh, rh)] += 1
			if lab["l"]:
				layer_n += 1
				hit = pr["layer"] in lab["l"]
				layer_ok += hit
				for gl in lab["l"]:
					layer_by_gold[gl][0] += pr["layer"] == gl
					layer_by_gold[gl][1] += 1
	tp = sum(c[0] for c in holder_counts.values())
	fp = sum(c[1] for c in holder_counts.values())
	fn = sum(c[2] for c in holder_counts.values())
	nc = [h for h in HOLDERS if h != "court"]
	tp2 = sum(holder_counts[h][0] for h in nc)
	fp2 = sum(holder_counts[h][1] for h in nc)
	fn2 = sum(holder_counts[h][2] for h in nc)
	return {
		"split": which, "decisions": decisions, "missing_texts": missing, "paragraphs": n,
		"exact_set_match": round(exact / n, 3) if n else None,
		"micro": dict(zip(("p", "r", "f1"), prf(tp, fp, fn))),
		"micro_non_court": dict(zip(("p", "r", "f1"), prf(tp2, fp2, fn2))),
		"per_holder": {h: dict(zip(("p", "r", "f1"), prf(*c)), support=c[0] + c[2]) for h, c in holder_counts.items()},
		"by_court": {k: {"paragraphs": v[1], "exact": round(v[0] / v[1], 3)} for k, v in sorted(by_court.items())},
		"layer": {"paragraphs": layer_n, "right": round(layer_ok / layer_n, 3) if layer_n else None,
			"recall_by_layer": {str(k): {"n": v[1], "recall": round(v[0] / v[1], 3)} for k, v in sorted(layer_by_gold.items())}},
		"per_decision": per_decision,
		"top_confusions": [[a, b, c] for (a, b), c in confusion.most_common(8)],
	}


def main() -> None:
	ap = argparse.ArgumentParser()
	ap.add_argument("--gold", action="append", required=True)
	ap.add_argument("--texts", required=True)
	ap.add_argument("--split", choices=("train", "test", "all"), default="test")
	ap.add_argument("--out")
	args = ap.parse_args()
	report = {}
	for g in args.gold:
		gold = json.load(open(g, encoding="utf-8"))
		report[os.path.basename(g)] = evaluate(gold, args.texts, args.split)
	text = json.dumps(report, indent=1)
	if args.out:
		open(args.out, "w", encoding="utf-8").write(text)
	print(text)


if __name__ == "__main__":
	main()
