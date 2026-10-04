"""Complete Discussion Units sandbox page built on the Data Explorer shell."""

from .data_explorer import data_explorer_page_html
from .skip_link import with_skip_link


@with_skip_link
def discussion_units_sandbox_page_html() -> str:
    html = data_explorer_page_html()
    for source, target in (
        ("/analytics/search/cases/", "/discussion-units-sandbox/cases/"),
        ("/analytics/search/cases?", "/discussion-units-sandbox/search?"),
        ("/cases/${caseId}/reader-data", "/discussion-units-sandbox/cases/${caseId}/reader-data"),
        (
            "/cases/${readerState.caseId}/statute-references",
            "/discussion-units-sandbox/cases/${readerState.caseId}/statute-references",
        ),
        ("/cases/${data.case?.id}/activity", "/discussion-units-sandbox/cases/${data.case?.id}/activity"),
        ("/data-explorer", "/discussion-units-sandbox"),
    ):
        html = html.replace(source, target)
    html = html.replace(
        "<title>Immigration Litigation Intelligence Tool | iLIT</title>",
        "<title>Sandbox | iLIT</title>",
    )
    html = html.replace(
        '<a class="active" href="/discussion-units-sandbox">Research</a>',
        '<a class="active" href="/discussion-units-sandbox">Sandbox</a>',
    )
    html = html.replace("Immigration Litigation Intelligence Tool", "Sandbox")
    html = html.replace(
        "</body>",
        """<script>
const sandboxAssessmentState={enabled:false,caseId:null,rows:{}};
function sandboxAssessmentHtml(row){return `<aside class="sandbox-assessment"><strong>${esc(row.topic||'Unclassified')}</strong><span>${esc(row.role||'Role unavailable')} · confidence ${esc(row.confidence??'n/a')}</span><p>${esc(row.explanation||'')}</p></aside>`;}
async function loadSandboxAssessments(){const caseId=readerState.caseId;if(!caseId)return;sandboxAssessmentState.caseId=caseId;const response=await fetch(`/discussion-units-sandbox/cases/${caseId}/paragraph-assessments`);if(!response.ok)throw new Error(`Assessment request failed (${response.status})`);const data=await response.json();sandboxAssessmentState.rows=data.assessments||{};sandboxAssessmentState.enabled=true;renderSandboxAssessments();}
function renderSandboxAssessments(){document.querySelectorAll('#decisionBody .chunk-body').forEach((body,index)=>{body.closest('.reader-chunk')?.querySelector('.sandbox-assessment')?.remove();const chunk=readerState.payload?.readerData?.chunks?.[index],number=String(chunk?.paragraph_start??index+1),row=sandboxAssessmentState.rows[number];if(row)body.insertAdjacentHTML('afterend',sandboxAssessmentHtml(row));});}
function installSandboxAssessmentToggle(){const target=document.getElementById('decisionTarget');if(!target||target.querySelector('#sandboxAssessmentToggle'))return;const button=document.createElement('button');button.id='sandboxAssessmentToggle';button.className='secondary';button.type='button';button.textContent='Show paragraph assessments';button.onclick=async()=>{if(!sandboxAssessmentState.enabled){button.textContent='Loading assessments...';try{await loadSandboxAssessments()}catch(error){button.textContent=error.message;return}}else{sandboxAssessmentState.enabled=false;document.querySelectorAll('.sandbox-assessment').forEach(item=>item.remove())}button.textContent=sandboxAssessmentState.enabled?'Hide paragraph assessments':'Show paragraph assessments'};target.querySelector('.reader-controls')?.append(button);}
new MutationObserver(installSandboxAssessmentToggle).observe(document.getElementById('decisionTarget'),{childList:true,subtree:true});
</script></body>""",
    )
    return html
