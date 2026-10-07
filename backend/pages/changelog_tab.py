"""About page sub-tabs: the overview text and a changelog built from GitHub records.

The changelog data is data/changelog/changelog.json (written by scripts/build_changelog.py) and is embedded in the
page when it is built, so viewing it makes no network calls and uses no AI.
"""

from __future__ import annotations

import html
import json
from pathlib import Path

from .pitch_nav import COMING_SOON

CHANGELOG_PATH = Path(__file__).resolve().parents[2] / "data" / "changelog" / "changelog.json"

_CSS = """
.about-subtabs{display:flex;gap:6px;margin:0 0 14px;padding:0 0 2px;overflow-x:auto;-webkit-overflow-scrolling:touch}
.about-subtabs .tab{flex:0 0 auto}
.cl{max-width:none;color:var(--text)}
.cl-head h2{margin:0;font:600 34px/1.1 "Newsreader",serif;letter-spacing:-.01em}
.cl-head .cl-sub{margin:8px 0 0;font:600 17px/1.3 "Newsreader",serif}
.cl-head p{margin:8px 0 0;color:var(--muted);font-size:13px;line-height:1.65;max-width:none}
.cl-filters{display:flex;flex-wrap:wrap;gap:6px;margin:16px 0 4px}
.cl-chip{border:1px solid var(--border);background:var(--surface);color:var(--muted);border-radius:999px;padding:5px 11px;font-family:inherit;font-size:12px;font-weight:600;line-height:1.2;cursor:pointer}
.cl-chip[aria-pressed="true"]{background:var(--rust);border-color:var(--rust);color:#fff}
.cl-chip small{font-weight:500;opacity:.8;margin-left:3px}
.cl-chip:focus-visible{outline:2px solid var(--blue);outline-offset:2px}
.cl-day{margin-top:22px}
.cl-day h4{margin:0 0 8px;padding-bottom:6px;border-bottom:1px solid var(--border);font:600 17px/1.2 "Newsreader",serif}
.cl-item{padding:10px 0 10px 14px;border-left:2px solid var(--border);margin-left:3px}
.cl-item+.cl-item{margin-top:2px}
.cl-item strong{display:block;font-size:14px;line-height:1.35}
.cl-item p{margin:3px 0 0;color:var(--muted);font-size:13px;line-height:1.6}
.cl-meta{display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px;margin-top:5px;font-size:11px;color:var(--muted)}
.cl-theme{padding:1px 7px;border:1px solid var(--border);border-radius:999px;background:var(--surface-alt);font-weight:600}
.cl-meta a{color:var(--blue)}
.cl-empty{margin-top:20px;color:var(--muted);font-size:13px}
.cl-foot{margin-top:28px;color:var(--muted);font-size:12px;line-height:1.6}
@media(max-width:520px){.cl-head h2{font-size:26px}.cl-filters{flex-wrap:nowrap;overflow-x:auto;padding-bottom:4px}.cl-chip{flex:0 0 auto}}
"""

