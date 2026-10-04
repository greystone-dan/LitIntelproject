"""Response helpers for revalidatable static HTML pages."""

from hashlib import sha256

from starlette.responses import HTMLResponse, Response


def compute_etag(content: str | bytes) -> str:
    """Return a weak validator for the identity and compressed forms of HTML."""
    if isinstance(content, str):
        content = content.encode("utf-8")
    return f'W/"{sha256(content).hexdigest()}"'


def _if_none_match_matches(header: str | None, etag: str) -> bool:
    if not header:
        return False
    expected = etag.removeprefix("W/")
    for candidate in header.split(","):
        candidate = candidate.strip()
        if candidate == "*":
            return True
        if candidate.startswith("W/"):
            candidate = candidate[2:]
        if candidate == expected:
            return True
    return False


def static_html_response(
    content: str,
    *,
    if_none_match: str | None = None,
    status_code: int = 200,
) -> Response:
    """Build a privately cached HTML response with conditional ETag support.

    ``private, no-cache`` allows a browser to retain the page but requires
    revalidation before reuse. Sensitive routes must continue to set their
    explicit no-store headers instead of using this helper.
    """
    etag = compute_etag(content)
    headers = {
        "Cache-Control": "private, no-cache",
        "ETag": etag,
    }
    if _if_none_match_matches(if_none_match, etag):
        return Response(status_code=304, headers=headers)
    return HTMLResponse(content=content, status_code=status_code, headers=headers)
