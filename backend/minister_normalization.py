"""
Normalization for Minister/Government Party names extracted from case titles.

This module provides a mapping-based approach to clean up and normalize
minister and government party names extracted from Canadian case titles.

The canonical source is case title parsing, format: "Canada (Party/Minister Name)"
"""

from functools import lru_cache
from typing import Callable

# Typo and variation mappings to canonical forms
_TYPO_MAPPINGS = {
    # Variations on main department
    'Citizenship & Immigration Canada': 'Citizenship and Immigration Canada',
    'Citizenship and Immigration Canada': 'Citizenship and Immigration Canada',
    'Citizensh. & Immigration Canada': 'Citizenship and Immigration Canada',
    'Citizenship, Immigration Canada': 'Citizenship and Immigration Canada',
    'Citizenship & Immig. Canada': 'Citizenship and Immigration Canada',

    # Immigration, Refugees and Citizenship Canada variations
    'Immigration Refugees Citizenship Canada': 'Immigration, Refugees and Citizenship Canada',
    'Immigration, Refugees and Citizenship Canada': 'Immigration, Refugees and Citizenship Canada',
    'Immigration, Refugees & Citizenship Canada': 'Immigration, Refugees and Citizenship Canada',
    'Immig. Refugees & Citizenship Canada': 'Immigration, Refugees and Citizenship Canada',
    'Immig. Ref. & Citizenship Canada': 'Immigration, Refugees and Citizenship Canada',
    'Immig. Refugees & Citizenship': 'Immigration, Refugees and Citizenship Canada',
    'Immigration Refugees & Citizenship': 'Immigration, Refugees and Citizenship Canada',
    'IRCC': 'Immigration, Refugees and Citizenship Canada',

    # CIC (older name)
    'CIC': 'Citizenship and Immigration Canada',

    # Minister titles with variations
    'Minister of Immigration, Refugees and Citizenship': 'Minister of Immigration, Refugees and Citizenship',
    'Minister of Immigration, Refugees & Citizenship': 'Minister of Immigration, Refugees and Citizenship',
    'Minister Immigration Refugees Citizenship': 'Minister of Immigration, Refugees and Citizenship',
    'Minister Immig. Refugees Citizenship': 'Minister of Immigration, Refugees and Citizenship',
    'Minister of Citizenship and Immigration': 'Minister of Citizenship and Immigration',
    'Minister Citizenship Immigration': 'Minister of Citizenship and Immigration',
    'Minister of Immigration': 'Minister of Immigration, Refugees and Citizenship',  # Use current form
    'Minister Immigration': 'Minister of Immigration, Refugees and Citizenship',
    'Min. of Immigration': 'Minister of Immigration, Refugees and Citizenship',
    'Min. of Citizenship': 'Minister of Citizenship and Immigration',

    # Other government parties
    'Canada': 'Canada',
    'Canada (Government)': 'Canada',
    'Government of Canada': 'Canada',
    'Attorney General of Canada': 'Attorney General of Canada',
    'Minister of Public Safety and Emergency Preparedness': 'Minister of Public Safety and Emergency Preparedness',
    'Canada Border Services Agency': 'Canada Border Services Agency',
    'CBSA': 'Canada Border Services Agency',
}

# Set of canonical immigration-related parties
_IMMIGRATION_PARTIES = {
    'Citizenship and Immigration Canada',
    'Immigration, Refugees and Citizenship Canada',
    'Minister of Citizenship and Immigration',
    'Minister of Immigration, Refugees and Citizenship',
    'Canada',
    'Attorney General of Canada',
    'Minister of Public Safety and Emergency Preparedness',
    'Canada Border Services Agency',
}


def normalize_minister_name(raw_name: str | None) -> str | None:
    """
    Normalize a minister/party name extracted from a case title.

    Returns the normalized canonical form, or None if empty/invalid.
    """
    if not raw_name or not isinstance(raw_name, str):
        return None

    trimmed = raw_name.strip()
    if not trimmed:
        return None

    # Check direct mappings first
    if trimmed in _TYPO_MAPPINGS:
        return _TYPO_MAPPINGS[trimmed]

    # Try case-insensitive match
    lower_name = trimmed.lower()
    for key, canonical in _TYPO_MAPPINGS.items():
        if key.lower() == lower_name:
            return canonical

    # If no mapping found, return the trimmed original
    # (allows for legitimate new parties to pass through)
    return trimmed


@lru_cache(maxsize=1)
def get_canonical_ministers() -> list[str]:
    """
    Get the set of canonical immigration-related minister/party names.

    These are the "approved" values that should appear in filters.
    """
    return sorted(_IMMIGRATION_PARTIES)


def filter_to_immigration_parties(name: str | None) -> bool:
    """
    Determine if a minister/party name is immigration-related.

    Used to filter out non-relevant parties from the search UI.
    """
    if not name:
        return False

    lower_name = name.lower()

    # Check against canonical set
    for canonical in _IMMIGRATION_PARTIES:
        if canonical.lower() == lower_name:
            return True

    # Check for immigration-related keywords
    keywords = ['immig', 'citizen', 'refugee', 'border', 'ircc', 'cic']
    if any(kw in lower_name for kw in keywords):
        return True

    # Check for government party names
    if lower_name in {'canada', 'government'}:
        return True

    return False


def apply_normalization_to_list(
    raw_ministers: list[str],
    normalize_fn: Callable[[str | None], str | None] | None = None,
    filter_fn: Callable[[str | None], bool] | None = None,
) -> list[str]:
    """
    Apply normalization and filtering to a list of minister names.

    Args:
        raw_ministers: List of minister names extracted from case titles
        normalize_fn: Function to normalize names (default: normalize_minister_name)
        filter_fn: Function to filter names (default: filter_to_immigration_parties)

    Returns:
        Sorted list of unique, normalized, filtered minister names
    """
    if normalize_fn is None:
        normalize_fn = normalize_minister_name
    if filter_fn is None:
        filter_fn = filter_to_immigration_parties

    normalized = set()
    for name in raw_ministers:
        norm = normalize_fn(name)
        if norm and filter_fn(norm):
            normalized.add(norm)

    return sorted(normalized)
