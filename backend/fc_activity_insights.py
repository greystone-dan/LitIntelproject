"""Aggregations over fc_activity_summaries for the Federal Court activity panels.

The summary table holds one flat row per classified IMM file (written by
scripts/classify_fc_activity.py), so these queries never parse classification_json.
"""

from __future__ import annotations

import re
import time
from statistics import median
from typing import Any

from fastapi import HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from backend.database import FCActivityClassification, FCActivitySummary

_CACHE: dict[tuple[Any, ...], tuple[float, dict[str, Any]]] = {}
_CACHE_SECONDS = 600

DURATION_FIELDS = {
    "days_filing_to_perfection": "Filing to applicant's record",
    "days_filing_to_leave_decision": "Filing to leave decision",
    "days_leave_grant_to_hearing": "Leave granted to hearing",
    "days_hearing_to_judgment": "Hearing to judgment",
    "days_filing_to_final_disposition": "Filing to final outcome",
}
BREAKDOWN_FIELDS = {
    "resolution": "Final outcome",
    "decision_body": "Decision under review",
    "leave_refusal_reason": "Why leave was refused",
    "respondent_position": "Respondent's position on leave",
    "representation": "Applicant representation",
    "stay_status": "Stay of removal motions",
    "hearing_mode": "Judicial review hearing format",
    "appeal_status": "Federal Court of Appeal",
    "certified_question": "Certified question",
    "proceeding_language": "Language of the file",
}


def _cached(key: tuple[Any, ...], build) -> dict[str, Any]:
    now = time.monotonic()
    hit = _CACHE.get(key)
    if hit and now - hit[0] < _CACHE_SECONDS:
        return hit[1]
    value = build()
    _CACHE[key] = (now, value)
    return value


def _filtered(statement, *, city: str, year_from: int | None, year_to: int | None, decision_body: str = ""):
    if city.strip():
        statement = statement.where(FCActivitySummary.city_filed == city.strip())
    if year_from is not None:
        statement = statement.where(FCActivitySummary.year >= year_from)
    if year_to is not None:
        statement = statement.where(FCActivitySummary.year <= year_to)
    if decision_body.strip():
        statement = statement.where(FCActivitySummary.decision_body == decision_body.strip())
    return statement


def _quantiles(values: list[int]) -> dict[str, Any]:
    if not values:
        return {"count": 0, "median": None, "p25": None, "p75": None}
    ordered = sorted(values)

    def at(share: float) -> int:
        return ordered[min(len(ordered) - 1, int(share * (len(ordered) - 1) + 0.5))]

    return {"count": len(ordered), "median": int(median(ordered)), "p25": at(0.25), "p75": at(0.75)}


def _rate(numerator: int, denominator: int) -> float | None:
    return round(numerator / denominator, 4) if denominator else None


