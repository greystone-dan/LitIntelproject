---
title: Technical Debt Register and Improvement Queue
---

# Technical Debt Register and Improvement Queue

This is the connected register for engineering debt and high-leverage product
improvements. It is a prioritization aid, not a replacement for task records,
the roadmap, or current architecture documentation.

## How To Read This Register

Each item should state the affected owner surface, evidence, user or system
impact, priority, candidate remedies, and the trigger for revisiting it. A debt
item is not closed because code was changed; it is closed when the stated pain
is measured again and the acceptance check passes.

## Current High-Priority Debt

| Priority | Debt or opportunity | Owner surface | Evidence / impact | Next check |
| --- | --- | --- | --- | --- |
| P0 | Browser regression coverage is incomplete | Active UI | Route tests cannot prove search-to-reader, highlighting, close flow, or mobile layout | **Addressed:** run `python scripts/browser_smoke.py` against the refreshed site; expand only when a journey fails |
| P0 | Corpus quality gates are not release-blocking | Evaluation / operations | Orphans, malformed citations, duplicate edges, and null metadata need repeatable thresholds | Run the data-quality evaluator and define thresholds |
| P0 | Citation extraction may truncate some case-to-case references | Citation extraction | External audit identified likely truncation patterns in a large stored sample | Produce labeled fixtures and measure precision/recall |
| P0 | Existing self-citation rows require reconciliation | Corpus integrity / citation resolution | **Resolved 2026-09-04:** guarded cleanup removed 241,272 exact self-links after recovery export and count verification | Keep rebuild filter and quality gate in place |
| P0 | Nested IRPA/IRPR extraction is release-sensitive | Citation/statute extraction | **Fixture baseline green:** 4 fixtures, 5 matches, 100% precision/recall/exact-span accuracy; corpus coverage remains separately measured | Expand labeled forms only when a concrete miss is identified |
| P1 | Retrieval quality lacks a broad benchmark | Search and retrieval | **Initial baseline addressed:** two fixed Data Explorer queries reach expected results at rank 1; broader legal research questions are still needed | Expand labeled questions and add ranking non-regression thresholds |
| P1 | Endpoint performance budgets are not established | API / analytics | Large corpus queries need p50/p95 and bounded-scan evidence | Measure representative endpoint samples |
| P1 | Citation context and purpose are not yet persisted | Citation intelligence | Researchers can see occurrences but not consistently why an authority is cited | Prototype context windows and purpose labels |
| P1 | Documentation authority is distributed across overlapping Markdown | Documentation / governance | Root docs, `docs/`, `.swm/`, tasks, and history have different freshness and roles | Complete the authority map before retiring duplicates |
| P1 | Core subset HTML reacquisition required iframe content handling | Ingestion / source acquisition | **Initial canary addressed:** five core cases now have validated snapshots; two fell back below mapping confidence threshold | Expand only with bounded preflight and confidence reporting |
| P1 | FCA/SCC HTML structure differs from FC | Ingestion / structural mapping | Cross-court canary found FCA clean, FC variable, and SCC lower whole-document confidence despite strong body block mapping | Add source-aware body scoping and paragraph rules |

## Deferred Opportunities

- Research workbench with saved questions, authorities, notes, and evidence bundles.
- Citation-only related-case discovery and authority recommendation.
- Distinguishing, boilerplate, and novel-reasoning signals.
- Read-only database evidence access for bounded product reviews.

## Closure Rule

Every item that enters implementation gets one task record, one owning surface,
one falsifiable acceptance check, and evidence recorded here or in the linked
Swimm walkthrough. Do not silently expand a debt item into multiple owner
surfaces.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBTGl0SW50ZWxwcm9qZWN0JTNBJTNBZ3JleXN0b25lLWRhbg==" repo-name="LitIntelproject"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
