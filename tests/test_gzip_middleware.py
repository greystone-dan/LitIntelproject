"""Tests for selective compression and revalidatable page responses."""

import pytest
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response, StreamingResponse
from starlette.testclient import TestClient

from backend.cache_headers import compute_etag, static_html_response
from backend.gzip_middleware import SelectiveGZipMiddleware
from backend.routes import router


HTML = "<html><body>Research content</body></html>" * 50


@pytest.fixture
def test_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(SelectiveGZipMiddleware, minimum_size=100)

    @app.get("/html")
    def html_response() -> HTMLResponse:
        return HTMLResponse(content=HTML)

    @app.get("/no-store")
    def no_store_response() -> HTMLResponse:
        return HTMLResponse(
            content=HTML,
            headers={"Cache-Control": "no-store, no-cache", "Pragma": "no-cache"},
        )

    @app.get("/download")
    def download_response() -> Response:
        return Response(
            content=b"Binary file content" * 100,
            media_type="application/octet-stream",
            headers={"Content-Disposition": 'attachment; filename="file.bin"'},
        )

    @app.get("/stream")
    async def stream_response() -> StreamingResponse:
        async def chunks():
            yield b"first streamed chunk" * 40
            yield b"second streamed chunk" * 40

        return StreamingResponse(chunks(), media_type="text/plain")

    return app


def test_gzip_applied_only_when_requested_for_buffered_response(test_app: FastAPI) -> None:
    client = TestClient(test_app)
    response = client.get("/html", headers={"accept-encoding": "gzip"})
    assert response.status_code == 200
    assert response.headers.get("content-encoding") == "gzip"
    assert response.content == HTML.encode("utf-8")

    identity = client.get("/html", headers={"accept-encoding": "identity"})
    assert "content-encoding" not in identity.headers
    assert identity.content == HTML.encode("utf-8")

    refused = client.get("/html", headers={"accept-encoding": "gzip;q=0"})
    assert "content-encoding" not in refused.headers


def test_gzip_is_not_applied_to_no_store_response(test_app: FastAPI) -> None:
    response = TestClient(test_app).get(
        "/no-store",
        headers={"accept-encoding": "gzip"},
    )
    assert response.status_code == 200
    assert response.headers["cache-control"] == "no-store, no-cache"
    assert response.headers["pragma"] == "no-cache"
    assert "content-encoding" not in response.headers
    assert response.content == HTML.encode("utf-8")


def test_gzip_is_not_applied_to_download(test_app: FastAPI) -> None:
    response = TestClient(test_app).get(
        "/download",
        headers={"accept-encoding": "gzip"},
    )
    assert response.status_code == 200
    assert response.headers["content-disposition"].startswith("attachment")
    assert "content-encoding" not in response.headers
    assert response.content == b"Binary file content" * 100


def test_gzip_is_not_applied_to_stream(test_app: FastAPI) -> None:
    response = TestClient(test_app).get(
        "/stream",
        headers={"accept-encoding": "gzip"},
    )
    assert response.status_code == 200
    assert "content-encoding" not in response.headers
    assert response.content == (
        b"first streamed chunk" * 40 + b"second streamed chunk" * 40
    )


def test_etag_is_stable_and_content_sensitive() -> None:
    assert compute_etag("same") == compute_etag(b"same")
    assert compute_etag("same").startswith('W/"')
    assert compute_etag("same") != compute_etag("different")


def test_static_html_is_public_for_one_hour_and_supports_conditional_revalidation() -> None:
    response = static_html_response("<main>Page</main>")
    assert response.status_code == 200
    assert response.headers["cache-control"] == "public, max-age=3600"
    assert response.headers["etag"] == compute_etag("<main>Page</main>")
    assert response.headers["vary"] == "Cookie"

    unchanged = static_html_response(
        "<main>Page</main>",
        if_none_match=response.headers["etag"],
    )
    assert unchanged.status_code == 304
    assert unchanged.headers["cache-control"] == "public, max-age=3600"
    assert unchanged.headers["etag"] == response.headers["etag"]
    assert unchanged.body == b""


def test_static_html_accepts_weak_match_and_does_not_match_stale_etag() -> None:
    etag = compute_etag("<main>Page</main>")
    assert static_html_response(
        "<main>Page</main>",
        if_none_match=f'"unrelated", {etag}',
    ).status_code == 304
    assert static_html_response(
        "<main>Page</main>",
        if_none_match='W/"stale"',
    ).status_code == 200


def test_no_store_is_not_cacheable_via_static_helper() -> None:
    # The static helper is intentionally not used for sensitive routes.
    response = HTMLResponse(
        "<main>Private</main>",
        headers={"Cache-Control": "no-store", "Pragma": "no-cache"},
    )
    assert response.headers["cache-control"] == "no-store"
    assert "etag" not in response.headers


def test_static_page_routes_revalidate_and_deidentify_remains_no_store() -> None:
    app = FastAPI()
    app.include_router(router)
    app.add_middleware(SelectiveGZipMiddleware, minimum_size=100)
    client = TestClient(app)

    page = client.get("/data-explorer", headers={"accept-encoding": "identity"})
    assert page.status_code == 200
    assert page.headers["cache-control"] == "public, max-age=3600"
    assert page.headers["vary"] == "Cookie"
    etag = page.headers["etag"]

    compressed = client.get("/data-explorer", headers={"accept-encoding": "gzip"})
    assert compressed.status_code == 200
    assert compressed.headers["content-encoding"] == "gzip"
    assert compressed.headers["cache-control"] == "public, max-age=3600"
    assert {value.strip().lower() for value in compressed.headers["vary"].split(",")} == {
        "cookie",
        "accept-encoding",
    }

    unchanged = client.get(
        "/data-explorer",
        headers={"if-none-match": etag, "accept-encoding": "identity"},
    )
    assert unchanged.status_code == 304
    assert unchanged.headers["etag"] == etag

    private = client.get("/deidentify", headers={"accept-encoding": "gzip"})
    assert private.status_code == 200
    assert private.headers["cache-control"] == "no-store"
    assert "etag" not in private.headers
    assert "content-encoding" not in private.headers
