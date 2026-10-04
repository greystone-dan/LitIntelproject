"""Aggregations over fc_activity_summaries for the Federal Court activity panels.

The summary table holds one flat row per classified IMM file (written by
scripts/classify_fc_activity.py), so these queries never parse classification_json.
"""

from __future__ import annotations

import re
import time
from collections import OrderedDict
from statistics import median
from threading import Lock
from typing import Any

from fastapi import HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from backend.database import FCActivityClassification, FCActivityMotion, FCActivitySummary

_CACHE: OrderedDict[tuple[Any, ...], tuple[float, dict[str, Any]]] = OrderedDict()
_CACHE_SECONDS = 1800
_CACHE_MAX_ENTRIES = 256
_CACHE_LOCK = Lock()

DURATION_FIELDS = {
    "days_decision_to_filing": "Tribunal decision to filing",
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
    "application_type": "Type of application",
    "office_location": "Office that decided",
    "extension_of_time": "Extension of time motions",
    "joint_applicants": "Joint applicants (families)",
    "dormant": "Open files with no activity for 2+ years",
    "lead_resolution": "Outcome of the lead file (group-managed files)",
    "filing_timeliness": "Filed within the IRPA s. 72 limit",
    "record_timeliness": "Applicant's record within 30 days (Rule 10)",
    "memorandum_timeliness": "Respondent's memorandum within 30 days (Rule 11)",
    "hearing_window": "Hearing 30 to 90 days after leave (Rule 15)",
}
BREAKDOWN_LIMITS = {"office_location": 15}


