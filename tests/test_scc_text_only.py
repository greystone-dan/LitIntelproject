from scripts.run_scc_text_only import STAGE_ORDER


def test_scc_runner_uses_all_text_enrichment_layers_without_embeddings():
    assert STAGE_ORDER == (
        "full_case",
        "heading_chunks",
        "metadata",
        "outcome",
        "case_citations",
        "statutes",
        "tags_v3",
    )
    assert "embedding" not in " ".join(STAGE_ORDER).lower()


def test_scc_runner_exposes_exact_case_selection():
    from scripts.run_scc_text_only import run

    assert "case_ids" in run.__annotations__
    assert "from_date" in run.__annotations__
    assert "resume" in run.__annotations__
