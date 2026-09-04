"""Unit tests for automated data quality evaluation script."""

from types import SimpleNamespace
from unittest.mock import MagicMock

from scripts.evaluate_data_quality import evaluate_corpus_quality


class FakeDB:
    def __init__(self, scalar_return=10):
        self.scalar_return = scalar_return

    def scalar(self, statement):
        return self.scalar_return


def test_evaluate_corpus_quality_returns_structured_metrics():
    db = FakeDB(scalar_return=42)
    report = evaluate_corpus_quality(db)

    assert "inventory" in report
    assert "citation_health" in report
    assert "statute_health" in report
    assert "metadata_completeness" in report
    assert "graph_health" in report
    assert report["inventory"]["total_cases"] == 42
    assert report["citation_health"]["total_citations"] == 42
    assert report["statute_health"]["total_statute_references"] == 42
