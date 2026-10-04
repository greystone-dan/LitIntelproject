# Task: Centralize database and AI settings

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add a stdlib grouped settings object; preserve defaults and names while migrating database and AI reads, and make process environment values outrank dotenv.

Why now: Issue #186 documents inconsistent configuration ownership and dotenv overriding exported environment values.

Owner surface: Backend configuration boundary (`backend/settings.py`, database, and AI consumers).

Commit allowed: yes

Push allowed: yes

Dependencies: Latest `main` integrated; retain existing dependencies and defaults.

Risk boundary: Do not read or change `.env`/`backend/.env`, use the live database, alter deploy scripts, change setting names/defaults, or migrate non-database/non-AI callsites.

Smallest falsifiable check: Focused settings tests prove exported values beat dotenv and database URL selection retains existing precedence/defaults.

Acceptance criteria:

- Grouped settings cover app, database, embedding, chat, audit, and access configuration using stdlib/existing dependencies.
- Database and AI runtime consumers use the settings object; other consumers remain unmigrated and are inventoried.
- Environment beats dotenv; setting names/defaults and current `.env` behavior remain compatible.
- `.env.example`, `config.yaml` assessment, configuration reference, architecture inventory, Swimm walkthrough, and changelog are updated accurately.
- Focused tests and documentation checks pass; diff has no secrets or prohibited file changes.

Harness criteria: Settings groups preserve defaults; process environment beats dotenv; focused tests pass; required docs updated.

Docs/generated references: `docs/CONFIGURATION_REFERENCE.md`, `docs/ARCHITECTURE.md`, `.swm/2.40nypbay.sw.md`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`; generated docs check.

Rollback/recovery: Revert the scoped settings/code/docs/test changes; no database mutation or migration is involved.

Evidence: Issue #186 and linked issue #112 Rules block read from GitHub HTML; `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`, `OVERNIGHT.md`, configuration reference, and database walkthrough reviewed. Initial `git pull --ff-only origin main` could not fast-forward; merged fetched `main` (`d5efc31`). A final fetch confirmed that same main commit is an ancestor of the issue branch. Delegated implementation and recovery returned structured results; no live DB, `.env`, or deploy script was used/changed. Updated canonical documents `docs/CONFIGURATION_REFERENCE.md`, `docs/ARCHITECTURE.md`, `SYSTEM_REFERENCE.md`, and `CHANGELOG.md`, plus Swimm walkthrough `.swm/2.40nypbay.sw.md`.

Files changed: `.env.example`; `.swm/2.40nypbay.sw.md`; `CHANGELOG.md`; `SYSTEM_REFERENCE.md`; `backend/settings.py`; `backend/database.py`; `backend/embedding_providers.py`; `backend/routes.py`; `backend/search_service.py`; `backend/text_generation_providers.py`; `config.yaml`; `docs/API_REFERENCE.generated.md`; `docs/ARCHITECTURE.md`; `docs/CONFIGURATION_REFERENCE.md`; `tests/test_database_config.py`; `tests/test_embedding_settings.py`; `tests/test_text_generation_providers.py`; `tests/test_text_generation_settings.py`; this task record.
Delegated work: Managed workers implemented database/settings and AI-consumer migrations; follow-ups preserved dotenv file precedence, restored test harness behavior, retained functional research-route coverage, and preserved existing `OPENAI_ORG_ID` suppression. Structured results recorded.
Focused validation: `PYTHONPATH=. pytest --noconftest -q tests/test_database_config.py tests/test_text_generation_settings.py tests/test_text_generation_providers.py tests/test_embedding_settings.py` — 16 passed. After the final embedding compatibility adjustment, `PYTHONPATH=. pytest -q tests/test_embedding_settings.py` — 4 passed. `python scripts/generate_api_reference.py` and `python scripts/embed_documentation_appendices.py` completed; `python scripts/check_generated_docs.py` — generated documentation current (3 references checked); `git diff --check` passed; changed documentation targets were present.
Residual risk: Other direct environment consumers remain intentionally unmigrated and are inventoried in `docs/CONFIGURATION_REFERENCE.md`. Full suite was not run; focused tests used `--noconftest` to avoid the tracked conftest's live PostgreSQL probe. The generated API reference was refreshed to reconcile upstream drift; no route contract changed.
Next bounded task: Migrate one remaining configuration group (access/audit or source/security) with focused behavior tests.

## Hypothesis

If database and AI callsites read one grouped settings object, focused tests will show unchanged defaults and precedence except that real process environment variables now win over dotenv.

## Plan

1. Integrate fetched latest `main` and confirm repository invariants (done).
2. Implement grouped settings, dotenv precedence, database/AI migration, and focused test.
3. Align configuration templates/docs, architecture inventory, Swimm, and changelog.
4. Run focused and documentation checks; inspect the final diff and secret/file boundaries.

## Execution Checkpoints

- Delegation: Managed-worker implementation and bounded repair/validation slices completed with structured returns.
- Implementation: Added grouped settings, preserved database selection and AI provider behavior, and migrated database plus active AI consumers.
- Documentation: Refreshed configuration reference, architecture inventory, changelog, system reference appendix, env example, config assessment, and database Swimm walkthrough.
- Recovery: Not applicable; no long operation or database write.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Use stdlib and preserve existing defaults; migrate only database and AI reads | Issue #186 explicitly forbids a dependency and scopes the incremental migration | Issue #186 description |
| 2026-10-04 | Merge fetched `main` instead of retrying a fast-forward | Branch has an issue-specific commit and diverged from latest `main`; merge preserved both histories without conflicts | `git merge --no-edit FETCH_HEAD` succeeded |

## Completion

Completion recorded: yes

Summary: Added stdlib grouped settings with environment-over-dotenv precedence, migrated database and active AI reads, aligned templates/docs, and regenerated the API/system-reference documentation.

Validation: Focused settings tests passed (16; final embedding compatibility test 4 passed); generated documentation check passed (3 references); diff whitespace check passed.

Residual risk: Remaining direct environment consumers are documented; no full suite or database test was run.

Next recommended task: Migrate one remaining configuration group under a separate bounded task.
