"""Welcome page (the site's front door) and the Demo / Admin mode switch.

The choice is a display mode kept in the browser (localStorage key ``ilit-mode``), not security:
Demo hides the development tabs (the "Development" and "Testing" groups); Admin shows the normal site.
Direct links never depend on the mode, so a link to a case or tab always works.
"""

from __future__ import annotations

MODE_KEY = "ilit-mode"

# Added to <head> of every explorer page: applies the saved mode before first paint.
MODE_HEAD = (
    "<script>try{if(localStorage.getItem('" + MODE_KEY + "')==='demo')document.documentElement.classList.add('ilit-demo')}catch(e){}</script>\n"
    "<style>.ilit-demo [data-group='soon'],.ilit-demo [data-group='testing'],.ilit-demo [data-nav-group='soon'],.ilit-demo [data-nav-group='testing']{display:none!important}</style>\n"
)

# Keeps a Demo visitor out of the development views even by direct tab link.
MODE_GUARD = (
    "const ilitDemoMode=()=>{try{return document.documentElement.classList.contains('ilit-demo')}catch(error){return false}};\n"
    "const ilitDevTab=key=>/^soon-|^research-bench$/.test(String(key||''));\n"
    "const ilitBaseActivate=activateResearchTab;\n"
    "activateResearchTab=function(tabKey,updateUrl=true){return ilitBaseActivate(ilitDemoMode()&&ilitDevTab(tabKey)?'search':tabKey,updateUrl)};\n"
)

MODE_SWITCH = '<a class="primary-link mode-switch" id="modeSwitch" href="/welcome" title="Back to the Welcome page">Welcome</a>'


def welcome_page_html() -> str:
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow,noarchive"><title>ILIT Welcome</title>
<style>
:root{--teal:#0f766e;--ink:#202522;--muted:#69726d;--border:#d8d5ca;--paper:#fffef9;--bg:#f1efe8}
*{box-sizing:border-box}body{margin:0;min-height:100vh;display:grid;place-items:center;background:var(--bg);color:var(--ink);font-family:system-ui,-apple-system,"Segoe UI",sans-serif}
main{width:min(720px,calc(100% - 32px));padding:40px 0}
.brand{font-size:44px;font-weight:800;letter-spacing:.12em;margin:0;color:var(--teal)}
.sub{margin:4px 0 0;color:var(--muted);font-size:15px}
h1{font-size:30px;margin:36px 0 6px}.lead{margin:0 0 24px;color:var(--muted);line-height:1.55}
.choices{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.choice{display:block;padding:22px;background:var(--paper);border:1px solid var(--border);border-radius:8px;color:inherit;text-decoration:none;cursor:pointer;font:inherit;text-align:left;width:100%}
.choice:hover,.choice:focus-visible{border-color:var(--teal);box-shadow:0 0 0 2px rgba(15,118,110,.18);outline:none}
.choice strong{display:block;font-size:20px;margin-bottom:6px}.choice span{color:var(--muted);font-size:14px;line-height:1.5}
.note{margin-top:20px;color:var(--muted);font-size:12px}
@media(max-width:560px){.choices{grid-template-columns:1fr}.brand{font-size:36px}}
</style></head>
<body><main>
<p class="brand">ILIT</p><p class="sub">Immigration Litigation Intelligence System</p>
<h1>Welcome</h1><p class="lead">Choose how you would like to open the site.</p>
<div class="choices">
<button type="button" class="choice" id="chooseDemo" data-mode="demo"><strong>Demo</strong><span>The polished presentation view. Development tools are hidden.</span></button>
<button type="button" class="choice" id="chooseAdmin" data-mode="admin"><strong>Admin / Development</strong><span>The full site, including the development and testing tabs.</span></button>
</div>
<p class="note">This only changes what is shown on this device. You can return to this page at any time from the Welcome link in the site menu.</p>
</main>
<script>
document.querySelectorAll('.choice').forEach(function(button){button.addEventListener('click',function(){
try{localStorage.setItem('ilit-mode',button.dataset.mode)}catch(e){}
location.href='/data-explorer';
})});
</script></body></html>"""
