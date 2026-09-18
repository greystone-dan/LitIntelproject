from __future__ import annotations

import argparse
import json
import re
from hashlib import sha256

from sqlalchemy import select

from backend.database import CaseChunk, Citation, SessionLocal


SIGNAL_PATTERNS: dict[str, tuple[str, ...]] = {
    "rule_language": (
        "test", "framework", "principle", "rule", "standard", "criteria",
        "elements", "factors", "requirements", "established", "set out",
        "held", "determined", "recognized",
    ),
    "comparison_language": (
        "similar", "similar to", "like", "resembles", "parallel", "comparable",
        "unlike", "different from", "distinguishable", "materially different",
    ),
    "authority_strength": (
        "binding", "controlling", "authoritative", "leading case", "settled law",
        "governing", "precedent", "subsequent jurisprudence", "later cases",
    ),
    "agreement_language": (
        "agree", "disagree", "accept", "adopt", "reject", "approve", "endorse",
        "decline", "persuasive", "unpersuasive",
    ),
    "application_language": (
        "apply", "applies", "applied", "applying", "falls within", "governed by", "under",
        "in accordance with", "consistent with", "on these facts", "in this case",
    ),
    "limitation_language": (
        "limited", "confined", "restricted", "narrow", "exception", "does not extend",
        "not applicable beyond",
    ),
    "explanation_language": (
        "because", "since", "given that", "in light of", "whereas", "due to",
    ),
    "party_position_language": (
        "applicant argues", "respondent argues", "minister argues", "counsel submits",
        "relies upon", "cites", "referred to", "contends", "maintains", "asserts",
    ),
}


def _signal_terms(text: str) -> dict[str, list[str]]:
    lowered = text.lower()
    return {
        category: [term for term in terms if re.search(r"(?<!\w)" + re.escape(term) + r"(?!\w)", lowered)]
        for category, terms in SIGNAL_PATTERNS.items()
    }


def _sentence_bounds(text: str, offset: int) -> tuple[int, int]:
    starts = [match.end() for match in re.finditer(r"[.!?](?:[\"']?\s+)", text[:offset])]
    start = starts[-1] if starts else 0
    end_match = re.search(r"[.!?](?:[\"']?\s+|$)", text[offset:])
    end = offset + end_match.end() if end_match else len(text)
    return start, end


def build_fixture(
    session,
    *,
    case_ids: list[int],
    limit: int,
    context_chars: int,
    after_context_chars: int | None = None,
    second_half_only: bool = True,
) -> list[dict[str, object]]:
    if context_chars < 0:
        raise ValueError("context_chars must be non-negative")
    if after_context_chars is None:
        after_context_chars = context_chars * 2
    if after_context_chars < 0:
        raise ValueError("after_context_chars must be non-negative")
    statement = (
        select(Citation, CaseChunk)
        .join(CaseChunk, CaseChunk.id == Citation.chunk_id)
        .where(
            Citation.offset_start.is_not(None),
            Citation.offset_end.is_not(None),
            CaseChunk.text.is_not(None),
        )
        .order_by(Citation.id)
        .limit(min(25_000, limit * 8 if second_half_only else limit))
    )
    if case_ids:
        statement = statement.where(Citation.source_case_id.in_(case_ids))
    rows: list[dict[str, object]] = []
    candidates = list(session.execute(statement))
    last_chunk_index_by_case: dict[int, int] = {}
    for citation, chunk in candidates:
        last_chunk_index_by_case[citation.source_case_id] = max(
            last_chunk_index_by_case.get(citation.source_case_id, 0),
            chunk.chunk_index,
        )
    selected = []
    for citation, chunk in candidates:
        case_midpoint = last_chunk_index_by_case[citation.source_case_id] / 2
        if second_half_only and chunk.chunk_index < case_midpoint:
            continue
        selected.append((citation, chunk))
        if len(selected) >= limit:
            break
    for index, (citation, chunk) in enumerate(selected, 1):
        start = max(0, citation.offset_start - context_chars)
        end = min(len(chunk.text), citation.offset_end + after_context_chars)
        text = chunk.text[start:end]
        citation_text = text[citation.offset_start - start : citation.offset_end - start]
        local_start = citation.offset_start - start
        sentence_start, sentence_end = _sentence_bounds(text, local_start)
        sentence = text[sentence_start:sentence_end].strip()
        signal_terms = _signal_terms(text)
        rows.append(
            {
                "example_id": f"citation-context-{index:04d}",
                "text": text,
                "source_text_sha256": sha256(text.encode("utf-8")).hexdigest(),
                "context_start_offset": start,
                "context_end_offset": end,
                "context_before_chars": citation.offset_start - start,
                "context_after_chars": end - citation.offset_end,
                "sentence": sentence,
                "left_context": text[:local_start],
                "right_context": text[local_start + len(citation_text):],
                "signal_terms": signal_terms,
                "signal_flags": {category: bool(terms) for category, terms in signal_terms.items()},
                "candidate_label": "review_required",
                "citations": [
                    {
                        "ordinal": 0,
                        "citation_text": citation_text,
                        "normalized_citation": citation.normalized_citation,
                        "start_offset": citation.offset_start - start,
                        "end_offset": citation.offset_end - start,
                    }
                ],
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a citation-centered treatment fixture without database writes.")
    parser.add_argument("--output", required=True, help="JSONL output path")
    parser.add_argument("--case-id", action="append", type=int, dest="case_ids")
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument(
        "--context-chars",
        type=int,
        default=1_000,
        help="Characters before each citation; the default post-citation context is twice this amount.",
    )
    parser.add_argument(
        "--after-context-chars",
        type=int,
        help="Characters after each citation; defaults to twice --context-chars.",
    )
    parser.add_argument(
        "--whole-decision",
        action="store_true",
        help="Include citations from the whole chunk instead of prioritizing the second half.",
    )
    args = parser.parse_args()
    if not 1 <= args.limit <= 2_500:
        parser.error("--limit must be between 1 and 2500")
    if not 50 <= args.context_chars <= 4_000:
        parser.error("--context-chars must be between 50 and 4000")
    if args.after_context_chars is not None and not 50 <= args.after_context_chars <= 8_000:
        parser.error("--after-context-chars must be between 50 and 8000")
    with SessionLocal() as session:
        rows = build_fixture(
            session,
            case_ids=args.case_ids or [],
            limit=args.limit,
            context_chars=args.context_chars,
            after_context_chars=args.after_context_chars,
            second_half_only=not args.whole_decision,
        )
    with open(args.output, "w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=True, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "read_only_fixture",
        "rows": len(rows),
        "output": args.output,
        "selection": "whole_chunk" if args.whole_decision else "second_half_only",
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
