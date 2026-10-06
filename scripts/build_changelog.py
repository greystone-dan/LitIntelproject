"""Build the About-page changelog from GitHub records plus hand-written entries.

Inputs (all committed under data/changelog/):
  entries.json         hand-written, plain-language entries. Each one lists the merged PRs ("#216"),
                       commits (short sha) or work-history days it summarises. An entry that cites merged
                       PRs takes the date of the latest one, so dates always match GitHub.
  skip.json            merged PRs deliberately left out (docs-only, CI tweaks, reverts, scratch work), with a reason.
  github_records.json  cache of merged PRs and commits, written by --refresh.
Output: data/changelog/changelog.json, which the About page embeds. Nothing is fetched when the page is viewed.

  python scripts/build_changelog.py             rebuild changelog.json from the committed inputs
  python scripts/build_changelog.py --refresh   first pull merged PRs and commits from GitHub (GITHUB_TOKEN, or the gh CLI)
  python scripts/build_changelog.py --check     exit 1 if changelog.json is out of date (used by tests)
  python scripts/build_changelog.py --uncovered list merged PRs that have no entry and are not skipped

Merged PRs that have no entry and are not skipped still appear, as short "auto" entries built from the PR title,
so a refresh never loses work; write a proper entry for them in entries.json when convenient.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO = "greystone-dan/LitIntelproject"
DATA = Path(__file__).resolve().parents[1] / "data" / "changelog"
ENTRIES, SKIP, RECORDS, OUT = (DATA / name for name in ("entries.json", "skip.json", "github_records.json", "changelog.json"))

THEMES = [
	("navigation", "Navigation"),
	("search", "Search"),
	("reader", "Case reader"),
	("markup", "Markup mode"),
	("tagging", "Tagging and themes"),
	("outcomes", "Outcomes"),
	("judges", "Judges"),
	("citations", "Citations"),
	("statutes", "Statutes"),
	("federal-court", "Federal Court files"),
	("library", "Library and data"),
	("performance", "Performance"),
	("mobile", "Phone layout"),
	("security", "Privacy and security"),
	("infrastructure", "Running the site"),
	("docs", "Documentation"),
]
THEME_IDS = {key for key, _ in THEMES}
# Keyword guess for auto entries only; hand-written entries name their theme.
_GUESS = [
	("markup", "markup"), ("phone", "mobile"), ("mobile", "mobile"), ("outcome", "outcomes"), ("judge", "judges"),
	("tag", "tagging"), ("theme", "tagging"), ("statute", "statutes"), ("citation", "citations"), ("docket", "federal-court"),
	("federal court", "federal-court"), ("search", "search"), ("reader", "reader"), ("cache", "performance"),
	("faster", "performance"), ("security", "security"), ("password", "security"), ("privacy", "security"),
	("doc", "docs"), ("import", "library"),
]


def _get(url: str) -> list:
	token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
	if token:
		request = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"})
		with urllib.request.urlopen(request, timeout=60) as response:  # noqa: S310 - fixed https GitHub API URL
			return json.load(response)
	result = subprocess.run(["gh", "api", url.removeprefix("https://api.github.com/")], capture_output=True, text=True, check=True)
	return json.loads(result.stdout)


def _paged(path: str) -> list:
	rows, page = [], 1
	while True:
		chunk = _get(f"https://api.github.com/repos/{REPO}/{path}{'&' if '?' in path else '?'}per_page=100&page={page}")
		rows += chunk
		if len(chunk) < 100:
			return rows
		page += 1


def refresh() -> None:
	prs = [
		{"number": pr["number"], "title": pr["title"], "merged_at": pr["merged_at"], "author": pr["user"]["login"]}
		for pr in _paged("pulls?state=closed") if pr.get("merged_at")
	]
	commits = [
		{"sha": c["sha"][:7], "date": c["commit"]["author"]["date"][:10], "subject": c["commit"]["message"].splitlines()[0]}
		for c in _paged("commits")
	]
	prs.sort(key=lambda p: p["number"])
	commits.sort(key=lambda c: (c["date"], c["sha"]))
	RECORDS.write_text(json.dumps({"repo": REPO, "prs": prs, "commits": commits}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def _load(path: Path, default):
	return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def _pr_refs(refs: list[str]) -> list[int]:
	return [int(ref[1:]) for ref in refs if re.fullmatch(r"#\d+", ref)]


def covered(entries: list[dict], skip: dict) -> set[int]:
	numbers = {number for entry in entries for number in _pr_refs(entry["refs"])}
	return numbers | {int(key.lstrip("#")) for key in skip}


def uncovered_prs() -> list[dict]:
	records = _load(RECORDS, {"prs": []})
	done = covered(_load(ENTRIES, []), _load(SKIP, {}))
	return [pr for pr in records["prs"] if pr["number"] not in done]


def build() -> dict:
	records = _load(RECORDS, {"prs": [], "commits": []})
	merged = {pr["number"]: pr["merged_at"][:10] for pr in records["prs"]}
	entries = []
	for raw in _load(ENTRIES, []):
		entry = {**raw, "auto": False}
		if entry["theme"] not in THEME_IDS:
			raise SystemExit(f"Unknown theme {entry['theme']!r} in entry {entry['title']!r}")
		dates = [merged[n] for n in _pr_refs(entry["refs"]) if n in merged]
		if dates:
			entry["date"] = max(dates)
		entries.append(entry)
	for pr in uncovered_prs():
		title = re.sub(r"^\W+|\s*\(#\d+\)$", "", pr["title"]).strip() or f"Change #{pr['number']}"
		lowered = title.lower()
		theme = next((theme for word, theme in _GUESS if word in lowered), "infrastructure")
		entries.append({"date": pr["merged_at"][:10], "theme": theme, "title": title, "text": "", "refs": [f"#{pr['number']}"], "auto": True})
	# Newest first; within a day the highest PR number (latest merged) comes first.
	entries.sort(key=lambda e: (e["date"], max(_pr_refs(e["refs"]), default=0), e["title"]), reverse=True)
	return {"repo": REPO, "themes": [{"id": key, "label": label} for key, label in THEMES], "entries": entries}


def render() -> str:
	return json.dumps(build(), indent=1, ensure_ascii=False) + "\n"


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--refresh", action="store_true", help="pull merged PRs and commits from GitHub first")
	parser.add_argument("--check", action="store_true", help="fail if changelog.json is out of date")
	parser.add_argument("--uncovered", action="store_true", help="list merged PRs with no entry and no skip reason")
	args = parser.parse_args()
	if args.refresh:
		refresh()
	if args.uncovered:
		for pr in uncovered_prs():
			print(f"#{pr['number']} {pr['merged_at'][:10]} {pr['title']}")
		return 0
	if args.check:
		if not OUT.exists() or OUT.read_text(encoding="utf-8") != render():
			print("data/changelog/changelog.json is out of date; run python scripts/build_changelog.py", file=sys.stderr)
			return 1
		return 0
	OUT.write_text(render(), encoding="utf-8")
	print(f"Wrote {OUT.relative_to(DATA.parents[1])}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
