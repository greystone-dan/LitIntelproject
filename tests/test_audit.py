import asyncio
import io
import json
from datetime import datetime, timezone
from uuid import UUID

import pytest
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.testclient import TestClient

from backend import audit


@pytest.fixture
def audit_app(monkeypatch, tmp_path):
    monkeypatch.delenv("CASELIBRARY_AUDIT_LOG", raising=False)
    monkeypatch.delenv("CASELIBRARY_AUDIT_LOG_RAW_ADDRESS", raising=False)
    app = FastAPI()

    async def echo(request: Request):
        return {"content": (await request.body()).decode("utf-8")}

    for path in (
        "/health",
        "/live-analysis",
        "/live-analysis/analyze",
        "/live-analysis/resolve",
        "/memo-citation-check",
        "/api/deidentify",
        "/api/deidentify/docx",
        "/api/reidentify",
        "/upload/{filename}",
    ):
        app.add_api_route(path, echo, methods=["GET", "POST"])

    middleware = audit.RequestAuditMiddleware(app)
    yield app, middleware, tmp_path / "requests.jsonl"
    if middleware.handler is not None:
        middleware.handler.close()


def enable(monkeypatch, audit_app):
    app, middleware, path = audit_app
    monkeypatch.setenv("CASELIBRARY_AUDIT_LOG", str(path))
    middleware.__init__(app)
    return middleware, path


@pytest.mark.parametrize("setting", [None, ""])
def test_audit_off_does_not_create_handler_or_file(monkeypatch, audit_app, setting):
    if setting is not None:
        monkeypatch.setenv("CASELIBRARY_AUDIT_LOG", setting)

    def forbidden_handler(*args, **kwargs):
        pytest.fail("disabled auditing must not open a file")

    monkeypatch.setattr(audit, "_QuietRotatingFileHandler", forbidden_handler)
    app, middleware, path = audit_app
    middleware.__init__(app)
    assert TestClient(middleware).get("/health").status_code == 200
    assert middleware.handler is None
    assert not path.exists()


def test_audit_metadata_and_hash(monkeypatch, audit_app):
    middleware, path = enable(monkeypatch, audit_app)
    client = TestClient(middleware)
    for _ in range(2):
        assert client.get("/health?query=private-query").status_code == 200
    records = [json.loads(line) for line in path.read_text().splitlines()]
    assert len(records) == 2
    record = records[0]
    assert set(record) == {
        "time",
        "request_id",
        "method",
        "path",
        "status",
        "duration_ms",
        "client_address_hash",
    }
    assert datetime.fromisoformat(record["time"]).tzinfo == timezone.utc
    UUID(record["request_id"])
    assert record["request_id"] != records[1]["request_id"]
    assert record["method"] == "GET"
    assert record["path"] == "/health"
    assert record["status"] == 200
    assert record["duration_ms"] >= 0
    assert len(record["client_address_hash"]) == 64
    assert record["client_address_hash"] == records[1]["client_address_hash"]
    assert "testclient" not in path.read_text()
    assert "private-query" not in path.read_text()


@pytest.mark.parametrize(
    "route",
    [
        "/live-analysis",
        "/live-analysis/analyze",
        "/live-analysis/resolve",
        "/memo-citation-check",
        "/api/deidentify",
        "/api/deidentify/docx",
        "/api/reidentify",
    ],
)
def test_sensitive_routes_never_log_content(monkeypatch, audit_app, route):
    middleware, path = enable(monkeypatch, audit_app)
    response = TestClient(middleware).post(
        route + "?text=private-query",
        headers={"X-Request-ID": "private-header"},
        files={"file": ("private-filename.docx", b"private-document")},
    )
    assert response.status_code == 200
    assert "private-document" in response.text
    text = path.read_text()
    assert "private-" not in text
    assert json.loads(text)["path"] == route


@pytest.mark.parametrize(
    "setting,allowed", [("true", True), ("TRUE", True), ("false", False), ("", False)]
)
def test_raw_address_requires_explicit_opt_in(monkeypatch, audit_app, setting, allowed):
    monkeypatch.setenv("CASELIBRARY_AUDIT_LOG_RAW_ADDRESS", setting)
    middleware, path = enable(monkeypatch, audit_app)
    TestClient(middleware).get("/health")
    record = json.loads(path.read_text())
    assert ("client_address" in record) is allowed
    if allowed:
        assert record["client_address"] == "testclient"
    assert len(record["client_address_hash"]) == 64


