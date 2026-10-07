from scripts.repair_range_word_sections import corrected_section


def test_range_word_suffix_is_removed():
    assert corrected_section("34 to 37", "34t") == "34"
    assert corrected_section("7and8", "7a") == "7"
    assert corrected_section("4.1 to 4.3", "4.1t") == "4.1"


def test_other_rows_are_left_alone():
    assert corrected_section("31A(1)", "31a") is None
    assert corrected_section("96", "96") is None


def test_spaced_word_letter_is_not_a_suffix():
    assert corrected_section("25 s. 3", "25s") == "25"
    assert corrected_section("2 d", "2d") == "2"
    assert corrected_section("224 a", "224a") == "224"
    assert corrected_section("224a", "224a") is None
