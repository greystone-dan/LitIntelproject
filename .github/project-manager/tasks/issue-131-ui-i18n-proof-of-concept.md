# Task: UI string inventory and French i18n proof of concept

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Inventory user-facing UI strings with human-readable and JSON reports, and demonstrate French localization on one page.

Why now: Issue #131 requests an evidence-backed inventory and a deliberately narrow localization proof of concept before any broader translation effort.

Owner surface: Generated research UI localization and string-inventory tooling.

Commit allowed: yes

Push allowed: yes

Dependencies: Active UI builders in `backend/pages/` and `backend/routes.py`; current UI tests and documentation.

Risk boundary: Keep localization limited to About unless an existing `/start` page is found; preserve default English behavior, routes, stored data, and evidence offsets. No database, deployment, or `.env` access.

Smallest falsifiable check: `python -m pytest tests/test_ui_string_inventory.py tests/test_feature_tabs.py -q`

Acceptance criteria:

- `scripts/inventory_ui_strings.py` generates `docs/reports/french-ui-inventory.md` and `docs/reports/ui-strings.json`.
- A single-page French proof of concept is available on About (or `/start` only if that route already exists), while English remains the default and the page language is set correctly.
- Focused tests cover inventory output and localization behavior without database access.
- `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and the Active Research UI Swimm walkthrough document the implemented behavior and its limits.
- Focused validation, prescribed full tests, generated-document check, changed-file secret scan, and `parallel_validation` are reported accurately.

Harness criteria:
- UI inventory has a reproducible JSON and readable report.
- French proof of concept is restricted to one page and preserves English default behavior.
- Required documentation and Swimm walkthrough are updated.
- Required validation commands and safety checks are recorded.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`; generated inventory report/JSON must come from its generator.

Rollback/recovery: Revert the bounded UI localization and inventory-tool changes together; no database or deployment state is involved.

Evidence: `/start` is absent, so About is the proof-of-concept page. The requested script and report paths are implemented. The English page output was compared with the pre-change builder and matched byte-for-byte; the French response has `lang="fr"`. Focused tests passed (60 passed, 1 skipped). Generated reports and generated-doc validation passed. The full CI-equivalent pytest run completed with 1,272 passed, 3 failed, 1 skipped, 1 xfailed, and 3 deselected; the three failures need network downloads from Hugging Face and OpenAI tokenizer storage, which DNS could not resolve here. GitHub Actions previously showed `action_required` for the draft PR and zero jobs, with no failed job logs. Canonical docs updated: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`; Swimm walkthrough updated: `.swm/6.maiixtsw.sw.md`.

Files changed: `.github/project-manager/tasks/issue-131-ui-i18n-proof-of-concept.md`, `.swm/6.maiixtsw.sw.md`, `SYSTEM_REFERENCE.md`, `backend/i18n.py`, `backend/pages/about_content.html`, `backend/pages/data_explorer.py`, `backend/routes.py`, `docs/API_REFERENCE.generated.md`, `docs/RESEARCH_UI_GUIDE.md`, `docs/SCRIPT_CATALOG.generated.md`, `docs/reports/french-ui-inventory.md`, `docs/reports/ui-strings.json`, `scripts/generate_script_catalog.py`, `scripts/inventory_ui_strings.py`, `tests/test_ui_string_inventory.py`.
Delegated work: The initial delegated implementation was corrected to the requested script/report paths and a catalog-backed About proof of concept. English catalog strings reproduce the original About text; only the French query localizes the selected strings and document language.
Focused validation: `python scripts/inventory_ui_strings.py --check`, `python scripts/check_generated_docs.py`, Python compilation, and `git diff --check` passed. Focused UI/localization tests passed (60 passed, 1 skipped). The script catalog was regenerated with `python scripts/generate_script_catalog.py`.
Residual risk: Three unrelated full-suite tests could not access remote model/tokenizer resources due DNS/network failure. Inventory extraction is static and cannot guarantee runtime completeness. French preview is intentionally limited to the About title/lead/three links and requires fluent-speaker review; legal terms are not final. The GitHub Actions workflows did not execute because the PR was draft (`action_required`).
Next bounded task: Re-run the three network-dependent tests and full suite from an environment with Hugging Face and OpenAI tokenizer-resource access before merge.

## Hypothesis

If the inventory and single-page language switch are implemented without changing the existing English default, focused tests will verify deterministic report/JSON output, the French About content, and unchanged navigation behavior.

## Plan

1. Inventory the active UI string sources and choose a reproducible report format.
2. Add the bounded About French localization proof of concept and focused tests.
3. Update the canonical UI docs and Swimm walkthrough, then run focused and required repository checks.

## Execution Checkpoints

- Delegation: Managed worker `issue-131-ui-i18n` implemented inventory, About language preview, and focused tests; manager accepted the bounded slice and corrected a documentation placement error.
- Implementation: Added deterministic static UI inventory generation, checked-in report/JSON outputs, a catalog-backed French About preview, and focused tests.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/6.maiixtsw.sw.md`; regenerated `docs/SCRIPT_CATALOG.generated.md`.
- Recovery: No persistent data or long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Use About as the proof-of-concept page | No `/start` route exists; About is the requested fallback. Translations stay limited to the title, lead, and three section links | `backend/routes.py`; `backend/pages/data_explorer.py` |
| 2026-10-04 | Keep task open pending the remote-resource tests | Three full-suite tests cannot resolve remote model/tokenizer resources in this environment | `python -m pytest -q` |

## Completion

Completion recorded: no

Summary: Implementation and required documentation are present; the CI-equivalent suite has three network-dependent failures.

Validation: Inventory freshness, compilation, focused UI tests, generated-document checks, and the final CodeQL scan (zero alerts) passed. The CI-equivalent full test run had three network-dependent failures.

Residual risk: Three network-dependent full-suite failures remain; see Evidence.

Next recommended task: Re-run the full suite where Hugging Face and tokenizer downloads are available.
