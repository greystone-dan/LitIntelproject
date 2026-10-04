from .accessibility import accessible_page


@accessible_page
def statute_viewer_page_html() -> str:
	return """<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Statute Library | AI CaseLibrary</title>
	<style>
		:root{--ink:#14212b;--muted:#63707a;--paper:#f6f4ee;--panel:#fffdfa;--line:#d9d5ca;--accent:#285d75;}
		*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,"Times New Roman",serif}.shell{max-width:1280px;margin:auto;padding:32px 24px 56px}.masthead{display:flex;justify-content:space-between;gap:24px;align-items:end;border-bottom:3px solid var(--ink);padding-bottom:20px}.eyebrow{font:700 12px/1.2 Arial,sans-serif;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent)}h1{font-size:34px;font-weight:normal;margin:7px 0 0;letter-spacing:0}.subhead{max-width:620px;margin:0;color:var(--muted);font-size:16px;line-height:1.45}.search-controls{display:flex;gap:12px;margin:24px 0;flex-wrap:wrap}.search-controls select,.search-controls input{padding:10px 12px;border:1px solid var(--line);border-radius:4px;font:14px Georgia,serif;background:var(--panel)}.search-controls button{padding:10px 20px;background:var(--accent);color:white;border:none;border-radius:4px;cursor:pointer;font:700 12px Arial,sans-serif;text-transform:uppercase;letter-spacing:.7px}.search-controls button:hover{background:#1e4a5f}.statute-list{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:20px;margin:24px 0}.statute-card{background:var(--panel);border:1px solid var(--line);padding:16px;border-radius:4px;cursor:pointer;transition:all .2s ease}.statute-card:hover{border-color:var(--accent);box-shadow:0 2px 8px rgba(40,93,117,.1)}.statute-card-code{font:700 12px Arial,sans-serif;letter-spacing:.7px;text-transform:uppercase;color:var(--accent);margin-bottom:6px}.statute-card-title{font-size:16px;font-weight:normal;margin:0 0 8px;line-height:1.35}.statute-card-type{font:12px Arial,sans-serif;color:var(--muted);margin:8px 0 0}.statute-view{margin:24px 0}.statute-header{background:var(--panel);border:1px solid var(--line);padding:20px;border-radius:4px;margin-bottom:16px}.statute-version-info{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;font-size:14px;margin:12px 0 0}.statute-version-info div{display:flex;gap:8px}.statute-version-info strong{font-weight:700;color:var(--ink);min-width:120px}section{margin:24px 0}.section-header{display:flex;gap:12px;align-items:baseline;margin:16px 0 8px;padding-bottom:8px;border-bottom:1px solid var(--line)}.section-number{font:700 14px Arial,sans-serif;color:var(--accent);min-width:60px}.section-heading{font-size:15px;font-weight:600}.section-text{background:var(--panel);padding:16px;border-left:3px solid var(--accent);margin:0 0 8px;line-height:1.6;font-size:14px;white-space:pre-wrap;word-wrap:break-word}.empty{padding:30px;text-align:center;color:var(--muted)}.loading{padding:30px;text-align:center;color:var(--muted)}@media(max-width:680px){.shell{padding:22px 14px}.masthead{display:block}.subhead{margin-top:15px}.search-controls{flex-direction:column}.search-controls select,.search-controls input,.search-controls button{width:100%}.statute-list{grid-template-columns:1fr}h1{font-size:29px}}
	</style>
</head>
<body>
	<main class="shell">
		<header class="masthead"><div><div class="eyebrow">Legislation Library</div><h1>Federal Statutes</h1></div><p class="subhead">Browse Canadian federal laws with point-in-time versions matched to decision dates. Find the text of statutes that were in force when cases were decided.</p></header>

		<div id="statute-browser">
			<div class="search-controls">
				<label class="a11y-visually-hidden" for="statute-select">Statute</label>
				<select id="statute-select">
					<option value="">Select a statute...</option>
					<option value="IRPA">Immigration and Refugee Protection Act (IRPA)</option>
					<option value="IRPR">Immigration and Refugee Protection Regulations (IRPR)</option>
					<option value="CA">Citizenship Act</option>
					<option value="CustA">Customs Act</option>
					<option value="FCA">Federal Courts Act</option>
					<option value="FCR">Federal Courts Rules</option>
					<option value="Charter">Canadian Charter of Rights and Freedoms</option>
				</select>
				<label class="a11y-visually-hidden" for="decision-date">Decision date (optional)</label>
				<input type="date" id="decision-date" placeholder="Decision date (optional)">
				<button onclick="loadStatute()">Load Statute</button>
			</div>

			<div id="statute-content">
				<div class="empty">Select a statute to view its text and sections.</div>
			</div>
		</div>

		<p class="note" style="color:var(--muted);font-size:13px;margin-top:32px;">Statute data is sourced from the Government of Canada's Justice Laws XML service (justice.gc.ca) under the Open Government License. Sections and subsections are indexed and searchable.</p>
	</main>

	<script>
		const escape=value=>String(value??'').replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));

		async function loadStatute(){
			const statuteCode=document.getElementById('statute-select').value;
			const decisionDate=document.getElementById('decision-date').value;

			if(!statuteCode){
				document.getElementById('statute-content').innerHTML='<div class="empty">Please select a statute.</div>';
				return;
			}

			const contentDiv=document.getElementById('statute-content');
			contentDiv.innerHTML='<div class="loading">Loading statute...</div>';

			try{
				// Fetch statute information and current version
				const response=await fetch(`/api/statutes/${statuteCode}${decisionDate?`?as_of=${decisionDate}`:''}`);
				if(!response.ok){
					if(response.status===404){
						contentDiv.innerHTML='<div class="empty">Statute not yet loaded in database. This feature will be available after Phase 1 deployment.</div>';
					}else{
						throw new Error(`Request failed (${response.status})`);
					}
					return;
				}

				const statute=await response.json();
				let html=`<div class="statute-header">
					<h2 style="margin:0 0 12px;">${escape(statute.title)}</h2>
					<div style="font:12px Arial,sans-serif;color:var(--muted);margin-bottom:8px;">${escape(statute.short_title)} | ${escape(statute.statute_type)} | ${escape(statute.jurisdiction)}</div>
					<div class="statute-version-info">
						<div><strong>Version:</strong><span>${escape(statute.current_version)}</span></div>
						<div><strong>In force:</strong><span>${escape(statute.in_force_date)}</span></div>
						<div><strong>License:</strong><span>${escape(statute.license)}</span></div>
					</div>
				</div>`;

				// Fetch sections for this statute version
				if(statute.version_id){
					const sectionsResponse=await fetch(`/api/statutes/${statuteCode}/versions/${statute.version_id}/sections`);
					if(sectionsResponse.ok){
						const sections=await sectionsResponse.json();
						if(sections && sections.length > 0){
							html+='<section><h3>Sections</h3>';
							sections.slice(0, 100).forEach(sec=>{
								html+=`<div class="section-header">
									<span class="section-number">${escape(sec.section_number)}${sec.subsection?'('+escape(sec.subsection)+')':''}</span>
									<span class="section-heading">${escape(sec.heading||'')}</span>
								</div>
								<div class="section-text">${escape(sec.text||'')}</div>`;
							});
							if(sections.length > 100){
								html+=`<p style="color:var(--muted);font-size:13px;">Showing first 100 of ${sections.length} sections.</p>`;
							}
							html+='</section>';
						}
					}
				}

				contentDiv.innerHTML=html;
			}catch(error){
				contentDiv.innerHTML=`<div class="empty">${escape(error.message)}</div>`;
			}
		}

		// Load default statute on page load
		document.getElementById('statute-select').addEventListener('change', loadStatute);
		document.getElementById('decision-date').addEventListener('change', loadStatute);
	</script>
</body>
</html>"""
