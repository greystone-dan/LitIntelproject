import calendar
from datetime import date, datetime, timedelta, timezone
from typing import Any, Dict, List, Optional


def _one_line(text: Optional[str]) -> str:
    if not text:
        return ""
    line = " ".join(text.split())
    if len(line) > 240:
        return line[:237] + "..."
    return line


def _pick_outcome(outcomes: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    if not outcomes:
        return None
    mainline = [o for o in outcomes if (o.get("source") or "").startswith("deterministic")]
    candidates = mainline or outcomes
    return max(
        candidates,
        key=lambda o: str(o.get("updated_at") or o.get("created_at") or ""),
    )


def _parse_datetime(value: Any) -> Optional[datetime]:
    if isinstance(value, datetime):
        parsed = value
    elif isinstance(value, str):
        try:
            parsed = datetime.fromisoformat(value)
        except ValueError:
            return None
    else:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _shift_months(value: date, months: int) -> date:
    absolute_month = value.year * 12 + value.month - 1 - months
    year, month_index = divmod(absolute_month, 12)
    month = month_index + 1
    return date(year, month, min(value.day, calendar.monthrange(year, month)[1]))


def _date_windows(as_of: datetime) -> tuple[date, date, date, date]:
    end = as_of.date() + timedelta(days=1)
    latest_start = _shift_months(as_of.date(), 12)
    previous_start = _shift_months(as_of.date(), 24)
    return previous_start, latest_start, latest_start, end


def _date_in_window(value: Any, start: date, end: date) -> bool:
    if isinstance(value, datetime):
        value = value.date()
    elif isinstance(value, str):
        try:
            value = date.fromisoformat(value[:10])
        except ValueError:
            return False
    return isinstance(value, date) and start <= value < end


# NOTE: avoid importing SQLAlchemy/database objects at module import time so this module
# can be imported in offline/test contexts without initializing DB engine.


def _resolve_reason_from_alert(alert_row: Any) -> str:
    """Derive a terse reason string from a SearchAlert row or fixture alert dict.

    Preference: use match_type and optionally relevance_score.
    """
    if not alert_row:
        return "Matched saved search criteria"
    match_type = getattr(alert_row, 'match_type', None) or (alert_row.get('match_type') if isinstance(alert_row, dict) else None)
    score = getattr(alert_row, 'relevance_score', None) if not isinstance(alert_row, dict) else alert_row.get('relevance_score')
    if match_type:
        if score is not None:
            try:
                s = float(score)
                return f"{_one_line(str(match_type))} (score: {s:.2f})"
            except Exception:
                return _one_line(str(match_type))
        return _one_line(str(match_type))
    return "Matched saved search criteria"


def compute_alerts_for_search(db_session, search_id: int, since: Optional[datetime] = None, limit: int = 200) -> Dict[str, Any]:
    """Compute alerts for a saved search against a live DB session.

    This function performs validation of the saved search (404-style semantics are left
    to the caller; here it raises ValueError to indicate missing search).
    Returns dict with search_id, new_case_matches and authority_watch.
    """
    # Local imports to avoid SQLAlchemy at module import
    from .database import SavedSearch, SearchAlert, Case, CaseOutcome, Citation

    # validate saved search exists
    saved = db_session.query(SavedSearch).filter(SavedSearch.id == search_id).first()
    if not saved:
        raise ValueError("Saved search not found")

    alerts_q = db_session.query(SearchAlert).filter(SearchAlert.search_id == search_id)
    if since:
        normalized_since = _parse_datetime(since)
        if normalized_since is None:
            raise ValueError("Invalid since parameter")
        alerts_q = alerts_q.filter(SearchAlert.discovered_at > normalized_since)
    alerts = alerts_q.order_by(SearchAlert.discovered_at.desc()).limit(limit).all()

    # Deduplicate alerts to preserve one result per matching decision safely.
    # We collapse multiple alerts for the same case by taking the most recent discovered_at.
    alerts_by_case = {}
    for a in alerts:
        cur = alerts_by_case.get(a.case_id)
        if not cur or getattr(a, 'discovered_at', None) and getattr(cur, 'discovered_at', None) and a.discovered_at > cur.discovered_at:
            alerts_by_case[a.case_id] = a
    unique_alerts = list(alerts_by_case.values())

    new_case_matches = []
    case_ids = [a.case_id for a in unique_alerts]

    if case_ids:
        cases = {c.id: c for c in db_session.query(Case).filter(Case.id.in_(case_ids)).all()}
        outcomes_rows = db_session.query(CaseOutcome).filter(CaseOutcome.case_id.in_(case_ids)).all()
        outcomes_by_case = {}
        for o in outcomes_rows:
            outcomes_by_case.setdefault(o.case_id, []).append({
                "decision_outcome": o.decision_outcome,
                "government_outcome": o.government_outcome,
                "disposition_evidence": o.disposition_evidence,
                "classifier_version": o.classifier_version,
                "source": o.source,
                "confidence": getattr(o, 'confidence', None),
                "created_at": getattr(o, 'created_at', None),
                "updated_at": getattr(o, 'updated_at', None),
            })

        for alert in unique_alerts:
            case = cases.get(alert.case_id)
            chosen = _pick_outcome(outcomes_by_case.get(alert.case_id, []))
            reason = _resolve_reason_from_alert(alert)
            new_case_matches.append({
                "case_id": alert.case_id,
                "case_title": getattr(case, 'title', None) if case else None,
                "case_citation": getattr(case, 'citation', None) if case else None,
                "case_date": getattr(case, 'date', None) if case else None,
                "outcome": chosen,
                "reason": reason,
                "discovered_at": getattr(alert, 'discovered_at', None),
            })

    # Authority watch: use resolved case-to-case citation targets from result cases,
    # then count all distinct decisions citing those targets in the two date windows.
    authority_watch = {}
    if case_ids:
        citations = (
            db_session.query(Citation)
            .filter(
                Citation.source_case_id.in_(case_ids),
                Citation.target_case_id.isnot(None),
                Citation.citation_kind != "statute",
            )
            .all()
        )
        authority_ids = sorted({c.target_case_id for c in citations if c.target_case_id})
        now = datetime.now(timezone.utc)
        previous_start, previous_end, latest_start, latest_end = _date_windows(now)
        authorities = {
            c.id: c
            for c in db_session.query(Case).filter(Case.id.in_(authority_ids)).all()
        } if authority_ids else {}
        citation_rows = []
        if authority_ids:
            citation_rows = (
                db_session.query(Citation.target_case_id, Citation.source_case_id)
                .join(Case, Case.id == Citation.source_case_id)
                .filter(
                    Citation.target_case_id.in_(authority_ids),
                    Citation.citation_kind != "statute",
                    Case.date >= previous_start,
                    Case.date < latest_end,
                )
                .all()
            )
        citing_by_authority: Dict[int, set[int]] = {}
        for authority_id, source_case_id in citation_rows:
            if authority_id is not None and source_case_id is not None:
                citing_by_authority.setdefault(authority_id, set()).add(source_case_id)
        all_citing_ids = sorted(
            {case_id for ids in citing_by_authority.values() for case_id in ids}
        )
        citing_cases = {
            c.id: c
            for c in db_session.query(Case).filter(Case.id.in_(all_citing_ids)).all()
        } if all_citing_ids else {}
        outcomes_by_case: Dict[int, List[Dict[str, Any]]] = {}
        if all_citing_ids:
            for outcome in db_session.query(CaseOutcome).filter(
                CaseOutcome.case_id.in_(all_citing_ids)
            ).all():
                outcomes_by_case.setdefault(outcome.case_id, []).append({
                    "government_outcome": outcome.government_outcome,
                    "source": outcome.source,
                    "created_at": getattr(outcome, "created_at", None),
                    "updated_at": getattr(outcome, "updated_at", None),
                })
        for auth in authority_ids:
            selected_ids = [
                case_id
                for case_id in citing_by_authority.get(auth, set())
                if case_id in citing_cases
                and _date_in_window(citing_cases[case_id].date, latest_start, latest_end)
            ]
            previous_ids = [
                case_id
                for case_id in citing_by_authority.get(auth, set())
                if case_id in citing_cases
                and _date_in_window(citing_cases[case_id].date, previous_start, previous_end)
            ]

            def _counts(source_ids: List[int]) -> tuple[int, int]:
                numerator = sum(
                    1
                    for case_id in source_ids
                    if (
                        (_pick_outcome(outcomes_by_case.get(case_id, [])) or {})
                        .get("government_outcome")
                        or ""
                    ).lower() == "lost"
                )
                return numerator, len(source_ids)

            latest_n, latest_d = _counts(selected_ids)
            prev_n, prev_d = _counts(previous_ids)
            suppressed = (latest_d < 8) or (prev_d < 8)
            entry = {
                "authority_id": auth,
                "title": getattr(authorities.get(auth), "title", None),
                "citation": getattr(authorities.get(auth), "citation", None),
                "latest": {"numerator": latest_n, "denominator": latest_d},
                "previous": {"numerator": prev_n, "denominator": prev_d},
                "comparison_suppressed": bool(suppressed),
            }
            if not suppressed:
                entry['latest']['proportion'] = (latest_n / latest_d) if latest_d else None
                entry['previous']['proportion'] = (prev_n / prev_d) if prev_d else None
            authority_watch[str(auth)] = entry

    return {"search_id": search_id, "new_case_matches": new_case_matches, "authority_watch": authority_watch}


# Lightweight fixture-oriented helper (pure)

def compute_alerts_from_fixture(saved_search: Dict[str, Any], cases: List[Dict[str, Any]], outcomes: List[Dict[str, Any]], since: Optional[str] = None, as_of: Optional[str] = None) -> Dict[str, Any]:
    """Pure function for tests and offline script.

    saved_search: dict with id,name
    cases include matching result decisions plus corpus citing decisions, with resolved
    Citation-like entries in ``citations`` (each has ``target_case_id``).
    outcomes include case_id, government_outcome, source, and optional evidence/timestamps.
    saved_search.alerts contains fixture rows with case_id, match_type, relevance_score,
    and discovered_at.
    as_of: ISO datetime string to deterministically control 'now' for windowing in tests
    """
    since_dt = _parse_datetime(since) if since else None
    if since and since_dt is None:
        raise ValueError("Invalid since parameter")
    as_of_dt = _parse_datetime(as_of) if as_of else None
    if as_of and as_of_dt is None:
        raise ValueError("Invalid as_of parameter")
    now = as_of_dt or datetime.now(timezone.utc)
    matched = []
    cases_by_id = {c['id']: c for c in cases}
    outcomes_by_case = {}
    for o in outcomes:
        outcomes_by_case.setdefault(o['case_id'], []).append(o)

    alerts_fixture = saved_search.get('alerts') if isinstance(saved_search, dict) else None
    alerts_rows = []
    for alert in alerts_fixture or []:
        discovered = _parse_datetime(alert.get('discovered_at'))
        if since_dt and (discovered is None or discovered <= since_dt):
            continue
        alerts_rows.append(alert)

    # dedupe by case_id keeping most recent discovered_at
    alerts_by_case = {}
    for a in alerts_rows:
        cid = a.get('case_id')
        cur = alerts_by_case.get(cid)
        cur_dt = _parse_datetime(cur.get('discovered_at')) if cur else None
        a_dt = _parse_datetime(a.get('discovered_at'))
        if not cur or (a_dt and cur_dt and a_dt > cur_dt) or (a_dt and not cur_dt):
            alerts_by_case[cid] = a

    unique_alerts = list(alerts_by_case.values())

    for alert in unique_alerts:
        c = cases_by_id.get(alert['case_id'])
        outs = outcomes_by_case.get(alert['case_id'], [])
        chosen = None
        if outs:
            det = [o for o in outs if (o.get('source') or '').startswith('deterministic')]
            chosen = det[0] if det else sorted(outs, key=lambda x: x.get('updated_at') or x.get('created_at') or '', reverse=True)[0]
        reason = _resolve_reason_from_alert(alert)
        matched.append({
            'case_id': alert['case_id'],
            'case_title': c.get('title') if c else None,
            'case_citation': c.get('citation') if c else None,
            'case_date': c.get('date') if c else None,
            'outcome': chosen,
            'reason': reason,
            'created_at': alert.get('discovered_at')
        })

    # Authority trends use all citing decisions in the corpus, including result cases.
    previous_start, previous_end, latest_start, latest_end = _date_windows(now)
    authority_watch = {}
    auth_map: Dict[Any, set[int]] = {}
    for alert in unique_alerts:
        cid = alert.get('case_id')
        c = cases_by_id.get(cid)
        if not c:
            continue
        for citation in c.get('citations') or []:
            if citation.get('citation_kind') == 'statute':
                continue
            target = citation.get('target_case_id')
            if target is not None:
                auth_map.setdefault(target, set())

    for auth in auth_map:
        citing_ids = set()
        for case in cases:
            for citation in case.get('citations') or []:
                if citation.get('citation_kind') != 'statute' and citation.get('target_case_id') == auth:
                    citing_ids.add(case['id'])
                    break
        latest_ids = [
            case_id for case_id in citing_ids
            if case_id in cases_by_id
            and _date_in_window(cases_by_id[case_id].get('date'), latest_start, latest_end)
        ]
        previous_ids = [
            case_id for case_id in citing_ids
            if case_id in cases_by_id
            and _date_in_window(cases_by_id[case_id].get('date'), previous_start, previous_end)
        ]
        latest_n, latest_d = _fixture_counts(latest_ids, outcomes_by_case)
        prev_n, prev_d = _fixture_counts(previous_ids, outcomes_by_case)
        suppressed = (latest_d < 8) or (prev_d < 8)
        authority_case = cases_by_id.get(auth, {})
        entry = {
            'authority_id': auth,
            'title': authority_case.get('title'),
            'citation': authority_case.get('citation'),
            'latest': {'numerator': latest_n, 'denominator': latest_d},
            'previous': {'numerator': prev_n, 'denominator': prev_d},
            'comparison_suppressed': bool(suppressed),
        }
        if not suppressed:
            entry['latest']['proportion'] = (latest_n / latest_d) if latest_d else None
            entry['previous']['proportion'] = (prev_n / prev_d) if prev_d else None
        authority_watch[str(auth)] = entry

    return {'search_id': saved_search.get('id'), 'new_case_matches': matched, 'authority_watch': authority_watch}


def _fixture_counts(
    case_ids: List[int], outcomes_by_case: Dict[int, List[Dict[str, Any]]]
) -> tuple[int, int]:
    numerator = sum(
        1
        for case_id in case_ids
        if (
            (_pick_outcome(outcomes_by_case.get(case_id, [])) or {}).get(
                "government_outcome"
            )
            or ""
        ).lower()
        == "lost"
    )
    return numerator, len(set(case_ids))
