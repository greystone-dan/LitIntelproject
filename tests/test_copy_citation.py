import shutil
import subprocess

from backend.pages.data_explorer import data_explorer_page_html


def test_result_cards_and_reader_have_copy_citation_buttons():
    html = data_explorer_page_html()
    assert 'class="rc-wrap"' in html
    assert 'data-copy-citation="${esc(item.citation||\'\')}"' in html
    assert 'id="readerCopyCite"' in html
    assert "@media print{.copy-cite{display:none!important}}" in html
    # the copy button is a sibling of the open button, never nested inside it
    assert "</button></div>`;};" in html


def test_copy_citation_text_format():
    node = shutil.which("node")
    assert node, "node is required for this test"
    html = data_explorer_page_html()
    start = html.index("function copyCitationText")
    end = html.index("\n", start)
    script = html[start:end] + """
const assert=require('node:assert/strict');
assert.equal(copyCitationText('Baker v. Canada','[1999] 2 SCR 817'),'Baker v. Canada, [1999] 2 SCR 817');
assert.equal(copyCitationText('Baker v. Canada','[1999] 2 SCR 817','12'),'Baker v. Canada, [1999] 2 SCR 817 at para 12');
assert.equal(copyCitationText('','2020 FC 1'),'2020 FC 1');
assert.equal(copyCitationText('Untitled',''),'Untitled');
assert.equal(copyCitationText('',''),'');
"""
    result = subprocess.run([node, "-"], input=script, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr
