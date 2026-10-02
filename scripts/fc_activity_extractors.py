"""Additional evidence-backed fields extracted from Federal Court docket entries.

Each extractor reads the docket entries of one IMM file (``ActivityEvent`` objects from
``scripts.classify_fc_activity``) and returns a JSON-ready dict. Every value carries the
entry it came from so a reviewer can check it, and a field is left ``unknown`` rather
than guessed when the registry text does not say.
"""

from __future__ import annotations

import re
from collections import Counter
from datetime import date
from typing import Any, Iterable


def _helpers():
    # Imported lazily: the classifier imports this module at load time.
    from scripts import classify_fc_activity as classifier

    return classifier


def _event_date(event: Any) -> str | None:
    return event.doc_date.isoformat() if event.doc_date else None


def _parse_date(token: str | None) -> str | None:
    if not token:
        return None
    return _helpers()._normalize_date_token(token)


def _days_between(start: str | None, end: str | None) -> int | None:
    if not start or not end:
        return None
    try:
        days = (date.fromisoformat(end) - date.fromisoformat(start)).days
    except ValueError:
        return None
    return days if days >= 0 else None


def _evidence(event: Any) -> dict[str, Any]:
    return {"doc_id": event.doc_id, "date": _event_date(event), "text": event.text}


# ---------------------------------------------------------------------------
# Hearings: "Toronto 17-JUN-2015 BEFORE The Honourable ... Language: E Before the Court:
# Judicial Review Result of Hearing: Matter reserved held in Court ... Total Duration: 2h40min
# Appearances: Mr. X 416-... representing Applicant Ms. Y representing Respondent Comments: ..."
# ---------------------------------------------------------------------------

_HEARING_ENTRY = re.compile(r"result of hearing\s*:", re.IGNORECASE)
_HEARING_HEAD = re.compile(r"^\s*([A-Za-zÀ-ÿ .'-]{3,40}?)\s+(\d{1,2}-[A-Za-zÀ-ÿ]{3,5}-\d{4})\s+(?:BEFORE|DEVANT)\b", re.IGNORECASE)
_HEARING_LANGUAGE = re.compile(r"\b(?:language|langue)\s*:\s*([EFB])\b", re.IGNORECASE)
_HEARING_SUBJECT = re.compile(r"before the court\s*:\s*(.+?)\s*result of hearing", re.IGNORECASE)
_HEARING_RESULT = re.compile(r"result of hearing\s*:\s*(.+?)(?:\s+held\b|\s+senior usher\b|\s+duration per day\b|$)", re.IGNORECASE)
_HEARING_TOTAL = re.compile(r"total duration\s*:\s*(?:(\d+(?:\.\d+)?)\s*d(?:ays?)?)?\s*(?:(\d+(?:\.\d+)?)\s*h(?:rs?|ours?)?\.?,?\s*)?(?:(\d+)\s*m(?:in(?:ute)?s?)?\.?)?", re.IGNORECASE)
_HEARING_SPAN = re.compile(r"from\s+(\d{1,2}):(\d{2})\s+to\s+(\d{1,2}):(\d{2})", re.IGNORECASE)
_APPEARANCE = re.compile(
    r"((?:(?:mr|mrs|ms|me|dr)\.?\s*)?[A-ZÀ-Ý][\w'’.\-]*(?:\s+[A-ZÀ-Ý][\w'’.\-]*){0,4})\s*(?:\(?\d{3}\)?[\s.-]*\d{3}[\s.-]*\d{4}\s*)?"
    r"(?i:\(self[- ]represented\)|representing\s+(?:the\s+)?(applicants?|respondents?|appellants?|interveners?|minister|tribunal))",
)


def _hearing_kind(subject: str) -> str:
    lowered = subject.casefold()
    if re.search(r"judicial review|contrôle judiciaire|trial of the matter", lowered):
        return "judicial_review"
    if re.search(r"\bstay\b|sursis", lowered):
        return "stay_motion"
    if re.search(r"motion|requête", lowered):
        return "motion"
    if re.search(r"case management|conference|gestion|^meeting", lowered):
        return "case_management"
    if re.search(r"status review|examen de l'état", lowered):
        return "status_review"
    return "other"


def _hearing_result(raw: str) -> str:
    lowered = raw.casefold()
    if "reserved" in lowered or "délibéré" in lowered:
        return "reserved"
    if "adjourn" in lowered or "ajourn" in lowered:
        return "adjourned"
    if "partially granted" in lowered or "granted in part" in lowered:
        return "granted_in_part"
    if "granted" in lowered or "allowed" in lowered or "accord" in lowered:
        return "granted"
    if "dismissed" in lowered or "rejet" in lowered:
        return "dismissed"
    if "withdrawn" in lowered or "abandon" in lowered:
        return "withdrawn"
    return "other"


def _hearing_mode(text: str) -> str:
    lowered = text.casefold()
    if re.search(r"video|zoom|teams|vidéo", lowered):
        return "video"
    if re.search(r"conference call|teleconference|telephone|téléconférence", lowered):
        return "telephone"
    if "in chambers" in lowered or "en cabinet" in lowered:
        return "chambers"
    if re.search(r"held in court|in camera|en salle", lowered):
        return "in_court"
    return "unknown"


def _hearing_minutes(text: str) -> int | None:
    total = _HEARING_TOTAL.search(text)
    if total and any(total.groups()):
        days, hours, minutes = total.groups()
        value = float(days or 0) * 24 * 60 + float(hours or 0) * 60 + float(minutes or 0)
        if 0 < value < 60 * 24 * 10:
            return int(round(value))
    spans = _HEARING_SPAN.findall(text)
    if spans:
        minutes = 0
        for start_h, start_m, end_h, end_m in spans:
            start = int(start_h) * 60 + int(start_m)
            end = int(end_h) * 60 + int(end_m)
            if end < start:  # registry writes afternoon times on a 12-hour clock
                end += 12 * 60
            minutes += end - start
        return minutes if 0 < minutes < 60 * 24 else None
    return None


def _tidy_case(value: str) -> str:
    """Title-case names the registry typed in capitals; leave mixed-case text alone."""
    if value.isupper() or value.islower():
        return re.sub(r"(?<![’'])\b([a-zà-ÿ])", lambda match: match.group(1).upper(), value.lower())
    return value


def _clean_person(raw: str) -> str | None:
    name = re.sub(r"^(?:mr|mrs|ms|me|dr)\.?\s*", "", raw.strip(" .,;:"), flags=re.IGNORECASE)
    name = _tidy_case(re.sub(r"\s+", " ", name).strip(" .,;:"))
    if len(name) < 4 or not re.search(r"[A-Za-zÀ-ÿ]{2,}\S*\s+(?:\S+\s+)*[A-Za-zÀ-ÿ'’-]{2,}", name):
        return None
    if re.search(r"\b(?:comments?|minutes|court|registrar|usher|duration|appearances?|counsel)\b", name, re.IGNORECASE):
        return None
    return name


def person_key(name: str) -> str:
    folded = _helpers()._fold(name)
    folded = re.sub(r"\b[a-z]\.\s*", "", folded)
    return re.sub(r"[^a-z]+", "-", folded).strip("-")


def _appearances(text: str) -> list[dict[str, Any]]:
    marker = re.search(r"appearances?\s*:(.*?)(?:comments?\s*:|minutes of hearing|$)", text, re.IGNORECASE | re.DOTALL)
    if not marker:
        return []
    found: list[dict[str, Any]] = []
    for match in _APPEARANCE.finditer(marker.group(1)):
        side = (match.group(2) or "").casefold()
        # "Patricia Ritter Mr. Matthew Jeffery representing Applicant" lists two counsel.
        for part in re.split(r"\s+(?=(?:mr|mrs|ms|me|dr)\.?\s)", match.group(1), flags=re.IGNORECASE):
            name = _clean_person(part)
            if name:
                found.append(_appearance_entry(name, side))
    return found


def _appearance_entry(name: str, side: str) -> dict[str, Any]:
    role = (
        "self_represented"
        if not side
        else "applicant_counsel"
        if side.startswith("applicant") or side.startswith("appellant")
        else "respondent_counsel"
        if side.startswith("respondent") or side == "minister"
        else "other"
    )
    return {"name": name, "key": person_key(name), "role": role}


