# Still To Do Register

Last reviewed: 2026-09-29

## Purpose

This is the consolidated register of remaining work across product delivery,
data quality, operations, and research intelligence. It is a planning
synthesis, not a live-status source: use APIs, database audits, run state, and
task records for current counts and executable details.

Status meanings:

- **Active**: a current commitment or measurable gap.
- **Ready**: can begin with a bounded validation or dry run.
- **Blocked**: needs an approval, decision, or prerequisite.
- **Deferred**: intentionally later than the demo and quality gates.
- **Implemented**: retained to avoid duplicate planning, not new backlog.

The active product sequence is in [ROADMAP.md](../ROADMAP.md); long-term
intelligence constraints are in [LONG_TERM_INTELLIGENCE_VISION.md](LONG_TERM_INTELLIGENCE_VISION.md).

## Priority Shortlist

Rank | Next task | Why now | Cheapest gate
--- | --- | --- | ---
1 | Citation short-form anchor quality audit and backfill decision | $78,372$ short-form rows lack anchor provenance and more unresolved anchored rows need bounded recovery evidence. | Run a $100$-case dry run with exact anchor-text and offset checks; approve no write until reviewed.
2 | Issue and case-type discovery entry points | The primary demo journey still starts too much from known case names. | Build five curated issue/type entry points and verify a new user reaches a relevant case in under two minutes.
3 | Judge extraction $95\%$ post-2005 evaluation | Judge profiles and any backfill depend on proving the gate over a fresh, batched cohort. | Resume the checkpointed read-only evaluation and measure profileable coverage.
4 | Release quality thresholds | Existing evaluator metrics are informative but not consistently release-blocking. | Define critical, warning, and pass thresholds; run the evaluator against the live database and record the result.
5 | Retrieval benchmark and endpoint performance baseline | Two fixed retrieval questions and no p50/p95 budget are insufficient for safe optimization. | Add ten labeled research questions and measure MRR/precision plus representative endpoint latency.
6 | Statute authority coverage dry run | Reference coverage is thin relative to stored statute rows, despite validated source snapshots. | Run the approved bounded source/indexing dry run and inspect resolution deltas before any corpus writer.
7 | Citation truncation gold-set audit | Likely truncation was observed externally but is not classified by shape or measured by F1. | Label $100$-$200$ examples across citation forms and run exact-span precision/recall evaluation.
8 | Data Explorer state and mobile workflow audit | Search-to-reader-to-return and $390$px behavior are core demo paths with incomplete browser evidence. | Run desktop and mobile browser journeys; convert any failure into a focused UI task.
9 | Review Discussion Unit pilot artifacts | Deterministic subthemes are promising, but model-assisted labels remain report-only and unapproved. | Review the first nine completed Markdown reports plus the case $677$ raw-error artifact; make an explicit continuation decision.
10 | FC Activity subject and judge coverage measurement | Activity data is useful but subjects are frequently unknown and judge/profile coverage is not yet at its gate. | Audit $100$ unknown-subject records and complete the judge coverage evaluation before any write approval.
11 | Documentation authority cleanup | Current rules exist, but root docs, `docs/`, Swimm, and task records still overlap. | Finish an authority-map audit and retire or cross-link stale duplicate documents.
12 | Citation Intelligence evidence navigation | The feature is strong analytically but researchers still need a shorter path from an authority to stored passages. | Reopen [task 146](../.github/project-manager/tasks/146-citation-intelligence-evidence-path.md) only after the shortlist confirms its priority.

## Product And Demo

