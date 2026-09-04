"""Automated data quality and corpus integrity evaluation script.

Audits canonical cases, chunk distributions, citation resolution,
statute references, metadata completeness, and graph consistency.
Emits structured JSON reports and console markdown summaries.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from sqlalchemy import func, select, text as sql_text
from sqlalchemy.orm import Session

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import (
    Case,
    CaseChunk,
    CaseChunkEmbedding,
    CaseSource,
    CaseTag,
    Citation,
    CitationMetrics,
    SessionLocal,
    StatuteReference,
)


def evaluate_corpus_quality(db: Session, sample_limit: int | None = None) -> dict[str, Any]:
    """Execute deterministic SQL audits across cases, chunks, citations, statutes, and metadata."""
    now_iso = datetime.now(timezone.utc).isoformat()

    # 1. Base Inventory Counts
    total_cases = int(db.scalar(select(func.count(Case.id))) or 0)
    cases_with_text = int(
        db.scalar(select(func.count(Case.id)).where(Case.full_text.is_not(None), Case.full_text != ""))
        or 0
    )
    cases_with_summary = int(
        db.scalar(select(func.count(Case.id)).where(Case.summary.is_not(None), Case.summary != ""))
        or 0
    )
    total_chunks = int(db.scalar(select(func.count(CaseChunk.id))) or 0)
    total_chunk_embeddings = int(db.scalar(select(func.count(CaseChunkEmbedding.id))) or 0)
    total_sources = int(db.scalar(select(func.count(CaseSource.id))) or 0)
    total_tags = int(db.scalar(select(func.count(CaseTag.id))) or 0)

    # 2. Citation Integrity & Resolution
    total_citations = int(db.scalar(select(func.count(Citation.id))) or 0)
    resolved_citations = int(
        db.scalar(select(func.count(Citation.id)).where(Citation.target_case_id.is_not(None))) or 0
    )
    unresolved_citations = int(
        db.scalar(select(func.count(Citation.id)).where(Citation.unresolved == True)) or 0  # noqa: E712
    )
    citations_with_chunks = int(
        db.scalar(select(func.count(Citation.id)).where(Citation.chunk_id.is_not(None))) or 0
    )

    # Orphan targets (target_case_id set but does not exist in cases table)
    orphan_citation_targets = int(
        db.scalar(
            sql_text(
                """
                SELECT COUNT(c.id)
                FROM citations c
                LEFT JOIN cases target ON target.id = c.target_case_id
                WHERE c.target_case_id IS NOT NULL AND target.id IS NULL
                """
            )
        )
        or 0
    )

    # Self-citations (source_case_id == target_case_id)
    self_citations = int(
        db.scalar(
            select(func.count(Citation.id)).where(
                Citation.target_case_id.is_not(None),
                Citation.source_case_id == Citation.target_case_id,
            )
        )
        or 0
    )

    # Invalid character offsets (offset_start >= offset_end or negative offsets)
    invalid_citation_offsets = int(
        db.scalar(
            select(func.count(Citation.id)).where(
                Citation.offset_start.is_not(None),
                Citation.offset_end.is_not(None),
                (Citation.offset_start >= Citation.offset_end) | (Citation.offset_start < 0),
            )
        )
        or 0
    )

    # 3. Statute References Health
    total_statutes = int(db.scalar(select(func.count(StatuteReference.id))) or 0)
    irpa_statutes = int(
        db.scalar(
            select(func.count(StatuteReference.id)).where(
                StatuteReference.normalized_reference.ilike("%Immigration and Refugee Protection Act%")
                | StatuteReference.reference_text.ilike("%IRPA%")
            )
        )
        or 0
    )
    irpr_statutes = int(
        db.scalar(
            select(func.count(StatuteReference.id)).where(
                StatuteReference.normalized_reference.ilike("%Immigration and Refugee Protection Regulations%")
                | StatuteReference.reference_text.ilike("%IRPR%")
            )
        )
        or 0
    )
    statutes_with_pinpoint = int(
        db.scalar(
            select(func.count(StatuteReference.id)).where(
                StatuteReference.pinpoint.is_not(None), StatuteReference.pinpoint != ""
            )
        )
        or 0
    )

    # 4. Metadata Field Completeness across Cases
    cases_with_court = int(
        db.scalar(select(func.count(Case.id)).where(Case.court.is_not(None), Case.court != "")) or 0
    )
    cases_with_date = int(db.scalar(select(func.count(Case.id)).where(Case.date.is_not(None))) or 0)
    cases_with_citation = int(
        db.scalar(select(func.count(Case.id)).where(Case.citation.is_not(None), Case.citation != ""))
        or 0
    )
    cases_with_judge = int(
        db.scalar(
            sql_text(
                "SELECT COUNT(id) FROM cases WHERE COALESCE(metadata_json->'reader_extracted'->>'judge', '') <> ''"
            )
        )
        or 0
    )
    cases_with_decision_outcome = int(
        db.scalar(
            sql_text(
                "SELECT COUNT(id) FROM cases WHERE COALESCE(metadata_json->'reader_extracted'->>'decision outcome', '') <> ''"
            )
        )
        or 0
    )
    cases_with_gov_outcome = int(
        db.scalar(
            sql_text(
                "SELECT COUNT(id) FROM cases WHERE COALESCE(metadata_json->'reader_extracted'->>'government outcome', '') <> ''"
            )
        )
        or 0
    )

    # 5. Graph Metrics Freshness
    cases_with_metrics = int(db.scalar(select(func.count(CitationMetrics.case_id))) or 0)

    # Calculate Percentages
    pct_resolved = round((resolved_citations / total_citations * 100), 2) if total_citations else 0.0
    pct_text = round((cases_with_text / total_cases * 100), 2) if total_cases else 0.0
    pct_judge = round((cases_with_judge / total_cases * 100), 2) if total_cases else 0.0
    pct_decision_outcome = (
        round((cases_with_decision_outcome / total_cases * 100), 2) if total_cases else 0.0
    )
    pct_gov_outcome = round((cases_with_gov_outcome / total_cases * 100), 2) if total_cases else 0.0
    pct_statute_pinpoint = (
        round((statutes_with_pinpoint / total_statutes * 100), 2) if total_statutes else 0.0
    )

    return {
        "timestamp": now_iso,
        "sample_limit": sample_limit,
        "inventory": {
            "total_cases": total_cases,
            "cases_with_full_text": cases_with_text,
            "cases_with_summary": cases_with_summary,
            "full_text_coverage_pct": pct_text,
            "total_chunks": total_chunks,
            "total_chunk_embeddings": total_chunk_embeddings,
            "total_sources": total_sources,
            "total_tags": total_tags,
        },
        "citation_health": {
            "total_citations": total_citations,
            "resolved_citations": resolved_citations,
            "unresolved_citations": unresolved_citations,
            "resolution_rate_pct": pct_resolved,
            "citations_with_chunk_id": citations_with_chunks,
            "orphan_citation_targets": orphan_citation_targets,
            "self_citations": self_citations,
            "invalid_offset_rows": invalid_citation_offsets,
        },
        "statute_health": {
            "total_statute_references": total_statutes,
            "irpa_references": irpa_statutes,
            "irpr_references": irpr_statutes,
            "statutes_with_pinpoint": statutes_with_pinpoint,
            "pinpoint_coverage_pct": pct_statute_pinpoint,
        },
        "metadata_completeness": {
            "court_coverage": cases_with_court,
            "date_coverage": cases_with_date,
            "citation_coverage": cases_with_citation,
            "judge_coverage": cases_with_judge,
            "judge_coverage_pct": pct_judge,
            "decision_outcome_coverage": cases_with_decision_outcome,
            "decision_outcome_pct": pct_decision_outcome,
            "gov_outcome_coverage": cases_with_gov_outcome,
            "gov_outcome_pct": pct_gov_outcome,
        },
        "graph_health": {
            "cases_with_citation_metrics": cases_with_metrics,
            "metrics_coverage_pct": round((cases_with_metrics / total_cases * 100), 2)
            if total_cases
            else 0.0,
        },
    }


def print_markdown_report(report: dict[str, Any]) -> None:
    inv = report["inventory"]
    cit = report["citation_health"]
    stat = report["statute_health"]
    meta = report["metadata_completeness"]
    graph = report["graph_health"]

    print("\n# AI CaseLibrary Data Quality & Health Audit Report")
    print(f"Generated at: {report['timestamp']}\n")
    print("## 1. Corpus Inventory")
    print(f"- Total Canonical Cases: **{inv['total_cases']:,}**")
    print(f"- Cases with Full Text: **{inv['cases_with_full_text']:,}** ({inv['full_text_coverage_pct']}%)")
    print(f"- Total Text Chunks: **{inv['total_chunks']:,}**")
    print(f"- Stored Chunk Embeddings: **{inv['total_chunk_embeddings']:,}**")
    print(f"- Preserved Case Sources: **{inv['total_sources']:,}**")
    print(f"- Applied Legal Tags: **{inv['total_tags']:,}**\n")

    print("## 2. Citation Health & Layer Separation")
    print(f"- Total Stored Citations: **{cit['total_citations']:,}**")
    print(f"- Resolved Target Links: **{cit['resolved_citations']:,}** ({cit['resolution_rate_pct']}%)")
    print(f"- Unresolved Occurrences: **{cit['unresolved_citations']:,}**")
    print(f"- Orphan Target IDs: **{cit['orphan_citation_targets']}** (Expected: 0)")
    print(f"- Self Citations: **{cit['self_citations']}** (Expected: 0)")
    print(f"- Invalid Offset Spans: **{cit['invalid_offset_rows']}** (Expected: 0)\n")

    print("## 3. Statute References (Separate Layer)")
    print(f"- Total Statute References: **{stat['total_statute_references']:,}**")
    print(f"- IRPA References: **{stat['irpa_references']:,}**")
    print(f"- IRPR References: **{stat['irpr_references']:,}**")
    print(f"- Specific Pinpoints Extracted: **{stat['statutes_with_pinpoint']:,}** ({stat['pinpoint_coverage_pct']}%)\n")

    print("## 4. Metadata Completeness")
    print(f"- Judge Coverage: **{meta['judge_coverage']:,}** ({meta['judge_coverage_pct']}%)")
    print(f"- Decision Outcome Coverage: **{meta['decision_outcome_coverage']:,}** ({meta['decision_outcome_pct']}%)")
    print(f"- Government Outcome Coverage: **{meta['gov_outcome_coverage']:,}** ({meta['gov_outcome_pct']}%)")
    print(f"- Citation Metrics Coverage: **{graph['cases_with_citation_metrics']:,}** ({graph['metrics_coverage_pct']}%)\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate AI CaseLibrary data quality and corpus health.")
    parser.add_argument("--json", action="store_true", help="Print JSON report output to stdout")
    parser.add_argument(
        "--output-file",
        type=str,
        default=None,
        help="Path to write JSON report file (e.g. data/eval/reports/data_quality.json)",
    )
    args = parser.parse_args()

    db = SessionLocal()
    try:
        report = evaluate_corpus_quality(db)
    finally:
        db.close()

    if args.output_file:
        out_path = Path(args.output_file)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Data quality report written to: {out_path}")

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_markdown_report(report)


if __name__ == "__main__":
    main()
