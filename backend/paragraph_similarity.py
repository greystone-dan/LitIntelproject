"""Bounded, stored-evidence paragraph matching; no embeddings or text inference."""

import re

from fastapi import HTTPException
from sqlalchemy import case as sql_case, func, select

from .case_formatter import DECISION_MARKER, format_decision
from .citations import CASE_CITATION_KINDS, _citation_variants
from .database import Case, CaseChunk, CaseTag, Citation
from .legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION
from .models import ParagraphSimilarityResponse

SOURCE_ROWS = 256
SIGNALS = 24
POSTINGS = 128
CANDIDATE_CASES = 32
PARAGRAPHS_PER_CASE = 64
PARAGRAPHS_TOTAL = 512
TEXT_CHARS = 12000


def _located_chunks(db, case_id, *, paragraph=None, budget=PARAGRAPHS_PER_CASE):
    """Fetch bounded paragraph text, never candidate full decisions or embeddings."""
    pos = sql_case((func.length(CaseChunk.text) <= TEXT_CHARS,
                    func.strpos(Case.full_text, CaseChunk.text)), else_=0)
    other = CaseChunk.__table__.alias("other_paragraph")
    duplicate = select(other.c.id).where(
        other.c.case_id == CaseChunk.case_id, other.c.chunk_set == "paragraph",
        other.c.paragraph_start == CaseChunk.paragraph_start,
        other.c.id != CaseChunk.id,
    ).exists()
    query = select(
        CaseChunk.id, CaseChunk.paragraph_start, CaseChunk.paragraph_end,
        func.substr(CaseChunk.text, 1, TEXT_CHARS + 1).label("text"), pos.label("pos"),
        duplicate.label("duplicate"),
        func.strpos(func.substr(Case.full_text, pos + 1), CaseChunk.text).label("repeat"),
        func.substr(Case.full_text, pos - 1, 1).label("previous"),
        sql_case(
            ((pos > 0) & (pos - 1 + func.length(CaseChunk.text) <= TEXT_CHARS),
             func.substr(Case.full_text, 1, pos - 1)),
            else_=None,
        ).label("prefix"),
        Case.title, Case.citation,
    ).join(Case, Case.id == CaseChunk.case_id).where(
        CaseChunk.case_id == case_id, CaseChunk.chunk_set == "paragraph",
    )
    if paragraph is not None:
        query = query.where(CaseChunk.paragraph_start == paragraph)
    rows = list(db.execute(query.order_by(CaseChunk.paragraph_start, CaseChunk.id).limit(budget)))
    verified = []
    for row in rows:
        if row.duplicate or not row.pos or row.repeat or (row.pos > 1 and row.previous != "\n"):
            continue
        bare = re.match(r"^\d{1,3}\s+(?=\S)", row.text)
        if bare:
            # Only complete, actual canonical context can establish SCC numbering.
            # The combined prefix and chunk is bounded; no invented marker or base.
            if row.prefix is None or len(row.prefix) != row.pos - 1:
                continue
            context = row.prefix + row.text
            if sum(line.strip() == DECISION_MARKER for line in context.split("\n")) != 1:
                continue
            blocks = format_decision(context)
            body_start = blocks[0]["end"]
            para_starts = {block["start"] for block in blocks if block["type"] == "para"}
            # A skipped bare number in the actual body breaks trustworthy context,
            # even if a later line happens to resume the formatter's sequence.
            if any(match.start() >= body_start and match.start() not in para_starts
                   for match in re.finditer(r"(?m)^\d{1,3}[^\S\n]+(?=\S)", context)):
                continue
            start = row.pos - 1
            if sum(block["type"] == "para" and block["num"] == row.paragraph_start
                   for block in blocks) != 1:
                continue
            blocks = [block for block in blocks if block["start"] >= start]
        else:
            blocks = format_decision(row.text)
            start = 0
        paras = [block for block in blocks if block["type"] == "para"]
        # Conservatively omit unnumbered, grouped, duplicated and footnote chunks.
        if (len(paras) != 1 or paras[0]["start"] != start
                or paras[0]["num"] != row.paragraph_start
                or row.paragraph_start != row.paragraph_end):
            continue
        verified.append(row)
    return verified, len(rows) >= budget, len(rows)


def _tag_query():
    return select(
        CaseTag,
        func.substr(Case.full_text, CaseTag.offset_start + 1,
                    CaseTag.offset_end - CaseTag.offset_start).label("exact"),
    ).join(Case, Case.id == CaseTag.case_id).where(
        CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
        CaseTag.offset_start >= 0, CaseTag.offset_end > CaseTag.offset_start,
        CaseTag.offset_end <= func.length(Case.full_text),
        CaseTag.offset_end - CaseTag.offset_start <= TEXT_CHARS,
        func.length(CaseTag.evidence) <= TEXT_CHARS,
    )


