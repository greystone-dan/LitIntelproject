from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from sqlalchemy import select

from backend.citations import (
    extract_raw_citation_matches_legacy,
    extract_raw_citation_matches_v2,
)
from backend.database import CaseChunk, SessionLocal


DEFAULT_CSV = ROOT / "data" / "eval" / "fc_priority_seed_case_map.csv"
DEFAULT_OUT = ROOT / "data" / "eval" / "reports" / "citation_pipeline_ab_report.json"


def load_review_case_ids(path: Path) -> list[int]:
    if not path.exists():
        return []
    out: list[int] = []
    seen: set[int] = set()
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if str(row.get("status") or "") != "matched":
                continue
            raw = str(row.get("local_case_id") or "").strip()
            if not raw.isdigit():
                continue
            case_id = int(raw)
            if case_id in seen:
                continue
            seen.add(case_id)
            out.append(case_id)
    return out


def preferred_chunks(rows: list[CaseChunk]) -> list[CaseChunk]:
    by_set: dict[str, list[CaseChunk]] = defaultdict(list)
    for row in rows:
        by_set[(row.chunk_set or "legacy")].append(row)
    for chunk_set in ("section", "legacy", "paragraph"):
        if chunk_set in by_set:
            return sorted(by_set[chunk_set], key=lambda r: (r.chunk_index, r.id or 0))
    return sorted(rows, key=lambda r: (r.chunk_index, r.id or 0))


def summarize(matches) -> Counter:
    c = Counter()
    for m in matches:
        c["total"] += 1
        c[f"kind:{m.kind}"] += 1
    return c


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare legacy vs v2 citation extraction on review cohort.")
    parser.add_argument("--csv", type=str, default=str(DEFAULT_CSV))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--out", type=str, default=str(DEFAULT_OUT))
    args = parser.parse_args()

    case_ids = load_review_case_ids(Path(args.csv))
    if args.limit and args.limit > 0:
        case_ids = case_ids[: args.limit]

    session = SessionLocal()
    overall_legacy = Counter()
    overall_v2 = Counter()
    deltas: list[dict] = []

    try:
        for case_id in case_ids:
            chunks = list(
                session.scalars(
                    select(CaseChunk).where(CaseChunk.case_id == case_id).order_by(CaseChunk.chunk_index)
                )
            )
            active = preferred_chunks(chunks)
            text = "\n".join((chunk.text or "") for chunk in active)

            legacy = extract_raw_citation_matches_legacy(text)
            v2 = extract_raw_citation_matches_v2(text)

            sum_legacy = summarize(legacy)
            sum_v2 = summarize(v2)
            overall_legacy.update(sum_legacy)
            overall_v2.update(sum_v2)

            delta_total = sum_v2["total"] - sum_legacy["total"]
            if delta_total != 0:
                deltas.append(
                    {
                        "case_id": case_id,
                        "legacy_total": sum_legacy["total"],
                        "v2_total": sum_v2["total"],
                        "delta_total": delta_total,
                        "legacy_instrument": sum_legacy["kind:instrument"],
                        "v2_instrument": sum_v2["kind:instrument"],
                        "legacy_statute": sum_legacy["kind:statute"],
                        "v2_statute": sum_v2["kind:statute"],
                        "legacy_secondary": sum_legacy["kind:secondary"],
                        "v2_secondary": sum_v2["kind:secondary"],
                    }
                )
    finally:
        session.close()

    report = {
        "cases_evaluated": len(case_ids),
        "legacy": dict(overall_legacy),
        "v2": dict(overall_v2),
        "delta": {
            key: overall_v2.get(key, 0) - overall_legacy.get(key, 0)
            for key in sorted(set(overall_legacy.keys()) | set(overall_v2.keys()))
        },
        "top_case_deltas": sorted(deltas, key=lambda d: abs(d["delta_total"]), reverse=True)[:50],
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"cases_evaluated={report['cases_evaluated']}")
    print(f"legacy_total={overall_legacy.get('total', 0)}")
    print(f"v2_total={overall_v2.get('total', 0)}")
    print(f"delta_total={report['delta'].get('total', 0)}")
    print(f"report={out_path}")


if __name__ == "__main__":
    main()
