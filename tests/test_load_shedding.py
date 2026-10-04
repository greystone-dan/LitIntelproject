import ast
import asyncio
import inspect
import textwrap
from types import SimpleNamespace

import httpx
from fastapi import FastAPI
from fastapi.params import File as FileParam
from fastapi.params import Form as FormParam
from fastapi.testclient import TestClient
from pydantic import BaseModel

from backend.load_shedding import (
    BUSY_MESSAGE,
    HeavyEndpointMiddleware,
    LoadSheddingState,
    classify_route,
    register,
)


def _disable_limits(monkeypatch) -> None:
    for name in (
        "HEAVY_ENDPOINT_MAX_CONCURRENCY",
        "HEAVY_ENDPOINT_QUEUE_SECONDS",
        "HEAVY_BUCKET_LIVE_ANALYSIS_MAX",
        "HEAVY_BUCKET_EXPORTS_MAX",
        "HEAVY_BUCKET_CITATION_MAP_MAX",
        "HEAVY_BUCKET_ANALYTICS_MAX",
        "HEAVY_BUCKET_BULK_SEARCH_MAX",
    ):
        monkeypatch.delenv(name, raising=False)


def test_full_bucket_returns_503_then_recovers_and_health_stays_available(monkeypatch):
    monkeypatch.setenv("HEAVY_ENDPOINT_MAX_CONCURRENCY", "1")
    monkeypatch.setenv("HEAVY_ENDPOINT_QUEUE_SECONDS", "0")
    started = asyncio.Event()
    release = asyncio.Event()
    app = FastAPI()

    @app.post("/live-analysis/analyze")
    async def analyze():
        started.set()
        await release.wait()
        return {"ok": True}

    @app.get("/health")
    async def health():
        return {"ok": True}

    @app.get("/search")
    async def search():
        return {"ok": True}

    limited_app = HeavyEndpointMiddleware(app, state=LoadSheddingState())

    async def exercise():
        transport = httpx.ASGITransport(app=limited_app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            first_request = asyncio.create_task(
                client.post("/live-analysis/analyze")
            )
            await asyncio.wait_for(started.wait(), timeout=2)

            second_response = await client.post("/live-analysis/analyze")
            assert second_response.status_code == 503
            assert second_response.headers["retry-after"] == "1"
            assert second_response.text == BUSY_MESSAGE
            assert second_response.headers["content-type"].startswith("text/plain")
            assert (await client.get("/health")).status_code == 200
            assert (await client.get("/search")).status_code == 200

            release.set()
            assert (await first_request).status_code == 200
            assert (await client.post("/live-analysis/analyze")).status_code == 200

    asyncio.run(exercise())


def test_default_configuration_does_not_limit_requests(monkeypatch):
    _disable_limits(monkeypatch)
    started = asyncio.Event()
    release = asyncio.Event()
    request_count = 0
    app = FastAPI()

    @app.post("/live-analysis/analyze")
    async def analyze():
        nonlocal request_count
        request_count += 1
        if request_count == 1:
            started.set()
            await release.wait()
        return {"ok": True}

    limited_app = HeavyEndpointMiddleware(app, state=LoadSheddingState())

    async def exercise():
        transport = httpx.ASGITransport(app=limited_app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            first_request = asyncio.create_task(
                client.post("/live-analysis/analyze")
            )
            await asyncio.wait_for(started.wait(), timeout=2)
            assert (await client.post("/live-analysis/analyze")).status_code == 200
            release.set()
            assert (await first_request).status_code == 200

    asyncio.run(exercise())


def test_bucket_override_applies_only_when_the_global_limit_is_enabled(monkeypatch):
    _disable_limits(monkeypatch)
    monkeypatch.setenv("HEAVY_BUCKET_ANALYTICS_MAX", "1")
    assert not LoadSheddingState().enabled

    monkeypatch.setenv("HEAVY_ENDPOINT_MAX_CONCURRENCY", "3")
    state = LoadSheddingState()
    assert state.buckets["analytics"].maximum == 1
    assert state.buckets["live_analysis"].maximum == 3


def test_debug_limits_endpoint_is_hidden_unless_enabled(monkeypatch):
    _disable_limits(monkeypatch)
    app = FastAPI()
    register(app)

    with TestClient(app) as client:
        assert client.get("/health/limits").status_code == 404
        monkeypatch.setenv("CASELIBRARY_DEBUG_ENDPOINTS", "1")
        response = client.get("/health/limits")

    assert response.status_code == 200
    assert response.json()["enabled"] is False
    assert set(response.json()["buckets"]) == {
        "live_analysis",
        "exports",
        "citation_map",
        "analytics",
        "bulk_search",
    }


def _has_free_text_body(route) -> bool:
    text_names = {
        "text",
        "query",
        "q",
        "search",
        "content",
        "memo",
        "document",
        "summary",
        "prompt",
        "message",
        "body",
        "html",
    }

    def is_text_field(name, annotation) -> bool:
        parts = set(name.lower().split("_"))
        return "str" in str(annotation) and bool(parts & text_names)

    for parameter in route.dependant.body_params:
        if isinstance(parameter.field_info, FileParam):
            return True
        if is_text_field(parameter.name, getattr(parameter, "type_", None)):
            return True
        annotation = getattr(parameter, "type_", None)
        if isinstance(annotation, type) and issubclass(annotation, BaseModel):
            fields = getattr(annotation, "model_fields", None) or getattr(
                annotation, "__fields__", {}
            )
            for name, model_field in fields.items():
                field_annotation = getattr(model_field, "annotation", None) or getattr(
                    model_field, "outer_type_", None
                )
                if is_text_field(name, field_annotation):
                    return True
        if isinstance(parameter.field_info, FormParam) and is_text_field(
            parameter.name, getattr(parameter, "type_", None)
        ):
            return True
    return False


def _reads_raw_request_body(route) -> bool:
    try:
        tree = ast.parse(textwrap.dedent(inspect.getsource(route.endpoint)))
    except (OSError, TypeError, IndentationError, SyntaxError):
        return False
    body_methods = {"body", "form", "json", "stream"}
    return any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in body_methods
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "request"
        for node in ast.walk(tree)
    )


def test_route_guard_detects_raw_streamed_request_bodies():
    async def raw_body_route(request):
        async for _chunk in request.stream():
            pass

    assert _reads_raw_request_body(SimpleNamespace(endpoint=raw_body_route))


def _has_free_text_query(route) -> bool:
    text_names = {"text", "query", "q", "search", "content", "memo", "document"}
    return any(
        set(parameter.name.lower().split("_")) & text_names
        and "str" in str(getattr(parameter, "type_", None))
        for parameter in route.dependant.query_params
    )


def test_main_exposes_debug_limits_endpoint(monkeypatch):
    _disable_limits(monkeypatch)
    monkeypatch.delenv("CASELIBRARY_ACCESS_PASSWORD", raising=False)
    monkeypatch.setenv("CASELIBRARY_DEBUG_ENDPOINTS", "1")
    from backend.main import app

    response = TestClient(app).get("/health/limits")
    assert response.status_code == 200
    assert set(response.json()) == {"enabled", "queue_seconds", "buckets"}


def test_upload_and_free_text_routes_are_classified():
    from backend.main import app

    for route in app.routes:
        if not hasattr(route, "dependant"):
            continue
        if not (
            _has_free_text_body(route)
            or _has_free_text_query(route)
            or _reads_raw_request_body(route)
        ):
            continue
        for method in route.methods or ():
            classified, _bucket = classify_route(route.path, method)
            assert classified, f"Unclassified free-text/upload route: {method} {route.path}"


def test_unlisted_and_light_routes_remain_unlimited():
    assert classify_route("/health/ready", "GET") == (False, None)
    assert classify_route("/static/app.css", "GET") == (False, None)
    assert classify_route("/search", "POST") == (True, None)
    assert classify_route("/prototype/cases", "GET") == (True, None)
    assert classify_route("/precedent-finder", "POST") == (True, "bulk_search")
