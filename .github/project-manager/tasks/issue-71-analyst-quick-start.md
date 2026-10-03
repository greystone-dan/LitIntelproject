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

Evidence: Managed worker inspected the requested UI builders and source documents, then added a 709-word guide. User source-check identified retired standalone Judge Outcomes wording and requested explicit Judge Profile metrics, Minister-filter scope, and same-issue citation leads not being recommendations. Corrected `docs/ANALYST_QUICK_START.md`, canonical `docs/RESEARCH_UI_GUIDE.md`, and Swimm `.swm/6.maiixtsw.sw.md`; source details spot-checked in `backend/pages/data_explorer.py`, `backend/pages/memo_citation_check.py`, and `DOCS_INDEX.md`. Final guide is 759 words; whitespace-normalized required-content and relative-link assertions passed, and `git diff --check` passed. An initial phrase assertion did not normalize Markdown line wraps and was corrected; the final check passed. `python scripts/check_generated_docs.py` previously could not complete because FastAPI and SQLAlchemy are not installed; no generated references changed. Improvement recorded at `.github/project-manager/improvements/2026-10-03-analyst-guide-source-check.md`.

Files changed: `docs/ANALYST_QUICK_START.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`, `.github/project-manager/tasks/issue-71-analyst-quick-start.md`, `.github/project-manager/improvements/2026-10-03-analyst-guide-source-check.md`.
Delegated work: `managed-worker` implemented the documentation slice and returned the required structured report; see results above.
Focused validation: `git diff --check` and corrected whitespace-normalized Python assertions passed: 759 words (800-word ceiling), requested source-check details present, and no broken relative links. Generated-doc consistency check attempted; blocked by missing `fastapi` and `sqlalchemy` dependencies.
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
- Implementation: Corrected the plain-language guide against source-check notes; final 759-word content and link check passed.
- Documentation: Canonical `docs/RESEARCH_UI_GUIDE.md` and Swimm `.swm/6.maiixtsw.sw.md` clarify the active Judge Profile workflow and Minister filter scope.
- Recovery: Not applicable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Task created | Issue #71 specifies a bounded user-facing guide and source set. | `SYSTEM_REFERENCE.md`; `DOCS_INDEX.md`; issue request |
| 2026-10-03 | Correct source-check gaps | Distinguish sole active Judge Profile from retired Judge Outcomes and state the profile's denominator/filter scope; mark same-issue memo authorities as context, not recommendations. | User review; `DOCS_INDEX.md`; `backend/pages/data_explorer.py`; `backend/pages/memo_citation_check.py` |

## Completion

Completion recorded: yes

Summary: Delivered and corrected the plain-language analyst guide, aligned its canonical and Swimm references, and recorded a follow-up documentation-process improvement.

Validation: `git diff --check` and corrected focused content/length/link checks passed; generated-doc check attempted but blocked by missing FastAPI/SQLAlchemy dependencies.

Residual risk: Generated-reference consistency was not verified in this dependency-incomplete environment; no generated artifacts were changed.

Next recommended task: None; the workflow cross-check recommendation is recorded for future documentation work.
