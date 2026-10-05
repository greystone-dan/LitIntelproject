import json
import shutil
import subprocess

from backend.pages.data_explorer import data_explorer_page_html

PROBE = """
const assert=require('node:assert/strict');
assert.equal(hoverParagraph('[6] one [7] two words [8] three',7),'[7] two words ');
assert.equal(hoverParagraph('no marker here',7),'no marker here');
assert.equal(hoverClip('a b c d',3),'a b\\u2026');
const s=hoverCitationInfo({citation_kind:'statute',authority_document_title:'IRPA',provision_section:'96',provision_text:'A Convention refugee is...'});
assert.equal(s.title,'IRPA');assert.equal(s.label,'Section 96');assert.match(s.text,/Convention refugee/);
assert.match(hoverCitationInfo({citation_kind:'statute',provenance:'statute_references'}).note,/not in the iLit library/);
assert.match(hoverCitationInfo({citation_kind:'case_short',citation_text:'X'}).note,/not in the iLit library/);
assert.match(hoverCitationInfo({citation_kind:'case_short',target_case_id:2}).note,/no pinpoint/);
const c=hoverCitationInfo({citation_kind:'case_short',target_case_id:2,target_title:'Vavilov',target_citation:'2019 SCC 65',target_paragraph:7,target_chunk_text:'[6] a [7] the text [8] b'});
assert.equal(c.text,'[7] the text ');assert.match(c.label,/Paragraph 7/);
assert.match(hoverCitationInfo({citation_kind:'case_short',target_case_id:2,target_paragraph:7}).note,/Paragraph 7 is not stored/);
"""


def test_hover_card_helpers():
    node = shutil.which("node")
    assert node, "node is required for this test"
    html = data_explorer_page_html()
    start = html.index("function hoverParagraph")
    end = html.index("let hoverRowsKey", start)
    res = subprocess.run([node, "-e", html[start:end] + PROBE], capture_output=True, text=True)
    assert res.returncode == 0, res.stderr


def test_statute_merge_keeps_case_citations():
    html = data_explorer_page_html()
    assert "provenance!=='statute_references'" in html
    assert "const row=element.dataset.citeId?hoverRow" in html or "hoverRow(element.dataset.citeId)" in html
