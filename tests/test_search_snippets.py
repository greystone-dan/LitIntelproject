from backend import routes
from backend.analytics_service import clean_search_snippet


def test_clean_search_snippet_collapses_whitespace_and_marks_cut_ends():
    assert clean_search_snippet("  procedural\n\n fairness   was\tbreached ") == "…procedural fairness was breached…"


def test_clean_search_snippet_is_none_for_blank_text():
    assert clean_search_snippet(None) is None
    assert clean_search_snippet("  \n ") is None


def test_result_card_shows_and_escapes_the_snippet():
    html = routes._data_explorer_page_html()

    assert "function snippetHtml(text,query)" in html
    assert "professionalResultCard=function(item,query='')" in html
    assert 'class="result-snippet">${snippetHtml(item.snippet,query)}' in html
    # The excerpt is escaped before the query is wrapped in <mark>.
    assert "esc(raw.slice(hit,hit+q.length))" in html
