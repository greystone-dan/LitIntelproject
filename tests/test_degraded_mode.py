"""Offline fixtures only; repository bootstrap must disable dotenv/DB probes."""

import shutil
import subprocess
from types import SimpleNamespace

import pytest
from fastapi import Depends, FastAPI, Request
from fastapi.testclient import TestClient
from sqlalchemy.exc import (
    InterfaceError,
    OperationalError,
    ProgrammingError,
    TimeoutError,
)

from backend.audit import RequestAuditMiddleware
from backend.degraded_mode import (
    DATABASE_UNAVAILABLE_MESSAGE,
    database_exception_handler,
    is_database_connection_error,
    panel_helpers_script,
    register_degraded_mode,
)


def driver_error(message="private-host.invalid: connection refused", state=None):
    error = Exception(message)
    error.pgcode = state
    return error


def db_error(message="private-host.invalid: connection refused", state=None, kind=OperationalError):
    return kind("SELECT private_value", {"password": "private-password"}, driver_error(message, state))


@pytest.mark.parametrize("kind", [OperationalError, InterfaceError])
@pytest.mark.parametrize(
    "message,state",
    [
        ("connection failure", "08000"),
        ("cannot connect", "08001"),
        ("connection does not exist", "08003"),
        ("connection lost", "08006"),
        ("protocol failure", "08P01"),
        ("admin shutdown", "57P01"),
        ("crash shutdown", "57P02"),
        ("database is starting up", "57P03"),
        ("connection refused", None),
        ("Network is unreachable", None),
        ("No route to host", None),
        ('could not translate host name "private-host.invalid" to address', None),
        ("Temporary failure in name resolution", None),
        ("Name or service not known", None),
        ("getaddrinfo failed", None),
        ("server closed the connection unexpectedly", None),
        ("connection already closed", None),
        ("connection reset by peer", None),
        ("SSL connection has been closed unexpectedly", None),
        ("connection not open", None),
        ("connection was closed in the middle of operation", None),
        ("could not resolve hostname", None),
        ("terminating connection due to administrator command", None),
        ("the database system is shutting down", None),
    ],
)
def test_classifies_only_driver_connectivity_messages_and_states(kind, message, state):
    assert is_database_connection_error(db_error(message, state, kind))


@pytest.mark.parametrize(
    "error",
    [
        TimeoutError("QueuePool limit reached, connection timed out"),
        ProgrammingError(None, None, driver_error("connection refused", "08006")),
        RuntimeError("connection refused"),
        db_error("connection timeout", "08001"),
        db_error("connection timed out", "08006"),
        db_error("timeout expired"),
        db_error("connect_timeout expired"),
        db_error("canceling statement due to statement timeout", "57014"),
        db_error("statement timeout", "08006"),
        db_error("query timed out"),
        db_error("canceling query", "08006"),
        db_error("deadlock detected", "40P01"),
        db_error("could not obtain lock", "55P03"),
        db_error("disk full", "53100"),
        db_error("password authentication failed", "28P01"),
        db_error("connection refused in application text", "23505"),
        db_error("unrelated operational failure"),
        db_error("could not connect to server"),  # Insufficient evidence by itself.
        db_error("connection refused in statement parameters"),
    ],
)
def test_rejects_timeouts_programming_and_unrelated_errors(error):
    assert not is_database_connection_error(error)


def test_classifier_uses_driver_sqlstate_and_diag_without_wrapper_sql():
    for attribute in ("sqlstate", "diag"):
        original = driver_error("connection lost")
        setattr(original, attribute, "08006" if attribute == "sqlstate" else SimpleNamespace(sqlstate="08006"))
        assert is_database_connection_error(OperationalError(None, None, original))
    error = OperationalError("connection refused", {"connection": "refused"}, Exception("disk full"))
    assert not is_database_connection_error(error)


def fixture_app(monkeypatch, error, request_id=None):
    """A session-dependent endpoint with a replaced factory, never a real engine."""
    monkeypatch.delenv("CASELIBRARY_AUDIT_LOG", raising=False)
    application = FastAPI()
    register_degraded_mode(application)
    application.add_middleware(RequestAuditMiddleware)
    factory = SimpleNamespace(session=lambda: None)

    class FailedSession:
        def execute(self, _statement):
            raise error

    monkeypatch.setattr(factory, "session", FailedSession)

    def get_session():
        yield factory.session()

    session_dependency = Depends(get_session)

    def endpoint(request: Request, session=session_dependency):
        if request_id is not None:
            request.state.request_id = request_id
        session.execute("SELECT 1")
        return {"ok": True}

    for path in ("/", "/data-explorer", "/api", "/api/panel", "/apiary"):
        application.add_api_route(path, endpoint)
    return application


