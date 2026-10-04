# Task: Version prompt text and report prompt versions

Status: blocked pending focused pytest validation
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Move the requested backend and script prompts into versioned text files, serve them through a registry, and expose versions in outputs.

Why now: Issue #189 requires reproducible prompt provenance without changing existing prompt wording or default behavior.

Owner surface: Prompt definitions and consumers (`backend/prompts/`, `backend/prompt_registry.py`, and the named route/scripts).

Commit allowed: yes

Push allowed: yes

Dependencies: Existing prompt definitions, API response tests, generated API documentation generator, and relevant Swimm walkthrough.

Risk boundary: Preserve exact prompt text and current behavior; only add the `prompt_version` output field. Do not access databases, deploy, read or write `.env`, add dependencies, or touch unrelated scripts.

Smallest falsifiable check: Golden prompt tests and focused `/research` response validation.

Acceptance criteria:

- Every in-scope prompt is in a versioned file and resolved by `backend/prompt_registry.py` returning `(text, version)`.
- Golden tests prove prompt bytes match existing text; `/research` and both script output formats include `prompt_version`.
- Relevant canonical docs and Swimm walkthrough are updated, generated API docs are refreshed from their generator, and focused checks pass.

Harness criteria: Prompt golden fixtures pass; research response version test passes; script prompt/output tests pass; generated docs check passes.

Docs/generated references: `docs/ARCHITECTURE.md`, `SYSTEM_REFERENCE.md`, relevant API generated docs via generator, and the relevant `.swm/` walkthrough.

Rollback/recovery: Revert only the prompt-file/registry consumer changes and documentation; no database or external state is involved.

Evidence: A managed-worker completed the requested read-only inventory of route, citation, teacher, and script prompt sources, focused tests, generator, and Swimm map; it changed no files. All nine migrated prompt texts and the interpolated contextual citation prompt matched baseline SHA-256 snapshots (`v1`). Mocked script-output checks passed without database or network access. Python compilation, backend inventory/link checks, and a local secret-pattern scan passed. `git diff --check` flags seven prompt-file lines with intentional trailing spaces; these spaces are part of the exact baseline prompt text verified by the golden hashes and must not be trimmed. After installing the repository-pinned runtime packages needed by the generators, `PYTHON_DOTENV_DISABLED=1 python scripts/generate_api_reference.py` regenerated the API reference and `PYTHON_DOTENV_DISABLED=1 python scripts/check_generated_docs.py` passed all three generated references. No generated reference was hand-edited. Focused pytest was not run after the custom implementation agent completed its work, and runtime `/research` behavior remains unverified. Latest `origin/main` was fetched before final validation and is an ancestor of HEAD. Canonical docs updated: `docs/ARCHITECTURE.md`, `SYSTEM_REFERENCE.md`, and `CHANGELOG.md`; Swimm walkthrough updated: `.swm/1.oi7rhqp2.sw.md`.

Files changed: Task record; `.swm/1.oi7rhqp2.sw.md`; `CHANGELOG.md`; `SYSTEM_REFERENCE.md`; `docs/ARCHITECTURE.md`; `backend/prompt_registry.py`; nine files under `backend/prompts/`; `backend/routes.py`; `backend/models.py`; `backend/citation_intelligence_prompts.py`; `backend/contextual_authority/teacher_contract.py`; `scripts/run_model_paragraph_experiment.py`; `scripts/package_discussion_units_llm.py`; `tests/test_prompt_registry.py`; `tests/test_text_generation_providers.py`; `tests/test_package_discussion_units_llm.py`.
Delegated work: `prompt-source-inventory` (managed-worker), read-only source/test/docs inventory; exact prompt source locations, existing tests, output caveat, generated-doc command, and relevant walkthrough returned; no files changed. Its initial `rg` search was unavailable and it continued with `grep`/`find`.
Focused validation: Python compilation; exact-prompt SHA-256 checks (8 static snapshots plus the dynamic citation snapshot); API response AST contract; architecture inventory and Swimm local links; mocked script JSON/Markdown outputs; local secret-pattern scan; API-reference generation; and `scripts/check_generated_docs.py` passed. `git diff --check` reports seven intentional trailing spaces in prompt files (see evidence above). Focused pytest was not run after the custom implementation agent completed its work.
Residual risk: Focused pytest and runtime `/research` behavior remain unverified. No DB, deployment, `.env`, or external model operations were performed.
Next bounded task: Run the focused pytest command in a dependency-equipped environment.

## Hypothesis

If prompt extraction is correct, exact-text golden tests will prove every migrated prompt is byte-identical and focused output tests will observe its version.

## Plan

1. Inventory the authoritative prompt text, nearby tests, documentation generator, and relevant walkthrough.
2. Add versioned prompt files/registry, migrate only requested consumers, and create exact-text/output tests.
3. Regenerate API documentation, update canonical docs and Swimm, then run focused checks and final safety verification.

## Execution Checkpoints

- Delegation: Completed bounded source inventory.
- Implementation: Versioned prompts and consumers implemented; static and mocked artifact checks passed.
- Documentation: `docs/ARCHITECTURE.md`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, and `.swm/` walkthrough updated; API reference regenerated and generated-doc check passed.
- Recovery: Not applicable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | Issue #189 is a multi-file implementation with code, tests, and documentation requirements. | User request; `origin/main` is an ancestor of HEAD after fetch. |
| 2026-10-04 | Added versioned prompt sources and consumers | Preserved prompt wording and kept versions outside model-facing content; outputs expose prompt provenance additively. | Baseline snapshots and mocked script artifact checks passed. |
| 2026-10-04 | Regenerated API reference and checked generated docs | Runtime dependencies were installed in the sandbox without changing project dependencies. Focused pytest remains unverified. | API generator and `check_generated_docs.py` passed; no database or `.env` access. |

## Completion

Completion recorded: no

Summary: Implementation and canonical/Swimm documentation are in the worktree. Generated API docs were regenerated and the generated-doc check passed; task acceptance remains blocked on focused pytest validation.

Validation: Compilation, prompt snapshots, mocked script artifact checks, local documentation inventory/link checks, local secret-pattern scan, API-reference generation, and generated-doc check passed. Prompt files retain seven trailing spaces required for byte-identical prompt text. Focused pytest was not run after the custom implementation agent completed its work.

Residual risk: Focused pytest and runtime `/research` behavior remain unverified.

Next recommended task: Run the focused pytest command in a dependency-equipped environment.
