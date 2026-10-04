"""Read-only hearing-to-judgment cohorts; Activity and canonical cases never mix.

Quantiles use linear interpolation at (n - 1) * p (including the median).
Same-day judgments are valid; judgments before hearings are excluded.
Activity years/filters are the summary's filing year, not judgment year.
Canonical hearing dates are only reader_extracted['date of hearing']; the
judgment date is Case.date. No filing, motion, docket, or inferred date fallback.
"""

from __future__ import annotations

import re
import unicodedata
from collections import Counter, defaultdict
from collections.abc import Iterable
from datetime import date, datetime
from typing import Any

MIN_SAMPLE = 10
FC_COURTS = ("FC", "Federal Court", "Federal Court of Canada")
MONTHS = {
    "january": 1, "jan": 1, "janvier": 1,
    "february": 2, "feb": 2, "fevrier": 2,
    "march": 3, "mar": 3, "mars": 3,
    "april": 4, "apr": 4, "avril": 4,
    "may": 5, "mai": 5, "june": 6, "jun": 6, "juin": 6,
    "july": 7, "jul": 7, "juillet": 7,
    "august": 8, "aug": 8, "aout": 8,
    "september": 9, "sep": 9, "sept": 9, "septembre": 9,
    "october": 10, "oct": 10, "octobre": 10,
    "november": 11, "nov": 11, "novembre": 11,
    "december": 12, "dec": 12, "decembre": 12,
}


def explicit_date(value: Any) -> date | None:
    """Accept calendar dates, producer YMD forms, and single named-month dates.

    The canonical producer preserves unrecognized strings. Reject ranges,
    multiple dates, timestamps, two-digit years and ambiguous numeric DMY/MDY.
    Activity dates have already been normalized to ISO by their producer.
    """
    if isinstance(value, datetime):
        return None
    if isinstance(value, date):
        return value
    if not isinstance(value, str):
        return None
    token = " ".join(value.split())
    numeric = re.fullmatch(r"(\d{4})(?:[-/]?)(\d{2})(?:[-/]?)(\d{2})", token)
    if numeric:
        parts = tuple(map(int, numeric.groups()))
    else:
        token = "".join(c for c in unicodedata.normalize("NFKD", token.casefold())
                        if not unicodedata.combining(c))
        day_first = re.fullmatch(r"(\d{1,2}) ([a-z]+)\.? (\d{4})", token)
        month_first = re.fullmatch(r"([a-z]+)\.? (\d{1,2}),? (\d{4})", token)
        if day_first:
            day, month, year = day_first.groups()
        elif month_first:
            month, day, year = month_first.groups()
        else:
            return None
        if month not in MONTHS:
            return None
        parts = (int(year), MONTHS[month], int(day))
    try:
        return date(*parts)
    except ValueError:
        return None


def timing_stats(values: Iterable[int]) -> dict[str, Any]:
    ordered = sorted(values)
    n = len(ordered)

    def quantile(p: float) -> float:
        index = (n - 1) * p
        lower = int(index)
        upper = min(lower + 1, n - 1)
        return ordered[lower] + (ordered[upper] - ordered[lower]) * (index - lower)

    return {
        "n": n, "suppressed": n < MIN_SAMPLE,
        "median_days": quantile(.5) if n >= MIN_SAMPLE else None,
        "p25_days": quantile(.25) if n >= MIN_SAMPLE else None,
        "p75_days": quantile(.75) if n >= MIN_SAMPLE else None,
    }


def _labels(value: Any) -> set[str]:
    """Stored string lists only; never infer taxonomy from prose."""
    if not isinstance(value, list):
        return set()
    return {" ".join(label.split()).casefold() for label in value
            if isinstance(label, str) and label.strip()
            and label.strip().casefold() != "unknown"}


def aggregate_timing(rows: Iterable[tuple]) -> dict[str, Any]:
    """Rows are (stable identity, cohort year, explicit hearing, judgment).

    Duplicate identities count once. Tiny year labels are never emitted; hidden
    counts describe only valid timed samples, not missing/invalid records.
    """
    seen = set()
    values = []
    yearly = defaultdict(list)
    issues, tags = defaultdict(list), defaultdict(list)
    exclusions = Counter(missing_dates=0, invalid_dates=0, reversed_dates=0,
                         duplicate_records=0)
    for row in rows:
        identity, year, start, end = row[:4]
        issue_labels, tag_labels = row[4:] if len(row) == 6 else ([], [])
        if identity in seen:
            exclusions["duplicate_records"] += 1
            continue
        seen.add(identity)
        if any(value is None or (isinstance(value, str) and not value.strip())
               for value in (start, end)):
            exclusions["missing_dates"] += 1
            continue
        hearing, judgment = explicit_date(start), explicit_date(end)
        if hearing is None or judgment is None:
            exclusions["invalid_dates"] += 1
            continue
        days = (judgment - hearing).days
        if days < 0:
            exclusions["reversed_dates"] += 1
            continue
        values.append(days)
        if isinstance(year, int) and not isinstance(year, bool):
            yearly[year].append(days)
        for label in _labels(issue_labels):
            issues[label].append(days)
        for label in _labels(tag_labels):
            tags[label].append(days)

    def visible(groups, key):
        return [{key: label, **timing_stats(values)}
                for label, values in sorted(groups.items()) if len(values) >= MIN_SAMPLE]

    def hidden(groups):
        values = [v for v in groups.values() if len(v) < MIN_SAMPLE]
        return {"groups": len(values), "samples": sum(map(len, values))}

    return {
        "overall": timing_stats(values),
        "by_year": visible(yearly, "year"),
        "by_issue": visible(issues, "issue"),
        "by_tag": visible(tags, "tag"),
        "hidden_groups": {"by_year": hidden(yearly), "by_issue": hidden(issues),
                          "by_tag": hidden(tags)},
        "eligible_records": len(seen),
        "excluded": dict(exclusions),
        "ungrouped_year_samples": len(values) - sum(map(len, yearly.values())),
    }


