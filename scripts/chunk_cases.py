"""Create resumable text chunks for canonical cases without embedding calls."""

from __future__ import annotations

import argparse
import csv
import logging
import re
import sys
from hashlib import sha256
from pathlib import Path

from sqlalchemy import delete, exists, func, or_, select
from sqlalchemy.orm import Session

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseChunk, SessionLocal
from backend.case_formatter import format_decision
from backend.document_structure import map_to_canonical_text, structure_source_html

CHUNK_CHARS = 6000
OVERLAP_CHARS = 600
CHUNK_SET_LEGACY = "legacy"
CHUNK_SET_FULL_CASE = "full_case"
CHUNK_SET_SECTION = "section"
CHUNK_SET_PARAGRAPH = "paragraph"
SECTION_HEADINGS = ("OVERVIEW", "BACKGROUND", "ANALYSIS", "CONCLUSION")
PARAGRAPH_MARKER_RE = re.compile(r"(?m)^[ \t]*\[(\d+)\]")
SCC_PARAGRAPH_MARKER_RE = re.compile(r"(?m)^[ \t]*(\d+)(?:[.)])?[ \t]+")
SCC_TEXT_PARAGRAPH_RE = re.compile(
    r"(?m)^[ \t]*(?:\[(\d{1,4})\]|(\d{1,4})(?:[.)])?)[ \t]+(?=[A-Z\[])"
)
SCC_TEXT_SECTION_RE = re.compile(r"(?mi)^\s*([IVXLC]{1,8})\.\s+([^\n]{3,160})\s*$")
SCC_BODY_START_RE = re.compile(
    r"(?mi)^\s*(?://The Court//|The judgment of the Court was delivered by|The following is the judgment delivered by)\s*$"
)
SCC_OUTRO_HEADING_RE = re.compile(r"(?mi)^\s*SOLICITORS?\s+FOR\b.*$")
SECTION_HEADING_RE = re.compile(
    r"(?mi)^\s*(?:[IVXLC]+\.\s+)?(OVERVIEW|BACKGROUND(?:\s+FACTS)?|ANALYSIS|CONCLUSION|INTRODUCTION|STANDARD OF REVIEW|ORDER|REASONS? AND ORDER)\b.*$"
)
OUTRO_HEADING_RE = re.compile(
    r"(?mi)^\s*(SOLICITORS OF RECORD|APPEARANCES|WRITTEN REPRESENTATIONS BY|STYLE OF CAUSE)\s*:?.*$"
)

logger = logging.getLogger(__name__)


def split_text(
    text: str,
    *,
    chunk_chars: int = CHUNK_CHARS,
    overlap_chars: int = OVERLAP_CHARS,
) -> list[str]:
    if chunk_chars < 1:
        raise ValueError("chunk_chars must be at least 1")
    if overlap_chars < 0 or overlap_chars >= chunk_chars:
        raise ValueError("overlap_chars must be between 0 and chunk_chars - 1")
    if not text.strip():
        return []

    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + chunk_chars, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = end - overlap_chars
    return chunks


def case_text(case: Case) -> str:
    full_text = case.full_text or ""
    if full_text.strip():
        return full_text
    return case.summary or ""


