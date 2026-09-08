"""Report unresolved citation shapes and exact local recovery signals.

The database query is read-only. The report distinguishes exact citation,
canonical-title, alias, self-case, and ambiguous signals so a later writer can
be limited to a measured, precision-safe family.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import _citation_variants, _normalize_alias_lookup, build_local_case_resolution_index
from backend.database import Case, Citation, SessionLocal
from scripts.resolve_citation_targets import _build_title_resolution_index, _citation_title_key
from scripts.resolve_short_citation_targets import (
    PINPOINT_RE,
    REPORTER_SUFFIX_RE,
    _case_alias_index,
)


FORMAL_RE = re.compile(r"\b(?:19|20)\d{2}\s+(?:canlii|[a-z]{1,8}(?:\.[a-z]{1,4})?)\s+\d{1,7}\b", re.IGNORECASE)
NEUTRAL_RE = re.compile(r"\b(?:19|20)\d{2}\s+canlii\s+\d{1,7}\b", re.IGNORECASE)
CONNECTOR_RE = re.compile(r"\s+(?:v\.?|vs\.?|c\.?|versus)\s+", re.IGNORECASE)


def _report_base(value: str | None) -> str:
    normalized = " ".join((value or "").split()).lower()
    pinpoint = PINPOINT_RE.search(normalized)
    if pinpoint is not None:
        normalized = normalized[: pinpoint.start()].rstrip(" ,;:-")
    if CONNECTOR_RE.search(normalized):
        normalized = REPORTER_SUFFIX_RE.sub("", normalized).rstrip(" ,;:-")
    return normalized


def _citation_years(value: str | None) -> set[int]:
    years = set()
    for variant in _citation_variants(value or ""):
        try:
            years.add(int(variant.split(maxsplit=1)[0]))
        except (IndexError, ValueError):
            continue
    return years


def _build_title_year_index(session) -> dict[tuple[str, int], set[int]]:
    index: dict[tuple[str, int], set[int]] = defaultdict(set)
    for case_id, title, decision_date in session.execute(select(Case.id, Case.title, Case.date)):
        key = _normalize_alias_lookup(title or "")
        if key and decision_date is not None:
            index[(key, decision_date.year)].add(case_id)
    return index


def _title_year_signal(
    citation: Citation,
    raw: str,
    title_index: dict[str, set[int]],
    title_year_index: dict[tuple[str, int], set[int]],
) -> str | None:
    title_key = _citation_title_key(raw)
    title_targets = set(title_index.get(title_key, set()))
    if len(title_targets) <= 1:
        return None
    year_targets: set[int] = set()
    for year in _citation_years(raw):
        year_targets.update(title_year_index.get((title_key, year), set()))
    year_targets.discard(citation.source_case_id)
    if len(year_targets) == 1:
        return "unique_title_year"
    if len(year_targets) > 1:
        return "ambiguous_title_year"
    return None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--top", type=int, default=100, help="Number of top normalized groups to report.")
    parser.add_argument("--batch-size", type=int, default=10_000)
    parser.add_argument(
        "--exclude-kind",
        action="append",
        default=[],
        choices=sorted({"case", "case_name", "case_short", "neutral"}),
        help="Citation kind to omit; may be repeated.",
    )
    parser.add_argument("--output", type=Path, default=None, help="Optional JSON report path.")
    return parser.parse_args()


def _shape(citation: Citation, base: str) -> str:
    if not base:
        return "empty"
    if NEUTRAL_RE.search(base):
        return "neutral"
    if FORMAL_RE.search(base):
        return "reported"
    if CONNECTOR_RE.search(base):
        if citation.citation_kind in {"case_short", "case_name"}:
            return "named_short" if len(base.split()) <= 8 else "named_full"
        return "named_other"
    if citation.citation_kind == "case_short":
        return "short_without_connector"
    if citation.citation_kind == "case_name":
        return "named_without_connector"
    return f"kind_{citation.citation_kind}"


def _candidate_signal(
    citation: Citation,
    local_citation_index: dict[str, int | None],
    exact_alias_index: dict[str, set[int]],
    title_index: dict[str, set[int]],
    title_year_index: dict[tuple[str, int], set[int]],
) -> str:
    raw = citation.normalized_citation or citation.citation_text or ""
    variant_targets: set[int] = set()
    variant_ambiguous = False
    for variant in _citation_variants(raw):
        if variant not in local_citation_index:
            continue
        target_id = local_citation_index[variant]
        if target_id is None:
            variant_ambiguous = True
        elif target_id != citation.source_case_id:
            variant_targets.add(target_id)
    if len(variant_targets) == 1:
        return "unique_citation_variant"
    if len(variant_targets) > 1 or variant_ambiguous:
        return "ambiguous_citation_variant"

    base_key = _normalize_alias_lookup(_report_base(raw))
    alias_targets = set(exact_alias_index.get(base_key, set()))
    non_self_alias_targets = alias_targets - {citation.source_case_id}
    if len(alias_targets) == 1 and len(non_self_alias_targets) == 1:
        return "unique_case_alias"
    if citation.source_case_id in alias_targets and len(non_self_alias_targets) == 1:
        return _title_year_signal(citation, raw, title_index, title_year_index) or "ambiguous_self_plus_alias"
    if len(non_self_alias_targets) > 1:
        return _title_year_signal(citation, raw, title_index, title_year_index) or "ambiguous_case_alias"
    if base_key and base_key in exact_alias_index and citation.source_case_id in exact_alias_index[base_key]:
        return "self_case_alias"

    title_key = _citation_title_key(raw)
    title_targets = set(title_index.get(title_key, set()))
    title_targets.discard(citation.source_case_id)
    if len(title_targets) == 1:
        return "unique_title"
    if len(title_targets) > 1:
        return _title_year_signal(citation, raw, title_index, title_year_index) or "ambiguous_title"
    return "no_exact_local_signal"


def build_report(
    session,
    top: int,
    batch_size: int,
    excluded_kinds: set[str] | None = None,
) -> dict[str, object]:
    if top < 1:
        raise ValueError("top must be at least 1")
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")

    local_citation_index = build_local_case_resolution_index(session)
    exact_alias_index, _, _ = _case_alias_index(session)
    title_index = _build_title_resolution_index(session)
    title_year_index = _build_title_year_index(session)
    counts = Counter()
    signal_counts = Counter()
    kind_counts = Counter()
    shape_counts = Counter()
    groups: dict[tuple[str, str, str], dict[str, object]] = {}
    unresolved = 0

    excluded_kinds = excluded_kinds or set()
    query = select(Citation).where(Citation.target_case_id.is_(None))
    if excluded_kinds:
        query = query.where(Citation.citation_kind.not_in(excluded_kinds))
    rows = session.scalars(query.order_by(Citation.id)).yield_per(batch_size)
    for citation in rows:
        unresolved += 1
        raw = citation.normalized_citation or citation.citation_text or ""
        base = _report_base(raw)
        kind = citation.citation_kind
        shape = _shape(citation, base)
        signal = _candidate_signal(citation, local_citation_index, exact_alias_index, title_index, title_year_index)
        key = (kind, shape, _normalize_alias_lookup(base))
        counts[key] += 1
        kind_counts[kind] += 1
        shape_counts[shape] += 1
        signal_counts[signal] += 1
        group = groups.setdefault(
            key,
            {"citation_kind": kind, "shape": shape, "normalized": base, "count": 0, "signals": Counter(), "examples": []},
        )
        group["count"] = int(group["count"]) + 1
        group["signals"][signal] += 1
        examples = group["examples"]
        if len(examples) < 3:
            examples.append({"id": citation.id, "source_case_id": citation.source_case_id, "text": raw[:500]})

    def serialize_group(group: dict[str, object]) -> dict[str, object]:
        return {
            "citation_kind": group["citation_kind"],
            "shape": group["shape"],
            "normalized": group["normalized"],
            "count": group["count"],
            "signals": dict(group["signals"]),
            "examples": list(group["examples"]),
        }

    ranked_groups = [
        serialize_group(group)
        for group in sorted(groups.values(), key=lambda group: int(group["count"]), reverse=True)[:top]
    ]
    signal_groups = {}
    for signal in (
        "unique_case_alias",
        "unique_title",
        "unique_citation_variant",
        "ambiguous_case_alias",
        "ambiguous_self_plus_alias",
        "unique_title_year",
        "ambiguous_title_year",
    ):
        signal_groups[signal] = [
            serialize_group(group)
            for group in sorted(
                (group for group in groups.values() if group["signals"].get(signal)),
                key=lambda group: int(group["signals"][signal]),
                reverse=True,
            )[:top]
        ]

    kind_groups = {
        kind: [
            serialize_group(group)
            for group in sorted(
                (group for group in groups.values() if group["citation_kind"] == kind),
                key=lambda group: int(group["count"]),
                reverse=True,
            )[:top]
        ]
        for kind in sorted(kind_counts)
    }

    return {
        "unresolved_rows": unresolved,
        "excluded_citation_kinds": sorted(excluded_kinds),
        "citation_kinds": dict(kind_counts),
        "shapes": dict(shape_counts),
        "candidate_signals": dict(signal_counts),
        "top_groups": ranked_groups,
        "top_groups_by_kind": kind_groups,
        "top_signal_groups": signal_groups,
    }


def main() -> None:
    args = parse_args()
    with SessionLocal() as session:
        report = build_report(session, args.top, args.batch_size, set(args.exclude_kind))
    serialized = json.dumps(report, indent=2, ensure_ascii=True)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized + "\n", encoding="utf-8")
    print(serialized)


if __name__ == "__main__":
    main()