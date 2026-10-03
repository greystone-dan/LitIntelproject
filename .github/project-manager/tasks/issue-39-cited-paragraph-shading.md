# Task: Shade cited paragraphs in the case reader

Status: blocked
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Resolve issue #39 by subtly shading source paragraphs cited by other cases and showing a citation-count tooltip.

Why now: Paragraph citation visibility improves traceability from case text to citing authorities while reusing existing citation evidence.

Owner surface: Reader data formatting and inline case-reader rendering (`backend/reader_service.py`, `backend/case_formatter.py`) with focused reader tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing stored case-citation rows and reader response/rendering contract.

Risk boundary: Do not recompute or change stored offsets, invent browser offsets, change persistence/database/deployment behavior, or shade broad text when no reliable pinpoint is available. Do not alter unrelated worktree content.

Smallest falsifiable check: `python -m pytest tests/test_api.py -k reader -q`

Acceptance criteria:

- Incoming pinpoint citations produce subtle paragraph shading and a tooltip such as “Cited by 12 cases”.
- Paragraph mapping uses existing backend-owned evidence/structure and preserves persisted offsets.
- Cases without pinpoint citations degrade cleanly without fabricated paragraph shading or offsets.
- Focused tests cover incoming citation display and no-pinpoint behavior.
- Canonical docs and the active-reader Swimm walkthrough explain the behavior and offset boundary.
- Workflow-equivalent pytest suite, required focused checks, and changed-file secret scan complete with evidence.

Harness criteria:

- Focused reader tests pass.
- Full CI pytest command passes with the workflow’s three explicit deselections.
- Documentation and generated-source checks pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/6.maiixtsw.sw.md`; no generated references expected.

Rollback/recovery: Revert the reader formatter/rendering and corresponding tests/docs; no database mutation or migration is involved.

Evidence: The reader formats backend-owned paragraph metadata from stored incoming citations, counts distinct other source cases, and emits a subtle shade/tooltip only for mapped pinpoints. The initial worker query was corrected after manager review because active citation writers do not populate `Citation.target_paragraph` consistently; it now prefers that persisted field and falls back to the established pinpoint parser over stored citation text. No citation offsets, database data, schema, deployment scripts, or `.env` files were changed. Canonical documentation updated at `SYSTEM_REFERENCE.md` and `CHANGELOG.md`; Swimm walkthrough updated at `.swm/6.maiixtsw.sw.md`.

Files changed: `.github/project-manager/tasks/issue-39-cited-paragraph-shading.md`, `backend/reader_service.py`, `backend/case_formatter.py`, `backend/pages/data_explorer.py`, `tests/test_api.py`, `tests/test_case_formatter.py`, `tests/test_feature_tabs.py`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/6.maiixtsw.sw.md`.
Delegated work: `managed-worker` inspected reader/formatter/model/database/page/test files and implemented backend citation counts, formatter metadata, inline shading/tooltip rendering, and focused tests. Worker returned the required structured report; pytest was initially unavailable. Manager installed repository requirements, reviewed the diff, repaired pinpoint fallback behavior, and retained final validation.
Focused validation: `python -m pytest tests/test_api.py -k reader -q` — 7 passed, 48 deselected; `python -m pytest tests/test_case_formatter.py -q` — 10 passed; `python -m pytest tests/test_feature_tabs.py -q` — 51 passed. Headless Chromium executed the page's extracted `esc`, `highlightedDecision`, and `formattedDecision` functions with backend-style paragraph metadata and confirmed the shaded paragraph class plus `Cited by 12 cases` tooltip. `python scripts/check_generated_docs.py` — current (3 references); Python compilation, `git diff --check`, Swimm source-link checks, and changed-file secret scan passed.
Residual risk: The requested workflow-equivalent full suite did not pass in this network-restricted environment: 969 passed, 3 deselected, and 3 unrelated tests failed because Hugging Face and OpenAI tokenizer model assets could not be downloaded. No live database or full-page API browser session was used.
Next bounded task: Rerun the exact full-suite command in a network-enabled CI environment (or with the required model/tokenizer assets cached) before unblocking the task.

## Hypothesis

If incoming pinpoint citation evidence is safely projected onto existing reader paragraph ranges, focused reader tests will verify shading and a case-count tooltip while cases without pinpoint data remain unchanged.

## Plan

1. Delegate a bounded reader implementation and test slice.
2. Independently accept the implementation and run focused reader validation.
3. Update the canonical behavior reference and Swimm walkthrough.
4. Run the requested suite, required checks, and secret scan; record actual evidence.

## Execution Checkpoints

- Delegation: Assign worker to reader service/formatter behavior and focused tests only.
- Implementation: Reader code and tests changed; focused API, formatter, and feature-tab checks passed.
- Documentation: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, and `.swm/6.maiixtsw.sw.md` updated.
- Recovery: No long operation or database state.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Use existing citation evidence and paragraph structure only | Preserve backend offset ownership and avoid browser-side inference | Issue #39; current reader ownership in `SYSTEM_REFERENCE.md` and `.swm/6.maiixtsw.sw.md` |
| 2026-10-03 | Prefer stored target paragraph, with established citation-text fallback | The target paragraph column is not consistently populated by active citation writers; text fallback retains existing pinpoint behavior | Focused reader tests passed; full suite blocked by three external-asset network failures |
| 2026-10-03 | Preserve existing outgoing pinpoint preview behavior | The new stored-paragraph preference is needed only for incoming shading; keep the established outgoing text-derived behavior unchanged | Final focused reader/formatter/UI checks passed |

## Completion

Completion recorded: no

Summary: The issue behavior and documentation are implemented and focused checks pass; the task remains blocked because the required full suite has three network-dependent failures.

Validation: Focused reader tests passed (7 API, 10 formatter, 51 feature-tab). The workflow-equivalent suite ran with all three configured deselections: 969 passed, 3 deselected, 3 failed due unavailable Hugging Face/OpenAI tokenizer downloads.

Residual risk: Full-suite green evidence requires network-enabled CI or pre-cached model/tokenizer assets; full-page API/browser interaction was not exercised.

Next recommended task: Rerun the workflow-equivalent suite in a network-enabled environment.
