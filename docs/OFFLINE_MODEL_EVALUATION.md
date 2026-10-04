# Offline Model Evaluation

`scripts/eval_models.py` compares local embedding and text-generation models on
small, versioned JSON datasets. The harness is a command-line tool: it is not
called by the web application, does not read the live database, and does not
send evaluation examples to a hosted provider. Keep datasets frozen and free of
user data.

The retrieval evaluator embeds each query and its candidate chunks, ranks by
cosine similarity, and reports per-query and macro-average Recall@k, MRR, and
nDCG@10. The JSON-task evaluator asks a local chat model for structured output
and reports JSON validity, field agreement, Cohen's kappa, and exact-span
validity. Exact-span validity is one only when the predicted span set exactly
matches the labeled spans and every offset selects the stated substring of
`source_text`. Offsets are zero-based Python character offsets with an
exclusive end.

## Run

Embedding models must already be available locally; model loading is forced
into Hugging Face offline mode and will fail rather than download weights. JSON
generation uses the local Ollama-compatible service at
`http://127.0.0.1:11434/v1`; the client ignores proxy environment variables so
the prompt stays on loopback. Only the provider `local` is currently supported.

```sh
python scripts/eval_models.py retrieval \
  --dataset tests/fixtures/eval/retrieval.json \
  --provider local --model /path/to/cached-embedding-model \
  --output /tmp/retrieval-run.json --k 10

python scripts/eval_models.py json_task \
  --dataset tests/fixtures/eval/json_task.json \
  --provider local --model qwen3:4b \
  --output /tmp/json-run.json

python scripts/compare_eval_runs.py \
  --baseline /tmp/retrieval-run-a.json \
  --candidate /tmp/retrieval-run-b.json \
  --metric ndcg_at_10 --samples 10000 --seed 42
```

The `--model` value is recorded as supplied. The comparison command requires
matching evaluation mode, dataset name/version, run parameters, item IDs, and
reference labels. Its interval is the percentile confidence interval of the
paired mean difference (candidate minus baseline); items are resampled
together with replacement. The default random seed is `42`.

## Dataset format

Both modes use a UTF-8 JSON object with `name`, `version`, and non-empty `items`.
Item IDs must be unique.

Retrieval items have a query, candidate chunks, and one or more relevant chunk
IDs:

```json
{
  "name": "retrieval-sample",
  "version": "1",
  "items": [
    {
      "id": "query-1",
      "query": "family status",
      "chunks": [{"id": "chunk-1", "text": "Relevant passage"}],
      "relevant_chunk_ids": ["chunk-1"]
    }
  ]
}
```

JSON-task items provide an instruction, source text, reference labels, and
optional exact-span annotations. The model receives the instruction, label
field names, and source text, but not the reference labels or spans. Expected
model output is an object with `labels` and `spans`; each span has `field`,
`start`, `end`, and `text`.

```json
{
  "name": "json-sample",
  "version": "1",
  "items": [
    {
      "id": "decision-1",
      "input": "Classify the decision.",
      "source_text": "The Court allowed the appeal.",
      "reference_labels": {"disposition": "allowed"},
      "reference_spans": [
        {"field": "disposition", "start": 10, "end": 17, "text": "allowed"}
      ]
    }
  ]
}
```

## Result format

Each evaluation JSON result contains:

| Field | Contents |
| --- | --- |
| `schema_version` | Result format version (`1.0`) |
| `mode`, `dataset`, `model`, `parameters` | Evaluation mode, frozen dataset identity, provider/model and prompt version, run settings |
| `created_at`, `timing_ms` | UTC creation time and elapsed wall-clock milliseconds |
| `metrics` | Macro-average metrics; Cohen's kappa is computed over all labeled fields |
| `items` | Item ID, model output, per-item metrics, elapsed time, and token counts |

JSON-generation token counts come from the provider response. The current local
embedding interface exposes no token usage, so retrieval token counts are
`null`. Per-item JSON results retain reference and predicted labels so the
comparison tool can recompute kappa for each paired bootstrap sample. Treat
result files as evaluation artifacts because they include model outputs and
reference labels.

The bundled fixtures and fake-provider tests run without model weights,
database access, or network calls.
