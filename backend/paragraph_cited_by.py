"""Paragraph-level "cited by" built from stored citation occurrences.

For every paragraph of a decision that other decisions cite by pinpoint, this answers:
which cases cite it, how often, and what signal phrase introduced the citation
("see also", "followed in", "distinguished", ...). It is a deterministic batch job over
rows already in the ``citations`` table plus the citing decision's own text: no AI, no
network, nothing typed by a user.

The signal phrase is what the citing judge wrote next to the citation. It is a reading
aid, not a verdict on whether the cited passage is still good law.

The batch is source-driven so each citing decision's text is read once. Results are
stored per (citing case, cited case, cited paragraph) and rewritten as a unit per citing
case, so a run can stop and resume at any point and re-running is harmless.
"""

from __future__ import annotations

import re
from bisect import bisect_right
from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from .citation_refine.pinpoints import target_paragraphs

ALGO_VERSION = 1

#: Display order, strongest signal first. "mentioned" means no signal phrase was found.
PURPOSES = ("disagreed", "distinguished", "followed", "quoted", "compared", "see", "mentioned")
PURPOSE_LABELS = {
    "disagreed": "Disagreed / declined to follow",
    "distinguished": "Distinguished",
    "followed": "Followed / applied",
    "quoted": "Quoted",
    "compared": "Compared (cf.)",
    "see": "See / see also",
    "mentioned": "Mentioned",
}

# (label, pattern). Matched against the text just before the citation; the match closest to
# the citation wins, ties go to the stronger label (PURPOSES order).
_SIGNAL_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = tuple(
    (label, re.compile(pattern, re.IGNORECASE))
    for label, pattern in (
        ("disagreed", r"\bbut\s+see\b|\bcontra\b|\bdeclin(?:e|ed|es|ing)\s+to\s+follow\b|\bnot\s+follow(?:ed|ing)?\b"
                      r"|\bdisagree(?:s|d)?\s+with\b|\boverrul(?:e|ed|es|ing)\b|\bno\s+longer\s+good\s+law\b|\bwrongly\s+decided\b"),
        ("distinguished", r"\bdistinguish(?:ed|es|ing|able)?\b|\bunlike\b|\bdiffers?\s+from\b|\bdifferent\s+from\b"),
        ("followed", r"\b(?:followed|applied|adopted|approved|endorsed|affirmed|confirmed|reiterated|restated|stated|held|noted"
                     r"|explained|set\s+out|described|developed|established|articulated|outlined)\s+(?:in|by|at)\b"
                     r"|\b(?:relied|rely|relying)\s+(?:on|upon)\b|\bconsistent\s+with\b|\bin\s+accordance\s+with\b"
                     r"|\bpursuant\s+to\b|\bbound\s+by\b"),
        ("compared", r"\bcf\.?(?=\s)|\bcompare\b"),
        ("see", r"\bsee\s+(?:also|generally|e\.g\.,?)\b|\bsee\b|\be\.g\.,?"),
    )
)
_QUOTE_BEFORE = re.compile(r"[”\"]\s*[,(\[]?\s*$")
# How far a signal phrase may sit from the citation, and what may not lie between them.
_MAX_TAIL = {"disagreed": 80, "distinguished": 80, "followed": 80, "compared": 30, "see": 30}
_BREAKS = re.compile(r"[;:!?]|(?<!\bv)(?<!\bMr)(?<!\bMs)(?<!\bMrs)(?<!\bDr)(?<!\bInc)(?<!\bLtd)(?<!\bc)(?<!\bNo)\.\s")
_WINDOW = 150


def citation_target_paragraph(
    citation_text: str | None,
    normalized_citation: str | None,
    stored_target_paragraph: int | None = None,
) -> int | None:
    """The first cited paragraph: the stored pinpoint, else one written in the citation text."""
    pins = target_paragraphs(citation_text, normalized_citation, stored_target_paragraph)
    return pins.first if pins is not None else None


