"""Pure configuration and HTTP timeout tests: no application or database startup."""

import builtins
import sqlite3
import sys
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
import sqlalchemy
from fastapi import FastAPI, HTTPException
from fastapi.datastructures import DefaultPlaceholder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.testclient import TestClient
from sqlalchemy.exc import DBAPIError, OperationalError, SQLAlchemyError, TimeoutError

from backend import db_limits


POSTGRES_URL = "postgresql+psycopg2://localhost/test_only"
SQLITE_URLS = ("sqlite://", "sqlite:///:memory:", "sqlite:///never-opened.db")
POOL_ENV = {
    "DB_POOL_SIZE": "0",
    "DB_MAX_OVERFLOW": "-1",
    "DB_POOL_TIMEOUT_SECONDS": "0.25",
    "DB_POOL_RECYCLE_SECONDS": "-1",
}
POOL_KWARGS = {
    "pool_size": 0,
    "max_overflow": -1,
    "pool_timeout": 0.25,
    "pool_recycle": -1,
}
TIMEOUT_ENV = {
    "DB_STATEMENT_TIMEOUT_MS": "123",
    "DB_LOCK_TIMEOUT_MS": "456",
}
PRIVATE_SQL = "SELECT private_sql_marker FROM confidential_table"
PRIVATE_PARAMS = {"token": "private_parameter_marker"}
PRIVATE_DRIVER = "private_driver_marker"


