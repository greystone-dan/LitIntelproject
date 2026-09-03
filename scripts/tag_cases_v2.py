"""Apply the independent Tagging V2 core whitelist to canonical cases."""

from __future__ import annotations

import argparse
import logging
import multiprocessing
import sys
import time
from pathlib import Path

from sqlalchemy import delete, exists, select
from sqlalchemy.orm import Session

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseTag, CaseTaggingStatus, SessionLocal
from backend.legal_tagger_v2 import CoreLegalTagger, TAXONOMY_VERSION

logger = logging.getLogger(__name__)


def _tag_batch_worker(case_payloads, result_pipe) -> None:
    tagger = CoreLegalTagger()
    results = []
    for case_id, text in case_payloads:
        occurrences = tagger.tag_occurrences(text)
        results.append((case_id, [
            {
                "category": tag.category,
                "value": tag.value,
                "score": tag.score,
                "evidence": tag.evidence,
                "offset_start": tag.offset_start,
                "offset_end": tag.offset_end,
                "source": tag.source,
                "taxonomy_version": tag.taxonomy_version,
            }
            for tag in occurrences
        ]))
    result_pipe.send(results)
    result_pipe.close()


def pending_case_query(*, last_case_id: int = 0, recent: bool = False, court: str | None = None):
    already_tagged = exists(
        select(CaseTaggingStatus.id).where(
            CaseTaggingStatus.case_id == Case.id,
            CaseTaggingStatus.taxonomy_version == TAXONOMY_VERSION,
        )
    )
    statement = select(Case).where(~already_tagged)
    if court:
        statement = statement.where(Case.court == court)
    if recent:
        return statement.order_by(Case.date.desc(), Case.id.desc())
    return statement.where(Case.id > last_case_id).order_by(Case.id)


def tag_pending_cases(
    db: Session,
    *,
    batch_size: int = 10,
    batch_timeout: float = 300,
    limit: int | None = None,
    recent: bool = False,
    court: str | None = None,
) -> tuple[int, int, int]:
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")
    if batch_timeout <= 0:
        raise ValueError("batch_timeout must be greater than 0")
    if limit is not None and limit < 1:
        raise ValueError("limit must be at least 1")
    context = multiprocessing.get_context("spawn")
    cases_tagged = tags_created = skipped_cases = last_case_id = 0
    while limit is None or cases_tagged < limit:
        size = min(batch_size, limit - cases_tagged) if limit else batch_size
        cases = db.scalars(pending_case_query(last_case_id=last_case_id, recent=recent, court=court).limit(size)).all()
        if not cases:
            break
        parent_pipe, child_pipe = context.Pipe(duplex=False)
        process = context.Process(
            target=_tag_batch_worker,
            args=([(case.id, case.full_text or "") for case in cases], child_pipe),
        )
        started = time.monotonic()
        process.start()
        child_pipe.close()
        results = None
        while time.monotonic() - started < batch_timeout:
            if parent_pipe.poll(0.25):
                results = parent_pipe.recv()
                break
            if not process.is_alive():
                break
        if results is None:
            process.terminate()
            process.join(5)
            db.rollback()
            db.add_all(CaseTaggingStatus(case_id=case.id, taxonomy_version=TAXONOMY_VERSION, tags_count=-1) for case in cases)
            db.commit()
            skipped_cases += len(cases)
            logger.warning("Tagging V2 skipped batch case_ids=%s after %.1fs timeout", [case.id for case in cases], time.monotonic() - started)
        else:
            process.join(5)
            for case_id, occurrence_rows in results:
                db.add_all(CaseTag(case_id=case_id, **row) for row in occurrence_rows)
                db.add(CaseTaggingStatus(case_id=case_id, taxonomy_version=TAXONOMY_VERSION, tags_count=len(occurrence_rows)))
                tags_created += len(occurrence_rows)
            db.commit()
        cases_tagged += len(cases)
        last_case_id = cases[-1].id
        logger.info("Tagging V2 processed %d cases, created %d tags, skipped %d", cases_tagged, tags_created, skipped_cases)
        if recent:
            break
    return cases_tagged, tags_created, skipped_cases


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--batch-timeout", type=float, default=300, help="Maximum seconds per batch before it is marked skipped")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--retag", action="store_true")
    parser.add_argument("--recent", action="store_true", help="Process newest pending cases first")
    parser.add_argument("--court", help="Restrict tagging to a court code, such as FC")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    with SessionLocal() as db:
        if args.retag:
            db.execute(delete(CaseTag).where(CaseTag.taxonomy_version == TAXONOMY_VERSION))
            db.execute(delete(CaseTaggingStatus).where(CaseTaggingStatus.taxonomy_version == TAXONOMY_VERSION))
            db.commit()
        if args.dry_run:
            cases = db.scalars(pending_case_query(court=args.court).limit(args.limit or 10)).all()
            tagger = CoreLegalTagger()
            count = sum(len(tagger.tag("\n".join(str(value) for value in (case.title, case.summary, case.full_text) if value))) for case in cases)
            print(f"pending_sample={len(cases)} preview_tags={count} taxonomy={TAXONOMY_VERSION}")
            return
        cases_tagged, tags_created, skipped_cases = tag_pending_cases(
            db, batch_size=args.batch_size, batch_timeout=args.batch_timeout, limit=args.limit, recent=args.recent, court=args.court
        )
        print(f"cases_tagged={cases_tagged} tags_created={tags_created} skipped_cases={skipped_cases} taxonomy={TAXONOMY_VERSION}")


if __name__ == "__main__":
    main()