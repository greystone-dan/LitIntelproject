"""Database side of the paragraph cited-by batch: write per citing case, read for the reader."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable, Sequence
from datetime import date

from sqlalchemy import delete, exists, func, select
from sqlalchemy.orm import Session

from backend.database import (
    Case,
    CaseChunk,
    Citation,
    ParagraphCitationEdge,
    ParagraphCitationStatus,
)
from backend.citation_refine.pinpoints import target_paragraphs
from backend.paragraph_cited_by import (
    ALGO_VERSION,
    PURPOSE_LABELS,
    Occurrence,
    build_edges,
    citer_sort_key,
    summarise_purposes,
)

TOP_CITERS_PER_PARAGRAPH = 8


ID_WINDOW = 5000


def pending_source_ids(
    db: Session,
    after_id: int = 0,
    limit: int = 50,
    window: int = ID_WINDOW,
    *,
    include_all_cases: bool = False,
) -> list[int]:
    """Cases missing the current cited-by status.

    Default behavior matches the original bulk job: only citing cases that already
    have at least one resolved outgoing citation. Set ``include_all_cases`` for the
    incremental path that also covers canonical cases with no citations yet.
    Looks at a bounded range of case ids at a time (``window``), so no single
    query ever scans the whole table, however sparse the remaining work is.
    """
    top = db.scalar(select(func.max(Case.id))) or 0
    if include_all_cases:
        done = exists().where(
            ParagraphCitationStatus.source_case_id == Case.id,
            ParagraphCitationStatus.algo_version == ALGO_VERSION,
        )
    else:
        done = exists().where(
            ParagraphCitationStatus.source_case_id == Citation.source_case_id,
            ParagraphCitationStatus.algo_version == ALGO_VERSION,
        )
    found: list[int] = []
    low = after_id
    while low < top and len(found) < limit:
        high = low + window
        if include_all_cases:
            query = (
                select(Case.id)
                .where(Case.id > low, Case.id <= high, ~done)
                .order_by(Case.id)
                .limit(limit - len(found))
            )
        else:
            query = (
                select(Citation.source_case_id)
                .where(
                    Citation.source_case_id > low,
                    Citation.source_case_id <= high,
                    Citation.target_case_id.is_not(None),
                    ~done,
                )
                .group_by(Citation.source_case_id)
                .order_by(Citation.source_case_id)
                .limit(limit - len(found))
            )
        found.extend(db.scalars(query))
        low = high
    return found


def count_processed_sources(db: Session) -> int:
    """Citing cases already processed at this version (a cheap count of the small status table)."""
    return int(
        db.scalar(
            select(func.count()).select_from(ParagraphCitationStatus).where(
                ParagraphCitationStatus.algo_version == ALGO_VERSION
            )
        )
        or 0
    )


def count_pending_sources(db: Session, include_all_cases: bool = False) -> tuple[int, int]:
    """(pending cases, of which already processed at this version)."""
    if include_all_cases:
        total = db.scalar(select(func.count()).select_from(Case)) or 0
    else:
        total = db.scalar(
            select(func.count(func.distinct(Citation.source_case_id))).where(Citation.target_case_id.is_not(None))
        ) or 0
    processed = db.scalar(
        select(func.count()).select_from(ParagraphCitationStatus).where(
            ParagraphCitationStatus.algo_version == ALGO_VERSION
        )
    ) or 0
    return int(total), int(processed)


def compute_source_edges(db: Session, source_case_id: int):
    """Edges for one citing case, read-only. Returns ``(edges, occurrences_used)``."""
    text = db.scalar(select(Case.full_text).where(Case.id == source_case_id)) or ""
    if not text:
        return [], 0
    rows = db.execute(
        select(
            Citation.target_case_id,
            Citation.citation_text,
            Citation.normalized_citation,
            Citation.target_paragraph,
            Citation.chunk_id,
            Citation.offset_start,
            Citation.offset_end,
        ).where(Citation.source_case_id == source_case_id)
    ).all()
    chunk_ids = {row.chunk_id for row in rows if row.chunk_id is not None}
    chunk_starts: dict[int, int] = {}
    if chunk_ids:
        cursor = 0  # chunks come in reading order, so look forward from the last hit before searching the whole text
        for chunk_id, chunk_text in db.execute(
            select(CaseChunk.id, CaseChunk.text).where(CaseChunk.id.in_(chunk_ids)).order_by(CaseChunk.chunk_index)
        ):
            position = text.find(chunk_text, cursor)
            if position < 0:
                position = text.find(chunk_text)
            if position >= 0:
                chunk_starts[chunk_id] = position
                cursor = position
    occurrences: list[Occurrence] = []
    spans: list[tuple[int, int]] = []
    for row in rows:
        if row.offset_start is None or row.offset_end is None:
            continue
        shift = 0
        if row.chunk_id is not None:
            if row.chunk_id not in chunk_starts:
                continue  # cannot place a chunk-relative offset in the full text
            shift = chunk_starts[row.chunk_id]
        start, end = row.offset_start + shift, row.offset_end + shift
        if not 0 <= start < end <= len(text):
            continue
        spans.append((start, end))
        if row.target_case_id is None or row.target_case_id == source_case_id:
            continue
        pins = target_paragraphs(row.citation_text, row.normalized_citation, row.target_paragraph)
        if pins is None:
            continue
        # "paras 45-48" is one mention of each paragraph it names.
        for paragraph in pins.paragraphs:
            occurrences.append(Occurrence(int(row.target_case_id), paragraph, start, end))
    return build_edges(text, occurrences, spans), len(occurrences)


def invalidate_source_edges(db: Session, source_case_id: int) -> None:
    """Forget one source case in the caller's transaction after locking the source row."""
    db.scalar(select(Case.id).where(Case.id == source_case_id).with_for_update())
    db.execute(delete(ParagraphCitationEdge).where(ParagraphCitationEdge.source_case_id == source_case_id))
    db.execute(delete(ParagraphCitationStatus).where(ParagraphCitationStatus.source_case_id == source_case_id))


