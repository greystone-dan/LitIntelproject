# Task: Document current CI, data model, and pipeline

Status: blocked
Created: 2026-10-24
Updated: 2026-10-24

## Task Record

Task: Implement issue #662 as a documentation-only correction and add the requested data dictionary and plain-language pipeline guide.

Why now: Existing CI and corpus language can mislead contributors; the data model and decision-enrichment steps need accessible, source-backed explanations.

Owner surface: Contributor and data-flow documentation.

Commit allowed: yes

Push allowed: yes

Dependencies: `backend/database.py`, `backend/models.py`, `alembic/versions/`, pipeline modules/scripts, `.github/workflows/tests.yml`, existing canonical docs, and Swimm walkthroughs.

Risk boundary: Documentation files only; preserve unrelated changes; do not alter CLAUDE.md Hard rules or other content, generated docs, code, tests, configuration, or requirements.

Smallest falsifiable check: Compare the revised CI note with `.github/workflows/tests.yml`, then run focused documentation checks and `git diff --check`.

Acceptance criteria:

- CLAUDE.md Run and test note matches the distinct pytest and migrations CI jobs; Hard rules and other content remain untouched.
- Any corrected scope/total statements in README.md or SYSTEM_REFERENCE.md use only repository sources and plainly distinguish FC/SCC/FCA working scope from a total that includes RPD/RAD.
- `docs/DATA_DICTIONARY.md` covers each main DB table with meaning, key columns, pipeline-fill step, and explicit `not determined` where unsupported by sources.
- `docs/PIPELINE_PLAIN.md` names source steps/modules, splitting, citation finding, outcome labeling, tagging, and search building, and accurately explains AI use.
- Relevant canonical documentation and Swimm walkthrough links are updated without editing generated docs.
- Focused documentation validation, secret scan, CodeQL attempt, and `git diff --check` are recorded honestly.

Harness criteria: CI note verified against workflow; dictionary source traceability checked; pipeline module names verified; documentation validation and `git diff --check` passed.

Docs/generated references: `README.md`, `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `CLAUDE.md`, `.swm/` pipeline/database walkthroughs; do not hand-edit generated references.

Rollback/recovery: Revert only this task's documentation edits; preserve any pre-existing worktree changes.

Evidence: Worktree was clean initially. Read `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`, `OVERNIGHT.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, and relevant database, ingestion, citation, and search Swimm walkthroughs. Verified `.github/workflows/tests.yml`: `pytest` has no `--deselect` and no Postgres service; `migrations` has Postgres. Added and reviewed the requested docs, updated the canonical index and the database/ingestion Swimm maps. The final dictionary has 57 unique entities, each with its own column/meaning table and fill note. Focused source/path/wording checks, changed-file secret scan, and `git diff --check` passed. `python scripts/check_generated_docs.py` was attempted but its API/schema generators could not import missing `fastapi` and `sqlalchemy`. CodeQL was attempted but the CLI is unavailable; `gh extension list` could not run without `GH_TOKEN`. A broad local-link scan also found an existing unrelated broken `.swm/2.40nypbay.sw.md` link to `../backend/vector_tables.py`; the new links resolve and the existing link was left untouched. One supplemental shell `grep` command failed because of an unmatched quoting delimiter; the equivalent Python structural check passed.

Files changed: `.github/project-manager/tasks/issue-662-docs.md`, `CLAUDE.md`, `README.md`, `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `docs/DATA_DICTIONARY.md`, `docs/PIPELINE_PLAIN.md`, `.swm/2.40nypbay.sw.md`, `.swm/3.sl0qpkcv.sw.md`.
Delegated work: `managed-worker` created `docs/DATA_DICTIONARY.md` with 49 ORM tables plus 8 contextual tables from migration `0026`, reporting source/path/format checks and fill uncertainty for `citation_paragraph_links`, `fc_activity_alerts`, contextual tables, and a separate `recent_case_chunk_embeddings` refresh. After its first completion, a second bounded `managed-worker` pass reformatted the same file into one column/meaning table per entity, preserving the entries.
Focused validation: Passing: CI note/workflow cross-check; court-scope/total wording check; pipeline source-path and local-link checks; dictionary structure check (57 unique entities, each with a column table and pipeline-fill note) and 45 source references; new Swimm links; changed-file secret-pattern scan; `git diff --check`. Blocked: `python scripts/check_generated_docs.py` (missing `fastapi`/`sqlalchemy` imports); CodeQL (CLI unavailable and no authenticated GitHub extension context). No tests, regeneration, or database operations run.
Residual risk: Generated-document consistency and CodeQL could not be completed in this environment. The task is documentation-only and did not modify generated docs. The broad link scan found the pre-existing `.swm/2.40nypbay.sw.md` reference to missing `backend/vector_tables.py`; no new link is affected.
Next bounded task: Re-run `python scripts/check_generated_docs.py` and CodeQL in an environment with the project dependencies and CodeQL tooling, then review/close this task.

## Hypothesis

If the docs are corrected from their implementation/workflow sources, a focused text/source cross-check and documentation validation will demonstrate that users are not told CI deselects tests or confuse the working court scope with the wider decision total.

## Plan

1. Read authoritative repository docs and relevant Swimm walkthroughs; verify source claims.
2. Delegate the database dictionary to one documentation-file owner; make the remaining docs updates.
3. Validate all claims against sources, scan changed documents, and review the diff.

## Execution Checkpoints

- Delegation: `managed-worker` created `docs/DATA_DICTIONARY.md` only; structured result received.
- Implementation: `CLAUDE.md`, `README.md`, `SYSTEM_REFERENCE.md`, and `docs/PIPELINE_PLAIN.md`; focused checks passed.
- Documentation: `DOCS_INDEX.md`, `SYSTEM_REFERENCE.md`, `README.md`; Swimm `.swm/2.40nypbay.sw.md` and `.swm/3.sl0qpkcv.sw.md`.
- Recovery: Not applicable; no long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-24 | Task created | Issue #662 requests several coordinated documentation updates, with strict doc-only scope. | Clean starting `git status --short`; docs/workflow/Swimm references inspected. |
| 2026-10-24 | Marked blocked after implementation | Required broad checks could not run in the available environment. | Generated-doc check lacks `fastapi`/`sqlalchemy`; CodeQL CLI unavailable. |

## Completion

Completion recorded: no

Summary: Documentation changes are implemented and focused checks pass; task remains blocked on unavailable generated-doc dependencies and CodeQL.

Validation: See focused validation evidence above; no tests or regeneration run.

Residual risk: CodeQL and generated-reference consistency remain unverified.

Next recommended task: Re-run the blocked checks in a provisioned environment, then close the task if they pass.