def _cached(key: tuple[Any, ...], build) -> dict[str, Any]:
    now = time.monotonic()
    with _CACHE_LOCK:
        hit = _CACHE.get(key)
        if hit and now - hit[0] < _CACHE_SECONDS:
            _CACHE.move_to_end(key)
            return hit[1]
    # Do not serialize database work; as before, concurrent misses may build
    # independently. Only the multi-step LRU bookkeeping needs protection.
    value = build()
    # Preserve the existing key and insertion-time TTL (hits do not refresh it).
    # Prune expired entries and evict least recently used live results, never
    # cache a failed build. The process-local cache bounds entries, not bytes.
    with _CACHE_LOCK:
        for old_key, (created, _) in list(_CACHE.items()):
            if now - created >= _CACHE_SECONDS:
                del _CACHE[old_key]
        _CACHE[key] = (now, value)
        _CACHE.move_to_end(key)
        while len(_CACHE) > _CACHE_MAX_ENTRIES:
            _CACHE.popitem(last=False)
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
                value = ("yes" if row.value else "no") if isinstance(row.value, bool) else row.value or missing
                merged[value] = merged.get(value, 0) + int(row.count)
            breakdowns[field] = {
                "label": label,
                "rows": [{"value": value, "count": count} for value, count in sorted(merged.items(), key=lambda item: -item[1])][: BREAKDOWN_LIMITS.get(field, 50)],
            }
        durations: dict[str, Any] = {}
        # Fetch only the six integer columns once rather than scanning the same
        # filtered slice six times. Exact quantiles still require every value.
        duration_values: dict[str, list[int]] = {field: [] for field in DURATION_FIELDS}
        duration_columns = [getattr(FCActivitySummary, field) for field in DURATION_FIELDS]
        for row in db.execute(_filtered(select(*duration_columns), **filters)):
            for field, value in zip(DURATION_FIELDS, row):
                if value is not None and value <= 3650:
                    duration_values[field].append(int(value))
        for field, label in DURATION_FIELDS.items():
            durations[field] = {"label": label, **_quantiles(duration_values[field])}
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
        body_rows = db.execute(
            _filtered(
                select(
                    FCActivitySummary.decision_body,
                    FCActivitySummary.leave_result,
                    FCActivitySummary.review_result,
                    func.count().label("count"),
                ).select_from(FCActivitySummary),
                **filters,
            ).group_by(FCActivitySummary.decision_body, FCActivitySummary.leave_result, FCActivitySummary.review_result)
        ).all()
        bodies: dict[str, dict[str, int]] = {}
        for row in body_rows:
            bucket = bodies.setdefault(row.decision_body or "unknown", {"files": 0, "leave_granted": 0, "leave_refused": 0, "jr_granted": 0, "jr_dismissed": 0})
            bucket["files"] += int(row.count)
            if row.leave_result in {"granted", "refused"}:
                bucket[f"leave_{row.leave_result}"] += int(row.count)
            if row.review_result in {"granted", "dismissed"}:
                bucket[f"jr_{row.review_result}"] += int(row.count)
        by_body = sorted(
            (
                {
                    "decision_body": body,
                    **values,
                    "leave_grant_rate": _rate(values["leave_granted"], values["leave_granted"] + values["leave_refused"]),
                    "jr_grant_rate": _rate(values["jr_granted"], values["jr_granted"] + values["jr_dismissed"]),
                }
                for body, values in bodies.items()
            ),
            key=lambda row: -row["files"],
        )
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
            "by_decision_body": by_body,
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
        )
        for row in merits_rows:
            if row.review_result in {"granted", "dismissed"}:
                entry = bucket(row.merits_judge_key, row.merits_judge_name)
                entry[f"jr_{row.review_result}"] += 1
                if row.days_hearing_to_judgment is not None:
                    entry["days_to_judgment"].append(int(row.days_hearing_to_judgment))
        motion_statement = select(FCActivityMotion.judge_key, FCActivityMotion.judge_name, FCActivityMotion.motion_type, FCActivityMotion.outcome, func.count().label("count")).where(
            FCActivityMotion.judge_key.is_not(None), FCActivityMotion.outcome.in_(("granted", "granted_in_part", "dismissed"))
        )
        if year_from is not None:
            motion_statement = motion_statement.where(FCActivityMotion.year >= year_from)
        if year_to is not None:
            motion_statement = motion_statement.where(FCActivityMotion.year <= year_to)
        for row in db.execute(motion_statement.group_by(FCActivityMotion.judge_key, FCActivityMotion.judge_name, FCActivityMotion.motion_type, FCActivityMotion.outcome)).all():
            entry = bucket(row.judge_key, row.judge_name)
            granted = row.outcome != "dismissed"
            entry["motion_decisions"] = entry.get("motion_decisions", 0) + int(row.count)
            entry["motion_granted"] = entry.get("motion_granted", 0) + (int(row.count) if granted else 0)
            if row.motion_type in {"stay_of_removal", "stay_of_release"}:
                entry["stay_decisions"] = entry.get("stay_decisions", 0) + int(row.count)
                entry["stay_granted"] = entry.get("stay_granted", 0) + (int(row.count) if granted else 0)
        rows = []
        for entry in judges.values():
            leave_total = entry["leave_granted"] + entry["leave_refused"]
            jr_total = entry["jr_granted"] + entry["jr_dismissed"]
            if max(leave_total, jr_total, entry.get("motion_decisions", 0)) < min_decisions:
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
                    "motion_decisions": entry.get("motion_decisions", 0),
                    "motion_grant_rate": _rate(entry.get("motion_granted", 0), entry.get("motion_decisions", 0)),
                    "stay_decisions": entry.get("stay_decisions", 0),
                    "stay_grant_rate": _rate(entry.get("stay_granted", 0), entry.get("stay_decisions", 0)),
                }
            )
        rows.sort(key=lambda row: (-(row["leave_decisions"] + row["jr_decisions"] + row["motion_decisions"]), row["name"]))
        return {
            "min_decisions": min_decisions,
            "filters": {key: value for key, value in filters.items() if value not in ("", None)},
            "judges": rows,
            "note": "Leave rates count leave orders naming the judge; JR rates count merits judgments; motion and stay rates count rulings linked to a filed motion. Prothonotaries (associate judges) appear mainly for motions. Small counts are not reliable.",
        }

    return _cached(("judges", min_decisions, year_from, year_to, decision_body.strip()), build)


