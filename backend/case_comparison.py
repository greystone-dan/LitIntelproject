"""Read-only comparison of two canonical cases and their stored signals."""

import re
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Case, CaseOutcome, CaseTag, Citation, StatuteReference
from .citations import _citation_variants
from .legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION
from .statutes import normalize_provision_pinpoint


def _label(value: Any) -> str:
    return " ".join(value.split()) if isinstance(value, str) else ""


def _mapping(value: Any) -> dict:
    return value if isinstance(value, dict) else {}


_TRAILING_PINPOINT = re.compile(
    r"(?:,\s*(?:at\s+)?|\s+at\s+)(?:paras?\.?|paragraphs?|pp?\.|pages?)\s+"
    r"\d+(?:\s*(?:[-–,]|\band\b|\bto\b)\s*\d+)*[.]?$",
    re.IGNORECASE,
)


def _unresolved_authority_label(citation: Citation) -> str:
    """Project stored text only; never extract mentions or resolve a target."""
    labels = [_label(citation.normalized_citation), _label(citation.citation_text)]
    # Short aliases inherit only their stored anchor, not a guessed case match.
    anchor = _label(citation.anchor_citation_text) if citation.citation_kind == "case_short" else ""
    if anchor:
        labels.insert(0, anchor)
    for label in labels:
        variants = _citation_variants(label)
        if variants:
            # The helper orders neutral before reporter identities and supplies
            # the FC/FCT spelling aliases. No neutral/reporter equivalence lookup.
            return variants[0].replace(" FCT ", " FC ").casefold()
    label = next((value for value in labels if value), "")
    # Require an explicit suffix delimiter and a numeric pinpoint. Names such
    # as "Page 1" or "Paragraph 2 Ltd" must remain intact.
    return (_TRAILING_PINPOINT.sub("", label).strip() or label).casefold()


def _outcome(db: Session, case_id: int, metadata: dict) -> dict:
    # Match the canonical reader's latest-assignment selection, including ties.
    row = db.scalar(
        select(CaseOutcome).where(CaseOutcome.case_id == case_id)
        .order_by(CaseOutcome.updated_at.desc(), CaseOutcome.id.desc()).limit(1)
    )
    raw = row.decision_outcome if row is not None else metadata.get("decision outcome")
    normalized = _label(raw).casefold().replace(" ", "_")
    known = {"allowed", "dismissed", "granted", "denied", "refused",
             "set_aside", "remitted", "mixed", "withdrawn"}
    if row is not None:
        provenance = {
            "storage": "case_outcomes", "assignment_id": row.id,
            "source": row.source, "classifier_version": row.classifier_version,
            "updated_at": row.updated_at.isoformat() if row.updated_at else None,
            "confidence": row.confidence, "outcome_status": row.outcome_status,
            "disposition_evidence": row.disposition_evidence,
            "evidence_offset_start": row.evidence_offset_start,
            "evidence_offset_end": row.evidence_offset_end,
            "evidence_note": "Stored assignment evidence; not re-verified by comparison.",
        }
    else:
        provenance = {
            "storage": "metadata_fallback",
            "source": "cases.metadata_json.reader_extracted.decision outcome",
            "field_sources": _mapping(metadata.get("_field_sources")).get("decision outcome"),
            "confidence": _mapping(metadata.get("_field_confidence")).get("decision outcome"),
        }
    return {
        "label": normalized if normalized in known else "unclassified",
        "raw_label": raw, "provenance": provenance,
    }