def extract_hearings(events: Iterable[Any]) -> dict[str, Any]:
    hearings: list[dict[str, Any]] = []
    for event in events:
        text = event.text
        if not _HEARING_ENTRY.search(text) or not re.search(r"\b(?:before|devant)\b", text, re.IGNORECASE):
            continue
        head = _HEARING_HEAD.search(text)
        subject_match = _HEARING_SUBJECT.search(text)
        subject = subject_match.group(1).strip() if subject_match else ""
        result_match = _HEARING_RESULT.search(text)
        raw_result = result_match.group(1).strip() if result_match else ""
        judge = _helpers()._clean_judge_name(_helpers()._judge_name(text))
        language = _HEARING_LANGUAGE.search(text)
        hearings.append(
            {
                "date": _parse_date(head.group(2)) if head else _event_date(event),
                "city": _tidy_case(head.group(1).strip()) if head else None,
                "judge": judge,
                "language": {"E": "english", "F": "french", "B": "bilingual"}.get(language.group(1).upper()) if language else None,
                "subject": subject[:120] or None,
                "kind": _hearing_kind(subject),
                "result": _hearing_result(raw_result),
                "result_text": raw_result[:160] or None,
                "mode": _hearing_mode(text),
                "duration_minutes": _hearing_minutes(text),
                "appearances": _appearances(text),
                "doc_id": event.doc_id,
            }
        )
    merits = [hearing for hearing in hearings if hearing["kind"] == "judicial_review" and hearing["result"] != "adjourned"]
    return {
        "count": len(hearings),
        "hearings": hearings,
        "judicial_review_hearing": merits[0] if merits else None,
        "status": "yes" if hearings else "none",
    }


# ---------------------------------------------------------------------------
# Certified question (IRPA s. 74(d)): an appeal to the FCA needs a certified question.
# ---------------------------------------------------------------------------

_CERTIFIED_YES = re.compile(
    r"(?:following|the)\s+(?:serious\s+)?questions?\s+(?:of general importance\s+)?(?:is|are|was|were|has been|have been)\s+certified"
    r"|certif(?:ies|y|ying)\s+the\s+following\s+(?:serious\s+)?questions?"
    r"|certified questions?\s*:"
    r"|(?:dismissed|granted|allowed)\s+with\s+(?:a\s+)?certified\s+questions?"
    r"|questions?\s+(?:is|are)\s+certified\s*:"
    r"|la\s+question\s+suivante\s+est\s+certifiée|certifie\s+la\s+question",
    re.IGNORECASE,
)
_CERTIFIED_NO = re.compile(
    r"\bno\s+(?:serious\s+)?questions?\s+(?:of general importance\s+)?(?:is|are|was|were|will be|shall be|has been|have been|to be|for)?\s*(?:certified|certification)"
    r"|no\s+questions?\s+(?:was|were)?\s*(?:proposed|submitted)\s+for\s+certification"
    r"|does\s+not\s+(?:have|propose)\s+(?:a\s+)?questions?\s+(?:for|to)\s+certif"
    r"|neither\s+(?:party|counsel)\s+(?:has|have)\s+(?:proposed\s+)?(?:a\s+)?(?:proposed\s+)?questions?"
    r"|aucune\s+question\s+(?:grave\s+)?(?:de\s+portée\s+générale\s+)?n['’]est\s+certifiée|aucune\s+question\s+n['’]a\s+été\s+(?:proposée|certifiée)"
    r"|(?:pas|aucune)\s+de\s+question\s+(?:grave\s+)?à\s+certifier|n['’]y\s+a\s+pas\s+de\s+question",
    re.IGNORECASE,
)
_JUDGMENT_ENTRY = re.compile(r"reasons for (?:judgment|order)|\bjudgment\b|\(final decision\)|jugement|motifs", re.IGNORECASE)


def extract_certified_question(events: Iterable[Any]) -> dict[str, Any]:
    certified: list[Any] = []
    not_certified: list[Any] = []
    for event in events:
        if re.match(r"^\W*copy of", event.text, re.IGNORECASE) and re.search(r"original (?:filed|placed) on court file no\.?\s*(?!imm)", event.text, re.IGNORECASE):
            continue
        if _CERTIFIED_YES.search(event.text) and not re.search(r"proposed questions? for certification|questions? proposed for certification|submissions? on (?:a )?certified", event.text, re.IGNORECASE):
            certified.append(event)
        elif _CERTIFIED_NO.search(event.text):
            not_certified.append(event)
    if certified:
        event = next((item for item in certified if _JUDGMENT_ENTRY.search(item.text)), certified[0])
        return {"status": "certified", **_evidence(event), "rule": "certified_question_entry"}
    if not_certified:
        event = next((item for item in not_certified if _JUDGMENT_ENTRY.search(item.text)), not_certified[0])
        return {"status": "not_certified", **_evidence(event), "rule": "no_question_certified_entry"}
    return {"status": "unknown", "doc_id": None, "date": None, "text": None, "rule": "no_certification_signal"}


# ---------------------------------------------------------------------------
# Appeals to the Federal Court of Appeal (court file numbers A-123-15).
# ---------------------------------------------------------------------------

_FCA_FILE = re.compile(r"\bA-\d{1,4}-\d{2}\b")
_NOTICE_OF_APPEAL = re.compile(r"notice of appeal|avis d['’]appel", re.IGNORECASE)


def extract_appeal(events: Iterable[Any]) -> dict[str, Any]:
    events = list(events)
    notices = [event for event in events if _NOTICE_OF_APPEAL.search(event.text) and (_FCA_FILE.search(event.text) or re.search(r"court of appeal|cour d['’]appel", event.text, re.IGNORECASE))]
    referenced = [event for event in events if _FCA_FILE.search(event.text)]
    if not notices and not referenced:
        return {"status": "none", "fca_files": [], "rule": "no_appeal_reference"}
    files = sorted({match.group(0) for event in notices + referenced for match in _FCA_FILE.finditer(event.text)})
    notice = notices[0] if notices else None
    appellant = "unknown"
    if notice is not None:
        text = notice.text.casefold()
        if re.search(r"on behalf of (?:the )?(?:respondent|minister)|by the (?:respondent|minister)|minister of", text):
            appellant = "minister"
        elif re.search(r"on behalf of (?:the )?applicant", text):
            appellant = "applicant"
    filed_date = None
    if notice is not None:
        filed = re.search(r"filed in the court of appeal on\s+(\d{1,2}-[A-Za-zÀ-ÿ]{3,5}-\d{4})", notice.text, re.IGNORECASE)
        filed_date = _parse_date(filed.group(1)) if filed else _event_date(notice)
    outcome = "pending_or_unknown"
    outcome_event = None
    for event in referenced:
        lowered = event.text.casefold()
        if re.search(r"notice of discontinuance|avis de désistement", lowered):
            outcome, outcome_event = "discontinued", event
        elif re.search(r"appeal (?:is )?(?:allowed|granted)|allowing the appeal|accueill", lowered):
            outcome, outcome_event = "allowed", event
        elif re.search(r"appeal (?:is )?dismissed|dismissing the appeal|rejet", lowered):
            outcome, outcome_event = "dismissed", event
        elif outcome == "pending_or_unknown" and re.search(r"reasons for judgment|\bjudgment\b|jugement", lowered) and not _NOTICE_OF_APPEAL.search(lowered):
            outcome, outcome_event = "decided_outcome_not_stated", event
    return {
        "status": "appealed" if notices else "referenced",
        "fca_files": files,
        "appellant": appellant,
        "filed_date": filed_date,
        "notice": _evidence(notice) if notice is not None else None,
        "outcome": outcome,
        "outcome_evidence": _evidence(outcome_event) if outcome_event is not None else None,
        "rule": "notice_of_appeal" if notices else "fca_file_reference",
    }


# ---------------------------------------------------------------------------
# Stay of removal motions.
# ---------------------------------------------------------------------------

_STAY = re.compile(r"stay of (?:the )?(?:execution|removal|deportation)|staying (?:the )?(?:execution|removal)|sursis (?:d['’]exécution|de la mesure|du renvoi|à l['’]exécution)|demande de sursis|\bstay motion\b", re.IGNORECASE)
_STAY_REQUEST = re.compile(r"notice of motion|avis de requête|motion record|dossier de (?:la )?requête|motion for", re.IGNORECASE)
_STAY_GRANTED = re.compile(r"granting the (?:motion for (?:a |an )?)?(?:interim )?stay|stay (?:of (?:execution|removal) )?(?:is )?granted|accordant (?:la demande de |le )?sursis|sursis (?:est )?accordé", re.IGNORECASE)
_STAY_REFUSED = re.compile(r"dismissing the (?:motion for (?:a |an )?)?(?:interim )?stay|stay (?:of (?:execution|removal) )?(?:is )?(?:dismissed|refused|denied)|rejetant (?:la demande de |le )?sursis|refusant (?:la demande de )?(?:le )?sursis", re.IGNORECASE)
_STAY_MOOT = re.compile(r"\bmoot\b|théorique|removal (?:has been|was|is) (?:cancelled|deferred)|renvoi (?:a été )?annulé", re.IGNORECASE)
_REMOVAL_DATE = re.compile(r"(?:scheduled|prévu)\s+(?:for|on|pour|le)\s+(\d{1,2}-[A-Za-zÀ-ÿ]{3,5}-\d{2,4})|on or before\s+(\d{1,2}-[A-Za-zÀ-ÿ]{3,5}-\d{2,4})", re.IGNORECASE)
_REMOVAL_TO = re.compile(r"(?:removal|removed|deport\w*|renvoi)\b[^.;]{0,80}?\b(?:to|vers|en|au)\s+((?-i:[A-Z][A-Za-z'-]+\.?(?:\s+(?:and\s+)?[A-Z][A-Za-z'-]+){0,2}))", re.IGNORECASE)
_NOT_A_PLACE = re.compile(r"^(?:be|begin|take|the|a|an|his|her|their|date|time|court|applicants?|respondents?|canada|stay|file|serve|consider|determine|proceed|occur|any|this|that|which|be determined)\b", re.IGNORECASE)


