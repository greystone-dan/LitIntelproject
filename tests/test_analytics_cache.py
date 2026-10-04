"""Test analytics TTL cache functionality.

Tests cover:
- Cache hits and misses with atomic hit status
- Distinct parameter keys create distinct cache entries
- TTL expiry using injected clock
- Disabled cache mode (behavior equivalence)
- Error non-caching
- Cache header propagation to routes
"""

from unittest.mock import MagicMock, patch

import pytest
from fastapi import Response
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

import backend.analytics_service as analytics_service
from backend.database import get_db
from backend.main import app
from backend.analytics_service import (
	ANALYTICS_CACHE_TTL_ENV,
	TTLCache,
	clear_analytics_cache,
	set_analytics_cache_enabled,
	get_analytics_cache_status,
	fetch_about_stats,
	fetch_fc_activity_analytics,
	fetch_judge_profiles,
)
from backend.routes import about_stats, fc_activity_analytics, judge_profiles


@pytest.fixture
def mock_db():
	"""Create a mock database session."""
	return MagicMock(spec=Session)


@pytest.fixture(autouse=True)
def reset_cache(monkeypatch):
	"""Reset cache before and after each test."""
	monkeypatch.setattr(analytics_service, "_analytics_cache", TTLCache(ttl_seconds=600))
	clear_analytics_cache()
	set_analytics_cache_enabled(True)
	yield
	clear_analytics_cache()
	set_analytics_cache_enabled(True)


