from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from typing import Any

from sqlalchemy import select

from backend.contextual_authority import (
    ParagraphFeatures,
    compute_continuity,
    segment_subthemes,
    segment_discussion_units,
)
from backend.database import CaseChunk, CaseTag, Citation, SessionLocal, StatuteReference


def _is_heading(chunk: CaseChunk) -> bool:
    return _heading_match(chunk.text or "") is not None or (chunk.chunk_label or "").strip().casefold() in {
        "heading",
        "section",
        "subsection",
    }


def _heading_match(text: str) -> re.Match[str] | None:
    text = text.strip()
    first_line = text.splitlines()[0].strip() if text else ""
    first_line = re.sub(r"^\[\d+\]\s*", "", first_line)
    section_words = (
        "background|facts?|issues?|analysis|reasons?|discussion|conclusion|"
        "disposition|order|law|standard of review|submissions?"
    )
    first_line_match = re.match(
        rf"^(?:#{{1,6}}\s+|[A-Z][A-Z\s]{{4,80}}:$|(?:{section_words})$)",
        first_line,
        re.IGNORECASE,
    )
    if first_line_match:
        offset = text.find(first_line) + first_line_match.start()
        return re.match(r".*", text[offset:])
    roman_section = re.search(
        rf"\b[IVXLC]+\.\s+(?:{section_words})\b",
        text[:240],
        re.IGNORECASE,
    )
    return roman_section or re.search(r"\b(?:JUDGMENT|ORDER)\b", text[:240])


def _paragraph_features(session, chunks: list[CaseChunk], case_id: int) -> tuple[ParagraphFeatures, ...]:
    chunk_ids = [chunk.id for chunk in chunks]
    citations = session.scalars(select(Citation).where(Citation.source_case_id == case_id, Citation.chunk_id.in_(chunk_ids))).all()
    statutes = session.scalars(select(StatuteReference).where(StatuteReference.source_case_id == case_id, StatuteReference.chunk_id.in_(chunk_ids))).all()
    tags = session.scalars(select(CaseTag).where(CaseTag.case_id == case_id, CaseTag.chunk_id.in_(chunk_ids))).all()
    citations_by_chunk: dict[int, list[int]] = {chunk_id: [] for chunk_id in chunk_ids}
    statutes_by_chunk: dict[int, list[int]] = {chunk_id: [] for chunk_id in chunk_ids}
    tags_by_chunk: dict[int, list[str]] = {chunk_id: [] for chunk_id in chunk_ids}
    for citation in citations:
        citations_by_chunk[citation.chunk_id].append(citation.id)
    for statute in statutes:
        statutes_by_chunk[statute.chunk_id].append(statute.id)
    for tag in tags:
        tags_by_chunk[tag.chunk_id].append(f"{tag.category}:{tag.value}")
    features: list[ParagraphFeatures] = []
    next_index = 0
    for chunk in chunks:
        text = chunk.text
        match = _heading_match(text)
        split_at = match.start() if match and match.start() > 0 else None
        label_is_heading = (chunk.chunk_label or "").strip().casefold() in {
            "heading",
            "section",
            "subsection",
        }
        spans = ((0, split_at, False), (split_at, len(text), True)) if split_at else ((0, len(text), bool(match) or label_is_heading),)
        for start, end, is_heading in spans:
            segment_text = text[start:end]
            if not segment_text:
                continue
            features.append(
                ParagraphFeatures(
                    case_id=chunk.case_id,
                    chunk_id=chunk.id,
                    paragraph_index=next_index,
                    start_offset=start,
                    end_offset=end,
                    text=segment_text,
                    source_text_hash=chunk.text_hash,
                    source_paragraph_index=chunk.chunk_index,
                    citation_ids=tuple(sorted(set(citations_by_chunk[chunk.id]))),
                    statute_ids=tuple(sorted(set(statutes_by_chunk[chunk.id]))),
                    tag_ids=tuple(sorted(set(tags_by_chunk[chunk.id]))),
                    is_heading=is_heading,
                )
            )
            next_index += 1
    return tuple(features)


