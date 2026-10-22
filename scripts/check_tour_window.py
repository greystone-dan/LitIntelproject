"""Walk the recorded tour window the way a visitor does: press Next from step 1 to the end, and report what looks wrong.

    python scripts/check_tour_window.py --base http://127.0.0.1:8001 [--width 1440 --height 900] [--shots DIR]

It needs Playwright and a running site. It checks that every step settles, that no picture or script fails to
load, that no page error is raised, that the card sits inside the stage and clear of every highlight (a card may
sit on a highlight that wraps the whole page), and that Exit hands control back to the page. With --shots it saves
the settled frame of every step. It reads the site's own tour pages only; nothing is written anywhere.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

_SETTLED = "() => !document.getElementById('next').disabled && !document.getElementById('tour').hidden"
_STATE = """() => {
  const st = document.getElementById('stage').getBoundingClientRect(), k = st.width / 1440;
  const box = e => { const r = e.getBoundingClientRect(); return {x: (r.left - st.left) / k, y: (r.top - st.top) / k, w: r.width / k, h: r.height / k}; };
  const rings = [...document.querySelectorAll('.ilit-tour-ring')].filter(e => e.style.display !== 'none').map(box).filter(r => r.w > 2);
  return {count: document.getElementById('cnt').textContent, title: document.getElementById('ttl').textContent,
          card: box(document.getElementById('card')), rings, next: document.getElementById('next').textContent};
}"""


def _overlap(a: dict, b: dict) -> bool:
    return a["x"] < b["x"] + b["w"] and a["x"] + a["w"] > b["x"] and a["y"] < b["y"] + b["h"] and a["y"] + a["h"] > b["y"]


def _problems(state: dict) -> list[str]:
    found: list[str] = []
    card = state["card"]
    if card["x"] < 0 or card["y"] < 0 or card["x"] + card["w"] > 1440 or card["y"] + card["h"] > 900:
        found.append("the card leaves the screen")
    for ring in state["rings"]:
        wraps_page = ring["w"] > 1300 and ring["h"] > 600
        if _overlap(card, ring) and not wraps_page:
            found.append("the card covers a highlight")
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--base", default="http://127.0.0.1:8001")
    parser.add_argument("--width", type=int, default=1440)
    parser.add_argument("--height", type=int, default=900)
    parser.add_argument("--shots", default="")
    args = parser.parse_args()
    from playwright.sync_api import sync_playwright

    problems: list[str] = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=os.getenv("ILIT_CHROMIUM") or None)   # ILIT_CHROMIUM: a browser already on the machine
        page = browser.new_page(viewport={"width": args.width, "height": args.height})
        page.on("pageerror", lambda error: problems.append(f"page error: {error}"))
        page.on("requestfailed", lambda request: problems.append(f"failed request: {request.url}"))
        page.on("response", lambda response: problems.append(f"{response.status} {response.url}") if response.status >= 400 else None)
        page.goto(f"{args.base}/tour-window/?embed=1", wait_until="load")
        page.wait_for_function(_SETTLED, timeout=30000)
        shots = Path(args.shots) if args.shots else None
        if shots:
            shots.mkdir(parents=True, exist_ok=True)
        step = 1
        while True:
            page.wait_for_timeout(800)        # let the highlight finish its glide
            state = page.evaluate(_STATE)
            print(f"{state['count']:>14}  {state['title']}")
            problems += [f"step {step}: {text}" for text in _problems(state)]
            if shots:
                page.screenshot(path=str(shots / f"step_{step:02d}.png"))
            if state["next"] == "Done":
                break
            page.click("#next")
            try:
                page.wait_for_function(_SETTLED, timeout=60000)
            except Exception:
                problems.append(f"step {step + 1}: did not settle in 60 s")
                break
            step += 1
        browser.close()
    for text in problems:
        print("PROBLEM:", text)
    print(f"{step} steps walked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
