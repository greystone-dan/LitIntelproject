"""Deterministic reader formatting for stored decision text.

``format_decision`` classifies the lines of ``Case.full_text`` into typed blocks.
It never edits text: every block is a ``[start, end)`` code-point range into the
original string (the same offsets citations, tags and discussion units use), so
the reader can render structure while the intelligence layers stay aligned.
"""

from __future__ import annotations

import re
from typing import Any, Mapping

DECISION_MARKER = "Decision Content"

_ROLE_RE = re.compile(
    r"^(?:Applicants?|Respondents?|Appellants?|Plaintiffs?|Defendants?|Intervener|Interveners|"
    r"Petitioners?|Moving Party|Responding Party)(?:\s*\(.*\))?$",
    re.IGNORECASE,
)
_CONNECTOR_RE = re.compile(r"^(?:BETWEEN:?|and|v\.?|‑ and ‑|- and -)$", re.IGNORECASE)
_DOCTITLE_RE = re.compile(
    r"^(?:(?:JUDGMENT|REASONS|ORDER|DIRECTION|AMENDED)[A-Z ,]*|REASONS FOR (?:JUDGMENT|ORDER|ASSESSMENT)[A-Z ,]*)$"
)
_PARA_RE = re.compile(r"^\[(\d{1,3})\]\s+(?=\S)")
_GLUED_PARA_RE = re.compile(r"^(?P<head>(?:[IVX]+|[A-Z]|\d{1,2})\.\s+\S.{0,160}?)\s+(?P<mark>\[(?P<n>\d{1,3})\])\s+(?=\S)")
_HEADING_RE = re.compile(r"^(?P<label>[IVX]+|[A-Z]|\d{1,2})\.\s+(?P<title>[A-Z][^\n]{1,160})$")
_UPPER_HEADING_RE = re.compile(r"^[A-Z][A-Z0-9 ,;:&’'()/\-]{3,80}$")
_LISTITEM_RE = re.compile(r"^(?:\([a-z]{1,3}\)|\([ivx]{1,5}\)|\(\d{1,2}\)|\d{1,2}\))\s+\S")
_FOOTER_START_RE = re.compile(r"^(?:(?:NAMES OF COUNSEL AND )?SOLICITORS OF RECORD|APPEARANCES):?$")
_COUNSEL_START_RE = re.compile(r"^(?:Solicitors?|Attorneys?|Counsel|Appeal (?:allowed|dismissed)|Judgment accordingly)", re.IGNORECASE)
_BARE_PARA_RE = re.compile(r"^(\d{1,3})\s+(?=\S)")
_FOOTNOTE_RE = re.compile(r"^\[(\d{1,3})\]\s+(?=\S)")
_SIGNATURE_RE = re.compile(
    r"^(?:[A-ZÀ-Ý][A-ZÀ-Ý'’ .\-]{2,40} (?:J\.A\.|J\.|C\.J\.|C\.J\.C\.|P\.)|J\.A\.|J\.|Judge|Prothonotary|Justice|Juge|Assessment Officer)$"
)
_SIGNED_NAME_RE = re.compile(r'^[“"][A-Z][^“”"]{3,60}[”"]$')
_COURTLINE_START_RE = re.compile(
    r"^(?:Heard at|Judgment delivered|Reasons for judgment|REASONS FOR JUDGMENT|Concurred in by|Dissenting reasons|Certified true translation|Date:|Docket:)",
    re.IGNORECASE,
)
_PLAIN_HEADING_RE = re.compile(
    r"^(?:Analysis(?: and decision)?|Conclusion|Background|Issues?|Facts|Overview|Introduction|Decision|Disposition|Standard of review|Relevant legislation|Costs?)$",
    re.IGNORECASE,
)
_OPERATIVE_RE = re.compile(r"^(?:THIS COURT[’']S (?:JUDGMENT|ORDER)(?: is)?(?: that)?:?|JUDGMENT|ORDER)$")
_QUOTE_FILLER_RE = re.compile(r"^(?:\[…\]|…|\.\.\.|\[Emphasis (?:added\.?|in original\.?)\]|\[footnotes? omitted\]|\[Citations? omitted\])$", re.IGNORECASE)
_NOTE_SHAPE_RE = re.compile(r"^\[(\d{1,3})\]\s+(?:\(\d{4}\)|\[\d{4}\]|\d{1,3}\s+[A-Z][A-Za-z.]*\s)")
_ROMAN = {"I", "V", "X"}
_NON_HEADING_UPPER = {"SOLICITORS OF RECORD", "APPEARANCES"}


def _lines(text: str) -> list[tuple[int, int, str]]:
    out: list[tuple[int, int, str]] = []
    pos = 0
    for raw in text.split("\n"):
        out.append((pos, pos + len(raw), raw))
        pos += len(raw) + 1
    return out


def _block(kind: str, start: int, end: int, **extra: Any) -> dict[str, Any]:
    row: dict[str, Any] = {"type": kind, "start": start, "end": end}
    row.update({key: value for key, value in extra.items() if value is not None})
    return row


def _heading_level(label: str) -> int:
    if label.isdigit():
        return 3
    if len(label) == 1 and label not in _ROMAN:
        return 2
    return 1


