"""Build a seeded, read-only evaluation report for FC Activity extraction."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import date
import json
from pathlib import Path
import random
import re
import sys
from typing import Any

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import FCActivityCase, FCActivityDocument, SessionLocal
from scripts.classify_fc_activity import classify_case


def _parse_date(value: Any) -> date | None:
    try:
        return date.fromisoformat(value) if value else None
    except (TypeError, ValueError):
        return None


def _delay_summary(values: list[int]) -> dict[str, Any]:
    if not values:
        return {"count": 0, "min_days": None, "p25_days": None, "p50_days": None, "p75_days": None, "max_days": None}
    ordered = sorted(values)

    def percentile(fraction: float) -> int:
        return ordered[min(len(ordered) - 1, int((len(ordered) - 1) * fraction))]

    return {
        "count": len(ordered),
        "min_days": ordered[0],
        "p25_days": percentile(0.25),
        "p50_days": percentile(0.5),
        "p75_days": percentile(0.75),
        "max_days": ordered[-1],
    }


def _delay_metric(events: list[dict[str, Any]], anchor_type: str) -> dict[str, Any]:
    stays = [
        item for item in events
        if item.get("event_type") == "stay" and item.get("removal_scheduled_date")
    ]
    stays.sort(key=lambda item: (_parse_date(item.get("event_date")) or date.min, item.get("doc_id") or 0))
    scheduled = stays[-1] if stays else None
    anchors = [
        item for item in events
        if item.get("event_type") == anchor_type and item.get("event_date")
    ]
    anchors.sort(key=lambda item: (_parse_date(item.get("event_date")) or date.min, item.get("doc_id") or 0))
    anchor = anchors[-1] if anchors else None
    removal_date = _parse_date(scheduled.get("removal_scheduled_date")) if scheduled else None
    anchor_date = _parse_date(anchor.get("event_date")) if anchor else None
    status = "complete"
    days = None
    if removal_date is None:
        status = "missing_removal_date"
    elif anchor_date is None:
        status = "missing_anchor_date"
    elif removal_date < anchor_date:
        status = "ambiguous_date_order"
    else:
        days = (removal_date - anchor_date).days
    return {
        "status": status,
        "days": days,
        "anchor_date_kind": anchor.get("date_kind") if anchor else None,
        "removal_scheduled_date": removal_date.isoformat() if removal_date else None,
        "anchor_date": anchor_date.isoformat() if anchor_date else None,
    }


def _build_delay_metrics(events: list[dict[str, Any]]) -> dict[str, Any]:
    metrics: dict[str, Any] = {}
    for name, anchor_type in (("filing_to_removal", "application_filed"), ("motion_to_removal", "motion_filed")):
        metric = _delay_metric(events, anchor_type)
        metrics[name] = {
            "status": metric["status"],
            "days": metric["days"],
            "anchor_date_kind": metric["anchor_date_kind"],
            "removal_scheduled_date": metric["removal_scheduled_date"],
            "anchor_date": metric["anchor_date"],
        }
    return metrics


def _aggregate_delay_metrics(case_metrics: list[dict[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for name in ("filing_to_removal", "motion_to_removal"):
        rows = [item[name] for item in case_metrics]
        by_status = Counter(item["status"] for item in rows)
        days = [item["days"] for item in rows if item["days"] is not None]
        output[name] = {
            "case_count": len(rows),
            "valid_count": len(days),
            "coverage_rate": round(len(days) / len(rows), 4) if rows else 0.0,
            "status_counts": dict(sorted(by_status.items())),
            "valid_delay": _delay_summary(days),
        }
    return output


def _motion_coverage(classifications: list[dict[str, Any]]) -> dict[str, Any]:
    motion_events: list[dict[str, Any]] = []
    motion_case_count = 0
    for classification in classifications:
        case_motion_events = []
        for event in classification.get("procedural_events", []):
            if not str(event.get("event_type", "")).startswith("motion"):
                continue
            case_motion_events.append(event)
            motion_events.append(event)
        if case_motion_events:
            motion_case_count += 1

    event_count = len(motion_events)
    case_count = len(classifications)
    subtype_counts = Counter(str(event.get("subtype") or "unknown") for event in motion_events)
    result_counts = Counter(str(event.get("outcome") or "unknown") for event in motion_events)
    unknown_subtype_count = subtype_counts.get("unknown", 0)
    unknown_result_count = result_counts.get("unknown", 0)
    metrics = {
        "case_count": case_count,
        "motion_case_count": motion_case_count,
        "motion_case_rate": round(motion_case_count / case_count, 4) if case_count else 0.0,
        "motion_event_count": event_count,
        "subtype_counts": dict(sorted(subtype_counts.items())),
        "result_counts": dict(sorted(result_counts.items())),
        "subtype_coverage_rate": round((event_count - unknown_subtype_count) / event_count, 4) if event_count else 0.0,
        "result_coverage_rate": round((event_count - unknown_result_count) / event_count, 4) if event_count else 0.0,
        "evidence_complete_count": sum(
            bool(event.get("doc_id") is not None and event.get("text") and event.get("rule"))
            for event in motion_events
        ),
    }
    metrics["grouped_motion_coverage"] = _grouped_motion_coverage(motion_events)
    return metrics


def _motion_document_reference(text: str) -> str | None:
    patterns = (
        r"(?:motion\s+)?doc(?:ument)?\.?\s*(?:n[°oº]?|no\.?)?\s*#?\s*(\d+)",
        r"(?:motion|requ[eê]te)\s*(?:n[°oº]?|no\.?)\s*#?\s*(\d+)",
    )
    for pattern in patterns:
        match = re.search(pattern, text or "", re.IGNORECASE)
        if match:
            return match.group(1)
    return None


def _grouped_motion_coverage(motion_events: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize unique motion records without hiding identifier uncertainty."""
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = {}
    fallback_count = 0
    for index, event in enumerate(motion_events):
        case_id = event.get("activity_case_id")
        motion_reference = event.get("motion_reference") or _motion_document_reference(str(event.get("text") or ""))
        re_no = event.get("re_no")
        if motion_reference:
            key = (case_id, "motion_doc_reference", motion_reference)
        elif re_no:
            key = (case_id, "re_no", str(re_no))
        else:
            fallback_count += 1
            key = (case_id, "singleton_doc", event.get("doc_id", index))
        groups.setdefault(key, []).append(event)

    grouped = []
    for key, events in groups.items():
        known_subtypes = {event.get("subtype") for event in events if event.get("subtype") not in {None, "unknown"}}
        known_outcomes = {event.get("outcome") for event in events if event.get("outcome") not in {None, "unknown"}}
        subtype = next(iter(known_subtypes)) if len(known_subtypes) == 1 else "conflict" if known_subtypes else "unknown"
        outcome = next(iter(known_outcomes)) if len(known_outcomes) == 1 and all(event.get("outcome") not in {None, "unknown"} for event in events) else "conflict" if len(known_outcomes) > 1 else "unknown"
        grouped.append({
            "group_key": f"{key[0]}:{key[1]}:{key[2]}",
            "group_key_kind": key[1],
            "doc_count": len(events),
            "subtype": subtype,
            "outcome": outcome,
            "doc_ids": [event.get("doc_id") for event in events],
        })

    subtype_counts = Counter(item["subtype"] for item in grouped)
    outcome_counts = Counter(item["outcome"] for item in grouped)
    group_count = len(grouped)
    return {
        "group_count": group_count,
        "motion_doc_reference_group_count": sum(item["group_key_kind"] == "motion_doc_reference" for item in grouped),
        "stable_re_no_group_count": sum(item["group_key_kind"] == "re_no" for item in grouped),
        "singleton_fallback_group_count": sum(item["group_key_kind"] == "singleton_doc" for item in grouped),
        "fallback_event_count": fallback_count,
        "subtype_counts": dict(sorted(subtype_counts.items())),
        "result_counts": dict(sorted(outcome_counts.items())),
        "subtype_conflict_count": subtype_counts.get("conflict", 0),
        "result_conflict_count": outcome_counts.get("conflict", 0),
        "subtype_coverage_rate": round((group_count - subtype_counts.get("unknown", 0) - subtype_counts.get("conflict", 0)) / group_count, 4) if group_count else 0.0,
        "result_coverage_rate": round((group_count - outcome_counts.get("unknown", 0) - outcome_counts.get("conflict", 0)) / group_count, 4) if group_count else 0.0,
        "groups": grouped,
    }


