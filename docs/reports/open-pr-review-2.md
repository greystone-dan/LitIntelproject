# Open PR Review 2 — Issue #69

Review date: 2026-10-03
Repository: `greystone-dan/LitIntelproject`
Base snapshot: `main` `89ebbc62268609e31e2ff27cc87e60db69b48402`

This is a read-only review. No target PR branch was changed. The requested
`docs/reports/open-pr-review.md` does **not** exist on the inspected `main`, so
this report establishes its own format. PR state at inspection: #22, #31, #33,
and #36 were open; #35 had already merged into `main` and is reviewed below as
a post-merge security/privacy follow-up.

## Review basis and confidence

| PR | Inspected head |
| --- | --- |
| #22 | `e716aa6bd6830dad573a724bcf1ddd6a7d26c54d` |
| #31 | `8865f1c2a8c3e7ec9320f4ffa2cdcf7872ca168b` |
| #33 | `13ef929536cf95bc748afd93c0d27ba8086b7e16` |
| #35 | `1a6ef4bc5487f83fbac4789ac9a21fe2a93d8bbc` |
| #36 | `cf150544763db1f0c3fac62f29251dadf65ed2bd` |

The local clone is shallow, so Git could not calculate merge bases against
these heads. Review evidence came from the fetched PR snapshots, public PR
patches/pages, relevant source and tests, and a bounded delegated review of
#31 discussions and #35 upload privacy. GitHub CLI/API access was unavailable
(`GH_TOKEN` unset / public API 403); public PR pages and diffs were accessible.
No local PR test suite or browser run was performed. Exact line references
below refer to the inspected PR heads unless identified as current `main`.

## PR #22 — Discussion Units v1.4 and reader outline

**State:** Open.

### Correctness risks

- **[should-fix] Footer detection can split ordinary merits text as boilerplate.**
  `backend/contextual_authority/discussion_units.py:159-178` uses unanchored
  substring markers including `"FOR THE"` and `"REASONS FOR"`. The reverse
  scan at `:286-292` treats the last matching paragraph as the footer and adds
  a unit boundary before it. A normal final reasoning paragraph containing
  “for the …” can therefore be isolated as metadata. Anchor the footer cues
  to recognizable end matter and add a negative fixture.
- **[nit] A header in paragraph zero is detected but not separated.**
  `backend/contextual_authority/discussion_units.py:277-285` adds a boundary
  only when `i > 0`; thus a first-paragraph neutral-citation/header marker
  creates no header/body boundary. `boilerplate_start_idx` is not otherwise
  used. Confirm whether keeping the header in the first discussion unit is
  intentional and cover it with a fixture.

### Untested paths

The PR changes `discussion_units.py` and `backend/pages/data_explorer.py`, but
does not change a test file. Existing discussion-unit tests do not establish
coverage for the new header/footer, disposition, and issue-marker branches,
the more aggressive 4-pair/40-paragraph signal-vacuum thresholds, or the
Structure-tab paragraph-jump/highlight interaction (`data_explorer.py:1007,
1013-1018`). Add adversarial unit fixtures and a browser check before treating
segmentation/display quality as established.

### Conflicts, security/privacy

No route or migration is added. PR #31 also edits
`backend/pages/data_explorer.py` in the adjacent reader/linked-case UI block;
the inspected hunks are distinct, so a textual conflict is not established,
but integrate/rebase the UI changes together and verify neither the new
Structure tab nor citation-context display is dropped. No new upload,
authentication, or sensitive-data path was identified.

**Merge recommendation:** First in the #22/#31 pair, after the boundary
fixtures and reader UI check pass.

## PR #31 — Citation context by discussion sub-theme

**State:** Open.

### Correctness risks

- **[nit, uncertain] A citation mapping can be overwritten when a paragraph
  belongs to multiple sub-themes.** In `backend/reader_service.py:146-155`,
  the loop assigns `citation_mappings[citation.id]` for each matching
  sub-theme; a later match replaces the earlier one. The review did not
  establish whether overlapping sub-theme membership occurs or is intended.
  Preserve all matches or establish/test the one-to-one invariant.

No change-request review or unresolved inline discussion was visible in the
accessible PR conversation. The PR author said they were waiting on pytest and
generated-doc checks; the visible checks were successful at this head. A
Cloudflare Workers Builds failure was described by the author as a disconnected,
unused integration. Anonymous page visibility means hidden/private review
activity cannot be ruled out.

### Untested paths

