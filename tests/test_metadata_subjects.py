from backend.metadata_subjects import _derive_case_subject_fields, _first_numbered_paragraphs


def test_first_numbered_paragraphs_selects_numbered_lines_before_preamble():
    content = "Court heading\n\n1. First numbered paragraph.\n2) Second numbered paragraph.\nUnnumbered note."

    assert _first_numbered_paragraphs(content) == [
        "1. First numbered paragraph.",
        "2) Second numbered paragraph.",
    ]


def test_subject_derivation_prioritizes_judicial_review_and_challenged_rpd_decision():
    content = (
        "This application for judicial review challenges a Refugee Protection Division decision. "
        "The applicant raises credibility and procedural fairness."
    )

    fields = _derive_case_subject_fields(content, {})

    assert fields["case type"][0] == "judicial_review"
    assert fields["case challenge"][0] == "refugee_protection_decision"
    assert fields["case issue"][0] in {"credibility", "procedural_fairness"}
    assert 0 < fields["case issue"][1] <= 1


def test_subject_derivation_returns_no_fields_for_blank_content():
    assert _derive_case_subject_fields(" \n ", {}) == {}
