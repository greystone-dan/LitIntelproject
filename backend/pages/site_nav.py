"""Shared presentation for finite HTML responses; never buffers a stream."""

from html import escape
from html.parser import HTMLParser
from urllib.parse import parse_qs

from starlette.types import ASGIApp, Message, Receive, Scope, Send


LINKS = (
    ("home", "Home", "/"),
    ("search", "Search", "/data-explorer?tab=search"),
    ("reader", "Case Reader", "/case-reader"),
    ("judges", "Judges", "/data-explorer?tab=judge-profile"),
    ("citations", "Citation Intelligence", "/data-explorer?tab=citation-intelligence"),
    ("fc", "FC Activity", "/data-explorer?tab=fc-history"),
    ("memo", "Memo Check", "/memo-citation-check"),
    ("briefs", "Issue Briefs", "/issue-brief-ui"),
    ("saved", "Saved Searches", "/saved-searches-ui"),
    ("about", "About", "/data-explorer?tab=about"),
)
TABS = {"search": "search", "judge-profile": "judges",
        "citation-intelligence": "citations", "fc-history": "fc", "fc-analytics": "fc",
        "about": "about", "info": "about", "site-architecture": "about"}
ROUTES = {"/": "home", "/case-reader": "reader", "/judges": "judges",
          "/citation-intelligence": "citations", "/citation-map": "citations",
          "/fc-history": "fc", "/memo-citation-check": "memo",
          "/issue-brief-ui": "briefs", "/saved-searches-ui": "saved",
          "/about": "about", "/quick-search": "search"}


def route_context(path: str, query: dict) -> tuple[str | None, str | None]:
    """Use the actual explorer tab and deep-link parameter contracts."""
    value = lambda key: query.get(key, [""])[0]
    if path == "/data-explorer":
        tab = value("tab") or {"info": "about", "research": "search",
                              "workbench": "workbench",
                              "testing": "research-bench"}.get(value("group"), "search")
        if tab == "search" and value("case_id"):
            return "reader", f"Case {value('case_id')}"
        if tab == "judge-profile":
            return "judges", value("judge") or None
        if tab == "citation-intelligence":
            return "citations", f"Case {value('case_id')}" if value("case_id") else None
        return TABS.get(tab), None
    if path.startswith("/case-reader-ui/"):
        return "reader", f"Case {path.rsplit('/', 1)[-1]}"
    if path.startswith("/judges/"):
        return "judges", path.rsplit("/", 1)[-1]
    if path == "/issue-brief-ui":
        return "briefs", value("tag") or None
    if path in {"/citation-map", "/citation-intelligence"}:
        return "citations", f"Case {value('case_id')}" if value("case_id") else None
    return ROUTES.get(path), None


STYLE = """<style>
[data-site-nav]{font:15px/1.5 system-ui,sans-serif;color:#202522;background:#fffef9;border-bottom:1px solid #d8d5ca;padding:12px 20px;position:relative;z-index:100}
[data-site-nav] *{box-sizing:border-box}
[data-site-nav] a{color:#193b54;text-decoration:underline;text-underline-offset:3px}
[data-site-nav] a[aria-current=page]{font-weight:800;text-decoration-thickness:3px}
[data-site-nav] .site-nav-links{display:flex;flex-wrap:wrap;gap:8px 18px;margin:8px 0}
[data-site-nav] form{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:8px 0}
[data-site-nav] input,[data-site-nav] button{font:inherit;padding:6px 10px;border:1px solid #69726d;border-radius:4px;background:white;color:#202522}
[data-site-nav] :focus-visible{outline:3px solid #17669b;outline-offset:3px}
[data-site-nav] .site-menu-toggle{display:none}
[data-site-nav] .site-breadcrumbs ol{display:flex;flex-wrap:wrap;gap:8px;list-style:none;margin:8px 0 0;padding:0}
[data-site-nav] .site-breadcrumbs li+li:before{content:"/";margin-right:8px}
@media(max-width:700px){[data-site-nav] .site-menu-toggle{display:inline-block}[data-site-nav] .site-nav-links{display:none}[data-site-nav] .site-nav-links[data-open=true]{display:flex;flex-direction:column}[data-site-nav] input{max-width:100%}}
@media print{[data-site-nav]{display:none}}
</style>"""

