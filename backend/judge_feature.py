"""One switch for the judge profile feature (Judge Profiles tab, reader judge panel, comparison, judge statistics).

Hidden unless ILIT_JUDGE_PROFILES is 1/true/yes/on. Judge names stay as plain text on cards, the reader header and
exports; only the profile pages, the profile APIs, the judge statistics and the links into them are switched off.
Stored data is never touched, so setting the variable and restarting brings everything back.
"""

from __future__ import annotations

import json
import os
import re

_TRUE = {"1", "true", "yes", "on"}

# Judge profile and judge statistics routes. Each answers 404 while the feature is hidden.
_HIDDEN_PATH = re.compile(
    r"^(?:/api/judge-profiles(?:/.*)?|/judges(?:/.*)?|/api/fc-activity/judges|/api/citation-intelligence/[^/]+/judges)/?$"
)
_SESSION_TAB = ("judge-profile", "judge-outcomes", "judge")


def judge_profiles_enabled() -> bool:
    return os.getenv("ILIT_JUDGE_PROFILES", "").strip().lower() in _TRUE


def is_hidden_judge_path(path: str) -> bool:
    return bool(_HIDDEN_PATH.match(path))


_PAGE_HEAD = """<style id="judgeFeatureOff">
[data-tab="judge-profile"],[data-tab="judge-outcomes"],#judgeProfilePanel,[data-v6-isub="judge"],#fcxJudges,.fcx-card:has(#fcxJudges),.v6-open-judge{display:none!important}
[data-v6-go="judge"],[data-v6-judge]{pointer-events:none!important;cursor:text!important;color:inherit!important;text-decoration:none!important}
[data-v6-judge] .v6-chev{display:none!important}
</style>
<script id="judgeFeatureOffRedirect">
window.ILIT_JUDGES_OFF=true;
(function(){try{var u=new URL(location.href),t=u.searchParams.get('tab');
if(t==='judge-profile'||t==='judge-outcomes'||t==='judge'){u.searchParams.set('tab','citation-intelligence');u.searchParams.delete('judge');u.searchParams.delete('minister');history.replaceState(null,'',u.pathname+u.search+u.hash)}}catch(e){}})();
document.addEventListener('click',function(e){var t=e.target&&e.target.closest&&e.target.closest('[data-v6-go="judge"],[data-v6-judge],[data-v6-isub="judge"]');if(t){e.preventDefault();e.stopImmediatePropagation()}},true);
</script>
"""


def hide_judge_profiles_in_page(html: str) -> str:
    """Remove the judge profile feature from the Data Explorer page. A no-op while the feature is switched on."""
    if judge_profiles_enabled():
        return html
    html = re.sub(r'<button[^>]*data-tab="judge-profile"[^>]*>.*?</button>', "", html, flags=re.S)
    html = html.replace("intel:['judge-profile','citation-intelligence','fc-analytics']", "intel:['citation-intelligence','fc-analytics']")
    html = html.replace("intel:'judge-profile'", "intel:'citation-intelligence'")
    return html.replace("</head>", _PAGE_HEAD + "</head>", 1)


def filter_tour_data(data: dict) -> dict:
    """Drop the tour steps and warm-up requests that open judge profiles while the feature is hidden."""
    if judge_profiles_enabled():
        return data

    def scrub(value):
        if isinstance(value, str):
            return value.replace("tab=judge-profile", "tab=citation-intelligence")
        if isinstance(value, list):
            return [scrub(v) for v in value if not (isinstance(v, str) and "judge" in v.lower() and v.startswith("/"))]
        if isinstance(value, dict):
            return {k: scrub(v) for k, v in value.items()}
        return value

    out = dict(data)
    out["steps"] = [s for s in data.get("steps", []) if s.get("id") not in {"sh-side-judge", "sh-judges"}]
    out["probes"] = [p for p in data.get("probes", []) if "judge" not in json.dumps(p).lower()]
    for key in ("steps", "warm", "cache"):
        if key in out:
            out[key] = scrub(out[key])
    return out


_TOUR_DROP = {"sh-side-judge", "sh-judges", "sh-judge-open", "sh-judge-charts"}


def filter_window_data(data: dict) -> dict:
    """Drop the recorded tour's judge profile steps while the feature is hidden, and renumber what is left."""
    if judge_profiles_enabled():
        return data
    moments = [dict(m) for m in data["moments"] if m.get("id") not in _TOUR_DROP]
    totals: dict[str, int] = {}
    for m in moments:
        totals[m["section"]] = totals.get(m["section"], 0) + 1
    seen: dict[str, int] = {}
    for n, m in enumerate(moments, 1):
        m["step"] = n
        seen[m["section"]] = seen.get(m["section"], 0) + 1
        if " OF " in m.get("kicker", ""):
            m["kicker"] = re.sub(r"\d+ OF \d+$", f"{seen[m['section']]} OF {totals[m['section']]}", m["kicker"])
        if m["id"] == "sh-side-cite":
            m["text"] = m["text"].replace("has two subsections, Citation Intelligence, and Judge Profiles. Both default to the current case.", "has one subsection, Citation Intelligence, which defaults to the current case.")
        if m["id"] == "sh-ci-charts":
            m["text"] = m["text"].replace(" Next, we continue to Judge Profiles.", "")
        if m["id"] == "sh-wrap":
            m["text"] = m["text"].replace(" profiles the judges,", "")
    return {**data, "moments": moments}
