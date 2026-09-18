from backend.contextual_authority import ChunkInput, build_context_units
from backend.contextual_authority.models import CitationInput, SnapshotSpec, text_hash


def test_phase0_generates_competing_context_variants_without_mutating_inputs():
    chunks = [
        ChunkInput(case_id=7, chunk_id=10, ordinal=0, text="The court follows Smith. It applies the test."),
        ChunkInput(case_id=7, chunk_id=11, ordinal=1, text="The applicant responds."),
        ChunkInput(case_id=7, chunk_id=12, ordinal=2, text="The court distinguishes Jones."),
    ]
    citations = [CitationInput(1, 10, 16, 21), CitationInput(2, 12, 28, 33)]

    units = build_context_units(chunks, citations)

    assert {unit.method for unit in units} == {"sentence_v1", "paragraph_v1", "window_p1", "citation_burst_v1"}
    assert {citation_id for unit in units for citation_id in unit.citation_ids} == {1, 2}
    assert all(segment.end_offset > segment.start_offset for unit in units for segment in unit.segments)
    assert all(segment.text_sha256 for unit in units for segment in unit.segments)
    assert chunks[0].text == "The court follows Smith. It applies the test."


def test_phase0_sentence_span_hash_is_reconstructable():
    chunk = ChunkInput(case_id=1, chunk_id=4, ordinal=0, text="First sentence. Second sentence!")

    units = build_context_units([chunk], methods=("sentence_v1",))

    assert len(units) == 2
    for unit in units:
        segment = unit.segments[0]
        source = chunk.text[segment.start_offset : segment.end_offset]
        assert text_hash(source) == segment.text_sha256


def test_phase0_keeps_citation_membership_for_noncontiguous_window_segments():
    chunks = [
        ChunkInput(case_id=2, chunk_id=20, ordinal=0, text="A"),
        ChunkInput(case_id=2, chunk_id=21, ordinal=1, text="B"),
        ChunkInput(case_id=2, chunk_id=22, ordinal=2, text="C"),
    ]
    units = build_context_units([chunks[0], chunks[1], chunks[2]], [CitationInput(9, 20, 0, 1)], methods=("window_p1",))

    assert units[1].citation_ids == (9,)
    assert [segment.chunk_id for segment in units[1].segments] == [20, 21, 22]


def test_phase0_snapshot_is_staged_by_default_and_config_hash_is_stable():
    snapshot = SnapshotSpec(
        code_sha="a" * 64,
        method_set_version="phase0.v1",
        config={"window": 1, "methods": ["sentence_v1"]},
        cohort_hash="b" * 64,
        snapshot_id="snapshot-fixture",
    )

    assert snapshot.status == "staged"
    assert snapshot.config_hash == SnapshotSpec(
        code_sha=snapshot.code_sha,
        method_set_version=snapshot.method_set_version,
        config={"methods": ["sentence_v1"], "window": 1},
        cohort_hash=snapshot.cohort_hash,
        snapshot_id=snapshot.snapshot_id,
    ).config_hash
