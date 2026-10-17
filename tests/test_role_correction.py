from backend.contextual_authority import case_structure as cs
from backend.contextual_authority import role_correction as rc

TEXTS = [f"[{i}] The applicant argues that the officer erred in paragraph {i}, see Smith v. Canada, 2015 FC 100." for i in range(1, 9)]


def test_passes_through_without_flag_or_forum(monkeypatch):
    roles = ["facts"] * len(TEXTS)
    monkeypatch.delenv("ILIT_ROLE_CORRECTION", raising=False)
    with rc.use_forum("scc"):
        assert rc.correct(TEXTS, list(roles)) == roles
    monkeypatch.setenv("ILIT_ROLE_CORRECTION", "1")
    assert rc.correct(TEXTS, list(roles)) == roles  # no court named


def test_corrected_roles_are_valid_and_same_length(monkeypatch):
    monkeypatch.setenv("ILIT_ROLE_CORRECTION", "1")
    roles = ["facts"] * 4 + ["analysis"] * 4
    for forum in rc.FORUMS:
        with rc.use_forum(forum):
            out = rc.correct(TEXTS, list(roles))
        assert len(out) == len(roles) and set(out) <= set(cs.ROLES)


def test_headings_and_unnumbered_lines_are_left_alone(monkeypatch):
    monkeypatch.setenv("ILIT_ROLE_CORRECTION", "1")
    texts = ["ANALYSIS"] + TEXTS
    roles = ["analysis"] + ["facts"] * len(TEXTS)
    with rc.use_forum("fca"):
        assert rc.correct(texts, roles)[0] == "analysis"