def fetch_fc_activity_insights(
    db: Session,
    *,
    city: str = "",
    year_from: int | None = None,
    year_to: int | None = None,
    decision_body: str = "",
) -> dict[str, Any]:
    """Outcome rates, wait times and procedural breakdowns for the selected slice of files."""

    def build() -> dict[str, Any]:
        filters = {"city": city, "year_from": year_from, "year_to": year_to, "decision_body": decision_body}
        total = db.scalar(_filtered(select(func.count()).select_from(FCActivitySummary), **filters)) or 0
        breakdowns: dict[str, Any] = {}
        for field, label in BREAKDOWN_FIELDS.items():
            column = getattr(FCActivitySummary, field)
            rows = db.execute(
                _filtered(select(column.label("value"), func.count().label("count")).select_from(FCActivitySummary), **filters)
                .group_by(column)
                .order_by(func.count().desc())
            ).all()
            missing = "not_applicable" if field == "leave_refusal_reason" else "unknown"
            merged: dict[str, int] = {}
            for row in rows:
                value = row.value or missing
                merged[value] = merged.get(value, 0) + int(row.count)
            breakdowns[field] = {
                "label": label,
                "rows": [{"value": value, "count": count} for value, count in sorted(merged.items(), key=lambda item: -item[1])],
            }
        durations: dict[str, Any] = {}
        for field, label in DURATION_FIELDS.items():
            column = getattr(FCActivitySummary, field)
            values = [int(value) for value in db.scalars(_filtered(select(column).where(column.is_not(None)), **filters)) if value is not None and value <= 3650]
            durations[field] = {"label": label, **_quantiles(values)}
        by_year_rows = db.execute(
            _filtered(
                select(
                    FCActivitySummary.year,
                    FCActivitySummary.leave_result,
                    FCActivitySummary.review_result,
                    func.count().label("count"),
                ).select_from(FCActivitySummary),
                **filters,
            ).group_by(FCActivitySummary.year, FCActivitySummary.leave_result, FCActivitySummary.review_result)
        ).all()
        years: dict[int, dict[str, int]] = {}
        for row in by_year_rows:
            if row.year is None:
                continue
            bucket = years.setdefault(int(row.year), {"files": 0, "leave_granted": 0, "leave_refused": 0, "jr_granted": 0, "jr_dismissed": 0})
            bucket["files"] += int(row.count)
            if row.leave_result in {"granted", "refused"}:
                bucket[f"leave_{row.leave_result}"] += int(row.count)
            if row.review_result in {"granted", "dismissed"}:
                bucket[f"jr_{row.review_result}"] += int(row.count)
        year_rows = [
            {
                "year": year,
                **values,
                "leave_grant_rate": _rate(values["leave_granted"], values["leave_granted"] + values["leave_refused"]),
                "jr_grant_rate": _rate(values["jr_granted"], values["jr_granted"] + values["jr_dismissed"]),
            }
            for year, values in sorted(years.items())
        ]
        leave_granted = sum(row["leave_granted"] for row in year_rows)
        leave_refused = sum(row["leave_refused"] for row in year_rows)
        jr_granted = sum(row["jr_granted"] for row in year_rows)
        jr_dismissed = sum(row["jr_dismissed"] for row in year_rows)
        consent = sum(item["count"] for item in breakdowns["resolution"]["rows"] if item["value"] == "resolved_by_consent")
        return {
            "filters": {key: value for key, value in filters.items() if value not in ("", None)},
            "total_files": int(total),
            "headline": {
                "leave_decisions": leave_granted + leave_refused,
                "leave_grant_rate": _rate(leave_granted, leave_granted + leave_refused),
                "judicial_review_decisions": jr_granted + jr_dismissed,
                "judicial_review_grant_rate": _rate(jr_granted, jr_granted + jr_dismissed),
                "resolved_by_consent": consent,
            },
            "durations": durations,
            "breakdowns": breakdowns,
            "by_year": year_rows,
            "note": "Rates use files with an observed decision. Wait times are in days; files without both dates are left out.",
        }

    return _cached(("insights", city.strip(), year_from, year_to, decision_body.strip()), build)


