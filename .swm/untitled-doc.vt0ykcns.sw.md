---
title: Data Quality Evaluation and Metrics
---

# Data Quality and Metrics

## Purpose

Counts describe inventory; quality metrics describe whether the inventory is
usable. Every metric must name its corpus scope, source scope, extraction date,
definition, and known limitations.

## Required Measures

| Area | Measures |
| --- | --- |
| Inventory | Cases, full-text cases, chunks, citations, statutes, tags, embeddings |
| Provenance | Source completeness, primary-source status, hashes, retrieval timestamps |
| Citations | Extracted occurrences, resolved targets, unresolved rows, unique targets, valid offsets |
| Statutes | IRPA/IRPR pickup, nested-provision coverage, false positives, span errors |
| Metadata | Field completeness, confidence, review flags, outcome classification coverage |
| Graph | Orphan targets, duplicate/self edges, connected cases, metric freshness |
| Retrieval | Recall/hit@k, MRR, query latency, candidate-pool and result bounds |
| Operations | Job completion, retry/resume state, records seen/updated, error reasons |

## Interpretation Rules

Occurrence counts are not unique-entity counts. A resolved citation link is not
proof of a correct legal proposition. A populated activity or staging layer is
not proof of official judgment capture. Extraction pickup and cleanliness must
be reported separately, and more rows do not automatically mean better quality.

## Quality Gates

Before a corpus-wide rebuild, run a bounded sample and compare before/after
counts, missing rows, unexpected rows, invalid offsets, duplicates, and source
provenance. For IRPA/IRPR, retain positive, negative, punctuation, heading, and
nested-form fixtures such as `34(1)(f)`.

## Refactoring Use

Metrics are acceptance evidence for structural changes. A route/module split
must preserve response counts and semantics; an extractor split must preserve
span validity and layer separation; an ingestion split must preserve source
identity and merge outcomes. Store reports under the existing evaluation/report
conventions and link them from the relevant Swimm walkthrough.

## Metric Ownership

Each metric has an owner and a scope. Extraction owns occurrence pickup and span
validity; resolution owns target-link rate and unresolved reasons; graph code
owns edge and centrality measures; search owns relevance and latency; ingestion
owns provenance completeness and merge outcomes; tagging owns label quality and
taxonomy coverage. Do not combine these into one quality score without showing
the underlying measures.

## Before/After Report Contract

A useful report records corpus/source scope, timestamp, code or taxonomy
version, input count, output count, missing/unexpected rows, duplicates,
invalid offsets, unresolved references, and sampled examples. Every percentage
must include its denominator. Occurrence counts, unique entities, and affected
cases must remain separate.

## Refactoring Signals

Use metrics to detect semantic drift during modularization: route response
counts and keys, extraction spans, statute layer counts, tag distributions,
source provenance completeness, and graph orphan rates. A structurally cleaner
module that changes these unexpectedly is not complete until the difference is
explained and accepted.

## Automated Data Quality Evaluation Tool

Corpus health and data quality audits are automated via `scripts/evaluate_data_quality.py`.
The tool executes deterministic SQL queries across the canonical PostgreSQL tables to
measure inventory completeness, citation resolution, self-citations, orphan targets,
invalid character offset spans, and metadata completeness.

Run from repository root:

```powershell
.\venv\Scripts\python.exe scripts\evaluate_data_quality.py --output-file data\eval\reports\data_quality_report.json
```

## Authority

Use `docs/METRICS_DICTIONARY.md` for definitions, `docs/TESTING_MATRIX.md` for
coverage boundaries, `SYSTEM_REFERENCE.md` for current system meaning, and live
API/database queries for current counts. Do not copy dated counts into a new
walkthrough without a timestamp and source statement.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBTGl0SW50ZWxwcm9qZWN0JTNBJTNBZ3JleXN0b25lLWRhbg==" repo-name="LitIntelproject"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
