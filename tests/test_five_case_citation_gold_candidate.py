from backend.citations import RawCitationMatch
from scripts.build_five_case_citation_gold_candidate import context_excerpt, occurrence_from_match, validate_match_span


def test_validate_match_span_requires_exact_in_bounds_text():
    text = "Before Vavilov, 2019 SCC 65 after."
    start = text.index("Vavilov")
    end = start + len("Vavilov, 2019 SCC 65")

    assert validate_match_span(text, start, end, "Vavilov, 2019 SCC 65")
    assert not validate_match_span(text, start, end, "Vavilov")
    assert not validate_match_span(text, -1, end, "Vavilov, 2019 SCC 65")


def test_context_excerpt_is_bounded_and_contains_match():
    text = "x" * 100 + "Vavilov, 2019 SCC 65" + "y" * 100
    start = 100
    end = start + len("Vavilov, 2019 SCC 65")

    excerpt = context_excerpt(text, start, end, radius=10)

    assert excerpt == text[90 : end + 10]
    assert len(excerpt) < len(text)
    assert "Vavilov, 2019 SCC 65" in excerpt


def test_occurrence_serialization_preserves_duplicate_emissions():
    text = "See Oakes at para. 4. See Oakes at para. 4."
    first_start = text.index("Oakes")
    second_start = text.rindex("Oakes")
    matches = [
        RawCitationMatch("case_short", "Oakes at para. 4", "Oakes", first_start, first_start + 16, "at para. 4"),
        RawCitationMatch("case_short", "Oakes at para. 4", "Oakes", second_start, second_start + 16, "at para. 4"),
    ]

    occurrences = [occurrence_from_match(text, match) for match in matches]

    assert len(occurrences) == 2
    assert [item["offset_start"] for item in occurrences] == [first_start, second_start]
    assert all(item["review_status"] == "proposed" for item in occurrences)