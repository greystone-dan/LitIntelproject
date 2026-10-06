from scripts.repair_range_word_sections import corrected_section


def test_range_word_suffix_is_removed():
    assert corrected_section("34 to 37", "34t") == "34"
    assert corrected_section("7and8", "7a") == "7"
    assert corrected_section("4.1 to 4.3", "4.1t") == "4.1"


def test_other_rows_are_left_alone():
    assert corrected_section("31A(1)", "31a") is None
    assert corrected_section("96", "96") is None
