"""Phone layout guards. The browser checks (390x844 and 360x740, touch) were run by hand with Playwright;
these tests pin the rules that fixed them so a later change cannot silently bring the problems back."""

import json
import re
import shutil
import subprocess
from pathlib import Path

from backend.pages.data_explorer import data_explorer_page_html

PAGES = Path(__file__).resolve().parent.parent / "backend" / "pages"
MOBILE_CSS = (PAGES / "mobile_layout.css").read_text(encoding="utf-8")
MARKUP_CSS = (PAGES / "markup_mode.css").read_text(encoding="utf-8")
MARKUP_JS = (PAGES / "markup_mode.js").read_text(encoding="utf-8")
RISK_JS = (PAGES / "overruling_risk_reader.js").read_text(encoding="utf-8")


def _phone_block(css: str) -> str:
    start = css.index("@media(max-width:760px){")
    depth, i = 0, css.index("{", start)
    begin = i
    while True:
        if css[i] == "{":
            depth += 1
        elif css[i] == "}":
            depth -= 1
            if depth == 0:
                return css[begin:i]
        i += 1


def test_mobile_css_is_injected_last():
    html = data_explorer_page_html()
    assert MOBILE_CSS.strip() in html
    assert html.index(MOBILE_CSS.strip()) > html.index(MARKUP_CSS.strip().splitlines()[0])


def test_search_form_stacks_on_phones():
    block = _phone_block(MOBILE_CSS)
    assert "#searchPanel .search-query-row{flex-direction:column!important" in block
    assert "#searchPanel .search-actions{margin-top:0!important" in block
    # 16px text keeps iOS from zooming into the field
    assert "input#searchQuery{height:50px!important;font-size:16px!important" in block
    # filters scroll sideways in one row instead of a tall wrapped block
    assert "overflow-x:auto" in block and ".quick-filters .qf-group" in block
    assert "html,body{overflow-x:hidden}" in block


def test_reader_is_not_fixed_height_or_overlapping_on_phones():
    block = _phone_block(MOBILE_CSS)
    assert ".inline-case-reader{height:auto!important" in block
    assert ".reader-toolbar{position:static!important" in block
    assert ".reader-hover-tooltip{display:none!important}" in block
    # the decision pane comes before case information
    assert ".reader-pane.source{min-height:0!important;order:1}" in block


def test_markup_bar_is_compact_and_not_sticky_on_phones():
    block = _phone_block(MARKUP_CSS)
    assert "#markupBar{position:static" in block
    assert "#markupBar:not(.is-open) .mk-row2" in block
    assert ".mk-panel.float,.mk-panel.dock{position:fixed;left:8px!important;right:8px!important" in block
    assert "max-height:45vh" in block
    assert "#mkHover{display:none!important}" in block
    assert "@media(hover:none){#mkHover{display:none!important}}" in MARKUP_CSS
    assert 'data-mk-act="more"' in MARKUP_JS and "state.barOpen" in MARKUP_JS
    assert "(hover: none)" in MARKUP_JS  # a tap must open the panel, not also a hover card
    assert "markup-peeking" in MARKUP_JS and "markup-peeking #markupStage" in MARKUP_CSS


def test_overruling_notice_folds_on_phones():
    assert "document.createElement('details')" in RISK_JS


def test_overruling_notice_details_are_closed_on_every_screen_size():
    node = shutil.which("node")
    assert node, "node is required for this test"
    script = r"""
const assert=require('node:assert/strict');
const banner={hidden:true,children:[],replaceChildren(){this.children=[]},append(...n){this.children.push(...n)}};
const document={getElementById(){return banner},
  createElement(tag){return {tag,textContent:'',children:[],append(...n){this.children.push(...n)}}},
  createTextNode(t){return {tag:'text',textContent:String(t),children:[]}}};
const readerState={caseId:null,payload:null};
let narrow=true;
global.window={matchMedia:()=>({matches:narrow})};
let openDecision=async id=>{readerState.caseId=Number(id);readerState.payload={}};
let closeDecisionReader=()=>{};
const payload={assessment:'A',flags:[{assignment:'indirect',event:'E',event_date:'2019-01-01',decision_date:'2018-01-01',rationale:'R',source:'S',how_assigned:'H',notice:'N'}]};
const fetch=async()=>({ok:true,json:async()=>payload});
const controller = __CONTROLLER__;
(async()=>{
  await openDecision(7);await new Promise(r=>setTimeout(r,0));
  let details=banner.children.find(c=>c.tag==='details');
  assert.ok(details,'details wrapper exists');assert.equal(details.open,false);
  assert.equal(banner.children[0].tag,'strong');
  narrow=false;
  await openDecision(7);await new Promise(r=>setTimeout(r,0));
  details=banner.children.find(c=>c.tag==='details');assert.equal(details.open,false);
})().catch(e=>{console.error(e);process.exitCode=1});
""".replace("__CONTROLLER__", RISK_JS)
    result = subprocess.run([node, "-"], input=script, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr


def test_other_tabs_have_phone_rules():
    assert ".about-story{grid-template-columns:minmax(0,1fr)!important}" in MOBILE_CSS
    assert ".panel-card table{display:block;max-width:100%;overflow-x:auto" in MOBILE_CSS
    assert "#judgeComparisonForm input{display:block;width:100%" in MOBILE_CSS


def test_statute_viewer_form_wraps_on_phones():
    from backend.case_reader_ui import statute_viewer_page_html

    html = statute_viewer_page_html()
    assert "@media (max-width: 600px)" in html and ".search-form { flex-wrap: wrap; }" in html
