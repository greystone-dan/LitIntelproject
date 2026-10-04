"""Test improved citation intelligence assessment prompts against real database cases.

This script fetches real cases from the database, runs both current and improved
paragraph assessment prompts, and compares output quality and cost.

Run on: PC thread (has live database access)
Usage: python scripts/test_citation_intelligence_prompts.py \
  --case-ids 123,456,789 \
  --max-paragraphs 300 \
  --budget-usd 20.0 \
  --output-dir /path/to/output
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from openai import OpenAI
from sqlalchemy.orm import Session

from backend.citation_intelligence_prompts import (
    build_issue_focused_assessment_request,
    build_citation_aware_assessment_request,
    build_lightweight_issue_extraction_request,
    build_unit_context_assessment_request,
)
from backend.database import Case, CaseChunk, get_session
from backend.package_discussion_units_llm import (
    build_paragraph_assessment_request,
    _parse_paragraph_assessment,
)
from backend.text_generation_providers import get_text_generation_provider


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def fetch_case_paragraphs(
    session: Session,
    case_id: int,
    max_paragraphs: int | None = None,
) -> tuple[Case, list[dict[str, Any]]] | None:
    """Fetch a case and its paragraph chunks from the database."""
    case = session.query(Case).filter(Case.id == case_id).first()
    if not case:
        return None

    chunks = session.query(CaseChunk).filter(
        CaseChunk.case_id == case_id,
        CaseChunk.chunk_set == "paragraph",
    ).order_by(CaseChunk.chunk_index).all()

    paragraphs = []
    for idx, chunk in enumerate(chunks):
        if max_paragraphs and len(paragraphs) >= max_paragraphs:
            break
        paragraphs.append({
            "paragraph_index": idx,
            "text": chunk.text,
            "chunk_id": chunk.id,
        })

    return case, paragraphs


def run_assessment(
    client: OpenAI,
    request: dict[str, Any],
    variant_name: str,
) -> tuple[dict[str, Any], dict[str, Any]] | None:
    """Run a single assessment request and parse response."""
    try:
        response = client.chat.completions.create(**request)
    except Exception as e:
        return None, {"error": str(e), "variant": variant_name}

    try:
        content = response.choices[0].message.content
        assessments, complete = _parse_paragraph_assessment(
            content,
            request.get("paragraphs", []),  # Note: won't have exact structure
        )
        # For new variants, just try raw JSON parse
        if not assessments:
            assessments = json.loads(content).get("assessments", [])

        usage = {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.prompt_tokens + response.usage.completion_tokens,
        }
        # Rough cost estimate (gpt-4o-mini rates)
        input_cost = response.usage.prompt_tokens * 0.00015
        output_cost = response.usage.completion_tokens * 0.0006
        usage["estimated_cost_usd"] = input_cost + output_cost

        return {
            "variant": variant_name,
            "assessment_count": len(assessments),
            "usage": usage,
            "sample_assessment": assessments[0] if assessments else None,
        }, None
    except Exception as e:
        return None, {"error": str(e), "variant": variant_name, "response": content[:200]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--case-ids",
        help="Comma-separated case IDs to test (required)",
        required=True,
    )
    parser.add_argument(
        "--max-paragraphs",
        type=int,
        default=300,
        help="Max paragraphs per case (default 300)",
    )
    parser.add_argument(
        "--budget-usd",
        type=float,
        default=20.0,
        help="Budget in USD for testing (default 20.0)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/eval/citation_intelligence_tests"),
        help="Output directory for results",
    )
    parser.add_argument(
        "--variants",
        default="current,issue_focused,citation_aware,lightweight,unit_context,unit_with_metadata",
        help="Comma-separated variant names to test. Options: current, issue_focused, citation_aware, "
             "lightweight, unit_context (full unit), unit_with_metadata (unit + case metadata)",
    )
    args = parser.parse_args()

    try:
        case_ids = [int(x.strip()) for x in args.case_ids.split(",") if x.strip()]
    except ValueError:
        parser.error("--case-ids must be comma-separated integers")

    if not case_ids:
        parser.error("--case-ids must contain at least one case ID")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    variants = [v.strip() for v in args.variants.split(",") if v.strip()]

    # Get database and API clients
    session = next(get_session())
    try:
        client = OpenAI()  # Uses OPENAI_API_KEY from environment
    except Exception as e:
        print(f"Error: Could not initialize OpenAI client: {e}", file=sys.stderr)
        return 1

    results: dict[str, Any] = {
        "test_run": _now(),
        "case_ids": case_ids,
        "variants": variants,
        "max_paragraphs": args.max_paragraphs,
        "budget_usd": args.budget_usd,
        "cases": {},
        "summary": {
            "total_cost_usd": 0.0,
            "cases_tested": 0,
            "paragraphs_tested": 0,
            "errors": [],
        },
    }

    spent_usd = 0.0

    for case_id in case_ids:
        if spent_usd >= args.budget_usd:
            print(f"Budget exhausted; stopping at case {case_id}", file=sys.stderr)
            break

        print(f"Fetching case {case_id}...", file=sys.stderr)
        fetch_result = fetch_case_paragraphs(session, case_id, args.max_paragraphs)
        if not fetch_result:
            results["summary"]["errors"].append(f"Case {case_id} not found")
            continue

        case, paragraphs = fetch_result
        results["cases"][case_id] = {
            "case_title": case.title,
            "case_citation": case.citation,
            "paragraph_count": len(paragraphs),
            "variants": {},
        }

        print(f"  Loaded {len(paragraphs)} paragraphs; testing variants...", file=sys.stderr)

        for variant in variants:
            if spent_usd >= args.budget_usd:
                print(f"  Budget exhausted before testing {variant}", file=sys.stderr)
                results["cases"][case_id]["variants"][variant] = {"status": "skipped_budget"}
                continue

            print(f"    Testing {variant}...", file=sys.stderr)

            # Build request for this variant
            if variant == "current":
                request = build_paragraph_assessment_request(
                    {"case_id": case_id},
                    paragraphs,
                    model="gpt-4o-mini",
                    budget_usd=args.budget_usd - spent_usd,
                )
            elif variant == "issue_focused":
                request = build_issue_focused_assessment_request(
                    case_id,
                    paragraphs,
                    model="gpt-4o-mini",
                    budget_usd=args.budget_usd - spent_usd,
                )
            elif variant == "citation_aware":
                request = build_citation_aware_assessment_request(
                    case_id,
                    paragraphs,
                    model="gpt-4o-mini",
                    budget_usd=args.budget_usd - spent_usd,
                )
            elif variant == "lightweight":
                request = build_lightweight_issue_extraction_request(
                    case_id,
                    paragraphs,
                    model="gpt-4o-mini",
                    budget_usd=args.budget_usd - spent_usd,
                )
            elif variant == "unit_context":
                # Simulate unit assessment: use first few paragraphs as a "unit"
                unit_text = " ".join([p["text"] for p in paragraphs[:min(10, len(paragraphs))]])
                request = build_unit_context_assessment_request(
                    case_id,
                    unit_text,
                    model="gpt-4o-mini",
                    budget_usd=args.budget_usd - spent_usd,
                )
            elif variant == "unit_with_metadata":
                # Unit with metadata: include case info as structured context
                unit_text = " ".join([p["text"] for p in paragraphs[:min(10, len(paragraphs))]])
                metadata = {
                    "case_name": case.title,
                    "court": case.court if hasattr(case, "court") else "Unknown",
                    "year": case.date_year if hasattr(case, "date_year") else "Unknown",
                    "tags": [],  # Would be populated from real tags in production
                    "statute_refs": [],  # Would be populated from real statute refs
                    "cited_authorities": [],  # Would be populated from real citations
                }
                request = build_unit_context_assessment_request(
                    case_id,
                    unit_text,
                    case_metadata=metadata,
                    model="gpt-4o-mini",
                    budget_usd=args.budget_usd - spent_usd,
                )
            else:
                results["cases"][case_id]["variants"][variant] = {"status": "unknown_variant"}
                continue

            # Run assessment
            result, error = run_assessment(client, request, variant)
            if error:
                print(f"      Error: {error.get('error', 'unknown')}", file=sys.stderr)
                results["cases"][case_id]["variants"][variant] = error
                results["summary"]["errors"].append(f"Case {case_id} {variant}: {error.get('error')}")
            else:
                cost = result.get("usage", {}).get("estimated_cost_usd", 0.0)
                spent_usd += cost
                results["summary"]["total_cost_usd"] = spent_usd
                print(f"      Cost: ${cost:.4f}, tokens: {result.get('usage', {}).get('total_tokens', 'N/A')}", file=sys.stderr)
                results["cases"][case_id]["variants"][variant] = result

        results["summary"]["cases_tested"] += 1
        results["summary"]["paragraphs_tested"] += len(paragraphs)

    # Write results
    output_file = args.output_dir / f"assessment_comparison_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    output_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nResults written to: {output_file}", file=sys.stderr)
    print(f"Total cost: ${results['summary']['total_cost_usd']:.4f}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
