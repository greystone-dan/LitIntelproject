"""Fetch decision texts for the position-rule scorer from the public pages of the live site.

Read-only: one GET per decision on the public ``/cases/<id>`` page, no database and no login. Writes
``<out>/<id>.json`` with title, court, citation and full_text, the folder ``scripts/eval_position_rules.py --texts`` reads.

    python scripts/fetch_position_texts.py --gold data/eval/position_gold_reader.json --gold data/eval/position_gold_ai.json --out position_texts
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = "https://www.ilit.ca/cases/"


def fetch(case_id: str, out: str) -> str:
	path = os.path.join(out, f"{case_id}.json")
	if os.path.exists(path):
		return "cached"
	try:
		with urllib.request.urlopen(BASE + case_id, timeout=60) as resp:
			data = json.load(resp)
	except Exception as exc:  # network or JSON problem: report and go on
		return f"failed: {exc}"
	keep = {k: data.get(k) for k in ("id", "title", "court", "citation", "full_text")}
	with open(path, "w", encoding="utf-8") as fh:
		json.dump(keep, fh, ensure_ascii=False)
	return "ok"


def main() -> None:
	ap = argparse.ArgumentParser(description=__doc__)
	ap.add_argument("--gold", action="append", required=True)
	ap.add_argument("--out", required=True)
	args = ap.parse_args()
	os.makedirs(args.out, exist_ok=True)
	ids: set[str] = set()
	for g in args.gold:
		ids.update(json.load(open(g, encoding="utf-8")))
	with ThreadPoolExecutor(6) as pool:
		results = list(pool.map(lambda i: (i, fetch(i, args.out)), sorted(ids)))
	bad = [(i, r) for i, r in results if r.startswith("failed")]
	print(f"{len(results) - len(bad)} of {len(results)} decisions available in {args.out}")
	for i, r in bad:
		print(i, r)


if __name__ == "__main__":
	main()
