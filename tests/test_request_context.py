"""Focused tests for request observability: ID generation, validation, and slow-request logging."""

from fastapi.testclient import TestClient
import json
import logging
from unittest.mock import MagicMock, patch
import os

from backend.request_context import (
    generate_request_id,
    validate_request_id,
    _REQUEST_ID_PATTERN,
    get_version_info,
    SlowRequestLogger,
    get_slow_request_logger,
    get_request_id,
    set_request_id,
    _request_id_context,
)


def _app_without_access_gate(monkeypatch):
    """Keep route tests independent of local optional-access configuration."""
    from backend import main

    monkeypatch.setattr(
        main, "_private_access_config", lambda: (None, "", 86400)
    )
    return main.app


class TestRequestIDGeneration:
    """Test request ID generation and format validation."""

    def test_generated_id_matches_pattern(self):
        """Generated request IDs must match the bounded pattern."""
        for _ in range(10):
            generated_id = generate_request_id()
            assert _REQUEST_ID_PATTERN.match(generated_id), f"Generated ID {generated_id} does not match pattern"

    def test_generated_id_has_correct_length(self):
        """Generated request IDs must be exactly 24 characters."""
        for _ in range(10):
            generated_id = generate_request_id()
            assert len(generated_id) == 24

    def test_generated_id_uses_allowed_charset(self):
        """Generated request IDs use only ASCII letters, digits, underscores, and hyphens."""
        allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
        for _ in range(10):
            generated_id = generate_request_id()
            assert all(c in allowed for c in generated_id)

    def test_generated_ids_are_unique(self):
        """Generated request IDs should be unique (with overwhelming probability)."""
        ids = {generate_request_id() for _ in range(100)}
        assert len(ids) == 100


class TestRequestIDValidation:
    """Test request ID validation and fallback."""

    def test_valid_id_is_preserved(self):
        """Valid incoming request IDs must be preserved."""
        valid_ids = [
            "abc123def456",
            "Test-Request-ID-12345",
            "a" * 24,  # Exactly 24 chars
            "a" * 8,   # Minimum 8 chars
            "a" * 64,  # Maximum 64 chars
            "abc_123-XYZ",
        ]
        for valid_id in valid_ids:
            result = validate_request_id(valid_id)
            assert result == valid_id, f"Valid ID {valid_id} was not preserved"

    def test_invalid_ids_are_rejected(self):
        """Invalid incoming request IDs must be replaced with a generated one."""
        invalid_ids = [
            None,
            "",
            "a" * 7,  # Too short
            "a" * 65,  # Too long
            "abc@123",  # Invalid character @
            "abc#123",  # Invalid character #
            "abc 123",  # Invalid character space
            "abc\n123",  # Invalid character newline
            "abcdefgh\n",  # Newline at the end must not pass a partial regex match
            "abc/123",  # Invalid character /
            "abc\\123",  # Invalid character backslash
            123,  # Non-string
            {"id": "test"},  # Dict
        ]
        for invalid_id in invalid_ids:
            result = validate_request_id(invalid_id)
            assert _REQUEST_ID_PATTERN.match(result), f"Replacement ID for {invalid_id} does not match pattern"
            assert result != invalid_id or invalid_id is None or invalid_id == "", f"Invalid ID {invalid_id} was not replaced"

    def test_malformed_control_oversized_are_replaced(self):
        """Malformed, control, and oversized incoming values must be replaced."""
        test_cases = [
            ("a" * 3, "too short"),
            ("a" * 100, "too long"),
            ("\x00\x01\x02", "control characters"),
            ("../../../etc/passwd", "path traversal attempt"),
        ]
        for invalid, reason in test_cases:
            result = validate_request_id(invalid)
            assert result != invalid, f"{reason}: ID should be replaced"
            assert _REQUEST_ID_PATTERN.match(result), f"{reason}: Replacement should match pattern"


