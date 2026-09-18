import pytest

from backend.contextual_authority import (
    ParagraphFeatures,
    compute_continuity,
    segment_discussion_units,
)


def paragraph(index, text, *, citations=(), statutes=(), tags=(), heading=False):
    return ParagraphFeatures(
        case_id=7,
        chunk_id=100 + index,
        paragraph_index=index,
        start_offset=0,
        end_offset=len(text),
        text=text,
        citation_ids=tuple(citations),
        statute_ids=tuple(statutes),
        tag_ids=tuple(tags),
        is_heading=heading,
    )


def test_paragraph_features_are_immutable_and_hashable():
    feature = paragraph(1, "The court applies the test.", citations=(1,), tags=("rule",))

    assert feature.text_sha256
    with pytest.raises(Exception):
        feature.paragraph_index = 2


def test_continuity_keeps_components_separate_and_penalizes_heading():
    left = paragraph(1, "The court applies the test.", citations=(1,), statutes=(2,), tags=("rule",))
    right = paragraph(2, "Analysis", citations=(1,), statutes=(2,), tags=("rule",), heading=True)

    components = compute_continuity(left, right)

    assert components.authority_overlap == 1.0
    assert components.statute_overlap == 1.0
    assert components.tag_overlap == 1.0
    assert components.text_overlap == 0.0
    assert components.heading_boundary_penalty == 1.0
    assert components.continuity_score < 0.5


def test_text_overlap_supports_continuity_and_empty_signals_do_not_fake_overlap():
    left = paragraph(1, "The reasonableness analysis considers the statutory purpose.")
    related = paragraph(2, "The reasonableness analysis applies that statutory purpose.")
    unrelated = paragraph(3, "The remedy concerns procedural fairness and jurisdiction.")

    related_components = compute_continuity(left, related)
    unrelated_components = compute_continuity(left, unrelated)

    assert related_components.text_overlap > unrelated_components.text_overlap
    assert related_components.continuity_score > unrelated_components.continuity_score
    assert compute_continuity(left, unrelated).authority_overlap == 0.0


def test_segmenter_requires_two_low_scores_unless_heading_boundary():
    paragraphs = (
        paragraph(1, "First discussion.", citations=(1,)),
        paragraph(2, "Same discussion.", citations=(1,)),
        paragraph(3, "Analysis", citations=(2,), heading=True),
        paragraph(4, "New discussion.", citations=(2,)),
    )
    continuity = tuple(compute_continuity(left, right) for left, right in zip(paragraphs, paragraphs[1:]))

    units = segment_discussion_units(paragraphs, continuity, threshold=0.5, consecutive_low_scores=2)

    assert [unit.paragraph_indices for unit in units] == [(1, 2), (3, 4)]
    assert units[0].citation_counts == {1: 2}
    assert units[1].citation_counts == {2: 2}
    assert units[0].text_sha256


def test_segmenter_splits_sustained_signal_vacuum_and_closes_on_signal():
    paragraphs = (
        paragraph(1, "First discussion.", citations=(1,)),
        paragraph(2, "Unrelated chronology."),
        paragraph(3, "Separate witness detail."),
        paragraph(4, "Distinct filing history."),
        paragraph(5, "New authority discussion.", citations=(2,)),
    )
    continuity = tuple(compute_continuity(left, right) for left, right in zip(paragraphs, paragraphs[1:]))

    units = segment_discussion_units(
        paragraphs,
        continuity,
        consecutive_signal_vacuum_pairs=2,
        signal_vacuum_min_paragraphs=5,
    )

    assert [unit.paragraph_indices for unit in units] == [(1, 2), (3, 4), (5,)]


def test_segmenter_signal_blocks_vacuum_boundary():
    paragraphs = (
        paragraph(1, "First discussion.", citations=(1,)),
        paragraph(2, "Sparse discussion one."),
        paragraph(3, "Sparse discussion two.", citations=(1,)),
        paragraph(4, "Next section.", citations=(2,)),
    )
    continuity = tuple(compute_continuity(left, right) for left, right in zip(paragraphs, paragraphs[1:]))

    units = segment_discussion_units(paragraphs, continuity)

    assert [unit.paragraph_indices for unit in units] == [(1, 2, 3, 4)]


def test_segmenter_is_deterministic_and_rejects_wrong_pair_count():
    paragraphs = (paragraph(1, "One."), paragraph(2, "Two."))
    continuity = (compute_continuity(paragraphs[0], paragraphs[1]),)

    first = segment_discussion_units(paragraphs, continuity)
    second = segment_discussion_units(paragraphs, continuity)

    assert first == second
    with pytest.raises(ValueError, match="one item per adjacent"):
        segment_discussion_units(paragraphs, ())
    with pytest.raises(ValueError, match="signal_vacuum_text_overlap"):
        segment_discussion_units(paragraphs, continuity, signal_vacuum_text_overlap=1.1)