@pytest.mark.parametrize("path", ["/", "/data-explorer", "/apiary"])
def test_html_outage_is_safe_with_navigation_and_escaped_request_id(monkeypatch, path):
    application = fixture_app(monkeypatch, db_error(), '<script>"&</script>')
    response = TestClient(application).get(path, headers={"accept": "text/html"})
    assert response.status_code == 503
    assert response.headers["content-type"].startswith("text/html")
    assert DATABASE_UNAVAILABLE_MESSAGE in response.text
    assert '<a href="/">Home</a>' in response.text
    assert '<a href="/data-explorer">Search</a>' in response.text
    assert "&lt;script&gt;&quot;&amp;&lt;/script&gt;" in response.text
    assert "<script>" not in response.text
    for private in ("private-host", "private-password", "private_value", "OperationalError"):
        assert private not in response.text


@pytest.mark.parametrize(
    "path,accept",
    [
        ("/api", "text/html"),
        ("/api/panel", "text/html"),
        ("/api/panel", "application/json"),
        ("/data-explorer", "application/json"),
        ("/data-explorer", "*/*"),
        ("/data-explorer", "text/html;q=0,application/json"),
        ("/data-explorer", "text/html;q=invalid"),
        ("/data-explorer", ""),
    ],
)
def test_json_outage_is_safe_and_has_generated_id_without_audit_log(monkeypatch, path, accept):
    response = TestClient(fixture_app(monkeypatch, db_error())).get(
        path, headers={"accept": accept}
    )
    assert response.status_code == 503
    assert response.headers["content-type"].startswith("application/json")
    document = response.json()
    assert document["detail"] == document["message"] == DATABASE_UNAVAILABLE_MESSAGE
    assert len(document["request_id"]) == 32
    int(document["request_id"], 16)
    assert "private" not in response.text


def test_request_id_is_optional_without_audit_middleware():
    application = FastAPI()
    register_degraded_mode(application)

    @application.get("/")
    def endpoint():
        raise db_error()

    client = TestClient(application)
    assert "request_id" not in client.get("/").json()
    assert "Request ID" not in client.get("/", headers={"accept": "text/html"}).text


@pytest.mark.parametrize(
    "error",
    [
        db_error("unrelated operational failure"),
        db_error("connect timeout expired", "08001"),
        db_error("statement timeout", "57014"),
        InterfaceError(None, None, driver_error("invalid cursor")),
        ProgrammingError(None, None, driver_error("bad SQL")),
        TimeoutError("pool timeout"),
        RuntimeError("unexpected bug"),
    ],
)
def test_starlette_preserves_rejected_original_exception(monkeypatch, error):
    application = fixture_app(monkeypatch, error)
    with pytest.raises(type(error)) as raised:
        TestClient(application).get("/data-explorer", headers={"accept": "text/html"})
    assert raised.value is error
    response = TestClient(application, raise_server_exceptions=False).get("/")
    assert response.status_code == 500
    assert DATABASE_UNAVAILABLE_MESSAGE not in response.text


@pytest.mark.parametrize("down", [False, True])
def test_main_registration_and_mocked_readiness_probe_status(monkeypatch, down):
    # Safe repository bootstrap is required before this application import.
    from backend import health
    from backend.main import app

    monkeypatch.delenv("CASELIBRARY_ACCESS_PASSWORD", raising=False)
    monkeypatch.delenv("CASELIBRARY_AUDIT_LOG", raising=False)
    monkeypatch.setattr(
        health,
        "_database_probe",
        lambda: {
            "database": {"status": "error" if down else "ok"},
            "vector_extension": {"status": "not_checked" if down else "ok"},
            "required_tables": {"status": "not_checked" if down else "ok", "missing": []},
        },
    )
    monkeypatch.setattr(
        health, "_model_endpoint_probe", lambda: {"status": "ok", "checks": {}}
    )
    assert app.exception_handlers[OperationalError] is database_exception_handler
    assert app.exception_handlers[InterfaceError] is database_exception_handler
    # No context manager: do not execute the database-initializing lifespan.
    response = TestClient(app).get("/health/ready")
    assert response.status_code == (503 if down else 200)
    assert response.json()["checks"]["database"]["status"] == ("error" if down else "ok")


