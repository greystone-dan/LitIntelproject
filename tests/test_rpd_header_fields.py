from backend.metadata import _rpd_header_fields

NEW_FORMAT = """RPD File No. / No de dossier de la SPR : MB5-04801
Reasons and Decision - Motifs et décision
Place of hearing
Montréal, Quebec
Date of decision
and reasons
March 1, 2016
Panel
Julie Morin
Tribunal
Counsel for the claimant(s)
Me Tony Manglaviti
"""

OLD_FORMAT = """Immigration and Refugee Board
Refugee Protection Division
Place (s) of Hearing
Vancouver, B.C.
Date of Decision
September 22, 2004
Panel
Tribunal
Barbara Hodgins
Claimant's Counsel
Martin Bauer
"""


def test_new_format_panel_and_one_line_place():
	assert _rpd_header_fields(NEW_FORMAT) == {"judge": "Julie Morin", "place of hearing": "Montréal, Quebec"}


def test_old_format_panel_after_tribunal_label():
	assert _rpd_header_fields(OLD_FORMAT) == {"judge": "Barbara Hodgins", "place of hearing": "Vancouver, B.C."}


def test_non_rpd_text_is_left_alone():
	assert _rpd_header_fields("Federal Court\nPanel\nJohn Smith\n") == {}
