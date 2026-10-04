"""Standalone, no-persistence legal proposition research page."""


def precedent_finder_page_html() -> str:
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Precedent Finder · AI CaseLibrary</title>
<style>
body{font:16px system-ui,sans-serif;margin:0;background:#f4f6fa;color:#182539}
main{max-width:900px;margin:auto;padding:24px}textarea{box-sizing:border-box;
width:100%;min-height:150px;font:inherit;padding:12px}button{font:inherit;
padding:10px 18px;margin:12px 8px 12px 0}article{background:white;border:1px solid
#cbd5e1;border-radius:8px;padding:16px;margin:16px 0;overflow-wrap:anywhere}
a{color:#184c98}button:focus-visible,a:focus-visible,textarea:focus-visible{
outline:3px solid #3570c9;outline-offset:3px}.muted{color:#43546a}
</style></head><body><main>
<a href="/data-explorer">Back to research</a>
<h1>Precedent Finder</h1>
<p>Find resolved authorities cited by decisions with matching V3 legal tags.
Research aid, not legal advice or an assessment of citation treatment.</p>
<p class="muted">Your proposition is used only for this request, not stored or
logged. No embeddings or external analysis. Do not include personal information.
Infrastructure outside this application may have its own logging policy.</p>
<form id="finder" autocomplete="off">
<label for="proposition">Legal proposition (up to 3000 characters)</label>
<textarea id="proposition" maxlength="3000" autocomplete="off"
spellcheck="false" placeholder="For example: procedural fairness and the duty to give reasons"></textarea>
<button id="submit" type="submit">Find authorities</button>
<button id="clear" type="button">Clear</button></form>
<div id="status" role="status" aria-live="polite"></div>
<section id="results" aria-label="Ranked authorities"></section>
<script>
const form=document.getElementById('finder'), input=document.getElementById('proposition');
const status=document.getElementById('status'), results=document.getElementById('results');
let generation=0;
function text(parent, tag, value) {
  const node=document.createElement(tag); node.textContent=value; parent.appendChild(node);
  return node;
}
function render(data) {
  results.replaceChildren();
  status.textContent=data.message || 'Authorities ranked by citing decisions, matched tags, then recency.';
  text(results,'p','Recognized V3 tags: '+(data.tags.join(', ') || 'none'));
  text(results,'p','Separate statute references: '+(data.statutes.join(', ') || 'none'));
  text(results,'p',data.coverage.note+(data.coverage.partial ? ' Search budgets reached: partial coverage.' : ''));
  for (const row of data.authorities) {
    const card=document.createElement('article'); results.appendChild(card);
    const heading=document.createElement('h2'); card.appendChild(heading);
    const link=text(heading,'a',row.citation);
    link.href='/data-explorer?case_id='+encodeURIComponent(row.case_id);
    text(card,'p','Court: '+row.court+' · Date: '+(row.date || 'not recorded'));
    text(card,'p',row.explanation);
    text(card,'p','Tags in matching citing decisions: '+row.matched_tags.join(', '));
    if (row.excerpt && row.excerpt_source) {
      const source=row.excerpt_source;
      const sourceLink=text(card,'a','Citing source paragraph: '+
        (source.source_citation || 'Case '+source.source_case_id)+
        ' · paragraph '+source.paragraph_number);
      sourceLink.href='/data-explorer?tab=search&case_id='+
        encodeURIComponent(source.source_case_id)+'&paragraph='+
        encodeURIComponent(source.paragraph_number);
      text(card,'blockquote',row.excerpt);
      text(card,'p',source.basis);
    }
    const mix=row.outcome_mix;
    text(card,'p','Outcome mix among matching citing decisions: government won '+mix.government_won+
      ', government lost '+mix.government_lost+', mixed '+mix.mixed+
      ', unclassified '+mix.unclassified+'; denominator '+mix.denominator+'.');
    text(card,'p',mix.basis);
  }
}
form.addEventListener('submit',async event=>{
  event.preventDefault();
  const request=++generation;
  results.replaceChildren(); status.textContent='Finding authorities…';
  try {
    const response=await fetch('/precedent-finder',{method:'POST',cache:'no-store',
      headers:{'Content-Type':'application/json'},body:JSON.stringify({proposition:input.value})});
    if (request!==generation) return;
    if (!response.ok) {
      status.textContent=response.status===413 ? 'Use at most 3000 characters.' :
        'Unable to analyze this request. Check the proposition and try again.';
      return;
    }
    const data=await response.json();
    if (request===generation) render(data);
  } catch {
    if (request===generation) status.textContent='Research service unavailable. Please try again.';
  }
});
document.getElementById('clear').addEventListener('click',()=>{
  ++generation; input.value=''; results.replaceChildren(); status.textContent=''; input.focus();
});
window.addEventListener('pagehide',()=>{++generation; input.value=''; results.replaceChildren();});
</script></main></body></html>"""