def signal_window(text: str, start: int, previous_end: int = 0, limit: int = _WINDOW) -> str:
    """Text immediately before a citation: back to the previous citation, a line break or ``limit``."""
    begin = max(0, previous_end, start - limit)
    window = text[begin:start]
    newline = window.rfind("\n")
    return window[newline + 1:] if newline >= 0 else window


def classify_signal(window: str) -> tuple[str, str | None]:
    """Return ``(purpose, phrase)`` for the text before a citation; ``phrase`` is what matched."""
    best: tuple[int, int, str, str] | None = None  # (end, -strength, label, phrase)
    for strength, (label, pattern) in enumerate(_SIGNAL_PATTERNS):
        for match in pattern.finditer(window):
            tail = window[match.end():]
            if len(tail) > _MAX_TAIL[label] or _BREAKS.search(tail):
                continue  # a clause or sentence break sits between the phrase and the citation
            candidate = (match.end(), -strength, label, match.group(0).strip().lower())
            if best is None or candidate[:2] > best[:2]:
                best = candidate
    if _QUOTE_BEFORE.search(window) and (best is None or best[2] in {"see", "compared"}):
        return "quoted", None
    if best is None:
        return "mentioned", None
    return best[2], best[3][:40]


@dataclass(frozen=True)
class Occurrence:
    target_case_id: int
    target_paragraph: int
    start: int  # absolute offset in the citing decision's text
    end: int


@dataclass(frozen=True)
class Edge:
    target_case_id: int
    target_paragraph: int
    mentions: int
    purpose: str
    purpose_counts: dict[str, int]
    signal: str | None


def dominant_purpose(counts: Mapping[str, int]) -> str:
    """Most frequent real signal; "mentioned" only when nothing else was seen. Ties: stronger label."""
    real = {label: n for label, n in counts.items() if label != "mentioned" and n > 0}
    pool = real or {label: n for label, n in counts.items() if n > 0}
    if not pool:
        return "mentioned"
    return min(pool, key=lambda label: (-pool[label], PURPOSES.index(label) if label in PURPOSES else len(PURPOSES)))


def build_edges(text: str, occurrences: Iterable[Occurrence], all_spans: Sequence[tuple[int, int]] = ()) -> list[Edge]:
    """Aggregate one citing decision's citations of other decisions into edges.

    ``all_spans`` are every citation span in the text (including statutes and unresolved ones) so the
    signal window of one citation never reads the previous citation as its own signal phrase.
    """
    unique = sorted({(o.start, o.end, o.target_case_id, o.target_paragraph) for o in occurrences})
    end_list = sorted({e for _, e in all_spans} | {e for _, e, _, _ in unique})
    groups: dict[tuple[int, int], list[tuple[str, str | None]]] = defaultdict(list)
    for start, end, target, paragraph in unique:
        index = bisect_right(end_list, start) - 1
        previous_end = end_list[index] if index >= 0 else 0
        groups[(target, paragraph)].append(classify_signal(signal_window(text, start, previous_end)))
    edges = []
    for (target, paragraph), signals in sorted(groups.items()):
        counts = Counter(label for label, _ in signals)
        purpose = dominant_purpose(counts)
        phrase = next((p for label, p in signals if label == purpose and p), None)
        edges.append(Edge(target, paragraph, len(signals), purpose, dict(counts), phrase))
    return edges


def summarise_purposes(rows: Iterable[Mapping[str, int]]) -> dict[str, int]:
    """Sum purpose_counts across edges, in display order."""
    total: Counter[str] = Counter()
    for counts in rows:
        total.update(counts or {})
    return {label: total[label] for label in PURPOSES if total.get(label)}


def citer_sort_key(row: Mapping[str, Any]) -> tuple:
    """Strongest signal, then most mentions, then newest decision first."""
    purpose = row.get("purpose") or "mentioned"
    strength = PURPOSES.index(purpose) if purpose in PURPOSES else len(PURPOSES)
    return (-int(row.get("mentions") or 0), strength, -(row.get("date_ordinal") or 0))