SCRIPT = """<script>
(()=>{const shell=document.querySelector('[data-site-nav]');if(!shell)return;
const button=shell.querySelector('.site-menu-toggle'),links=shell.querySelector('.site-nav-links'),input=shell.querySelector('#site-quick-search');
function menu(open){button.setAttribute('aria-expanded',String(open));links.dataset.open=String(open)}
button.addEventListener('click',()=>menu(button.getAttribute('aria-expanded')!=='true'));
document.addEventListener('keydown',event=>{
 if(event.key==='Escape'&&button.getAttribute('aria-expanded')==='true'){menu(false);button.focus()}
 const target=event.target;
 if(event.key==='/'&&!event.ctrlKey&&!event.metaKey&&!event.altKey&&!event.isComposing&&
 !(target instanceof Element&&
 (target.closest('input,textarea,select,[role="textbox"]')||target.isContentEditable||target.closest('[contenteditable]:not([contenteditable="false"])')))){
 event.preventDefault();input.focus();
 }
});
function sync(){
 const p=new URLSearchParams(location.search);let key;
 if(location.pathname==='/data-explorer'){
 const tab=p.get('tab')||({info:'about',research:'search',workbench:'workbench',testing:'research-bench'}[p.get('group')]||'search');
 const reader=document.getElementById('caseReaderPanel');
 key=tab==='search'&&(reader?!reader.hidden:p.get('case_id'))?'reader':
 ({search:'search','judge-profile':'judges','citation-intelligence':'citations','fc-history':'fc','fc-analytics':'fc',about:'about',info:'about','site-architecture':'about'})[tab];
 shell.querySelectorAll('[data-site-link]').forEach(a=>{a.removeAttribute('aria-current');if(a.dataset.siteLink===key)a.setAttribute('aria-current','page')});
 }
}
window.addEventListener('popstate',()=>setTimeout(sync,0));
document.addEventListener('click',()=>setTimeout(sync,0));
document.addEventListener('DOMContentLoaded',()=>{
 // The explorer's existing submit handler calls /analytics/search/cases?query=...
 const p=new URLSearchParams(location.search),query=p.get('query');
 if(location.pathname==='/data-explorer'&&(p.get('tab')||'search')==='search'&&query){
 const field=document.getElementById('searchQuery'),form=document.getElementById('caseSearch');
 if(field&&form){field.value=query;form.requestSubmit()}
 }
 sync();
 const panel=document.getElementById('caseReaderPanel');
 const panels=document.querySelectorAll('#researchViews ~ section, #caseReaderPanel, [data-tab], [data-group]');
 if(panels.length){const observer=new MutationObserver(sync);panels.forEach(panel=>observer.observe(panel,{attributes:true,attributeFilter:['hidden','aria-pressed']}))}
});
})();
</script>"""


def navigation(path: str, query: dict) -> str:
    active, detail = route_context(path, query)
    link_parts = []
    for key, label, url in LINKS:
        current = ' aria-current="page"' if key == active else ""
        link_parts.append(
            f'<a data-site-link="{key}" href="{escape(url, quote=True)}"{current}>{label}</a>'
        )
    links = "".join(link_parts)
    crumbs = '<li><a href="/">Home</a></li>'
    if active and active != "home":
        _, label, url = next(link for link in LINKS if link[0] == active)
        crumbs += (f'<li><a href="{escape(url, quote=True)}">{label}</a></li>'
                   if detail else f'<li aria-current="page">{label}</li>')
    if detail:
        crumbs += f'<li aria-current="page">{escape(detail)}</li>'
    return (
        STYLE + '<header data-site-nav><strong>iLit · AI CaseLibrary</strong> '
        '<button type="button" class="site-menu-toggle" aria-expanded="false" '
        'aria-controls="site-primary-links">Menu</button>'
        f'<nav aria-label="Primary" id="site-primary-links" class="site-nav-links">{links}</nav>'
        '<form method="get" action="/data-explorer" role="search">'
        '<input type="hidden" name="tab" value="search">'
        '<label for="site-quick-search">Quick case search</label>'
        '<input id="site-quick-search" name="query" type="search" placeholder="Vavilov or 2019 SCC 65">'
        '<button type="submit">Search</button></form>'
        f'<nav class="site-breadcrumbs" aria-label="Breadcrumb"><ol>{crumbs}</ol></nav>'
        '</header>' + SCRIPT
    )


class _InsertionPoint(HTMLParser):
    """Locate source offsets only; never serialize or rebuild the document."""

    def __init__(self, text: str):
        super().__init__(convert_charrefs=False)
        # HTMLParser counts LF, not every separator recognized by splitlines().
        self.offsets = [0] + [index + 1 for index, char in enumerate(text) if char == "\n"]
        self.body_end = None
        self.opt_out = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "data-site-nav" in attributes:
            self.opt_out = True
        if tag == "meta" and (attributes.get("name") or "").lower() in {
            "x-no-site-nav", "no-site-nav"
        }:
            self.opt_out = True
        if (tag == "meta" and (attributes.get("name") or "").lower() == "site-nav"
                and (attributes.get("content") or "").lower() in {"off", "false", "none"}):
            self.opt_out = True
        if tag == "body" and self.body_end is None:
            line, column = self.getpos()
            self.body_end = self.offsets[line - 1] + column + len(self.get_starttag_text())

    handle_startendtag = handle_starttag


def inject_html(body: bytes, path: str, query_string: bytes) -> bytes:
    try:
        text = body.decode("utf-8")
        point = _InsertionPoint(text)
        if point.opt_out or point.body_end is None:
            return body
        query = parse_qs(query_string.decode("utf-8", errors="replace"))
        offset = len(text[:point.body_end].encode("utf-8"))
        return body[:offset] + navigation(path, query).encode("utf-8") + body[offset:]
    except (UnicodeError, ValueError):
        return body


