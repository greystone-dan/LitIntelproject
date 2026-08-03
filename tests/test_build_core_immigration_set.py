from pathlib import Path

import pandas as pd

from scripts import build_core_immigration_set as core_builder


def _sample_df() -> pd.DataFrame:
	return pd.DataFrame(
		[
			{
				"id": "a1",
				"neutral_citation": "2021 FC 100",
				"court": "Federal Court",
				"decision_date": "2021-01-01",
				"title": "Alpha v. Canada",
				"summary": "refugee removal IRCC",
				"cases_cited": ["IRPA s. 72"],
				"cases_citing": [],
				"citing_cases_count": 10,
			},
			{
				"id": "a2",
				"neutral_citation": "2019 FC 200",
				"court": "Federal Court",
				"decision_date": "2019-05-01",
				"title": "Beta v. Canada",
				"summary": "sponsorship H&C IRCC",
				"cases_cited": [],
				"cases_citing": [],
				"citing_cases_count": 5,
			},
			{
				"id": "a3",
				"neutral_citation": "2010 FC 300",
				"court": "Federal Court",
				"decision_date": "2010-02-01",
				"title": "Gamma v. Canada",
				"summary": "administrative law reasons",
				"cases_cited": [],
				"cases_citing": [],
				"citing_cases_count": 0,
			},
		]
	)


def test_build_candidates_scores_immigration_signals_higher():
	df = core_builder.preprocess_a2aj(_sample_df(), recent_year_cutoff=2005)
	df["local_incoming"] = [7, 2, 0]
	df["has_local_case"] = [True, True, False]

	result = core_builder.build_candidates(df, recent_year_cutoff=2005, min_citation_importance=3)

	scores = {
		row["neutral_citation"]: row["imm_score"]
		for _, row in result.iterrows()
	}
	assert scores["2021 FC 100"] > scores["2010 FC 300"]
	assert scores["2019 FC 200"] > scores["2010 FC 300"]


def test_select_core_set_respects_target_size():
	df = core_builder.preprocess_a2aj(_sample_df(), recent_year_cutoff=2005)
	df["local_incoming"] = [7, 2, 0]
	df["has_local_case"] = [True, True, False]
	df = core_builder.build_candidates(df, recent_year_cutoff=2005, min_citation_importance=3)

	selected = core_builder.select_core_set(df, target=2)

	assert len(selected) == 2
	assert "imm_score" in selected.columns


def test_export_core_set_writes_csv(tmp_path: Path):
	df = core_builder.preprocess_a2aj(_sample_df(), recent_year_cutoff=2005)
	df["local_incoming"] = [7, 2, 0]
	df["has_local_case"] = [True, True, False]
	df["local_case_id"] = [1, 2, None]
	df = core_builder.build_candidates(df, recent_year_cutoff=2005, min_citation_importance=3)
	df["tribunal_bucket"] = df["court"].apply(core_builder.tribunal_bucket)

	out_file = tmp_path / "core.csv"
	core_builder.export_core_set(df.head(2), out_csv=out_file)

	loaded = pd.read_csv(out_file)
	assert len(loaded) == 2
	assert "neutral_citation" in loaded.columns
