import base64
import binascii
import hmac
import os
import time
from contextlib import asynccontextmanager
from hashlib import sha256

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, Response
from starlette.routing import Match, Mount
from starlette.staticfiles import StaticFiles

from . import load_shedding
from .audit import RequestAuditMiddleware
from .database import init_db
from .db_limits import register_timeout_handlers
from .health import liveness, readiness
from .request_context import (
    RequestContextMiddleware,
    get_version_info,
)
from .overruling_risk_routes import router as overruling_risk_router
from .routes import router
from .security_headers import SecurityHeadersMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
register_timeout_handlers(app)
load_shedding.register(app)


ACCESS_COOKIE = "caselibrary_access"


def _private_access_config() -> tuple[str | None, str, int]:
    password = os.getenv("CASELIBRARY_ACCESS_PASSWORD")
    secret = os.getenv("CASELIBRARY_SESSION_SECRET") or os.getenv("SECRET_KEY") or password or ""
    try:
        lifetime = max(300, int(os.getenv("CASELIBRARY_SESSION_SECONDS", "86400")))
    except ValueError:
        lifetime = 86400
    return password, secret, lifetime


def _access_signature(issued_at: str, secret: str) -> str:
    return hmac.new(secret.encode("utf-8"), issued_at.encode("ascii"), sha256).hexdigest()


def _valid_access_cookie(value: str | None, secret: str, lifetime: int) -> bool:
    if not value or "." not in value:
        return False
    issued_at, supplied_signature = value.split(".", 1)
    if (
        not issued_at.isascii()
        or not issued_at.isdigit()
        or len(issued_at) > 20
        or not supplied_signature.isascii()
        or not hmac.compare_digest(supplied_signature, _access_signature(issued_at, secret))
    ):
        return False
    return 0 <= int(time.time()) - int(issued_at) <= lifetime


def _is_localhost_request(request: Request) -> bool:
    hostnames = {
        "localhost",
        "127.0.0.1",
        "0.0.0.0",
        "::1",
    }
    requested_host = (request.url.hostname or "").lower()
    client_host = (request.client.host if request.client else "").lower()
    forwarded_host = (request.headers.get("x-forwarded-host") or "").split(",", 1)[0].strip().lower()
    host_candidates = {requested_host, client_host, forwarded_host}
    return bool(host_candidates & hostnames) or any(host.startswith("localhost") for host in host_candidates if host)


