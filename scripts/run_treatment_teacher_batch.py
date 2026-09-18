from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
from typing import Any

from openai import OpenAI

from backend.contextual_authority.teacher_contract import estimate_tokens


ALLOWED_TREATMENTS = {"supportive", "distinguishing", "negative", "neutral", "absent", "ambiguous"}
HARD_CAP_USD = 3.0


def estimate_batch_cost(messages: list[dict[str, str]], output_tokens: int, input_rate: float, output_rate: float) -> float:
    input_tokens = estimate_tokens(messages)
    return (input_tokens / 1_000_000 * input_rate) + (output_tokens / 1_000_000 * output_rate)


def parse_teacher_response(content: str, examples: list[dict[str, Any]]) -> dict[str, Any]:
    text = content.strip()
    if text.startswith("```"):
        text = text.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    if not text.startswith("{"):
        start = text.find("{")
        end = text.rfind("}")
        if start < 0 or end <= start:
            raise ValueError("teacher response contains no JSON object")
        text = text[start : end + 1]
    payload = json.loads(text)
    if not isinstance(payload, dict) or not isinstance(payload.get("labels"), list):
        raise ValueError("teacher response must be an object with a labels array")

    example_map = {str(example["example_id"]): example for example in examples}
    valid_labels: list[dict[str, Any]] = []
    errors: list[str] = []
    for index, label in enumerate(payload["labels"]):
        if not isinstance(label, dict):
            errors.append(f"label {index}: not an object")
            continue
        example_id = str(label.get("example_id") or "")
        example = example_map.get(example_id)
        if example is None:
            errors.append(f"label {index}: unknown example_id")
            continue
        try:
            ordinal = int(label["citation_ordinal"])
            citation = example["citations"][ordinal]
            label_key = (example_id, ordinal)
            if any(existing.get("example_id") == label_key[0] and existing.get("citation_ordinal") == label_key[1] for existing in valid_labels):
                raise ValueError("duplicate label for example citation")
            treatment = str(label["treatment"])
            phrase = str(label.get("phrase") or "")
            start = int(label["phrase_start"])
            end = int(label["phrase_end"])
            if treatment not in ALLOWED_TREATMENTS:
                raise ValueError("unsupported treatment")
            if start < 0 or end < start or end > len(example["text"]):
                raise ValueError("phrase offsets out of bounds")
            offsets_repaired = False
            if example["text"][start:end] != phrase:
                occurrences: list[int] = []
                search_start = 0
                while phrase:
                    match_start = example["text"].find(phrase, search_start)
                    if match_start < 0:
                        break
                    occurrences.append(match_start)
                    search_start = match_start + 1
                if len(occurrences) != 1:
                    raise ValueError("phrase offsets do not reconstruct phrase and phrase is not uniquely locatable")
                start = occurrences[0]
                end = start + len(phrase)
                offsets_repaired = True
            if treatment == "absent" and phrase:
                raise ValueError("absent treatment must use an empty phrase and zero offsets")
            if treatment != "absent" and not phrase.strip():
                raise ValueError("non-absent treatment requires a phrase")
            valid_labels.append(
                {
                    "example_id": example_id,
                    "citation_ordinal": ordinal,
                    "citation_text": citation["citation_text"],
                    "treatment": treatment,
                    "phrase": phrase,
                    "phrase_start": start,
                    "phrase_end": end,
                    "offsets_repaired": offsets_repaired,
                    "confidence": label.get("confidence"),
                    "rationale": label.get("rationale"),
                }
            )
        except (KeyError, IndexError, TypeError, ValueError) as exc:
            errors.append(f"label {index}: {exc}")
    return {"labels": valid_labels, "invalid_labels": errors}


def _cost_from_usage(usage: Any, estimated: float, input_rate: float, output_rate: float) -> tuple[int, int, float]:
    input_tokens = int(getattr(usage, "prompt_tokens", 0) or 0)
    output_tokens = int(getattr(usage, "completion_tokens", 0) or 0)
    if not input_tokens:
        return input_tokens, output_tokens, estimated
    cost = (input_tokens / 1_000_000 * input_rate) + (output_tokens / 1_000_000 * output_rate)
    return input_tokens, output_tokens, cost


