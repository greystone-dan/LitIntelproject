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


def test_stored_data_covers_the_665_decisions_with_the_reserved_citation_slot() -> None:
	assert len(stored_case_ids()) == 665
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


def test_layer_is_set_where_the_holder_decides_it_and_marked_undetected_otherwise() -> None:
	data = case_positions(28105)
	layers = {row["positions"][0]["key"]: row["layer"] for row in FilePositionSource(layers_directory=None).paragraphs_for(28105).values()}
	assert layers["court"]["key"] == "judge" and layers["court"]["depth"] == 0
	# An applicant or respondent paragraph could be a review argument or a position inside the earlier decision.
	assert layers["respondent"] == {"key": "unknown", **data["layers"]["unknown"]}
	assert data["layers"]["unknown"]["detected"] is False and "nested" in data["legend"]


def test_an_explicit_layer_overrides_the_holder_default(tmp_path: Path) -> None:
	(tmp_path / "case_1.json").write_text(
		'{"paragraphs":{"5":{"h":["applicant"],"k":[],"s":"x","r":"analysis","l":"first_instance"}}}', encoding="utf-8")
	row = FilePositionSource(tmp_path).paragraphs_for(1)["5"]
	assert row["layer"]["key"] == "first_instance" and row["layer"]["depth"] == 2


def test_live_rules_rows_carry_a_layer_too() -> None:
	text = "The Board found that the claim was not credible."
	row = rules_positions(text, _blocks(text))["1"]
	assert row["layer"]["key"] == "earlier_decision"


def test_framework_commentary_is_flagged_from_stored_labels_and_unknown_in_rules() -> None:
	flags = {row["framework"] for row in case_positions(28105)["paragraphs"].values()}
	assert "yes" in flags and "no" in flags
	text = "The applicant submits the test in Vavilov applies."
	assert rules_positions(text, _blocks(text))["1"]["framework"] == "unknown"
	assert "not linked to the cited cases" in case_positions(28105)["framework_note"]


def test_rules_export_sets_the_level_and_default_rows_stay_not_detected() -> None:
	paragraphs = case_positions(28105)["paragraphs"]
	keys = {row["layer"]["key"] for row in paragraphs.values()}
	assert {"jr_party", "framework", "unknown"} <= keys
	assert paragraphs["10"]["layer"]["key"] == "unknown"  # rules decided it by default only
	assert paragraphs["15"]["layer"]["key"] == "framework" and paragraphs["15"]["framework"] == "yes"


def test_reader_script_only_tags_paragraphs_the_page_has() -> None:
	js = (PAGES / "reader_positions.js").read_text(encoding="utf-8")
	assert "data.paragraphs[String(p.dataset.para)]" in js  # tags are looked up from the page's own paragraphs
	assert "real.has(n)" in js  # the legend ignores stored numbers that are not in the decision


def test_lf_builder_derives_a_reader_level_from_holder_and_kind() -> None:
	from scripts.build_position_preview_lf import compact_case, point_layer

	assert point_layer({"holder": "court", "kind": "rule_of_law"}) == 6
	assert point_layer({"holder": "applicant", "kind": "allegation_or_argument", "layer": 2}) == 2
	assert point_layer({"holder": "applicant", "kind": "allegation_or_argument", "layer": 4}) == 4
	raw = {"case_id": 1, "paragraphs": [{"para": 3, "summary": "s", "role": "analysis", "propositions": [
		{"holder": "respondent", "kind": "allegation_or_argument", "layer": 2}, {"holder": "court", "kind": "finding", "layer": 1}, {"holder": "respondent", "kind": "fact", "layer": 2}]}]}
	row = compact_case(raw)["paragraphs"]["3"]
	assert row["h"] == ["respondent", "court"] and row["l"] == "jr_party"


def test_new_stored_decisions_load_from_the_same_reader_path() -> None:
	for case_id in sorted(stored_case_ids())[::40]:
		data = case_positions(case_id)
		assert data["available"] and data["paragraphs"]
		row = next(iter(data["paragraphs"].values()))
		assert row["positions"][0]["key"] in POSITION_LABELS and row["layer"]["key"] in {"judge", "jr_party", "earlier_decision", "first_instance", "framework", "source", "unknown"}
