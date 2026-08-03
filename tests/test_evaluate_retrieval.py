from scripts.evaluate_retrieval import EvalResult, _check_gates, _summarize


def test_summarize_computes_topic_metrics():
    results = [
        EvalResult(
            topic="a",
            query="q1",
            expected_citations=["x"],
            hit=True,
            reciprocal_rank=1.0,
            matched_citation="x",
            top_citations=["x"],
        ),
        EvalResult(
            topic="a",
            query="q2",
            expected_citations=["x"],
            hit=False,
            reciprocal_rank=0.0,
            matched_citation=None,
            top_citations=["y"],
        ),
        EvalResult(
            topic="b",
            query="q3",
            expected_citations=["z"],
            hit=True,
            reciprocal_rank=0.5,
            matched_citation="z",
            top_citations=["w", "z"],
        ),
    ]

    summary = _summarize(results)

    assert summary.fixtures == 3
    assert summary.hits == 2
    assert summary.hit_rate == 2 / 3
    assert summary.mrr == (1.0 + 0.0 + 0.5) / 3
    assert summary.by_topic["a"]["fixtures"] == 2
    assert summary.by_topic["a"]["hits"] == 1
    assert summary.by_topic["a"]["hit_rate"] == 0.5


def test_check_gates_fails_for_low_topic_rate():
    summary = _summarize(
        [
            EvalResult(
                topic="a",
                query="q1",
                expected_citations=["x"],
                hit=False,
                reciprocal_rank=0.0,
                matched_citation=None,
                top_citations=["y"],
            ),
            EvalResult(
                topic="a",
                query="q2",
                expected_citations=["x"],
                hit=False,
                reciprocal_rank=0.0,
                matched_citation=None,
                top_citations=["y"],
            ),
            EvalResult(
                topic="b",
                query="q3",
                expected_citations=["z"],
                hit=True,
                reciprocal_rank=1.0,
                matched_citation="z",
                top_citations=["z"],
            ),
        ]
    )

    passed, failures = _check_gates(
        summary,
        min_hit_rate=0.2,
        min_mrr=0.1,
        min_topic_hit_rate=0.5,
        min_topic_fixtures=2,
    )

    assert passed is False
    assert any("topic 'a'" in f for f in failures)