def extract_stay_of_removal(events: Iterable[Any]) -> dict[str, Any]:
    stay_events = [event for event in events if _STAY.search(event.text)]
    if not stay_events:
        return {"status": "none", "rule": "no_stay_signal"}
    request = next((event for event in stay_events if _STAY_REQUEST.search(event.text)), None)
    decisions = [event for event in stay_events if _STAY_GRANTED.search(event.text) or _STAY_REFUSED.search(event.text)]
    interim = any(re.search(r"interim stay|administrative stay|sursis provisoire|sursis administratif", event.text, re.IGNORECASE) for event in stay_events)
    outcome = "requested" if request else "mentioned"
    decision = None
    if decisions:
        decision = decisions[-1]
        outcome = "granted" if _STAY_GRANTED.search(decision.text) else "refused"
    elif any(_STAY_MOOT.search(event.text) for event in stay_events):
        outcome = "moot_or_removal_cancelled"
    removal_date = None
    destination = None
    for event in stay_events:
        date_match = _REMOVAL_DATE.search(event.text)
        if date_match and removal_date is None:
            removal_date = _parse_date(date_match.group(1) or date_match.group(2))
        destination_match = _REMOVAL_TO.search(event.text)
        if destination_match and destination is None:
            candidate = destination_match.group(1).strip()
            if candidate and not _NOT_A_PLACE.search(candidate) and not re.search(r"\d", candidate):
                destination = candidate
    return {
        "status": outcome,
        "interim_stay": interim,
        "requested_date": _event_date(request) if request else None,
        "decision_date": _event_date(decision) if decision else None,
        "decision_judge": _helpers()._clean_judge_name(_helpers()._judge_name(decision.text)) if decision else None,
        "removal_date": removal_date,
        "removal_destination": destination,
        "request": _evidence(request) if request else None,
        "decision": _evidence(decision) if decision else None,
        "rule": "stay_decision_entry" if decision else "stay_request_without_decision" if request else "stay_mentioned",
    }


# ---------------------------------------------------------------------------
# Representation: the applicant's counsel or self-representation.
# ---------------------------------------------------------------------------

_SERVICE_BY_COUNSEL = re.compile(
    r"solicitor['’]s certificate of service on behalf of\s+(.+?)(?:,\s*counsel for the applicants?)?,?\s+confirming (?:attempted )?service of .{0,160}?\bupon (?:the )?respondent",
    re.IGNORECASE,
)
_SERVICE_BY_COUNSEL_FR = re.compile(
    r"attestation de signification de l['’]avocat de la part (?:de\s+)?(?:me\.?\s+)?(.+?)\s+attestant la signification .{0,160}?\bà la partie défenderesse",
    re.IGNORECASE,
)
_COUNSEL_IS = re.compile(r"\bcounsel (?:is|for the applicants? is)\s+((?:me\.?\s+|mr\.?\s+|ms\.?\s+)?[A-ZÀ-Ý][\w'’.-]+(?:\s+[A-ZÀ-Ý][\w'’.-]+){1,3})", re.IGNORECASE)
_SELF_REPRESENTED = re.compile(r"self[- ]represented|acting in person|on (?:his|her|their) own behalf|se représente (?:seule?|lui-même|elle-même)|non représentée?|unrepresented", re.IGNORECASE)
_DOJ_ROLES = re.compile(r"department of justice|ministère de la justice|attorney general|procureur général", re.IGNORECASE)


def extract_representation(events: Iterable[Any], hearings: dict[str, Any] | None = None) -> dict[str, Any]:
    events = list(events)
    counsel: Counter[str] = Counter()
    display: dict[str, str] = {}
    sources: Counter[str] = Counter()
    for event in events:
        for pattern, source in ((_SERVICE_BY_COUNSEL, "certificate_of_service"), (_SERVICE_BY_COUNSEL_FR, "certificate_of_service"), (_COUNSEL_IS, "motion_record")):
            match = pattern.search(event.text)
            if not match or _DOJ_ROLES.search(match.group(1)):
                continue
            name = _clean_person(re.split(r",|\s+\(|\s+of\s+|\s+barrister|\s+\d", match.group(1))[0])
            if name and len(name.split()) <= 5:
                key = person_key(name)
                counsel[key] += 1
                display.setdefault(key, name)
                sources[source] += 1
    self_represented = any(_SELF_REPRESENTED.search(event.text) for event in events)
    for hearing in (hearings or {}).get("hearings", []):
        for appearance in hearing.get("appearances", []):
            if appearance["role"] == "applicant_counsel":
                counsel[appearance["key"]] += 2
                display.setdefault(appearance["key"], appearance["name"])
                sources["hearing_appearance"] += 1
            elif appearance["role"] == "self_represented":
                self_represented = True
    ranked = [{"name": display[key], "key": key, "mentions": count} for key, count in counsel.most_common()]
    status = "represented" if ranked else "self_represented" if self_represented else "unknown"
    if ranked and self_represented:
        status = "mixed"
    return {
        "status": status,
        "applicant_counsel": ranked[0] if ranked else None,
        "all_applicant_counsel": ranked[:5],
        "change_of_solicitor": sum(1 for event in events if re.search(r"notice of (?:change|appointment|removal) of solicitor|changement d['’]avocat|nomination d['’]avocat|cessation d['’]occuper", event.text, re.IGNORECASE)),
        "sources": dict(sources),
        "rule": "counsel_named_in_service_or_appearance" if ranked else "self_representation_signal" if self_represented else "no_counsel_signal",
    }


# ---------------------------------------------------------------------------
# Respondent's position on leave.
# ---------------------------------------------------------------------------

_RESPONDENT_MEMO = re.compile(r"memorandum of argument (?:on behalf )?of the respondent|memorandum of argument on behalf of (?:the )?respondent|respondent['’]s memorandum|mémoire (?:des arguments )?de la partie défenderesse|mémoire de la partie intimée|mémoire (?:des arguments )?de la part (?:de la partie défenderesse|du défendeur|de la défenderesse|de l['’]intimée?|de la partie intimée)|respondent['’]s (?:record|written submissions)", re.IGNORECASE)
_RESPONDENT_NOT_OPPOSING = re.compile(r"(?:does not|will not|doesn['’]t|won['’]t) (?:oppose|contest) (?:the )?(?:application for )?leave|not oppos(?:e|ing) (?:the )?(?:granting of )?leave|consents? to (?:the granting of )?leave|ne s['’]oppose pas à (?:la demande d['’])?autorisation", re.IGNORECASE)
_RESPONDENT_NO_MEMO = re.compile(r"(?:will not|does not intend to|shall not) (?:be )?fil(?:e|ing) (?:a |any )?(?:memorandum|written submissions)|n['’]a pas l['’]intention de déposer (?:de |un )?mémoire|ne déposera pas", re.IGNORECASE)


def extract_respondent_position(events: Iterable[Any], leave_decision_date: str | None) -> dict[str, Any]:
    before = [event for event in events if not leave_decision_date or not event.doc_date or event.doc_date.isoformat() <= leave_decision_date]
    for pattern, status in ((_RESPONDENT_NOT_OPPOSING, "not_opposed"), (_RESPONDENT_NO_MEMO, "no_memorandum"), (_RESPONDENT_MEMO, "opposed")):
        event = next((item for item in before if pattern.search(item.text) and (status != "opposed" or not re.search(r"motion|requête", item.text, re.IGNORECASE))), None)
        if event is not None:
            return {"status": status, **_evidence(event), "rule": f"respondent_{status}"}
    return {"status": "unknown", "doc_id": None, "date": None, "text": None, "rule": "no_respondent_position_signal"}


# ---------------------------------------------------------------------------
# Filing details, perfection and related files.
# ---------------------------------------------------------------------------


