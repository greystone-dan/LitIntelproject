import importlib

from fastapi import FastAPI
from fastapi.responses import Response, StreamingResponse
from fastapi.testclient import TestClient

from backend import main
from backend.security_headers import SecurityHeadersMiddleware


def _client(monkeypatch, *, enabled: bool, https: bool = False):
    if enabled:
        monkeypatch.setenv("CASELIBRARY_SECURITY_HEADERS", "1")
    else:
        monkeypatch.delenv("CASELIBRARY_SECURITY_HEADERS", raising=False)
    monkeypatch.delenv("CASELIBRARY_CSP_ENFORCE", raising=False)
    monkeypatch.delenv("CASELIBRARY_HSTS_SUBDOMAINS", raising=False)
    monkeypatch.delenv("CASELIBRARY_HSTS_MAX_AGE", raising=False)

    app = FastAPI()
    app.add_middleware(SecurityHeadersMiddleware)

    @app.get("/")
    def root():
        return Response("ok", media_type="text/plain")

    return TestClient(app, base_url=("https://testserver" if https else "http://testserver"))


def test_security_headers_default_passthrough(monkeypatch):
    client = _client(monkeypatch, enabled=False)

    response = client.get("/")

    assert response.status_code == 200
    assert response.text == "ok"
    assert "x-content-type-options" not in response.headers
    assert "strict-transport-security" not in response.headers


def test_security_headers_all_enabled_expected_headers(monkeypatch):
    monkeypatch.setenv("CASELIBRARY_SECURITY_HEADERS", "1")
    monkeypatch.setenv("CASELIBRARY_HSTS_MAX_AGE", "123")
    monkeypatch.setenv("CASELIBRARY_HSTS_SUBDOMAINS", "1")

    app = FastAPI()
    app.add_middleware(SecurityHeadersMiddleware)

    @app.get("/")
    def root():
        return Response("ok", media_type="text/plain")

    client = TestClient(app, base_url="https://testserver")
    response = client.get("/")

    assert response.headers["x-content-type-options"] == "nosniff"
    assert response.headers["referrer-policy"] == "strict-origin-when-cross-origin"
    assert response.headers["x-frame-options"] == "SAMEORIGIN"
    assert response.headers["permissions-policy"] == "camera=(), microphone=(), geolocation=()"
    assert response.headers["strict-transport-security"] == "max-age=123; includeSubDomains"
    assert response.headers["content-security-policy-report-only"] == (
        "default-src 'self'; base-uri 'self'; form-action 'self'; object-src 'none'; "
        "frame-ancestors 'self'; img-src 'self' data:; font-src 'self' https://fonts.gstatic.com; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "script-src 'self' 'unsafe-inline' https://unpkg.com"
    )


def test_security_headers_csp_enforce_mode(monkeypatch):
    monkeypatch.setenv("CASELIBRARY_SECURITY_HEADERS", "1")
    monkeypatch.setenv("CASELIBRARY_CSP_ENFORCE", "1")

    app = FastAPI()
    app.add_middleware(SecurityHeadersMiddleware)

    @app.get("/")
    def root():
        return Response("ok", media_type="text/plain")

    response = TestClient(app, base_url="https://testserver").get("/")

    assert response.headers["content-security-policy"] == (
        "default-src 'self'; base-uri 'self'; form-action 'self'; object-src 'none'; "
        "frame-ancestors 'self'; img-src 'self' data:; font-src 'self' https://fonts.gstatic.com; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "script-src 'self' 'unsafe-inline' https://unpkg.com"
    )
    assert "content-security-policy-report-only" not in response.headers


def test_security_headers_https_only_hsts(monkeypatch):
    client = _client(monkeypatch, enabled=True, https=False)

    response = client.get("/")

    assert "strict-transport-security" not in response.headers


def test_security_headers_forwarded_proto_enables_hsts(monkeypatch):
    client = _client(monkeypatch, enabled=True, https=False)

    response = client.get("/", headers={"x-forwarded-proto": "https"})

    assert response.headers["strict-transport-security"] == "max-age=31536000"


def test_security_headers_preserve_existing_response_headers(monkeypatch):
    monkeypatch.setenv("CASELIBRARY_SECURITY_HEADERS", "1")

    app = FastAPI()
    app.add_middleware(SecurityHeadersMiddleware)

    @app.get("/")
    def root():
        return Response(
            "ok",
            media_type="text/plain",
            headers={
                "X-Frame-Options": "DENY",
                "Content-Security-Policy-Report-Only": "default-src 'none'",
                "X-Robots-Tag": "noindex",
                "Cache-Control": "no-store",
                "Pragma": "no-cache",
            },
        )

    client = TestClient(app, base_url="https://testserver")
    response = client.get("/")

    assert response.headers["x-frame-options"] == "DENY"
    assert response.headers["content-security-policy-report-only"] == "default-src 'none'"
    assert response.headers["x-robots-tag"] == "noindex"
    assert response.headers["cache-control"] == "no-store"
    assert response.headers["pragma"] == "no-cache"
    assert response.headers["x-content-type-options"] == "nosniff"


def test_security_headers_streaming_body_unchanged(monkeypatch):
    monkeypatch.setenv("CASELIBRARY_SECURITY_HEADERS", "1")

    app = FastAPI()
    app.add_middleware(SecurityHeadersMiddleware)

    @app.get("/")
    def root():
        def body():
            yield b"alpha"
            yield b"beta"

        return StreamingResponse(body(), media_type="text/plain")

    client = TestClient(app, base_url="https://testserver")
    response = client.get("/")

    assert response.content == b"alphabeta"


def test_security_headers_registration_and_order(monkeypatch):
    monkeypatch.setenv("CASELIBRARY_SECURITY_HEADERS", "1")
    monkeypatch.setenv("CASELIBRARY_ACCESS_PASSWORD", "test-password")
    monkeypatch.delenv("CASELIBRARY_AUDIT_LOG", raising=False)
    original_app = main.app
    module = importlib.reload(main)

    try:
        middleware_classes = [middleware.cls.__name__ for middleware in module.app.user_middleware]

        assert middleware_classes[:4] == [
            "RequestContextMiddleware",
            "RequestAuditMiddleware",
            "SecurityHeadersMiddleware",
            "BaseHTTPMiddleware",
        ]

        client = TestClient(module.app, base_url="https://testserver", follow_redirects=False)
        response = client.get("/health")
        assert response.headers["x-robots-tag"] == "noindex, nofollow, noarchive"
        assert response.headers["x-content-type-options"] == "nosniff"
        protected = client.get("/data-explorer", headers={"accept": "text/html"})
        assert protected.status_code == 303
        assert protected.headers["location"] == "/access"
        assert protected.headers["x-robots-tag"] == "noindex, nofollow, noarchive"
        assert protected.headers["x-content-type-options"] == "nosniff"
    finally:
        module.app = original_app