def _chunk_row(
    case_id: int,
    *,
    chunk_set: str,
    chunk_index: int,
    text: str,
    chunk_label: str | None = None,
    paragraph_start: int | None = None,
    paragraph_end: int | None = None,
) -> CaseChunk:
    return CaseChunk(
        case_id=case_id,
        chunk_set=chunk_set,
        chunk_index=chunk_index,
        chunk_label=chunk_label,
        paragraph_start=paragraph_start,
        paragraph_end=paragraph_end,
        text=text,
        text_hash=sha256(text.encode("utf-8")).hexdigest(),
        token_estimate=max(1, len(text) // 4),
    )


def _build_section_chunks(case: Case, text: str) -> list[CaseChunk]:
    heading_matches = list(SECTION_HEADING_RE.finditer(text))
    outro_matches = list(OUTRO_HEADING_RE.finditer(text))
    paragraph_matches = list(PARAGRAPH_MARKER_RE.finditer(text))
    rows: list[CaseChunk] = []
    first_paragraph_start = paragraph_matches[0].start() if paragraph_matches else len(text)
    first_outro_start = outro_matches[0].start() if outro_matches else len(text)
    first_content_start = len(text)
    if heading_matches:
        first_content_start = min(first_content_start, heading_matches[0].start())
    if outro_matches:
        first_content_start = min(first_content_start, outro_matches[0].start())
    if paragraph_matches:
        first_content_start = min(first_content_start, paragraph_matches[0].start())
    intro = text[:first_content_start].strip()
    if intro:
        rows.append(
            _chunk_row(
                case.id,
                chunk_set=CHUNK_SET_SECTION,
                chunk_index=len(rows),
                text=intro,
                chunk_label="Intro Metadata",
                paragraph_start=0,
                paragraph_end=0,
            )
        )

    section_markers: list[tuple[int, str]] = []
    for match in heading_matches:
        start = match.start()
        label = _normalize_section_heading(match.group(1))
        if label == "Order" and start < first_paragraph_start:
            continue
        if start >= first_outro_start:
            label = "Outro Metadata"
        section_markers.append((start, label))
    for match in outro_matches:
        section_markers.append((match.start(), "Outro Metadata"))
    section_markers = sorted(section_markers, key=lambda item: item[0])
    # Collapse adjacent duplicate labels, especially repeated footer metadata markers.
    collapsed_markers: list[tuple[int, str]] = []
    for start, label in section_markers:
        if collapsed_markers and collapsed_markers[-1][1] == label:
            continue
        collapsed_markers.append((start, label))
    section_markers = collapsed_markers

    if section_markers:
        for index, (start, label) in enumerate(section_markers):
            end = section_markers[index + 1][0] if index + 1 < len(section_markers) else len(text)
            section_text = text[start:end].strip()
            if not section_text:
                continue
            rows.append(
                _chunk_row(
                    case.id,
                    chunk_set=CHUNK_SET_SECTION,
                    chunk_index=len(rows),
                    text=section_text,
                    chunk_label=label,
                )
            )
    else:
        body = text[first_content_start:].strip() if first_content_start < len(text) else ""
        if body:
            rows.append(
                _chunk_row(
                    case.id,
                    chunk_set=CHUNK_SET_SECTION,
                    chunk_index=len(rows),
                    text=body,
                    chunk_label="Body" if rows else "Document",
                )
            )
        elif not rows and text.strip():
            rows.append(
                _chunk_row(
                    case.id,
                    chunk_set=CHUNK_SET_SECTION,
                    chunk_index=0,
                    text=text.strip(),
                    chunk_label="Document",
                )
            )

    return rows


def _normalize_section_heading(value: str) -> str:
    label = value.strip().title()
    if label == "Introduction":
        return "Overview"
    if label == "Background Facts":
        return "Background"
    if label == "Reasons And Order":
        return "Order"
    return label


def load_case_ids_from_csv(path: str | Path) -> list[int]:
    case_ids: list[int] = []
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            for key in ("local_case_id", "case_id", "id"):
                value = (row.get(key) or "").strip()
                if value.isdigit():
                    case_ids.append(int(value))
                    break
    return sorted(set(case_ids))


def _build_paragraph_chunks(case: Case, text: str) -> list[CaseChunk]:
    marker_re = SCC_PARAGRAPH_MARKER_RE if (getattr(case, "court", "") or "").upper() == "SCC" else PARAGRAPH_MARKER_RE
    matches = list(marker_re.finditer(text))
    heading_matches = list(SECTION_HEADING_RE.finditer(text))
    first_outro_start = next(
        (
            match.start()
            for match in OUTRO_HEADING_RE.finditer(text)
            if not matches or match.start() > matches[-1].start()
        ),
        len(text),
    )
    heading_matches = [match for match in heading_matches if match.start() < first_outro_start]
    rows: list[CaseChunk] = []
    if not matches and not heading_matches:
        if text.strip():
            rows.append(
                _chunk_row(
                    case.id,
                    chunk_set=CHUNK_SET_PARAGRAPH,
                    chunk_index=0,
                    text=text.strip(),
                    chunk_label="document",
                    paragraph_start=0,
                    paragraph_end=0,
                )
            )
        return rows

    structural_matches = sorted(
        [(match.start(), "heading", match) for match in heading_matches]
        + [(match.start(), "paragraph", match) for match in matches],
        key=lambda item: item[0],
    )
    intro = text[: structural_matches[0][0]].strip()
    if intro:
        rows.append(
            _chunk_row(
                case.id,
                chunk_set=CHUNK_SET_PARAGRAPH,
                chunk_index=len(rows),
                text=intro,
                chunk_label="intro",
                paragraph_start=0,
                paragraph_end=0,
            )
        )

    last_paragraph_number: int | None = None
    consumed_end = structural_matches[0][0]
    for match_index, (start, kind, match) in enumerate(structural_matches):
        if kind == "heading":
            heading_text = match.group(0).strip()
            if heading_text:
                rows.append(
                    _chunk_row(
                        case.id,
                        chunk_set=CHUNK_SET_PARAGRAPH,
                        chunk_index=len(rows),
                        text=heading_text,
                        chunk_label="heading",
                    )
                )
            consumed_end = match.end()
            continue

        next_start = (
            structural_matches[match_index + 1][0]
            if match_index + 1 < len(structural_matches)
            else first_outro_start
        )
        paragraph_text = text[start:next_start].strip()
        if not paragraph_text:
            consumed_end = next_start
            continue
        paragraph_number = _mapped_paragraph_number(paragraph_text, last_paragraph_number)
        rows.append(
            _chunk_row(
                case.id,
                chunk_set=CHUNK_SET_PARAGRAPH,
                chunk_index=len(rows),
                text=paragraph_text,
                chunk_label=str(paragraph_number),
                paragraph_start=paragraph_number,
                paragraph_end=paragraph_number,
            )
        )
        if paragraph_number is not None:
            last_paragraph_number = paragraph_number
        consumed_end = next_start

    trailing_context = text[consumed_end:first_outro_start].strip()
    if trailing_context:
        rows.append(
            _chunk_row(
                case.id,
                chunk_set=CHUNK_SET_PARAGRAPH,
                chunk_index=len(rows),
                text=trailing_context,
                chunk_label="tail",
                paragraph_start=(last_paragraph_number or 0) + 1,
                paragraph_end=(last_paragraph_number or 0) + 1,
            )
        )

    tail = text[first_outro_start:].strip() if first_outro_start < len(text) else ""
    if tail:
        last_number = last_paragraph_number or 0
        rows.append(
            _chunk_row(
                case.id,
                chunk_set=CHUNK_SET_PARAGRAPH,
                chunk_index=len(rows),
                text=tail,
                chunk_label="tail",
                paragraph_start=last_number + 1,
                paragraph_end=last_number + 1,
            )
        )

    return rows


def _scc_text_paragraph_matches(text: str) -> list[re.Match[str]]:
    matches: list[re.Match[str]] = []
    for match in SCC_TEXT_PARAGRAPH_RE.finditer(text):
        number = int(match.group(1) or match.group(2))
        line_end = text.find("\n", match.start())
        line = text[match.start() : line_end if line_end >= 0 else len(text)]
        if number >= 1900 or re.match(r"\d{4}\s+(?:SCC|SCR)\b", line, re.IGNORECASE):
            continue
        matches.append(match)
    return matches


def _build_scc_line_paragraph_chunks(case: Case, text: str, first_outro_start: int) -> list[CaseChunk]:
    body_match = SCC_BODY_START_RE.search(text)
    body_start = body_match.start() if body_match else 0
    body_text = text[body_start:first_outro_start]
    rows: list[CaseChunk] = []
    for line in body_text.splitlines():
        value = line.strip()
        if not value:
            continue
        rows.append(
            _chunk_row(
                case.id,
                chunk_set=CHUNK_SET_PARAGRAPH,
                chunk_index=len(rows),
                text=value,
                chunk_label=f"body-{len(rows) + 1}",
            )
        )
    return rows


def _build_scc_text_chunk_layers(case: Case, text: str) -> tuple[list[CaseChunk], list[CaseChunk]]:
    """Build SCC sections and paragraphs from canonical text when HTML is unavailable."""
    paragraph_matches = _scc_text_paragraph_matches(text)
    section_matches = list(SCC_TEXT_SECTION_RE.finditer(text))
    outro_matches = list(OUTRO_HEADING_RE.finditer(text)) + list(SCC_OUTRO_HEADING_RE.finditer(text))
    outro_matches.sort(key=lambda match: match.start())
    first_paragraph_start = paragraph_matches[0].start() if paragraph_matches else len(text)
    first_outro_start = outro_matches[0].start() if outro_matches else len(text)
    first_content_start = min(
        [len(text), first_paragraph_start, first_outro_start]
        + [match.start() for match in section_matches]
    )

    section_rows: list[CaseChunk] = []
    intro = text[:first_content_start].strip()
    if intro:
        section_rows.append(
            _chunk_row(
                case.id,
                chunk_set=CHUNK_SET_SECTION,
                chunk_index=0,
                text=intro,
                chunk_label="Intro Metadata",
                paragraph_start=0,
                paragraph_end=0,
            )
        )
    usable_sections = [match for match in section_matches if match.start() < first_outro_start]
    for index, match in enumerate(usable_sections):
        start = match.start()
        end = usable_sections[index + 1].start() if index + 1 < len(usable_sections) else first_outro_start
        value = text[start:end].strip()
        if value:
            section_rows.append(
                _chunk_row(
                    case.id,
                    chunk_set=CHUNK_SET_SECTION,
                    chunk_index=len(section_rows),
                    text=value,
                    chunk_label=match.group(2).strip().title(),
                )
            )
    if not usable_sections:
        body = text[first_content_start:first_outro_start].strip()
        if body:
            section_rows.append(
                _chunk_row(
                    case.id,
                    chunk_set=CHUNK_SET_SECTION,
                    chunk_index=len(section_rows),
                    text=body,
                    chunk_label="Body",
                )
            )

    last_paragraph_number: int | None = None
    if not paragraph_matches:
        paragraph_rows = _build_scc_line_paragraph_chunks(case, text, first_outro_start)
    else:
        paragraph_rows = []
        intro = text[: paragraph_matches[0].start()].strip()
        if intro:
            paragraph_rows.append(
                _chunk_row(
                    case.id,
                    chunk_set=CHUNK_SET_PARAGRAPH,
                    chunk_index=0,
                    text=intro,
                    chunk_label="intro",
                    paragraph_start=0,
                    paragraph_end=0,
                )
            )
        for index, match in enumerate(paragraph_matches):
            end = paragraph_matches[index + 1].start() if index + 1 < len(paragraph_matches) else first_outro_start
            value = text[match.start() : end].strip()
            if value:
                number = _mapped_paragraph_number(value, last_paragraph_number)
                paragraph_rows.append(
                    _chunk_row(
                        case.id,
                        chunk_set=CHUNK_SET_PARAGRAPH,
                        chunk_index=len(paragraph_rows),
                        text=value,
                        chunk_label=str(number),
                        paragraph_start=number,
                        paragraph_end=number,
                    )
                )
                if number is not None:
                    last_paragraph_number = number
    tail = text[first_outro_start:].strip() if first_outro_start < len(text) else ""
    if tail:
        last_number = last_paragraph_number or 0
        paragraph_rows.append(
            _chunk_row(
                case.id,
                chunk_set=CHUNK_SET_PARAGRAPH,
                chunk_index=len(paragraph_rows),
                text=tail,
                chunk_label="tail",
                paragraph_start=last_number + 1,
                paragraph_end=last_number + 1,
            )
        )
    return section_rows, paragraph_rows


MIN_READER_PARAGRAPHS = 3
READER_MAX_GAP = 3


HANGING_HEADING_MAX_WORDS = 15
LABELLED_HEADING_MAX_WORDS = 30
_HANGING_END_RE = re.compile(r"[.,;:?!)”\"\]]$")


_LABELLED_HEADING_RE = re.compile(r"^(?:[IVX]+|[A-Z]|\d{1,2})\.\s+(?P<title>\S.*)$")
_ANSWER_START_RE = re.compile(r"^(?:I|We|You|My|Yes|No|It|He|She|They)\b")


def _is_hanging_heading_line(line: str) -> bool:
    """A short unnumbered title line directly before a numbered paragraph.

    Either an unlabelled line with no closing punctuation ("Issue Estoppel") or a labelled one ("B. Court of Appeal,
    2015 ABCA 85 — Slatter J.A."), which may end in a full stop. A one-word "A. Yes." or a transcript answer
    ("A. I don't recall ...") is not a heading.
    """
    line = line.strip()
    if not line or len(line) > 220:
        return False
    words = len(line.split())
    labelled = _LABELLED_HEADING_RE.match(line)
    if words > (LABELLED_HEADING_MAX_WORDS if labelled else HANGING_HEADING_MAX_WORDS):
        return False
    if labelled:
        title = labelled.group("title")
        if title[0] == "[" or _ANSWER_START_RE.match(title) or title.endswith((",", ";", ":", "?")):
            return False
        return not title.endswith(".") or len(title.split()) >= 3
    if not (line[0].isupper() or line[0].isdigit()) or _HANGING_END_RE.search(line):
        return False
    return not re.match(r"^(?:\(\w{1,5}\)|\w{1,3}[.)])\s", line)


def _split_hanging_headings(text: str, entries: list[dict]) -> list[dict]:
    """Move heading lines that trail a numbered paragraph into their own heading rows.

    The stored text puts a sub-heading ("Issue Estoppel") on the line after the last paragraph of the previous part.
    Only a line directly before the next numbered paragraph counts, so a list of defined terms inside a quoted
    statute, or a signature line at the end of the reasons, stays where it is.
    """
    out: list[dict] = []
    for index, entry in enumerate(entries):
        following = entries[index + 1] if index + 1 < len(entries) else None
        if entry["kind"] != "paragraph" or following is None or following["kind"] not in {"paragraph", "heading"}:
            out.append(entry)
            continue
        body = text[entry["start"] : entry["end"]]
        lines = body.rstrip().split("\n")
        cut = len(lines)
        while cut > 1 and _is_hanging_heading_line(lines[cut - 1]):
            cut -= 1
        if cut == len(lines):
            out.append(entry)
            continue
        offset = entry["start"] + len("\n".join(lines[:cut]))
        out.append({**entry, "end": offset})
        position = offset + 1
        for line in lines[cut:]:
            out.append({"kind": "heading", "start": position, "end": position + len(line)})
            position += len(line) + 1
    return out


def _expected_number_comes_later(blocks: list[dict], index: int, expected: int, window: int = 3) -> bool:
    """True when paragraph ``expected`` is one of the next few numbered blocks after ``blocks[index]``."""
    seen = 0
    for block in blocks[index + 1 :]:
        if block.get("type") != "para" or block.get("num") is None:
            continue
        if block["num"] == expected:
            return True
        seen += 1
        if seen >= window:
            return False
    return False


def _tail_after_last_paragraph(text: str, entries: list[dict]) -> list[dict]:
    """After the last numbered paragraph a heading row keeps only its first line ("ORDER"); the order text, counsel
    list or appendix that followed it is the tail, not part of a heading."""
    last_paragraph = max((i for i, entry in enumerate(entries) if entry["kind"] == "paragraph"), default=-1)
    out: list[dict] = []
    for index, entry in enumerate(entries):
        out.append(entry)
        if index <= last_paragraph or entry["kind"] != "heading":
            continue
        body = text[entry["start"] : entry["end"]]
        first, sep, rest = body.partition("\n")
        if sep and rest.strip():
            entry["end"] = entry["start"] + len(first)
            out.append({"kind": "tail", "start": entry["end"] + 1, "end": entry["start"] + len(body)})
    return out


def reader_paragraph_layout(text: str) -> list[dict]:
    """Paragraph rows as the reader numbers them: intro, numbered paragraphs, headings, tail.

    Uses the reader's formatter (``format_decision``), which accepts a bracketed or bare number only when it
    follows the previous paragraph, so a year or a report citation such as ``[2010] 3 S.C.R.`` is not a
    paragraph, and a paragraph that starts on the same line as its heading ("II. Facts [5] The Applicant")
    is its own paragraph. A numbered block that does not follow the sequence (a paragraph quoted from another
    decision) stays inside the paragraph before it. Returns ``[]`` when fewer than three paragraphs are found.
    """
    blocks = format_decision(text)
    entries: list[dict] = []
    current: dict | None = None
    last_num: int | None = None
    intro_end: int | None = None
    head_run: list[tuple[int, int]] = []  # headings directly before the first numbered paragraph
    for index, block in enumerate(blocks):
        kind = block.get("type")
        start, end = block["start"], block["end"]
        before_run = head_run
        if intro_end is None:
            head_run = head_run + [(start, end)] if kind == "heading" else []
        if kind == "para":
            num = block.get("num")
            follows = num is not None and (
                (last_num is None and 1 <= num <= READER_MAX_GAP)
                or (last_num is not None and last_num < num <= last_num + READER_MAX_GAP)
            )
            if follows and last_num is not None and num > last_num + 1 and _expected_number_comes_later(blocks, index, last_num + 1):
                follows = False  # a quoted paragraph number ("[31] ...") ahead of the real paragraph 30
            if follows:
                if intro_end is None:
                    intro_end = start
                    for head_start, head_end in before_run:
                        entries.append({"kind": "heading", "start": head_start, "end": head_end})
                    if before_run:
                        intro_end = before_run[0][0]
                current = {"kind": "paragraph", "num": num, "start": start, "end": end}
                entries.append(current)
                last_num = num
                continue
        if kind == "heading" and current is not None:
            entries.append({"kind": "heading", "start": start, "end": end})
            current = None
            continue
        if kind == "footer":
            entries.append({"kind": "tail", "start": start, "end": end})
            current = None
            continue
        if current is not None:
            current["end"] = end
        elif entries and entries[-1]["kind"] in {"heading", "tail"}:
            entries[-1]["end"] = end
    numbered = [entry for entry in entries if entry["kind"] == "paragraph"]
    if len(numbered) < MIN_READER_PARAGRAPHS:
        return []
    entries = _tail_after_last_paragraph(text, _split_hanging_headings(text, entries))
    layout: list[dict] = []
    if intro_end:
        layout.append({"kind": "intro", "start": 0, "end": intro_end})
    layout.extend(entries)
    merged: list[dict] = []
    for entry in layout:
        if entry["kind"] == "tail" and merged and merged[-1]["kind"] == "tail":
            merged[-1]["end"] = entry["end"]
        else:
            merged.append(dict(entry))
    return merged


def _build_reader_paragraph_chunks(case: Case, text: str) -> list[CaseChunk]:
    """Paragraph rows from ``reader_paragraph_layout``; empty when the text has no usable numbering."""
    rows: list[CaseChunk] = []
    last_number = 0
    for entry in reader_paragraph_layout(text):
        value = text[entry["start"] : entry["end"]].strip()
        if not value:
            continue
        kind = entry["kind"]
        if kind == "paragraph":
            number = entry["num"]
            last_number = number
            label, first, last = str(number), number, number
        elif kind == "intro":
            label, first, last = "intro", 0, 0
        elif kind == "tail":
            label, first, last = "tail", last_number + 1, last_number + 1
        else:
            label, first, last = "heading", None, None
        rows.append(
            _chunk_row(
                case.id,
                chunk_set=CHUNK_SET_PARAGRAPH,
                chunk_index=len(rows),
                text=value,
                chunk_label=label,
                paragraph_start=first,
                paragraph_end=last,
            )
        )
    return rows


def _with_reader_paragraphs(case: Case, text: str, rows: list[CaseChunk]) -> list[CaseChunk]:
    """Swap the paragraph rows in ``rows`` for the reader-numbered ones when the reader finds numbered paragraphs."""
    reader_rows = _build_reader_paragraph_chunks(case, text)
    if not reader_rows:
        return rows
    return [row for row in rows if row.chunk_set != CHUNK_SET_PARAGRAPH] + reader_rows


def _build_full_case_chunk(case: Case, text: str) -> list[CaseChunk]:
    if not text.strip():
        return []
    return [
        _chunk_row(
            case.id,
            chunk_set=CHUNK_SET_FULL_CASE,
            chunk_index=0,
            text=text,
            chunk_label="Full case",
        )
    ]


def build_case_chunk_layers(case: Case) -> list[CaseChunk]:
    """Build the canonical full-case, section, and paragraph chunk layers."""
    text = case_text(case)
    if not text.strip():
        return []
    source_family = "scc" if (getattr(case, "court", "") or "").upper() == "SCC" else None
    structured = map_to_canonical_text(structure_source_html(getattr(case, "source_html", None), text, source_family), text)
    mapping_threshold = 0.85 if source_family == "scc" else 0.98
    if structured.mapping_confidence is not None and structured.mapping_confidence >= mapping_threshold:
        html_layers = _build_html_chunk_layers(case, text, structured, source_family=source_family)
        if html_layers is not None:
            return _with_reader_paragraphs(case, text, _build_full_case_chunk(case, text) + html_layers[0] + html_layers[1])
    if source_family == "scc":
        text_layers = _build_scc_text_chunk_layers(case, text)
        return _with_reader_paragraphs(case, text, _build_full_case_chunk(case, text) + text_layers[0] + text_layers[1])
    return _with_reader_paragraphs(
        case,
        text,
        _build_full_case_chunk(case, text)
        + _build_section_chunks(case, text)
        + _build_paragraph_chunks(case, text),
    )


def _canonical_block_text(block, text: str) -> str | None:
    if block.canonical_text_start is None or block.canonical_text_end is None:
        return None
    value = text[block.canonical_text_start : block.canonical_text_end].strip()
    return value or None


def _mapped_paragraph_number(block_text: str, last_number: int | None) -> int | None:
    match = re.match(r"(?:\[(\d+)\]|(\d+)(?:[.)])?)[ \t]+", block_text)
    if match is None:
        return None
    number = int(match.group(1) or match.group(2))
    if last_number is None:
        return number if number == 1 else None
    return number if number > last_number else None


def _build_html_chunk_layers(case: Case, text: str, document, *, source_family: str | None = None) -> tuple[list[CaseChunk], list[CaseChunk]] | None:
    """Build section and paragraph rows from confidently mapped HTML blocks."""
    mapped_blocks = [
        block
        for block in document.blocks
        if block.mapping_confidence >= 0.9
        and block.canonical_text_start is not None
        and block.canonical_text_end is not None
        and block.canonical_text_end > block.canonical_text_start
    ]
    if not mapped_blocks:
        return None
    top_level = min(
        (block.heading_level for block in mapped_blocks if block.kind == "heading" and block.heading_level is not None),
        default=None,
    )
    headings = [
        block
        for block in mapped_blocks
        if block.kind == "heading" and block.heading_level == top_level
    ]
    if not headings:
        return None

    section_rows: list[CaseChunk] = []
    section_start = 0
    for heading_index, heading in enumerate(headings):
        heading_start = heading.canonical_text_start or 0
        if heading_start > section_start:
            prefix = text[section_start:heading_start].strip()
            if prefix:
                section_rows.append(_chunk_row(case.id, chunk_set=CHUNK_SET_SECTION, chunk_index=len(section_rows), text=prefix, chunk_label="Intro Metadata"))
        section_start = heading_start
        section_end = headings[heading_index + 1].canonical_text_start if heading_index + 1 < len(headings) else len(text)
        section_text = text[section_start:section_end].strip()
        label = re.sub(r"^[IVXLC]+\.\s*", "", heading.text).strip().title() or "Section"
        if section_text:
            section_rows.append(_chunk_row(case.id, chunk_set=CHUNK_SET_SECTION, chunk_index=len(section_rows), text=section_text, chunk_label=label))
        section_start = section_end

    paragraph_rows: list[CaseChunk] = []
    last_end = 0
    last_paragraph_number: int | None = None
    for block in mapped_blocks:
        if block.kind not in {"heading", "paragraph", "list_item", "table_row", "quote", "preformatted"}:
            continue
        start = block.canonical_text_start or 0
        end = block.canonical_text_end or start
        if start < last_end:
            continue
        block_text = text[start:end].strip()
        if not block_text:
            continue
        if block.kind == "heading":
            paragraph_rows.append(
                _chunk_row(
                    case.id,
                    chunk_set=CHUNK_SET_PARAGRAPH,
                    chunk_index=len(paragraph_rows),
                    text=block_text,
                    chunk_label="heading",
                )
            )
            last_end = end
            continue
        paragraph_number = _mapped_paragraph_number(block_text, last_paragraph_number)
        paragraph_rows.append(_chunk_row(case.id, chunk_set=CHUNK_SET_PARAGRAPH, chunk_index=len(paragraph_rows), text=block_text, chunk_label=str(paragraph_number) if paragraph_number is not None else block.kind, paragraph_start=paragraph_number, paragraph_end=paragraph_number))
        if paragraph_number is not None:
            last_paragraph_number = paragraph_number
        last_end = end
    return section_rows, paragraph_rows


def build_case_chunks(case: Case) -> list[CaseChunk]:
    text = case_text(case)
    if not text.strip():
        return []
    return _build_reader_paragraph_chunks(case, text) or _build_paragraph_chunks(case, text)


def pending_case_query(
    *,
    last_case_id: int = 0,
    court: str | None = None,
    source_type: str | None = None,
):
    already_chunked = exists(select(CaseChunk.id).where(CaseChunk.case_id == Case.id))
    has_text = or_(
        func.length(func.trim(func.coalesce(Case.full_text, ""))) > 0,
        func.length(func.trim(func.coalesce(Case.summary, ""))) > 0,
    )
    statement = (
        select(Case)
        .where(Case.id > last_case_id, ~already_chunked, has_text)
        .order_by(Case.id)
    )
    if court:
        statement = statement.where(Case.court == court)
    if source_type:
        statement = statement.where(Case.source_type == source_type)
    return statement


def chunk_pending_cases(
    db: Session,
    *,
    batch_size: int = 50,
    limit: int | None = None,
    court: str | None = None,
    source_type: str | None = None,
) -> tuple[int, int]:
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")
    if limit is not None and limit < 1:
        raise ValueError("limit must be at least 1")

    cases_chunked = 0
    chunks_created = 0
    last_case_id = 0
    while limit is None or cases_chunked < limit:
        current_batch_size = min(batch_size, limit - cases_chunked) if limit else batch_size
        cases = db.scalars(
            pending_case_query(
                last_case_id=last_case_id,
                court=court,
                source_type=source_type,
            ).limit(current_batch_size)
        ).all()
        if not cases:
            break

        batch_chunks: list[CaseChunk] = []
        for case in cases:
            batch_chunks.extend(build_case_chunk_layers(case))
        db.add_all(batch_chunks)
        db.commit()

        cases_chunked += len(cases)
        chunks_created += len(batch_chunks)
        last_case_id = cases[-1].id
        logger.info("Chunked %d cases into %d chunks", cases_chunked, chunks_created)

    return cases_chunked, chunks_created


def rebuild_case_chunks(
    db: Session,
    *,
    case_ids: list[int],
    replace_existing: bool = True,
) -> tuple[int, int]:
    if not case_ids:
        return 0, 0

    cases = list(
        db.scalars(select(Case).where(Case.id.in_(case_ids)).order_by(Case.id))
    )
    if replace_existing:
        db.execute(delete(CaseChunk).where(CaseChunk.case_id.in_([case.id for case in cases])))

    rows: list[CaseChunk] = []
    for case in cases:
        rows.extend(build_case_chunk_layers(case))
    if rows:
        db.add_all(rows)
    db.commit()
    return len(cases), len(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=50)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--court", default=None)
    parser.add_argument("--source-type", default=None)
    parser.add_argument("--case-id", type=int, action="append", default=[])
    parser.add_argument("--case-ids-csv", default=None)
    parser.add_argument("--replace-existing", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    with SessionLocal() as db:
        scoped_case_ids = sorted(set(args.case_id or []))
        if args.case_ids_csv:
            scoped_case_ids = sorted(set(scoped_case_ids + load_case_ids_from_csv(args.case_ids_csv)))

        if scoped_case_ids:
            cases_chunked, chunks_created = rebuild_case_chunks(
                db,
                case_ids=scoped_case_ids,
                replace_existing=args.replace_existing or True,
            )
            print(f"cases_chunked={cases_chunked} chunks_created={chunks_created}")
            return

        if args.dry_run:
            pending = db.scalars(
                pending_case_query(court=args.court, source_type=args.source_type).limit(
                    args.limit or 10
                )
            ).all()
            estimated_chunks = sum(len(build_case_chunk_layers(case)) for case in pending)
            print(f"pending_sample={len(pending)} estimated_chunks={estimated_chunks}")
            return

        cases_chunked, chunks_created = chunk_pending_cases(
            db,
            batch_size=args.batch_size,
            limit=args.limit,
            court=args.court,
            source_type=args.source_type,
        )
        print(f"cases_chunked={cases_chunked} chunks_created={chunks_created}")


if __name__ == "__main__":
    main()