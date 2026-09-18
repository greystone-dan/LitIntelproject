from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import json
import re
from typing import Sequence

from .models import text_hash


DISCUSSION_UNIT_METHOD = "discussion_unit_v1"
DISCUSSION_UNIT_VERSION = "1.2"
_CONTENT_STOPWORDS = frozenset(
    "a an and are as at be been being by for from had has have he her his in is it its may of on or that the their them they this to was were will with would".split()
)
_CONTENT_WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9'-]{2,}")


@dataclass(frozen=True)
class ParagraphFeatures:
    case_id: int
    chunk_id: int
    paragraph_index: int
    start_offset: int
    end_offset: int
    text: str
    source_text_hash: str = ""
    source_paragraph_index: int = -1
    citation_ids: tuple[int, ...] = ()
    statute_ids: tuple[int, ...] = ()
    tag_ids: tuple[str, ...] = ()
    is_heading: bool = False

    def __post_init__(self) -> None:
        if self.start_offset < 0 or self.start_offset >= self.end_offset:
            raise ValueError("paragraph offsets must be a non-empty span")
        if not self.text:
            raise ValueError("paragraph text must not be empty")
        if self.end_offset - self.start_offset != len(self.text):
            raise ValueError("paragraph offsets must match text length")
        if self.source_text_hash and len(self.source_text_hash) != 64:
            raise ValueError("source text hash must be a SHA-256 hex digest")

    @property
    def text_sha256(self) -> str:
        return text_hash(self.text)

    @property
    def source_sha256(self) -> str:
        return self.source_text_hash or self.text_sha256

    @property
    def authority_density(self) -> float:
        return len(set(self.citation_ids)) / max(1, len(self.text.split()))

    @property
    def statute_density(self) -> float:
        return len(set(self.statute_ids)) / max(1, len(self.text.split()))

    @property
    def tag_density(self) -> float:
        return len(set(self.tag_ids)) / max(1, len(self.text.split()))


@dataclass(frozen=True)
class ContinuityComponents:
    left_paragraph_index: int
    right_paragraph_index: int
    authority_overlap: float
    statute_overlap: float
    tag_overlap: float
    text_overlap: float
    heading_boundary_penalty: float
    signal_density_shift: float
    continuity_score: float


@dataclass(frozen=True)
class DiscussionUnit:
    case_id: int
    unit_index: int
    paragraph_indices: tuple[int, ...]
    paragraphs: tuple[ParagraphFeatures, ...]
    generation_method: str = DISCUSSION_UNIT_METHOD
    generation_version: str = DISCUSSION_UNIT_VERSION
    config_hash: str = ""

    @property
    def discussion_unit_id(self) -> str:
        return f"{self.case_id}:{self.unit_index}"

    @property
    def start_paragraph(self) -> int:
        return self.paragraph_indices[0]

    @property
    def end_paragraph(self) -> int:
        return self.paragraph_indices[-1]

    @property
    def text(self) -> str:
        return "\n\n".join(paragraph.text for paragraph in self.paragraphs)

    @property
    def text_sha256(self) -> str:
        return text_hash(self.text)

    @property
    def citation_counts(self) -> dict[int, int]:
        return dict(Counter(citation_id for paragraph in self.paragraphs for citation_id in paragraph.citation_ids))

    @property
    def statute_counts(self) -> dict[int, int]:
        return dict(Counter(statute_id for paragraph in self.paragraphs for statute_id in paragraph.statute_ids))

    @property
    def tag_counts(self) -> dict[str, int]:
        return dict(Counter(tag_id for paragraph in self.paragraphs for tag_id in paragraph.tag_ids))


def _jaccard(left: Sequence[object], right: Sequence[object]) -> float:
    left_set = set(left)
    right_set = set(right)
    union = left_set | right_set
    return len(left_set & right_set) / len(union) if union else 0.0


def _content_words(text: str) -> frozenset[str]:
    return frozenset(
        word
        for word in _CONTENT_WORD_RE.findall(text.casefold())
        if word not in _CONTENT_STOPWORDS
    )


def _text_overlap(left: ParagraphFeatures, right: ParagraphFeatures) -> float:
    return _jaccard(_content_words(left.text), _content_words(right.text))


def _density_shift(left: ParagraphFeatures, right: ParagraphFeatures) -> float:
    left_density = left.authority_density + left.statute_density + left.tag_density
    right_density = right.authority_density + right.statute_density + right.tag_density
    return min(1.0, abs(left_density - right_density))


