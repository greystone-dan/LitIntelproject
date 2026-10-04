"""Improved prompts for citation intelligence analysis.

These prompts operate at the discussion unit level (not per-paragraph),
to leverage unit boundaries and reduce LLM cost while improving quality.
"""

from __future__ import annotations
from typing import Any
import json


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
    system = (
        "You are a legal researcher analyzing Canadian court decisions. For each paragraph, "
        "identify the legal ISSUE being addressed (not procedural categories, but substantive "
        "legal questions like standing, duty to consult, breach of fiduciary duty, etc.). "
        "\n"
        "For each paragraph, return JSON with: paragraph_index, issue (one phrase like "
        "'Standing' or 'Breach of Fiduciary Duty'), issue_role (how this paragraph addresses "
        "the issue: 'establishing_law', 'applying_law', 'citing_authority', 'distinguishing', "
        "'outcome'), cited_authority (case name + citation if cited; null if none), "
        "authority_function (if cited: 'establishing_rule', 'applying_rule', 'distinguished', "
        "'followed', 'dicta'; null if none), explanation (1-2 sentences), and confidence "
        "(0.0-1.0). "
        "\n"
        "Return all paragraphs in order. Do not invent facts, citations, or paragraph indices. "
        "Use only the supplied paragraph text."
    )
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
    system = (
        "You are analyzing legal authorities and issues in a Canadian court decision. "
        "For each paragraph, identify: (1) What legal ISSUE is being addressed? "
        "(2) What authorities (cases, statutes, regulations) are cited, and how? "
        "(3) What is the conclusion about that issue? "
        "\n"
        "For 'how the authority is used', distinguish: establishing_governing_rule, "
        "applying_rule_to_facts, distinguished_not_followed, followed_or_approved, "
        "dicta_or_obiter. "
        "\n"
        "Return JSON with: paragraph_index, issue (one phrase), authorities (array of "
        "{citation: string, how_used: string, conclusion: string}), paragraph_conclusion "
        "(one sentence about the issue outcome), explanation (1-2 sentences), confidence. "
        "\n"
        "Return all paragraphs in order. Use only supplied text; do not invent."
    )
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
    system = (
        "For each legal paragraph, extract three pieces of information in plain language: "
        "(1) What is the legal ISSUE being addressed? (one phrase) "
        "(2) Which authorities (cases/statutes) are cited and how are they used? "
        "(one sentence max) (3) What is the conclusion about that issue? (one sentence) "
        "\n"
        "Return JSON with: paragraph_index, issue, cited_authorities (brief description), "
        "conclusion, explanation (optional, brief), confidence (0.0-1.0). "
        "\n"
        "Use paragraph text exactly as written. Return all paragraphs in order."
    )
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

    system = (
        "You are analyzing a discussion unit from a Canadian court decision. "
        "Identify: (1) the PRIMARY legal ISSUE (one phrase like 'Standing' or 'Duty to Consult'), "
        "(2) a KEY PROPOSITION (one sentence stating the legal principle or outcome), "
        "(3) AUTHORITIES CITED (case names and statutes relevant to this issue). "
        f"{context_note}"
        f"{metadata_context}"
        "\n"
        "Return JSON with: issue_label (string), proposition (string), "
        "key_authorities (array of strings), confidence (0.0-1.0). "
        "Use only the supplied text; do not invent facts or citations."
    )

    user_content = f"DISCUSSION UNIT:\n\n{unit_text}"
    if preceding_unit:
        user_content = f"PRECEDING UNIT (context):\n{preceding_unit}\n\n" + user_content
    if following_unit:
        user_content = user_content + f"\n\nFOLLOWING UNIT (context):\n{following_unit}"

    return {
        "model": model,
        "budget_usd": budget_usd,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user_content},
        ],
    }
