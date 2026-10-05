# Task: Design ID/IAD decision coverage for CBSA hearings

Status: complete
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Produce a cited, evidence-labeled design for adding Immigration Division (ID) and Immigration Appeal Division (IAD) decisions relevant to CBSA hearings; documentation only.

Why now: The requested coverage needs trustworthy source/licence evaluation, distinct tribunal and outcome treatment, and a phased ingestion/UI plan before implementation.

Owner surface: Documentation — `docs/reports/id-iad-coverage-design.md`, its canonical documentation pointers, and Swimm architecture rationale.

Commit allowed: yes

Push allowed: yes

Dependencies: Current architecture references; cautious source and terms verification; no code or data changes.

Risk boundary: No implementation, acquisition, database writes, licensing assertions without evidence, or changes to unrelated worktree state. Mark every unchecked factual claim unverified.

Smallest falsifiable check: `python scripts/check_generated_docs.py` plus a focused local-link scan and `git diff --check`.

Acceptance criteria:

- The report covers sources and licence evidence, backend/schema impacts, outcome and Minister analytics, affected filters/pages, and a phased plan with a smallest first slice.
- Every unchecked claim is explicitly marked unverified; citations include URLs and access/verification limits.
- Canonical repository documentation and the relevant Swimm walkthrough point to the report.
- Documentation checks and `parallel_validation` run, with results recorded; no source-code files are changed.

Harness criteria:

- Report content and evidence labels reviewed.
- Canonical documentation and Swimm walkthrough updated.
- Documentation validation and `parallel_validation` results recorded.
- Changed files contain no secrets.

Docs/generated references: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, and the new report; generated references remain untouched.

Rollback/recovery: Revert only this task's documentation changes; preserve all pre-existing worktree changes.

Evidence: Documentation-only design completed. `docs/reports/id-iad-coverage-design.md` labels source, licence, availability, and legal-taxonomy claims unverified when not confirmed; source requests failed DNS resolution (`curl` HTTP 000), and no external terms were fetched. Canonical repository references updated at `SYSTEM_REFERENCE.md` and `DOCS_INDEX.md`; Swimm architecture rationale updated at `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`.

Files changed: `.github/project-manager/tasks/id-iad-coverage-design.md`, `docs/reports/id-iad-coverage-design.md`, `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`. No source-code or generated reference files changed.
Delegated work: `managed-worker` (`id-iad-evidence`) performed a bounded read-only review of candidate public sources/terms and local ingestion, schema, outcomes, and UI touchpoints before manager synthesis. Structured result: no files changed; candidate source URLs and repository observations supplied; all page/licence claims unverified because DNS resolution failed; see final evidence summary below.
Focused validation: Passed local Markdown link check (21 links; zero broken), `git diff --check`, changed-file whitespace scan, report-topic/claim-label check (all required topics present; 24 unverified markers), and changed-file secret-pattern scan (zero matches). `python scripts/check_generated_docs.py` was attempted but could not import FastAPI or SQLAlchemy, so generated-reference consistency remains unverified; no generated references were changed. These independent checks were run through `multi_tool_use.parallel`, the available parallel-call mechanism; no standalone `parallel_validation` tool/command was exposed.
Residual risk: External source availability, publication coverage, access method, licensing/reuse permissions, and legal outcome taxonomy remain unverified. Generated-document check is blocked by missing dependencies.
Next bounded task: Verify authoritative IRB source coverage and applicable access/reuse terms before any acquisition or schema implementation.

## Hypothesis

If the design is evidence-labeled and linked from the canonical architecture and Swimm rationale, then focused documentation validation will pass without source-code changes.

## Plan

1. Delegate bounded source and architecture evidence gathering.
2. Synthesize a documentation-only design with explicit claim status and phased scope.
3. Update canonical pointers and Swimm rationale, then validate and record evidence.

## Execution Checkpoints

- Delegation: Complete — worker returned required structured headings and reported zero files changed, bounded local inspection, and failed DNS/source-page access.
- Implementation: Documentation-only report and canonical pointers drafted; no source changes.
- Documentation: `docs/reports/id-iad-coverage-design.md`, `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, and `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`.
- Recovery: Not applicable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Task created as documentation-only | User explicitly requested the design note and no code changes | User request; `DOCS_INDEX.md` documentation ownership rules |

## Completion

Completion recorded: yes

Summary: Added the requested ID/IAD design note, linked it from canonical documentation and Swimm architecture rationale, and preserved the documentation-only boundary.

Validation: Local links, diff whitespace, report topic/evidence labels, and secret-pattern scan passed. Generated documentation check was run but could not complete because FastAPI and SQLAlchemy are not installed. Parallel validations were run with the available multi-tool parallel wrapper.

Residual risk: Candidate sources/licences and domain outcome taxonomy remain unverified; generated-reference consistency was not checked successfully due to missing dependencies.

Next recommended task: Perform authoritative source/terms review and a legal/domain taxonomy check before any acquisition pilot.
