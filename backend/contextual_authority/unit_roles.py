"""Deterministic role labels for discussion units (no AI).

Each unit gets one of six coarse roles, in the order they usually appear in a
Federal Court judgment:

    metadata     header or footer block (style of cause, solicitors of record)
    overview     opening paragraphs saying what the application is and how it ends
    facts        background, procedural history and the decision under review
    issues       statement of the issues and the standard of review
    analysis     the court's reasoning
    disposition  conclusion, certified questions and the formal order

The rules read only the unit's text and its position in the case.
"""

from __future__ import annotations

import re
from typing import Sequence

ROLE_CLASSES = ("metadata", "overview", "facts", "issues", "analysis", "disposition")

_FOOTER_RE = re.compile(r"SOLICITORS OF RECORD|STYLE OF CAUSE|PLACE OF HEARING|DATE OF HEARING|APPEARANCES", re.I)
_ORDER_RE = re.compile(
    r"THIS COURT(?:'|’)?S? (?:ORDERS|JUDGMENT)|IT IS (?:THE JUDGMENT|ORDERED)|^\s*(?:JUDGMENT|ORDER)\b", re.I | re.M
)
_OUTCOME_RE = re.compile(
    r"\b(?:application|appeal)\b[^.]{0,80}\b(?:is|are|will be|must be|should be|be)\s+(?:therefore\s+|accordingly\s+)?"
    r"(?:allowed|granted|dismissed)|\bfor (?:all )?(?:these|the foregoing|the above) reasons\b|\bin the result\b"
    r"|\bcertif(?:y|ied|ication)\b[^.]{0,60}\bquestion|\bI (?:therefore |accordingly )?conclude\b|\bin conclusion\b",
    re.I,
)
_CONCLUSION_HEAD_RE = re.compile(r"^\s*(?:[IVX]+\.\s*)?(?:conclusion|disposition)\b", re.I)
_OVERVIEW_RE = re.compile(
    r"\b(?:seeks?|seeking|for) (?:leave and )?judicial review\b|\bapplication for judicial review\b|\bappeals? (?:from|against)\b"
    r"|\bfor the (?:following )?reasons (?:that follow|below|set out)\b|^\s*(?:[IVX]+\.\s*)?(?:overview|introduction)\b",
    re.I | re.M,
)
_ISSUES_RE = re.compile(
    r"^\s*(?:\[\d+\]\s*)?(?:[IVX]+\.\s*|[A-Z]\.\s*)?(?:issues?|standard of review)\b|\bstandard of review\b"
    r"|\b(?:the|two|three|following|sole|only|primary|main) issues?\b[^.]{0,40}\b(?:is|are|raised?|whether)\b|\braises? (?:\w+ ){0,3}issues?\b",
    re.I | re.M,
)
_FACTS_RE = re.compile(
    r"^\s*(?:\[\d+\]\s*)?(?:[IVX]+\.\s*)?(?:background|facts|the facts|factual background|decision under review|the decision)\b"
    r"|\bcitizen of\b|\bwas born\b|\barrived in canada\b|\bclaimed (?:refugee )?protection\b|\bin (?:january|february|march|april|may|june|july|august|september|october|november|december) \d{4}\b"
    r"|\bthe (?:RAD|RPD|IAD|ID|Board|officer|Officer|panel|Member|Tribunal|delegate)\b[^.]{0,40}\b(?:found|concluded|determined|held|rejected|refused|noted)\b",
    re.I | re.M,
)
_ANALYSIS_RE = re.compile(
    r"\b(?:I (?:find|agree|disagree|am (?:not )?(?:satisfied|persuaded))|in my view|it was (?:not )?unreasonable|was (?:not )?reasonable)\b",
    re.I,
)


def _first(texts: Sequence[str], count: int = 2) -> str:
    return "\n".join(texts[:count])


def label_unit_roles(units: Sequence[Sequence[str]]) -> list[str]:
    """Return one role per unit. ``units`` lists each unit's paragraph texts, in case order."""
    total = sum(len(unit) for unit in units) or 1
    roles: list[str] = []
    seen_analysis = False
    position = 0
    for unit_index, texts in enumerate(units):
        start = position / total
        position += len(texts)
        head = _first(texts)
        opening = texts[0] if texts else ""
        if start > 0.5 and _ORDER_RE.search(opening[:200]):
            role = "disposition"
        elif _FOOTER_RE.search(opening) and start > 0.5:
            role = "metadata"
        elif unit_index == 0 and len(texts) == 1 and not re.search(r"\[\d+\]", opening):
            role = "metadata"
        elif start > 0.5 and (_OUTCOME_RE.search(opening) or _CONCLUSION_HEAD_RE.search(opening)):
            role = "disposition"
        elif start < 0.15 and _OVERVIEW_RE.search(head):
            role = "overview"
        elif start < 0.5 and _ISSUES_RE.search(opening[:160]):
            role = "issues"
        elif not seen_analysis and _FACTS_RE.search(head) and not _ANALYSIS_RE.search(opening):
            role = "facts"
        elif start < 0.1:
            role = "overview"
        else:
            role = "analysis"
        if role in ("issues", "analysis"):
            seen_analysis = True
        roles.append(role)
    return roles
