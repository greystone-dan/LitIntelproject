from fastapi.testclient import TestClient

from backend import main, routes


def _client():
    return TestClient(main.app, raise_server_exceptions=False)


def test_unknown_page_returns_html_404_for_browsers():
    r = _client().get("/nonexistent-page", headers={"Accept": "text/html,application/xhtml+xml"})
    assert r.status_code == 404
    assert r.headers["content-type"].startswith("text/html")
    assert "Page not found" in r.text and 'href="/"' in r.text


def test_unknown_page_keeps_json_for_api_clients():
    for headers in ({"Accept": "application/json"}, {}):
        r = _client().get("/nonexistent-page", headers=headers)
        assert r.status_code == 404
        assert r.json() == {"detail": "Not Found"}


def test_favicon_is_served_and_linked():
    r = _client().get("/favicon.ico")
    assert r.status_code == 200
    assert r.headers["content-type"].startswith("image/svg+xml")
    assert "<svg" in r.text
    assert 'rel="icon"' in routes._data_explorer_page_html()


def test_experimental_needed_notice_is_present_and_scripted():
    html = routes._data_explorer_page_html()
    assert 'id="experimentalNeeded"' in html
    assert "This preview needs Experimental turned on" in html
    assert "updateExperimentalNeeded" in html and "soon-" in html