@pytest.fixture(autouse=True)
def forbid_connections(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Database connections forbidden")

    monkeypatch.setattr(sqlalchemy.engine.Engine, "connect", forbidden)
    monkeypatch.setattr(sqlalchemy.engine.Engine, "raw_connection", forbidden)
    monkeypatch.setattr(sqlite3, "connect", forbidden)


@pytest.mark.parametrize("url", (POSTGRES_URL, *SQLITE_URLS))
def test_unset_values_have_no_defaults(url):
    assert db_limits.engine_kwargs(url, environ={}) == {}


@pytest.mark.parametrize(
    ("name", "value", "expected"),
    [
        ("DB_STATEMENT_TIMEOUT_MS", "0", {"connect_args": {"options": "-c statement_timeout=0"}}),
        ("DB_STATEMENT_TIMEOUT_MS", "2147483647", {"connect_args": {"options": "-c statement_timeout=2147483647"}}),
        ("DB_LOCK_TIMEOUT_MS", "0", {"connect_args": {"options": "-c lock_timeout=0"}}),
        ("DB_LOCK_TIMEOUT_MS", "2147483647", {"connect_args": {"options": "-c lock_timeout=2147483647"}}),
        ("DB_POOL_SIZE", "0", {"pool_size": 0}),
        ("DB_POOL_SIZE", "8", {"pool_size": 8}),
        ("DB_MAX_OVERFLOW", "-1", {"max_overflow": -1}),
        ("DB_MAX_OVERFLOW", "0", {"max_overflow": 0}),
        ("DB_MAX_OVERFLOW", "12", {"max_overflow": 12}),
        ("DB_POOL_TIMEOUT_SECONDS", "0", {"pool_timeout": 0.0}),
        ("DB_POOL_TIMEOUT_SECONDS", "1.25", {"pool_timeout": 1.25}),
        ("DB_POOL_RECYCLE_SECONDS", "-1", {"pool_recycle": -1}),
        ("DB_POOL_RECYCLE_SECONDS", "0", {"pool_recycle": 0}),
        ("DB_POOL_RECYCLE_SECONDS", "1800", {"pool_recycle": 1800}),
    ],
)
def test_valid_values_and_bounds(name, value, expected):
    assert db_limits.engine_kwargs(POSTGRES_URL, environ={name: value}) == expected


def test_combined_postgresql_options_and_pool_configuration():
    environ = {**TIMEOUT_ENV, **POOL_ENV}
    before = environ.copy()
    assert db_limits.engine_kwargs(POSTGRES_URL, environ=environ) == {
        **POOL_KWARGS,
        "connect_args": {"options": "-c statement_timeout=123 -c lock_timeout=456"},
    }
    assert environ == before
    assert db_limits.engine_kwargs(
        POSTGRES_URL, environ=environ, include_timeouts=False
    ) == POOL_KWARGS


@pytest.mark.parametrize("url", SQLITE_URLS)
@pytest.mark.parametrize("include_timeouts", [True, False])
def test_sqlite_filters_unsupported_kwargs_without_opening_database(url, include_timeouts):
    assert db_limits.engine_kwargs(
        url,
        environ={**TIMEOUT_ENV, **POOL_ENV},
        include_timeouts=include_timeouts,
    ) == {"pool_recycle": -1}


INVALID_VALUES = [
    (name, value)
    for name in ("DB_STATEMENT_TIMEOUT_MS", "DB_LOCK_TIMEOUT_MS")
    for value in ("-1", "2147483648", "1.5", "", "not-an-integer", "NaN", "inf")
] + [
    (name, value)
    for name in ("DB_POOL_SIZE", "DB_MAX_OVERFLOW", "DB_POOL_RECYCLE_SECONDS")
    for value in ("1.5", "", "not-an-integer", "NaN", "-inf")
] + [
    ("DB_POOL_SIZE", "-1"),
    ("DB_MAX_OVERFLOW", "-2"),
    ("DB_POOL_RECYCLE_SECONDS", "-2"),
] + [
    ("DB_POOL_TIMEOUT_SECONDS", value)
    for value in ("-0.1", "nan", "NaN", "inf", "-inf", "1e309", "", "invalid")
]


@pytest.mark.parametrize(("name", "value"), INVALID_VALUES)
@pytest.mark.parametrize("url", (POSTGRES_URL, *SQLITE_URLS))
@pytest.mark.parametrize("include_timeouts", [True, False])
def test_invalid_values_are_validated_even_when_ignored(name, value, url, include_timeouts):
    with pytest.raises(ValueError, match=name):
        db_limits.engine_kwargs(
            url, environ={name: value}, include_timeouts=include_timeouts
        )


def test_explicit_environ_does_not_inherit_process_values(monkeypatch):
    monkeypatch.setenv("DB_POOL_SIZE", "invalid")
    monkeypatch.setenv("DB_STATEMENT_TIMEOUT_MS", "invalid")
    assert db_limits.engine_kwargs(POSTGRES_URL, environ={}) == {}


def test_default_environ_reads_process_values(monkeypatch):
    for name in (*TIMEOUT_ENV, *POOL_ENV):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("DB_POOL_SIZE", "4")
    monkeypatch.setenv("DB_LOCK_TIMEOUT_MS", "9")
    assert db_limits.engine_kwargs(POSTGRES_URL) == {
        "pool_size": 4,
        "connect_args": {"options": "-c lock_timeout=9"},
    }


@pytest.mark.parametrize("url", (POSTGRES_URL, *SQLITE_URLS))
def test_engine_without_timeout_uses_mock_and_never_imports_database(monkeypatch, url):
    sentinel = object()
    create = Mock(return_value=sentinel)
    monkeypatch.setattr(sqlalchemy, "create_engine", create)
    # Accommodate either a module-level import or a lazy SQLAlchemy import.
    monkeypatch.setattr(db_limits, "create_engine", create, raising=False)
    original_import = builtins.__import__

    def guarded_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name == "backend.database" or (
            name == "backend" and "database" in (fromlist or ())
        ) or (level and name == "database"):
            raise AssertionError("Explicit URL must not import backend.database")
        return original_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, "__import__", guarded_import)
    assert db_limits.engine_without_timeout(
        url, environ={**TIMEOUT_ENV, **POOL_ENV}
    ) is sentinel
    expected = POOL_KWARGS if url == POSTGRES_URL else {"pool_recycle": -1}
    create.assert_called_once_with(url, pool_pre_ping=True, **expected)


