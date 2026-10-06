"""Turn a stored case_type_labels row into what the site shows. Reads stored data only; no classification, no AI."""

from __future__ import annotations

import re
from typing import Any

from .classifier import STATUS_CLASSIFIED
from .taxonomy import TAXONOMY_VERSION, TYPES_BY_KEY

_CONVENTION_RE = re.compile(r"^1[A-F](?:\(|$)")


def provision_text(detail: str | None) -> str | None:
    """'34(1)(f)' -> 's. 34(1)(f)'; '1F(b)' -> 'Art. 1F(b)'."""
    if not detail:
        return None
    detail = detail.strip()
    if _CONVENTION_RE.match(detail):
        return f"Art. {detail}"
    return f"s. {detail}"


def _entry(key: str | None, detail: str | None) -> dict[str, Any] | None:
    case_type = TYPES_BY_KEY.get(key or "")
    if case_type is None:
        return None
    return {"key": case_type.key, "label": case_type.label, "group": case_type.group, "provision": provision_text(detail)}


def case_type_payload(row: Any) -> dict[str, Any] | None:
    """The reader/search payload for one stored label row, or None when nothing should be shown.

    Unclear, not-immigration and too-short decisions show nothing; so does a row from another taxonomy version.
    """
    if row is None or getattr(row, "taxonomy_version", None) != TAXONOMY_VERSION:
        return None
    if getattr(row, "status", None) != STATUS_CLASSIFIED:
        return None
    primary = _entry(row.primary_type, row.primary_detail)
    if primary is None:
        return None
    payload: dict[str, Any] = {"primary": primary, "second": _entry(getattr(row, "second_type", None), getattr(row, "second_detail", None))}
    payload["issues"] = list(getattr(row, "issues", None) or [])
    return payload
