"""Audit deterministic FC Activity events with a bounded OpenAI sample."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import random
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL = "gpt-4.1-nano"
INPUT_COST_PER_MILLION = 0.10
OUTPUT_COST_PER_MILLION = 0.40


def select_audit_cases(
    cases: list[dict[str, Any]],
    *,
    limit: int,
    recent_years: int,
    recent_share: float,
    seed: int,
) -> list[dict[str, Any]]:
    if limit < 1:
        raise ValueError("limit must be positive")
    years = sorted({int(case["year"]) for case in cases if case.get("year") is not None})
    cutoff = years[-min(recent_years, len(years))] if years else None
    recent = [case for case in cases if cutoff is not None and case.get("year") is not None and int(case["year"]) >= cutoff]
    older = [case for case in cases if case not in recent]
    recent_count = min(len(recent), max(1, round(limit * recent_share)))
    older_count = min(len(older), limit - recent_count)
    if recent_count + older_count < limit:
        remaining = limit - recent_count - older_count
        recent_count += min(remaining, len(recent) - recent_count)
        older_count += min(limit - recent_count - older_count, len(older) - older_count)
    rng = random.Random(seed)
    return sorted(rng.sample(recent, recent_count) + rng.sample(older, older_count), key=lambda case: (case.get("year") or 0, case.get("activity_case_id") or 0))


def _compact_case(case: dict[str, Any]) -> dict[str, Any]:
    classification = case.get("classification", {})
    events = classification.get("procedural_events", [])
    source_documents = case.get("source_documents", [])
    return {
        "activity_case_id": case.get("activity_case_id"),
        "year": case.get("year"),
        "case_name": case.get("case_name"),
        "document_count": case.get("document_count"),
        "deterministic_events": [
            {
                "event_type": event.get("event_type"),
                "subtype": event.get("subtype"),
                "outcome": event.get("outcome"),
                "source_document_date": event.get("source_document_date"),
                "doc_id": event.get("doc_id"),
                "rule": event.get("rule"),
                "text": str(event.get("text") or "")[:1200],
            }
            for event in events
        ],
        "source_documents": [
            {
                "doc_id": document.get("doc_id"),
                "source_document_date": document.get("source_document_date"),
                "text": str(document.get("text") or "")[:500],
            }
            for document in source_documents[:20]
        ],
    }


def build_messages(cases: list[dict[str, Any]]) -> list[dict[str, str]]:
    system = (
        "You audit deterministic extraction from Federal Court procedural-history records. "
        "Do not infer legal outcomes beyond the supplied text. For each case, identify only "
        "missed procedural events, false positives, ambiguous outcomes, missing judge or date "
        "signals, and concrete rule improvements. Treat source_document_date as a registry "
        "date, not automatically a filing, hearing, or decision date. Return JSON with a "
        "findings array; each finding has activity_case_id, issue_type, event_type, "
        "deterministic_value, suggested_value, evidence, and rule_suggestion. Do not propose "
        "database writes or canonical case changes."
        " Keep the response concise: at most three findings per case and quote no more than 240 characters of evidence."
    )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": json.dumps({"cases": [_compact_case(case) for case in cases]}, ensure_ascii=True)},
    ]


def estimate_cost(usage: Any) -> float:
    prompt_tokens = int(getattr(usage, "prompt_tokens", 0) or 0)
    completion_tokens = int(getattr(usage, "completion_tokens", 0) or 0)
    return (prompt_tokens * INPUT_COST_PER_MILLION + completion_tokens * OUTPUT_COST_PER_MILLION) / 1_000_000


def parse_audit_response(raw_response: str) -> tuple[list[dict[str, Any]], str | None]:
    try:
        parsed_response = json.loads(raw_response or "{}")
    except json.JSONDecodeError as exc:
        return [], f"{type(exc).__name__}: {exc}"
    if not isinstance(parsed_response, dict) or not isinstance(parsed_response.get("findings", []), list):
        return [], "response must be a JSON object with a findings array"
    return parsed_response["findings"], None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/eval/fc_activity_deterministic_evaluation_20260925.json"))
    parser.add_argument("--output", type=Path, default=Path("data/eval/fc_activity_openai_audit_20260925.json"))
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--recent-years", type=int, default=7)
    parser.add_argument("--recent-share", type=float, default=0.75)
    parser.add_argument("--seed", type=int, default=20260925)
    parser.add_argument("--budget-usd", type=float, default=5.0)
    parser.add_argument("--send", action="store_true", help="Send the bounded sample to OpenAI")
    args = parser.parse_args()
    if args.budget_usd <= 0 or args.budget_usd > 5:
        parser.error("--budget-usd must be greater than 0 and at most 5")
    report = json.loads(args.input.read_text(encoding="utf-8"))
    cases = select_audit_cases(
        report["cases"],
        limit=args.limit,
        recent_years=args.recent_years,
        recent_share=args.recent_share,
        seed=args.seed,
    )
    messages = build_messages(cases)
    result: dict[str, Any] = {
        "audit_version": "fc_activity_openai_audit_v1",
        "model": MODEL,
        "sample_size": len(cases),
        "recent_years": args.recent_years,
        "recent_share": args.recent_share,
        "budget_usd": args.budget_usd,
        "network_called": False,
        "database_written": False,
        "sample_case_ids": [case.get("activity_case_id") for case in cases],
    }
    if not args.send:
        result["status"] = "prepared"
    else:
        load_dotenv(PROJECT_ROOT / ".env", override=False)
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise SystemExit("OPENAI_API_KEY is required for --send; no request was made")
        os.environ.pop("OPENAI_ORG_ID", None)
        os.environ.pop("OPENAI_ORGANIZATION", None)
        client = OpenAI(api_key=api_key, timeout=120.0, max_retries=0)
        response = client.chat.completions.create(
            model=MODEL,
            temperature=0,
            max_tokens=8000,
            response_format={"type": "json_object"},
            messages=messages,
        )
        usage = {
            "prompt_tokens": int(getattr(response.usage, "prompt_tokens", 0) or 0),
            "completion_tokens": int(getattr(response.usage, "completion_tokens", 0) or 0),
            "total_tokens": int(getattr(response.usage, "total_tokens", 0) or 0),
            "estimated_cost_usd": estimate_cost(response.usage),
        }
        if usage["estimated_cost_usd"] > args.budget_usd:
            raise SystemExit("estimated API spend exceeded the configured budget")
        raw_response = response.choices[0].message.content or ""
        result.update(
            {
                "network_called": True,
                "created_at": datetime.now(timezone.utc).isoformat(),
                "usage": usage,
            }
        )
        findings, response_error = parse_audit_response(raw_response)
        if response_error:
            result.update(
                {
                    "status": "invalid_response",
                    "response_error": response_error,
                    "raw_response": raw_response,
                    "findings": [],
                }
            )
        else:
            result.update(
                {
                    "status": "complete",
                    "findings": findings,
                }
            )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("status", "sample_size", "network_called", "database_written")}, sort_keys=True))
    return 0 if result.get("status") in {"prepared", "complete"} else 1


if __name__ == "__main__":
    raise SystemExit(main())