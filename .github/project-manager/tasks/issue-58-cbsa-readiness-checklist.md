# Task: CBSA Hearings and Litigation Division readiness checklist

Status: complete
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Deliver an evidence-grounded CBSA Hearings and Litigation Division readiness checklist.

Why now: Issue #58 requests a practical assessment of readiness across legal, technical, operational, and service risks.

Owner surface: Documentation — `docs/reports/cbsa-readiness-checklist.md`.

Commit allowed: yes

Push allowed: yes

Dependencies: Read-only inspection of application access helpers, setup/operations documentation, and project dependencies; unknown organizational facts require Daniel's input.

Risk boundary: No code, configuration, data, access, retention, or hosting changes; do not imply government approval, compliance, or controls unsupported by evidence.

Smallest falsifiable check: `git diff --check` plus manual local-link and exact-path review of the checklist.

Acceptance criteria:

- Checklist covers every requested topic, assigns met/partly/not met/unknown status, cites exact repository paths, and gives the smallest next step per item.
- Unknown organizational/operational facts needing Daniel input are called out explicitly.
- The issue report and task record link to the relevant Swimm walkthrough and canonical repository document.
- Focused documentation validation passes without running tests or builds.

Harness criteria: Report covers requested controls; evidence and Daniel-input unknowns are explicit; required docs and focused validation are recorded.

Docs/generated references: `docs/reports/cbsa-readiness-checklist.md`; related Swimm walkthrough under `.swm/`; no generated references.

Rollback/recovery: Documentation-only; remove or correct the new report and task record if unsupported claims are found.

Evidence: Managed-worker `cbsa-readiness-inventory` returned the required structured report after read-only inspection of 15 listed source/config/docs files; no files changed. It identified an application access-control gap and separated repository facts from deployment/organizational unknowns. Manager independently read `backend/main.py`, relevant sections of `SYSTEM_REFERENCE.md` and `SETUP.md`, the memo route/helper, live-analysis parser/UI, deployment/recovery/source-register docs, requirements, CI workflows, and `.swm/system-map.ovnldklv.sw.md`. Documentation now warns against relying on the app login, and the report labels production and policy facts unknown pending Daniel. No tests/builds were run per user constraint.

Files changed: `docs/reports/cbsa-readiness-checklist.md`; `SETUP.md`; `.swm/system-map.ovnldklv.sw.md`; `.github/project-manager/tasks/issue-58-cbsa-readiness-checklist.md`.
Delegated work: Managed-worker `cbsa-readiness-inventory`; read-only inventory, no changed files. `rg` was unavailable in its environment; targeted `grep` and file views supplied evidence. See structured result in manager conversation.
Focused validation: Passed in parallel — `git diff --check`; Python whitespace checks for new report/task Markdown; checklist topic/status coverage, cited-path existence, and added-link checks; task-field/docs-checkpoint check. A broader whole-file whitespace probe also surfaced pre-existing trailing whitespace at `.swm/system-map.ovnldklv.sw.md:5`; it was not changed, while `git diff --check` passed on changed hunks. No tests/builds run per user constraint.
Residual risk: Actual hosting/regions, external access enforcement, organization policies/approvals, data flows, and operational practices require Daniel or designated owners; report is not a compliance assessment.
Next bounded task: Obtain Daniel's answers to the report's explicit unknowns, starting with access enforcement and hosting/data-flow approval.

## Hypothesis

If this report is grounded and accurate, every requested readiness topic will have a conservative status, verifiable repository evidence (or an explicit absence of evidence), a minimum next step, and named Daniel questions where facts are organizational.

## Plan

1. Delegate a bounded read-only inventory of access, hosting, logging, retention, upload handling, backup/recovery, accessibility, languages, external services, licensing, and dependency controls.
2. Review the structured inventory and required source documents; draft the report with exact paths and clearly bounded conclusions.
3. Correct contradictory setup guidance, update the system-map walkthrough, and validate documentation links and diff formatting without tests/builds.

## Execution Checkpoints

- Delegation: Managed-worker `cbsa-readiness-inventory`; structured evidence inventory returned before manager's equivalent source review.
- Implementation: `docs/reports/cbsa-readiness-checklist.md`; focused draft check first found trailing whitespace on the assessment-date line, corrected before the path/whitespace check passed.
- Documentation: Canonical report `docs/reports/cbsa-readiness-checklist.md`; access warning corrected in `SETUP.md`; runtime walkthrough updated at `.swm/system-map.ovnldklv.sw.md`.
- Recovery: Not applicable; no long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Task created | Issue #58 asks for a bounded readiness report; source facts need verification before claims. | User scope and repository manager workflow |
| 2026-10-03 | Correct `SETUP.md` access claim while delivering report | Its prior statement that the app redirects/returns 401 conflicted with inspected middleware and could create false assurance. | `backend/main.py:78-82`; `SYSTEM_REFERENCE.md:1396-1400` |

## Completion

Completion recorded: yes

Summary: Delivered the evidence-grounded readiness checklist, corrected the setup access warning, and linked the report from the system-map walkthrough.

Validation: `git diff --check` passed; focused whitespace, coverage/status, cited-path/link, and task-record checks passed. No tests/builds were run.

Residual risk: Organizational facts may be unavailable in source control.

Next recommended task: Obtain Daniel's answers to explicitly listed unknowns.
