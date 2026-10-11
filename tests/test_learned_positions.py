import json

import numpy as np

from backend import learned_positions as lp
from backend import position_tags
from backend.position_holder import HOLDERS

HEADER = "Singh v. Canada (Citizenship and Immigration)\nCourt (s) Database Federal Court\nDate: 20200101\n"
PARAGRAPHS = [
	"[1] The applicant is a citizen of India who claimed refugee protection in Canada.",
	"[2] The applicant submits that the Officer ignored the medical evidence and that the decision is unreasonable.",
	"[3] The Officer found that the evidence was insufficient and rejected the application.",
	"[4] I am not persuaded that the Officer erred. The application for judicial review is dismissed.",
]
FULL_TEXT = HEADER + "\n".join(PARAGRAPHS)


def test_weights_load_and_tags_cover_every_paragraph():
	assert lp.available()
	numbers, tags = lp.tag_decision_text(FULL_TEXT, "Singh v. Canada (Citizenship and Immigration)")
	assert numbers == [1, 2, 3, 4]
	assert [t["source"] for t in tags] == ["learned"] * 4
	assert all(t["holder"] in HOLDERS and 0 < t["p"] <= 1 for t in tags)


def test_probabilities_are_deterministic_and_normalised():
	header, body = lp.split_header(FULL_TEXT)
	a = lp.probabilities(PARAGRAPHS, "Singh v. Canada", header, body)
	b = lp.probabilities(PARAGRAPHS, "Singh v. Canada", header, body)
	assert np.array_equal(a, b)
	assert a.shape == (4, len(HOLDERS)) and np.allclose(a.sum(axis=1), 1.0, atol=0.01)


def test_clear_cues_read_as_expected():
	_, tags = lp.tag_decision_text(FULL_TEXT, "Singh v. Canada (Citizenship and Immigration)")
	assert tags[1]["holder"] == "applicant"
	assert tags[3]["holder"] == "court"


def test_empty_input():
	assert lp.tag_paragraphs([]) == []
	assert lp.tag_decision_text("no numbered paragraphs here") == ([], [])


def _write_learned(directory, case_id):
	directory.mkdir(parents=True, exist_ok=True)
	(directory / f"case_{case_id}.json").write_text(json.dumps({"case_id": case_id, "paragraphs": {"1": {"h": "applicant", "p": 0.9, "r": "facts"}}}))


def test_reader_ignores_learned_files_unless_flag_is_on(tmp_path, monkeypatch):
	stored, learned = tmp_path / "stored", tmp_path / "learned"
	stored.mkdir()
	_write_learned(learned, 777001)
	source = position_tags.FilePositionSource(stored, None, learned)
	monkeypatch.delenv(position_tags.LEARNED_FLAG, raising=False)
	assert position_tags.case_positions(777001, source)["available"] is False
	monkeypatch.setenv(position_tags.LEARNED_FLAG, "1")
	data = position_tags.case_positions(777001, source)
	assert data["available"] is True and data["source"] == "learned"
	assert data["paragraphs"]["1"]["positions"][0]["key"] == "applicant"
	assert "statistical" in data["reliability"]


def test_stored_preview_wins_over_learned(tmp_path, monkeypatch):
	monkeypatch.setenv(position_tags.LEARNED_FLAG, "1")
	_write_learned(tmp_path / "learned", 28105)
	data = position_tags.case_positions(28105, position_tags.FilePositionSource(position_tags.DATA_DIR, position_tags.LAYERS_DIR, tmp_path / "learned"))
	assert data.get("source") != "learned"