def test_engine_without_timeout_does_not_add_pool_defaults(monkeypatch):
    create = Mock()
    monkeypatch.setattr(sqlalchemy, "create_engine", create)
    monkeypatch.setattr(db_limits, "create_engine", create, raising=False)
    db_limits.engine_without_timeout(POSTGRES_URL, environ={})
    create.assert_called_once_with(POSTGRES_URL, pool_pre_ping=True)


def test_engine_without_timeout_lazily_uses_configured_url(monkeypatch):
    create = Mock()
    monkeypatch.setattr(db_limits, "create_engine", create)
    monkeypatch.setitem(
        sys.modules, "backend.database", SimpleNamespace(DATABASE_URL=POSTGRES_URL)
    )
    db_limits.engine_without_timeout(environ={**TIMEOUT_ENV, **POOL_ENV})
    create.assert_called_once_with(POSTGRES_URL, pool_pre_ping=True, **POOL_KWARGS)


def operational_error(code, primary, *, code_attribute="pgcode"):
    original = RuntimeError(PRIVATE_DRIVER)
    setattr(original, code_attribute, code)
    original.diag = SimpleNamespace(message_primary=primary)
    return OperationalError(PRIVATE_SQL, PRIVATE_PARAMS, original)


def timeout_error(kind, code_attribute="pgcode"):
    if kind == "pool":
        return TimeoutError(
            "QueuePool limit of size 5 overflow 10 reached, "
            "connection timed out, timeout 30.00 " + PRIVATE_DRIVER
        )
    code, primary = {
        "statement": ("57014", "canceling statement due to statement timeout"),
        "lock": ("55P03", "canceling statement due to lock timeout"),
    }[kind]
    return operational_error(code, primary, code_attribute=code_attribute)


def make_app(error, *, path="/cases", response_class=None, fallback=None):
    app = FastAPI()
    if fallback:
        error_type, handler = fallback
        app.add_exception_handler(error_type, handler)

    async def simulated_endpoint():
        raise error

    options = {} if response_class is None else {"response_class": response_class}
    app.add_api_route(path, simulated_endpoint, methods=["GET"], **options)
    db_limits.register_timeout_handlers(app)
    return app


def request(app, path="/cases", accept="application/json"):
    # Deliberately no context manager: TestClient must not run lifespan hooks.
    client = TestClient(app)
    try:
        return client.get(path, headers={"Accept": accept})
    finally:
        client.close()


@pytest.mark.parametrize("kind", ["statement", "lock", "pool"])
@pytest.mark.parametrize(
    ("path", "response_class", "accept", "html"),
    [
        ("/api/cases", HTMLResponse, "text/html", False),
        ("/api", HTMLResponse, "text/html", False),
        ("/cases", None, "text/html", False),
        ("/cases", JSONResponse, "text/html", False),
        ("/cases", DefaultPlaceholder(JSONResponse), "text/html", False),
        ("/cases", HTMLResponse, "text/html", True),
        ("/cases", HTMLResponse, "application/json", False),
        ("/cases", HTMLResponse, "*/*", False),
    ],
)
def test_timeout_response_negotiation_and_no_information_leak(
    kind, path, response_class, accept, html
):
    response = request(
        make_app(timeout_error(kind), path=path, response_class=response_class),
        path,
        accept,
    )
    assert response.status_code == 503
    assert response.headers["retry-after"] == "5"
    for private in (PRIVATE_SQL, "confidential_table", "token", *PRIVATE_PARAMS.values(), PRIVATE_DRIVER):
        assert private not in response.text
    if html:
        assert response.headers["content-type"].startswith("text/html")
        assert "<" in response.text
    else:
        assert response.headers["content-type"].startswith("application/json")
        payload = response.json()
        assert set(payload) == {"detail"}
        assert isinstance(payload["detail"], str) and payload["detail"]


@pytest.mark.parametrize("kind", ["statement", "lock"])
def test_sqlstate_supported_without_pgcode(kind):
    response = request(make_app(timeout_error(kind, "sqlstate")))
    assert response.status_code == 503
    assert response.headers["retry-after"] == "5"


