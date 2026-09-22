# Task: Preserve long-term intelligence vision

Status: complete
Created: 2026-09-22
Updated: 2026-09-22

## Task Record

Task: Create a durable architecture and product-vision document for citation-treatment intelligence, Decision Units, Argument Packets, and cross-case argument comparison.

Why now: Recent deterministic work establishes the evidence and contextual-authority foundation, but the larger intelligence direction is currently distributed across task records, roadmap notes, and conversation decisions. A maintained document is needed to preserve the direction without prematurely committing to implementation.

Owner surface: `docs/LONG_TERM_INTELLIGENCE_VISION.md` and its canonical documentation links.

Commit allowed: yes

Push allowed: yes

Dependencies: `SYSTEM_REFERENCE.md`, `ROADMAP.md`, `MASTER_IDEAS.md`, recent tasks 134-137, contextual-authority walkthroughs, and existing citation/statute provenance contracts.

Risk boundary: Documentation only. Do not add schema changes, canonical writes, local generative-model integration, semantic clustering, or UI commitments. Do not describe deferred or report-only layers as production facts.

Smallest falsifiable check: `git diff --check` plus a local-link and status review of the new document.

Acceptance criteria:

- The document defines the long-term intelligence model, data relationships, technical challenges, evidence/provenance rules, evaluation gates, sequencing, and non-goals in depth.
- It reflects the validated work from tasks 134-137 and distinguishes current, planned, deferred, and unknown capabilities.
- `SYSTEM_REFERENCE.md`, `ROADMAP.md`, and the relevant Swimm walkthrough link to the document where appropriate.
- Focused documentation validation passes with no whitespace errors or misleading implementation claims.

Docs/generated references: `SYSTEM_REFERENCE.md`, `ROADMAP.md`, `.swm/8.upryk5h6.sw.md`, and this task record. No generated document is hand-edited.

Rollback/recovery: Revert only the documentation changes from this task. No data or runtime recovery is required.

Evidence: Delegated Explore review inspected tasks 134-137, ROADMAP.md, SYSTEM_REFERENCE.md, MASTER_IDEAS.md, current contextual-authority code and tests, and relevant Swimm maps. Added `docs/LONG_TERM_INTELLIGENCE_VISION.md` and linked it from `SYSTEM_REFERENCE.md`, `ROADMAP.md`, and `.swm/8.upryk5h6.sw.md`. `git diff --check` passed with no whitespace errors. A follow-up path/status check confirmed both new files are present and untracked as expected. Final reference inspection found one link in each of the three consumer documents; automated raw-string counts report two per file because Markdown links contain the path in both label and target.

## Hypothesis

If the vision is expressed as a provenance-first projection over existing evidence layers, then a documentation review can distinguish implemented foundations from deferred intelligence without requiring code or schema changes.

## Plan

1. Synthesize the delegated review and current architecture documents into one maintained vision.
2. Add focused links from canonical architecture, roadmap, and contextual-authority documentation.
3. Run markdown hygiene, link/status review, and inspect the final diff.

## Execution Checkpoints

- Delegation: Explore agent reviewed recent task records and strategy documents; report saved in the chat-session resource path.
- Implementation: Added `docs/LONG_TERM_INTELLIGENCE_VISION.md` and three canonical links; `git diff --check` passed.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `ROADMAP.md`, and `.swm/8.upryk5h6.sw.md`.
- Recovery: Not applicable; documentation-only task.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-22 | Task created | Preserve the larger intelligence direction while keeping delivery deferred and bounded | Recent review of tasks 134-137 and current architecture docs |

## Completion

Completion recorded: yes

Summary: Created and linked the durable long-term intelligence vision. The document covers Decision Units, citation treatment, Argument Packets, provenance, deterministic/probabilistic boundaries, evaluation, risks, sequencing, and deferred scope.

Validation: `git diff --check` passed. `Test-Path docs/LONG_TERM_INTELLIGENCE_VISION.md` returned `True`. Final reference inspection found one Markdown link in each canonical consumer document. No runtime or schema changes were made.

Residual risk: The proposed intelligence model will require legal-domain review and benchmark construction before runtime activation.

Next recommended task: Define a bounded Decision Unit benchmark from the existing read-only cohort.
