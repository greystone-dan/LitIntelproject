"""Pitch navigation: four top-level tabs on the main explorer page.

About, Research, Intelligence / Statistics (Judge Profiles, Citation
Intelligence, Federal Court Analytics) and Coming soon (every other feature, each with a
short explainer). The real pages stay in the code and stay reachable by direct
URL, for example ``/data-explorer?tab=themes`` or ``/live-analysis``.
"""

from __future__ import annotations

import json
import re

from .coming_soon_page import ORDER as ROADMAP_ORDER
from .roadmap_page import REDIRECT_ANCHORS

# (key, name, plain explainer)
COMING_SOON = [
    ("themes", "Legal Themes & Statutes", "Find the legal themes and arguments that recur across decisions, and see which statutory provisions each one leans on."),
    ("tag-analytics", "Tag Analytics", "See how legal issue tags trend over time, which judges lean on which tags, and which tags come up most often."),
    ("citation-map", "Citation Map", "Start from one case and follow what it cites and what cites it. Compare two cases to find the authorities they share."),
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
    "saved-searches": ("page", "/saved-searches-ui"),
    "precedent-finder": ("page", "/precedent-finder"),
    "memo-citation-check": ("page", "/memo-citation-check"),
    "case-compare": ("page", "/compare"),
    "issue-brief": ("page", "/issue-brief-ui"),
    "quick-search": ("page", "/quick-search"),
    "tag-finder": ("page", "/tag-finder"),
    "statutes": ("page", "/statute-library"),
}

# Extra Lab tools that are not Coming soon items: the Research Bench panel and two internal check pages.
LAB_EXTRA = [
    ("status", "Status board", "Everything planned, built or imagined, one row each, with how well it is proven, where it stands and what it depends on. Filters by evidence, status and area."),
    ("research-bench", "Research Bench", "A personal and team workspace for saving decisions, tracking live court files and testing decision-level analysis. Concept prototype."),
    ("units-sandbox", "Discussion Units Sandbox", "A separate search and reader for the 300-case discussion unit test group."),
    ("citation-pass", "Citation Pass QA", "An internal check of how well the citation pass finds and resolves references."),
]
SOON_TARGETS["status"] = ("page", "/roadmap")
SOON_TARGETS["research-bench"] = ("panel", "research-bench")
SOON_TARGETS["units-sandbox"] = ("page", "/discussion-units-sandbox")
SOON_TARGETS["citation-pass"] = ("page", "/citation-pass")

# The Lab: every built-but-experimental tool, in four categories (key, label, one-line description, tools).
LAB = [
    ("status", "Status and evidence", "The private side of Coming soon: every item with its evidence, status and what it depends on.", ["status"]),
    ("search", "Search and issues", "New ways to find decisions, issues and passages.",
     ["themes", "tag-analytics", "quick-search", "precedent-finder", "tag-finder", "issue-brief"]),
    ("authorities", "Citations and statutes", "Follow authorities, compare decisions and read the law.",
     ["citation-map", "memo-citation-check", "case-compare", "statutes"]),
    ("workspace", "Reading and workspace", "Reader modes, saved work and alerts.",
     ["markup", "saved-searches", "research-bench"]),
    ("checks", "Checks and testing", "Internal checks on how the data and the tools behave.",
     ["units-sandbox", "citation-pass", "site-architecture"]),
]
LAB_FIRST_TAB = "soon-status"

_BRAND = """<a class="brand-home" id="brandHome" href="/data-explorer?tab=about&amp;group=info" title="Back to the About page" aria-label="ILIT, Immigration Litigation Intelligence System: back to the About page"><span class="brand-name">ILIT</span><span class="brand-sub">Immigration Litigation Intelligence System</span></a>
"""

