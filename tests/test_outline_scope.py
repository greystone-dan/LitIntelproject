from backend.contextual_authority import outline_v2 as o


def _unit(text, heading=False):
	return {"text": text, "heading": heading, "body": not heading}


def test_scope_flag_default_off(monkeypatch):
	monkeypatch.delenv("ILIT_OUTLINE_SCOPE", raising=False)
	assert not o.outline_scope_enabled()
	monkeypatch.setenv("ILIT_OUTLINE_SCOPE", "1")
	assert o.outline_scope_enabled()


def test_statute_before_the_question_is_background():
	units = [_unit("THE STATUTORY SCHEME", True), _unit("Sections 73 to 85 set a grid."), _unit("THE QUESTION TO BE DECIDED", True), _unit("The question is whether the officer erred.")]
	section = [None, "issues", "issues", "issues"]
	o._demote_early_issues(units, section, [(0, "issues"), (2, "issues")], [1, 3])
	assert section == [None, "background", "issues", "issues"]


def test_review_standard_just_before_analysis_opens_issues():
	units = [_unit(f"Paragraph {n}.") for n in range(6)]
	units[2] = _unit("The standard of review is reasonableness.")
	section = ["background", "background", "background", "background", "analysis", "analysis"]
	o._open_issues_at_review_standard(units, section, list(range(6)))
	assert section == ["background", "background", "issues", "issues", "analysis", "analysis"]


def test_review_standard_far_from_analysis_is_left_alone():
	units = [_unit(f"Paragraph {n}.") for n in range(10)]
	units[1] = _unit("The standard of review is reasonableness.")
	section = ["background"] * 8 + ["analysis", "analysis"]
	before = list(section)
	o._open_issues_at_review_standard(units, section, list(range(10)))
	assert section == before
