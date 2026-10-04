"""Conservative, seed-based indicators for possible later legal developments.

The editable event list is not an authoritative or comprehensive statement of law.
"""

from __future__ import annotations

import re
from datetime import date
from typing import Any, Iterable, Mapping


# Keep entries explicit and reviewable. Add an event only when its source and
# effect can be stated accurately; this list intentionally contains one event.
OVERRULING_RISK_SEEDS: list[dict[str, Any]] = [
    {
        "event": "Vavilov standard-of-review framework",
        "case_name": "Canada (Minister of Citizenship and Immigration) v. Vavilov",
        "match_case_names": [
            "Canada (Minister of Citizenship and Immigration) v. Vavilov",
            "Canada (MCI) v. Vavilov",
        ],
        "citation": "2019 SCC 65",
        "match_citations": ["2019 SCC 65"],
        "date": "2019-12-19",
        "source": (
            "Canada (Minister of Citizenship and Immigration) v. Vavilov, "
            "2019 SCC 65 (CanLII), https://canlii.ca/t/j46kb"
        ),
        "rationale": (
            "The Supreme Court of Canada established a revised standard-of-review "
            "framework, displacing the pre-Vavilov framework. This seed identifies "
            "that framework event only; it does not determine whether or how the "
            "framework applies to any particular decision."
        ),
        "notice": "seed list, needs lawyer review.",
    }
]

_CAUTIOUS_ASSESSMENT = (
    "This case may be affected by the listed legal development; this is an "
    "indicator for review, not a legal conclusion."
)
_DIRECT_ASSESSMENT = (
    "This case is itself a listed development authority; other cases may be "
    "affected by this development. This is an indicator for review, not a legal conclusion."
)


def _normalized(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value or "").lower())


def seed_for_case(case: Any) -> dict[str, Any] | None:
    """Return an event only for an exact listed citation or full case-name match."""
    citation = _normalized(getattr(case, "citation", None))
    title = _normalized(getattr(case, "title", None))
    for seed in OVERRULING_RISK_SEEDS:
        citations = {_normalized(value) for value in seed.get("match_citations", [])}
        names = {_normalized(value) for value in seed.get("match_case_names", [])}
        if citation and citation in citations or title and title in names:
            return seed
    return None


def _flag(
    *,
    assignment: str,
    subject_case: Any,
    authority: Any,
    seed: Mapping[str, Any],
    citation: Any | None = None,
) -> dict[str, Any]:
    authority_id = getattr(authority, "id", None)
    subject_id = getattr(subject_case, "id", None)
    flag: dict[str, Any] = {
        "assignment": assignment,
        "event": seed["event"],
        "authority": {
            "case_id": authority_id,
            "title": getattr(authority, "title", seed["case_name"]),
            "citation": getattr(authority, "citation", None) or seed["citation"],
        },
        "source": seed["source"],
        "rationale": seed["rationale"],
        "event_date": seed["date"],
        "decision_date": _date_text(getattr(subject_case, "date", None)),
        "authority_decision_date": _date_text(getattr(authority, "date", None)),
        "notice": seed["notice"],
        "assessment": (
            _DIRECT_ASSESSMENT if assignment == "direct" else _CAUTIOUS_ASSESSMENT
        ),
        "how_assigned": "",
    }
    if assignment == "direct":
        flag["how_assigned"] = (
            "Direct flag: the requested case's citation or full case name matches "
            "an entry in the editable seed list after case and punctuation normalization."
        )
    else:
        flag["citation_relationship"] = {
            "citation_id": getattr(citation, "id", None),
            "source_case_id": getattr(citation, "source_case_id", subject_id),
            "target_case_id": getattr(citation, "target_case_id", authority_id),
            "citation_text": getattr(citation, "citation_text", None),
            "normalized_citation": getattr(citation, "normalized_citation", None),
            "relationship": "stored resolved Citation.source_case_id -> Citation.target_case_id",
        }
        flag["how_assigned"] = (
            "Indirect flag: a stored resolved Citation relationship links the "
            "requested case as source_case_id to this seeded authority as "
            "target_case_id. This relationship is an indicator, not a legal conclusion."
        )
    return flag


def _date_text(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, (date,)):
        return value.isoformat()
    return str(value)


def build_overruling_risk_result(
    requested_case: Any,
    resolved_citations: Iterable[tuple[Any, Any]],
) -> dict[str, Any]:
    """Build a deterministic response from a case and its joined stored citations."""
    direct_seed = seed_for_case(requested_case)
    direct_flags = (
        [
            _flag(
                assignment="direct",
                subject_case=requested_case,
                authority=requested_case,
                seed=direct_seed,
            )
        ]
        if direct_seed
        else []
    )
    indirect_flags: list[dict[str, Any]] = []
    for citation, authority in resolved_citations:
        seed = seed_for_case(authority)
        if seed is not None:
            indirect_flags.append(
                _flag(
                    assignment="indirect",
                    subject_case=requested_case,
                    authority=authority,
                    seed=seed,
                    citation=citation,
                )
            )
    flags = direct_flags + indirect_flags
    return {
        "case": {
            "case_id": getattr(requested_case, "id", None),
            "title": getattr(requested_case, "title", None),
            "citation": getattr(requested_case, "citation", None),
            "decision_date": _date_text(getattr(requested_case, "date", None)),
        },
        "counts": {
            "direct": len(direct_flags),
            "indirect": len(indirect_flags),
            "total": len(flags),
        },
        "flags": flags,
        "notice": "Seeded indicators only; seed list, needs lawyer review.",
        "assessment": (
            _CAUTIOUS_ASSESSMENT
            if indirect_flags
            else _DIRECT_ASSESSMENT
            if direct_flags
            else "No seeded indicator matched; this is not a determination of legal effect."
        ),
    }