def fetch_fc_activity_judges(
    db: Session,
    *,
    min_decisions: int = 25,
    year_from: int | None = None,
    year_to: int | None = None,
    decision_body: str = "",
) -> dict[str, Any]:
    """Leave and judicial review grant rates per judge, with decision counts so small samples are visible."""

    def build() -> dict[str, Any]:
        filters = {"city": "", "year_from": year_from, "year_to": year_to, "decision_body": decision_body}
        judges: dict[str, dict[str, Any]] = {}

        def bucket(key: str, name: str | None) -> dict[str, Any]:
            entry = judges.setdefault(
                key,
                {"key": key, "names": {}, "leave_granted": 0, "leave_refused": 0, "jr_granted": 0, "jr_dismissed": 0, "days_to_judgment": []},
            )
            if name:
                entry["names"][name] = entry["names"].get(name, 0) + 1
            return entry

        leave_rows = db.execute(
            _filtered(
                select(
                    FCActivitySummary.leave_judge_key,
                    FCActivitySummary.leave_judge_name,
                    FCActivitySummary.leave_result,
                    func.count().label("count"),
                ).where(FCActivitySummary.leave_judge_key.is_not(None)),
                **filters,
            ).group_by(FCActivitySummary.leave_judge_key, FCActivitySummary.leave_judge_name, FCActivitySummary.leave_result)
        ).all()
        for row in leave_rows:
            if row.leave_result in {"granted", "refused"}:
                bucket(row.leave_judge_key, row.leave_judge_name)[f"leave_{row.leave_result}"] += int(row.count)
        merits_rows = db.execute(
            _filtered(
                select(
                    FCActivitySummary.merits_judge_key,
                    FCActivitySummary.merits_judge_name,
                    FCActivitySummary.review_result,
                    FCActivitySummary.days_hearing_to_judgment,
                ).where(FCActivitySummary.merits_judge_key.is_not(None)),
                **filters,
            )
        ).all()
        for row in merits_rows:
            if row.review_result in {"granted", "dismissed"}:
                entry = bucket(row.merits_judge_key, row.merits_judge_name)
                entry[f"jr_{row.review_result}"] += 1
                if row.days_hearing_to_judgment is not None:
                    entry["days_to_judgment"].append(int(row.days_hearing_to_judgment))
        rows = []
        for entry in judges.values():
            leave_total = entry["leave_granted"] + entry["leave_refused"]
            jr_total = entry["jr_granted"] + entry["jr_dismissed"]
            if max(leave_total, jr_total) < min_decisions:
                continue
            name = max(entry["names"].items(), key=lambda item: item[1])[0] if entry["names"] else entry["key"]
            rows.append(
                {
                    "key": entry["key"],
                    "name": name,
                    "leave_decisions": leave_total,
                    "leave_grant_rate": _rate(entry["leave_granted"], leave_total),
                    "jr_decisions": jr_total,
                    "jr_grant_rate": _rate(entry["jr_granted"], jr_total),
                    "median_days_hearing_to_judgment": int(median(entry["days_to_judgment"])) if entry["days_to_judgment"] else None,
                }
            )
        rows.sort(key=lambda row: (-(row["leave_decisions"] + row["jr_decisions"]), row["name"]))
        return {
            "min_decisions": min_decisions,
            "filters": {key: value for key, value in filters.items() if value not in ("", None)},
            "judges": rows,
            "note": "Leave rates count leave decisions where the judge is named on the order. Judicial review rates count merits judgments. Small counts are not reliable.",
        }

    return _cached(("judges", min_decisions, year_from, year_to, decision_body.strip()), build)


def fetch_fc_activity_case(db: Session, imm: str) -> dict[str, Any]:
    """Return the classifier's reading of one IMM file, without the bulky per-entry lists."""
    normalized = (imm or "").strip().upper()
    if not re.fullmatch(r"IMM-\d{1,6}-\d{2,4}", normalized):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Provide an IMM number like IMM-1234-19.")
    row = db.scalar(select(FCActivityClassification).where(FCActivityClassification.imm_number == normalized))
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{normalized} is not in the classified FC activity data.")
    classification = dict(row.classification_json or {})
    keep = (
        "full_history_resolution", "lifecycle_status", "leave_decision", "leave_context", "judicial_review_result",
        "decision_body", "challenged_decision", "judge_roles", "consent_disposition", "timeline", "hearings",
        "certified_question", "appeal", "stay_of_removal", "representation", "respondent_position", "filing_details",
    )
    summary = {key: classification.get(key) for key in keep if key in classification}
    challenged = summary.get("challenged_decision")
    if isinstance(challenged, dict):
        summary["challenged_decision"] = {key: challenged.get(key) for key in ("application_type", "decision_maker", "decision_date", "decision_subject", "filing_date", "tribunal_file_numbers")}
    return {
        "imm_number": row.imm_number,
        "case_name": row.case_name,
        "year": row.year,
        "city_filed": row.city_filed,
        "nature": row.nature,
        "classifier_version": row.classifier_version,
        "classification": summary,
    }
