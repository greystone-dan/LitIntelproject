"""Content-negotiated HTML error pages for browser requests."""

from fastapi.exception_handlers import http_exception_handler as default_http_exception_handler
from fastapi.responses import HTMLResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request
from starlette.responses import Response


def request_accepts_html(request: Request) -> bool:
    """Return whether the Accept header permits an HTML representation."""
    for item in request.headers.get("accept", "").lower().split(","):
        media_type, *parameters = item.strip().split(";")
        if media_type not in {"text/html", "application/xhtml+xml"}:
            continue
        quality = 1.0
        for parameter in parameters:
            name, separator, value = parameter.strip().partition("=")
            if separator and name.strip() == "q":
                try:
                    quality = float(value.strip())
                except ValueError:
                    quality = 0.0
        if quality > 0:
            return True
    return False


def html_error_page(status_code: int) -> HTMLResponse:
    """Build a minimal, safe error page without echoing exception details."""
    if status_code == 404:
        title = "Page not found"
        message = "The requested page could not be found."
    else:
        title = "Server error"
        message = "The server could not complete this request."
    content = (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        f"<title>{title}</title></head><body><main><h1>{title}</h1>"
        f"<p>{message}</p><nav><a href=\"/data-explorer\">Home</a> "
        "<a href=\"/data-explorer?tab=search\">Search</a></nav>"
        "</main></body></html>"
    )
    return HTMLResponse(content=content, status_code=status_code)


async def handle_http_exception(
    request: Request, exc: StarletteHTTPException
) -> Response:
    if request_accepts_html(request) and exc.status_code in {404, 500}:
        response = html_error_page(exc.status_code)
        if exc.headers:
            response.headers.update(exc.headers)
        return response
    return await default_http_exception_handler(request, exc)


async def handle_unhandled_exception(request: Request, exc: Exception) -> Response:
    del exc  # Never expose implementation details in an error response.
    if request_accepts_html(request):
        return html_error_page(500)
    return PlainTextResponse("Internal Server Error", status_code=500)
