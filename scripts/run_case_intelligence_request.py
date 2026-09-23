from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
from typing import Any

from openai import OpenAI


HARD_CAP_USD = 3.0


def estimate_tokens(messages: list[dict[str, str]]) -> int:
    return max(1, sum(len(message.get("content", "")) for message in messages) // 4)


def estimate_cost(messages: list[dict[str, str]], max_output_tokens: int, input_rate: float, output_rate: float) -> float:
    return estimate_tokens(messages) / 1_000_000 * input_rate + max_output_tokens / 1_000_000 * output_rate


def run_request(
    request: dict[str, Any],
    *,
    client: Any,
    output_path: Path,
    max_output_tokens: int,
    input_rate: float,
    output_rate: float,
) -> dict[str, Any]:
    messages = request["messages"]
    estimated_cost = estimate_cost(messages, max_output_tokens, input_rate, output_rate)
    if estimated_cost > float(request["budget_usd"]):
        raise ValueError(f"estimated cost ${estimated_cost:.4f} exceeds budget ${request['budget_usd']:.2f}")
    completion = client.chat.completions.create(
        model=request["model"],
        temperature=0,
        max_tokens=max_output_tokens,
        response_format={"type": "json_object"},
        messages=messages,
    )
    content = completion.choices[0].message.content or ""
    usage = completion.usage
    input_tokens = int(getattr(usage, "prompt_tokens", 0) or 0)
    output_tokens = int(getattr(usage, "completion_tokens", 0) or 0)
    actual_cost = (
        input_tokens / 1_000_000 * input_rate + output_tokens / 1_000_000 * output_rate
        if input_tokens
        else estimated_cost
    )
    result = {
        "status": "case_intelligence_run_complete",
        "network_called": True,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "request_id": request.get("request_id"),
        "model": request["model"],
        "budget_usd": request["budget_usd"],
        "estimated_cost_usd": estimated_cost,
        "spent_usd": actual_cost,
        "usage": {"prompt_tokens": input_tokens, "completion_tokens": output_tokens},
        "raw_response": content,
    }
    try:
        result["parsed_response"] = json.loads(content)
    except json.JSONDecodeError as exc:
        result["parsed_response_error"] = str(exc)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    return {
        "status": result["status"],
        "model": result["model"],
        "prompt_tokens": input_tokens,
        "completion_tokens": output_tokens,
        "spent_usd": actual_cost,
        "parsed": "parsed_response" in result,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one bounded case-level intelligence request.")
    parser.add_argument("--request", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-output-tokens", type=int, default=8_000)
    parser.add_argument("--input-cost-per-1m", type=float, default=2.0)
    parser.add_argument("--output-cost-per-1m", type=float, default=8.0)
    args = parser.parse_args()
    if args.max_output_tokens < 1:
        parser.error("--max-output-tokens must be positive")
    request = json.loads(args.request.read_text(encoding="utf-8"))
    if request.get("status") != "dry_run_ready" or request.get("network_called"):
        raise SystemExit("request must be a dry_run_ready, network-free payload")
    if float(request.get("budget_usd", 0)) <= 0 or float(request["budget_usd"]) > HARD_CAP_USD:
        raise SystemExit(f"request budget must be between 0 and {HARD_CAP_USD}")
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is required for the paid case-intelligence run")
    print(json.dumps(run_request(
        request,
        client=OpenAI(),
        output_path=args.output,
        max_output_tokens=args.max_output_tokens,
        input_rate=args.input_cost_per_1m,
        output_rate=args.output_cost_per_1m,
    ), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())