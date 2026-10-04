import json
import re
import subprocess
import sys
from pathlib import Path

from backend.pages.changelog_tab import about_panel_html
from backend.pages.data_explorer import data_explorer_page_html

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "changelog"
sys.path.insert(0, str(ROOT / "scripts"))

import build_changelog  # noqa: E402


def _changelog() -> dict:
	return json.loads((DATA / "changelog.json").read_text(encoding="utf-8"))


def test_changelog_json_is_in_sync_with_its_inputs():
	assert build_changelog.OUT.read_text(encoding="utf-8") == build_changelog.render()


def test_every_merged_pr_has_an_entry_or_a_skip_reason():
	assert [pr["number"] for pr in build_changelog.uncovered_prs()] == []


def test_skip_reasons_are_not_empty():
	skip = json.loads((DATA / "skip.json").read_text(encoding="utf-8"))
	assert all(reason.strip() for reason in skip.values())


def test_entries_are_complete_newest_first_and_use_known_themes():
	data = _changelog()
	themes = {theme["id"] for theme in data["themes"]}
	dates = [entry["date"] for entry in data["entries"]]
	assert dates == sorted(dates, reverse=True)
	assert len(data["entries"]) >= 50
	for entry in data["entries"]:
		assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", entry["date"])
		assert entry["theme"] in themes
		assert entry["title"].strip() and entry["refs"]
		if not entry["auto"]:
			assert entry["text"].strip()


def test_pr_refs_exist_in_the_github_records():
	known = {pr["number"] for pr in json.loads(build_changelog.RECORDS.read_text(encoding="utf-8"))["prs"]}
	cited = {number for entry in _changelog()["entries"] for number in build_changelog._pr_refs(entry["refs"])}
	assert cited <= known


def test_entry_dates_follow_the_merge_date_of_their_prs():
	merged = {pr["number"]: pr["merged_at"][:10] for pr in json.loads(build_changelog.RECORDS.read_text(encoding="utf-8"))["prs"]}
	for entry in _changelog()["entries"]:
		numbers = build_changelog._pr_refs(entry["refs"])
		if numbers:
			assert entry["date"] == max(merged[number] for number in numbers)


def test_uncovered_pr_becomes_an_auto_entry(monkeypatch):
	records = {"prs": [{"number": 9999, "title": "Add colour-blind friendly search chips (#9999)", "merged_at": "2026-10-05T12:00:00Z", "author": "x"}], "commits": []}
	real = build_changelog._load
	monkeypatch.setattr(build_changelog, "_load", lambda path, default: records if path == build_changelog.RECORDS else real(path, default))
	first = build_changelog.build()["entries"][0]
	assert first["auto"] is True and first["date"] == "2026-10-05"
	assert first["title"] == "Add colour-blind friendly search chips" and first["theme"] == "search"


def test_about_page_has_overview_and_changelog_views_without_network_calls():
	html = data_explorer_page_html()
	assert 'data-about-view="overview"' in html and 'data-about-view="changelog"' in html
	assert 'id="changelogData"' in html and 'id="aboutChangelogPane"' in html
	script = re.search(r"<script>\s*\(function\(\)\{\nconst data=JSON.parse.*?</script>", html, re.S).group(0)
	assert "fetch(" not in script


def test_changelog_data_is_an_escaped_attribute_not_a_script():
	import html as html_lib

	html = about_panel_html("<p>overview</p>")
	attribute = re.search(r'id="changelogData" data-json="([^"]*)"', html).group(1)
	assert "<" not in attribute
	assert json.loads(html_lib.unescape(attribute))["entries"]


def test_build_script_check_passes():
	result = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_changelog.py"), "--check"], capture_output=True, text=True)
	assert result.returncode == 0, result.stderr


def test_about_text_has_no_stale_figures():
	text = (ROOT / "backend" / "pages" / "about_content.html").read_text(encoding="utf-8")
	for stale in ("316,940", "61,000", "1.44 M", "183,010", "705 automated", "About 700", "3 of 10", "13,424", "28 Sept 2026"):
		assert stale not in text, stale
	for key in ("cases", "citations", "linked_citations", "fc_activity_cases", "fc_activity_documents"):
		assert f'data-live="{key}"' in text
