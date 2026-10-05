import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "evaluate_discussion_unit_boundaries",
    Path(__file__).resolve().parent.parent / "scripts" / "evaluate_discussion_unit_boundaries.py",
)
evaluator = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = evaluator
_SPEC.loader.exec_module(evaluator)
score_boundaries = evaluator.score_boundaries


def test_identical_lists_are_all_hits():
    s = score_boundaries([0, 3, 7], [0, 3, 7])
    assert (s.gold, s.predicted, s.hits, s.missed, s.spurious, s.within_1) == (3, 3, 3, 0, 0, 3)
    assert s.exact_cases == 1


def test_partial_overlap_counts_each_boundary_not_whole_list():
    # Whole-list comparison would say 0; per-boundary is 2 of 4.
    s = score_boundaries([0, 2, 5, 9], [0, 5, 6, 12])
    assert (s.hits, s.missed, s.spurious) == (2, 2, 2)
    assert s.exact_cases == 0


def test_within_one_is_one_to_one():
    # Predicted 3 is adjacent to gold 2 and gold 4 but may satisfy only one.
    s = score_boundaries([0, 2, 4], [0, 3])
    assert s.hits == 1
    assert s.within_1 == 2


def test_exact_match_is_not_reused_for_a_neighbour():
    # Predicted 5 hits gold 5 exactly, so it cannot also count for gold 6.
    s = score_boundaries([0, 5, 6], [0, 5])
    assert (s.hits, s.within_1) == (2, 2)


def test_distance_two_is_not_within_one():
    s = score_boundaries([0, 10], [0, 12])
    assert (s.hits, s.within_1) == (1, 1)


def test_interior_counts_drop_paragraph_zero():
    s = score_boundaries([0, 4], [0, 8])
    assert (s.hits, s.interior_gold, s.interior_predicted, s.interior_hits) == (1, 1, 1, 0)


def test_duplicates_are_ignored_and_totals_add_up():
    total = evaluator.BoundaryScore()
    total.add(score_boundaries([0, 3, 3], [0, 3]))
    total.add(score_boundaries([0, 2], [0, 1, 9]))
    assert (total.cases, total.gold, total.predicted, total.hits) == (2, 4, 5, 3)
    assert (total.missed, total.spurious, total.within_1) == (1, 2, 4)
    assert evaluator.pct(total.hits, total.gold) == "75.0%"
