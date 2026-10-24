"""Pinpoints naming more than one paragraph: ranges, lists, "ff", several pinpoints in one citation."""

import pytest

from backend.citation_refine.pinpoints import (
	_expand_range,
	parse_pinpoint,
	paragraph_pinpoints,
	target_paragraphs,
)
from backend.paragraph_cited_by import Occurrence, build_edges, citation_target_paragraph
from backend.reader_service import _pinpoint_response_fields


@pytest.mark.parametrize(
	"text, paragraphs, label",
	[
		("2019 SCC 65 at para 45", (45,), "para 45"),
		("at paras 45-48", (45, 46, 47, 48), "paras 45-48"),
		("at paras. 12–14", (12, 13, 14), "paras 12-14"),
		("paras 278 to 281", (278, 279, 280, 281), "paras 278-281"),
		("paras. 12, 15 and 20", (12, 15, 20), "paras 12, 15, 20"),
		("paras. 45, 47-49 and 52", (45, 47, 48, 49, 52), "paras 45, 47-49, 52"),
		("at para 3 and at para 9", (3, 9), "paras 3, 9"),
		("aux paragraphes 12 et 13", (12, 13), "paras 12-13"),
		# The next citation's reporter volume is not part of the pinpoint.
		("at paras 12-14, 444 N.R. 120", (12, 13, 14), "paras 12-14"),
		("at para 28, 459 N.R. 134", (28,), "para 28"),
	],
)
def test_paragraph_forms(text, paragraphs, label):
	pins = paragraph_pinpoints(text)
	assert pins is not None and pins.paragraphs == paragraphs and pins.label == label
	assert not pins.open_ended


@pytest.mark.parametrize("text", ["para 45 ff", "para 45 ff.", "paras 45 et seq.", "para 45 and following"])
def test_open_ended_pinpoint_keeps_only_stated_paragraphs(text):
	pins = paragraph_pinpoints(text)
	assert pins.paragraphs == (45,) and pins.open_ended and pins.label == "para 45 ff"


def test_page_pinpoints_are_not_paragraphs():
	assert paragraph_pinpoints("at p. 841") is None
	assert paragraph_pinpoints("no pinpoint") is None


def test_very_long_range_is_capped():
	pins = paragraph_pinpoints("paras 20-120")
	assert pins.capped and len(pins.paragraphs) == 30 and pins.paragraphs[0] == 20


def test_stored_paragraph_wins_and_first_is_unchanged():
	assert target_paragraphs("at paras 12-14", None, 13).paragraphs == (13,)
	assert target_paragraphs("at paras 12-14", None, 12).paragraphs == (12, 13, 14)
	assert target_paragraphs("at para. 12", None, 9).paragraphs == (9,)
	assert citation_target_paragraph("reported case at paras. 12-14", None) == 12


def test_reader_fields_carry_all_paragraphs_and_text():
	pins = paragraph_pinpoints("at paras 45-48 ff")
	fields = _pinpoint_response_fields(pins, 9, {(9, 45): "[45] a", (9, 46): "[46] b"})
	assert fields["target_paragraphs"] == [45, 46, 47, 48]
	assert fields["target_pinpoint_label"] == "paras 45-48 ff" and fields["target_pinpoint_open_ended"]
	assert fields["target_chunk_texts"] == {"45": "[45] a", "46": "[46] b"}
	assert _pinpoint_response_fields(None, 9, {}) == {} and _pinpoint_response_fields(pins, None, {}) == {}


def test_each_named_paragraph_gets_a_cited_by_edge():
	text = "x" * 40
	pins = paragraph_pinpoints("at paras 45-46")
	occurrences = [Occurrence(9, paragraph, 5, 20) for paragraph in pins.paragraphs]
	edges = build_edges(text, occurrences)
	assert [(e.target_case_id, e.target_paragraph, e.mentions) for e in edges] == [(9, 45, 1), (9, 46, 1)]


@pytest.mark.parametrize(
	"text, paragraphs",
	[
		# French decisions join ranges with a non-breaking hyphen (U+2011).
		("aux para 88‑90, 94 et 133‑135", (88, 89, 90, 94, 133, 134, 135)),
		("par. 318‑319 et 321‑323", (318, 319, 321, 322, 323)),
		("at paras. 65‑66 and 211‑12", (65, 66, 211, 212)),
		("paras 84−86", (84, 85, 86)),
		("at paras 84 through 86", (84, 85, 86)),
		("aux paragraphes 12 ou 14", (12, 14)),
		("at paras. [84]-[86]", (84, 85, 86)),
		("at para [84]", (84,)),
	],
)
def test_more_range_spellings(text, paragraphs):
	pins = paragraph_pinpoints(text)
	assert pins is not None and pins.paragraphs == paragraphs


@pytest.mark.parametrize(
	"start, end, expected",
	[
		(199, 2, [199, 200, 201, 202]),
		(45, 8, [45, 46, 47, 48]),
		(1203, 5, [1203, 1204, 1205]),
		(10, 12, [10, 11, 12]),
		(45, 48, [45, 46, 47, 48]),
		(199, 1, [199, 200, 201]),
		(50, 20, [50]),
	],
)
def test_abbreviated_and_full_ranges_expand_correctly(start, end, expected):
	assert _expand_range(start, end) == expected


@pytest.mark.parametrize(
	"text, expected",
	[
		("paras 199-02", (199, 200, 201, 202)),
		("paras 45-8", (45, 46, 47, 48)),
		("paras 1203-05", (1203, 1204, 1205)),
		("paras 10-12", (10, 11, 12)),
		("paras 45-48", (45, 46, 47, 48)),
		("paras 50-20", (50,)),
	],
)
def test_pinpoint_parser_expands_abbreviated_and_full_ranges(text, expected):
	pinpoint = parse_pinpoint(text)
	assert pinpoint is not None and pinpoint.values == expected


def test_reporter_year_in_brackets_is_not_a_paragraph():
	assert paragraph_pinpoints("at para 34, [2013] 2 S.C.R. 559").paragraphs == (34,)
	assert paragraph_pinpoints("at paras 12-14, [2014] 1 F.C.R. 766").paragraphs == (12, 13, 14)


@pytest.mark.parametrize(
	"text",
	[
		"paragraph 72(1)(a) of the Act",
		"paras 34(1)(f) and 35(2)(b)",
		"paragraph 34 of the IRPA",
		"alinéa 12 de la LIPR, paragraphe 34 de la Loi",
	],
)
def test_statute_provisions_are_not_decision_paragraphs(text):
	assert paragraph_pinpoints(text) is None


def test_non_breaking_hyphen_page_range():
	from backend.citation_refine.pinpoints import parse_pinpoint

	pin = parse_pinpoint("p. 173‑174")
	assert pin.kind == "page" and pin.values == (173, 174)


def test_stored_values_merge_every_paragraph_pinpoint_and_never_cut_a_number():
	import importlib.util, pathlib

	spec = importlib.util.spec_from_file_location("brc", pathlib.Path(__file__).parents[1] / "scripts" / "build_refined_citations.py")
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	from backend.citation_refine.pinpoints import parse_all_pinpoints

	class Row:
		pinpoints = parse_all_pinpoints("at para 3 and at paras 9-10")
		pinpoint = "at paras. 3"

	cols = module.pinpoint_columns(Row)
	assert cols["pinpoint_values"] == "3,9,10" and cols["target_paragraph"] == 3
	joined = module._join_values(range(1000, 1100))
	assert len(joined) <= 255 and all(len(part) == 4 for part in joined.split(","))