def test_paths_do_not_log_filenames_or_unmatched_input(monkeypatch, audit_app):
    middleware, path = enable(monkeypatch, audit_app)
    client = TestClient(middleware)
    assert client.post("/upload/private-filename.docx").status_code == 200
    assert client.get("/private-unmatched").status_code == 404
    records = [json.loads(line) for line in path.read_text().splitlines()]
    assert [record["path"] for record in records] == [
        "/upload/{filename}",
        "<unmatched>",
    ]
    assert records[1]["status"] == 404
    assert "private-" not in path.read_text()


@pytest.mark.parametrize("failure", ["open", "write", "rotation", "handler"])
def test_audit_failure_does_not_break_request(monkeypatch, audit_app, capsys, failure):
    middleware, path = enable(monkeypatch, audit_app)

    def fail(*args, **kwargs):
        raise OSError("private-error")

    if failure == "open":
        monkeypatch.setattr(middleware.handler, "_open", fail)
    elif failure == "write":

        class BrokenStream(io.StringIO):
            write = fail

        middleware.handler.stream = BrokenStream()
    elif failure == "rotation":
        middleware.handler.maxBytes = 1
        monkeypatch.setattr(middleware.handler, "doRollover", fail)
    else:
        monkeypatch.setattr(middleware.handler, "handle", fail)
    response = TestClient(middleware).post("/health", content="private-document")
    assert response.status_code == 200
    assert response.json() == {"content": "private-document"}
    assert capsys.readouterr().err == ""


def test_audit_configuration_failure_is_fail_open(monkeypatch, audit_app):
    monkeypatch.setenv("CASELIBRARY_AUDIT_LOG", "invalid-path")

    def fail(*args, **kwargs):
        raise OSError("private-error")

    monkeypatch.setattr(audit, "_QuietRotatingFileHandler", fail)
    app, middleware, path = audit_app
    middleware.__init__(app)
    assert TestClient(middleware).get("/health").status_code == 200
    assert not path.exists()


def test_handler_errors_are_logged_without_changing_exception(monkeypatch, audit_app):
    app, _, _ = audit_app

    @app.get("/broken")
    def broken():
        raise RuntimeError("private-error")

    middleware, path = enable(monkeypatch, audit_app)
    with pytest.raises(RuntimeError, match="private-error"):
        TestClient(middleware).get("/broken")
    assert json.loads(path.read_text())["status"] == 500
    assert "private-error" not in path.read_text()


def test_audit_rotates(monkeypatch, audit_app):
    middleware, path = enable(monkeypatch, audit_app)
    assert middleware.handler.maxBytes == 5 * 1024 * 1024
    assert middleware.handler.backupCount == 3
    middleware.handler.maxBytes = 500
    client = TestClient(middleware)
    for _ in range(8):
        client.get("/health")
    assert path.exists()
    assert path.with_name(path.name + ".1").exists()
    assert not path.with_name(path.name + ".4").exists()
    for file in path.parent.glob("requests.jsonl*"):
        for line in file.read_text().splitlines():
            assert json.loads(line)["status"] == 200


def test_streaming_response_is_not_consumed_or_logged(monkeypatch, audit_app):
    app, _, _ = audit_app

    @app.get("/stream")
    def stream():
        return StreamingResponse(iter(["private-first", "private-second"]))

    middleware, path = enable(monkeypatch, audit_app)
    assert TestClient(middleware).get("/stream").text == "private-firstprivate-second"
    assert "private-" not in path.read_text()


def test_missing_client_address(monkeypatch, audit_app):
    middleware, path = enable(monkeypatch, audit_app)

    async def request(scope, receive, send):
        await send({"type": "http.response.start", "status": 204, "headers": []})
        await send({"type": "http.response.body", "body": b""})

    async def unused_receive():
        pytest.fail("middleware must not read the request body")

    async def send(message):
        pass

    middleware.app = request
    asyncio.run(middleware({"type": "http", "method": "GET"}, unused_receive, send))
    assert json.loads(path.read_text())["client_address_hash"] is None


def test_non_http_scope_is_not_logged(monkeypatch, audit_app):
    middleware, path = enable(monkeypatch, audit_app)
    with TestClient(middleware):
        pass
    assert not path.exists()


def test_main_registers_audit_middleware():
    from backend.main import app

    assert any(item.cls is audit.RequestAuditMiddleware for item in app.user_middleware)
