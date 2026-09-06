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
    rows: list[CaseChunk] = []
    if not matches:
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

    intro = text[: matches[0].start()].strip()
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

    outro_start = len(text)
    for outro_match in OUTRO_HEADING_RE.finditer(text):
        if outro_match.start() > matches[-1].start():
            outro_start = outro_match.start()
            break

    for match_index, match in enumerate(matches):
        paragraph_number = int(match.group(1))
        start = match.start()
        end = matches[match_index + 1].start() if match_index + 1 < len(matches) else outro_start
        paragraph_text = text[start:end].strip()
        if not paragraph_text:
            continue
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

    tail = text[outro_start:].strip() if outro_start < len(text) else ""
    if tail:
        last_number = int(matches[-1].group(1))
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
            return _build_full_case_chunk(case, text) + html_layers[0] + html_layers[1]
    return (
        _build_full_case_chunk(case, text)
        + _build_section_chunks(case, text)
        + _build_paragraph_chunks(case, text)
    )


def _canonical_block_text(block, text: str) -> str | None:
    if block.canonical_text_start is None or block.canonical_text_end is None:
        return None
    value = text[block.canonical_text_start : block.canonical_text_end].strip()
    return value or None


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
    for block in mapped_blocks:
        if block.kind not in {"paragraph", "list_item", "table_row", "quote", "preformatted"} and not (source_family == "scc" and block.kind == "heading"):
            continue
        start = block.canonical_text_start or 0
        end = block.canonical_text_end or start
        if start < last_end:
            continue
        block_text = text[start:end].strip()
        if not block_text:
            continue
        paragraph_match = re.match(r"\[(\d+)\]", block_text)
        paragraph_number = int(paragraph_match.group(1)) if paragraph_match else None
        paragraph_rows.append(_chunk_row(case.id, chunk_set=CHUNK_SET_PARAGRAPH, chunk_index=len(paragraph_rows), text=block_text, chunk_label=str(paragraph_number) if paragraph_number is not None else block.kind, paragraph_start=paragraph_number, paragraph_end=paragraph_number))
        last_end = end
    return section_rows, paragraph_rows


def build_case_chunks(case: Case) -> list[CaseChunk]:
    text = case_text(case)
    if not text.strip():
        return []
    return _build_paragraph_chunks(case, text)


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