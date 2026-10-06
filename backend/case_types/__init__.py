"""Deterministic case-type labels ("what kind of case is this"). No AI at any point."""

from .classifier import (
    STATUS_CLASSIFIED,
    STATUS_INSUFFICIENT,
    STATUS_NOT_IMMIGRATION,
    STATUS_UNCLEAR,
    CaseTypeResult,
    classify_text,
)
from .taxonomy import CASE_TYPES, TAXONOMY_VERSION, TYPES_BY_KEY, CaseType

__all__ = [
    "CASE_TYPES",
    "CaseType",
    "CaseTypeResult",
    "STATUS_CLASSIFIED",
    "STATUS_INSUFFICIENT",
    "STATUS_NOT_IMMIGRATION",
    "STATUS_UNCLEAR",
    "TAXONOMY_VERSION",
    "TYPES_BY_KEY",
    "classify_text",
]
