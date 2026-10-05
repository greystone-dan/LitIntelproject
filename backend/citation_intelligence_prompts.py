"""Improved prompts for citation intelligence analysis.

These prompts operate at the discussion unit level (not per-paragraph),
to leverage unit boundaries and reduce LLM cost while improving quality.
"""

from __future__ import annotations
from typing import Any
import json

from .prompt_registry import get_prompt


def build_issue_focused_assessment_request(
    case_id: int,
    paragraphs: list[dict[str, Any]],
    *,
    model: str = "gpt-4o-mini",
    budget_usd: float = 1.0,
) -> dict[str, Any]:
    """Assessment focused on identifying legal ISSUES and how authorities are used.

    Returns: issue, issue_role, cited_authority, authority_function, explanation, confidence
    """
    system, prompt_version = get_prompt("citation_issue_focused_assessment")
    payload = {
        "request_id": f"citation-intelligence-assessment-case-{case_id}",
        "contract_version": "citation_intelligence_assessment_v1",
        "case_id": case_id,
        "paragraphs": [
            {"paragraph_index": item["paragraph_index"], "text": item["text"]}
            for item in paragraphs
        ],
    }
    return {
        "model": model,
        "budget_usd": budget_usd,
        "prompt_version": prompt_version,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=True, sort_keys=True)},
        ],
    }


def build_citation_aware_assessment_request(
    case_id: int,
    paragraphs: list[dict[str, Any]],
    *,
    model: str = "gpt-4o-mini",
    budget_usd: float = 1.0,
) -> dict[str, Any]:
    """Assessment that tracks which authorities are cited for which issues.

    Returns: issue, authorities (array), conclusion, explanation, confidence
    """
    system, prompt_version = get_prompt("citation_aware_assessment")
    payload = {
        "request_id": f"citation-aware-assessment-case-{case_id}",
        "contract_version": "citation_aware_assessment_v1",
        "case_id": case_id,
        "paragraphs": [
            {"paragraph_index": item["paragraph_index"], "text": item["text"]}
            for item in paragraphs
        ],
    }
    return {
        "model": model,
        "budget_usd": budget_usd,
        "prompt_version": prompt_version,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=True, sort_keys=True)},
        ],
    }


def build_lightweight_issue_extraction_request(
    case_id: int,
    paragraphs: list[dict[str, Any]],
    *,
    model: str = "gpt-4o-mini",
    budget_usd: float = 1.0,
) -> dict[str, Any]:
    """Lightweight extraction: one sentence per question.

    Returns: issue, cited_authorities, conclusion, explanation, confidence
    """
    system, prompt_version = get_prompt("citation_lightweight_issue_extraction")
    payload = {
        "request_id": f"lightweight-issue-extraction-case-{case_id}",
        "contract_version": "lightweight_issue_extraction_v1",
        "case_id": case_id,
        "paragraphs": [
            {"paragraph_index": item["paragraph_index"], "text": item["text"]}
            for item in paragraphs
        ],
    }
    return {
        "model": model,
        "budget_usd": budget_usd,
        "prompt_version": prompt_version,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=True, sort_keys=True)},
        ],
    }


def build_unit_context_assessment_request(
    case_id: int,
    unit_text: str,
    *,
    case_metadata: dict[str, Any] | None = None,
    preceding_unit: str | None = None,
    following_unit: str | None = None,
    model: str = "gpt-4o-mini",
    budget_usd: float = 1.0,
) -> dict[str, Any]:
    """Assessment with full unit context and optional metadata for sharpened issue labels.

    Args:
        case_id: Case identifier
        unit_text: Full discussion unit text
        case_metadata: Dict with case_name, court, year, tags, statute_refs, cited_authorities
        preceding_unit: Previous discussion unit for context (optional)
        following_unit: Next discussion unit for context (optional)
        model: LLM model to use
        budget_usd: Budget limit

    Returns: issue_label, proposition, key_authorities, confidence
    """
    metadata_context = ""
    if case_metadata:
        metadata_context = (
            "\n\nCASE CONTEXT (structured data):\n"
            f"  Case: {case_metadata.get('case_name', 'N/A')}\n"
            f"  Court: {case_metadata.get('court', 'N/A')}\n"
            f"  Year: {case_metadata.get('year', 'N/A')}\n"
            f"  Legal tags: {', '.join(case_metadata.get('tags', []))}\n"
            f"  Statute references: {', '.join(case_metadata.get('statute_refs', []))}\n"
            f"  Cited authorities: {', '.join(case_metadata.get('cited_authorities', []))}"
        )

    context_note = ""
    if preceding_unit or following_unit:
        context_note = "\nCONTEXT: This unit is part of a larger discussion. "
        if preceding_unit:
            context_note += "The preceding unit discusses: [context unit provided]. "
        if following_unit:
            context_note += "The following unit discusses: [context unit provided]."

    system, prompt_version = get_prompt("citation_unit_context_assessment")
    system = system.replace("{{context_note}}", context_note, 1).replace(
        "{{metadata_context}}", metadata_context, 1
    )

    user_content = f"DISCUSSION UNIT:\n\n{unit_text}"
    if preceding_unit:
        user_content = f"PRECEDING UNIT (context):\n{preceding_unit}\n\n" + user_content
    if following_unit:
        user_content = user_content + f"\n\nFOLLOWING UNIT (context):\n{following_unit}"

    return {
        "model": model,
        "budget_usd": budget_usd,
        "prompt_version": prompt_version,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user_content},
        ],
    }
