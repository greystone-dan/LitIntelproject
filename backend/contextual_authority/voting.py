from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
from typing import Literal, Sequence

from .models import text_hash

VoteVerdict = Literal["accept", "reject", "abstain"]
ReportVerdict = Literal["accept", "reject", "conflict", "abstain"]
AGREEMENT_REPORT_VERSION = "agreement_v1"


@dataclass(frozen=True)
class RuleVote:
    case_id: int
    observation_id: str
    source_rule: str
    verdict: VoteVerdict
    confidence: float
    threshold: float
    method_version: str
    config_hash: str
    evidence_hash: str
    evidence_text: str
    rationale: str

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        if not 0.0 <= self.threshold <= 1.0:
            raise ValueError("threshold must be between 0 and 1")
        if text_hash(self.evidence_text) != self.evidence_hash:
            raise ValueError("evidence_hash must match evidence_text")

    @property
    def effective_verdict(self) -> VoteVerdict:
        if self.confidence < self.threshold:
            return "abstain"
        return self.verdict


@dataclass(frozen=True)
class RuleAgreementReport:
    case_id: int
    observation_id: str
    observation_snapshot_hash: str
    votes: tuple[RuleVote, ...]
    active_votes: tuple[RuleVote, ...]
    verdict: ReportVerdict
    accept_count: int
    reject_count: int
    abstain_count: int
    agreement_ratio: float
    report_version: str
    config_hash: str


def _normalized_vote(vote: RuleVote) -> RuleVote:
    if vote.effective_verdict == vote.verdict:
        return vote
    return replace(vote, verdict="abstain")


def _stable_vote_payload(vote: RuleVote) -> str:
    return "|".join(
        (
            vote.case_id.__str__(),
            vote.observation_id,
            vote.source_rule,
            vote.verdict,
            f"{vote.confidence:.6f}",
            f"{vote.threshold:.6f}",
            vote.method_version,
            vote.config_hash,
            vote.evidence_hash,
            vote.rationale,
        )
    )


def build_agreement_report(votes: Sequence[RuleVote]) -> RuleAgreementReport:
    """Aggregate rule votes without producing or persisting a pseudo-label."""
    if not votes:
        raise ValueError("at least one rule vote is required")
    normalized = tuple(_normalized_vote(vote) for vote in votes)
    identities = {(vote.case_id, vote.observation_id) for vote in normalized}
    if len(identities) != 1:
        raise ValueError("all votes must target one case observation")
    case_id, observation_id = next(iter(identities))
    active_votes = tuple(vote for vote in normalized if vote.verdict != "abstain")
    accept_count = sum(vote.verdict == "accept" for vote in normalized)
    reject_count = sum(vote.verdict == "reject" for vote in normalized)
    abstain_count = sum(vote.verdict == "abstain" for vote in normalized)
    if not active_votes:
        verdict: ReportVerdict = "abstain"
    elif accept_count and reject_count:
        verdict = "conflict"
    elif accept_count:
        verdict = "accept"
    else:
        verdict = "reject"
    agreement_ratio = (
        max(accept_count, reject_count) / len(active_votes) if active_votes else 0.0
    )
    payload = "\n".join(_stable_vote_payload(vote) for vote in normalized)
    config_payload = "\n".join(
        f"{vote.source_rule}|{vote.threshold:.6f}|{vote.config_hash}" for vote in normalized
    )
    return RuleAgreementReport(
        case_id=case_id,
        observation_id=observation_id,
        observation_snapshot_hash=sha256(payload.encode("utf-8")).hexdigest(),
        votes=normalized,
        active_votes=active_votes,
        verdict=verdict,
        accept_count=accept_count,
        reject_count=reject_count,
        abstain_count=abstain_count,
        agreement_ratio=agreement_ratio,
        report_version=AGREEMENT_REPORT_VERSION,
        config_hash=sha256(config_payload.encode("utf-8")).hexdigest(),
    )
