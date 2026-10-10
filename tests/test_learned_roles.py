from backend.contextual_authority import case_structure as cs
from backend.contextual_authority import learned_roles as lr

PARAS = (
    ["Smith v. Canada (Citizenship and Immigration) Federal Court Date: 2020-01-01 Docket: IMM-1-20", "REASONS FOR JUDGMENT"]
    + ["[1] This is an application for judicial review of a decision of an officer dated May 3, 2019."]
    + [f"[{n}] The applicant was born in 1980 and arrived in Canada in 2015. He claimed protection in {2015 + n % 3}." for n in range(2, 8)]
    + ["[8] The issues are whether the officer's decision was reasonable. The standard of review is reasonableness."]
    + [f"[{n}] In my view the officer erred. I find that the finding was unreasonable; however, the applicant submits otherwise." for n in range(9, 20)]
    + ["[20] For these reasons the application is allowed. No question is certified.", "JUDGMENT", "THIS COURT'S JUDGMENT is that the application is allowed.", "Judge"]
)


def test_weights_are_present():
    assert lr.available()


def test_learned_labels_cover_every_paragraph_and_are_deterministic():
    first = lr.label_paragraph_roles(PARAS)
    assert first == lr.label_paragraph_roles(PARAS)
    assert len(first) == len(PARAS) and set(first) <= set(cs.ROLES)
    assert first[0] == "metadata" and "analysis" in first and first[-1] in {"metadata", "disposition"}


def test_flag_selects_learned_labeller(monkeypatch):
    monkeypatch.delenv("ILIT_LEARNED_ROLES", raising=False)
    assert cs.label_paragraph_roles(PARAS) == cs.label_paragraph_roles_rules(PARAS)
    monkeypatch.setenv("ILIT_LEARNED_ROLES", "1")
    assert cs.label_paragraph_roles(PARAS) == lr.label_paragraph_roles(PARAS)


def test_empty_input():
    assert lr.label_paragraph_roles([]) == [] and cs.label_paragraph_roles([]) == []


def test_second_stage_weights_loaded_and_probabilities_normalised():
    import numpy as np

    paragraphs = ["1. The applicant is a citizen of Iran.", "2. The issue is whether the decision was reasonable.", "3. The application is dismissed."]
    emissions = cs._emissions(paragraphs)
    log_p = lr.stage_two(lr.log_probabilities(paragraphs, emissions), emissions, paragraphs)
    assert log_p.shape == (3, len(cs.ROLES))
    assert np.allclose(np.exp(log_p).sum(axis=1), 1.0, atol=0.01)
