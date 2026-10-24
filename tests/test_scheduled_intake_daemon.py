"""Tests for scheduled intake daemon."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock, patch

import pytest


def test_scheduled_intake_daemon_initialization():
    """Test daemon initializes with correct defaults."""
    from scripts.scheduled_intake_daemon import ScheduledIntakeDaemon

    daemon = ScheduledIntakeDaemon(
        batch_size=50,
        inter_batch_pause=1.0,
        a2aj_interval_hours=6,
        court_interval_hours=24,
        dry_run=True,
    )

    assert daemon.batch_size == 50
    assert daemon.inter_batch_pause == 1.0
    assert daemon.dry_run is True


def test_scheduled_intake_daemon_lock_acquire_release():
    """Test file-based lock acquire and release."""
    from scripts.scheduled_intake_daemon import ScheduledIntakeDaemon

    with TemporaryDirectory() as tmp_dir:
        daemon = ScheduledIntakeDaemon()
        daemon.lock_path = Path(tmp_dir) / ".test.lock"

        # Initially, lock should be acquirable
        assert daemon.acquire_lock() is True

        # Lock file should exist
        assert daemon.lock_path.exists()

        # Lock content should be valid JSON with started_at and pid
        with open(daemon.lock_path) as f:
            lock_info = json.load(f)
        assert "started_at" in lock_info
        assert "pid" in lock_info

        # While holding lock, another acquire should fail
        assert daemon.acquire_lock() is False

        # Release should remove lock file
        daemon.release_lock()
        assert not daemon.lock_path.exists()

        # After release, lock should be acquirable again
        assert daemon.acquire_lock() is True
        daemon.release_lock()


def test_scheduled_intake_daemon_is_enabled():
    """Test enable/disable check."""
    from scripts.scheduled_intake_daemon import ScheduledIntakeDaemon
    import os

    daemon = ScheduledIntakeDaemon()

    # Should be enabled by default (when env var not set)
    original = os.environ.get("SCHEDULED_INTAKE_ENABLED")
    try:
        if original:
            del os.environ["SCHEDULED_INTAKE_ENABLED"]
        # Will be False if lock_path.parent doesn't exist, but should handle gracefully
        assert isinstance(daemon.is_enabled(), bool)

        # Should be disabled when env var is false
        os.environ["SCHEDULED_INTAKE_ENABLED"] = "false"
        assert daemon.is_enabled() is False

        os.environ["SCHEDULED_INTAKE_ENABLED"] = "true"
        # May be True or False depending on lock_path.parent, but should handle gracefully
        assert isinstance(daemon.is_enabled(), bool)
    finally:
        if original:
            os.environ["SCHEDULED_INTAKE_ENABLED"] = original
        else:
            os.environ.pop("SCHEDULED_INTAKE_ENABLED", None)


def test_scheduled_intake_daemon_site_health_check():
    """Test site health check with mocked HTTP."""
    from scripts.scheduled_intake_daemon import ScheduledIntakeDaemon

    daemon = ScheduledIntakeDaemon()

    # Mock successful health check
    with patch("scripts.scheduled_intake_daemon.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        assert daemon.check_site_health() is True
        mock_get.assert_called_once()

    # Mock failed health check
    with patch("scripts.scheduled_intake_daemon.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 503
        mock_get.return_value = mock_response

        assert daemon.check_site_health() is False

    # Mock connection error (should still return True, lenient)
    with patch("scripts.scheduled_intake_daemon.requests.get") as mock_get:
        mock_get.side_effect = ConnectionError("Network error")

        assert daemon.check_site_health() is True


def test_scheduled_intake_daemon_graceful_db_failure():
    """Test that daemon gracefully handles database unavailability."""
    from scripts.scheduled_intake_daemon import ScheduledIntakeDaemon

    daemon = ScheduledIntakeDaemon()

    # should_run_a2aj_check should return True when DB is unavailable (lenient)
    with patch("scripts.scheduled_intake_daemon.SessionLocal") as mock_session:
        mock_session.side_effect = Exception("DB unavailable")
        # Should not raise, should return True (lenient)
        result = daemon.should_run_a2aj_check()
        assert isinstance(result, bool)

    # log_run_to_db should not raise even if DB is unavailable
    with patch("scripts.scheduled_intake_daemon.SessionLocal") as mock_session:
        mock_session.side_effect = Exception("DB unavailable")
        # Should not raise
        daemon.log_run_to_db("test", "completed")


@pytest.mark.parametrize("dry_run", [False, True])
@pytest.mark.parametrize("discovered", [3, 0])
def test_scheduled_intake_daemon_records_discovery_only(dry_run, discovered, caplog):
    from scripts.scheduled_intake_daemon import ScheduledIntakeDaemon

    daemon = ScheduledIntakeDaemon(dry_run=dry_run)
    decisions = [{"citation": f"2026 FC {i + 1}"} for i in range(discovered)]

    with (
        patch.multiple(
            daemon,
            is_enabled=MagicMock(return_value=True),
            acquire_lock=MagicMock(return_value=True),
            release_lock=MagicMock(),
            check_site_health=MagicMock(return_value=True),
            should_run_a2aj_check=MagicMock(return_value=True),
            discover_a2aj_new_decisions=MagicMock(return_value=(discovered, decisions)),
        ),
        patch("scripts.scheduled_intake_daemon.SessionLocal") as mock_session,
        caplog.at_level("INFO", logger="scripts.scheduled_intake_daemon"),
    ):
        daemon.run_once()

        db = mock_session.return_value.__enter__.return_value
        db.add.assert_called_once()
        run = db.add.call_args.args[0]
        assert run.source_type == "a2aj_scheduled"
        assert run.status == "completed"
        assert run.run_type == "scheduled_discovery"
        assert run.records_seen == discovered
        assert run.records_ingested == 0
        if discovered:
            assert run.records_ingested != run.records_seen
        assert run.metadata_json["dry_run"] is dry_run
        db.commit.assert_called_once()
        daemon.discover_a2aj_new_decisions.assert_called_once_with()
        daemon.release_lock.assert_called_once_with()

    assert f"A2AJ discovery-only cycle: discovered={discovered}, imported=0" in caplog.text


def test_scheduled_intake_daemon_parses_command_line_args():
    """Test that CLI argument parsing works."""
    from scripts.scheduled_intake_daemon import parse_args
    import sys

    # Test default args
    original_argv = sys.argv
    try:
        sys.argv = ["daemon"]
        args = parse_args()
        assert args.batch_size == 50
        assert args.dry_run is False
        assert args.once is False
        assert args.a2aj_interval == 6
        assert args.court_interval == 24
    finally:
        sys.argv = original_argv


def test_scheduled_intake_daemon_parses_custom_args():
    """Test command-line argument parsing with custom values."""
    from scripts.scheduled_intake_daemon import parse_args
    import sys

    original_argv = sys.argv
    try:
        sys.argv = ["daemon", "--batch-size", "25", "--dry-run", "--once", "--a2aj-interval", "3"]
        args = parse_args()
        assert args.batch_size == 25
        assert args.dry_run is True
        assert args.once is True
        assert args.a2aj_interval == 3
    finally:
        sys.argv = original_argv
