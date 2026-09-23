from datetime import date

from scripts.select_discussion_unit_cohort import Candidate, select_cohort


def candidate(case_id: int, year: int, inbound_count: int) -> Candidate:
	return Candidate(
		case_id=case_id,
		title=f"Case {case_id}",
		citation=f"{year} FC {case_id}",
		decision_date=date(year, 1, 1),
		inbound_count=inbound_count,
		inbound_count_source="test",
	)


def test_priority_cases_bypass_cutoff_and_ranked_cases_are_capped_and_ordered():
	candidates = [
		candidate(1, 2000, 1),
		candidate(2, 2020, 5),
		candidate(3, 2021, 9),
		candidate(4, 2004, 100),
	]

	result = select_cohort(candidates, {1}, cutoff=date(2005, 1, 1), ranked_limit=2)

	assert [item["case_id"] for item in result] == [1, 3, 2]
	assert result[0]["inclusion_reason"] == "explicit_priority"
	assert result[1]["rank"] == 1
	assert all(item["case_id"] != 4 for item in result)


def test_duplicate_priority_and_ranked_members_are_emitted_once():
	result = select_cohort([candidate(1, 2020, 4), candidate(2, 2021, 3)], {1, 2}, ranked_limit=10)

	assert [item["case_id"] for item in result] == [1, 2]