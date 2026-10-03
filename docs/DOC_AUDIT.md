# Documentation audit against current code

Audited against `origin/main` at `3d903767d22f09df1e69e49cb12b1e9c11a15af3`.
The checkout branch is `copilot/audit-docs-statements-contradicting-code` at
`9bd7f29`; a targeted diff confirmed the audited documents and cited
implementation paths are identical to that main commit. Statuses are limited to
substantive current-state claims; proposals and historical notes are not treated
as implemented behavior.

| File | Claim | Status | Evidence |
|---|---|---|---|
| `ROADMAP.md` | The “Active Corpus Rebuild Sequence” makes full-corpus processing the current priority before interface work (`184–190`). | contradicted | Current direction in `ROADMAP.md:7–23` is demo-first; `/` redirects to `/data-explorer` in `backend/main.py:88–90`, while the active page is served in `backend/routes.py:1075–1077`. |
| `docs/NEXT_STEPS.md` | Only the first 10 API validations ran: 9 complete, case 677 failed, and no later cases were attempted (`20–29`). | stale | The checked-in `data/eval/llm_discussion_units_pilot/core_300_run/ledger.json` records 20 cases (17 complete, 3 failed, including 2044 and 2220); `scripts/run_discussion_units_cohort.py:61–75` records completed and failed runs. |
| `docs/NEXT_STEPS.md` | Paragraph-assessment artifacts are retained under `paragraph_level_300_run` (`31–36`). | stale | `backend/discussion_units_sandbox.py:22–29` points to that location, but the directory is absent in this checkout; the loader returns `available: false` when the expected file is missing (`80–85`). |
| `docs/STILL_TO_DO.md` | Review the first nine completed reports and case 677’s raw-error artifact (`35`). | stale | The same checked-in pilot ledger records 17 completed and 3 failed cases, not nine and one: `data/eval/llm_discussion_units_pilot/core_300_run/ledger.json`. |
| `MASTER_IDEAS.md` | “Jurisprudential Shift Detection” is an implemented capability (`28`). | stale | `backend/citation_map.py:1079–1088,1146–1188` estimates citation-frequency replacement and labels it `replacement_likely`; it does not establish a doctrinal shift. |
| `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md` | The Python classifier lacks normalized motion types and reusable cross-field validation (`29–44`). | contradicted | The classifier normalizes motion subtypes and exposes validation findings in `scripts/classify_fc_activity.py:383–407,1761–1779`; the document’s own later checkpoint acknowledges both at `122–133`. |
| `docs/about/AGENT-NOTES.md` | The Data Explorer About tab is empty and needs the proposed content wired in (`17–23`). | stale | The active page contains an About panel and architecture graph in `backend/pages/data_explorer.py:386–394`; the overview is also shown under Site Architecture at `486–490`. |
| `docs/TESTING_MATRIX.md` | There is no browser interaction test for the active Data Explorer (`23,71–83`). | stale | A bounded Playwright smoke script searches, opens the inline reader, checks reader tabs, evidence highlights, and a mobile-width page in `scripts/browser_smoke.py:11–25,31–52,68–71`. It does not cover every listed E2E case or a screenshot assertion. |
| `docs/CITATION_REFINEMENT.md` | Pass one misses anchored short forms and paragraph lists/ranges (`15–18`). | stale | The active extractor finds anchored short forms with paragraph lists/ranges in `backend/citations.py:1265–1303`; this does not establish complete coverage or that every occurrence resolves. |

## Unverified claims and scope

Database-backed counts in `docs/STILL_TO_DO.md` (including the short-form-row
count) and live deployment settings were not verified; no database or deployment
was accessed, so no status is assigned to those claims. The pilot ledger is
artifact evidence only; its operational provenance was not independently
verified. Historical snapshots and future-state proposals in `docs/` were not
audited as current behavior. Generated API, schema, and script references were
checked by `scripts/check_generated_docs.py`.
