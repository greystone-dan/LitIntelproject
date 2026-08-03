"""Build deterministic text and metadata tags for canonical cases."""

from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path
from typing import Any

from sqlalchemy import delete, exists, select
from sqlalchemy.orm import Session

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseTag, CaseTaggingStatus, SessionLocal
from backend.legal_tagger import LegalTag, LegalTagger, TAXONOMY_VERSION

logger = logging.getLogger(__name__)


def _slug(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(value).strip().lower()).strip("_")


def _metadata_tag(category: str, value: object, evidence: str) -> LegalTag | None:
    normalized = _slug(value)
    if not normalized:
        return None
    return LegalTag(category, normalized, 1.0, evidence, "structured_metadata", TAXONOMY_VERSION)


def build_case_tags(case: Any, tagger: LegalTagger) -> list[LegalTag]:
    text = "\n".join(
        str(value) for value in (getattr(case, "title", None), getattr(case, "summary", None), getattr(case, "full_text", None)) if value
    )
    tags = tagger.tag(text, language=getattr(case, "language", None))
    metadata = getattr(case, "metadata_json", None) or {}

    candidates = (
        _metadata_tag("court", getattr(case, "court", ""), f"court={getattr(case, 'court', '')}"),
        _metadata_tag("decision_year", getattr(getattr(case, "date", None), "year", ""), f"date={getattr(case, 'date', '')}"),
        _metadata_tag("source", getattr(case, "source_type", ""), f"source_type={getattr(case, 'source_type', '')}"),
        _metadata_tag("judge", metadata.get("judge", ""), f"metadata.judge={metadata.get('judge', '')}"),
    )
    tags.extend(tag for tag in candidates if tag is not None)

    docket = str(metadata.get("docket_number") or "")
    docket_match = re.match(r"([A-Za-z]+)-", docket)
    if docket_match:
        tag = _metadata_tag("docket_type", docket_match.group(1), f"metadata.docket_number={docket}")
        if tag:
            tags.append(tag)

    for topic in metadata.get("topic_keywords") or []:
        tag = _metadata_tag("legacy_topic", topic, f"metadata.topic_keywords={topic}")
        if tag:
            tags.append(tag)

    if getattr(case, "cases_cited", None):
        tags.append(LegalTag("citation_network", "cites_cases", 1.0, "cases_cited", "structured_metadata"))
    if (getattr(case, "citing_cases_count", None) or 0) > 0 or getattr(case, "cases_citing", None):
        tags.append(LegalTag("citation_network", "cited_by_cases", 1.0, "citing_cases_count", "structured_metadata"))

    deduplicated = {(tag.category, tag.value): tag for tag in tags}
    return sorted(deduplicated.values(), key=lambda tag: (tag.category, tag.value))


def pending_case_query(
    taxonomy_version: str,
    *,
    last_case_id: int = 0,
    court: str | None = None,
    source_type: str | None = None,
):
    already_tagged = exists(
        select(CaseTaggingStatus.id).where(
            CaseTaggingStatus.case_id == Case.id,
            CaseTaggingStatus.taxonomy_version == taxonomy_version,
        )
    )
    statement = select(Case).where(Case.id > last_case_id, ~already_tagged).order_by(Case.id)
    if court:
        statement = statement.where(Case.court == court)
    if source_type:
        statement = statement.where(Case.source_type == source_type)
    return statement


def tag_pending_cases(
    db: Session,
    tagger: LegalTagger,
    *,
    batch_size: int = 100,
    limit: int | None = None,
    court: str | None = None,
    source_type: str | None = None,
) -> tuple[int, int]:
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")
    if limit is not None and limit < 1:
        raise ValueError("limit must be at least 1")

    cases_tagged = 0
    tags_created = 0
    last_case_id = 0
    while limit is None or cases_tagged < limit:
        current_batch_size = min(batch_size, limit - cases_tagged) if limit else batch_size
        cases = db.scalars(
            pending_case_query(
                TAXONOMY_VERSION,
                last_case_id=last_case_id,
                court=court,
                source_type=source_type,
            ).limit(current_batch_size)
        ).all()
        if not cases:
            break

        for case in cases:
            tags = build_case_tags(case, tagger)
            db.add_all(
                CaseTag(
                    case_id=case.id,
                    category=tag.category,
                    value=tag.value,
                    score=tag.score,
                    evidence=tag.evidence,
                    source=tag.source,
                    taxonomy_version=tag.taxonomy_version,
                )
                for tag in tags
            )
            db.add(
                CaseTaggingStatus(
                    case_id=case.id,
                    taxonomy_version=TAXONOMY_VERSION,
                    tags_count=len(tags),
                )
            )
            tags_created += len(tags)

        db.commit()
        cases_tagged += len(cases)
        last_case_id = cases[-1].id
        logger.info("Tagged %d cases and created %d tags", cases_tagged, tags_created)

    return cases_tagged, tags_created


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--court", default=None)
    parser.add_argument("--source-type", default=None)
    parser.add_argument("--retag", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    with SessionLocal() as db:
        if args.retag:
            db.execute(delete(CaseTag).where(CaseTag.taxonomy_version == TAXONOMY_VERSION))
            db.execute(
                delete(CaseTaggingStatus).where(
                    CaseTaggingStatus.taxonomy_version == TAXONOMY_VERSION
                )
            )
            db.commit()

        if args.dry_run:
            pending = db.scalars(
                pending_case_query(
                    TAXONOMY_VERSION,
                    court=args.court,
                    source_type=args.source_type,
                ).limit(args.limit or 10)
            ).all()
            preview_tags = sum(len(build_case_tags(case, LegalTagger())) for case in pending)
            print(
                f"pending_sample={len(pending)} preview_tags={preview_tags} "
                f"taxonomy={TAXONOMY_VERSION}"
            )
            return

        cases_tagged, tags_created = tag_pending_cases(
            db,
            LegalTagger(),
            batch_size=args.batch_size,
            limit=args.limit,
            court=args.court,
            source_type=args.source_type,
        )
        print(
            f"cases_tagged={cases_tagged} tags_created={tags_created} "
            f"taxonomy={TAXONOMY_VERSION}"
        )


if __name__ == "__main__":
    main()
