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

CLASSIFIER_VERSION = "fc_activity_v5"


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
            r"\bleave\s*(?:is\s*)?granted\b",
            r"\bresult\s*[-:]\s*leave\s+granted\b",
            r"accordant la demande d['’]autorisation",
            r"demande d['’]autorisation .* accordée",
            r"demande d['’]autorisation .* accordee",
            r"demande d['’]autorisation .* accordant",
            r"demande d['’]autorisation\s+(?:accordée|accordee|accordant)",
        ),
    ),
    "leave_refused": (
        "leave_refused",
        (
            r"dismissing the application for leave",
            r"dismissing .* application for leave",
            r"application for leave dismissed",
            r"application for leave:\s*dismissed",
            r"\bleave\s*(?:is\s*)?(?:refused|denied|dismissed)\b",
            r"\bresult\s*[-:]\s*leave\s+(?:refused|denied|dismissed)\b",
            r"leave denied on papers",
            r"rejetant la demande d['’]autorisation",
            r"demande d['’]autorisation .* rejetée",
            r"demande d['’]autorisation .* rejetee",
            r"demande d['’]autorisation .* refusée",
            r"demande d['’]autorisation .* refusee",
            r"demande d['’]autorisation\s+(?:refusée|refusee)",
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
        (
            r"stay of execution",
            r"staying the removal",
            r"stay application",
            r"sursis à l'exécution",
            r"removal (?:has been|was|is) cancelled",
            r"removal cancelled",
        ),
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


def _judge_name(text: str) -> str | None:
    match = re.search(
        r"\b(?:before|coram|devant|\(?presiding\s+judge\)?|rendered\s+by|rendu(?:e|es)?\s+par|rendu\(e\)\s+par)[,:]?\s*"
        r"(?:(?:the|la)\s+)?(?:honou?rable\s+)?(?:madam\s+justice\s+|mr\.\s+justice\s+|"
        r"ms\.\s+justice\s+|(?:monsieur|madame)\s+le\s+juge\s+|justice\s+|j\.\s+|"
        r"juge\s+|prothonotary\s+|protonotaire\s+)([A-Za-zÀ-ÖØ-öø-ÿ'’-]+\.?"
        r"(?:\s+[A-Za-zÀ-ÖØ-öø-ÿ'’-]+\.?){0,2}?)"
        r"(?=\s+(?:at|on|le|a|à|in|language|before|result|matter|dated)\b|[.,;]|$)",
        text,
        re.IGNORECASE,
    )
    return re.sub(r"\s+", " ", match.group(1)).strip(" .,;") if match else None


_MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
    "january": 1, "february": 2, "march": 3, "april": 4, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10,
    "november": 11, "december": 12,
    "janv": 1, "févr": 2, "fevr": 2, "mars": 3, "avr": 4, "mai": 5,
    "juin": 6, "juil": 7, "août": 8, "aout": 8, "sept": 9, "oct": 10,
    "nov": 11, "déc": 12, "dec": 12,
}
_DATE_TOKEN = r"\d{1,2}(?:[-/]\d{1,2}|[-/][A-Za-zÀ-ÖØ-öø-ÿ]{3,9})[-/]\d{2,4}|\d{1,2}\s+[A-Za-zÀ-ÖØ-öø-ÿ]{3,9}\s+\d{2,4}|[A-Za-zÀ-ÖØ-öø-ÿ]{3,9}\s+\d{1,2},\s*\d{2,4}"


def _normalize_date_token(value: str) -> str | None:
    cleaned = value.strip(" .,;:()")
    natural_match = re.fullmatch(r"([A-Za-zÀ-ÖØ-öø-ÿ]{3,9})\s+(\d{1,2}),\s*(\d{2,4})", cleaned)
    if natural_match:
        cleaned = f"{natural_match.group(2)} {natural_match.group(1)} {natural_match.group(3)}"
    parts = re.split(r"[-/\s]+", cleaned)
    if len(parts) != 3:
        return None
    try:
        day = int(parts[0])
        year = int(parts[2])
        if year < 100:
            year += 2000 if year < 50 else 1900
        month = int(parts[1]) if parts[1].isdigit() else _MONTHS.get(parts[1].casefold().rstrip("."))
        if month is None:
            return None
        return date(year, month, day).isoformat()
    except (TypeError, ValueError):
        return None


def _semantic_date(text: str, event_type: str) -> tuple[str | None, str]:
    filing_pattern = (r"(?:filed|déposée?|deposee?)\s+(?:on|le)?\s*(" + _DATE_TOKEN + r")", "filing_date")
    event_patterns = (
        (r"(?:rendered|rendu(?:e|es)?|rendu\(e\))[^\r\n]{0,180}?\b(?:on|le)\s*(" + _DATE_TOKEN + r")", "event_date"),
        (r"(?:held|tenue)\s+(?:on|le)?\s*(" + _DATE_TOKEN + r")", "event_date"),
        (r"(?:dated|date[eé]e?|on|le)\s+(" + _DATE_TOKEN + r")", "event_date"),
    )
    if event_type in {"leave_decision", "decision", "motion_decision"}:
        patterns = (*event_patterns, filing_pattern)
    else:
        patterns = (filing_pattern, *event_patterns)
    for pattern, date_kind in patterns:
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        if matches:
            normalized = _normalize_date_token(matches[-1].group(1))
            if normalized:
                if date_kind == "filing_date":
                    return normalized, date_kind
                if event_type != "application_filed" and date_kind == "event_date":
                    return normalized, date_kind
    return None, "source_document_date"


def _explicit_filing_date(text: str) -> str | None:
    pattern = r"(?:filed|déposée?|deposee?)\s+(?:on|le)?\s*(" + _DATE_TOKEN + r")"
    matches = list(re.finditer(pattern, text, re.IGNORECASE))
    return _normalize_date_token(matches[-1].group(1)) if matches else None


def _removal_schedule(text: str) -> tuple[str | None, str | None]:
    match = re.search(
        r"\b(?:removal|deportation|renvoi)(?:\s+order)?[^.;]{0,180}?"
        r"\b(?:scheduled|set)\s+for\s+(" + _DATE_TOKEN + r")",
        text,
        re.IGNORECASE,
    )
    if not match:
        match = re.search(
            r"\b(?:removal|deportation|renvoi)(?:\s+order)?[^.;]{0,180}?"
            r"\bon\s+(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),?\s+"
            r"([A-Za-zÀ-ÖØ-öø-ÿ]{3,9}\s+\d{1,2},\s*\d{2,4})",
            text,
            re.IGNORECASE,
        )
    if not match:
        return None, None
    scheduled_date = _normalize_date_token(match.group(1))
    destination_match = re.search(
        r"\bto\s+(.+?)(?=\s+(?:filed|received|with|on)\b|[.;]|$)",
        text[match.end():],
        re.IGNORECASE,
    )
    destination = re.sub(r"\s+", " ", destination_match.group(1)).strip(" .,;") if destination_match else None
    return scheduled_date, destination


def _normalize_motion_subtype(text: str) -> str:
    lowered = text.casefold()
    subtype_rules = (
        ("stay_removal", (r"stay of execution of (?:the )?removal", r"stay(?: of| the execution of)? removal", r"(?:staying|stay(?:ing)?) (?:their|the|a) removal", r"removal order.*\bstay\b", r"sursis (?:à|a) l['’]exécution du renvoi", r"demande de sursis(?: au| du)? renvoi")),
        ("stay_deportation", (r"stay of deportation", r"(?:staying|stay(?:ing)?) (?:their|the|a) deportation", r"sursis .*déportation", r"sursis .*deportation")),
        ("stay_release", (r"stay of release",)),
        ("stay_admissibility_hearing", (r"stay of admissibility hearing",)),
        ("stay_proceedings", (r"stay of proceedings",)),
        ("stay_execution", (r"stay of execution",)),
        ("abeyance", (r"abeyance",)),
        ("s_37_cea", (r"s\.?\s*37", r"canada evidence act")),
        ("s_87_irpa", (r"s\.?\s*87\s+irpa",)),
        ("anonymity", (r"anonym",)),
        ("amendment_aljr", (r"amend",)),
        ("extension_of_time", (r"extension of time", r"extend(?:ing)? time", r"prorogation de délai", r"prorogation de delai")),
        ("consent_judgment", (r"judgment on consent", r"request for judgment on consent", r"notice of settlement", r"jugement .*par consentement", r"requête .*consentement", r"requete .*consentement", r"par consentement")),
        ("confidentiality", (r"confidential",)),
        ("production", (r"production",)),
        ("intervention", (r"intervene", r"intervention")),
        ("stay", (r"\bstay\b",)),
    )
    for subtype, patterns in subtype_rules:
        if any(re.search(pattern, lowered) for pattern in patterns):
            return subtype
    return "unknown"


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


def _motion_docno_reference(docno: str | None) -> str | None:
    match = re.fullmatch(r"\s*(\d+)(?:\.0+)?\s*", str(docno or ""))
    return match.group(1) if match else None


def _motion_reference(text: str, docno: str | None) -> tuple[str | None, str | None]:
    text_reference = _motion_document_reference(text)
    if text_reference:
        return text_reference, "text"
    if re.search(r"\bnotice of motion\b", text, re.IGNORECASE):
        docno_reference = _motion_docno_reference(docno)
        if docno_reference:
            return docno_reference, "docno"
    return None, None


def _propagate_motion_subtypes(extracted: list[dict[str, Any]]) -> None:
    """Propagate subtype from a filing to entries for the same motion reference."""
    groups: dict[tuple[int, str, str], list[dict[str, Any]]] = {}
    for item in extracted:
        if not item["event_type"].startswith("motion"):
            continue
        reference = item.get("motion_reference")
        if reference:
            key = (item["activity_case_id"], "motion_reference", str(reference))
        elif item.get("re_no"):
            key = (item["activity_case_id"], "re_no", str(item["re_no"]))
        else:
            continue
        groups.setdefault(key, []).append(item)

    for items in groups.values():
        explicit = [item for item in items if item.get("subtype") not in {None, "unknown", "stay"}]
        subtypes = {item["subtype"] for item in explicit}
        if len(subtypes) != 1:
            continue
        source = explicit[0]
        for item in items:
            if item.get("subtype") != "unknown":
                continue
            item["subtype"] = source["subtype"]
            item["subtype_source_doc_id"] = source["doc_id"]
            item["subtype_source_text"] = source["text"]
            item["rule"] = f"motion_context:{source['doc_id']}"


def _normalize_motion_result(text: str) -> str | None:
    lowered = text.casefold()
    if re.search(r"granted in part|partially granted|partially allowed|accordée? en partie|accorde(?:e|e)? en partie|partiellement accord", lowered):
        return "granted_in_part"
    if re.search(r"abandon(?:ed|ned)?|withdrawn|abandonn[éee]|retir[éee]", lowered):
        return "abandoned"
    if re.search(r"discontinu(?:ed|ance)|d[eé]sistement", lowered):
        return "discontinued"
    if re.search(r"grant(?:ed|ing)?|allow(?:ed|ing)?|accord(?:ant|ée|ee)", lowered):
        return "granted"
    if re.search(r"dismiss(?:ed|ing)?|refus(?:ed|ing)?|rejet(?:ant|ée|ee)", lowered):
        return "refused"
    return None


def extract_procedural_events(events: Iterable[ActivityEvent]) -> list[dict[str, Any]]:
    """Extract repeatable, evidence-backed procedural events without database writes."""
    extracted: list[dict[str, Any]] = []
    for event in events:
        text = event.text
        lowered = text.casefold()
        judge_name = _judge_name(text)
        base = {
            "activity_case_id": event.activity_case_id,
            "doc_id": event.doc_id,
            "re_no": event.re_no,
            "docno": event.docno,
            "source_document_date": _event_date(event),
            "event_date": None,
            "date_kind": "source_document_date",
            "filing_date": None,
            "judge_name": judge_name,
            "removal_scheduled_date": None,
            "removal_destination": None,
            "text": text,
            "confidence": "exact",
        }
        motion_reference, motion_reference_source = _motion_reference(text, event.docno)
        base["motion_reference"] = motion_reference
        base["motion_reference_source"] = motion_reference_source

        def add(event_type: str, *, subtype: str | None = None, outcome: str | None = None, rule: str) -> None:
            event_date, date_kind = _semantic_date(text, event_type)
            filing_date = _explicit_filing_date(text)
            extracted.append({**base, "event_date": event_date or base["source_document_date"], "date_kind": date_kind, "filing_date": filing_date, "event_type": event_type, "subtype": subtype, "outcome": outcome, "rule": rule})

        if re.search(r"application for leave .* judicial review|demande d['’]autorisation .* contrôle judiciaire|notice of application .* judicial review", text, re.IGNORECASE):
            add("application_filed", subtype="leave_and_judicial_review", rule="originating_application")
        if re.search(r"application record .* filed|applicant['’]?s record .* filed|dossier de la partie demanderesse .* dépos", text, re.IGNORECASE):
            add("application_perfected", rule="application_record_filed")
        if re.search(r"notice of appearance\b.*\b(?:filed|served|received)\b|avis de comparution\b.*\b(?:déposé|depose|signifié|signifie|reçu|recu)\b", text, re.IGNORECASE):
            add("appearance_filed", subtype="notice_of_appearance", rule="notice_of_appearance")

        if re.search(r"application for leave|demande d['’]autorisation", text, re.IGNORECASE):
            if re.search(r"granting|granted|accordant|accordée|accordee", lowered, re.IGNORECASE):
                add("leave_decision", outcome="granted", rule="leave_granted")
            elif re.search(r"dismissing|dismissed|rejetant|rejetée|rejetee", lowered, re.IGNORECASE):
                add("leave_decision", outcome="refused", rule="leave_refused")

        if re.search(r"\bmotion\b|\bnotice of motion\b|\brequête\b|\brequete\b|demande de sursis|\bstaying\b", text, re.IGNORECASE):
            motion_outcome = _normalize_motion_result(text)
            event_type = "motion_decision" if motion_outcome else "motion_filed"
            add(
                event_type,
                subtype=_normalize_motion_subtype(text),
                outcome=motion_outcome,
                rule="motion_with_explicit_outcome" if motion_outcome else "motion_reference",
            )

        hearing_negation = re.search(
            r"hearing (?:was|is|has been)?\s*(?:not held|cancelled|did not proceed)|"
            r"without (?:a )?hearing|(?:no|without) personal appearance|sans audience|"
            r"l'audience n['’]a pas eu lieu|audience .* non tenue|sans comparution en personne",
            text,
            re.IGNORECASE,
        )
        hearing_subtype = (
            "not_held"
            if hearing_negation
            else "scheduled"
            if re.search(r"hearing (?:is )?(?:scheduled|set) for|audience (?:est )?(?:fixée|fixee|prévue|prevue) pour", text, re.IGNORECASE)
            else "reserved"
            if re.search(r"matter reserved|decision reserved|affaire mise en délibéré|audience mise en délibéré", text, re.IGNORECASE)
            else "held"
            if re.search(r"result of hearing|hearing held|held in court|comparution en personne|audience .* tenue|audience .* a eu lieu", text, re.IGNORECASE)
            else None
        )
        if hearing_subtype and hearing_subtype != "not_held":
            add("hearing", subtype=hearing_subtype, rule=f"hearing_{hearing_subtype}")

        if re.search(r"\(final decision\)|final decision|reasons for judgment|judgment rendered|décision finale|decision finale|jugement rendu", text, re.IGNORECASE):
            add("decision", subtype="final_or_reasons", rule="final_decision_marker")

        stay_signal = re.search(
            r"\bstay\b|sursis|removal (?:has been|was|is) cancelled|removal cancelled",
            text,
            re.IGNORECASE,
        )
        if stay_signal:
            removal_scheduled_date, removal_destination = _removal_schedule(text)
            base["removal_scheduled_date"] = removal_scheduled_date
            base["removal_destination"] = removal_destination
            stay_outcome = None
            if re.search(r"granting|granted|accordant|accordée|accordee", lowered, re.IGNORECASE):
                stay_outcome = "granted"
            elif re.search(r"dismissing|dismissed|refusing|refused|rejetant|rejetée|rejetee", lowered, re.IGNORECASE):
                stay_outcome = "refused"
            elif re.search(r"removal (?:has been|was|is) cancelled|removal cancelled", lowered, re.IGNORECASE):
                stay_outcome = "granted"
            add("stay", outcome=stay_outcome, rule="stay_cancellation" if stay_outcome == "granted" and not re.search(r"\bstay\b|sursis", text, re.IGNORECASE) else "stay_reference")

        if judge_name:
            add("judge_identified", subtype="presiding_or_assigned", rule=f"judge_name:{judge_name}")

    _propagate_motion_subtypes(extracted)
    return extracted


def _match_events(events: Iterable[ActivityEvent], rule_key: str) -> list[tuple[ActivityEvent, re.Match[str]]]:
    _, patterns = COMPILED_RULES[rule_key]
    matches: list[tuple[ActivityEvent, re.Match[str]]] = []
    for event in events:
        if rule_key == "hearing_held" and re.search(r"without personal appearance|sans comparution en personne|no personal appearance", event.text, re.IGNORECASE):
            continue
        for pattern in patterns:
            match = pattern.search(event.text)
            if match:
                matches.append((event, match))
                break
    return matches


def _hearing_status(events: list[ActivityEvent]) -> dict[str, Any]:
    patterns = (
        ("not_held", r"hearing (?:was|is|has been)?\s*(?:not held|cancelled|did not proceed)|without (?:a )?hearing|(?:no|without) personal appearance|sans audience|l'audience n['’]a pas eu lieu|audience .* non tenue|sans comparution en personne"),
        ("scheduled", r"hearing (?:is )?(?:scheduled|set) for|audience (?:est )?(?:fixée|fixee|prévue|prevue) pour"),
        ("reserved", r"matter reserved|decision reserved|affaire mise en délibéré|audience mise en délibéré"),
        ("held", r"result of hearing|hearing held|held in court|comparution en personne|audience .* tenue|audience .* a eu lieu"),
    )
    matches: list[tuple[ActivityEvent, str, re.Match[str]]] = []
    for event in events:
        for status, pattern in patterns:
            match = re.search(pattern, event.text, re.IGNORECASE)
            if match:
                matches.append((event, status, match))
                break
    if not matches:
        return {"status": "unknown", "date": None, "doc_id": None, "re_no": None, "docno": None, "text": None, "rule": "no_hearing_signal"}
    event, status, match = matches[0]
    return {"status": status, "date": _event_date(event), "doc_id": event.doc_id, "re_no": event.re_no, "docno": event.docno, "text": event.text, "rule": f"hearing_status:{status}:{match.group(0)}"}


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


def _lifecycle_status(
    events: list[ActivityEvent],
    closing_status: dict[str, Any],
    full_history_resolution: dict[str, Any],
    history_profile: dict[str, Any],
) -> dict[str, Any]:
    terminal_statuses = {
        "discontinued",
        "withdrawn",
        "administratively_terminated",
        "leave_refused",
        "judicial_review_granted",
        "judicial_review_dismissed",
    }
    for signal in (closing_status, full_history_resolution):
        status = signal.get("status")
        if status in terminal_statuses:
            return {
                "status": "closed",
                "status_kind": status,
                "date": signal.get("date"),
                "doc_id": signal.get("doc_id"),
                "re_no": signal.get("re_no"),
                "docno": signal.get("docno"),
                "text": signal.get("text"),
                "rule": signal.get("rule"),
                "confidence": "exact",
            }
        if status == "abeyance":
            return {
                "status": "abeyance",
                "status_kind": status,
                "date": signal.get("date"),
                "doc_id": signal.get("doc_id"),
                "re_no": signal.get("re_no"),
                "docno": signal.get("docno"),
                "text": signal.get("text"),
                "rule": signal.get("rule"),
                "confidence": "exact",
            }
    if not events:
        return {"status": "unknown", "status_kind": None, "date": None, "doc_id": None, "re_no": None, "docno": None, "text": None, "rule": "no_activity_events", "confidence": "unknown"}
    if history_profile.get("last_substantive_entry_date"):
        return {
            "status": "active",
            "status_kind": "no_terminal_signal",
            "date": history_profile["last_substantive_entry_date"],
            "doc_id": None,
            "re_no": None,
            "docno": None,
            "text": None,
            "rule": "substantive_activity_without_terminal_signal",
            "confidence": "inferred",
        }
    return {"status": "unknown", "status_kind": None, "date": None, "doc_id": None, "re_no": None, "docno": None, "text": None, "rule": "no_substantive_activity", "confidence": "unknown"}


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
        return {"status": "unknown", "application_type": None, "decision_maker": None, "decision_maker_type": "unknown", "underlying_tribunal": None, "underlying_tribunal_type": "unknown", "decision_subject": "unknown", "decision_date": None, "tribunal_file_numbers": [], "doc_id": None, "re_no": None, "docno": None, "text": None, "rule": "no_originating_application_entry"}
    text = event.text
    lowered = text.casefold()
    category_rules = (
        ("irb_refugee_or_appeal", r"\b(?:irb|rpd|rad|crdd|cisr|iad|id)\b|immigration and refugee board|immigration division|refugee division|refugee protection division|immigration appeal division|section de la protection des réfugiés|section d['’]appel(?: des réfugiés| d'immigration)"),
        ("cbsa_enforcement", r"\b(?:cbsa|asfc)\b|canada border services|agence des services frontaliers|border services agency|services frontaliers"),
        ("cic_ircc_processing", r"\b(?:cic|ircc)\b|citizenship and immigration|immigration,? refugees?,? and citizenship canada|immigration canada|case processing centre"),
        ("visa_office_or_consulate", r"consulate|consulat|embassy|ambassade|high commission|visa office|agent(?:e)? de visa(?:s)?|bureau de visa"),
        ("minister_or_department", r"\b(?:mci|mpsep)\b|minister|ministre|department of citizenship"),
        ("mandamus", r"\bmandamus\b"),
        ("extension_of_time", r"extension of time|prorogation de délai"),
        ("removal_or_exclusion", r"removal|deportation|exclusion|renvoi|mesure d['’]exclusion|sursis.*renvoi"),
        ("detention", r"detention|detained|détention|detenu|détenu"),
        ("inadmissibility", r"inadmissib|criminality|security|misrepresentation|interdiction de territoire"),
        ("citizenship", r"citizenship(?!\s+(?:and immigration|canada))|citoyenneté"),
        ("humanitarian_and_compassionate", r"humanitarian migration|migration humanitaire|humanitarian and compassionate|\bH&C\b"),
        ("permanent_residence", r"permanent resid(?:ent|ence|ency)|résidence permanente|express entry|family class|spousal sponsorship|sponsored application|application for landing|backlog reduction office"),
        ("temporary_residence", r"study permit|work permit|visitor(?:['’]s)? visa|electronic travel authorization|\beTA\b|LMIA|foreign service worker program|temporary resident|permis d['’]études|permis de travail|résident temporaire"),
        ("provincial_nominee", r"provincial nominee|provincial nominee program|programme des candidats des provinces"),
        ("refugee_protection", r"refugee protection|refugee claim|refugee appeal|refugee appeal division|refugee division|convention refugee determination division|\b(?:rpd|rad|crdd|spr|sar|prra|er ar|erar)\b|risk of return|risque de retour|section (?:du )?statut des réfugiés|section de la protection (?:du statut des |des )réfugiés|section d['’]appel des réfugiés"),
    )
    challenge_categories = [category for category, pattern in category_rules if re.search(pattern, text, re.IGNORECASE)]
    decision_maker_type = next(
        (
            category
            for category in (
                "irb_refugee_or_appeal",
                "cbsa_enforcement",
                "cic_ircc_processing",
                "visa_office_or_consulate",
                "minister_or_department",
            )
            if category in challenge_categories
        ),
        "unknown",
    )
    maker_categories = {"irb_refugee_or_appeal", "cbsa_enforcement", "cic_ircc_processing", "visa_office_or_consulate", "minister_or_department"}
    maker_events = [
        candidate
        for candidate in events
        if any(category in maker_categories and re.search(pattern, candidate.text, re.IGNORECASE) for category, pattern in category_rules)
    ]
    maker_event = max(
        maker_events,
        key=lambda candidate: sum(
            bool(re.search(pattern, candidate.text, re.IGNORECASE))
            for category, pattern in category_rules
            if category in maker_categories
        ),
        default=event,
    )
    maker_matches = [
        category
        for category, pattern in category_rules
        if category in maker_categories and re.search(pattern, maker_event.text, re.IGNORECASE)
    ]
    decision_maker_type = next(
        (category for category in ("irb_refugee_or_appeal", "cbsa_enforcement", "cic_ircc_processing", "visa_office_or_consulate", "minister_or_department") if category in maker_matches),
        decision_maker_type,
    )
    subject_categories = {
        "removal_or_exclusion": "removal_or_exclusion",
        "detention": "detention",
        "inadmissibility": "inadmissibility",
        "citizenship": "citizenship",
        "humanitarian_and_compassionate": "humanitarian_and_compassionate",
        "permanent_residence": "permanent_residence",
        "temporary_residence": "temporary_residence",
        "provincial_nominee": "provincial_nominee",
        "refugee_protection": "refugee_protection",
    }
    subject_events = [
        candidate
        for candidate in events
        if any(
            category in subject_categories and re.search(pattern, candidate.text, re.IGNORECASE)
            for category, pattern in category_rules
        )
    ]
    subject_event = max(
        subject_events,
        key=lambda candidate: sum(
            bool(re.search(pattern, candidate.text, re.IGNORECASE))
            for category, pattern in category_rules
            if category in subject_categories
        ),
        default=event,
    )
    subject_matches = [
        category
        for category, pattern in category_rules
        if category in subject_categories and re.search(pattern, subject_event.text, re.IGNORECASE)
    ]
    decision_subject = next((subject_categories[category] for category in subject_categories if category in subject_matches), "unknown")
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
    if decision_maker is None:
        marker = re.search(
            r"against (?:a )?decision\s+(?:made by\s+)?(.+?)(?=\s+(?:dated|rendered|filed|and the notice)\b|,\s*(?:\d|dated|decision|file|files?|uci)\b|\s+file\s+no\b|$)",
            text,
            re.IGNORECASE,
        )
        if marker:
            decision_maker = _clean_origin_value(marker.group(1))
    if decision_maker:
        decision_maker = re.sub(
            r",\s*(?:\d{1,2}[-/]?[A-Za-z]{3,9}[-/]?\d{2,4}|dated\b|decision\b|file(?:s)?\b).*$",
            "",
            decision_maker,
            flags=re.IGNORECASE,
        ).strip(" ,;:")
    tribunal_types = {
        "irb_refugee_or_appeal": "irb",
        "cbsa_enforcement": "cbsa",
        "cic_ircc_processing": "ircc",
        "visa_office_or_consulate": "visa_office_or_consulate",
        "minister_or_department": "ministerial_or_departmental",
    }
    underlying_tribunal_type = tribunal_types.get(decision_maker_type, "unknown")
    generic_subject_marker = re.compile(
        r"\b(?:IRCC|CIC|CPC|CBSA|ASFC|CISR|C\.?\s*I\.?\s*S\.?\s*R\.?|IRB|IAD|MPSEP|GTEC|CE-[A-Z]+|visa office|visa section|visa officer|agent(?:e)? de visa(?:s)?|bureau de visa|embassy|consulate|high commission|"
        r"immigration and refugee board|immigration division|immigration appeal division|section d['’]appel d'immigration|"
        r"citizenship and immigration|immigration,? refugees?,? and citizenship canada|immigration canada|case processing centre|immigration program manager|immigration section|agence des services frontaliers|commission de l'immigration|program support officer|foreign worker|migration humanitaire)\b",
        re.IGNORECASE,
    )
    subject_availability = (
        "explicit_subject"
        if decision_subject != "unknown"
        else "generic_institution_only"
        if any(generic_subject_marker.search(candidate.text) for candidate in events)
        else "no_subject_evidence"
    )
    return {"status": "yes", "application_type": application_type, "challenge_categories": challenge_categories, "decision_maker": decision_maker, "decision_maker_type": decision_maker_type, "decision_maker_evidence_doc_id": maker_event.doc_id, "decision_maker_evidence_text": maker_event.text, "underlying_tribunal": decision_maker, "underlying_tribunal_type": underlying_tribunal_type, "decision_subject": decision_subject, "decision_subject_availability": subject_availability, "decision_subject_label": decision_maker if subject_availability == "generic_institution_only" else None, "decision_subject_doc_id": subject_event.doc_id, "decision_subject_text": subject_event.text, "decision_date": decision_date_match.group(1) if decision_date_match else None, "tribunal_file_numbers": tribunal_file_numbers, "doc_id": event.doc_id, "re_no": event.re_no, "docno": event.docno, "text": event.text, "rule": "originating_application_entry"}


def _clean_origin_value(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip(" ,;:.")).strip()


def _judge_stage(event: dict[str, Any]) -> str:
    text = str(event.get("text") or "").casefold()
    event_type = event.get("event_type")
    if event_type == "decision" or re.search(r"final decision|reasons for judgment|judgment rendered|décision finale|jugement rendu", text):
        return "final_decision"
    if event_type in {"leave_decision"} or "application for leave" in text or "demande d'autorisation" in text:
        return "leave"
    if event_type in {"motion_filed", "motion_decision"} or re.search(r"\bmotion\b|\bnotice of motion\b|\brequ[eê]te\b", text):
        return "motion"
    if event_type == "hearing":
        return "hearing"
    return "other"


def _judge_observations(events: list[dict[str, Any]]) -> dict[str, Any]:
    observations: list[dict[str, Any]] = []
    by_stage: dict[str, list[dict[str, Any]]] = {}
    for event in events:
        judge_name = event.get("judge_name")
        if not judge_name:
            continue
        stage = _judge_stage(event)
        observation = {
            "name": judge_name,
            "stage": stage,
            "doc_id": event.get("doc_id"),
            "re_no": event.get("re_no"),
            "docno": event.get("docno"),
            "date": event.get("event_date") or event.get("source_document_date"),
            "text": event.get("text"),
            "rule": event.get("rule"),
            "confidence": "exact",
        }
        observations.append(observation)
        by_stage.setdefault(stage, []).append(observation)
    return {
        "observations": observations,
        "by_stage": by_stage,
        "status": "yes" if observations else "unknown",
        "rule": "judge_name_stage_observations" if observations else "no_judge_name_observation",
    }


def _milestone_rollups(
    *,
    application_filed: Evidence,
    perfection_status: dict[str, Any],
    leave: Evidence,
    leave_result: str,
    motion_final_decision: Evidence,
    hearing_status: dict[str, Any],
    final_decision: Evidence,
    closing_status: dict[str, Any],
    lifecycle_status: dict[str, Any],
) -> dict[str, Any]:
    return {
        "application": {
            "filed": asdict(application_filed),
            "perfection": perfection_status,
        },
        "leave": {
            "decision": asdict(leave),
            "result": leave_result,
        },
        "motion": {
            "latest_decision": asdict(motion_final_decision),
        },
        "hearing": hearing_status,
        "final_decision": asdict(final_decision),
        "closure": {
            "closing_signal": closing_status,
            "lifecycle": lifecycle_status,
        },
    }


def _field_applicability(
    *,
    application_filed: Evidence,
    application_perfected: Evidence,
    leave_result: str,
    effective_leave_result: str,
    leave_context: dict[str, Any],
    review_result: str,
    judicial_review_final: Evidence,
    final_decision: Evidence,
    closing_status: dict[str, Any],
    full_history_resolution: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    terminal_kinds = {"discontinued", "withdrawn", "administratively_terminated"}
    terminal = closing_status if closing_status.get("status_kind") in terminal_kinds else full_history_resolution
    terminal_kind = terminal.get("status") if terminal.get("status") in terminal_kinds else None
    leave_date = leave_context.get("evidence", {}).get("date") or (leave_context.get("evidence") or {}).get("event_date")
    terminal_date = terminal.get("date")
    terminated_before_leave = bool(terminal_kind and (not leave_date or not terminal_date or terminal_date <= leave_date))
    terminated_after_leave = bool(terminal_kind and effective_leave_result == "granted" and leave_date and terminal_date and terminal_date > leave_date)

    if leave_context.get("status") == "not_applicable_direct_judicial_review":
        leave_status = {
            "status": "not_applicable",
            "reason": "direct_judicial_review",
            "explanation": "This application proceeded as direct judicial review and did not require leave.",
        }
    elif effective_leave_result in {"granted", "refused"}:
        leave_status = {"status": "known", "reason": leave_context.get("status") if leave_context.get("status", "").startswith("inferred_") else effective_leave_result}
    elif terminated_before_leave and application_perfected.status != "yes":
        leave_status = {
            "status": "not_applicable",
            "reason": f"not_perfected_before_{terminal_kind}",
            "explanation": f"The case reached {terminal_kind} before an applicant record was perfected, so leave could not proceed.",
        }
    elif terminated_before_leave:
        leave_status = {
            "status": "not_applicable",
            "reason": f"{terminal_kind}_before_leave",
            "explanation": f"The case reached {terminal_kind} before a leave decision was recorded.",
        }
    elif application_filed.status == "yes":
        leave_status = {"status": "pending", "reason": "leave_decision_not_observed"}
    else:
        leave_status = {"status": "not_observed", "reason": "no_originating_application"}

    if effective_leave_result == "refused":
        review_status = {"status": "not_applicable", "reason": "leave_refused"}
        review_final_status = {"status": "not_applicable", "reason": "leave_refused"}
    elif terminated_after_leave:
        review_status = {"status": "not_applicable", "reason": f"{terminal_kind}_after_leave_granted"}
        review_final_status = {"status": "not_applicable", "reason": f"{terminal_kind}_after_leave_granted"}
    elif effective_leave_result == "granted" or leave_context.get("status") == "not_applicable_direct_judicial_review":
        review_status = {"status": "known", "reason": review_result} if review_result in {"granted", "dismissed"} else {"status": "pending", "reason": "judicial_review_result_not_observed"}
        review_final_status = {"status": "known", "reason": "substantive_final_decision"} if judicial_review_final.status == "yes" else {"status": "pending", "reason": "judicial_review_final_decision_not_observed"}
    elif leave_status["status"] == "not_applicable":
        review_status = {"status": "not_applicable", "reason": leave_status["reason"]}
        review_final_status = {"status": "not_applicable", "reason": leave_status["reason"]}
    else:
        review_status = {"status": "not_observed", "reason": "leave_not_resolved"}
        review_final_status = {"status": "not_observed", "reason": "leave_not_resolved"}

    return {
        "leave_decision": {**leave_status, "evidence_status": leave_result},
        "judicial_review_result": {**review_status, "evidence_result": review_result},
        "judicial_review_final_decision": {**review_final_status, "evidence_status": judicial_review_final.status},
        "final_decision": {"status": "known" if final_decision.status == "yes" else "not_observed", "reason": "generic_final_decision_marker" if final_decision.status == "yes" else "generic_final_decision_not_observed"},
    }


def classify_events(events: Iterable[ActivityEvent]) -> dict[str, Any]:
    ordered = list(events)
    procedural_events = extract_procedural_events(ordered)
    challenged_decision = _challenged_decision(ordered)
    application_filed = _evidence(ordered, "application_filed")
    application_perfected = _evidence(ordered, "application_perfected")
    leave_granted = _evidence(ordered, "leave_granted")
    leave_refused = _evidence(ordered, "leave_refused")
    final_decision = _evidence(ordered, "final_decision", latest=True)
    review_granted = _evidence(ordered, "judicial_review_granted", latest=True)
    review_dismissed = _evidence(ordered, "judicial_review_dismissed", latest=True)
    hearing_held = _evidence(ordered, "hearing_held")
    hearing_status = _hearing_status(ordered)

    leave = leave_granted if leave_granted.status == "yes" else leave_refused
    leave_result = "granted" if leave_granted.status == "yes" else "refused" if leave_refused.status == "yes" else "unknown"
    preliminary_resolution = _full_history_resolution(ordered, leave_result)
    later_review_granted = _evidence(ordered, "judicial_review_granted", latest=True)
    later_review_dismissed = _evidence(ordered, "judicial_review_dismissed", latest=True)
    if leave_result == "unknown" and (later_review_granted.status == "yes" or later_review_dismissed.status == "yes"):
        leave_context = {"status": "inferred_granted", "evidence": asdict(later_review_granted if later_review_granted.status == "yes" else later_review_dismissed), "rule": "later_judicial_review_requires_leave"}
        effective_leave_result = "granted"
    elif leave_result == "unknown" and any(
        event.get("subtype") == "production"
        and (event.get("outcome") == "granted" or re.search(r"production order\s+(?:issued|made|granted)", event.get("text", ""), re.IGNORECASE))
        for event in procedural_events
    ):
        production_event = next(event for event in procedural_events if event.get("subtype") == "production")
        leave_context = {"status": "inferred_granted_production_order", "evidence": production_event, "rule": "production_order_supports_leave_grant"}
        effective_leave_result = "granted"
    elif leave_result == "unknown" and challenged_decision.get("application_type") == "direct_judicial_review":
        leave_context = {"status": "not_applicable_direct_judicial_review", "evidence": challenged_decision, "rule": "direct_judicial_review_does_not_require_leave"}
        effective_leave_result = "unknown"
    elif leave_result == "unknown" and preliminary_resolution["status"] == "discontinued":
        leave_context = {"status": "not_relevant_discontinued", "evidence": preliminary_resolution, "rule": "discontinuance_before_confirmed_leave"}
        effective_leave_result = "unknown"
    elif leave_result == "unknown" and preliminary_resolution["status"] == "withdrawn":
        leave_context = {"status": "not_relevant_withdrawn", "evidence": preliminary_resolution, "rule": "withdrawal_before_confirmed_leave"}
        effective_leave_result = "unknown"
    elif leave_result == "unknown" and preliminary_resolution["status"] == "administratively_terminated":
        leave_context = {"status": "not_relevant_terminated", "evidence": preliminary_resolution, "rule": "administrative_termination_before_confirmed_leave"}
        effective_leave_result = "unknown"
    elif leave_result == "unknown" and challenged_decision.get("status") == "yes" and application_filed.status == "yes":
        leave_context = {"status": "pending", "evidence": asdict(application_filed), "rule": "leave_decision_not_yet_observed"}
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
    lifecycle_status = _lifecycle_status(ordered, closing_status, full_history_resolution, history_profile)
    judges = _judge_observations(procedural_events)
    field_applicability = _field_applicability(
        application_filed=application_filed,
        application_perfected=application_perfected,
        leave_result=leave_result,
        effective_leave_result=effective_leave_result,
        leave_context=leave_context,
        review_result=review_result,
        judicial_review_final=judicial_review_final,
        final_decision=final_decision,
        closing_status=closing_status,
        full_history_resolution=full_history_resolution,
    )
    milestone_rollups = _milestone_rollups(
        application_filed=application_filed,
        perfection_status=perfection_status,
        leave=leave,
        leave_result=leave_result,
        motion_final_decision=motion_final_decision,
        hearing_status=hearing_status,
        final_decision=final_decision,
        closing_status=closing_status,
        lifecycle_status=lifecycle_status,
    )

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
        "field_applicability": field_applicability,
        "closing_status": closing_status,
        "full_history_resolution": full_history_resolution,
        "lifecycle_status": lifecycle_status,
        "challenged_decision": challenged_decision,
        "history_profile": history_profile,
        "hearing_held": asdict(hearing_held),
        "hearing_status": hearing_status,
        "judges": judges,
        "milestone_rollups": milestone_rollups,
        "procedural_events": procedural_events,
    }


def validate_fc_activity_classification(classification: dict[str, Any]) -> dict[str, Any]:
    """Return deterministic cross-field findings without changing the input."""
    issues: list[dict[str, Any]] = []
    leave = classification.get("leave_decision") or {}
    leave_context = classification.get("leave_context") or {}
    review = classification.get("judicial_review_result") or {}
    review_final = classification.get("judicial_review_final_decision") or {}
    history = classification.get("history_profile") or {}
    events = classification.get("procedural_events") or []

    def add_issue(rule: str, fields: list[str], description: str, evidence_doc_ids: list[Any] | None = None) -> None:
        issues.append(
            {
                "severity": "error",
                "rule": rule,
                "fields_affected": fields,
                "evidence_doc_ids": sorted({doc_id for doc_id in (evidence_doc_ids or []) if doc_id is not None}),
                "description": description,
            }
        )

    leave_result = leave.get("result")
    review_result = review.get("result")
    leave_date = leave.get("date")
    review_date = review_final.get("date")
    latest_date = history.get("last_any_entry_date")
    substantive_review = review_result in {"granted", "dismissed"}
    event_doc_ids = [event.get("doc_id") for event in events if isinstance(event, dict)]

    if leave_context.get("status") == "pending" and substantive_review:
        add_issue(
            "leave_still_pending_with_jr_result",
            ["leave_context.status", "judicial_review_result.result"],
            "Leave remains pending even though a substantive judicial review result exists.",
            event_doc_ids,
        )
    if substantive_review and not review_date:
        add_issue(
            "jr_result_without_jr_date",
            ["judicial_review_result.result", "judicial_review_final_decision.date"],
            "A substantive judicial review result has no decision date.",
            event_doc_ids,
        )
    if leave_date and review_date and leave_date > review_date:
        add_issue(
            "leave_date_after_jr_date",
            ["leave_decision.date", "judicial_review_final_decision.date"],
            "The leave decision date is later than the judicial review decision date.",
            event_doc_ids,
        )
    if leave_date and latest_date and leave_date > latest_date:
        add_issue(
            "leave_date_after_latest_activity",
            ["leave_decision.date", "history_profile.last_any_entry_date"],
            "The leave decision date is later than the latest recorded activity date.",
            event_doc_ids,
        )
    if events and not latest_date:
        add_issue(
            "missing_latest_activity_date",
            ["history_profile.last_any_entry_date"],
            "Activity events exist but the latest activity date is missing.",
            event_doc_ids,
        )
    if leave_result in {None, "unknown"} and substantive_review and leave_context.get("status") not in {"inferred_granted", "not_applicable_direct_judicial_review"}:
        add_issue(
            "leave_na_with_substantive_jr_result",
            ["leave_decision.result", "judicial_review_result.result"],
            "Leave is unresolved while a substantive judicial review result is present.",
            event_doc_ids,
        )

    return {
        "is_valid": not issues,
        "issues": issues,
        "summary": "No cross-field issues found." if not issues else f"{len(issues)} cross-field issue(s) found.",
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
