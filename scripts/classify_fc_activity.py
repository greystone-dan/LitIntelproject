"""Deterministically classify Federal Court activity milestones without writing to the database."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import select

from backend.database import FCActivityCase, FCActivityClassification, FCActivityDocument, SessionLocal, init_db

CLASSIFIER_VERSION = "fc_activity_v3"


@dataclass(frozen=True)
class Evidence:
    status: str
    date: str | None
    doc_id: int | None
    re_no: str | None
    docno: str | None
    text: str | None
    rule: str | None


@dataclass(frozen=True)
class ActivityEvent:
    activity_case_id: int
    citation: str | None
    case_name: str | None
    doc_id: int
    doc_date: date | None
    text: str
    re_no: str | None = None
    docno: str | None = None


RULES: dict[str, tuple[str, tuple[str, ...]]] = {
    "application_filed": (
        "application_filed",
        (
            r"application for leave and judicial review",
            r"application for leave .* judicial review",
            r"demande d['’]autorisation et de contrôle judiciaire",
            r"notice of application .* judicial review",
        ),
    ),
    "application_perfected": (
        "application_perfected",
        (
            r"application record .* filed",
            r"applicant['’]?s record .* filed",
            r"record .* on behalf of applicant .* filed",
            r"record number of copies received/prepared\s*:?\s*.* on behalf of applicant",
            r"dossier(?: \(demande\))? nombre de copies reçu(?:e)?/préparé(?:e)?",
            r"dossier de la partie demanderesse .* déposé",
            r"dossier de la partie demanderesse .* depose",
        ),
    ),
    "leave_granted": (
        "leave_granted",
        (
            r"granting the application for leave",
            r"application for leave granted",
            r"accordant la demande d['’]autorisation",
            r"demande d['’]autorisation .* accordée",
            r"demande d['’]autorisation .* accordee",
        ),
    ),
    "leave_refused": (
        "leave_refused",
        (
            r"dismissing the application for leave",
            r"dismissing .* application for leave",
            r"application for leave dismissed",
            r"application for leave:\s*dismissed",
            r"rejetant la demande d['’]autorisation",
            r"demande d['’]autorisation .* rejetée",
            r"demande d['’]autorisation .* rejetee",
        ),
    ),
    "final_decision": (
        "final_decision",
        (
            r"\(final decision\)",
            r"final decision",
            r"\(décision finale\)",
            r"\(decision finale\)",
            r"reasons for judgment and judgment",
            r"reasons for judgment .* judgment",
        ),
    ),
    "leave_final_decision": (
        "leave_final_decision",
        (r"\(final decision\).*application for leave", r"\(décision finale\).*demande d['’]autorisation", r"final decision.*application for leave"),
    ),
    "motion_final_decision": (
        "motion_final_decision",
        (r"\(final decision\).*motion", r"final decision.*motion", r"order rendered.*motion.*decision filed"),
    ),
    "stay_decision": (
        "stay_decision",
        (r"stay of execution", r"staying the removal", r"stay application", r"sursis à l'exécution"),
    ),
    "judicial_review_granted": (
        "judicial_review_granted",
        (
            r"judicial review result:\s*granted",
            r"judicial review .* result:\s*granted",
            r"result:\s*granted .* judicial review",
            r"contrôle judiciaire .* accord",
            r"accordant la demande de contrôle judiciaire",
            r"granting the application for judicial review",
        ),
    ),
    "judicial_review_dismissed": (
        "judicial_review_dismissed",
        (
            r"judicial review result:\s*dismissed",
            r"judicial review .* result:\s*dismissed",
            r"result:\s*dismissed .* judicial review",
            r"dismissing the application for judicial review",
            r"contrôle judiciaire .* rejet",
            r"rejetant la demande de contrôle judiciaire",
        ),
    ),
    "hearing_held": (
        "hearing_held",
        (
            r"result of hearing",
            r"held in court",
            r"matter reserved",
            r"comparution en personne",
            r"audience .* tenue",
        ),
    ),
}

COMPILED_RULES = {
    name: (rule_name, tuple(re.compile(pattern, re.IGNORECASE) for pattern in patterns))
    for name, (rule_name, patterns) in RULES.items()
}


def _event_date(event: ActivityEvent) -> str | None:
    return event.doc_date.isoformat() if event.doc_date else None


def _match_events(events: Iterable[ActivityEvent], rule_key: str) -> list[tuple[ActivityEvent, re.Match[str]]]:
    _, patterns = COMPILED_RULES[rule_key]
    matches: list[tuple[ActivityEvent, re.Match[str]]] = []
    for event in events:
        for pattern in patterns:
            match = pattern.search(event.text)
            if match:
                matches.append((event, match))
                break
    return matches


def _evidence(events: list[ActivityEvent], rule_key: str, *, latest: bool = False) -> Evidence:
    matches = [
        item
        for item in _match_events(events, rule_key)
        if not (rule_key == "final_decision" and "cancelled" in item[0].text.casefold())
    ]
    if not matches:
        return Evidence("unknown", None, None, None, None, None, "no_matching_entry")
    event, match = (max(matches, key=lambda item: (item[0].doc_date or date.min, item[0].doc_id)) if latest else min(matches, key=lambda item: (item[0].doc_date or date.max, item[0].doc_id)))
    return Evidence("yes", _event_date(event), event.doc_id, event.re_no, event.docno, event.text, f"{rule_key}:{match.group(0)}")


def _perfection_status(events: list[ActivityEvent], application_perfected: Evidence) -> dict[str, Any]:
    if application_perfected.status == "yes":
        return {**asdict(application_perfected), "status": "perfected"}
    negative_patterns = (
        r"failure to file an application record",
        r"application record not filed",
        r"applicant['’]?s record not filed",
        r"dossier de la partie demanderesse .* non déposé",
    )
    for event in events:
        for pattern in negative_patterns:
            match = re.search(pattern, event.text, re.IGNORECASE)
            if match:
                return {"status": "not_perfected", "date": _event_date(event), "doc_id": event.doc_id, "re_no": event.re_no, "docno": event.docno, "text": event.text, "rule": f"perfection_failure:{match.group(0)}"}
    return {"status": "unknown", "date": None, "doc_id": None, "re_no": None, "docno": None, "text": None, "rule": "no_perfection_signal"}


def _artifact_type(text: str) -> str:
    patterns = (
        ("copy_related_file", r"copy of|original (?:file|filed) on court file|attached schedule"),
        ("service_or_acknowledgment", r"proof of service|certificate of service|acknowledgment of receipt"),
        ("translation", r"certified (?:french )?translation"),
        ("registry_note", r"memorandum to file|communication to the court|letter advising"),
        ("hearing_record", r"result of hearing|held in court|matter reserved|case management conference"),
        ("substantive_order", r"final decision|décision finale|order rendered|judgment rendered|jugement rendu"),
        ("filing", r"filed|déposé|depose|received|reçu"),
    )
    for kind, pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return kind
    return "other"


def _history_profile(events: list[ActivityEvent], resolution: dict[str, Any]) -> dict[str, Any]:
    today = date.today()
    all_dates = [event.doc_date for event in events if event.doc_date]
    substantive = [event for event in events if _artifact_type(event.text) not in {"copy_related_file", "service_or_acknowledgment", "translation"}]
    last_any = max(all_dates) if all_dates else None
    last_substantive = max((event.doc_date for event in substantive if event.doc_date), default=None)
    age = (today - last_any).days if last_any else None
    if resolution["status"] != "unknown":
        completeness = "likely_complete"
    elif events and _artifact_type(events[-1].text) in {"copy_related_file", "service_or_acknowledgment", "translation", "registry_note"}:
        completeness = "incomplete"
    else:
        completeness = "unknown"
    counts = {}
    for event in events:
        kind = _artifact_type(event.text)
        counts[kind] = counts.get(kind, 0) + 1
    return {"completeness": completeness, "last_any_entry_date": last_any.isoformat() if last_any else None, "last_substantive_entry_date": last_substantive.isoformat() if last_substantive else None, "days_since_last_entry": age, "artifact_counts": counts}


def _closing_status(events: list[ActivityEvent], leave_result: str, review_result: str) -> dict[str, Any]:
    """Derive the IMM-level closing signal from the three latest docket entries."""
    recent = events[-3:]
    patterns: tuple[tuple[str, str], ...] = (
        ("discontinued", r"notice of discontinuance|\bdiscontinuance\b|désistement|desistement"),
        ("administratively_terminated", r"application terminated by s\.?\s*87\.4\(1\) of irpa"),
        ("abeyance", r"held in abeyance until|file is held in abeyance"),
        ("leave_refused", r"dismissing the application for leave|application for leave:\s*dismissed|rejetant la demande d['’]autorisation|rejetant la demande d['’]autorisation"),
        ("judicial_review_granted", r"judicial review result:\s*granted|contrôle judiciaire .* accord"),
        ("judicial_review_dismissed", r"judicial review result:\s*dismissed|dismissing the application for judicial review|contrôle judiciaire .* rejet"),
            ("withdrawn", r"notice of withdrawal|retrait de la demande"),
            ("underlying_decision_pending", r"no decision has yet been made, as such, no reasons exist|aucune décision n['’]a encore été rendue"),
            ("case_management", r"case management conference|parties are to consult each other to reach consent"),
    )
    for event in reversed(recent):
        for status, pattern in patterns:
            match = re.search(pattern, event.text, re.IGNORECASE)
            if match:
                if status.startswith("judicial_review") and leave_result != "granted":
                    continue
                return {
                    "status": status,
                    "date": _event_date(event),
                    "doc_id": event.doc_id,
                    "re_no": event.re_no,
                    "docno": event.docno,
                    "text": event.text,
                    "rule": f"last_three:{status}:{match.group(0)}",
                }
    return {"status": "unknown", "date": None, "doc_id": None, "re_no": None, "docno": None, "text": None, "rule": "no_closing_signal_in_last_three"}


def _full_history_resolution(events: list[ActivityEvent], leave_result: str) -> dict[str, Any]:
    """Find the decisive IMM-level outcome across the complete docket history."""
    rules: tuple[tuple[str, str], ...] = (
        ("judicial_review_granted", r"judicial review result:\s*granted|result:\s*granted .* judicial review|contrôle judiciaire .* accord|accordant la demande de contrôle judiciaire|granting the application for judicial review"),
        ("judicial_review_dismissed", r"judicial review result:\s*dismissed|dismissing the application for judicial review|contrôle judiciaire .* rejet|rejetant la demande de contrôle judiciaire"),
        ("leave_refused", r"dismissing the application for leave|application for leave:\s*dismissed|rejetant la demande d['’]autorisation"),
        ("discontinued", r"notice of discontinuance|\bdiscontinuance\b|désistement|desistement"),
        ("withdrawn", r"notice of withdrawal|retrait de la demande"),
        ("administratively_terminated", r"application terminated by s\.?\s*87\.4\(1\)(?:\s+of)?\s*irpa|termination under s\.?\s*87\.4\(1\)"),
    )
    matches: list[tuple[ActivityEvent, str, re.Match[str]]] = []
    for event in events:
        for status, pattern in rules:
            match = re.search(pattern, event.text, re.IGNORECASE)
            if match:
                if status.startswith("judicial_review") and leave_result != "granted":
                    continue
                if "cancelled" in event.text.casefold():
                    continue
                matches.append((event, status, match))
                break
    if not matches:
        return {"status": "unknown", "date": None, "doc_id": None, "re_no": None, "docno": None, "text": None, "rule": "no_decisive_signal_in_full_history"}
    all_matches = matches
    final_markers = ("final decision", "décision finale", "decision finale", "judgment rendered", "jugement rendu", "reasons for judgment")
    final_matches = [item for item in matches if any(marker in item[0].text.casefold() for marker in final_markers)]
    if final_matches:
        matches = final_matches
    if any(status == "leave_refused" for _, status, _ in all_matches):
        leave_matches = [item for item in all_matches if item[1] == "leave_refused"]
        if leave_matches:
            event, status, match = min(leave_matches, key=lambda item: (item[0].doc_date or date.max, item[0].doc_id))
            return {"status": status, "date": _event_date(event), "doc_id": event.doc_id, "re_no": event.re_no, "docno": event.docno, "text": event.text, "rule": f"full_history:{status}:{match.group(0)}"}
    event, status, match = max(matches, key=lambda item: (item[0].doc_date or date.min, item[0].doc_id))
    return {"status": status, "date": _event_date(event), "doc_id": event.doc_id, "re_no": event.re_no, "docno": event.docno, "text": event.text, "rule": f"full_history:{status}:{match.group(0)}"}


def _challenged_decision(events: list[ActivityEvent]) -> dict[str, Any]:
    """Parse the originating application entry into challenged-decision fields."""
    application_patterns = (
        re.compile(r"application for leave(?: and|,)? judicial review(?: and mandamus)?", re.IGNORECASE),
        re.compile(r"demande d['’]autorisation(?: et|,)? de contrôle judiciaire", re.IGNORECASE),
        re.compile(r"notice of application .* judicial review", re.IGNORECASE),
    )
    event = next((item for item in events if any(pattern.search(item.text) for pattern in application_patterns)), None)
    if event is None:
        return {"status": "unknown", "application_type": None, "decision_maker": None, "decision_date": None, "tribunal_file_numbers": [], "doc_id": None, "re_no": None, "docno": None, "text": None, "rule": "no_originating_application_entry"}
    text = event.text
    lowered = text.casefold()
    category_rules = (
        ("irb_refugee_or_appeal", r"\b(?:irb|rpd|rad|crdd|cisr|iad|id)\b|refugee protection division|section de la protection des réfugiés|section d['’]appel des réfugiés"),
        ("cbsa_enforcement", r"\b(?:cbsa|asfc)\b|canada border services|agence des services frontaliers|border services agency|services frontaliers"),
        ("cic_ircc_processing", r"\b(?:cic|ircc)\b|citizenship and immigration|immigration canada|case processing centre"),
        ("visa_office_or_consulate", r"consulate|consulat|embassy|ambassade|high commission|visa office"),
        ("minister_or_department", r"\b(?:mci|mpsep)\b|minister|ministre|department of citizenship"),
        ("mandamus", r"\bmandamus\b"),
        ("extension_of_time", r"extension of time|prorogation de délai"),
        ("removal_or_exclusion", r"removal|deportation|exclusion|renvoi|mesure d['’]exclusion|sursis.*renvoi"),
        ("detention", r"detention|detained|détention|detenu|détenu"),
        ("inadmissibility", r"inadmissib|criminality|security|misrepresentation|interdiction de territoire"),
        ("citizenship", r"citizenship|citoyenneté"),
        ("permanent_residence", r"permanent resident|permanent residence|résidence permanente"),
        ("temporary_residence", r"study permit|work permit|visitor visa|temporary resident|permis d['’]études|permis de travail|résident temporaire"),
        ("provincial_nominee", r"provincial nominee|provincial nominee program|programme des candidats des provinces"),
    )
    challenge_categories = [category for category, pattern in category_rules if re.search(pattern, text, re.IGNORECASE)]
    application_type = "leave_and_judicial_review"
    if re.search(r"notice of application .* judicial review", text, re.IGNORECASE) and not re.search(r"leave|autorisation", text, re.IGNORECASE):
        application_type = "direct_judicial_review"
    if "mandamus" in lowered:
        application_type = "leave_judicial_review_and_mandamus"
    if "extension of time" in lowered or "prorogation de délai" in lowered:
        application_type += "_extension_of_time"
    decision_date_match = re.search(r"(?:decision|décision|decision)\s+(?:of|du|de)?\s*[^,;]+?,?\s*(?:dated|rendue?\s+le|rendered\s+on)\s+(\d{1,2}[-/][A-Za-z]{3,9}[-/]\d{2,4}|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{1,2}[A-Za-z]{3,9}\d{2,4})", text, re.IGNORECASE)
    if decision_date_match is None:
        decision_date_match = re.search(r"\b(?:dated|rendue?\s+le)\s+(\d{1,2}[-/]?[A-Za-z]{3,9}[-/]?\d{2,4})", text, re.IGNORECASE)
    if decision_date_match is None:
        decision_date_match = re.search(r"against (?:a )?decision\s+[^,]+,\s*(\d{1,2}-[A-Za-z]{3,9}-\d{2,4})", text, re.IGNORECASE)
    tribunal_file_numbers = sorted(set(re.findall(r"\b[A-Z]{1,4}\d[-A-Z0-9]{3,}\b", text, re.IGNORECASE)))
    decision_maker = None
    marker = re.search(r"against (?:a )?decision\s+(.+?)(?:,\s*(?:mandamus|dated|file|IRB|RPD|RAD)\b|\s+dated\b|\s+file\s+no\.?\b)", text, re.IGNORECASE)
    if marker:
        decision_maker = _clean_origin_value(marker.group(1))
    if decision_maker is None:
        marker = re.search(r"(?:décision de|decisión de|decision of)\s+(.+?)(?:,\s*(?:rendue|dated|file|dans les dossiers)\b|\s+rendue\b)", text, re.IGNORECASE)
        if marker:
            decision_maker = _clean_origin_value(marker.group(1))
    return {"status": "yes", "application_type": application_type, "challenge_categories": challenge_categories, "decision_maker": decision_maker, "decision_date": decision_date_match.group(1) if decision_date_match else None, "tribunal_file_numbers": tribunal_file_numbers, "doc_id": event.doc_id, "re_no": event.re_no, "docno": event.docno, "text": event.text, "rule": "originating_application_entry"}


def _clean_origin_value(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip(" ,;:.")).strip()


def classify_events(events: Iterable[ActivityEvent]) -> dict[str, Any]:
    ordered = list(events)
    challenged_decision = _challenged_decision(ordered)
    application_filed = _evidence(ordered, "application_filed")
    application_perfected = _evidence(ordered, "application_perfected")
    leave_granted = _evidence(ordered, "leave_granted")
    leave_refused = _evidence(ordered, "leave_refused")
    final_decision = _evidence(ordered, "final_decision", latest=True)
    review_granted = _evidence(ordered, "judicial_review_granted", latest=True)
    review_dismissed = _evidence(ordered, "judicial_review_dismissed", latest=True)
    hearing_held = _evidence(ordered, "hearing_held")

    leave = leave_granted if leave_granted.status == "yes" else leave_refused
    leave_result = "granted" if leave_granted.status == "yes" else "refused" if leave_refused.status == "yes" else "unknown"
    preliminary_resolution = _full_history_resolution(ordered, leave_result)
    later_review_granted = _evidence(ordered, "judicial_review_granted", latest=True)
    later_review_dismissed = _evidence(ordered, "judicial_review_dismissed", latest=True)
    if leave_result == "unknown" and (later_review_granted.status == "yes" or later_review_dismissed.status == "yes"):
        leave_context = {"status": "inferred_granted", "evidence": asdict(later_review_granted if later_review_granted.status == "yes" else later_review_dismissed), "rule": "later_judicial_review_requires_leave"}
        effective_leave_result = "granted"
    elif leave_result == "unknown" and preliminary_resolution["status"] == "discontinued":
        leave_context = {"status": "not_relevant_discontinued", "evidence": preliminary_resolution, "rule": "discontinuance_before_confirmed_leave"}
        effective_leave_result = "unknown"
    elif leave_result == "unknown" and preliminary_resolution["status"] == "withdrawn":
        leave_context = {"status": "not_relevant_withdrawn", "evidence": preliminary_resolution, "rule": "withdrawal_before_confirmed_leave"}
        effective_leave_result = "unknown"
    elif leave_result == "unknown" and preliminary_resolution["status"] == "administratively_terminated":
        leave_context = {"status": "not_relevant_terminated", "evidence": preliminary_resolution, "rule": "administrative_termination_before_confirmed_leave"}
        effective_leave_result = "unknown"
    elif leave_result == "unknown" and challenged_decision.get("application_type") == "direct_judicial_review":
        leave_context = {"status": "not_applicable_direct_judicial_review", "evidence": challenged_decision, "rule": "direct_judicial_review_does_not_require_leave"}
        effective_leave_result = "unknown"
    else:
        leave_context = {"status": leave_result, "evidence": asdict(leave), "rule": "direct_leave_entry" if leave_result != "unknown" else "no_later_leave_resolution"}
        effective_leave_result = leave_result
    review_result = (
        "granted"
        if effective_leave_result == "granted" and review_granted.status == "yes"
        else "dismissed"
        if effective_leave_result == "granted" and review_dismissed.status == "yes"
        else "not_reached"
        if effective_leave_result == "refused"
        else "unknown"
    )
    judicial_review_final = final_decision if effective_leave_result == "granted" and review_result in {"granted", "dismissed"} else Evidence("unknown", None, None, None, None, None, "leave_not_confirmed_or_review_result_missing")
    closing_status = _closing_status(ordered, leave_result, review_result)
    full_history_resolution = _full_history_resolution(ordered, effective_leave_result)
    perfection_status = _perfection_status(ordered, application_perfected)
    leave_final_decision = _evidence(ordered, "leave_final_decision", latest=True)
    motion_final_decision = _evidence(ordered, "motion_final_decision", latest=True)
    stay_decision = _evidence(ordered, "stay_decision", latest=True)
    history_profile = _history_profile(ordered, full_history_resolution)

    return {
        "application_filed": asdict(application_filed),
        "application_perfected": asdict(application_perfected),
        "perfection_status": perfection_status,
        "leave_decision": {**asdict(leave), "result": leave_result},
        "leave_context": leave_context,
        "final_decision": asdict(final_decision),
        "leave_final_decision": asdict(leave_final_decision),
        "motion_final_decision": asdict(motion_final_decision),
        "stay_decision": asdict(stay_decision),
        "judicial_review_result": {"result": review_result, "granted": asdict(review_granted), "dismissed": asdict(review_dismissed)},
        "judicial_review_final_decision": asdict(judicial_review_final),
        "closing_status": closing_status,
        "full_history_resolution": full_history_resolution,
        "challenged_decision": challenged_decision,
        "history_profile": history_profile,
        "hearing_held": asdict(hearing_held),
    }


def classify_case(activity_case: FCActivityCase, documents: Iterable[FCActivityDocument]) -> dict[str, Any]:
    events = [
        ActivityEvent(
            activity_case_id=activity_case.id,
            citation=activity_case.citation,
            case_name=activity_case.case_name,
            doc_id=document.id,
            doc_date=document.doc_dt,
            text=" ".join((document.recorded_entry or "").split()),
            re_no=document.re_no,
            docno=document.docno,
        )
        for document in documents
        if (document.recorded_entry or "").strip()
    ]
    return {
        "activity_case_id": activity_case.id,
        "citation": activity_case.citation,
        "imm_number": activity_case.citation,
        "year": activity_case.year,
        "case_name": activity_case.case_name,
        "document_count": len(events),
        "classification": classify_events(events),
    }


def load_report(limit: int | None = None, citation: str | None = None, per_year: int | None = None) -> list[dict[str, Any]]:
    with SessionLocal() as session:
        if per_year:
            years = list(session.scalars(select(FCActivityCase.year).where(FCActivityCase.year.is_not(None)).distinct().order_by(FCActivityCase.year)))
            cases = []
            for year in years:
                statement = select(FCActivityCase).where(FCActivityCase.year == year).order_by(FCActivityCase.id).limit(per_year)
                if citation:
                    statement = statement.where(FCActivityCase.citation == citation.upper().strip())
                cases.extend(session.scalars(statement))
        else:
            statement = select(FCActivityCase).order_by(FCActivityCase.id)
            if citation:
                statement = statement.where(FCActivityCase.citation == citation.upper().strip())
            if limit:
                statement = statement.limit(limit)
            cases = list(session.scalars(statement))
        case_ids = [row.id for row in cases]
        documents = list(
            session.scalars(
                select(FCActivityDocument)
                .where(FCActivityDocument.case_id.in_(case_ids))
                .order_by(FCActivityDocument.case_id, FCActivityDocument.doc_dt, FCActivityDocument.id)
            )
        ) if case_ids else []
        documents_by_case: dict[int, list[FCActivityDocument]] = {}
        for document in documents:
            documents_by_case.setdefault(document.case_id, []).append(document)
        return [classify_case(row, documents_by_case.get(row.id, [])) for row in cases]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("data/eval/fc_activity_classification.json"))
    parser.add_argument("--csv-output", type=Path, default=None)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--per-year", type=int, default=None, help="Take this many IMM records from each available year")
    parser.add_argument("--citation", type=str, default=None, help="Classify one IMM citation")
    parser.add_argument("--write", action="store_true", help="Persist derived rows to fc_activity_classifications")
    parser.add_argument("--all", action="store_true", help="Persist the complete FC activity inventory in batches")
    parser.add_argument("--batch-size", type=int, default=500, help="Cases per full-inventory batch")
    return parser.parse_args()


def persist_report(report: list[dict[str, Any]]) -> int:
    written = 0
    with SessionLocal() as session:
        source_ids = [int(row["activity_case_id"]) for row in report]
        source_cases = {
            row.id: row
            for row in session.scalars(select(FCActivityCase).where(FCActivityCase.id.in_(source_ids)))
        }
        for row in report:
            source = source_cases.get(int(row["activity_case_id"]))
            if source is None:
                continue
            derived = session.scalar(
                select(FCActivityClassification).where(FCActivityClassification.source_case_id == source.id)
            )
            values = {
                "source_case_id": source.id,
                "source_key": source.source_key,
                "imm_number": source.citation,
                "year": source.year,
                "case_name": source.case_name,
                "date_filed": source.date_filed,
                "city_filed": source.city_filed,
                "nature": source.nature,
                "case_class": source.case_class,
                "track": source.track,
                "source_url": source.source_url,
                "scraped_timestamp": source.scraped_timestamp,
                "classification_json": row["classification"],
                "classifier_version": CLASSIFIER_VERSION,
                "classified_at": datetime.now(timezone.utc),
            }
            if derived is None:
                session.add(FCActivityClassification(**values))
            else:
                for key, value in values.items():
                    if key != "source_case_id":
                        setattr(derived, key, value)
            written += 1
        session.commit()
    return written


def persist_all(batch_size: int) -> int:
    written = 0
    last_id = 0
    while True:
        with SessionLocal() as session:
            cases = list(session.scalars(select(FCActivityCase).where(FCActivityCase.id > last_id).order_by(FCActivityCase.id).limit(batch_size)))
            if not cases:
                break
            case_ids = [case.id for case in cases]
            documents = list(session.scalars(select(FCActivityDocument).where(FCActivityDocument.case_id.in_(case_ids)).order_by(FCActivityDocument.case_id, FCActivityDocument.doc_dt, FCActivityDocument.id)))
            documents_by_case: dict[int, list[FCActivityDocument]] = {}
            for document in documents:
                documents_by_case.setdefault(document.case_id, []).append(document)
            report = [classify_case(case, documents_by_case.get(case.id, [])) for case in cases]
        written += persist_report(report)
        last_id = cases[-1].id
        print(f"written={written} last_source_case_id={last_id}", flush=True)
    return written


def main() -> None:
    args = parse_args()
    init_db()
    if args.all:
        if not args.write or args.limit or args.per_year or args.citation:
            raise SystemExit("--all requires --write and cannot be combined with filters")
        written = persist_all(args.batch_size)
        print(f"classified_cases={written} written={written}")
        return
    if args.limit and args.per_year:
        raise SystemExit("Use either --limit or --per-year, not both")
    report = load_report(limit=args.limit, citation=args.citation, per_year=args.per_year)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    if args.csv_output:
        args.csv_output.parent.mkdir(parents=True, exist_ok=True)
        fields = ["activity_case_id", "imm_number", "case_name", "document_count", "application_filed", "application_perfected", "leave_decision", "final_decision", "judicial_review_result", "hearing_held"]
        with args.csv_output.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            for row in report:
                output = {key: row.get(key) for key in fields[:4]}
                output.update({key: json.dumps(row["classification"].get(key), ensure_ascii=False) for key in fields[4:]})
                writer.writerow(output)
    written = persist_report(report) if args.write else 0
    print(f"classified_cases={len(report)} written={written} output={args.output}")


if __name__ == "__main__":
    main()
