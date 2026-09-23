from __future__ import annotations

import argparse
from datetime import date, datetime
import json
from pathlib import Path
import sys
from typing import Any

from sqlalchemy import select

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.database import Case, CaseChunk, CaseOutcome, CaseTag, Citation, SessionLocal, StatuteReference


SYSTEM_PROMPT = (
    "You are a senior legal-research intelligence analyst reviewing one Canadian immigration decision. "
    "The supplied dossier is a deterministic database printout plus source text. Do not write a generic "
    "whole-case summary. Produce structured intelligence about arguments, discussion units, and advanced "
    "citation treatment. Treat deterministic IDs, offsets, hashes, extracted citations, statutes, tags, "
    "and outcomes as evidence about the source record, not as conclusions. Use the source text to decide "
    "what an authority is doing in context. Distinguish the court's reasoning from party submissions and "
    "from procedural history. Do not infer a treatment relationship merely because a citation is nearby. "
    "For every material conclusion, cite one or more supplied citation_id values and paragraph numbers. "
    "Mark uncertainty explicitly and say when the source does not support a conclusion. Preserve the "
    "difference between citation treatment, statute use, argument role, and outcome. Return one JSON object "
    "with exactly these top-level keys: case_orientation, discussion_unit_intelligence, argument_map, "
    "citation_treatment, statute_and_issue_intelligence, unresolved_questions, quality_control. "
    "Coverage is mandatory: citation_treatment must contain exactly one record for every citation "
    "in deterministic_record.identified_citation_windows, currently 97 records. Use its citation_record.citation_id "
    "as the key; do not return a representative sample and do not omit citations. If a citation has no "
    "supported treatment, return treatment=absent or neutral with a short evidence-based explanation. "
    "Keep each citation-treatment record extremely concise so all required records fit in the response: "
    "use only citation_id, treatment, confidence, rationale, and paragraph_indices; do not repeat the "
    "normalized citation, source quote, or long authority propositions. Keep each rationale under 35 words."
)


