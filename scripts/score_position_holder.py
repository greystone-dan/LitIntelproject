"""Score backend/position_holder.py against stored model labels.

Offline only: reads two folders of JSON (no database, no network).
  --props    folder of proposition files (para number, propositions with holder)
  --reports  folder of deterministic case reports holding the paragraph text
Example:
  python scripts/score_position_holder.py --props ai_poc_data/bundle5/props \
      --reports ai_poc_data/bundle4/recent/reports --out position_holder_scores.json
The stored labels are model output, not a lawyer's truth; this measures agreement only.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from backend.position_holder import (  # noqa: E402
	APPLICANT, COURT, HOLDERS, RESPONDENT, detect_forum, parse_parties, split_numbered_paragraphs, split_sentences, tag_paragraph,
)

_WORD = re.compile(r"[a-z0-9]{3,}")


def best_sentence(prop_text: str, sentences: list[str]) -> int:
	want = set(_WORD.findall(prop_text.lower()))
	best, best_i = -1.0, 0
	for i, s in enumerate(sentences):
		have = set(_WORD.findall(s.lower()))
		score = len(want & have) / (len(want) ** 0.5 * max(len(have), 1) ** 0.5 + 1e-9)
		if score > best:
			best, best_i = score, i
	return best_i


def load_case(props_path: str, reports_dir: str):
	props = json.load(open(props_path, encoding="utf-8"))
	cid = props["case_id"]
	rp = os.path.join(reports_dir, f"case_{cid}_deterministic.json")
	if not os.path.exists(rp):
		return None
	rep = json.load(open(rp, encoding="utf-8"))
	text = "\n".join(p["text"] for p in rep["paragraphs"])
	title = rep["paragraphs"][0]["text"].splitlines()[0] if rep["paragraphs"] else ""
	return cid, props, title, split_numbered_paragraphs(text), detect_forum(rep["paragraphs"][0]["text"] if rep["paragraphs"] else "")


def run(props_dir: str, reports_dir: str, literal: bool = False) -> dict:
	pairs: Counter = Counter()  # (stored, predicted) for propositions
	para_pairs: Counter = Counter()
	examples: dict[tuple[str, str], list] = defaultdict(list)
	minister_first_cases = []
	n_props = n_missing = 0
	mf_n = mf_ok = 0
	by_conf: Counter = Counter()
	by_conf_ok: Counter = Counter()
	for pf in sorted(glob.glob(os.path.join(props_dir, "*.json"))):
		loaded = load_case(pf, reports_dir)
		if not loaded:
			continue
		cid, props, title, texts, forum = loaded
		parties = parse_parties(title)
		parties.forum = forum
		parties.normalize = not literal
		if parties.minister_first:
			minister_first_cases.append((cid, title))
		prev = None
		for row in props["paragraphs"]:
			num = row["para"]
			text = texts.get(num)
			if not text:
				n_missing += len(row["propositions"])
				continue
			res = tag_paragraph(text, parties, previous=prev)
			prev = res.sentence_holders[-1] if res.sentence_holders and res.sentence_holders[-1] != COURT else None
			sents = split_sentences(text)
			stored = {p["holder"] for p in row["propositions"]}
			for h in HOLDERS:
				para_pairs[(h, h in stored, h in res.holders)] += 1
			for p in row["propositions"]:
				if p["holder"] == "other":
					continue
				i = best_sentence(p["text"], sents) if sents else 0
				pred = res.sentence_holders[i] if i < len(res.sentence_holders) else COURT
				conf = res.cues[i].confidence if i < len(res.cues) else "default"
				n_props += 1
				pairs[(p["holder"], pred)] += 1
				by_conf[conf] += 1
				if parties.minister_first and p["holder"] in (APPLICANT, RESPONDENT):
					mf_n += 1
					mf_ok += pred == p["holder"]
				by_conf_ok[conf] += pred == p["holder"]
				if pred != p["holder"] and len(examples[(p["holder"], pred)]) < 4:
					examples[(p["holder"], pred)].append({
						"case_id": cid, "para": num, "proposition": p["text"],
						"sentence": sents[i] if sents else text[:200]})
	per_label = {}
	for h in HOLDERS:
		tp = pairs[(h, h)]
		stored_n = sum(v for (s, _), v in pairs.items() if s == h)
		pred_n = sum(v for (_, p), v in pairs.items() if p == h)
		per_label[h] = {
			"stored": stored_n, "predicted": pred_n, "agree": tp,
			"recall": round(tp / stored_n, 3) if stored_n else None,
			"precision": round(tp / pred_n, 3) if pred_n else None,
		}
	agree = sum(pairs[(h, h)] for h in HOLDERS)
	para_label = {}
	for h in HOLDERS:
		tp = para_pairs[(h, True, True)]
		fn = para_pairs[(h, True, False)]
		fp = para_pairs[(h, False, True)]
		para_label[h] = {"tp": tp, "fn": fn, "fp": fp,
			"recall": round(tp / (tp + fn), 3) if tp + fn else None,
			"precision": round(tp / (tp + fp), 3) if tp + fp else None}
	confusion = sorted(((s, p, v) for (s, p), v in pairs.items() if s != p), key=lambda t: -t[2])
	return {
		"propositions_scored": n_props, "propositions_without_text": n_missing,
		"overall_agreement": round(agree / n_props, 3) if n_props else None,
		"per_label": per_label, "paragraph_level": para_label,
		"by_confidence": {k: {"n": v, "agree": by_conf_ok[k], "rate": round(by_conf_ok[k] / v, 3)}
			for k, v in by_conf.items()},
		"biggest_disagreements": [{"stored": s, "rules": p, "count": v, "examples": examples[(s, p)]}
			for s, p, v in confusion[:10]],
		"minister_first_cases": minister_first_cases,
		"minister_first_party_propositions": {"n": mf_n, "agree": mf_ok},
		"mode": "literal" if literal else "normalized",
	}


def main() -> None:
	ap = argparse.ArgumentParser(description=__doc__)
	ap.add_argument("--props", required=True)
	ap.add_argument("--reports", required=True)
	ap.add_argument("--out")
	ap.add_argument("--literal", action="store_true", help="treat applicant/respondent as the title says, not as individual/Minister")
	a = ap.parse_args()
	out = run(a.props, a.reports, a.literal)
	text = json.dumps(out, indent=1, ensure_ascii=False)
	if a.out:
		open(a.out, "w", encoding="utf-8").write(text)
	print(json.dumps({k: out[k] for k in ("propositions_scored", "propositions_without_text",
		"overall_agreement", "per_label", "by_confidence", "minister_first_party_propositions", "mode")}, indent=1))


if __name__ == "__main__":
	main()
