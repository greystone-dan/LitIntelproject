"""Bounded, resumable source-HTML acquisition for canonical cases."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests
from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseSource, SessionLocal
from backend.ingestion import sanitize_source_html
from scripts.reacquire_source_html import decision_content_url, validate_snapshot

ALLOWED_HOSTS = {
    "decisions.fct-cf.gc.ca",
    "www.fct-cf.gc.ca",
    "decisions.fca-caf.gc.ca",
    "decisions.scc-csc.ca",
    "www.canlii.org",
    "canlii.org",
}


def acquire_case(case: Case, client: requests.Session, timeout: float, retries: int) -> dict[str, object]:
    source_url = (case.source_url or "").strip()
    parsed = urlparse(source_url)
    if not source_url:
        return {"case_id": case.id, "status": "quarantined", "reason": "missing-source-url"}
    if not parsed.hostname:
        return {"case_id": case.id, "status": "quarantined", "reason": "malformed-source-url", "url": source_url}
    if parsed.hostname not in ALLOWED_HOSTS:
        return {"case_id": case.id, "status": "quarantined", "reason": "unsupported-source-host", "host": parsed.hostname, "url": source_url}
    last_error = "unknown"
    for attempt in range(1, retries + 1):
        try:
            response = client.get(decision_content_url(source_url), timeout=timeout, allow_redirects=True)
            valid, reason = validate_snapshot(response, case.citation)
            if not valid:
                return {"case_id": case.id, "status": "quarantined", "reason": reason, "attempt": attempt, "url": source_url}
            sanitized = sanitize_source_html(response.text)
            return {
                "case_id": case.id,
                "status": "ready",
                "url": source_url,
                "final_url": response.url,
                "bytes": len(response.content),
                "sha256": hashlib.sha256(response.content).hexdigest(),
                "sanitized": sanitized,
                "retrieved_at": datetime.now(timezone.utc).isoformat(),
                "attempt": attempt,
            }
        except requests.RequestException as error:
            last_error = f"{type(error).__name__}: {error}"
            if attempt < retries:
                time.sleep(min(2**attempt, 8))
    return {"case_id": case.id, "status": "quarantined", "reason": last_error, "attempt": retries, "url": source_url}


def apply_result(db, case: Case, result: dict[str, object]) -> None:
    if result["status"] != "ready":
        return
    retrieved_at = str(result["retrieved_at"])
    metadata = dict(case.metadata_json or {})
    metadata["source_html_snapshot"] = {
        "sha256": result["sha256"],
        "retrieved_at": retrieved_at,
        "final_url": result["final_url"],
        "parser_input": "network_html",
    }
    case.source_html = str(result["sanitized"])
    case.metadata_json = metadata
    source = db.scalar(select(CaseSource).where(CaseSource.case_id == case.id, CaseSource.source_url == case.source_url).limit(1))
    if source is None:
        db.add(CaseSource(case_id=case.id, source_type="source_html", source_name="Canonical source HTML", source_url=case.source_url, is_primary=False, raw_hash=str(result["sha256"]), metadata_json={"retrieved_at": retrieved_at, "final_url": result["final_url"]}))
    else:
        source.raw_hash = str(result["sha256"])
        source.metadata_json = {**(source.metadata_json or {}), "retrieved_at": retrieved_at, "final_url": result["final_url"]}
    db.add(case)


def run(*, limit: int | None, batch_size: int, timeout: float, retries: int, dry_run: bool, quarantine_path: Path) -> dict[str, int]:
    if batch_size < 1 or retries < 1 or timeout <= 0:
        raise ValueError("batch-size/retries must be positive and timeout must be greater than zero")
    client = requests.Session()
    client.headers.update({"User-Agent": "AI-CaseLibrary/2.0 (bounded source refresh)", "Accept": "text/html,application/xhtml+xml;q=0.9"})
    counts = {"scanned": 0, "ready": 0, "applied": 0, "quarantined": 0}
    quarantine_path.parent.mkdir(parents=True, exist_ok=True)
    quarantine = quarantine_path.open("a", encoding="utf-8")
    try:
        with SessionLocal() as db:
            cases = db.scalars(select(Case).where(Case.source_url.is_not(None), Case.source_url != "").order_by(Case.id).limit(limit or 1000000)).yield_per(batch_size)
            batch = []
            for case in cases:
                batch.append(case)
                if len(batch) < batch_size:
                    continue
                _process_batch(db, batch, client, timeout, retries, dry_run, counts, quarantine)
                batch = []
            if batch:
                _process_batch(db, batch, client, timeout, retries, dry_run, counts, quarantine)
    finally:
        quarantine.close()
    return counts


def _process_batch(db, cases, client, timeout, retries, dry_run, counts, quarantine) -> None:
    for case in cases:
        counts["scanned"] += 1
        result = acquire_case(case, client, timeout, retries)
        status = str(result["status"])
        if status == "ready":
            counts["ready"] += 1
            if not dry_run:
                apply_result(db, case, result)
                counts["applied"] += 1
        else:
            counts["quarantined"] += 1
            quarantine.write(json.dumps({key: value for key, value in result.items() if key != "sanitized"}) + "\n")
    if not dry_run:
        db.commit()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--batch-size", type=int, default=25)
    parser.add_argument("--timeout", type=float, default=30)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--quarantine", type=Path, default=Path("data/overnight_runs/v2-pipeline/source-quarantine.jsonl"))
    args = parser.parse_args()
    print(run(limit=args.limit, batch_size=args.batch_size, timeout=args.timeout, retries=args.retries, dry_run=args.dry_run, quarantine_path=args.quarantine))


if __name__ == "__main__":
    main()
