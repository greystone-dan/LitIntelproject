# Task: Resolve documentation integrity issues from #432

Status: blocked
Created: 2026-10-09
Updated: 2026-10-09

## Task Record

Task: Repair broken relative documentation links/references, index all hand-written `docs/` Markdown files, and align deployment/recovery guidance with the current Windows `iLitSite` scheduled-task procedure.

Why now: Issue #432 identifies stale or broken operator and document navigation guidance that undermines reliable use of repository documentation.

Owner surface: Hand-written repository documentation (`docs/`, `DOCS_INDEX.md`, and the documentation Swimm map).

Commit allowed: no

Push allowed: no

Dependencies: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `CLAUDE.md` (read-only deployment facts), `.swm/8.upryk5h6.sw.md`, and repository documentation contracts.

Risk boundary: Documentation-only. Do not access the database, `.env`, or live site; do not edit `*.generated.md`, delete documents, change tour or Coming soon content, or perform deployment actions. Keep `scripts\refresh_site.ps1` only as a fallback when the scheduled task is removed.

Smallest falsifiable check: `python -m pytest -q tests/test_documentation_contracts.py`.

Acceptance criteria:

- Every hand-written Markdown document under `docs/` is listed in `DOCS_INDEX.md` with a one-line description; generated Markdown outputs are not manually changed.
- Broken relative links/references in the scoped hand-written docs are repaired; clearly superseded docs are marked at the top and retained.
- Deployment/recovery guidance consistently names Windows scheduled task `iLitSite` as the primary procedure and `scripts\refresh_site.ps1` as fallback only.
- Documentation contracts, `python scripts/check_generated_docs.py`, local-link review, and `git diff --check` pass.
- The relevant Swimm operations walkthrough and canonical repository documentation are updated in the same checkpoint.

Harness criteria:

- Documentation integrity requirements pass focused documentation-contract tests.
- Generated-document check and local-link review pass without generated-file edits.

Docs/generated references: `DOCS_INDEX.md`; relevant deployment/recovery docs under `docs/`; `.swm/8.upryk5h6.sw.md`; generated references remain generator-owned and unchanged.

Rollback/recovery: Revert only this task's documentation/task-record edits; preserve unrelated worktree changes. Recheck `git diff --check` and focused documentation tests after any repair.

Evidence: Delegated documentation audit/edits completed by the managed-worker. The worker audited 65 authored Markdown docs (generated Markdown excluded), repaired broken local targets, updated deployment guidance, marked retained historical docs as superseded, and reported its local-link audit and `git diff --check` passing. Manager verified the index lists all 67 hand-written Markdown/text documents (generated outputs excluded), independently checked relative Markdown targets in 67 docs/index/Swimm files (0 missing), and ran `git diff --check` successfully. `python scripts/check_generated_docs.py` was attempted but generator imports failed because `fastapi` and `sqlalchemy` are unavailable. The requested `python -m pytest -q tests/test_documentation_contracts.py` was attempted and could not start because `pytest` is unavailable. No database, `.env`, or live site was accessed.

Files changed: `DOCS_INDEX.md`; `.swm/8.upryk5h6.sw.md`; `docs/CLOUDFLARE_TUNNEL_SETUP.md`; `docs/DEPLOYMENT_COMMANDS.md`; `docs/LOCAL_DEPLOYMENT_SETUP.md`; `docs/OPERATIONAL_RECOVERY_GUIDE.md`; `docs/SITE_RECOVERY.md`; `docs/history/AI_HANDOFF.md`; `docs/history/AI_HANDOFF_2026-09-02_root.md`; `docs/history/AI_STAGE_SUMMARY_2026-07-31.md`; `docs/history/FC_CITATION_REBUILD_IMPLEMENTATION.md`; `docs/history/FORMATTING_IMPROVEMENTS.md`; `docs/history/PROJECT_NOTES.md`; this task record.
Delegated work: Managed-worker audited and updated hand-written docs under `docs/` only, excluding generated outputs and protected tour/Coming soon content. Structured return reported 65 Markdown files inspected, 11 docs files changed, nine broken local targets repaired, final link target audit clean, and `git diff --check` passing. Initial audit command had a quoting-related Python syntax error and was corrected.
Focused validation: Passed — index coverage script (67 authored Markdown/text docs); local Markdown target audit (67 files, 0 missing targets); `git diff --check`. Blocked — `python scripts/check_generated_docs.py` (missing `fastapi`, `sqlalchemy`); requested `python -m pytest -q tests/test_documentation_contracts.py` (missing `pytest`).
Residual risk: Repository test and generated-reference checks remain unverified in this environment because required Python dependencies are absent. The tests conftest also attempts a PostgreSQL availability probe; no database was accessed, consistent with the task boundary.
Next bounded task: Run the two requested checks in a provisioned test environment while preventing database access during pytest collection.

## Hypothesis

If scoped hand-written docs are reconciled against repository targets and the current `iLitSite` runbook, the link/reference audit and documentation checks will show no dangling local references or conflicting primary deployment procedures.

## Plan

1. Delegate bounded audit and edits of hand-written docs, excluding generated outputs and tour/Coming soon content.
2. Complete the docs index and relevant Swimm walkthrough; review the resulting changes.
3. Run requested checks and a local-link review, then record evidence and residual risk.

## Execution Checkpoints

- Delegation: Managed-worker returned structured findings and implemented scoped documentation edits; details recorded above.
- Implementation: Reconciled operational docs to the current scheduled-task workflow and repaired broken links.
- Documentation: Updated `DOCS_INDEX.md` and `.swm/8.upryk5h6.sw.md`.
- Recovery: Not applicable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-09 | Task created | Issue #432 requests a bounded docs-only cleanup with explicit deployment constraints. | User request and repository task template |
| 2026-10-09 | Implementation completed; validation blocked | Documentation checks could not start because the environment lacks pytest, FastAPI, and SQLAlchemy. | Manager link/index checks passed; requested commands' import failures recorded above |

## Completion

Completion recorded: no

Summary: Requested documentation edits and static audits completed; repository test and generated-reference checks remain blocked by missing dependencies.

Validation: Index coverage, local-link audit, and `git diff --check` passed. Requested generated-doc and pytest commands were attempted but could not run.

Residual risk: No test-suite or generator result is available. No database/live-site operations were performed.

Next recommended task: Re-run generated-doc and documentation-contract checks in a provisioned environment that does not access PostgreSQL.
