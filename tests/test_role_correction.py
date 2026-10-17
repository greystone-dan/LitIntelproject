import numpy as np

from backend.contextual_authority import case_structure as cs
from backend.contextual_authority import role_correction as rc

UNITS = [{"text": f"[{i}] The applicant argues that the officer erred, see Smith v. Canada, 2015 FC 100.", "num": i, "heading": False} for i in range(1, 9)]


def _log_p(roles):
    out = np.full((len(roles), len(cs.ROLES)), -4.0)
    for i, role in enumerate(roles):
        out[i, cs.ROLES.index(role)] = -0.1
    return out


def test_passes_through_without_flag_or_forum(monkeypatch):
    roles = ["facts"] * len(UNITS)
    monkeypatch.delenv("ILIT_ROLE_CORRECTION", raising=False)
    with rc.use_forum("scc"):
        assert rc.correct_units(UNITS, list(roles), _log_p(roles)) == (roles, None)
    monkeypatch.setenv("ILIT_ROLE_CORRECTION", "1")
    assert rc.correct_units(UNITS, list(roles), _log_p(roles)) == (roles, None)  # no court named


def test_corrected_roles_are_valid_and_scores_shaped(monkeypatch):
    monkeypatch.setenv("ILIT_ROLE_CORRECTION", "1")
    roles = ["facts"] * 4 + ["analysis"] * 4
    for forum in rc.FORUMS:
        with rc.use_forum(forum, ""):
            out, scores = rc.correct_units(UNITS, list(roles), _log_p(roles))
        assert len(out) == len(roles) and set(out) <= set(cs.ROLES)
        assert scores is None or scores.shape == (len(UNITS), 4)


def test_unnumbered_lines_are_left_alone(monkeypatch):
    monkeypatch.setenv("ILIT_ROLE_CORRECTION", "1")
    units = [{"text": "ANALYSIS", "num": None, "heading": True}] + UNITS
    roles = ["analysis"] + ["facts"] * len(UNITS)
    with rc.use_forum("fca", ""):
        out, _ = rc.correct_units(units, roles, _log_p(roles))
    assert out[0] == "analysis"


def test_monotone_sections_never_go_backwards():
    scores = np.log(np.array([[0.9, 0.05, 0.03, 0.02], [0.2, 0.1, 0.6, 0.1], [0.1, 0.6, 0.2, 0.1], [0.1, 0.1, 0.7, 0.1], [0.05, 0.05, 0.1, 0.8]]))
    path = rc.monotone_sections(scores)
    assert path == sorted(path) and path[0] == 0 and path[-1] == 3
