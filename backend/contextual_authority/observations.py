from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Sequence

from backend.metadata_outcomes import _GOVERNMENT_PARTY_RE, _OUTCOME_PATTERNS

from .models import ContextSegment, ContextUnit, text_hash

OBSERVATION_METHOD_VERSION = "deterministic_observations_v1"

_ISSUE_PATTERNS: tuple[tuple[str, re.Pattern[str], float], ...] = (
    ("procedural_fairness", re.compile(r"\bprocedural\s+fairness\b", re.IGNORECASE), 0.82),
    ("credibility", re.compile(r"\bcredibility\b", re.IGNORECASE), 0.80),
    ("state_protection", re.compile(r"\bstate\s+protection\b", re.IGNORECASE), 0.78),
    ("internal_flight_alternative", re.compile(r"\binternal\s+flight\s+alternative\b", re.IGNORECASE), 0.78),
    ("non_refoulement", re.compile(r"\bnon[- ]refoulement\b", re.IGNORECASE), 0.76),
    ("detention", re.compile(r"\bdetention\b", re.IGNORECASE), 0.76),
)


@dataclass(frozen=True)
class ContextObservation:
    case_id: int
    method: str
    method_version: str
    config_hash: str
    variant_key: str
    segment_ordinal: int
    chunk_id: int
    cue_category: str
    cue_label: str
    confidence: float
    evidence_start: int
    evidence_end: int
    evidence_sha256: str
    source_rule: str
    citation_ids: tuple[int, ...] = ()


def _observation(
    unit: ContextUnit,
    segment: ContextSegment,
    label: str,
    category: str,
    confidence: float,
    start: int,
    end: int,
    source_rule: str,
) -> ContextObservation:
    return ContextObservation(
        case_id=unit.case_id,
        method=unit.method,
        method_version=OBSERVATION_METHOD_VERSION,
        config_hash=unit.config_hash,
        variant_key=unit.variant_key,
        segment_ordinal=segment.ordinal,
        chunk_id=segment.chunk_id,
        cue_category=category,
        cue_label=label,
        confidence=confidence,
        evidence_start=start,
        evidence_end=end,
        evidence_sha256="",
        source_rule=source_rule,
        citation_ids=unit.citation_ids,
    )


def extract_segment_observations(
    unit: ContextUnit,
    segment: ContextSegment,
    chunk_text: str,
) -> list[ContextObservation]:
    """Extract transparent, chunk-local cues from one immutable context segment."""
    segment_text = chunk_text[segment.start_offset : segment.end_offset]
    observations: list[ContextObservation] = []
    for label, pattern in _OUTCOME_PATTERNS:
        match = pattern.search(segment_text)
        if match:
            observations.append(
                _observation(
                    unit,
                    segment,
                    label,
                    "disposition_cue",
                    0.75,
                    segment.start_offset + match.start(),
                    segment.start_offset + match.end(),
                    "metadata_outcomes._OUTCOME_PATTERNS",
                )
            )
    for label, pattern, confidence in _ISSUE_PATTERNS:
        for match in pattern.finditer(segment_text):
            observations.append(
                _observation(
                    unit,
                    segment,
                    label,
                    "issue_cue",
                    confidence,
                    segment.start_offset + match.start(),
                    segment.start_offset + match.end(),
                    "contextual_authority._ISSUE_PATTERNS",
                )
            )
    for match in _GOVERNMENT_PARTY_RE.finditer(segment_text):
        observations.append(
            _observation(
                unit,
                segment,
                "government_party_mentioned",
                "authority_role_cue",
                0.70,
                segment.start_offset + match.start(),
                segment.start_offset + match.end(),
                "metadata_outcomes._GOVERNMENT_PARTY_RE",
            )
        )
    return [
        observation.__class__(
            **{
                **observation.__dict__,
                "evidence_sha256": text_hash(chunk_text[observation.evidence_start : observation.evidence_end]),
            }
        )
        for observation in observations
    ]


def extract_context_observations(
    unit: ContextUnit,
    chunks_by_id: dict[int, str],
) -> list[ContextObservation]:
    """Extract observations for every unit segment without mutating source inputs."""
    observations: list[ContextObservation] = []
    for segment in unit.segments:
        chunk_text = chunks_by_id.get(segment.chunk_id)
        if chunk_text is None:
            raise KeyError(f"missing canonical chunk text for chunk {segment.chunk_id}")
        observations.extend(extract_segment_observations(unit, segment, chunk_text))
    return observations
