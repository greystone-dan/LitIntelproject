"""Check the site tour in a real browser: every step's target must resolve, and the controls must work.

Needs Playwright with Chromium and a running copy of the site. Read-only: it never clicks a step button
that writes (the Workbench demo sign-in), so it is safe to point at the live site.

    python scripts/check_site_tour.py --base-url http://localhost:8001
    python scripts/check_site_tour.py --base-url https://www.ilit.ca --shots /tmp/tour-shots
    python scripts/check_site_tour.py --steps-only      # only validate site_tour_steps.json (no browser)

A step marked optional, or one that names a feature in "needs", may be skipped without failing the check;
every other step must show its card on the page it names. Exit code 1 if any required step failed or the
page raised an error.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STEPS_FILE = ROOT / "backend" / "pages" / "site_tour_steps.json"
ACTIONS = {"type", "check", "uncheck", "click", "submit", "scroll", "waitFor"}


def validate_steps(data: dict) -> list[str]:
    """Structural checks that need no browser."""
    problems: list[str] = []
    steps = data.get("steps") or []
    cases = data.get("cases") or {}
    if not steps:
        problems.append("no steps")
    seen: set[str] = set()
    for index, step in enumerate(steps, 1):
        label = f"step {index} ({step.get('id', '?')})"
        for key in ("id", "section", "url", "title", "text"):
            if not step.get(key):
                problems.append(f"{label}: missing {key}")
        if step.get("id") in seen:
            problems.append(f"{label}: duplicate id")
        seen.add(step.get("id"))
        if not str(step.get("url", "")).startswith("/"):
            problems.append(f"{label}: url must be a path on this site")
        for name in re.findall(r"\{(\w+)\}", step.get("url", "")):
            if name not in cases:
                problems.append(f"{label}: url names unknown case '{name}'")
        target = step.get("target")
        if target is not None and not (isinstance(target, str) or (isinstance(target, list) and target and all(isinstance(t, str) for t in target))):
            problems.append(f"{label}: target must be a selector or a list of selectors")
        for action in step.get("before", []):
            if action.get("do") not in ACTIONS:
                problems.append(f"{label}: unknown action {action.get('do')!r}")
            if not action.get("selector"):
                problems.append(f"{label}: action without a selector")
        for button in step.get("buttons", []):
            if not button.get("label") or not button.get("click"):
                problems.append(f"{label}: button needs a label and a click selector")
            if not button.get("writes"):
                problems.append(f"{label}: a step button must say what it writes (writes)")
    return problems


def launch(playwright):
    options = {"args": ["--no-sandbox"]}
    for candidate in (os.environ.get("CHROMIUM_PATH"), "/opt/pw-browsers/chromium"):
        if candidate and Path(candidate).exists():
            return playwright.chromium.launch(executable_path=candidate, **options)
    return playwright.chromium.launch(**options)


def sign_in(context, base: str) -> None:
    """Demo sign-in for the Workbench steps. This WRITES a demo user to the site, so it is opt-in."""
    response = context.request.post(base + "/workbench/api/signin", data=json.dumps({"name": "Tour check"}), headers={"Content-Type": "application/json"})
    if not response.ok:
        print(f"demo sign-in failed ({response.status}); Workbench steps will be skipped")


def run_browser(base: str, shots: Path | None, shot_ids: set[str], width: int, demo: bool) -> int:
    from playwright.sync_api import sync_playwright

    data = json.loads(STEPS_FILE.read_text(encoding="utf-8"))
    steps = data["steps"]
    failures = 0
    rows = []
    with sync_playwright() as pw:
        browser = launch(pw)
        for index, step in enumerate(steps):
            context = browser.new_context(viewport={"width": width, "height": 900 if width > 700 else 800})
            if demo:
                sign_in(context, base)
            page = context.new_page()
            errors: list[str] = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.add_init_script(
                "if(!sessionStorage.getItem('ilit.tour.v1'))sessionStorage.setItem('ilit.tour.v1',JSON.stringify({i:%d,active:true,dir:1}))" % index
            )
            status = "ok"
            try:
                page.goto(base + "/data-explorer?tab=about", wait_until="domcontentloaded", timeout=60000)
                # The tour opens the step's own page and waits for its target; give a slow search time to answer.
                wait_ms = int((step.get("timeout") or 8) * 1000) + 30000
                page.wait_for_function(
                    """i => {
                      const s = JSON.parse(sessionStorage.getItem('ilit.tour.v1') || 'null');
                      const card = document.querySelector('.ilit-tour-card');
                      if (!s || !s.active) return true;
                      if (s.i !== i) return true;
                      return !!card && !card.classList.contains('pending');
                    }""",
                    arg=index,
                    timeout=wait_ms,
                )
                page.wait_for_timeout(500)
                state = page.evaluate("JSON.parse(sessionStorage.getItem('ilit.tour.v1') || 'null')")
                shown = bool(state and state.get("active") and state.get("i") == index and page.locator(".ilit-tour-card").count())
                if not shown:
                    status = "skipped"
                elif step.get("target"):
                    inside = page.evaluate(
                        "() => { const r = document.querySelector('.ilit-tour-ring'); return r && getComputedStyle(r).display !== 'none' && r.getBoundingClientRect().width > 0 }"
                    )
                    if not inside:
                        status = "no-highlight"
                if shown and shots and step["id"] in shot_ids:
                    shots.mkdir(parents=True, exist_ok=True)
                    page.screenshot(path=str(shots / f"{index + 1:02d}-{step['id']}{'-phone' if width < 700 else ''}.png"))
            except Exception as error:  # noqa: BLE001 - report and carry on with the next step
                status = f"error: {str(error).splitlines()[0][:90]}"
            relaxed = bool(step.get("optional") or step.get("needs"))
            if errors:
                status += f" (page error: {errors[0][:80]})"
            ok = status == "ok" or (status == "skipped" and relaxed)
            if not ok:
                failures += 1
            rows.append((index + 1, step["id"], status + (" [relaxed]" if status == "skipped" and relaxed else "")))
            context.close()
        browser.close()
    for number, step_id, status in rows:
        print(f"{number:>2}  {step_id:<24} {status}")
    return failures


def run_controls(base: str, width: int) -> int:
    """Walk the controls: start from About, Next/Back/Skip, refresh keeps the place, Exit clears it."""
    from playwright.sync_api import sync_playwright

    problems: list[str] = []
    with sync_playwright() as pw:
        browser = launch(pw)
        context = browser.new_context(viewport={"width": width, "height": 900 if width > 700 else 800})
        page = context.new_page()
        errors: list[str] = []
        page.on("pageerror", lambda error: errors.append(str(error)))

        def counter() -> str:
            page.wait_for_selector(".ilit-tour-card:not(.pending) .ilit-tour-count", timeout=45000)
            return page.locator(".ilit-tour-count").inner_text()

        page.goto(base + "/data-explorer?tab=about", wait_until="domcontentloaded", timeout=60000)
        page.click("[data-ilit-tour-start]")
        first = counter()
        page.keyboard.press("ArrowRight")
        page.wait_for_function("document.querySelector('.ilit-tour-count')&&!document.querySelector('.ilit-tour-count').textContent.startsWith('Step 1 ')", timeout=45000)
        second = counter()
        if first == second:
            problems.append("Next did not advance")
        page.click(".ilit-tour-btn:has-text('Back')")
        page.wait_for_function("document.querySelector('.ilit-tour-count')&&document.querySelector('.ilit-tour-count').textContent.startsWith('Step 1 ')", timeout=45000)
        page.reload(wait_until="domcontentloaded")
        if not counter().startswith("Step 1 "):
            problems.append("a refresh lost the place")
        page.click(".ilit-tour-btn:has-text('Skip section')")
        after_skip = counter()
        if after_skip.startswith("Step 1 ") or after_skip.startswith("Step 2 "):
            problems.append(f"Skip section did not leave the section ({after_skip})")
        page.keyboard.press("Escape")
        page.wait_for_timeout(300)
        if page.locator(".ilit-tour").count() or page.evaluate("sessionStorage.getItem('ilit.tour.v1')"):
            problems.append("Exit did not clear the tour")
        if errors:
            problems.append("page error: " + errors[0])
        browser.close()
    for problem in problems:
        print("CONTROLS FAIL:", problem)
    if not problems:
        print("controls: start, Next, Back, refresh, Skip section, Exit all work")
    return len(problems)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base-url", default="http://localhost:8001")
    parser.add_argument("--shots", type=Path, help="folder for screenshots")
    parser.add_argument("--shot-ids", default="", help="comma list of step ids to photograph (default: all, when --shots is set)")
    parser.add_argument("--width", type=int, default=1280, help="viewport width (390 for a phone)")
    parser.add_argument("--demo-sign-in", action="store_true", help="sign in to the Workbench demo first (writes a demo user; leave off for the live site)")
    parser.add_argument("--steps-only", action="store_true")
    args = parser.parse_args()

    problems = validate_steps(json.loads(STEPS_FILE.read_text(encoding="utf-8")))
    for problem in problems:
        print("STEPS FAIL:", problem)
    if problems or args.steps_only:
        print("steps file: " + ("problems found" if problems else "ok"))
        return 1 if problems else 0
    base = args.base_url.rstrip("/")
    shot_ids = {s for s in args.shot_ids.split(",") if s}
    if args.shots and not shot_ids:
        shot_ids = {step["id"] for step in json.loads(STEPS_FILE.read_text(encoding="utf-8"))["steps"]}
    failures = run_browser(base, args.shots, shot_ids, args.width, args.demo_sign_in) + run_controls(base, args.width)
    print("FAILED" if failures else "all steps resolve")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
