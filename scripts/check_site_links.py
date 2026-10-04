"""Offline audit of local URLs emitted by the application's served HTML pages."""

from __future__ import annotations

import argparse
import inspect
import os
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlsplit

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

_DYNAMIC_MARKERS = ("${", "{{", "}}", "<%", "%>")
_FETCH_RE = re.compile(
    r"\bfetch\s*\(\s*([^,\)]+)(?:,\s*(\{[^)]*\}))?", re.IGNORECASE
)
_XHR_RE = re.compile(
    r"\.\s*open\s*\(\s*(['\"])([A-Z]+)\1\s*,\s*([^,\)]+)",
    re.IGNORECASE,
)
_METHOD_OPTION_RE = re.compile(
    r"\bmethod\s*:\s*(['\"])([A-Z]+)\1", re.IGNORECASE
)
_STRING_RE = re.compile(r"""^\s*(['"])(.*?)\1\s*$""", re.DOTALL)
_TEMPLATE_RE = re.compile(r"^\s*`(.*?)`\s*$", re.DOTALL)


@dataclass(frozen=True)
class Route:
    path: str
    methods: frozenset[str] = frozenset()
    static_directories: tuple[Path, ...] = ()


@dataclass(frozen=True)
class Finding:
    page: str
    url: str
    source: str
    reason: str
    suggestion: str

    def __str__(self) -> str:
        return (
            f"{self.page}: {self.source} URL {self.url!r}: {self.reason}. "
            f"{self.suggestion}"
        )


class _HTMLLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.urls: list[tuple[str, str, str]] = []
        self.scripts: list[str] = []
        self._script_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("href") is not None:
            self.urls.append(("href", values["href"] or "", "GET"))
        if tag == "form":
            self.urls.append((
                "action",
                values.get("action") or "",
                (values.get("method") or "GET").upper(),
            ))
        if tag == "script":
            self._script_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._script_depth:
            self._script_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._script_depth:
            self.scripts.append(data)


def _literal_url(expression: str) -> tuple[str | None, bool]:
    """Return a statically known URL, or mark a nonliteral expression dynamic."""
    match = _STRING_RE.match(expression)
    if match:
        return match.group(2), False
    match = _TEMPLATE_RE.match(expression)
    if match:
        value = match.group(1)
        if any(marker in value for marker in _DYNAMIC_MARKERS):
            return None, True
        return value, False
    return None, True


def _classify(url: str, page: str) -> tuple[str, str | None]:
    value = url.strip()
    if not value:
        return "empty", None
    if any(marker in value for marker in _DYNAMIC_MARKERS):
        return "dynamic", None
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc:
        return "external", None
    if value.startswith("#"):
        return "fragment", None
    if parsed.path == "":
        return "fragment", None
    resolved = urlsplit(urljoin("http://local.invalid" + page, value))
    path = resolved.path or "/"
    return "local", path


def _known_static_asset(path: str, routes: Iterable[Route | object]) -> bool:
    for route in routes:
        directories = getattr(route, "static_directories", ())
        mount_path = route.path.rstrip("/")
        if not directories or not mount_path:
            continue
        prefix = mount_path + "/"
        if not path.startswith(prefix):
            continue
        relative_path = path[len(prefix):]
        if any((Path(directory) / relative_path).is_file() for directory in directories):
            return True
    return False


def _route_match(
    path: str, routes: Iterable[Route | object], method: str | None = "GET"
) -> bool:
    """Match a path/method, allowing Starlette's normal trailing-slash redirect."""
    candidates = {path}
    if path != "/":
        candidates.add(path[:-1] if path.endswith("/") else path + "/")
    for route in routes:
        route_path = route.path
        pattern = ""
        cursor = 0
        for match in re.finditer(r"\{([A-Za-z_][A-Za-z0-9_]*)(?::([A-Za-z_][A-Za-z0-9_]*))?\}", route_path):
            pattern += re.escape(route_path[cursor:match.start()])
            converter = match.group(2) or "str"
            expressions = {
                "str": r"[^/]+",
                "int": r"[0-9]+",
                "float": r"[0-9]+(?:\.[0-9]+)?",
                "uuid": r"[0-9a-fA-F-]+",
                "path": r".+",
            }
            if converter not in expressions:
                pattern = ""
                break
            pattern += expressions[converter]
            cursor = match.end()
        if pattern or not re.search(r"\{[^}]+\}", route_path):
            pattern += re.escape(route_path[cursor:])
        else:
            continue
        if method is not None and route.methods and method.upper() not in route.methods:
            continue
        if any(re.fullmatch(pattern, candidate) for candidate in candidates):
            return True
    return False


