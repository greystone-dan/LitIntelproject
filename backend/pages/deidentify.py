from __future__ import annotations


def deidentify_page_html() -> str:
	return r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>De-identify | iLit</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--ink:#182421;--muted:#66756f;--paper:#e8eee9;--surface:#fbfdf9;--line:#cbd8d0;--teal:#087f73;--rust:#bd5638;--gold:#c18a25;--mark:#fdeccc}
*{box-sizing:border-box}
body{margin:0;color:var(--ink);font-family:Manrope,sans-serif;background:linear-gradient(135deg,#eef3ed,#e5ece8);min-height:100vh}
header{min-height:72px;padding:12px 5vw;display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line);background:rgba(251,253,249,.84)}
.brand{font-size:18px;font-weight:800;letter-spacing:.02em}.brand small{display:block;color:var(--muted);font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase}
.nav{display:flex;flex-wrap:wrap;gap:8px}.nav a{padding:8px 10px;color:var(--muted);font-size:11px;text-decoration:none;border-radius:4px}.nav a:hover,.nav a.active{color:var(--ink);background:#dce9e2}
.wrap{width:min(1100px,calc(100% - 32px));margin:0 auto;padding:44px 0 70px}
.eyebrow{color:var(--rust);font:500 11px/1 "DM Mono",monospace;letter-spacing:.12em;text-transform:uppercase}
h1{margin:12px 0 10px;font-size:clamp(30px,5vw,52px);line-height:1.04;letter-spacing:-.03em}
.lead{max-width:680px;color:var(--muted);font-size:15px;line-height:1.65}
.privacy{margin-top:18px;padding:12px 14px;border-left:3px solid var(--teal);background:#eaf5f0;font-size:13px;line-height:1.55;max-width:760px}
.steps{display:flex;gap:6px;margin-top:30px}
.step{height:40px;padding:0 16px;border:1px solid var(--line);border-bottom:0;border-radius:6px 6px 0 0;background:#dfe8e2;color:var(--muted);font:700 13px Manrope,sans-serif;cursor:pointer}
.step[aria-selected="true"]{background:var(--surface);color:var(--ink)}
.panel{padding:24px;border:1px solid var(--line);background:var(--surface);box-shadow:0 18px 50px rgba(24,36,33,.07)}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:20px}
@media (max-width:760px){.cols{grid-template-columns:1fr}.panel{padding:16px}}
label.field{display:block;margin:0 0 6px;font-size:12px;font-weight:700}
.hint{margin:4px 0 0;color:var(--muted);font-size:11px;line-height:1.45}
textarea{width:100%;min-height:110px;padding:10px;border:1px solid var(--line);border-radius:4px;background:white;font:13px/1.5 Manrope,sans-serif;resize:vertical}
textarea.big{min-height:150px}
.drop{display:grid;place-items:center;min-height:120px;padding:18px;border:1px dashed #8da89b;background:#f4f8f4;text-align:center;cursor:pointer;border-radius:4px}
.drop:hover,.drop.drag{border-color:var(--teal);background:#eaf5f0}.drop strong{display:block;font-size:15px}.drop span{display:block;margin-top:6px;color:var(--muted);font-size:12px}.drop input{display:none}
.or{margin:10px 0;color:var(--muted);font-size:11px;text-align:center}
.block,label.field.block{margin-top:18px}
details.opts{margin-top:18px;font-size:12px}details.opts summary{cursor:pointer;font-weight:700}
.checks{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:6px;margin-top:10px}.checks label{display:flex;gap:6px;align-items:center}
.actions{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-top:18px}
.button{height:40px;padding:0 15px;border:0;border-radius:4px;background:var(--ink);color:white;font:700 12px Manrope;cursor:pointer}
.button.secondary{border:1px solid var(--line);background:transparent;color:var(--ink)}
.button.key{background:var(--rust)}
.button:disabled{opacity:.45;cursor:wait}
.status{color:var(--muted);font-size:12px}
.error{margin-top:16px;padding:12px;border-left:3px solid var(--rust);background:#fff3ee;color:#87341f;font-size:13px}
.warn{margin-top:12px;padding:10px 12px;border-left:3px solid var(--gold);background:#fff8e8;font-size:12px;line-height:1.5}
.warn ul{margin:4px 0 0;padding-left:18px}
.hidden{display:none!important}
.result{margin-top:28px;border-top:1px solid var(--line);padding-top:20px}
.result h2{margin:0 0 10px;font-size:20px}
.chips{display:flex;flex-wrap:wrap;gap:6px}.chip{padding:5px 9px;border-radius:999px;background:#dce9e2;font-size:11px}.chip strong{margin-right:4px}
.preview{margin-top:14px;max-height:520px;overflow:auto;padding:16px;border:1px solid var(--line);background:white;font:13px/1.65 Manrope,sans-serif;white-space:pre-wrap;overflow-wrap:anywhere}
.preview mark{padding:0 2px;border-radius:3px;background:var(--mark);color:#6b4708;font:500 12px "DM Mono",monospace}
.keytable{width:100%;margin-top:10px;border-collapse:collapse;font-size:12px}.keytable td{padding:5px 8px;border-bottom:1px solid var(--line);vertical-align:top;overflow-wrap:anywhere}.keytable td:first-child{font-family:"DM Mono",monospace;white-space:nowrap;color:#6b4708}
.toggle{display:flex;gap:8px;align-items:center;font-size:13px}
textarea.small{min-height:70px}
.names-box{margin-top:14px;padding:12px;border:1px solid var(--line);border-radius:4px;background:#f7faf7;font-size:12px}
.names-box .chips{margin-top:8px}
.chip button{margin-left:6px;padding:1px 6px;border:1px solid var(--line);border-radius:999px;background:white;font:600 10px Manrope,sans-serif;cursor:pointer}
.chip.off{opacity:.45;text-decoration:line-through}
.chip em{color:var(--muted);font-style:normal;margin-left:4px}
.rerun{margin-top:12px;display:flex;gap:10px;align-items:center;font-size:12px;font-weight:700}
.keynote{margin-top:12px;font-size:12px;color:#87341f}
</style>
</head>
<body>
<header><div class="brand">ILIT <small>De-identify documents</small></div><nav class="nav"><a href="/data-explorer">Research</a><a href="/citation-map">Citation Map</a><a href="/live-analysis">Live Analysis</a><a class="active" href="/deidentify">De-identify</a></nav></header>
<main class="wrap">
<div class="eyebrow">Private materials</div>
<h1>De-identify a document, then put it back together</h1>
<p class="lead">People's names (found automatically, plus any you add), ID numbers, contact details, specific dates and ages are swapped for placeholders like <code>[PERSON_1]</code>, following how published RPD decisions are redacted. Countries and employment are left in. Later, the key file puts the real details back.</p>
<div class="privacy"><strong>Nothing is saved.</strong> Your file is read in memory, the result is sent back to this page, and the server forgets it. It is never added to the case library. The <strong>key file</strong> is the only copy of the hidden details, and it is downloaded to your computer. Keep it private.</div>

<div class="steps" role="tablist">
<button class="step" type="button" role="tab" id="tabDeid" aria-selected="true" data-step="deid">1. De-identify</button>
<button class="step" type="button" role="tab" id="tabRestore" aria-selected="false" data-step="restore">2. Restore</button>
</div>

<section class="panel" id="panelDeid">
<div class="cols">
<div>
<label class="field">Document</label>
<label class="drop" id="deidDrop"><input type="file" id="deidFile" accept=".docx,.pdf,.txt"><div><strong id="deidFileName">Choose or drop a file</strong><span>Word (.docx), PDF with selectable text, or .txt · up to 10 MB</span></div></label>
<div class="or">or paste text</div>
<textarea id="deidText" class="big" placeholder="Paste text here"></textarea>
</div>
<div>
<label class="toggle"><input type="checkbox" id="autoNames" checked> <strong>Find names automatically</strong></label>
<p class="hint">A language model on the iLit server looks for people's names. Nothing is sent anywhere else. Names in cited cases (Vavilov, Baker) and judges' names are left in.</p>
<label class="field block" for="names">Always hide these people</label>
<textarea id="names" placeholder="One person per line, e.g.&#10;Maria Elena Lopez&#10;Juan Perez"></textarea>
<p class="hint">Add anyone the automatic search missed, one full name per line. The tool also catches the surname or given name on its own, "Lopez, Maria", plurals and ALL-CAPS spellings.</p>
<label class="field block" for="details">Other details to hide</label>
<textarea id="details" placeholder="One per line, e.g. a home town, a church, a school"></textarea>
<p class="hint">Anything else that could point to the person: a small town, an organization, a school, a nickname.</p>
<label class="field block" for="neverHide">Never hide</label>
<textarea id="neverHide" class="small" placeholder="Names found by mistake, one per line"></textarea>
</div>
</div>
<details class="opts"><summary>What gets hidden automatically</summary><div class="checks" id="categoryChecks"></div></details>
<div class="actions"><button class="button" id="runDeid" type="button">De-identify</button><span class="status" id="deidStatus"></span></div>
<div class="error hidden" id="deidError"></div>

<div class="result hidden" id="deidResult">
<h2>De-identified text</h2>
<div class="chips" id="deidChips"></div>
<div class="warn hidden" id="deidWarn"></div>
<div class="names-box hidden" id="foundBox"><strong>Names found automatically</strong> <span class="hint">These are hidden. Click "Don't hide" on any that are not people, or are fine to share.</span><div class="chips" id="foundChips"></div></div>
<div class="names-box hidden" id="keptBox"><strong>Left in on purpose</strong> <span class="hint">Public names. Click "Hide" if one is actually someone in your file.</span><div class="chips" id="keptChips"></div></div>
<div class="rerun hidden" id="rerunNote">Lists changed. <button class="button" id="rerun" type="button">Run again</button></div>
<div class="warn">Read the preview before using it. Automatic detection can miss things, for example a name you did not list, or a detail only the person would have. Add anything you spot to the lists above and run it again.</div>
<div class="actions">
<button class="button key" id="saveKey" type="button">Download key file</button>
<button class="button secondary" id="copyDeid" type="button">Copy text</button>
<button class="button secondary" id="saveDeidTxt" type="button">Download .txt</button>
<button class="button secondary" id="saveDeidDocx" type="button">Download .docx</button>
</div>
<p class="keynote">Download the key file before leaving this page. Without it the details cannot be put back.</p>
<div class="preview" id="deidPreview"></div>
<details class="opts"><summary>Review what was hidden (<span id="keyCount">0</span> placeholders)</summary><table class="keytable" id="keyTable"></table></details>
</div>
</section>

<section class="panel hidden" id="panelRestore">
<div class="cols">
<div>
<label class="field">Processed document (with placeholders)</label>
<label class="drop" id="restoreDrop"><input type="file" id="restoreFile" accept=".docx,.pdf,.txt"><div><strong id="restoreFileName">Choose or drop a file</strong><span>.docx, .pdf or .txt</span></div></label>
<div class="or">or paste text</div>
<textarea id="restoreText" class="big" placeholder="Paste the text that contains [PERSON_1] style placeholders"></textarea>
</div>
<div>
<label class="field">Key file</label>
<label class="drop" id="keyDrop"><input type="file" id="keyFile" accept=".json,application/json"><div><strong id="keyFileName">Choose or drop the key file</strong><span>The .json file saved in step 1</span></div></label>
<p class="hint" id="sessionKeyHint"></p>
</div>
</div>
<div class="actions"><button class="button" id="runRestore" type="button">Restore details</button><span class="status" id="restoreStatus"></span></div>
<div class="error hidden" id="restoreError"></div>
<div class="result hidden" id="restoreResult">
<h2>Restored text</h2>
<div class="chips" id="restoreChips"></div>
<div class="warn hidden" id="restoreWarn"></div>
<div class="actions">
<button class="button secondary" id="copyRestore" type="button">Copy text</button>
<button class="button secondary" id="saveRestoreTxt" type="button">Download .txt</button>
<button class="button secondary" id="saveRestoreDocx" type="button">Download .docx</button>
</div>
<div class="preview" id="restorePreview"></div>
</div>
</section>
</main>
<script>
const CATEGORIES=[['EMAIL','Email addresses'],['PHONE','Phone numbers'],['SIN','Social insurance numbers'],['UCI','UCI / client ID numbers'],['APPLICATION','IRCC application numbers'],['IRB_FILE','IRB file numbers (TB9-12345)'],['COURT_FILE','Federal Court file numbers (IMM-1234-25)'],['PASSPORT','Passport numbers'],['ID','Other numbered IDs ("file no.", "permit no.")'],['ADDRESS','Street addresses'],['POSTAL','Postal codes'],['DATE','Specific dates (day, month, year)'],['AGE','Ages']];
const $=id=>document.getElementById(id);
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[c]);
let deidResult=null,restoreResult=null,sessionKey=null,loadedKey=null,sourceName='document';
$('categoryChecks').innerHTML=CATEGORIES.map(([v,l])=>`<label><input type="checkbox" value="${v}" checked> ${esc(l)}</label>`).join('');

function showStep(step){for(const [tab,panel,name] of [['tabDeid','panelDeid','deid'],['tabRestore','panelRestore','restore']]){$(tab).setAttribute('aria-selected',String(step===name));$(panel).classList.toggle('hidden',step!==name)}
  $('sessionKeyHint').textContent=sessionKey&&!loadedKey?'No key file chosen: the key from step 1 on this page will be used.':''}
document.querySelectorAll('.step').forEach(b=>b.onclick=()=>showStep(b.dataset.step));

function wireDrop(dropId,inputId,nameId,onFile){const drop=$(dropId),input=$(inputId);
  input.onchange=()=>{if(input.files[0]){$(nameId).textContent=input.files[0].name;onFile&&onFile(input.files[0])}};
  drop.addEventListener('dragover',e=>{e.preventDefault();drop.classList.add('drag')});
  drop.addEventListener('dragleave',()=>drop.classList.remove('drag'));
  drop.addEventListener('drop',e=>{e.preventDefault();drop.classList.remove('drag');if(e.dataTransfer.files[0]){input.files=e.dataTransfer.files;input.onchange()}})}
wireDrop('deidDrop','deidFile','deidFileName');
wireDrop('restoreDrop','restoreFile','restoreFileName');
wireDrop('keyDrop','keyFile','keyFileName',async file=>{try{loadedKey=JSON.parse(await file.text());$('restoreError').classList.add('hidden')}catch(e){loadedKey=null;showError('restoreError','That key file is not valid JSON.')}showStep('restore')});

function showError(id,msg){$(id).textContent=msg;$(id).classList.remove('hidden')}
function showWarnings(id,list){const el=$(id);if(!list||!list.length){el.classList.add('hidden');return}el.innerHTML='<strong>Check these:</strong><ul>'+list.map(w=>`<li>${esc(w)}</li>`).join('')+'</ul>';el.classList.remove('hidden')}
async function post(url,form){const res=await fetch(url,{method:'POST',body:form,cache:'no-store'});const body=await res.json().catch(()=>({}));if(!res.ok)throw new Error(body.detail||`Request failed (${res.status})`);return body}
function download(name,blob){const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},500)}
function baseName(){return sourceName.replace(/\.[^.]+$/,'')||'document'}
async function downloadDocx(text,name){const form=new FormData();form.append('text',text);form.append('filename',name);const res=await fetch('/api/deidentify/docx',{method:'POST',body:form,cache:'no-store'});if(!res.ok){alert('Could not build the .docx file.');return}download(name,await res.blob())}
function copy(text,button){navigator.clipboard.writeText(text).then(()=>{const t=button.textContent;button.textContent='Copied';setTimeout(()=>button.textContent=t,1200)})}

$('runDeid').onclick=async()=>{
  const file=$('deidFile').files[0],text=$('deidText').value;
  $('deidError').classList.add('hidden');
  if(!file&&!text.trim()){showError('deidError','Choose a file or paste some text first.');return}
  const form=new FormData();if(file)form.append('file',file);else form.append('text',text);
  form.append('names',$('names').value);form.append('details',$('details').value);
  form.append('never_hide',$('neverHide').value);form.append('auto_names',$('autoNames').checked?'true':'false');
  form.append('categories',[...document.querySelectorAll('#categoryChecks input:checked')].map(i=>i.value).join(',')||'NONE');
  $('runDeid').disabled=true;$('deidStatus').textContent=$('autoNames').checked?'Working… the first run can take a few seconds while the name model loads.':'Working…';$('rerunNote').classList.add('hidden');
  try{deidResult=await post('/api/deidentify',form);sessionKey=deidResult.key;sourceName=file?file.name:'pasted-text';renderDeid()}
  catch(e){showError('deidError',e.message)}
  finally{$('runDeid').disabled=false;$('deidStatus').textContent=''}};

function renderDeid(){const r=deidResult;
  $('deidChips').innerHTML=`<span class="chip"><strong>${r.replacements}</strong>replacements</span>`+r.summary.map(s=>`<span class="chip"><strong>${s.count}</strong>${esc(s.label)}</span>`).join('');
  showWarnings('deidWarn',r.warnings);
  renderNames(r);
  $('deidPreview').innerHTML=esc(r.text).replace(/\[[A-Z][A-Z_]*_\d+(?:_[A-Z0-9]+)*\]/g,m=>`<mark>${m}</mark>`);
  const entries=Object.entries(r.key.entries);$('keyCount').textContent=entries.length;
  $('keyTable').innerHTML=entries.map(([k,v])=>`<tr><td>[${esc(k)}]</td><td>${esc(v)}</td></tr>`).join('');
  $('deidResult').classList.remove('hidden');$('deidResult').scrollIntoView({behavior:'smooth'})}
function addLine(id,value){const box=$(id);const lines=box.value.split('\n').map(l=>l.trim()).filter(Boolean);if(!lines.some(l=>l.toLowerCase()===value.toLowerCase()))lines.push(value);box.value=lines.join('\n');$('rerunNote').classList.remove('hidden')}
function renderNames(r){const found=r.detected_names||[],kept=r.kept_names||[];
  $('foundBox').classList.toggle('hidden',!found.length);$('keptBox').classList.toggle('hidden',!kept.length);
  $('foundChips').innerHTML=found.map((n,i)=>`<span class="chip" data-i="${i}">${esc(n)}<button type="button" data-keep="${i}">Don't hide</button></span>`).join('');
  $('keptChips').innerHTML=kept.map((k,i)=>`<span class="chip" data-i="${i}">${esc(k.name)}<em>${esc(k.reason)}</em><button type="button" data-hide="${i}">Hide</button></span>`).join('');
  $('foundChips').querySelectorAll('[data-keep]').forEach(b=>b.onclick=()=>{addLine('neverHide',found[b.dataset.keep]);b.parentElement.classList.add('off');b.remove()});
  $('keptChips').querySelectorAll('[data-hide]').forEach(b=>b.onclick=()=>{addLine('names',kept[b.dataset.hide].name);b.parentElement.classList.add('off');b.remove()})}
$('rerun').onclick=()=>$('runDeid').click();
$('saveKey').onclick=()=>download(`${baseName()}.key.json`,new Blob([JSON.stringify(deidResult.key,null,2)],{type:'application/json'}));
$('copyDeid').onclick=e=>copy(deidResult.text,e.target);
$('saveDeidTxt').onclick=()=>download(`${baseName()}.deidentified.txt`,new Blob([deidResult.text],{type:'text/plain'}));
$('saveDeidDocx').onclick=()=>downloadDocx(deidResult.text,`${baseName()}.deidentified.docx`);

$('runRestore').onclick=async()=>{
  const file=$('restoreFile').files[0],text=$('restoreText').value,key=loadedKey||sessionKey;
  $('restoreError').classList.add('hidden');
  if(!file&&!text.trim()){showError('restoreError','Choose a file or paste the text to restore.');return}
  if(!key){showError('restoreError','Choose the key file saved in step 1.');return}
  const form=new FormData();if(file)form.append('file',file);else form.append('text',text);form.append('key',JSON.stringify(key));
  $('runRestore').disabled=true;$('restoreStatus').textContent='Working…';
  try{restoreResult=await post('/api/reidentify',form);restoreResult.name=(file?file.name:(key.source||'document')).replace(/\.[^.]+$/,'').replace(/\.deidentified$/,'');renderRestore()}
  catch(e){showError('restoreError',e.message)}
  finally{$('runRestore').disabled=false;$('restoreStatus').textContent=''}};

function renderRestore(){const r=restoreResult;
  $('restoreChips').innerHTML=`<span class="chip"><strong>${r.restored}</strong>details put back</span>`+(r.unused_placeholders.length?`<span class="chip"><strong>${r.unused_placeholders.length}</strong>key entries not used</span>`:'');
  showWarnings('restoreWarn',r.warnings);
  $('restorePreview').textContent=r.text;
  $('restoreResult').classList.remove('hidden');$('restoreResult').scrollIntoView({behavior:'smooth'})}
$('copyRestore').onclick=e=>copy(restoreResult.text,e.target);
$('saveRestoreTxt').onclick=()=>download(`${restoreResult.name}.restored.txt`,new Blob([restoreResult.text],{type:'text/plain'}));
$('saveRestoreDocx').onclick=()=>downloadDocx(restoreResult.text,`${restoreResult.name}.restored.docx`);
</script>
</body></html>'''