class TestTTLCacheBasics:
	"""Test core TTL cache functionality."""

	def test_cache_key_distinct_from_params(self):
		"""Test that different parameter combinations create different keys."""
		cache = TTLCache()

		# Same parameters should give same key
		key1 = cache._make_key("endpoint", a="value", b=123)
		key2 = cache._make_key("endpoint", a="value", b=123)
		assert key1 == key2

		# Different parameters should give different keys
		key3 = cache._make_key("endpoint", a="other", b=123)
		assert key3 != key1

		key4 = cache._make_key("endpoint", a="value", b=456)
		assert key4 != key1

	def test_cache_preserves_string_values(self):
		"""String values that may affect filters must not collide in the cache."""
		cache = TTLCache()

		# Distinct casing and whitespace are retained to avoid false cache hits.
		key1 = cache._make_key("endpoint", q="QUERY")
		key2 = cache._make_key("endpoint", q="query")
		assert key1 != key2
		key3 = cache._make_key("endpoint", q="  QUERY  ")
		assert key3 != key1

	def test_cache_set_and_get_hit(self):
		"""Test cache set and get with hit, returns hit status atomically."""
		cache = TTLCache()
		test_data = {"key": "value"}

		cache.set("endpoint", test_data, param="test")
		value, was_hit = cache.get("endpoint", param="test")

		assert was_hit is True
		assert value == test_data

	def test_cache_get_miss(self):
		"""Test cache get with miss, returns False for was_hit."""
		cache = TTLCache()

		value, was_hit = cache.get("endpoint", param="test")
		assert was_hit is False
		assert value is None

	def test_cache_expiry_with_injected_clock(self):
		"""Test cache expiry using injected clock."""
		clock_time = [0.0]  # Mutable to simulate time progression

		def mock_clock():
			return clock_time[0]

		cache = TTLCache(ttl_seconds=10, clock=mock_clock)
		test_data = {"key": "value"}

		# Set a value at time 0
		cache.set("endpoint", test_data, param="test")

		# Get at time 5 (should hit)
		clock_time[0] = 5.0
		value, was_hit = cache.get("endpoint", param="test")
		assert was_hit is True

		# At the exact TTL boundary the entry expires.
		clock_time[0] = 10.0
		value, was_hit = cache.get("endpoint", param="test")
		assert was_hit is False

	def test_cache_disabled_mode_always_misses(self):
		"""Test that disabled cache always reports miss."""
		cache = TTLCache(enabled=False)
		test_data = {"key": "value"}

		cache.set("endpoint", test_data, param="test")
		value, was_hit = cache.get("endpoint", param="test")

		assert was_hit is False
		assert value is None

	def test_cache_enable_disable_toggle(self):
		"""Test toggling cache enabled/disabled."""
		cache = TTLCache()
		test_data = {"key": "value"}

		cache.set("endpoint", test_data, param="test")
		value, was_hit = cache.get("endpoint", param="test")
		assert was_hit is True

		# Disable cache
		cache.set_enabled(False)
		value, was_hit = cache.get("endpoint", param="test")
		assert was_hit is False

		# Re-enable should still have the cached data
		cache.set_enabled(True)
		value, was_hit = cache.get("endpoint", param="test")
		assert was_hit is True

	def test_cache_clear_all(self):
		"""Test clearing entire cache."""
		cache = TTLCache()

		cache.set("endpoint1", {"data": 1}, param="test")
		cache.set("endpoint2", {"data": 2}, param="test")

		# Verify both are cached
		_, hit1 = cache.get("endpoint1", param="test")
		_, hit2 = cache.get("endpoint2", param="test")
		assert hit1 and hit2

		# Clear all
		cache.clear()

		# Verify both are gone
		_, hit1 = cache.get("endpoint1", param="test")
		_, hit2 = cache.get("endpoint2", param="test")
		assert not hit1 and not hit2

	def test_cache_status(self):
		"""Test cache status reporting from global cache."""
		# Clear and set up the global cache
		from backend.analytics_service import get_analytics_cache
		global_cache = get_analytics_cache()
		global_cache.clear()
		global_cache.set("endpoint", {"data": 1})

		status = get_analytics_cache_status()
		assert status["enabled"] is True
		# TTL comes from env var ANALYTICS_CACHE_TTL_SECONDS, default 600
		assert status["ttl_seconds"] >= 0
		assert status["cached_entries"] > 0

	def test_ttl_is_configurable_and_nonpositive_values_disable_cache(self, monkeypatch):
		monkeypatch.delenv(ANALYTICS_CACHE_TTL_ENV, raising=False)
		assert TTLCache().ttl_seconds == 600

		monkeypatch.setenv(ANALYTICS_CACHE_TTL_ENV, "37")
		configured_cache = TTLCache()
		assert configured_cache.ttl_seconds == 37
		assert configured_cache.is_enabled()

		monkeypatch.setenv(ANALYTICS_CACHE_TTL_ENV, "0")
		disabled_cache = TTLCache()
		assert disabled_cache.ttl_seconds == 0
		assert not disabled_cache.is_enabled()

		monkeypatch.setenv(ANALYTICS_CACHE_TTL_ENV, "-1")
		disabled_cache = TTLCache()
		assert not disabled_cache.is_enabled()
		disabled_cache.set_enabled(True)
		assert not disabled_cache.is_enabled()

	def test_cache_is_bounded_by_max_entries(self):
		cache = TTLCache(max_entries=2)
		cache.set("endpoint", "first", key=1)
		cache.set("endpoint", "second", key=2)
		cache.set("endpoint", "third", key=3)

		assert len(cache._cache) == 2
		assert cache.get("endpoint", key=1) == (None, False)
		assert cache.get("endpoint", key=2) == ("second", True)
		assert cache.get("endpoint", key=3) == ("third", True)


