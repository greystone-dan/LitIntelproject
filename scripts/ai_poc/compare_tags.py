"""Compare two paragraph-tagging runs. Offline, no model calls, no database.

Each side is a directory of either v2 `case_<id>_tags.json` files or old-run review files
(`case_<id>_paragraph_assessment.md` with a Paragraph|Topic|Role|Confidence|Explanation table).
Topics are free text, so topic agreement = word overlap (Jaccard >= 0.4 after dropping stop words); it is a rough
consistency signal, not accuracy. Roles are only compared when both sides use the v2 role list.
Writes a summary JSON and a CSV of paragraphs for a person to judge (disagreements plus some agreements).
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
from pathlib import Path

REPORTS = Path(__file__).resolve().parents[2] / "data" / "eval" / "llm_discussion_units_pilot" / "core_300_run" / "reports"
STOP = {"the", "of", "and", "a", "an", "in", "on", "to", "for", "by", "with", "at", "as", "is", "was", "from", "or"}


def words(text: str) -> set[str]:
	return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP}


def similar(a: str, b: str) -> bool:
	wa, wb = words(a), words(b)
	return bool(wa and wb) and len(wa & wb) / len(wa | wb) >= 0.4


def load_side(directory: Path) -> dict[int, dict[int, dict]]:
	cases: dict[int, dict[int, dict]] = {}
	for path in directory.glob("case_*"):
		match = re.match(r"case_(\d+)_", path.name)
		if not match:
			continue
		case_id = int(match.group(1))
		rows: dict[int, dict] = {}
		if path.name.endswith("_tags.json"):
			for item in json.loads(path.read_text(encoding="utf-8")).get("assessments", []):
				rows[int(item["paragraph_index"])] = item
		elif path.name.endswith("_paragraph_assessment.md"):
			for line in path.read_text(encoding="utf-8").splitlines():
				cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
				if len(cells) >= 5 and cells[0].isdigit() and cells[1] != "Not found":
					rows[int(cells[0])] = {"topic": cells[1], "role": cells[2], "confidence": cells[3], "explanation": cells[4]}
		if rows:
			cases[case_id] = rows
	return cases


def boundaries(rows: dict[int, dict], indices: list[int]) -> set[int]:
	out = set()
	for prev, cur in zip(indices, indices[1:]):
		if not similar(rows[prev]["topic"], rows[cur]["topic"]):
			out.add(cur)
	return out


def paragraph_texts(case_id: int) -> dict[int, str]:
	import sys
	sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
	sys.path.insert(0, str(Path(__file__).resolve().parent))
	from tag_paragraphs import load_paragraphs

	path = REPORTS / f"case_{case_id}_deterministic.json"
	if not path.exists():
		return {}
	return {p["paragraph_index"]: p["text"] for p in load_paragraphs(json.loads(path.read_text(encoding="utf-8")))}


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--a", type=Path, required=True)
	parser.add_argument("--b", type=Path, required=True)
	parser.add_argument("--label-a", default="A")
	parser.add_argument("--label-b", default="B")
	parser.add_argument("--out", type=Path, required=True, help="Prefix for <out>_summary.json and <out>_sample.csv")
	parser.add_argument("--sample", type=int, default=60)
	parser.add_argument("--seed", type=int, default=7)
	args = parser.parse_args()
	a_side, b_side = load_side(args.a), load_side(args.b)
	common = sorted(set(a_side) & set(b_side))
	both = topic_same = role_same = role_n = 0
	tp = fa = fn = 0
	pairs = []
	for case_id in common:
		a, b = a_side[case_id], b_side[case_id]
		indices = sorted(set(a) & set(b))
		for i in indices:
			both += 1
			same_topic = similar(a[i]["topic"], b[i]["topic"])
			topic_same += same_topic
			same_role = None
			if a[i]["role"] in ROLE_SET and b[i]["role"] in ROLE_SET:
				role_n += 1
				same_role = a[i]["role"] == b[i]["role"]
				role_same += same_role
			pairs.append((case_id, i, same_topic, same_role))
		ba, bb = boundaries(a, indices), boundaries(b, indices)
		tp += len(ba & bb)
		fa += len(ba - bb)
		fn += len(bb - ba)
	precision = tp / (tp + fa) if tp + fa else 0.0
	recall = tp / (tp + fn) if tp + fn else 0.0
	summary = {
		"a": args.label_a, "b": args.label_b, "cases_in_common": len(common),
		"paragraphs_tagged_a": sum(len(v) for v in a_side.values()), "paragraphs_tagged_b": sum(len(v) for v in b_side.values()),
		"paragraphs_in_both": both,
		"topic_similar_rate": round(topic_same / both, 3) if both else None,
		"role_agreement_rate": round(role_same / role_n, 3) if role_n else None, "role_compared": role_n,
		"topic_change_agreement": {"both": tp, "only_a": fa, "only_b": fn, "f1": round(2 * precision * recall / (precision + recall), 3) if precision + recall else None},
	}
	args.out.parent.mkdir(parents=True, exist_ok=True)
	Path(f"{args.out}_summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
	rng = random.Random(args.seed)
	disagree = [p for p in pairs if (p[3] is False) or not p[2]]
	agree = [p for p in pairs if p not in disagree]
	picked = rng.sample(disagree, min(len(disagree), args.sample * 2 // 3)) + rng.sample(agree, min(len(agree), args.sample // 3))
	rng.shuffle(picked)
	with Path(f"{args.out}_sample.csv").open("w", newline="", encoding="utf-8") as handle:
		writer = csv.writer(handle)
		writer.writerow(["case_id", "paragraph", "text_excerpt", f"{args.label_a}_topic", f"{args.label_a}_role", f"{args.label_b}_topic", f"{args.label_b}_role", "better (A/B/both/neither)"])
		for case_id, i, _, _ in picked:
			texts = paragraph_texts(case_id)
			writer.writerow([case_id, i, texts.get(i, "")[:500].replace("\n", " "), a_side[case_id][i]["topic"], a_side[case_id][i]["role"],
				b_side[case_id][i]["topic"], b_side[case_id][i]["role"], ""])
	print(json.dumps(summary, indent=1))
	return 0


ROLE_SET = {"procedural_history", "background_facts", "issue_framing", "legal_test", "party_position", "evidence_assessment", "reasoning_application", "disposition", "other"}

if __name__ == "__main__":
	raise SystemExit(main())