No tests were added. CI status is not a substitute for targeted regression
coverage of overlapping paragraph/sub-theme matches, citations lacking a
paragraph chunk, the new response mapping, and browser rendering of citation
context in the linked-case panel. No local tests or browser checks were run for
this review.

### Conflicts, security/privacy

No route or migration changes. PR #22 modifies the same
`backend/pages/data_explorer.py` reader/sidebar surface; merge #22 first or
integrate both UI diffs together, then verify the Structure tab and linked-case
context. The mapped data is derived from existing case/citation evidence; no
new privacy-sensitive upload or access path was identified.

**Merge recommendation:** After #22, with an explicit overlapping-membership
test or a documented one-sub-theme-per-paragraph invariant.

## PR #33 — Saved searches and alerts

**State:** Open.

### Correctness and security/privacy risks

- **[blocker] Saved searches have no owner boundary, and the new CRUD routes
  have no authentication dependency.** `backend/database.py:731-748` defines
  no owner/user field; `backend/routes.py:3144-3200` creates/lists searches,
  while `:3254-3299` updates/deletes by ID. The response includes the search
  query and filters (`backend/models.py:834-846`). In the repository’s
  documented access posture, application authentication is not enforced.
  Anyone who can reach these routes can read or alter other researchers’
  search strategy. Add an enforced identity/ownership boundary before exposing
  saved searches to multiple users or an untrusted network.
- **[should-fix] The `/check` route advances the alert cursor without checking
  for new results.** `backend/routes.py:3302-3345` loads existing alert rows,
  returns them, and calls `update_last_check`; it does not run a search or
  create alerts. The separate scheduled script filters cases using
  `last_alert_check` (`scripts/check_saved_searches.py:76-104`), so calling
  `/check` before that job can advance the cursor past unseen matches and
  prevent them from being recorded.
- **[should-fix] FC activity alerts read a model attribute that does not
  exist.** `scripts/check_saved_searches.py:151-160` uses `doc.entry_type`;
  the `FCActivityDocument` model fields at `backend/database.py:714-728`
  contain no `entry_type`. The per-document exception handler catches the
  resulting failure, so matching docket documents do not produce alerts.

### Untested paths

No tests were added for API contracts, owner isolation, alert generation,
the scheduled runner, FC activity, or migration upgrade/downgrade. The new
`scripts/check_saved_searches.py` is an operational runner, not test coverage.
Also test retries/concurrent runs for duplicate alerts: the migration defines
no uniqueness constraint on a search/case alert.

### Conflicts, migrations, security/privacy

Migration `alembic/versions/0031_saved_searches_alerts.py:3-14` follows
`0030_full_paragraph_ivfflat`; `main` had only revision 0030 at inspection and
no other requested open PR adds a migration, so no competing revision ID was
found. PR #35 is already merged and also changed `backend/routes.py` and
`backend/models.py`; its memo route and PR #33’s saved-search routes occupy
different areas, but #33 should be rebased against current `main` and the
combined API/model contract checked. No deployment migration was run.

**Merge recommendation:** Hold until ownership isolation, `/check` cursor
semantics, FC activity field mapping, and schema/API tests are corrected.

## PR #35 — Memo citation check (post-merge review)

**State:** Merged into `main` at inspection; this is not an open branch review.
The PR head files matched current-main blobs. Findings below need follow-up on
the current branch, not edits to the merged PR.

### Correctness and security/privacy risks

- **[should-fix] The upload is fully buffered before the size limit is checked.**
  `backend/routes.py:975` reads the entire `UploadFile`; the 10 MB validation
  occurs later in `backend/live_analysis.py:79-87`. A large or concurrent
  upload can consume memory before rejection. Enforce a bounded read/request
  size before buffering.
- **[should-fix, runtime detail unverified] The “held in memory and not stored”
  notice may not describe multipart handling.** `backend/pages/memo_citation_check.py:18`
  makes that promise, while FastAPI’s `UploadFile` normally uses a spooled
  temporary file that can roll to disk. The installed Starlette runtime was
  unavailable for verification. Confirm the deployed behavior and either
  prevent disk spooling or accurately disclose temporary storage.
- **[should-fix] The API returns the entire extracted memo text and lacks an
  explicit no-store policy.** `backend/models.py:843` includes the full `text`
  in the response; the UI uses `text_length` rather than that full field.
  The route at `backend/routes.py:970-982` does not set `Cache-Control:
  no-store`. Omit unused memo text and prevent caching of the sensitive
  response.

### Untested paths

