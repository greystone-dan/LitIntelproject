"""No-AI matching of extracted draft arguments to decided issues in the library (stage 2 issue maps). TF-IDF cosine on issue wording, standard library only.
Self-retrieval test: for each draft argument, is an issue of the draft's own source case in the top-k of all library issues?
Usage: python match_library.py --arm F41 --k 3"""
from __future__ import annotations
import argparse, glob, json, math, re
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent
STOP = set("the a an of to in and or is are was were be by for on at with as that this did does do whether it its his her their court err erred unreasonable reasonable".split())

def toks(s):
	return [w for w in re.findall(r"[a-zà-ÿ0-9]{3,}", s.lower()) if w not in STOP]

def library(model="gpt-4.1-mini"):
	lib = []
	for f in sorted((HERE / "out_stage2" / "issues").glob(f"case_*_issues_{model}.json")):
		d = json.loads(f.read_text(encoding="utf-8"))
		for i in d["result"]["issues"]:
			lib.append({"case_id": d["case_id"], "issue": i["issue"], "result": i["result"], "text": i["issue"] + " " + i["applicant_position"]})
	return lib

class Index:
	def __init__(self, lib):
		self.lib = lib
		df = Counter()
		self.tf = []
		for x in lib:
			c = Counter(toks(x["text"]))
			self.tf.append(c)
			df.update(c.keys())
		n = len(lib)
		self.idf = {w: math.log((n + 1) / (v + 1)) + 1 for w, v in df.items()}
		self.vec = [self._v(c) for c in self.tf]

	def _v(self, c):
		v = {w: t * self.idf.get(w, 1.0) for w, t in c.items()}
		nm = math.sqrt(sum(x * x for x in v.values())) or 1.0
		return {w: x / nm for w, x in v.items()}

	def top(self, text, k=3):
		q = self._v(Counter(toks(text)))
		sc = [(sum(x * v.get(w, 0) for w, x in q.items()), i) for i, v in enumerate(self.vec)]
		sc.sort(reverse=True)
		return [(round(s, 3), self.lib[i]) for s, i in sc[:k]]

def main() -> int:
	ap = argparse.ArgumentParser()
	ap.add_argument("--arm", default="F41")
	ap.add_argument("--k", type=int, default=3)
	a = ap.parse_args()
	idx = Index(library())
	hit = n = 0
	for f in sorted(glob.glob(str(HERE / "out_drafts" / a.arm / "C*_*.json"))):
		d = json.loads(Path(f).read_text(encoding="utf-8"))
		cid = int(d["draft_id"][1:])
		for arg in d["result"]["arguments"]:
			n += 1
			if any(x["case_id"] == cid for _, x in idx.top(arg["issue"] + " " + arg["claim"], a.k)):
				hit += 1
	print(json.dumps({"arm": a.arm, "k": a.k, "library_issues": len(idx.lib), "arguments": n, "own_case_in_top_k": hit, "rate": round(hit / n, 3)}))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
