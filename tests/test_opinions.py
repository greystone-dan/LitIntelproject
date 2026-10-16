from backend.case_formatter import format_decision
from backend.contextual_authority.heading_reader import read_headings
from backend.contextual_authority.opinions import cover_author, find_opinions, opinion_title
from backend.contextual_authority import opinions as op
from backend.contextual_authority.outline_v2 import _mark_printed_headings, _units, outline_v2


def _p(n: int, tail: str = "the evidence and the arguments of the parties in some detail here.") -> str:
	return f"[{n}] The Court considered {tail}"


def _scc(index: bool = True) -> str:
	head = ["Smith v. Canada", "Decision Content", "SUPREME COURT OF CANADA", "Citation: Smith v. Canada, 2015 SCC 9", "Coram: McLachlin C.J. and Abella, Rothstein JJ."]
	if index:
		head += ["Reasons for Judgment:", "(paras. 1 to 12)", "Dissenting Reasons:", "(paras. 13 to 24)", "Fish J. (Abella J. concurring)", "Rothstein J."]
	head += ["______________________________", "Smith v. Canada, 2015 SCC 9", "Indexed as: Smith v. Canada", "Held (Rothstein J. dissenting): The appeal should be dismissed.", "Counsel for the appellant."]
	lead = ["The judgment of McLachlin C.J. and Abella J. was delivered by", "Fish J. —", "I. Introduction"] + [_p(n) for n in range(1, 5)]
	lead += ["II. Analysis"] + [_p(n) for n in range(5, 12)] + ["[12] I would dismiss the appeal with costs."]
	dis = ["The reasons of Rothstein J. were delivered by", "Rothstein J. (dissenting) —", "III. Analysis"] + [_p(n) for n in range(13, 23)] + ["[23] The error is clear.", "[24] I would allow the appeal and enter a conviction."]
	return "\n".join(head + lead + dis + ["Appeal dismissed, Rothstein J. dissenting.", "Solicitors for the appellant: Smith."])


def _units_of(text: str):
	blocks = _mark_printed_headings(text, format_decision(text, {}), read_headings(text))
	return _units(text, blocks)


def test_index_gives_each_opinion_its_first_paragraph():
	text = _scc()
	found = find_opinions(text, _units_of(text))
	assert [(o.kind, o.para, o.source) for o in found] == [("lead", 1, "index"), ("dissenting", 13, "index")]
	assert found[0].author == "Fish J." and found[0].concurring == "Abella J."


def test_opening_lines_find_the_opinions_when_there_is_no_index():
	text = _scc(index=False)
	found = find_opinions(text, _units_of(text))
	assert [o.kind for o in found] == ["lead", "dissenting"]
	assert found[1].source == "openers" and found[1].para == 13


def test_disposition_belongs_to_the_lead_opinion(monkeypatch):
	monkeypatch.setenv("ILIT_OUTLINE_HEADINGS", "1")
	text = _scc()
	rows = outline_v2(text, format_decision(text, {}))
	assert [r["opinion"] for r in rows if r["kind"] == "opinion"] == ["lead", "dissenting"]
	dispositions = [r for r in rows if r["kind"] == "section" and r["section"] == "disposition"]
	assert len(dispositions) == 1 and dispositions[0]["para"] <= 12


def test_bare_numbered_paragraphs_still_give_printed_headings():
	lines = ["Smith v. Canada", "Decision Content", "The judgment of the Court was delivered by", "Fish J. —", "I. Introduction"]
	lines += ["1 The appeal concerns a question of law about the meaning of the section.", "II. Facts", "2 The facts are not in dispute and can be shortly stated here.", "III. Analysis", "3 The analysis begins with the text of the provision itself."]
	assert [h.title for h in read_headings("\n".join(lines))] == ["Introduction", "Facts", "Analysis"]


def test_court_of_appeal_cover_block_names_author_and_concurring_judges():
	text = "x\nDecision Content\nREASONS FOR JUDGMENT BY:\nGLEASON J.A.\nCONCURRED IN BY:\nMACTAVISH J.A. MONAGHAN J.A.\nDate: 1"
	cover = cover_author(text)
	assert cover["author"] == "GLEASON J.A."
	title = opinion_title(op.Opinion("lead", "reasons", cover["author"], cover["concurring"], 0, None, "cover"), 1)
	assert title == "Reasons for judgment, Gleason J.A. (Mactavish J.A. and Monaghan J.A. concurring)"
	assert cover_author("x\nDecision Content\nREASONS FOR JUDGMENT OF THE COURT BY:\nRYER J.A.\n")["court"] == "the Court"
