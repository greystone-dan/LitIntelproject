"""Synthetic FC, SCC and FCA dispositions with hand-written expected results."""

import pytest

from backend.metadata_outcomes import build_case_outcome, derive_outcome_detail


@pytest.mark.parametrize(
    ("disposition", "label", "government_role", "government", "applicant", "winner"),
    [
        ("The appeal is allowed.", "allowed", "respondent", "lost", "won", "applicant"),
        ("The appeal is allowed.", "allowed", "applicant", "won", "won", "applicant"),
        ("The application is dismissed.", "dismissed", "respondent", "won", "lost", "respondent"),
        ("The application is dismissed.", "dismissed", "applicant", "lost", "lost", "respondent"),
        ("The application is granted.", "granted", "respondent", "lost", "won", "applicant"),
        ("The application is granted.", "granted", "applicant", "won", "won", "applicant"),
        ("The decision is set aside.", "set_aside", "respondent", "lost", "won", "applicant"),
        ("The decision is set aside.", "set_aside", "applicant", "won", "won", "applicant"),
        ("The matter is remitted for redetermination.", "remitted", "respondent", "lost", "won", "applicant"),
        ("The matter is remitted for redetermination.", "remitted", "applicant", "won", "won", "applicant"),
        ("The appeal is allowed in part.", "mixed", "respondent", "mixed", "mixed", "mixed"),
        ("The appeal is allowed in part.", "mixed", "applicant", "mixed", "mixed", "mixed"),
    ],
)
def test_dispositions_have_known_party_results(
    disposition, label, government_role, government, applicant, winner
):
    # "Applicant" means the party bringing the proceeding, including a Minister's appeal.
    style = (
        "Singh v. Canada (Citizenship and Immigration)"
        if government_role == "respondent"
        else "Canada (Citizenship and Immigration) v. Singh"
    )
    text = f"Federal Court of Appeal\nJUDGMENT\n{disposition}"
    metadata = {"style of cause": style}

    outcome = build_case_outcome(text, metadata)
    detail = derive_outcome_detail(text, metadata)

    assert outcome["decision_outcome"] == label
    assert outcome["government_role"] == government_role
    assert outcome["government_outcome"] == government
    assert outcome["outcome_status"] == applicant
    assert detail["status"] == applicant
    assert outcome["winner_side"] == winner


@pytest.mark.parametrize(
    ("court", "disposition", "label"),
    [
        ("Federal Court", "The motion for an extension of time is granted.", "procedural"),
        ("Supreme Court of Canada", "Reasons will follow.", "unclear"),
        ("Federal Court of Appeal", "The application is allowed. The appeal is dismissed.", "unclear"),
        ("Federal Court", "", None),
    ],
)
def test_no_merits_result_has_no_winner(court, disposition, label):
    text = f"{court}\nJUDGMENT\n{disposition}" if disposition else ""
    metadata = {"style of cause": "Singh v. Canada (Citizenship and Immigration)"}

    outcome = build_case_outcome(text, metadata)
    detail = derive_outcome_detail(text, metadata)

    assert outcome["decision_outcome"] == label
    assert outcome["government_outcome"] is None
    assert outcome["outcome_status"] == "undetermined"
    assert detail["status"] == "undetermined"
    assert outcome["winner_side"] is None
    assert outcome["loser_side"] is None


@pytest.mark.xfail(strict=True, reason="known bug: withdrawn cases get a named winner")
@pytest.mark.parametrize("verb", ["withdrawn", "discontinued"])
@pytest.mark.parametrize(
    "style",
    [
        "Singh v. Canada (Citizenship and Immigration)",
        "Canada (Citizenship and Immigration) v. Singh",
    ],
)
def test_withdrawal_is_not_a_win_or_loss(verb, style):
    text = f"Federal Court\nJUDGMENT\nThe application is {verb}."
    metadata = {"style of cause": style}
    outcome = build_case_outcome(text, metadata)
    detail = derive_outcome_detail(text, metadata)

    # Discontinuance is normalized to the withdrawn label, not a merits dismissal.
    assert outcome["decision_outcome"] == "withdrawn"
    assert outcome["government_outcome"] == "undetermined"
    assert (outcome["winner_side"], outcome["loser_side"]) == (None, None)
    assert outcome["outcome_status"] == "undetermined"
    assert detail["status"] == "undetermined"
    assert (detail["winner"], detail["loser"]) == (None, None)
