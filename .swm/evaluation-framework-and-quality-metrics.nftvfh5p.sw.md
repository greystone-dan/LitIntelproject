---
title: Evaluation Framework and Quality Metrics
---
# Evaluation Framework and Quality Metrics

This walkthrough defines how the project measures trust, quality, cost, and
research usefulness. Reports and benchmark outputs remain generated or stored
under `data/eval/`; this document defines their interpretation and gates.

## Evaluation Record Format

```text
Goal:
Dataset or sample:
Options compared:
Metrics:
Result:
Limitations:
Decision:
Next experiment:
```

## Core Metrics

| Metric | Meaning | Required interpretation |
| --- | --- | --- |
| Citation resolution rate | Stored case-citation rows linked to a local target | Separate extraction validity from local library coverage |
| Offset validity | Evidence spans that fit the owning source/chunk text | Measure exact-span integrity, not visual highlight count |
| Statute extraction coverage | Labeled statute references recovered from the evaluation set | Keep IRPA/IRPR nested provisions, including `34(1)(f)`, explicit |
| Tag coverage | Cases or labeled issue examples with supported taxonomy tags | State the denominator and distinguish unprocessed from untagged |
| Metadata completeness | Required structured fields populated with provenance | Do not treat inferred values as source facts without labels |
| Orphan/duplicate rate | Broken graph links or duplicate citation edges | Track as integrity defects, not merely search noise |
| Retrieval quality | MRR, recall@k, and precision@k on fixed questions | Compare against a stable benchmark before changing ranking |
| Performance | p50/p95 latency and bounded scan behavior | Measure on representative corpus and query conditions |

## Evaluation Families

1. **Citation and statute extraction:** precision, recall/coverage, exact spans,
	normalization, and negative cases.
2. **Metadata, outcomes, and tagging:** field accuracy, taxonomy consistency,
	evidence quality, winner/loser accuracy, mixed/unknown handling, and review
	burden.
3. **Search and retrieval:** benchmark hit quality, ranking stability, and
	latency budgets.
4. **Corpus integrity:** null metadata, malformed references, orphan links,
	duplicate edges, provenance completeness, and source hashes.
5. **Research workflow:** task completion time, evidence traceability, false
	positives, missed authorities, and researcher review burden.

## Release Gates

- No regression in focused exact-span tests.
- No new critical integrity defects.
- Benchmark and performance changes are recorded with their sample and method.
- Every surfaced recommendation retains a path to source evidence and
  uncertainty where applicable.
- Outcome classifications must preserve `mixed` and `undetermined` states and
	expose the operative disposition evidence used to derive winner/loser sides.
- The versioned `case_outcomes` table is the outcome source of truth; metadata
	fields are a compatibility mirror until downstream consumers migrate.
- A failed or unavailable optional model/integration cannot corrupt deterministic
  processing or canonical source records.

## Latest Baseline Signal

The 2026-09-04 read-only corpus run found zero orphan targets and zero invalid
citation offsets, but the quality gate failed on 241,272 self-citation rows.
Citation resolution was 62.0% and statute pinpoint coverage was 12.74% (advisory
until a release baseline is established). The self-citation count requires a
bounded cleanup design before any deletion or rewrite decision. New citation
rebuilds now filter exact source-case neutral and secondary citations; existing
rows were then removed by an explicitly authorized guarded cleanup with a
recovery export. The post-cleanup gate is `WARN`: self-citations, orphan targets,
and invalid offsets are zero; statute pinpoint coverage remains advisory at
12.74%.

A bounded self-citation audit classified the first 100 rows as 40 exact source
citation headers, 36 source-header caption artifacts, and 24 remaining review
candidates. The audit is read-only and does not establish that every remaining
candidate is invalid.

The read-only cleanup planner at `scripts/plan_self_citation_cleanup.py` is the
required checkpoint before any mutation. It caps samples at 1,000 rows and
reports `write_performed=False` and `cleanup_authorized=False`; its output is
evidence for review, not deletion authorization.

## Statute Extraction Baseline

The dedicated fixture evaluator at `scripts/evaluate_statute_extraction.py`
currently passes 4 fixtures and 5 expected statute matches with 100% precision,
100% recall, 100% exact-span accuracy, and zero false positives or negatives.
This is a deterministic fixture baseline, not a claim that corpus-wide statute
coverage is complete; the live corpus coverage signal remains 12.74% until its
denominator and target are further established.

## Decision Rule

Do not select a tagging, retrieval, or extraction approach from intuition alone
when a bounded labeled sample can compare it. Report accuracy, operational cost,
maintenance burden, scalability, and explainability together.

## Retrieval Benchmark Baseline

The fixed benchmark at `data/eval/retrieval_benchmark.json` evaluates the
user-facing Data Explorer search endpoint with two authority queries and a
top-10 result limit. The 2026-09-04 baseline reached rank 1 for both queries:
mean reciprocal rank `1.0`, recall@10 `1.0`, and precision@10 `0.30`. Precision
is intentionally reported against the expected relevant set per query, so the
authority-family query has five expected cases while the exact OU query has one.
Run `scripts/evaluate_retrieval_benchmark.py` after ranking changes; this is a
small regression baseline, not a complete retrieval-quality evaluation.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBTGl0SW50ZWxwcm9qZWN0JTNBJTNBZ3JleXN0b25lLWRhbg==" repo-name="LitIntelproject"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
