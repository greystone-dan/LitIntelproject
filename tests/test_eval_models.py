from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from scripts import compare_eval_runs, eval_models

FIXTURES = Path(__file__).parent / "fixtures" / "eval"


class FakeEmbeddings:
    def embed_documents(self, texts):
        return [self._vector(text) for text in texts]

    def embed_query(self, text):
        return self._vector(text)

    @staticmethod
    def _vector(text):
        return (
            [1.0, 0.0]
            if any(word in text for word in ("family", "employment"))
            else [0.0, 1.0]
        )


class FakeChat:
    def create_chat_completion(self, **kwargs):
        request = json.loads(kwargs["messages"][1]["content"])
        source = request["source_text"]
        label = "allowed" if "allowed" in source else "dismissed"
        start = source.index(label)
        output = {
            "labels": {"disposition": label},
            "spans": [
                {
                    "field": "disposition",
                    "start": start,
                    "end": start + len(label),
                    "text": label,
                }
            ],
        }
        return SimpleNamespace(
            choices=[
                SimpleNamespace(message=SimpleNamespace(content=json.dumps(output)))
            ],
            usage=SimpleNamespace(prompt_tokens=12, completion_tokens=8),
        )


def test_retrieval_cli_runs_fixture_with_fake_provider(monkeypatch, tmp_path):
    monkeypatch.setattr(
        eval_models, "create_embedding_provider", lambda *_: FakeEmbeddings()
    )
    output = tmp_path / "retrieval-result.json"

    assert (
        eval_models.main(
            [
                "retrieval",
                "--dataset",
                str(FIXTURES / "retrieval.json"),
                "--provider",
                "local",
                "--model",
                "fake-embedder",
                "--output",
                str(output),
            ]
        )
        == 0
    )

    result = json.loads(output.read_text())
    assert result["metrics"] == {"recall_at_k": 1.0, "mrr": 1.0, "ndcg_at_10": 1.0}
    assert result["items"][0]["output"]["ranked_chunk_ids"][0] == "family-1"
    assert result["items"][0]["token_counts"] == {"input": None, "output": None}


def test_json_task_cli_runs_fixture_with_fake_provider(monkeypatch, tmp_path):
    monkeypatch.setattr(
        eval_models, "create_generation_provider", lambda *_: FakeChat()
    )
    output = tmp_path / "json-result.json"

    assert (
        eval_models.main(
            [
                "json_task",
                "--dataset",
                str(FIXTURES / "json_task.json"),
                "--provider",
                "local",
                "--model",
                "fake-generator",
                "--output",
                str(output),
            ]
        )
        == 0
    )

    result = json.loads(output.read_text())
    assert result["metrics"] == {
        "json_valid": 1.0,
        "field_agreement": 1.0,
        "exact_span_validity": 1.0,
        "cohen_kappa": 1.0,
    }
    assert result["items"][0]["token_counts"] == {"input": 12, "output": 8}
    assert result["model"]["prompt_version"] == eval_models.JSON_PROMPT_VERSION


def test_json_task_invalid_json_and_invalid_span_are_scored():
    dataset = eval_models.load_dataset(FIXTURES / "json_task.json", "json_task")

    class InvalidChat:
        def create_chat_completion(self, **_kwargs):
            return SimpleNamespace(
                choices=[SimpleNamespace(message=SimpleNamespace(content="not JSON"))],
                usage=None,
            )

    result = eval_models.evaluate_json_task(dataset, InvalidChat(), "broken")
    assert result["metrics"]["json_valid"] == 0.0
    assert result["metrics"]["field_agreement"] == 0.0
    assert result["metrics"]["exact_span_validity"] == 0.0
    assert result["metrics"]["cohen_kappa"] == 0.0


def test_json_task_rejects_span_with_wrong_source_offsets():
    dataset = eval_models.load_dataset(FIXTURES / "json_task.json", "json_task")

    class WrongSpanChat:
        def create_chat_completion(self, **kwargs):
            request = json.loads(kwargs["messages"][1]["content"])
            source = request["source_text"]
            label = "allowed" if "allowed" in source else "dismissed"
            return SimpleNamespace(
                choices=[
                    SimpleNamespace(
                        message=SimpleNamespace(
                            content=json.dumps(
                                {
                                    "labels": {"disposition": label},
                                    "spans": [
                                        {
                                            "field": "disposition",
                                            "start": 0,
                                            "end": len(label),
                                            "text": label,
                                        }
                                    ],
                                }
                            )
                        )
                    )
                ],
                usage=None,
            )

    result = eval_models.evaluate_json_task(dataset, WrongSpanChat(), "wrong-span")
    assert result["metrics"]["json_valid"] == 1.0
    assert result["metrics"]["field_agreement"] == 1.0
    assert result["metrics"]["exact_span_validity"] == 0.0


def test_paired_bootstrap_is_seeded_and_pairs_by_item_id():
    baseline = {
        "mode": "retrieval",
        "dataset": {"name": "d", "version": "1", "item_count": 2},
        "model": {"name": "baseline"},
        "items": [
            {"id": "a", "metrics": {"mrr": 0.0}},
            {"id": "b", "metrics": {"mrr": 1.0}},
        ],
    }
    candidate = {
        **baseline,
        "model": {"name": "candidate"},
        "items": [
            {"id": "b", "metrics": {"mrr": 1.0}},
            {"id": "a", "metrics": {"mrr": 1.0}},
        ],
    }

    first = compare_eval_runs.compare_runs(
        baseline, candidate, "mrr", samples=200, seed=17
    )
    second = compare_eval_runs.compare_runs(
        baseline, candidate, "mrr", samples=200, seed=17
    )

    assert first == second
    assert first["difference"]["estimate"] == 0.5
    assert first["difference"]["confidence_interval"][0] >= 0.0


def test_comparison_cli_writes_result_file(tmp_path):
    run = {
        "mode": "retrieval",
        "dataset": {"name": "d", "version": "1", "item_count": 1},
        "parameters": {"k": 10},
        "model": {"name": "test"},
        "items": [{"id": "a", "metrics": {"mrr": 1.0}, "relevant_chunk_ids": ["x"]}],
    }
    baseline = tmp_path / "baseline.json"
    candidate = tmp_path / "candidate.json"
    output = tmp_path / "comparison.json"
    baseline.write_text(json.dumps(run))
    candidate.write_text(json.dumps(run))

    assert (
        compare_eval_runs.main(
            [
                "--baseline",
                str(baseline),
                "--candidate",
                str(candidate),
                "--metric",
                "mrr",
                "--samples",
                "20",
                "--output",
                str(output),
            ]
        )
        == 0
    )
    assert json.loads(output.read_text())["difference"]["estimate"] == 0.0


def test_paired_comparison_rejects_different_item_sets():
    run = {
        "mode": "retrieval",
        "dataset": {"name": "d", "version": "1", "item_count": 1},
        "items": [{"id": "a", "metrics": {"mrr": 1.0}}],
    }
    other = {**run, "items": [{"id": "b", "metrics": {"mrr": 1.0}}]}

    with pytest.raises(ValueError, match="same non-empty item ids"):
        compare_eval_runs.compare_runs(run, other, "mrr", samples=10)
