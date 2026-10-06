"""Pitch navigation: four top-level tabs on the main explorer page.

About, Case search, Intelligence / Statistics (Judge Profiles, Citation
Intelligence, Federal Court Analytics) and Coming soon (every other feature, each with a
short explainer). The real pages stay in the code and stay reachable by direct
URL, for example ``/data-explorer?tab=themes`` or ``/live-analysis``.
"""

from __future__ import annotations

import json
import re

# (key, name, plain explainer)
COMING_SOON = [
    ("themes", "Legal Themes & Statutes", "Find the legal themes and arguments that recur across decisions, and see which statutory provisions each one leans on."),
    ("tag-analytics", "Tag Analytics", "See how legal issue tags trend over time, which judges lean on which tags, and which tags come up most often."),
    ("citation-map", "Citation Map", "Start from one case and follow what it cites and what cites it. Compare two cases to find the authorities they share."),
    ("live-analysis", "Live Analysis", "Paste text or upload a Word or text PDF file to list its case citations and statute references with paragraph locations. The file is read in memory and not stored."),
    ("deidentify", "De-identify", "Swap names, ID numbers, contact details and dates in a document for placeholders, then put them back later with a key file."),
    ("markup", "Markup Reader", "A fuller reading mode with margin notes, citation panels and a case drawer layered over the decision text."),
    ("saved-searches", "Saved Searches & Alerts", "Save a search and review any new decisions that match it."),
    ("precedent-finder", "Precedent Finder", "Describe the legal issue and get the authorities cited by decisions that carry matching issue tags."),
    ("memo-citation-check", "Memo Citation Check", "Upload a memo or brief to list the authorities it cites, see how each has been treated, and discover commonly cited authorities on related issues."),
    ("case-compare", "Case Compare", "Put two decisions side by side and compare their stored details, tags and citations."),
    ("issue-brief", "Issue Briefs", "A short research brief on one legal issue tag, built from the decisions that address it."),
    ("quick-search", "Quick Search", "Search the text of decisions by passage instead of by case, to find the paragraphs that say what you are looking for."),
    ("tag-finder", "Tag Finder", "Pick a decision and find others that share its legal issue tags."),
    ("statutes", "Federal Statutes", "Read a section of IRPA, IRPR and other federal acts and see every decision in the library that cites it, by year, court and outcome."),
    ("site-architecture", "Site Architecture", "A live map of how decisions move from official sources into the library and out to each research page."),
]

# How each Coming soon item loads under the banner: an explorer panel that is already in the page,
# a real page shown in a same-origin frame, or None (explainer only).
SOON_TARGETS = {
    "themes": ("panel", "themes"),
    "tag-analytics": ("panel", "tag-analytics"),
    "site-architecture": ("panel", "site-architecture"),
    "citation-map": ("page", "/citation-map"),
    "live-analysis": ("page", "/live-analysis"),
    "deidentify": ("page", "/deidentify"),
    "saved-searches": ("page", "/saved-searches-ui"),
    "precedent-finder": ("page", "/precedent-finder"),
    "memo-citation-check": ("page", "/memo-citation-check"),
    "case-compare": ("page", "/compare"),
    "issue-brief": ("page", "/issue-brief-ui"),
    "quick-search": ("page", "/quick-search"),
    "tag-finder": ("page", "/tag-finder"),
    "statutes": ("page", "/statute-library"),
}

_PRIMARY = """<nav class="research-nav primary-groups" aria-label="Primary navigation">
<button type="button" data-group="info" aria-pressed="false" aria-controls="researchViews">About</button>
<button type="button" class="active" data-group="research" aria-pressed="true" aria-controls="researchViews">Case search</button>
<button type="button" data-group="intel" aria-pressed="false" aria-controls="researchViews">Intelligence / Statistics</button>
<button type="button" data-group="soon" aria-pressed="false" aria-controls="researchViews">Coming soon</button>
<button type="button" data-group="testing" aria-pressed="false" aria-controls="researchViews">Testing</button>
</nav>"""


def _tab(group: str, tab: str, panel: str, label: str, active: bool = False, hidden: bool = True) -> str:
    return (
        f'<button class="tab{" active" if active else ""}" type="button" data-nav-group="{group}" data-tab="{tab}" '
        f'aria-pressed="{"true" if active else "false"}" aria-controls="{panel}"{" hidden" if hidden else ""}>{label}</button>'
    )


def _subnav() -> str:
    rows = [
        _tab("info", "about", "aboutPanel", "About"),
        _tab("research", "search", "searchPanel", "Case search", active=True, hidden=False),
        _tab("intel", "judge-profile", "judgeProfilePanel", "Judge Profiles"),
        _tab("intel", "citation-intelligence", "citationIntelligencePanel", "Citation Intelligence"),
        _tab("intel", "fc-analytics", "fcAnalyticsPanel", "Federal Court Analytics"),
    ]
    rows += [_tab("soon", f"soon-{key}", "comingSoonPanel", name.replace("&", "&amp;")) for key, name, _ in COMING_SOON]
    rows += [
        _tab("testing", "research-bench", "researchBenchPanel", "Research Bench"),
        '<a class="tab" data-nav-group="testing" href="/discussion-units-sandbox" hidden>Discussion Units Sandbox</a>',
        '<a class="tab" data-nav-group="testing" href="/citation-pass" hidden>Citation Pass QA</a>',
    ]
    return '<nav id="researchViews" class="view-tabs group-views" aria-label="Case search views">\n' + "\n".join(rows) + "\n</nav>"


_BANNER = """<div id="comingSoonBanner" class="cs-banner" hidden><div class="cs-strip" role="img" aria-label="Coming soon"><span>Coming soon</span></div></div>
"""

_PANEL = _BANNER + """<section id="comingSoonPanel" class="panel-card" hidden>
<div class="page-header" id="comingSoonHead"><h2 id="comingSoonTitle"></h2><p id="comingSoonText"></p></div>
<iframe id="comingSoonFrame" class="cs-frame" title="Coming soon preview" hidden></iframe>
</section>
"""

_CSS = """<style>
.pitch-embedded .topbar,.pitch-embedded #researchViews{display:none!important}
.cs-strip{display:flex;align-items:center;justify-content:center;min-height:44px;margin:0 0 14px;border-radius:6px;background:repeating-linear-gradient(-45deg,#111 0 14px,#f5c400 14px 28px)}
.cs-strip span{background:#111;color:#f5c400;font-weight:800;letter-spacing:.14em;text-transform:uppercase;padding:6px 18px;border-radius:3px;font-size:13px}
.cs-banner{margin:0 0 10px}.cs-banner .cs-strip{margin:0}
.cs-frame[hidden],#comingSoonHead[hidden]{display:none}
.cs-frame{display:block;width:100%;height:calc(100vh - 230px);min-height:520px;border:1px solid var(--border);border-radius:6px;background:#fff}
#comingSoonPanel{padding:14px}#comingSoonPanel .page-header p{max-width:60ch;font-size:15px;line-height:1.55}
</style>
"""