class TestContextVar:
    """Test ContextVar storage and retrieval."""

    def test_set_and_get_request_id(self):
        """Request ID must be settable and retrievable from context."""
        test_id = "test-request-id-12345678"
        token = set_request_id(test_id)
        assert get_request_id() == test_id
        _request_id_context.reset(token)
        # After reset, should be None (default)
        assert get_request_id() is None

    def test_context_var_reset_in_finally(self):
        """Context must be resetable via token."""
        id1 = "first-request-12345678"
        id2 = "second-request-1234567"

        token1 = set_request_id(id1)
        assert get_request_id() == id1

        token2 = set_request_id(id2)
        assert get_request_id() == id2

        # Reset to id1
        _request_id_context.reset(token2)
        assert get_request_id() == id1

        # Reset to None
        _request_id_context.reset(token1)
        assert get_request_id() is None


class TestVersionInfo:
    """Test safe version information."""

    def test_version_info_has_required_fields(self):
        """Version info must include commit, started_at, and python_version."""
        version_info = get_version_info()
        assert "commit" in version_info
        assert "started_at" in version_info
        assert "python_version" in version_info

    def test_commit_is_git_hash_or_unknown(self):
        """Commit must be either a valid hex string or 'unknown'."""
        version_info = get_version_info()
        commit = version_info["commit"]
        assert isinstance(commit, str)
        if commit != "unknown":
            # Must be hex (lowercase or uppercase) and/or dash
            assert all(c in "0123456789abcdefABCDEF-" for c in commit)
            assert len(commit) <= 40

    def test_commit_from_app_commit_env(self):
        """APP_COMMIT env var should be used if valid."""
        with patch.dict(os.environ, {"APP_COMMIT": "abc123def4"}, clear=False):
            version_info = get_version_info()
            assert version_info["commit"] == "abc123def4"

    def test_commit_invalid_app_commit_becomes_unknown(self):
        """Invalid APP_COMMIT is never exposed; safe Git fallback is used."""
        with (
            patch.dict(os.environ, {"APP_COMMIT": "invalid@@@"}, clear=False),
            patch(
                "backend.request_context._get_git_commit",
                return_value="unknown",
            ) as git_commit,
        ):
            version_info = get_version_info()
            assert version_info["commit"] == "unknown"
            git_commit.assert_called_once()

    def test_git_commit_not_read_without_git_directory(self, monkeypatch, tmp_path):
        """Git is not invoked unless the repository .git directory exists."""
        from backend import request_context

        monkeypatch.setattr(request_context, "_REPOSITORY_ROOT", tmp_path)
        run = MagicMock()
        monkeypatch.setattr(request_context.subprocess, "run", run)
        request_context._get_git_commit.cache_clear()

        assert request_context._get_git_commit() == "unknown"
        run.assert_not_called()

        request_context._get_git_commit.cache_clear()

    def test_git_commit_is_sanitized_when_git_directory_exists(self, monkeypatch, tmp_path):
        """A valid short hash is returned only after the guarded Git query."""
        from backend import request_context

        (tmp_path / ".git").mkdir()
        monkeypatch.setattr(request_context, "_REPOSITORY_ROOT", tmp_path)
        run = MagicMock(return_value=MagicMock(returncode=0, stdout="ABC1234\n"))
        monkeypatch.setattr(request_context.subprocess, "run", run)
        request_context._get_git_commit.cache_clear()

        assert request_context._get_git_commit() == "abc1234"
        assert run.call_args.kwargs["cwd"] == str(tmp_path)
        run.assert_called_once()

        request_context._get_git_commit.cache_clear()

    def test_git_commit_output_with_extra_data_becomes_unknown(self, monkeypatch, tmp_path):
        """Git output is accepted only when it is a sanitized short hash."""
        from backend import request_context

        (tmp_path / ".git").mkdir()
        monkeypatch.setattr(request_context, "_REPOSITORY_ROOT", tmp_path)
        run = MagicMock(
            return_value=MagicMock(
                returncode=0, stdout="abc1234\nhost.example"
            )
        )
        monkeypatch.setattr(request_context.subprocess, "run", run)
        request_context._get_git_commit.cache_clear()

        assert request_context._get_git_commit() == "unknown"
        run.assert_called_once()

        request_context._get_git_commit.cache_clear()

    def test_started_at_is_unix_timestamp(self):
        """started_at must be a Unix timestamp (integer)."""
        version_info = get_version_info()
        started_at = version_info["started_at"]
        assert isinstance(started_at, int)
        assert started_at > 0

    def test_python_version_is_string(self):
        """python_version must be a string."""
        version_info = get_version_info()
        python_version = version_info["python_version"]
        assert isinstance(python_version, str)
        assert len(python_version) > 0
        # Should look like a version (has dots)
        assert "." in python_version

    def test_version_no_secrets_or_hostnames(self):
        """Version info must never expose secrets or hostnames."""
        version_info = get_version_info()
        info_str = str(version_info)
        assert "localhost" not in info_str.lower()
        assert "127.0.0.1" not in info_str
        assert "$" not in info_str
        assert "${" not in info_str


