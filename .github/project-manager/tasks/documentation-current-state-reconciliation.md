# Task: Reconcile current-state reference documentation

Status: complete
Created: 2026-09-22
Updated: 2026-09-22

## Task Record

Task: Review and update the canonical reference documentation so completed work and current product behavior are captured consistently.

Why now: The active UI navigation changed after the reference docs were last updated, and the user requested a current-state reconciliation across the reference set.

Owner surface: Repository documentation authority: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `OVERNIGHT.md`, `CHANGELOG.md`, and the relevant Swimm walkthroughs.

Dependencies: Completed project-manager task records, current page builder/routes, generated-document checks, and the delegated documentation inventory.

Risk boundary: Documentation only. Do not alter generated references by hand, code behavior, data, schema, production operations, or deferred product priorities.

Smallest falsifiable check: Search the authoritative documents for the current visible tab set, retired Data Explorer references, completed task outcomes, and stale dates; validate with `git diff --check` and the documentation consistency checker.

Acceptance criteria:

- Canonical docs describe the current visible product shell and compatibility boundaries.
- Completed work that materially changes current behavior is represented in the appropriate authority document.
- Stale or unsupported current-state claims are corrected or explicitly marked historical/deferred.
- Relevant Swimm walkthrough and canonical repository documents are updated together.
- Focused documentation validation passes.

Docs/generated references: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `OVERNIGHT.md`, `CHANGELOG.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`, and relevant task records. Generated API/schema/script catalogs remain outputs.

Rollback/recovery: Revert only the documentation changes from this task; preserve unrelated worktree changes and generated outputs.

Commit allowed: yes
Push allowed: yes

Delegated work: Explore agent performed a read-only bounded inventory of authority docs, ingestion/current-state surfaces, and completed work evidence. Manager retains implementation, documentation acceptance, and final validation.

Hypothesis: If current-state claims are reconciled against the active page builder, routes, completed task records, and changelog rather than copied forward from older snapshots, the reference set will stop contradicting the current product shell while preserving deferred and historical boundaries.

Evidence:

- Updated `SYSTEM_REFERENCE.md` to describe the seven visible tabs, retired
	visible Data Explorer and Judge Outcomes surfaces, and the historical judge
	audit boundary; regenerated all embedded appendices from their maintained
	sources.
- Updated `DOCS_INDEX.md` and `docs/RESEARCH_UI_GUIDE.md` to the seven-tab
	current shell and removed the retired Judge outcomes row.
- Updated `.swm/6.maiixtsw.sw.md` with the same current-shell checkpoint.
- Added verified Unreleased changelog entries for the deterministic case
	summary, Judge Outcomes retirement, and read-only judge reconciliation.
- Regenerated `docs/API_REFERENCE.generated.md` with its approved generator.
- Delegation: the first broad inventory response was rejected as unrelated;
	the second bounded Explore inventory supplied the stale-claim findings.
- Validation: `scripts/embed_documentation_appendices.py` passed;
	`scripts/generate_api_reference.py --output docs/API_REFERENCE.generated.md`
	passed; `pytest tests/test_feature_tabs.py -q` passed (15 passed, 1 warning);
	`git diff --check` passed.
- `scripts/check_generated_docs.py` still reports the pre-existing U+FEFF BOM
	in `scripts/run_treatment_teacher_batch.py`; that leading BOM was removed,
	`docs/SCRIPT_CATALOG.generated.md` was regenerated, and the checker now
	passes. API reference drift was also regenerated and resolved.
- Canonical repository docs updated: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`,
	`docs/RESEARCH_UI_GUIDE.md`, and `CHANGELOG.md`. Swimm updated:
	`.swm/6.maiixtsw.sw.md`.
- Residual risk: one cryptography deprecation warning remains in the focused
	test output. No browser validation or database work was run for this
	documentation-only task.
