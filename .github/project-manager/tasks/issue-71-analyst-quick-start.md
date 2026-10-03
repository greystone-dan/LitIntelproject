# Task: Create an analyst quick-start guide for iLit

Status: complete
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Create a plain-language, at-most-two-page quick-start for a CBSA litigation analyst new to iLit.

Why now: Issue #71 requests a practical research guide grounded in the current interface and honest about metric limitations.

Owner surface: User-facing research documentation (`docs/ANALYST_QUICK_START.md`).

Commit allowed: yes

Push allowed: yes

Dependencies: Current feature behavior in `backend/pages/`, `docs/RESEARCH_UI_GUIDE.md`, `README.md`, and `docs/METRICS_DICTIONARY.md`.

Risk boundary: Documentation only. Do not describe unimplemented features or imply outcome metrics are legal conclusions, complete coverage, or causal findings.

Smallest falsifiable check: `python scripts/check_generated_docs.py` plus a focused guide-content/length check and `git diff --check`.

Acceptance criteria:

- `docs/ANALYST_QUICK_START.md` is a clear plain-language guide of no more than two pages covering case search/reading, Citation Intelligence noting-up, judge profiles, FC activity analytics, memo citation checks, outcome and Minister win-rate metric interpretation (including unclassified cases and limitations), and what iLit does not do.
- All described workflows and metric caveats match current implementation and canonical references.
- The relevant Swimm Active UI walkthrough and canonical `docs/RESEARCH_UI_GUIDE.md` reference the guide and remain aligned.
- Focused documentation checks pass.

Harness criteria: N/A; no harness run declared.

Docs/generated references: Canonical `docs/RESEARCH_UI_GUIDE.md`; Swimm Active UI walkthrough under `.swm/`; read `README.md` and `docs/METRICS_DICTIONARY.md`. Generated references are not expected to change.

Rollback/recovery: Revert only this task's documentation changes if inaccurate; no runtime or data changes.

Evidence: Managed worker inspected the requested UI builders and source documents, then added a 709-word guide. Manager spot-checked the government win-rate denominator and unclassified semantics against `docs/METRICS_DICTIONARY.md` (lines 75–78), and memo upload/privacy wording against `backend/pages/memo_citation_check.py` (line 18). The guide and links passed the focused content/length/link check and `git diff --check`. `python scripts/check_generated_docs.py` was attempted but could not complete because FastAPI and SQLAlchemy are not installed in this environment; no generated references were changed. Canonical documentation updated: `docs/RESEARCH_UI_GUIDE.md`. Swimm walkthrough updated: `.swm/6.maiixtsw.sw.md`.

Files changed: `docs/ANALYST_QUICK_START.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`, `.github/project-manager/tasks/issue-71-analyst-quick-start.md`.
Delegated work: `managed-worker` implemented the documentation slice and returned the required structured report; see results above.
Focused validation: Passed `git diff --check` plus Python content checks: 709 words (800-word ceiling), all requested topics present, and no broken relative links. Generated-doc consistency check attempted; blocked by missing `fastapi` and `sqlalchemy` dependencies.
Residual risk: The generated-reference check could not run in this environment. The guide describes current behavior and points readers to the canonical UI guide for detailed limitations.
Next bounded task: None.

## Hypothesis

If the guide reflects current UI builders and metric definitions, a bounded content/length check and generated-document consistency check will confirm that it is complete, concise, and does not drift into unsupported behavior.

## Plan

1. Delegate bounded evidence gathering and documentation implementation against the requested current sources.
2. Independently review the returned evidence and guide for accuracy, length, and required topics.
3. Run focused documentation validation and record both canonical and Swimm updates.

## Execution Checkpoints

- Delegation: Managed worker completed the source review and documentation edits with a structured report.
- Implementation: Added 709-word analyst quick-start; focused completeness, link, and length check passed.
- Documentation: Canonical `docs/RESEARCH_UI_GUIDE.md` and Swimm `.swm/6.maiixtsw.sw.md` updated and linked.
- Recovery: Not applicable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Task created | Issue #71 specifies a bounded user-facing guide and source set. | `SYSTEM_REFERENCE.md`; `DOCS_INDEX.md`; issue request |

## Completion

Completion recorded: yes

Summary: Delivered the plain-language analyst guide and connected it to the canonical UI reference and Active UI walkthrough.

Validation: `git diff --check` and focused content/length/link checks passed; generated-doc check attempted but blocked by missing FastAPI/SQLAlchemy dependencies.

Residual risk: Generated-reference consistency was not verified in this dependency-incomplete environment; no generated artifacts were changed.

Next recommended task: None.
