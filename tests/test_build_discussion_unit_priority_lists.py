from datetime import date

from scripts.build_discussion_unit_priority_lists import CaseRecord, select_layers


def record(case_id: int, court: str, year: int, inbound: int) -> CaseRecord:
	return CaseRecord(case_id, f"Case {case_id}", None, date(year, 1, 1), court, inbound, "test")


def test_expanded_layer_contains_core_and_respects_quotas_and_cutoff():
	core = [record(1, "FC", 2000, 10), record(2, "FC", 2020, 9)]
	core.extend(record(case_id, "FC", 2020, 1) for case_id in range(3, 301))
	candidates = [
		record(301, "SCC", 2020, 20),
		record(302, "SCC", 2004, 100),
		record(303, "FCA", 2020, 19),
		record(304, "FC", 2020, 18),
	]
	quotas = {"SCC": 1, "FCA": 1, "FC": 300}

	core_rows, expanded_rows = select_layers(core, candidates, quotas=quotas)
	all_rows = core_rows + expanded_rows

	assert len(core_rows) == 300
	assert len(all_rows) == 302
	assert {row["case_id"] for row in core_rows}.issubset({row["case_id"] for row in all_rows})
	assert 302 not in {row["case_id"] for row in all_rows}
	assert sum(row["court"] == "SCC" for row in all_rows) == 1
	assert sum(row["court"] == "FCA" for row in all_rows) == 1
	assert sum(row["court"] == "FC" for row in all_rows) == 300