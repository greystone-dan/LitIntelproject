"""Paste-based Table of Authorities builder page."""


def table_of_authorities_page_html() -> str:
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Table of Authorities | AI CaseLibrary</title>
  <style>
    body{max-width:900px;margin:48px auto;padding:0 20px;font:16px/1.5 system-ui,sans-serif;color:#182421;background:#f3f7f3}
    main{padding:28px;background:#fff;border:1px solid #cbd8d0}h1{margin-top:0}
    textarea{box-sizing:border-box;width:100%;min-height:340px;padding:12px;font:14px/1.5 monospace}
    button{margin:12px 8px 0 0;padding:10px 16px;border:0;background:#182421;color:white;font-weight:700;cursor:pointer}
    button.secondary{border:1px solid #87958e;background:white;color:#182421}
    #status{min-height:1.5em;color:#40514a}#status.error{color:#a33b27}
    .privacy{font-size:13px;color:#53615b}
  </style>
</head>
<body><main>
  <h1>Table of Authorities</h1>
  <p>Paste case citations below, one per line. Paragraph references such as “at para 23” are retained in the output. Authorities are checked against local case citation metadata only.</p>
  <form id="builder">
    <label for="text">Case citations (maximum 200 nonblank lines)</label>
    <textarea id="text" name="text" required></textarea>
    <div><button id="build" type="submit">Build DOCX</button><button class="secondary" id="clear" type="button">Clear</button></div>
  </form>
  <p class="privacy">Privacy: submitted text is processed for this request only. It is not stored or included in application logs.</p>
  <p id="status" role="status" aria-live="polite"></p>
</main>
<script>
const form=document.getElementById('builder'),input=document.getElementById('text'),status=document.getElementById('status'),button=document.getElementById('build');
form.addEventListener('submit',async event=>{
  event.preventDefault();
  const lines=input.value.split(/\\r\\n|\\r|\\n/).filter(line=>line.trim()).length;
  if(lines>200){status.textContent='Please limit the submission to 200 nonblank lines (received '+lines+').';status.className='error';return}
  button.disabled=true;status.className='';status.textContent='Building document…';
  try{
    const response=await fetch('/table-of-authorities/build',{method:'POST',body:new FormData(form)});
    if(!response.ok){let message='Request failed ('+response.status+')';try{message=(await response.json()).detail||message}catch(_){}throw new Error(message)}
    const blob=await response.blob(),url=URL.createObjectURL(blob),link=document.createElement('a');
    link.href=url;link.download='table-of-authorities.docx';link.click();URL.revokeObjectURL(url);status.textContent='DOCX downloaded.';
  }catch(error){status.textContent=error.message;status.className='error'}
  finally{button.disabled=false}
});
document.getElementById('clear').addEventListener('click',()=>{input.value='';status.textContent='';status.className='';input.focus()});
</script></body></html>"""
