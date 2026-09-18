from __future__ import annotations

import argparse
import json

from backend.contextual_authority.teacher_contract import (
    DEFAULT_MODEL,
    TeacherBatch,
    build_teacher_messages,
    estimate_cost_usd,
    load_teacher_examples,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare a no-network treatment-label request.")
    parser.add_argument("--fixture", required=True, help="Input citation-context JSONL")
    parser.add_argument("--output", required=True, help="Output request JSON")
    parser.add_argument("--request-id", required=True)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--budget-usd", type=float, default=10.0)
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--offset", type=int, default=0, help="Number of fixture examples to skip before selecting the batch.")
    args = parser.parse_args()
    if not 1 <= args.limit <= 2_500:
        parser.error("--limit must be between 1 and 2500")
    if args.offset < 0:
        parser.error("--offset must be non-negative")
    examples = load_teacher_examples(args.fixture)[args.offset : args.offset + args.limit]
    if not examples:
        parser.error("--offset selects no examples")
    batch = TeacherBatch(args.request_id, args.model, args.budget_usd, examples)
    messages = build_teacher_messages(batch)
    estimated_cost = estimate_cost_usd(messages)
    if estimated_cost > batch.budget_usd:
        raise SystemExit(
            f"estimated cost ${estimated_cost:.4f} exceeds budget ${batch.budget_usd:.2f}"
        )
    payload = {
        "status": "dry_run_ready",
        "network_called": False,
        "request_id": batch.request_id,
        "model": batch.model,
        "example_count": len(batch.examples),
        "budget_usd": batch.budget_usd,
        "estimated_cost_usd": round(estimated_cost, 6),
        "messages": messages,
    }
    with open(args.output, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=True, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps({key: payload[key] for key in payload if key != "messages"}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
