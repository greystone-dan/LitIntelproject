"""Run FC citation evidence extraction in deterministic batches and merge outputs."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

DEFAULT_CASE_MAP_CSV = Path("data/eval/fc_priority_seed_case_map.csv")
DEFAULT_OUT_CSV = Path("data/eval/reports/fc_citation_evidence_seed422.csv")
DEFAULT_SUMMARY_JSON = Path("data/eval/reports/fc_citation_evidence_seed422_summary.json")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-map-csv", type=Path, default=DEFAULT_CASE_MAP_CSV)
    parser.add_argument("--out-csv", type=Path, default=DEFAULT_OUT_CSV)
    parser.add_argument("--summary-json", type=Path, default=DEFAULT_SUMMARY_JSON)
    parser.add_argument("--batch-size", type=int, default=25)
    parser.add_argument("--fc-only", action="store_true", default=True)
    parser.add_argument("--keep-temp", action="store_true")
    return parser.parse_args()


def _load_matched_case_ids(path: Path) -> list[int]:
    if not path.exists():
        raise SystemExit(f"Case map CSV not found: {path}")

    case_ids: list[int] = []
    with path.open("r", encoding="utf-8", newline="") as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            if str(row.get("status") or "") != "matched":
                continue
            raw_id = str(row.get("local_case_id") or "").strip()
            if not raw_id:
                continue
            try:
                case_ids.append(int(raw_id))
            except ValueError:
                continue

    return sorted(set(case_ids))


def _chunk(values: list[int], size: int) -> list[list[int]]:
    return [values[index:index + size] for index in range(0, len(values), size)]


def main() -> None:
    args = parse_args()
    if args.batch_size < 1:
        raise SystemExit("--batch-size must be at least 1")

    case_ids = _load_matched_case_ids(args.case_map_csv)
    if not case_ids:
        raise SystemExit("No matched case IDs found in case map CSV")

    batches = _chunk(case_ids, args.batch_size)

    temp_dir = args.out_csv.parent / "_tmp_fc_evidence_batches"
    temp_dir.mkdir(parents=True, exist_ok=True)

    merged_rows: list[dict[str, object]] = []
    totals = {
        "batch_count": len(batches),
        "matched_case_count": len(case_ids),
        "case_count": 0,
        "citations_total": 0,
        "resolved": 0,
        "unresolved": 0,
        "by_kind": {},
        "by_reason": {},
    }

    for idx, batch in enumerate(batches, start=1):
        batch_csv = temp_dir / f"batch_{idx:04d}.csv"
        batch_summary = temp_dir / f"batch_{idx:04d}_summary.json"

        cmd = [
            sys.executable,
            "scripts/extract_fc_citation_evidence.py",
            "--out-csv",
            str(batch_csv),
            "--summary-json",
            str(batch_summary),
        ]
        if args.fc_only:
            cmd.append("--fc-only")
        for case_id in batch:
            cmd.extend(["--case-id", str(case_id)])

        print(f"running_batch={idx}/{len(batches)} cases={len(batch)}")
        subprocess.run(cmd, check=True)

        with batch_csv.open("r", encoding="utf-8", newline="") as file_obj:
            rows = list(csv.DictReader(file_obj))
            merged_rows.extend(rows)

        summary_payload = json.loads(batch_summary.read_text(encoding="utf-8"))
        totals["case_count"] += int(summary_payload.get("case_count", 0))
        totals["citations_total"] += int(summary_payload.get("citations_total", 0))
        totals["resolved"] += int(summary_payload.get("resolved", 0))
        totals["unresolved"] += int(summary_payload.get("unresolved", 0))

        for key, value in dict(summary_payload.get("by_kind", {})).items():
            totals["by_kind"][key] = int(totals["by_kind"].get(key, 0)) + int(value)
        for key, value in dict(summary_payload.get("by_reason", {})).items():
            totals["by_reason"][key] = int(totals["by_reason"].get(key, 0)) + int(value)

    args.out_csv.parent.mkdir(parents=True, exist_ok=True)
    if merged_rows:
        with args.out_csv.open("w", encoding="utf-8", newline="") as file_obj:
            writer = csv.DictWriter(file_obj, fieldnames=list(merged_rows[0].keys()))
            writer.writeheader()
            writer.writerows(merged_rows)

    args.summary_json.parent.mkdir(parents=True, exist_ok=True)
    args.summary_json.write_text(json.dumps(totals, indent=2), encoding="utf-8")

    if not args.keep_temp:
        for file_path in temp_dir.glob("*"):
            file_path.unlink()
        temp_dir.rmdir()

    print(f"matched_case_count={totals['matched_case_count']}")
    print(f"citations_total={totals['citations_total']}")
    print(f"resolved={totals['resolved']}")
    print(f"unresolved={totals['unresolved']}")
    print(f"out_csv={args.out_csv}")
    print(f"summary_json={args.summary_json}")


if __name__ == "__main__":
    main()
