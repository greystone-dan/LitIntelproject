"""Check the site tour in a real browser: every step's target must resolve, and the controls must work.

Needs Playwright with Chromium and a running copy of the site.

    python scripts/check_site_tour.py --base-url http://localhost:8001 --walk --shots /tmp/tour-shots
    python scripts/check_site_tour.py --base-url http://localhost:8001 --walk --require-data   # on the PC that serves the site
    python scripts/check_site_tour.py --steps-only      # only validate site_tour_steps.json (no browser)

--walk takes the tour as a visitor does (start on About, press only Next) and prints, for each step, the
milliseconds from pressing Next to the card being ready, any step that was skipped, and any highlight that is
off screen or hidden behind the card. Like a visitor's tour it signs in to the Workbench demo and pins the
example decisions. Without --walk (or with --each) every step is also opened on its own, as after a refresh;
that mode is read-only unless --demo-sign-in is given.

A step marked optional, or one that names a feature in "needs", may be skipped without failing the check;
every other step must show its card on the page it names. Exit code 1 if any required step failed, a highlight
was off screen, or the page raised an error.
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
ACTIONS = {"type", "fill", "check", "uncheck", "open", "click", "submit", "scroll", "waitFor", "wait", "drop"}


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

        def selector_ok(item) -> bool:
            return isinstance(item, str) or (isinstance(item, dict) and isinstance(item.get("css"), str))

        if target is not None and not (selector_ok(target) or (isinstance(target, list) and target and all(selector_ok(t) for t in target))):
            problems.append(f"{label}: target must be a selector or a list of selectors")
        for extra in step.get("also", []):
            sel = extra.get("sel") if isinstance(extra, dict) and "sel" in extra else extra
            if not (selector_ok(sel) or (isinstance(sel, list) and sel and all(selector_ok(t) for t in sel))):
                problems.append(f"{label}: each 'also' entry must be a selector or {{sel, label}}")
        for key in ("via", "point", "lead"):
            if step.get(key) is not None and not isinstance(step[key], str):
                problems.append(f"{label}: {key} must be a string")
        for action in step.get("before", []):
            if action.get("do") not in ACTIONS:
                problems.append(f"{label}: unknown action {action.get('do')!r}")
            if action.get("do") != "wait" and not action.get("selector"):
                problems.append(f"{label}: action without a selector")
            if action.get("do") == "fill" and action.get("sample") not in (data.get("texts") or {}):
                problems.append(f"{label}: fill names an unknown sample text")
            if action.get("do") == "drop" and not str(action.get("file", "")).startswith("/site-tour/"):
                problems.append(f"{label}: drop must name one of the tour's own sample files (/site-tour/...)")
        for button in step.get("buttons", []):
            if not button.get("label") or not button.get("click"):
                problems.append(f"{label}: button needs a label and a click selector")
            if not button.get("writes"):
                problems.append(f"{label}: a step button must say what it writes (writes)")
    for probe in data.get("probes") or []:
        if not (str(probe.get("url", "")).startswith("/") and isinstance(probe.get("min"), int)):
            problems.append(f"probe {probe.get('id', '?')}: needs a url path and an integer min")
    return problems


def run_probes(base: str) -> int:
    """Search the example data the tour relies on (read-only GETs). Returns how many came back short."""
    import urllib.request

    short = 0
    for probe in json.loads(STEPS_FILE.read_text(encoding="utf-8")).get("probes") or []:
        try:
            request = urllib.request.Request(base + probe["url"], headers={"User-Agent": "Mozilla/5.0 (iLit tour check)"})
            with urllib.request.urlopen(request, timeout=60) as response:
                count = len(json.load(response).get(probe.get("key", "results"), []))
        except Exception as error:  # noqa: BLE001
            count, note = -1, f" ({str(error)[:60]})"
        else:
            note = ""
        verdict = "ok" if count >= probe["min"] else "NO DATA"
        short += verdict != "ok"
        print(f"probe {probe['id']:<32} {count:>3} results  {verdict}{note}  - {probe.get('note', '')}")
    return short


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


def run_browser(base: str, shots: Path | None, shot_ids: set[str], width: int, demo: bool, require_data: bool) -> int:
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
                elif step.get("needsData") and not page.evaluate(
                    "() => /[1-9]/.test(document.querySelector('#fcxKpis')?.innerText || '')"
                ):
                    status = "empty"
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
            ok = status == "ok" or (status == "skipped" and relaxed) or (status == "empty" and not require_data)
            if not ok:
                failures += 1
            rows.append((index + 1, step["id"], status + (" [relaxed]" if status == "skipped" and relaxed else "")))
            context.close()
        browser.close()
    for number, step_id, status in rows:
        print(f"{number:>2}  {step_id:<24} {status}")
    return failures


RING_REPORT = """() => {
  const vh = innerHeight, card = document.querySelector('.ilit-tour-card');
  const c = card ? card.getBoundingClientRect() : null, sheet = card && card.classList.contains('sheet');
  return [...document.querySelectorAll('.ilit-tour-ring')].filter(r => r.style.display !== 'none').map(r => {
    const b = r.getBoundingClientRect(), tag = null;
    const covered = c ? Math.max(0, Math.min(b.bottom, c.bottom) - Math.max(b.top, c.top)) * Math.max(0, Math.min(b.right, c.right) - Math.max(b.left, c.left)) : 0;
    return {label: tag && !tag.hidden ? tag.textContent : '', top: b.top, bottom: b.bottom, h: b.height, w: b.width,
            shown: Math.max(0, Math.min(b.bottom, sheet ? c.top : vh) - Math.max(b.top, 0)), covered: covered / Math.max(1, b.width * b.height)};
  });
}"""


def run_walk(base: str, width: int, shots: Path | None, require_data: bool = False) -> int:
    """Take the tour the way a visitor does: start on About and press only Next, timing each step.

    The tour signs in to the Workbench demo and pins decisions as it goes (the same writes a visitor's tour makes).
    Reports per step: how long it took after Next, whether it was skipped, and whether every highlight is on screen."""
    from playwright.sync_api import sync_playwright

    steps = json.loads(STEPS_FILE.read_text(encoding="utf-8"))["steps"]
    by_id = {step["id"]: step for step in steps}
    problems = 0
    seen: list[str] = []
    with sync_playwright() as pw:
        browser = launch(pw)
        context = browser.new_context(viewport={"width": width, "height": 900 if width > 700 else 800})
        page = context.new_page()
        errors: list[str] = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(base + "/data-explorer?tab=about", wait_until="domcontentloaded", timeout=60000)
        page.click("[data-ilit-tour-start]")
        print(f"{'#':>2}  {'step':<22} {'ms':>6}  {'scroll':>6}  highlights")
        last_page, last_y = "", 0
        for _ in range(len(steps) + 5):
            try:
                page.wait_for_selector(".ilit-tour-card:not(.pending)[data-ms]", timeout=60000)
            except Exception:  # noqa: BLE001
                if not page.locator(".ilit-tour").count():
                    break
                print("    stuck: the card never finished loading")
                problems += 1
                break
            page.wait_for_timeout(350)                         # let the rings settle after the scroll
            step_id = page.get_attribute(".ilit-tour-card", "data-step")
            ms = int(page.get_attribute(".ilit-tour-card", "data-ms") or 0)
            rings = page.evaluate(RING_REPORT)
            notes = []
            for ring in rings:
                name = ring["label"] or "target"
                if ring["shown"] < min(40, ring["h"] * 0.9):
                    notes.append(f"{name} OFF SCREEN")
                elif ring["covered"] > 0.5 and ring["h"] < 300:
                    notes.append(f"{name} under the card")
            main_lit = page.evaluate(
                "n => { const r = document.querySelectorAll('.ilit-tour-rings > .ilit-tour-ring')[n]; return !!r && r.style.display !== 'none' }",
                by_id.get(step_id, {}).get("focus", 0),
            )
            if by_id.get(step_id, {}).get("target") and not main_lit:
                notes.append("main highlight NOT SHOWN")
            if by_id.get(step_id, {}).get("needsData") and not page.evaluate(
                "() => /[1-9]/.test(document.querySelector('#fcxKpis')?.innerText || '')"
            ):
                notes.append("statistics EMPTY")
            if step_id == "reader-citation-card" and page.evaluate(
                "() => /has not matched|no pinpoint/i.test(document.querySelector('.v6-card2:not(.v6-para)')?.innerText || '')"
            ):
                notes.append("citation card has NO PINPOINT")
            index = next((k for k, step in enumerate(steps) if step["id"] == step_id), -1)
            expected = steps[len(seen)]["id"] if len(seen) < len(steps) else None
            while expected and expected != step_id and expected in by_id and len(seen) < len(steps):
                relaxed = by_id[expected].get("optional") or by_id[expected].get("needs")
                print(f"{len(seen) + 1:>2}  {expected:<22} {'':>6}  SKIPPED{' [relaxed]' if relaxed else ''}")
                problems += 0 if relaxed else 1
                seen.append(expected)
                expected = steps[len(seen)]["id"] if len(seen) < len(steps) else None
            seen.append(step_id)
            slow = " SLOW" if ms > 6000 else ""
            here, y = page.evaluate("() => [location.pathname + location.search, Math.round(scrollY)]")
            moved = abs(y - last_y) if here == last_page else 0      # how far the page scrolled under the visitor
            last_page, last_y = here, y
            print(f"{index + 1:>2}  {step_id:<22} {ms:>6}{slow}  {moved:>6}  {len(rings)} lit{'; ' + '; '.join(notes) if notes else ''}")
            problems += len([note for note in notes if note not in ("statistics EMPTY", "citation card has NO PINPOINT") or require_data])
            if shots:
                shots.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(shots / f"{index + 1:02d}-{step_id}{'-phone' if width < 700 else ''}.png"))
            if step_id == steps[-1]["id"]:
                break
            page.click(".ilit-tour-btn.primary")
        if errors:
            print("page error:", errors[0][:200])
            problems += 1
        browser.close()
    return problems


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
    parser.add_argument("--require-data", action="store_true", help="fail when example data is missing (probes short, statistics empty); use on the real library")
    parser.add_argument("--steps-only", action="store_true")
    parser.add_argument("--walk", action="store_true", help="take the whole tour pressing only Next, with timings (makes the tour's demo writes)")
    parser.add_argument("--each", action="store_true", help="also open every step on its own, as after a refresh")
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
    short = run_probes(base)
    failures = run_controls(base, args.width)
    if args.walk:
        failures += run_walk(base, args.width, args.shots, args.require_data)
    if args.each or not args.walk:
        failures += run_browser(base, args.shots if not args.walk else None, shot_ids, args.width, args.demo_sign_in, args.require_data)
    if args.require_data:
        failures += short
    print("FAILED" if failures else "all steps resolve")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
