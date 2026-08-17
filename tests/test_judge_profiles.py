from scripts.backfill_judge_profiles import is_profileable_judge, judge_slug, normalize_judge_name


def test_normalize_judge_name_removes_titles_and_accents():
	assert normalize_judge_name("The Honourable Justice Rene Cote") == "rene cote"
	assert judge_slug("rene cote") == "judge-rene-cote"


def test_rejects_malformed_oversized_judge_extraction():
	assert is_profileable_judge("Justice Smith") is True
	assert is_profileable_judge("Judge " + "x" * 300) is False