def extract_filing_details(events: Iterable[Any], citation: str | None) -> dict[str, Any]:
    events = list(events)
    application = next((event for event in events if re.search(r"application for leave|demande d['’]autorisation|notice of application", event.text, re.IGNORECASE)), None)
    reasons = "unknown"
    if application is not None:
        if re.search(r"written reasons not received|motifs écrits non reçus|motifs non reçus", application.text, re.IGNORECASE):
            reasons = "not_received"
        elif re.search(r"written reasons received|motifs écrits reçus|motifs reçus", application.text, re.IGNORECASE):
            reasons = "received"
    reasons_request = any(re.search(r"rule 9\b|règle 9\b|request for (?:written )?reasons", event.text, re.IGNORECASE) for event in events)
    own = (citation or "").upper()
    lead_counts: Counter[str] = Counter()
    for event in events:
        for match in re.finditer(r"(?:original (?:filed|placed) on court file no\.?|original (?:on|file\s*:?)|order filed on|filed on)\s*(IMM-\d+-\d{2})", event.text, re.IGNORECASE):
            number = match.group(1).upper()
            if number != own:
                lead_counts[number] += 1
    french = sum(1 for event in events if re.search(r"\b(?:déposé|partie demanderesse|partie défenderesse|ordonnance|requête|avis de|reçu|le dossier)\b", event.text, re.IGNORECASE))
    share = french / len(events) if events else 0
    return {
        "reasons_at_filing": reasons,
        "rule_9_reasons_request": reasons_request,
        "extension_of_time_requested": bool(application and re.search(r"extension of time|prorogation", application.text, re.IGNORECASE)),
        "lead_file": lead_counts.most_common(1)[0][0] if lead_counts else None,
        "related_files": sorted(lead_counts),
        "proceeding_language": "unknown" if not events else "french" if share >= 0.6 else "english" if share <= 0.2 else "mixed",
        "french_entry_share": round(share, 2),
    }


def leave_refusal_reason(
    leave_result: str,
    leave_date: str | None,
    leave_text: str | None,
    perfected_date: str | None,
) -> str | None:
    """Why leave failed: the applicant never perfected (filed a record) or the Court refused on the record."""
    if leave_result != "refused":
        return None
    text = (leave_text or "").casefold()
    if re.search(r"fail(?:ure|ed|ing)? (?:of the applicant )?to (?:file|serve|perfect)|no application record|not perfected|défaut de (?:déposer|produire)", text):
        return "not_perfected"
    if perfected_date and (not leave_date or perfected_date <= leave_date):
        return "refused_after_perfection"
    if leave_date and not perfected_date:
        return "not_perfected"
    return "unknown"


def _plausible(days: int | None, limit: int = 3650) -> int | None:
    """Drop gaps produced by mistyped dates (a decision "dated" decades before filing)."""
    return days if days is not None and days <= limit else None


def build_timeline(classification: dict[str, Any], hearings: dict[str, Any]) -> dict[str, Any]:
    """Day counts between procedural milestones; null when either end is not observed."""
    filed = (classification.get("application_filed") or {}).get("date") or (classification.get("challenged_decision") or {}).get("filing_date")
    perfected = (classification.get("application_perfected") or {}).get("date")
    leave = classification.get("leave_decision") or {}
    leave_date = leave.get("date") if leave.get("result") in {"granted", "refused"} else None
    review = classification.get("judicial_review_final_decision") or {}
    review_date = review.get("date") if (classification.get("judicial_review_result") or {}).get("result") in {"granted", "dismissed"} else None
    hearing = hearings.get("judicial_review_hearing") or {}
    hearing_date = hearing.get("date")
    resolution = classification.get("full_history_resolution") or {}
    final_date = resolution.get("date") if resolution.get("status") not in {None, "unknown"} else None
    decision_date = (classification.get("challenged_decision") or {}).get("decision_date")
    return {
        "filed": filed,
        "perfected": perfected,
        "leave_decided": leave_date,
        "judicial_review_heard": hearing_date,
        "judicial_review_decided": review_date,
        "final_disposition": final_date,
        "days_filing_to_perfection": _days_between(filed, perfected),
        "days_filing_to_leave_decision": _days_between(filed, leave_date),
        "days_perfection_to_leave_decision": _days_between(perfected, leave_date),
        "days_leave_grant_to_hearing": _days_between(leave_date, hearing_date) if leave.get("result") == "granted" else None,
        "days_hearing_to_judgment": _days_between(hearing_date, review_date),
        "days_filing_to_final_disposition": _days_between(filed, final_date),
        "judgment_from_bench": bool(hearing_date and review_date and hearing_date == review_date),
        "challenged_decision_date": _parse_date(decision_date) if decision_date else None,
        "days_decision_to_filing": _plausible(_days_between(_parse_date(decision_date) if decision_date else None, filed)),
    }


def extract_insights(events: list[Any], classification: dict[str, Any], citation: str | None) -> dict[str, Any]:
    """Run every extractor for one file and return the new top-level classification fields."""
    hearings = extract_hearings(events)
    leave = classification.get("leave_decision") or {}
    appeal = extract_appeal(events)
    review_result = (classification.get("judicial_review_result") or {}).get("result")
    if appeal["status"] == "appealed" and appeal["appellant"] == "unknown" and review_result in {"granted", "dismissed"}:
        # The losing side appeals: the applicant after a dismissal, the Minister after a grant.
        appeal["appellant"] = "applicant_inferred" if review_result == "dismissed" else "minister_inferred"
    certified = extract_certified_question(events)
    if certified["status"] == "unknown" and appeal["status"] == "appealed" and review_result in {"granted", "dismissed"}:
        # IRPA s. 74(d): no appeal lies from a judicial review judgment without a certified question.
        certified = {**certified, "status": "certified_inferred_from_appeal", "rule": "appeal_requires_certified_question"}
    filing = extract_filing_details(events, citation)
    perfected_date = (classification.get("application_perfected") or {}).get("date")
    return {
        "hearings": hearings,
        "certified_question": certified,
        "appeal": appeal,
        "stay_of_removal": _stay_from_register(extract_stay_of_removal(events), classification.get("motions") or {}),
        "representation": extract_representation(events, hearings),
        "respondent_position": extract_respondent_position(events, leave.get("date") if leave.get("result") in {"granted", "refused"} else None),
        "filing_details": {
            **filing,
            "leave_refusal_reason": leave_refusal_reason(leave.get("result") or "unknown", leave.get("date"), leave.get("text"), perfected_date),
        },
        "timeline": build_timeline(classification, hearings),
        "office_location": extract_office_location(classification),
        "motion_profile": motion_profile_from_register(classification.get("motions") or extract_motions(events)),
        "parties": extract_parties(events),
    }


# ---------------------------------------------------------------------------
# Where the challenged decision was made: visa office abroad, IRB region or processing centre.
# ---------------------------------------------------------------------------

