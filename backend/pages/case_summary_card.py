"""Formatted-reader card for the API's extractive case-summary projection."""

SUMMARY_CARD_JS = r"""
/* Extractive case summary card: exact selected paragraphs, no generated prose. */
const extractiveSummaryState={generation:0,caseId:null,status:'idle',data:null,controller:null};
function extractiveSummaryEscape(value){
    return String(value??'').replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
}
function extractiveSummaryHasData(data){
    return Boolean(data&&(
        (typeof data.citation==='string'&&data.citation.trim())||
        (typeof data.court==='string'&&data.court.trim())||data.date||
        (data.judge&&typeof data.judge.name==='string'&&data.judge.name.trim())||
        (data.outcome&&typeof data.outcome.value==='string'&&data.outcome.value.trim())||
        (Array.isArray(data.statutes)&&data.statutes.length)||
        (Array.isArray(data.top_tags)&&data.top_tags.length)||
        (Array.isArray(data.key_paragraphs)&&data.key_paragraphs.length)
    ));
}
function extractiveSummaryVerifiedParagraph(row,payload=readerState.payload){
    if(!row||typeof row.text!=='string'||!row.text||!payload)return false;
    const {start,end,block_start,paragraph_number}=row;
    if(![start,end,block_start,paragraph_number].every(Number.isInteger)||
       start<0||end<=start||block_start!==start||paragraph_number<0)return false;
    const blocks=payload?.readerData?.format_blocks||[];
    const index=blocks.findIndex(block=>block.type==='para'&&
        block.start===block_start&&block.num===paragraph_number);
    if(index<0)return false;
    let paragraphEnd=blocks[index].end;
    for(let i=index+1;i<blocks.length&&['text','quote','listitem'].includes(blocks[i].type);i++){
        paragraphEnd=blocks[i].end;
    }
    const chars=Array.from(payload?.item?.full_text||'');
    return end===paragraphEnd&&end<=chars.length&&
        chars.slice(start,end).join('')===row.text;
}
function extractiveSummaryTruncate(text,limit=640){
    const value=String(text??'');
    if(value.length<=limit)return {text:value,truncated:false};
    const boundaries=[];
    const punctuation=/[.!?](?=\s|$)/g;
    let match;
    while((match=punctuation.exec(value))!==null){
        const end=match.index+1;
        const token=value.slice(Math.max(0,value.lastIndexOf(' ',match.index)+1),match.index);
        if(match[0]==='.'&&(value[match.index-1]==='.'||value[match.index+1]==='.'))continue;
        if(match[0]==='.'&&/^(?:[A-Z]|Mr|Mrs|Ms|Dr|Prof|No|para|paras|s|ss|Ltd|Inc|Corp|etc|cf|viz|approx|dept|v)$/i.test(token))continue;
        boundaries.push(end);
    }
    const inRange=boundaries.filter(end=>end<=limit);
    const end=inRange.length?inRange[inRange.length-1]:boundaries.find(valueEnd=>valueEnd>limit&&valueEnd<=limit*1.5);
    if(!end)return {text:value,truncated:false};
    return {text:value.slice(0,end).trimEnd()+'…',truncated:true};
}
function extractiveSummarySourceLink(row){
    const start=Number(row?.block_start),paragraph=Number(row?.paragraph_number);
    if(!Number.isInteger(start)||start<0||!Number.isInteger(paragraph)||paragraph<0)return '';
    return `<a href="#decision-source-${start}" data-extractive-summary-start="${start}" `+
        `data-extractive-summary-paragraph="${paragraph}">View full paragraph [${paragraph}]</a>`;
}
function extractiveSummaryHtml(data){
    const esc=extractiveSummaryEscape;
    const facts=[
        ['Citation',data.citation],['Court',data.court],['Date',data.date],
        ['Judge',data.judge?.name],
        ['Outcome',data.outcome?.value],
    ].filter(([,value])=>typeof value==='string'&&value.trim())
      .map(([label,value])=>`<dt>${label}</dt><dd>${esc(value)}</dd>`).join('');
    const outcomeSource=data.outcome?.source?
        `<p class="extractive-summary-source">Outcome source: ${esc(data.outcome.source)}`+
        (data.outcome.status?` · status: ${esc(data.outcome.status)}`:'')+
        (Number.isFinite(data.outcome.confidence)?` · confidence: ${esc(data.outcome.confidence)}`:'')+
        `</p>`:'';
    const statutes=(Array.isArray(data.statutes)?data.statutes:[])
        .filter(row=>row&&typeof row.instrument_key==='string'&&row.instrument_key.trim())
        .slice(0,5).map(row=>`<li><strong>${esc(row.instrument_key)}</strong> · ${esc(row.count)} stored mention(s)</li>`).join('');
    const tags=(Array.isArray(data.top_tags)?data.top_tags:[])
        .filter(row=>row&&typeof row.category==='string'&&typeof row.value==='string')
        .slice(0,5).map(row=>`<li><strong>${esc(row.category)}: ${esc(row.value)}</strong> · `+
            `score ${esc(row.score)} · source ${esc(row.source)}</li>`).join('');
    const paragraphs=(Array.isArray(data.key_paragraphs)?data.key_paragraphs:[])
        .filter(row=>extractiveSummaryVerifiedParagraph(row))
        .slice(0,3).map(row=>{
            const excerpt=extractiveSummaryTruncate(row.text);
            const count=Number.isInteger(row.pinpoint_citation_count)?
                ` · ${esc(row.pinpoint_citation_count)} later pinpoint citation(s)`: '';
            return `<li><p>${esc(excerpt.text)}</p><small>${esc(row.selection_rule||'Stored source paragraph')}${count}</small>`+
                extractiveSummarySourceLink(row)+'</li>';
        }).join('');
    return `<p class="extractive-summary-notice">Selected passages, not a summary written by AI</p>`+
        (facts?`<dl>${facts}</dl>${outcomeSource}`:'')+
        (statutes?`<h4>Statutes cited · stored mentions</h4><ul>${statutes}</ul>`:'')+
        (tags?`<h4>Top tags · separate stored layer</h4><ul>${tags}</ul>`:'')+
        (paragraphs?`<h4>Key paragraphs</h4><ol>${paragraphs}</ol>`:'');
}
function mountExtractiveSummaryCard(){
    const body=document.getElementById('decisionBody'),state=extractiveSummaryState;
    if(!body)return;
    body.querySelectorAll('.reader-extractive-summary').forEach(node=>node.remove());
    if(state.status!=='ready'||!extractiveSummaryHasData(state.data)||
       state.caseId===null||readerState.caseId!==state.caseId||!readerState.payload||
       readerState.mode==='chunks'||readerState.formatted===false||
       document.getElementById('caseReaderPanel')?.hidden)return;
    body.insertAdjacentHTML('afterbegin',
        `<details class="rs-card reader-extractive-summary" aria-label="Quick summary — selected passages" style="overflow-wrap:anywhere">`+
        `<summary style="cursor:pointer"><strong>Quick summary</strong> · selected passages</summary>`+
        extractiveSummaryHtml(state.data)+'</details>');
}
function resetExtractiveSummaryCard(caseId=null){
    extractiveSummaryState.controller?.abort();
    Object.assign(extractiveSummaryState,{
        generation:extractiveSummaryState.generation+1,caseId,status:'idle',data:null,controller:null
    });
    document.getElementById('decisionBody')?.querySelectorAll('.reader-extractive-summary').forEach(node=>node.remove());
}
async function loadExtractiveSummaryCard(caseId,generation){
    const controller=new AbortController();
    extractiveSummaryState.controller=controller;
    const timer=setTimeout(()=>controller.abort(),10000);
    try{
        const response=await fetch(`/api/cases/${encodeURIComponent(caseId)}/summary-card`,{
            method:'GET',signal:controller.signal
        });
        if(!response.ok)throw new Error('Summary card unavailable');
        const data=await response.json();
        if(extractiveSummaryState.generation!==generation||extractiveSummaryState.caseId!==caseId)return;
        if(!data||Number(data.case_id)!==Number(caseId))throw new Error('Summary card identity mismatch');
        extractiveSummaryState.data=data;
        extractiveSummaryState.status='ready';
    }catch(error){
        if(extractiveSummaryState.generation!==generation||extractiveSummaryState.caseId!==caseId)return;
        extractiveSummaryState.status='error';
    }finally{
        clearTimeout(timer);
        if(extractiveSummaryState.generation===generation){
            extractiveSummaryState.controller=null;
            try{mountExtractiveSummaryCard();}catch(error){/* Never disrupt the existing reader. */}
        }
    }
}
function adoptLoadedExtractiveSummaryCard(){
    if(extractiveSummaryState.caseId===null&&Number.isInteger(readerState.caseId)&&readerState.payload&&
       !document.getElementById('caseReaderPanel')?.hidden){
        resetExtractiveSummaryCard(readerState.caseId);
        void loadExtractiveSummaryCard(readerState.caseId,extractiveSummaryState.generation);
    }
}
const extractiveSummaryPreviousMode=setReaderMode;
setReaderMode=function(mode){
    extractiveSummaryPreviousMode(mode);
    adoptLoadedExtractiveSummaryCard();
    try{mountExtractiveSummaryCard();}catch(error){/* Preserve the existing reader. */}
};
const extractiveSummaryPreviousOpen=openDecision;
openDecision=async function(caseId){
    resetExtractiveSummaryCard(caseId);
    const generation=extractiveSummaryState.generation;
    void loadExtractiveSummaryCard(caseId,generation);
    try{return await extractiveSummaryPreviousOpen(caseId);}
    finally{if(extractiveSummaryState.generation===generation){
        try{mountExtractiveSummaryCard();}catch(error){/* Preserve the existing reader. */}
    }}
};
const extractiveSummaryPreviousClose=closeDecisionReader;
closeDecisionReader=function(){
    resetExtractiveSummaryCard();
    return extractiveSummaryPreviousClose();
};
document.getElementById('decisionBody')?.addEventListener('click',event=>{
    const link=event.target.closest?.('[data-extractive-summary-start]');
    if(!link)return;
    event.preventDefault();
    const start=Number(link.dataset.extractiveSummaryStart);
    const paragraph=Number(link.dataset.extractiveSummaryParagraph);
    const selected=(extractiveSummaryState.data?.key_paragraphs||[]).find(row=>
        row.block_start===start&&row.paragraph_number===paragraph&&
        extractiveSummaryVerifiedParagraph(row,readerState.payload));
    if(!selected||readerState.caseId!==extractiveSummaryState.caseId||!readerState.payload)return;
    setReaderMode('normalized');
    const confirmed=document.getElementById('decisionBody')?.querySelector(`[id="decision-source-${start}"]`);
    if(!confirmed)return;
    confirmed.setAttribute('tabindex','-1');
    confirmed.scrollIntoView({block:'center',behavior:
        window.matchMedia?.('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});
    confirmed.focus({preventScroll:true});
});
try{adoptLoadedExtractiveSummaryCard();mountExtractiveSummaryCard();}catch(error){/* Reader remains usable. */}
"""


def inject_case_summary_card(html: str) -> str:
    """Install the independent extractive card after the existing reader tools."""
    style = """
<style>
.reader-extractive-summary{margin:12px 0;padding:12px 14px;border:1px solid var(--border);border-radius:8px;background:var(--surface-alt);color:var(--text);font-size:12px;line-height:1.6}
.reader-extractive-summary>summary{font-size:13px}
.reader-extractive-summary dt{font-weight:700;color:var(--muted)}
.reader-extractive-summary dd{margin:0 0 6px}
.reader-extractive-summary ul,.reader-extractive-summary ol{margin:4px 0 10px;padding-left:22px}
.reader-extractive-summary li{margin:7px 0}
.reader-extractive-summary p{margin:4px 0}
.extractive-summary-notice,.extractive-summary-source{color:var(--muted);font-size:11px}
.reader-extractive-summary small{display:block;color:var(--muted);font-size:10px}
.reader-extractive-summary a{display:inline-block;margin-top:3px;color:var(--navy);font-weight:600}
</style>
"""
    result = html.replace("</head>", style + "\n</head>", 1)
    return result.replace("</body>", "<script>\n" + SUMMARY_CARD_JS + "\n</script>\n</body>", 1)
