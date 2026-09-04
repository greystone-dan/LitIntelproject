"""HTML page modules served by the FastAPI application."""

from .citation_map import citation_map_html
from .citation_pass import citation_pass_page_html
from .data_explorer import data_explorer_page_html
from .judge_outcomes import judge_outcomes_page_html
from .live_analysis import live_analysis_page_html
from .prototype import prototype_page_html
from .quick_search import quick_search_page_html
from .research import research_page_html
from .testing import testing_page_html

__all__ = [
	"citation_map_html",
	"citation_pass_page_html",
	"data_explorer_page_html",
	"judge_outcomes_page_html",
	"live_analysis_page_html",
	"prototype_page_html",
	"quick_search_page_html",
	"research_page_html",
	"testing_page_html",
]
