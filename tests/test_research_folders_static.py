import shutil
import subprocess

import pytest

from backend import routes
from backend.pages.research_folders import (
    RESEARCH_FOLDERS_SCRIPT,
    inject_research_folders,
    research_folders_page_html,
)


def test_research_folder_page_and_data_explorer_controls_are_registered():
    page = research_folders_page_html()
    explorer = inject_research_folders(
        '<html><body><div class="saved-search-actions"></div>'
        '<div id="searchResults"></div><section id="caseReaderPanel">'
        '<div class="reader-toolbar"></div></section></body></html>'
    )

    assert 'id="researchFoldersApp"' in page
    assert 'id="researchFolderCreate"' in page
    assert 'id="researchFolderBackup"' in page
    assert 'id="researchFolderImport"' in page
    assert 'id="researchFolderList"' in page
    assert 'href="/data-explorer"' in page
    assert 'id="researchFolderPicker"' in explorer
    assert "link.id = 'researchFoldersLink'" in RESEARCH_FOLDERS_SCRIPT
    assert "Add to folder" in RESEARCH_FOLDERS_SCRIPT
    assert "new MutationObserver(mountSearchControls)" in RESEARCH_FOLDERS_SCRIPT
    assert "activeCaseId" in RESEARCH_FOLDERS_SCRIPT


def test_research_folder_injection_preserves_current_search_and_summary_controls():
    html = routes._data_explorer_page_html()

    for marker in (
        'id="researchFolderPicker"',
        'id="searchTipsToggle"',
        'id="searchQueryEcho"',
        'id="readerCaseSummaryToggle"',
        'id="readerCaseSummaryDetail"',
    ):
        assert marker in html


def test_research_folder_storage_failure_and_user_actions_are_visible():
    assert "localStorage.setItem(probe" in RESEARCH_FOLDERS_SCRIPT
    assert "catch (error)" in RESEARCH_FOLDERS_SCRIPT
    assert "Browser storage is unavailable" in RESEARCH_FOLDERS_SCRIPT
    assert "window.confirm(" in RESEARCH_FOLDERS_SCRIPT
    assert "Rename" in RESEARCH_FOLDERS_SCRIPT
    assert "Delete folder" in RESEARCH_FOLDERS_SCRIPT
    assert "textarea" in RESEARCH_FOLDERS_SCRIPT
    assert "JSON.stringify(state, null, 2)" in RESEARCH_FOLDERS_SCRIPT
    assert "normalizeState(JSON.parse(await file.text()))" in RESEARCH_FOLDERS_SCRIPT
    assert "selected.length > 500" in RESEARCH_FOLDERS_SCRIPT
    assert "'unclassified'" in RESEARCH_FOLDERS_SCRIPT


def test_research_folder_javascript_passes_node_syntax_check():
    node = shutil.which("node")
    if not node:
        pytest.skip("Node.js is not installed")
    result = subprocess.run(
        [node, "--check", "-"],
        input=RESEARCH_FOLDERS_SCRIPT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
