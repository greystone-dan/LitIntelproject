# Task: Add legally cautious overruling-risk warnings

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Implement issue #150's seed-based direct and citation-derived overruling-risk warnings in the API and active case reader.

Why now: Researchers need traceable, explicitly provisional signals for selected legal developments, including Vavilov's displacement of the pre-Vavilov standard-of-review framework.

Owner surface: Overruling-risk feature (new service/seed module with minimal API and active-reader registration).

Commit allowed: no

Push allowed: no

Dependencies: Existing case/citation ORM and active Data Explorer case-reader payload; canonical and Swimm documentation.

Risk boundary: No database access or schema/DB-operation changes, deployment, secrets, password-gate changes, or removals of existing features. Every seed entry and returned flag must say “seed list, needs lawyer review”; avoid definitive statements about legal status. Keep exact sources, dates, rationales, and assignment explanations visible. Preserve unrelated worktree changes.

Smallest falsifiable check: `python -m pytest -q tests/test_overruling_risk.py`

Acceptance criteria:

- An editable, documented seed list contains source and rationale per entry and includes only certain events, including Canada (MCI) v Vavilov, 2019 SCC 65, as displacing the pre-Vavilov standard-of-review framework.
- `GET /api/overruling-risk/{case_id}` returns direct and citation-derived indirect flags with count, relevant dates, source/rationale, and “how assigned”; the feature is read-only.
- The active reader adds a non-destructive banner when a flag exists; indirect warnings say “may be affected,” while a direct match to the development authority is not incorrectly described as affected by itself.
- Requested fixture tests cover direct flags, indirect reliance, dates/count, cautious wording, and absent flags.
- `docs/reports/overruling-risk.md`, `SYSTEM_REFERENCE.md`, and the relevant Swimm walkthrough explain behavior and how to extend the seed list.
- Focused tests, required generated-document check, secret scan of changed files, and `git diff --check` pass; generated references are regenerated rather than hand-edited if needed.

Harness criteria:
- API contract returns direct and indirect flags with provenance, assignment explanation, count, and dates.
- Reader warning is additive, cautious, and absent when there are no flags.
- Required tests and documentation checks pass.

Docs/generated references: `docs/reports/overruling-risk.md`, `SYSTEM_REFERENCE.md`, `docs/ARCHITECTURE.md`, `DOCS_INDEX.md`, `CHANGELOG.md`, `.swm/1.oi7rhqp2.sw.md`, `.swm/6.maiixtsw.sw.md`, and `docs/API_REFERENCE.generated.md` via `scripts/generate_api_reference.py`.

Rollback/recovery: Revert the additive feature modules, focused route/reader integration, fixtures, and documentation; no database state or migration is involved.

