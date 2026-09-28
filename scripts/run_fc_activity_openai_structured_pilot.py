"""Run a bounded, review-only structured FC Activity extraction pilot."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import random
import sys
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI
from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import FCActivityClassification, SessionLocal

MODEL = "gpt-4.1-nano"
MODEL_RATES = {
    "gpt-4.1-nano": (0.10, 0.40),
    "gpt-4.1-mini": (0.40, 1.60),
    "gpt-4.1": (2.00, 8.00),
}
MAX_OUTPUT_TOKENS = 1400
USAGE_KEYS = ("prompt_tokens", "completion_tokens", "total_tokens")


def select_cases(report: dict[str, Any], limit: int, seed: int) -> list[dict[str, Any]]:
    cases = list(report.get("cases", []))
    if limit < 1 or limit > len(cases):
        raise ValueError("limit must be between 1 and the report case count")
    return sorted(
        random.Random(seed).sample(cases, limit),
        key=lambda case: (case.get("year") or 0, case.get("activity_case_id") or 0),
    )



def attach_imm_numbers(cases: list[dict[str, Any]]) -> None:
    case_ids = [case.get("activity_case_id") for case in cases if case.get("activity_case_id") is not None]
    if not case_ids:
        return
    with SessionLocal() as session:
        classifications = session.scalars(
            select(FCActivityClassification).where(FCActivityClassification.source_case_id.in_(case_ids))
        ).all()
    imm_by_case = {item.source_case_id: item.imm_number for item in classifications}
    for case in cases:
        case["imm_number"] = imm_by_case.get(case.get("activity_case_id"), case.get("imm_number"))


def _nullable_string() -> dict[str, Any]:
    return {"type": ["string", "null"]}


def _nullable_integer() -> dict[str, Any]:
    return {"type": ["integer", "null"]}


def _object(properties: dict[str, Any], required: list[str] | None = None) -> dict[str, Any]:
    return {
        "type": "object",
        "properties": properties,
        "required": required or list(properties),
        "additionalProperties": False,
    }


RESPONSE_SCHEMA = _object(
    {
        "case": _object({"activity_case_id": {"type": "integer"}, "imm_number": {"type": "string"}}),
        "application": _object({"status": {"type": "string"}, "filing_date": _nullable_string(), "event_date": _nullable_string(), "evidence_doc_id": _nullable_integer()}),
        "challenged_decision": _object({
            "status": {"type": "string"}, "application_type": _nullable_string(), "filing_date": _nullable_string(),
            "decision_maker": _nullable_string(), "decision_maker_type": {"type": "string"},
            "decision_type": {"type": "string"}, "decision_subject": {"type": "string"},
            "decision_date": _nullable_string(), "tribunal_file_numbers": {"type": "array", "items": {"type": "string"}},
            "evidence_doc_id": _nullable_integer(),
        }),
        "perfection": _object({"status": {"type": "string"}, "filing_date": _nullable_string(), "evidence_doc_id": _nullable_integer()}),
        "leave_decision": _object({"status": {"type": "string"}, "result": _nullable_string(), "decision_date": _nullable_string(), "evidence_doc_id": _nullable_integer()}),
        "judicial_review_result": _object({"status": {"type": "string"}, "result": _nullable_string(), "decision_date": _nullable_string(), "evidence_doc_id": _nullable_integer()}),
        "judicial_review_final_decision": _object({"status": {"type": "string"}, "result": _nullable_string(), "decision_date": _nullable_string(), "evidence_doc_id": _nullable_integer()}),
        "final_decision": _object({"status": {"type": "string"}, "result": _nullable_string(), "decision_date": _nullable_string(), "evidence_doc_id": _nullable_integer()}),
        "judges": {"type": "array", "items": _object({"name": {"type": "string"}, "stage": {"type": "string"}, "date": _nullable_string(), "evidence_doc_id": _nullable_integer()})},
        "motions": {"type": "array", "items": _object({"reference": _nullable_string(), "filing_date": _nullable_string(), "type": {"type": "string"}, "result": _nullable_string(), "result_date": _nullable_string(), "evidence_doc_id": _nullable_integer()})},
    }
)


def compact_case(case: dict[str, Any]) -> dict[str, Any]:
    return {
        "activity_case_id": case.get("activity_case_id"),
        "imm_number": case.get("imm_number"),
        "case_name": case.get("case_name"),
        "source_documents": [
            {
                "doc_id": document.get("doc_id"),
                "source_document_date": document.get("source_document_date"),
                "text": document.get("text") or "",
            }
            for document in case.get("source_documents", [])
        ],
    }


def build_messages(case: dict[str, Any], response_mode: str = "strict") -> list[dict[str, str]]:
    if response_mode == "loose":
        system = (
            "Review one Canadian Federal Court FC Activity record and return a JSON object. "
            "Use the requested field names as a guide, but choose the most informative structure "
            "for the evidence rather than forcing empty stages or categorical values. Include "
            "application, challenged decision, perfection, leave decision, judicial review result, "
            "judicial review final decision, final decision, judges, and motions when supported. "
            "You may include concise explanatory fields when they clarify an event. Use only the "
            "supplied rows, do not invent facts, and preserve the distinction between filing dates, "
            "decision dates, event dates, and result dates. Include evidence document IDs whenever "
            "available. Copy the supplied activity_case_id and imm_number exactly. Return JSON only."
        )
    else:
        system = (
            "Extract one Canadian Federal Court FC Activity record into the required JSON schema. "
            "No prose, reasoning, confidence, or recommendations. Use only the supplied rows. "
            "Every property is mandatory: use null for unavailable dates or evidence_doc_id, and "
            "unknown for unsupported categorical strings. Never infer a legal subject, date, judge, "
            "decision maker, or motion result. Preserve date meanings: filing_date, decision_date, "
            "event_date, and result_date. Include every identifiable motion and judge. The supplied "
            "activity_case_id and imm_number must be copied exactly. Evidence is represented by the "
            "source document ID only."
        )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": json.dumps({"case": compact_case(case)}, ensure_ascii=True)},
    ]


def estimate_request_cost(
    case: dict[str, Any], max_output_tokens: int = MAX_OUTPUT_TOKENS, model: str = MODEL
) -> float:
    payload = json.dumps({"case": compact_case(case)}, ensure_ascii=True, separators=(",", ":"))
    prompt_tokens = (len(payload) + 3) // 4 + 700
    input_rate, output_rate = MODEL_RATES[model]
    return (prompt_tokens * input_rate + max_output_tokens * output_rate) / 1_000_000


def empty_usage() -> dict[str, int]:
    return {key: 0 for key in USAGE_KEYS}


def merge_usage(total: dict[str, int], usage: Any) -> None:
    for key in USAGE_KEYS:
        value = usage.get(key, 0) if isinstance(usage, dict) else getattr(usage, key, 0)
        total[key] = total.get(key, 0) + int(value or 0)


def actual_cost(usage: Any, model: str = MODEL) -> float:
    input_rate, output_rate = MODEL_RATES[model]
    return (
        int(getattr(usage, "prompt_tokens", 0) or 0) * input_rate
        + int(getattr(usage, "completion_tokens", 0) or 0) * output_rate
    ) / 1_000_000


def parse_response(raw: str, case: dict[str, Any], response_mode: str = "strict") -> tuple[dict[str, Any], list[str]]:
    parsed = json.loads(raw or "{}")
    if not isinstance(parsed, dict):
        raise ValueError("response must be a JSON object")
    case_result = parsed.get("case")
    missing_fields: list[str] = []
    if not isinstance(case_result, dict):
        if response_mode == "strict":
            raise ValueError("response.case must be an object")
        parsed["case"] = {
            "activity_case_id": case.get("activity_case_id"),
            "imm_number": case.get("imm_number"),
        }
        missing_fields.append("case")
    else:
        if case_result.get("activity_case_id") != case.get("activity_case_id"):
            raise ValueError("response case id does not match request")
        if case_result.get("imm_number") != case.get("imm_number"):
            raise ValueError("response IMM number does not match request")
    for field in ("application", "challenged_decision", "perfection", "leave_decision", "judicial_review_result", "judicial_review_final_decision", "final_decision"):
        if field not in parsed or not isinstance(parsed[field], dict):
            parsed[field] = {"status": "unknown", "evidence_doc_id": None, "evidence_text": None}
            missing_fields.append(field)
    for field in ("judges", "motions"):
        if field not in parsed or not isinstance(parsed[field], list):
            parsed[field] = []
            missing_fields.append(field)
    return parsed, missing_fields


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20260928)
    parser.add_argument("--budget-usd", type=float, default=1.0)
    parser.add_argument("--workers", type=int, default=5)
    parser.add_argument("--max-output-tokens", type=int, default=MAX_OUTPUT_TOKENS)
    parser.add_argument("--model", choices=tuple(MODEL_RATES), default=MODEL)
    parser.add_argument("--response-mode", choices=("strict", "loose"), default="strict")
    parser.add_argument("--retry-failures", action="store_true")
    parser.add_argument("--send", action="store_true")
    args = parser.parse_args()
    if args.budget_usd <= 0 or args.budget_usd > 5 or not 1 <= args.workers <= 10 or not 400 <= args.max_output_tokens <= 4000:
        parser.error("budget must be greater than 0 and at most 5; workers 1-10; max output tokens 400-4000")

    report = json.loads(args.input.read_text(encoding="utf-8"))
    cases = select_cases(report, args.limit, args.seed)
    attach_imm_numbers(cases)
    selected_ids = [case.get("activity_case_id") for case in cases]
    checkpoint = json.loads(args.checkpoint.read_text(encoding="utf-8")) if args.checkpoint.exists() else {
        "completed_case_ids": [], "results": [], "spent_usd": 0.0, "usage": empty_usage(), "failures": []
    }
    completed = set(checkpoint.get("completed_case_ids", []))
    failed_ids = {item.get("activity_case_id") for item in checkpoint.get("failures", [])}
    pending = [
        case for case in cases
        if case.get("activity_case_id") not in completed
        or (args.retry_failures and case.get("activity_case_id") in failed_ids)
    ]
    projected_cost = sum(estimate_request_cost(case, args.max_output_tokens, args.model) for case in pending)
    result: dict[str, Any] = {
        "pilot_version": "fc_activity_openai_structured_pilot_v1",
        "response_mode": args.response_mode,
        "model": args.model,
        "input_report": str(args.input),
        "seed": args.seed,
        "sample_size": len(cases),
        "selected_case_ids": selected_ids,
        "requests_planned": len(pending),
        "requests_per_case": True,
        "workers": args.workers,
        "max_output_tokens": args.max_output_tokens,
        "budget_usd": args.budget_usd,
        "projected_cost_usd": projected_cost,
        "network_called": False,
        "database_written": False,
        "status": "prepared",
    }
    if projected_cost > args.budget_usd:
        result["status"] = "budget_exceeded"
    elif args.send and pending:
        load_dotenv(PROJECT_ROOT / ".env", override=False)
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise SystemExit("OPENAI_API_KEY is required for --send; no request was made")
        for name in ("OPENAI_ORG_ID", "OPENAI_ORGANIZATION", "OPENAI_PROJECT_ID"):
            os.environ.pop(name, None)
        client = OpenAI(api_key=api_key, timeout=120.0, max_retries=0)
        spent = float(checkpoint.get("spent_usd", 0.0))
        usage_total = {**empty_usage(), **checkpoint.get("usage", {})}
        results = list(checkpoint.get("results", []))
        failures = list(checkpoint.get("failures", []))
        if args.retry_failures:
            pending_ids = {case.get("activity_case_id") for case in pending}
            results = [item for item in results if item.get("activity_case_id") not in pending_ids]
            failures = [item for item in failures if item.get("activity_case_id") not in pending_ids]
        if spent + projected_cost > args.budget_usd:
            raise SystemExit("projected API spend would exceed the configured budget")

        def request_case(case: dict[str, Any]) -> tuple[dict[str, Any], dict[str, int], float]:
            case_id = case.get("activity_case_id")
            record: dict[str, Any] = {"activity_case_id": case_id, "imm_number": case.get("imm_number")}
            usage_increment = empty_usage()
            cost = 0.0
            try:
                response = client.chat.completions.create(
                    model=args.model,
                    temperature=0,
                    max_tokens=args.max_output_tokens,
                    response_format=(
                        {"type": "json_object"}
                        if args.response_mode == "loose"
                        else {
                            "type": "json_schema",
                            "json_schema": {"name": "fc_activity_extraction", "strict": True, "schema": RESPONSE_SCHEMA},
                        }
                    ),
                    messages=build_messages(case, args.response_mode),
                )
                cost = actual_cost(response.usage, args.model)
                usage_increment = {key: int(getattr(response.usage, key, 0) or 0) for key in USAGE_KEYS}
                extraction, missing_fields = parse_response(
                    response.choices[0].message.content or "{}", case, args.response_mode
                )
                record.update({
                    "status": "complete",
                    "cost_usd": cost,
                    "usage": usage_increment,
                    "missing_fields": missing_fields,
                    "extraction": extraction,
                })
            except Exception as exc:
                record.update({
                    "status": "failed",
                    "cost_usd": cost,
                    "usage": usage_increment,
                    "error": f"{type(exc).__name__}: {exc}",
                })
            return record, usage_increment, cost

        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            for record, usage_increment, cost in executor.map(request_case, pending):
                if spent + cost > args.budget_usd:
                    raise SystemExit("actual API spend exceeded the configured budget")
                merge_usage(usage_total, usage_increment)
                spent += cost
                if record["status"] == "complete":
                    results.append(record)
                else:
                    failures.append(record)
                completed.add(record["activity_case_id"])
                checkpoint = {
                    "completed_case_ids": sorted(completed),
                    "results": results,
                    "failures": failures,
                    "spent_usd": spent,
                    "usage": usage_total,
                }
                args.checkpoint.parent.mkdir(parents=True, exist_ok=True)
                args.checkpoint.write_text(json.dumps(checkpoint, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
        result.update({
            "status": "complete",
            "network_called": True,
            "requests_attempted": len(pending),
            "completed_count": len(results),
            "failure_count": len(failures),
            "spent_usd": spent,
            "usage": usage_total,
            "results": results,
            "failures": failures,
            "created_at": datetime.now(timezone.utc).isoformat(),
        })
    elif args.send:
        result.update({
            "status": "complete",
            "network_called": True,
            "requests_attempted": 0,
            "completed_count": len(checkpoint.get("results", [])),
            "failure_count": len(checkpoint.get("failures", [])),
            "spent_usd": float(checkpoint.get("spent_usd", 0.0)),
            "usage": {**empty_usage(), **checkpoint.get("usage", {})},
            "results": checkpoint.get("results", []),
            "failures": checkpoint.get("failures", []),
        })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(json.dumps({key: result.get(key) for key in ("status", "sample_size", "requests_planned", "projected_cost_usd", "network_called", "database_written")}, sort_keys=True))
    return 0 if result["status"] in {"prepared", "complete"} else 1


if __name__ == "__main__":
    raise SystemExit(main())