def format_decision(
    text: str | None, cited_paragraph_counts: Mapping[int, int] | None = None
) -> list[dict[str, Any]]:
    """Return ordered, non-overlapping typed blocks covering the non-blank lines of ``text``."""
    if not text:
        return []
    lines = _lines(text)
    marker = next((i for i, (_, _, raw) in enumerate(lines) if raw.strip() == DECISION_MARKER), None)
    blocks: list[dict[str, Any]] = []
    body_from = 0
    if marker is not None:
        header_end = lines[marker][1]
        if header_end > 0:
            blocks.append(_block("meta", 0, header_end))
        body_from = marker + 1

    footer_from = len(lines)
    court_footer = [
        i
        for i in range(body_from, len(lines) - 1)
        if re.match(r"^FEDERAL COURT(?: OF APPEAL)?$", lines[i][2].strip())
        and _FOOTER_START_RE.match(lines[i + 1][2].strip())
    ]
    if court_footer:
        footer_from = court_footer[-1]
    else:
        for i in range(len(lines) - 1, body_from - 1, -1):
            if _FOOTER_START_RE.match(lines[i][2].strip()):
                footer_from = i
                break
    in_counsel = False
    first_para_seen = False
    last_num = 0
    for i in range(body_from, len(lines)):
        start, end, raw = lines[i]
        stripped = raw.strip()
        if not stripped:
            continue
        if i >= footer_from:
            blocks.append(_block("footer", start, end))
            continue
        glued = _GLUED_PARA_RE.match(raw)
        if glued:
            label = glued.group("head")
            hm = _HEADING_RE.match(label)
            if hm:
                head_end = start + len(glued.group("head"))
                blocks.append(_block("heading", start, head_end, level=_heading_level(hm.group("label"))))
                mark_start = start + glued.start("mark")
                blocks.append(
                    _block("para", mark_start, end, num=int(glued.group("n")), mark_end=mark_start + len(glued.group("mark")))
                )
                first_para_seen = True
                continue
        para = _PARA_RE.match(raw)
        if para and len(raw) <= 120 and _NOTE_SHAPE_RE.match(raw):
            blocks.append(_block("footnote", start, end, num=int(para.group(1))))
            continue
        if para and not in_counsel:
            first_para_seen = True
            last_num = int(para.group(1))
            blocks.append(_block("para", start, end, num=last_num, mark_end=start + len(para.group(0).rstrip())))
            continue
        bare = _BARE_PARA_RE.match(raw)
        # Modern SCC reasons number paragraphs without brackets; only trust the next number in sequence.
        if bare and not in_counsel and int(bare.group(1)) == last_num + 1 and marker is not None:
            first_para_seen = True
            last_num += 1
            blocks.append(_block("para", start, end, num=last_num, mark_end=start + len(bare.group(1))))
            continue
        if in_counsel and _FOOTNOTE_RE.match(raw):
            blocks.append(_block("footnote", start, end, num=int(_FOOTNOTE_RE.match(raw).group(1))))
            continue
        if stripped.lower().startswith("solicitors for") and not _PARA_RE.match(raw):
            in_counsel = True
            blocks.append(_block("footer", start, end))
            continue
        if in_counsel:
            blocks.append(_block("footer", start, end))
            continue
        if not first_para_seen:
            if _DOCTITLE_RE.match(stripped):
                blocks.append(_block("doctitle", start, end))
            elif _ROLE_RE.match(stripped):
                blocks.append(_block("role", start, end))
            elif _CONNECTOR_RE.match(stripped):
                blocks.append(_block("connector", start, end))
            elif _SIGNATURE_RE.match(stripped) or _COURTLINE_START_RE.match(stripped):
                blocks.append(_block("courtline", start, end))
            elif re.match(r"^(?:Date|Docket|Citation|Neutral citation|File No\.?|Present|PRESENT|Coram|CORAM):", stripped) or re.match(
                r"^(?:Ottawa|Toronto|Montréal|Montreal|Vancouver|Calgary|Winnipeg|Halifax|Edmonton|Quebec|Québec),\s", stripped
            ):
                blocks.append(_block("courtline", start, end))
            else:
                hm = _HEADING_RE.match(stripped)
                if hm and not stripped.endswith("."):
                    blocks.append(_block("heading", start, end, level=_heading_level(hm.group("label"))))
                elif _UPPER_HEADING_RE.match(stripped) and stripped not in _NON_HEADING_UPPER and len(stripped.split()) <= 8:
                    blocks.append(_block("caption", start, end))
                else:
                    blocks.append(_block("text", start, end))
            continue
        prev = blocks[-1]["type"] if blocks else None
        if _SIGNATURE_RE.match(stripped) or (_SIGNED_NAME_RE.match(stripped) and len(stripped) < 50):
            blocks.append(_block("signature", start, end))
        elif _COURTLINE_START_RE.match(stripped):
            blocks.append(_block("courtline", start, end))
        elif _OPERATIVE_RE.match(stripped) or _PLAIN_HEADING_RE.match(stripped):
            blocks.append(_block("heading", start, end, level=1))
        elif _QUOTE_FILLER_RE.match(stripped) and prev in ("quote", "text", "para"):
            blocks.append(_block("quote", start, end))
        elif stripped[0] in "“\"" and len(stripped) >= 80:
            blocks.append(_block("quote", start, end))
        else:
            hm = _HEADING_RE.match(stripped)
            if hm and not stripped.endswith((".", ",", ";", ":")):
                blocks.append(_block("heading", start, end, level=_heading_level(hm.group("label"))))
            elif _UPPER_HEADING_RE.match(stripped) and stripped not in _NON_HEADING_UPPER and len(stripped.split()) <= 8:
                blocks.append(_block("heading", start, end, level=1))
            elif _LISTITEM_RE.match(stripped):
                blocks.append(_block("listitem", start, end))
            else:
                blocks.append(_block("text", start, end))
    for block in blocks:
        if block["type"] != "para":
            continue
        count = int((cited_paragraph_counts or {}).get(block["num"], 0))
        if count > 0:
            block["cited_by_count"] = count
            block["citation_tooltip"] = f"Cited by {count} case{'s' if count != 1 else ''}"
    return blocks