def _script() -> str:
    info = {}
    for key, name, text in COMING_SOON:
        kind, target = SOON_TARGETS.get(key, ("text", ""))
        info[f"soon-{key}"] = {"name": name, "text": text, "kind": kind, "target": target}
    return (
        "const pitchSoon=" + json.dumps(info) + ";\n"
        "const pitchLabels={info:'About',research:'Case search',intel:'Intelligence and statistics',soon:'Coming soon',testing:'Testing',direct:'Other'};\n"
        "activeResearchPanels.soon='comingSoonPanel';\n"
        "for(const key of Object.keys(researchGroups))delete researchGroups[key];\n"
        "Object.assign(researchGroups,{info:['about'],research:['search'],intel:['judge-profile','citation-intelligence','fc-analytics'],soon:['soon'],testing:['research-bench']});\n"
        "researchGroups.direct=Object.keys(activeResearchPanels).filter(key=>!Object.values(researchGroups).some(list=>list.includes(key)));\n"
        "for(const key of Object.keys(lastGroupTabs))delete lastGroupTabs[key];\n"
        "Object.assign(lastGroupTabs,{info:'about',research:'search',intel:'judge-profile',soon:Object.keys(pitchSoon)[0],testing:'research-bench'});\n"
        "const pitchFrame=document.getElementById('comingSoonFrame');\n"
        "if(pitchFrame&&pitchFrame.addEventListener)pitchFrame.addEventListener('load',()=>{try{const doc=pitchFrame.contentDocument;if(!doc||!doc.head)return;const style=doc.createElement('style');style.textContent='.topbar,#researchViews,.research-nav{display:none!important}';doc.head.appendChild(style)}catch(error){}});\n"
        "const pitchBaseActivate=activateResearchTab;\n"
        "function pitchShowSoonNav(soon){\n"
        "  document.querySelectorAll('[data-group]').forEach(button=>{const on=button.dataset.group==='soon';button.classList.toggle('active',on);button.setAttribute('aria-pressed',String(on))});\n"
        "  document.querySelectorAll('[data-nav-group]').forEach(item=>{item.hidden=item.dataset.navGroup!=='soon'});\n"
        "  document.querySelectorAll('[data-tab]').forEach(tab=>{const on=tab.dataset.tab===soon;tab.classList.toggle('active',on);tab.setAttribute('aria-pressed',String(on))});\n"
        "}\n"
        "activateResearchTab=function(tabKey,updateUrl=true){\n"
        "  const wanted=tabKey==='info'?'about':String(tabKey||'search');\n"
        "  const soon=pitchSoon[wanted]?wanted:null,item=soon?pitchSoon[soon]:null;\n"
        "  const banner=document.getElementById('comingSoonBanner');if(banner)banner.hidden=!soon;\n"
        "  if(!soon){pitchBaseActivate(wanted,updateUrl);}\n"
        "  else{\n"
        "    pitchBaseActivate(item.kind==='panel'?item.target:'soon',false);\n"
        "    lastGroupTabs.soon=soon;pitchShowSoonNav(soon);\n"
        "    const frame=document.getElementById('comingSoonFrame'),head=document.getElementById('comingSoonHead');\n"
        "    const framed=item.kind==='page';\n"
        "    if(frame){frame.hidden=!framed;if(framed&&frame.getAttribute('src')!==item.target)frame.setAttribute('src',item.target);if(framed)frame.title=item.name+' (coming soon)'}\n"
        "    if(head){head.hidden=item.kind!=='text';document.getElementById('comingSoonTitle').textContent=item.name;document.getElementById('comingSoonText').textContent=item.text}\n"
        "    if(updateUrl){const url=new URL(location.href);url.searchParams.set('tab',soon);url.searchParams.set('group','soon');url.searchParams.delete('case_id');history.pushState(null,'',url.pathname+url.search+url.hash)}\n"
        "  }\n"
        "  const group=soon?'soon':Object.keys(researchGroups).find(key=>researchGroups[key].includes(activeResearchPanels[wanted]?wanted:'search'));\n"
        "  const nav=document.getElementById('researchViews');\n"
        "  if(nav)nav.setAttribute('aria-label',(pitchLabels[group]||'Site')+' views');\n"
        "  if(nav)nav.hidden=!soon&&[...(nav.querySelectorAll?.('[data-nav-group]')||[])].filter(item=>!item.hidden).length<2;\n"
        "};\n"
    )


def apply_pitch_navigation(html: str) -> str:
    html, n = re.subn(r'<nav class="research-nav primary-groups".*?</nav>', lambda _m: _PRIMARY, html, count=1, flags=re.S)
    if n != 1:
        raise RuntimeError("pitch navigation: primary nav not found")
    html, n = re.subn(r'<nav id="researchViews".*?</nav>', lambda _m: _subnav(), html, count=1, flags=re.S)
    if n != 1:
        raise RuntimeError("pitch navigation: view tabs not found")
    if html.count('<section id="aboutPanel"') != 1:
        raise RuntimeError("pitch navigation: about panel not found")
    html = html.replace('<section id="aboutPanel"', _PANEL + '<section id="aboutPanel"', 1)
    marker = "function restoreResearchNavigation(){"
    if html.count(marker) != 1:
        raise RuntimeError("pitch navigation: restore function not found")
    html = html.replace(marker, _script() + marker, 1)
    html = html.replace("</head>", _CSS + "<script>if(window.self!==window.top)document.documentElement.classList.add('pitch-embedded')</script>\n</head>", 1)
    return html
