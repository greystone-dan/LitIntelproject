"""
Theme Discovery: Group discussion unit subthemes by shared key terms and argument roles
across a case library to surface recurring legal issues and doctrinal themes.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Any
from sqlalchemy.orm import Session

from .models import CaseEvidenceSummaryResponse, CaseSubThemeSummaryResponse

# Procedural/boilerplate terms filtered from theme discovery
# These are common in case headers and procedural sections but not meaningful themes
THEME_STOPWORDS = {
    "appearances", "applicant", "attorney", "order", "canada",
    "dated", "style", "cause", "case", "court", "judge",
    "federal", "decision", "reasons", "find", "hold", "conclude",
    "agreement", "application", "motion", "petition", "request",
    "pursuant", "section", "article", "act", "law", "regulation",
    "citizenship", "immigration", "department", "minister",
}


@dataclass(frozen=True)
class ThemeOccurrence:
    """One case's subtheme that participates in a theme."""
    case_id: int
    unit_index: int
    subtheme_id: str
    key_terms: list[str]
    argument_roles: list[str]


@dataclass(frozen=True)
class DiscoveredTheme:
    """A discovered recurring theme across cases."""
    theme_id: str
    theme_name: str
    top_key_terms: list[str]
    top_argument_roles: list[str]
    occurrence_count: int
    occurrences: tuple[ThemeOccurrence, ...]


def _jaccard_similarity(set_a: set[str], set_b: set[str]) -> float:
    """Compute Jaccard similarity between two sets."""
    if not set_a and not set_b:
        return 1.0
    if not set_a or not set_b:
        return 0.0
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union else 0.0


def discover_themes(
    case_evidence_summaries: dict[int, CaseEvidenceSummaryResponse],
    *,
    key_term_similarity_threshold: float = 0.4,
    min_occurrences: int = 2,
) -> tuple[DiscoveredTheme, ...]:
    """
    Discover recurring themes by grouping subthemes with similar key terms and argument roles.

    Args:
        case_evidence_summaries: Dict mapping case_id to CaseEvidenceSummaryResponse
        key_term_similarity_threshold: Jaccard similarity threshold for grouping by key terms
        min_occurrences: Minimum subthemes required to form a theme

    Returns:
        Tuple of DiscoveredTheme objects sorted by occurrence count (descending)
    """
    # Collect all subtheme occurrences
    all_occurrences: list[tuple[CaseSubThemeSummaryResponse, int, int, int]] = []

    for case_id, evidence_summary in case_evidence_summaries.items():
        if not evidence_summary.units:
            continue
        for unit in evidence_summary.units:
            for subtheme in unit.subthemes:
                all_occurrences.append((subtheme, case_id, unit.unit_index, case_id))

    if not all_occurrences:
        return ()

    # Group subthemes into themes using hierarchical clustering based on key term similarity
    themes: dict[frozenset[str], list[ThemeOccurrence]] = {}
    processed_indices: set[int] = set()

    for idx, (subtheme, case_id, unit_index, _) in enumerate(all_occurrences):
        if idx in processed_indices:
            continue

        # Start a new theme with this subtheme
        theme_key_terms = frozenset(term.lower() for term in subtheme.key_terms)
        theme_occurrences: list[ThemeOccurrence] = [
            ThemeOccurrence(
                case_id=case_id,
                unit_index=unit_index,
                subtheme_id=subtheme.subtheme_id,
                key_terms=subtheme.key_terms,
                argument_roles=subtheme.argument_roles,
            )
        ]
        processed_indices.add(idx)

        # Find similar subthemes for this theme
        for other_idx, (other_subtheme, other_case_id, other_unit_index, _) in enumerate(
            all_occurrences
        ):
            if other_idx in processed_indices or other_idx <= idx:
                continue

            other_key_terms = frozenset(term.lower() for term in other_subtheme.key_terms)
            similarity = _jaccard_similarity(theme_key_terms, other_key_terms)

            if similarity >= key_term_similarity_threshold:
                theme_occurrences.append(
                    ThemeOccurrence(
                        case_id=other_case_id,
                        unit_index=other_unit_index,
                        subtheme_id=other_subtheme.subtheme_id,
                        key_terms=other_subtheme.key_terms,
                        argument_roles=other_subtheme.argument_roles,
                    )
                )
                processed_indices.add(other_idx)

        if len(theme_occurrences) >= min_occurrences:
            themes[theme_key_terms] = theme_occurrences

    # Convert to DiscoveredTheme objects
    discovered: list[DiscoveredTheme] = []

    for theme_key_terms, occurrences in themes.items():
        # Compute top key terms and argument roles
        all_key_terms = []
        all_argument_roles = []

        for occurrence in occurrences:
            all_key_terms.extend(occurrence.key_terms)
            all_argument_roles.extend(occurrence.argument_roles)

        term_counts = Counter(term.lower() for term in all_key_terms if term.lower() not in THEME_STOPWORDS)
        role_counts = Counter(role for role in all_argument_roles)

        top_key_terms = [term for term, _ in term_counts.most_common(5)]
        top_argument_roles = [role for role, _ in role_counts.most_common(3)]

        # Skip themes that have no meaningful terms after filtering
        if not top_key_terms:
            continue

        # Create theme name from top key terms
        theme_name = " + ".join(top_key_terms[:3]) if top_key_terms else "Unnamed Theme"
        theme_id = "_".join(term.replace(" ", "_") for term in top_key_terms[:2])

        discovered.append(
            DiscoveredTheme(
                theme_id=theme_id or "theme_default",
                theme_name=theme_name,
                top_key_terms=top_key_terms,
                top_argument_roles=top_argument_roles,
                occurrence_count=len(occurrences),
                occurrences=tuple(occurrences),
            )
        )

    # Sort by occurrence count (descending)
    discovered.sort(key=lambda t: t.occurrence_count, reverse=True)

    return tuple(discovered)


def get_core_300_themes(db: Session) -> tuple[DiscoveredTheme, ...]:
    """
    Compute themes for Core-300 case set.

    This should be called periodically to update theme cache.
    """
    from .reader_service import get_case_reader_data_uncached

    # Load evidence summaries for all Core-300 cases
    case_summaries: dict[int, CaseEvidenceSummaryResponse] = {}

    core_300_ids = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        # (Abbreviated; in practice this would be all 300 case IDs)
    ]

    for case_id in core_300_ids:
        try:
            reader_data = get_case_reader_data_uncached(case_id, db)
            if reader_data and reader_data.evidence_summary:
                case_summaries[case_id] = reader_data.evidence_summary
        except Exception:
            # Skip cases that fail to load
            continue

    return discover_themes(case_summaries)