def write_source_edges(db: Session, source_case_id: int, edges: Sequence) -> int:
    """Replace this citing case's edges and mark it processed, in the caller's transaction."""
    db.execute(delete(ParagraphCitationEdge).where(ParagraphCitationEdge.source_case_id == source_case_id))
    db.add_all(
        ParagraphCitationEdge(
            source_case_id=source_case_id,
            target_case_id=edge.target_case_id,
            target_paragraph=edge.target_paragraph,
            mentions=edge.mentions,
            purpose=edge.purpose,
            purpose_counts=edge.purpose_counts,
            signal=edge.signal,
            algo_version=ALGO_VERSION,
        )
        for edge in edges
    )
    status = db.get(ParagraphCitationStatus, source_case_id)
    if status is None:
        db.add(ParagraphCitationStatus(source_case_id=source_case_id, algo_version=ALGO_VERSION, edges=len(edges)))
    else:
        status.algo_version = ALGO_VERSION
        status.edges = len(edges)
        status.computed_at = func.now()
    return len(edges)


def _coverage(db: Session, target_ids: Iterable[int]) -> dict[int, tuple[int, int]]:
    """Per cited case: (distinct citing cases, of which processed at this version)."""
    ids = sorted({int(t) for t in target_ids})
    if not ids:
        return {}
    totals = dict(
        db.execute(
            select(Citation.target_case_id, func.count(func.distinct(Citation.source_case_id)))
            .where(Citation.target_case_id.in_(ids), Citation.source_case_id != Citation.target_case_id)
            .group_by(Citation.target_case_id)
        ).all()
    )
    done = dict(
        db.execute(
            select(Citation.target_case_id, func.count(func.distinct(Citation.source_case_id)))
            .join(ParagraphCitationStatus, ParagraphCitationStatus.source_case_id == Citation.source_case_id)
            .where(
                Citation.target_case_id.in_(ids),
                Citation.source_case_id != Citation.target_case_id,
                ParagraphCitationStatus.algo_version == ALGO_VERSION,
            )
            .group_by(Citation.target_case_id)
        ).all()
    )
    return {t: (int(totals.get(t, 0)), int(done.get(t, 0))) for t in ids}


