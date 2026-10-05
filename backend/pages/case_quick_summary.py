"""Additive stored-evidence summary for the formatted inline case reader."""

QUICK_SUMMARY_JS = r"""
/* Quick summary: stored data only; independent of the extracted/technical cards. */
const quickSummaryState={generation:0,caseId:null,status:'idle',data:null,controller:null,open:false};
function quickSummaryEscape(value){
    return String(value??'').replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
}
function quickSummaryVerifiedEvidence(evidence,payload){
    if(!evidence||typeof evidence.text!=='string'||!evidence.text)return false;
    const {start,end,block_start,paragraph_number}=evidence;
    if(![start,end,block_start,paragraph_number].every(Number.isInteger)||
       start<0||end<=start||block_start<0||paragraph_number<0)return false;
    const blocks=payload?.readerData?.format_blocks||[];
    const index=blocks.findIndex(block=>block.type==='para'&&block.start===block_start&&block.num===paragraph_number);
    if(index<0)return false;
    let paragraphEnd=blocks[index].end;
    for(let i=index+1;i<blocks.length&&['text','quote','listitem'].includes(blocks[i].type);i++)paragraphEnd=blocks[i].end;
    const chars=Array.from(payload?.item?.full_text||'');
    return Number.isInteger(paragraphEnd)&&block_start<=start&&end<=paragraphEnd&&
        end<=chars.length&&chars.slice(start,end).join('')===evidence.text;
}
function quickSummaryEvidenceHtml(evidence,payload){
    if(!quickSummaryVerifiedEvidence(evidence,payload))return '';
    return `<blockquote style="white-space:pre-wrap">${quickSummaryEscape(evidence.text)}</blockquote>`+
        `<a href="#decision-source-${evidence.block_start}" data-quick-summary-start="${evidence.block_start}" `+
        `data-quick-summary-paragraph="${evidence.paragraph_number}">Source paragraph [${evidence.paragraph_number}]</a>`;
}
function quickSummaryHtml(data,payload){
    const esc=quickSummaryEscape;
    const facts=[['Style of cause',data.style_of_cause],['Citation',data.citation],['Court',data.court],['Date',data.date]]
        .filter(([,value])=>typeof value==='string'&&value.trim())
        .map(([label,value])=>`<dt>${label}</dt><dd>${esc(value)}</dd>`).join('');
    const statutes=(Array.isArray(data.top_statutes)?data.top_statutes:[]).slice(0,5)
        .map(row=>`<li><strong>${esc(row.instrument_key)}</strong> · ${esc(row.count)} stored occurrence(s)`+
            quickSummaryEvidenceHtml(row.evidence,payload)+'</li>').join('');
    const tags=(Array.isArray(data.top_tags)?data.top_tags:[])
        .filter(row=>row&&quickSummaryVerifiedEvidence(row.evidence,payload)).slice(0,5)
        .map(row=>`<li><strong>${esc(row.category)}: ${esc(row.value)}</strong> · score ${esc(row.score)} · source ${esc(row.source)}`+
            quickSummaryEvidenceHtml(row.evidence,payload)+'</li>').join('');
    const issueLabel=data.issue?.kind==='standard_of_review'?'Standard of review':'Issue';
    const disposition=quickSummaryEvidenceHtml(data.disposition,payload);
    const issue=quickSummaryEvidenceHtml(data.issue,payload);
    return `<p>Stored research aid, not a generated legal conclusion. Verify against the decision.</p>`+
        `<dl class="rs-facts">${facts}<dt>Decision outcome</dt><dd>${esc(data.decision_outcome&&data.decision_outcome!=='unclear'?data.decision_outcome:'unclassified')} · source: ${esc(data.outcome_source||'unknown')}</dd></dl>`+
        (disposition?`<h4>Disposition · verbatim</h4>${disposition}`:'')+
        (issue?`<h4>${issueLabel} · verbatim</h4>${issue}`:'')+
        (statutes?`<h4>Top statutes · stored occurrences</h4><ul>${statutes}</ul>`:'')+
        (tags?`<h4>Top tags · stored scores and provenance</h4><ul>${tags}</ul>`:'');
}
function mountQuickSummary(){
    const body=document.getElementById('decisionBody'),state=quickSummaryState;
    if(!body)return;
    body.querySelectorAll('.reader-quick-summary').forEach(node=>node.remove());
    if(state.caseId===null||readerState.caseId!==state.caseId||!readerState.payload||
       readerState.mode==='chunks'||readerState.formatted===false||document.getElementById('caseReaderPanel')?.hidden)return;
    const content=state.status==='ready'?quickSummaryHtml(state.data,readerState.payload):
        `<p role="status">${state.status==='error'?'Quick summary unavailable. The decision and existing reader tools remain available.':'Loading stored quick summary…'}</p>`;
    body.insertAdjacentHTML('afterbegin',`<details class="rs-card reader-quick-summary" ${state.open?'open':''} `+
        `aria-label="Quick summary" style="overflow-wrap:anywhere"><summary style="cursor:pointer"><strong>Quick summary</strong></summary>${content}</details>`);
    const panel=body.querySelector('.reader-quick-summary');
    panel?.addEventListener('toggle',()=>{if(panel.isConnected)state.open=panel.open;});
}
function resetQuickSummary(caseId=null){
    quickSummaryState.controller?.abort();
    Object.assign(quickSummaryState,{generation:quickSummaryState.generation+1,caseId,status:'idle',data:null,controller:null,open:false});
    document.getElementById('decisionBody')?.querySelectorAll('.reader-quick-summary').forEach(node=>node.remove());
}
async function loadQuickSummary(caseId,generation){
    const controller=new AbortController();
    quickSummaryState.controller=controller;
    quickSummaryState.status='loading';
    const timer=setTimeout(()=>controller.abort(),10000);
    try{
        const response=await fetch(`/api/cases/${encodeURIComponent(caseId)}/summary`,{method:'GET',signal:controller.signal});
        if(!response.ok)throw new Error('Summary unavailable');
        const data=await response.json();
        if(quickSummaryState.generation!==generation||quickSummaryState.caseId!==caseId)return;
        if(!data||data.case_id!==caseId)throw new Error('Summary identity mismatch');
        quickSummaryState.data=data;
        quickSummaryState.status='ready';
    }catch(error){
        if(quickSummaryState.generation!==generation||quickSummaryState.caseId!==caseId)return;
        quickSummaryState.status='error';
    }finally{
        clearTimeout(timer);
        if(quickSummaryState.generation===generation){
            quickSummaryState.controller=null;
            try{mountQuickSummary();}catch(error){/* Never disrupt the existing reader. */}
        }
    }
}
function adoptLoadedQuickSummary(){
    // The earlier main script may already have started a case_id deep-link
    // load before this additive script installs its openDecision wrapper.
    if(quickSummaryState.caseId===null&&Number.isInteger(readerState.caseId)&&readerState.payload&&
       !document.getElementById('caseReaderPanel')?.hidden){
        resetQuickSummary(readerState.caseId);
        void loadQuickSummary(readerState.caseId,quickSummaryState.generation);
    }
}
const quickSummaryPreviousMode=setReaderMode;
setReaderMode=function(mode){
    quickSummaryPreviousMode(mode);
    adoptLoadedQuickSummary();
    try{mountQuickSummary();}catch(error){/* Existing reader remains usable. */}
};
const quickSummaryPreviousOpen=openDecision;
openDecision=async function(caseId){
    resetQuickSummary(caseId);
    const generation=quickSummaryState.generation;
    void loadQuickSummary(caseId,generation);
    try{return await quickSummaryPreviousOpen(caseId);}
    finally{if(quickSummaryState.generation===generation){try{mountQuickSummary();}catch(error){}}}
};
const quickSummaryPreviousClose=closeDecisionReader;
closeDecisionReader=function(){resetQuickSummary();return quickSummaryPreviousClose();};
document.getElementById('decisionBody')?.addEventListener('click',event=>{
    const link=event.target.closest?.('[data-quick-summary-start]');
    if(!link)return;
    event.preventDefault();
    const start=Number(link.dataset.quickSummaryStart),paragraph=Number(link.dataset.quickSummaryParagraph);
    const state=quickSummaryState,payload=readerState.payload;
    if(state.status!=='ready'||readerState.caseId!==state.caseId||!payload)return;
    const evidence=[state.data.disposition,state.data.issue,...(state.data.top_statutes||[]).map(row=>row.evidence),
        ...(state.data.top_tags||[]).map(row=>row.evidence)]
        .find(row=>row?.block_start===start&&row?.paragraph_number===paragraph&&quickSummaryVerifiedEvidence(row,payload));
    if(!evidence)return;
    const target=document.getElementById('decisionBody')?.querySelector(`[id="decision-source-${start}"]`);
    if(!target)return;
    target.closest('details')?.setAttribute('open','');
    target.setAttribute('tabindex','-1');
    target.scrollIntoView({block:'center',behavior:window.matchMedia?.('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});
    target.focus({preventScroll:true});
});
// Also cover a deep-link load that completed before this script was installed.
try{adoptLoadedQuickSummary();mountQuickSummary();}catch(error){/* Existing reader remains usable. */}
"""


def inject_case_quick_summary(html: str) -> str:
    """Install after existing reader hooks without replacing their cards."""
    return html.replace("</body>", "<script>\n" + QUICK_SUMMARY_JS + "\n</script>\n</body>", 1)
