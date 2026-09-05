"""Run and compare the complete V2 Pipeline for one canonical case."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import requests
from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.case_processing import process_case_in_five_layers  # noqa: E402
from backend.database import Case, SessionLocal  # noqa: E402
from scripts.chunk_cases import rebuild_case_chunks  # noqa: E402
from scripts.compare_pipeline_case import compare_snapshots, snapshot_case  # noqa: E402
from scripts.reacquire_source_html import apply_snapshot, validate_snapshot, decision_content_url  # noqa: E402


def refresh_html(case_id: int, timeout: float) -> None:
    with SessionLocal() as db:
        case = db.scalar(select(Case).where(Case.id == case_id))
        if case is None:
            raise ValueError(f"Case {case_id} not found")
        url = (case.source_url or "").strip()
        if not url:
            raise ValueError(f"Case {case_id} has no source URL")
        client = requests.Session()
        client.headers.update({
            "User-Agent": "AI-CaseLibrary/1.0 (V2 Pipeline case test)",
            "Accept": "text/html,application/xhtml+xml;q=0.9",
        })
        response = client.get(decision_content_url(url), timeout=timeout, allow_redirects=True)
        valid, reason = validate_snapshot(response, case.citation)
        if not valid:
            raise RuntimeError(f"Case {case_id} HTML validation failed: {reason}")
        result = apply_snapshot(case, client, timeout, db)
        db.add(case)
        db.commit()
        print(f"html=applied case_id={case_id} bytes={result['bytes']} hash={result['html_sha256']}")


def run_case(case_id: int, output_dir: Path, timeout: float) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    before = snapshot_case(case_id)
    before_path = output_dir / f"pipeline-case-{case_id}-before.json"
    before_path.write_text(__import__("json").dumps(before, indent=2) + "\n", encoding="utf-8")

    refresh_html(case_id, timeout)
    with SessionLocal() as db:
        chunked, chunks = rebuild_case_chunks(db, case_ids=[case_id], replace_existing=True)
        print(f"chunks=rebuilt cases={chunked} rows={chunks}")
    with SessionLocal() as db:
        report = process_case_in_five_layers(
            db,
            case_id,
            stage_order=("metadata", "outcome", "case_citations", "statutes", "tags_v3"),
        )
        db.commit()
        print(f"stages={report}")

    after = snapshot_case(case_id)
    after_path = output_dir / f"pipeline-case-{case_id}-after.json"
    compare_path = output_dir / f"pipeline-case-{case_id}-compare.json"
    after_path.write_text(__import__("json").dumps(after, indent=2) + "\n", encoding="utf-8")
    comparison = compare_snapshots(before, after)
    compare_path.write_text(__import__("json").dumps(comparison, indent=2) + "\n", encoding="utf-8")
    print(f"before={before_path}")
    print(f"after={after_path}")
    print(f"compare={compare_path}")
    return comparison


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-id", type=int, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("data/eval/reports/v2-pipeline"))
    parser.add_argument("--timeout", type=float, default=30.0)
    args = parser.parse_args()
    run_case(args.case_id, args.output_dir, args.timeout)


if __name__ == "__main__":
    main()
