"""Check the site tour in a real browser: every step's target must resolve, and the controls must work.

Needs Playwright with Chromium and a running copy of the site.

    python scripts/check_site_tour.py --base-url http://localhost:8001 --walk --shots /tmp/tour-shots
    python scripts/check_site_tour.py --base-url http://localhost:8001 --walk --require-data   # on the PC that serves the site
    python scripts/check_site_tour.py --walk --sizes 1440x900,1920x1080 --shots /tmp/tour-shots   # geometry at both desktop sizes
    python scripts/check_site_tour.py --steps-only      # only validate site_tour_steps.json (no browser)
    python scripts/check_site_tour.py --pick-case       # read-only: which cessation decision the tour should open

--walk takes the tour as a visitor does (start on About, press only Next) and prints, for each step, the
milliseconds from pressing Next to the card being ready, any step that was skipped, and, at every card, the
geometric checks in geometry_problems(): each ring goes right round its element, the card covers no lit element,
stays on screen and does not jump when its last place was still clear, and the pointer is never on the card.
Like a visitor's tour it signs in to the Workbench demo and pins the example decisions. Without --walk (or with --each) every step is also opened on its own, as after a refresh;
that mode is read-only unless --demo-sign-in is given.

A step marked optional, or one that names a feature in "needs", may be skipped without failing the check;
every other step must show its card on the page it names. Exit code 1 if any required step failed, a geometric
check failed, or the page raised an error.
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
ACTIONS = {"type", "fill", "check", "uncheck", "open", "click", "submit", "waitFor", "wait", "drop", "hover", "glide"}


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
        if step.get("span") is not None and not (isinstance(step["span"], list) and all(isinstance(t, str) for t in step["span"])):
            problems.append(f"{label}: span must be a list of selectors")

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
        if step.get("act") and not step.get("say"):
            problems.append(f"{label}: a step that acts must first say what it will do (say)")
        if step.get("say") and not step.get("act"):
            problems.append(f"{label}: say is only for a step that acts")
        if (step.get("via") or step.get("point")) and not step.get("lead"):
            problems.append(f"{label}: via or point needs a lead line")
        for action in step.get("before", []) + step.get("act", []):
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
    import urllib.parse
    import urllib.request

    short = 0
    data = json.loads(STEPS_FILE.read_text(encoding="utf-8"))
    cases = data.get("cases") or {}

    def case_id(name: str) -> str:                       # a {name} in a probe URL is that tour case, found by citation
        want = re.sub(r"\s+", " ", cases[name]["citation"]).lower()
        found = _get_json(base, "/analytics/search/cases?" + urllib.parse.urlencode({"query": cases[name]["citation"], "limit": 8, "facets": 0}))
        return next((str(r["case_id"]) for r in found.get("results") or [] if want in str(r.get("citation")).lower()), "0")

    for probe in data.get("probes") or []:
        first = ""
        try:
            url = re.sub(r"\{(\w+)\}", lambda m: case_id(m.group(1)), probe["url"])
            request = urllib.request.Request(base + url, headers={"User-Agent": "Mozilla/5.0 (iLit tour check)"})
            with urllib.request.urlopen(request, timeout=60) as response:
                rows = json.load(response).get(probe.get("key", "results"), [])
            count = len(rows)
            first = str(rows[0].get("citation")) if rows and isinstance(rows[0], dict) else ""
        except Exception as error:  # noqa: BLE001
            count, note = -1, f" ({str(error)[:60]})"
        else:
            note = ""
        verdict = "ok" if count >= probe["min"] else "NO DATA"
        if verdict == "ok" and probe.get("first"):          # this case must head the list
            if cases[probe["first"]]["citation"] not in first:
                verdict, note = "WRONG FIRST", f" (first is {first or 'nothing'})"
        short += verdict != "ok"
        print(f"probe {probe['id']:<32} {count:>3} results  {verdict}{note}  - {probe.get('note', '')}")
    return short


PICK_SEARCH = "/analytics/search/cases?tags=cessation%2Cindia&cites_case_id={vavilov}&government_outcome=won&case_type=refugee_cessation&limit=25&facets=0"   # only real cessation decisions (tags alone also match other kinds)


def _get_json(base: str, path: str):
    import urllib.request

    request = urllib.request.Request(base + path, headers={"User-Agent": "Mozilla/5.0 (iLit tour check)"})
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.load(response)


def pick_example_case(base: str) -> int:
    """Read-only: rank the decisions the tour's filtered search returns (tags cessation and india, citing Vavilov,
    Government won) by how well each shows off the reader: a long outline, a citation matched to a library case at
    a paragraph, a statute reference, a judge, and decisions that cite it. Prints the table and the best citation."""
    found = _get_json(base, "/analytics/search/cases?query=2019%20SCC%2065&limit=5&facets=0").get("results") or []
    vavilov = next((row["case_id"] for row in found if "2019 SCC 65" in str(row.get("citation"))), None)
    if vavilov is None:
        print("Vavilov (2019 SCC 65) is not in this library")
        return 1
    rows = _get_json(base, PICK_SEARCH.format(vavilov=vavilov)).get("results") or []
    print(f"{len(rows)} decisions match the tour's search")
    ranked = []
    for rank, row in enumerate(rows, 1):
        try:
            reader = _get_json(base, f"/cases/{row['case_id']}/reader-data")
            statutes = _get_json(base, f"/cases/{row['case_id']}/statute-references")
        except Exception as error:  # noqa: BLE001
            print(f"  {row.get('citation')}: reader failed ({str(error)[:60]})")
            continue
        outline = len(reader.get("structure_outline") or [])
        pins = sum(1 for c in reader.get("citations") or [] if c.get("target_case_id") and c.get("target_paragraph") is not None and c.get("citation_kind") != "statute")
        acts = sum(1 for c in statutes or [] if c.get("instrument_key") or c.get("legislation_url"))
        cited_by = int((reader.get("metrics") or {}).get("in_degree") or row.get("cited_by_cases") or 0)
        judge = bool(row.get("judge"))
        usable = outline >= 4 and pins >= 1 and acts >= 1 and judge and cited_by >= 1   # the tour shows how it has been cited
        score = (100 if usable else 0) + min(outline, 10) * 3 + min(pins, 5) * 2 + min(cited_by, 20) * 2 - rank
        ranked.append((score, rank, row, outline, pins, acts, cited_by, judge, usable))
    ranked.sort(key=lambda item: -item[0])
    print(f"{'score':>5} {'rank':>4}  {'citation':<16} {'outline':>7} {'pinpoints':>9} {'statutes':>8} {'cited by':>8}  judge  title")
    for score, rank, row, outline, pins, acts, cited_by, judge, usable in ranked:
        print(f"{score:>5} {rank:>4}  {str(row.get('citation')):<16} {outline:>7} {pins:>9} {acts:>8} {cited_by:>8}  {'yes' if judge else 'no ':<5}  {str(row.get('title'))[:60]}{'' if usable else '  (not usable)'}")
    best = next((item for item in ranked if item[8]), None)
    if not best:
        print("no decision has an outline, a pinpoint citation, a statute, a judge and a citing decision")
        return 1
    print(f"BEST: {best[2].get('citation')} (case {best[2]['case_id']}): {best[2].get('title')}")
    return 0


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
                "if(!sessionStorage.getItem('ilit.tour.v1'))sessionStorage.setItem('ilit.tour.v1',JSON.stringify({i:%d,active:true,dir:1,phase:'show'}))" % index
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


def _overlap(a: dict | None, b: dict | None) -> float:
    if not a or not b:
        return 0.0
    w = min(a["x"] + a["w"], b["x"] + b["w"]) - max(a["x"], b["x"])
    h = min(a["y"] + a["h"], b["y"] + b["h"]) - max(a["y"], b["y"])
    return max(0.0, w) * max(0.0, h)


def _fits(card: dict, g: dict) -> bool:
    """The card lies inside the window and clear of the control bar."""
    dock = g.get("dock")
    inside = card["x"] >= -1 and card["y"] >= -1 and card["x"] + card["w"] <= g["vw"] + 1 and card["y"] + card["h"] <= g["vh"] + 1
    return inside and not _overlap(card, dock)


def _clear_place(card: dict, g: dict) -> bool:
    """Is there any place on the screen where the card would cover no ring? (If not, covering one is unavoidable.)"""
    rings = [item["ring"] for item in g.get("items") or [] if item.get("ring")]
    floor = g["dock"]["y"] if g.get("dock") else g["vh"]
    for x in range(14, max(15, g["vw"] - int(card["w"]) - 13), 20):
        for y in range(14, max(15, int(floor - card["h"]) - 13), 20):
            spot = dict(card, x=x, y=y)
            if not any(_overlap(spot, ring) for ring in rings):
                return True
    return False


GEOMETRY_SLACK = 2       # px: rounding and sub-pixel borders
CARD_STILL = 24          # px: a card that moves less than this has not moved
CARD_NEAR = 360          # px: a card further than this from its region should move closer (the engine's NEAR)


def geometry_problems(g: dict | None, previous_card: dict | None = None) -> list[str]:
    """What looks wrong in one settled moment of the tour (the dict ilitTour.geometry() returns).

    - every lit element has a ring that goes right round it (none of it cut off by the screen, a panel or the bar);
      one taller than the screen or its panel can show is ringed from its top, across its width, down the screen;
    - the card stays on the screen, off the control bar, and covers no lit element (nor, when it has room elsewhere,
      the site header or a bar pinned at the top of the screen);
    - the pointer, when it shows, is not on the card;
    - the card did not move from where it was when that place would still have been fine: clear, and within
      CARD_NEAR of the region it explains (otherwise it jumps for no reason).
    """
    if not g:
        return ["no tour on the page"]
    problems: list[str] = []
    card, dock = g.get("card"), g.get("dock")
    floor = dock["y"] if dock else g["vh"]
    for k, item in enumerate(g.get("items") or []):
        name = "target" if k == g.get("focus", 0) else f"also[{k}]"
        full, seen, ring = item.get("full"), item.get("seen"), item.get("ring")
        if not full:
            continue                                     # not on this page (an optional extra region)
        if not ring:
            main = (g.get("items") or [{}])[g.get("focus", 0)]
            mf, room = main.get("full"), item.get("room")
            together = mf and room and max(full["y"] + full["h"], mf["y"] + mf["h"]) - min(full["y"], mf["y"]) > room["h"]
            if k != g.get("focus", 0) and not item.get("seen") and together:
                problems.append(f"note: {name} out of view (it and the target do not fit on the screen together)")
            else:
                problems.append(f"{name} has no ring")
            continue
        if (item.get("underBar") or 0) > 6:                  # a tab strip overlapping by a few pixels is its design
            problems.append(f"top of {name} hidden by {round(item['underBar'])}px under a bar pinned to the screen")
        cut = max(ring["x"] - full["x"], ring["y"] - full["y"], full["x"] + full["w"] - ring["x"] - ring["w"], full["y"] + full["h"] - ring["y"] - ring["h"])
        room = item.get("room")
        if cut > GEOMETRY_SLACK and room and full["h"] > room["h"] + GEOMETRY_SLACK:
            # Taller than the screen (or its panel) can show: the ring goes round its first part. It must start at the
            # element's top, reach across its whole width, end on the screen and show a real part of it.
            top_and_sides = max(ring["x"] - full["x"], ring["y"] - full["y"], full["x"] + full["w"] - ring["x"] - ring["w"]) <= GEOMETRY_SLACK
            if not top_and_sides:
                problems.append(f"ring misses the top of {name} (taller than the screen: its start must show)")
            elif ring["h"] < min(150, room["h"] / 3) or ring["y"] + ring["h"] > floor + GEOMETRY_SLACK:
                problems.append(f"ring shows too little of {name} ({round(ring['h'])}px of a {round(room['h'])}px screen)")
        elif cut > GEOMETRY_SLACK:
            off = full["y"] < 0 or full["y"] + full["h"] > floor or full["x"] < 0 or full["x"] + full["w"] > g["vw"]
            hidden = bool(seen) and (seen["h"] < full["h"] - GEOMETRY_SLACK or seen["w"] < full["w"] - GEOMETRY_SLACK)
            where = "off screen" if off else ("hidden by its panel" if hidden else "cut")
            problems.append(f"ring cuts {name} by {round(cut)}px ({where})")
        if card and _overlap(card, ring) > 0:
            problems.append(f"card covers {name}" if _clear_place(card, g) else f"note: card on {name} (no clear place for it on this screen)")
    if card:
        keep = [box for box in g.get("keep") or [] if _overlap(card, box) > 0]
        if keep:
            blocked = dict(g, items=(g.get("items") or []) + [{"ring": box} for box in g.get("keep") or []])
            if _clear_place(card, blocked):
                problems.append("card covers the site header or the bar pinned at the top")
        if not _fits(card, g):
            problems.append("card off screen or over the control bar")
        cursor = g.get("cursor")
        if cursor and _overlap(cursor, card) > 0:
            problems.append("pointer on the card")
        if previous_card:
            moved = ((card["x"] - previous_card["x"]) ** 2 + (card["y"] - previous_card["y"]) ** 2) ** 0.5
            stay = dict(previous_card, h=card["h"], w=card["w"])
            items = g.get("items") or []
            focus = items[g.get("focus", 0)].get("ring") if len(items) > g.get("focus", 0) else None
            near = not focus or max(focus["x"] - stay["x"] - stay["w"], stay["x"] - focus["x"] - focus["w"],
                                    focus["y"] - stay["y"] - stay["h"], stay["y"] - focus["y"] - focus["h"]) <= CARD_NEAR
            could_stay = near and _fits(stay, g) and not any(_overlap(stay, item.get("ring")) for item in items)
            if moved > CARD_STILL and could_stay:
                problems.append(f"card jumped {round(moved)}px (its last place was still clear)")
    return problems


# Installed in the page before the tour starts: notes every move of the card and the worst overlap of the pointer
# with the card while each step and phase is on screen, including the moments between settled cards.
MOTION_RECORDER = """(() => {
  const log = window.__ilitTourMotion = {};
  const key = () => { const c = document.querySelector('.ilit-tour-card'); return c ? (c.dataset.step || '?') + ':' + (c.dataset.phase || '?') : null };
  let lastCard = null;
  function tick() {
    const c = document.querySelector('.ilit-tour-card'), cur = document.querySelector('.ilit-tour-cursor.on'), k = key();
    if (c && k && !c.classList.contains('pending')) {
      const e = log[k] = log[k] || {moves: 0, pointer: 0};
      const m = /translate\\((-?[\\d.]+)px, *(-?[\\d.]+)px\\)/.exec(c.style.transform || '');
      if (m) {
        const p = [+m[1], +m[2]];
        if (lastCard && lastCard.k === k && Math.hypot(p[0] - lastCard.p[0], p[1] - lastCard.p[1]) > %d) e.moves++;
        if (!lastCard || lastCard.k !== k || Math.hypot(p[0] - lastCard.p[0], p[1] - lastCard.p[1]) > %d) lastCard = {k, p};
      }
      if (cur) {
        const a = cur.getBoundingClientRect(), b = c.getBoundingClientRect();
        const o = Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left)) * Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
        e.pointer = Math.max(e.pointer, Math.round(o));
      }
    }
    requestAnimationFrame(tick);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => requestAnimationFrame(tick)); else requestAnimationFrame(tick);
})();""" % (CARD_STILL, CARD_STILL)


def run_walk(base: str, width: int, shots: Path | None, require_data: bool = False, height: int | None = None,
             part: tuple[str, str] | None = None) -> int:
    """Take the tour the way a visitor does: start on About and press only Next, timing each step.

    The tour signs in to the Workbench demo and pins decisions as it goes (the same writes a visitor's tour makes).
    Reports per step: how long it took after Next, whether it was skipped, and, at every card (lead, say and show),
    what geometry_problems() finds: a ring that cuts its element off, a card over a lit element, off the screen or
    jumping for no reason, and the pointer on the card. Ends with the count of failing geometric checks.
    part=(first, last) walks only those steps (from first, as after a refresh there), to re-check a few quickly."""
    from playwright.sync_api import sync_playwright

    steps = json.loads(STEPS_FILE.read_text(encoding="utf-8"))["steps"]
    by_id = {step["id"]: step for step in steps}
    problems = 0
    geometry_fails: list[str] = []
    seen: list[str] = []
    size = f"{width}x{height or (900 if width > 700 else 800)}"
    with sync_playwright() as pw:
        browser = launch(pw)
        context = browser.new_context(viewport={"width": width, "height": height or (900 if width > 700 else 800)})
        context.add_init_script(MOTION_RECORDER)
        page = context.new_page()
        errors: list[str] = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(base + "/data-explorer?tab=about", wait_until="domcontentloaded", timeout=60000)
        page.click("[data-ilit-tour-start]")
        if part:
            first = next(k for k, step in enumerate(steps) if step["id"] == part[0])
            page.wait_for_selector(".ilit-tour-card:not(.pending)[data-ms]", timeout=60000)
            page.wait_for_timeout(500)
            page.evaluate("i => { window.ilitTour.exit(); sessionStorage.setItem('ilit.tour.v1', JSON.stringify({i: i, active: true, phase: 'enter', dir: 1, t0: Date.now()})) }", first)
            page.reload(wait_until="domcontentloaded")
            seen.extend(step["id"] for step in steps[:first])
        print(f"walk at {size}" + (f" (steps {part[0]} to {part[1]})" if part else ""))
        print(f"{'#':>2}  {'step':<22} {'ms':>6}  {'scroll':>6}  highlights   (ms: Next to result; 'say' and 'lead' cards are not timed here)")
        last_page, last_y = "", 0
        previous_card = None
        first_result = None                                    # the top result once the filter demo has run

        def check_geometry(label: str) -> list[str]:
            nonlocal previous_card
            g = page.evaluate("() => window.ilitTour && window.ilitTour.geometry()")
            here = page.evaluate("() => location.pathname + location.search")
            if here != check_geometry.page:                  # a new page: the card starts afresh beside its region
                previous_card, check_geometry.page = None, here
            found = geometry_problems(g, previous_card)
            motion = page.evaluate("k => (window.__ilitTourMotion || {})[k] || null", label)
            if motion and motion.get("moves"):
                found.append(f"card moved {motion['moves']} time(s) while this card was up")
            if motion and motion.get("pointer") and not any("pointer on the card" in f for f in found):
                found.append("pointer crossed the card")
            previous_card = g.get("card") if g else None
            geometry_fails.extend(f"{label}: {f}" for f in found if not f.startswith("note:"))
            return found

        check_geometry.page = ""
        for _ in range(3 * len(steps) + 5):
            try:
                page.wait_for_selector(".ilit-tour-card:not(.pending)[data-ms]", timeout=60000)
            except Exception:  # noqa: BLE001
                if not page.locator(".ilit-tour").count():
                    break
                print("    stuck: the card never finished loading")
                problems += 1
                break
            page.wait_for_timeout(800)                         # let the rings and the card finish gliding
            step_id = page.get_attribute(".ilit-tour-card", "data-step")
            ms = int(page.get_attribute(".ilit-tour-card", "data-ms") or 0)
            phase = page.get_attribute(".ilit-tour-card", "data-phase") or "show"
            if phase != "show":                                # "OK, let's move on" or "I'll ...": press Next to see it happen
                found = check_geometry(f"{step_id}:{phase}")
                if not page.evaluate("() => [...document.querySelectorAll('.ilit-tour-ring')].some(r => r.style.display !== 'none')") and phase == "say":
                    found.append("nothing lit")
                    geometry_fails.append(f"{step_id}:{phase}: nothing lit")
                if found:
                    print(f"    {step_id} ({phase}): {'; '.join(found)}")
                before_shot = shots / f"{size}" if shots else None
                if before_shot:
                    before_shot.mkdir(parents=True, exist_ok=True)
                    page.screenshot(path=str(before_shot / f"{len(seen) + 1:02d}-{step_id}-{phase}.png"))
                page.click(".ilit-tour-btn.primary")
                continue
            notes = check_geometry(f"{step_id}:show")
            main_lit = page.evaluate(
                "n => { const r = document.querySelectorAll('.ilit-tour-rings > .ilit-tour-ring')[n]; return !!r && r.style.display !== 'none' }",
                by_id.get(step_id, {}).get("focus", 0),
            )
            if by_id.get(step_id, {}).get("target") and not main_lit:
                notes.append("main highlight NOT SHOWN")
                problems += 1
            data_notes = []
            if by_id.get(step_id, {}).get("needsData") and not page.evaluate(
                "() => /[1-9]/.test(document.querySelector('#fcxKpis')?.innerText || '')"
            ):
                data_notes.append("statistics EMPTY")
            if step_id == "reader-cite-card" and page.evaluate(
                "() => /has not matched|no pinpoint/i.test(document.querySelector('.v6-card2:not(.v6-para)')?.innerText || '')"
            ):
                data_notes.append("citation card has NO PINPOINT")
            # The filter demo must end with the tour's decision at the top of the list, and that is the one it opens.
            if step_id == "adv-won":
                first_result = page.evaluate("() => document.querySelector('#searchResults .case-result')?.dataset.caseId || ''")
            if step_id == "reader-open":
                opened = page.evaluate("() => new URLSearchParams(location.search).get('case_id') || ''")
                if first_result is not None and opened != first_result:
                    notes.append(f"the decision opened ({opened}) is NOT the first result of the filter demo ({first_result})")
                    problems += 1
            if require_data:
                problems += len(data_notes)
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
            lit = page.evaluate("() => [...document.querySelectorAll('.ilit-tour-ring')].filter(r => r.style.display !== 'none').length")
            all_notes = notes + data_notes
            print(f"{index + 1:>2}  {step_id:<22} {ms:>6}{slow}  {moved:>6}  {lit} lit{'; ' + '; '.join(all_notes) if all_notes else ''}")
            if shots:
                (shots / size).mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(shots / size / f"{len(seen):02d}-{step_id}.png"))
            if step_id == steps[-1]["id"] or (part and step_id == part[1]):
                break
            page.click(".ilit-tour-btn.primary")
        if errors:
            print("page error:", errors[0][:200])
            problems += 1
        browser.close()
    print(f"geometric checks failing at {size}: {len(geometry_fails)}")
    for fail in geometry_fails:
        print("  GEOMETRY FAIL:", fail)
    return problems + len(geometry_fails)


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
            page.wait_for_selector(".ilit-tour-card:not(.pending)", timeout=45000)
            page.wait_for_selector(".ilit-tour-dock:not(.pending)", timeout=45000)
            return page.locator(".ilit-tour-count").inner_text()

        page.goto(base + "/data-explorer?tab=about", wait_until="domcontentloaded", timeout=60000)
        page.click("[data-ilit-tour-start]")
        first = second = counter()
        for _ in range(4):                       # a first step that opens with a lead line takes more than one Next
            page.keyboard.press("ArrowRight")
            page.wait_for_timeout(300)
            second = counter()
            if not second.startswith("Step 1 "):
                break
        if first == second:
            problems.append("Next did not advance")
        page.click(".ilit-tour-btn:has-text('Back'):not([disabled])")
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
    parser.add_argument("--sizes", default="", help="walk at each of these window sizes, e.g. 1440x900,1920x1080 (with --walk; overrides --width)")
    parser.add_argument("--demo-sign-in", action="store_true", help="sign in to the Workbench demo first (writes a demo user; leave off for the live site)")
    parser.add_argument("--require-data", action="store_true", help="fail when example data is missing (probes short, statistics empty); use on the real library")
    parser.add_argument("--steps-only", action="store_true")
    parser.add_argument("--walk", action="store_true", help="take the whole tour pressing only Next, with timings (makes the tour's demo writes)")
    parser.add_argument("--part", default="", help="with --walk: walk only steps FIRST:LAST (step ids), e.g. plain-search:adv-won")
    parser.add_argument("--each", action="store_true", help="also open every step on its own, as after a refresh")
    parser.add_argument("--pick-case", action="store_true", help="read-only: rank the cessation decisions the tour could open and print the best one")
    args = parser.parse_args()
    if args.pick_case:
        return pick_example_case(args.base_url.rstrip("/"))

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
        sizes = [tuple(int(n) for n in size.lower().split("x")) for size in args.sizes.split(",") if size] or [(args.width, None)]
        for width, height in sizes:
            failures += run_walk(base, width, args.shots, args.require_data, height, tuple(args.part.split(":", 1)) if args.part else None)
    if args.each or not args.walk:
        failures += run_browser(base, args.shots if not args.walk else None, shot_ids, args.width, args.demo_sign_in, args.require_data)
    if args.require_data:
        failures += short
    print("FAILED" if failures else "all steps resolve")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
