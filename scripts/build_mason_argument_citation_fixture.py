from __future__ import annotations

import argparse
import json
from hashlib import sha256
from pathlib import Path
import re
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from sqlalchemy import select

from backend.database import CaseChunk, Citation, SessionLocal


PARAGRAPH_RE = re.compile(r"(?m)^\s*\[(\d{1,3})\](?=\s|$)")


def _load_units(directory: Path) -> dict[tuple[int, int], dict[str, Any]]:
    units: dict[tuple[int, int], dict[str, Any]] = {}
    for path in sorted(directory.glob("mason_scc_2023_window_*_result_request.json")):
        if "llm_only" in path.name:
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        for unit in payload.get("response", {}).get("result", {}).get("units", []):
            start = int(unit["start_paragraph"])
            end = int(unit["end_paragraph"])
            units.setdefault(
                (start, end),
                {
                    "label": str(unit.get("label") or "Unlabelled discussion"),
                    "explanation": str(unit.get("explanation") or ""),
                    "confidence": unit.get("confidence"),
                    "source_artifact": str(path),
                },
            )
    return units


def _paragraphs(text: str) -> list[dict[str, Any]]:
    matches = list(PARAGRAPH_RE.finditer(text))
    return [
        {
            "paragraph_index": int(match.group(1)),
            "start_offset": match.start(),
            "end_offset": matches[index + 1].start() if index + 1 < len(matches) else len(text),
            "text": text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)].strip(),
        }
        for index, match in enumerate(matches)
    ]


def _unit_for_paragraph(units: dict[tuple[int, int], dict[str, Any]], paragraph_index: int) -> tuple[tuple[int, int], dict[str, Any]] | None:
    matches = [item for item in units.items() if item[0][0] <= paragraph_index <= item[0][1]]
    return min(matches, key=lambda item: item[0][1] - item[0][0]) if matches else None


def build_fixture(
    session,
    *,
    artifact_directory: Path,
    case_id: int,
    limit: int,
    min_paragraph: int,
    paragraph_context: int,
) -> list[dict[str, Any]]:
    units = _load_units(artifact_directory)
    citations = session.execute(
        select(Citation, CaseChunk)
        .join(CaseChunk, CaseChunk.id == Citation.chunk_id)
        .where(
            Citation.source_case_id == case_id,
            Citation.offset_start.is_not(None),
            Citation.offset_end.is_not(None),
            CaseChunk.case_id == case_id,
            CaseChunk.chunk_set.in_(["section", "full_case"]),
        ).order_by(Citation.id)
    )
    rows: list[dict[str, Any]] = []
    seen: set[tuple[int, int]] = set()
    for citation, source_chunk in citations:
        start = int(citation.offset_start)
        end = int(citation.offset_end)
        source_text = source_chunk.text or ""
        paragraphs = _paragraphs(source_text)
        by_index = {item["paragraph_index"]: item for item in paragraphs}
        paragraph = next(
            (item for item in paragraphs if item["start_offset"] <= start and end <= item["end_offset"]),
            None,
        )
        if paragraph is None or paragraph["paragraph_index"] < min_paragraph:
            continue
        unit_match = _unit_for_paragraph(units, paragraph["paragraph_index"])
        if unit_match is None:
            continue
        unit_range, unit = unit_match
        unit_start = by_index.get(unit_range[0])
        unit_end = by_index.get(unit_range[1])
        if unit_start is None or unit_end is None:
            continue
        key = (int(citation.id), unit_range[0])
        if key in seen:
            continue
        seen.add(key)
        paragraph_position = paragraphs.index(paragraph)
        context_start = max(0, paragraph_position - paragraph_context)
        context_end = min(len(paragraphs), paragraph_position + paragraph_context + 1)
        source_start = paragraphs[context_start]["start_offset"]
        source_end = paragraphs[context_end - 1]["end_offset"]
        text = source_text[source_start:source_end].strip()
        trim_start = source_start + (len(source_text[source_start:source_end]) - len(source_text[source_start:source_end].lstrip()))
        local_start = start - trim_start
        local_end = end - trim_start
        citation_text = text[local_start:local_end]
        if citation_text != source_text[start:end] or citation_text != getattr(citation, "citation_text", citation_text):
            continue
        rows.append(
            {
                "example_id": f"mason-argument-citation-{len(rows) + 1:03d}",
                "text": text,
                "source_text_sha256": sha256(text.encode("utf-8")).hexdigest(),
                "metadata": {
                    "case_id": case_id,
                    "citation_record": {
                        "citation_id": int(citation.id),
                        "normalized_citation": getattr(citation, "normalized_citation", None),
                        "source_case_id": case_id,
                        "source_chunk_id": int(source_chunk.id),
                        "source_offsets": [start, end],
                    },
                    "paragraph": {
                        "start": paragraph["paragraph_index"],
                        "end": paragraph["paragraph_index"],
                        "text": paragraph["text"],
                    },
                    "discussion_unit": {
                        "start_paragraph": unit_range[0],
                        "end_paragraph": unit_range[1],
                        **unit,
                    },
                },
                "citations": [
                    {
                        "ordinal": 0,
                        "citation_text": citation_text,
                        "normalized_citation": getattr(citation, "normalized_citation", None),
                        "start_offset": local_start,
                        "end_offset": local_end,
                    }
                ],
            }
        )
        if len(rows) >= limit:
            break
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a report-only Mason argument-level citation fixture.")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--artifact-directory", type=Path, default=ROOT / "data" / "eval" / "llm_discussion_units_pilot")
    parser.add_argument("--case-id", type=int, default=53164)
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--min-paragraph", type=int, default=1)
    parser.add_argument(
        "--paragraph-context",
        type=int,
        default=2,
        help="Number of paragraphs to include before and after the citation paragraph.",
    )
    args = parser.parse_args()
    if not 1 <= args.limit <= 100:
        parser.error("--limit must be between 1 and 100")
    if args.paragraph_context < 0:
        parser.error("--paragraph-context must be non-negative")
    with SessionLocal() as session:
        rows = build_fixture(
            session,
            artifact_directory=args.artifact_directory,
            case_id=args.case_id,
            limit=args.limit,
            min_paragraph=args.min_paragraph,
            paragraph_context=args.paragraph_context,
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=True, sort_keys=True) + "\n")
    print(json.dumps({"status": "read_only_fixture", "case_id": args.case_id, "rows": len(rows), "output": str(args.output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
