# Task: Add non-blocking lint and dependency audit workflow

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add an independent GitHub Actions workflow for PR and weekly Ruff and pip-audit checks, with separately uploaded logs and a first-results report.

Why now: Establish visible code/dependency-quality signals without making existing PR checks blocking or changing the test workflow.

Owner surface: `.github/workflows/` quality checks and their CI documentation.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing `tests.yml` remains unchanged; check pinned tool versions on main before selecting versions.

Risk boundary: Do not alter `.github/workflows/tests.yml`, existing test behavior, dependency resolution, application files, secrets, or production data.

Smallest falsifiable check: Run the same Ruff and pip-audit commands used by CI, inspect both outputs, and confirm each workflow result is uploaded independently.

Acceptance criteria:

- PR and weekly triggers run independent, non-blocking Ruff and pip-audit checks.
- Minimal Ruff errors and unused-import rules are enabled; tool outputs are uploaded as separate artifacts even on command failure.
- A plain-language first-results report is committed under `docs/reports/`.
- The manager Swimm walkthrough and canonical repository docs explain the workflow and link to its executable source.
- The required CI pytest command, documentation checks, secret scan, and final parallel validation are run and reported.
- `.github/workflows/tests.yml` is unchanged.

Harness criteria:
One criterion per line: both independent lint and audit results are artifact-backed and non-blocking
One criterion per line: first-results report and linked canonical/Swimm docs are coherent
One criterion per line: tests workflow remains unchanged and validation evidence is recorded

Docs/generated references: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.swm/11.nf15c1hd.sw.md`, `docs/reports/baseline-lint-and-audit.md`; no generated references.

Rollback/recovery: Revert only the new quality workflow and associated report/documentation/task changes; existing test workflow and other work remain untouched.

Evidence: The managed worker added the workflow; manager reviewed and narrowed its Ruff policy, pinned tools, and verified `FETCH_HEAD` at `079fb5451381be6108a829f8317b9104440bd90b` has no Ruff or pip-audit pins in `requirements-dev.txt`. Ruff 0.16.10 found 8,039 findings in 341 files; pip-audit 2.10.1 reported 242 advisory matches in 18 of 188 resolved packages. The required CI pytest command ran: 1,032 passed, 3 failed, 1 skipped, 1 xfailed, and 3 configured deselections. The three failures involved external Hugging Face model and OpenAI tokenizer downloads; the existing tests/call path were inspected and no tests or runtime files were changed. Focused workflow/YAML/shell validation passed; `python scripts/check_generated_docs.py`, `git diff --check`, local-link checks, changed-file secret-pattern scan, and the final parallel validation passed. `.github/workflows/tests.yml` remained unchanged (SHA-256 `e4c4f882e3127285570d8ace8ca19500bbc27f9e91d95fc60adc4e02c2c32426`). Canonical doc: `SYSTEM_REFERENCE.md`; report: `docs/reports/baseline-lint-and-audit.md`; Swimm walkthrough: `.swm/12.ci-quality-workflow.sw.md`.

Files changed: `.github/workflows/quality-checks.yml`, `docs/reports/baseline-lint-and-audit.md`, `.swm/12.ci-quality-workflow.sw.md`, `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `CHANGELOG.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, this task record.
Delegated work: `managed-worker` implemented only the new workflow and returned structured evidence; a second `managed-worker` ran the exact CI pytest command without modifying files.
Focused validation: `ruff check . --select E,F401 --output-format json` — 8,039 baseline findings (expected non-zero); `pip-audit --desc --format json -r requirements.txt` — 242 advisory matches (expected non-zero); YAML and embedded shell syntax validation plus `yamllint -d relaxed .github/workflows/quality-checks.yml` — passed; exact workflow artifact/job contracts — passed.
Residual risk: Existing Ruff baseline is large; dependency audit findings need separate compatibility and reachability triage. Three unrelated CI tests require external downloads and failed in this network-restricted environment.
Next bounded task: Triage the 18 dependency packages flagged by pip-audit and prioritize compatible remediation.

## Hypothesis

If an isolated CI workflow runs Ruff and pip-audit with error-tolerant steps and unconditional, separate artifact uploads, then PR and weekly quality findings remain reviewable without blocking the existing test gate.

## Plan

1. Verify applicable pinned tool versions and the narrowest relevant workflow/documentation surface.
2. Add and run the independent workflow and capture first results in a report.
3. Update canonical and Swimm documentation; validate tests, docs, secrets, and final changes.

## Execution Checkpoints

- Delegation: Pending.
- Implementation: Pending.
- Documentation: Pending.
- Recovery: Not applicable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | User requested an independent non-blocking quality workflow and evidence report | Existing workflow inventory and task template inspected |

## Completion

Completion recorded: yes

Summary: Added an independent, non-blocking PR/weekly Ruff and pip-audit workflow with pinned tools, isolated jobs, separate output/status artifacts, a first-results report, and canonical/Swimm documentation.

Validation: Focused quality tools ran and their initial results are documented. YAML, embedded shell, job/artifact contracts, generated documentation, local links, secret-pattern scan, whitespace, and final scope checks passed. `.github/workflows/tests.yml` is unchanged. The required existing CI pytest command ran but had three pre-existing network-dependent failures (1032 passed, 1 skipped, 1 xfailed, 3 deselected).

Residual risk: Ruff's existing baseline is large; audit findings need separate compatibility/reachability triage. The three network-dependent pytest failures remain outside this task.

Next recommended task: Triage the 18 dependency packages flagged by pip-audit and prioritize compatible remediation.
