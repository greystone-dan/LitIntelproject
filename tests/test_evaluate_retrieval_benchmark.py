from scripts.evaluate_retrieval_benchmark import ranking_metrics


def test_ranking_metrics_measure_first_relevant_result():
    metrics = ranking_metrics([9, 4, 2], [2, 4], 3)

    assert metrics["hit_at_k"] == 1
    assert metrics["reciprocal_rank"] == 0.5
    assert metrics["precision_at_k"] == 2 / 3
    assert metrics["recall_at_k"] == 1.0


def test_ranking_metrics_report_miss():
    metrics = ranking_metrics([9, 4], [2], 2)

    assert metrics["hit_at_k"] == 0
    assert metrics["reciprocal_rank"] == 0.0
    assert metrics["precision_at_k"] == 0.0
    assert metrics["recall_at_k"] == 0.0