def _intelligence_coverage(classifications: list[dict[str, Any]]) -> dict[str, Any]:
    stage_counts: Counter[str] = Counter()
    decision_maker_counts: Counter[str] = Counter()
    decision_subject_counts: Counter[str] = Counter()
    lifecycle_counts: Counter[str] = Counter()
    for classification in classifications:
        judges = classification.get("judges", {})
        for stage, observations in judges.get("by_stage", {}).items():
            if observations:
                stage_counts[stage] += 1
        challenged = classification.get("challenged_decision", {})
        decision_maker_counts[challenged.get("decision_maker_type") or "unknown"] += 1
        decision_subject_counts[challenged.get("decision_subject") or "unknown"] += 1
        lifecycle_counts[classification.get("lifecycle_status", {}).get("status") or "unknown"] += 1
    total = len(classifications)
    return {
        "case_count": total,
        "judge_stage_case_counts": dict(sorted(stage_counts.items())),
        "judge_stage_coverage": {stage: round(count / total, 4) if total else 0.0 for stage, count in sorted(stage_counts.items())},
        "decision_maker_type_counts": dict(sorted(decision_maker_counts.items())),
        "decision_subject_counts": dict(sorted(decision_subject_counts.items())),
        "lifecycle_status_counts": dict(sorted(lifecycle_counts.items())),
    }