_PRIMARY = """<nav class="research-nav primary-groups" aria-label="Primary navigation">
<button type="button" data-group="info" aria-pressed="false" aria-controls="researchViews">About</button>
<button type="button" class="active" data-group="research" aria-pressed="true" aria-controls="researchViews">Research</button>
<button type="button" data-group="intel" aria-pressed="false" aria-controls="researchViews">Intelligence / Statistics</button>
<a class="primary-link" href="/workbench">Workbench</a>
<button type="button" data-group="roadmap" aria-pressed="false" aria-controls="researchViews">Coming soon</button>
<button type="button" data-group="lab" aria-pressed="false" aria-controls="researchViews" title="Experimental tools that are built but not yet proven">Lab</button>
<button type="button" class="site-experimental-toggle" id="siteExperimentalToggle" aria-pressed="false" title="One click turns all experimental features on or off: the Lab, units, Find the unit and unfinished reader tools">Experimental: off</button>
</nav>"""


def _tab(group: str, tab: str, panel: str, label: str, active: bool = False, hidden: bool = True) -> str:
    return (
        f'<button class="tab{" active" if active else ""}" type="button" data-nav-group="{group}" data-tab="{tab}" '
        f'aria-pressed="{"true" if active else "false"}" aria-controls="{panel}"{" hidden" if hidden else ""}>{label}</button>'
    )


def _lab_names() -> dict[str, tuple[str, str]]:
    names = {key: (name, text) for key, name, text in COMING_SOON}
    names.update({key: (name, text) for key, name, text in LAB_EXTRA})
    return names


def _subnav() -> str:
    names = _lab_names()
    rows = [
        _tab("info", "about", "aboutPanel", "Overview"),
        _tab("info", "about-how", "aboutPanel", "How it works"),
        _tab("info", "about-changelog", "aboutPanel", "Changelog"),
        _tab("research", "search", "searchPanel", "Research", active=True),
        _tab("intel", "judge-profile", "judgeProfilePanel", "Judge Profiles"),
        _tab("intel", "citation-intelligence", "citationIntelligencePanel", "Citation Intelligence"),
        _tab("intel", "fc-analytics", "fcAnalyticsPanel", "Federal Court Analytics"),
    ]
    rows.append(_tab("roadmap", "roadmap-overview", "comingSoonPanel", "Coming soon"))
    for cat, _label, _blurb, keys in LAB:
        for key in keys:
            tab = _tab("lab", f"soon-{key}", "comingSoonPanel", names[key][0].replace("&", "&amp;"))
            rows.append(tab.replace("<button ", f'<button data-lab-cat="{cat}" ', 1))
    tools = '<nav id="researchViews" class="view-tabs group-views" aria-label="Research views">\n' + "\n".join(rows) + "\n</nav>"
    cats = "".join(
        f'<button type="button" class="tab lab-cat" data-lab-cat="{cat}" data-lab-first="soon-{keys[0]}" aria-pressed="false">{label}<span class="lab-count">{len(keys)}</span></button>'
        for cat, label, _blurb, keys in LAB
    )
    return ('<nav id="labCats" class="view-tabs lab-cats" aria-label="Lab sections" hidden>' + cats + "</nav>\n" + tools +
            "")


_BANNER = """<div id="comingSoonBanner" class="cs-banner lab-notice" hidden><span class="lab-flag">Experimental</span><span class="lab-notice-text" id="labNotice">Built and reachable, but not yet proven. Nothing in the Lab is a finished feature.</span><a id="comingSoonRoadmap" href="/data-explorer?tab=soon-status&amp;group=lab">See how well each is proven on the Status board &rarr;</a></div>
"""

_PANEL = _BANNER + """<section id="comingSoonPanel" class="panel-card" hidden>
<div class="page-header" id="comingSoonHead"><h2 id="comingSoonTitle"></h2><p id="comingSoonText"></p><p class="cs-more"><a href="/data-explorer?tab=soon-status&amp;group=lab">There is no separate page for this one yet. See its entry on the Status board &rarr;</a></p></div>
<iframe id="comingSoonFrame" class="cs-frame" title="Coming soon preview" hidden></iframe>
</section>
"""

