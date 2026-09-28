from scripts.review_fc_activity_local import validate_review


def test_validate_review_requires_source_linked_evidence():
    result = validate_review(
        {
            "ambiguity": "none",
            "candidate_event": "motion_decision",
            "evidence_quote": "Order granting the motion.",
            "abstain": False,
        },
        "Order granting the motion.",
    )

    assert result["valid"] is True
    assert result["candidate_event"] == "motion_decision"


def test_validate_review_abstains_when_quote_is_not_in_source():
    result = validate_review(
        {
            "ambiguity": "unclear",
            "candidate_event": "motion_decision",
            "evidence_quote": "invented quote",
            "abstain": False,
        },
        "The entry contains no outcome.",
    )

    assert result == {
        "valid": False,
        "reason": "evidence_quote_not_in_source",
        "abstain": True,
    }


def test_validate_review_accepts_explicit_abstention_without_evidence():
    result = validate_review(
        {
            "ambiguity": "no procedural event",
            "candidate_event": "",
            "evidence_quote": "",
            "abstain": True,
        },
        "Administrative note.",
    )

    assert result["valid"] is True
    assert result["abstain"] is True


def test_validate_review_normalizes_literal_boolean_string():
    result = validate_review(
        {
            "ambiguity": "none",
            "candidate_event": "motion_decision",
            "evidence_quote": "Order granting the motion.",
            "abstain": "false",
        },
        "Order granting the motion.",
    )

    assert result["valid"] is True
    assert result["abstain"] is False
