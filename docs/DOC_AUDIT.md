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

## Follow-up (2026-10-17)

The detailed root run note `docs/NEXT_STEPS.md` was moved to
`docs/history/NEXT_STEPS.md` after its current pilot status and approval gate
were consolidated in the Discussion Unit row of `docs/STILL_TO_DO.md`. The audit
table above remains a record of the claims and evidence at its audited revision.

The 21 `docs/case-reader/*.png` files were removed after exact filename/path
searches found no references in `backend/`, `docs/`, or `.swm/`; the `/case-reader`
compatibility endpoint remains. The point-in-time reports
`docs/reports/backend-unused-code.md` and `docs/reports/open-pr-review-2.md` were
removed after exact-filename searches found no inbound references outside their
inventory rows in `DOCS_INDEX.md`.
Two artifact links in `OVERNIGHT.md` were converted to recorded paths after
checking that their target files are absent from this checkout.
Remote Control setup and deployment now have one owner in
`docs/DEPLOYMENT_COMMANDS.md`; application,
site, and tunnel recovery are consolidated in
`docs/OPERATIONAL_RECOVERY_GUIDE.md`.

Other stale claims from that snapshot were corrected in
`docs/about/AGENT-NOTES.md`, `docs/STILL_TO_DO.md`, `docs/TESTING_MATRIX.md`,
`docs/CITATION_REFINEMENT.md`, and `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`.
The Testing Matrix's dated numerical baselines remain historical snapshots.

Deployment/recovery overlaps were consolidated. `docs/DEPLOYMENT_COMMANDS.md`
owns current Remote Control/site commands and links to
`docs/OPERATIONAL_RECOVERY_GUIDE.md`, which now owns cross-system triage and
the iLitSite restart/health/log checklist. Government-readiness links were
repointed to the command guide (`data-flow.md`, `pia-inputs.md`, and the
CBSA-readiness hosting evidence); backup/recovery evidence points to both
deployment and operational recovery guidance. The overlapping
`docs/LOCAL_DEPLOYMENT_SETUP.md` and `docs/SITE_RECOVERY.md` were retired, and
their current workflow is indexed under the remaining owners in `DOCS_INDEX.md`.
The old local-setup path remains only in the historical issue-432 task record,
which was not changed. `docs/CLOUDFLARE_TUNNEL_SETUP.md` remains the one-time/
fallback tunnel guide; `docs/DEPLOYMENT_DOCKER.md` remains the optional
container workflow.
