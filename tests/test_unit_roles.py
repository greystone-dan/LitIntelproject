from backend.contextual_authority.unit_roles import ROLE_CLASSES, label_unit_roles


def test_typical_judgment_gets_roles_in_order():
    units = [
        ["Smith v. Canada (Citizenship and Immigration) Court (s) Database Federal Court Decisions"],
        ["[1] This is an application for judicial review of a decision of the Refugee Appeal Division."],
        ["[2] The applicant is a citizen of Nigeria.", "[3] In March 2018 she arrived in Canada."],
        ["[4] The sole issue is whether the RAD decision was reasonable."],
        ["[5] I find that the RAD ignored the evidence.", "[6] In my view this was a reviewable error."] * 4,
        ["[14] For these reasons, the application is allowed."],
        ["SOLICITORS OF RECORD\nDOCKET: IMM-1-20\nSTYLE OF CAUSE: SMITH v MCI"],
    ]
    assert label_unit_roles(units) == [
        "metadata", "overview", "facts", "issues", "analysis", "disposition", "metadata",
    ]


def test_order_block_is_disposition_not_footer():
    units = [["[1] This is an application for judicial review."], ["[2] I find the decision reasonable."] * 6,
             ["JUDGMENT\nTHIS COURT'S JUDGMENT is that the application is dismissed.\nSTYLE OF CAUSE: X v Y"]]
    assert label_unit_roles(units)[-1] == "disposition"


def test_facts_not_assigned_after_analysis_starts():
    units = [["[1] This is an application for judicial review."], ["[2] I find the officer erred."] * 3,
             ["[9] The officer found that the applicant was a citizen of Iran."], ["[10] More reasoning."] * 3]
    assert label_unit_roles(units)[2] == "analysis"


def test_every_label_is_a_known_class_and_empty_input_is_empty():
    assert label_unit_roles([]) == []
    assert set(label_unit_roles([["[1] text"], ["[2] more"]])) <= set(ROLE_CLASSES)


def test_structure_roles_follow_the_skeleton_and_use_the_plurality_of_a_units_paragraphs():
    from backend.contextual_authority.unit_roles import label_unit_roles_by_structure

    units = [
        ["Smith v. Canada (Citizenship and Immigration) Court (s) Database Federal Court Decisions"],
        ["[1] This is an application for judicial review of a decision of the Refugee Appeal Division."],
        ["[2] The applicant is a citizen of Nigeria.", "[3] In March 2018 she arrived in Canada."],
        ["[4] The sole issue is whether the RAD decision was reasonable. The standard of review is reasonableness."],
        ["[5] I find that the RAD ignored the evidence.", "[6] In my view this was a reviewable error."] * 4,
        ["[14] For these reasons, the application is allowed. THIS COURT'S JUDGMENT is that the application is allowed."],
    ]
    roles = label_unit_roles_by_structure(units)
    assert len(roles) == len(units) and set(roles) <= set(ROLE_CLASSES)
    assert roles[1] == "overview" and roles[-2] == "analysis" and roles[-1] == "disposition"
    assert label_unit_roles_by_structure([]) == []
