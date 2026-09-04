import json

from scripts.evaluate_statute_extraction import DEFAULT_FIXTURES, evaluate_fixtures


def test_statute_fixture_baseline_is_exact():
    fixtures = json.loads(DEFAULT_FIXTURES.read_text(encoding="utf-8"))

    report = evaluate_fixtures(fixtures)

    assert report["passed"] is True
    assert report["precision_pct"] == 100.0
    assert report["recall_pct"] == 100.0
    assert report["exact_span_accuracy_pct"] == 100.0
    assert report["false_positives"] == 0
    assert report["false_negatives"] == 0
