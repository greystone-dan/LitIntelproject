import os

from starlette.types import ASGIApp, Message, Receive, Scope, Send


def _flag(name: str) -> bool:
    return os.getenv(name, "") == "1"


def _header_value(scope: Scope, name: bytes) -> str:
    for key, value in scope.get("headers", []):
        if key == name:
            return value.decode("latin-1")
    return ""


def _is_https(scope: Scope) -> bool:
    if scope.get("scheme") == "https":
        return True
    forwarded_proto = _header_value(scope, b"x-forwarded-proto").split(",", 1)[0].strip().lower()
    return forwarded_proto == "https"


def _csp_value() -> str:
    policy = [
        "default-src 'self'",
        "base-uri 'self'",
        "form-action 'self'",
        "object-src 'none'",
        "frame-ancestors 'self'",
        "img-src 'self' data:",
        "font-src 'self' https://fonts.gstatic.com",
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
        "script-src 'self' 'unsafe-inline' https://unpkg.com",
    ]
    return "; ".join(policy)


class SecurityHeadersMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app
        self.enabled = _flag("CASELIBRARY_SECURITY_HEADERS")
        try:
            self.hsts_max_age = max(0, int(os.getenv("CASELIBRARY_HSTS_MAX_AGE", "31536000")))
        except ValueError:
            self.hsts_max_age = 31536000
        self.hsts_subdomains = _flag("CASELIBRARY_HSTS_SUBDOMAINS")
        self.csp_enforce = _flag("CASELIBRARY_CSP_ENFORCE")

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http" or not self.enabled:
            await self.app(scope, receive, send)
            return

        hsts = None
        if _is_https(scope):
            hsts = f"max-age={self.hsts_max_age}"
            if self.hsts_subdomains:
                hsts += "; includeSubDomains"

        header_name = "Content-Security-Policy" if self.csp_enforce else "Content-Security-Policy-Report-Only"
        csp = _csp_value()

        async def send_wrapper(message: Message) -> None:
            if message["type"] == "http.response.start":
                headers = list(message.get("headers", []))
                message["headers"] = headers
                existing = {k.lower() for k, _ in headers}

                def add(name: str, value: str) -> None:
                    encoded = name.encode("latin-1")
                    if encoded.lower() not in existing:
                        headers.append((encoded, value.encode("latin-1")))
                        existing.add(encoded.lower())

                add("x-content-type-options", "nosniff")
                add("referrer-policy", "strict-origin-when-cross-origin")
                add("x-frame-options", "SAMEORIGIN")
                add("permissions-policy", "camera=(), microphone=(), geolocation=()")
                if hsts:
                    add("strict-transport-security", hsts)
                add(header_name, csp)
            await send(message)

        await self.app(scope, receive, send_wrapper)
