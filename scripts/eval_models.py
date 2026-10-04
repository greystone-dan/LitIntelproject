"""Evaluate local embedding and JSON-generation models on frozen datasets."""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

JSON_PROMPT_VERSION = "json-task-v1"
RETRIEVAL_PROMPT_VERSION = "embedding-retrieval-v1"
DEFAULT_LOCAL_CHAT_URL = "http://127.0.0.1:11434/v1"


def load_dataset(path: Path, mode: str) -> dict[str, Any]:
    dataset = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(dataset, dict) or not isinstance(dataset.get("items"), list):
        raise TypeError("Dataset must be a JSON object with an items array")
    if not dataset["items"]:
        raise ValueError("Dataset items must not be empty")
    if not isinstance(dataset.get("name"), str) or not isinstance(
        dataset.get("version"), str
    ):
        raise TypeError("Dataset must include string name and version fields")

    seen_ids: set[str] = set()
    for item in dataset["items"]:
        if (
            not isinstance(item, dict)
            or not isinstance(item.get("id"), str)
            or not item["id"]
        ):
            raise ValueError("Every dataset item must have a non-empty string id")
        if item["id"] in seen_ids:
            raise ValueError(f"Duplicate dataset item id: {item['id']}")
        seen_ids.add(item["id"])

        if mode == "retrieval":
            query = item.get("query")
            chunks = item.get("chunks")
            relevant_ids = item.get("relevant_chunk_ids")
            if not isinstance(query, str) or not query.strip():
                raise ValueError(f"Retrieval item {item['id']} requires a query")
            if not isinstance(chunks, list) or not chunks:
                raise ValueError(
                    f"Retrieval item {item['id']} requires candidate chunks"
                )
            if not isinstance(relevant_ids, list) or not relevant_ids:
                raise ValueError(
                    f"Retrieval item {item['id']} requires relevant_chunk_ids"
                )
            chunk_ids: set[str] = set()
            for chunk in chunks:
                if (
                    not isinstance(chunk, dict)
                    or not isinstance(chunk.get("id"), str)
                    or not isinstance(chunk.get("text"), str)
                ):
                    raise TypeError(f"Retrieval item {item['id']} has an invalid chunk")
                if chunk["id"] in chunk_ids:
                    raise ValueError(
                        f"Duplicate chunk id in item {item['id']}: {chunk['id']}"
                    )
                chunk_ids.add(chunk["id"])
            if any(
                not isinstance(value, str) or value not in chunk_ids
                for value in relevant_ids
            ):
                raise ValueError(
                    f"Retrieval item {item['id']} has unknown relevant chunk ids"
                )
        elif mode == "json_task":
            if not isinstance(item.get("input"), str):
                raise ValueError(f"JSON-task item {item['id']} requires string input")
            if (
                not isinstance(item.get("reference_labels"), dict)
                or not item["reference_labels"]
            ):
                raise ValueError(
                    f"JSON-task item {item['id']} requires reference_labels"
                )
            if not isinstance(item.get("source_text"), str):
                raise ValueError(f"JSON-task item {item['id']} requires source_text")
            spans = item.get("reference_spans", [])
            if not isinstance(spans, list):
                raise ValueError(
                    f"JSON-task item {item['id']} reference_spans must be an array"
                )
            for span in spans:
                if not _span_matches_source(span, item["source_text"]):
                    raise ValueError(
                        f"JSON-task item {item['id']} has an invalid reference span"
                    )
        else:
            raise ValueError(f"Unsupported evaluation mode: {mode}")
    return dataset


def _span_matches_source(span: Any, source_text: str) -> bool:
    return (
        isinstance(span, dict)
        and isinstance(span.get("field"), str)
        and isinstance(span.get("start"), int)
        and not isinstance(span.get("start"), bool)
        and isinstance(span.get("end"), int)
        and not isinstance(span.get("end"), bool)
        and isinstance(span.get("text"), str)
        and 0 <= span["start"] < span["end"] <= len(source_text)
        and source_text[span["start"] : span["end"]] == span["text"]
    )


def _cosine(left: list[float], right: list[float]) -> float:
    if not left or len(left) != len(right):
        raise ValueError("Embedding vectors must have the same non-zero dimension")
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return sum(a * b for a, b in zip(left, right)) / (left_norm * right_norm)


def retrieval_item_metrics(
    ranked_ids: list[str], relevant_ids: list[str], k: int
) -> dict[str, float]:
    relevant = set(relevant_ids)
    ranks = [
        position for position, value in enumerate(ranked_ids, 1) if value in relevant
    ]
    hits_at_k = sum(value in relevant for value in ranked_ids[:k])
    dcg = sum(
        1 / math.log2(position + 1)
        for position, value in enumerate(ranked_ids[:10], 1)
        if value in relevant
    )
    ideal_count = min(len(relevant), 10)
    ideal_dcg = sum(
        1 / math.log2(position + 1) for position in range(1, ideal_count + 1)
    )
    return {
        "recall_at_k": hits_at_k / len(relevant) if relevant else 1.0,
        "mrr": 1 / ranks[0] if ranks else 0.0,
        "ndcg_at_10": dcg / ideal_dcg if ideal_dcg else 0.0,
    }


