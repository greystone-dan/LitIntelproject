import base64
import binascii
import hmac
import os
import time
from contextlib import asynccontextmanager
from hashlib import sha256

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, Response

from .database import init_db
from .routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


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
    if not issued_at.isdigit() or not hmac.compare_digest(
        supplied_signature, _access_signature(issued_at, secret)
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
    response = await call_next(request)
    response.headers["X-Robots-Tag"] = "noindex, nofollow, noarchive"
    return response


app.include_router(router)


@app.get("/")
def root():
    return RedirectResponse(url="/data-explorer", status_code=307)


@app.get("/health")
def health():
    return {"message": "AI CaseLibrary backend is running"}


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
    if not configured_password or not hmac.compare_digest(password, configured_password):
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
