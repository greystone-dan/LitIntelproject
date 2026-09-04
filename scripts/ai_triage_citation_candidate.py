"""Bounded AI triage for proposed case-citation review candidates.

This script produces suggestions only. It never modifies the candidate fixture,
database rows, or confirmed gold data. Use --dry-run first.
"""
from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from openai import OpenAI

DEFAULT_INPUT = Path("data/eval/five_case_citation_gold_candidate.json")
DEFAULT_OUTPUT = Path("data/eval/five_case_citation_ai_triage_suggestions.json")
DEFAULT_MODEL = os.getenv("OPENAI_AUDIT_MODEL", "gpt-4.1-nano")
DEFAULT_BUDGET_USD = float(os.getenv("OPENAI_AUDIT_BUDGET_USD", "0.10"))
DEFAULT_INPUT_COST = float(os.getenv("OPENAI_AUDIT_INPUT_COST_PER_1M", "0.10"))
DEFAULT_OUTPUT_COST = float(os.getenv("OPENAI_AUDIT_OUTPUT_COST_PER_1M", "0.40"))


def load_candidates(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    # Reviewers may place a plain-language comment immediately after an opening
    # object brace. Strip that annotation for parsing; the source fixture stays
    # untouched and the AI receives only structured occurrence fields.
    text = re.sub(r"(?m)^(\s*)\{[^\"\n]+\n", r"\1{\n", text)
    payload = json.loads(text)
    if payload.get("review_status") != "proposed":
        raise ValueError("Only proposed candidate fixtures may be triaged")
    return payload


def select_occurrences(payload: dict[str, Any], limit: int, context_chars: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for case in payload.get("cases", []):
        for index, occurrence in enumerate(case.get("occurrences", [])):
            row = {
                "review_id": f"{case['case_id']}:{index}",
                "case_id": case["case_id"],
                "court": case.get("court"),
                "case_citation": case.get("citation"),
                "kind": occurrence.get("kind"),
                "citation_text": occurrence.get("citation_text"),
                "normalized_citation": occurrence.get("normalized_citation"),
                "offset_start": occurrence.get("offset_start"),
                "offset_end": occurrence.get("offset_end"),
                "pinpoint": occurrence.get("pinpoint"),
                "declared_alias": occurrence.get("declared_alias"),
                "anchor_citation_text": occurrence.get("anchor_citation_text"),
                "source_context_excerpt": (occurrence.get("source_context_excerpt") or "")[:context_chars],
            }
            rows.append(row)
    # Prioritize structurally complex records first, then preserve fixture order.
    rows.sort(key=lambda row: (not bool(row["pinpoint"]), not bool(row["declared_alias"]), row["review_id"]))
    return rows[:limit]


def estimate_cost(rows: list[dict[str, Any]], output_tokens: int, input_rate: float, output_rate: float) -> dict[str, Any]:
    input_chars = sum(len(json.dumps(row, ensure_ascii=False)) for row in rows)
    input_tokens = max(1, input_chars // 4)
    cost = (input_tokens / 1_000_000 * input_rate) + (output_tokens / 1_000_000 * output_rate)
    return {"input_chars": input_chars, "estimated_input_tokens": input_tokens, "estimated_output_tokens": output_tokens, "estimated_cost_usd": round(cost, 8)}


def build_messages(rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    system = (
        "You are a citation-extraction triage reviewer. Review only case-to-case citations. "
        "Do not review statutes or tagging. Do not declare gold. Flag likely issues only. "
        "Every occurrence is data, including duplicates. Return JSON with key suggestions, "
        "an array of objects containing review_id, issue_type (one of WRONG_KIND, WRONG_SPAN, "
        "WRONG_PINPOINT, WRONG_ALIAS, WRONG_ANCHOR, FALSE_POSITIVE, UNCLEAR, NONE), "
        "confidence (0 to 1), and concise rationale. Flag NONE when no likely issue is visible."
    )
    user = "Review these proposed occurrences. Do not invent missed citations beyond the supplied context:\n" + json.dumps(rows, ensure_ascii=False)
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def parse_suggestions(content: str) -> list[dict[str, Any]]:
    cleaned = content.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", cleaned, flags=re.IGNORECASE | re.DOTALL).strip()
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start < 0 or end <= start:
        raise ValueError("AI response did not contain a JSON object")
    payload = json.loads(cleaned[start : end + 1])
    suggestions = payload.get("suggestions", [])
    if not isinstance(suggestions, list):
        raise ValueError("AI response suggestions must be a list")
    return suggestions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--context-chars", type=int, default=1200)
    parser.add_argument("--max-output-tokens", type=int, default=400)
    parser.add_argument("--budget-usd", type=float, default=DEFAULT_BUDGET_USD)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.limit < 1 or args.context_chars < 100 or args.max_output_tokens < 1 or args.budget_usd <= 0:
        parser.error("limit/context/output/budget values must be positive")

    rows = select_occurrences(load_candidates(args.input), args.limit, args.context_chars)
    estimate = estimate_cost(rows, args.max_output_tokens, DEFAULT_INPUT_COST, DEFAULT_OUTPUT_COST)
    if estimate["estimated_cost_usd"] > args.budget_usd:
        raise SystemExit(f"estimated cost exceeds budget: {estimate['estimated_cost_usd']} > {args.budget_usd}")

    if args.dry_run:
        print(json.dumps({"dry_run": True, "api_call": False, "model": args.model, "selected_count": len(rows), "estimate": estimate, "database_writes": False}, indent=2))
        return 0

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is required unless --dry-run is used")
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=args.model,
        messages=build_messages(rows),
        temperature=0,
        max_tokens=args.max_output_tokens,
        response_format={"type": "json_object"},
    )
    suggestions = parse_suggestions(response.choices[0].message.content or "{}")
    report = {
        "fixture_name": "five_case_citation_gold_candidate",
        "report_type": "ai_suggestion_only",
        "review_status": "ai_suggestions_unconfirmed",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model": args.model,
        "selected_occurrence_count": len(rows),
        "suggestions": suggestions,
        "database_writes": False,
        "gold_fixture_modified": False,
        "external_api_used": True,
        "cost_estimate": estimate,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(args.output), "suggestion_count": len(suggestions), "database_writes": False}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
