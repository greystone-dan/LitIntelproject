"""Build a deterministic ~300-case immigration prototype set from A2AJ data.

This script reads the local A2AJ Federal Court parquet source, applies transparent
ranking rules, maps selected citations to local case IDs, and exports a CSV for
prototype testing and embedding workflows.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import sys

import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import select

# Allow running this file directly via "python scripts/...py".
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal

SOURCE_FILE = Path("data/raw/a2aj/FC/train.parquet")
DEFAULT_OUT_CSV = Path("data/eval/core_immigration_cases.csv")
TARGET_SIZE = 300
RECENT_YEAR_CUTOFF = 2005
MIN_CITATION_COUNT_FOR_IMPORTANCE = 3

IMM_KEYWORDS = [
	"refugee",
	"asylum",
	"removal",
	"inadmiss",
	"prra",
	"h&c",
	"protected person",
	"sponsorship",
	"cbsa",
	"ircc",
	"visa",
	"permit",
	"inadmissibility",
	"refugee protection",
]

IMM_COURT_TOKENS = [
	"irb",
	"rpd",
	"rad",
	"iad",
	"id",
	"imm",
	"immigration",
	"refugee",
	"federal court",
]


@dataclass
class CoreBuildSummary:
	selected: int
	mapped_local_ids: int
	output_csv: Path


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("source_file", type=Path, nargs="?", default=SOURCE_FILE)
	parser.add_argument("--target", type=int, default=TARGET_SIZE)
	parser.add_argument("--recent-year-cutoff", type=int, default=RECENT_YEAR_CUTOFF)
	parser.add_argument("--min-citation-importance", type=int, default=MIN_CITATION_COUNT_FOR_IMPORTANCE)
	parser.add_argument("--out-csv", type=Path, default=DEFAULT_OUT_CSV)
	parser.add_argument("--dry-run", action="store_true")
	return parser.parse_args()


def is_immigration_by_court(court_str: str) -> bool:
	if not court_str:
		return False
	lower = court_str.lower()
	return any(token in lower for token in IMM_COURT_TOKENS)


def contains_imm_keyword(text: str) -> bool:
	if text is None or (isinstance(text, float) and pd.isna(text)):
		return False
	lower = str(text).lower()
	return any(keyword in lower for keyword in IMM_KEYWORDS)


def load_a2aj_dataframe(source_file: Path) -> pd.DataFrame:
	columns = [
		"citation_en",
		"dataset",
		"document_date_en",
		"name_en",
		"unofficial_text_en",
		"cases_cited_en",
		"cases_citing_en",
		"citing_cases_count",
	]
	table = pq.read_table(source_file, columns=columns)
	df = table.to_pandas()
	df = df.rename(
		columns={
			"citation_en": "neutral_citation",
			"dataset": "court",
			"document_date_en": "decision_date",
			"name_en": "title",
			"unofficial_text_en": "summary",
			"cases_cited_en": "cases_cited",
			"cases_citing_en": "cases_citing",
		}
	)
	# A2AJ parquet does not provide stable row IDs in the selected subset, so derive
	# an in-file deterministic identifier.
	df.insert(0, "id", [f"a2aj_fc_{idx + 1}" for idx in range(len(df))])
	return df


def preprocess_a2aj(df: pd.DataFrame, recent_year_cutoff: int) -> pd.DataFrame:
	df = df.copy()
	df["neutral_citation"] = df["neutral_citation"].astype("string")
	df["decision_date"] = pd.to_datetime(df["decision_date"], errors="coerce")
	df["court_imm_signal"] = df["court"].fillna("").astype(str).apply(is_immigration_by_court)

	text_cols = [column for column in ("neutral_citation", "court", "title", "summary") if column in df.columns]

	def safe_text(value: object) -> str:
		if value is None or pd.isna(value):
			return ""
		return str(value)

	def any_text_contains_imm(row: pd.Series) -> bool:
		for column in text_cols:
			if contains_imm_keyword(safe_text(row.get(column, ""))):
				return True
		return False

	df["keyword_imm_signal"] = df.apply(any_text_contains_imm, axis=1)
	df["a2aj_incoming"] = pd.to_numeric(df.get("citing_cases_count", 0), errors="coerce").fillna(0).astype(int)
	df["modern"] = df["decision_date"].dt.year.fillna(0).astype(int) >= recent_year_cutoff
	df["neutral_upper"] = df["neutral_citation"].fillna("").astype(str).str.upper()
	return df


def build_candidates(df: pd.DataFrame, recent_year_cutoff: int, min_citation_importance: int) -> pd.DataFrame:
	df = df.copy()
	df["prefix_imm"] = df["neutral_upper"].str.match(r"^(IMM|ID|IAD|RPD|RAD)\b", na=False)
	df["tier1"] = df["prefix_imm"] | df["court_imm_signal"]

	def cites_irpa(row: pd.Series) -> bool:
		for column in ("cases_cited", "cases_citing"):
			value = row.get(column)
			if isinstance(value, (list, tuple)):
				for citation in value:
					if isinstance(citation, str) and ("IRPA" in citation.upper() or "IRPR" in citation.upper()):
						return True
		return False

	df["cites_irpa"] = df.apply(cites_irpa, axis=1)
	df["tier2"] = (~df["tier1"]) & (df["keyword_imm_signal"] | df["cites_irpa"])
	df["tier3"] = (~df["tier1"]) & (~df["tier2"]) & df["keyword_imm_signal"]

	def score_row(row: pd.Series) -> float:
		score = 0.0
		if row["tier1"]:
			score += 50.0
		if row["tier2"]:
			score += 20.0
		if row["tier3"]:
			score += 5.0
		a2aj_incoming = int(row.get("a2aj_incoming", 0) or 0)
		score += min(a2aj_incoming, 200) * 0.5
		if a2aj_incoming >= min_citation_importance:
			score += 5.0
		if bool(row.get("modern", False)):
			score += 5.0
		if pd.notna(row.get("decision_date")):
			year = int(row["decision_date"].year)
			score += max(0, (year - recent_year_cutoff) * 0.2)
		local_incoming = int(row.get("local_incoming", 0) or 0)
		score += min(local_incoming, 200) * 0.3
		if bool(row.get("has_local_case", False)):
			score += 10.0
		return score

	df["imm_score"] = df.apply(score_row, axis=1)
	return df


def tribunal_bucket(court: str) -> str:
	if not court:
		return "OTHER"
	upper = court.upper()
	if upper in {"FC", "FCA"}:
		return "FEDERAL"
	if any(token in upper for token in ("IRB", "RPD", "RAD", "IAD", " ID ")):
		return "IRB"
	if "FEDERAL" in upper or "FED" in upper or "IMM" in upper:
		return "FEDERAL"
	if "SCC" in upper or "SUPREME" in upper:
		return "SCC"
	return "OTHER"


def select_core_set(df: pd.DataFrame, target: int) -> pd.DataFrame:
	df = df.sort_values(by=["imm_score", "neutral_citation"], ascending=[False, True]).copy()
	top = df.head(max(target, int(target * 1.5))).copy()
	top["tribunal_bucket"] = top["court"].fillna("").astype(str).apply(tribunal_bucket)

	quotas = {
		"IRB": int(target * 0.50),
		"FEDERAL": int(target * 0.35),
		"SCC": int(target * 0.02),
		"OTHER": int(target * 0.13),
	}

	selected_indices: list[int] = []
	for bucket, quota in quotas.items():
		bucket_rows = top[top["tribunal_bucket"] == bucket]
		selected_indices.extend(bucket_rows.head(quota).index.tolist())

	if len(selected_indices) < target:
		remaining = [index for index in top.index.tolist() if index not in selected_indices]
		selected_indices.extend(remaining[: target - len(selected_indices)])

	selected_indices = selected_indices[:target]
	core_df = top.loc[selected_indices].copy()
	core_df = core_df.sort_values(by=["imm_score", "neutral_citation"], ascending=[False, True])
	return core_df


def map_local_signals(df: pd.DataFrame) -> pd.DataFrame:
	df = df.copy()
	with SessionLocal() as session:
		local_rows = list(
			session.execute(
				select(Case.id, Case.citation, Case.citing_cases_count).where(Case.citation.is_not(None))
			)
		)

	local_by_citation: dict[str, tuple[int, int]] = {}
	for case_id, citation, citing_cases_count in local_rows:
		key = str(citation).strip()
		if key and key not in local_by_citation:
			local_by_citation[key] = (int(case_id), int(citing_cases_count or 0))

	df["local_case_id"] = df["neutral_citation"].astype(str).str.strip().map(
		lambda citation: local_by_citation.get(citation, (None, 0))[0]
	)
	df["local_incoming"] = df["neutral_citation"].astype(str).str.strip().map(
		lambda citation: local_by_citation.get(citation, (None, 0))[1]
	)
	df["has_local_case"] = df["local_case_id"].notna()
	return df


def export_core_set(core_df: pd.DataFrame, out_csv: Path) -> None:
	columns = [
		"id",
		"neutral_citation",
		"court",
		"decision_date",
		"imm_score",
		"a2aj_incoming",
		"local_incoming",
		"local_case_id",
		"tribunal_bucket",
		"title",
	]
	columns = [column for column in columns if column in core_df.columns]
	out_csv.parent.mkdir(parents=True, exist_ok=True)
	core_df[columns].to_csv(out_csv, index=False)


def build_core_immigration_set(
	dataframe: pd.DataFrame,
	target: int,
	recent_year_cutoff: int,
	min_citation_importance: int,
	out_csv: Path,
) -> tuple[pd.DataFrame, CoreBuildSummary]:
	df = preprocess_a2aj(dataframe, recent_year_cutoff=recent_year_cutoff)
	df = map_local_signals(df)
	df = build_candidates(
		df,
		recent_year_cutoff=recent_year_cutoff,
		min_citation_importance=min_citation_importance,
	)
	core_df = select_core_set(df, target=target)
	export_core_set(core_df, out_csv=out_csv)
	summary = CoreBuildSummary(
		selected=len(core_df),
		mapped_local_ids=int(core_df["local_case_id"].notna().sum()),
		output_csv=out_csv,
	)
	return core_df, summary


def main() -> None:
	args = parse_args()
	if args.target < 1:
		raise SystemExit("--target must be at least 1")
	if not args.source_file.exists():
		raise SystemExit(f"Source file does not exist: {args.source_file}")

	a2aj_df = load_a2aj_dataframe(args.source_file)
	core_df, summary = build_core_immigration_set(
		a2aj_df,
		target=args.target,
		recent_year_cutoff=args.recent_year_cutoff,
		min_citation_importance=args.min_citation_importance,
		out_csv=args.out_csv,
	)

	print(f"selected={summary.selected}")
	print(f"mapped_local_ids={summary.mapped_local_ids}")
	print(f"out_csv={summary.output_csv}")

	preview = core_df.head(15)
	for _, row in preview.iterrows():
		print(
			f"{row.get('neutral_citation')} | score={row.get('imm_score'):.2f} | "
			f"bucket={row.get('tribunal_bucket')} | local_case_id={row.get('local_case_id')}"
		)

	if args.dry_run:
		print("dry_run=true (selection exported for review only)")


if __name__ == "__main__":
	main()