def load_paragraph_cited_by(db: Session, case_id: int) -> dict | None:
    """Stored "cited by" for every paragraph of one case, or None when the batch has not covered it."""
    total, processed = _coverage(db, [case_id]).get(case_id, (0, 0))
    if total == 0 or processed == 0:
        return None
    rows = db.execute(
        select(
            ParagraphCitationEdge.target_paragraph,
            ParagraphCitationEdge.source_case_id,
            ParagraphCitationEdge.mentions,
            ParagraphCitationEdge.purpose,
            ParagraphCitationEdge.purpose_counts,
            ParagraphCitationEdge.signal,
            Case.title,
            Case.citation,
            Case.court,
            Case.date,
        )
        .join(Case, Case.id == ParagraphCitationEdge.source_case_id)
        .where(ParagraphCitationEdge.target_case_id == case_id, ParagraphCitationEdge.source_case_id != case_id)
    ).all()
    by_paragraph: dict[int, list] = defaultdict(list)
    for row in rows:
        by_paragraph[int(row.target_paragraph)].append(row)
    paragraphs = []
    for paragraph, group in sorted(by_paragraph.items()):
        citers = [
            {
                "case_id": r.source_case_id,
                "title": r.title,
                "citation": r.citation,
                "court": r.court,
                "date": r.date.isoformat() if isinstance(r.date, date) else None,
                "date_ordinal": r.date.toordinal() if isinstance(r.date, date) else 0,
                "mentions": int(r.mentions),
                "purpose": r.purpose,
                "signal": r.signal,
            }
            for r in group
        ]
        citers.sort(key=citer_sort_key)
        for citer in citers:
            citer.pop("date_ordinal")
        paragraphs.append(
            {
                "paragraph": paragraph,
                "citer_count": len(group),
                "mention_count": sum(int(r.mentions) for r in group),
                "purposes": summarise_purposes(r.purpose_counts or {r.purpose: int(r.mentions)} for r in group),
                "citers": citers[:TOP_CITERS_PER_PARAGRAPH],
            }
        )
    return {
        "algo_version": ALGO_VERSION,
        "coverage": {"sources_total": total, "sources_processed": processed, "complete": processed >= total},
        "purpose_labels": PURPOSE_LABELS,
        "paragraphs": paragraphs,
    }


def load_target_cited_by(db: Session, pinpoints: Iterable[tuple[int, int]]) -> dict[tuple[int, int], dict]:
    """Stored cited-by summary for (cited case, paragraph) pairs, only where the batch covered that case."""
    wanted = {(int(c), int(p)) for c, p in pinpoints}
    summaries = load_pinpoint_cited_by(db, {(c, (p,)) for c, p in wanted})
    return {(c, p): summaries[(c, (p,))] for c, p in wanted if (c, (p,)) in summaries}


def load_pinpoint_cited_by(db: Session, pinpoints: Iterable[tuple[int, tuple[int, ...]]]) -> dict[tuple[int, tuple[int, ...]], dict]:
    """Stored cited-by summary for (cited case, paragraphs) pinpoints, e.g. "paras 45-48".

    Cases that cite any of the named paragraphs are counted once; mentions are summed.
    """
    wanted = {(int(c), tuple(int(p) for p in ps)) for c, ps in pinpoints if ps}
    if not wanted:
        return {}
    coverage = _coverage(db, {c for c, _ in wanted})
    complete = {c for c, (total, done) in coverage.items() if total > 0 and done >= total}
    if not complete:
        return {}
    rows = db.execute(
        select(
            ParagraphCitationEdge.source_case_id,
            ParagraphCitationEdge.target_case_id,
            ParagraphCitationEdge.target_paragraph,
            ParagraphCitationEdge.mentions,
            ParagraphCitationEdge.purpose,
            ParagraphCitationEdge.purpose_counts,
        ).where(ParagraphCitationEdge.target_case_id.in_(complete))
    ).all()
    by_case: dict[int, list] = defaultdict(list)
    for row in rows:
        by_case[int(row.target_case_id)].append(row)
    result: dict[tuple[int, tuple[int, ...]], dict] = {}
    for key in wanted:
        case_id, paragraphs = key
        group = [r for r in by_case.get(case_id, ()) if int(r.target_paragraph) in paragraphs]
        if not group:
            continue
        result[key] = {
            "citer_count": len({int(r.source_case_id) for r in group}),
            "mention_count": sum(int(r.mentions) for r in group),
            "purposes": summarise_purposes(r.purpose_counts or {r.purpose: int(r.mentions)} for r in group),
        }
    return result