Item | Status | Evidence | Next gate
--- | --- | --- | ---
Issue/type discovery for procedural fairness, H&C, inadmissibility, refugee protection, and judicial review | Ready | [ROADMAP P0](../ROADMAP.md) | Curated entry-point prototype and non-expert journey test.
Unified research journey: discovery, reader, evidence, authority, return | Active | [ROADMAP P1](../ROADMAP.md) | Three scripted golden-path scenarios and browser checks.
Reader hierarchy, loading, empty/error states, accessibility, and mobile polish | Active | [ROADMAP P2](../ROADMAP.md) | Desktop plus $390$px interaction review.
Search-state persistence and return navigation | Partially active | [ROADMAP P1](../ROADMAP.md) | Browser test of filters, selected case, reader close, and return state.
Citation Intelligence evidence navigation | Deferred | [task 146](../.github/project-manager/tasks/146-citation-intelligence-evidence-path.md) | Read-only UI/API inventory before a small evidence-first change.
Research workbench, saved questions, notes, and evidence bundles | Deferred | [ROADMAP deferred track](../ROADMAP.md) | Reconsider only after demo acceptance and a persistence design decision.

## Citation, Statute, And Corpus Accuracy

Item | Status | Evidence | Next gate
--- | --- | --- | ---
Short-form anchor provenance gaps and unresolved anchored rows | Ready | [OVERNIGHT.md](../OVERNIGHT.md), tasks $068$-$070$ | Bounded exact-anchor dry run; extraction and resolution stay separate.
High-confidence unresolved citation recovery | Deferred behind anchors | [OVERNIGHT.md](../OVERNIGHT.md), tasks $065$-$069$ | Use only formal/exact and source-provenance evidence; no fuzzy bulk resolution.
Citation truncation precision/recall | Active gap | [technical debt register](../.swm/technical-debt-register-and-improvement-queue.tlm730zr.sw.md) | Labeled $100$-$200$ fixture set by citation type and exact-span score.
IRPA/IRPR nested-provision corpus pickup | Ready measurement | [SYSTEM_REFERENCE.md](../SYSTEM_REFERENCE.md) | Read-only $1,000$-case pickup audit; preserve positive, negative, and exact-span fixtures.
Statute/instrument authority coverage | Active | [OVERNIGHT.md](../OVERNIGHT.md), tasks $099$-$111$ | Priority source dry run and resolution report before any writer.
Paragraph chunk HTML/text parity | Active gap | [OVERNIGHT.md](../OVERNIGHT.md), task $052$ | Cross-court $50$-case comparison and explicit acceptance rule for divergence.
Citation resolution remainder | Deferred | [OVERNIGHT.md](../OVERNIGHT.md) | Do not reopen broad resolution until anchor quality and confidence gates pass.

## Operations, Reliability, And Documentation

Item | Status | Evidence | Next gate
--- | --- | --- | ---
Corpus quality evaluator thresholds | Active | [technical debt register](../.swm/technical-debt-register-and-improvement-queue.tlm730zr.sw.md) | Turn current measures into release pass/warn/fail rules.
Retrieval benchmark expansion | Ready | [ROADMAP](../ROADMAP.md), task $024$ | Ten labeled questions with MRR, precision@$k$, and recall@$k$.
Endpoint performance budgets | Ready | [technical debt register](../.swm/technical-debt-register-and-improvement-queue.tlm730zr.sw.md) | Representative p50/p95 and row-scan baseline for search and citation-map routes.
Browser regression coverage | Active | [technical debt register](../.swm/technical-debt-register-and-improvement-queue.tlm730zr.sw.md) | Extend the existing smoke journey only when a primary flow lacks proof.
Judge extraction/profileability $95\%$ gate | Blocked by measurement | [task 143](../.github/project-manager/tasks/143-judge-extraction-95-percent.md) | Checkpointed fresh post-2005 evaluation; no profile backfill until it passes.
Documentation authority map and retirement | Active | [DOCS_INDEX.md](../DOCS_INDEX.md) | Inventory overlaps, update authority links, and retire stale copies.
Overnight safety and checkpointing | Implemented | [OVERNIGHT.md](../OVERNIGHT.md) | Maintain exclusive-writer and resume safeguards; no new feature work required.

## Contextual And Advanced Intelligence