OFFICE_LOCATIONS: tuple[tuple[str, str], ...] = (
    ("New Delhi", r"new delhi|\bdelhi\b"), ("Chandigarh", r"chandigarh"), ("Hong Kong", r"hong\s*kong"), ("Beijing", r"beijing|pékin"),
    ("Shanghai", r"shanghai"), ("Guangzhou", r"guangzhou"), ("Manila", r"manila|makati"), ("Singapore", r"singapore|singapour"),
    ("Islamabad", r"islamabad"), ("Abu Dhabi", r"abu\s*dhabi"), ("Dubai", r"dubai"), ("Ankara", r"ankara"), ("Damascus", r"damascus|damas\b"),
    ("Beirut", r"beyrouth|beirut"), ("Amman", r"\bamman\b"), ("Cairo", r"cairo|le caire"), ("Tel Aviv", r"tel\s*aviv"), ("Riyadh", r"riyadh"),
    ("Nairobi", r"nairobi"), ("Accra", r"accra"), ("Lagos", r"lagos"), ("Dakar", r"dakar"), ("Pretoria", r"pretoria"), ("Abidjan", r"abidjan"),
    ("Rabat", r"rabat"), ("Tunis", r"\btunis\b"), ("Dar es Salaam", r"dar es salaam"), ("Colombo", r"colombo"), ("Dhaka", r"dhaka"),
    ("Kathmandu", r"kathmandu"), ("Bangkok", r"bangkok"), ("Ho Chi Minh City", r"ho chi minh"), ("Seoul", r"seoul|séoul"), ("Tokyo", r"tokyo"),
    ("Sydney (Australia)", r"sydney,? australia"), ("London", r"\blondon\b(?!,? ont)"), ("Paris", r"\bparis\b"), ("Rome", r"\brome\b"),
    ("Vienna", r"vienna|vienne"), ("Warsaw", r"warsaw|varsovie"), ("Bucharest", r"bucharest|bucarest"), ("Moscow", r"moscow|moscou"),
    ("Kyiv", r"kyiv|kiev"), ("Berlin", r"berlin"), ("Buffalo", r"buffalo"), ("Seattle", r"seattle"), ("Los Angeles", r"los angeles"),
    ("New York", r"new york"), ("Detroit", r"detroit"), ("Mexico City", r"mexico city|mexico,? mexico|ciudad de méxico"),
    ("Port of Spain", r"port of spain"), ("Kingston", r"kingston,? jamaica"), ("Port-au-Prince", r"port-au-prince"), ("Bogotá", r"bogot"),
    ("Lima", r"\blima\b"), ("Santiago", r"santiago"), ("São Paulo", r"s[ãa]o paulo"), ("Guatemala City", r"guatemala"),
    ("Sydney NS (CIO)", r"sydney,? (?:ns|nova scotia)|centralized intake"), ("Vegreville CPC", r"vegreville"), ("Mississauga", r"mississauga"),
    ("Etobicoke", r"etobicoke"), ("Scarborough", r"scarborough"), ("Niagara Falls", r"niagara"), ("Toronto", r"toronto|\btor\b"),
    ("Montréal", r"montr[ée]al|\bmtl\b"), ("Vancouver", r"vancouver|\bvan\b"), ("Calgary", r"calgary"), ("Edmonton", r"edmonton"),
    ("Winnipeg", r"winnipeg"), ("Ottawa", r"ottawa|\bnhq\b"), ("Halifax", r"halifax"), ("Québec City", r"qu[ée]bec city|ville de qu[ée]bec"),
)
_OFFICE_PATTERNS = tuple((name, re.compile(pattern, re.IGNORECASE)) for name, pattern in OFFICE_LOCATIONS)


def extract_office_location(classification: dict[str, Any]) -> dict[str, Any]:
    """Name the office that made the challenged decision, from the decision maker or tribunal-record sender text."""
    body = classification.get("decision_body") or {}
    challenged = classification.get("challenged_decision") or {}
    for source, text in (("decision_maker", challenged.get("decision_maker")), ("record_sender", body.get("evidence") if body.get("source") == "record_sender" else None), ("application_text", challenged.get("text"))):
        if not text:
            continue
        for name, pattern in _OFFICE_PATTERNS:
            if pattern.search(text):
                return {"office": name, "abroad": not re.search(r"\(cio\)|cpc|^(?:mississauga|etobicoke|scarborough|niagara falls|toronto|montréal|vancouver|calgary|edmonton|winnipeg|ottawa|halifax|québec city)$", name, re.IGNORECASE), "source": source}
    return {"office": None, "abroad": None, "source": None}


# ---------------------------------------------------------------------------
# Motions filed in the file, by type and outcome.
# ---------------------------------------------------------------------------

_MOTION_FAMILIES = (
    ("stay", r"^stay"),
    ("extension_of_time", r"extension"),
    ("consent_judgment", r"consent"),
    ("amendment", r"amend"),
    ("reconsideration", r"reconsider|rule_397"),
    ("confidentiality", r"confiden|anonym"),
    ("abeyance", r"abeyance"),
    ("intervention", r"interven"),
    ("production", r"production"),
)


_MOTION_NOTICE = re.compile(r"^\W*(?:amended\s+)?(?:notice of motion|avis de requête|requête (?:par voie de lettre|informelle)|informal motion|motion (?:in writing )?by (?:way of )?letter)", re.IGNORECASE)


def extract_motion_profile(classification: dict[str, Any], events: list[Any]) -> dict[str, Any]:
    decided: dict[str, Counter[str]] = {}
    filed = sum(1 for event in events if _MOTION_NOTICE.search(event.text))
    for item in classification.get("procedural_events") or []:
        if item.get("event_type") != "motion_decision":
            continue
        subtype = str(item.get("subtype") or "unknown")
        family = next((name for name, pattern in _MOTION_FAMILIES if re.search(pattern, subtype)), "other")
        if item.get("outcome"):
            decided.setdefault(family, Counter())[item["outcome"]] += 1
    reconsideration = any(re.search(r"reconsideration|rule 397|règle 397|nouvel examen", event.text, re.IGNORECASE) for event in events)
    return {
        "motions_filed": filed,
        "decisions": {family: dict(counts) for family, counts in decided.items()},
        "families": sorted(decided),
        "reconsideration_requested": reconsideration,
        "extension_of_time": (
            "granted" if decided.get("extension_of_time", Counter()).get("granted") else "refused" if decided.get("extension_of_time") else None
        ),
    }


_STAY_STATUS = {"granted": "granted", "granted_in_part": "granted", "dismissed": "refused", "withdrawn": "withdrawn", "moot": "moot_or_removal_cancelled"}


def _stay_from_register(stay: dict[str, Any], register: dict[str, Any]) -> dict[str, Any]:
    """Prefer the motion register's linked ruling for the stay outcome, keeping removal details from the text reader."""
    stays = [motion for motion in register.get("motions") or [] if motion["type"] in {"stay_of_removal", "stay_of_release"}]
    if not stays:
        return stay
    decided = [motion for motion in stays if motion["outcome"] in _STAY_STATUS]
    chosen = decided[-1] if decided else stays[-1]
    status = _STAY_STATUS.get(chosen["outcome"], "requested" if chosen.get("filed_doc_id") else stay.get("status", "mentioned"))
    return {
        **stay,
        "status": status,
        "motions": len(stays),
        "decision_date": chosen.get("decision_date") or stay.get("decision_date"),
        "decision_judge": chosen.get("judge") or stay.get("decision_judge"),
        "rule": "motion_register",
    }


def motion_rows(register: dict[str, Any]) -> list[dict[str, Any]]:
    """Flat rows for fc_activity_motions."""
    rows = []
    for position, motion in enumerate(register.get("motions") or [], start=1):
        judge = motion.get("judge") or {}
        rows.append(
            {
                "position": position,
                "motion_type": motion["type"],
                "filer": motion.get("filer"),
                "outcome": motion["outcome"],
                "link": motion.get("link"),
                "judge_key": judge.get("key"),
                "judge_name": judge.get("name"),
                "filed_date": motion.get("filed_date"),
                "decision_date": motion.get("decision_date"),
                "days_to_decision": motion.get("days_to_decision"),
                "in_writing": motion.get("in_writing"),
                "relief": (motion.get("relief") or "")[:400] or None,
            }
        )
    return rows


def motion_profile_from_register(register: dict[str, Any]) -> dict[str, Any]:
    motions = register.get("motions") or []
    extension = [motion for motion in motions if motion["type"] == "extension_of_time" and motion["outcome"] in {"granted", "granted_in_part", "dismissed"}]
    return {
        "motions_filed": sum(1 for motion in motions if motion.get("filed_doc_id")),
        "motions_ruled": register.get("decided", 0),
        "families": sorted({motion["type"] for motion in motions}),
        "decisions": register.get("by_type", {}),
        "reconsideration_requested": any(motion["type"] == "reconsideration" for motion in motions),
        "extension_of_time": None if not extension else "granted" if any(motion["outcome"] != "dismissed" for motion in extension) else "refused",
    }


def extract_parties(events: list[Any]) -> dict[str, Any]:
    name = next((event.case_name for event in events if getattr(event, "case_name", None)), None) or ""
    parts = re.split(r"\s+v\.?\s+|\s+c\.\s+", name, maxsplit=1)
    applicants = parts[0]
    respondent = parts[1] if len(parts) > 1 else ""
    joint = bool(re.search(r"\bet al\b|\s(?:and|et|&)\s|,", applicants, re.IGNORECASE))
    return {"joint_applicants": joint if name else None, "respondent_style": respondent.strip()[:80] or None}


