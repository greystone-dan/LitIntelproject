"""Read-only source projection for the experimental treatment endpoint."""

from sqlalchemy import select

from .case_formatter import format_decision
from .citation_treatment import classify_paragraph, summarize_treatment, unknown_event
from .citations import CASE_CITATION_KINDS
from .database import Case, CaseChunk, Citation


def _absolute_span(citation, chunk, full_text):
    """Stored chunk offsets must reconstruct against a unique canonical chunk."""
    start, end = citation.offset_start, citation.offset_end
    if not isinstance(start, int) or not isinstance(end, int):
        return None
    if citation.chunk_id is not None:
        if chunk is None or chunk.case_id != citation.source_case_id or not chunk.text:
            return None
        base = full_text.find(chunk.text)
        if base < 0 or full_text.find(chunk.text, base + 1) >= 0:
            return None
        if not 0 <= start < end <= len(chunk.text):
            return None
        start, end = base + start, base + end
    if not 0 <= start < end <= len(full_text) or full_text[start:end] != citation.citation_text:
        return None
    return start, end


def citation_treatment_summary(db, case_id):
    """Read resolved incoming case citations; never write or recompute metrics.

    All stored case authorities in each citing decision are loaded to avoid
    attributing another authority's cue to the selected target. Numbered,
    canonical formatter paragraphs are required; unverifiable evidence abstains.
    """
    source_ids = select(Citation.source_case_id).where(
        Citation.target_case_id == case_id,
        Citation.source_case_id != case_id,
        Citation.citation_kind.in_(CASE_CITATION_KINDS),
    ).distinct()
    rows = list(db.execute(
        select(Citation, CaseChunk, Case)
        .join(Case, Case.id == Citation.source_case_id)
        .outerjoin(CaseChunk, CaseChunk.id == Citation.chunk_id)
        .where(Citation.source_case_id.in_(source_ids),
               Citation.citation_kind.in_(CASE_CITATION_KINDS))
        .order_by(Citation.source_case_id, Citation.id)
    ))
    sources, paragraphs, groups, missing = {}, {}, {}, []
    for citation, chunk, source in rows:
        sources[source.id] = source
        text = source.full_text or ""
        if source.id not in paragraphs:
            paragraphs[source.id] = [b for b in format_decision(text) if b["type"] == "para"]
        span = _absolute_span(citation, chunk, text)
        block = next((b for b in paragraphs[source.id]
                      if span and b["start"] <= span[0] < span[1] <= b["end"]), None)
        item = {
            "citation_id": citation.id, "target_case_id": citation.target_case_id,
            "citation_text": citation.citation_text,
            "start": span[0] - block["start"] if block else None,
            "end": span[1] - block["start"] if block else None,
        }
        if block:
            key = (source.id, block["start"], block["end"], block["num"])
            groups.setdefault(key, []).append(item)
        elif citation.target_case_id == case_id:
            missing.append({
                **unknown_event(item, "missing_or_unverified_canonical_paragraph"),
                "source_case_id": source.id, "source_title": source.title,
                "paragraph_number": None, "paragraph_start": None, "paragraph_end": None,
                "paragraph_text": None, "phrase_document_start": None,
                "phrase_document_end": None,
            })
    evidence = list(missing)
    for (source_id, start, end, number), citations in sorted(groups.items()):
        source = sources[source_id]
        text = source.full_text[start:end]
        for event in classify_paragraph(text, citations):
            if event["target_case_id"] != case_id:
                continue
            evidence.append({
                **event, "source_case_id": source_id, "source_title": source.title,
                "paragraph_number": number, "paragraph_start": start, "paragraph_end": end,
                "paragraph_text": text,
                "phrase_document_start": start + event["phrase_start"] if event["phrase_start"] is not None else None,
                "phrase_document_end": start + event["phrase_end"] if event["phrase_end"] is not None else None,
            })
    evidence.sort(key=lambda e: (e["source_case_id"], e["paragraph_start"] or 0,
                                 e["citation_id"], e["phrase_start"] or 0))
    return summarize_treatment(case_id, evidence)
