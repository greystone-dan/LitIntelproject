---
title: Data Quality and Metrics
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

## Authority

Use `docs/METRICS_DICTIONARY.md` for definitions, `docs/TESTING_MATRIX.md` for
coverage boundaries, `SYSTEM_REFERENCE.md` for current system meaning, and live
API/database queries for current counts. Do not copy dated counts into a new
walkthrough without a timestamp and source statement.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBTGl0SW50ZWxwcm9qZWN0JTNBJTNBZ3JleXN0b25lLWRhbg==" repo-name="LitIntelproject"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