def _login_page(error: str = "") -> HTMLResponse:
    message = f'<p class="error">{error}</p>' if error else ""
    return HTMLResponse(
        content=f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow,noarchive"><title>Private site access</title>
<style>body{{margin:0;min-height:100vh;display:grid;place-items:center;background:#f1efe8;color:#202522;font-family:system-ui,sans-serif}}main{{width:min(360px,calc(100% - 32px));padding:28px;background:#fffef9;border:1px solid #d8d5ca;border-radius:8px}}h1{{margin:0 0 8px;font-size:22px}}p{{color:#69726d;font-size:13px;line-height:1.5}}label{{display:block;margin:18px 0 6px;font-size:12px;font-weight:700}}input,button{{box-sizing:border-box;width:100%;height:42px;padding:0 12px;border:1px solid #d8d5ca;border-radius:5px;font:inherit}}button{{margin-top:12px;background:#202522;color:white;font-weight:700;cursor:pointer}}.error{{color:#a4412b}}</style></head>
<body><main><h1>Private research site</h1><p>Enter the access password to continue.</p>{message}<form method="post" action="/access/login"><label for="password">Access password</label><input id="password" name="password" type="password" autocomplete="current-password" required autofocus><button type="submit">Continue</button></form></main></body></html>""",
        status_code=401 if error else 200,
    )


@app.middleware("http")
async def private_access_and_noindex(request: Request, call_next):
    password, secret, lifetime = _private_access_config()
    public_path = request.url.path in {
        "/access",
        "/access/login",
        "/health",
        "/health/live",
        "/health/ready",
        "/health/limits",
    }
    matched_route = next(
        (route for route in app.routes if route.matches(request.scope)[0] == Match.FULL),
        None,
    ) if password else None
    static_asset = isinstance(matched_route, Mount) and isinstance(matched_route.app, StaticFiles)
    if password and not public_path and not static_asset and not _valid_access_cookie(
        request.cookies.get(ACCESS_COOKIE), secret, lifetime
    ):
        if "text/html" in request.headers.get("accept", "") and not (
            request.url.path == "/api" or request.url.path.startswith("/api/")
        ):
            response = RedirectResponse(url="/access", status_code=303)
        else:
            response = JSONResponse({"detail": "Authentication required."}, status_code=401)
    else:
        response = await call_next(request)
    response.headers["X-Robots-Tag"] = "noindex, nofollow, noarchive"
    return response


if os.getenv("CASELIBRARY_SECURITY_HEADERS") == "1":
    app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(RequestAuditMiddleware)
app.add_middleware(RequestContextMiddleware)


app.include_router(router)
app.include_router(overruling_risk_router)


@app.get("/")
def root():
    return RedirectResponse(url="/data-explorer", status_code=307)


@app.get("/health")
def health():
    return {"message": "AI CaseLibrary backend is running"}


@app.get("/health/live")
def health_live():
    return liveness()


@app.get(
    "/health/ready",
    responses={503: {"description": "A required dependency is unavailable"}},
)
def health_ready():
    document, is_ready = readiness()
    # Add safe version information to readiness response
    version_info = get_version_info()
    document["version"] = version_info
    return JSONResponse(document, status_code=200 if is_ready else 503)


@app.get("/api/version", response_model=dict[str, str | int])
def api_version() -> dict[str, str | int]:
    """Return safe application version information.

    The response contains only a sanitized commit, process start time, and
    interpreter version.
    """
    return get_version_info()


@app.exception_handler(Exception)
async def unhandled_exception_with_request_id(request: Request, _exc: Exception):
    """Preserve request correlation on the framework's generic 500 response."""
    request_id = getattr(request.state, "request_id", None)
    headers = {"X-Request-ID": request_id} if request_id else {}
    return Response(
        content="Internal Server Error",
        status_code=500,
        media_type="text/plain",
        headers=headers,
    )


@app.get("/robots.txt", response_class=Response, include_in_schema=False)
def robots() -> Response:
    return Response(content="User-agent: *\nDisallow: /\n", media_type="text/plain", headers={"X-Robots-Tag": "noindex, nofollow, noarchive"})


@app.get("/access", response_class=HTMLResponse, include_in_schema=False)
def access_page() -> HTMLResponse:
    password, _, _ = _private_access_config()
    if not password:
        return HTMLResponse("Private access is not configured.", status_code=503)
    return _login_page()


@app.post("/access/login", response_class=HTMLResponse, include_in_schema=False)
def access_login(request: Request, password: str = Form(...)) -> Response:
    configured_password, secret, lifetime = _private_access_config()
    if not configured_password or not hmac.compare_digest(
        password.encode("utf-8"), configured_password.encode("utf-8")
    ):
        return _login_page("That password was not accepted.")
    issued_at = str(int(time.time()))
    response = RedirectResponse(url="/data-explorer", status_code=303)
    response.set_cookie(
        ACCESS_COOKIE,
        f"{issued_at}.{_access_signature(issued_at, secret)}",
        max_age=lifetime,
        httponly=True,
        samesite="lax",
        secure=request.url.scheme == "https",
    )
    return response


@app.post("/access/logout", include_in_schema=False)
def access_logout(request: Request) -> Response:
    password, _, _ = _private_access_config()
    response = RedirectResponse(url="/access" if password else "/data-explorer", status_code=303)
    response.delete_cookie(
        ACCESS_COOKIE,
        httponly=True,
        samesite="lax",
        secure=request.url.scheme == "https",
    )
    return response