_JS = """
(function(){
const data=JSON.parse(document.getElementById('changelogData').dataset.json);
const labels=Object.fromEntries(data.themes.map(t=>[t.id,t.label]));
const root=document.getElementById('changelogList'),filters=document.getElementById('changelogFilters');
let active='all';
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const MONTHS=['January','February','March','April','May','June','July','August','September','October','November','December'];
const nice=iso=>{const [y,m,d]=iso.split('-').map(Number);return d+' '+MONTHS[m-1]+' '+y};
function refLink(ref){const m=/^#(\\d+)$/.exec(ref);return m?`<a href="https://github.com/${data.repo}/pull/${m[1]}" target="_blank" rel="noopener">PR ${ref}</a>`:null}
function renderFilters(){
  const counts={};data.entries.forEach(e=>{counts[e.theme]=(counts[e.theme]||0)+1});
  const chips=[['all','All',data.entries.length]].concat(data.themes.filter(t=>counts[t.id]).map(t=>[t.id,t.label,counts[t.id]]));
  filters.innerHTML=chips.map(([id,label,n])=>`<button type="button" class="cl-chip" data-theme="${id}" aria-pressed="${id===active}">${esc(label)}<small>${n}</small></button>`).join('');
}
function renderList(){
  const rows=data.entries.filter(e=>active==='all'||e.theme===active);
  if(!rows.length){root.innerHTML='<p class="cl-empty">No entries for this theme yet.</p>';return}
  let html='',day='';
  rows.forEach(e=>{
    if(e.date!==day){if(day)html+='</div>';day=e.date;html+=`<div class="cl-day"><h4>${nice(day)}</h4>`}
    const links=e.refs.map(refLink).filter(Boolean).join(' ');
    html+=`<div class="cl-item"><strong>${esc(e.title)}</strong>${e.text?`<p>${esc(e.text)}</p>`:''}<div class="cl-meta"><span class="cl-theme">${esc(labels[e.theme]||e.theme)}</span>${links}</div></div>`;
  });
  root.innerHTML=html+'</div>';
}
filters.addEventListener('click',ev=>{const b=ev.target.closest('.cl-chip');if(!b)return;active=b.dataset.theme;renderFilters();renderList()});
renderFilters();renderList();
const summary=document.getElementById('changelogSummary');
if(summary&&data.entries.length){const dates=data.entries.map(e=>e.date).sort();summary.textContent=data.entries.length+' entries, from '+nice(dates[0])+' to '+nice(dates[dates.length-1])+'.'}

const views={overview:document.getElementById('aboutOverviewPane'),changelog:document.getElementById('aboutChangelogPane')};
const navTabs={overview:'[data-tab="about"]',changelog:'[data-tab="about-changelog"]'};
function showAboutView(name,updateUrl){
  if(!views[name])name='overview';
  Object.entries(views).forEach(([key,pane])=>{pane.hidden=key!==name});
  Object.entries(navTabs).forEach(([key,selector])=>{document.querySelectorAll(selector).forEach(b=>{const on=key===name;b.classList.toggle('active',on);b.setAttribute('aria-pressed',String(on))})});
  if(updateUrl){try{const url=new URL(location.href);if(name==='overview')url.searchParams.delete('about');else url.searchParams.set('about',name);history.replaceState(null,'',url.pathname+url.search+url.hash)}catch(e){}}
}
window.showAboutView=showAboutView;
try{showAboutView(new URLSearchParams(location.search).get('about')||'overview',false)}catch(e){}
})();
"""


def load_changelog() -> dict:
	if CHANGELOG_PATH.exists():
		return json.loads(CHANGELOG_PATH.read_text(encoding="utf-8"))
	return {"repo": "", "themes": [], "entries": []}


def about_panel_html(overview_fragment: str) -> str:
	"""Wrap the About overview and the changelog in two switchable views."""
	# Kept in an escaped attribute rather than a script block so no entry text can end a script early.
	soon = "".join(f"<li><b>{html.escape(name)}</b>{html.escape(text)}</li>" for _key, name, text in COMING_SOON)
	overview_fragment = overview_fragment.replace("<!--COMING_SOON_LIST-->", soon)
	data = html.escape(json.dumps(load_changelog(), ensure_ascii=False), quote=True)
	return (
		f"<style>{_CSS}</style>\n"
		f'<div id="aboutOverviewPane">\n{overview_fragment}\n</div>\n'
		'<div id="aboutChangelogPane" class="cl" hidden>\n'
		'<div class="cl-head"><div class="about-kicker">About \u00b7 Project timeline</div><h2>Changelog</h2><p class="cl-sub">What has been added, and when</p>'
		"<p>A running record of what has been added to iLit, newest first. It is built from the project\u2019s GitHub history "
		"(merged changes and commits) and written in plain language. Small fixes, documentation-only changes and test or build "
		'changes are left out. <span id="changelogSummary"></span></p></div>\n'
		'<div class="cl-filters" id="changelogFilters" role="group" aria-label="Filter by theme"></div>\n'
		'<div id="changelogList"></div>\n'
		'<p class="cl-foot">Refresh with <code>python scripts/build_changelog.py --refresh</code>. Entries are stored in '
		"<code>data/changelog/</code>; viewing this page makes no outside requests and uses no AI.</p>\n"
		"</div>\n"
		f'<div id="changelogData" data-json="{data}" hidden></div>\n'
		f"<script>{_JS}</script>"
	)
