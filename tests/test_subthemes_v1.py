import pytest

from backend.contextual_authority import (
    DiscussionUnit,
    ParagraphFeatures,
    extract_argument_evidence,
    segment_subthemes,
)


def paragraph(index: int, text: str, *, is_heading: bool = False) -> ParagraphFeatures:
    return ParagraphFeatures(
        case_id=7,
        chunk_id=100 + index,
        paragraph_index=index,
        start_offset=0,
        end_offset=len(text),
        text=text,
        is_heading=is_heading,
    )


def test_argument_evidence_preserves_exact_local_span_and_source_hash():
    feature = paragraph(3, "The applicants argue that the decision was unreasonable.")

    evidence = extract_argument_evidence(feature)

    party_position = next(item for item in evidence if item.role == "party_position")
    assert party_position.text == "argue"
    assert feature.text[party_position.start_offset:party_position.end_offset] == party_position.text
    assert party_position.source_text_hash == feature.source_sha256
    assert party_position.rationale == "explicit party-position cue"
    assert "applicants argue" in party_position.context_text
    assert feature.text[party_position.context_start_offset:party_position.context_end_offset] == party_position.context_text


def test_disposition_requires_operative_outcome_language():
    ordinary = extract_argument_evidence(paragraph(1, "The order was discussed but no remedy followed."))
    heading = extract_argument_evidence(paragraph(2, "JUDGMENT AND REASONS", is_heading=True))
    operative = extract_argument_evidence(paragraph(3, "The application is dismissed."))

    assert not any(item.role == "disposition" for item in ordinary)
    assert not heading
    assert any(item.role == "disposition" and item.text == "dismissed" for item in operative)


def test_party_position_requires_actor_context():
    without_actor = extract_argument_evidence(paragraph(4, "The reasons argue that the test is wrong."))
    with_actor = extract_argument_evidence(paragraph(5, "The applicant argues that the test is wrong."))

    assert not any(item.role == "party_position" for item in without_actor)
    assert any(item.role == "party_position" for item in with_actor)


def test_party_position_excludes_procedural_claim_nouns_but_keeps_advocacy_claims():
    procedural = extract_argument_evidence(paragraph(5, "The applicant made a claim for refugee protection."))
    refugee_claim = extract_argument_evidence(paragraph(6, "The RPD rejected the Applicants' refugee claims."))
    possessive_claim = extract_argument_evidence(paragraph(7, "The children were not included on this claim."))
    advocacy = extract_argument_evidence(paragraph(8, "The applicant claims that the test was applied unreasonably."))

    assert not any(item.role == "party_position" for item in procedural)
    assert not any(item.role == "party_position" for item in refugee_claim)
    assert not any(item.role == "party_position" for item in possessive_claim)
    assert any(item.role == "party_position" and item.text == "claims" for item in advocacy)


def test_governing_rule_excludes_status_and_narrative_under_phrases():
    corporate = extract_argument_evidence(paragraph(9, "The company was organized under the laws of Yukon."))
    narrative = extract_argument_evidence(paragraph(10, "The group operated under their own agenda."))
    legal = extract_argument_evidence(paragraph(11, "The claim was assessed under section 97(1)(b) of the IRPA."))

    assert not any(item.role == "governing_rule" for item in corporate)
    assert not any(item.role == "governing_rule" for item in narrative)
    assert any(item.role == "governing_rule" and item.text == "under" for item in legal)


def test_metadata_headings_and_records_do_not_generate_substantive_cues():
    heading = extract_argument_evidence(paragraph(6, "Issues and Standard of Review", is_heading=True))
    record = extract_argument_evidence(paragraph(7, "SOLICITORS OF RECORD\nDOCKET: IMM-1"))

    assert heading == ()
    assert record == ()


def test_counterargument_requires_local_contrast_context():
    standalone = extract_argument_evidence(paragraph(8, "However, the panel found no risk."))
    contrasted = extract_argument_evidence(paragraph(9, "The applicant presented evidence. However, the panel found no risk."))

    assert not any(item.role == "counterargument_limitation" for item in standalone)
    assert any(item.role == "counterargument_limitation" for item in contrasted)


def test_counterargument_excludes_procedural_and_distant_contrasts():
    procedural = extract_argument_evidence(
        paragraph(10, "The standard was disputed. Although the parties' arguments were filed before Vavilov, the case confirms reasonableness.")
    )
    distant = extract_argument_evidence(
        paragraph(11, "The applicant presented evidence. The panel reviewed the record. The court considered the issue. But the order remained unchanged.")
    )

    assert not any(item.role == "counterargument_limitation" for item in procedural)
    assert not any(item.role == "counterargument_limitation" for item in distant)


def test_key_terms_preserve_raw_terms_and_filter_display_terms():
    unit = DiscussionUnit(
        case_id=7,
        unit_index=2,
        paragraph_indices=(10,),
        paragraphs=(paragraph(10, "The applicant presents procedural fairness evidence about internal flight alternatives."),),
    )

    subtheme = segment_subthemes(unit)[0]

    assert "applicant" in subtheme.key_terms
    assert "applicant" not in subtheme.display_key_terms
    assert "procedural" in subtheme.display_key_terms
    assert "fairness" in subtheme.display_key_terms

def test_explanation_marks_cue_free_spans_without_inventing_roles():
    unit = DiscussionUnit(
        case_id=7,
        unit_index=1,
        paragraph_indices=(1,),
        paragraphs=(paragraph(1, "V. Issues and Standard of Review", is_heading=True),),
    )

    subtheme = segment_subthemes(unit)[0]

    assert subtheme.argument_roles == ()
    assert subtheme.argument_evidence == ()
    assert "No explicit argument evidence was detected" in subtheme.explanation
    assert "metadata or cue-free text" in subtheme.explanation


def test_subthemes_are_deterministic_and_contained_by_parent_unit():
    paragraphs = (
        paragraph(0, "The issue is whether the decision was reasonable."),
        paragraph(1, "The applicants argue that the evidence was overlooked."),
        paragraph(2, "However, the record supports the decision and the court concludes otherwise."),
        paragraph(3, "The application is dismissed."),
    )
    unit = DiscussionUnit(case_id=7, unit_index=1, paragraph_indices=tuple(range(4)), paragraphs=paragraphs)

    first = segment_subthemes(unit)
    second = segment_subthemes(unit)

    assert first == second
    assert first
    assert any(item.argument_roles for item in first)
    assert {index for item in first for index in item.paragraph_indices} == set(unit.paragraph_indices)
    for item in first:
        assert set(item.paragraph_indices) <= set(unit.paragraph_indices)
        assert all(evidence.paragraph_index in item.paragraph_indices for evidence in item.argument_evidence)
        assert item.config_hash
        assert "Observed roles:" in item.explanation
        assert "not a legal conclusion" in item.explanation


def test_subthemes_reject_invalid_similarity_configuration():
    unit = DiscussionUnit(case_id=7, unit_index=1, paragraph_indices=(0,), paragraphs=(paragraph(0, "The issue is clear."),))

    with pytest.raises(ValueError):
        segment_subthemes(unit, threshold=1.1)
    with pytest.raises(ValueError):
        segment_subthemes(unit, consecutive_low_similarity=0)