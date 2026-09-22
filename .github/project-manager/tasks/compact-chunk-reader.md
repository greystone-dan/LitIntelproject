# Task: Compact Chunk Reader

Status: complete
Created: 2026-09-22
Updated: 2026-09-22

## Task Record

Task: Make chunk view visually continuous and compact by removing visible chunk numbering and character counts, reducing inter-chunk card treatment, and keeping inline statute/case references at the surrounding text size.

Why now: The active reader currently spends excessive vertical space on chunk chrome and makes highlighted legal references look typographically smaller than the judgment text.

Owner surface: `backend/pages/data_explorer.py` inline reader chunk rendering and styles.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing reader-data payload, citation/statute evidence spans, `tests/test_feature_tabs.py`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/6.maiixtsw.sw.md`.

Risk boundary: Presentation-only. Preserve chunk DOM boundaries, ordering, text, backend offsets, evidence attributes, linked-authority behavior, full-text mode, and reader navigation. No database, extraction, or API changes.

Smallest falsifiable check: `& '.\\venv\\Scripts\\python.exe' -m pytest tests/test_feature_tabs.py -q`

Acceptance criteria:

- Chunk view no longer displays chunk labels, ordinal fallback text, chunk-set labels, or character counts.
- Chunk sections use subtle separators and tighter spacing rather than large independent cards.
- Inline case citations and statute references inherit the surrounding judgment font size and line height.
- Stored text, evidence spans, data attributes, links, and chunk ordering remain unchanged.
- Focused tests, compilation, and a browser screenshot/evidence check pass.
- Canonical UI documentation and the active Swimm walkthrough describe the presentation contract.

Docs/generated references: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`; no generated references expected.

Rollback/recovery: Revert only the reader chunk markup/style, focused test, and documentation changes; no data recovery required.

Evidence:

- Files changed: `backend/pages/data_explorer.py`, `tests/test_feature_tabs.py`, `docs/RESEARCH_UI_GUIDE.md`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/6.maiixtsw.sw.md`, and this task record.
- Delegated work: Explore agent completed a bounded read-only audit of chunk rendering, typography CSS, focused tests, and documentation. No delegated files changed.
- Focused validation: `& '.\\venv\\Scripts\\python.exe' -m pytest tests/test_feature_tabs.py -q` passed 17 tests after the implementation.
- Compilation: `& '.\\venv\\Scripts\\python.exe' -m py_compile backend/pages/data_explorer.py` passed with the existing invalid-escape warning.
- Browser validation: Playwright opened the B010 reader and found 41 preserved `.chunk-panel` elements, zero visible `.chunk-header` elements, no visible `Chunk <number>` or `<number> chars` text, and zero inter-panel gap. The first chunk had transparent background, zero radius, no card border, and `7px 3px` body padding.
- Evidence/typography validation: 111 citation and 155 statute highlights remained. Both computed to `15px` font size and `23.7px` line height, matching their enclosing chunk body; 460 `data-authority` elements remained present. No console/page errors or failed responses occurred.
- Visual inspection: `%TEMP%\\compact-chunk-reader.png` showed a continuous source-decision reading surface with subtle separators and unchanged evidence colors.
- Canonical documentation: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, and `docs/RESEARCH_UI_GUIDE.md`.
- Swimm walkthrough: `.swm/6.maiixtsw.sw.md`.

## Hypothesis

If the chunk header is removed while article boundaries remain and inline reference styles inherit typography, browser validation will show a denser continuous judgment with no visible chunk/character labels and equal body/reference font sizes without losing evidence elements.

## Plan

1. Remove presentation-only chunk headers and compact the chunk container CSS.
2. Normalize citation/statute typography and add focused source-contract assertions.
3. Refresh and browser-check chunk boundaries, evidence counts, font sizes, and responsive rendering; then update documentation.

## Execution Checkpoints

- Delegation: Explore agent completed a bounded read-only audit of chunk markup, CSS, tests, and documentation; no files changed.
- Implementation: Completed in `backend/pages/data_explorer.py` with focused assertions in `tests/test_feature_tabs.py`.
- Documentation: Completed in `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/6.maiixtsw.sw.md`.
- Recovery: No long-running or data-writing operation planned.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-22 | Preserve article boundaries but remove visible headers | Maintains DOM/evidence grouping while reducing chrome and hiding implementation metadata | Owner-file audit |
| 2026-09-22 | Apply inherited typography to both case and statute references | Both are inline judgment evidence and should not alter reading size or line rhythm | CSS audit |

## Completion

Completion recorded: yes

Summary: Chunk view now reads as a compact continuous judgment without visible implementation numbering or character counts, and legal references retain surrounding typography.

Validation: Focused tests, compilation, browser DOM/style/evidence checks, screenshot review, and final diff validation.

Residual risk: The hidden chunk header remains in the generated DOM for a minimal presentation-only change, but `display:none` removes it from visual and accessibility presentation. Linked-context click behavior was not exercised in the B010 check because no rendered linked citation was available in that sample; the linked citation element and event wiring were unchanged.

Next recommended task: None for this request; keep any broader reader-density changes separate and browser-validated.
