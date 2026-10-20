"""Merge the full-text and notes argument lists for each decision with the vote rule and the side-label rule (files only).

Reads a JSON list ``{"id", "full_text": [{"side", "text", "para"}], "notes": [{"side", "text", "paras"}], "repeat_runs": [[...], [...]]}``
(``repeat_runs`` are extra independent full-text reads) and writes the same list with a ``merged`` list per decision. Needs the
``sentence-transformers`` package for the similarity (BAAI/bge-base-en-v1.5, runs on CPU). Nothing is sent anywhere and the
database is not touched. Off unless ILIT_ARGUMENT_CHECKER is set.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from backend.argument_checker import enabled, merge_by_votes  # noqa: E402


def _similarity(model_name: str):
	from sentence_transformers import SentenceTransformer  # noqa: PLC0415 - optional dependency

	model = SentenceTransformer(model_name, device="cpu")
	cache: dict[str, object] = {}

	def vector(text: str):
		if text not in cache:
			cache[text] = model.encode(text, normalize_embeddings=True)
		return cache[text]

	return lambda a, b: float(vector(a) @ vector(b))


def main() -> int:
	p = argparse.ArgumentParser(description=__doc__)
	p.add_argument("input")
	p.add_argument("output")
	p.add_argument("--model", default="BAAI/bge-base-en-v1.5")
	p.add_argument("--threshold", type=float, default=0.8)
	p.add_argument("--min-votes", type=int, default=1)
	args = p.parse_args()
	if not enabled():
		print("ILIT_ARGUMENT_CHECKER is not set; nothing done.")
		return 0
	similarity = _similarity(args.model)
	data = json.loads(Path(args.input).read_text(encoding="utf-8"))
	kept = 0
	for d in data:
		d["merged"] = merge_by_votes(d.get("full_text", []), d.get("notes", []), d.get("repeat_runs", []), similarity, args.threshold, args.min_votes)
		kept += len(d["merged"])
	Path(args.output).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
	print(f"{len(data)} decisions, {kept} arguments kept -> {args.output}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
