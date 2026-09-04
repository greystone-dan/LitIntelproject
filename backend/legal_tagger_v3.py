"""Inactive exact-match matcher for the proposed Tagging V3 core layer."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path


TAXONOMY_VERSION = "ca_legal_v3_core"
ACTIVE_TAG_TAXONOMY_VERSION = TAXONOMY_VERSION
PROPOSAL_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "eval"
    / "reports"
    / "tagging-v3-core-whitelist-proposal.json"
)


@dataclass(frozen=True)
class CoreTag:
    category: str
    value: str
    score: float
    evidence: str
    offset_start: int | None = None
    offset_end: int | None = None
    rule_id: str | None = None
    language: str = "unknown"
    evidence_role: str = "mention"
    chunk_id: int | None = None
    source: str = "core_whitelist"
    taxonomy_version: str = TAXONOMY_VERSION


def _pattern(*terms: str) -> str:
    return r"(?<!\w)(?:" + "|".join(re.escape(term) for term in terms) + r")(?!\w)"


def load_core_terms() -> dict[str, dict[str, tuple[str, ...]]]:
    proposal = json.loads(PROPOSAL_PATH.read_text(encoding="utf-8"))
    if proposal.get("taxonomy_version") != TAXONOMY_VERSION:
        raise ValueError("V3 proposal taxonomy version does not match the tagger")
    if proposal.get("review_status") != "proposed":
        raise ValueError("V3 proposal must remain explicitly review-only")
    return {
        category: {
            value: tuple(aliases)
            for value, aliases in values.items()
        }
        for category, values in proposal["categories"].items()
    }


class CoreLegalTaggerV3:
    def __init__(self) -> None:
        self._entries = tuple(
            (category, value, re.compile(_pattern(*aliases), re.IGNORECASE))
            for category, values in load_core_terms().items()
            for value, aliases in values.items()
        )

    def tag(self, text: str | None) -> list[CoreTag]:
        return self._tag(text, occurrences=False)

    def tag_occurrences(self, text: str | None) -> list[CoreTag]:
        return self._tag(text, occurrences=True)

    def _tag(self, text: str | None, occurrences: bool) -> list[CoreTag]:
        content = text or ""
        found: list[CoreTag] = []
        for category, value, pattern in self._entries:
            matches = pattern.finditer(content) if occurrences else [pattern.search(content)]
            for match in matches:
                if match is None:
                    continue
                found.append(
                    CoreTag(
                        category,
                        value,
                        1.0,
                        match.group(0),
                        match.start() if occurrences else None,
                        match.end() if occurrences else None,
                        f"{category}.{value}",
                    )
                )
        if occurrences:
            return sorted(
                found,
                key=lambda tag: (
                    tag.offset_start or 0,
                    tag.offset_end or 0,
                    tag.category,
                    tag.value,
                ),
            )
        return sorted(found, key=lambda tag: (tag.category, tag.value))