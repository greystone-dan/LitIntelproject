from fastapi.testclient import TestClient

from backend.main import app
from backend.pages.data_explorer import data_explorer_page_html
from backend.pages.live_analysis import live_analysis_page_html

client = TestClient(app, follow_redirects=False)


def test_root_goes_to_welcome():
    response = client.get("/")
    assert response.status_code == 307 and response.headers["location"] == "/welcome"


def test_welcome_has_two_choices_and_no_db():
    html = client.get("/welcome").text
    assert "Welcome" in html and 'data-mode="demo"' in html and 'data-mode="admin"' in html


def test_explorer_pages_apply_saved_mode():
    for html in (data_explorer_page_html(), live_analysis_page_html()):
        assert "ilit-demo" in html and "ilitDevTab" in html
    assert 'id="modeSwitch" href="/welcome"' in data_explorer_page_html()
