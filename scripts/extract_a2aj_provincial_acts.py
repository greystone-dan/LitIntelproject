"""Cut a few provincial acts out of the A2AJ canadian-laws parquet files into small JSON snapshots.

Source: https://huggingface.co/datasets/a2aj/canadian-laws (one LEGISLATION-<PROVINCE>.parquet per jurisdiction).
Only the acts listed in ACTS are taken, never whole provinces. Each snapshot carries the upstream licence text
and is indexed by scripts/index_legislation.py (source format "json_sections").

Tier "open": the dataset's licence note permits reproduction with attribution (Ontario, Alberta, Manitoba).
Tier "held": British Columbia (licence field blank), Quebec (CC BY-NC-ND 4.0, non-commercial, no derivatives)
and Saskatchewan (non-commercial use by permission). Held acts are only counted unless --include-held is given;
do not commit their snapshots until the licence question is settled.

Usage: python scripts/extract_a2aj_provincial_acts.py --parquet-dir DIR [--write] [--include-held]
Without --write it only prints section counts.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = PROJECT_ROOT / "data" / "reference_library" / "provincial_json"


@dataclass(frozen=True)
class ProvincialAct:
	key: str
	province: str
	name_en: str
	file_name: str
	tier: str  # "open" or "held"


ACTS = (
	ProvincialAct("ontario.immigration_act_2015", "ON", "Ontario Immigration Act, 2015", "ontario_immigration_act_2015.json", "open"),
	ProvincialAct("alberta.immigration_oversight_act", "AB", "Immigration Oversight Act", "alberta_immigration_oversight_act.json", "open"),
	ProvincialAct("manitoba.worker_recruitment_protection_act", "MB", "The Worker Recruitment and Protection Act", "manitoba_worker_recruitment_protection_act.json", "open"),
	ProvincialAct("bc.provincial_immigration_programs_act", "BC", "Provincial Immigration Programs Act", "bc_provincial_immigration_programs_act.json", "held"),
	ProvincialAct("bc.temporary_foreign_worker_protection_act", "BC", "Temporary Foreign Worker Protection Act", "bc_temporary_foreign_worker_protection_act.json", "held"),
	ProvincialAct("quebec.immigration_act", "QC", "Québec Immigration Act", "quebec_immigration_act.json", "held"),
	ProvincialAct("quebec.civil_code", "QC", "Civil Code of Québec", "quebec_civil_code.json", "held"),
	ProvincialAct("quebec.ministry_immigration_act", "QC", "Act respecting the Ministère de l’Immigration, de la Francisation et de l'Intégration", "quebec_ministry_immigration_act.json", "held"),
	ProvincialAct("saskatchewan.immigration_services_act", "SK", "The Immigration Services Act", "saskatchewan_immigration_services_act.json", "held"),
)


def load_snapshot(act: ProvincialAct, parquet_dir: Path) -> dict | None:
	import pyarrow.parquet as pq

	rows = pq.read_table(parquet_dir / f"LEGISLATION-{act.province}.parquet").to_pylist()
	for row in rows:
		if (row["name_en"] or "").strip() == act.name_en:
			sections = json.loads(row["unofficial_sections_en"] or "{}")
			return {
				"key": act.key,
				"title": row["name_en"].strip(),
				"citation": (row["citation_en"] or "").strip(),
				"source_url": row["source_url_en"],
				"document_date": row["document_date_en"].date().isoformat() if row["document_date_en"] else None,
				"licence": row["upstream_license"],
				"dataset": "a2aj/canadian-laws " + (row["dataset"] or ""),
				"sections": [[str(number), " ".join(str(text).split())] for number, text in sections.items()],
			}
	return None


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--parquet-dir", type=Path, required=True)
	parser.add_argument("--write", action="store_true", help="write the JSON snapshots (default: counts only)")
	parser.add_argument("--include-held", action="store_true", help="also write the held-tier acts (licence not settled)")
	args = parser.parse_args()
	for act in ACTS:
		snapshot = load_snapshot(act, args.parquet_dir)
		if snapshot is None:
			print(f"{act.key}: NOT FOUND in LEGISLATION-{act.province}")
			continue
		chars = sum(len(text) for _, text in snapshot["sections"])
		write = args.write and (act.tier == "open" or args.include_held)
		print(f"{act.key}: tier={act.tier} sections={len(snapshot['sections'])} chars={chars} {'WRITTEN' if write else 'counted only'}")
		if write:
			OUT_DIR.mkdir(parents=True, exist_ok=True)
			(OUT_DIR / act.file_name).write_text(json.dumps(snapshot, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
	main()
