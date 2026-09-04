"""Bounded HTML snapshot reacquisition for the curated core case subset."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, urlunparse

import requests
from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseSource, SessionLocal
from backend.ingestion import sanitize_source_html

DEFAULT_CORE_CSV = PROJECT_ROOT / "data" / "eval" / "core_immigration_cases.csv"
ALLOWED_HOSTS = {
    "decisions.fct-cf.gc.ca",
    "decisions.fca-caf.gc.ca",
    "decisions.scc-csc.ca",
    "www.canlii.org",
    "canlii.org",
}
USER_AGENT = "AI-CaseLibrary/1.0 (source snapshot validation)"


def decision_content_url(url: str) -> str:
    """Return the Federal Court iframe variant containing the decision body."""
    parsed = urlparse(url)
    query = "iframe=true" if not parsed.query else f"{parsed.query}&iframe=true"
    return urlunparse(parsed._replace(query=query))


def load_case_ids(path: Path, limit: int | None) -> list[int]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    ids = [int(float(row["local_case_id"])) for row in rows if row.get("local_case_id") not in {None, "", "nan"}]
    return ids[:limit] if limit is not None else ids


def validate_snapshot(response: requests.Response, expected_citation: str | None = None) -> tuple[bool, str]:
    content_type = (response.headers.get("Content-Type") or "").lower()
    body = response.text.lstrip().lower()
    if response.status_code != 200:
        return False, f"HTTP {response.status_code}"
    if "html" not in content_type and "<html" not in body and "<!doctype" not in body:
        return False, f"not-html content-type={content_type or 'missing'}"
    if len(response.content) < 1000:
        return False, "response-too-small"
    if any(marker in body[:5000] for marker in ("access denied", "captcha", "cloudflare error")):
        return False, "access-or-challenge-page"
    if expected_citation and expected_citation.casefold() not in body:
        return False, "decision-content-not-found"
    return True, "valid-html"


def inspect_case(case: Case, client: requests.Session, timeout: float) -> dict[str, object]:
    url = (case.source_url or "").strip()
    parsed = urlparse(url)
    if parsed.hostname not in ALLOWED_HOSTS:
        return {"case_id": case.id, "citation": case.citation, "status": "skipped", "reason": "unapproved-host", "url": url}
    try:
        content_url = decision_content_url(url)
        response = client.get(content_url, timeout=timeout, allow_redirects=True)
        valid, reason = validate_snapshot(response, case.citation)
        result: dict[str, object] = {"case_id": case.id, "citation": case.citation, "status": "ready" if valid else "failed", "reason": reason, "url": url, "content_url": content_url, "final_url": response.url, "bytes": len(response.content)}
        if valid:
            sanitized = sanitize_source_html(response.text)
            result["sanitized_bytes"] = len((sanitized or "").encode("utf-8"))
            result["html_sha256"] = hashlib.sha256(response.content).hexdigest()
        return result
    except requests.RequestException as error:
        return {"case_id": case.id, "citation": case.citation, "status": "failed", "reason": f"{type(error).__name__}: {error}", "url": url}


def apply_snapshot(case: Case, client: requests.Session, timeout: float, db) -> dict[str, object]:
    url = (case.source_url or "").strip()
    response = client.get(decision_content_url(url), timeout=timeout, allow_redirects=True)
    valid, reason = validate_snapshot(response, case.citation)
    if not valid:
        raise RuntimeError(reason)
    sanitized = sanitize_source_html(response.text)
    html_hash = hashlib.sha256(response.content).hexdigest()
    retrieved_at = datetime.now(timezone.utc).isoformat()
    metadata = dict(case.metadata_json or {})
    metadata["source_html_snapshot"] = {
        "sha256": html_hash,
        "retrieved_at": retrieved_at,
        "final_url": response.url,
        "parser_input": "network_html",
    }
    case.source_html = sanitized
    case.metadata_json = metadata
    source = db.scalar(
        select(CaseSource).where(CaseSource.case_id == case.id, CaseSource.source_url == url).limit(1)
    )
    if source is None:
        db.add(
            CaseSource(
                case_id=case.id,
                source_type="federal_court_html",
                source_name="Federal Court decision page",
                source_url=url,
                is_primary=False,
                raw_hash=html_hash,
                metadata_json={"retrieved_at": retrieved_at, "final_url": response.url},
            )
        )
    else:
        source.raw_hash = html_hash
        source.metadata_json = {**(source.metadata_json or {}), "retrieved_at": retrieved_at, "final_url": response.url}
    return {"case_id": case.id, "citation": case.citation, "status": "applied", "reason": reason, "bytes": len(response.content), "html_sha256": html_hash}


def run(core_csv: Path, limit: int | None, case_id: int | None, timeout: float, apply: bool) -> dict[str, object]:
    ids = [case_id] if case_id is not None else load_case_ids(core_csv, limit)
    with SessionLocal() as db:
        cases = list(db.scalars(select(Case).where(Case.id.in_(ids)).order_by(Case.id)))
    client = requests.Session()
    client.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml;q=0.9"})
    results = []
    for case in cases:
        if (case.source_html or "").strip():
            results.append({"case_id": case.id, "citation": case.citation, "status": "skipped", "reason": "already-has-html"})
            continue
        result = inspect_case(case, client, timeout)
        if apply and result["status"] == "ready":
            try:
                result = apply_snapshot(case, client, timeout, db)
            except requests.RequestException as error:
                result = {**result, "status": "failed", "reason": f"{type(error).__name__}: {error}"}
            else:
                db.add(case)
        results.append(result)
    if apply:
        db.commit()
    counts = {status: sum(result["status"] == status for result in results) for status in ("ready", "applied", "failed", "skipped")}
    return {"timestamp": datetime.now(timezone.utc).isoformat(), "core_csv": str(core_csv), "requested": len(ids), "inspected": len(results), "counts": counts, "apply_performed": apply, "results": results}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core-csv", type=Path, default=DEFAULT_CORE_CSV)
    parser.add_argument("--limit", type=int, default=5, help="Maximum cases to inspect; default 5")
    parser.add_argument("--case-id", type=int)
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--apply", action="store_true", help="Store validated sanitized HTML snapshots and provenance")
    parser.add_argument("--output-file", type=Path)
    args = parser.parse_args()
    if args.limit is not None and args.limit < 1:
        raise SystemExit("--limit must be at least 1")
    report = run(args.core_csv, args.limit, args.case_id, args.timeout, args.apply)
    if args.output_file:
        args.output_file.parent.mkdir(parents=True, exist_ok=True)
        args.output_file.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"inspected={report['inspected']} counts={report['counts']} apply_performed={report['apply_performed']}")
    for result in report["results"]:
        print(f"case_id={result['case_id']} citation={result.get('citation')} status={result['status']} reason={result['reason']}")
    return 0 if not report["counts"]["failed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