class TestSlowRequestLogger:
    """Test optional slow-request logging."""

    def test_slow_request_logger_disabled_by_default(self):
        """Slow-request logging must be disabled by default."""
        with patch.dict(os.environ, {}, clear=False):
            # Remove any existing threshold env var
            if "SLOW_REQUEST_LOG_MS" in os.environ:
                del os.environ["SLOW_REQUEST_LOG_MS"]

            logger = SlowRequestLogger()
            assert logger.threshold_ms is None
            assert logger.logger is None

    def test_slow_request_logger_respects_threshold_config(self):
        """Slow-request logger must respect SLOW_REQUEST_LOG_MS."""
        with patch.dict(os.environ, {"SLOW_REQUEST_LOG_MS": "500"}):
            logger = SlowRequestLogger()
            assert logger.threshold_ms == 500

    def test_slow_request_logger_ignores_invalid_threshold(self):
        """Invalid threshold values must be ignored."""
        with patch.dict(os.environ, {"SLOW_REQUEST_LOG_MS": "invalid"}):
            logger = SlowRequestLogger()
            assert logger.threshold_ms is None
            assert logger.logger is None

    def test_slow_request_logger_ignores_zero_or_negative_threshold(self):
        """Zero or negative threshold values must be ignored."""
        for invalid_value in ["0", "-100", "-1"]:
            with patch.dict(os.environ, {"SLOW_REQUEST_LOG_MS": invalid_value}):
                logger = SlowRequestLogger()
                assert logger.threshold_ms is None

    def test_should_log_respects_threshold_strictly_greater_than(self):
        """Only requests strictly exceeding threshold are logged, not equal to threshold."""
        with patch.dict(os.environ, {"SLOW_REQUEST_LOG_MS": "100"}):
            logger = SlowRequestLogger()
            assert logger.should_log(99.9) is False  # Below threshold
            assert logger.should_log(100.0) is False  # Equal to threshold (not strictly greater)
            assert logger.should_log(100.1) is True   # Strictly greater

    def test_slow_request_logger_logs_safe_info_only(self):
        """Slow-request logging must include only safe information."""
        with patch.dict(os.environ, {"SLOW_REQUEST_LOG_MS": "10"}):
            logger = SlowRequestLogger()

            # Mock the logger to capture calls
            logger.logger = MagicMock()

            logger.log(
                request_id="test-request-123",
                method="GET",
                route_template="/api/search",
                status=200,
                elapsed_ms=50.0,
            )

            # Verify logger was called
            logger.logger.info.assert_called_once()
            args, kwargs = logger.logger.info.call_args

            # Should include safe fields
            metadata = json.loads(args[0])
            assert set(metadata) == {
                "request_id", "method", "route_template", "status", "duration_ms"
            }
            assert metadata["request_id"] == "test-request-123"
            assert metadata["method"] == "GET"
            assert metadata["route_template"] == "/api/search"
            assert metadata["status"] == 200
            assert metadata["duration_ms"] == 50.0
            assert "\n" not in args[0]

    def test_slow_request_info_reaches_uvicorn_error_logger(self, caplog):
        """INFO events use Uvicorn's configured stderr logger path."""
        from uvicorn.config import LOGGING_CONFIG

        with patch.dict(os.environ, {"SLOW_REQUEST_LOG_MS": "10"}):
            logger = SlowRequestLogger()

        with caplog.at_level(logging.INFO, logger="uvicorn.error"):
            logger.log(
                request_id="test-request-123",
                method="GET",
                route_template="/api/search",
                status=200,
                elapsed_ms=20.0,
            )

        error_logger_config = LOGGING_CONFIG["loggers"]["uvicorn.error"]
        parent_logger_config = LOGGING_CONFIG["loggers"]["uvicorn"]
        default_handler = LOGGING_CONFIG["handlers"]["default"]
        assert logger.logger.name == "uvicorn.error"
        assert error_logger_config["level"] == "INFO"
        assert error_logger_config.get("propagate", True)
        assert "default" in parent_logger_config["handlers"]
        assert default_handler["stream"] == "ext://sys.stderr"
        record = next(record for record in caplog.records if record.name == "uvicorn.error")
        metadata = json.loads(record.getMessage())
        assert metadata["request_id"] == "test-request-123"
        assert metadata["route_template"] == "/api/search"

    def test_slow_request_logger_uses_safe_marker_for_unknown_route(self):
        """When route template is unavailable, use a fixed safe marker."""
        with patch.dict(os.environ, {"SLOW_REQUEST_LOG_MS": "10"}):
            logger = SlowRequestLogger()
            logger.logger = MagicMock()

            logger.log(
                request_id="test-request",
                method="POST",
                route_template=None,
                status=500,
                elapsed_ms=150.0,
            )

            args, kwargs = logger.logger.info.call_args
            metadata = json.loads(args[0])
            assert metadata["route_template"] == "<unknown>"

    def test_get_slow_request_logger_returns_singleton(self):
        """get_slow_request_logger must return the same instance."""
        logger1 = get_slow_request_logger()
        logger2 = get_slow_request_logger()
        assert logger1 is logger2