class TestAnalyticsWrappersWithCache:
	"""Test analytics functions with caching, returns hit status atomically."""

	def test_fetch_about_stats_returns_hit_status_on_hit(self, mock_db):
		"""Test that fetch_about_stats returns hit status atomically."""
		clear_analytics_cache()

		with patch('backend.analytics_service._fetch_about_stats_impl') as mock_impl:
			mock_impl.return_value = {"cases": 100, "judges": 50}

			# First call should return miss
			result1, was_hit1 = fetch_about_stats(mock_db)
			assert was_hit1 is False
			assert result1 == {"cases": 100, "judges": 50}
			assert mock_impl.call_count == 1

			# Second call should return hit
			result2, was_hit2 = fetch_about_stats(mock_db)
			assert was_hit2 is True
			assert result2 == {"cases": 100, "judges": 50}
			assert mock_impl.call_count == 1  # Not called again

	def test_fetch_fc_analytics_caches_per_parameters(self, mock_db):
		"""Test that FC analytics caches different parameters separately."""
		clear_analytics_cache()

		with patch('backend.analytics_service._fetch_fc_activity_analytics_impl') as mock_impl:
			mock_impl.side_effect = [
				{"data": "set1"},
				{"data": "set2"},
			]

			# Call with different parameters
			result1, hit1 = fetch_fc_activity_analytics(mock_db, x="year")
			result2, hit2 = fetch_fc_activity_analytics(mock_db, x="city")

			# Both should be misses (first calls)
			assert hit1 is False
			assert hit2 is False
			assert result1 == {"data": "set1"}
			assert result2 == {"data": "set2"}
			assert mock_impl.call_count == 2

			# Calling again with same params should use cache
			result1_again, hit1_again = fetch_fc_activity_analytics(mock_db, x="year")
			result2_again, hit2_again = fetch_fc_activity_analytics(mock_db, x="city")

			assert hit1_again is True
			assert hit2_again is True
			assert mock_impl.call_count == 2  # Still 2, no new calls
			assert result1_again == result1
			assert result2_again == result2

	def test_fetch_judge_profiles_caches_per_parameters(self, mock_db):
		"""Test that judge profiles caches different queries separately."""
		clear_analytics_cache()

		with patch('backend.analytics_service._fetch_judge_profiles_impl') as mock_impl:
			mock_impl.side_effect = [
				[{"name": "Smith"}],
				[{"name": "Jones"}],
			]

			# Call with different queries
			result1, hit1 = fetch_judge_profiles(mock_db, q="smith")
			result2, hit2 = fetch_judge_profiles(mock_db, q="jones")

			assert hit1 is False
			assert hit2 is False
			assert mock_impl.call_count == 2

			# Calling again with same query should use cache
			result1_again, hit1_again = fetch_judge_profiles(mock_db, q="smith")

			assert hit1_again is True
			assert mock_impl.call_count == 2  # Still 2
			assert result1_again == result1

	def test_cache_does_not_cache_errors(self, mock_db):
		"""Test that errors are not cached."""
		clear_analytics_cache()

		with patch('backend.analytics_service._fetch_about_stats_impl') as mock_impl:
			# First call raises an error
			mock_impl.side_effect = RuntimeError("Database error")

			with pytest.raises(RuntimeError):
				fetch_about_stats(mock_db)

			# Reset the mock to return a valid result
			mock_impl.side_effect = None
			mock_impl.return_value = {"cases": 100}

			# Second call should execute (not use cache of error)
			result, was_hit = fetch_about_stats(mock_db)
			assert result == {"cases": 100}
			assert was_hit is False  # Not a hit because error wasn't cached
			assert mock_impl.call_count == 2  # Called twice

	def test_cache_disabled_always_reports_miss(self, mock_db):
		"""Test that disabling cache always reports miss."""
		clear_analytics_cache()
		set_analytics_cache_enabled(False)

		with patch('backend.analytics_service._fetch_about_stats_impl') as mock_impl:
			mock_impl.return_value = {"cases": 100}

			# Call twice
			result1, was_hit1 = fetch_about_stats(mock_db)
			result2, was_hit2 = fetch_about_stats(mock_db)

			# Should always be miss and call implementation both times
			assert was_hit1 is False
			assert was_hit2 is False
			assert mock_impl.call_count == 2

		set_analytics_cache_enabled(True)

	def test_cache_disabled_response_equivalence(self, mock_db):
		"""Test that disabled cache produces identical results."""
		with patch('backend.analytics_service._fetch_about_stats_impl') as mock_impl:
			mock_impl.return_value = {"cases": 100}

			# Get result with caching enabled
			clear_analytics_cache()
			set_analytics_cache_enabled(True)
			result_cached, _ = fetch_about_stats(mock_db)

			# Get result with caching disabled
			clear_analytics_cache()
			set_analytics_cache_enabled(False)
			result_uncached, _ = fetch_about_stats(mock_db)

			# Results should be identical
			assert result_cached == result_uncached

			set_analytics_cache_enabled(True)


