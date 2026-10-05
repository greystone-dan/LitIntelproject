from backend.judge_fc_activity import combine_rows, match_fc_rows


def _row(name, leave=0, rate=None, **extra):
	return {"key": name.lower(), "name": name, "leave_decisions": leave, "leave_grant_rate": rate,
		"jr_decisions": 0, "jr_grant_rate": None, "motion_decisions": 0, "motion_grant_rate": None,
		"stay_decisions": 0, "stay_grant_rate": None, "median_days_hearing_to_judgment": None, **extra}


def test_matches_by_surname_and_initial_across_name_forms():
	rows = [_row("S. Noël", 100, 0.2), _row("Noël", 50, 0.4), _row("de Montigny", 10, 0.5), _row("Zinn", 5, 0.1)]
	got = match_fc_rows(rows, ["The Honourable Mr. Justice Simon Noël", "Noël J."], ["Zinn"])
	assert [r["name"] for r in got] == ["S. Noël", "Noël"]
	combined = combine_rows(got)
	assert combined["leave_decisions"] == 150 and combined["leave_grant_rate"] == 0.2667


def test_surname_shared_with_another_judge_is_not_guessed():
	rows = [_row("Roy", 40, 0.3)]
	assert match_fc_rows(rows, ["Madam Justice Roy"], ["Mr. Justice Roy"]) == []
	assert match_fc_rows(rows, ["Madam Justice Roy"], []) == rows


def test_initial_mismatch_is_excluded_and_empty_is_none():
	assert match_fc_rows([_row("J. Smith", 5, 0.5)], ["Anne Smith"], []) == []
	assert combine_rows([]) is None
