def citation_pass_page_html() -> str:
	return r"""<!doctype html>
<html lang=\"en\">
<head>
	<meta charset=\"utf-8\">
	<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
	<title>Citation Pass | AI CaseLibrary</title>
	<style>
		:root{
			--bg:#eef2f6;
			--panel:#ffffff;
			--panel-2:#f8fafc;
			--text:#16202a;
			--muted:#5f6b78;
			--line:#d7dfe8;
			--accent:#2457d6;
			--accent-2:#6a7dff;
			--accent-soft:#e8efff;
			--gold:#f5b942;
			--shadow:0 18px 50px rgba(22,32,42,.08);
		}
		*{box-sizing:border-box}
		body{margin:0;color:var(--text);background:
			radial-gradient(circle at top left, rgba(36,87,214,.12), transparent 34%),
			radial-gradient(circle at top right, rgba(106,125,255,.10), transparent 26%),
			linear-gradient(180deg,#f4f7fb 0%, #eef2f6 34%, #edf1f6 100%);
			font-family:"Trebuchet MS","Segoe UI",sans-serif}
		.shell{display:grid;grid-template-rows:auto 1fr;min-height:100vh}
		.hero{position:relative;overflow:hidden;padding:22px 28px 18px;border-bottom:1px solid rgba(215,223,232,.85);background:rgba(255,255,255,.76);backdrop-filter:blur(12px)}
		.hero::after{content:"";position:absolute;inset:auto -40px -90px auto;width:240px;height:240px;border-radius:50%;background:radial-gradient(circle, rgba(36,87,214,.14), transparent 70%);pointer-events:none}
		.hero-top{display:flex;justify-content:space-between;align-items:flex-start;gap:20px;flex-wrap:wrap}
		.kicker{text-transform:uppercase;letter-spacing:.14em;font-size:11px;font-weight:700;color:var(--accent);margin:0 0 8px}
		h1{margin:0;font-size:30px;line-height:1.05;font-family:Georgia,serif;letter-spacing:-.02em}
		.hero-copy{max-width:760px;margin-top:10px;color:var(--muted);font-size:13px;line-height:1.5}
		.hero-stats{display:flex;gap:10px;flex-wrap:wrap;justify-content:flex-end}
		.stat{min-width:140px;padding:12px 14px;border:1px solid var(--line);border-radius:14px;background:rgba(255,255,255,.8);box-shadow:var(--shadow)}
		.stat strong{display:block;font-size:20px;line-height:1;color:var(--text)}
		.stat span{display:block;margin-top:4px;font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}
		.main-grid{display:grid;grid-template-columns:340px 1fr;min-height:0;gap:16px;padding:16px 16px 18px}
		.sidebar,.content{min-height:0}
		.sidebar{display:flex;flex-direction:column;overflow:hidden;border:1px solid var(--line);border-radius:20px;background:rgba(255,255,255,.75);box-shadow:var(--shadow)}
		.sidebar-head{padding:14px 14px 12px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,250,252,.92))}
		.sidebar-head strong{display:block;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
		.sidebar-head .sub{margin-top:6px;font-size:12px;color:var(--muted);line-height:1.45}
		#cases{overflow:auto;min-height:0}
		button.case{display:block;width:100%;text-align:left;padding:13px 14px;border:0;border-bottom:1px solid rgba(215,223,232,.75);background:transparent;cursor:pointer;transition:background .15s ease,transform .15s ease}
		button.case:hover{background:#f4f8ff;transform:translateX(2px)}
		button.case.active{background:linear-gradient(90deg,rgba(36,87,214,.10),rgba(106,125,255,.04));box-shadow:inset 3px 0 0 var(--accent)}
		button.case strong{display:block;font-size:13px;line-height:1.35}
		button.case small{display:block;color:var(--muted);font-size:11px;margin-top:4px;line-height:1.35}
		.content{display:grid;grid-template-rows:auto auto auto 1fr;gap:16px;min-height:0}
		.card{background:rgba(255,255,255,.88);border:1px solid var(--line);border-radius:20px;padding:16px 18px;box-shadow:var(--shadow)}
		.card-head{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap}
		.case-title{font-family:Georgia,serif;font-size:21px;line-height:1.15;margin:0 0 8px}
		.case-meta{font-size:12px;color:var(--muted);line-height:1.5}
		.badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
		.badge{display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border-radius:999px;border:1px solid var(--line);background:var(--panel-2);font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}
		.badge strong{color:var(--text);font-size:12px;letter-spacing:0;text-transform:none}
		.detail-panel{background:rgba(255,255,255,.88);border:1px solid var(--line);border-left:4px solid var(--accent);padding:15px 18px;box-shadow:var(--shadow)}
		.detail-title{display:flex;align-items:baseline;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:12px}
		.detail-title h2{margin:0;font:700 17px/1.25 Georgia,serif}
		.detail-title span{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.08em}
		.detail-grid{display:grid;grid-template-columns:repeat(6,minmax(100px,1fr));gap:1px;background:var(--line);border:1px solid var(--line)}
		.detail-field{min-width:0;padding:9px 10px;background:#fff}
		.detail-field small{display:block;margin-bottom:4px;color:var(--muted);font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.08em}
		.detail-field strong{display:block;overflow-wrap:anywhere;font-size:12px;line-height:1.35}
		.detail-section{margin-top:12px}
		.detail-section h3{margin:0 0 6px;color:var(--muted);font-size:10px;text-transform:uppercase;letter-spacing:.08em}
		.detail-text{margin:0;padding:10px 12px;overflow:auto;white-space:pre-wrap;border:1px solid var(--line);background:#f8fafc;font:12px/1.55 "Cascadia Mono",Consolas,monospace}
		.chunk-detail{margin-top:6px;border:1px solid var(--line);background:#fff}
		.chunk-detail summary{padding:9px 11px;cursor:pointer;font-size:11px;font-weight:700}
		.chunk-detail .detail-text{border-width:1px 0 0}
		.record-row{padding:9px 11px;border:1px solid var(--line);background:#fff;font-size:12px;line-height:1.5}
		.record-row+.record-row{border-top:0}
		.record-row a{color:var(--accent);font-weight:700}
		.citation-panel{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(320px,.95fr);gap:16px;min-height:0}
		.text-card,.table-card{min-height:0;background:rgba(255,255,255,.88);border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow)}
		.text-card{display:flex;flex-direction:column;overflow:hidden}
		.table-card{display:flex;flex-direction:column;overflow:hidden}
		.panel-head{padding:14px 16px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,250,252,.92))}
		.panel-head strong{display:block;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
		.panel-head .sub{margin-top:6px;font-size:12px;color:var(--muted);line-height:1.45}
		.case-text{flex:1;min-height:0;white-space:pre-wrap;background:linear-gradient(180deg,#fff,#fcfdff);padding:18px 18px 20px;overflow:auto;font-family:"Cascadia Mono","SFMono-Regular",Consolas,monospace;font-size:12px;line-height:1.62}
		table{width:100%;border-collapse:collapse;background:transparent}
		thead th{position:sticky;top:0;background:#f7f9fc;z-index:1}
		th,td{padding:10px 11px;border-bottom:1px solid #e7edf4;vertical-align:top;text-align:left;font-size:12px}
		th{font-weight:700;color:#334155;text-transform:uppercase;letter-spacing:.05em;font-size:10px}
		tr.clickable{cursor:pointer}
		tr.clickable:hover{background:#f4f8ff}
		tr.active-row{background:rgba(36,87,214,.08)}
		.empty{padding:18px;color:var(--muted)}
		.list-wrap{overflow:auto;min-height:0}
		.mark-help{font-size:12px;color:var(--muted);margin:0}
		.mark-help strong{color:var(--text)}
		mark.cite-case{background:rgba(245,185,66,.32);box-shadow:inset 0 -2px rgba(245,185,66,.9);padding:0 1px;border-radius:2px}
		mark.cite-law{background:rgba(45,166,108,.22);box-shadow:inset 0 -2px rgba(35,139,89,.9);padding:0 1px;border-radius:2px}
		mark.cite-metadata{background:rgba(64,120,220,.20);box-shadow:inset 0 -2px rgba(53,109,204,.92);padding:0 1px;border-radius:2px}
		mark[data-row-key]{cursor:pointer}
		mark[data-row-key]:hover{outline:2px solid rgba(36,87,214,.55)}
		mark.active-hit{outline:2px solid var(--accent);background:rgba(36,87,214,.18)!important}
		@media (max-width: 1100px){
			.main-grid{grid-template-columns:1fr}
			.citation-panel{grid-template-columns:1fr}
			.detail-grid{grid-template-columns:repeat(3,minmax(100px,1fr))}
			.sidebar{max-height:360px}
		}
		@media (max-width: 760px){
			.hero{padding:18px 14px}
			h1{font-size:24px}
			.main-grid{padding:12px}
			.card,.sidebar,.text-card,.table-card{border-radius:16px}
			.detail-grid{grid-template-columns:repeat(2,minmax(100px,1fr))}
		}
	</style>
</head>
<body>
	<div class=\"shell\">
		<div class=\"hero\">
			<div class=\"hero-top\">
				<div>
					<p class=\"kicker\">AI CaseLibrary</p>
					<h1>Citation Pass</h1>
					<div class=\"hero-copy\">Layered extraction review. Case citations are orange, statutes and legal instruments are green, and extracted metadata is blue. Each layer keeps its own extraction process and exact offsets.</div>
				</div>
				<div class=\"hero-stats\">
					<div class=\"stat\"><strong id=\"liveCount\">0</strong><span>Live citations</span></div>
					<div class=\"stat\"><strong id=\"lawCount\">0</strong><span>Statutes / laws</span></div>
					<div class=\"stat\"><strong id=\"metadataCount\">0</strong><span>Metadata fields</span></div>
					<div class=\"stat\"><strong id=\"selectedCount\">0</strong><span>Selected row</span></div>
					<div class=\"stat\"><strong id=\"caseCount\">0</strong><span>Cases in list</span></div>
				</div>
			</div>
		</div>
		<div class=\"main-grid\">
			<aside class=\"sidebar\">
				<div class=\"sidebar-head\">
					<strong>Review Cohort</strong>
					<div class=\"sub\">Choose a case to inspect the extraction output. The list stays focused on the current proof-of-concept set.</div>
				</div>
				<div id=\"cases\" class=\"list-wrap\"><div class=\"empty\">Loading cases...</div></div>
			</aside>
			<section class=\"content\">
				<div id=\"caseCard\" class=\"card\">Select a case.</div>
				<section id=\"detailPanel\" class=\"detail-panel\"><div class=\"empty\">Select a reference to inspect its exact text, document position, chunks, and stored records.</div></section>
				<div class=\"citation-panel\">
					<div class=\"text-card\">
						<div class=\"panel-head\">
							<strong>Highlighted Text</strong>
							<div class=\"sub\">Case citations are orange. Statutes and legal instruments are green. Metadata is blue.</div>
						</div>
						<div id=\"annotatedText\" class=\"case-text\">No case loaded.</div>
					</div>
					<div class=\"table-card\">
						<div class=\"panel-head\">
							<strong>Extracted References</strong>
							<div class=\"sub\" id=\"tableSummary\">Waiting for a case selection.</div>
						</div>
						<div id=\"citationTables\" class=\"list-wrap empty\">No citation pass loaded yet.</div>
					</div>
				</div>
			</section>
		</div>
	</div>
	<script>
		const state={selected:null,payload:null,activeRowKey:null,detail:null};
		const esc=v=>String(v??'').replace(/[&<>\'\"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','\"':'&quot;'}[c]));
		async function json(url){const r=await fetch(url);if(!r.ok){throw new Error('Request failed: '+r.status)}return r.json();}
		const shown=v=>v===null||v===undefined||v===''?'Not stored':String(v);
		function renderCaseList(rows){document.getElementById('caseCount').textContent=String(rows.length);const box=document.getElementById('cases');box.innerHTML=rows.map(row=>`<button class=\"case ${state.selected===row.case_id?'active':''}\" data-id=\"${row.case_id}\"><strong>${esc(row.title)}</strong><small>${esc(row.citation||'No citation')} · ${esc(row.court)} · ${esc(row.date)}</small></button>`).join('')||'<div class="empty">No cases in review list.</div>';box.querySelectorAll('button.case').forEach(b=>b.onclick=()=>openCase(Number(b.dataset.id)));}
		function rowsForView(payload){const cases=(payload.live_extracted||[]).map((row,index)=>({...row,__rowKey:`case:${index}`,__layer:'case'}));const laws=(payload.live_statutes||[]).map((row,index)=>({...row,__rowKey:`law:${index}`,__layer:'law'}));const metadata=(payload.live_metadata||[]).map((row,index)=>({...row,citation_text:row.text,normalized_citation:`${row.field}: ${row.value}`,__rowKey:`metadata:${index}`,__layer:'metadata'}));return [...cases,...laws,...metadata];}
		function findRanges(text,rows){const candidates=[];const codePointToCodeUnit=[0];let codeUnits=0;for(const char of text){codeUnits+=char.length;codePointToCodeUnit.push(codeUnits);}for(const row of rows){const codePointStart=Number(row.offset_start),codePointEnd=Number(row.offset_end);if(!Number.isInteger(codePointStart)||!Number.isInteger(codePointEnd)||codePointStart<0||codePointEnd<=codePointStart||codePointEnd>=codePointToCodeUnit.length)continue;const start=codePointToCodeUnit[codePointStart],end=codePointToCodeUnit[codePointEnd];const citationText=String(row.citation_text||'');if(!citationText||text.slice(start,end)!==citationText)continue;candidates.push({start,end,label:String(row.normalized_citation||citationText),rowKey:String(row.__rowKey||''),layer:String(row.__layer||'case')});}const ranges=[];for(const candidate of candidates.sort((a,b)=>(a.end-a.start)-(b.end-b.start)||a.start-b.start)){if(ranges.some(range=>candidate.start<range.end&&candidate.end>range.start))continue;ranges.push(candidate);}return ranges.sort((a,b)=>a.start-b.start||b.end-a.end);}
		function paragraphBreaks(segment,allowLeadingBreak){const value=String(segment||'');return value.replace(/\[(\d+)\]/g,(m,n,idx)=>{if(idx===0&&!allowLeadingBreak)return`[${n}]`;return`\n\n[${n}]`;});}
		function highlightText(text,ranges){let out='';let cursor=0;for(const range of ranges){if(range.start<cursor||range.start>=text.length)continue;const end=Math.min(range.end,text.length);if(end<=cursor)continue;out+=esc(paragraphBreaks(text.slice(cursor,range.start),cursor>0));const active=state.activeRowKey&&range.rowKey===state.activeRowKey?' active-hit':'';const layerClass=range.layer==='law'?'cite-law':range.layer==='metadata'?'cite-metadata':'cite-case';out+=`<mark class=\"${layerClass}${active}\" data-row-key=\"${esc(range.rowKey)}\" title=\"Click for details: ${esc(range.label)}\">${esc(paragraphBreaks(text.slice(range.start,end),cursor>0||range.start>0))}</mark>`;cursor=end;}out+=esc(paragraphBreaks(text.slice(cursor),cursor>0));return out;}
		function renderHighlights(){if(!state.payload)return;const text=(state.payload.case.full_text||state.payload.case.summary||'').toString();if(!text){document.getElementById('annotatedText').textContent='No case text available.';return;}const ranges=findRanges(text,rowsForView(state.payload));document.getElementById('annotatedText').innerHTML=highlightText(text,ranges);document.querySelectorAll('mark[data-row-key]').forEach(mark=>{mark.onclick=()=>selectReference(String(mark.dataset.rowKey||''));});if(state.activeRowKey){const mark=document.querySelector('mark.active-hit');if(mark)mark.scrollIntoView({behavior:'smooth',block:'center'});}}
		function pinpointFromText(value){const text=String(value||'');const m=text.match(/\bat\s+para(?:s|graph(?:s)?)?\.?\s+\d+(?:\s*[-–]\s*\d+)?(?:\s*(?:,|;|and|or)\s*\d+(?:\s*[-–]\s*\d+)?)*\b/i);return m?m[0].replace(/\s+/g,' ').trim():'';}
		function codePointSlice(value,start,end){const chars=Array.from(String(value||''));const safeStart=Math.max(0,Math.min(start,chars.length));const safeEnd=Math.max(safeStart,Math.min(end,chars.length));return chars.slice(safeStart,safeEnd).join('');}
		function trailingPinpoint(row){if(String(row.__layer||'')!=='Case'||!state.payload)return '';const text=(state.payload.case.full_text||state.payload.case.summary||'').toString();const end=Number(row.offset_end);if(!Number.isInteger(end)||end<0)return '';const tail=codePointSlice(text,end,end+140);const m=tail.match(/^\s*[)\],;:\-]*\s*(?:\[\s*)?(?:at\s+)?para(?:s|graph(?:s)?)?\.?\s+\d+(?:\s*[-–]\s*\d+)?(?:\s*(?:,|;|and|or)\s*\d+(?:\s*[-–]\s*\d+)?)*(?:\s*\])?\b/i);return m?m[0].replace(/\s+/g,' ').trim():'';}
		function pinpointBadge(row){const layer=String(row.__layer||'');if(layer==='Metadata'){const confidence=Number(row.confidence);const confidenceText=Number.isFinite(confidence)?confidence.toFixed(2):'n/a';if(row.span_matched){return `<span class=\"badge\" style=\"background:#edf7ed;border-color:#78b27b;color:#1f5c26\" title=\"Exact text span matched (source: ${esc(String(row.source||'unknown'))}, confidence: ${esc(confidenceText)})\">Matched span</span>`;}return `<span class=\"badge\" style=\"background:#fff4e8;border-color:#d8aa78;color:#8b4e11\" title=\"Extracted metadata without exact text span (source: ${esc(String(row.source||'unknown'))}, confidence: ${esc(confidenceText)})\">Extracted only</span>`;}if(layer!=='Case')return '<span class=\"badge\" style=\"opacity:.58\">N/A</span>';const pinpoint=pinpointFromText(row.normalized_citation)||pinpointFromText(row.citation_text);if(pinpoint){return `<span class=\"badge\" style=\"background:#edf7ed;border-color:#78b27b;color:#1f5c26\" title=\"${esc(pinpoint)}\">Pinpoint</span>`;}const missed=trailingPinpoint(row);if(missed){return `<span class=\"badge\" style=\"background:#ffe8e8;border-color:#d89494;color:#7f1d1d\" title=\"Trailing pinpoint in source text not captured: ${esc(missed)}\">Missed</span>`;}return '<span class=\"badge\" style=\"background:#f7f7f7;border-color:#c9c9c9;color:#4b5563\" title=\"This citation has no para/paras marker in the source text.\">None cited</span>';}
		function renderRows(cases,laws,metadata){document.getElementById('liveCount').textContent=String(cases.length);document.getElementById('lawCount').textContent=String(laws.length);document.getElementById('metadataCount').textContent=String(metadata.length);document.getElementById('selectedCount').textContent=state.activeRowKey?'1':'0';const casePinpointCount=cases.filter(row=>pinpointFromText(row.normalized_citation)||pinpointFromText(row.citation_text)).length;const metadataSpanCount=metadata.filter(row=>Boolean(row.span_matched)).length;document.getElementById('tableSummary').textContent=`${cases.length} case citation${cases.length===1?'':'s'} · ${laws.length} statute/law reference${laws.length===1?'':'s'} · ${metadata.length} metadata field${metadata.length===1?'':'s'} · ${casePinpointCount}/${cases.length} case cites with pinpoint · ${metadataSpanCount}/${metadata.length} metadata spans matched.`;const rows=[...cases.map((row,index)=>({...row,__rowKey:`case:${index}`,__layer:'Case'})),...laws.map((row,index)=>({...row,__rowKey:`law:${index}`,__layer:'Law'})),...metadata.map((row,index)=>({...row,kind:row.field,citation_text:row.text,normalized_citation:row.value,__rowKey:`metadata:${index}`,__layer:'Metadata'}))];if(!rows.length)return '<div class=\"empty\">No references extracted.</div>';return `<table><thead><tr><th>#</th><th>Layer</th><th>Kind</th><th>Reference text</th><th>Status</th><th>Normalized</th><th>Where</th><th>Context</th></tr></thead><tbody>${rows.map((r,i)=>`<tr class=\"clickable ${state.activeRowKey===r.__rowKey?'active-row':''}\" data-row-key=\"${r.__rowKey}\"><td>${i+1}</td><td>${esc(r.__layer)}</td><td>${esc(r.kind||'')}</td><td>${esc(r.citation_text||'')}</td><td>${pinpointBadge(r)}</td><td>${esc(r.normalized_citation||'')}</td><td>${esc(`${r.offset_start??''}-${r.offset_end??''}`)}</td><td>${esc(r.context||'')}</td></tr>`).join('')}</tbody></table>`;}
		function detailField(label,value){return `<div class=\"detail-field\"><small>${esc(label)}</small><strong>${esc(shown(value))}</strong></div>`;}
		function renderDetail(detail){const panel=document.getElementById('detailPanel');if(!detail){panel.innerHTML='<div class=\"empty\">Select a reference to inspect its exact text, document position, chunks, and stored records.</div>';return;}const location=detail.location||{},passage=detail.passage||{},metadata=detail.metadata||null;const chunks=(detail.chunks||[]).map(chunk=>`<details class=\"chunk-detail\"><summary>${esc(chunk.chunk_set)} #${esc(chunk.chunk_index)} · ${esc(shown(chunk.chunk_label))} · chunk id ${esc(chunk.chunk_id)}</summary><div class=\"detail-grid\">${detailField('Paragraph range',chunk.paragraph_start===null?'Not stored':chunk.paragraph_start===chunk.paragraph_end?chunk.paragraph_start:`${chunk.paragraph_start}-${chunk.paragraph_end}`)}${detailField('Chunk offsets',`${chunk.offset_start}-${chunk.offset_end}`)}${detailField('Document offsets',`${chunk.document_start}-${chunk.document_end}`)}${detailField('Text length',chunk.text_length)}${detailField('Token estimate',chunk.token_estimate)}${detailField('Exact chunk match',chunk.citation_text)}</div><pre class=\"detail-text\">${esc(chunk.text)}</pre></details>`).join('')||'<div class=\"record-row\">No stored chunk contains this exact document span.</div>';const records=(detail.stored_records||[]).map(record=>{const target=record.target;const targetHtml=record.target===undefined?'':target?` · resolved to <a href=\"/data-explorer?case_id=${encodeURIComponent(target.case_id)}\">${esc(target.title||target.citation||`Case ${target.case_id}`)}</a> (${esc(shown(target.citation))})`:' · no resolved target';return `<div class=\"record-row\"><strong>Record ${esc(record.record_id)}</strong> · ${esc(shown(record.citation_kind))} · chunk ${esc(shown(record.chunk_id))} · offsets ${esc(shown(record.offset_start))}-${esc(shown(record.offset_end))}${record.provenance!==undefined?` · provenance ${esc(shown(record.provenance))}`:''}${record.unresolved!==undefined?` · ${record.unresolved?'unresolved':'resolved flag clear'}`:''}${targetHtml}</div>`;}).join('')||'<div class=\"record-row\">No matching stored record for this extracted occurrence.</div>';panel.innerHTML=`<div class=\"detail-title\"><h2>${esc(detail.citation_text)}</h2><span>${esc(detail.layer)} · ${esc(detail.kind)}</span></div><div class=\"detail-grid\">${detailField('Normalized value',detail.normalized_value)}${detailField('Document offsets',`${detail.offset_start}-${detail.offset_end}`)}${detailField('Span length',detail.span_length)}${detailField('Line / column',`${location.line_number} / ${location.column_number}`)}${detailField('Paragraph',location.paragraph_number)}${detailField('Document position',`${location.position_percent}%`)}${metadata?detailField('Confidence',metadata.confidence)+detailField('Source',metadata.source):''}</div><div class=\"detail-section\"><h3>Line-aligned passage · offsets ${esc(passage.offset_start)}-${esc(passage.offset_end)}</h3><pre class=\"detail-text\">${esc(passage.text)}</pre></div><div class=\"detail-section\"><h3>Containing chunks (${detail.chunks.length})</h3>${chunks}</div><div class=\"detail-section\"><h3>Stored records (${detail.stored_records.length})</h3>${records}</div>`;}
		async function loadDetail(rowKey){const selectedRow=rowsForView(state.payload).find(row=>row.__rowKey===rowKey);if(!selectedRow)return;const start=Number(selectedRow.offset_start),end=Number(selectedRow.offset_end);if(!Number.isInteger(start)||!Number.isInteger(end)||end<=start){document.getElementById('detailPanel').innerHTML='<div class=\"empty\">No exact source span is available for this extracted metadata field.</div>';return;}document.getElementById('detailPanel').innerHTML='<div class=\"empty\">Loading citation details...</div>';const query=new URLSearchParams({layer:selectedRow.__layer,offset_start:String(start),offset_end:String(end)});try{const detail=await json(`/cases/${state.selected}/citation-pass/detail?${query}`);if(state.activeRowKey!==rowKey)return;state.detail=detail;renderDetail(detail);}catch(error){if(state.activeRowKey===rowKey)document.getElementById('detailPanel').innerHTML=`<div class=\"empty\">${esc(error.message)}</div>`;}}
		function selectReference(rowKey){if(!rowKey)return;state.activeRowKey=rowKey;state.detail=null;renderPayload(state.payload);loadDetail(rowKey);}
		function bindRowClicks(){document.querySelectorAll('tr[data-row-key]').forEach(row=>{row.onclick=()=>selectReference(String(row.getAttribute('data-row-key')||''));});}
		function metadataFieldValue(rows,name){const target=String(name||'').toLowerCase();const row=(rows||[]).find(r=>String(r.field||'').toLowerCase()===target);return row?String(row.value||'').trim():'';}
		function aljrSummaryText(metadataRows){const role=metadataFieldValue(metadataRows,'government role').toLowerCase();const outcomeRaw=metadataFieldValue(metadataRows,'decision outcome').toLowerCase();const filedBy=role==='applicant'?'Minister':role==='respondent'?'Individual':'Unknown';let result='Unknown';if(outcomeRaw==='dismissed'){result='Dismissed';}else if(outcomeRaw==='allowed'||outcomeRaw==='granted'){result='Granted';}return `ALJR Filed by ${filedBy}, result: ${result}`;}
		function renderPayload(payload){state.payload=payload;const c=payload.case;const s=payload.summary||{};const cases=(payload.live_extracted||[]).map(row=>({...row,context:row.context||''}));const laws=(payload.live_statutes||[]).map(row=>({...row,context:row.context||''}));const metadata=(payload.live_metadata||[]).map(row=>({...row,context:row.context||''}));const aljrSummary=aljrSummaryText(metadata);document.getElementById('caseCard').innerHTML=`<div class=\"card-head\"><div><h2 class=\"case-title\">${esc(c.title)}</h2><div class=\"case-meta\">${esc(c.citation||'No citation')} · ${esc(c.court)} · ${esc(c.date)} · id ${c.id}</div><div class=\"case-meta\" style=\"margin-top:6px\"><strong>${esc(aljrSummary)}</strong></div></div><div class=\"badges\"><span class=\"badge\"><strong>${s.live_total||0}</strong> case citations</span><span class=\"badge\"><strong>${s.statute_total||0}</strong> statutes/laws</span><span class=\"badge\"><strong>${s.metadata_total||0}</strong> metadata fields</span><span class=\"badge\"><strong>${c.full_text?'Yes':'No'}</strong> full text</span></div></div><div class=\"badges\" style=\"margin-top:14px\"><span class=\"badge\">Orange: cases</span><span class=\"badge\">Green: statutes/laws</span><span class=\"badge\">Blue: metadata</span></div>`;document.getElementById('citationTables').innerHTML=renderRows(cases,laws,metadata);bindRowClicks();renderHighlights();}
		async function openCase(caseId){state.selected=caseId;state.activeRowKey=null;state.detail=null;renderDetail(null);const payload=await json(`/cases/${caseId}/citation-pass`);renderPayload(payload);const list=await json('/citation-map/cases/review/fc-priority?limit=300');renderCaseList(list);}
		async function load(){const list=await json('/citation-map/cases/review/fc-priority?limit=300');renderCaseList(list);if(list.length){await openCase(list[0].case_id);}}
		load().catch(e=>{document.getElementById('cases').innerHTML=`<div class=\"empty\">${esc(e.message)}</div>`;});
	</script>
</body>
</html>"""


