"""Run the case-type classifier over a stratified sample of A2AJ parquet files (read-only, no database).

Example:
    python scripts/case_types_eval.py --parquet-dir /path/to/parquets --per-stratum 40 --out out.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from multiprocessing import Pool
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

ERAS = ((0, 2009), (2010, 2014), (2015, 2019), (2020, 2100))
COURTS = ("FC", "FCA", "SCC", "RPD", "RAD")


def _work(row: dict) -> dict:
    from backend.case_types import classify_text

    text = row.pop("text")
    result = classify_text(text, court=row["court"], title=row["title"], docket=row.get("docket"),
                           source_citations=[row["citation"]])
    return {**row, "result": result.to_dict(), "excerpt": _excerpt(text)}


def _excerpt(text: str) -> str:
    start = text.find("Decision Content")
    start = start + 16 if start >= 0 else 0
    first = text.find("[1]", start)
    start = first if first >= 0 else start
    return " ".join(text[start:start + 1400].split())


def load_sample(parquet_dir: Path, per_stratum: int, seed: int, courts: tuple[str, ...]):
    import pandas as pd

    rows = []
    for court in courts:
        path = parquet_dir / f"{court}.parquet"
        if not path.exists():
            continue
        frame = pd.read_parquet(path, columns=["citation_en", "name_en", "document_date_en", "unofficial_text_en", "unofficial_text_fr", "citation_fr"])
        frame["year"] = frame["document_date_en"].dt.year
        for low, high in ERAS:
            part = frame[(frame["year"] >= low) & (frame["year"] <= high)]
            if part.empty:
                continue
            for _, record in part.sample(min(per_stratum, len(part)), random_state=seed).iterrows():
                text = record["unofficial_text_en"] if isinstance(record["unofficial_text_en"], str) and record["unofficial_text_en"] else record["unofficial_text_fr"]
                if not isinstance(text, str):
                    continue
                docket = None
                marker = text.find("File numbers")
                if marker >= 0:
                    docket = " ".join(text[marker:marker + 80].split())
                rows.append({"court": court, "era": f"{low}-{high}", "citation": record["citation_en"] or record["citation_fr"] or "",
                             "title": record["name_en"] or "", "year": int(record["year"]) if record["year"] == record["year"] else None,
                             "docket": docket, "text": text})
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parquet-dir", required=True, type=Path)
    parser.add_argument("--per-stratum", type=int, default=40)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--courts", default=",".join(COURTS))
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    rows = load_sample(args.parquet_dir, args.per_stratum, args.seed, tuple(args.courts.split(",")))
    with Pool(args.workers) as pool, args.out.open("w", encoding="utf-8") as handle:
        for done, item in enumerate(pool.imap_unordered(_work, rows, chunksize=4), 1):
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")
            if done % 100 == 0:
                print(done, "of", len(rows), flush=True)


if __name__ == "__main__":
    main()
