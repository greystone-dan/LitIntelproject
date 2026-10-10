"""Live Analysis: "Find decided issues" block (default off; see backend/issue_match.py).

One pasted argument goes to /live-analysis/issue-matches and comes back as up to three decided issues,
each shown as a keyword match to check. Nothing is stored and no model is called.
"""

from __future__ import annotations

MATCH_HTML = r'''<div class="la-matches" id="laMatchesBox">
<h3>Find decided issues</h3>
<p class="la-note">Paste one argument from your draft. You get up to three decided issues with similar wording, who won on each, and the paragraph that says so. These are keyword matches to check, not confirmed precedents: no AI is used, and the text you paste is not stored.</p>
<label class="la-paste"><span class="la-sr">One argument from your draft</span><textarea id="laArg" rows="5" maxlength="4000" placeholder="Paste a paragraph that makes one argument, for example: The officer unreasonably discounted the applicant's establishment in Canada in refusing the humanitarian application."></textarea></label>
<div class="la-actions"><button type="button" class="la-go" id="laFind" disabled>Find decided issues</button><span class="la-status" id="laFindStatus" role="status"></span></div>
<div class="la-error" id="laFindError" role="alert" hidden></div>
<div id="laMatchResults" aria-live="polite"></div>
</div>
'''

STYLE = r'''<style>
.la-matches{max-width:820px;margin:22px 0 4px;padding-top:16px;border-top:1px solid var(--border)}
.la-matches h3{margin:0 0 6px;font:600 19px "Newsreader",serif}
.la-card{margin:12px 0;padding:12px 14px;border:1px solid var(--border);border-left:3px solid var(--teal,#176c68);border-radius:4px;background:var(--surface)}
.la-card .la-cite{font:600 13px "IBM Plex Sans",sans-serif}.la-card .la-cite a{color:var(--teal,#176c68)}
.la-card .la-issue{margin:6px 0;font-size:14px;line-height:1.5}
.la-card .la-res{margin:4px 0;font-size:13px;font-weight:600}
.la-card blockquote{margin:8px 0 0;padding:8px 12px;border-left:2px solid var(--border);background:var(--surface-alt);font:13px/1.55 Georgia,"Times New Roman",serif;max-height:11em;overflow:auto}
.la-card .la-warn{margin:6px 0 0;color:var(--muted);font-size:12px}
</style>
'''

SCRIPT = r'''<script>
(function(){
const $=id=>document.getElementById(id);
const box=$('laMatchesBox');if(!box)return;
const arg=$('laArg'),go=$('laFind'),status=$('laFindStatus'),err=$('laFindError'),out=$('laMatchResults');
const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const refresh=()=>{go.disabled=arg.value.trim().length<20};
arg.addEventListener('input',refresh);refresh();
function card(m){
  const cite=esc(m.citation||'No neutral citation')+(m.court?' ('+esc(m.court)+')':'');
  const link=m.case_url?`<a href="${esc(m.case_url)}" target="_blank" rel="noopener">${cite}</a>`:cite;
  const para=m.result_paragraph?`<blockquote>${m.result_paragraph_number?'['+esc(m.result_paragraph_number)+'] ':''}${esc(m.result_paragraph)}</blockquote>`:'';
  return `<div class="la-card"><div class="la-cite">${link}</div><div class="la-issue">${esc(m.issue)}</div><div class="la-res">${esc(m.result_label)}</div>${para}${m.note?`<div class="la-warn">${esc(m.note)}</div>`:''}</div>`;
}
go.addEventListener('click',async()=>{
  err.hidden=true;err.textContent='';out.innerHTML='';go.disabled=true;status.textContent='Searching…';
  try{
    const r=await fetch('/live-analysis/issue-matches',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text:arg.value})});
    if(!r.ok)throw new Error(r.status===404?'Decided-issue search is not switched on.':'The search could not run. Check that the argument is at least 20 characters.');
    const d=await r.json();
    status.textContent=`Searched ${d.library_issues} issues from ${d.library_decisions} decisions (2005 and later, immigration).`;
    out.innerHTML=d.matches.length?d.matches.map(card).join('')+`<p class="la-note">${esc(d.basis)}</p>`:'<p class="la-note">No close match in the library. That does not mean there is no precedent; it means none of the decisions loaded here use similar wording.</p>';
  }catch(e){err.textContent=e.message;err.hidden=false;status.textContent=''}
  finally{refresh()}
});
})();
</script>
'''