def _citation_query():
    # Occurrence offsets are chunk-local when chunk_id is present; canonical
    # rebuilds always leave short-form anchor offsets document-relative.
    pos = func.strpos(Case.full_text, CaseChunk.text)
    base = func.coalesce(pos - 1, 0)
    start = base + Citation.offset_start
    end = base + Citation.offset_end
    return select(
        Citation, start.label("start"), end.label("end"),
        func.substr(Case.full_text, start + 1, end - start).label("exact"),
        sql_case((Citation.citation_kind == "case_short",
                  func.substr(Case.full_text, Citation.anchor_offset_start + 1,
                              Citation.anchor_offset_end - Citation.anchor_offset_start)),
                 else_=None).label("anchor"),
    ).join(Case, Case.id == Citation.source_case_id).outerjoin(
        CaseChunk, CaseChunk.id == Citation.chunk_id,
    ).where(
        Citation.citation_kind.in_(sorted(CASE_CITATION_KINDS)),
        Citation.offset_start >= 0, Citation.offset_end > Citation.offset_start,
        start >= 0, end <= func.length(Case.full_text), end - start <= TEXT_CHARS,
        func.length(Citation.citation_text) <= TEXT_CHARS,
        (Citation.normalized_citation.is_(None)) | (func.length(Citation.normalized_citation) <= TEXT_CHARS),
        (Citation.anchor_citation_text.is_(None)) | (func.length(Citation.anchor_citation_text) <= TEXT_CHARS),
        (Citation.citation_kind != "case_short") | (
            (Citation.anchor_offset_start >= 0)
            & (Citation.anchor_offset_end > Citation.anchor_offset_start)
            & (Citation.anchor_offset_end <= start)
            & (Citation.anchor_offset_end <= func.length(Case.full_text))
            & (Citation.anchor_offset_end - Citation.anchor_offset_start <= TEXT_CHARS)
        ),
        (Citation.chunk_id.is_(None)) | (
            (CaseChunk.case_id == Citation.source_case_id) & (pos > 0)
            & (Citation.offset_end <= func.length(CaseChunk.text))
            & (func.strpos(func.substr(Case.full_text, pos + 1), CaseChunk.text) == 0)
        ),
    )


def _authority(row):
    citation = row[0]
    if not row.exact or row.exact != citation.citation_text:
        return None
    if citation.citation_kind == "case_short":
        if (not citation.anchor_citation_text or row.anchor != citation.anchor_citation_text
                or citation.anchor_offset_start is None
                or citation.anchor_offset_end is None
                or citation.anchor_offset_start < 0
                or citation.anchor_offset_end <= citation.anchor_offset_start):
            return None
    if citation.target_case_id is not None:
        return f"case:{citation.target_case_id}"
    # Existing resolver's formal citation keys omit pinpoints. Bare aliases are
    # not authority identities. Unresolved discovery uses exact indexed labels.
    label = citation.anchor_citation_text if citation.citation_kind == "case_short" else citation.normalized_citation
    variants = _citation_variants(label or "")
    return f"citation:{variants[0].replace(' FCT ', ' FC ')}" if variants else None


def _signals(paragraph, tags, citations):
    start, end = paragraph.pos - 1, paragraph.pos - 1 + len(paragraph.text)
    tag_set, authorities = set(), set()
    for tag, exact in tags:
        # V3 evidence and offsets are the exact canonical match
        # even when chunk_id is None. Never reinterpret them as chunk indices.
        if exact and exact == tag.evidence and start <= tag.offset_start < tag.offset_end <= end:
            tag_set.add((tag.category, tag.value))
    for row in citations:
        identity = _authority(row)
        if identity and start <= row.start < row.end <= end:
            authorities.add(identity)
    return tag_set, authorities


def _source_rows(db, model, owner_column, case_id, verification_query):
    ids = list(db.scalars(select(model.id).where(owner_column == case_id)
                          .order_by(model.id).limit(SOURCE_ROWS + 1)))
    rows = list(db.execute(verification_query.where(model.id.in_(ids[:SOURCE_ROWS]))
                          .order_by(model.id).limit(SOURCE_ROWS)))
    return rows, len(ids) > SOURCE_ROWS


