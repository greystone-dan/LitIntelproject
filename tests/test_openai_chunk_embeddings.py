from types import SimpleNamespace

from scripts.embed_openai_chunks import BudgetState, estimate_cost_usd, fit_batch_to_budget


def test_estimate_cost_usd_scales_linearly():
    assert estimate_cost_usd(0, 0.02) == 0.0
    assert estimate_cost_usd(1_000_000, 0.02) == 0.02
    assert estimate_cost_usd(500_000, 0.02) == 0.01


def test_fit_batch_to_budget_truncates_before_exceeding_cap():
    chunks = [
        SimpleNamespace(token_estimate=250_000),
        SimpleNamespace(token_estimate=250_000),
        SimpleNamespace(token_estimate=250_000),
    ]
    budget = BudgetState(spent_usd=0.0, budget_usd=0.01)

    selected = fit_batch_to_budget(chunks, budget, cost_per_1m=0.02)

    assert len(selected) == 2


def test_fit_batch_to_budget_returns_empty_when_first_chunk_exceeds_cap():
    chunks = [SimpleNamespace(token_estimate=600_000)]
    budget = BudgetState(spent_usd=0.0, budget_usd=0.01)

    selected = fit_batch_to_budget(chunks, budget, cost_per_1m=0.02)

    assert selected == []