def evaluate_retrieval(
    dataset: dict[str, Any],
    provider: Any,
    model_name: str,
    *,
    k: int = 10,
    provider_name: str = "local",
) -> dict[str, Any]:
    if k <= 0:
        raise ValueError("k must be greater than zero")
    rows = []
    started = time.perf_counter()
    for item in dataset["items"]:
        item_started = time.perf_counter()
        chunks = item["chunks"]
        document_vectors = provider.embed_documents([chunk["text"] for chunk in chunks])
        query_vector = provider.embed_query(item["query"])
        if len(document_vectors) != len(chunks):
            raise ValueError(
                "Embedding provider returned a different number of document vectors"
            )
        ranked = sorted(
            zip(chunks, document_vectors),
            key=lambda pair: _cosine(query_vector, pair[1]),
            reverse=True,
        )
        ranked_ids = [chunk["id"] for chunk, _ in ranked]
        item_metrics = retrieval_item_metrics(ranked_ids, item["relevant_chunk_ids"], k)
        rows.append(
            {
                "id": item["id"],
                "output": {"ranked_chunk_ids": ranked_ids},
                "relevant_chunk_ids": item["relevant_chunk_ids"],
                "metrics": item_metrics,
                "timing_ms": (time.perf_counter() - item_started) * 1000,
                "token_counts": {"input": None, "output": None},
            }
        )
    metric_names = ("recall_at_k", "mrr", "ndcg_at_10")
    return {
        "schema_version": "1.0",
        "mode": "retrieval",
        "dataset": _dataset_metadata(dataset, len(rows)),
        "model": {
            "provider": provider_name,
            "name": model_name,
            "prompt_version": RETRIEVAL_PROMPT_VERSION,
        },
        "parameters": {"k": k},
        "created_at": datetime.now(timezone.utc).isoformat(),
        "timing_ms": (time.perf_counter() - started) * 1000,
        "metrics": {
            name: mean(row["metrics"][name] for row in rows) for name in metric_names
        },
        "items": rows,
    }


def _canonical_label(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def cohen_kappa(rows: list[dict[str, Any]]) -> float:
    reference_values: list[str] = []
    predicted_values: list[str] = []
    missing = '"__missing__"'
    for row in rows:
        reference = row["reference_labels"]
        predicted = row["predicted_labels"]
        for field, value in reference.items():
            reference_values.append(_canonical_label(value))
            predicted_values.append(_canonical_label(predicted.get(field, missing)))
    if not reference_values:
        return 0.0
    observed = sum(a == b for a, b in zip(reference_values, predicted_values)) / len(
        reference_values
    )
    categories = set(reference_values) | set(predicted_values)
    expected = sum(
        reference_values.count(category) * predicted_values.count(category)
        for category in categories
    ) / (len(reference_values) ** 2)
    if expected == 1:
        return 1.0 if observed == 1 else 0.0
    return (observed - expected) / (1 - expected)


def _valid_output(raw: str) -> tuple[bool, dict[str, Any], dict[str, Any], list[Any]]:
    try:
        parsed = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return False, {}, {}, []
    if not isinstance(parsed, dict) or not isinstance(parsed.get("labels"), dict):
        return False, parsed if isinstance(parsed, dict) else {}, {}, []
    spans = parsed.get("spans")
    if not isinstance(spans, list):
        return False, parsed, parsed["labels"], []
    if any(
        not isinstance(span, dict)
        or not isinstance(span.get("field"), str)
        or not isinstance(span.get("start"), int)
        or isinstance(span.get("start"), bool)
        or not isinstance(span.get("end"), int)
        or isinstance(span.get("end"), bool)
        or not isinstance(span.get("text"), str)
        for span in spans
    ):
        return False, parsed, parsed["labels"], spans
    return True, parsed, parsed["labels"], spans


def _span_key(span: dict[str, Any]) -> tuple[str, int, int, str]:
    return span["field"], span["start"], span["end"], span["text"]


def _extract_completion(response: Any) -> tuple[str, int | None, int | None]:
    content = response.choices[0].message.content
    usage = getattr(response, "usage", None)
    return (
        content if isinstance(content, str) else "",
        getattr(usage, "prompt_tokens", None),
        getattr(usage, "completion_tokens", None),
    )


def evaluate_json_task(
    dataset: dict[str, Any],
    provider: Any,
    model_name: str,
    *,
    provider_name: str = "local",
    max_tokens: int = 512,
) -> dict[str, Any]:
    rows = []
    started = time.perf_counter()
    for item in dataset["items"]:
        item_started = time.perf_counter()
        request_item = {
            "input": item["input"],
            "label_fields": list(item["reference_labels"]),
            "source_text": item["source_text"],
        }
        response = provider.create_chat_completion(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Extract the requested labels from the supplied input. Return only a JSON "
                        "object with a labels object containing every requested label field and "
                        "a spans array. Each span must contain "
                        "field, start, end, and text. Offsets are zero-based Python character "
                        "offsets into source_text; copy the exact source substring. Do not guess."
                    ),
                },
                {
                    "role": "user",
                    "content": json.dumps(request_item, ensure_ascii=False),
                },
            ],
            response_format={"type": "json_object"},
            temperature=0.0,
            max_tokens=max_tokens,
        )
        raw, input_tokens, output_tokens = _extract_completion(response)
        valid, parsed, predicted_labels, predicted_spans = _valid_output(raw)
        reference_labels = item["reference_labels"]
        fields = list(reference_labels)
        field_agreement = sum(
            field in predicted_labels
            and _canonical_label(predicted_labels[field])
            == _canonical_label(reference_labels[field])
            for field in fields
        ) / len(fields)
        references = item.get("reference_spans", [])
        spans_are_exact = valid and all(
            _span_matches_source(span, item["source_text"]) for span in predicted_spans
        )
        exact_span_validity = spans_are_exact and {
            _span_key(span) for span in predicted_spans
        } == {_span_key(span) for span in references}
        rows.append(
            {
                "id": item["id"],
                "output": {"raw": raw, "parsed": parsed},
                "reference_labels": reference_labels,
                "predicted_labels": predicted_labels,
                "metrics": {
                    "json_valid": float(valid),
                    "field_agreement": field_agreement,
                    "exact_span_validity": float(exact_span_validity),
                },
                "timing_ms": (time.perf_counter() - item_started) * 1000,
                "token_counts": {"input": input_tokens, "output": output_tokens},
            }
        )
    metrics = {
        name: mean(row["metrics"][name] for row in rows)
        for name in ("json_valid", "field_agreement", "exact_span_validity")
    }
    metrics["cohen_kappa"] = cohen_kappa(rows)
    return {
        "schema_version": "1.0",
        "mode": "json_task",
        "dataset": _dataset_metadata(dataset, len(rows)),
        "model": {
            "provider": provider_name,
            "name": model_name,
            "prompt_version": JSON_PROMPT_VERSION,
        },
        "parameters": {"max_tokens": max_tokens},
        "created_at": datetime.now(timezone.utc).isoformat(),
        "timing_ms": (time.perf_counter() - started) * 1000,
        "metrics": metrics,
        "items": rows,
    }