def _queryable_analytics(classifications: list[dict[str, Any]]) -> dict[str, Any]:
    dimensions = {
        "lifecycle_status": Counter(),
        "hearing_status": Counter(),
        "decision_maker_type": Counter(),
        "underlying_tribunal_type": Counter(),
        "decision_subject": Counter(),
        "milestone_stage": Counter(),
    }
    for classification in classifications:
        dimensions["lifecycle_status"][classification.get("lifecycle_status", {}).get("status") or "unknown"] += 1
        dimensions["hearing_status"][classification.get("hearing_status", {}).get("status") or "unknown"] += 1
        challenged = classification.get("challenged_decision", {})
        dimensions["decision_maker_type"][challenged.get("decision_maker_type") or "unknown"] += 1
        dimensions["underlying_tribunal_type"][challenged.get("underlying_tribunal_type") or "unknown"] += 1
        dimensions["decision_subject"][challenged.get("decision_subject") or "unknown"] += 1
        for stage, value in classification.get("milestone_rollups", {}).items():
            if _milestone_has_known_signal(value):
                dimensions["milestone_stage"][stage] += 1
    return {
        "dimensions": {name: dict(sorted(counts.items())) for name, counts in dimensions.items()},
        "queryable_fields": [
            "lifecycle_status.status",
            "hearing_status.status",
            "challenged_decision.decision_maker_type",
            "challenged_decision.underlying_tribunal_type",
            "challenged_decision.decision_subject",
            "milestone_rollups.<stage>",
        ],
    }


def _milestone_has_known_signal(value: Any) -> bool:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in {"status", "result"} and nested not in {None, "unknown"}:
                return True
            if _milestone_has_known_signal(nested):
                return True
    elif isinstance(value, list):
        return any(_milestone_has_known_signal(item) for item in value)
    return False


