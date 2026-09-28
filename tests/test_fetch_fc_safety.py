import pytest
from datetime import date, datetime, timezone

from scripts import fetch_fc_procedural_history as fetcher


def test_delay_floor_rejects_fast_collection():
    with pytest.raises(ValueError, match="at least 2000"):
        fetcher.validate_delay_ms(1999)

    fetcher.validate_delay_ms(2000)
    fetcher.validate_delay_ms(1999, allow_sub_floor=True)


def test_request_budget_stops_before_extra_attempt():
    budget = fetcher.RequestBudget(1)
    budget.spend()

    with pytest.raises(RuntimeError, match="budget exhausted"):
        budget.spend()


def test_request_budget_is_independent_of_robots_policy():
    budget = fetcher.RequestBudget(2)

    budget.spend()
    budget.spend()

    assert budget.used == 2


def test_adaptive_backoff_increases_and_caps_delay():
    assert fetcher.adaptive_backoff_delay_ms(100, 2.0, 2000) == 200
    assert fetcher.adaptive_backoff_delay_ms(1500, 2.0, 2000) == 2000


def test_activity_payload_normalizes_dates_for_json_storage():
    value = fetcher._json_safe({
        "date": date(2026, 9, 25),
        "fetched_at": datetime(2026, 9, 25, tzinfo=timezone.utc),
        "entries": [{"date": date(2026, 9, 24)}],
    })

    assert value == {
        "date": "2026-09-25",
        "fetched_at": "2026-09-25T00:00:00+00:00",
        "entries": [{"date": "2026-09-24"}],
    }
