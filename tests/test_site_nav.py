"""Static presentation tests: no lifespan, database session or endpoint I/O."""

import asyncio
import inspect
import shutil
import subprocess
from html.parser import HTMLParser
from urllib.parse import parse_qs, urlencode, urlsplit

import pytest
from fastapi.responses import HTMLResponse
from fastapi.testclient import TestClient

from backend import main, routes
from backend.pages.site_nav import (
    LINKS, SCRIPT, SiteNavMiddleware, home_html, inject_html, route_context,
)


class Elements(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


def exchange(path="/data-explorer", body=b"<html><body>decision</body></html>",
             status=200, headers=None, streaming=False, query=b"", method="GET"):
    messages = []
    original_headers = headers if headers is not None else [
        (b"content-type", b"text/html; charset=utf-8"),
        (b"content-length", str(len(body)).encode()),
    ]
    original = [
        {"type": "http.response.start", "status": status, "headers": original_headers},
        {"type": "http.response.body", "body": body, "more_body": streaming},
    ]
    if streaming:
        original.append({"type": "http.response.body", "body": b"tail", "more_body": False})

    async def app(scope, receive, send):
        for message in original:
            await send(message)

    async def receive():
        return {"type": "http.request", "body": b""}

    async def send(message):
        messages.append(message)

    asyncio.run(SiteNavMiddleware(app)(
        {"type": "http", "method": method, "path": path, "query_string": query},
        receive, send,
    ))
    return original, messages


def test_preserves_original_bytes_and_body_attributes_and_length():
    body = '<!doctype html><html><body class="a > b" data-note=\'é > x\' onload="ready()">évidence</body></html>'.encode()
    _, messages = exchange(body=body)
    result = messages[1]["body"]
    opening, ending = body.split("évidence".encode())
    assert result.startswith(opening)
    assert result.endswith("évidence</body></html>".encode())
    assert int(dict(messages[0]["headers"])[b"content-length"]) == len(result)
    tags = Elements(result.decode()).tags
    assert sum("data-site-nav" in attrs for _, attrs in tags) == 1
    assert inject_html(result, "/data-explorer", b"") == result


def test_body_offset_uses_htmlparser_newline_convention():
    body = '<html><head>\r<title>title</title>\n</head>\n<body data-note="x > y">page</body></html>'.encode()
    result = inject_html(body, "/", b"")
    assert result.startswith(body.split(b"page")[0])
    assert result.endswith(b"page</body></html>")


@pytest.mark.parametrize("path", [
    "/health", "/api", "/api/cases", "/access", "/access/login", "/login",
    "/cases/export", "/exports/cases", "/cases/4/download", "/cases.csv",
    "/cases.docx", "/cases.json",
])
def test_excluded_paths(path):
    original, result = exchange(path=path)
    assert result == original


@pytest.mark.parametrize("status", [201, 204, 301, 307, 400, 401, 404, 500])
def test_non_200(status):
    original, result = exchange(status=status)
    assert result == original


@pytest.mark.parametrize("headers", [
    [(b"content-type", b"application/json")],
    [(b"content-type", b"text/csv")],
    [(b"content-type", b"application/vnd.openxmlformats-officedocument.wordprocessingml.document")],
    [(b"content-type", b"text/plain")],
    [(b"content-type", b"text/html; charset=iso-8859-1")],
    [(b"content-type", b"text/html"), (b"x-no-site-nav", b"1")],
    [(b"content-type", b"text/html"), (b"content-encoding", b"gzip")],
    [(b"content-type", b"text/html"), (b"content-disposition", b"attachment")],
])
def test_header_exclusions(headers):
    original, result = exchange(headers=headers)
    assert result == original


def test_streaming_is_forwarded_unchanged():
    original, result = exchange(streaming=True)
    assert result == original


def test_head_is_forwarded_unchanged():
    original, result = exchange(method="HEAD")
    assert result == original


@pytest.mark.parametrize("body", [
    b'<html><head><meta name="x-no-site-nav" content="true"></head><body>x</body></html>',
    b'<html><head><meta content="1" name="no-site-nav" /></head><body>x</body></html>',
    b'<html><head><meta name="site-nav" content="off"></head><body>x</body></html>',
    b'<body><nav data-site-nav>already</nav></body>',
    b'{"detail":"not HTML"}', b'<body>\xff</body>',
    b'<script>const text="<body>";</script>',
])
def test_body_optouts_and_non_documents(body):
    assert inject_html(body, "/data-explorer", b"") == body


@pytest.mark.parametrize("path,query,key,detail", [
    ("/", "", "home", None),
    ("/data-explorer", "", "search", None),
    ("/data-explorer", "tab=search&case_id=17", "reader", "Case 17"),
    ("/data-explorer", "tab=judge-profile&judge=smith", "judges", "smith"),
    ("/data-explorer", "tab=citation-intelligence&case_id=17", "citations", "Case 17"),
    ("/data-explorer", "tab=fc-history", "fc", None),
    ("/data-explorer", "tab=fc-analytics", "fc", None),
    ("/data-explorer", "tab=about", "about", None),
    ("/data-explorer", "tab=info", "about", None),
    ("/data-explorer", "tab=site-architecture", "about", None),
    ("/data-explorer", "group=info", "about", None),
    ("/data-explorer", "tab=themes", None, None),
    ("/data-explorer", "tab=workbench", None, None),
    ("/case-reader-ui/17", "", "reader", "Case 17"),
    ("/judges/smith", "", "judges", "smith"),
    ("/issue-brief-ui", "tag=topic%3Afairness", "briefs", "topic:fairness"),
    ("/citation-map", "case_id=17", "citations", "Case 17"),
    ("/memo-citation-check", "", "memo", None),
    ("/saved-searches-ui", "", "saved", None),
])
def test_route_context_and_current(path, query, key, detail):
    assert route_context(path, parse_qs(query)) == (key, detail)
    text = inject_html(b"<body>page</body>", path, query.encode()).decode()
    current = [attrs["data-site-link"] for _, attrs in Elements(text).tags
               if "data-site-link" in attrs and attrs.get("aria-current") == "page"]
    assert current == ([key] if key else [])


def test_breadcrumb_labels_are_escaped():
    text = inject_html(b"<body>x</body>", "/issue-brief-ui",
                       urlencode({"tag": '<img src=x onerror="bad()"> & issue'}).encode()).decode()
    assert '&lt;img src=x onerror=&quot;bad()&quot;&gt; &amp; issue' in text
    assert not any(tag == "img" for tag, _ in Elements(text).tags)


# This inventory is compared to the actual router, so new HTML routes require a
# deliberate review. DB-dependent pages are represented by finite fixture HTML,
# not invoked; static builders can safely be called without dependencies.
HTML_ROUTES = {
    "/citation-map", "/live-analysis", "/memo-citation-check", "/deidentify",
    "/case-reader", "/data-explorer", "/saved-searches-ui", "/statutes",
    "/case-reader-ui/{case_id}", "/discussion-units-sandbox", "/issue-brief-ui",
    "/citation-pass", "/quick-search", "/testing", "/prototype", "/research",
    "/tag-finder", "/themes",
}
DB_HTML_ROUTES = {"/case-reader-ui/{case_id}", "/issue-brief-ui"}


def test_actual_router_html_inventory_without_invoking_db():
    actual = {route.path: route for route in routes.router.routes
              if getattr(route, "response_class", None) is HTMLResponse}
    assert set(actual) == HTML_ROUTES
    for path, route in actual.items():
        if path in DB_HTML_ROUTES:
            assert route.dependant.dependencies
            body = b"<html><body>DB-dependent fixture</body></html>"
        elif path == "/case-reader":
            assert route.endpoint().headers["location"] == "/data-explorer"
            assert route.endpoint(17).headers["location"] == "/data-explorer?case_id=17"
            continue
        else:
            assert not route.dependant.dependencies
            assert not inspect.iscoroutinefunction(route.endpoint)
            response = route.endpoint()
            body = response.body if isinstance(response, HTMLResponse) else response.encode()
        result = inject_html(body, path.replace("{case_id}", "17"), b"")
        assert any("data-site-nav" in attrs for _, attrs in Elements(result.decode()).tags), path


def test_navigation_targets_match_routes_and_redirect_contracts():
    paths = {route.path for route in main.app.routes}
    for _, _, url in LINKS:
        assert url.split("?")[0] in paths
    assert routes.about_page().headers["location"] == "/data-explorer?tab=about"
    assert routes.judges_page().headers["location"] == "/data-explorer?tab=judge-profile"
    assert routes.citation_intelligence_page().headers["location"] == "/data-explorer?tab=citation-intelligence"
    assert routes.fc_history_page().headers["location"] == "/data-explorer?tab=fc-history"
    assert routes.judge_profile_page("smith").headers["location"] == "/data-explorer?tab=judge-profile&judge=smith"


class HomeCards(HTMLParser):
    """Collect each card's own description and example, not the shared nav."""

    def __init__(self):
        super().__init__()
        self.cards = {}
        self.card = None
        self.field = None
        self.feed(home_html())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "data-tool-card" in attrs:
            key = attrs["data-tool-card"]
            assert key not in self.cards
            self.card = self.cards[key] = {"descriptions": [], "examples": []}
        if self.card is not None and "data-tool-description" in attrs:
            self.card["descriptions"].append("")
            self.field = "descriptions"
        if self.card is not None and "data-tool-example" in attrs:
            assert tag == "a"
            self.card["examples"].append({"href": attrs["href"], "text": ""})
            self.field = "examples"

    def handle_data(self, data):
        if self.field == "descriptions":
            self.card["descriptions"][-1] += data
        elif self.field == "examples":
            self.card["examples"][-1]["text"] += data

    def handle_endtag(self, tag):
        if tag in {"p", "a"}:
            self.field = None
        if tag == "section":
            self.card = None


def test_every_home_tool_has_one_plain_description_and_meaningful_example():
    cards = HomeCards().cards
    assert set(cards) == {key for key, _, _ in LINKS if key != "home"}
    for card in cards.values():
        assert len(card["descriptions"]) == len(card["examples"]) == 1
        description = card["descriptions"][0]
        assert description.strip() == description
        assert 5 <= len(description.split()) <= 15
        assert "\n" not in description
        assert card["examples"][0]["text"].startswith("Example")
        assert len(card["examples"][0]["text"].split()) >= 3


@pytest.mark.parametrize("key,path,query,label", [
    ("search", "/data-explorer", {"tab": ["search"], "query": ["Vavilov"]}, "Vavilov"),
    ("reader", "/data-explorer", {"tab": ["search"], "query": ["2019 SCC 65"]}, "open a result"),
    ("judges", "/data-explorer", {"tab": ["judge-profile"]}, "search a judge"),
    ("citations", "/data-explorer", {"tab": ["search"], "query": ["Vavilov"]}, "select Citation Intelligence"),
    ("fc", "/data-explorer", {"tab": ["fc-history"], "imm": ["IMM-1234-19"]}, "IMM-1234-19"),
    ("memo", "/memo-citation-check", {}, "upload a memo"),
    ("briefs", "/issue-brief-ui", {"tag": ["topic:fairness"]}, "topic:fairness"),
    ("saved", "/saved-searches-ui", {}, "open a saved search"),
    ("about", "/data-explorer", {"tab": ["site-architecture"]}, "system architecture"),
])
def test_home_example_links_use_existing_route_and_query_contracts(key, path, query, label):
    example = HomeCards().cards[key]["examples"][0]
    url = urlsplit(example["href"])
    assert not url.scheme and not url.netloc and not url.fragment
    assert url.path == path
    assert path in {route.path for route in main.app.routes}
    assert parse_qs(url.query) == query
    assert label in example["text"]
    if "tab" in query:
        assert f"data-tab=\"{query['tab'][0]}\"" in routes._data_explorer_page_html()
    if key == "fc":
        assert ".get('imm')" in routes._data_explorer_page_html()
    if key == "briefs":
        assert "tag" in inspect.signature(routes.get_issue_brief_ui).parameters


def test_home_and_gate_without_lifespan(monkeypatch):
    monkeypatch.delenv("CASELIBRARY_ACCESS_PASSWORD", raising=False)
    monkeypatch.delenv("CASELIBRARY_AUDIT_LOG", raising=False)
    # Do not use a context manager: TestClient must not run init_db lifespan.
    client = TestClient(main.app, headers={"accept": "text/html"})
    response = client.get("/")
    assert response.status_code == 200
    assert "data-site-nav" in response.text
    assert "Vavilov" in response.text and "IMM-1234-19" in response.text
    assert "/data-explorer" in response.text
    assert response.headers["x-robots-tag"] == "noindex, nofollow, noarchive"
    monkeypatch.setenv("CASELIBRARY_ACCESS_PASSWORD", "test-password")
    monkeypatch.setenv("CASELIBRARY_SESSION_SECRET", "test-session-secret")
    assert client.get("/", follow_redirects=False).headers["location"] == "/access"
    for path in HTML_ROUTES:
        blocked = client.get(path.replace("{case_id}", "17"), follow_redirects=False)
        assert blocked.status_code == 303 and blocked.headers["location"] == "/access"
        assert "data-site-nav" not in blocked.text
    login = client.get("/access")
    assert login.status_code == 200 and "data-site-nav" not in login.text
    assert client.get("/api/private").status_code == 401
    rejected = client.post("/access/login", data={"password": "wrong"})
    assert rejected.status_code == 401 and "data-site-nav" not in rejected.text
    client.post("/access/login", data={"password": "test-password"}, follow_redirects=False)
    assert "data-site-nav" in client.get("/").text
    client.close()


def test_middleware_order():
    order = [middleware.cls.__name__ for middleware in main.app.user_middleware]
    assert order.index("RequestAuditMiddleware") < order.index("BaseHTTPMiddleware") < order.index("SiteNavMiddleware")


def test_accessible_quick_search_and_actual_handler():
    tags = Elements(inject_html(b"<body>x</body>", "/", b"").decode()).tags
    assert any(tag == "button" and attrs.get("aria-expanded") == "false"
               and attrs.get("aria-controls") == "site-primary-links" for tag, attrs in tags)
    assert any(tag == "form" and attrs.get("method") == "get"
               and attrs.get("action") == "/data-explorer" for tag, attrs in tags)
    assert any(tag == "input" and attrs.get("name") == "query" for tag, attrs in tags)
    html = routes._data_explorer_page_html()
    assert 'fetch(`/analytics/search/cases?${params}`)' in html
    assert "query:document.getElementById('searchQuery').value" in html
    assert "field.value=query;form.requestSubmit()" in SCRIPT
    encoded = urlencode({"tab": "search", "query": "A & B / 2019 SCC 65"})
    assert parse_qs(encoded)["query"] == ["A & B / 2019 SCC 65"]


def test_script_syntax_and_shortcut_behavior():
    node = shutil.which("node")
    if not node:
        pytest.skip("Node unavailable for isolated JavaScript test")
    # Minimal DOM double exercises the injected script, not a browser or server.
    harness = """
const listeners={};let focused=0,prevented=0,expanded='false';
const input={focus(){focused++}};
const button={getAttribute(){return expanded},setAttribute(k,v){expanded=v},addEventListener(k,fn){listeners.menu=fn},focus(){}};
const links={dataset:{}};
const shell={querySelector(s){return s==='.site-menu-toggle'?button:s==='.site-nav-links'?links:input},querySelectorAll(){return []}};
const searchText='A & B / 2019 SCC 65';let submitted=0;
const field={value:''},form={requestSubmit(){if(field.value!==searchText)throw Error('query decode');submitted++}};
global.location=new URL('http://localhost/data-explorer?'+new URLSearchParams({tab:'search',query:searchText}));
class Element{constructor(editable=false,ancestor=false,control=false){this.isContentEditable=editable;this.ancestor=ancestor;this.control=control}
closest(s){return s.includes('contenteditable')?this.ancestor:this.control}}
global.Element=Element;
global.document={querySelector(){return shell},querySelectorAll(){return []},
getElementById(id){return id==='searchQuery'?field:id==='caseSearch'?form:null},
addEventListener(k,fn){listeners[k]=fn}};
global.window={addEventListener(){}};
"""
    script = SCRIPT.removeprefix("<script>").removesuffix("</script>")
    checks = """
function key(target,key='/',options={}){listeners.keydown({target,key,...options,preventDefault(){prevented++}})}
key(new Element());if(focused!==1||prevented!==1)throw Error('shortcut');
key(new Element(true));key(new Element(false,true));key(new Element(false,false,true));
key(new Element(),'/',{ctrlKey:true});key(new Element(),'/',{metaKey:true});
key(new Element(),'/',{altKey:true});key(new Element(),'/',{isComposing:true});
if(focused!==1)throw Error('editable shortcut');
listeners.menu();if(expanded!=='true'||links.dataset.open!=='true')throw Error('menu');
key(new Element(),'Escape');if(expanded!=='false'||links.dataset.open!=='false')throw Error('Escape');
listeners.DOMContentLoaded();if(submitted!==1)throw Error('quick search not submitted');
"""
    result = subprocess.run([node, "-e", harness + script + checks], capture_output=True, text=True, timeout=10)
    assert result.returncode == 0, result.stderr