def summary_row(classification: dict[str, Any]) -> dict[str, Any]:
    """Flatten the fields the site aggregates into one fc_activity_summaries row."""

    def get(*path: str) -> Any:
        value: Any = classification
        for key in path:
            if not isinstance(value, dict):
                return None
            value = value.get(key)
        return value

    def text(value: Any, limit: int) -> str | None:
        return str(value)[:limit] if value not in (None, "") else None

    timeline = classification.get("timeline") or {}
    return {
        "resolution": text(get("full_history_resolution", "status"), 80),
        "lifecycle": text(get("lifecycle_status", "status"), 40),
        "leave_result": text(get("leave_decision", "result"), 40),
        "review_result": text(get("judicial_review_result", "result"), 40),
        "decision_body": text(get("decision_body", "code"), 40),
        "leave_judge_key": text(get("judge_roles", "leave_judge", "key"), 120),
        "leave_judge_name": text(get("judge_roles", "leave_judge", "name"), 255),
        "merits_judge_key": text(get("judge_roles", "merits_judge", "key"), 120),
        "merits_judge_name": text(get("judge_roles", "merits_judge", "name"), 255),
        "applicant_counsel_key": text(get("representation", "applicant_counsel", "key"), 160),
        "applicant_counsel_name": text(get("representation", "applicant_counsel", "name"), 255),
        "representation": text(get("representation", "status"), 40),
        "respondent_position": text(get("respondent_position", "status"), 40),
        "leave_refusal_reason": text(get("filing_details", "leave_refusal_reason"), 40),
        "stay_status": text(get("stay_of_removal", "status"), 40),
        "hearing_mode": text(get("hearings", "judicial_review_hearing", "mode"), 40),
        "hearing_minutes": get("hearings", "judicial_review_hearing", "duration_minutes"),
        "appeal_status": text(get("appeal", "status"), 40),
        "certified_question": text(get("certified_question", "status"), 60),
        "consent_status": text(get("consent_disposition", "status"), 40),
        "reasons_at_filing": text(get("filing_details", "reasons_at_filing"), 40),
        "proceeding_language": text(get("filing_details", "proceeding_language"), 20),
        "lead_file": text(get("filing_details", "lead_file"), 40),
        "days_filing_to_perfection": timeline.get("days_filing_to_perfection"),
        "days_filing_to_leave_decision": timeline.get("days_filing_to_leave_decision"),
        "days_leave_grant_to_hearing": timeline.get("days_leave_grant_to_hearing"),
        "days_hearing_to_judgment": timeline.get("days_hearing_to_judgment"),
        "days_filing_to_final_disposition": timeline.get("days_filing_to_final_disposition"),
        "judgment_from_bench": timeline.get("judgment_from_bench"),
        "application_type": text(get("challenged_decision", "application_type"), 80),
        "office_location": text(get("office_location", "office"), 80),
        "joint_applicants": get("parties", "joint_applicants"),
        "motions_filed": get("motion_profile", "motions_filed"),
        "extension_of_time": text(get("motion_profile", "extension_of_time"), 40),
        "dormant": bool(get("lifecycle_status", "status") == "active" and (get("history_profile", "days_since_last_entry") or 0) > 730),
        "days_decision_to_filing": timeline.get("days_decision_to_filing"),
    }


# ---------------------------------------------------------------------------
# Motion register: each motion filed, its type, who filed it, and the decision on it.
# ---------------------------------------------------------------------------

_MOTION_FILING = re.compile(
    r"^\W*(?:\*+\s*)?(?:amended\s+|further\s+amended\s+)?(?:notice of motion|avis de requ[êe]te|requ[êe]te (?:par voie de lettre|informelle|écrite)|requ[êe]te (?:de la part|en vertu|pour|selon)|informal (?:motion|request)|request by way of letter|motion (?:in writing )?by (?:way of )?letter|notice of (?:cross|urgent) motion)",
    re.IGNORECASE,
)
_NOT_DECISION = re.compile(
    r"^\W*(?:copy|copie|acknowledg|accus[ée]|certified|traduction|draft|projet|letter|lettre|communication|memorandum|mémoire|notice of|avis de|motion record|dossier de (?:la )?requ|affidavit|written representations|book of|reply|réplique|consent|consentement|solicitor|attestation|record|reasons for order dated)",
    re.IGNORECASE,
)
_COURT_ACT = re.compile(r"\brendered\b|\brendu(?:\(e\))?s?\b|^\W*(?:\(final decision\)\s*|\(décision finale\)\s*)?(?:order|ordonnance|judgment|jugement)\b[^\n]{0,40}?(?:dated|en date)|order of the court", re.IGNORECASE)
_MOTION_DOC_REF = re.compile(
    r"(?:motion|requ[êe]te)(?:\s+in\s+writing)?\s*(?:\(|,)?\s*(?:doc(?:ument)?s?\.?|#)\s*(?:n[°oº]?\.?|no\.?|number|#)?\s*(\d{1,3})\b"
    r"|\(\s*(?:motion|requ[êe]te)\s+doc(?:ument)?\.?\s*(?:n[°oº]?\.?|no\.?|#)?\s*(\d{1,3})\s*\)"
    r"|(?:granting|dismissing|accordant|rejetant)\s+(?:the\s+|la\s+)?(?:motion|requ[êe]te)(?:\(s\))?\s*(?:doc\.?\s*)?#?\s*(\d{1,3})\b"
    r"|(?:motion|requ[êe]te)[^\n]{0,80}?\(\s*doc(?:ument)?\.?\s*(?:n[°oº]?\.?|no\.?|#)?\s*(\d{1,3})\s*\)"
    # 1990s registry wording names every motion "the application for an extension of time <doc>".
    r"|(?:application|demande) (?:for an |de )(?:extension of time|prorogation de délai)\s+(\d{1,3})\b",
    re.IGNORECASE,
)
_ENTRY_ID_REF = re.compile(r"\(\s*id\s*(?:no\.?|#)?\s*(\d{1,3})\s*\)|\bid\s*#\s*(\d{1,3})\b|\(id\s*#?(\d{1,3})\)", re.IGNORECASE)
_STRUCTURED_MOTION_RESULT = re.compile(
    r"with regard to (?:the )?(?:motion|requ[êe]te|letter|informal (?:motion|request)|request)[^\n]{0,160}?result\s*:\s*([^\n]{0,60})"
    r"|concernant (?:\(le/la/l['’]\) )?(?:la |le |l['’])?(?:requ[êe]te|lettre|demande informelle)[^\n]{0,160}?r[ée]sultat\s*:\s*([^\n]{0,60})",
    re.IGNORECASE,
)
_DIRECTION_RULING = re.compile(r"^\W*(?:oral\s+)?directions? (?:of the (?:court|presiding judge)|verbales|de la cour)[^\n]{0,160}?directing[^\n]{0,40}?\b(granted|is granted|refused|is refused|dismissed|denied|accordée?|rejetée?)\b", re.IGNORECASE)
_IMPLICIT_GRANT = re.compile(r"this court orders|il est ordonné|la cour ordonne|is (?:hereby )?(?:extended|adjourned|granted an extension)|(?:is|are) granted an extension|time (?:for|to) [^\n]{0,60}?is extended", re.IGNORECASE)
_HEARING_MOTION = re.compile(r"(?:before the court|matière en litige)\s*:\s*(?:continuation of (?:the )?)?(?:reprise [^\n]{0,30})?(?:motion|requ[êe]te)[^\n]{0,200}?(?:result of hearing|résultat de l['’]audition)\s*:\s*([^\n]{0,60})", re.IGNORECASE)
_LEAVE_ORDER = re.compile(r"(?:granting|dismissing|accordant|rejetant)\s+(?:the\s+|la\s+)?(?:application for leave|demande d['’]autorisation)|dismissing the (?:application for (?:an )?)?extension of time to (?:file|commence)", re.IGNORECASE)
_WITHDRAWN_MOTION = re.compile(r"(?:(?:motion|requ[êe]te)\s+doc(?:ument)?\.?\s*(?:no\.?\s*)?\d+[^\n]{0,120}?\bnow withdrawn|notice of (?:withdrawal|abandonment|discontinuance) of (?:the |its |their |[\w-]+['’]s )*(?:\w+ )?motion|(?<!if current )(?<!if the )(?<!if )withdraw(?:s|ing)? (?:the |its |their |his |her )?motion|motion (?:is |was |has been )?(?:withdrawn|abandoned)|désistement de (?:la )?requ[êe]te|retrait de la requ[êe]te)", re.IGNORECASE)

