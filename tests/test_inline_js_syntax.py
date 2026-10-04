import re
import shutil
import subprocess

import pytest

from backend.pages.case_compare import case_compare_page_html
from backend.pages.case_quick_summary import inject_case_quick_summary
from backend.pages.citation_map import citation_map_html
from backend.pages.citation_pass import citation_pass_page_html
from backend.pages.data_explorer import data_explorer_page_html
from backend.pages.deidentify import deidentify_page_html
from backend.pages.discussion_units_sandbox import discussion_units_sandbox_page_html
from backend.pages.fc_analytics import inject_fc_analytics
from backend.pages.issue_brief import issue_brief_page_html
from backend.pages.judge_outcomes import judge_outcomes_page_html
from backend.pages.live_analysis import live_analysis_page_html
from backend.pages.memo_authority_suggestions import SUGGESTION_SCRIPT
from backend.pages.memo_citation_check import memo_citation_check_page_html
from backend.pages.prototype import prototype_page_html
from backend.pages.quick_search import quick_search_page_html
from backend.pages.research import research_page_html
from backend.pages.saved_searches import saved_searches_page_html
from backend.pages.statute_viewer import statute_viewer_page_html
from backend.pages.tag_analytics import inject_tag_analytics
from backend.pages.tag_finder import tag_finder_page_html
from backend.pages.testing import testing_page_html as render_testing_page_html
from backend.pages.theme_explorer import theme_explorer_page_html


PAGE_RENDERERS = [
    ("case_compare", case_compare_page_html),
    ("case_quick_summary", lambda: inject_case_quick_summary("<body></body>")),
    ("citation_map", citation_map_html),
    ("citation_pass", citation_pass_page_html),
    ("data_explorer", data_explorer_page_html),
    ("deidentify", deidentify_page_html),
    ("discussion_units_sandbox", discussion_units_sandbox_page_html),
    ("fc_analytics", lambda: inject_fc_analytics("<body></body>")),
    ("issue_brief", lambda: issue_brief_page_html({})),
    ("judge_outcomes", judge_outcomes_page_html),
    ("live_analysis", live_analysis_page_html),
    ("memo_authority_suggestions", lambda: f"<script>{SUGGESTION_SCRIPT}</script>"),
    ("memo_citation_check", memo_citation_check_page_html),
    ("prototype", prototype_page_html),
    ("quick_search", quick_search_page_html),
    ("research", research_page_html),
    ("saved_searches", saved_searches_page_html),
    ("statute_viewer", statute_viewer_page_html),
    ("tag_analytics", lambda: inject_tag_analytics("<section id='fcAnalyticsPanel'></section>")),
    ("tag_finder", tag_finder_page_html),
    ("testing", render_testing_page_html),
    ("theme_explorer", theme_explorer_page_html),
]


@pytest.fixture(scope="module")
def node_binary():
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is not installed; skipping inline JavaScript syntax checks")
    return node


@pytest.mark.parametrize(("module_name", "render_html"), PAGE_RENDERERS)
def test_inline_scripts_parse_with_node(module_name, render_html, node_binary, tmp_path):
    html = render_html()
    scripts = re.finditer(r"<script\b([^>]*)>(.*?)</script\b[^>]*>", html, re.IGNORECASE | re.DOTALL)

    for index, match in enumerate(scripts, start=1):
        if re.search(r"\bsrc\s*=", match.group(1), re.IGNORECASE):
            continue

        script_path = tmp_path / f"{module_name}-{index}.js"
        script_path.write_text(match.group(2), encoding="utf-8")
        result = subprocess.run(
            [node_binary, "--check", str(script_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode:
            line_match = re.search(rf"{re.escape(str(script_path))}:(\d+)", result.stderr)
            line = line_match.group(1) if line_match else "unknown"
            pytest.fail(
                f"Inline script {index} from backend.pages.{module_name} "
                f"failed node --check at script line {line}:\n{result.stderr}"
            )
