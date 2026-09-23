from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
from typing import Any

from backend.contextual_authority.teacher_contract import load_teacher_examples
from scripts.run_treatment_teacher_batch import CONTEXT_FIELDS, _parse_context_field


ALLOWED_TREATMENTS = {"supportive", "distinguishing", "negative", "neutral", "absent", "ambiguous"}


def _normalise_phrase(phrase: str) -> str:
    return re.sub(r"\s+", " ", phrase.casefold()).strip()


def _load_results(paths: list[Path]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for path in paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        for batch in payload.get("results", []):
            results.extend(batch.get("labels", []))
    return results


def build_distillation(
    fixture_path: Path,
    result_paths: list[Path],
    *,
    min_confidence: float,
    min_count: int,
) -> dict[str, Any]:
    examples = {example.example_id: example for example in load_teacher_examples(str(fixture_path))}
    labels = _load_results(result_paths)
    valid: list[dict[str, Any]] = []
    rejected: Counter[str] = Counter()
    seen_labels: set[tuple[str, int]] = set()

    for label in labels:
        example_id = str(label.get("example_id") or "")
        example = examples.get(example_id)
        if example is None:
            rejected["unknown_example"] += 1
            continue
        try:
            ordinal = int(label["citation_ordinal"])
            citation = example.citations[ordinal]
            treatment = str(label["treatment"])
            phrase = str(label.get("phrase") or "")
            start = int(label["phrase_start"])
            end = int(label["phrase_end"])
            confidence = float(label["confidence"])
            if treatment not in ALLOWED_TREATMENTS:
                raise ValueError("unsupported_treatment")
            if example.text[start:end] != phrase:
                raise ValueError("phrase_span_mismatch")
            if treatment == "absent" and (phrase or start != 0 or end != 0):
                raise ValueError("absent_span_not_empty")
            if treatment != "absent" and not phrase.strip():
                raise ValueError("empty_treatment_phrase")
            treatment_context = {
                field_name: _parse_context_field(
                    label.get("treatment_context", {}).get(
                        field_name,
                        {"status": "not_stated", "text": "", "start": 0, "end": 0},
                    ),
                    example.text,
                    field_name,
                )
                for field_name in CONTEXT_FIELDS
            }
            key = (example_id, ordinal)
            if key in seen_labels:
                rejected["duplicate_label"] += 1
                continue
            seen_labels.add(key)
            valid.append(
                {
                    "example_id": example_id,
                    "citation_ordinal": ordinal,
                    "citation_text": citation.citation_text,
                    "treatment": treatment,
                    "phrase": phrase,
                    "phrase_start": start,
                    "phrase_end": end,
                    "confidence": confidence,
                    "offsets_repaired": bool(label.get("offsets_repaired")),
                    "source_text_sha256": example.source_text_sha256,
                    "evidence_text": example.text[start:end],
                    "treatment_context": treatment_context,
                }
            )
        except (KeyError, IndexError, TypeError, ValueError) as exc:
            rejected[str(exc)] += 1

    eligible = [label for label in valid if label["confidence"] >= min_confidence]
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for label in eligible:
        phrase_key = _normalise_phrase(label["phrase"])
        if label["treatment"] == "absent":
            continue
        grouped[(label["treatment"], phrase_key)].append(label)

    rules = []
    for (treatment, phrase), evidence in sorted(grouped.items()):
        if len(evidence) < min_count:
            continue
        rules.append(
            {
                "rule_id": f"teacher-phrase-{treatment}-{len(rules) + 1:04d}",
                "treatment": treatment,
                "phrase": phrase,
                "support_count": len(evidence),
                "mean_confidence": sum(item["confidence"] for item in evidence) / len(evidence),
                "evidence": evidence,
                "status": "proposed_review_required",
            }
        )

    return {
        "artifact": "treatment_distillation_candidate",
        "status": "proposed_review_required",
        "runtime_publishable": False,
        "fixture": str(fixture_path),
        "teacher_result_files": [str(path) for path in result_paths],
        "policy": {
            "min_confidence": min_confidence,
            "min_support_count": min_count,
            "source_spans_revalidated": True,
            "canonical_database_writes": False,
            "external_ai_required_at_runtime": False,
        },
        "summary": {
            "raw_labels": len(labels),
            "valid_labels": len(valid),
            "eligible_labels": len(eligible),
            "proposed_rule_count": len(rules),
            "treatment_counts": dict(Counter(label["treatment"] for label in eligible)),
            "rejected_counts": dict(rejected),
        },
        "rules": rules,
        "eligible_labels": eligible,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a read-only provisional treatment distillation report.")
    parser.add_argument("--fixture", required=True, type=Path)
    parser.add_argument("--result", required=True, type=Path, action="append")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--min-confidence", type=float, default=0.85)
    parser.add_argument("--min-count", type=int, default=2)
    args = parser.parse_args()
    if not 0 <= args.min_confidence <= 1:
        parser.error("--min-confidence must be between 0 and 1")
    if args.min_count < 1:
        parser.error("--min-count must be positive")
    report = build_distillation(
        args.fixture,
        args.result,
        min_confidence=args.min_confidence,
        min_count=args.min_count,
    )
    args.output.write_text(json.dumps(report, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())