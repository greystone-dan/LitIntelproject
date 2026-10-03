# Read-only review: PRs #28, #29, #32, and #34

Reviewed: 2026-10-03
Repository: `greystone-dan/LitIntelproject`
Scope: Static review of the four local PR-head refs, their diffs from common base
`3d903767d22f09df1e69e49cb12b1e9c11a15af3`, and compatibility between the
branches. No PR branch was checked out or modified.

## Executive summary

| PR | Reviewed head | Assessment |
| --- | --- | --- |
| [#28](https://github.com/greystone-dan/LitIntelproject/pull/28) | `49dccf34e0942c71dfd2825567fc261adc07626b` | No cross-PR route/schema collision found; upload-size and generated-API-reference should-fixes remain. Closest to fine, not an unconditional approval. |
| [#29](https://github.com/greystone-dan/LitIntelproject/pull/29) | `867af60d00d2d7c9c66717501f1a58376613605a` | Its migration correctly follows revision `0030` and is the prerequisite for #32, but contains a redundant uniqueness/index definition (nit). Merge before a corrected #32. |
| [#32](https://github.com/greystone-dan/LitIntelproject/pull/32) | `6b164fdc21f156af7adc378cd8ad1dfdaa60d92e` | **Not merge-ready:** its Alembic `down_revision` does not match #29's actual revision ID. |
| [#34](https://github.com/greystone-dan/LitIntelproject/pull/34) | `19ed285ef63a8b86050b71d6b1a46e8b43d5cc93` | **Not merge-ready as-is:** requires #32's table migration and overlaps/conflicts with #32's routes/page and duplicates its theme response models. |

**Merge order:** #28 can be merged independently (after bounding its upload
read). Merge #29 before #32, but first correct #32's revision identifier to
`0031_statute_library_phase1` and verify the resulting single Alembic head.
Then reconcile and merge #34 on top of #32: retain one `/themes` page and one
`/themes/discovery` handler, deduplicate the theme response models, and preserve
the unit-search additions. Regenerate generated references after conflict
resolution. Do not merge #32 or #34 as currently reviewed.

**Does any PR look fine?** #28 is the closest: its additions are separate from
the other PR routes and migrations, but it needs a bounded upload read and its
generated API reference must be refreshed. #29's own `0031` migration is ordered
correctly; it is a suitable prerequisite, not a reason to merge the currently
broken #32 migration unchanged.

## Review method and verification boundary

All four refs share the local merge base above. Immutable source citations below
link to the reviewed head commits and exact file lines. `git merge-tree
--write-tree` was used for read-only pairwise merge simulations; no merge,
checkout, or branch update was performed. Those simulations found #28+#29 and
#29+#32 conflict-free at the text-merge level, but #32+#34 conflicts in
`backend/database.py`, `backend/routes.py`, generated API/schema/script docs,
and an add/add conflict in `backend/pages/theme_explorer.py`. The #32/#34
`backend/models.py` additions auto-merge, leaving duplicate class declarations
unless explicitly deduplicated.

At 2026-10-03 18:29 UTC, GitHub metadata confirmed all four PRs were open, with
the head SHAs listed above; #28 was a draft and #29, #32, and #34 were not.
GitHub Actions' pytest check passed for each reviewed head: [#28](https://github.com/greystone-dan/LitIntelproject/actions/runs/37140601159),
[#29](https://github.com/greystone-dan/LitIntelproject/actions/runs/37143240385),
[#32](https://github.com/greystone-dan/LitIntelproject/actions/runs/37141905997),
and [#34](https://github.com/greystone-dan/LitIntelproject/actions/runs/37141858689).
The generated-docs check failed on #28 because
`docs/API_REFERENCE.generated.md` is stale
([workflow log](https://github.com/greystone-dan/LitIntelproject/actions/runs/37140601161/job/111254069520));
it passed on #29, #32, and #34. GitHub's mergeability assessment remains
unknown. The local `gh` CLI lacked `GH_TOKEN` and unauthenticated REST returned
HTTP 403, but the read-only GitHub tools supplied the metadata above.

## PR #28 — memo citation check

Reviewed head: `49dccf34e0942c71dfd2825567fc261adc07626b`.

### Findings

- **[should-fix] Bound the request body before buffering it.** The new endpoint
  reads the entire uploaded body at
  [backend/routes.py:970-990](https://github.com/greystone-dan/LitIntelproject/blob/49dccf34e0942c71dfd2825567fc261adc07626b/backend/routes.py#L970-L990),
  then calls the shared document analyzer. That analyzer checks the 10 MiB limit
  only after it receives the bytes
  ([backend/live_analysis.py:80-87](https://github.com/greystone-dan/LitIntelproject/blob/49dccf34e0942c71dfd2825567fc261adc07626b/backend/live_analysis.py#L80-L87)).
  Thus a much larger request is already fully resident before rejection. Enforce
  a streaming/request-body limit before accepting the complete payload. The
  existing Live Analysis handlers use the same read-then-validate pattern; that
  does not remove the resource-boundary concern for this new route.

- **[should-fix] Regenerate the API reference.** The generated-docs check for
  this head fails because `docs/API_REFERENCE.generated.md` is stale
  ([workflow log](https://github.com/greystone-dan/LitIntelproject/actions/runs/37140601161/job/111254069520)).
  Regenerate the reference from the route source and review the resulting diff
  before merge.

### Untested paths

The PR adds normalization unit tests, but no route-level tests were found in its
changed files. The memo upload route, oversize and unsupported uploads, DOCX/PDF
analysis, treatment lookup, missing-authority suggestions, and response
validation were not exercised in this review. The GitHub pytest workflow passed;
no tests were run locally for this review.

### Interactions

No Alembic migration is added. The `/memo-citation-check` page and POST route are
distinct from the routes added by #29, #32, and #34; the local #28+#29 merge
simulation reported no textual conflicts. **Assessment:** closest to fine, with
the upload-bound and generated-reference should-fixes above.

## PR #29 — statute library integration

Reviewed head: `867af60d00d2d7c9c66717501f1a58376613605a`.

### Findings

- **[nit] Remove redundant unique indexes/constraints on `instrument_key`.**
  The migration declares `unique=True` on the column, adds a named unique
  constraint, and then creates a separate index on the same key
  ([alembic/versions/0031_statute_library_phase1.py:21-40](https://github.com/greystone-dan/LitIntelproject/blob/867af60d00d2d7c9c66717501f1a58376613605a/alembic/versions/0031_statute_library_phase1.py#L21-L40)).
  This is redundant index work/storage; retain one uniqueness mechanism and
  regenerate/check the migration before rollout.

### Untested paths

The PR includes `test_statute_integration.py`; the GitHub pytest workflow passed,
but the test was not run locally for this review. The Justice Laws/A2AJ import
scripts, source availability and terms handling, version-date selection against
a populated database, and migration upgrade/downgrade on both fresh and
existing schemas were not exercised.

### Interactions

The migration correctly declares
`revision = "0031_statute_library_phase1"` and
`down_revision = "0030_full_paragraph_ivfflat"`
([migration:12-16](https://github.com/greystone-dan/LitIntelproject/blob/867af60d00d2d7c9c66717501f1a58376613605a/alembic/versions/0031_statute_library_phase1.py#L12-L16)).
That makes #29 the required predecessor for #32, whose current
`down_revision` names a different revision. PR #29 adds the statute routes at
[backend/routes.py:1089-1182](https://github.com/greystone-dan/LitIntelproject/blob/867af60d00d2d7c9c66717501f1a58376613605a/backend/routes.py#L1089-L1182);
no duplicate endpoint with #28 or #32/#34's theme and unit routes was found.

## PR #32 — discussion-unit cache and theme discovery

Reviewed head: `6b164fdc21f156af7adc378cd8ad1dfdaa60d92e`.

### Findings

- **[blocker] Alembic dependency points to a revision ID that does not exist in
  the requested PR set.** Migration
  [alembic/versions/0032_discussion_unit_cache.py:12-15](https://github.com/greystone-dan/LitIntelproject/blob/6b164fdc21f156af7adc378cd8ad1dfdaa60d92e/alembic/versions/0032_discussion_unit_cache.py#L12-L15)
  says `down_revision = "0031_statute_library_schema"`. PR #29's actual revision
  ID is `0031_statute_library_phase1`
  ([#29 migration:12-16](https://github.com/greystone-dan/LitIntelproject/blob/867af60d00d2d7c9c66717501f1a58376613605a/alembic/versions/0031_statute_library_phase1.py#L12-L16)).
  Even merging #29 first will not repair this mismatch; Alembic cannot resolve
  the chain as written. Update the identifier and inspect `alembic heads` and
  the full revision path before merge.

- **[blocker] Reconcile same-path route/page additions with #34 before combining
  the branches.** #32 adds `/themes/discovery` and `/themes` at
  [backend/routes.py:754-800](https://github.com/greystone-dan/LitIntelproject/blob/6b164fdc21f156af7adc378cd8ad1dfdaa60d92e/backend/routes.py#L754-L800)
  and
  [backend/routes.py:1133-1135](https://github.com/greystone-dan/LitIntelproject/blob/6b164fdc21f156af7adc378cd8ad1dfdaa60d92e/backend/routes.py#L1133-L1135).
  #34 independently adds the same GET paths at
  [backend/routes.py:1088-1090](https://github.com/greystone-dan/LitIntelproject/blob/19ed285ef63a8b86050b71d6b1a46e8b43d5cc93/backend/routes.py#L1088-L1090)
  and
  [backend/routes.py:3241-3290](https://github.com/greystone-dan/LitIntelproject/blob/19ed285ef63a8b86050b71d6b1a46e8b43d5cc93/backend/routes.py#L3241-L3290).
  Merge simulation confirms route/page conflicts. Resolve to one handler per
  path and one combined page; do not concatenate both definitions. Both branches
  also add `ThemeOccurrenceResponse`, `DiscoveredThemeResponse`, and
  `ThemeDiscoveryResponse` at different positions in `backend/models.py`
  ([#32:334-352](https://github.com/greystone-dan/LitIntelproject/blob/6b164fdc21f156af7adc378cd8ad1dfdaa60d92e/backend/models.py#L334-L352);
  [#34:854-874](https://github.com/greystone-dan/LitIntelproject/blob/19ed285ef63a8b86050b71d6b1a46e8b43d5cc93/backend/models.py#L854-L874)).
  Python allows the duplicate declarations and the latter shadows the former,
  but they must be consolidated rather than treated as an import error.

### Untested paths

No tests were added in #32's changed paths. Although the GitHub pytest workflow
passed, the cache migration, batch job,
`/themes/discovery` API, `/themes` rendering, and empty/partial Core-300
behavior were not exercised. The route iterates IDs 1–300 and suppresses every
per-case exception
([backend/routes.py:760-773](https://github.com/greystone-dan/LitIntelproject/blob/6b164fdc21f156af7adc378cd8ad1dfdaa60d92e/backend/routes.py#L760-L773));
query cost and whether partial results are visible to researchers need a route
test and an explicit error/coverage policy.

## PR #34 — unit search and theme analytics

Reviewed head: `19ed285ef63a8b86050b71d6b1a46e8b43d5cc93`.

### Findings

- **[blocker] The unit-search route requires a table whose migration is only in
  #32.** `search_units` calls the new search service at
  [backend/routes.py:3293-3316](https://github.com/greystone-dan/LitIntelproject/blob/19ed285ef63a8b86050b71d6b1a46e8b43d5cc93/backend/routes.py#L3293-L3316);
  the service queries `DiscussionUnitCache`
  ([backend/unit_search.py:263-272](https://github.com/greystone-dan/LitIntelproject/blob/19ed285ef63a8b86050b71d6b1a46e8b43d5cc93/backend/unit_search.py#L263-L272)).
  #34 adds the ORM declaration but no Alembic migration. The table is created
  only by #32's `0032_discussion_unit_cache` migration. #34 therefore cannot be
  deployed independently; make the dependency explicit and merge only after
  #32's revision chain is repaired and applied.

- **[blocker] Consolidate the overlapping theme route/page and model definitions
  with #32.** See the paired route and model citations in the #32 section.
  `git merge-tree` reports conflicts for the route module, page, database module,
  and generated references; the model file auto-merges but contains duplicate
  theme response classes. Resolve these together and regenerate, rather than
  hand-edit, the generated API/schema/script references.

### Untested paths

The PR adds `tests/test_unit_search_e2e.py`; the GitHub pytest workflow passed,
but it was not run locally for this review. Its fixture
uses `Base.metadata.create_all()` on SQLite
([test:27-33](https://github.com/greystone-dan/LitIntelproject/blob/19ed285ef63a8b86050b71d6b1a46e8b43d5cc93/tests/test_unit_search_e2e.py#L27-L33)),
so it does not validate the Alembic dependency or an existing PostgreSQL
deployment. The FastAPI route contracts, theme-page interaction, analytics
response, and migration-backed unit search were not exercised.

## Validation and residual risk

- Read-only ancestry/diff inspection: common base and four local head refs
  recorded above.
- Pairwise merge simulations: `git merge-tree --write-tree` for #28/#29,
  #29/#32, #32/#34, #28/#32, and #29/#34. These are not actual merges or
  migration execution.
- No review-local application tests, browser checks, Alembic upgrade/downgrade,
  or importer jobs were run.
- GitHub pytest passed on all four reviewed heads. The generated-docs check
  failed for #28 (`docs/API_REFERENCE.generated.md` stale) and passed for #29,
  #32, and #34. Recheck current PR checks and rerun generated references and
  focused tests after conflict resolution.
