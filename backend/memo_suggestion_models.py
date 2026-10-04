"""Additive, descriptive memo-authority response contracts."""

from pydantic import BaseModel, Field


class SuggestionSignals(BaseModel):
    tags: list[str] = Field(default_factory=list)
    statutes: list[str] = Field(default_factory=list)


class SuggestionWhy(BaseModel):
    shared_tags: list[str] = Field(default_factory=list)
    shared_statutes: list[str] = Field(default_factory=list)


class SuggestionOutcomes(BaseModel):
    won: int
    lost: int
    mixed: int
    unclassified: int
    denominator: int


class AuthoritySuggestion(BaseModel):
    id: int
    title: str
    citation: str | None = None
    citing_decisions: int
    cohort_denominator: int
    why: SuggestionWhy
    outcomes: SuggestionOutcomes


class SuggestionCoverage(BaseModel):
    partial: bool = False
    cohort_limit: int = 500
    citation_edge_limit: int = 10000
    cohort_truncated: bool = False
    citation_edges_truncated: bool = False
    citation_edges_checked: int = 0
    missing_total: int = 0
    contrary_total: int = 0
    missing_truncated: bool = False
    contrary_truncated: bool = False
    outcome_source: str = "cases.metadata_json.reader_extracted.government outcome"
    note: str = "Counts describe the checked cohort, not all decisions."


class MemoAuthoritySuggestions(BaseModel):
    disclaimer: str = "Suggestions, not legal advice"
    status: str = "session_unavailable"
    signals: SuggestionSignals = Field(default_factory=SuggestionSignals)
    cohort_denominator: int = 0
    missing: list[AuthoritySuggestion] = Field(default_factory=list)
    contrary: list[AuthoritySuggestion] = Field(default_factory=list)
    contrary_hidden_below_threshold: int = 0
    coverage: SuggestionCoverage = Field(default_factory=SuggestionCoverage)
