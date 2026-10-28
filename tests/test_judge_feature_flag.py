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
    ids = {s["id"] for s in tour_steps()["steps"]}
    assert "sh-judges" not in ids and "sh-side-judge" not in ids
    monkeypatch.setenv("ILIT_JUDGE_PROFILES", "1")
    assert hide_judge_profiles_in_page(page) == page
    assert "sh-judges" in {s["id"] for s in tour_steps()["steps"]}
