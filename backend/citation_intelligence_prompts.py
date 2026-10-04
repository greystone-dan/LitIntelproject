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
