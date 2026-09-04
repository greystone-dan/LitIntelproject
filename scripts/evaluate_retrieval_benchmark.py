"""Evaluate the Data Explorer case-search ranking against a fixed benchmark."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

DEFAULT_BENCHMARK = PROJECT_ROOT / "data" / "eval" / "retrieval_benchmark.json"


def ranking_metrics(ranked_ids: list[int], expected_ids: list[int], k: int) -> dict[str, float | int]:
    expected = set(expected_ids)
    top = ranked_ids[:k]
    ranks = [index + 1 for index, case_id in enumerate(ranked_ids) if case_id in expected]
    return {
        "hit_at_k": int(bool(ranks)),
        "reciprocal_rank": 1 / ranks[0] if ranks else 0.0,
        "precision_at_k": sum(case_id in expected for case_id in top) / k if k else 0.0,
        "recall_at_k": sum(case_id in expected for case_id in top) / len(expected) if expected else 1.0,
    }


def fetch_results(base_url: str, query: str, limit: int) -> list[int]:
    params = urlencode({"query": query, "limit": limit})
    request = Request(f"{base_url.rstrip('/')}/analytics/search/cases?{params}")
    with urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return [int(item["case_id"]) for item in payload.get("results", [])]


def evaluate_benchmark(cases: list[dict], base_url: str) -> dict:
    rows = []
    for case in cases:
        ranked_ids = fetch_results(base_url, case["query"], int(case.get("limit", 10)))
        metrics = ranking_metrics(ranked_ids, case["expected_case_ids"], int(case.get("limit", 10)))
        rows.append({"id": case["id"], "query": case["query"], "ranked_case_ids": ranked_ids, **metrics})
    count = len(rows)
    return {
        "benchmark_count": count,
        "mean_reciprocal_rank": sum(row["reciprocal_rank"] for row in rows) / count if count else 0.0,
        "mean_precision_at_k": sum(row["precision_at_k"] for row in rows) / count if count else 0.0,
        "mean_recall_at_k": sum(row["recall_at_k"] for row in rows) / count if count else 0.0,
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default="http://127.0.0.1:8000")
    parser.add_argument("--benchmark", type=Path, default=DEFAULT_BENCHMARK)
    parser.add_argument("--output-file", type=Path)
    args = parser.parse_args()
    report = evaluate_benchmark(json.loads(args.benchmark.read_text(encoding="utf-8")), args.base_url)
    if args.output_file:
        args.output_file.parent.mkdir(parents=True, exist_ok=True)
        args.output_file.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "rows"}, indent=2))
    for row in report["rows"]:
        print(json.dumps(row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
