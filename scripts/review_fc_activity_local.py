"""Run one bounded, evidence-constrained FC Activity review through the local provider."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

import httpx

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.text_generation_providers import get_text_generation_provider


def _review_prompt(text: str) -> list[dict[str, str]]:
    return [
        {
            "role": "system",
            "content": (
                "Return a JSON object with exactly these keys: ambiguity, candidate_event, "
                "evidence_quote, abstain. Review only the supplied Activity text. "
                "Do not infer facts absent from the text. Set abstain to true when the "
                "text is ambiguous or does not support a candidate event."
            ),
        },
        {
            "role": "user",
            "content": f"Activity text:\n{text}",
        },
    ]


def validate_review(review: Any, source_text: str) -> dict[str, Any]:
    if not isinstance(review, dict):
        return {"valid": False, "reason": "response_is_not_an_object", "abstain": True}
    required = {"ambiguity", "candidate_event", "evidence_quote", "abstain"}
    if isinstance(review.get("abstain"), str) and review["abstain"].casefold() in {"true", "false"}:
        review = {**review, "abstain": review["abstain"].casefold() == "true"}
    if set(review) != required or not isinstance(review["abstain"], bool):
        return {"valid": False, "reason": "unexpected_review_schema", "abstain": True}
    evidence_quote = review["evidence_quote"]
    if evidence_quote and evidence_quote not in source_text:
        return {"valid": False, "reason": "evidence_quote_not_in_source", "abstain": True}
    if not review["abstain"] and (not review["candidate_event"] or not evidence_quote):
        return {"valid": False, "reason": "non_abstaining_review_lacks_evidence", "abstain": True}
    return {"valid": True, "reason": None, **review}


def review_text(text: str) -> dict[str, Any]:
    provider = get_text_generation_provider()
    try:
        response = provider.create_chat_completion(
            messages=_review_prompt(text),
            temperature=0,
            max_tokens=400,
            response_format={"type": "json_object"},
        )
    except httpx.HTTPError as exc:
        return {
            "provider": "local",
            "model": provider.model_name,
            "source_text": text,
            "status": "blocked",
            "blocker": f"local_provider_http_error: {exc}",
            "database_written": False,
            "production_fact_written": False,
        }
    content = response.choices[0].message.content or ""
    try:
        parsed = json.loads(content)
    except json.JSONDecodeError:
        parsed = None
    review = validate_review(parsed, text)
    return {
        "provider": "local",
        "model": provider.model_name,
        "status": "completed",
        "source_text": text,
        "raw_response": content,
        "review": review,
        "database_written": False,
        "production_fact_written": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", required=True, help="One Activity entry to review")
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    result = review_text(args.text)
    payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0 if result.get("status") == "completed" and result.get("review", {}).get("valid") else 2


if __name__ == "__main__":
    raise SystemExit(main())
