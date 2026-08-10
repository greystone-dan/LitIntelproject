from __future__ import annotations

import re
from typing import Callable

from .models import CitationCandidate


RuleFn = Callable[[str], list[CitationCandidate]]


def _norm(value: str) -> str:
    return " ".join((value or "").split()).strip()


def _mk(kind: str, text: str, normalized: str, start: int, end: int, confidence: float, source_rule: str) -> CitationCandidate:
    return CitationCandidate(
        kind=kind,
        citation_text=text,
        normalized_citation=normalized,
        offset_start=start,
        offset_end=end,
        confidence=confidence,
        source_rule=source_rule,
    )


RE_NEUTRAL = re.compile(r"\b((?:19|20)\d{2})\s+(FC|FCA|SCC|CanLII)\s+(\d{1,7})\b", re.IGNORECASE)
RE_SCR = re.compile(
    r"\[(19|20)\d{2}\]\s*\d+\s*S\.?C\.?R\.?\s*\d+(?:,\s*at\s*(?:p{1,2}\.\s*\d+(?:\s*[-–]\s*\d+)?|para(?:s)?\.\s*\d+(?:\s*[-–]\s*\d+)?(?:\s*(?:,|and|or)\s*\d+(?:\s*[-–]\s*\d+)?)*))?",
    re.IGNORECASE,
)
RE_SHORT_AUTH = re.compile(
    r"\b([A-Z][A-Za-z'\-.]+(?:\s+[A-Z][A-Za-z'\-.]+){0,4}),\s+at\s+para(?:s)?\.?\s+\d+(?:\s*[-–]\s*\d+)?(?:\s*(?:,|and|or)\s*\d+(?:\s*[-–]\s*\d+)?)*",
    re.IGNORECASE,
)
RE_CASE_NAME = re.compile(
    r"\b([A-Z][A-Za-z'’\-&,()\[\]. ]{1,120}?\s+v\.?\s+[A-Z][A-Za-z'’\-&,()\[\]. ]{1,120}?)(?=[,.;)\]]|\s|$)",
    re.IGNORECASE,
)
RE_IRPA_SECTION = re.compile(
    r"\b(IRPA|IRPR)\s*,?\s*ss?\.\s*((?:\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)(?:(?:(?:\s*,\s*(?:and|or)?\s*)|(?:\s+(?:and|or|to)\s+)|(?:\s*[-–]\s*))(?:\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*))+)",
    re.IGNORECASE,
)
RE_GENERIC_STATUTE = re.compile(
    r"\b([A-Z][A-Za-z'’\-]+(?:\s+[A-Z][A-Za-z'’\-]+|\s+(?:of|and|the|for|de|du|des|la|le|les)){0,10}\s+(?:Act|Code|Regulations?)(?:,\s*(?:R\.?S\.?C\.?|S\.?C\.?)\s*,?\s*\d{4},\s*c\.?\s*[A-Z0-9.-]+)?)\b",
    re.IGNORECASE,
)
RE_REFUGEE_ART = re.compile(r"\b(?:art\.|article)\s*(1[EF])(?:\s*\(\s*([A-Fa-f])\s*\)|\s*([A-Fa-f]))?(?!\w)", re.IGNORECASE)
RE_REFUGEE_ART_33 = re.compile(r"\b(?:art\.|article)\s*(33(?:\s*\(\s*\d+\s*\))?)(?!\w)", re.IGNORECASE)
RE_ARTICLE_LIST = re.compile(
    r"\barticles?\s+(\d{1,3}(?:\s*(?:,|and|or|to|-|–)\s*\d{1,3})+)\s+of\s+(?:the\s+)?(Vienna Convention on the Law of Treaties|Convention Relating to the Status of Refugees|Refugee Convention)\b",
    re.IGNORECASE,
)


def _norm_sections(v: str) -> str:
    t = _norm(v).replace("–", "-")
    t = re.sub(r",\s*(?:and|or)\s+", ", ", t, flags=re.IGNORECASE)
    t = re.sub(r"\b(?:and|or)\b", ",", t, flags=re.IGNORECASE)
    t = re.sub(r"\s*,\s*", ", ", t)
    t = re.sub(r"\s*\bto\b\s*", " to ", t, flags=re.IGNORECASE)
    t = re.sub(r"\s*\-\s*", "-", t)
    return re.sub(r"\s+", " ", t).strip(" ,")