def test_inline_helper_is_valid_and_recovers_with_same_renderer():
    node = shutil.which("node")
    if not node:
        pytest.skip("Node.js is unavailable")
    script = panel_helpers_script().removeprefix("<script>").removesuffix("</script>")
    harness = r"""
const assert = require('node:assert/strict');
class Element {
    constructor(tag) { this.tagName = tag; this.children = []; this.attributes = {};
        this.listeners = {}; this.disabled = false; this.parent = null; this.textContent = ''; }
    setAttribute(key, value) { this.attributes[key] = value; }
    replaceChildren(...items) {
        this.children.forEach(item => item.parent = null);
        this.children = []; this.append(...items);
    }
    append(...items) { for (const item of items) { item.parent = this; this.children.push(item); } }
    prepend(item) { item.parent = this; this.children.unshift(item); }
    contains(item) { return this.children.some(child => child === item || child.contains(item)); }
    remove() { if (this.parent) this.parent.children = this.parent.children.filter(x => x !== this); }
    addEventListener(name, listener) { this.listeners[name] = listener; }
    click() { if (!this.disabled && this.listeners.click) this.listeners.click(); }
}
global.document = {createElement: tag => new Element(tag)};
const tick = () => new Promise(resolve => setImmediate(resolve));
"""
    checks = r"""
(async () => {
    const panel = new Element('section'), neighbor = new Element('section');
    neighbor.textContent = 'Untouched';
    let calls = 0, renders = 0, cleanup = 0, resolveFetch;
    const request = {headers: {'X-Test': 'fixture'}};
    global.fetch = (url, opts) => {
        calls++; assert.equal(url, '/panel'); assert.equal(opts, request);
        return new Promise(resolve => { resolveFetch = resolve; });
    };
    const options = {request, render: data => {
        renders++; panel.replaceChildren(); panel.textContent = data.value;
    }, onError: () => { cleanup++; panel.replaceChildren(); throw Error('private exception'); }};
    const first = fetchPanel('/panel', panel, options);
    assert.equal(fetchPanel('/panel', panel, options), first);
    assert.equal(panel.children[0].attributes['aria-live'], 'polite');
    await tick(); assert.equal(calls, 1);
    resolveFetch({ok: false, json: () => { throw Error('must not parse failed status'); }});
    assert.equal(await first, null); assert.equal(cleanup, 1);
    assert.equal(renders, 0); assert.equal(neighbor.textContent, 'Untouched');
    let failure = panel.children[0];
    assert.equal(failure.children[0].textContent, 'This section could not load.');
    const retry = failure.children[1];
    assert.equal(retry.tagName, 'button'); assert.equal(retry.textContent, 'Retry');
    retry.click(); retry.click(); assert.equal(retry.disabled, true);
    await tick(); assert.equal(calls, 2); assert(panel.contains(retry));
    resolveFetch({ok: true, json: async () => ({value: 'Recovered'})});
    await tick(); assert.equal(renders, 1); assert.equal(panel.textContent, 'Recovered');
    assert.equal(neighbor.textContent, 'Untouched');
    global.fetch = async () => ({ok: true, json: async () => { throw Error('private JSON'); }});
    assert.equal(await fetchPanel('/panel', panel, options), null);
    assert.equal(panel.children[0].children[0].textContent, 'This section could not load.');
    global.fetch = async () => { throw Error('private network'); };
    assert.equal(await fetchPanel('/panel', panel, options), null);
    let current = true;
    global.fetch = () => new Promise(resolve => { resolveFetch = resolve; });
    const stale = fetchPanel('/panel', panel, {...options, isCurrent: () => current});
    await tick(); current = false;
    panel.replaceChildren(); panel.textContent = 'New selection';
    resolveFetch({ok: true, json: async () => ({value: 'Stale'})});
    assert.equal(await stale, null); assert.equal(panel.textContent, 'New selection');
    assert.equal(renders, 1);
    current = true;
    const staleFailure = fetchPanel('/panel', panel, {...options, isCurrent: () => current});
    await tick(); current = false;
    panel.replaceChildren(); panel.textContent = 'Newer selection';
    resolveFetch({ok: false});
    assert.equal(await staleFailure, null); assert.equal(panel.textContent, 'Newer selection');
    assert.equal(cleanup, 3);
    assert.equal(await fetchPanel('/panel', panel, {isCurrent: () => false}), null);
    assert.equal(await fetchPanel('/panel', null), null);
})().catch(error => { console.error(error); process.exitCode = 1; });
"""
    completed = subprocess.run(
        [node, "-e", harness + script + checks],
        capture_output=True,
        text=True,
        timeout=15,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
