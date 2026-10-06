"""Deterministic "what was the claim decided on" labels for refugee-protection decisions.

Two approaches are kept side by side so they can be compared on real decisions:
  * ``issues_by_counts``: which issue vocabulary the whole decision leans on.
  * ``issues_by_anchor``: which issue the court itself calls determinative or central, falling back to counts.
No model of any kind is used.
"""

from __future__ import annotations

import re
from collections import Counter

ISSUE_CUES: dict[str, tuple[str, ...]] = {
    "credibility": (r"credib", r"inconsisten", r"omission", r"embellish", r"implausib", r"not believe", r"adverse (?:credibility )?finding"),
    "state_protection": (r"state protection", r"adequate (?:state )?protection", r"operational adequacy", r"presumption of state protection",
                         r"protection de l['’]État"),
    "internal_flight_alternative": (r"internal flight", r"\bIFA\b", r"viable (?:flight|relocation)", r"possibilité de refuge intérieur", r"\bPRI\b"),
    "nexus_convention_ground": (r"\bnexus\b", r"convention ground", r"particular social group", r"political opinion",
                                r"persecution for reasons", r"generalized (?:risk|violence)", r"personalized risk", r"section 97\(1\)\(b\)"),
    "identity": (r"\bidentity\b", r"identity documents?", r"genuineness of (?:the|his|her) (?:passport|documents?)", r"\bpassport\b"),
    "subjective_fear_delay": (r"subjective fear", r"\bdelay\b", r"failure to claim", r"did not claim (?:in|at|asylum)", r"re-?availment", r"crainte subjective"),
    "sur_place": (r"sur place",),
    "procedural_fairness": (r"procedural fairness", r"natural justice", r"reasonable apprehension of bias", r"duty of fairness", r"right to be heard",
                            r"équité procédurale"),
    "new_evidence_rad": (r"new evidence", r"subsection 110\(4\)", r"nouveaux éléments de preuve", r"Singh v\.? Canada[^.]{0,40}2016 FCA 96"),
    "jurisdiction_or_process": (r"credible basis", r"manifestly unfounded", r"abandon(?:ed|ment)", r"reinstate", r"change of (?:counsel|venue)"),
}
_COMPILED = {issue: tuple(re.compile(cue, re.IGNORECASE) for cue in cues) for issue, cues in ISSUE_CUES.items()}
ANCHOR_RE = re.compile(
    r"[^.\n]{0,220}\b(?:determinative|dispositive|central (?:issue|question)|key (?:issue|question)|main (?:issue|concern)|crux|"
    r"decisive|determining factor|déterminant|question (?:centrale|déterminante))\b[^.\n]{0,260}",
    re.IGNORECASE,
)
MIN_COUNT = 4
SECONDARY_FRACTION = 0.5


def _counts(text: str) -> Counter:
    counts: Counter = Counter()
    for issue, patterns in _COMPILED.items():
        counts[issue] = sum(len(pattern.findall(text)) for pattern in patterns)
    return counts


def issues_by_counts(text: str, *, limit: int = 3) -> list[str]:
    counts = _counts(text)
    ranked = [(issue, count) for issue, count in counts.most_common() if count >= MIN_COUNT]
    if not ranked:
        return []
    top = ranked[0][1]
    return [issue for issue, count in ranked if count >= SECONDARY_FRACTION * top][:limit]


def anchor_sentences(text: str, *, limit: int = 4) -> list[str]:
    return [" ".join(match.group(0).split()) for match in ANCHOR_RE.finditer(text)][:limit]


def issues_by_anchor(text: str, *, limit: int = 2) -> list[str]:
    """Issues named in the court's own 'determinative / central issue' sentences.

    Empty when the decision states none: word counts alone label almost everything "credibility", so they are
    not stored as a result (see issues_by_counts for experiments).
    """
    found: Counter = Counter()
    for sentence in anchor_sentences(text, limit=6):
        counts = _counts(sentence)
        for issue, count in counts.items():
            if count:
                found[issue] += count
    if found:
        return [issue for issue, _ in found.most_common(limit)]
    return []
