"""Structure-based discussion units: shape, sub-theme hand-over, and the flag in the reader (off by default)."""
import copy

from backend import reader_service
from backend.contextual_authority.structure_units import STRUCTURE_UNITS_METHOD, structure_report

TEXTS = [
    "Smith v. Canada (Citizenship and Immigration) Court (s) Database Federal Court Decisions",
    "[1] This is an application for judicial review of a decision of the Refugee Appeal Division.",
    "[2] The applicant is a citizen of Nigeria.",
    "[3] In March 2018 she arrived in Canada.",
    "[4] The sole issue is whether the RAD decision was reasonable. The standard of review is reasonableness.",
    "[5] The applicant argues that the RAD ignored the evidence.",
    "[6] I find that the RAD ignored the evidence.",
    "[7] In my view this was a reviewable error.",
    "[8] The respondent submits that the decision was reasonable.",
    "[9] I disagree with the respondent.",
    "[10] For these reasons, the application is allowed. THIS COURT'S JUDGMENT is that the application is allowed.",
]


def _report():
	paragraphs = [{"paragraph_index": i, "text": text, "source_paragraph_index": i} for i, text in enumerate(TEXTS)]
	# similarity units cut every two paragraphs; one sub-theme sits on paragraphs 6-7
	units = [
		{"discussion_unit_id": f"case:7:{n}", "start_paragraph": 2 * n, "end_paragraph": min(2 * n + 1, len(TEXTS) - 1),
		 "paragraph_count": 2 if 2 * n + 1 < len(TEXTS) else 1,
		 "subthemes": [{"subtheme_id": "s1", "paragraph_indices": [6, 7], "key_terms": ["evidence"], "argument_roles": [], "explanation": "x", "argument_evidence": []}] if n == 3 else []}
		for n in range(6)
	]
	return {"case_id": 7, "paragraphs": paragraphs, "discussion_units": units, "discussion_unit_count": len(units)}


def test_structure_units_cover_the_decision_once_in_order_and_keep_the_report_shape():
	base = _report()
	before = copy.deepcopy(base)
	out = structure_report(base)
	assert base == before  # the cached original is untouched
	units = out["discussion_units"]
	assert units[0]["start_paragraph"] == 0 and units[-1]["end_paragraph"] == len(TEXTS) - 1
	for left, right in zip(units, units[1:]):
		assert right["start_paragraph"] == left["end_paragraph"] + 1
	assert sum(unit["paragraph_count"] for unit in units) == len(TEXTS)
	assert out["unit_source"] == STRUCTURE_UNITS_METHOD and out["discussion_unit_count"] == len(units)
	assert [u["start_paragraph"] for u in units] != [u["start_paragraph"] for u in base["discussion_units"]]
	assert [int(unit["discussion_unit_id"].rsplit(":", 1)[-1]) for unit in units] == list(range(len(units)))
	assert all(unit["discussion_unit_id"].startswith("case:7:") for unit in units)


def test_subthemes_move_to_the_unit_holding_their_first_paragraph():
	units = structure_report(_report())["discussion_units"]
	holders = [u for u in units if u["subthemes"]]
	assert len(holders) == 1 and holders[0]["start_paragraph"] <= 6 <= holders[0]["end_paragraph"]


def test_reports_without_text_or_units_come_back_unchanged():
	assert structure_report({"paragraphs": [], "discussion_units": []}) == {"paragraphs": [], "discussion_units": []}
	only_units = {"discussion_units": [{"discussion_unit_id": "c:0"}]}
	assert structure_report(only_units) is only_units


def _summary(monkeypatch, flag):
	base = _report()
	monkeypatch.setattr(reader_service, "_cached_inspect_base", lambda db, case_id, chunks: base)
	if flag:
		monkeypatch.setenv("ILIT_STRUCTURE_UNITS", "1")
	else:
		monkeypatch.delenv("ILIT_STRUCTURE_UNITS", raising=False)
	return reader_service._build_evidence_summary(7, None, has_paragraph_chunks=True, title="Smith v. Canada")


def test_flag_off_keeps_the_similarity_units_and_flag_on_switches(monkeypatch):
	off = _summary(monkeypatch, False)
	on = _summary(monkeypatch, True)
	assert [u.start_paragraph for u in off.units] == [0, 2, 4, 6, 8, 10]
	assert [u.start_paragraph for u in on.units] != [u.start_paragraph for u in off.units]
	for summary in (off, on):
		assert summary.units[0].start_paragraph == 0 and summary.units[-1].end_paragraph == len(TEXTS) - 1
		for unit in summary.units:  # printed numbers and roles are still filled in
			assert unit.role in {"metadata", "overview", "facts", "issues", "analysis", "disposition"}
			if unit.start_number is not None:
				assert unit.end_number >= unit.start_number
		for unit in summary.units:  # party arguments stay inside their unit
			for argument in unit.party_arguments:
				assert unit.start_paragraph <= argument.paragraph_index <= unit.end_paragraph
	assert [u.role for u in on.units][0] == "metadata" and [u.role for u in on.units][-1] == "disposition"