_CSS = """<style>
.topbar .brand-home{display:flex;align-items:baseline;gap:13px;margin:0 auto 0 0;padding:6px 10px;border-radius:6px;color:inherit;text-decoration:none;cursor:pointer;min-width:0}
.topbar .brand-home:hover{background:#f1efe6}.topbar .brand-home:focus-visible{outline:2px solid var(--teal);outline-offset:2px}
.topbar .primary-groups{margin-left:auto}
@media(max-width:600px){.topbar .brand-home{flex-basis:100%;margin:0}.topbar .primary-groups{margin-left:0}}
.research-nav a.primary-link{display:flex;align-items:center;justify-content:center;min-width:72px;min-height:40px;padding:8px 12px;border-radius:5px;color:var(--muted);font-size:12px;font-weight:600;text-decoration:none}.research-nav a.primary-link:hover{color:var(--teal)}
.pitch-embedded .topbar,.pitch-embedded #researchViews{display:none!important}
#researchViews[hidden]{display:none!important}
.lab-notice{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;padding:9px 12px;border:1px solid #e3d28a;border-left:4px solid #c9a100;border-radius:6px;background:#fdf8e1;font-size:13px;color:#4b4320}
.lab-flag{background:#111;color:#f5c400;font-weight:800;letter-spacing:.12em;text-transform:uppercase;font-size:11px;padding:3px 9px;border-radius:3px}
.lab-notice a{margin-left:auto;font-weight:600;color:var(--teal);text-decoration:none}.lab-notice a:hover{text-decoration:underline}
.lab-cats{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 0}.lab-cats[hidden]{display:none!important}
.lab-cats .tab{display:inline-flex;align-items:center;gap:8px;padding:9px 14px;font-size:13px;text-transform:none;letter-spacing:0;border-radius:999px}
.lab-cats .tab.active{background:var(--teal);border-color:var(--teal);color:#fff}
.lab-count{display:inline-block;min-width:20px;padding:0 6px;border-radius:999px;background:rgba(0,0,0,.08);font-size:11px;line-height:18px;text-align:center}.lab-cats .tab.active .lab-count{background:rgba(255,255,255,.25)}
.lab-notice[hidden]{display:none}
.cs-more{margin-top:10px}.cs-more a{color:var(--teal);font-weight:600;text-decoration:none}
@media(max-width:600px){.lab-cats:not([hidden]){display:grid!important;grid-template-columns:1fr 1fr;gap:6px!important;overflow:visible!important}.lab-cats .tab{justify-content:space-between;white-space:normal!important;padding:6px 12px!important;font-size:12px;border-radius:12px}.lab-notice a{margin-left:0}}
.lab-cats .tab{border:1px solid var(--border);background:#fffdf9}.lab-cats .tab.active{border-color:var(--teal)}
@media(max-width:600px){.primary-groups{display:grid!important;grid-template-columns:repeat(3,1fr);gap:4px!important}.primary-groups button{min-width:0!important;padding:8px 4px!important;text-align:center;line-height:1.25}.site-experimental-toggle{padding:6px 10px!important;font-size:12px!important;min-height:0!important}}
.pitch-embedded #labCats{display:none!important}
.cs-strip{display:flex;align-items:center;justify-content:center;min-height:44px;margin:0 0 14px;border-radius:6px;background:repeating-linear-gradient(-45deg,#111 0 14px,#f5c400 14px 28px)}
.cs-strip span{background:#111;color:#f5c400;font-weight:800;letter-spacing:.14em;text-transform:uppercase;padding:6px 18px;border-radius:3px;font-size:13px}
.cs-banner{margin:0 0 10px}.cs-banner .ilit-tour-start{margin:10px 0 0}.cs-banner .cs-strip{margin:0}
.cs-frame[hidden],#comingSoonHead[hidden]{display:none}
.cs-frame.cs-frame-flat{border:0;border-radius:0;height:600px;min-height:0;background:transparent}
.cs-frame{display:block;width:100%;height:calc(100vh - 230px);min-height:520px;border:1px solid var(--border);border-radius:6px;background:#fff}
#comingSoonPanel{padding:14px}#comingSoonPanel .page-header p{max-width:60ch;font-size:15px;line-height:1.55}
</style>
"""


