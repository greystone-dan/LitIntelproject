from backend.contextual_authority import ChunkInput, build_context_units
from backend.contextual_authority.observations import extract_context_observations
from backend.contextual_authority.models import text_hash


def test_observations_preserve_exact_evidence_spans_and_source_identity():
    text = "The Minister argued that procedural fairness was satisfied. The application is dismissed."
    chunk = ChunkInput(case_id=9, chunk_id=90, ordinal=0, text=text)
    unit = build_context_units([chunk], methods=("paragraph_v1",))[0]

    observations = extract_context_observations(unit, {chunk.chunk_id: text})

    labels = {(item.cue_category, item.cue_label) for item in observations}
    assert ("disposition_cue", "dismissed") in labels
    assert ("issue_cue", "procedural_fairness") in labels
    assert ("authority_role_cue", "government_party_mentioned") in labels
    for item in observations:
        evidence = text[item.evidence_start : item.evidence_end]
        assert evidence
        assert item.chunk_id == chunk.chunk_id
        assert item.evidence_sha256 == text_hash(evidence)
        assert item.method_version == "deterministic_observations_v1"


def test_observations_do_not_infer_treatment_or_merits_from_a_citation():
    text = "The court cites Smith but does not decide whether the application succeeds."
    chunk = ChunkInput(case_id=10, chunk_id=100, ordinal=0, text=text)
    unit = build_context_units([chunk], methods=("paragraph_v1",))[0]

    observations = extract_context_observations(unit, {chunk.chunk_id: text})

    assert not any(item.cue_category == "treatment_cue" for item in observations)
    assert not any(item.cue_label in {"applicant_prevails", "strong_finding"} for item in observations)


def test_observations_are_negative_when_no_supported_cue_is_present():
    text = "The parties filed written submissions and attended the hearing."
    chunk = ChunkInput(case_id=11, chunk_id=110, ordinal=0, text=text)
    unit = build_context_units([chunk], methods=("paragraph_v1",))[0]

    assert extract_context_observations(unit, {chunk.chunk_id: text}) == []
