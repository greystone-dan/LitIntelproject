from __future__ import annotations

from collections.abc import Callable

from .models import CitationCandidate
from .rules import RuleFn, default_rules


def _rank(candidate: CitationCandidate) -> tuple[float, int]:
    # Higher confidence first, then longer spans.
    return (candidate.confidence, candidate.offset_end - candidate.offset_start)


def _overlaps(a: CitationCandidate, b: CitationCandidate) -> bool:
    return not (a.offset_end <= b.offset_start or b.offset_end <= a.offset_start)


def _select_non_overlapping(candidates: list[CitationCandidate]) -> list[CitationCandidate]:
    accepted: list[CitationCandidate] = []
    for cand in sorted(candidates, key=lambda c: (-_rank(c)[0], -_rank(c)[1], c.offset_start)):
        if any(_overlaps(cand, seen) for seen in accepted):
            continue
        accepted.append(cand)
    accepted.sort(key=lambda c: (c.offset_start, c.offset_end))
    return accepted


class CitationExtractionPipeline:
    def __init__(self, rules: list[RuleFn] | None = None):
        self._rules = rules or default_rules()

    def extract(self, text: str | None) -> list[CitationCandidate]:
        content = text or ""
        if not content.strip():
            return []

        all_candidates: list[CitationCandidate] = []
        for rule in self._rules:
            try:
                all_candidates.extend(rule(content))
            except Exception:
                # Rule failures should not fail the entire extraction pass.
                continue

        deduped: dict[tuple[int, int, str, str], CitationCandidate] = {}
        for cand in all_candidates:
            key = cand.key()
            prev = deduped.get(key)
            if prev is None or _rank(cand) > _rank(prev):
                deduped[key] = cand

        return _select_non_overlapping(list(deduped.values()))


def build_default_pipeline() -> CitationExtractionPipeline:
    return CitationExtractionPipeline()
