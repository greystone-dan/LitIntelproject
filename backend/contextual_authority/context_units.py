from __future__ import annotations

from collections import defaultdict
from dataclasses import replace
from typing import Iterable, Mapping, Sequence

from .models import ChunkInput, CitationInput, ContextSegment, ContextUnit, text_hash

DEFAULT_METHOD_VERSION = "phase0.v1"


def _full_segment(chunk: ChunkInput, ordinal: int) -> ContextSegment:
    return ContextSegment(
        ordinal=ordinal,
        chunk_id=chunk.chunk_id,
        start_offset=0,
        end_offset=len(chunk.text),
        text_sha256=chunk.text_sha256,
    )


def _sentence_spans(text: str) -> list[tuple[int, int]]:
    """Return deterministic sentence-like spans without changing source offsets."""
    import re

    spans: list[tuple[int, int]] = []
    start = 0
    boundary = re.compile(r"(?<=[.!?])(?:\"|')?\s+(?=[A-Z0-9\"'])")
    for match in boundary.finditer(text):
        end = match.start() + 1
        if text[start:end].strip():
            spans.append((start, end))
        start = match.end() - 1
    if text[start:].strip():
        spans.append((start, len(text)))
    return spans or ([(0, len(text))] if text else [])


def _citation_map(citations: Iterable[CitationInput]) -> dict[int, list[CitationInput]]:
    by_chunk: dict[int, list[CitationInput]] = defaultdict(list)
    for citation in citations:
        if citation.chunk_id is not None:
            by_chunk[citation.chunk_id].append(citation)
    return by_chunk


def _citation_ids_for_segments(
    segments: Sequence[ContextSegment],
    chunks_by_id: Mapping[int, ChunkInput],
    citations_by_chunk: Mapping[int, Sequence[CitationInput]],
) -> tuple[int, ...]:
    ids: set[int] = set()
    for segment in segments:
        for citation in citations_by_chunk.get(segment.chunk_id, ()):
            start, end = citation.offset_start, citation.offset_end
            if start is None or end is None or start < segment.end_offset and end > segment.start_offset:
                ids.add(citation.citation_id)
    return tuple(sorted(ids))


def _unit(
    chunks: Sequence[ChunkInput],
    method: str,
    variant_key: str,
    config_hash: str,
    citations_by_chunk: Mapping[int, Sequence[CitationInput]],
    method_version: str,
) -> ContextUnit:
    segments = tuple(_full_segment(chunk, index) for index, chunk in enumerate(chunks))
    return ContextUnit(
        case_id=chunks[0].case_id,
        method=method,
        method_version=method_version,
        config_hash=config_hash,
        variant_key=variant_key,
        segments=segments,
        citation_ids=_citation_ids_for_segments(segments, {chunk.chunk_id: chunk for chunk in chunks}, citations_by_chunk),
    )


def build_context_units(
    chunks: Sequence[ChunkInput],
    citations: Sequence[CitationInput] = (),
    *,
    methods: Sequence[str] = ("sentence_v1", "paragraph_v1", "window_p1", "citation_burst_v1"),
    method_version: str = DEFAULT_METHOD_VERSION,
    config_hash: str = "phase0-default",
) -> list[ContextUnit]:
    """Build deterministic, competing context candidates from canonical chunks.

    The function is pure: it never edits chunks or citations and preserves every
    source span as a chunk-local segment.
    """
    ordered = sorted(chunks, key=lambda chunk: (chunk.case_id, chunk.chunk_set, chunk.ordinal, chunk.chunk_id))
    if not ordered:
        return []
    citations_by_chunk = _citation_map(citations)
    units: list[ContextUnit] = []
    for chunk in ordered:
        if "sentence_v1" in methods:
            for sentence_index, (start, end) in enumerate(_sentence_spans(chunk.text)):
                segment = ContextSegment(sentence_index, chunk.chunk_id, start, end, text_hash(chunk.text[start:end]))
                units.append(ContextUnit(chunk.case_id, "sentence_v1", method_version, config_hash, f"chunk:{chunk.chunk_id}:sentence:{sentence_index}", (segment,), _citation_ids_for_segments((segment,), {chunk.chunk_id: chunk}, citations_by_chunk)))
        if "paragraph_v1" in methods:
            units.append(_unit((chunk,), "paragraph_v1", f"chunk:{chunk.chunk_id}", config_hash, citations_by_chunk, method_version))
    if "window_p1" in methods:
        for index, chunk in enumerate(ordered):
            window = ordered[max(0, index - 1) : index + 2]
            units.append(_unit(window, "window_p1", f"anchor:{chunk.chunk_id}", config_hash, citations_by_chunk, method_version))
    if "citation_burst_v1" in methods:
        cited = [chunk for chunk in ordered if citations_by_chunk.get(chunk.chunk_id)]
        burst: list[ChunkInput] = []
        previous_index: int | None = None
        for chunk in cited:
            if previous_index is not None and chunk.ordinal - previous_index > 3 and burst:
                units.append(_unit(tuple(burst), "citation_burst_v1", f"burst:{burst[0].chunk_id}:{burst[-1].chunk_id}", config_hash, citations_by_chunk, method_version))
                burst = []
            burst.append(chunk)
            previous_index = chunk.ordinal
        if burst:
            units.append(_unit(tuple(burst), "citation_burst_v1", f"burst:{burst[0].chunk_id}:{burst[-1].chunk_id}", config_hash, citations_by_chunk, method_version))
    return units
