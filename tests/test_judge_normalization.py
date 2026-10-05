from backend.judge_normalization import group_judge_names, parse_judge_name, same_person


def test_parse_strips_titles_suffixes_and_accents():
	p = parse_judge_name("The Honourable Madam Justice Mactavish")
	assert p and p.surname == "mactavish" and p.given == ()
	p = parse_judge_name("Gagné, J.")
	assert p and p.surname == "gagne"
	p = parse_judge_name("l’honorable juge Marie-Josée Bédard")
	assert p and p.surname == "bedard"
	assert parse_judge_name("Prothonotary Aalto").role == "prothonotary"


def test_parse_rejects_junk():
	assert parse_judge_name("") is None
	assert parse_judge_name("J.") is None
	assert parse_judge_name("1234") is None


def test_same_person_initials_and_full_names():
	a, b = parse_judge_name("D. Gleason"), parse_judge_name("Dawn Gleason J.")
	assert same_person(a, b)
	assert not same_person(parse_judge_name("D. Gleason"), parse_judge_name("S. Gleason"))
	assert not same_person(parse_judge_name("Gleason"), parse_judge_name("Gleason"))  # surname-only never auto-merges


def test_mac_prefix_and_case_variants_group():
	groups = group_judge_names({"Mactavish J.": 10, "MacTavish J.": 3})
	assert len(groups) == 1 and len(groups[0].members) == 2


def test_surname_only_attaches_when_unambiguous_else_review():
	g = group_judge_names({"Anne Mactavish": 5, "Mactavish J.": 20})
	assert len(g) == 1 and set(g[0].members) == {"Anne Mactavish", "Mactavish J."}
	g = group_judge_names({"Anne Smith": 5, "Bob Smith": 4, "Smith J.": 7})
	assert g and all(grp.needs_review == ["Smith J."] for grp in g) or g == []
	assert not any("Smith J." in grp.members for grp in g)


def test_mojibake_and_apostrophes_repaired():
	a = parse_judge_name("Justice James W. Oâ€™Reilly")
	b = parse_judge_name("The Honourable Mr. Justice O'Reilly")
	assert a.surname == b.surname == "o'reilly"
	assert parse_judge_name("Â Â Â Â THE HONOURABLE MR. JUSTICE BEAUDRY").surname == "beaudry"


def test_particles_deputy_suffix_and_noise():
	assert parse_judge_name("The Honourable Mr. Justice de Montigny").surname == "montigny"
	assert parse_judge_name("THE HONOURABLE MR. JUSTICE KONRAD VON FINCKENSTEIN").surname == "finckenstein"
	assert parse_judge_name("Rouleau D.J.").surname == "rouleau"
	assert parse_judge_name("Justice de Montigny BETWEEN:").surname == "montigny"
	assert parse_judge_name("Justice St-Louis Docket: T-1790-17").surname == "st louis"
	assert parse_judge_name("THE CHIEF JUSTICE") is None
	assert parse_judge_name("-------- Prothonotary ----------") is None


def test_prothonotary_who_became_judge_merges_and_gender_clash_does_not():
	g = group_judge_names({"Prothonotary Mandy Aylen": 24, "The Honourable Madam Justice Mandy Aylen": 3})
	assert len(g) == 1 and g[0].roles == ["judge", "prothonotary"]
	g = group_judge_names({"The Honourable Madam Justice Roy": 5, "The Honourable Mr. Justice Roy": 9})
	assert all(len(x.members) == 1 for x in g)


def test_display_name_prefers_full_mixed_case_name():
	g = group_judge_names({"THE HONOURABLE MR. JUSTICE SIMON NOËL": 400, "Justice Simon Noël": 3, "NOËL J.": 4})
	assert g[0].canonical == "Simon Noël"