`tests/test_memo_citation_check.py:112-199` tests helper behavior with mocks,
not multipart upload parsing, over-limit reads, temporary-file behavior,
endpoint response headers, or browser handling. The delegated review did not
run tests; the environment lacked Starlette for direct spool verification.

### Conflicts, security/privacy

No migration was added. PR #33 also changes `backend/routes.py` and
`backend/models.py`; its saved-search additions are in separate route/model
regions, but the branches need integration against the already-merged memo
implementation. The broader app access posture remains unauthenticated per
`SYSTEM_REFERENCE.md:1894-1899`; do not interpret `noindex` as protection for
uploaded legal work product.

**Merge recommendation:** Already merged; file a focused follow-up for
bounded upload handling, storage disclosure, and response minimization.

## PR #36 — V3 tagging expansion

**State:** Open.

### Correctness risks

- **[blocker] The tag vocabulary changes without changing the taxonomy version,
  leaving a mixed corpus under one version.** The modified proposal still says
  `taxonomy_version: ca_legal_v3_core` (`data/eval/reports/tagging-v3-core-whitelist-proposal.json:2`).
  `backend/legal_tagger_v3.py:42-53` loads every category from that file, even
  when `review_status` is `"proposed"`. `scripts/tag_cases_v3.py:82-95`
  skips cases already marked complete for the same `TAXONOMY_VERSION`, and
  `scripts/run_overnight.py:97` invokes that tagger in the enrichment profile.
  After the proposal changes, new/reprocessed cases can receive expanded tags
  while previously tagged cases retain the old set under the same version.
  Version the taxonomy and require a controlled, complete rebuild or keep
  candidates outside the file loaded by the runtime tagger.
- **[should-fix] The expansion measurement does not measure an expansion, and
  its precision result is not evidence.** `scripts/measure_real_coverage.py:109-124`
  loads one proposal and passes it to both “before” and “after”; `:175-185`
  then increments `correct` unconditionally. In
  `scripts/validate_precision.py:134-139,184-210`, matches are selected only
  when the alias is already present and “correctness” checks that same alias
  again. These scripts cannot substantiate the claimed coverage/precision.
  Keep separate frozen baseline/candidate vocabularies and use labeled
  positive/negative examples with reproducible scoring.

### Untested paths

No tests were changed. The new candidate aliases lack adversarial
positive/negative fixtures, and the taxonomy-version/backfill behavior is
untested. `mine_a2aj_concepts.py:77` and `measure_real_coverage.py:71` load
the full Hugging Face train split before stopping at a sample count; this is
not a bounded download merely because later loops retain 200/500 cases. The
review did not run that network/data workflow.

### Conflicts, security/privacy

No route or migration is added. This PR changes the proposal file consumed by
the runtime tagger, so it conflicts at the data/version boundary with existing
V3-tagged records rather than with another PR’s endpoint or migration. No new
user-upload or private-data path was identified; confirm source/terms handling
before retaining or redistributing derived dataset artifacts.

**Merge recommendation:** Do not merge until taxonomy versioning/rebuild and
valid precision/coverage evidence are in place.

## Cross-PR route/migration summary and suggested order

- Among the remaining open PRs (#22, #31, #33, #36), #33 is the only one
  adding API routes or an Alembic migration. No duplicate migration revision
  was found. PR #35 is already merged and shares `backend/routes.py` and
  `backend/models.py` with #33; those additions are in distinct regions.
- **#22 → #31:** review/integrate together. Both edit the Data Explorer reader
  UI: #22 adds the Structure tab/jumps (`backend/pages/data_explorer.py:1007-1018`)
  and #31 adds citation-context rendering in the adjacent linked-case block
  (`:1016-1017` in its head). No textual conflict is established, but preserve
  both behaviors in the integrated UI. No migration overlap.
- **#33:** rebase against current `main` after #35’s merge. Its `0031` migration
  follows the inspected `0030` head with no competing migration among these
  PRs. Do not merge until the ownership/privacy boundary and both alert
  correctness issues are fixed and tested.
- **#35:** already merged; treat its upload findings as a focused follow-up,
  not an item in the open-PR merge queue.
- **#36:** hold until the taxonomy is versioned/rebuilt consistently and
  coverage/precision are measured with real baseline/candidate data and
  labeled fixtures. Do not use its current metrics as merge evidence.

Suggested order for eligible open work: **#22, then #31; #33 only after its
blockers are resolved; #36 last after its versioning and evaluation gates.**
This is sequencing guidance, not approval to merge any branch.
