"""Derived intelligence layer for case records.

This module owns the derivation of higher-level *intelligence* fields that are
inferred from decision text rather than scraped verbatim from the source
document: decision outcome, government role/result, and case
type/challenge/issue/topic. It composes the outcome helpers in
`backend.metadata_outcomes` with the subject helpers in
`backend.metadata_subjects` and exposes them as a single derivation pass.

The deterministic source-extracted fields live behind `backend.metadata`,
which composes this layer. Downstream consumers keep reading the derived
values from the stored `metadata_json->'reader_extracted'` payload, so the
storage path and payload shape are unchanged.
"""

from __future__ import annotations

from .metadata_outcomes import _derive_outcome_fields, derive_outcome_detail
from .metadata_subjects import _derive_case_subject_fields


INTELLIGENCE_FIELDS = (
	"decision outcome",
	"government role",
	"government outcome",
	"case winner",
	"case loser",
	"outcome status",
	"case type",
	"case challenge",
	"case issue",
	"challenged issue",
	"challenged issues",
	"case topic",
)


def derive_intelligence_fields(content: str, metadata: dict) -> dict[str, tuple[str, float]]:
	"""Combine every derived intelligence-field group into a single mapping.

	Runs outcome/government-role derivation first, then subject derivation,
	and returns a field -> (value, confidence) mapping. This is the same
	derivation previously performed inline by `backend.metadata`.
	"""
	derived = _derive_outcome_fields(content, metadata)
	derived.update(_derive_case_subject_fields(content, metadata))
	return derived


def derive_outcome_payload(content: str, metadata: dict) -> dict[str, object]:
	return derive_outcome_detail(content, metadata)
