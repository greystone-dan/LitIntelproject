import asyncio

from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request

from backend.html_errors import handle_http_exception, handle_unhandled_exception


def _request(accept: str) -> Request:
    return Request({
        "type": "http",
        "method": "GET",
        "path": "/missing",
        "query_string": b"",
        "headers": [(b"accept", accept.encode("latin-1"))],
        "server": ("testserver", 80),
        "client": ("testclient", 50000),
        "scheme": "http",
    })


def test_html_not_found_response_is_safe_html_with_correct_status():
    response = asyncio.run(
        handle_http_exception(
            _request("text/html,application/xhtml+xml"),
            StarletteHTTPException(status_code=404, detail="private detail"),
        )
    )

    assert response.status_code == 404
    assert response.media_type == "text/html"
    assert b"Page not found" in response.body
    assert b'href="/data-explorer">Home</a>' in response.body
    assert b'href="/data-explorer?tab=search">Search</a>' in response.body
    assert b"private detail" not in response.body


def test_api_http_errors_remain_json_and_keep_status():
    response = asyncio.run(
        handle_http_exception(
            _request("application/json"),
            StarletteHTTPException(status_code=404, detail="missing"),
        )
    )

    assert response.status_code == 404
    assert response.media_type == "application/json"
    assert response.body == b'{"detail":"missing"}'


def test_unhandled_html_error_is_a_generic_500_page():
    response = asyncio.run(
        handle_unhandled_exception(_request("text/html"), RuntimeError("secret detail"))
    )

    assert response.status_code == 500
    assert response.media_type == "text/html"
    assert b"Server error" in response.body
    assert b"secret detail" not in response.body


def test_unhandled_non_html_error_keeps_plain_text_500():
    response = asyncio.run(
        handle_unhandled_exception(_request("application/json"), RuntimeError("detail"))
    )

    assert response.status_code == 500
    assert response.media_type == "text/plain"
    assert response.body == b"Internal Server Error"