def _json_value(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {str(key): _json_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_value(item) for item in value]
    return value


def _model_record(instance: Any, fields: tuple[str, ...]) -> dict[str, Any]:
    return {field: _json_value(getattr(instance, field, None)) for field in fields}


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_identified_citations(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _load_prior_discussion_units(directory: Path) -> list[dict[str, Any]]:
    units: list[dict[str, Any]] = []
    for path in sorted(directory.glob("mason_scc_2023_window_*_result_request.json")):
        if "llm_only" in path.name:
            continue
        payload = _load_json(path)
        for unit in payload.get("response", {}).get("result", {}).get("units", []):
            units.append({"source_artifact": str(path), **unit})
    return units


def _without_repeated_text(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: _without_repeated_text(item)
            for key, item in value.items()
            if key not in {"text", "context_text"}
        }
    if isinstance(value, list):
        return [_without_repeated_text(item) for item in value]
    return value


def _without_nulls(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: _without_nulls(item)
            for key, item in value.items()
            if item is not None
        }
    if isinstance(value, list):
        return [_without_nulls(item) for item in value]
    return value


def _compact_identified_citation(row: dict[str, Any]) -> dict[str, Any]:
    metadata = row.get("metadata", {})
    citation_record = metadata.get("citation_record", {})
    paragraph = metadata.get("paragraph", {})
    discussion_unit = metadata.get("discussion_unit", {})
    return {
        "example_id": row.get("example_id"),
        "source_text_sha256": row.get("source_text_sha256"),
        "citation_record": citation_record,
        "paragraph": {
            "start": paragraph.get("start"),
            "end": paragraph.get("end"),
        },
        "discussion_unit": {
            "start_paragraph": discussion_unit.get("start_paragraph"),
            "end_paragraph": discussion_unit.get("end_paragraph"),
            "label": discussion_unit.get("label"),
            "confidence": discussion_unit.get("confidence"),
        },
        "citations": row.get("citations", []),
    }


def _compact_prior_unit(unit: dict[str, Any]) -> dict[str, Any]:
    return {
        "source_artifact": unit.get("source_artifact"),
        "start_paragraph": unit.get("start_paragraph"),
        "end_paragraph": unit.get("end_paragraph"),
        "label": unit.get("label"),
        "explanation": unit.get("explanation"),
        "transition_from_previous": unit.get("transition_from_previous"),
        "confidence": unit.get("confidence"),
    }


def _compact_database_record(instance: Any, fields: tuple[str, ...]) -> dict[str, Any]:
    return _without_nulls(_model_record(instance, fields))


def _compact_unit(unit: dict[str, Any]) -> dict[str, Any]:
    return {
        key: unit.get(key)
        for key in ("discussion_unit_id", "start_paragraph", "end_paragraph", "paragraph_count",
                    "citation_counts", "statute_counts", "tag_counts", "generation_method",
                    "generation_version", "text_sha256")
        if unit.get(key) is not None
    }


def build_dossier(
    session: Any,
    *,
    case_id: int,
    deterministic_path: Path,
    identified_citations_path: Path,
    artifact_directory: Path,
) -> dict[str, Any]:
    case = session.execute(select(Case).where(Case.id == case_id)).scalar_one()
    chunks = session.execute(
        select(CaseChunk).where(CaseChunk.case_id == case_id, CaseChunk.chunk_set == "paragraph").order_by(CaseChunk.chunk_index)
    ).scalars().all()
    citations = session.execute(
        select(Citation).where(Citation.source_case_id == case_id).order_by(Citation.id)
    ).scalars().all()
    statutes = session.execute(
        select(StatuteReference).where(StatuteReference.source_case_id == case_id).order_by(StatuteReference.id)
    ).scalars().all()
    tags = session.execute(
        select(CaseTag).where(CaseTag.case_id == case_id).order_by(CaseTag.id)
    ).scalars().all()
    outcomes = session.execute(
        select(CaseOutcome).where(CaseOutcome.case_id == case_id).order_by(CaseOutcome.id)
    ).scalars().all()

    case_fields = (
        "id", "title", "court", "jurisdiction", "date", "citation", "docket_number", "summary",
        "issues", "metadata_json", "source_url", "source_name", "source_id", "source_type",
        "dataset_version", "upstream_license", "language", "full_text_hash", "processing_status",
    )
    chunk_fields = (
        "id", "chunk_set", "chunk_index", "chunk_label", "paragraph_start", "paragraph_end",
        "text", "text_hash", "token_estimate",
    )
    citation_fields = (
        "id", "target_case_id", "citation_kind", "citation_text", "normalized_citation",
        "anchor_citation_text", "anchor_offset_start", "anchor_offset_end", "declared_alias",
        "target_paragraph", "target_chunk_id", "provenance", "chunk_id", "offset_start",
        "offset_end", "unresolved",
    )
    statute_fields = (
        "id", "chunk_id", "offset_start", "offset_end", "reference_text", "normalized_reference",
        "instrument_key", "pinpoint", "provision_section", "provision_subsection",
        "provision_paragraph", "provision_nested_depth", "provision_is_range_or_list",
        "legislation_url", "reference_kind",
    )
    tag_fields = (
        "id", "chunk_id", "category", "value", "score", "evidence", "offset_start", "offset_end",
        "rule_id", "language", "evidence_role", "source", "taxonomy_version",
    )
    outcome_fields = (
        "id", "classifier_version", "decision_outcome", "outcome_status", "winner_side",
        "loser_side", "government_role", "government_outcome", "challenged_issue",
        "challenged_issues", "disposition_evidence", "evidence_offset_start", "evidence_offset_end",
        "confidence", "source",
    )
    deterministic = _load_json(deterministic_path)
    identified = _load_identified_citations(identified_citations_path)
    prior_units = _load_prior_discussion_units(artifact_directory)
    return {
        "request_id": f"mason-case-intelligence-{case_id}",
        "contract_version": "case_intelligence_dossier_v1",
        "case_id": case_id,
        "system_task": {
            "primary_goal": "Extract argument-level and advanced citation-treatment intelligence from the full deterministic record.",
            "explicit_non_goal": "Do not summarize the whole case as the primary output.",
            "required_evidence_link": "Every material finding must name citation_id and/or paragraph_index evidence.",
            "treatment_vocabulary": ["supportive", "distinguishing", "negative", "neutral", "absent", "ambiguous"],
        },
        "deterministic_record": {
            "case": _model_record(case, case_fields),
            "source_text_note": "Paragraph chunks contain the source text; full_text is omitted here to avoid duplicating those authoritative chunks.",
            "paragraph_chunks": [
                _compact_database_record(chunk, ("id", "chunk_index", "paragraph_start", "paragraph_end", "text", "text_hash"))
                for chunk in chunks
            ],
            "all_citation_records": [
                _compact_database_record(
                    citation,
                    ("id", "target_case_id", "citation_kind", "citation_text", "normalized_citation",
                     "target_paragraph", "target_chunk_id", "provenance", "chunk_id", "offset_start",
                     "offset_end", "unresolved"),
                )
                for citation in citations
            ],
            "all_statute_references": [
                _compact_database_record(
                    statute,
                    ("id", "chunk_id", "offset_start", "offset_end", "reference_text", "normalized_reference",
                     "instrument_key", "provision_section", "provision_subsection", "provision_paragraph",
                     "provision_nested_depth", "provision_is_range_or_list", "reference_kind"),
                )
                for statute in statutes
            ],
            "all_tags": [
                _compact_database_record(
                    tag,
                    ("id", "chunk_id", "category", "value", "score", "offset_start", "offset_end",
                     "rule_id", "evidence_role", "source", "taxonomy_version"),
                )
                for tag in tags
            ],
            "all_outcomes": [_compact_database_record(outcome, outcome_fields) for outcome in outcomes],
            "discussion_units": [_compact_unit(unit) for unit in deterministic.get("discussion_units", [])],
            "prior_llm_discussion_unit_hypotheses": [_compact_prior_unit(unit) for unit in prior_units],
            "paragraph_evidence_note": "Paragraph-level citation, statute, tag, heading, and hash evidence is represented by paragraph_chunks and the deterministic record fields above.",
            "identified_citation_windows": [_compact_identified_citation(row) for row in identified],
        },
        "output_schema": {
            "case_orientation": "One short orientation only: central legal questions, posture, and decision-maker layers, with evidence refs.",
            "discussion_unit_intelligence": [{
                "discussion_unit_id": "string",
                "function": "facts | procedural_history | party_submission | legal_framework | analysis | disposition | other",
                "core_propositions": ["string"],
                "argument_roles": ["string"],
                "citation_treatment_patterns": ["string"],
                "evidence": [{"paragraph_indices": ["integer"], "citation_ids": ["integer"]}],
                "confidence": "number 0..1",
            }],
            "argument_map": [{
                "argument_id": "string",
                "actor": "party | tribunal | reviewing_court | other",
                "proposition": "string",
                "legal_issue": "string",
                "authorities_used": [{"citation_id": "integer", "role": "string", "treatment": "string"}],
                "response": "string",
                "result_for_argument": "accepted | rejected | qualified | unresolved | not_applicable",
                "evidence": [{"paragraph_indices": ["integer"], "citation_ids": ["integer"]}],
                "confidence": "number 0..1",
            }],
            "citation_treatment": [{
                "citation_id": "integer",
                "treatment": "supportive | distinguishing | negative | neutral | absent | ambiguous",
                "rationale": "string under 35 words",
                "paragraph_indices": ["integer"],
                "confidence": "number 0..1",
            }],
            "statute_and_issue_intelligence": [{
                "reference_id": "integer",
                "provision": "string",
                "issue_or_argument": "string",
                "role_in_reasoning": "string",
                "evidence": [{"paragraph_indices": ["integer"]}],
                "confidence": "number 0..1",
            }],
            "unresolved_questions": ["Only material questions not answerable from the supplied record."],
            "quality_control": {
                "unsupported_or_ambiguous_findings": ["string"],
                "citation_records_not_semantically_used": ["integer"],
                "deterministic_conflicts": ["string"],
            },
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a no-network Mason case-level intelligence dossier request.")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--case-id", type=int, default=53164)
    parser.add_argument("--model", default="gpt-4.1")
    parser.add_argument("--budget-usd", type=float, default=3.0)
    parser.add_argument(
        "--deterministic-json",
        type=Path,
        default=ROOT / "data/eval/llm_discussion_units_pilot/mason_scc_2023_deterministic.json",
    )
    parser.add_argument(
        "--identified-citations",
        type=Path,
        default=ROOT / "data/eval/llm_discussion_units_pilot/mason_argument_citation_compact_fixture.jsonl",
    )
    parser.add_argument(
        "--artifact-directory",
        type=Path,
        default=ROOT / "data/eval/llm_discussion_units_pilot",
        help="Directory containing prior Mason discussion-unit request/result artifacts.",
    )
    args = parser.parse_args()
    if args.budget_usd <= 0 or args.budget_usd > 3.0:
        parser.error("--budget-usd must be between 0 and 3")
    with SessionLocal() as session:
        dossier = build_dossier(
            session,
            case_id=args.case_id,
            deterministic_path=args.deterministic_json,
            identified_citations_path=args.identified_citations,
            artifact_directory=args.artifact_directory,
        )
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": json.dumps(dossier, ensure_ascii=True, sort_keys=True)},
    ]
    payload = {
        "status": "dry_run_ready",
        "network_called": False,
        "request_id": dossier["request_id"],
        "model": args.model,
        "budget_usd": args.budget_usd,
        "case_id": args.case_id,
        "citation_record_count": len(dossier["deterministic_record"]["all_citation_records"]),
        "identified_citation_count": len(dossier["deterministic_record"]["identified_citation_windows"]),
        "statute_reference_count": len(dossier["deterministic_record"]["all_statute_references"]),
        "tag_count": len(dossier["deterministic_record"]["all_tags"]),
        "discussion_unit_count": len(dossier["deterministic_record"]["discussion_units"]),
        "paragraph_count": len(dossier["deterministic_record"]["paragraph_chunks"]),
        "messages": messages,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "messages"}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())