MOTION_TYPES: tuple[tuple[str, str], ...] = (
    ("stay_of_release", r"stay(?:ing)?\b[^\n]{0,40}?(?:order (?:of|for) release|release order|release of the respondent)|sursis [^\n]{0,30}mise en liberté"),
    ("stay_of_removal", r"\bstay(?:ing)?\b[^\n]{0,60}?(?:removal|deportation|execution|exclusion|departure)|sursis|\bstay of (?:the )?(?:removal|execution|deportation)"),
    ("judgment_on_consent", r"(?:judgment|order|jugement)\s+(?:on|by|par|sur)\s+consent|consent judgment|consentement (?:à|a) jugement|settle|allow(?:ing)? the (?:application|judicial review|jr)|grant(?:ing)? the (?:application for )?(?:leave and )?(?:for )?judicial review|grant(?:ing)? the application\b(?! for (?:an )?extension)|(?:judicial review|application|jr) (?:is|be|shall be) (?:allowed|granted)|leave (?:of the court )?(?:is|be|shall be) granted[^\n]{0,80}?(?:judicial review|set aside|quash|redetermin)|set(?:ting)? aside the decision|quash(?:ing)? the decision|redetermination|referr?(?:ing|ed)? (?:the matter )?back|accueillir la demande de contrôle"),
    ("extension_of_time", r"extension of time|extend(?:ing)? (?:the )?time|prorogation|proroger|délai|more time|additional time"),
    ("reconsideration", r"reconsider|rule\s*39[79]|règle\s*39[79]|nouvel examen|vary (?:the|an?) order"),
    ("adjournment", r"adjourn|reschedul|postpone|ajourn|remise|change (?:the )?(?:date|hearing)"),
    ("abeyance", r"abeyance|suspen[ds]|en suspens|stay of (?:the )?proceedings"),
    ("dismiss_or_strike", r"(?:to|an order|order) (?:dismiss|strike|quash)(?:ing)? (?:the |this |his |her |their |applicant['’]s )?(?:application|proceeding)|dismissing the (?:applicant['’]s )?application|motion to (?:dismiss|strike)|radier|rejeter la demande"),
    ("amendment", r"amend|style of cause|intitulé|modifi"),
    ("confidentiality", r"confidential|anonym|sealing|seal\b|non-disclosure|section 87|s\.?\s*87|s\.?\s*37|huis clos"),
    ("production_or_record", r"production|tribunal record|certified (?:tribunal )?record|rule\s*(?:14|17|317|318)|transcript|dossier certifié"),
    ("further_evidence", r"further (?:affidavit|evidence|memorandum)|additional (?:affidavit|evidence)|fresh evidence|nouvelle preuve|affidavit supplémentaire|file (?:a )?(?:further|reply)"),
    ("consolidation", r"consolidat|join (?:the )?(?:files|proceedings)|joinder|réunion|jonction|heard together"),
    ("counsel", r"solicitor of record|removal (?:of|as) (?:counsel|solicitor)|cease to act|cesser d['’]occuper|withdraw as counsel|change of solicitor"),
    ("intervention", r"interven"),
    ("expedite", r"expedit|urgent|abridg|accélér"),
    ("release_or_detention", r"release|detention|détention|mise en liberté"),
    ("costs", r"\bcosts\b|dépens"),
)
_MOTION_TYPE_PATTERNS = tuple((name, re.compile(pattern, re.IGNORECASE)) for name, pattern in MOTION_TYPES)


_TYPE_FAMILY = {"stay_of_removal": "stay", "stay_of_release": "stay"}


def _same_family(first: str, second: str) -> bool:
    return first == second or (_TYPE_FAMILY.get(first) is not None and _TYPE_FAMILY.get(first) == _TYPE_FAMILY.get(second))


def motion_type(text: str) -> str:
    return next((name for name, pattern in _MOTION_TYPE_PATTERNS if pattern.search(text)), "other")


def _motion_relief(text: str) -> str:
    """The relief asked for: the text after the first "for"/"pour", up to the filing details."""
    start = re.search(r"\b(?:for|pour|seeking|requesting|visant à obtenir|en vue d['’]obtenir)\s+", text, re.IGNORECASE)
    relief = text[start.end():] if start else text
    relief = re.split(r"\s+(?:filed|déposée?\(?s?\)?)\s+(?:on|le)\b|\s+draft order|\s+projet d|\s+with proof of service|\s+avec preuve de signification", relief, maxsplit=1, flags=re.IGNORECASE)[0]
    return relief[:400]


def _motion_filer(text: str) -> str:
    lowered = text.casefold()
    if re.search(r"on behalf of (?:the )?(?:respondent|minister)|de la part (?:de la partie (?:défenderesse|intimée)|du défendeur|du ministre)", lowered):
        return "respondent"
    if re.search(r"on behalf of (?:the )?applicants?|de la part (?:de la partie (?:demanderesse|requérante)|du demandeur|de la demanderesse)", lowered):
        return "applicant"
    if re.search(r"on behalf of (?:all parties|the parties)|joint motion|requête conjointe", lowered):
        return "joint"
    return "unknown"


def _normalize_outcome(raw: str) -> str | None:
    lowered = raw.casefold()
    if re.search(r"reserved|délibéré|under advisement", lowered):
        return "reserved"
    if re.search(r"adjourn|ajourn|sine die|remis", lowered):
        return "adjourned"
    if re.search(r"granted in part|partially granted|in part|en partie|partiellement", lowered):
        return "granted_in_part"
    if re.search(r"moot|théorique|sans objet", lowered):
        return "moot"
    if re.search(r"withdrawn|abandon|retir|désist", lowered):
        return "withdrawn"
    if re.search(r"grant|allow|accord|accueill|order to go as asked|quashed|set aside|remitted|referred back|returned for redetermination|cass[ée]|renvoy", lowered):
        return "granted"
    if re.search(r"dismiss|refus|deni|rejet|reject", lowered):
        return "dismissed"
    return None


def _decision_on_motion(text: str) -> dict[str, Any] | None:
    """Read one docket entry as a ruling on a motion; None when it is not one."""
    direction = _DIRECTION_RULING.search(text)
    if direction:
        return {"outcome": _normalize_outcome(direction.group(1)), "source": "direction", "raw": direction.group(0)[-80:]}
    hearing = _HEARING_MOTION.search(text)
    if hearing:
        outcome = _normalize_outcome(hearing.group(1))
        if outcome:
            return {"outcome": outcome, "source": "hearing_record", "raw": hearing.group(1).strip()[:80]}
    if _NOT_DECISION.search(text) or not _COURT_ACT.search(text):
        return None
    structured = _STRUCTURED_MOTION_RESULT.search(text)
    if structured:
        result = structured.group(1) or structured.group(2) or ""
        outcome = _normalize_outcome(result) or ("granted" if re.search(r"this court orders|il est ordonné", result, re.IGNORECASE) else None)
        if outcome:
            return {"outcome": outcome, "source": "structured_result", "raw": result.strip()[:80]}
    if _LEAVE_ORDER.search(text) and not re.search(r"\b(?:motion|requ[êe]te)\b", text[:200], re.IGNORECASE):
        return None
    verb = re.search(
        r"\b(granting|dismissing|allowing|refusing|accordant|rejetant|accueillant)\b[^\n]{0,30}?\b(?:the\s+|la\s+|le\s+|respondent['’]s\s+|applicant['’]s\s+|motion\s+)?(motion|requ[êe]te|stay|sursis|demande de sursis|request|extension)"
        r"|\b(?:motion|requ[êe]te|stay|request)\s+(?:is|was|est)\s+(granted|dismissed|allowed|refused|accordée?|rejetée?|accueillie)"
        r"|\bla cour (?:accueille|rejette) la re\w*te|\bthe court (?:allows|grants|dismisses) the (?:motion|request)"
        r"|\b(?:granting|dismissing|accordant|rejetant)\s+(?:the\s+)?(?:applicant['’]s|respondent['’]s|a['’]s|r['’]s)?\s*informal\s+(?:request|motion)"
        r"|\b(?:accordant|rejetant)\s+(?:les?\s+|la\s+)?(?:deux\s+)?demandes?\s+de\s+prorogation",
        text,
        re.IGNORECASE,
    )
    if verb:
        raw = verb.group(0)
        return {"outcome": _normalize_outcome(raw.replace("motion", "")), "source": "order_text", "raw": raw[:80]}
    if _MOTION_DOC_REF.search(text):
        # "granting the Application for Judicial Review on Consent (Motion Doc. No. 7)"
        anywhere = re.search(r"\b(granting|allowing|dismissing|refusing|accordant|accueillant|rejetant)\b", text, re.IGNORECASE)
        if anywhere:
            return {"outcome": _normalize_outcome(anywhere.group(1)), "source": "order_with_motion_reference", "raw": anywhere.group(0)}
    if _IMPLICIT_GRANT.search(text):
        return {"outcome": "granted", "source": "implicit_order", "raw": _IMPLICIT_GRANT.search(text).group(0)}
    return None


