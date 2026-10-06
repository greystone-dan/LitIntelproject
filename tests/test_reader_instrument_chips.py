from pathlib import Path

from backend.pages.data_explorer import data_explorer_page_html


def test_treaty_references_are_styled_as_statutes_not_unmatched_cases():
	"""Convention references are stored as kind "instrument"; the reader must treat them like statutes (purple, not case yellow)."""
	html = data_explorer_page_html()
	source = Path("backend/pages/data_explorer.py").read_text(encoding="utf-8")
	assert "citation_kind==='statute'" not in source
	assert "citation_kind!=='statute'" not in source
	assert "['statute','instrument'].includes(item.citation_kind)" in html
