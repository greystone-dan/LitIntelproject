"""Map normalized FC/CanLII seed links to local case IDs.

This creates a deterministic bridge from seed links to local DB cases so
citation evidence extraction can run on a concrete case set.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from sqlalchemy import func, or_, select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal

DEFAULT_SEED_CSV = Path("data/eval/fc_priority_seed_links.csv")
DEFAULT_OUT_CSV = Path("data/eval/fc_priority_seed_case_map.csv")
DEFAULT_SUMMARY_JSON = Path("data/eval/fc_priority_seed_case_map_summary.json")

CANLII_DOC_PARTS_RE = re.compile(r"^(?P<year>\d{4})(?P<court>[a-z]+)(?P<num>\d+)$", re.IGNORECASE)


@dataclass(frozen=True)
class SeedRow:
    source_file: str
    source_row: str
    priority_group: str
    source_system: str
    raw_url: str
    normalized_url: str
    item_id: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-csv", type=Path, default=DEFAULT_SEED_CSV)
    parser.add_argument("--out-csv", type=Path, default=DEFAULT_OUT_CSV)
    parser.add_argument("--summary-json", type=Path, default=DEFAULT_SUMMARY_JSON)
    parser.add_argument("--limit", type=int, default=None)
    return parser.parse_args()


def _norm_ws_upper(value: str | None) -> str:
    return " ".join(str(value or "").split()).strip().upper()


def _neutral_from_canlii_docid(docid: str) -> str | None:
    match = CANLII_DOC_PARTS_RE.match(docid)
    if not match:
        return None

    year = match.group("year")
    court = match.group("court").upper()
    num = int(match.group("num"))

    if court == "FCT":
        court = "FC"

    if court in {"FC", "FCA", "SCC"}:
        return f"{year} {court} {num}"

    return None


def _load_seed_rows(path: Path) -> list[SeedRow]:
    if not path.exists():
        raise SystemExit(f"Seed CSV does not exist: {path}")

    rows: list[SeedRow] = []
    with path.open("r", encoding="utf-8", newline="") as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            rows.append(
                SeedRow(
                    source_file=str(row.get("source_file") or ""),
                    source_row=str(row.get("source_row") or ""),
                    priority_group=str(row.get("priority_group") or ""),
                    source_system=str(row.get("source_system") or ""),
                    raw_url=str(row.get("raw_url") or ""),
                    normalized_url=str(row.get("normalized_url") or ""),
                    item_id=str(row.get("item_id") or ""),
                )
            )
    return rows


def _find_by_source_url(session, normalized_url: str) -> list[Case]:
    return list(session.scalars(select(Case).where(Case.source_url == normalized_url).order_by(Case.id)))


def _find_by_citation(session, citation: str) -> list[Case]:
    normalized = _norm_ws_upper(citation)
    if not normalized:
        return []

    return list(
        session.scalars(
            select(Case)
            .where(
                or_(
                    func.upper(func.regexp_replace(func.coalesce(Case.citation, ""), r"\\s+", " ", "g")) == normalized,
                    func.upper(func.regexp_replace(func.coalesce(Case.secondary_citation, ""), r"\\s+", " ", "g"))
                    == normalized,
                )
            )
            .order_by(Case.id)
        )
    )


def main() -> None:
    args = parse_args()
    if args.limit is not None and args.limit < 1:
        raise SystemExit("--limit must be at least 1")

    seeds = _load_seed_rows(args.seed_csv)
    if args.limit is not None:
        seeds = seeds[: args.limit]

    mapped_rows: list[dict[str, object]] = []
    counts = {
        "total": len(seeds),
        "matched": 0,
        "missing": 0,
        "ambiguous": 0,
        "matched_by_source_url": 0,
        "matched_by_citation": 0,
    }

    with SessionLocal() as session:
        for seed in seeds:
            status = "missing"
            match_method = "none"
            local_case_id: int | None = None
            matched_title = ""
            matched_citation = ""
            inferred_neutral = ""

            source_url_matches = _find_by_source_url(session, seed.normalized_url)
            matches: list[Case] = source_url_matches
            if source_url_matches:
                match_method = "source_url"
            else:
                if seed.source_system == "canlii":
                    neutral = _neutral_from_canlii_docid(seed.item_id)
                    inferred_neutral = neutral or ""
                    if neutral:
                        citation_matches = _find_by_citation(session, neutral)
                        if citation_matches:
                            matches = citation_matches
                            match_method = "citation"

            if len(matches) == 1:
                case = matches[0]
                local_case_id = int(case.id)
                matched_title = str(case.title or "")
                matched_citation = str(case.citation or "")
                status = "matched"
                counts["matched"] += 1
                if match_method == "source_url":
                    counts["matched_by_source_url"] += 1
                elif match_method == "citation":
                    counts["matched_by_citation"] += 1
            elif len(matches) > 1:
                status = "ambiguous"
                counts["ambiguous"] += 1
            else:
                counts["missing"] += 1

            mapped_rows.append(
                {
                    "source_file": seed.source_file,
                    "source_row": seed.source_row,
                    "priority_group": seed.priority_group,
                    "source_system": seed.source_system,
                    "raw_url": seed.raw_url,
                    "normalized_url": seed.normalized_url,
                    "item_id": seed.item_id,
                    "inferred_neutral_citation": inferred_neutral,
                    "status": status,
                    "match_method": match_method,
                    "local_case_id": local_case_id,
                    "matched_title": matched_title,
                    "matched_citation": matched_citation,
                }
            )

    args.out_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.out_csv.open("w", encoding="utf-8", newline="") as file_obj:
        writer = csv.DictWriter(
            file_obj,
            fieldnames=[
                "source_file",
                "source_row",
                "priority_group",
                "source_system",
                "raw_url",
                "normalized_url",
                "item_id",
                "inferred_neutral_citation",
                "status",
                "match_method",
                "local_case_id",
                "matched_title",
                "matched_citation",
            ],
        )
        writer.writeheader()
        writer.writerows(mapped_rows)

    args.summary_json.parent.mkdir(parents=True, exist_ok=True)
    args.summary_json.write_text(json.dumps(counts, indent=2), encoding="utf-8")

    print(f"seed_csv={args.seed_csv}")
    print(f"mapped_csv={args.out_csv}")
    print(f"summary_json={args.summary_json}")
    print(f"total={counts['total']} matched={counts['matched']} missing={counts['missing']} ambiguous={counts['ambiguous']}")


if __name__ == "__main__":
    main()
