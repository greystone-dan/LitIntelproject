"""Compare two model-evaluation runs using paired bootstrap confidence intervals."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from statistics import mean
from typing import Any

METRICS_BY_MODE = {
    "retrieval": ("recall_at_k", "mrr", "ndcg_at_10"),
    "json_task": (
        "json_valid",
        "field_agreement",
        "cohen_kappa",
        "exact_span_validity",
    ),
}


def _canonical_label(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _kappa(rows: list[dict[str, Any]]) -> float:
    pairs = [
        (
            _canonical_label(value),
            _canonical_label(row["predicted_labels"].get(field, '"__missing__"')),
        )
        for row in rows
        for field, value in row["reference_labels"].items()
    ]
    if not pairs:
        return 0.0
    expected_values, predicted_values = zip(*pairs)
    observed = sum(a == b for a, b in pairs) / len(pairs)
    categories = set(expected_values) | set(predicted_values)
    expected = sum(
        expected_values.count(category) * predicted_values.count(category)
        for category in categories
    ) / (len(pairs) ** 2)
    if expected == 1:
        return 1.0 if observed == 1 else 0.0
    return (observed - expected) / (1 - expected)


def _score(rows: list[dict[str, Any]], mode: str, metric: str) -> float:
    if metric == "cohen_kappa":
        return _kappa(rows)
    return mean(float(row["metrics"][metric]) for row in rows)


def _percentile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower
    return ordered[lower] * (1 - fraction) + ordered[upper] * fraction


def compare_runs(
    baseline: dict[str, Any],
    candidate: dict[str, Any],
    metric: str,
    *,
    samples: int = 10_000,
    seed: int = 42,
    confidence: float = 0.95,
) -> dict[str, Any]:
    mode = baseline.get("mode")
    if mode not in METRICS_BY_MODE or candidate.get("mode") != mode:
        raise ValueError("Evaluation runs must use the same supported mode")
    if metric not in METRICS_BY_MODE[mode]:
        raise ValueError(f"Metric {metric!r} is not available for {mode}")
    if baseline.get("dataset") != candidate.get("dataset"):
        raise ValueError("Evaluation runs must use the same dataset name and version")
    baseline_rows = baseline.get("items")
    candidate_rows = candidate.get("items")
    if not isinstance(baseline_rows, list) or not isinstance(candidate_rows, list):
        raise TypeError("Evaluation runs must contain item arrays")
    baseline_by_id = {row["id"]: row for row in baseline_rows}
    candidate_by_id = {row["id"]: row for row in candidate_rows}
    if len(baseline_by_id) != len(baseline_rows) or len(candidate_by_id) != len(
        candidate_rows
    ):
        raise ValueError("Evaluation run item ids must be unique")
    if not baseline_by_id or baseline_by_id.keys() != candidate_by_id.keys():
        raise ValueError("Evaluation runs must contain the same non-empty item ids")
    ids = sorted(baseline_by_id)
    paired_baseline = [baseline_by_id[item_id] for item_id in ids]
    paired_candidate = [candidate_by_id[item_id] for item_id in ids]
    if baseline.get("parameters") != candidate.get("parameters"):
        raise ValueError("Evaluation runs must use the same parameters")
    reference_key = "relevant_chunk_ids" if mode == "retrieval" else "reference_labels"
    if any(
        left.get(reference_key) != right.get(reference_key)
        for left, right in zip(paired_baseline, paired_candidate)
    ):
        raise ValueError("Evaluation runs must use the same reference labels")
    if samples <= 0 or not 0 < confidence < 1:
        raise ValueError(
            "samples must be positive and confidence must be between 0 and 1"
        )
    baseline_score = _score(paired_baseline, mode, metric)
    candidate_score = _score(paired_candidate, mode, metric)
    point_delta = candidate_score - baseline_score
    rng = random.Random(seed)
    deltas = []
    for _ in range(samples):
        indices = [rng.randrange(len(ids)) for _ in ids]
        deltas.append(
            _score([paired_candidate[index] for index in indices], mode, metric)
            - _score([paired_baseline[index] for index in indices], mode, metric)
        )
    tail = (1 - confidence) / 2
    return {
        "schema_version": "1.0",
        "mode": mode,
        "dataset": baseline["dataset"],
        "metric": metric,
        "baseline_model": baseline.get("model"),
        "candidate_model": candidate.get("model"),
        "item_count": len(ids),
        "difference": {
            "direction": "candidate_minus_baseline",
            "estimate": point_delta,
            "confidence_level": confidence,
            "confidence_interval": [
                _percentile(deltas, tail),
                _percentile(deltas, 1 - tail),
            ],
        },
        "bootstrap": {"samples": samples, "seed": seed},
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True, type=Path)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument(
        "--metric",
        required=True,
        choices=sorted(set(sum(METRICS_BY_MODE.values(), ()))),
    )
    parser.add_argument("--samples", type=int, default=10_000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--confidence", type=float, default=0.95)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    result = compare_runs(
        json.loads(args.baseline.read_text(encoding="utf-8")),
        json.loads(args.candidate.read_text(encoding="utf-8")),
        args.metric,
        samples=args.samples,
        seed=args.seed,
        confidence=args.confidence,
    )
    encoded = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