def _field_value(value: dict[str, Any], path: str) -> Any:
    current: Any = value
    for component in path.split("."):
        if not isinstance(current, dict):
            return None
        current = current.get(component)
    return current


def evaluate_gold_set(
    classifications: list[dict[str, Any]],
    gold_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    by_case = {int(row["activity_case_id"]): row for row in classifications if row.get("activity_case_id") is not None}
    comparisons: list[dict[str, Any]] = []
    for gold in gold_rows:
        actual_row = by_case.get(int(gold["activity_case_id"]))
        actual = actual_row.get("classification", {}) if actual_row else {}
        expected_fields = gold.get("expected", {})
        for field, expected in expected_fields.items():
            observed = _field_value(actual, field)
            comparisons.append({
                "activity_case_id": int(gold["activity_case_id"]),
                "field": field,
                "expected": expected,
                "observed": observed,
                "match": observed == expected,
                "covered": actual_row is not None,
            })
    total = len(comparisons)
    matched = sum(item["match"] for item in comparisons)
    covered = sum(item["covered"] for item in comparisons)
    return {
        "case_count": len(gold_rows),
        "field_count": total,
        "covered_count": covered,
        "matched_count": matched,
        "coverage_rate": round(covered / total, 4) if total else 0.0,
        "accuracy": round(matched / total, 4) if total else 0.0,
        "disagreements": [item for item in comparisons if not item["match"]],
    }


def sample_case_ids(
    candidates: list[tuple[int, int | None]],
    *,
    sample_size: int,
    recent_years: int,
    recent_share: float,
    seed: int,
) -> list[int]:
    if sample_size < 1:
        raise ValueError("sample_size must be positive")
    if recent_years < 1:
        raise ValueError("recent_years must be positive")
    if not 0 < recent_share <= 1:
        raise ValueError("recent_share must be greater than 0 and at most 1")
    if not candidates:
        return []

    numeric_years = sorted({year for _, year in candidates if year is not None})
    recent_cutoff = numeric_years[-min(recent_years, len(numeric_years))] if numeric_years else None
    recent = [item for item in candidates if recent_cutoff is not None and item[1] is not None and item[1] >= recent_cutoff]
    recent_ids = {case_id for case_id, _ in recent}
    older = [item for item in candidates if item[0] not in recent_ids]
    desired_recent = min(len(recent), max(1, round(sample_size * recent_share)))
    desired_older = min(len(older), sample_size - desired_recent)
    remaining = sample_size - desired_recent - desired_older
    if remaining and len(recent) > desired_recent:
        extra = min(remaining, len(recent) - desired_recent)
        desired_recent += extra
        remaining -= extra
    if remaining and len(older) > desired_older:
        desired_older += min(remaining, len(older) - desired_older)

    rng = random.Random(seed)
    selected = rng.sample(recent, desired_recent) + rng.sample(older, desired_older)
    return sorted(case_id for case_id, _ in selected)


def _imm_number(case: FCActivityCase) -> str | None:
    payload = case.raw_payload if isinstance(case.raw_payload, dict) else {}
    value = payload.get("imm_number")
    return str(value) if value else None


def build_report(
    *,
    sample_size: int,
    recent_years: int,
    recent_share: float,
    seed: int,
    output: Path,
    gold_set: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    with SessionLocal() as session:
        candidates = list(session.execute(select(FCActivityCase.id, FCActivityCase.year)).all())
        selected_ids = sample_case_ids(
            [(int(case_id), year) for case_id, year in candidates],
            sample_size=sample_size,
            recent_years=recent_years,
            recent_share=recent_share,
            seed=seed,
        )
        cases = list(session.scalars(select(FCActivityCase).where(FCActivityCase.id.in_(selected_ids)))) if selected_ids else []
        documents = list(
            session.scalars(
                select(FCActivityDocument)
                .where(FCActivityDocument.case_id.in_(selected_ids))
                .order_by(FCActivityDocument.case_id, FCActivityDocument.doc_dt, FCActivityDocument.id)
            )
        ) if selected_ids else []

    documents_by_case: dict[int, list[FCActivityDocument]] = defaultdict(list)
    for document in documents:
        documents_by_case[document.case_id].append(document)

    rows: list[dict[str, Any]] = []
    event_counts: Counter[str] = Counter()
    event_outcomes: Counter[str] = Counter()
    evidence_complete = 0
    case_delay_metrics: list[dict[str, Any]] = []
    intelligence_classifications: list[dict[str, Any]] = []
    for case in sorted(cases, key=lambda item: item.id):
        classification = classify_case(case, documents_by_case.get(case.id, []))
        procedural_events = classification["classification"].get("procedural_events", [])
        intelligence_classifications.append(classification["classification"])
        case_delay_metrics.append(_build_delay_metrics(procedural_events))
        event_counts.update(item["event_type"] for item in procedural_events)
        event_outcomes.update(
            f"{item['event_type']}:{item['outcome']}"
            for item in procedural_events
            if item.get("outcome")
        )
        evidence_complete += sum(
            bool(item.get("doc_id") is not None and item.get("text") and item.get("rule"))
            for item in procedural_events
        )
        rows.append(
            {
                "activity_case_id": case.id,
                "imm_number": _imm_number(case),
                "source_key": case.source_key,
                "year": case.year,
                "case_name": case.case_name,
                "document_count": len(documents_by_case.get(case.id, [])),
                "source_documents": [
                    {
                        "doc_id": document.id,
                        "source_document_date": document.doc_dt.isoformat() if document.doc_dt else None,
                        "text": document.recorded_entry,
                    }
                    for document in documents_by_case.get(case.id, [])
                ],
                "classification": classification["classification"],
            }
        )

    report = {
        "report_version": "fc_activity_deterministic_evaluation_v1",
        "seed": seed,
        "sample_size_requested": sample_size,
        "sample_size_actual": len(rows),
        "recent_years": recent_years,
        "recent_share_requested": recent_share,
        "year_counts": dict(Counter(str(row["year"]) for row in rows)),
        "event_counts": dict(sorted(event_counts.items())),
        "event_outcomes": dict(sorted(event_outcomes.items())),
        "motion_coverage": _motion_coverage(intelligence_classifications),
        "evidence_fields_present": evidence_complete,
        "delay_metrics": _aggregate_delay_metrics(case_delay_metrics),
        "intelligence_coverage": _intelligence_coverage(intelligence_classifications),
        "analytics": _queryable_analytics(intelligence_classifications),
        "gold_set_metrics": evaluate_gold_set(rows, gold_set or []),
        "cases": rows,
        "network_called": False,
        "database_written": False,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("data/eval/fc_activity_deterministic_evaluation.json"))
    parser.add_argument("--sample-size", type=int, default=100)
    parser.add_argument("--recent-years", type=int, default=7)
    parser.add_argument("--recent-share", type=float, default=0.7)
    parser.add_argument("--seed", type=int, default=20260925)
    parser.add_argument("--gold-set", type=Path, default=None, help="Optional JSON gold set with activity_case_id and expected dotted fields")
    args = parser.parse_args()
    gold_set: list[dict[str, Any]] = []
    if args.gold_set:
        loaded = json.loads(args.gold_set.read_text(encoding="utf-8"))
        gold_set = loaded.get("cases", loaded) if isinstance(loaded, (dict, list)) else []
    report = build_report(
        sample_size=args.sample_size,
        recent_years=args.recent_years,
        recent_share=args.recent_share,
        seed=args.seed,
        output=args.output,
        gold_set=gold_set,
    )
    print(json.dumps({key: report[key] for key in ("sample_size_actual", "year_counts", "event_counts", "database_written")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())