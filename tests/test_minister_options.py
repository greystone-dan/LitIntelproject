from backend.analytics_service import clean_minister_options


def test_typos_years_and_case_variants_are_collapsed():
	rows = [
		("Attorney General", 900),
		("Atorney General", 2),
		("Attoreny General", 1),
		("attorney General", 3),
		("Attorney general", 4),
		("1966", 1),
		("Border Services Agency", 300),
		("Border Services Angency", 1),
		("Canada Border Services Agency", 120),
	]
	assert clean_minister_options(rows) == [
		"Attorney General",
		"Border Services Agency",
		"Canada Border Services Agency",
	]


def test_two_real_names_with_similar_size_are_both_kept():
	rows = [("Minister of Citizenship", 50), ("Minister of Citizenship and Immigration", 60)]
	assert len(clean_minister_options(rows)) == 2
