from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from hashlib import sha256
from typing import Any


def text_hash(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class SnapshotSpec:
    code_sha: str
    method_set_version: str
    config: dict[str, Any]
    cohort_hash: str
    snapshot_id: str
    status: str = "staged"
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    @property
    def config_hash(self) -> str:
        import json

        payload = json.dumps(self.config, sort_keys=True, separators=(",", ":"))
        return text_hash(payload)


@dataclass(frozen=True)
class ChunkInput:
    case_id: int
    chunk_id: int
    ordinal: int
    text: str
    citation_ids: tuple[int, ...] = ()
    chunk_set: str = "heading_chunks"

    @property
    def text_sha256(self) -> str:
        return text_hash(self.text)


@dataclass(frozen=True)
class CitationInput:
    citation_id: int
    chunk_id: int | None
    offset_start: int | None
    offset_end: int | None


@dataclass(frozen=True)
class ContextSegment:
    ordinal: int
    chunk_id: int
    start_offset: int
    end_offset: int
    text_sha256: str


@dataclass(frozen=True)
class ContextUnit:
    case_id: int
    method: str
    method_version: str
    config_hash: str
    variant_key: str
    segments: tuple[ContextSegment, ...]
    citation_ids: tuple[int, ...] = ()

    @property
    def text_sha256(self) -> str:
        payload = "\n".join(
            f"{segment.chunk_id}:{segment.start_offset}:{segment.end_offset}:{segment.text_sha256}"
            for segment in self.segments
        )
        return text_hash(payload)
