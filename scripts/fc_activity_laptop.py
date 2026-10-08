#!/usr/bin/env python3
"""FC Activity laptop runner: fetch docket activity for a list of IMM numbers, no database, no installs.

Standard library only (Python 3.9+). One file. It reads a plain-text list of IMM numbers (one per line,
made on the iLit PC with `fc_activity_backlog.py export-list`), fetches each from the Federal Court
site (2 requests per file, one file at a time) and appends the results to a .jsonl file. The PC later
imports that file (`fc_activity_backlog.py import`). Nothing is sent anywhere else.

Pace follows the 2026-09-25/26 live sweep that fetched 98,300 files with zero errors and no 403/429:
100 ms between files, a 2 s pause after every 20 files. Safety (kept on):
  * after a failed file the delay doubles (up to 2 s), the run pauses 10 s (doubling to 5 min), and it
    speeds up again after 50 clean files
  * any HTTP 403 or 429 stops the whole run at once; it is never retried
  * 10 failed files in a row stop the run
  * a stop file ends the run cleanly after the current file; running again resumes where it left off

Usage:
  python fc_activity_laptop.py --list imm_list.txt --test        # 200-file speed test, results kept separate
  python fc_activity_laptop.py --list imm_list.txt               # the real run (add --max-minutes 600)
  stop:    create an empty file named stop.txt in the data folder
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

META_URL = ("https://www.fct-cf.ca/CourtFilesAndDecisions/"
            "proceedingQueriesCourtNumberList?division=t&courtnumber={imm}")
RE_URL = ("https://www.fct-cf.ca/CourtFilesAndDecisions/"
          "proceedingQueriesRE?division={imm}&courtnumber={imm}")
HEADERS = {
    "User-Agent": "iLit-daily-intake/1.0 (+https://www.ilit.ca; research use)",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-CA,en;q=0.9",
    "Referer": "https://www.fct-cf.ca/",
}
IMM_RE = re.compile(r"^IMM-\d{1,6}-\d{2}$")


class Blocked(RuntimeError):
    """The Court site answered 403 or 429."""


# --- parsing (identical to scripts/fetch_fc_procedural_history.py) ---

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

# --- fetching ---

def http_get(url: str, retries: int = 3) -> str:
    last: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            request = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(request, timeout=20) as response:
                if response.status == 200:
                    return response.read().decode("utf-8", errors="replace")
                raise RuntimeError(f"HTTP {response.status}")
        except urllib.error.HTTPError as exc:
            if exc.code in (403, 429):
                raise Blocked(f"HTTP {exc.code}") from exc
            last = exc
        except (urllib.error.URLError, TimeoutError, OSError, RuntimeError) as exc:
            last = exc
        if attempt < retries:
            time.sleep(attempt)
    raise RuntimeError(f"failed after {retries} attempts: {last}")


def fetch_one(imm: str) -> dict:
    """Same result shape as the PC importer expects (process_imm in fetch_fc_procedural_history.py)."""
    style = ""
    try:
        style = get_json_value(http_get(META_URL.format(imm=imm)), "STYLE_OF_CAUSE")
    except Blocked:
        raise
    except Exception:
        pass
    try:
        re_text = http_get(RE_URL.format(imm=imm))
    except Blocked:
        raise
    except Exception:
        return {"error": "no_re_data"}
    entries = parse_all_entries(re_text)
    if not style:
        try:
            outer = json.loads(re_text)
            rows = outer.get("data") if isinstance(outer, dict) else outer
            if rows and isinstance(rows[0], dict):
                style = rows[0].get("STYLE_OF_CAUSE", "") or ""
        except Exception:
            pass
    return {"imm_number": imm, "style_of_cause": style or None, "entries_json": entries,
            "fetched_at": datetime.now(timezone.utc).isoformat()}


def is_missing(result: dict) -> bool:
    return not result.get("entries_json") and not result.get("style_of_cause")


# --- run ---

def log(handle, message: str) -> None:
    line = f"{datetime.now():%Y-%m-%d %H:%M:%S} {message}"
    print(line, flush=True)
    handle.write(line + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--list", required=True, help="text file of IMM numbers, one per line")
    parser.add_argument("--data-dir", default="fc_data", help="folder for results, log, progress, stop file")
    parser.add_argument("--test", action="store_true", help="fetch 200 files into a separate test file and print the speed")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--max-minutes", type=float)
    parser.add_argument("--delay-ms", type=int, default=100)
    parser.add_argument("--max-delay-ms", type=int, default=2000)
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--batch-pause-ms", type=int, default=2000)
    parser.add_argument("--max-consecutive-failures", type=int, default=10)
    args = parser.parse_args()

    data = Path(args.data_dir)
    data.mkdir(parents=True, exist_ok=True)
    tag = "test" if args.test else "run"
    out_path = data / f"results_{tag}.jsonl"
    done_path = data / f"done_{tag}.txt"
    stop_path = data / "stop.txt"
    progress_path = data / f"progress_{tag}.json"
    if stop_path.exists():
        print(f"{stop_path} exists. Delete it and run again.")
        return 1

    wanted = []
    for line in Path(args.list).read_text(encoding="utf-8").splitlines():
        imm = line.split("\t", 1)[0].strip().upper()
        if IMM_RE.match(imm):
            wanted.append(imm)
    done = set(done_path.read_text(encoding="utf-8").split()) if done_path.exists() else set()
    todo = [imm for imm in wanted if imm not in done]
    limit = 200 if args.test and not args.limit else args.limit
    if limit:
        todo = todo[:limit]

    stats = {"processed": 0, "with_entries": 0, "missing": 0, "failed": 0}
    started = time.monotonic()
    delay_ms, clean, fails, pause_s = args.delay_ms, 0, 0, 10.0
    reason = "finished"
    with open(data / f"log_{tag}.txt", "a", encoding="utf-8", buffering=1) as lg, \
            open(out_path, "a", encoding="utf-8", buffering=1) as out, \
            open(done_path, "a", encoding="utf-8", buffering=1) as done_out:
        log(lg, f"{len(wanted):,} in list, {len(done):,} already done, {len(todo):,} to fetch ({tag})")
        for i, imm in enumerate(todo, 1):
            if stop_path.exists():
                reason = "stop file"
                break
            if args.max_minutes and time.monotonic() - started > args.max_minutes * 60:
                reason = "time limit"
                break
            if i > 1:
                time.sleep(delay_ms / 1000)
            try:
                result = fetch_one(imm)
            except Blocked as exc:
                reason = f"{exc} from the Court site: stopped, not retried"
                log(lg, f"[BLOCK] {imm}: {reason}")
                break
            if result.get("error"):
                stats["failed"] += 1
                fails += 1
                clean = 0
                delay_ms = min(args.max_delay_ms, max(delay_ms * 2, 250))
                log(lg, f"[fail] {imm} ({fails} in a row); delay now {delay_ms} ms; pausing {pause_s:.0f}s")
                time.sleep(pause_s)
                pause_s = min(pause_s * 2, 300)
                if fails >= args.max_consecutive_failures:
                    reason = f"{fails} failures in a row"
                    break
                continue
            fails, pause_s = 0, 10.0
            clean += 1
            if clean >= 50 and delay_ms > args.delay_ms:
                delay_ms, clean = max(args.delay_ms, int(delay_ms * 0.75)), 0
            stats["processed"] += 1
            if is_missing(result):
                stats["missing"] += 1
            else:
                stats["with_entries"] += 1
                out.write(json.dumps({"imm": imm, "result": result}) + "\n")
            done_out.write(imm + "\n")
            if i % 100 == 0:
                log(lg, f"{i:,}/{len(todo):,} done; {stats}")
            if i % 25 == 0:
                progress_path.write_text(json.dumps({**stats, "remaining": len(todo) - i, "delay_ms": delay_ms,
                                                     "updated": datetime.now().isoformat(timespec="seconds")}, indent=2))
            if i % args.batch_size == 0:
                time.sleep(args.batch_pause_ms / 1000)
        elapsed = max(time.monotonic() - started, 0.001)
        progress_path.write_text(json.dumps({**stats, "stopped": reason, "remaining": len(todo) - stats["processed"],
                                             "updated": datetime.now().isoformat(timespec="seconds")}, indent=2))
        log(lg, f"Stopped: {reason}. {stats}")
        log(lg, f"Speed: {stats['processed']} files in {elapsed / 60:.1f} min = "
                f"{stats['processed'] / elapsed * 3600:,.0f} files/hour")
    return 0 if reason in ("finished", "stop file", "time limit") else 2


if __name__ == "__main__":
    sys.exit(main())
