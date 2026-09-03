"""Apply the independent Tagging V2 core whitelist to canonical cases."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from sqlalchemy import delete, exists, select
from sqlalchemy.orm import Session

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseTag, CaseTaggingStatus, SessionLocal
from backend.legal_tagger_v2 import CoreLegalTagger, TAXONOMY_VERSION

logger = logging.getLogger(__name__)


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


def tag_pending_cases(db: Session, *, batch_size: int = 100, limit: int | None = None, recent: bool = False, court: str | None = None) -> tuple[int, int]:
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")
    if limit is not None and limit < 1:
        raise ValueError("limit must be at least 1")
    tagger = CoreLegalTagger()
    cases_tagged = tags_created = last_case_id = 0
    while limit is None or cases_tagged < limit:
        size = min(batch_size, limit - cases_tagged) if limit else batch_size
        cases = db.scalars(pending_case_query(last_case_id=last_case_id, recent=recent, court=court).limit(size)).all()
        if not cases:
            break
        for case in cases:
            text = case.full_text or ""
            occurrences = tagger.tag_occurrences(text)
            db.add_all(CaseTag(case_id=case.id, category=tag.category, value=tag.value, score=tag.score,
                               evidence=tag.evidence, offset_start=tag.offset_start, offset_end=tag.offset_end,
                               source=tag.source, taxonomy_version=tag.taxonomy_version)
                       for tag in occurrences)
            db.add(CaseTaggingStatus(case_id=case.id, taxonomy_version=TAXONOMY_VERSION, tags_count=len(occurrences)))
            tags_created += len(occurrences)
        db.commit()
        cases_tagged += len(cases)
        last_case_id = cases[-1].id
        logger.info("Tagging V2 processed %d cases and created %d tags", cases_tagged, tags_created)
        if recent:
            break
    return cases_tagged, tags_created


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=100)
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
        cases_tagged, tags_created = tag_pending_cases(db, batch_size=args.batch_size, limit=args.limit, recent=args.recent, court=args.court)
        print(f"cases_tagged={cases_tagged} tags_created={tags_created} taxonomy={TAXONOMY_VERSION}")


if __name__ == "__main__":
    main()