"""Hand-checkable FC, SCC and FCA citations, source spans and paragraph targets."""

import pytest

from backend.citation_refine import parse_pinpoint, refine_case_citations
from backend.citations import extract_case_citation_matches


@pytest.mark.parametrize("layer", ["extraction", "refinement"])
@pytest.mark.parametrize(
    ("text", "citation", "normalized", "start", "end"),
    [
        ("2024 FC 639", "2024 FC 639", "2024 FC 639", 0, 11),
        ("2022 FC 884", "2022 FC 884", "2022 FC 884", 0, 11),
        ("2019 SCC 65", "2019 SCC 65", "2019 SCC 65", 0, 11),
        ("2020 FCA 10", "2020 FCA 10", "2020 FCA 10", 0, 11),
        ("See (2024 FC 639).", "2024 FC 639", "2024 FC 639", 5, 16),
        ("See 2022 FC 884;", "2022 FC 884", "2022 FC 884", 4, 15),
        ("See 2019 SCC 65,", "2019 SCC 65", "2019 SCC 65", 4, 15),
        ("See 2020 FCA 10.", "2020 FCA 10", "2020 FCA 10", 4, 15),
    ],
)
def test_neutral_citation_identity_and_exact_span(
    layer, text, citation, normalized, start, end
):
    rows = (
        extract_case_citation_matches(text)
        if layer == "extraction"
        else refine_case_citations(text, current_year=2026).rows
    )
    assert len(rows) == 1
    row = rows[0]
    assert row.citation_text == citation
    assert row.normalized_citation == normalized
    assert (row.offset_start, row.offset_end) == (start, end)
    assert text[start:end] == citation
    if layer == "refinement":
        assert row.identifiers[0] == normalized


@pytest.mark.parametrize(
    ("citation", "identifier"),
    [
        ("2019 CSC 65", "2019 SCC 65"),
        ("2024 CF 639", "2024 FC 639"),
        ("2020 CAF 10", "2020 FCA 10"),
    ],
)
def test_refinement_maps_french_courts_to_english_identifiers(citation, identifier):
    text = f"See ({citation})."
    rows = refine_case_citations(text, current_year=2026).rows
    assert len(rows) == 1
    row = rows[0]
    assert row.citation_text == citation
    assert row.normalized_citation == citation
    assert row.identifiers[0] == identifier
    assert row.language == "fr"
    assert (row.offset_start, row.offset_end) == (5, 16)
    assert text[row.offset_start:row.offset_end] == citation


@pytest.mark.parametrize(
    ("phrase", "paragraphs"),
    [
        ("at para 12", (12,)),
        ("paras 12-14", (12, 13, 14)),
        ("at paras 199-202", (199, 200, 201, 202)),
        ("aux paragraphes 12 à 14", (12, 13, 14)),
    ],
)
def test_pinpoints_have_exact_paragraph_targets(phrase, paragraphs):
    pinpoint = parse_pinpoint(phrase)
    assert pinpoint is not None
    assert pinpoint.kind == "paragraph"
    assert pinpoint.values == paragraphs
    assert not pinpoint.truncated

    citation = f"2019 SCC 65, {phrase}"
    text = f"See ({citation})."
    rows = refine_case_citations(text, current_year=2026).rows
    assert len(rows) == 1
    row = rows[0]
    assert row.citation_text == citation
    assert (row.offset_start, row.offset_end) == (5, 5 + len(citation))
    assert text[row.offset_start:row.offset_end] == citation
    assert row.identifiers == ("2019 SCC 65",)
    assert len(row.pinpoints) == 1
    assert row.pinpoints[0].kind == "paragraph"
    assert row.pinpoints[0].values == paragraphs


@pytest.mark.xfail(
    strict=True, reason="known bug: 199-02 pinpoint parses as 199 only"
)
def test_abbreviated_pinpoint_rolls_over_the_hundred():
    pinpoint = parse_pinpoint("paras 199-02")
    assert pinpoint is not None
    assert pinpoint.values == (199, 200, 201, 202)

    rows = refine_case_citations(
        "2019 SCC 65, paras 199-02.", current_year=2026
    ).rows
    assert len(rows) == 1
    assert rows[0].pinpoints[0].values == (199, 200, 201, 202)


@pytest.mark.parametrize("layer", ["extraction", "refinement"])
def test_declared_short_form_retains_the_correct_anchor(layer):
    text = (
        "Canada v. Vavilov, 2019 SCC 65 [Vavilov]. "
        "Vavilov, supra."
    )
    rows = (
        extract_case_citation_matches(text)
        if layer == "extraction"
        else refine_case_citations(text, current_year=2026).rows
    )
    short = [row for row in rows if row.kind == "case_short"]
    assert len(short) == 1
    row = short[0]
    assert row.citation_text == "Vavilov, supra"
    assert row.normalized_citation == "Canada v. Vavilov, 2019 SCC 65"
    assert (row.offset_start, row.offset_end) == (42, 56)
    assert text[row.offset_start:row.offset_end] == row.citation_text
    assert row.anchor_citation_text == "Canada v. Vavilov, 2019 SCC 65 [Vavilov]"
    assert (row.anchor_offset_start, row.anchor_offset_end) == (0, 40)
    assert text[row.anchor_offset_start:row.anchor_offset_end] == row.anchor_citation_text


def test_refinement_attaches_short_form_pinpoint_without_trailing_punctuation():
    text = (
        "Canada v. Vavilov, 2019 SCC 65 [Vavilov]. "
        "Vavilov, supra at para 12."
    )
    rows = refine_case_citations(text, current_year=2026).rows
    short = [row for row in rows if row.kind == "case_short"]
    assert len(short) == 1
    row = short[0]
    assert row.citation_text == "Vavilov, supra at para 12"
    assert row.normalized_citation == "Canada v. Vavilov, 2019 SCC 65, at para. 12"
    assert (row.offset_start, row.offset_end) == (42, 67)
    assert text[row.offset_start:row.offset_end] == row.citation_text
    assert (row.anchor_offset_start, row.anchor_offset_end) == (0, 40)
    assert text[row.anchor_offset_start:row.anchor_offset_end] == (
        "Canada v. Vavilov, 2019 SCC 65 [Vavilov]"
    )
    assert row.identifiers == ("2019 SCC 65",)
    assert row.pinpoints[0].values == (12,)


def test_ibid_uses_the_previous_case_not_an_unrelated_neutral_citation():
    text = "2024 FC 639. 2019 SCC 65. Ibid at para 12."
    rows = refine_case_citations(text, current_year=2026).rows
    short = [row for row in rows if row.kind == "case_short"]
    assert len(short) == 1
    row = short[0]
    assert row.citation_text == "Ibid at para 12"
    assert (row.offset_start, row.offset_end) == (26, 41)
    assert row.identifiers == ("2019 SCC 65",)
    assert (row.anchor_offset_start, row.anchor_offset_end) == (13, 24)
    assert row.anchor_citation_text == "2019 SCC 65"
    assert text[row.anchor_offset_start:row.anchor_offset_end] == "2019 SCC 65"
    assert row.pinpoints[0].values == (12,)
