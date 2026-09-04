from types import SimpleNamespace

from backend.citations import RawCitationMatch
from scripts.benchmark_citation_resolution import aggregate_case, resolve_occurrence


def target(case_id, title=None, citation=None, secondary_citation=None):
    return SimpleNamespace(
        case_id=case_id,
        title=title,
        citation=citation,
        secondary_citation=secondary_citation,
    )


def test_aggregate_counts_duplicate_occurrences_without_deduplicating():
    text = "See 2019 SCC 65 twice: 2019 SCC 65."
    matches = [
        RawCitationMatch("neutral", "2019 SCC 65", "2019 SCC 65", 4, 16),
        RawCitationMatch("neutral", "2019 SCC 65", "2019 SCC 65", 24, 36),
    ]
    case = SimpleNamespace(id=99, title="Source v Canada", citation="2024 FC 1", secondary_citation=None)

    metrics = aggregate_case(case, text, matches, [target(7, "Vavilov v Canada", "2019 SCC 65")])

    assert metrics["all_extracted_occurrence_count"] == 2
    assert metrics["duplicate_occurrence_count"] == 1
    assert metrics["resolved_occurrence_count"] == 2
    assert metrics["unresolved_occurrence_count"] == 0


def test_aggregate_counts_explicit_pinpoints_for_every_duplicate_occurrence():
    text = "See 2019 SCC 65 at para. 10; 2019 SCC 65; 2019 SCC 65 at paras. 20-21."
    matches = [
        RawCitationMatch("neutral", "2019 SCC 65 at para. 10", "2019 SCC 65", 4, 27, "at para. 10"),
        RawCitationMatch("neutral", "2019 SCC 65", "2019 SCC 65", 29, 41),
        RawCitationMatch("neutral", "2019 SCC 65 at paras. 20-21", "2019 SCC 65", 43, 71, "at paras. 20-21"),
    ]
    case = SimpleNamespace(id=99, title="Source v Canada", citation="2024 FC 1", secondary_citation=None)

    metrics = aggregate_case(case, text, matches, [target(7, "Vavilov v Canada", "2019 SCC 65")])

    assert metrics["explicit_pinpoint_count"] == 2
    assert metrics["all_extracted_occurrence_count"] == 3
    assert metrics["duplicate_occurrence_count"] == 2


def test_resolve_occurrence_classifies_alias_candidates():
    match = RawCitationMatch("case_short", "Oakes at para 10", "Oakes at para 10", 0, 18)

    assert resolve_occurrence(match, [target(1, "R v Oakes")]) == "unique"
    assert resolve_occurrence(match, [target(1, "R v Oakes"), target(2, "Oakes v Canada")]) == "ambiguous"
    assert resolve_occurrence(match, [target(1, "R v Smith")]) == "unresolved"


def test_aggregate_counts_invalid_span_and_alias_ambiguity():
    text = "Oakes at para 10"
    match = RawCitationMatch("case_short", "Oakes at para 10", "Oakes at para 10", 1, 19)
    case = SimpleNamespace(id=99, title="Source v Canada", citation="2024 FC 1", secondary_citation=None)

    metrics = aggregate_case(
        case,
        text,
        [match],
        [target(1, "R v Oakes"), target(2, "Oakes v Canada")],
    )

    assert metrics["exact_span_valid_count"] == 0
    assert metrics["exact_span_invalid_count"] == 1
    assert metrics["ambiguous_alias_occurrence_count"] == 1
    assert metrics["resolved_occurrence_count"] == 0
    assert metrics["unresolved_occurrence_count"] == 0