class TestCacheHeadersViaRoutes:
	"""Test X-Cache header accuracy in API responses via routes."""

	def test_about_stats_http_header_without_database_access(self):
		"""Exercise FastAPI header injection with the database dependency replaced."""
		db_override = MagicMock(spec=Session)
		previous_override = app.dependency_overrides.get(get_db)
		app.dependency_overrides[get_db] = lambda: db_override
		try:
			client = TestClient(app)
			with patch("backend.analytics_service._fetch_about_stats_impl", return_value={"cases": 100}):
				clear_analytics_cache()
				first = client.get("/api/about/stats")
				second = client.get("/api/about/stats")
			assert first.status_code == 200
			assert first.json() == {"cases": 100}
			assert first.headers["X-Cache"] == "miss"
			assert second.json() == first.json()
			assert second.headers["X-Cache"] == "hit"
		finally:
			if previous_override is None:
				app.dependency_overrides.pop(get_db, None)
			else:
				app.dependency_overrides[get_db] = previous_override

	def test_about_stats_cache_header_miss_then_hit(self, mock_db):
		"""Test that /api/about/stats X-Cache header is accurate (miss, then hit)."""

		with patch('backend.analytics_service._fetch_about_stats_impl') as mock_impl:
			mock_impl.return_value = {"cases": 100}

			clear_analytics_cache()
			set_analytics_cache_enabled(True)

			# First call should be miss
			headers1 = Response()
			result1 = about_stats(response=headers1, db=mock_db)
			assert result1 == {"cases": 100}
			assert "X-Cache" in headers1.headers
			assert headers1.headers["X-Cache"] == "miss", "First request should be miss"

			# Second call should be hit
			headers2 = Response()
			result2 = about_stats(response=headers2, db=mock_db)
			assert result2 == result1
			assert headers2.headers["X-Cache"] == "hit", "Second request with same params should be hit"

	def test_judge_profiles_cache_header_distinct_params(self, mock_db):
		"""Test that /api/judge-profiles X-Cache header respects parameter differences."""

		with patch('backend.analytics_service._fetch_judge_profiles_impl') as mock_impl:
			mock_impl.return_value = [{"name": "Smith"}]

			clear_analytics_cache()
			set_analytics_cache_enabled(True)

			# First call with query=smith should be miss
			headers1 = Response()
			judge_profiles(response=headers1, q="smith", limit=50, db=mock_db)
			assert headers1.headers["X-Cache"] == "miss"

			# Second call with same query should be hit
			headers2 = Response()
			judge_profiles(response=headers2, q="smith", limit=50, db=mock_db)
			assert headers2.headers["X-Cache"] == "hit"

			# Different query should be miss
			headers3 = Response()
			judge_profiles(response=headers3, q="jones", limit=50, db=mock_db)
			assert headers3.headers["X-Cache"] == "miss"

	def test_fc_analytics_cache_header_distinct_params(self, mock_db):
		"""Test that /api/fc-activity/analytics X-Cache header respects parameter differences."""

		with patch('backend.analytics_service._fetch_fc_activity_analytics_impl') as mock_impl:
			mock_impl.return_value = {"x": "year", "data": []}

			clear_analytics_cache()
			set_analytics_cache_enabled(True)

			# First call should be miss
			headers1 = Response()
			fc_activity_analytics(
				response=headers1,
				x="year",
				group_by="full_history_resolution",
				year_from=None,
				year_to=None,
				city="",
				source_type="",
				db=mock_db,
			)
			assert headers1.headers["X-Cache"] == "miss"

			# Second call with same params should be hit
			headers2 = Response()
			fc_activity_analytics(
				response=headers2,
				x="year",
				group_by="full_history_resolution",
				year_from=None,
				year_to=None,
				city="",
				source_type="",
				db=mock_db,
			)
			assert headers2.headers["X-Cache"] == "hit"

			# Different params should be miss
			headers3 = Response()
			fc_activity_analytics(
				response=headers3,
				x="city",
				group_by="full_history_resolution",
				year_from=None,
				year_to=None,
				city="",
				source_type="",
				db=mock_db,
			)
			assert headers3.headers["X-Cache"] == "miss"

	def test_cache_header_when_disabled(self, mock_db):
		"""Test that X-Cache header is set even when cache is disabled."""
		with patch('backend.analytics_service._fetch_about_stats_impl') as mock_impl:
			mock_impl.return_value = {"cases": 100}

			clear_analytics_cache()
			set_analytics_cache_enabled(True)
			enabled_headers = Response()
			enabled_result = about_stats(response=enabled_headers, db=mock_db)

			clear_analytics_cache()
			set_analytics_cache_enabled(False)
			disabled_headers = Response()
			disabled_result = about_stats(response=disabled_headers, db=mock_db)
			assert "X-Cache" in disabled_headers.headers
			assert disabled_headers.headers["X-Cache"] == "miss"
			assert disabled_result == enabled_result

			set_analytics_cache_enabled(True)


