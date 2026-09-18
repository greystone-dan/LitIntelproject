import pytest

from backend.contextual_authority.models import text_hash
from backend.contextual_authority.voting import RuleVote, build_agreement_report


def make_vote(rule: str, verdict: str, confidence: float, threshold: float = 0.5) -> RuleVote:
    evidence = "application is dismissed"
    return RuleVote(
        case_id=1,
        observation_id="1:10:0:25",
        source_rule=rule,
        verdict=verdict,
        confidence=confidence,
        threshold=threshold,
        method_version="deterministic_observations_v1",
        config_hash=f"config-{rule}",
        evidence_hash=text_hash(evidence),
        evidence_text=evidence,
        rationale=f"{rule} evaluated the evidence",
    )


def test_agreement_report_retains_conflict_and_provenance():
    report = build_agreement_report(
        [make_vote("rule_accept", "accept", 0.92), make_vote("rule_reject", "reject", 0.65)]
    )

    assert report.verdict == "conflict"
    assert report.accept_count == 1
    assert report.reject_count == 1
    assert report.abstain_count == 0
    assert report.agreement_ratio == 0.5
    assert len(report.votes) == 2
    assert report.observation_snapshot_hash
    assert report.config_hash


def test_agreement_report_makes_low_confidence_votes_explicit_abstentions():
    report = build_agreement_report([make_vote("weak_rule", "accept", 0.49, threshold=0.5)])

    assert report.verdict == "abstain"
    assert report.abstain_count == 1
    assert report.active_votes == ()
    assert report.agreement_ratio == 0.0
    assert report.votes[0].verdict == "abstain"


def test_agreement_report_is_unanimous_without_emitting_a_label():
    report = build_agreement_report(
        [make_vote("rule_one", "accept", 0.80), make_vote("rule_two", "accept", 0.90)]
    )

    assert report.verdict == "accept"
    assert report.agreement_ratio == 1.0
    assert all(vote.verdict == "accept" for vote in report.active_votes)


def test_rule_vote_rejects_incorrect_evidence_hash():
    with pytest.raises(ValueError, match="evidence_hash"):
        RuleVote(
            case_id=1,
            observation_id="observation",
            source_rule="rule",
            verdict="accept",
            confidence=1.0,
            threshold=0.5,
            method_version="v1",
            config_hash="config",
            evidence_hash="wrong",
            evidence_text="source text",
            rationale="matched",
        )
