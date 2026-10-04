def saved_search_alerts_page_html(search_id: int) -> str:
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Saved search alerts</title></head>
<body>
<main>
<h1>Saved search alerts</h1>
<div id="status">Loading…</div>
<pre id="output" style="white-space:pre-wrap;border:1px solid #ddd;padding:12px"></pre>
<script>
(async function(){
  try{
    const res=await fetch(`/saved-searches/{search_id}/alerts`);
    if(!res.ok)throw new Error('Request failed');
    const data=await res.json();
    document.getElementById('status').textContent = `Search ${data.search_id}: ${data.new_case_matches.length} new case matches`;
    document.getElementById('output').textContent = JSON.stringify(data, null, 2);
  }catch(e){document.getElementById('status').textContent = 'Error: '+e.message}
})();
</script>
</main>
</body></html>"""
