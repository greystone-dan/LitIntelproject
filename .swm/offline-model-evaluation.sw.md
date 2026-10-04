---
title: Offline Model Evaluation
---
# Offline Model Evaluation

The offline evaluation scripts compare models against versioned fixture datasets
without coupling evaluation to web requests or canonical records. See
[`docs/OFFLINE_MODEL_EVALUATION.md`](../docs/OFFLINE_MODEL_EVALUATION.md) for
commands, fixture schemas, result fields, and metric definitions.

## Execution flow

1. Freeze and version a labeled dataset.
2. `scripts/eval_models.py` loads the dataset and runs either cosine-ranked
   retrieval over its candidate chunks or local JSON generation.
3. The run file records per-item results and evaluation metrics. Model output
   timing is measured locally; token counts are provider-reported when exposed.
4. `scripts/compare_eval_runs.py` validates the paired item/reference contract
   and estimates the candidate-minus-baseline metric difference using a
   fixed-seed paired bootstrap.

Embedding models must be locally cached; Hugging Face offline mode prevents
weight downloads. JSON generation is restricted to the local Ollama-compatible
endpoint. The scripts are not part of web startup, do not access the database,
and must only be given frozen evaluation examples, never user data.

## Interpretation

Retrieval reports Recall@k, MRR, and nDCG@10. JSON tasks report validity, field
agreement, Cohen's kappa, and exact-span validity. The latter requires exact
agreement with the labeled span set and verifies each character offset against
the original source text. Bootstrap intervals quantify uncertainty on the
paired sample; they do not establish corpus-wide quality or justify a model
change without representative data and operational review.
