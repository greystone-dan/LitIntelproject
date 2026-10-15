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


def test_live_analysis_serves_to_direct_visits_with_the_main_site_bar():
	response = routes.live_analysis_page(_request({"sec-fetch-dest": "document"}))
	assert response.status_code == 200
	html = response.body.decode()
	header = html[html.index('<header class="topbar"'):html.index("</header>")]
	assert ">Home</a>" in header and "tab=roadmap-overview" not in header and "siteExperimentalToggle" in header  # Coming soon lives under Home now
	assert "tab-coming-soon" not in header and "tab=soon-themes&amp;group=lab" in header  # the old greyed tab is gone; one Lab link


def test_bare_coming_soon_redirects_to_roadmap():
	for path in ("/coming-soon", "/coming-soon/"):
		response = routes.coming_soon_index()
		assert response.status_code == 307 and response.headers["location"] == "/roadmap"


def test_every_roadmap_item_has_a_tier_a_place_and_a_dependency_line():
	from backend.pages.coming_soon_content import SECTIONS
	from backend.pages.roadmap_page import PLACE, PLACES, TIERS, render, tier_of

	html = render()
	for area in SECTIONS.values():
		for entry in area["items"]:
			assert PLACE[entry[0]] in PLACES and tier_of(entry[0]) in TIERS
			assert f'id="{entry[0]}" data-tier="{tier_of(entry[0])}" data-place="{PLACE[entry[0]]}"' in html
	assert set(PLACE) == {entry[0] for area in SECTIONS.values() for entry in area["items"]}
	assert html.count("<b>Depends on:</b>") >= 56 and html.count("Graded by a model, not a lawyer.") >= 4 and 'id="rmArea"' in html and 'id="glance"' in html


def test_internal_notes_stay_out_of_the_page_and_come_from_an_untracked_file(tmp_path, monkeypatch):
	import json

	from backend.pages import roadmap_page

	assert "PR 4" not in roadmap_page.render()
	monkeypatch.setattr(roadmap_page, "HERE", tmp_path / "backend" / "pages")
	assert roadmap_page.internal_notes() == {}
	(tmp_path / "data").mkdir()
	(tmp_path / "data" / "roadmap_internal.json").write_text(json.dumps({"fingerprints": "note", "bad": 3}), encoding="utf-8")
	assert roadmap_page.internal_notes() == {"fingerprints": "note", "bad": "3"}
	assert routes.roadmap_internal_notes().headers["cache-control"] == "no-store"
