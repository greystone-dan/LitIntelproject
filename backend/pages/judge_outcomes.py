def judge_outcomes_page_html() -> str:
	return """<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Judge Outcomes | AI CaseLibrary</title>
	<style>
		:root{--ink:#14212b;--muted:#63707a;--paper:#f6f4ee;--panel:#fffdfa;--line:#d9d5ca;--gov:#285d75;--ind:#b65a34;--unknown:#b8b3a8;}
		*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,"Times New Roman",serif}.shell{max-width:1280px;margin:auto;padding:32px 24px 56px}.masthead{display:flex;justify-content:space-between;gap:24px;align-items:end;border-bottom:3px solid var(--ink);padding-bottom:20px}.eyebrow{font:700 12px/1.2 Arial,sans-serif;letter-spacing:1.4px;text-transform:uppercase;color:var(--gov)}h1{font-size:34px;font-weight:normal;margin:7px 0 0;letter-spacing:0}.subhead{max-width:620px;margin:0;color:var(--muted);font-size:16px;line-height:1.45}.summary{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-bottom:1px solid var(--line);margin:25px 0 18px}.metric{padding:13px 16px 14px 0}.metric+.metric{border-left:1px solid var(--line);padding-left:16px}.metric small{display:block;font:700 11px Arial,sans-serif;letter-spacing:1px;text-transform:uppercase;color:var(--muted)}.metric strong{font-size:27px;font-weight:normal}.legend{display:flex;gap:16px;align-items:center;font:12px Arial,sans-serif;color:var(--muted);margin:12px 0}.key{display:inline-flex;align-items:center;gap:6px}.dot{width:10px;height:10px;display:inline-block}.table-wrap{overflow:auto;background:var(--panel);border:1px solid var(--line)}table{border-collapse:collapse;width:100%;min-width:820px}th{text-align:left;padding:12px 10px;font:700 11px Arial,sans-serif;letter-spacing:.7px;text-transform:uppercase;color:var(--muted);border-bottom:2px solid var(--ink);white-space:nowrap}td{padding:13px 10px;border-bottom:1px solid var(--line);font-size:15px;vertical-align:middle}.rank{font:700 13px Arial,sans-serif;color:var(--muted)}.judge{min-width:250px}.count{font-variant-numeric:tabular-nums;text-align:right}.bar{height:13px;display:flex;min-width:180px;background:#eeeae1}.gov{background:var(--gov)}.individual{background:var(--ind)}.unknown{background:var(--unknown)}.rate{font:700 13px Arial,sans-serif}.note{color:var(--muted);font-size:13px;line-height:1.45;margin:16px 0 0}.empty{padding:30px;color:var(--muted)}@media(max-width:680px){.shell{padding:22px 14px}.masthead{display:block}.subhead{margin-top:15px}.summary{grid-template-columns:1fr}.metric+.metric{border-left:0;border-top:1px solid var(--line);padding-left:0}h1{font-size:29px}}
	</style>
</head>
<body>
	<main class="shell">
		<header class="masthead"><div><div class="eyebrow">Decision Analytics</div><h1>How Top Judges Rule</h1></div><p class="subhead">The 50 judges with the most decisions, showing outcomes where the government and individual sides can be determined from the decision record.</p></header>
		<section class="summary" id="summary"><div class="metric"><small>Loading</small><strong>...</strong></div></section>
		<div class="legend"><span class="key"><i class="dot" style="background:var(--gov)"></i>Government wins</span><span class="key"><i class="dot" style="background:var(--ind)"></i>Individual wins</span><span class="key"><i class="dot" style="background:var(--unknown)"></i>Unclassified</span></div>
		<div class="table-wrap"><table><thead><tr><th>#</th><th>Judge</th><th>Decisions</th><th>Outcome split</th><th>Government wins</th><th>Individual wins</th><th>Unclassified</th><th>Gov. win rate</th></tr></thead><tbody id="rows"><tr><td colspan="8" class="empty">Loading analytics...</td></tr></tbody></table></div>
		<p class="note">Win rate uses only classified decisions. Unclassified decisions are included in the decision total but excluded from the rate.</p>
	</main>
	<script>
		const number=value=>new Intl.NumberFormat().format(Number(value||0));
		const escape=value=>String(value??'').replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
		function metric(label,value){return `<div class="metric"><small>${escape(label)}</small><strong>${escape(value)}</strong></div>`;}
		function row(item,index){const classified=item.government_wins+item.individual_wins;const govWidth=classified?item.government_wins/classified*100:0;const individualWidth=classified?item.individual_wins/classified*100:0;const unknownWidth=item.decisions?item.unclassified/item.decisions*100:0;const rate=classified?`${(govWidth).toFixed(1)}%`:'--';return `<tr><td class="rank">${index+1}</td><td class="judge">${escape(item.judge)}</td><td class="count">${number(item.decisions)}</td><td><div class="bar" title="Government: ${number(item.government_wins)} | Individual: ${number(item.individual_wins)} | Unclassified: ${number(item.unclassified)}"><span class="gov" style="width:${govWidth}%"></span><span class="individual" style="width:${individualWidth}%"></span><span class="unknown" style="width:${unknownWidth}%"></span></div></td><td class="count">${number(item.government_wins)}</td><td class="count">${number(item.individual_wins)}</td><td class="count">${number(item.unclassified)}</td><td class="rate">${rate}</td></tr>`;}
		async function load(){try{const response=await fetch('/analytics/judge-outcomes?limit=50');if(!response.ok)throw new Error(`Request failed (${response.status})`);const data=await response.json();document.getElementById('summary').innerHTML=metric('Judges ranked',data.judges.length)+metric('Decisions shown',number(data.totals.decisions))+metric('Classified outcomes',number(data.totals.classified));document.getElementById('rows').innerHTML=data.judges.map(row).join('')||'<tr><td colspan="8" class="empty">No judge outcome data is available.</td></tr>';}catch(error){document.getElementById('rows').innerHTML=`<tr><td colspan="8" class="empty">${escape(error.message)}</td></tr>`;}}
		load();
	</script>
</body>
</html>"""
