"""Extract citation evidence rows for FC-focused evaluation.

This script is read-only against the main case DB. It does not write citation rows.
Use it to produce transparent extraction evidence before pipeline integration changes.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import (
    NEUTRAL_CIT_RE,
    extract_raw_citation_matches,
    normalize_neutral_citation,
    resolve_neutral_to_case_id,
)
from backend.database import Case, SessionLocal

DEFAULT_OUT_CSV = Path("data/eval/reports/fc_citation_evidence.csv")
DEFAULT_SUMMARY_JSON = Path("data/eval/reports/fc_citation_evidence_summary.json")
PARA_MARKER_RE = re.compile(r"\[(\d+)\]")


@dataclass(frozen=True)
class ParagraphMarker:
    paragraph_number: int
    marker_offset: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-id", type=int, action="append", default=[])
    parser.add_argument("--case-ids-csv", type=Path, default=None, help="CSV with case_id or local_case_id column")
    parser.add_argument("--fc-only", action="store_true", help="Filter to probable Federal Court records")
    parser.add_argument("--limit-cases", type=int, default=None)
    parser.add_argument("--out-csv", type=Path, default=DEFAULT_OUT_CSV)
    parser.add_argument("--summary-json", type=Path, default=DEFAULT_SUMMARY_JSON)
    return parser.parse_args()


def _load_case_ids_from_csv(path: Path) -> list[int]:
    if not path.exists():
        raise SystemExit(f"Case ID CSV does not exist: {path}")

    results: list[int] = []
    with path.open("r", encoding="utf-8", newline="") as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            raw = row.get("case_id") or row.get("local_case_id")
            if raw is None or str(raw).strip() == "":
                continue
            try:
                results.append(int(str(raw).strip()))
            except ValueError:
                continue

    return results


def _collect_markers(text: str) -> list[ParagraphMarker]:
    markers: list[ParagraphMarker] = []
    for match in PARA_MARKER_RE.finditer(text):
        try:
            paragraph_number = int(match.group(1))
        except Exception:
            continue
        markers.append(ParagraphMarker(paragraph_number=paragraph_number, marker_offset=match.start()))
    return markers


def _paragraph_for_offset(markers: list[ParagraphMarker], offset: int) -> int | None:
    if not markers:
        return None

    best: ParagraphMarker | None = None
    for marker in markers:
        if marker.marker_offset <= offset:
            best = marker
        else:
            break
    return best.paragraph_number if best else markers[0].paragraph_number


def _resolve_status(session, kind: str, normalized_citation: str) -> tuple[int | None, str, str]:
    if kind == "neutral":
        target_case_id = resolve_neutral_to_case_id(session, normalized_citation)
        if target_case_id is not None:
            return target_case_id, "resolved", "neutral_exact"
        return None, "unresolved", "neutral_not_found"

    if kind == "case":
        embedded = NEUTRAL_CIT_RE.search(normalized_citation)
        if embedded is None:
            return None, "unresolved", "case_no_embedded_neutral"
        target_case_id = resolve_neutral_to_case_id(session, normalize_neutral_citation(embedded))
        if target_case_id is not None:
            return target_case_id, "resolved", "case_embedded_neutral"
        return None, "unresolved", "case_embedded_neutral_not_found"

    return None, "unresolved", "non_case_non_neutral"


def _is_probable_fc(case: Case) -> bool:
    court = (case.court or "").lower()
    citation = (case.citation or "").upper()
    source_url = (case.source_url or "").lower()
    return (
        "federal court" in court
        or court == "fc"
        or " FC " in f" {citation} "
        or "decisions.fct-cf.gc.ca" in source_url
    )


def main() -> None:
    args = parse_args()
    if args.limit_cases is not None and args.limit_cases < 1:
        raise SystemExit("--limit-cases must be at least 1")

    explicit_ids = list(args.case_id or [])
    if args.case_ids_csv:
        explicit_ids.extend(_load_case_ids_from_csv(args.case_ids_csv))
    explicit_ids = sorted(set(explicit_ids))

    summary: dict[str, object] = {
        "case_count": 0,
        "citations_total": 0,
        "resolved": 0,
        "unresolved": 0,
        "by_kind": {},
        "by_reason": {},
    }

    rows: list[dict[str, object]] = []
    by_kind: dict[str, int] = {}
    by_reason: dict[str, int] = {}

    with SessionLocal() as session:
        query = select(Case).order_by(Case.id)
        if explicit_ids:
            query = query.where(Case.id.in_(explicit_ids))
        cases = list(session.scalars(query))

        if args.fc_only:
            cases = [case for case in cases if _is_probable_fc(case)]

        if args.limit_cases is not None:
            cases = cases[: args.limit_cases]

        for case in cases:
            text = case.full_text or ""
            if not text.strip():
                continue
            markers = _collect_markers(text)
            extracted = extract_raw_citation_matches(text)

            for raw in extracted:
                target_case_id, status, reason = _resolve_status(session, raw.kind, raw.normalized_citation)
                paragraph_number = _paragraph_for_offset(markers, raw.offset_start)
                context_start = max(0, raw.offset_start - 80)
                context_end = min(len(text), raw.offset_end + 80)
                context = text[context_start:context_end].replace("\n", " ").strip()

                rows.append(
                    {
                        "source_case_id": case.id,
                        "source_case_title": case.title or "",
                        "source_case_citation": case.citation or "",
                        "citation_kind": raw.kind,
                        "citation_text": raw.citation_text,
                        "normalized_citation": raw.normalized_citation,
                        "offset_start": raw.offset_start,
                        "offset_end": raw.offset_end,
                        "paragraph_number": paragraph_number,
                        "target_case_id": target_case_id,
                        "resolution_status": status,
                        "resolution_reason": reason,
                        "context": context,
                    }
                )

                by_kind[raw.kind] = by_kind.get(raw.kind, 0) + 1
                by_reason[reason] = by_reason.get(reason, 0) + 1

    resolved = sum(1 for row in rows if row["resolution_status"] == "resolved")
    unresolved = sum(1 for row in rows if row["resolution_status"] != "resolved")

    summary["case_count"] = len(sorted({int(row["source_case_id"]) for row in rows}))
    summary["citations_total"] = len(rows)
    summary["resolved"] = resolved
    summary["unresolved"] = unresolved
    summary["by_kind"] = dict(sorted(by_kind.items()))
    summary["by_reason"] = dict(sorted(by_reason.items()))

    args.out_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.out_csv.open("w", encoding="utf-8", newline="") as file_obj:
        writer = csv.DictWriter(
            file_obj,
            fieldnames=[
                "source_case_id",
                "source_case_title",
                "source_case_citation",
                "citation_kind",
                "citation_text",
                "normalized_citation",
                "offset_start",
                "offset_end",
                "paragraph_number",
                "target_case_id",
                "resolution_status",
                "resolution_reason",
                "context",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    args.summary_json.parent.mkdir(parents=True, exist_ok=True)
    args.summary_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"evidence_rows={len(rows)}")
    print(f"resolved={resolved}")
    print(f"unresolved={unresolved}")
    print(f"out_csv={args.out_csv}")
    print(f"summary_json={args.summary_json}")


if __name__ == "__main__":
    main()