def similar_paragraphs(case_id, paragraph_number, limit, db):
    """Score distinct shared tags one each and distinct authorities two each.

    Ties sort by case ID, then paragraph number.
    """
    if db.scalar(select(Case.id).where(Case.id == case_id).limit(1)) is None:
        raise HTTPException(404, "Case not found")
    source, partial, _ = _located_chunks(db, case_id, paragraph=paragraph_number, budget=2)
    if len(source) != 1:
        raise HTTPException(404, "No uniquely verified numbered paragraph available")
    source_tags, tags_capped = _source_rows(
        db, CaseTag, CaseTag.case_id, case_id, _tag_query())
    source_cites, cites_capped = _source_rows(
        db, Citation, Citation.source_case_id, case_id, _citation_query())
    partial |= tags_capped or cites_capped
    tags, authorities = _signals(source[0], source_tags, source_cites)
    partial |= len(tags) + len(authorities) > SIGNALS
    chosen = ([("tag", tag) for tag in sorted(tags)]
              + [("authority", authority) for authority in sorted(authorities)])[:SIGNALS]
    tags = {value for kind, value in chosen if kind == "tag"}
    authorities = {value for kind, value in chosen if kind == "authority"}
    candidate_tags, candidate_cites = {}, {}
    for kind, value in chosen:
        queries = []
        if kind == "tag":
            query = select(CaseTag.id, CaseTag.case_id.label("owner")).where(
                CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
                CaseTag.category == value[0], CaseTag.value == value[1],
                CaseTag.case_id != case_id).order_by(CaseTag.case_id, CaseTag.id)
            queries.append(query)
        else:
            if value.startswith("case:"):
                predicates = [Citation.target_case_id == int(value.split(":", 1)[1])]
            else:
                labels = sorted({row[0].normalized_citation for row in source_cites[:SOURCE_ROWS]
                                 if _authority(row) == value and row[0].normalized_citation})
                predicates = [Citation.normalized_citation == label for label in labels]
            for predicate in predicates:
                queries.append(select(Citation.id, Citation.source_case_id.label("owner")).where(
                    predicate, Citation.source_case_id != case_id,
                    Citation.citation_kind.in_(sorted(CASE_CITATION_KINDS))).order_by(
                        Citation.source_case_id, Citation.id))
        # Sorted-label seeks share one postings budget and at most one lookahead.
        # Charge fetched rows, not unique owners or the later verified evidence.
        remaining = POSTINGS
        for index, query in enumerate(queries):
            rows = list(db.execute(query.limit(remaining + 1)))
            partial |= len(rows) > remaining
            for row in rows[:remaining]:
                store = candidate_tags if kind == "tag" else candidate_cites
                store.setdefault(row.owner, set()).add(row.id)
            remaining -= min(len(rows), remaining)
            if remaining == 0:
                partial |= index + 1 < len(queries)
                break
    case_ids = sorted(set(candidate_tags) | set(candidate_cites))
    partial |= len(case_ids) > CANDIDATE_CASES
    results, checked, cases_checked = [], 0, 0
    for owner in case_ids[:CANDIDATE_CASES]:
        budget = min(PARAGRAPHS_PER_CASE, PARAGRAPHS_TOTAL - checked)
        if budget <= 0:
            partial = True
            break
        # Discovery reads only indexed IDs. Canonical verification happens only
        # for the bounded candidate cases, not every case in a posting list.
        verified_tags = list(db.execute(_tag_query().where(
            CaseTag.id.in_(sorted(candidate_tags.get(owner, set()))))
            .limit(POSTINGS * SIGNALS)))
        verified_cites = list(db.execute(_citation_query().where(
            Citation.id.in_(sorted(candidate_cites.get(owner, set()))))
            .limit(POSTINGS * SIGNALS)))
        paragraphs, capped, consumed = _located_chunks(db, owner, budget=budget)
        cases_checked += 1
        # Charge every fetched paragraph row, including unverified rows.
        checked += consumed
        partial |= capped
        for paragraph in paragraphs:
            found_tags, found_authorities = _signals(
                paragraph, verified_tags, verified_cites)
            shared_tags = sorted(tags & found_tags)
            shared_authorities = sorted(authorities & found_authorities)
            score = len(shared_tags) + 2 * len(shared_authorities)
            if score:
                results.append(dict(
                    case_id=owner, title=paragraph.title, citation=paragraph.citation,
                    paragraph_number=paragraph.paragraph_start,
                    excerpt=" ".join(paragraph.text.split())[:280], score=score,
                    shared_tags=[f"{category}:{value}" for category, value in shared_tags],
                    shared_authorities=shared_authorities,
                    why_matched=f"{len(shared_tags)} shared stored V3 legal tag(s) + "
                                f"{len(shared_authorities)} shared cited authority/authorities "
                                f"(two points each) = {score} points.",
                ))
    results.sort(key=lambda item: (-item["score"], item["case_id"], item["paragraph_number"]))
    return ParagraphSimilarityResponse(
        results=results[:limit],
        coverage=dict(
            partial=bool(partial), candidate_cases_checked=cases_checked,
            source_row_budget=SOURCE_ROWS, signal_budget=SIGNALS, postings_per_signal=POSTINGS,
            candidate_case_budget=CANDIDATE_CASES, paragraph_row_budget=PARAGRAPHS_TOTAL,
            note="Bounded stored-evidence search, not exhaustive corpus ranking. "
                 "Only uniquely located, numbered canonical paragraph chunks and verified spans count. "
                 "Unverified, oversized or ambiguous rows are omitted; statutes are separate. "
                 "Unresolved authorities use formal citation identities with exact stored-label discovery. "
                 + ("A budget was reached; coverage is partial." if partial else "No row budget was reached."),
        ),
    )