def inspect_case(session, case_id: int, chunk_set: str, threshold: float, consecutive_low_scores: int) -> dict[str, Any]:
    chunks = session.scalars(
        select(CaseChunk)
        .where(CaseChunk.case_id == case_id, CaseChunk.chunk_set == chunk_set)
        .order_by(CaseChunk.chunk_index, CaseChunk.id)
    ).all()
    paragraphs = _paragraph_features(session, chunks, case_id)
    continuity = tuple(compute_continuity(left, right) for left, right in zip(paragraphs, paragraphs[1:]))
    units = segment_discussion_units(
        paragraphs,
        continuity,
        threshold=threshold,
        consecutive_low_scores=consecutive_low_scores,
        config={"chunk_set": chunk_set},
    )
    subthemes_by_unit = {unit.discussion_unit_id: segment_subthemes(unit) for unit in units}
    chunk_hashes = {chunk.id: chunk.text_hash for chunk in chunks}
    for paragraph in paragraphs:
        if paragraph.source_sha256 != chunk_hashes[paragraph.chunk_id]:
            raise ValueError(f"source hash mismatch for case {case_id}, chunk {paragraph.chunk_id}")
    return {
        "case_id": case_id,
        "chunk_set": chunk_set,
        "paragraph_source": f"CaseChunk rows (chunk_set={chunk_set})",
        "paragraph_count": len(paragraphs),
        "continuity_count": len(continuity),
        "discussion_unit_count": len(units),
        "paragraphs": [
            {
                "paragraph_index": paragraph.paragraph_index,
                "chunk_id": paragraph.chunk_id,
                "source_paragraph_index": paragraph.source_paragraph_index,
                "start_offset": paragraph.start_offset,
                "end_offset": paragraph.end_offset,
                "text": paragraph.text,
                "text_sha256": paragraph.text_sha256,
                "source_text_sha256": paragraph.source_sha256,
                "citation_ids": paragraph.citation_ids,
                "statute_ids": paragraph.statute_ids,
                "tag_ids": paragraph.tag_ids,
                "is_heading": paragraph.is_heading,
            }
            for paragraph in paragraphs
        ],
        "continuity": [component.__dict__ for component in continuity],
        "discussion_units": [
            {
                "discussion_unit_id": unit.discussion_unit_id,
                "start_paragraph": unit.start_paragraph,
                "end_paragraph": unit.end_paragraph,
                "paragraph_count": len(unit.paragraphs),
                "citation_counts": unit.citation_counts,
                "statute_counts": unit.statute_counts,
                "tag_counts": unit.tag_counts,
                "text": unit.text,
                "text_sha256": unit.text_sha256,
                "generation_method": unit.generation_method,
                "generation_version": unit.generation_version,
                "config_hash": unit.config_hash,
                "subthemes": [
                    {
                        "subtheme_id": subtheme.subtheme_id,
                        "subtheme_index": subtheme.subtheme_index,
                        "paragraph_indices": subtheme.paragraph_indices,
                        "key_terms": subtheme.key_terms,
                        "display_key_terms": subtheme.display_key_terms,
                        "argument_roles": subtheme.argument_roles,
                        "explanation": subtheme.explanation,
                        "text": subtheme.text,
                        "text_sha256": subtheme.text_sha256,
                        "config_hash": subtheme.config_hash,
                        "method": subtheme.method,
                        "version": subtheme.version,
                        "argument_evidence": [
                            {
                                "paragraph_index": evidence.paragraph_index,
                                "chunk_id": evidence.chunk_id,
                                "start_offset": evidence.start_offset,
                                "end_offset": evidence.end_offset,
                                "text": evidence.text,
                                "role": evidence.role,
                                "cue": evidence.cue,
                                "rationale": evidence.rationale,
                                "source_text_hash": evidence.source_text_hash,
                                "context_start_offset": evidence.context_start_offset,
                                "context_end_offset": evidence.context_end_offset,
                                "context_text": evidence.context_text,
                                "method": evidence.method,
                                "version": evidence.version,
                            }
                            for evidence in subtheme.argument_evidence
                        ],
                    }
                    for subtheme in subthemes_by_unit[unit.discussion_unit_id]
                ],
            }
            for unit in units
        ],
        "canonical_writes": 0,
        "contextual_writes": 0,
    }


