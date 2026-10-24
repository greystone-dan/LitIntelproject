"""Known judge-name pairs and synthetic service windows, without a database."""

from datetime import date
from unittest.mock import Mock

import pytest
from sqlalchemy.orm import Session

from backend.judge_aliases import alias_map, member_ids
from backend.judge_normalization import group_judge_names, parse_judge_name, same_person


@pytest.mark.parametrize(
    ("left", "right", "court"),
    [
        ("James W. O’Reilly", "James W. O'Reilly J.", "FC"),
        ("Simon Noël", "Simon Noel", "FC"),
        ("René LeBlanc", "Rene LeBlanc J.", "FC"),
        ("David Gleason", "D. Gleason J.A.", "FCA"),
        ("Anne L. Mactavish", "A. L. Mactavish J.A.", "FCA"),
        ("Suzanne Côté", "Côté, Suzanne", "SCC"),
    ],
)
def test_same_judge_variants_merge(left, right, court):
    first, second = parse_judge_name(left), parse_judge_name(right)
    assert first is not None and second is not None
    assert same_person(first, second)
    assert same_person(second, first)

    groups = group_judge_names(
        {left: 5, right: 2}, courts={left: {court}, right: {court}}
    )
    assert len(groups) == 1
    assert set(groups[0].members) == {left, right}
    assert groups[0].needs_review == []


@pytest.mark.parametrize(
    ("left", "right", "left_court", "right_court"),
    [
        ("Simon Noël", "Marc Noël", "FC", "FCA"),
        ("Henry S. Brown", "Russell Brown", "FC", "SCC"),
    ],
)
def test_different_given_names_do_not_merge(left, right, left_court, right_court):
    first, second = parse_judge_name(left), parse_judge_name(right)
    assert first is not None and second is not None
    assert not same_person(first, second)
    assert not same_person(second, first)
    assert group_judge_names(
        {left: 5, right: 2},
        courts={left: {left_court}, right: {right_court}},
    ) == []


@pytest.mark.parametrize(
    ("spans", "expected_members"),
    [
        (
            {
                "Eleanor Dawson": (date(2000, 1, 1).toordinal(), date(2009, 12, 31).toordinal()),
                "DAWSON J.A.": (date(2010, 1, 1).toordinal(), date(2020, 12, 31).toordinal()),
            },
            {"Eleanor Dawson", "DAWSON J.A."},
        ),
        (
            {
                "Eleanor Dawson": (date(2000, 1, 1).toordinal(), date(2020, 12, 31).toordinal()),
                "DAWSON J.A.": (date(2005, 1, 1).toordinal(), date(2015, 12, 31).toordinal()),
            },
            set(),
        ),
        (None, set()),
    ],
    ids=["forward-elevation", "overlapping-careers", "unknown-careers"],
)
def test_fc_to_fca_matching_requires_compatible_service(spans, expected_members):
    groups = group_judge_names(
        {"Eleanor Dawson": 5, "DAWSON J.A.": 2},
        spans=spans,
        courts={"Eleanor Dawson": {"FC"}, "DAWSON J.A.": {"FCA"}},
    )
    assert {name for group in groups for name in group.members} == expected_members


@pytest.mark.xfail(
    strict=True,
    reason="known bug: judge merge accepts an FCA range ending before FC service starts",
)
def test_earlier_fca_career_does_not_merge_into_later_fc_judge():
    groups = group_judge_names(
        {"Simon Noël": 5, "NOËL J.A.": 2},
        spans={
            "Simon Noël": (date(2002, 1, 1).toordinal(), date(2024, 12, 31).toordinal()),
            "NOËL J.A.": (date(1980, 1, 1).toordinal(), date(1990, 12, 31).toordinal()),
        },
        courts={"Simon Noël": {"FC"}, "NOËL J.A.": {"FCA"}},
    )
    assert groups == []


def test_alias_map_preserves_explicit_profile_targets():
    session = Mock(spec=Session)
    session.execute.return_value = [(31, 10), (22, 10), (99, 80)]

    assert alias_map(session) == {31: 10, 22: 10, 99: 80}
    session.execute.assert_called_once()


@pytest.mark.parametrize(
    ("profile_id", "expected"),
    [(10, [10, 22, 31]), (31, [10, 22, 31]), (99, [80, 99]), (7, [7])],
    ids=["canonical", "alias", "separate-judge", "unaliased-judge"],
)
def test_alias_members_stay_with_their_known_judge(profile_id, expected):
    session = Mock(spec=Session)
    session.execute.return_value = [(31, 10), (22, 10), (99, 80)]

    assert member_ids(session, profile_id) == expected


def test_no_aliases_leaves_profile_unchanged():
    session = Mock(spec=Session)
    session.execute.return_value = []

    assert alias_map(session) == {}
    assert member_ids(session, 10) == [10]
