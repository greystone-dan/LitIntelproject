"""Snapshot and compare one case across V2 Pipeline derived layers."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import (  # noqa: E402
    Case,
    CaseChunk,
    CaseOutcome,
    CaseTag,
    Citation,
    SessionLocal,
    StatuteReference,
)
from backend.legal_tagger_v3 import TAXONOMY_VERSION  # noqa: E402
from backend.metadata_outcomes import OUTCOME_CLASSIFIER_VERSION  # noqa: E402


def _json_value(value: Any) -> Any:
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, list):
        return [_json_value(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _json_value(item) for key, item in value.items()}
    return str(value)


def _citation_key(row: dict[str, Any]) -> tuple[Any, ...]:
    return (
        row.get("kind"),
        row.get("normalized"),
        row.get("text"),
        row.get("offset_start"),
        row.get("offset_end"),
    )


def _statute_key(row: dict[str, Any]) -> tuple[Any, ...]:
    return (
        row.get("kind"),
        row.get("normalized"),
        row.get("instrument_key"),
        row.get("pinpoint"),
        row.get("offset_start"),
        row.get("offset_end"),
    )


def _chunk_key(row: dict[str, Any]) -> tuple[Any, ...]:
    return (row.get("chunk_set"), row.get("chunk_index"), row.get("text_hash"))


def _tag_key(row: dict[str, Any]) -> tuple[Any, ...]:
    return (
        row.get("category"),
        row.get("value"),
        row.get("offset_start"),
        row.get("offset_end"),
    )


def snapshot_case(case_id: int) -> dict[str, Any]:
    with SessionLocal() as db:
        case = db.scalar(select(Case).where(Case.id == case_id))
        if case is None:
            raise ValueError(f"Case {case_id} not found")
        chunks = list(db.scalars(select(CaseChunk).where(CaseChunk.case_id == case_id).order_by(CaseChunk.chunk_set, CaseChunk.chunk_index)))
        citations = list(db.scalars(select(Citation).where(Citation.source_case_id == case_id).order_by(Citation.id)))
        statutes = list(db.scalars(select(StatuteReference).where(StatuteReference.source_case_id == case_id).order_by(StatuteReference.id)))
        tags = list(db.scalars(select(CaseTag).where(CaseTag.case_id == case_id, CaseTag.taxonomy_version == TAXONOMY_VERSION).order_by(CaseTag.id)))
        outcome = db.scalar(select(CaseOutcome).where(CaseOutcome.case_id == case_id, CaseOutcome.classifier_version == OUTCOME_CLASSIFIER_VERSION))

        chunk_rows = [
            {
                "chunk_set": row.chunk_set,
                "chunk_index": row.chunk_index,
                "label": row.chunk_label,
                "text_hash": row.text_hash,
                "text_length": len(row.text or ""),
                "paragraph_start": row.paragraph_start,
                "paragraph_end": row.paragraph_end,
            }
            for row in chunks
        ]
        citation_rows = [
            {
                "kind": row.citation_kind,
                "text": row.citation_text,
                "normalized": row.normalized_citation,
                "offset_start": row.offset_start,
                "offset_end": row.offset_end,
                "chunk_id": row.chunk_id,
                "unresolved": row.unresolved,
            }
            for row in citations
        ]
        statute_rows = [
            {
                "kind": row.reference_kind,
                "text": row.reference_text,
                "normalized": row.normalized_reference,
                "instrument_key": row.instrument_key,
                "pinpoint": row.pinpoint,
                "offset_start": row.offset_start,
                "offset_end": row.offset_end,
                "chunk_id": row.chunk_id,
            }
            for row in statutes
        ]
        tag_rows = [
            {
                "category": row.category,
                "value": row.value,
                "evidence": row.evidence,
                "offset_start": row.offset_start,
                "offset_end": row.offset_end,
                "rule_id": row.rule_id,
                "evidence_role": row.evidence_role,
            }
            for row in tags
        ]
        outcome_row = None
        if outcome is not None:
            outcome_row = {
                "classifier_version": outcome.classifier_version,
                "decision_outcome": outcome.decision_outcome,
                "outcome_status": outcome.outcome_status,
                "winner_side": outcome.winner_side,
                "loser_side": outcome.loser_side,
                "government_role": outcome.government_role,
                "government_outcome": outcome.government_outcome,
                "challenged_issue": outcome.challenged_issue,
                "challenged_issues": _json_value(outcome.challenged_issues),
                "disposition_evidence": outcome.disposition_evidence,
                "evidence_offset_start": outcome.evidence_offset_start,
                "evidence_offset_end": outcome.evidence_offset_end,
                "confidence": outcome.confidence,
            }
        return {
            "case_id": case.id,
            "court": case.court,
            "citation": case.citation,
            "text_length": len(case.full_text or ""),
            "source_url": case.source_url,
            "source_html_present": bool((case.source_html or "").strip()),
            "source_html_sha256": hashlib.sha256((case.source_html or "").encode("utf-8")).hexdigest() if case.source_html else None,
            "metadata": _json_value((case.metadata_json or {}).get("reader_extracted") or {}),
            "chunks": chunk_rows,
            "citations": citation_rows,
            "statutes": statute_rows,
            "tags_v3": tag_rows,
            "outcome": outcome_row,
        }


def _delta(
    before: list[dict[str, Any]],
    after: list[dict[str, Any]],
    key_fn,
    *,
    major_absolute_threshold: int = 50,
    major_relative_threshold: float = 0.5,
) -> dict[str, Any]:
    before_keys = {_json_value(key_fn(row)): row for row in before}
    after_keys = {_json_value(key_fn(row)): row for row in after}
    added = [after_keys[key] for key in after_keys.keys() - before_keys.keys()]
    removed = [before_keys[key] for key in before_keys.keys() - after_keys.keys()]
    delta = len(after) - len(before)
    relative = abs(delta) / max(1, len(before))
    major = abs(delta) >= major_absolute_threshold or (
        len(before) >= 20 and relative >= major_relative_threshold
    ) or (len(before) == 0 and len(after) >= major_absolute_threshold)
    return {
        "before": len(before),
        "after": len(after),
        "delta": delta,
        "relative_delta": round(relative, 4),
        "major_delta": major,
        "added": added,
        "removed": removed,
    }


def compare_snapshots(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    if before.get("case_id") != after.get("case_id"):
        raise ValueError("Snapshots must belong to the same case")
    return {
        "case_id": before["case_id"],
        "before_source_html_present": before.get("source_html_present"),
        "after_source_html_present": after.get("source_html_present"),
        "text_length_before": before.get("text_length"),
        "text_length_after": after.get("text_length"),
        "chunks": _delta(before.get("chunks", []), after.get("chunks", []), _chunk_key),
        "citations": _delta(before.get("citations", []), after.get("citations", []), _citation_key),
        "statutes": _delta(before.get("statutes", []), after.get("statutes", []), _statute_key),
        "tags_v3": _delta(before.get("tags_v3", []), after.get("tags_v3", []), _tag_key),
        "outcome_before": before.get("outcome"),
        "outcome_after": after.get("outcome"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--snapshot", action="store_true")
    mode.add_argument("--compare", nargs=2, metavar=("BEFORE", "AFTER"))
    parser.add_argument("--case-id", type=int)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.snapshot:
        if args.case_id is None:
            parser.error("--case-id is required with --snapshot")
        payload = snapshot_case(args.case_id)
    else:
        before = json.loads(args.compare[0] and Path(args.compare[0]).read_text(encoding="utf-8"))
        after = json.loads(Path(args.compare[1]).read_text(encoding="utf-8"))
        payload = compare_snapshots(before, after)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"wrote={args.output}")


if __name__ == "__main__":
    main()
