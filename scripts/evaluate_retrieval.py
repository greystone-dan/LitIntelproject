from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from statistics import mean
from typing import Any

import httpx


@dataclass
class EvalResult:
    topic: str
    query: str
    expected_citations: list[str]
    hit: bool
    reciprocal_rank: float
    matched_citation: str | None
    top_citations: list[str]


@dataclass
class EvalSummary:
    fixtures: int
    hits: int
    hit_rate: float
    mrr: float
    by_topic: dict[str, dict[str, float | int]]


def _normalize(text: str | None) -> str:
    return (text or "").strip().lower()


def _load_fixtures(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("Fixture file must contain a top-level JSON array")
    return payload


def _select_fixtures(fixtures: list[dict], limit: int | None) -> list[dict]:
    if limit is None:
        return fixtures
    if limit <= 0:
        raise ValueError("--limit must be greater than zero")
    return fixtures[:limit]


def _run_one(
    client: httpx.Client,
    base_url: str,
    fixture: dict,
    page_size: int,
    search_mode: str,
    semantic_weight: float,
    lexical_weight: float,
    candidate_pool: int,
) -> EvalResult:
    topic = str(fixture.get("topic", "unclassified"))
    query = fixture.get("query", "")
    expected = [c for c in fixture.get("expected_citations", []) if isinstance(c, str)]
    if not query or not expected:
        raise ValueError("Each fixture requires non-empty query and expected_citations")

    request_payload = {
        "query": query,
        "search_mode": fixture.get("search_mode", search_mode),
        "semantic_weight": float(fixture.get("semantic_weight", semantic_weight)),
        "lexical_weight": float(fixture.get("lexical_weight", lexical_weight)),
        "candidate_pool": int(fixture.get("candidate_pool", candidate_pool)),
        "page": 1,
        "page_size": int(fixture.get("page_size", page_size)),
        "source_type": fixture.get("source_type", "a2aj_curated"),
        "max_chunks_per_case": int(fixture.get("max_chunks_per_case", 2)),
    }

    response = client.post(f"{base_url}/search/chunks/grouped", json=request_payload, timeout=60)
    response.raise_for_status()
    body = response.json()

    expected_norm = {_normalize(x): x for x in expected}
    ranked = body.get("cases", []) if isinstance(body, dict) else []
    top_citations = [(item.get("citation") or "") for item in ranked]

    hit = False
    reciprocal_rank = 0.0
    matched = None
    for index, citation in enumerate(top_citations, start=1):
        norm = _normalize(citation)
        if norm in expected_norm:
            hit = True
            reciprocal_rank = 1.0 / index
            matched = expected_norm[norm]
            break

    return EvalResult(
        topic=topic,
        query=query,
        expected_citations=expected,
        hit=hit,
        reciprocal_rank=reciprocal_rank,
        matched_citation=matched,
        top_citations=top_citations,
    )


def _summarize(results: list[EvalResult]) -> EvalSummary:
    hits = sum(1 for r in results if r.hit)
    hit_rate = (hits / len(results)) if results else 0.0
    mrr = mean(r.reciprocal_rank for r in results) if results else 0.0

    by_topic: dict[str, dict[str, float | int]] = {}
    for result in results:
        topic_stats = by_topic.setdefault(
            result.topic,
            {
                "fixtures": 0,
                "hits": 0,
                "hit_rate": 0.0,
                "mrr": 0.0,
                "reciprocal_rank_sum": 0.0,
            },
        )
        topic_stats["fixtures"] = int(topic_stats["fixtures"]) + 1
        topic_stats["hits"] = int(topic_stats["hits"]) + (1 if result.hit else 0)
        topic_stats["reciprocal_rank_sum"] = float(topic_stats["reciprocal_rank_sum"]) + result.reciprocal_rank

    for topic, topic_stats in by_topic.items():
        fixtures = int(topic_stats["fixtures"])
        hits_topic = int(topic_stats["hits"])
        rr_sum = float(topic_stats["reciprocal_rank_sum"])
        topic_stats["hit_rate"] = (hits_topic / fixtures) if fixtures else 0.0
        topic_stats["mrr"] = (rr_sum / fixtures) if fixtures else 0.0
        del topic_stats["reciprocal_rank_sum"]

    return EvalSummary(
        fixtures=len(results),
        hits=hits,
        hit_rate=hit_rate,
        mrr=mrr,
        by_topic=by_topic,
    )


def _check_gates(
    summary: EvalSummary,
    min_hit_rate: float,
    min_mrr: float,
    min_topic_hit_rate: float,
    min_topic_fixtures: int,
) -> tuple[bool, list[str]]:
    failures: list[str] = []
    if summary.hit_rate < min_hit_rate:
        failures.append(f"overall hit rate {summary.hit_rate:.2%} < required {min_hit_rate:.2%}")
    if summary.mrr < min_mrr:
        failures.append(f"overall MRR {summary.mrr:.4f} < required {min_mrr:.4f}")

    for topic, stats in summary.by_topic.items():
        fixtures = int(stats["fixtures"])
        hit_rate = float(stats["hit_rate"])
        if fixtures >= min_topic_fixtures and hit_rate < min_topic_hit_rate:
            failures.append(
                f"topic '{topic}' hit rate {hit_rate:.2%} < required {min_topic_hit_rate:.2%}"
            )

    return (len(failures) == 0), failures


def _write_report(report_path: Path, summary: EvalSummary, results: list[EvalResult]) -> None:
    payload: dict[str, Any] = {
        "summary": {
            "fixtures": summary.fixtures,
            "hits": summary.hits,
            "hit_rate": summary.hit_rate,
            "mrr": summary.mrr,
            "by_topic": summary.by_topic,
        },
        "results": [
            {
                "topic": item.topic,
                "query": item.query,
                "expected_citations": item.expected_citations,
                "hit": item.hit,
                "reciprocal_rank": item.reciprocal_rank,
                "matched_citation": item.matched_citation,
                "top_citations": item.top_citations,
            }
            for item in results
        ],
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate grouped retrieval against citation fixtures")
    parser.add_argument(
        "fixture_file",
        type=Path,
        nargs="?",
        default=Path("data/eval/research_questions.sample.json"),
        help="Path to JSON fixture file",
    )
    parser.add_argument("--base-url", default="http://127.0.0.1:8000", help="Backend base URL")
    parser.add_argument("--page-size", type=int, default=10, help="Default retrieval page size")
    parser.add_argument(
        "--search-mode",
        choices=["semantic", "lexical", "hybrid"],
        default="semantic",
        help="Search mode for grouped retrieval benchmark",
    )
    parser.add_argument("--semantic-weight", type=float, default=0.7, help="Hybrid semantic weight")
    parser.add_argument("--lexical-weight", type=float, default=0.3, help="Hybrid lexical weight")
    parser.add_argument("--candidate-pool", type=int, default=100, help="Grouped retrieval candidate pool")
    parser.add_argument("--min-hit-rate", type=float, default=0.0, help="Fail if overall hit rate is below this")
    parser.add_argument("--min-mrr", type=float, default=0.0, help="Fail if overall MRR is below this")
    parser.add_argument(
        "--min-topic-hit-rate",
        type=float,
        default=0.0,
        help="Fail if topic hit rate is below this for topics with enough fixtures",
    )
    parser.add_argument(
        "--min-topic-fixtures",
        type=int,
        default=3,
        help="Minimum fixtures in a topic before topic gate is applied",
    )
    parser.add_argument(
        "--report-json",
        type=Path,
        default=None,
        help="Optional path to write machine-readable JSON report",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional max number of fixtures to evaluate from the top of the file",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print per-query result details",
    )
    args = parser.parse_args()

    fixtures = _select_fixtures(_load_fixtures(args.fixture_file), args.limit)
    if not fixtures:
        raise ValueError("Fixture file is empty")

    results: list[EvalResult] = []
    with httpx.Client() as client:
        for fixture in fixtures:
            results.append(
                _run_one(
                    client,
                    args.base_url.rstrip("/"),
                    fixture,
                    args.page_size,
                    args.search_mode,
                    args.semantic_weight,
                    args.lexical_weight,
                    args.candidate_pool,
                )
            )

    summary = _summarize(results)

    print("Retrieval evaluation complete")
    print(f"Fixtures: {summary.fixtures}")
    print(f"Hit@k: {summary.hit_rate:.2%} ({summary.hits}/{summary.fixtures})")
    print(f"MRR: {summary.mrr:.4f}")
    print()
    print("By topic:")
    for topic, stats in sorted(summary.by_topic.items()):
        print(
            f"  - {topic}: fixtures={int(stats['fixtures'])}, "
            f"hit_rate={float(stats['hit_rate']):.2%}, mrr={float(stats['mrr']):.4f}"
        )
    print()

    if args.verbose:
        for idx, result in enumerate(results, start=1):
            status = "HIT" if result.hit else "MISS"
            print(f"[{idx}] {status} | query={result.query}")
            if result.matched_citation:
                print(f"     matched: {result.matched_citation}")
            preview = ", ".join(c for c in result.top_citations[:5] if c) or "(no citations returned)"
            print(f"     top citations: {preview}")

    passed, failures = _check_gates(
        summary,
        min_hit_rate=args.min_hit_rate,
        min_mrr=args.min_mrr,
        min_topic_hit_rate=args.min_topic_hit_rate,
        min_topic_fixtures=args.min_topic_fixtures,
    )

    if args.report_json:
        _write_report(args.report_json, summary, results)
        print()
        print(f"Wrote JSON report: {args.report_json}")

    if passed:
        print()
        print("Quality gates: PASS")
        return

    print()
    print("Quality gates: FAIL")
    for failure in failures:
        print(f"  - {failure}")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
