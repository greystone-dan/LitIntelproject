"""Score the case search box against a gold query set (read-only; run on the PC).

Modes: legacy (exact-phrase only, the behaviour before the sentence fix), words (most-of-the-words ILIKE),
paragraph (paragraph index; needs the paragraph_search table). Example:
    python scripts/score_search_gold.py --mode paragraph --out scores_paragraph.json
    python scripts/score_search_gold.py --compare scores_legacy.json scores_paragraph.json
Nothing is written to the database. Landmark and citation queries count a hit when an expected citation
is in the top 10; topic and French queries count a hit when a top-10 case text matches every oracle regex
(a weak, loose check), and the top 3 titles are printed so a person can read them.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

DEFAULT_QUERIES = ROOT / "scripts" / "search_gold_queries.json"


def norm(value: str | None) -> str:
	return re.sub(r"[^a-z0-9]+", "", (value or "").lower())


def first_hit_rank(results: list[dict], hit_flags: list[bool]) -> int | None:
	for index, flag in enumerate(hit_flags, 1):
		if flag:
			return index
	return None


def summarize(rows: list[dict]) -> dict:
	def block(subset: list[dict]) -> dict:
		if not subset:
			return {"queries": 0}
		ranks = [row["first_hit_rank"] for row in subset]
		return {
			"queries": len(subset),
			"success_at_10": round(sum(1 for rank in ranks if rank) / len(subset), 3),
			"success_at_3": round(sum(1 for rank in ranks if rank and rank <= 3) / len(subset), 3),
			"mrr": round(sum(1 / rank for rank in ranks if rank) / len(subset), 3),
			"zero_results": sum(1 for row in subset if row["results"] == 0),
			"p50_ms": round(statistics.median(row["ms"] for row in subset)),
			"p95_ms": round(sorted(row["ms"] for row in subset)[max(0, int(len(subset) * 0.95) - 1)]),
		}

	kinds = sorted({row["kind"] for row in rows})
	return {"all": block(rows), **{kind: block([row for row in rows if row["kind"] == kind]) for kind in kinds}}


def run(args: argparse.Namespace) -> None:
	if args.mode == "legacy":
		os.environ["ILIT_PARAGRAPH_SEARCH"] = "0"
	elif args.mode == "words":
		os.environ["ILIT_PARAGRAPH_SEARCH"] = "0"
	from sqlalchemy import text

	from backend import analytics_service
	from backend.database import SessionLocal

	if args.mode == "legacy":
		analytics_service.sentence_hits_sql = lambda *a, **k: ("", "", {})
	queries = json.loads(Path(args.queries).read_text(encoding="utf-8"))["queries"]
	rows = []
	with SessionLocal() as db:
		for item in queries:
			regexes = [re.compile(pattern, re.I) for pattern in item.get("oracle_all", [])]
			wanted = {norm(citation) for citation in item.get("expect_citations", [])}
			start = time.perf_counter()
			try:
				page = analytics_service.fetch_analytics_search_cases(
					db, query=item["query"], search_full_text=True, limit=10,
					include_facets=False, include_citation_stats=False,
				)
				results = page["results"]
			except Exception as error:  # a timeout on one query should not stop the run
				db.rollback()
				results, page = [], {"error": str(error)[:200]}
			ms = (time.perf_counter() - start) * 1000
			flags = []
			for result in results:
				hit = bool(wanted) and norm(result.get("citation")) in wanted
				if not hit and wanted:
					secondary = db.execute(
						text("SELECT secondary_citation FROM cases WHERE id = :id"), {"id": result["case_id"]}
					).scalar()
					hit = norm(secondary) in wanted
				if not hit and regexes:
					body = db.execute(text("SELECT full_text FROM cases WHERE id = :id"), {"id": result["case_id"]}).scalar() or ""
					hit = all(regex.search(body) for regex in regexes)
				flags.append(hit)
			rank = first_hit_rank(results, flags)
			rows.append({
				"id": item["id"], "query": item["query"], "kind": item["kind"], "results": len(results),
				"first_hit_rank": rank, "ms": round(ms), "error": page.get("error"),
				"top3": [f"{r.get('citation') or ''} {r.get('title') or ''}"[:90] for r in results[:3]],
			})
			print(f"{item['id']} {'HIT@%d' % rank if rank else 'miss ':7} {len(results):3} results {ms:6.0f} ms  {item['query'][:60]}")
	summary = summarize(rows)
	print(json.dumps(summary, indent=1))
	if args.out:
		Path(args.out).write_text(json.dumps({"mode": args.mode, "summary": summary, "rows": rows}, indent=1), encoding="utf-8")


def compare(paths: list[str]) -> None:
	runs = [json.loads(Path(path).read_text(encoding="utf-8")) for path in paths]
	print("kind | " + " | ".join(f"{run['mode']} (s@10 / MRR / zero)" for run in runs))
	for kind in runs[0]["summary"]:
		cells = []
		for run in runs:
			block = run["summary"].get(kind, {})
			cells.append(f"{block.get('success_at_10', '-')} / {block.get('mrr', '-')} / {block.get('zero_results', '-')}" if block.get("queries") else "-")
		print(f"{kind} | " + " | ".join(cells))


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--mode", choices=["legacy", "words", "paragraph"], default="paragraph")
	parser.add_argument("--queries", default=str(DEFAULT_QUERIES))
	parser.add_argument("--out")
	parser.add_argument("--compare", nargs="+", metavar="SCORES_JSON")
	args = parser.parse_args()
	compare(args.compare) if args.compare else run(args)


if __name__ == "__main__":
	main()
