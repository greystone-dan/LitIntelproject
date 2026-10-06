import json
from pathlib import Path

from scripts.evaluate_statute_sections import DEFAULT_GOLD, evaluate


def _cases():
    return json.loads(Path(DEFAULT_GOLD).read_text(encoding="utf-8"))


def test_gold_set_is_well_formed_and_big_enough():
    cases = _cases()
    ids = [c["id"] for c in cases]
    assert len(ids) == len(set(ids))
    assert sum(len(c["expected"]) for c in cases) >= 150
    holdout = [c for c in cases if c["holdout"]]
    assert 0.2 <= len(holdout) / len(cases) <= 0.3
    assert any(not c["expected"] for c in cases), "needs negative cases"


def test_evaluator_scores_a_small_split():
    cases = [c for c in _cases() if c["id"] in {"sg001", "sg152", "sg170"} or not c["expected"]][:6]
    result = evaluate(cases, "all")
    assert result["cases"] == len(cases)
    assert 0 <= result["recall_pct"] <= 100 and 0 <= result["precision_pct"] <= 100