def compute_continuity(left: ParagraphFeatures, right: ParagraphFeatures) -> ContinuityComponents:
    authority_overlap = _jaccard(left.citation_ids, right.citation_ids)
    statute_overlap = _jaccard(left.statute_ids, right.statute_ids)
    tag_overlap = _jaccard(left.tag_ids, right.tag_ids)
    text_overlap = _text_overlap(left, right)
    heading_boundary_penalty = 1.0 if right.is_heading else 0.0
    signal_density_shift = _density_shift(left, right)
    continuity_score = (
        0.25 * (authority_overlap if left.citation_ids or right.citation_ids else 0.5)
        + 0.15 * (statute_overlap if left.statute_ids or right.statute_ids else 0.5)
        + 0.15 * (tag_overlap if left.tag_ids or right.tag_ids else 0.5)
        + 0.30 * (0.5 + 0.5 * text_overlap)
        + 0.15 * (1.0 - signal_density_shift)
        - 0.50 * heading_boundary_penalty
    )
    return ContinuityComponents(
        left_paragraph_index=left.paragraph_index,
        right_paragraph_index=right.paragraph_index,
        authority_overlap=authority_overlap,
        statute_overlap=statute_overlap,
        tag_overlap=tag_overlap,
        text_overlap=text_overlap,
        heading_boundary_penalty=heading_boundary_penalty,
        signal_density_shift=signal_density_shift,
        continuity_score=max(0.0, min(1.0, continuity_score)),
    )


def segment_discussion_units(
    paragraphs: Sequence[ParagraphFeatures],
    continuity: Sequence[ContinuityComponents],
    *,
    threshold: float = 0.35,
    consecutive_low_scores: int = 2,
    consecutive_signal_vacuum_pairs: int = 8,
    signal_vacuum_text_overlap: float = 0.10,
    signal_vacuum_min_paragraphs: int = 50,
    config: dict[str, object] | None = None,
) -> tuple[DiscussionUnit, ...]:
    if not paragraphs:
        return ()
    if len(continuity) != max(0, len(paragraphs) - 1):
        raise ValueError("continuity must contain one item per adjacent paragraph pair")
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")
    if consecutive_low_scores < 1:
        raise ValueError("consecutive_low_scores must be positive")
    if consecutive_signal_vacuum_pairs < 1:
        raise ValueError("consecutive_signal_vacuum_pairs must be positive")
    if not 0 <= signal_vacuum_text_overlap <= 1:
        raise ValueError("signal_vacuum_text_overlap must be between 0 and 1")
    if signal_vacuum_min_paragraphs < 1:
        raise ValueError("signal_vacuum_min_paragraphs must be positive")

    config_payload = {
        "threshold": threshold,
        "consecutive_low_scores": consecutive_low_scores,
        "consecutive_signal_vacuum_pairs": consecutive_signal_vacuum_pairs,
        "signal_vacuum_text_overlap": signal_vacuum_text_overlap,
        "signal_vacuum_min_paragraphs": signal_vacuum_min_paragraphs,
        **(config or {}),
    }
    config_hash = text_hash(json.dumps(config_payload, sort_keys=True, separators=(",", ":")))
    boundaries = {0}
    low_score_count = 0
    signal_vacuum_count = 0
    signal_vacuum_active = False
    for index, component in enumerate(continuity, 1):
        left = paragraphs[index - 1]
        right = paragraphs[index]
        has_signal = bool(
            left.citation_ids
            or left.statute_ids
            or left.tag_ids
            or right.citation_ids
            or right.statute_ids
            or right.tag_ids
        )
        is_signal_vacuum = (
            len(paragraphs) >= signal_vacuum_min_paragraphs
            and not has_signal
            and component.text_overlap < signal_vacuum_text_overlap
        )
        if is_signal_vacuum:
            signal_vacuum_count += 1
            if signal_vacuum_count >= consecutive_signal_vacuum_pairs and not signal_vacuum_active:
                boundaries.add(index - consecutive_signal_vacuum_pairs + 1)
                signal_vacuum_active = True
        else:
            if signal_vacuum_active:
                boundaries.add(index)
            signal_vacuum_count = 0
            signal_vacuum_active = False
        if component.continuity_score < threshold:
            low_score_count += 1
        else:
            low_score_count = 0
        if component.heading_boundary_penalty or low_score_count >= consecutive_low_scores:
            boundaries.add(index)
            low_score_count = 0
    ordered_boundaries = sorted(boundaries) + [len(paragraphs)]
    units = []
    for unit_index, (start, end) in enumerate(zip(ordered_boundaries, ordered_boundaries[1:]), 1):
        selected = tuple(paragraphs[start:end])
        units.append(
            DiscussionUnit(
                case_id=selected[0].case_id,
                unit_index=unit_index,
                paragraph_indices=tuple(paragraph.paragraph_index for paragraph in selected),
                paragraphs=selected,
                config_hash=config_hash,
            )
        )
    return tuple(units)