from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class CitationCandidate:
    kind: str
    citation_text: str
    normalized_citation: str
    offset_start: int
    offset_end: int
    confidence: float = 0.5
    source_rule: str = "unknown"
    metadata: dict[str, Any] = field(default_factory=dict)

    def span(self) -> tuple[int, int]:
        return (self.offset_start, self.offset_end)

    def key(self) -> tuple[int, int, str, str]:
        return (
            self.offset_start,
            self.offset_end,
            self.kind,
            self.normalized_citation.lower(),
        )