def _render_markdown(report: dict[str, Any], *, max_unit_text_chars: int = 20000) -> str:
    if max_unit_text_chars < 1:
        raise ValueError("max_unit_text_chars must be positive")
    paragraph_source = report.get("paragraph_source", "CaseChunk rows")
    paragraph_hashes = report.get("paragraphs", ())
    lines = [
        f"# Discussion Units: case {report['case_id']}",
        "",
        f"> Read-only inspection. Units are derived from existing `{paragraph_source}`; no canonical rows were written.",
        "",
        "## Deterministic reading",
        "",
        "This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.",
        "The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.",
        "",
        f"- Paragraph-like inputs: **{report['paragraph_count']}**",
        f"- Continuity pairs: **{report['continuity_count']}**",
        f"- Discussion Units: **{report['discussion_unit_count']}**",
        f"- Paragraph source hashes: **{len(paragraph_hashes)}**",
        f"- Sub-themes: **{sum(len(unit.get('subthemes', ())) for unit in report['discussion_units'])}**",
        "",
    ]
    for unit in report["discussion_units"]:
        lines.extend(
            [
                f"## {unit['discussion_unit_id']} · paragraphs {unit['start_paragraph']}-{unit['end_paragraph']}",
                "",
                f"- Citations: `{json.dumps(unit['citation_counts'], sort_keys=True)}`",
                f"- Statutes: `{json.dumps(unit['statute_counts'], sort_keys=True)}`",
                f"- Tags: `{json.dumps(unit['tag_counts'], sort_keys=True)}`",
                f"- Source hash: `{unit['text_sha256']}`",
                "",
            ]
        )
        if unit.get("subthemes"):
            lines.extend([
                "### Deterministic evidence spans",
                "",
                "These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.",
                "",
            ])
            for subtheme in unit["subthemes"]:
                lines.extend(
                    [
                        f"#### {subtheme['subtheme_id']} · paragraphs {subtheme['paragraph_indices'][0]}-{subtheme['paragraph_indices'][-1]}",
                        "",
                        f"- Raw key terms: `{', '.join(subtheme['key_terms']) or 'none'}`",
                        f"- Display key terms: `{', '.join(subtheme.get('display_key_terms', subtheme['key_terms'])) or 'none'}`",
                        f"- Argument roles: `{', '.join(subtheme['argument_roles']) or 'none'}`",
                        f"- Explanation: {subtheme.get('explanation', 'No deterministic explanation recorded.')}",
                    ]
                )
                for evidence in subtheme["argument_evidence"]:
                    lines.append(
                        f"- Evidence: `{evidence['role']}` cue `{evidence['text']}` at chunk `{evidence['chunk_id']}` offsets `{evidence['start_offset']}-{evidence['end_offset']}`; context: {evidence['context_text']}"
                    )
                lines.append("")
        unit_text = unit["text"]
        if len(unit_text) > max_unit_text_chars:
            unit_text = (
                unit_text[:max_unit_text_chars]
                + f"\n\n[Section text truncated at {max_unit_text_chars} characters; full text and hashes remain in JSON.]\n"
            )
        lines.extend(["#### Section text", "", unit_text, ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect deterministic Discussion Units without database writes.")
    parser.add_argument("--case-id", required=True, type=int)
    parser.add_argument("--chunk-set", default="heading_chunks")
    parser.add_argument("--threshold", type=float, default=0.35)
    parser.add_argument("--consecutive-low-scores", type=int, default=2)
    parser.add_argument("--output-json", type=Path)
    parser.add_argument("--output-markdown", type=Path)
    parser.add_argument("--max-unit-text-chars", type=int, default=20000)
    args = parser.parse_args()
    if not 0 <= args.threshold <= 1:
        parser.error("--threshold must be between 0 and 1")
    if args.consecutive_low_scores < 1:
        parser.error("--consecutive-low-scores must be positive")
    if args.max_unit_text_chars < 1:
        parser.error("--max-unit-text-chars must be positive")
    with SessionLocal() as session:
        report = inspect_case(session, args.case_id, args.chunk_set, args.threshold, args.consecutive_low_scores)
    payload = {"status": "dry_run", **report}
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.output_markdown:
        args.output_markdown.parent.mkdir(parents=True, exist_ok=True)
        args.output_markdown.write_text(
            _render_markdown(payload, max_unit_text_chars=args.max_unit_text_chars),
            encoding="utf-8",
        )
    print(json.dumps({key: payload[key] for key in ("status", "case_id", "paragraph_count", "discussion_unit_count", "canonical_writes", "contextual_writes")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())