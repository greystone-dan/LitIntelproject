"""Find the unit (experimental search box): wiring, Experimental gating and card rendering."""
import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

from backend.pages.data_explorer import data_explorer_page_html

PAGES = Path(__file__).resolve().parents[1] / "backend" / "pages"


def test_panel_is_injected_and_hidden_unless_experimental():
	html = data_explorer_page_html()
	assert html.count('id="unitSearchPanel"') == 1
	assert (PAGES / "unit_search_ui.js").read_text(encoding="utf-8") in html
	assert (PAGES / "unit_search_ui.css").read_text(encoding="utf-8") in html
	assert "body:not(.reader-experimental) #unitSearchPanel{display:none!important}" in html


def test_ui_calls_only_the_unit_search_endpoint_and_no_model():
	js = (PAGES / "unit_search_ui.js").read_text(encoding="utf-8")
	assert "/unit-search?" in js
	for forbidden in ("openai", "ollama", "embedding", "/rag", "semantic"):
		assert forbidden not in js.lower()


def test_card_html_shows_case_unit_judge_and_escapes_text():
	node = shutil.which("node")
	if node is None:
		pytest.skip("node is not installed")
	js = (PAGES / "unit_search_ui.js").read_text(encoding="utf-8")
	snippet = re.search(r"/\* unit-search-cards:start \*/(.*?)/\* unit-search-cards:end \*/", js, re.S).group(1)
	esc = "const esc=value=>String(value??'').replace(/[&<>\"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',\"'\":'&#39;'}[c]));"
	rows = [
		{"case_id": 7, "title": "A <b>v</b> B", "citation": "TB4-03181", "court": "RAD", "date": "2019-01-02", "judge": "S.S. Kular",
		 "judge_label": "Member", "outcome": "allowed", "unit_index": 7, "role": "analysis", "start_number": 16, "end_number": 44,
		 "paragraph_number": 30, "snippet": "The RAD finds <script>"},
		{"case_id": 8, "title": None, "unit_index": 1, "role": None, "start_number": None, "end_number": None, "paragraph_number": None, "snippet": "x"},
	]
	probe = esc + snippet + "\nconsole.log(JSON.stringify(JSON.parse(process.argv[1]).map(unitCardHtml)));"
	out = json.loads(subprocess.run([node, "-e", probe, json.dumps(rows)], capture_output=True, text=True, check=True).stdout)
	first, second = out
	assert 'data-us-case="7"' in first and 'data-us-para="30"' in first
	assert "Member: S.S. Kular" in first and "Outcome: allowed" in first
	assert "Unit 7 · ¶16–44 · Analysis · match at ¶30" in first
	assert "<script>" not in first and "&lt;script&gt;" in first and "A &lt;b&gt;v&lt;/b&gt; B" in first
	assert 'data-us-para=""' in second and "no paragraph number" in second and "Untitled decision" in second


def test_arrival_highlight_beats_the_readers_own_paragraph_rules():
	css = (PAGES / "unit_search_ui.css").read_text(encoding="utf-8")
	assert "#decisionBody .fmt-para.us-flash" in css and "background:#fde68a!important" in css
	assert "classList.add('us-flash')" in (PAGES / "unit_search_ui.js").read_text(encoding="utf-8")