def audit_html_pages(
    pages: dict[str, str], routes: Iterable[Route | object]
) -> list[Finding]:
    """Audit HTML snapshots by page path against registered application routes."""
    route_list = list(routes)
    findings: list[Finding] = []
    for page, html in sorted(pages.items()):
        page_path = urlsplit(page).path or "/"
        parser = _HTMLLinks()
        parser.feed(html)
        urls = list(parser.urls)
        for script in parser.scripts:
            for pattern, source in ((_FETCH_RE, "fetch"), (_XHR_RE, "XHR")):
                for match in pattern.finditer(script):
                    if source == "fetch":
                        expression = match.group(1)
                        options = match.group(2) or ""
                        method_match = _METHOD_OPTION_RE.search(options)
                        method = method_match.group(2).upper() if method_match else "GET"
                    else:
                        expression = match.group(3)
                        method = match.group(2).upper()
                    url, dynamic = _literal_url(expression)
                    if dynamic:
                        continue
                    if url is not None:
                        urls.append((source, url, method))
        seen: set[tuple[str, str, str]] = set()
        for source, url, method in urls:
            key = (source, url, method)
            if key in seen:
                continue
            seen.add(key)
            kind, path = _classify(url, page_path)
            if source in {"action", "href"} and not url.strip():
                kind, path = "local", page_path
            if kind != "local":
                continue
            if path is not None and _route_match(path, route_list, method):
                continue
            if path is not None and _known_static_asset(path, route_list):
                continue
            route_exists = path is not None and _route_match(path, route_list, None)
            reason = (
                f"local path {path!r} has no registered {method} route"
                if route_exists
                else f"local path {path!r} does not match a registered route"
            )
            findings.append(Finding(
                page=page_path,
                url=url,
                source=source,
                reason=reason,
                suggestion=(
                    "Correct the URL or register the intended local route; "
                    "use an explicit dynamic expression only when runtime construction is intentional."
                ),
            ))
    return findings


def _served_html_pages() -> tuple[dict[str, str], list[Route]]:
    """Render HTML routes without starting app lifespan or connecting to a database."""
    # Importing the application normally makes backend.database load local dotenv
    # files and inspect database credentials. The audit must not access either.
    import dotenv

    dotenv.load_dotenv = lambda *args, **kwargs: False
    for key, value in {
        "POSTGRES_USER": "site-link-audit",
        "POSTGRES_PASSWORD": "site-link-audit",
        "POSTGRES_HOST": "127.0.0.1",
        "POSTGRES_PORT": "5432",
        "POSTGRES_DB": "site-link-audit",
        "DATABASE_URL": "",
    }.items():
        os.environ[key] = value

    from fastapi.responses import HTMLResponse
    from fastapi.routing import APIRoute
    from fastapi.testclient import TestClient
    from backend.main import app
    from backend.routes import issue_brief_page_html
    from backend.case_reader_ui import case_reader_with_statutes_html

    pages: dict[str, str] = {}
    routes: list[Route] = []
    client = TestClient(app, raise_server_exceptions=True)
    for route in app.routes:
        route_methods = frozenset(getattr(route, "methods", None) or ())
        static_app = getattr(route, "app", None)
        static_directories = tuple(
            Path(directory)
            for directory in getattr(static_app, "all_directories", ())
        )
        routes.append(Route(route.path, route_methods, static_directories))
        path = route.path
        is_builtin_html = path in {
            app.docs_url,
            app.redoc_url,
            app.swagger_ui_oauth2_redirect_url,
        }
        if (
            (
                getattr(route, "response_class", None) is not HTMLResponse
                and not is_builtin_html
            )
            or "GET" not in route_methods
        ):
            continue
        if path == app.docs_url:
            content = client.get(path).text
            pages[path] = content
            continue
        if path == app.redoc_url:
            content = client.get(path).text
            pages[path] = content
            continue
        if path == app.swagger_ui_oauth2_redirect_url:
            content = client.get(path).text
            pages[path] = content
            continue
        if not isinstance(route, APIRoute):
            continue
        endpoint = route.endpoint
        if path == "/access":
            content = client.get(path).text
        elif path == "/issue-brief-ui":
            content = issue_brief_page_html({})
        elif path == "/case-reader-ui/{case_id}":
            content = case_reader_with_statutes_html(
                case_id=1, case_title="Fixture", case_citation="", case_date="",
                case_court="", case_summary="",
            )
        else:
            signature = inspect.signature(endpoint)
            required = [
                parameter for parameter in signature.parameters.values()
                if parameter.default is inspect.Parameter.empty
            ]
            if required:
                raise RuntimeError(
                    f"HTML route {path} needs a deterministic fixture for "
                    f"{', '.join(parameter.name for parameter in required)}"
                )
            response = client.get(path)
            if response.status_code >= 400 or "text/html" not in response.headers.get(
                "content-type", ""
            ):
                raise RuntimeError(
                    f"HTML route {path} returned {response.status_code} "
                    f"with {response.headers.get('content-type', 'no content type')}"
                )
            content = response.text
        pages[path] = content
    return pages, routes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--quiet", action="store_true", help="print only failures and final status"
    )
    args = parser.parse_args()
    try:
        pages, routes = _served_html_pages()
    except Exception as exc:  # Report unsupported page rendering rather than silently passing.
        print(f"Unable to build served HTML page snapshots: {type(exc).__name__}: {exc}")
        return 2
    findings = audit_html_pages(pages, routes)
    if not args.quiet:
        print(f"Audited {len(pages)} HTML page snapshots against {len(routes)} registered routes.")
    for finding in findings:
        print(f"ERROR: {finding}")
    print(f"{len(findings)} local URL finding(s).")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
