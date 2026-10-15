"""Home > About: the one-page introduction that opens the site and the main tour."""

import json
import re
from pathlib import Path

from backend import routes
from backend.pages.pitch_nav import pitch_soon_info

PAGES = Path(__file__).resolve().parents[1] / "backend" / "pages"


def _html() -> str:
    return routes._data_explorer_page_html()


def test_home_is_the_first_tab_with_about_and_coming_soon_sub_tabs():
    html = _html()
    header = html.split('<header class="topbar">', 1)[1].split("</header>", 1)[0]
    assert re.search(r'data-group="info"[^>]*>Home</button>', header)
    assert ">Coming soon</button>" not in header and ">About</button>" not in header
    assert re.search(r'data-nav-group="info" data-tab="about"[^>]*aria-controls="homeAboutPanel"[^>]*>About</button>', html)
    assert re.search(r'data-nav-group="info" data-tab="roadmap-overview"[^>]*>Coming soon</button>', html)
    assert pitch_soon_info()["roadmap-overview"]["group"] == "info"   # the public preview now sits under Home


def test_the_old_about_page_is_kept_under_development():
    html = _html()
    assert re.search(r'data-nav-group="dev" data-tab="dev-about"[^>]*aria-controls="aboutPanel"[^>]*>About \(stored\)</button>', html)
    assert 'id="aboutPanel"' in html and 'id="aboutOverviewPane"' in html and 'id="aboutHowPane"' in html   # stored, not deleted
    assert "activeResearchPanels.about='homeAboutPanel'" in html and "activeResearchPanels['dev-about']='aboutPanel'" in html
    assert "'about-how':'dev-about'" in html   # old How it works addresses open the stored page


def test_home_about_says_what_daniel_approved():
    page = (PAGES / "home_about.html").read_text(encoding="utf-8")
    assert page.count('id="homeAbout"') == 1
    assert "The Immigration Litigation Intelligence Tool (iLIT) is a website built to support the work of the Hearings and Litigation Division of the CBSA." in page
    assert "enhanced version of Canlii" in page and "Each of the 75k decisions in the library has been processed" in page
    assert "not officially affiliated with the Government of Canada" in page
    assert "private website hosted on a personal computer" in page
    assert "Automatic daily updates are not switched on yet" in page                 # the import tools are built, not scheduled
    assert "Federal Court only" in page and "Case A cites Case B at paragraph 84" in page and "Statutes cited" in page
    assert "Case search and reader" in page and "Intelligence" in page and "Workbench" in page
    assert "Where files go" in page and "What happens to those files" not in page   # one graph; the files-by-step funnel is gone
    assert "CanLII" not in page.replace("Canlii", "")                                # no comparison table; only the approved blurb names it
    assert 'data-ilit-tour-start' in page


def test_home_counts_are_read_live_not_typed_in():
    page = (PAGES / "home_about.html").read_text(encoding="utf-8")
    assert "fetch('/api/about/stats')" in page and "fetch('/api/about/library')" in page
    for key in ("cases", "citations", "fcFiles", "fcDecisions"):
        assert f'data-home="{key}"' in page


def test_the_tour_starts_on_home_and_every_home_step_points_at_something_real():
    steps = json.loads((PAGES / "site_tour_steps.json").read_text(encoding="utf-8"))["steps"]
    assert steps[0]["id"] == "tour-welcome" and steps[1]["id"] == "home-what"
    home_ids = [step["id"] for step in steps if step["id"].startswith("home-")]
    assert home_ids == ["home-what", "home-counts", "home-who-what", "home-where-why-how", "home-connects", "home-citations", "home-files", "home-how", "home-parts"]
    assert steps[1 + len(home_ids)]["id"] == "search-page"                            # then the existing tour carries on
    page = (PAGES / "home_about.html").read_text(encoding="utf-8")
    by_id = {step["id"]: step for step in steps}
    for name in home_ids + ["wrap", "done"]:
        selectors = [by_id[name]["target"]] + list(by_id[name].get("span", []))
        for selector in selectors:
            first = selector.split()[0]
            assert first.startswith("#home"), (name, selector)
            assert f'id="{first[1:]}"' in page, (name, selector)
        assert by_id[name]["url"] == "/data-explorer?tab=about"
