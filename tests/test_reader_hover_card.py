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
assert.match(hoverCitationInfo({citation_kind:'case_short',citation_text:'X'}).note,/not matched this citation/);
assert.match(hoverCitationInfo({citation_kind:'case_short',target_case_id:2}).note,/no pinpoint/);
const c=hoverCitationInfo({citation_kind:'case_short',target_case_id:2,target_title:'Vavilov',target_citation:'2019 SCC 65',target_paragraph:7,target_chunk_text:'[6] a [7] the text [8] b'});
assert.equal(c.text,'[7] the text ');assert.match(c.label,/Paragraph 7/);
const pending=hoverCitationInfo({citation_kind:'case_short',target_case_id:2,target_paragraph:7});
assert.deepEqual(pending.fetch,{caseId:2,paragraphs:[7]});assert.match(pending.note,/Loading/);
assert.match(hoverCitationInfo({citation_kind:'case_short',target_case_id:2,target_paragraph:7,_hoverFetched:true}).note,/Paragraph 7 is not stored/);
assert.equal(hoverCitationInfo({citation_kind:'case_short',target_case_id:2,target_paragraph:7,target_chunk_text:'[7] x'}).fetch,undefined);
assert.equal(hoverCitationInfo({citation_kind:'statute',provision_section:'96',statute_version_label:'Version unknown',provision_text:'t'}).label,'Section 96');
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


def test_hover_card_shows_range_pinpoint():
    node = shutil.which("node")
    html = data_explorer_page_html()
    start = html.index("function hoverParagraph")
    end = html.index("let hoverRowsKey", start)
    probe = """
const assert=require('node:assert/strict');
const c=hoverCitationInfo({citation_kind:'case_short',target_case_id:2,target_title:'V',target_citation:'2019 SCC 65',target_paragraph:7,
 target_paragraphs:[7,8],target_pinpoint_label:'paras 7-8',target_chunk_texts:{7:'[7] a ',8:'[8] b'}});
assert.match(c.label,/Paragraphs 7-8/);assert.match(c.text,/\\[7\\] a/);assert.match(c.text,/\\[8\\] b/);
"""
    res = subprocess.run([node, "-e", html[start:end] + probe], capture_output=True, text=True)
    assert res.returncode == 0, res.stderr


def test_case_info_helpers_clean_dates_and_decision_makers():
    node = shutil.which("node")
    html = data_explorer_page_html()
    start = html.index("const SIDE_MONTHS")
    end = html.index("function sideFact", start)
    probe = """
const assert=require('node:assert/strict');
function sideOutcome(){return null}
assert.equal(sideDate('2018-02-08'),'February 8, 2018');
assert.equal(sideJudge('The Honourable Mr. Justice Mosley'),'Justice Mosley');
assert.equal(sideJudge('The Honourable Madam Justice Strickland'),'Justice Strickland');
assert.equal(sideJudge('JUSTICE ZINN'),'Justice Zinn');
const f=sideCaseFacts({item:{title:'A v B',citation:'2018 FC 147',court:'FC',date:'2018-02-08',docket_number:'IMM-1-17',metadata_json:{reader_extracted:{'place of hearing':'toronto, ontario','date of hearing':'FEBRUARY 5, 2018'}}},meta:{}});
assert.equal(f.docket,'IMM-1-17');assert.equal(f.hearing,'Toronto, Ontario \\u00b7 February 5, 2018');
"""
    res = subprocess.run([node, "-e", html[start:end] + probe], capture_output=True, text=True)
    assert res.returncode == 0, res.stderr
