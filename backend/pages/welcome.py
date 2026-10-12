"""Admin / experimental switch: one remembered toggle (top right of the site) that reveals the hidden tabs and tools.

Off (default) shows the normal site: the "Development" and "Testing" groups and the unfinished reader tools are hidden.
On shows all of them. The choice is a display mode kept in the browser (localStorage key ``ilit.reader.experimental``),
not security. Direct links to a case or normal tab never depend on it. Server env flags are separate and unchanged.
"""

from __future__ import annotations

MODE_KEY = "ilit.reader.experimental"

# Added to <head> of every explorer page: hides the development groups before first paint unless the switch is on.
MODE_HEAD = (
    "<script>try{if(localStorage.getItem('" + MODE_KEY + "')!=='1')document.documentElement.classList.add('ilit-demo')}catch(e){document.documentElement.classList.add('ilit-demo')}</script>\n"
    "<style>.ilit-demo [data-group='lab'],.ilit-demo [data-nav-group='lab'],.ilit-demo #labCats{display:none!important}"
    "#siteExperimentalToggle{position:relative}</style>\n"
)

# Keeps a normal-mode visitor out of the development views even by direct tab link.
MODE_GUARD = (
    "const ilitDemoMode=()=>{try{return document.documentElement.classList.contains('ilit-demo')}catch(error){return false}};\n"
    "const ilitDevTab=key=>/^soon-|^research-bench$/.test(String(key||''));\n"
    "const ilitBaseActivate=activateResearchTab;\n"
    "activateResearchTab=function(tabKey,updateUrl=true){return ilitBaseActivate(ilitDemoMode()&&ilitDevTab(tabKey)?'search':tabKey,updateUrl)};\n"
)