def _dataset_metadata(dataset: dict[str, Any], count: int) -> dict[str, Any]:
    return {"name": dataset["name"], "version": dataset["version"], "item_count": count}


def create_embedding_provider(provider: str, model_name: str) -> Any:
    if provider != "local":
        raise ValueError("Only the local embedding provider is supported")
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    from backend.embedding_providers import SentenceTransformerEmbeddingProvider

    return SentenceTransformerEmbeddingProvider(model_name=model_name)


def create_generation_provider(provider: str, model_name: str) -> Any:
    if provider != "local":
        raise ValueError("Only the local text-generation provider is supported")
    return LocalOnlyChatProvider(model_name)


class LocalOnlyChatProvider:
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    def create_chat_completion(self, **kwargs: Any) -> Any:
        from types import SimpleNamespace

        import httpx

        messages = kwargs.get("messages")
        if isinstance(messages, list):
            messages = [dict(message) for message in messages]
        else:
            messages = []
        payload: dict[str, Any] = {
            "model": kwargs.get("model", self.model_name),
            "messages": messages,
            "stream": False,
            "think": False,
            "options": {"temperature": kwargs.get("temperature", 0.0)},
        }
        if "max_tokens" in kwargs:
            payload["options"]["num_predict"] = kwargs["max_tokens"]
        if kwargs.get("response_format") == {"type": "json_object"}:
            payload["format"] = "json"

        api_url = DEFAULT_LOCAL_CHAT_URL.removesuffix("/v1") + "/api/chat"
        with httpx.Client(trust_env=False) as client:
            response = client.post(api_url, json=payload, timeout=120.0)
        response.raise_for_status()
        data = response.json()
        message = data.get("message", {})
        return SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content=message.get("content", ""))
                )
            ],
            usage=SimpleNamespace(
                prompt_tokens=data.get("prompt_eval_count", 0),
                completion_tokens=data.get("eval_count", 0),
            ),
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="mode", required=True)
    for mode in ("retrieval", "json_task"):
        command = subparsers.add_parser(mode)
        command.add_argument("--dataset", required=True, type=Path)
        command.add_argument("--provider", default="local", choices=["local"])
        command.add_argument("--model", required=True)
        command.add_argument("--output", required=True, type=Path)
        if mode == "retrieval":
            command.add_argument("--k", type=int, default=10)
        else:
            command.add_argument("--max-tokens", type=int, default=512)
    args = parser.parse_args(argv)
    dataset = load_dataset(args.dataset, args.mode)
    if args.mode == "retrieval":
        report = evaluate_retrieval(
            dataset,
            create_embedding_provider(args.provider, args.model),
            args.model,
            k=args.k,
            provider_name=args.provider,
        )
    else:
        report = evaluate_json_task(
            dataset,
            create_generation_provider(args.provider, args.model),
            args.model,
            provider_name=args.provider,
            max_tokens=args.max_tokens,
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "mode": report["mode"],
                "metrics": report["metrics"],
                "output": str(args.output),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
