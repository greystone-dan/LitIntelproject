"""Create a compact before-snapshot for every canonical case."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from sqlalchemy import func, select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseChunk, CaseOutcome, CaseTag, Citation, SessionLocal, StatuteReference  # noqa: E402
from backend.legal_tagger_v3 import TAXONOMY_VERSION  # noqa: E402
from backend.metadata_outcomes import OUTCOME_CLASSIFIER_VERSION  # noqa: E402


def digest(value: object) -> str | None:
    if value is None:
        return None
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def snapshot_case(case: Case, chunk_counts, citation_counts, statute_counts, tag_counts, outcomes) -> dict[str, object]:
    outcome = outcomes.get(case.id)
    extracted = (case.metadata_json or {}).get("reader_extracted") or {}
    return {
        "case_id": case.id,
        "court": case.court,
        "citation": case.citation,
        "text_length": len(case.full_text or ""),
        "full_text_hash": case.full_text_hash or digest(case.full_text or ""),
        "source_url": case.source_url,
        "source_html_present": bool((case.source_html or "").strip()),
        "source_html_hash": digest(case.source_html) if case.source_html else None,
        "metadata_hash": digest(json.dumps(extracted, sort_keys=True, ensure_ascii=True)),
        "chunk_counts": {str(key): int(value) for key, value in chunk_counts.get(case.id, {}).items()},
        "citation_count": int(citation_counts.get(case.id, 0)),
        "statute_count": int(statute_counts.get(case.id, 0)),
        "v3_tag_count": int(tag_counts.get(case.id, 0)),
        "outcome": {
            "status": outcome.outcome_status,
            "decision": outcome.decision_outcome,
            "winner": outcome.winner_side,
            "loser": outcome.loser_side,
            "classifier_version": outcome.classifier_version,
        } if outcome else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("data/eval/reports/v2-pipeline-before-all.jsonl"))
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    count = 0
    with SessionLocal() as db, temporary.open("w", encoding="utf-8") as handle:
        statement = select(Case).order_by(Case.id)
        if args.limit:
            statement = statement.limit(args.limit)
        result = db.scalars(statement).yield_per(100)
        while True:
            cases = result.fetchmany(500)
            if not cases:
                break
            ids = [case.id for case in cases]
            chunk_counts = {}
            for case_id, chunk_set, total in db.execute(select(CaseChunk.case_id, CaseChunk.chunk_set, func.count(CaseChunk.id)).where(CaseChunk.case_id.in_(ids)).group_by(CaseChunk.case_id, CaseChunk.chunk_set)):
                chunk_counts.setdefault(case_id, {})[chunk_set] = total
            citation_counts = dict(db.execute(select(Citation.source_case_id, func.count(Citation.id)).where(Citation.source_case_id.in_(ids)).group_by(Citation.source_case_id)).all())
            statute_counts = dict(db.execute(select(StatuteReference.source_case_id, func.count(StatuteReference.id)).where(StatuteReference.source_case_id.in_(ids)).group_by(StatuteReference.source_case_id)).all())
            tag_counts = dict(db.execute(select(CaseTag.case_id, func.count(CaseTag.id)).where(CaseTag.case_id.in_(ids), CaseTag.taxonomy_version == TAXONOMY_VERSION).group_by(CaseTag.case_id)).all())
            outcomes = {outcome.case_id: outcome for outcome in db.scalars(select(CaseOutcome).where(CaseOutcome.case_id.in_(ids), CaseOutcome.classifier_version == OUTCOME_CLASSIFIER_VERSION))}
            for case in cases:
                handle.write(json.dumps(snapshot_case(case, chunk_counts, citation_counts, statute_counts, tag_counts, outcomes), ensure_ascii=True) + "\n")
                count += 1
            handle.flush()
            print(f"snapshotted={count}", flush=True)
    temporary.replace(args.output)
    print(f"snapshot_cases={count} output={args.output}")


if __name__ == "__main__":
    main()
