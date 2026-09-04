# Task: Validate SCC Source-Link HTML Acquisition And HTML-Assisted Chunking

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Verify that SCC source links follow the same shell-page pattern as FC/FCA, reacquire valid decision HTML for missing cases, and measure the resulting HTML-assisted chunking structure without assuming FC-style sections.
Why now: The FC/FCA pattern showed that the official item URL can be a shell while the real decision body sits behind a second decision-body URL. SCC must be tested the same way before scaling any source reacquisition or chunk rebuild.
Owner surface: `scripts/reacquire_source_html.py`, `backend/document_structure.py`, `scripts/chunk_cases.py`
Dependencies: Curated SCC cases, existing source HTML sanitization and mapping tools, task 028 cross-court HTML matrix, source-specific SCC parser logic
Risk boundary: Keep reacquisition bounded to a small sample and preserve the existing FC/FCA thresholds; do not broaden to activity/submissions or bulk SQL writes.
Smallest falsifiable check: Reacquire a small set of SCC cases with no stored HTML and run HTML-assisted chunking on the resulting sample.
Acceptance criteria:

- A bounded SCC sample with no stored HTML can be reacquired from the source links using the same shell-page pattern as FC/FCA.
- The reacquirer validates the page before storing it and rejects shell/challenge pages.
- HTML-assisted chunking produces structured sections and paragraphs without assuming FC/FCA section layouts.
- No bulk acquisition or global threshold change occurs without a separate acceptance check.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, task 028, Swimm architecture walkthroughs
Rollback/recovery: Remove only the newly applied HTML records for the bounded SCC sample and revert any temporary chunk rebuilds in that sample set; no bulk rollback required.
Evidence: A 10-case SCC sample with no stored HTML was reacquired via the source-link pattern; all 10 returned `status=applied reason=valid-html` in the bounded validation. The resulting HTML-assisted chunking produced 1 full-case chunk per case plus section/paragraph layers; sections varied from 2 to 7, and labels included `Intro Metadata`, `Facts`, `Legislation`, `Issues`, `Analysis`, `Conclusion`, `Overview`, `Background`, and `Decision Content`. This confirms SCC is structurally variable, but source HTML is available and the HTML-assisted path is viable. FC/FCA thresholds were not weakened.

## Hypothesis

If the SCC source-link pattern behaves like FC/FCA and the HTML-assisted chunker is source-aware, then a bounded SCC sample with missing HTML will acquire valid decision HTML and produce structured section/paragraph layers without assuming FC/FCA layouts.

## Plan

1. Identify SCC cases with no stored HTML.
2. Reacquire a bounded sample via the source-link pattern.
3. Validate each snapshot before storing.
4. Run HTML-assisted chunking on the reacquired sample.
5. Compare section labels and chunk counts against FC/FCA assumptions.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-04 | Keep SCC acquisition bounded and source-link-driven | FC/FCA shell-page precedent and user requirement to avoid bulk scope | Verified 10/10 SCC sample cases acquired valid HTML |

## Completion

Status: complete
Summary: Source-link HTML reacquisition for SCC works in bounded samples, and the HTML-assisted chunking method yields meaningful structure without imposing FC/FCA assumptions.
Validation: Ran the bounded SCC reacquisition on 10 cases with no stored HTML; each returned `status=applied reason=valid-html`. Ran the HTML-assisted chunking pass on those same cases; all produced full-case chunks and varied section/paragraph layouts with labels such as `Facts`, `Overview`, `Analysis`, and `Decision Content`.
Residual risk: SCC still shows structural variance across decisions; more samples are needed before broad cohort scaling, but the gap is now measured rather than guessed.
Next recommended task: Expand to a second small SCC batch only after confirming the same pattern remains stable; keep activity/history/submissions out of scope.