class TestRequestContextMiddlewareIntegration:
    """Exercise the middleware registered on the real application."""

    def test_every_response_receives_request_id_header(self, monkeypatch):
        """Successful and ordinary error responses carry an X-Request-ID."""

        app = _app_without_access_gate(monkeypatch)
        response = TestClient(app).get("/api/version")
        assert response.status_code == 200
        assert "x-request-id" in response.headers
        assert _REQUEST_ID_PATTERN.fullmatch(response.headers["x-request-id"])

    def test_incoming_valid_request_id_is_preserved_in_response(self, monkeypatch):
        """Valid incoming request IDs must be preserved in response header."""

        app = _app_without_access_gate(monkeypatch)
        custom_id = "custom-request-id-12345678"
        response = TestClient(app).get(
            "/api/version", headers={"x-request-id": custom_id}
        )

        assert response.status_code == 200
        assert response.headers["x-request-id"] == custom_id

    def test_middleware_sets_and_resets_contextvar(self, monkeypatch):
        """The current ID is available downstream and reset after the response."""
        app = _app_without_access_gate(monkeypatch)

        def context_endpoint():
            return {"request_id": get_request_id()}

        app.add_api_route(
            "/__request_context_test_context",
            context_endpoint,
            methods=["GET"],
            include_in_schema=False,
        )
        response = TestClient(app).get("/__request_context_test_context")

        assert response.status_code == 200
        assert response.json()["request_id"] == response.headers["x-request-id"]
        assert get_request_id() is None

    def test_invalid_request_id_is_replaced_in_response(self, monkeypatch):
        """Invalid incoming request IDs must be replaced with a generated one."""

        app = _app_without_access_gate(monkeypatch)
        response = TestClient(app).get(
            "/api/version", headers={"x-request-id": "invalid@@@"}
        )

        assert response.status_code == 200
        returned_id = response.headers["x-request-id"]
        assert returned_id != "invalid@@@"
        assert _REQUEST_ID_PATTERN.fullmatch(returned_id)

    def test_unknown_route_response_preserves_request_id(self, monkeypatch):
        """Responses returned by middleware/routing also carry request IDs."""
        app = _app_without_access_gate(monkeypatch)
        incoming_id = "route-request-id-12345678"

        response = TestClient(app).get(
            "/not-a-real-route", headers={"x-request-id": incoming_id}
        )
        assert response.status_code == 404
        assert "x-request-id" in response.headers
        assert response.headers["x-request-id"] == incoming_id

    def test_password_gate_response_receives_request_id(self, monkeypatch):
        """A response generated by the access middleware also carries the ID."""
        from backend import main

        monkeypatch.setattr(
            main, "_private_access_config", lambda: ("test-only", "test-only", 86400)
        )
        response = TestClient(main.app).get(
            "/not-a-real-route",
            headers={
                "accept": "application/json",
                "x-request-id": "auth-request-id-12345678",
            },
        )

        assert response.status_code == 401
        assert response.headers["x-request-id"] == "auth-request-id-12345678"

    def test_internal_error_response_receives_request_id(self, monkeypatch):
        """The generic server error response preserves request correlation."""
        from backend import main

        monkeypatch.setattr(
            main, "_private_access_config", lambda: (None, "", 86400)
        )

        def fail():
            raise RuntimeError("test-only failure")

        main.app.add_api_route(
            "/__request_context_test_error",
            fail,
            methods=["GET"],
            include_in_schema=False,
        )
        response = TestClient(main.app, raise_server_exceptions=False).get(
            "/__request_context_test_error",
            headers={"x-request-id": "malformed@@@"},
        )

        assert response.status_code == 500
        assert "x-request-id" in response.headers
        assert response.headers["x-request-id"] != "malformed@@@"
        assert _REQUEST_ID_PATTERN.fullmatch(response.headers["x-request-id"])

    def test_slow_log_uses_resolved_route_template_only(self, monkeypatch):
        """Slow-request fields exclude the raw path and query string."""

        app = _app_without_access_gate(monkeypatch)
        logger = MagicMock()
        logger.should_log.return_value = True
        # Patch at the source in request_context where middleware calls it
        monkeypatch.setattr("backend.request_context.get_slow_request_logger", lambda: logger)

        response = TestClient(app).get(
            "/api/version?search=private-user-query"
        )

        assert response.status_code == 200
        logger.log.assert_called_once()
        fields = logger.log.call_args.kwargs
        assert fields["route_template"] == "/api/version"
        assert fields["request_id"] == response.headers["x-request-id"]
        assert "private-user-query" not in repr(fields)


