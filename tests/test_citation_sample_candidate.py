from types import SimpleNamespace

from backend.citations import RawCitationMatch
from scripts.build_citation_sample_candidate import (
    context_excerpt,
    occurrence_from_match,
    parse_quotas,
    select_cases,
    validate_match_span,
)


def test_validate_match_span_and_context_excerpt_are_source_bounded():
    text = "x" * 40 + "Vavilov, 2019 SCC 65" + "y" * 40
    start = text.index("Vavilov")
    end = start + len("Vavilov, 2019 SCC 65")

    assert validate_match_span(text, start, end, "Vavilov, 2019 SCC 65")
    assert not validate_match_span(text, start, end, "Vavilov")
    assert context_excerpt(text, start, end, 5) == text[start - 5 : end + 5]


def test_occurrence_serialization_preserves_duplicate_occurrences():
    text = "See Oakes at para. 4. See Oakes at para. 4."
    first = text.index("Oakes")
    second = text.rindex("Oakes")
    matches = [
        RawCitationMatch("case_short", "Oakes at para. 4", "Oakes", first, first + 16, "at para. 4"),
        RawCitationMatch("case_short", "Oakes at para. 4", "Oakes", second, second + 16, "at para. 4"),
    ]

    occurrences = [occurrence_from_match(text, match, 4) for match in matches]

    assert len(occurrences) == 2
    assert [item["offset_start"] for item in occurrences] == [first, second]
    assert [item["citation_text"] for item in occurrences] == ["Oakes at para. 4"] * 2
    assert all(item["review_status"] == "proposed" for item in occurrences)


def test_select_cases_uses_available_quota_rows_then_fills_missing_courts():
    rows = [
        SimpleNamespace(id=1, court="Federal Court", citation="2020 FC 1"),
        SimpleNamespace(id=2, court="Federal Court of Appeal", citation="2020 FCA 2"),
        SimpleNamespace(id=3, court="Supreme Court of Canada", citation="2020 SCC 3"),
        SimpleNamespace(id=4, court="Federal Court", citation="2020 FC 4"),
    ]

    selected = select_cases(rows, 5, {"FC": 3, "FCA": 2, "SCC": 2, "OTHER": 0})

    assert [row.id for row in selected] == [1, 4, 2, 3]


def test_parse_quotas_defaults_and_overrides():
    assert parse_quotas(None) == {"FC": 10, "FCA": 5, "SCC": 5}
    assert parse_quotas(["FC=2", "SCC=1"]) == {"FC": 2, "FCA": 0, "SCC": 1, "OTHER": 0}