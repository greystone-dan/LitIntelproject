"""Send all unknown FC Activity motions for bounded OpenAI subtype suggestions."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL = "gpt-4.1-nano"
INPUT_COST_PER_MILLION = 0.10
OUTPUT_COST_PER_MILLION = 0.40
SUBTYPES = (
    "stay_removal", "stay_deportation", "stay_release", "stay_admissibility_hearing",
    "stay_proceedings", "stay_execution", "abeyance", "s_37_cea", "s_87_irpa",
    "anonymity", "amendment_aljr", "extension_of_time", "consent_judgment",
    "confidentiality", "production", "intervention", "stay", "unknown",
)
USAGE_KEYS = ("prompt_tokens", "completion_tokens", "total_tokens")


def extract_unknown_motions(report: dict[str, Any]) -> list[dict[str, Any]]:
    motions: list[dict[str, Any]] = []
    for case in report.get("cases", []):
        for event in case.get("classification", {}).get("procedural_events", []):
            if not str(event.get("event_type", "")).startswith("motion") or event.get("subtype") != "unknown":
                continue
            motions.append({
                "activity_case_id": case.get("activity_case_id"),
                "doc_id": event.get("doc_id"),
                "event_type": event.get("event_type"),
                "outcome": event.get("outcome"),
                "source_document_date": event.get("source_document_date"),
                "evidence": str(event.get("text") or "")[:900],
            })
    return motions


def _key(item: dict[str, Any]) -> str:
    return f"{item.get('activity_case_id')}:{item.get('doc_id')}:{item.get('event_type')}"


def estimate_prompt_tokens(items: list[dict[str, Any]]) -> int:
    payload = json.dumps(items, ensure_ascii=True, separators=(",", ":"))
    return max(1, (len(payload) + 3) // 4) + 180


def estimate_batch_cost(items: list[dict[str, Any]]) -> float:
    prompt_tokens = estimate_prompt_tokens(items)
    completion_tokens = max(200, len(items) * 120)
    return (prompt_tokens * INPUT_COST_PER_MILLION + completion_tokens * OUTPUT_COST_PER_MILLION) / 1_000_000


def empty_usage() -> dict[str, int]:
    return {key: 0 for key in USAGE_KEYS}


def merge_usage(total: dict[str, int], increment: dict[str, int]) -> None:
    for key in USAGE_KEYS:
        total[key] = total.get(key, 0) + int(increment.get(key, 0) or 0)


def build_messages(items: list[dict[str, Any]]) -> list[dict[str, str]]:
    system = (
        "You are an advisory classifier for Canadian Federal Court procedural history. "
        "For each supplied unknown motion event, suggest exactly one subtype from "
        f"{list(SUBTYPES)} or unknown. Use only the supplied evidence; prioritize precision "
        "over coverage. Never infer a legal result. Return JSON with a suggestions array. "
        "Each suggestion must contain activity_case_id, doc_id, event_type, suggested_subtype, "
        "confidence (low, medium, or high), and short reasoning. Keep reasoning under 240 characters. "
        "These are review suggestions only and must not propose database writes or rule promotion."
    )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": json.dumps({"motions": items}, ensure_ascii=True)},
    ]


def parse_suggestions(raw_response: str, expected: list[dict[str, Any]]) -> list[dict[str, Any]]:
    parsed = json.loads(raw_response or "{}")
    suggestions = parsed.get("suggestions") if isinstance(parsed, dict) else None
    if not isinstance(suggestions, list):
        raise ValueError("response must be a JSON object with a suggestions array")
    allowed_keys = {_key(item) for item in expected}
    output: list[dict[str, Any]] = []
    for suggestion in suggestions:
        if not isinstance(suggestion, dict):
            continue
        key = _key(suggestion)
        subtype = suggestion.get("suggested_subtype", "unknown")
        if key not in allowed_keys or subtype not in SUBTYPES:
            continue
        output.append({
            "activity_case_id": suggestion.get("activity_case_id"),
            "doc_id": suggestion.get("doc_id"),
            "event_type": suggestion.get("event_type"),
            "suggested_subtype": subtype,
            "confidence": suggestion.get("confidence") if suggestion.get("confidence") in {"low", "medium", "high"} else "low",
            "reasoning": str(suggestion.get("reasoning") or "")[:240],
        })
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--budget-usd", type=float, default=5.0)
    parser.add_argument("--send", action="store_true")
    args = parser.parse_args()
    if args.batch_size < 1 or args.budget_usd <= 0 or args.budget_usd > 5:
        parser.error("batch size must be positive and budget must be greater than 0 and at most 5")

    motions = extract_unknown_motions(json.loads(args.input.read_text(encoding="utf-8")))
    checkpoint = json.loads(args.checkpoint.read_text(encoding="utf-8")) if args.checkpoint.exists() else {"completed_keys": [], "suggestions": [], "spent_usd": 0.0}
    completed = set(checkpoint.get("completed_keys", []))
    pending = [item for item in motions if _key(item) not in completed]
    batches = [pending[index:index + args.batch_size] for index in range(0, len(pending), args.batch_size)]
    projected_cost = sum(estimate_batch_cost(batch) for batch in batches)
    result: dict[str, Any] = {
        "audit_version": "fc_activity_motion_unknowns_openai_v1",
        "model": MODEL,
        "source_motion_count": len(motions),
        "pending_motion_count": len(pending),
        "batch_size": args.batch_size,
        "batch_count": len(batches),
        "budget_usd": args.budget_usd,
        "projected_cost_usd": projected_cost,
        "network_called": False,
        "database_written": False,
        "rules_promoted": False,
        "status": "prepared",
    }
    if projected_cost > args.budget_usd:
        result["status"] = "budget_exceeded"
    elif args.send and batches:
        load_dotenv(PROJECT_ROOT / ".env", override=False)
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise SystemExit("OPENAI_API_KEY is required for --send; no request was made")
        os.environ.pop("OPENAI_ORG_ID", None)
        os.environ.pop("OPENAI_ORGANIZATION", None)
        os.environ.pop("OPENAI_PROJECT_ID", None)
        client = OpenAI(api_key=api_key, timeout=120.0, max_retries=0)
        spent = float(checkpoint.get("spent_usd", 0.0))
        starting_spent = spent
        suggestions = list(checkpoint.get("suggestions", []))
        usage_total = {**empty_usage(), **checkpoint.get("usage_total", {})}
        run_history = list(checkpoint.get("run_history", []))
        pass_usage = empty_usage()
        pass_record = {
            "pass_index": len(run_history) + 1,
            "pending_motion_count": len(pending),
            "batch_count": len(batches),
            "status": "running",
            "spent_usd": 0.0,
            "usage": pass_usage,
        }
        run_history.append(pass_record)
        for batch in batches:
            response = client.chat.completions.create(
                model=MODEL, temperature=0, max_tokens=4000,
                response_format={"type": "json_object"}, messages=build_messages(batch),
            )
            usage = response.usage
            prompt_tokens = int(getattr(usage, "prompt_tokens", 0) or 0)
            completion_tokens = int(getattr(usage, "completion_tokens", 0) or 0)
            total_tokens = int(getattr(usage, "total_tokens", 0) or 0)
            cost = (prompt_tokens * INPUT_COST_PER_MILLION + completion_tokens * OUTPUT_COST_PER_MILLION) / 1_000_000
            if spent + cost > args.budget_usd:
                raise SystemExit("actual API spend exceeded the configured budget")
            batch_suggestions = parse_suggestions(response.choices[0].message.content or "{}", batch)
            suggestion_by_key = {_key(item): item for item in suggestions}
            suggestion_by_key.update({_key(item): item for item in batch_suggestions})
            suggestions = list(suggestion_by_key.values())
            spent += cost
            increment = {"prompt_tokens": prompt_tokens, "completion_tokens": completion_tokens, "total_tokens": total_tokens}
            merge_usage(usage_total, increment)
            merge_usage(pass_usage, increment)
            completed.update(_key(item) for item in batch_suggestions)
            unresolved_keys = sorted({_key(item) for item in motions} - completed)
            pass_record.update({"spent_usd": spent - starting_spent, "usage": pass_usage, "completed_motion_count": len(completed), "unresolved_keys": unresolved_keys})
            pass_record["completed_motion_count"] = len(completed)
            checkpoint = {
                "completed_keys": sorted(completed),
                "unresolved_keys": unresolved_keys,
                "suggestions": suggestions,
                "spent_usd": spent,
                "usage_total": usage_total,
                "run_history": run_history,
            }
            args.checkpoint.parent.mkdir(parents=True, exist_ok=True)
            args.checkpoint.write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")
        pass_record["status"] = "complete"
        checkpoint["run_history"] = run_history
        args.checkpoint.write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")
        result.update({
            "status": "complete",
            "network_called": True,
            "completed_motion_count": len(completed),
            "unresolved_motion_count": len(motions) - len(completed),
            "unresolved_keys": sorted({_key(item) for item in motions} - completed),
            "suggestion_count": len(suggestions),
            "pending_motion_count": len(motions) - len(completed),
            "spent_usd": spent,
            "usage": usage_total,
            "run_history": run_history,
            "suggestions": suggestions,
            "created_at": datetime.now(timezone.utc).isoformat(),
        })
    elif args.send:
        result.update({
            "status": "complete",
            "completed_motion_count": len(completed),
            "unresolved_motion_count": len(motions) - len(completed),
            "unresolved_keys": sorted({_key(item) for item in motions} - completed),
            "suggestion_count": len(checkpoint.get("suggestions", [])),
            "spent_usd": float(checkpoint.get("spent_usd", 0.0)),
            "usage": {**empty_usage(), **checkpoint.get("usage_total", {})},
            "run_history": checkpoint.get("run_history", []),
            "suggestions": checkpoint.get("suggestions", []),
        })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(json.dumps({key: result.get(key) for key in ("status", "source_motion_count", "pending_motion_count", "batch_count", "projected_cost_usd", "network_called", "database_written")}, sort_keys=True))
    return 0 if result["status"] in {"prepared", "complete"} else 1


if __name__ == "__main__":
    raise SystemExit(main())