def _rule_neutral(text: str) -> list[CitationCandidate]:
    out: list[CitationCandidate] = []
    for m in RE_NEUTRAL.finditer(text):
        yr, ct, num = m.groups()
        out.append(_mk("neutral", m.group(0), f"{yr} {ct.upper()} {int(num)}", m.start(), m.end(), 0.95, "neutral"))
    return out


def _rule_scr(text: str) -> list[CitationCandidate]:
    return [_mk("secondary", m.group(0), _norm(m.group(0)).replace("–", "-"), m.start(), m.end(), 0.9, "scr_pinpoint") for m in RE_SCR.finditer(text)]


def _rule_short_authority(text: str) -> list[CitationCandidate]:
    out: list[CitationCandidate] = []
    for m in RE_SHORT_AUTH.finditer(text):
        normalized = _norm(m.group(0)).replace("–", "-")
        normalized = re.sub(r"^(?:and|or)\s+", "", normalized, flags=re.IGNORECASE)
        out.append(_mk("secondary", m.group(0), normalized, m.start(), m.end(), 0.68, "short_authority"))
    return out


def _rule_case_name(text: str) -> list[CitationCandidate]:
    out: list[CitationCandidate] = []
    for m in RE_CASE_NAME.finditer(text):
        normalized = _norm(m.group(1))
        normalized = re.sub(r"\bv\s*\.?\s+", " v. ", normalized, flags=re.IGNORECASE)
        out.append(_mk("case_name", m.group(1), normalized, m.start(1), m.end(1), 0.75, "case_name"))
    return out


def _rule_irpa(text: str) -> list[CitationCandidate]:
    out: list[CitationCandidate] = []
    for m in RE_IRPA_SECTION.finditer(text):
        statute, section_list = m.groups()
        base = "Immigration and Refugee Protection Act, S.C. 2001, c. 27" if statute.upper() == "IRPA" else "Immigration and Refugee Protection Regulations, SOR/2002-227"
        out.append(_mk("statute", m.group(0), f"{base} ss. {_norm_sections(section_list)}", m.start(), m.end(), 0.92, "irpa_sections"))
    return out


def _rule_generic_statute(text: str) -> list[CitationCandidate]:
    out: list[CitationCandidate] = []
    for m in RE_GENERIC_STATUTE.finditer(text):
        normalized = _norm(m.group(1))
        normalized = re.sub(r"\b(R\.?S\.?C\.?|S\.?C\.?)\s*,\s*(\d{4})\b", r"\1 \2", normalized, flags=re.IGNORECASE)
        out.append(_mk("statute", m.group(1), normalized, m.start(1), m.end(1), 0.7, "generic_statute"))
    return out


def _rule_refugee_articles(text: str) -> list[CitationCandidate]:
    out: list[CitationCandidate] = []
    for m in RE_REFUGEE_ART.finditer(text):
        base, paren_letter, suffix_letter = m.groups()
        letter = (paren_letter or suffix_letter or "").strip().lower()
        norm = f"art. {base.upper()}({letter}) of Refugee Convention" if letter else f"art. {base.upper()} of Refugee Convention"
        out.append(_mk("instrument", m.group(0), norm, m.start(), m.end(), 0.9, "refugee_article"))
    for m in RE_REFUGEE_ART_33.finditer(text):
        v = re.sub(r"\s+", "", _norm(m.group(1)))
        out.append(_mk("instrument", m.group(0), f"art. {v} of Refugee Convention", m.start(), m.end(), 0.9, "refugee_article_33"))
    return out


def _rule_article_lists(text: str) -> list[CitationCandidate]:
    out: list[CitationCandidate] = []
    for m in RE_ARTICLE_LIST.finditer(text):
        nums, conv = m.groups()
        nums_norm = _norm_sections(nums)
        name = "Refugee Convention" if re.search(r"refugee", conv, re.IGNORECASE) else "Vienna Convention on the Law of Treaties"
        out.append(_mk("instrument", m.group(0), f"arts. {nums_norm} of {name}", m.start(), m.end(), 0.86, "article_list"))
    return out


def default_rules() -> list[RuleFn]:
    return [
        _rule_neutral,
        _rule_scr,
        _rule_refugee_articles,
        _rule_article_lists,
        _rule_irpa,
        _rule_generic_statute,
        _rule_case_name,
        _rule_short_authority,
    ]