UNRECOGNIZED = [
    operational_error("57014", "canceling statement due to user request"),
    operational_error("57014", "canceling statement due to statement timeout extra"),
    operational_error("57014", "canceling statement due to statement timeout "),
    operational_error("57014", "Canceling statement due to statement timeout"),
    operational_error("57014", "canceling statement due to lock timeout"),
    operational_error("55P03", "canceling statement due to statement timeout"),
    operational_error("55P03", "could not obtain lock on relation"),
    operational_error("08006", "canceling statement due to statement timeout"),
    operational_error(None, "canceling statement due to statement timeout"),
    operational_error("57014", None),
    OperationalError(PRIVATE_SQL, PRIVATE_PARAMS, RuntimeError(
        "canceling statement due to statement timeout"
    )),
    TimeoutError("unrelated timeout " + PRIVATE_DRIVER),
    TimeoutError("QueuePool limit of size 5 overflow 10 reached"),
    TimeoutError("connection timed out, timeout 30.00"),
    TimeoutError("prefix QueuePool limit of size 5 connection timed out, timeout 30"),
]


@pytest.mark.parametrize("error", UNRECOGNIZED)
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("handler_scope", ["precise", "dbapi", "sqlalchemy", "exception"])
def test_unrecognized_errors_preserve_existing_sync_async_and_superclass_handlers(
    error, asynchronous, handler_scope
):
    calls = []

    def sync_handler(req, exc):
        calls.append(exc)
        return JSONResponse({"detail": "existing-handler"}, status_code=409)

    async def async_handler(req, exc):
        return sync_handler(req, exc)

    error_type = {
        "precise": type(error),
        "dbapi": DBAPIError if isinstance(error, DBAPIError) else SQLAlchemyError,
        "sqlalchemy": SQLAlchemyError,
        "exception": Exception,
    }[handler_scope]
    response = request(make_app(
        error, fallback=(error_type, async_handler if asynchronous else sync_handler)
    ))
    assert response.status_code == 409
    assert response.json() == {"detail": "existing-handler"}
    assert "retry-after" not in response.headers
    assert calls == [error]


@pytest.mark.parametrize("error", UNRECOGNIZED)
def test_unrecognized_errors_without_handler_are_reraised(error):
    with pytest.raises(type(error)) as caught:
        request(make_app(error))
    assert caught.value is error


@pytest.mark.parametrize("error", [UNRECOGNIZED[0], TimeoutError("ordinary timeout")])
def test_most_specific_existing_handler_wins_over_superclass(error):
    app = FastAPI()
    calls = []

    def broad_handler(req, exc):
        pytest.fail("A more specific existing handler is applicable")

    async def specific_handler(req, exc):
        calls.append(exc)
        return JSONResponse({"detail": "specific"}, status_code=409)

    app.add_exception_handler(SQLAlchemyError, broad_handler)
    app.add_exception_handler(type(error), specific_handler)

    async def simulated_endpoint():
        raise error

    app.add_api_route("/cases", simulated_endpoint)
    db_limits.register_timeout_handlers(app)
    response = request(app)
    assert response.status_code == 409
    assert response.json() == {"detail": "specific"}
    assert calls == [error]


@pytest.mark.parametrize("kind", ["statement", "lock", "pool"])
def test_recognized_timeout_takes_priority_over_existing_handler(kind):
    def existing(req, exc):
        pytest.fail("Recognized timeouts must not invoke the old handler")

    error = timeout_error(kind)
    response = request(make_app(error, fallback=(type(error), existing)))
    assert response.status_code == 503


def test_unrelated_http_exception_keeps_fastapi_default_handler():
    response = request(make_app(HTTPException(status_code=418, detail="ordinary-error")))
    assert response.status_code == 418
    assert response.json() == {"detail": "ordinary-error"}
    assert "retry-after" not in response.headers


def test_client_requests_do_not_start_application_lifespan():
    app = make_app(timeout_error("pool"))

    @app.on_event("startup")
    async def forbidden_startup():
        pytest.fail("Tests must not run application startup")

    assert request(app).status_code == 503
