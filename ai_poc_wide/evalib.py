"""Shared helpers for checking the wide run offline: load arm outputs, quote verification, point matching, derived layers."""
from __future__ import annotations

import difflib
import json
import re
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
LAYER_NAMES = {1: "court's own", 2: "party submission", 3: "earlier decision-maker", 4: "first-instance position", 5: "document or testimony", 6: "law / precedent commentary"}


def load_inputs(root: Path = HERE / "inputs") -> dict[int, dict]:
	return {int(p.stem.split("_")[1]): json.loads(p.read_text(encoding="utf-8")) for p in root.glob("case_*.json")}


def load_arm(folder: Path) -> dict[int, dict]:
	out = {}
	for p in sorted(folder.glob("case_*.json")):
		d = json.loads(p.read_text(encoding="utf-8"))
		out[int(d["case_id"])] = d
	return out


def points(arm: dict[int, dict]):
	"""Yield (case_id, para, index_in_para(1-based), point_dict)."""
	for cid, d in arm.items():
		for r in d["paragraphs"]:
			for i, pr in enumerate(r["propositions"], 1):
				yield cid, r["para"], i, pr


def norm(s: str) -> str:
	s = unicodedata.normalize("NFKC", s or "")
	s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-").replace(" ", " ")
	return re.sub(r"\s+", " ", s).strip().casefold()


def quote_status(quote: str, para_text: str, other_paras: dict[int, str] | None = None, own: int | None = None) -> str:
	"""exact | parts (split on an ellipsis, every part found) | near (>=90% of the quote is one contiguous match) | elsewhere (found verbatim in another paragraph) | unsupported | empty"""
	nq, npara = norm(quote), norm(para_text)
	if len(nq) < 8:
		return "empty"
	if nq in npara:
		return "exact"
	parts = [p.strip(" .") for p in re.split(r"\.\.\.|…|\[\.\.\.\]", nq) if len(p.strip(" .")) >= 8]
	if len(parts) > 1 and all(p in npara for p in parts):
		return "parts"
	m = difflib.SequenceMatcher(None, nq, npara, autojunk=False).find_longest_match(0, len(nq), 0, len(npara))
	if m.size >= 0.9 * len(nq):
		return "near"
	if other_paras:
		for k, t in other_paras.items():
			if k != own and nq in norm(t):
				return "elsewhere"
	return "unsupported"


def toks(s: str) -> set[str]:
	return set(re.findall(r"[a-z0-9À-ſ]{3,}", norm(s)))


def jaccard(a: str, b: str) -> float:
	x, y = toks(a), toks(b)
	return len(x & y) / len(x | y) if x and y else 0.0


def derive_layer(holder: str, kind: str) -> int:
	"""How the first review sheet turned a stored holder (and kind) into a level; v4 has no layer of its own."""
	if kind == "rule_of_law" and holder in ("court", "prior_court_or_authority", "earlier_decision_maker"):
		return 6
	return {"court": 1, "applicant": 2, "respondent": 2, "earlier_decision_maker": 3, "witness_or_document": 5, "prior_court_or_authority": 5, "other": 1}[holder]


OK_PAIRS = {1: {"court"}, 2: {"applicant", "respondent", "other"}, 3: {"earlier_decision_maker"}, 4: {"applicant", "respondent", "witness_or_document", "earlier_decision_maker", "other"},
	5: {"witness_or_document", "prior_court_or_authority", "other"}, 6: {"court", "prior_court_or_authority", "earlier_decision_maker", "other"}}


def match_points(a_pts: list[dict], b_pts: list[dict], key=lambda p: p.get("quote") or p["text"], thr: float = 0.5) -> list[tuple[int, int, float]]:
	"""Greedy one-to-one matching of two point lists from the same paragraph by word overlap of key(); returns (i, j, score)."""
	cand = sorted(((jaccard(key(x), key(y)), i, j) for i, x in enumerate(a_pts) for j, y in enumerate(b_pts)), reverse=True)
	used_a, used_b, out = set(), set(), []
	for s, i, j in cand:
		if s < thr:
			break
		if i in used_a or j in used_b:
			continue
		used_a.add(i)
		used_b.add(j)
		out.append((i, j, s))
	return out


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
	if n == 0:
		return (0.0, 0.0)
	p = k / n
	d = 1 + z * z / n
	c = p + z * z / (2 * n)
	h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)
	return ((c - h) / d, (c + h) / d)


def pct(k: int, n: int) -> str:
	if n == 0:
		return "n/a"
	lo, hi = wilson(k, n)
	return f"{100 * k / n:.0f}% ({k}/{n}; 95% range {100 * lo:.0f}-{100 * hi:.0f}%)"