Item | Status | Evidence | Next gate
--- | --- | --- | ---
Discussion Unit coarse-boundary quality | Measured, review-only | [task 145](../.github/project-manager/tasks/145-discussion-unit-core-300-structural-audit.md) | Stratified human review of the $11$ collapsed and $231$ oversized-unit cases.
Discussion Unit subtheme/argument segments | Promising, review-only | [task 145](../.github/project-manager/tasks/145-discussion-unit-core-300-structural-audit.md) | Decide whether to prototype fine-subtheme-first segmentation after review.
Model-assisted Discussion Unit labels | Blocked by review | [NEXT_STEPS.md](NEXT_STEPS.md) | Approve or reject first-ten artifacts before any remaining $290$ calls.
Citation context and purpose candidates | Deferred architecture | [LONG_TERM_INTELLIGENCE_VISION.md](LONG_TERM_INTELLIGENCE_VISION.md), task $122$ | $100$-case context-window prototype with evidence spans; no runtime treatment claim.
Distinguishing, boilerplate, novelty, and authority-use evolution | Deferred | [MASTER_IDEAS.md](../MASTER_IDEAS.md) | Revisit only after reviewed context/purpose evidence exists.
Authority recommendation and research-gap detection | Deferred | [MASTER_IDEAS.md](../MASTER_IDEAS.md) | Begin with bounded missing-authority evidence; do not treat recommendations as legal conclusions.
Semantic clustering, embeddings, forecasting, and knowledge-graph overlays | Deferred | [MASTER_IDEAS.md](../MASTER_IDEAS.md) | Require demo acceptance, stable evidence layers, and an explicit product decision.

## Federal Court Activity

Item | Status | Evidence | Next gate
--- | --- | --- | ---
Judge recognition and profile linkage | In progress | [task 143](../.github/project-manager/tasks/143-judge-extraction-95-percent.md) | Same fresh $95\%$ evaluation gate as the case corpus.
Subject taxonomy coverage | Active gap | FC Activity task records and [SYSTEM_REFERENCE.md](../SYSTEM_REFERENCE.md) | Review $100$ records with `unknown` subject and propose evidence-backed taxonomy additions.
Filing-to-removal and motion-to-removal delay coverage | Sparse measurement | FC Activity evaluation reports | Expand to a $1,000$-case read-only sample and report missing-date patterns.
Removal destination and stay-cancellation grounding | Ready audit | [SYSTEM_REFERENCE.md](../SYSTEM_REFERENCE.md) | Read $50$ stored records against source text before publishing any aggregate claim.
Independent Oracle Worker operation | Blocked by approval | [FC Activity Oracle Worker runbook](FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md) | Security/runbook review, then a bounded $100$-case staging dry run; no canonical writer yet.
FC History charts | Implemented | [task 144](../.github/project-manager/tasks/144-fc-activity-panel-charts.md) | Keep descriptive inventory charts separate from procedural-outcome claims.

## Implemented Or Closed: Do Not Replan As New Work

- Citation Surprise, Missing Authority Detection, Citation Completion, position
  profiles, hidden authority paths, lifecycle tracking, and cross-court flow
  are implemented citation-map capabilities; see [MASTER_IDEAS.md](../MASTER_IDEAS.md).
- IRPA/IRPR nested provision extraction has passing exact-span fixtures. The
  remaining task is corpus pickup measurement, not a duplicate parser rewrite.
- The self-citation cleanup is complete; future rebuilds must retain its filter.
- The FC Activity annual filings, registry-location, case-class, and filing-track
  views are active; do not reintroduce a misleading outcome-flow graph without
  exclusive source-grounded branch data.
- Discussion Units and paragraph assessments are report-only experimental
  evidence, not canonical data layers or runtime citation-treatment labels.

## Deliberately Out Of Scope

Do not schedule automatic legal advice, outcome prediction, opaque clustering
as an evidence replacement, unreviewed treatment classification, or a broad
corpus writer without its own bounded task, preflight, and approval.