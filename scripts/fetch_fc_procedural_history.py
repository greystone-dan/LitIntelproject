"""
Fetch Federal Court procedural history for a list of IMM numbers.

Hits two FC API endpoints per IMM number:
  - proceedingQueriesCourtNumberList  → style of cause
  - proceedingQueriesRE               → all DOC_DT / RECORDED_ENTRY events

Parses leave decision, JR decision, case status, judge, and full activity text
using the same priority-based logic as the VBA original.

Results are upserted into the fc_procedural_history table, tagged by IMM number.

Input sources (choose one or more):
  --imm-numbers  IMM-1234-19 IMM-5678-20   (space-separated on command line)
  --imm-file FILE                            CSV/text file, one IMM per line or 'imm_number' column
  --from-prototype                           Pull IMM numbers from prototype cohort (source_id field)

Options:
  --update       Re-fetch and overwrite entries that already exist
    --delay-ms     Milliseconds between requests (default 2000)
    --diagnostic-allow-sub-2000ms-delay
                                 Explicitly allow a faster diagnostic probe; never use for routine collection
  --dry-run      Parse and print without writing to DB
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import re
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import httpx
from bs4 import BeautifulSoup

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import select

from backend.database import (
    Case,
    FCActivityCase,
    FCActivityDocument,
    FCProceduralHistory,
    SessionLocal,
)

# ---------------------------------------------------------------------------
# FC API endpoints
# ---------------------------------------------------------------------------

FC_META_URL = (
    "https://www.fct-cf.ca/CourtFilesAndDecisions/"
    "proceedingQueriesCourtNumberList?division=t&courtnumber={imm}"
)
FC_RE_URL = (
    "https://www.fct-cf.ca/CourtFilesAndDecisions/"
    "proceedingQueriesRE?division={imm}&courtnumber={imm}"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-CA,en;q=0.9",
    "Referer": "https://www.fct-cf.ca/",
}

MIN_DELAY_MS = 2000
LOG_HANDLE = None


def log_print(*args: Any, **kwargs: Any) -> None:
    kwargs.setdefault("flush", True)
    print(*args, **kwargs)
    if LOG_HANDLE is not None:
        log_kwargs = dict(kwargs)
        log_kwargs["file"] = LOG_HANDLE
        log_kwargs["flush"] = True
        print(*args, **log_kwargs)


class RequestBudget:
    def __init__(self, maximum: int) -> None:
        if maximum < 1:
            raise ValueError("request budget must be at least 1")
        self.maximum = maximum
        self.used = 0

    def spend(self) -> None:
        if self.used >= self.maximum:
            raise RuntimeError(f"request budget exhausted ({self.maximum})")
        self.used += 1


def validate_delay_ms(delay_ms: int, allow_sub_floor: bool = False) -> None:
    if delay_ms < MIN_DELAY_MS and not allow_sub_floor:
        raise ValueError(f"--delay-ms must be at least {MIN_DELAY_MS} ms")


def wait_between_candidates(delay_ms: int, jitter_ms: int) -> None:
    if jitter_ms < 0:
        raise ValueError("--jitter-ms must be non-negative")
    time.sleep((delay_ms + random.randint(0, jitter_ms)) / 1000)


def adaptive_backoff_delay_ms(current_delay_ms: int, factor: float, maximum_ms: int) -> int:
    if current_delay_ms < 0 or factor <= 1 or maximum_ms < current_delay_ms:
        raise ValueError("invalid adaptive delay parameters")
    return min(maximum_ms, max(current_delay_ms + 1, int(current_delay_ms * factor)))

# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

def http_get(
    client: httpx.Client,
    url: str,
    retries: int = 3,
    delay: float = 1.0,
    request_budget: RequestBudget | None = None,
) -> str:
    last_err: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            if request_budget is not None:
                request_budget.spend()
            resp = client.get(url, timeout=20)
            if resp.status_code == 200:
                return resp.text
            raise RuntimeError(f"HTTP {resp.status_code}")
        except Exception as exc:
            last_err = exc
            if attempt < retries:
                time.sleep(delay * attempt)
    raise RuntimeError(f"Failed after {retries} attempts: {last_err}")

# ---------------------------------------------------------------------------
# JSON field extraction (mirrors VBA GetJsonValue)
# ---------------------------------------------------------------------------

def get_json_value(json_text: str, field: str) -> str:
    """Extract first string value for a field from the FC API response structure."""
    try:
        outer = json.loads(json_text)
        data = outer.get("data") if isinstance(outer, dict) else outer
        if isinstance(data, list) and data and isinstance(data[0], dict):
            val = data[0].get(field)
            return str(val) if val is not None else ""
        if isinstance(outer, dict):
            val = outer.get(field)
            return str(val) if val is not None else ""
    except Exception:
        pass
    # Fallback: regex string search
    pattern = rf'"{re.escape(field)}"\s*:\s*"([^"]*)"'
    m = re.search(pattern, json_text)
    return m.group(1) if m else ""

# ---------------------------------------------------------------------------
# Parse all DOC_DT + RECORDED_ENTRY pairs (mirrors VBA ParseAllEntries)
# ---------------------------------------------------------------------------

def parse_all_entries(re_text: str) -> list[dict[str, str]]:
    """Return list of {date, entry} dicts parsed from the RE JSON response."""
    entries: list[dict[str, str]] = []
    try:
        outer = json.loads(re_text)
        # FC API wraps results as {"Count": N, "data": [...]}
        data = outer.get("data") if isinstance(outer, dict) else outer
        if not isinstance(data, list):
            data = [data]
        for item in data:
            if not isinstance(item, dict):
                continue
            raw_date = item.get("DOC_DT", "") or ""
            entry_text = item.get("RECORDED_ENTRY", "") or ""
            entries.append({
                "date": _clean_date(str(raw_date)),
                "entry": str(entry_text).strip(),
                "re_no": str(item.get("RE_NO") or item.get("RENO") or "").strip(),
                "docno": str(item.get("DOCNO") or item.get("DOC_NO") or "").strip(),
            })
    except Exception:
        # Fallback: regex extraction (same as VBA)
        for m_date, m_entry in re.findall(
            r'"DOC_DT"\s*:\s*"([^"]*)".*?"RECORDED_ENTRY"\s*:\s*"([^"]*)"',
            re_text,
            re.DOTALL,
        ):
            entries.append({"date": _clean_date(m_date), "entry": m_entry.strip(), "re_no": "", "docno": ""})
    return [e for e in entries if e["entry"]]  # drop header rows with no entry text


def _clean_date(s: str) -> str:
    s = s.strip()
    if not s:
        return ""
    # Handle .NET /Date(timestamp)/ format
    net_m = re.match(r"/Date\((\d+)\)/", s)
    if net_m:
        import datetime as _dt
        ts = int(net_m.group(1)) / 1000
        return _dt.datetime.utcfromtimestamp(ts).date().isoformat()
    if "T" in s:
        s = s.split("T")[0]
    try:
        d = datetime.strptime(s, "%Y-%m-%d").date()
        return d.isoformat()
    except ValueError:
        pass
    for fmt in ("%Y/%m/%d", "%d-%m-%Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            pass
    return ""


def _norm(s: str) -> str:
    """Normalize entry text for matching (mirrors VBA NormalizeEntry)."""
    return " ".join(s.lower().split())

# ---------------------------------------------------------------------------
# Leave decision extraction (mirrors VBA ExtractLeaveInfoFromArrays)
# ---------------------------------------------------------------------------

def extract_leave(entries: list[dict[str, str]]) -> tuple[str, str]:
    decision = "Pending"
    best_date = date(1900, 1, 1)
    leave_date = ""

    for item in entries:
        e = _norm(item["entry"])
        d_str = item["date"]
        d = _parse_date(d_str)

        if (
            "dismissing the application for leave" in e
            or "leave dismissed" in e
            or "result - leave dismissed" in e
            or "result: leave dismissed" in e
        ):
            if d and d >= best_date:
                best_date = d
                decision = "Dismissed"
                leave_date = d_str
            elif not d:
                decision = "Dismissed"

        if (
            "leave granted" in e
            or "result - leave granted" in e
            or "result: leave granted" in e
            or "granting the application for leave" in e
        ):
            if d and d >= best_date:
                best_date = d
                decision = "Granted"
                leave_date = d_str
            elif not d and decision != "Dismissed":
                decision = "Granted"

    return decision, leave_date

# ---------------------------------------------------------------------------
# JR decision extraction (mirrors VBA ExtractJRInfoFromArrays, priority-based)
# ---------------------------------------------------------------------------

def extract_jr(entries: list[dict[str, str]]) -> tuple[str, str]:
    jr_decision = "N/A"
    jr_date = ""
    best_priority = 0

    for item in entries:
        e = _norm(item["entry"])
        d_str = item["date"]

        # Priority 200 — explicit leave dismissal (overrides everything)
        if (
            "dismissing the application for leave" in e
            or "leave dismissed" in e
            or "result - leave dismissed" in e
            or "result: leave dismissed" in e
        ):
            if 200 > best_priority:
                best_priority = 200
                jr_decision = "N/A"
                jr_date = d_str

        # Priority 180 — discontinuance
        elif "notice of discontinuance" in e or "discontinued" in e:
            if 180 > best_priority:
                best_priority = 180
                jr_decision = "Discontinued"
                jr_date = d_str

        # Priority 170 — consent judgment
        elif "consent judgment" in e or "granted on consent" in e:
            if 170 > best_priority:
                best_priority = 170
                jr_decision = "JR Granted (Consent)"
                jr_date = d_str

        # Priority 160 — explicit granted/dismissed
        elif (
            "application granted" in e
            or "result - granted" in e
            or "result: granted" in e
            or "granting the application for judicial review" in e
        ):
            if 160 > best_priority:
                best_priority = 160
                jr_decision = "JR Granted"
                jr_date = d_str

        elif (
            "application dismissed" in e
            or "result - dismissed" in e
            or "result: dismissed" in e
            or "dismissing the application for judicial review" in e
        ):
            if 160 > best_priority:
                best_priority = 160
                jr_decision = "JR Dismissed"
                jr_date = d_str

        # Priority 150 — generic reasons/judgment
        elif (
            "reasons for judgment" in e
            or "(final decision)" in e
            or ("judgment" in e and "reasons" in e)
        ):
            if 150 > best_priority:
                best_priority = 150
                jr_decision = "JR Granted"
                jr_date = d_str

    return jr_decision, jr_date

# ---------------------------------------------------------------------------
# Resolve leave vs JR conflicts (mirrors VBA ResolveLeaveAndNormalizeDates)
# ---------------------------------------------------------------------------

def resolve_leave_jr(
    leave_decision: str,
    leave_date: str,
    jr_decision: str,
    jr_date: str,
) -> tuple[str, str, str, str, bool]:
    conflict = False

    if leave_decision in ("Dismissed", "Granted"):
        if leave_decision == "Dismissed" and jr_decision in ("JR Granted", "JR Granted (Consent)"):
            jr_decision = "N/A"
            jr_date = ""
            conflict = True
        return leave_decision, leave_date, jr_decision, jr_date, conflict

    # Infer leave from JR outcome
    if jr_decision in ("JR Granted", "JR Granted (Consent)", "JR Dismissed"):
        leave_decision = "Granted"
        if not leave_date:
            leave_date = jr_date
    elif jr_decision == "Discontinued":
        leave_decision = "N/A"
        leave_date = ""
    else:
        if not leave_decision:
            leave_decision = "Pending"

    return leave_decision, leave_date, jr_decision, jr_date, conflict

# ---------------------------------------------------------------------------
# Case status derivation (mirrors VBA DetermineCaseStatus)
# ---------------------------------------------------------------------------

def determine_case_status(leave_decision: str, jr_decision: str) -> str:
    if jr_decision == "JR Granted":
        return "JR Granted"
    if jr_decision == "JR Granted (Consent)":
        return "JR Granted (Consent)"
    if jr_decision == "JR Dismissed":
        return "JR Dismissed"
    if jr_decision == "Discontinued":
        return "Discontinued"
    if leave_decision == "Dismissed":
        return "Leave Dismissed"
    if leave_decision == "Granted":
        return "JR Active"
    return "Awaiting Leave Decision"

# ---------------------------------------------------------------------------
# Judge extraction (mirrors VBA ExtractJudge)
# ---------------------------------------------------------------------------

def extract_judge(entries: list[dict[str, str]]) -> str:
    for item in entries:
        e = item["entry"]
        m = re.search(r"Justice\s+([A-Z][a-zA-Z\-]+)", e)
        if m:
            return f"Justice {m.group(1)}"
    return ""

# ---------------------------------------------------------------------------
# Build full activity text, reverse-chronological
# ---------------------------------------------------------------------------

def build_full_activity(entries: list[dict[str, str]]) -> tuple[str, str]:
    """Return (full_activity_text, latest_date_str)."""
    sorted_entries = sorted(
        entries,
        key=lambda x: x["date"] if x["date"] else "0000-00-00",
        reverse=True,
    )
    lines = [
        f"{item['date']} — {item['entry']}" if item["date"] else item["entry"]
        for item in sorted_entries
    ]
    dates = [item["date"] for item in entries if item["date"]]
    latest = max(dates) if dates else ""
    return "\n".join(lines), latest

# ---------------------------------------------------------------------------
# Process a single IMM number
# ---------------------------------------------------------------------------

def _parse_date(s: str) -> date | None:
    if not s:
        return None
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return None


def process_imm(
    client: httpx.Client,
    imm: str,
    request_budget: RequestBudget | None = None,
) -> dict[str, Any]:
    imm = imm.strip().upper()

    # Metadata
    meta_text = ""
    try:
        meta_text = http_get(client, FC_META_URL.format(imm=imm), request_budget=request_budget)
    except Exception as exc:
        log_print(f"  [warn] meta fetch failed for {imm}: {exc}")

    style_of_cause = get_json_value(meta_text, "STYLE_OF_CAUSE") if meta_text else ""

    # Record of events
    re_text = ""
    try:
        re_text = http_get(client, FC_RE_URL.format(imm=imm), request_budget=request_budget)
    except Exception as exc:
        log_print(f"  [warn] RE fetch failed for {imm}: {exc}")

    if not re_text:
        return {
            "imm_number": imm,
            "style_of_cause": style_of_cause or None,
            "judge": None,
            "leave_decision": "Pending",
            "leave_date": None,
            "jr_decision": "N/A",
            "jr_decision_date": None,
            "case_status": "Awaiting Leave Decision",
            "latest_activity_date": None,
            "full_activity_text": "No RE data",
            "entries_json": [],
            "conflict_flag": False,
            "fetched_at": datetime.now(timezone.utc),
            "error": "no_re_data",
        }

    entries = parse_all_entries(re_text)
    # Pull style_of_cause from RE data directly (it's on every row)
    if not style_of_cause and re_text:
        try:
            outer = json.loads(re_text)
            rows = outer.get("data") if isinstance(outer, dict) else outer
            if rows and isinstance(rows[0], dict):
                style_of_cause = rows[0].get("STYLE_OF_CAUSE", "") or ""
        except Exception:
            pass
    leave_decision, leave_date = extract_leave(entries)
    jr_decision, jr_date = extract_jr(entries)
    leave_decision, leave_date, jr_decision, jr_date, conflict = resolve_leave_jr(
        leave_decision, leave_date, jr_decision, jr_date
    )
    case_status = determine_case_status(leave_decision, jr_decision)
    judge = extract_judge(entries)
    full_activity, latest_date = build_full_activity(entries)

    return {
        "imm_number": imm,
        "style_of_cause": style_of_cause or None,
        "judge": judge or None,
        "leave_decision": leave_decision,
        "leave_date": _parse_date(leave_date),
        "jr_decision": jr_decision,
        "jr_decision_date": _parse_date(jr_date),
        "case_status": case_status,
        "latest_activity_date": _parse_date(latest_date),
        "full_activity_text": full_activity,
        "entries_json": entries,
        "conflict_flag": conflict,
        "fetched_at": datetime.now(timezone.utc),
    }

# ---------------------------------------------------------------------------
# DB upsert
# ---------------------------------------------------------------------------

def upsert_result(db, result: dict[str, Any]) -> None:
    existing = db.scalar(
        select(FCProceduralHistory).where(
            FCProceduralHistory.imm_number == result["imm_number"]
        )
    )
    if existing:
        for field, value in result.items():
            if field != "imm_number" and hasattr(existing, field):
                setattr(existing, field, value)
    else:
        row = FCProceduralHistory(**{k: v for k, v in result.items() if k != "error"})
        db.add(row)
    db.commit()


def _activity_hash(*parts: Any) -> str:
    payload = "|".join("" if part is None else str(part) for part in parts)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _activity_year(imm_number: str) -> int | None:
    suffix = imm_number.rsplit("-", 1)[-1]
    if not suffix.isdigit():
        return None
    value = int(suffix)
    return 2000 + value if value <= 50 else 1900 + value


def _json_safe(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: _json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    return value


def _activity_document_identity(re_no: str | None, docno: str | None) -> tuple[str, str] | None:
    if re_no is None or docno is None:
        return None
    return re_no, docno


def write_activity_result(db, result: dict[str, Any]) -> tuple[int | None, int]:
    """Upsert one endpoint result into the separate FC Activity tables."""
    imm_number = str(result.get("imm_number") or "").strip().upper()
    if not imm_number or result.get("error"):
        return None, 0

    year = _activity_year(imm_number)
    source_key = _activity_hash("fc-procedural-endpoint", imm_number)
    case = db.scalar(select(FCActivityCase).where(FCActivityCase.source_key == source_key))
    payload = _json_safe(result)
    if case is None:
        case = FCActivityCase(
            source_key=source_key,
            citation=None,
            year=year,
            case_name=result.get("style_of_cause"),
            date_filed=result.get("latest_activity_date"),
            scraped_timestamp=result.get("fetched_at"),
            raw_payload=payload,
        )
        db.add(case)
        db.flush()
    else:
        case.case_name = result.get("style_of_cause") or case.case_name
        case.year = year
        case.date_filed = result.get("latest_activity_date")
        case.scraped_timestamp = result.get("fetched_at")
        case.raw_payload = payload

    added = 0
    seen_identities: set[tuple[str, str]] = set()
    for entry in result.get("entries_json") or []:
        entry_text = str(entry.get("entry") or "").strip()
        entry_date = entry.get("date") or None
        re_no = str(entry.get("re_no") or "").strip() or None
        docno = str(entry.get("docno") or "").strip() or None
        if not entry_text and not entry_date:
            continue
        entry_hash = _activity_hash(imm_number, re_no, docno, entry_date, entry_text)
        identity = _activity_document_identity(re_no, docno)
        if identity is not None:
            if identity in seen_identities:
                continue
            seen_identities.add(identity)
            existing = db.scalar(
                select(FCActivityDocument).where(
                    FCActivityDocument.case_id == case.id,
                    FCActivityDocument.re_no == re_no,
                    FCActivityDocument.docno == docno,
                )
            )
            if existing is not None:
                continue
        existing = db.scalar(
            select(FCActivityDocument).where(
                FCActivityDocument.case_id == case.id,
                FCActivityDocument.entry_hash == entry_hash,
            )
        )
        if existing is not None:
            continue
        db.add(
            FCActivityDocument(
                case_id=case.id,
                re_no=re_no,
                docno=docno,
                doc_dt=_parse_date(entry_date) if entry_date else None,
                recorded_entry=entry_text or None,
                entry_hash=entry_hash,
                raw_document={"imm_number": imm_number, **entry},
            )
        )
        added += 1

    db.commit()
    return case.id, added

# ---------------------------------------------------------------------------
# Seed loading
# ---------------------------------------------------------------------------

def load_imm_from_file(path: Path) -> list[str]:
    imms: list[str] = []
    with path.open("r", encoding="utf-8", newline="") as fh:
        # Try CSV with header
        sample = fh.read(1024)
        fh.seek(0)
        if "," in sample or "\t" in sample:
            dialect = "excel-tab" if "\t" in sample else "excel"
            reader = csv.DictReader(fh, dialect=dialect)
            col = next(
                (h for h in (reader.fieldnames or []) if "imm" in h.lower()),
                (reader.fieldnames or [None])[0],
            )
            for row in reader:
                val = (row.get(col) or "").strip()
                if val:
                    imms.append(val)
        else:
            for line in fh:
                val = line.strip()
                if val and not val.startswith("#"):
                    imms.append(val)
    return imms


def load_imm_from_prototype() -> list[str]:
    """Extract IMM numbers from source_id field of prototype cohort cases."""
    proto_csv = PROJECT_ROOT / "data" / "eval" / "prototype_case_ids_v1.csv"
    if not proto_csv.exists():
        return []

    ids: list[int] = []
    with proto_csv.open("r", encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            raw = row.get("case_id", "").strip()
            if raw.isdigit():
                ids.append(int(raw))

    db = SessionLocal()
    try:
        imms: list[str] = []
        rows = db.scalars(select(Case).where(Case.id.in_(ids)))
        for case in rows:
            sid = (case.source_id or "").strip()
            if re.match(r"IMM-\d+-\d+", sid, re.IGNORECASE):
                imms.append(sid.upper())
        return sorted(set(imms))
    finally:
        db.close()

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = parser.add_argument_group("Input")
    src.add_argument("--imm-numbers", nargs="+", metavar="IMM", help="IMM numbers directly (e.g. IMM-1234-19)")
    src.add_argument("--imm-file", metavar="FILE", help="CSV or text file with IMM numbers")
    src.add_argument("--from-prototype", action="store_true", help="Pull IMM numbers from prototype cohort source_id fields")
    src.add_argument("--generate-years", metavar="YEARS", help="Sweep all possible IMM numbers for given years, e.g. 23,24,25")
    src.add_argument("--max-imm", type=int, default=25000, metavar="N", help="Upper bound for --generate-years sweep (default 25000)")

    ctl = parser.add_argument_group("Options")
    ctl.add_argument("--update", action="store_true", help="Re-fetch and overwrite existing entries")
    ctl.add_argument("--reverse", action="store_true", help="Process IMM numbers in reverse order (newest first)")
    ctl.add_argument("--delay-ms", type=int, default=2000, metavar="MS", help="Milliseconds between IMM fetches (minimum 2000)")
    ctl.add_argument(
        "--diagnostic-allow-sub-2000ms-delay",
        action="store_true",
        help="Allow --delay-ms below 2000 ms for a bounded diagnostic probe only",
    )
    ctl.add_argument(
        "--adaptive-delay",
        action="store_true",
        help="Back off after fetch issues and report bounded batch checkpoints",
    )
    ctl.add_argument("--batch-size", type=int, default=20, metavar="N", help="Cases per adaptive checkpoint (default 20)")
    ctl.add_argument("--batch-pause-ms", type=int, default=0, metavar="MS", help="Pause after each adaptive checkpoint (default 0)")
    ctl.add_argument("--issue-pause-ms", type=int, default=5000, metavar="MS", help="Pause after an adaptive fetch issue (default 5000)")
    ctl.add_argument("--backoff-factor", type=float, default=2.0, metavar="FACTOR", help="Multiply delay after an adaptive fetch issue (default 2.0)")
    ctl.add_argument("--max-delay-ms", type=int, default=None, metavar="MS", help="Adaptive delay ceiling (default 2000 or the starting delay, whichever is higher)")
    ctl.add_argument("--jitter-ms", type=int, default=500, metavar="MS", help="Additional random delay up to this many milliseconds")
    ctl.add_argument("--max-requests", type=int, default=100, metavar="N", help="Maximum API attempts including retries")
    ctl.add_argument("--limit", type=int, default=None, metavar="N", help="Max IMM numbers to process")
    ctl.add_argument("--log-file", metavar="FILE", help="Append live console output to a UTF-8 log file")
    ctl.add_argument("--dry-run", action="store_true", help="Fetch and parse without writing to DB")
    ctl.add_argument(
        "--write-activity",
        action="store_true",
        help="Write endpoint results to fc_activity_* instead of fc_procedural_history",
    )

    args = parser.parse_args()
    try:
        validate_delay_ms(args.delay_ms, args.diagnostic_allow_sub_2000ms_delay)
    except ValueError as exc:
        parser.error(str(exc))
    if args.jitter_ms < 0:
        parser.error("--jitter-ms must be non-negative")
    if args.batch_size < 1:
        parser.error("--batch-size must be at least 1")
    if args.batch_pause_ms < 0:
        parser.error("--batch-pause-ms must be non-negative")
    if args.issue_pause_ms < 0:
        parser.error("--issue-pause-ms must be non-negative")
    if args.backoff_factor <= 1:
        parser.error("--backoff-factor must be greater than 1")
    if args.max_delay_ms is None:
        args.max_delay_ms = max(MIN_DELAY_MS, args.delay_ms)
    elif args.max_delay_ms < args.delay_ms:
        parser.error("--max-delay-ms must be at least --delay-ms")
    if args.max_requests < 1:
        parser.error("--max-requests must be at least 1")
    return args


def main() -> None:
    global LOG_HANDLE
    args = parse_args()
    if args.log_file:
        try:
            LOG_HANDLE = Path(args.log_file).open("a", encoding="utf-8", buffering=1)
        except OSError as exc:
            sys.exit(f"[error] Cannot open --log-file: {exc}")
        log_print(f"[log] Writing live output to {Path(args.log_file)}")

    # Collect IMM numbers
    imms: list[str] = []
    if args.imm_numbers:
        imms.extend(args.imm_numbers)
    if args.imm_file:
        imms.extend(load_imm_from_file(Path(args.imm_file)))
    if args.from_prototype:
        proto_imms = load_imm_from_prototype()
        log_print(f"[info] {len(proto_imms)} IMM numbers from prototype cohort")
        imms.extend(proto_imms)
    if args.generate_years:
        years = [y.strip().zfill(2) for y in args.generate_years.split(",") if y.strip()]
        generated = [
            f"IMM-{n}-{yr}"
            for yr in sorted(years, reverse=True)  # newest year first
            for n in range(args.max_imm, 0, -1)     # highest number first within each year
        ]
        log_print(f"[info] Generated {len(generated):,} IMM numbers for years {', '.join(years)} (max_imm={args.max_imm})")
        # Only add ones not already in the explicit lists
        existing_keys = {i.upper() for i in imms}
        imms.extend(g for g in generated if g not in existing_keys)

    if not imms:
        if args.from_prototype:
            log_print("[info] No prototype IMM numbers require procedural-history fetching.")
            return
        sys.exit("[error] No IMM numbers provided. Use --imm-numbers, --imm-file, --from-prototype, or --generate-years.")

    # Deduplicate preserving order
    seen: set[str] = set()
    deduped: list[str] = []
    for imm in imms:
        key = imm.strip().upper()
        if key not in seen:
            seen.add(key)
            deduped.append(key)
    imms = deduped

    if args.reverse:
        imms = list(reversed(imms))

    if args.limit:
        imms = imms[: args.limit]

    log_print(f"[info] Processing {len(imms)} IMM numbers")

    # Skip already-existing unless --update
    if not args.update and not args.dry_run and not args.write_activity:
        db = SessionLocal()
        try:
            # For large lists, load all already-fetched IMM numbers once rather than a giant IN clause
            already_done: set[str] = set(
                db.scalars(select(FCProceduralHistory.imm_number))
            )
            before = len(imms)
            imms = [imm for imm in imms if imm not in already_done]
            skipped = before - len(imms)
            if skipped:
                log_print(f"[info] Skipping {skipped:,} already-fetched IMM numbers (use --update to refresh)")
        finally:
            db.close()

    if not imms:
        log_print("[info] Nothing to fetch.")
        return

    fetched = 0
    errors = 0
    batch_pause_ms = getattr(args, "batch_pause_ms", 0)

    with httpx.Client(headers=HEADERS, follow_redirects=True) as client:
        request_budget = RequestBudget(args.max_requests)
        db = SessionLocal() if not args.dry_run else None
        current_delay_ms = args.delay_ms
        try:
            for i, imm in enumerate(imms, 1):
                log_print(f"[fetch] ({i}/{len(imms)}) {imm}")
                if i > 1:
                    wait_between_candidates(current_delay_ms, args.jitter_ms)

                try:
                    result = process_imm(client, imm, request_budget=request_budget)
                except Exception as exc:
                    if "request budget exhausted" in str(exc).lower():
                        raise
                    log_print(f"  [error] {imm}: {exc}")
                    errors += 1
                    if args.adaptive_delay:
                        log_print(f"  [adaptive] pausing {args.issue_pause_ms} ms after issue")
                        time.sleep(args.issue_pause_ms / 1000)
                        current_delay_ms = adaptive_backoff_delay_ms(
                            current_delay_ms, args.backoff_factor, args.max_delay_ms
                        )
                        log_print(f"  [adaptive] next delay: {current_delay_ms} ms")
                    if args.adaptive_delay and (i % args.batch_size == 0 or i == len(imms)):
                        log_print(f"[batch] checkpoint after {i}/{len(imms)} cases; delay={current_delay_ms} ms")
                        if batch_pause_ms:
                            log_print(f"[batch] pausing {batch_pause_ms} ms")
                            time.sleep(batch_pause_ms / 1000)
                    continue

                if args.dry_run:
                    log_print(f"  style_of_cause : {result.get('style_of_cause') or '—'}")
                    log_print(f"  leave_decision : {result.get('leave_decision')}")
                    log_print(f"  jr_decision    : {result.get('jr_decision')}")
                    log_print(f"  case_status    : {result.get('case_status')}")
                    log_print(f"  latest_activity: {result.get('latest_activity_date')}")
                    log_print(f"  entries        : {len(result.get('entries_json') or [])}")
                    if result.get("conflict_flag"):
                        log_print(f"  [conflict] leave/JR conflict resolved")
                elif args.write_activity:
                    case_id, document_count = write_activity_result(db, result)
                    if case_id is not None:
                        log_print(f"  activity case {case_id}: {document_count} new documents")
                else:
                    upsert_result(db, result)

                fetched += 1
                if args.adaptive_delay and (i % args.batch_size == 0 or i == len(imms)):
                    log_print(f"[batch] checkpoint after {i}/{len(imms)} cases; delay={current_delay_ms} ms")
                    if batch_pause_ms:
                        log_print(f"[batch] pausing {batch_pause_ms} ms")
                        time.sleep(batch_pause_ms / 1000)

        finally:
            if db:
                db.close()

    log_print(f"\n[done] {fetched} processed, {errors} errors.")
    log_print(f"       API attempts: {request_budget.used}/{request_budget.maximum}")
    if not args.dry_run:
        if args.write_activity:
            log_print("       Results in fc_activity_cases and fc_activity_documents tables.")
        else:
            log_print("       Results in fc_procedural_history table.")

    if LOG_HANDLE is not None:
        LOG_HANDLE.close()
        LOG_HANDLE = None


if __name__ == "__main__":
    main()