def fetch_case_comparison(db: Session, a: int, b: int) -> dict[str, Any]:
    """Distinct identities, not mention counts. Never classify or persist data."""
    with db.no_autoflush:
        rows = db.execute(select(
            Case.id, Case.title, Case.citation, Case.court, Case.date, Case.metadata_json,
        ).where(Case.id.in_({a, b}))).mappings().all()
        cases = {row["id"]: row for row in rows}
        unknown = list(dict.fromkeys(case_id for case_id in (a, b) if case_id not in cases))
        if unknown:
            return {"status": "unknown_case", "unknown_ids": unknown}

        sides = {}
        signals = {}
        for side, case_id in (("a", a), ("b", b)):
            row = cases[case_id]
            metadata = _mapping(_mapping(row["metadata_json"]).get("reader_extracted"))
            sides[side] = {
                "case_id": case_id, "title": row["title"], "citation": row["citation"],
                "court": row["court"], "date": row["date"].isoformat() if row["date"] else None,
                "judge": metadata.get("judge"),
                "judge_source": "cases.metadata_json.reader_extracted.judge",
                "outcome": _outcome(db, case_id, metadata),
                "url": f"/data-explorer?case_id={case_id}",
            }
            tags = {}
            for category, value in db.execute(select(CaseTag.category, CaseTag.value).where(
                CaseTag.case_id == case_id,
                CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
            )):
                if _label(category) and _label(value):
                    # Taxonomy identity is exact category/value, not an inferred alias.
                    tags[(category, value)] = {"category": category, "value": value,
                                              "label": f"{category}:{value}"}
            authorities = {}
            for citation, target_id, target_citation, target_title in db.execute(
                select(Citation, Case.id, Case.citation, Case.title)
                .outerjoin(Case, Case.id == Citation.target_case_id)
                .where(
                    Citation.source_case_id == case_id,
                    Citation.citation_kind.in_(("neutral", "case", "case_short", "case_name", "unknown")),
                )
                .order_by(Citation.id)
            ):
                label = _label(citation.normalized_citation) or _label(citation.citation_text)
                if citation.target_case_id is not None:
                    key = ("target", citation.target_case_id)
                    label = (target_citation or target_title) if target_id is not None else label
                else:
                    label = _unresolved_authority_label(citation)
                    if not label:
                        continue
                    key = ("unresolved", label)
                authorities.setdefault(key, {
                    "label": label or f"Case {citation.target_case_id}",
                    "target_case_id": citation.target_case_id,
                    "resolved": citation.target_case_id is not None,
                    "url": f"/data-explorer?case_id={citation.target_case_id}"
                    if target_id is not None else None,
                })
            statutes = {}
            for ref in db.scalars(select(StatuteReference).where(
                StatuteReference.source_case_id == case_id,
            ).order_by(StatuteReference.id)):
                instrument = _label(ref.instrument_key).casefold()
                structured = "".join(
                    _label(value) if index == 0 else f"({_label(value)})"
                    for index, value in enumerate(
                        (ref.provision_section, ref.provision_subsection, ref.provision_paragraph)
                    ) if _label(value)
                )
                provision = normalize_provision_pinpoint(_label(ref.pinpoint) or structured).casefold()
                label = _label(ref.normalized_reference) or _label(ref.reference_text)
                if instrument:
                    key = ("instrument", instrument, provision)
                    label = f"{instrument} {provision}".strip()
                elif label:
                    key = ("unresolved", label.casefold())
                    label = label.casefold()
                else:
                    continue
                statutes.setdefault(key, {"label": label, "instrument_key": instrument or None,
                                         "provision": provision or None})
            signals[side] = {"tags": tags, "authorities": authorities, "statutes": statutes}

        sections = {}
        for section in ("tags", "statutes", "authorities"):
            left, right = signals["a"][section], signals["b"][section]
            shared = left.keys() & right.keys()
            sections[section] = {
                "counts": {"a": len(left), "b": len(right), "shared": len(shared),
                           "unique_a": len(left.keys() - right.keys()),
                           "unique_b": len(right.keys() - left.keys())},
                "items": [
                    {**(left.get(key) or right[key]), "in_a": key in left, "in_b": key in right,
                     "shared": key in shared}
                    for key in sorted(left.keys() | right.keys(), key=str)
                ],
            }
        return {
            "status": "ok", "cases": sides, **sections,
            "semantics": {
                "counts": "Distinct stored identities; repeated mentions count once.",
                "tags": f"Active taxonomy only: {ACTIVE_TAG_TAXONOMY_VERSION}",
                "authorities": (
                    "Resolved target case ID stays separate from unresolved identities. "
                    "Unresolved display labels are canonical stored neutral/reporter identifiers "
                    "(neutral first, FC/FCT folded), or case/whitespace-folded stored labels "
                    "with explicit trailing paragraph/page pinpoints removed. "
                    "Only case_short uses its stored anchor; no resolution or equivalence lookup."
                ),
                "statutes": "Instrument plus whitespace/case-normalized provision; ranges/lists retained; otherwise normalized unresolved label.",
                "outcomes": "Latest stored reader assignment; explicitly labelled metadata fallback only if absent.",
                "caution": "Stored coverage is not a finding of legal equivalence. Verify in the reader.",
            },
        }