class TestParameterNormalization:
	"""Test that complete parameter sets create distinct cache keys."""

	def test_all_parameters_included_in_key(self, mock_db):
		"""Test that all endpoint parameters are included in cache key."""
		clear_analytics_cache()

		with patch('backend.analytics_service._fetch_judge_profiles_impl') as mock_impl:
			mock_impl.return_value = [{"name": "Smith"}]

			# Call with q="smith" and default limit=50
			result1, hit1 = fetch_judge_profiles(mock_db, q="smith", limit=50)
			assert hit1 is False
			assert mock_impl.call_count == 1

			# Call with q="smith" and explicit limit=50 (should hit same cache)
			result2, hit2 = fetch_judge_profiles(mock_db, q="smith", limit=50)
			assert hit2 is True
			assert mock_impl.call_count == 1

			# Call with q="smith" but different limit should be miss
			mock_impl.return_value = [{"name": "Smith"}]  # Same result
			result3, hit3 = fetch_judge_profiles(mock_db, q="smith", limit=100)
			assert hit3 is False  # Different limit creates different cache key
			assert mock_impl.call_count == 2

	def test_fc_analytics_all_parameters_distinct(self, mock_db):
		"""Test that FC analytics distinguishes all parameter values."""
		clear_analytics_cache()

		with patch('backend.analytics_service._fetch_fc_activity_analytics_impl') as mock_impl:
			mock_impl.return_value = {"x": "year", "data": []}

			# First call with x="year"
			result1, hit1 = fetch_fc_activity_analytics(mock_db, x="year", group_by="full_history_resolution")
			assert hit1 is False
			assert mock_impl.call_count == 1

			# Same parameters should hit
			result2, hit2 = fetch_fc_activity_analytics(mock_db, x="year", group_by="full_history_resolution")
			assert hit2 is True
			assert mock_impl.call_count == 1

			# Different x value should miss
			result3, hit3 = fetch_fc_activity_analytics(mock_db, x="city", group_by="full_history_resolution")
			assert hit3 is False
			assert mock_impl.call_count == 2

			# Different group_by value should miss
			result4, hit4 = fetch_fc_activity_analytics(mock_db, x="year", group_by="other_grouping")
			assert hit4 is False
			assert mock_impl.call_count == 3

	def test_fc_analytics_includes_every_query_parameter(self, mock_db):
		base = {
			"x": "year",
			"group_by": "full_history_resolution",
			"year_from": None,
			"year_to": None,
			"city": "",
			"source_type": "",
		}
		changes = {
			"x": "city",
			"group_by": "case_class",
			"year_from": 2010,
			"year_to": 2020,
			"city": "Ottawa",
			"source_type": "portal",
		}
		with patch("backend.analytics_service._fetch_fc_activity_analytics_impl", return_value={"data": []}) as impl:
			for parameter, value in changes.items():
				clear_analytics_cache()
				fetch_fc_activity_analytics(mock_db, **base)
				changed = {**base, parameter: value}
				_, was_hit = fetch_fc_activity_analytics(mock_db, **changed)
				assert not was_hit, f"{parameter} must be part of the cache key"
			assert impl.call_count == len(changes) * 2
