"""Shared recognition of paragraph markers that the line-start pattern ``[n] text`` misses.

Decision text sometimes puts the marker after a heading on the same line ("Issue [19]",
"(i) Textual Analysis [45]"), alone on its line ("[14]" with the text on the next line), or
glued to the text ("[97]Dr. Grover"). A bracketed number is only trusted when it is the next
expected paragraph number (or a plausible near jump), so cross-references such as
"see paragraph [5] of Dunsmuir" or "[2019] 4 SCR" are not mistaken for paragraphs.
"""

from __future__ import annotations

import re
from typing import NamedTuple

MAX_GAP = 3
MAX_HEAD_CHARS = 200
MAX_HEAD_WORDS = 30

_MARK_RE = re.compile(r"\[(\d{1,3})\](?=\s|$)")
_ACRONYM_RE = re.compile(r"\[[A-Za-z]{2,6}\]")
_ALONE_RE = re.compile(r"^\[(\d{1,3})\]\s*$")
_NOSPACE_RE = re.compile(r"^\[(\d{1,3})\](?=[A-Za-z“\"(])")
# Words that make "<word> [n]" a cross-reference rather than a heading.
_XREF_WORDS = {"paragraph", "paragraphs", "para", "paras", "at", "see", "and", "to", "in", "of", "at", "para.", "paras.", "or", "by", "from", "under"}


class Marker(NamedTuple):
    num: int
    head_end: int  # end of the heading text before the marker (0 when there is none)
    mark_start: int
    mark_end: int


def plausible(num: int, last: int, top: int | None = None) -> bool:
    """``num`` follows ``last`` (the previous paragraph) or ``top`` (the highest so far; a mistyped number must not stall the walk)."""
    return any(base < num <= base + MAX_GAP for base in (last, last if top is None else top))


def _heading_like(head: str) -> bool:
    head = _ACRONYM_RE.sub("", head).strip()  # "Internal Flight Alternative [IFA] [22]"
    if not head or len(head) > MAX_HEAD_CHARS or "[" in head or "]" in head:
        return False
    if head.endswith((".", ",", ";", ":", "!")):
        return False
    words = head.split()
    if len(words) > MAX_HEAD_WORDS or words[-1].lower() in _XREF_WORDS:
        return False
    return True


def find_marker(line: str, last: int, top: int | None = None) -> Marker | None:
    """The paragraph marker of ``line`` that is not at its start in the usual ``[n] text`` form.

    ``last`` is the number of the previous paragraph, ``top`` the highest so far. Returns offsets into ``line``; ``None``
    when the line holds no plausible marker (a normal ``[n] text`` line also returns ``None``).
    """
    m = _ALONE_RE.match(line)
    if m and plausible(int(m.group(1)), last, top):
        return Marker(int(m.group(1)), 0, line.index("["), line.index("]") + 1)
    m = _NOSPACE_RE.match(line)
    if m and plausible(int(m.group(1)), last, top):
        return Marker(int(m.group(1)), 0, 0, m.end())
    for m in _MARK_RE.finditer(line):
        if m.start() == 0:
            return None
        num = int(m.group(1))
        if plausible(num, last, top) and _heading_like(line[: m.start()]):
            head_end = len(line[: m.start()].rstrip())
            return Marker(num, head_end, m.start(), m.end())
        return None
    return None
