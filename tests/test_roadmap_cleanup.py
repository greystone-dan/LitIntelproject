from starlette.requests import Request

from backend import routes
from backend.pages.coming_soon_page import render


def _request(headers=None, query=b""):
	raw = [(k.lower().encode(), v.encode()) for k, v in (headers or {}).items()]
	return Request({"type": "http", "method": "GET", "path": "/live-analysis", "headers": raw, "query_string": query})


def test_overview_has_no_stray_tuple_text():
	html = render("overview")
	assert "('" not in html and "','" not in html and "\\'" not in html


def test_position_item_has_no_stale_decision_count():
	for slug in ("intelligence", "argument-breakdown"):
		html = render(slug)
		assert "665" not in html and "about 660" not in html


def test_live_analysis_opened_directly_goes_to_workbench():
	response = routes.live_analysis_page(_request({"sec-fetch-dest": "document"}))
	assert response.status_code == 307 and response.headers["location"] == "/workbench#live"


def test_live_analysis_frame_and_plain_requests_still_serve_the_page():
	assert routes.live_analysis_page(_request({"sec-fetch-dest": "iframe"})).status_code == 200
	assert routes.live_analysis_page(_request()).status_code == 200
	assert routes.live_analysis_page(_request({"sec-fetch-dest": "document"}, b"embed=1")).status_code == 200