class TestHealthAndVersionEndpoints:
    """Test health readiness with version and /api/version endpoint."""

    def test_api_version_endpoint_returns_version_info(self, monkeypatch):
        """GET /api/version must return safe version information."""

        app = _app_without_access_gate(monkeypatch)
        client = TestClient(app)
        response = client.get("/api/version")

        assert response.status_code == 200
        data = response.json()
        assert set(data) == {"commit", "started_at", "python_version"}
        assert "commit" in data
        assert "started_at" in data
        assert "python_version" in data

    def test_api_version_endpoint_no_secrets_or_hostnames(self, monkeypatch):
        """GET /api/version must never expose secrets or hostnames."""

        app = _app_without_access_gate(monkeypatch)
        client = TestClient(app)
        response = client.get("/api/version")

        assert response.status_code == 200
        body = response.json()
        body_str = str(body)

        # Should not contain common secret patterns
        assert "$" not in body_str
        assert "localhost" not in body_str.lower()
        assert "127.0.0.1" not in body_str

    def test_health_ready_includes_version(self, monkeypatch):
        """GET /health/ready must include version information."""
        from backend import main

        monkeypatch.setattr(
            main,
            "readiness",
            lambda: (
                {"status": "ok", "checks": {"test": {"status": "ok"}}},
                True,
            ),
        )

        client = TestClient(main.app)
        response = client.get("/health/ready")

        assert response.status_code == 200
        data = response.json()
        assert "version" in data
        version_info = data["version"]
        assert "commit" in version_info
        assert "started_at" in version_info
        assert "python_version" in version_info
