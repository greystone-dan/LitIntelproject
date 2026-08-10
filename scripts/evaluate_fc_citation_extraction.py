"""Evaluate citation extraction output against gold annotations.

The gold file can be partially complete. Only rows with sufficient annotation
fields are scored.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

DEFAULT_GOLD_CSV = Path("data/eval/fc_citation_gold_template.csv")
DEFAULT_EVIDENCE_CSV = Path("data/eval/reports/fc_citation_evidence.csv")
DEFAULT_SUMMARY_JSON = Path("data/eval/reports/fc_citation_eval_summary.json")
DEFAULT_FN_CSV = Path("data/eval/reports/fc_citation_eval_false_negatives.csv")
DEFAULT_FP_CSV = Path("data/eval/reports/fc_citation_eval_false_positives.csv")


@dataclass(frozen=True)
class GoldCitation:
    annotation_id: str
    source_case_id: int
    normalized_citation: str
    citation_type: str
    paragraph_index: int | None


@dataclass(frozen=True)
class PredCitation:
    source_case_id: int
    normalized_citation: str
    citation_kind: str
    paragraph_number: int | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gold-csv", type=Path, default=DEFAULT_GOLD_CSV)
    parser.add_argument("--evidence-csv", type=Path, default=DEFAULT_EVIDENCE_CSV)
    parser.add_argument("--summary-json", type=Path, default=DEFAULT_SUMMARY_JSON)
    parser.add_argument("--false-negatives-csv", type=Path, default=DEFAULT_FN_CSV)
    parser.add_argument("--false-positives-csv", type=Path, default=DEFAULT_FP_CSV)
    parser.add_argument("--resolved-only", action="store_true")
    return parser.parse_args()


def _norm_ws_upper(value: str | None) -> str:
    return " ".join(str(value or "").split()).strip().upper()


def _norm_lower(value: str | None) -> str:
    return " ".join(str(value or "").split()).strip().lower()


def _to_int(value: str | None) -> int | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    try:
        return int(text)
    except ValueError:
        return None


def _load_gold(path: Path) -> list[GoldCitation]:
    if not path.exists():
        raise SystemExit(f"Gold CSV not found: {path}")

    rows: list[GoldCitation] = []
    with path.open("r", encoding="utf-8", newline="") as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            source_case_id = _to_int(row.get("local_case_id"))
            normalized_citation = _norm_ws_upper(row.get("normalized_citation"))
            if source_case_id is None or not normalized_citation:
                continue

            rows.append(
                GoldCitation(
                    annotation_id=str(row.get("annotation_id") or ""),
                    source_case_id=source_case_id,
                    normalized_citation=normalized_citation,
                    citation_type=_norm_lower(row.get("citation_type")),
                    paragraph_index=_to_int(row.get("paragraph_index")),
                )
            )
    return rows


def _load_pred(path: Path, resolved_only: bool) -> list[PredCitation]:
    if not path.exists():
        raise SystemExit(f"Evidence CSV not found: {path}")

    rows: list[PredCitation] = []
    with path.open("r", encoding="utf-8", newline="") as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            if resolved_only and str(row.get("resolution_status") or "") != "resolved":
                continue

            source_case_id = _to_int(row.get("source_case_id"))
            normalized_citation = _norm_ws_upper(row.get("normalized_citation"))
            if source_case_id is None or not normalized_citation:
                continue

            rows.append(
                PredCitation(
                    source_case_id=source_case_id,
                    normalized_citation=normalized_citation,
                    citation_kind=_norm_lower(row.get("citation_kind")),
                    paragraph_number=_to_int(row.get("paragraph_number")),
                )
            )
    return rows


def _kind_matches(gold_kind: str, pred_kind: str) -> bool:
    if not gold_kind:
        return True
    return gold_kind == pred_kind


def _score(gold_rows: list[GoldCitation], pred_rows: list[PredCitation]) -> tuple[dict[str, float], list[dict[str, object]], list[dict[str, object]]]:
    pred_buckets: dict[tuple[int, str], list[PredCitation]] = {}
    for pred in pred_rows:
        key = (pred.source_case_id, pred.normalized_citation)
        pred_buckets.setdefault(key, []).append(pred)

    tp = 0
    fn = 0
    used_pred_ids: set[int] = set()
    false_negatives: list[dict[str, object]] = []

    for gold in gold_rows:
        key = (gold.source_case_id, gold.normalized_citation)
        candidates = pred_buckets.get(key, [])

        match_index: int | None = None
        for idx, pred in enumerate(candidates):
            pred_id = id(pred)
            if pred_id in used_pred_ids:
                continue
            if not _kind_matches(gold.citation_type, pred.citation_kind):
                continue
            if gold.paragraph_index is not None and pred.paragraph_number != gold.paragraph_index:
                continue
            match_index = idx
            used_pred_ids.add(pred_id)
            break

        if match_index is not None:
            tp += 1
        else:
            fn += 1
            false_negatives.append(
                {
                    "annotation_id": gold.annotation_id,
                    "source_case_id": gold.source_case_id,
                    "normalized_citation": gold.normalized_citation,
                    "citation_type": gold.citation_type,
                    "paragraph_index": gold.paragraph_index,
                }
            )

    fp = 0
    false_positives: list[dict[str, object]] = []
    for pred in pred_rows:
        pred_id = id(pred)
        if pred_id in used_pred_ids:
            continue
        fp += 1
        false_positives.append(
            {
                "source_case_id": pred.source_case_id,
                "normalized_citation": pred.normalized_citation,
                "citation_kind": pred.citation_kind,
                "paragraph_number": pred.paragraph_number,
            }
        )

    precision = (tp / (tp + fp)) if (tp + fp) else 0.0
    recall = (tp / (tp + fn)) if (tp + fn) else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0

    summary = {
        "gold_scored_rows": float(len(gold_rows)),
        "pred_scored_rows": float(len(pred_rows)),
        "tp": float(tp),
        "fp": float(fp),
        "fn": float(fn),
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }
    return summary, false_negatives, false_positives


def main() -> None:
    args = parse_args()

    gold_rows = _load_gold(args.gold_csv)
    pred_rows = _load_pred(args.evidence_csv, resolved_only=args.resolved_only)

    summary, false_negatives, false_positives = _score(gold_rows, pred_rows)

    if not gold_rows:
        summary["note"] = "No scored gold rows found. Fill local_case_id + normalized_citation in gold template."

    args.summary_json.parent.mkdir(parents=True, exist_ok=True)
    args.summary_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    args.false_negatives_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.false_negatives_csv.open("w", encoding="utf-8", newline="") as file_obj:
        writer = csv.DictWriter(
            file_obj,
            fieldnames=["annotation_id", "source_case_id", "normalized_citation", "citation_type", "paragraph_index"],
        )
        writer.writeheader()
        writer.writerows(false_negatives)

    args.false_positives_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.false_positives_csv.open("w", encoding="utf-8", newline="") as file_obj:
        writer = csv.DictWriter(
            file_obj,
            fieldnames=["source_case_id", "normalized_citation", "citation_kind", "paragraph_number"],
        )
        writer.writeheader()
        writer.writerows(false_positives)

    print(f"gold_scored_rows={int(summary['gold_scored_rows'])}")
    print(f"pred_scored_rows={int(summary['pred_scored_rows'])}")
    print(f"precision={summary['precision']:.4f}")
    print(f"recall={summary['recall']:.4f}")
    print(f"f1={summary['f1']:.4f}")
    print(f"summary_json={args.summary_json}")


if __name__ == "__main__":
    main()
