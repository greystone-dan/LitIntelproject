import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.staticfiles import StaticFiles

from backend import main


def test_access_cookie_signature_and_expiry(monkeypatch):
    monkeypatch.setattr(main.time, "time", lambda: 1_000)
    token = f"1000.{main._access_signature('1000', 'secret')}"

    assert main._valid_access_cookie(token, "secret", 86400)
    assert not main._valid_access_cookie(token, "wrong-secret", 86400)

    monkeypatch.setattr(main.time, "time", lambda: 87_401)
    assert not main._valid_access_cookie(token, "secret", 86400)


def test_access_cookie_rejects_future_issue_time(monkeypatch):
    monkeypatch.setattr(main.time, "time", lambda: 1_000)
    token = f"1001.{main._access_signature('1001', 'secret')}"

    assert not main._valid_access_cookie(token, "secret", 86400)


def test_robots_disallows_all_crawlers():
    response = main.robots()

    assert response.body == b"User-agent: *\nDisallow: /\n"
    assert response.headers["x-robots-tag"] == "noindex, nofollow, noarchive"


@pytest.fixture
def access_client(monkeypatch, tmp_path):
    monkeypatch.delenv("CASELIBRARY_ACCESS_PASSWORD", raising=False)
    monkeypatch.setenv("CASELIBRARY_SESSION_SECRET", "test-session-secret")
    application = FastAPI()
    application.router.routes.extend(main.app.router.routes)
    application.middleware("http")(main.private_access_and_noindex)

    @application.get("/private")
    @application.get("/static/private")
    @application.post("/api/private")
    def protected_route():
        return {"ok": True}

    (tmp_path / "style.css").write_text("body { color: black; }")
    application.mount("/static", StaticFiles(directory=tmp_path))
    monkeypatch.setattr(main, "app", application)
    return TestClient(application, follow_redirects=False)


@pytest.mark.parametrize("password", [None, ""])
def test_private_gate_is_not_enforced_without_password(access_client, monkeypatch, password):
    if password is not None:
        monkeypatch.setenv("CASELIBRARY_ACCESS_PASSWORD", password)
    for method, path in [("GET", "/private"), ("POST", "/api/private"), ("GET", "/health")]:
        response = access_client.request(method, path)
        assert response.status_code == 200
        assert response.headers["x-robots-tag"] == "noindex, nofollow, noarchive"
    home = access_client.get("/")
    assert home.status_code == 200
    assert home.headers["content-type"].startswith("text/html")
    assert "/data-explorer" in home.text
    assert "Immigration litigation research" in home.text
    assert access_client.get("/access").status_code == 503
    assert access_client.get("/robots.txt").status_code == 200
    assert access_client.get("/docs").status_code == 200
    assert access_client.get("/missing").status_code == 404


def test_private_gate_redirects_html_and_denies_api(access_client, monkeypatch):
    monkeypatch.setenv("CASELIBRARY_ACCESS_PASSWORD", "test-password")
    response = access_client.get("/private", headers={"accept": "text/html"})
    assert response.status_code == 303
    assert response.headers["location"] == "/access"
    assert response.headers["x-robots-tag"] == "noindex, nofollow, noarchive"
    response = access_client.post("/api/private", headers={"accept": "text/html"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Authentication required."}
    assert response.headers["x-robots-tag"] == "noindex, nofollow, noarchive"


@pytest.mark.parametrize("path", [
    "/", "/private", "/data-explorer", "/cases", "/robots.txt", "/docs",
    "/openapi.json", "/access/logout", "/missing", "/access/extra", "/static-private",
    "/private.css", "/static/private",
])
def test_private_gate_protects_all_other_routes(access_client, monkeypatch, path):
    monkeypatch.setenv("CASELIBRARY_ACCESS_PASSWORD", "test-password")
    response = access_client.get(path, headers={"x-forwarded-host": "localhost"})
    assert response.status_code == 401


def test_private_gate_keeps_login_health_and_static_open(access_client, monkeypatch):
    monkeypatch.setenv("CASELIBRARY_ACCESS_PASSWORD", "test-password")
    assert access_client.get("/access").status_code == 200
    assert access_client.get("/health").json() == {"message": "AI CaseLibrary backend is running"}
    assert access_client.get("/static/style.css").status_code == 200
    assert access_client.get("/static/missing.css").status_code == 404
    assert access_client.post("/access/login", data={"password": "wrong"}).status_code == 401


@pytest.mark.parametrize("scheme", ["http", "https"])
def test_login_and_logout(access_client, monkeypatch, scheme):
    monkeypatch.setenv("CASELIBRARY_ACCESS_PASSWORD", "test-password")
    access_client.base_url = f"{scheme}://testserver"
    response = access_client.post("/access/login", data={"password": "test-password"})
    assert response.status_code == 303
    assert response.headers["location"] == "/data-explorer"
    cookie = response.headers["set-cookie"]
    assert "HttpOnly" in cookie and "SameSite=lax" in cookie and "Path=/" in cookie
    assert ("Secure" in cookie) == (scheme == "https")
    assert access_client.get("/private").status_code == 200
    assert access_client.post("/api/private").status_code == 200
    response = access_client.post("/access/logout")
    assert response.status_code == 303
    assert response.headers["location"] == "/access"
    assert "Max-Age=0" in response.headers["set-cookie"]
    assert main.ACCESS_COOKIE not in access_client.cookies
    assert access_client.get("/private", headers={"accept": "text/html"}).status_code == 303
    assert access_client.post("/api/private").status_code == 401


def test_login_supports_unicode_passwords(access_client, monkeypatch):
    monkeypatch.setenv("CASELIBRARY_ACCESS_PASSWORD", "tést-password")
    assert access_client.post("/access/login", data={"password": "incorrect-é"}).status_code == 401
    assert access_client.post("/access/login", data={"password": "tést-password"}).status_code == 303
    assert access_client.get("/private").status_code == 200


@pytest.mark.parametrize("token", [
    "invalid", "1000.wrong", f"{'1' * 5000}.signature",
])
def test_private_gate_rejects_malformed_cookies(access_client, monkeypatch, token):
    monkeypatch.setenv("CASELIBRARY_ACCESS_PASSWORD", "test-password")
    access_client.cookies.set(main.ACCESS_COOKIE, token)
    assert access_client.get("/private").status_code == 401


@pytest.mark.parametrize("token", ["1000.é", "١٠٠٠.signature"])
def test_access_cookie_rejects_unicode(token):
    assert not main._valid_access_cookie(token, "test-session-secret", 86400)


def test_private_gate_rejects_expired_cookie(access_client, monkeypatch):
    monkeypatch.setenv("CASELIBRARY_ACCESS_PASSWORD", "test-password")
    monkeypatch.setattr(main.time, "time", lambda: 1_000)
    assert access_client.post("/access/login", data={"password": "test-password"}).status_code == 303
    monkeypatch.setattr(main.time, "time", lambda: 87_401)
    assert access_client.get("/private").status_code == 401
