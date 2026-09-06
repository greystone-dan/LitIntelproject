from scripts.run_v2_text_only_fast import STAGE_ORDER


def test_fast_runner_uses_combined_local_stage_order_without_embeddings():
    assert STAGE_ORDER == ("full_case", "heading_chunks", "metadata", "outcome", "case_citations", "statutes", "tags_v3")
    assert "embedding" not in " ".join(STAGE_ORDER).lower()
