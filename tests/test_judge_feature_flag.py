from fastapi.testclient import TestClient

from backend.judge_feature import hide_judge_profiles_in_page, is_hidden_judge_path
from backend.main import app
from backend.site_tour import tour_steps

HIDDEN = [
    "/api/judge-profiles",
    "/api/judge-profiles/judge-zinn",
    "/api/judge-profiles/judge-zinn/issues",
    "/judges",
    "/judges/judge-zinn",
    "/judges/compare",
    "/api/fc-activity/judges",
    "/api/citation-intelligence/35874/judges",
]


def test_paths_match_only_judge_profile_routes():
    assert all(is_hidden_judge_path(p) for p in HIDDEN)
    assert not is_hidden_judge_path("/api/fc-activity/dashboard")
    assert not is_hidden_judge_path("/analytics/search/cases")


def test_routes_404_when_hidden_and_pass_through_when_on(monkeypatch):
    client = TestClient(app, follow_redirects=False)
    monkeypatch.delenv("ILIT_JUDGE_PROFILES", raising=False)
    for path in HIDDEN:
        assert client.get(path).status_code == 404, path
    monkeypatch.setenv("ILIT_JUDGE_PROFILES", "1")
    assert client.get("/judges").status_code == 307


def test_page_hides_tab_and_tour_steps(monkeypatch):
    page = '<html><head></head><body><button data-tab="judge-profile">Judge Profiles</button>intel:\'judge-profile\'</body></html>'
    monkeypatch.delenv("ILIT_JUDGE_PROFILES", raising=False)
    hidden = hide_judge_profiles_in_page(page)
    assert 'data-tab="judge-profile">Judge' not in hidden and "judgeFeatureOff" in hidden
    tour_steps.cache_clear()
    ids = {s["id"] for s in tour_steps()["steps"]}
    assert "sh-judges" not in ids and "sh-side-judge" not in ids
    monkeypatch.setenv("ILIT_JUDGE_PROFILES", "1")
    assert hide_judge_profiles_in_page(page) == page
    tour_steps.cache_clear()
    assert "sh-judges" in {s["id"] for s in tour_steps()["steps"]}
    tour_steps.cache_clear()


def test_recorded_tour_drops_judge_steps_and_renumbers(monkeypatch):
    import json
    from backend.judge_feature import filter_window_data
    from backend.tour_window import _ASSETS

    data = json.loads((_ASSETS / "tour_data.json").read_text(encoding="utf-8"))
    monkeypatch.delenv("ILIT_JUDGE_PROFILES", raising=False)
    out = filter_window_data(data)
    ids = [m["id"] for m in out["moments"]]
    assert not {"sh-side-judge", "sh-judges", "sh-judge-open", "sh-judge-charts"} & set(ids)
    assert [m["step"] for m in out["moments"]] == list(range(1, len(ids) + 1))
    assert "Judge Profiles" not in json.dumps(out["moments"][13]["text"])
    monkeypatch.setenv("ILIT_JUDGE_PROFILES", "1")
    assert filter_window_data(data) is data
