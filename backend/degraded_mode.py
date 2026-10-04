"""Narrow database-outage responses and opt-in, container-local panel recovery."""

import html
import re

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.exc import InterfaceError, OperationalError

DATABASE_UNAVAILABLE_MESSAGE = (
    "iLit cannot reach its database right now. Try again in a minute."
)

_TIMEOUT_OR_STATEMENT = re.compile(
    r"time[\s_-]*out|timed\s+out|statement|query\s+cancel|canceling\s+query",
    re.IGNORECASE,
)
_CONNECTION_MESSAGE = re.compile(
    r"\bconnection refused\b|\bnetwork is unreachable\b|\bno route to host\b"
    r"|\bcould not translate host name\b|\btemporary failure in name resolution\b"
    r"|\bname or service not known\b|\bgetaddrinfo failed\b"
    r"|\bcould not resolve (?:host name|hostname)\b"
    r"|\bserver closed the connection unexpectedly\b"
    r"|\bconnection (?:is |already )?closed\b|\bconnection reset by peer\b"
    r"|\bconnection not open\b"
    r"|\bconnection was closed in the middle of operation\b"
    r"|\bSSL connection has been closed unexpectedly\b"
    r"|\bterminating connection due to administrator command\b"
    r"|\bthe database system is (?:shutting down|starting up)\b",
    re.IGNORECASE,
)


def is_database_connection_error(exc: Exception) -> bool:
    """Only DBAPI connection failures qualify; timeouts never qualify."""
    if not isinstance(exc, (OperationalError, InterfaceError)):
        return False
    original = exc.orig
    if original is None:
        return False
    # Inspect the driver error, not SQLAlchemy's SQL/parameters/URL rendering.
    message = str(original)
    if _TIMEOUT_OR_STATEMENT.search(message):
        return False
    state = (
        getattr(original, "sqlstate", None)
        or getattr(original, "pgcode", None)
        or getattr(getattr(original, "diag", None), "sqlstate", None)
    )
    if state:
        return isinstance(state, str) and (
            state.startswith("08") or state in {"57P01", "57P02", "57P03"}
        )
    return bool(_CONNECTION_MESSAGE.search(message))


def _accepts_html(request: Request) -> bool:
    for item in request.headers.get("accept", "").lower().split(","):
        media_type, *parameters = item.strip().split(";")
        if media_type != "text/html":
            continue
        quality = 1.0
        for parameter in parameters:
            key, _, value = parameter.strip().partition("=")
            if key == "q":
                try:
                    quality = float(value)
                except ValueError:
                    quality = 0.0
        if 0 < quality <= 1:
            return True
    return False


async def database_exception_handler(request: Request, exc: Exception):
    if not is_database_connection_error(exc):
        # Starlette's ExceptionMiddleware does not redispatch a raised handler
        # exception: the original continues to ServerErrorMiddleware/the caller.
        raise exc
    request_id = getattr(request.state, "request_id", None)
    path = request.url.path
    if (path == "/api" or path.startswith("/api/")) or not _accepts_html(request):
        document = {
            "detail": DATABASE_UNAVAILABLE_MESSAGE,
            "message": DATABASE_UNAVAILABLE_MESSAGE,
        }
        if request_id is not None:
            document["request_id"] = str(request_id)
        return JSONResponse(document, status_code=503)
    identifier = (
        f"<p>Request ID: {html.escape(str(request_id))}</p>"
        if request_id is not None
        else ""
    )
    return HTMLResponse(
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        "<title>Database unavailable</title></head><body><main>"
        f"<h1>Temporarily unavailable</h1><p>{DATABASE_UNAVAILABLE_MESSAGE}</p>"
        f'{identifier}<nav><a href="/">Home</a> '
        '<a href="/data-explorer">Search</a></nav></main></body></html>',
        status_code=503,
    )


def register_degraded_mode(app: FastAPI) -> None:
    app.add_exception_handler(OperationalError, database_exception_handler)
    app.add_exception_handler(InterfaceError, database_exception_handler)


def panel_helpers_script() -> str:
    """Include once per page, before callers; no interception or automatic fetch."""
    return r"""<script>
const fetchPanel = (() => {
    const inFlight = new WeakMap();
    const retryButtons = new WeakMap();
    return function fetchPanel(url, container, options = {}) {
        if (!container) return Promise.resolve(null);
        if (inFlight.has(container)) return inFlight.get(container);
        const current = () => {
            try { return !options.isCurrent || !!options.isCurrent(); }
            catch (_) { return false; }
        };
        if (!current()) return Promise.resolve(null);
        const button = retryButtons.get(container);
        if (button) button.disabled = true;
        const skeleton = document.createElement('div');
        skeleton.className = 'panel-skeleton';
        skeleton.setAttribute('aria-live', 'polite');
        skeleton.textContent = 'Loading…';
        if (button && container.contains(button)) container.prepend(skeleton);
        else container.replaceChildren(skeleton);
        // Defer work until the promise has been installed in the WeakMap.
        const pending = Promise.resolve().then(async () => {
            try {
                const response = await fetch(url, options.request || {});
                if (!response.ok) throw new Error('Panel request failed');
                const data = await response.json();
                if (!current()) return null;
                if (typeof options.render !== 'function') throw new Error('Missing renderer');
                container.replaceChildren();
                await options.render(data);
                if (!current()) return null;
                skeleton.remove();
                retryButtons.delete(container);
                return data;
            } catch (_) {
                if (!current()) return null;
                // Legacy cleanup may replace this container: install recovery after it.
                try { if (options.onError) await options.onError(); } catch (_) {}
                if (!current()) return null;
                const failure = document.createElement('div');
                failure.setAttribute('aria-live', 'polite');
                const message = document.createElement('p');
                message.textContent = 'This section could not load.';
                const retry = document.createElement('button');
                retry.type = 'button';
                retry.textContent = 'Retry';
                retry.addEventListener('click', () => {
                    if (retry.disabled || !current()) return;
                    retry.disabled = true;
                    fetchPanel(url, container, options);
                });
                failure.append(message, retry);
                retryButtons.set(container, retry);
                container.replaceChildren(failure);
                return null;
            } finally {
                if (inFlight.get(container) === pending) inFlight.delete(container);
                if (current() && button && container.contains(button)) button.disabled = false;
            }
        });
        inFlight.set(container, pending);
        return pending;
    };
})();
</script>"""