def _models():
    # Import only when a caller supplies a live session. Pure tests never load
    # database.py (which reads environment files and constructs an engine).
    from . import database
    return database


def _methodology() -> dict[str, Any]:
    return {
        "metric": "hearing_to_judgment_days", "minimum_sample": MIN_SAMPLE,
        "quantiles": "linear interpolation at (n - 1) * p",
        "chronology": "judgment >= hearing; same-day judgments included",
        "suppression": "n < 10: statistics null; grouped labels omitted; hidden group and timed membership counts disclosed",
        "count_unit": "distinct cohort records with two valid dates; overlapping label groups are not additive",
        "exclusions": "missing endpoint, invalid/ambiguous endpoint, reversed chronology; mutually exclusive per distinct record",
        "note": "Descriptive recorded-date coverage, not a ranking or prediction.",
    }


def fetch_fc_activity_timing(db, **filters: Any) -> dict[str, Any]:
    from sqlalchemy import select

    m = _models()
    c, s = m.FCActivityClassification, m.FCActivitySummary
    timeline = c.classification_json["timeline"]
    challenged = c.classification_json["challenged_decision"]
    statement = select(c.source_case_id, s.year,
                       timeline["judicial_review_heard"],
                       timeline["judicial_review_decided"],
                       challenged["decision_subject"],
                       challenged["challenge_categories"]).join(
                           s, s.source_case_id == c.source_case_id)
    # Match the active dashboard's summary filters, including judge-role OR.
    columns = {"city": s.city_filed, "decision_body": s.decision_body,
               "application_type": s.application_type, "representation": s.representation,
               "language": s.proceeding_language, "office": s.office_location,
               "resolution": s.resolution, "counsel": s.applicant_counsel_key}
    for key, column in columns.items():
        value = (filters.get(key) or "").strip()
        if value:
            statement = statement.where(column == value)
    if filters.get("year_from") is not None:
        statement = statement.where(s.year >= filters["year_from"])
    if filters.get("year_to") is not None:
        statement = statement.where(s.year <= filters["year_to"])
    judge = (filters.get("judge") or "").strip()
    if judge:
        statement = statement.where((s.leave_judge_key == judge) | (s.merits_judge_key == judge))
    with db.no_autoflush:
        rows = db.execute(statement.order_by(c.source_case_id)).all()
        result = aggregate_timing(
            (identity, year, start, end, [subject], categories)
            for identity, year, start, end, subject, categories in rows)
    return {**result, "cohort": "fc_activity_classifications",
            "year_basis": "summary filing year", "filters": filters,
            "group_sources": {
                "by_issue": "classification_json.challenged_decision.decision_subject",
                "by_tag": "classification_json.challenged_decision.challenge_categories",
                "note": "Stored Activity challenge subjects/categories, not canonical Case.issues or V3 tags; overlapping groups count each file once per label.",
            },
            "date_sources": {
                "hearing": "classification_json.timeline.judicial_review_heard",
                "judgment": "classification_json.timeline.judicial_review_decided",
            }, "methodology": _methodology()}


def fetch_judge_timing(db, slug: str) -> dict[str, Any]:
    """Independent of the profile's repeated Minister filters, like issues.

    Both comparison cohorts are canonical Federal Court decisions. Baseline
    includes the judge's cases; staged Activity never enters this comparison.
    """
    from sqlalchemy import func, select

    m = _models()
    c, j, link = m.Case, m.JudgeProfile, m.CaseJudgeProfile
    hearing = c.metadata_json["reader_extracted"]["date of hearing"]
    statement = select(c.id, c.date, hearing).where(
        func.lower(func.trim(c.court)).in_(tuple(name.casefold() for name in FC_COURTS)))
    with db.no_autoflush:
        profile = db.execute(select(j.id, j.slug).where(j.slug == slug)).first()
        if profile is None:
            return {"status": "unknown_judge"}
        judge_statement = statement.join(link, link.case_id == c.id).where(
            link.judge_profile_id == profile[0])
        judge_rows = db.execute(judge_statement.order_by(c.id)).all()
        baseline_rows = db.execute(statement.order_by(c.id)).all()

    def cohort(rows):
        return aggregate_timing((identity, None, start, end)
                                for identity, end, start in rows)

    judge_result, baseline = cohort(judge_rows), cohort(baseline_rows)
    return {
        "status": "ok", "slug": profile[1], "cohort": "canonical_federal_court",
        "judge": judge_result["overall"], "baseline": baseline["overall"],
        "coverage": {"judge": {"eligible_records": judge_result["eligible_records"],
                               "excluded": judge_result["excluded"]},
                     "baseline": {"eligible_records": baseline["eligible_records"],
                                  "excluded": baseline["excluded"]}},
        "minister_filter_applied": False,
        "filter_note": "Timing is independent of profile Minister filters.",
        "baseline_includes_judge": True, "methodology": _methodology(),
        "date_sources": {"hearing": "cases.metadata_json.reader_extracted.date of hearing",
                         "judgment": "cases.date"},
    }
