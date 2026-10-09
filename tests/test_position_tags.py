"""Whose-position tags (preview): stored source, rules-only source, route, Live Analysis payload and page assets."""

from pathlib import Path

from fastapi.testclient import TestClient

from backend.live_reader import build_live_reader_payload, format_blocks_for_text
from backend.live_analysis import paragraphs_from_pasted_text
from backend.main import app
from backend.pages.data_explorer import data_explorer_page_html
from backend.position_tags import (
	POSITION_LABELS,
	FilePositionSource,
	case_positions,
	rules_positions,
	stored_case_ids,
)

PAGES = Path(__file__).resolve().parents[1] / "backend" / "pages"


def _blocks(text: str) -> list[dict]:
	return format_blocks_for_text(text)


def test_stored_data_covers_the_100_decisions_with_the_reserved_citation_slot() -> None:
	assert len(stored_case_ids()) == 100
	data = case_positions(28105)
	assert data["available"] and data["preview"] and data["mode"] == "stored"
	assert "not yet checked by a lawyer" in data["notice"]
	row = data["paragraphs"]["3"]
	assert row["summary"] and row["positions"][0]["key"] in POSITION_LABELS
	assert row["citations"] == []


def test_unknown_decision_is_unavailable_not_an_error() -> None:
	assert case_positions(999999999)["available"] is False
	assert FilePositionSource(Path("/nonexistent")).paragraphs_for(1) is None


def test_route_serves_stored_positions_without_a_database() -> None:
	client = TestClient(app)
	body = client.get("/cases/28105/paragraph-positions").json()
	assert body["available"] and "3" in body["paragraphs"]
	assert client.get("/cases/999999999/paragraph-positions").json()["available"] is False


def test_rules_tag_clear_cues_and_leave_the_rest_untagged() -> None:
	text = (
		"The applicant submits that the officer ignored the evidence.\n\n"
		"The respondent argues the decision was reasonable.\n\n"
		"The Board found that the claimant lacked credibility.\n\n"
		"I am not persuaded by this argument.\n\n"
		"The applicant arrived in Canada in 2019."
	)
	rows = rules_positions(text, _blocks(text))
	assert [rows[str(n)]["positions"][0]["key"] for n in (1, 2, 3, 4)] == [
		"applicant", "respondent", "earlier_decision_maker", "court"]
	assert "5" not in rows
	assert rows["1"]["cue"] == "The applicant submits" and rows["1"]["summary"] == ""
	assert rows["1"]["citations"] == []


def test_rules_read_french_cues() -> None:
	text = "Le demandeur soutient que l’agent a erré.\n\nLa SPR a conclu que la demande n’était pas crédible."
	rows = rules_positions(text, _blocks(text))
	assert rows["1"]["positions"][0]["key"] == "applicant"
	assert rows["2"]["positions"][0]["key"] == "earlier_decision_maker"


def test_live_payload_carries_the_rules_block() -> None:
	text, paragraphs = paragraphs_from_pasted_text("The applicant submits that the decision was unfair.\n")
	payload = build_live_reader_payload(text, paragraphs, "memo.txt")
	block = payload["readerData"]["position_tags"]
	assert block["mode"] == "rules" and block["available"] and "no AI" in block["notice"]


def test_reader_page_injects_the_assets_and_makes_no_model_calls() -> None:
	html = data_explorer_page_html()
	css = (PAGES / "reader_positions.css").read_text(encoding="utf-8")
	js = (PAGES / "reader_positions.js").read_text(encoding="utf-8")
	assert css in html and js in html
	assert html.index(css) < html.index((PAGES / "mobile_layout.css").read_text(encoding="utf-8"))
	assert "paragraph-positions" in js and "data-pos-cites" in js and "@media(max-width:700px)" in css
	for forbidden in ("openai", "ollama", "embedding", "/rag"):
		assert forbidden not in js.lower()
