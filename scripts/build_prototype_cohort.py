"""Build and operationalize prototype cohort for immigration case research.

Pipeline:
1) Combine the 300-case core list with exact-matched seed/canon cases.
2) Embed cohort cases that are not yet embedded.
3) Export citation map edges restricted to cohort-internal citations.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

import pandas as pd
from openai import OpenAI
from sqlalchemy import delete, select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseChunk, SessionLocal

CORE_300_CSV = Path("data/eval/core_immigration_cases.csv")
SEED_REPORT_CSV = Path("data/eval/reports/seed_case_cross_reference_100.csv")
OUT_IDS_CSV = Path("data/eval/prototype_case_ids_v1.csv")
OUT_NODES_CSV = Path("data/eval/reports/prototype_v1_citation_nodes.csv")
OUT_EDGES_CSV = Path("data/eval/reports/prototype_v1_citation_edges.csv")
OUT_SUMMARY_JSON = Path("data/eval/reports/prototype_v1_summary.json")

MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
CHUNK_CHARS = 6000
OVERLAP_CHARS = 600

NEUTRAL_RE = re.compile(r"\b(\d{4})\s+(FC|FCA|SCC|FCT|IRB|RPD|RAD|IAD|ID)\s+(\d+)\b", re.IGNORECASE)


@dataclass
class CohortCase:
    case_id: int
    from_core_300: bool
    from_seed_exact: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core-csv", type=Path, default=CORE_300_CSV)
    parser.add_argument("--seed-report-csv", type=Path, default=SEED_REPORT_CSV)
    parser.add_argument("--out-ids-csv", type=Path, default=OUT_IDS_CSV)
    parser.add_argument("--out-nodes-csv", type=Path, default=OUT_NODES_CSV)
    parser.add_argument("--out-edges-csv", type=Path, default=OUT_EDGES_CSV)
    parser.add_argument("--out-summary-json", type=Path, default=OUT_SUMMARY_JSON)
    parser.add_argument("--embed", action="store_true", help="Embed cohort cases missing embeddings")
    parser.add_argument("--force-reembed", action="store_true", help="Re-embed all cohort cases (deletes existing chunks for them)")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def normalize_neutral(text: str | None) -> str:
    if not text:
        return ""
    compact = " ".join(str(text).split()).strip().upper()
    compact = compact.replace(" FCT ", " FC ")
    return compact


def chunks(text: str) -> list[str]:
    result: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + CHUNK_CHARS, len(text))
        result.append(text[start:end])
        if end == len(text):
            break
        start = end - OVERLAP_CHARS
    return result


def collect_cohort(core_csv: Path, seed_report_csv: Path) -> list[CohortCase]:
    if not core_csv.exists():
        raise SystemExit(f"Missing core csv: {core_csv}")
    if not seed_report_csv.exists():
        raise SystemExit(f"Missing seed report csv: {seed_report_csv}")

    core = pd.read_csv(core_csv)
    seed = pd.read_csv(seed_report_csv)

    cohort_by_id: dict[int, CohortCase] = {}

    for value in core.get("local_case_id", pd.Series(dtype="float64")).dropna().tolist():
        case_id = int(value)
        cohort_by_id[case_id] = CohortCase(case_id=case_id, from_core_300=True, from_seed_exact=False)

    exact_seed = seed[seed["status"].isin(["in_db_exact", "in_core_exact"])]
    for value in exact_seed.get("matched_case_id", pd.Series(dtype="float64")).dropna().tolist():
        case_id = int(value)
        existing = cohort_by_id.get(case_id)
        if existing is None:
            cohort_by_id[case_id] = CohortCase(case_id=case_id, from_core_300=False, from_seed_exact=True)
        else:
            existing.from_seed_exact = True

    return sorted(cohort_by_id.values(), key=lambda item: item.case_id)


def export_cohort_ids(path: Path, cohort: list[CohortCase]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(
        [
            {
                "case_id": case.case_id,
                "from_core_300": case.from_core_300,
                "from_seed_exact": case.from_seed_exact,
            }
            for case in cohort
        ]
    )
    df.to_csv(path, index=False)


def embed_cohort_cases(session, cohort_ids: list[int], force_reembed: bool) -> dict[str, int]:
    rows = list(session.scalars(select(Case).where(Case.id.in_(cohort_ids)).order_by(Case.id)))
    cases_by_id = {case.id: case for case in rows}

    to_embed: list[Case] = []
    for case in rows:
        if force_reembed:
            to_embed.append(case)
            continue
        if case.processing_status != "embedded" or case.embedding is None:
            to_embed.append(case)

    if force_reembed and to_embed:
        session.execute(delete(CaseChunk).where(CaseChunk.case_id.in_([case.id for case in to_embed])))
        session.flush()

    all_chunks: list[tuple[Case, int, str]] = []
    for case in to_embed:
        text = case.full_text or case.summary or ""
        for idx, chunk_text in enumerate(chunks(text)):
            all_chunks.append((case, idx, chunk_text))

    if not all_chunks:
        return {
            "cohort_cases": len(cases_by_id),
            "embedded_now": 0,
            "chunk_rows_added": 0,
        }

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    responses = []
    for start in range(0, len(all_chunks), 100):
        batch = all_chunks[start:start + 100]
        resp = client.embeddings.create(model=MODEL, input=[text for _, _, text in batch])
        responses.extend(resp.data)

    by_case: dict[int, list[list[float]]] = {}
    for (case, idx, chunk_text), item in zip(all_chunks, responses):
        session.add(
            CaseChunk(
                case_id=case.id,
                chunk_index=idx,
                text=chunk_text,
                text_hash=sha256(chunk_text.encode("utf-8")).hexdigest(),
                token_estimate=max(1, len(chunk_text) // 4),
                embedding=item.embedding,
                embedding_model=MODEL,
            )
        )
        by_case.setdefault(case.id, []).append(item.embedding)

    for case in to_embed:
        vectors = by_case.get(case.id, [])
        if not vectors:
            continue
        case.embedding = [sum(vector[i] for vector in vectors) / len(vectors) for i in range(len(vectors[0]))]
        case.processing_status = "embedded"
        case.metadata_json = {
            **(case.metadata_json or {}),
            "embedding_model": MODEL,
            "embedding_chunk_count": len(vectors),
            "prototype_v1": True,
        }

    session.commit()
    return {
        "cohort_cases": len(cases_by_id),
        "embedded_now": len(to_embed),
        "chunk_rows_added": len(all_chunks),
    }


def extract_neutral_citations_from_text(text: str) -> list[str]:
    values: list[str] = []
    for match in NEUTRAL_RE.finditer(text):
        year, court, number = match.groups()
        values.append(normalize_neutral(f"{year} {court} {number}"))
    # preserve order while deduping
    deduped: list[str] = []
    seen: set[str] = set()
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        deduped.append(value)
    return deduped


def build_citation_map(session, cohort: list[CohortCase], out_nodes: Path, out_edges: Path) -> dict[str, int]:
    ids = [case.case_id for case in cohort]
    cohort_df = pd.DataFrame(
        [
            {
                "case_id": case.case_id,
                "from_core_300": case.from_core_300,
                "from_seed_exact": case.from_seed_exact,
            }
            for case in cohort
        ]
    )

    rows = list(session.scalars(select(Case).where(Case.id.in_(ids)).order_by(Case.id)))
    citation_to_case_id: dict[str, int] = {}
    for case in rows:
        key = normalize_neutral(case.citation)
        if key:
            citation_to_case_id[key] = case.id

    node_rows: list[dict[str, object]] = []
    edge_rows: list[dict[str, object]] = []

    cohort_flags = {row["case_id"]: row for _, row in cohort_df.iterrows()}

    for case in rows:
        flags = cohort_flags.get(case.id)
        node_rows.append(
            {
                "case_id": case.id,
                "citation": case.citation,
                "title": case.title,
                "court": case.court,
                "date": case.date,
                "from_core_300": bool(flags["from_core_300"]) if flags is not None else False,
                "from_seed_exact": bool(flags["from_seed_exact"]) if flags is not None else False,
            }
        )

        method = "cases_cited"
        cited_values: list[str] = []
        if isinstance(case.cases_cited, list) and case.cases_cited:
            cited_values = [normalize_neutral(value) for value in case.cases_cited if value]
        else:
            method = "regex"
            text = case.full_text or case.summary or ""
            cited_values = extract_neutral_citations_from_text(text)

        seen_targets: set[int] = set()
        for cited in cited_values:
            if not cited:
                continue
            target_id = citation_to_case_id.get(cited)
            if target_id is None or target_id == case.id or target_id in seen_targets:
                continue
            seen_targets.add(target_id)
            edge_rows.append(
                {
                    "source_case_id": case.id,
                    "target_case_id": target_id,
                    "normalized_citation": cited,
                    "method": method,
                }
            )

    out_nodes.parent.mkdir(parents=True, exist_ok=True)
    out_edges.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(node_rows).to_csv(out_nodes, index=False)
    pd.DataFrame(edge_rows).to_csv(out_edges, index=False)

    return {
        "nodes": len(node_rows),
        "edges": len(edge_rows),
    }


def main() -> None:
    args = parse_args()

    cohort = collect_cohort(args.core_csv, args.seed_report_csv)
    export_cohort_ids(args.out_ids_csv, cohort)

    embed_stats = {
        "cohort_cases": len(cohort),
        "embedded_now": 0,
        "chunk_rows_added": 0,
    }
    map_stats = {
        "nodes": 0,
        "edges": 0,
    }

    with SessionLocal() as session:
        ids = [case.case_id for case in cohort]
        if args.embed and not args.dry_run:
            embed_stats = embed_cohort_cases(session, ids, force_reembed=args.force_reembed)
        map_stats = build_citation_map(session, cohort, args.out_nodes_csv, args.out_edges_csv)

    summary = {
        "cohort_cases": len(cohort),
        "core_300_count": sum(1 for case in cohort if case.from_core_300),
        "seed_exact_count": sum(1 for case in cohort if case.from_seed_exact),
        "embed": args.embed,
        "force_reembed": args.force_reembed,
        **embed_stats,
        **map_stats,
        "out_ids_csv": str(args.out_ids_csv),
        "out_nodes_csv": str(args.out_nodes_csv),
        "out_edges_csv": str(args.out_edges_csv),
    }

    args.out_summary_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_summary_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"cohort_cases={summary['cohort_cases']}")
    print(f"core_300_count={summary['core_300_count']}")
    print(f"seed_exact_count={summary['seed_exact_count']}")
    print(f"embedded_now={summary['embedded_now']}")
    print(f"chunk_rows_added={summary['chunk_rows_added']}")
    print(f"citation_nodes={summary['nodes']}")
    print(f"citation_edges={summary['edges']}")
    print(f"summary_json={args.out_summary_json}")


if __name__ == "__main__":
    main()