def fetch_fc_activity_case(db: Session, imm: str) -> dict[str, Any]:
    """Return the classifier's reading of one IMM file, without the bulky per-entry lists."""
    normalized = (imm or "").strip().upper()
    if not re.fullmatch(r"IMM-\d{1,6}-\d{2,4}", normalized):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Provide an IMM number like IMM-1234-19.")
    # Avoid loading unused source/provenance columns and ORM state. JSON is
    # still required for the portable compact projection below.
    row = db.execute(select(
        FCActivityClassification.imm_number,
        FCActivityClassification.case_name,
        FCActivityClassification.year,
        FCActivityClassification.city_filed,
        FCActivityClassification.nature,
        FCActivityClassification.classifier_version,
        FCActivityClassification.classification_json,
    ).where(FCActivityClassification.imm_number == normalized)).first()
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{normalized} is not in the classified FC activity data.")
    classification = dict(row.classification_json or {})
    keep = (
        "full_history_resolution", "lifecycle_status", "leave_decision", "leave_context", "judicial_review_result",
        "decision_body", "challenged_decision", "judge_roles", "consent_disposition", "timeline", "hearings",
        "certified_question", "appeal", "stay_of_removal", "representation", "respondent_position", "filing_details",
        "office_location", "motion_profile", "parties", "motions", "deadlines",
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


def fetch_fc_activity_counsel(
    db: Session,
    *,
    min_files: int = 20,
    year_from: int | None = None,
    year_to: int | None = None,
    decision_body: str = "",
    city: str = "",
) -> dict[str, Any]:
    """Applicant counsel by volume with leave and judicial review grant rates."""

    def build() -> dict[str, Any]:
        filters = {"city": city, "year_from": year_from, "year_to": year_to, "decision_body": decision_body}
        rows = db.execute(
            _filtered(
                select(
                    FCActivitySummary.applicant_counsel_key,
                    FCActivitySummary.applicant_counsel_name,
                    FCActivitySummary.leave_result,
                    FCActivitySummary.review_result,
                    FCActivitySummary.resolution,
                    func.count().label("count"),
                ).where(FCActivitySummary.applicant_counsel_key.is_not(None)),
                **filters,
            ).group_by(
                FCActivitySummary.applicant_counsel_key,
                FCActivitySummary.applicant_counsel_name,
                FCActivitySummary.leave_result,
                FCActivitySummary.review_result,
                FCActivitySummary.resolution,
            )
        ).all()
        counsel: dict[str, dict[str, Any]] = {}
        for row in rows:
            entry = counsel.setdefault(row.applicant_counsel_key, {"key": row.applicant_counsel_key, "names": {}, "files": 0, "leave_granted": 0, "leave_refused": 0, "jr_granted": 0, "jr_dismissed": 0, "consent": 0})
            count = int(row.count)
            entry["files"] += count
            if row.applicant_counsel_name:
                entry["names"][row.applicant_counsel_name] = entry["names"].get(row.applicant_counsel_name, 0) + count
            if row.leave_result in {"granted", "refused"}:
                entry[f"leave_{row.leave_result}"] += count
            if row.review_result in {"granted", "dismissed"}:
                entry[f"jr_{row.review_result}"] += count
            if row.resolution == "resolved_by_consent":
                entry["consent"] += count
        result = []
        for entry in counsel.values():
            if entry["files"] < min_files:
                continue
            leave_total = entry["leave_granted"] + entry["leave_refused"]
            jr_total = entry["jr_granted"] + entry["jr_dismissed"]
            result.append(
                {
                    "key": entry["key"],
                    "name": max(entry["names"].items(), key=lambda item: item[1])[0] if entry["names"] else entry["key"],
                    "files": entry["files"],
                    "leave_decisions": leave_total,
                    "leave_grant_rate": _rate(entry["leave_granted"], leave_total),
                    "jr_decisions": jr_total,
                    "jr_grant_rate": _rate(entry["jr_granted"], jr_total),
                    "resolved_by_consent": entry["consent"],
                }
            )
        result.sort(key=lambda row: (-row["files"], row["name"]))
        return {
            "min_files": min_files,
            "filters": {key: value for key, value in filters.items() if value not in ("", None)},
            "counsel": result,
            "note": "Counsel is named in about a quarter of files (certificates of service and hearing appearances), so these are partial counts.",
        }

    return _cached(("counsel", min_files, year_from, year_to, decision_body.strip(), city.strip()), build)


MOTION_TYPE_LABELS = {
    "stay_of_removal": "Stay of removal",
    "stay_of_release": "Stay of release or tribunal order (Minister)",
    "extension_of_time": "Extension of time",
    "judgment_on_consent": "Consent judgment / allow the application",
    "reconsideration": "Reconsideration",
    "adjournment": "Adjournment",
    "abeyance": "Abeyance",
    "dismiss_or_strike": "Dismiss or strike",
    "amendment": "Amendment",
    "confidentiality": "Confidentiality",
    "production_or_record": "Production or record",
    "further_evidence": "Further evidence",
    "consolidation": "Consolidation",
    "counsel": "Change or removal of counsel",
    "intervention": "Intervention",
    "expedite": "Expedite",
    "release_or_detention": "Release or detention",
    "costs": "Costs",
    "other": "Other",
}


def fetch_fc_activity_motions(
    db: Session,
    *,
    city: str = "",
    year_from: int | None = None,
    year_to: int | None = None,
) -> dict[str, Any]:
    """Motions by type: how often they are filed, granted, dismissed or never ruled on, and how long rulings take."""

    def build() -> dict[str, Any]:
        statement = select(FCActivityMotion.motion_type, FCActivityMotion.filer, FCActivityMotion.outcome, FCActivityMotion.days_to_decision)
        if city.strip():
            statement = statement.where(FCActivityMotion.city_filed == city.strip())
        if year_from is not None:
            statement = statement.where(FCActivityMotion.year >= year_from)
        if year_to is not None:
            statement = statement.where(FCActivityMotion.year <= year_to)
        types: dict[str, dict[str, Any]] = {}
        for row in db.execute(statement):
            entry = types.setdefault(row.motion_type, {"motions": 0, "outcomes": {}, "by_filer": {}, "days": []})
            entry["motions"] += 1
            entry["outcomes"][row.outcome] = entry["outcomes"].get(row.outcome, 0) + 1
            filer = entry["by_filer"].setdefault(row.filer or "unknown", {"granted": 0, "dismissed": 0})
            if row.outcome in {"granted", "granted_in_part"}:
                filer["granted"] += 1
            elif row.outcome == "dismissed":
                filer["dismissed"] += 1
            if row.days_to_decision is not None and 0 <= row.days_to_decision <= 730:
                entry["days"].append(int(row.days_to_decision))
        rows = []
        for motion_type, entry in types.items():
            granted = entry["outcomes"].get("granted", 0) + entry["outcomes"].get("granted_in_part", 0)
            dismissed = entry["outcomes"].get("dismissed", 0)
            rows.append(
                {
                    "type": motion_type,
                    "label": MOTION_TYPE_LABELS.get(motion_type, motion_type),
                    "motions": entry["motions"],
                    "granted": granted,
                    "dismissed": dismissed,
                    "grant_rate": _rate(granted, granted + dismissed),
                    "withdrawn": entry["outcomes"].get("withdrawn", 0),
                    "not_ruled": sum(count for key, count in entry["outcomes"].items() if key not in {"granted", "granted_in_part", "dismissed", "withdrawn", "moot", "declined_to_hear", "ruled_unclear", "ruled_in_related_file"}),
                    "not_ruled_reasons": {key: count for key, count in entry["outcomes"].items() if key not in {"granted", "granted_in_part", "dismissed", "withdrawn", "moot", "declined_to_hear", "ruled_unclear", "ruled_in_related_file"}},
                    "median_days_to_ruling": int(median(entry["days"])) if entry["days"] else None,
                    "person_grant_rate": _rate(entry["by_filer"].get("person", {}).get("granted", 0), sum(entry["by_filer"].get("person", {}).values())),
                    "government_grant_rate": _rate(entry["by_filer"].get("government", {}).get("granted", 0), sum(entry["by_filer"].get("government", {}).values())),
                }
            )
        rows.sort(key=lambda row: -row["motions"])
        return {
            "filters": {key: value for key, value in {"city": city, "year_from": year_from, "year_to": year_to}.items() if value not in ("", None)},
            "total_motions": sum(row["motions"] for row in rows),
            "types": rows,
            "note": "Grant rates use motions with a ruling linked to them. Person/government is the side that brought the motion (the Minister is the applicant when the Minister filed the leave application). 'Not ruled' covers motions overtaken by the end of the file, removed from the list, or still pending.",
        }

    return _cached(("motions", city.strip(), year_from, year_to), build)


# ---------------------------------------------------------------------------
# Dashboard: every aggregate the FC Analytics tab draws, for one filter slice.
# ---------------------------------------------------------------------------

DASHBOARD_FILTERS = {
    "city": FCActivitySummary.city_filed,
    "decision_body": FCActivitySummary.decision_body,
    "application_type": FCActivitySummary.application_type,
    "representation": FCActivitySummary.representation,
    "language": FCActivitySummary.proceeding_language,
    "office": FCActivitySummary.office_location,
    "resolution": FCActivitySummary.resolution,
    "counsel": FCActivitySummary.applicant_counsel_key,
}
OUTCOME_GROUPS = {
    "leave_refused": "leave_refused",
    "judicial_review_granted": "jr_granted",
    "judicial_review_dismissed": "jr_dismissed",
    "resolved_by_consent": "settled",
    "discontinued": "discontinued",
    "withdrawn": "discontinued",
}


def _dashboard_where(statement, filters: dict[str, Any]):
    if filters.get("year_from") is not None:
        statement = statement.where(FCActivitySummary.year >= filters["year_from"])
    if filters.get("year_to") is not None:
        statement = statement.where(FCActivitySummary.year <= filters["year_to"])
    for key, column in DASHBOARD_FILTERS.items():
        value = filters.get(key)
        if value:
            statement = statement.where(column == value)
    judge = filters.get("judge")
    if judge:
        statement = statement.where((FCActivitySummary.leave_judge_key == judge) | (FCActivitySummary.merits_judge_key == judge))
    return statement


def fetch_fc_activity_dashboard(db: Session, **raw_filters: Any) -> dict[str, Any]:
    filters = {key: value for key, value in raw_filters.items() if value not in (None, "")}

    def build() -> dict[str, Any]:
        columns = (
            FCActivitySummary.year,
            FCActivitySummary.city_filed,
            FCActivitySummary.resolution,
            FCActivitySummary.leave_result,
            FCActivitySummary.review_result,
            FCActivitySummary.decision_body,
            FCActivitySummary.office_location,
            FCActivitySummary.days_filing_to_perfection,
            FCActivitySummary.days_filing_to_leave_decision,
            FCActivitySummary.days_leave_grant_to_hearing,
            FCActivitySummary.days_hearing_to_judgment,
            FCActivitySummary.days_filing_to_final_disposition,
            FCActivitySummary.days_decision_to_filing,
            FCActivitySummary.filing_timeliness,
            FCActivitySummary.record_timeliness,
            FCActivitySummary.memorandum_timeliness,
            FCActivitySummary.hearing_window,
            FCActivitySummary.leave_refusal_reason,
            FCActivitySummary.representation,
        )
        rows = db.execute(_dashboard_where(select(*columns), filters)).all()
        files = len(rows)

        def rate(granted: int, other: int) -> float | None:
            return _rate(granted, granted + other)

        leave_granted = sum(1 for row in rows if row.leave_result == "granted")
        leave_refused = sum(1 for row in rows if row.leave_result == "refused")
        jr_granted = sum(1 for row in rows if row.review_result == "granted")
        jr_dismissed = sum(1 for row in rows if row.review_result == "dismissed")
        settled = sum(1 for row in rows if row.resolution == "resolved_by_consent")
        perfected = sum(1 for row in rows if row.days_filing_to_perfection is not None)
        leave_days = [row.days_filing_to_leave_decision for row in rows if row.days_filing_to_leave_decision is not None and row.days_filing_to_leave_decision <= 3650]

        by_year: dict[int, dict[str, Any]] = {}
        for row in rows:
            if row.year is None:
                continue
            bucket = by_year.setdefault(int(row.year), {"year": int(row.year), "files": 0, "leave_granted": 0, "leave_refused": 0, "jr_granted": 0, "jr_dismissed": 0, "outcomes": {}, "_leave_days": []})
            bucket["files"] += 1
            group = OUTCOME_GROUPS.get(row.resolution or "", "other" if row.resolution not in (None, "unknown") else "open_or_unknown")
            bucket["outcomes"][group] = bucket["outcomes"].get(group, 0) + 1
            if row.leave_result in {"granted", "refused"}:
                bucket[f"leave_{row.leave_result}"] += 1
            if row.review_result in {"granted", "dismissed"}:
                bucket[f"jr_{row.review_result}"] += 1
            if row.days_filing_to_leave_decision is not None and row.days_filing_to_leave_decision <= 3650:
                bucket["_leave_days"].append(row.days_filing_to_leave_decision)
        year_rows = []
        for year in sorted(by_year):
            bucket = by_year[year]
            days = bucket.pop("_leave_days")
            bucket["leave_grant_rate"] = rate(bucket["leave_granted"], bucket["leave_refused"])
            bucket["jr_grant_rate"] = rate(bucket["jr_granted"], bucket["jr_dismissed"])
            bucket["median_days_to_leave"] = int(median(days)) if days else None
            year_rows.append(bucket)

        def grouped(attribute: str, limit: int = 20) -> list[dict[str, Any]]:
            groups: dict[str, dict[str, int]] = {}
            for row in rows:
                key = getattr(row, attribute) or "unknown"
                bucket = groups.setdefault(key, {"files": 0, "leave_granted": 0, "leave_refused": 0, "jr_granted": 0, "jr_dismissed": 0})
                bucket["files"] += 1
                if row.leave_result in {"granted", "refused"}:
                    bucket[f"leave_{row.leave_result}"] += 1
                if row.review_result in {"granted", "dismissed"}:
                    bucket[f"jr_{row.review_result}"] += 1
            result = [
                {"value": key, **values, "leave_grant_rate": rate(values["leave_granted"], values["leave_refused"]), "jr_grant_rate": rate(values["jr_granted"], values["jr_dismissed"])}
                for key, values in groups.items()
            ]
            result.sort(key=lambda item: -item["files"])
            return result[:limit]

        def counts(attribute: str) -> list[dict[str, Any]]:
            tally: dict[str, int] = {}
            for row in rows:
                key = getattr(row, attribute) or "unknown"
                tally[key] = tally.get(key, 0) + 1
            return [{"value": key, "count": count} for key, count in sorted(tally.items(), key=lambda item: -item[1])]

        durations = {}
        for field, label in {
            "days_decision_to_filing": "Decision to filing",
            "days_filing_to_perfection": "Filing to applicant's record",
            "days_filing_to_leave_decision": "Filing to leave decision",
            "days_leave_grant_to_hearing": "Leave granted to hearing",
            "days_hearing_to_judgment": "Hearing to judgment",
            "days_filing_to_final_disposition": "Filing to final outcome",
        }.items():
            values = [getattr(row, field) for row in rows if getattr(row, field) is not None and 0 <= getattr(row, field) <= 3650]
            durations[field] = {"label": label, **_quantiles(values)}

        motion_types: dict[str, dict[str, Any]] = {}
        if rows:
            motion_statement = select(FCActivityMotion.motion_type, FCActivityMotion.outcome, FCActivityMotion.days_to_decision).where(
                FCActivityMotion.source_case_id.in_(_dashboard_where(select(FCActivitySummary.source_case_id), filters))
            )
            for motion in db.execute(motion_statement):
                bucket = motion_types.setdefault(motion.motion_type, {"type": motion.motion_type, "label": MOTION_TYPE_LABELS.get(motion.motion_type, motion.motion_type), "motions": 0, "granted": 0, "dismissed": 0, "withdrawn": 0, "not_ruled": 0, "_days": []})
                bucket["motions"] += 1
                if motion.outcome in {"granted", "granted_in_part"}:
                    bucket["granted"] += 1
                elif motion.outcome == "dismissed":
                    bucket["dismissed"] += 1
                elif motion.outcome == "withdrawn":
                    bucket["withdrawn"] += 1
                elif motion.outcome not in {"moot", "declined_to_hear", "ruled_unclear", "ruled_in_related_file"}:
                    bucket["not_ruled"] += 1
                if motion.days_to_decision is not None and 0 <= motion.days_to_decision <= 730:
                    bucket["_days"].append(motion.days_to_decision)
        motion_rows = []
        for bucket in motion_types.values():
            days = bucket.pop("_days")
            bucket["grant_rate"] = rate(bucket["granted"], bucket["dismissed"])
            bucket["median_days"] = int(median(days)) if days else None
            motion_rows.append(bucket)
        motion_rows.sort(key=lambda item: -item["motions"])
        stays = next((item for item in motion_rows if item["type"] == "stay_of_removal"), None)

        return {
            "filters": filters,
            "kpis": {
                "files": files,
                "leave_decisions": leave_granted + leave_refused,
                "leave_grant_rate": rate(leave_granted, leave_refused),
                "jr_decisions": jr_granted + jr_dismissed,
                "jr_grant_rate": rate(jr_granted, jr_dismissed),
                "settled": settled,
                "median_days_to_leave": int(median(leave_days)) if leave_days else None,
                "record_filed": perfected,
                "stay_grant_rate": stays["grant_rate"] if stays else None,
                "stay_rulings": (stays["granted"] + stays["dismissed"]) if stays else 0,
            },
            "funnel": [
                {"stage": "Filed", "count": files},
                {"stage": "Leave decided", "count": leave_granted + leave_refused},
                {"stage": "Leave granted", "count": leave_granted},
                {"stage": "Judgment on the merits", "count": jr_granted + jr_dismissed},
                {"stage": "Judicial review granted", "count": jr_granted},
            ],
            "by_year": year_rows,
            "by_decision_body": grouped("decision_body"),
            "by_office": [item for item in grouped("office_location", 16) if item["value"] != "unknown"][:15],
            "by_city": grouped("city_filed", 12),
            "durations": durations,
            "motions": motion_rows,
            "compliance": {
                "filing_timeliness": counts("filing_timeliness"),
                "record_timeliness": counts("record_timeliness"),
                "memorandum_timeliness": counts("memorandum_timeliness"),
                "hearing_window": counts("hearing_window"),
            },
            "refusal_reasons": counts("leave_refusal_reason"),
            "representation": counts("representation"),
        }

    key = ("dashboard",) + tuple(sorted(filters.items()))
    return _cached(key, build)