def excluded_path(path: str) -> bool:
    segments = path.lower().strip("/").split("/")
    return (segments[0] in {"api", "health", "access", "login"}
            or any(segment in {"export", "exports", "download"} for segment in segments)
            or path.lower().endswith((".csv", ".docx", ".json")))


class SiteNavMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if (scope["type"] != "http" or scope.get("method") == "HEAD"
                or excluded_path(scope.get("path", ""))):
            await self.app(scope, receive, send)
            return
        pending = None

        async def present(message: Message):
            nonlocal pending
            if message["type"] == "http.response.start":
                headers = {key.lower(): value for key, value in message.get("headers", [])}
                content_type = headers.get(b"content-type", b"").lower().replace(b" ", b"")
                if (message["status"] == 200 and content_type.split(b";")[0] == b"text/html"
                        and (b"charset=" not in content_type or b"charset=utf-8" in content_type)
                        and b"x-no-site-nav" not in headers
                        and b"content-encoding" not in headers
                        and b"content-disposition" not in headers
                        and not message.get("trailers")):
                    pending = message
                    return
            if pending is not None:
                start, pending = pending, None
                if (message["type"] == "http.response.body" and not message.get("more_body")
                        and len(message.get("body", b"")) <= 4 * 1024 * 1024):
                    original = message.get("body", b"")
                    body = inject_html(original, scope["path"], scope.get("query_string", b""))
                    if body != original:
                        start = dict(start)
                        start["headers"] = [
                            (key, value) for key, value in start.get("headers", [])
                            if key.lower() not in {b"content-length", b"etag", b"content-md5"}
                        ] + [(b"content-length", str(len(body)).encode("ascii"))]
                        message = {**message, "body": body}
                await send(start)
            await send(message)

        await self.app(scope, receive, present)


def home_html() -> str:
    descriptions = {
        "search": "Find decisions by case name or citation.",
        "reader": "Read a decision's text, source details and highlighted authorities.",
        "judges": "Review a judge's aliases, linked decisions and classified outcomes.",
        "citations": "Explore a selected case's stored citing decisions and citation evidence.",
        "fc": "Look up recorded Federal Court history and activity summaries.",
        "memo": "Check citations in a DOCX or text-based PDF up to 10 MB.",
        "briefs": "Review source-linked decisions for an exact legal tag.",
        "saved": "Return to saved research queries and continue investigating their results.",
        "about": "Understand library coverage, limitations and the processing pipeline.",
    }
    # Case IDs and judge slugs belong to the local library, not a portable demo.
    # Start case examples with a real citation search rather than inventing IDs.
    examples = {
        "search": ("Example: search Vavilov", "/data-explorer?tab=search&query=Vavilov"),
        "reader": ("Example: find 2019 SCC 65, then open a result",
                   "/data-explorer?tab=search&query=2019+SCC+65"),
        "judges": ("Example: open Judge Profile, then search a judge's name",
                   "/data-explorer?tab=judge-profile"),
        "citations": ("Example: find Vavilov, then select Citation Intelligence",
                      "/data-explorer?tab=search&query=Vavilov"),
        "fc": ("Example: look up IMM-1234-19",
               "/data-explorer?tab=fc-history&imm=IMM-1234-19"),
        "memo": ("Example workflow: upload a memo and analyze its citations",
                 "/memo-citation-check"),
        "briefs": ("Example: review the topic:fairness brief",
                   "/issue-brief-ui?tag=topic%3Afairness"),
        "saved": ("Example workflow: open a saved search",
                  "/saved-searches-ui"),
        "about": ("Example: explore the system architecture",
                  "/data-explorer?tab=site-architecture"),
    }
    cards = "".join(
        f'<section data-tool-card="{key}">'
        f'<h2><a href="{escape(url, quote=True)}">{label}</a></h2>'
        f'<p data-tool-description>{escape(descriptions[key])}</p>'
        f'<a data-tool-example href="{escape(examples[key][1], quote=True)}">'
        f'{escape(examples[key][0])}</a></section>'
        for key, label, url in LINKS if key != "home"
    )
    return """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>iLit research home</title>
<style>body{margin:0;background:#f1efe8;color:#202522;font-family:system-ui,sans-serif}
main{max-width:1100px;margin:32px auto;padding:0 20px} .tools{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}
section{padding:20px;background:#fffef9;border:1px solid #d8d5ca;border-radius:8px}h2{font-size:20px}p{line-height:1.6}a{color:#193b54}</style>
</head><body><main><h1>Immigration litigation research</h1>
<p>Start with a name or citation, read the decision, then investigate its research context.
iLit is not a legal citator, an official court record, or legal advice. Verify important findings against authoritative sources.</p>
<p><a href="/data-explorer">Open the Data Explorer</a> — the existing research workspace remains available.</p>
<div class="tools">""" + cards + "</div></main></body></html>"