def extract_motions(events: Iterable[Any]) -> dict[str, Any]:
    events = [event for event in events]
    motions: list[dict[str, Any]] = []
    by_doc: dict[str, dict[str, Any]] = {}
    for event in events:
        if not _MOTION_FILING.search(event.text):
            continue
        relief = _motion_relief(event.text)
        number = re.fullmatch(r"\s*(\d+)(?:\.0+)?\s*", str(event.docno or ""))
        doc_number = number.group(1) if number else None
        if doc_number and doc_number in by_doc:
            by_doc[doc_number]["amended"] = True
            continue
        motion = {
            "doc_number": doc_number,
            "filed_date": _event_date(event),
            "filed_doc_id": event.doc_id,
            "filer": _motion_filer(event.text),
            "type": motion_type(relief) if motion_type(relief) != "other" else motion_type(event.text),
            "relief": relief,
            "in_writing": bool(re.search(r"in writing|par écrit|rule 369|règle 369|by (?:way of )?letter|par voie de lettre", event.text, re.IGNORECASE)),
            "outcome": "pending_or_unknown",
            "decision_date": None,
            "decision_doc_id": None,
            "decision_text": None,
            "judge": None,
            "link": None,
            "days_to_decision": None,
            "interim_results": [],
        }
        motion["entry_id"] = str(event.re_no) if getattr(event, "re_no", None) not in (None, "") else None
        motions.append(motion)
        if doc_number:
            by_doc[doc_number] = motion
    by_entry = {motion["entry_id"]: motion for motion in motions if motion.get("entry_id")}
    unlinked: list[dict[str, Any]] = []
    for event in events:
        if _MOTION_FILING.search(event.text):
            continue
        withdrawn = _WITHDRAWN_MOTION.search(event.text)
        if withdrawn and re.search(r"\b(?:if|unless|whether|si)\b[^.]{0,40}$", event.text[: withdrawn.start()], re.IGNORECASE):
            withdrawn = None  # "out of time ... if current motion is withdrawn" is not a withdrawal
        ruling = {"outcome": "withdrawn", "source": "withdrawal", "raw": withdrawn.group(0)} if withdrawn else _decision_on_motion(event.text)
        if ruling is None and not _NOT_DECISION.search(event.text) and _COURT_ACT.search(event.text) and re.search(
            r"granting the application for (?:leave and )?(?:for )?judicial review|allowing the application|accordant la demande de contrôle judiciaire", event.text, re.IGNORECASE
        ) and any(motion["type"] == "judgment_on_consent" and motion["outcome"] == "pending_or_unknown" for motion in motions):
            ruling = {"outcome": "granted", "source": "judgment_granting_review", "raw": "judgment granting the application"}
        if not ruling or not ruling.get("outcome"):
            continue
        reference = _MOTION_DOC_REF.search(event.text)
        reference_number = next((group for group in reference.groups() if group), None) if reference else None
        when = event.doc_date.isoformat() if event.doc_date else None
        target, link = None, None
        entry_reference = _ENTRY_ID_REF.search(event.text)
        entry_number = next((group for group in entry_reference.groups() if group), None) if entry_reference else None
        if reference_number and reference_number in by_doc:
            target, link = by_doc[reference_number], "doc_number"
        elif entry_number and entry_number in by_entry:
            target, link = by_entry[entry_number], "entry_id"
        else:
            hint = motion_type(event.text)
            open_motions = [
                motion
                for motion in motions
                if motion["outcome"] in {"pending_or_unknown", "reserved", "adjourned"}
                and (not when or not motion["filed_date"] or motion["filed_date"] <= when)
            ]
            if re.search(r"(?:application|demande) (?:for an |de )(?:extension of time|prorogation de délai)\s+\d", event.text, re.IGNORECASE):
                hint = "other"  # generic old wording, not an extension-of-time ruling
            same_type = [motion for motion in open_motions if hint != "other" and _same_family(motion["type"], hint)]
            if not same_type and re.search(r"granting the application for (?:leave and )?(?:for )?judicial review|allowing the application|referring the matter back|accordant la demande de contrôle", event.text, re.IGNORECASE):
                same_type = [motion for motion in open_motions if motion["type"] == "judgment_on_consent"]
            if same_type:
                target, link = same_type[-1], "same_type_open_motion"
            elif len(open_motions) == 1 and not reference_number and (hint == "other" or open_motions[0]["type"] in {hint, "other"}):
                target, link = open_motions[0], "only_open_motion"
        judge = _helpers()._clean_judge_name(_helpers()._judge_name(event.text))
        if target is None and ruling["source"] != "withdrawal":
            # The formal order often follows the hearing record that already announced the result.
            hint = motion_type(event.text)
            def gap(motion: dict[str, Any]) -> int:
                days = _days_between(motion["decision_date"], when) if motion["decision_date"] and when else None
                return 99 if days is None else days

            confirmed = [
                motion
                for motion in motions
                if gap(motion) <= 45
                and (
                    (reference_number and motion["doc_number"] == reference_number)
                    or (_same_family(motion["type"], hint) and (motion["outcome"] == ruling["outcome"] or gap(motion) <= 7))
                    or (len(motions) == 1 and motion["outcome"] == ruling["outcome"])
                )
            ]
            if confirmed:
                motion = confirmed[-1]
                motion["order_doc_id"] = event.doc_id
                motion["order_outcome"] = ruling["outcome"]
                if judge and not motion["judge"]:
                    motion["judge"] = judge
                if ruling["outcome"] != motion["outcome"] and ruling["outcome"] not in {"reserved", "adjourned"}:
                    motion["conflict"] = f"hearing record {motion['outcome']} but order {ruling['outcome']}"
                    motion["outcome"] = ruling["outcome"]
                continue
        if target is None and ruling["source"] == "implicit_order":
            continue
        if target is None:
            if ruling["outcome"] in {"reserved", "adjourned", "withdrawn"}:
                unlinked.append({"doc_id": event.doc_id, "date": when, "outcome": ruling["outcome"], "type": motion_type(event.text), "judge": judge, "reference": reference_number, "source": ruling["source"]})
                continue
            # A ruling with no filed motion behind it: oral motions, informal requests, filings missing from the registry.
            motion = {
                "doc_number": reference_number,
                "filed_date": None,
                "filed_doc_id": None,
                "filer": _motion_filer(event.text),
                "type": motion_type(event.text),
                "relief": event.text[:240],
                "in_writing": None,
                "outcome": ruling["outcome"],
                "decision_date": when,
                "decision_doc_id": event.doc_id,
                "decision_text": event.text[:400],
                "judge": judge,
                "link": "ruling_without_filing",
                "decision_source": ruling["source"],
                "days_to_decision": None,
                "interim_results": [],
            }
            motions.append(motion)
            if reference_number:
                by_doc.setdefault(reference_number, motion)
            continue
        if ruling["outcome"] in {"reserved", "adjourned"}:
            target["interim_results"].append({"date": when, "outcome": ruling["outcome"], "doc_id": event.doc_id})
            if target["outcome"] == "pending_or_unknown":
                target["outcome"] = ruling["outcome"]
            if judge and not target["judge"]:
                target["judge"] = judge
            continue
        if target["outcome"] not in {"pending_or_unknown", "reserved", "adjourned"}:
            continue  # first final ruling wins; later entries are reasons, corrections or duplicates
        target.update(
            {
                "outcome": ruling["outcome"],
                "decision_date": when,
                "decision_doc_id": event.doc_id,
                "decision_text": event.text[:400],
                "judge": judge or target["judge"],
                "link": link,
                "decision_source": ruling["source"],
                "days_to_decision": _days_between(target["filed_date"], when),
            }
        )
    removed = [event for event in events if re.search(r"hearing removed from|removed from (?:the )?(?:general sitting|list)|audition retirée du rôle|retirée? du rôle", event.text, re.IGNORECASE)]
    last_date = max((event.doc_date.isoformat() for event in events if event.doc_date), default=None)
    closing = next((event for event in events if re.search(r"notice of discontinuance|avis de désistement|\(final decision\)|\(décision finale\)", event.text, re.IGNORECASE)), None)
    for motion in motions:
        if motion["outcome"] != "pending_or_unknown":
            continue
        reference = motion.get("doc_number")
        if reference and any(re.search(rf"(?:motion|requ[êe]te)\s*(?:doc\.?\s*)?(?:no\.?\s*|#\s*)?{reference}\b", event.text, re.IGNORECASE) for event in removed):
            motion["outcome"] = "removed_from_list"
        elif closing is not None and closing.doc_date and motion["filed_date"] and closing.doc_date.isoformat() >= motion["filed_date"]:
            motion["outcome"] = "not_ruled_case_closed"
        elif last_date and motion["filed_date"] and last_date == motion["filed_date"]:
            motion["outcome"] = "pending_at_last_entry"
    decided = [motion for motion in motions if motion["outcome"] not in {"pending_or_unknown", "reserved", "adjourned", "removed_from_list", "not_ruled_case_closed", "pending_at_last_entry"}]
    by_type: dict[str, Counter[str]] = {}
    for motion in motions:
        by_type.setdefault(motion["type"], Counter())[motion["outcome"]] += 1
    return {
        "count": len(motions),
        "decided": len(decided),
        "motions": motions,
        "unlinked_rulings": unlinked,
        "by_type": {name: dict(counts) for name, counts in by_type.items()},
    }