def run_batches(
    request: dict[str, Any],
    *,
    client: Any,
    output_path: Path,
    batch_size: int,
    budget_usd: float,
    max_output_tokens: int,
    input_rate: float,
    output_rate: float,
) -> dict[str, Any]:
    if budget_usd <= 0 or budget_usd > HARD_CAP_USD:
        raise ValueError(f"budget_usd must be between 0 and {HARD_CAP_USD}")
    messages = request["messages"]
    payload = json.loads(messages[1]["content"])
    examples = payload["examples"]
    results: list[dict[str, Any]] = []
    spent = 0.0
    for batch_number, start in enumerate(range(0, len(examples), batch_size), 1):
        batch_examples = examples[start : start + batch_size]
        batch_payload = {**payload, "examples": batch_examples, "request_id": f"{payload['request_id']}-{batch_number:03d}"}
        batch_messages = [messages[0], {"role": "user", "content": json.dumps(batch_payload, ensure_ascii=True, sort_keys=True)}]
        estimated = estimate_batch_cost(batch_messages, max_output_tokens, input_rate, output_rate)
        if spent + estimated > budget_usd:
            break
        completion = client.chat.completions.create(
            model=request["model"],
            temperature=0,
            max_tokens=max_output_tokens,
            response_format={"type": "json_object"},
            messages=batch_messages,
        )
        content = completion.choices[0].message.content or "{}"
        input_tokens, output_tokens, cost = _cost_from_usage(completion.usage, estimated, input_rate, output_rate)
        spent += cost
        try:
            parsed = parse_teacher_response(content, batch_examples)
        except (TypeError, ValueError, json.JSONDecodeError) as exc:
            parsed = {"labels": [], "invalid_labels": [f"response: {exc}"]}
        results.append(
            {
                "batch_number": batch_number,
                "example_start": start,
                "example_count": len(batch_examples),
                "usage": {
                    "prompt_tokens": input_tokens,
                    "completion_tokens": output_tokens,
                    "estimated_cost_usd": estimated,
                    "cost_usd": cost,
                },
                "validation": {
                    "valid_label_count": len(parsed["labels"]),
                    "invalid_label_count": len(parsed["invalid_labels"]),
                    "invalid_labels": parsed["invalid_labels"],
                },
                "labels": parsed["labels"],
                "raw_response": content,
            }
        )
        output_path.write_text(
            json.dumps(
                {
                    "status": "teacher_run_complete",
                    "network_called": True,
                    "started_at": datetime.now(timezone.utc).isoformat(),
                    "model": request["model"],
                    "budget_usd": budget_usd,
                    "spent_usd": spent,
                    "results": results,
                },
                ensure_ascii=True,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    return {"batch_count": len(results), "example_count": sum(item["example_count"] for item in results), "spent_usd": spent}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run bounded treatment teacher batches with exact-span validation.")
    parser.add_argument("--request", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--budget-usd", type=float, default=3.0)
    parser.add_argument("--max-output-tokens", type=int, default=1_200)
    parser.add_argument("--input-cost-per-1m", type=float, default=0.10)
    parser.add_argument("--output-cost-per-1m", type=float, default=0.40)
    args = parser.parse_args()
    if not 1 <= args.batch_size <= 250:
        parser.error("--batch-size must be between 1 and 250")
    if args.max_output_tokens < 1:
        parser.error("--max-output-tokens must be positive")
    request = json.loads(args.request.read_text(encoding="utf-8"))
    if request.get("status") != "dry_run_ready" or request.get("network_called"):
        raise SystemExit("request must be a dry_run_ready, network-free payload")
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is required for the paid teacher run")
    summary = run_batches(
        request,
        client=OpenAI(),
        output_path=args.output,
        batch_size=args.batch_size,
        budget_usd=args.budget_usd,
        max_output_tokens=args.max_output_tokens,
        input_rate=args.input_cost_per_1m,
        output_rate=args.output_cost_per_1m,
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