def _script() -> str:
    info = {}
    for key, (name, text) in _lab_names().items():
        kind, target = SOON_TARGETS.get(key, ("text", ""))
        info[f"soon-{key}"] = {"name": name, "text": text, "kind": kind, "target": target, "group": "lab"}
    labCats = {cat: {"label": label, "blurb": blurb, "tabs": [f"soon-{key}" for key in keys]} for cat, label, blurb, keys in LAB}
    # Coming soon is the public preview; the Status board (the old long Roadmap page) is the private side inside the Lab.
    # Every older Roadmap address opens the Status board at the matching place, except the overview, tour and demos.
    for key in ROADMAP_ORDER:
        anchor = REDIRECT_ANCHORS.get(key, "")
        if key == "overview":
            info["roadmap-overview"] = {"name": "Coming soon", "text": "", "kind": "page", "target": "/roadmap/preview", "group": "roadmap", "flat": True}
        else:
            info[f"roadmap-{key}"] = {"name": "Status board", "text": "", "kind": "page", "target": "/roadmap" + anchor, "group": "lab", "navTab": "soon-status", "flat": True}
    info["roadmap-tour"] = {"name": "Coming soon", "text": "", "kind": "page", "target": "/roadmap/preview#tour", "group": "roadmap", "flat": True}
    info["roadmap-demos"] = {"name": "Coming soon", "text": "", "kind": "page", "target": "/roadmap/preview#demos", "group": "roadmap", "flat": True}
    info["roadmap-future-features"] = {"name": "Status board", "text": "", "kind": "page", "target": "/roadmap#future-features", "group": "lab", "navTab": "soon-status", "flat": True}
    info["soon-status"]["flat"] = True
    return (
        "const pitchSoon=" + json.dumps(info) + ";\nconst pitchLabCats=" + json.dumps(labCats) + ";\n"
        "const pitchLabels={info:'About',research:'Research',intel:'Intelligence and statistics',roadmap:'Coming soon',lab:'Lab',direct:'Other'};\n"
        "activeResearchPanels.soon='comingSoonPanel';\n"
        "const pitchOldTab={'research-bench':'soon-research-bench'};\n\n"
        "for(const key of Object.keys(researchGroups))delete researchGroups[key];\n"
        "Object.assign(researchGroups,{info:['about'],research:['search'],intel:['judge-profile','citation-intelligence','fc-analytics'],roadmap:['soon'],lab:['soon','research-bench'],soon:['soon'],testing:['soon']});\n"
        "researchGroups.direct=Object.keys(activeResearchPanels).filter(key=>!Object.values(researchGroups).some(list=>list.includes(key)));\n"
        "for(const key of Object.keys(lastGroupTabs))delete lastGroupTabs[key];\n"
        "Object.assign(lastGroupTabs,{info:'about',research:'search',intel:'judge-profile',roadmap:'roadmap-overview',lab:'soon-status',soon:'soon-status',testing:'soon-research-bench'});\n"
        "const pitchFrame=document.getElementById('comingSoonFrame');\n"
        "if(pitchFrame&&pitchFrame.addEventListener)pitchFrame.addEventListener('load',()=>{try{const doc=pitchFrame.contentDocument;if(!doc||!doc.head)return;const style=doc.createElement('style');style.textContent='.topbar,#researchViews,.research-nav,header.top,header:has(.brand),p:has(>a[href*=explorer]){display:none!important}';doc.head.appendChild(style);if(pitchFrame.getAttribute('data-auto')==='1'){const fit=()=>{pitchFrame.style.height=Math.ceil(doc.documentElement.scrollHeight)+'px'};fit();if(window.ResizeObserver)new ResizeObserver(fit).observe(doc.documentElement);if(doc.fonts&&doc.fonts.ready)doc.fonts.ready.then(fit)}}catch(error){}});\n"
        "const pitchCleanStart={info:'about',research:'search',intel:'judge-profile',roadmap:'roadmap-overview',lab:'soon-status'};\n"
        "function pitchResetState(){\n"
        "  const attempt=step=>{try{step()}catch(error){}};\n"
        "  attempt(()=>{const reader=document.getElementById('caseReaderPanel');if(reader&&!reader.hidden&&typeof closeDecisionReader==='function')closeDecisionReader()});\n"
        "  attempt(()=>document.getElementById('clearSearch')?.click());\n"
        "  attempt(()=>{document.querySelectorAll('#citationCaseQuery,#judgeProfileQuery').forEach(input=>{input.value=''})});\n"
        "  attempt(()=>{if(typeof ciState!=='undefined'){ciState.caseId=null;ciState.initialized=false;ciState.active='overview';ciState.page=1;ciState.selectedYear=null}});\n"
        "  attempt(()=>{const panel=document.getElementById('fcAnalyticsPanel');if(panel&&([...panel.querySelectorAll('[data-filter]')].some(select=>select.value)||panel.querySelector('.fcx-chip')||panel.querySelector('#fcxPresets button[aria-pressed=\\'true\\']:not([data-preset=\\'all\\'])')))document.getElementById('fcxClear')?.click()});\n"
        "  attempt(()=>{const frame=document.getElementById('comingSoonFrame');if(frame)frame.removeAttribute('src')});\n"
        "  attempt(()=>window.scrollTo(0,0));\n"
        "}\n"
        "function pitchCleanOpen(group){\n"
        "  pitchResetState();\n"
        "  activateResearchTab(pitchCleanStart[group]);\n"
        "  const url=new URL(location.href);for(const key of [...url.searchParams.keys()])if(key!=='tab'&&key!=='group')url.searchParams.delete(key);\n"
        "  history.replaceState(null,'',url.pathname+url.search+url.hash);\n"
        "}\n"
        "document.addEventListener('click',event=>{\n"
        "  const home=event.target.closest?.('#brandHome');\n"
        "  if(home&&!event.defaultPrevented&&event.button===0&&!(event.ctrlKey||event.metaKey||event.shiftKey||event.altKey)){event.preventDefault();event.stopImmediatePropagation();pitchCleanOpen('info');return}\n"
        "  const button=event.target.closest?.('[data-group]');\n"
        "  if(!button||!pitchCleanStart[button.dataset.group])return;\n"
        "  event.preventDefault();event.stopImmediatePropagation();pitchCleanOpen(button.dataset.group);\n"
        "},true);\n"
        "function pitchLabSync(soon){\n"
        "  try{const cats=document.getElementById('labCats'),blurb=document.getElementById('labNotice');\n"
        "  const cat=soon?Object.keys(pitchLabCats).find(key=>pitchLabCats[key].tabs.includes(soon)):null;\n"
        "  if(cats){cats.hidden=!cat;cats.querySelectorAll('[data-lab-cat]').forEach(button=>{const on=button.dataset.labCat===cat;button.classList.toggle('active',on);button.setAttribute('aria-pressed',String(on))})}\n"
        "  if(blurb&&cat)blurb.textContent=pitchLabCats[cat].blurb+' Built and reachable, but not yet proven.'\n"
        "  if(cat)document.querySelectorAll('#researchViews [data-lab-cat]').forEach(tab=>{tab.hidden=tab.dataset.labCat!==cat})}catch(error){}\n"
        "}\n"
        "document.addEventListener('click',event=>{\n"
        "  const button=event.target.closest?.('#labCats [data-lab-first]');\n"
        "  if(!button||event.defaultPrevented)return;\n"
        "  event.preventDefault();event.stopImmediatePropagation();activateResearchTab(button.dataset.labFirst);\n"
        "},true);\n"
        "const pitchBaseActivate=activateResearchTab;\n"
        "function pitchShowSoonNav(soon,groupKey){\n"
        "  document.querySelectorAll('[data-group]').forEach(button=>{const on=button.dataset.group===groupKey;button.classList.toggle('active',on);button.setAttribute('aria-pressed',String(on))});\n"
        "  document.querySelectorAll('[data-nav-group]').forEach(item=>{item.hidden=item.dataset.navGroup!==groupKey});\n"
        "  document.querySelectorAll('[data-tab]').forEach(tab=>{const on=tab.dataset.tab===soon;tab.classList.toggle('active',on);tab.setAttribute('aria-pressed',String(on))});\n"
        "}\n"
        "activateResearchTab=function(tabKey,updateUrl=true){\n"
        "  const wanted0=tabKey==='info'?'about':String(tabKey||'search'),wanted=pitchOldTab[wanted0]||wanted0;\n"
        "  const target=wanted.indexOf('about-')===0?'about':wanted;\n"
        "  const aboutParam=!updateUrl?new URLSearchParams(location.search).get('about'):null;\n"
        "  const aboutView=wanted.indexOf('about-')===0?wanted.slice(6):wanted==='about'?(aboutParam==='changelog'||aboutParam==='how'?aboutParam:'overview'):null;\n"
        "  const soon=pitchSoon[wanted]?wanted:null,item=soon?pitchSoon[soon]:null;\n"
        "  const banner=document.getElementById('comingSoonBanner');if(banner)banner.hidden=!soon||pitchSoon[soon].group!=='lab'||Boolean(pitchSoon[soon].flat);\n"
        "  if(!soon)pitchLabSync(null);\n"
        "  if(!soon){pitchBaseActivate(target,updateUrl);if(aboutView&&window.showAboutView)window.showAboutView(aboutView,updateUrl)}\n"
        "  else{\n"
        "    pitchBaseActivate(item.kind==='panel'?item.target:'soon',false);\n"
        "    lastGroupTabs[item.group]=item.navTab||soon;pitchShowSoonNav(item.navTab||soon,item.group);pitchLabSync(item.group==='lab'?(item.navTab||soon):null);\n"
        "    const frame=document.getElementById('comingSoonFrame'),head=document.getElementById('comingSoonHead');\n"
        "    const framed=item.kind==='page';\n"
        "    if(frame){const flat=Boolean(item.flat);try{frame.setAttribute('data-auto',flat?'1':'0');frame.setAttribute('class',flat?'cs-frame cs-frame-flat':'cs-frame');if(!flat)frame.style.height=''}catch(error){}frame.hidden=!framed;if(framed&&frame.getAttribute('src')!==item.target)frame.setAttribute('src',item.target);if(framed)frame.title=item.name+(item.group==='roadmap'?' (roadmap)':' (in development)')}\n"
        "    if(head){head.hidden=item.kind!=='text';document.getElementById('comingSoonTitle').textContent=item.name;document.getElementById('comingSoonText').textContent=item.text}\n"
        "    if(updateUrl){const url=new URL(location.href);url.searchParams.set('tab',soon);url.searchParams.set('group',item.group);url.searchParams.delete('case_id');history.pushState(null,'',url.pathname+url.search+url.hash)}\n"
        "  }\n"
        "  const group=soon?item.group:Object.keys(researchGroups).find(key=>researchGroups[key].includes(activeResearchPanels[target]?target:'search'));\n"
        "  const nav=document.getElementById('researchViews');\n"
        "  if(nav)nav.setAttribute('aria-label',(pitchLabels[group]||'Site')+' views');\n"
        "  if(nav)nav.hidden=[...(nav.querySelectorAll?.('[data-nav-group]')||[])].filter(item=>!item.hidden).length<2;\n"
        "};\n"
    )


def apply_pitch_navigation(html: str) -> str:
    html, n = re.subn(r'<header class="topbar">.*?</header>', lambda _m: '<header class="topbar">\n' + _BRAND + _PRIMARY + '\n</header>', html, count=1, flags=re.S)
    if n != 1:
        raise RuntimeError("pitch navigation: header not found")
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