Evidence: Read `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`, `OVERNIGHT.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, `.swm/1.oi7rhqp2.sw.md`, and `.swm/6.maiixtsw.sw.md`. Updated `docs/reports/overruling-risk.md`, `SYSTEM_REFERENCE.md`, `docs/ARCHITECTURE.md`, `DOCS_INDEX.md`, `CHANGELOG.md`, and both named Swimm walkthroughs; regenerated `docs/API_REFERENCE.generated.md`. A managed worker returned the structured API/service implementation and fixture-test result; the manager completed reader integration, documentation, generated-reference regeneration, review fixes, and acceptance. Refreshed `origin/main`; `git rev-list --left-right --count HEAD...origin/main` returned `1 0` (HEAD is one existing commit ahead, origin/main is its ancestor), so no merge was needed. No database access, deployment, commit, or push.

Files changed: `.github/project-manager/tasks/issue-150-overruling-risk.md`, `.swm/1.oi7rhqp2.sw.md`, `.swm/6.maiixtsw.sw.md`, `CHANGELOG.md`, `DOCS_INDEX.md`, `SYSTEM_REFERENCE.md`, `backend/main.py`, `backend/overruling_risk.py`, `backend/overruling_risk_routes.py`, `backend/pages/data_explorer.py`, `backend/pages/overruling_risk_reader.js`, `docs/API_REFERENCE.generated.md`, `docs/ARCHITECTURE.md`, `docs/reports/overruling-risk.md`, `tests/test_feature_tabs.py`, `tests/test_overruling_risk.py`.
Delegated work: `managed-worker` owned only the seed/service, route registration, and API fixture tests. It returned the required structured report, noting that pytest was initially absent. Manager later installed only existing pinned project/test packages into the local user environment (no dependency manifest changed), validated the work, and retained task/documentation/review ownership.
Focused validation: `python -m pytest -q tests/test_overruling_risk.py tests/test_feature_tabs.py tests/test_documentation_contracts.py::test_architecture_backend_inventory_matches_files_on_disk` — 66 passed, 1 skipped. `python scripts/generate_api_reference.py` regenerated 107 operations; `python scripts/check_generated_docs.py` passed (3 references current). Node syntax, Python compilation, targeted secret-pattern scan, 9 new local-link checks, and `git diff --check` passed.
Residual risk: The full suite with the three configured deselections reported 1,267 passed, 2 skipped, 1 xfailed, and 3 failures: one requires the absent `sentence-transformers` package and two require an unavailable tokenizer download from `openaipublic.blob.core.windows.net`. No browser/server or database validation was performed; the reader renderer was exercised with a deterministic Node DOM fixture. The seed is intentionally non-exhaustive and requires lawyer review; stored citations do not prove legal reliance or effect.
Next bounded task: Have counsel review the Vavilov seed's source/rationale and approve any additional events before the seed list is expanded.

## Hypothesis

If a read-only seed-backed service is correctly wired to the active reader, focused fixture tests will demonstrate transparent direct/indirect flags with dates and cautious wording without requiring a schema change.

## Plan

1. Delegate a bounded implementation/test slice and inspect the relevant Swimm walkthrough.
2. Independently accept the API/UI behavior and complete the canonical report and Swimm documentation checkpoint.
3. Run required security, generated-document, focused, and appropriate broader validations; refresh/check main as instructed without merging unrelated changes.

## Execution Checkpoints

- Delegation: `managed-worker` returned the required structured result for the API/service slice.
- Implementation: Read-only API, one Vavilov seed, direct/indirect fixture coverage, and escaped reader banner implemented; direct-authority wording distinguishes the listed development case from cases that may be affected.
- Documentation: Updated `docs/reports/overruling-risk.md`, `SYSTEM_REFERENCE.md`, `docs/ARCHITECTURE.md`, `DOCS_INDEX.md`, `CHANGELOG.md`, `.swm/1.oi7rhqp2.sw.md`, and `.swm/6.maiixtsw.sw.md`; generated `docs/API_REFERENCE.generated.md` using its generator.
- Recovery: Not applicable; no data writes.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | Issue #150 is a multi-phase API/reader change with legal-risk constraints. | Read `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`, `OVERNIGHT.md`, and `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`; baseline refs observed above. |
| 2026-10-04 | Separated development-authority direct match from affected-case language | The seeded Vavilov authority should not be described as affected by the event it establishes. | Code review finding fixed in service assessments and reader banner; direct/indirect fixture tests pass. |
| 2026-10-04 | Regenerated API reference and synchronized backend inventory | The new public endpoint belongs in the generated API reference and file inventory. | API generator succeeded; generated-doc and architecture inventory checks pass. |
| 2026-10-04 | Accepted with bounded full-suite limitations | Focused tests and generated docs pass; remaining broad-suite failures require an unavailable local model package or external tokenizer download. | Focused results and full-suite counts are recorded above. |

## Completion

Completion recorded: yes

Summary: Implemented the legally cautious Vavilov seed-backed direct/indirect warning API and additive active-reader banner, with fixtures and synchronized docs.

Validation: Focused combined tests: 66 passed, 1 skipped. Generated-doc check passed. Full suite: 1,267 passed, 2 skipped, 1 xfailed, 3 deselected, 3 failed for the recorded environment/network blockers. Secret scan, source syntax, new local links, and whitespace checks passed.

Residual risk: Seed coverage is deliberately narrow and needs lawyer review; citation edges do not establish legal reliance. No live browser/server/database operation was performed.

Next recommended task: Obtain lawyer review of the Vavilov seed before considering additional entries.
