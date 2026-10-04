"""Response helpers for cacheable, non-personalized HTML page shells."""

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
    """Build a publicly cached, non-personalized HTML response with ETag support.

    The one-hour freshness lifetime applies only to static page shells. Dynamic
    API responses and sensitive routes must continue to set their explicit
    no-store headers instead of using this helper. Varying on Cookie keeps
    optional authenticated deployments from sharing a cached shell across
    distinct access-cookie states.
    """
    etag = compute_etag(content)
    headers = {
        "Cache-Control": "public, max-age=3600",
        "ETag": etag,
        "Vary": "Cookie",
    }
    if _if_none_match_matches(if_none_match, etag):
        return Response(status_code=304, headers=headers)
    return HTMLResponse(content=content, status_code=status_code, headers=headers)
