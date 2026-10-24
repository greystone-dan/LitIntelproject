# Code review 8/11 — `scripts/` files d–l

## Summary

Reviewed all 74 files directly under `scripts/` whose names start with d–l
(there are no matching h- or k-prefixed files). The review is a static,
line-by-line source review at `e2df6e7f3058484b485172d00b48e2ec5d7e050e`;
latest `main` (`d2bcb41ea1e424024fabd3bc5c19028d75ebf6e2`) is an ancestor of that
commit. No scripts, database jobs, network requests, or tests were run. No
in-scope files were left unread.

Highest-priority concerns are unguarded or broad database writes, unsafe undo
paths, permanent skipping of failed work, out-of-scope RPD/RAD handling, and
scripts that send case text to OpenAI despite the project’s no-OpenAI rule.
No confirmed challenge-evasion behavior was found; the CanLII importer surfaces
HTTP 403 responses rather than bypassing them.

The table flags describe database/provider behavior (`read-only` means no
database mutation); local reports, caches, and generated files are noted in the
purpose. “Reads keys” names code that reads a credential from its environment.

## Script inventory

| Script | One-line purpose | Risk flag |
| --- | --- | --- |
| `scripts/daily_intake.py` | Imports A2AJ FC/FCA/SCC cases and FC IMM activity; may update activity rows and write a download cache. | overwrites data (activity); dry-run available |
| `scripts/deduplicate_a2aj.py` | Demonstrates deduplication with mock data; no database work. | read-only |
| `scripts/discover_recent_case_themes.py` | Reads recent decisions and writes a JSON theme report. | read-only |
| `scripts/discussion_units_ledger.py` | Reads and atomically replaces a local resumable-run JSON ledger. | read-only |
| `scripts/download_reference_library.py` | Downloads manifest-listed public documents and updates local manifest/inventory files. | read-only |
| `scripts/dry_run_paragraph_evidence_bridge.py` | Reads database evidence and writes a JSON bridge report. | read-only |
| `scripts/embed_a2aj_cases.py` | Sends A2AJ case chunks to OpenAI and writes embeddings and processing metadata. | overwrites data; spends money; reads keys |
| `scripts/embed_documentation_appendices.py` | Regenerates embedded appendix content in `SYSTEM_REFERENCE.md`. | read-only (database); overwrites file |
| `scripts/embed_local_chunks.py` | Generates local-model chunk embeddings and inserts them into the database. | insert-only; dry-run available |
| `scripts/embed_openai_chunks.py` | Sends paragraph chunks to OpenAI and fills missing embedding fields with a ledger and budget cap. | overwrites data; spends money; reads keys |
| `scripts/eval_models.py` | Runs local embedding/JSON model evaluations and writes a result report. | read-only |
| `scripts/eval_position_rules.py` | Evaluates position rules against local gold/text files. | read-only |
| `scripts/evaluate_case_structure.py` | Evaluates case structure from local inputs, optionally including an external RPD extract. | read-only |
| `scripts/evaluate_citation_refinement.py` | Compares citation-refinement results and writes CSV/JSON reports. | read-only |
| `scripts/evaluate_data_quality.py` | Audits database quality and can write a JSON report. | read-only |
| `scripts/evaluate_discussion_unit_boundaries.py` | Evaluates discussion-unit boundaries against local fixtures and can write JSON. | read-only |
| `scripts/evaluate_fc_activity_deterministic.py` | Evaluates deterministic FC Activity classifications and writes JSON. | read-only |
| `scripts/evaluate_fc_citation_extraction.py` | Compares evidence CSV rows with citation gold data and writes CSV summaries. | read-only |
| `scripts/evaluate_retrieval.py` | Posts evaluation queries to a configured search service and can write a report. | read-only |
| `scripts/evaluate_retrieval_benchmark.py` | Benchmarks a configured search service with bounded HTTP requests and can write a report. | read-only |
| `scripts/evaluate_statute_extraction.py` | Evaluates statute extraction from local fixtures and can write a report. | read-only |
| `scripts/evaluate_statute_sections.py` | Evaluates statute-section extraction against local gold data. | read-only |
| `scripts/evidence_gate.py` | Reads task/run evidence files and reports whether completion criteria pass. | read-only |
| `scripts/export_fc_activity_package.py` | Exports read-only FC Activity data to a new package directory. | read-only |
| `scripts/extract_a2aj_case_citations_resumable.py` | Extracts citations for A2AJ RPD/SCC cases and writes citation/processed-state rows. | insert-only; overwrites processing metadata |
| `scripts/extract_a2aj_provincial_acts.py` | Extracts selected acts from local Parquet into JSON snapshots when explicitly asked to write. | read-only (database); overwrites files |
| `scripts/extract_citation_network.py` | Extracts citations/statute references and optionally recomputes citation metrics. | overwrites data |
| `scripts/extract_fc_citation_evidence.py` | Exports database citation evidence to CSV/JSON; FC-only filtering is optional. | read-only |
| `scripts/extract_irpa_irpr_references.py` | Rebuilds statute-reference rows in batches by deleting and reinserting per-case references. | overwrites data |
| `scripts/fc_activity_backlog.py` | Counts, fetches, imports, and undoes FC IMM docket activity. | insert-only; overwrites data (optional update); network |
| `scripts/fc_activity_extractors.py` | Extracts structured procedural and motion fields from docket events. | read-only |
| `scripts/fc_activity_laptop.py` | Fetches FC IMM activity and appends results to local files. | read-only (database); writes files |
| `scripts/fc_portal_collector.py` | Collects FC file listings and optional detail pages into JSONL/checkpoint files. | read-only (database); writes files |
| `scripts/fetch_fc_procedural_history.py` | Fetches FC procedural history and writes history/activity rows; `--update` can replace existing data. | insert-only; overwrites data (optional update) |
| `scripts/fetch_position_texts.py` | Fetches public case-page JSON for evaluation IDs and stores local files. | read-only (database); writes files |
| `scripts/fill_fca_headline_outcomes.py` | Fills missing FCA headline outcomes from deterministic metadata; supports undo. | overwrites data; dry-run by default |
| `scripts/fill_paragraph_search.py` | Inserts missing paragraph-search rows for an explicitly selected court. | insert-only; dry-run by default |
| `scripts/fix_common.py` | Provides shared batching and undo-file helpers for repair scripts. | read-only (database) |
| `scripts/fix_french_metadata.py` | Re-extracts French FC/FCA metadata and optionally fills outcome fields. | overwrites data; dry-run by default |
| `scripts/fix_junk_judge_profiles.py` | Removes junk judge profiles and can restore profiles, links, and aliases. | overwrites data; dry-run by default |
| `scripts/fix_junk_judges.py` | Repairs or removes junk judge metadata and supports undo. | overwrites data; dry-run by default |
| `scripts/fix_non_immigration_report.py` | Reports non-immigration classifications and judge win-rate effects. | read-only |
| `scripts/fix_own_caption_links.py` | Unlinks citation rows that resolve a case’s own caption to another case. | overwrites data; dry-run by default |
| `scripts/fix_self_citations.py` | Deletes self-citation rows and supports restoration from an undo file. | overwrites data; dry-run by default |
| `scripts/flag_weak_short_form_links.py` | Reports weak short-form citation links and can unlink/revert selected rows. | overwrites data (optional); dry-run by default |
| `scripts/generate_api_reference.py` | Generates the API reference from the application schema. | read-only (database); overwrites file |
| `scripts/generate_schema_reference.py` | Generates the ORM schema reference and ERD. | read-only (database); overwrites files |
| `scripts/generate_script_catalog.py` | Generates the script catalog from script metadata. | read-only (database); overwrites file |
| `scripts/generate_work_history.py` | Generates a work-history report from local JSON exports. | read-only (database); overwrites file |
| `scripts/import_a2aj_decisions.py` | Reads/samples A2AJ decisions, including RPD/RAD, and reports parse statistics; no DB import. | read-only |
| `scripts/import_a2aj_full.py` | Streams and imports A2AJ cases in `import` mode; its target list includes FC/FCA/SCC/RAD/RPD. | overwrites data in import mode; dry-run is opt-in |
| `scripts/import_canlaw_staging.py` | Posts staged CanLaw records to the canonical merge endpoint. | insert-only / overwrites data via merge; dry-run available |
| `scripts/import_fc_decisions.py` | Posts Federal Court JSON/JSONL/CSV records to `/ingest`. | insert-only |
| `scripts/import_historical_statutes.py` | Fetches and reports historical IRPA/IRPR point-in-time versions. | read-only |
| `scripts/import_seed_cases_from_a2aj_api.py` | Looks up missing seed cases through A2AJ and posts them to `/ingest`. | insert-only; dry-run available |
| `scripts/import_statutes.py` | Fetches Justice Laws XML and imports statute versions and sections. | insert-only |
| `scripts/index_legislation.py` | Parses local legislation snapshots into indexed documents and sections. | overwrites data; dry-run available |
| `scripts/ingest_a2aj_api.py` | Pages through a configurable source API and posts selected records to `/ingest`. | insert-only; reads keys; dry-run available |
| `scripts/ingest_a2aj_citation_network.py` | Loads FC Parquet cases and citation-graph data into provenance/network tables. | insert-only / overwrites mappings |
| `scripts/ingest_a2aj_parquet.py` | Posts selected local A2AJ Parquet records to `/ingest`. | insert-only; dry-run available |
| `scripts/ingest_canlii_seed_cases.py` | Fetches CanLII seed decisions, optionally falls back to A2AJ, and posts to `/ingest`. | insert-only; dry-run available |
| `scripts/ingest_hf_fc_activity.py` | Loads Hugging Face Federal Court activity data into activity tables. | insert-only / overwrites data; dry-run available |
| `scripts/ingest_synthetic_cases.py` | Posts hardcoded synthetic cases to the configured `/ingest` target. | insert-only; runs at import time |
| `scripts/inspect_context_variants.py` | Inspects contextual-authority variants for bounded cases. | read-only |
| `scripts/inspect_discussion_units.py` | Inspects discussion units and can write JSON/Markdown reports. | read-only |
| `scripts/judge_alias_report.py` | Reports proposed same-person judge-merge groups. | read-only |
| `scripts/judge_reconciliation_report.py` | Reports judge metadata/profile-link mismatches and optional local extraction comparisons. | read-only |
| `scripts/link_citation_pinpoints.py` | Resolves citation paragraph pinpoints to stored paragraph chunks. | overwrites data; dry-run by default |
| `scripts/link_refined_citations.py` | Resolves refined citation rows to cases and marks unresolved rows. | overwrites data; dry-run by default |
| `scripts/load_case_frames.py` | Loads missing case frames from JSON files. | insert-only; dry-run by default |
| `scripts/load_core150_layers.py` | Loads/removes core case frames, issue maps, and paragraph notes. | insert-only / overwrites data on undo; dry-run by default |
| `scripts/load_issue_maps.py` | Loads issue maps/questions and fills missing case links. | insert-only / overwrites data; dry-run by default |
| `scripts/load_note_links.py` | Loads paragraph-note links and offers source-scoped undo. | insert-only; dry-run by default |
| `scripts/load_position_tags.py` | Loads missing paragraph-position records. | insert-only; dry-run by default |

## Bugs

- `scripts/fetch_fc_procedural_history.py:340-349` — **High:** Generic “reasons
  for judgment” or “(final decision)” entries are classified as “JR Granted”
  without explicit outcome evidence, which can mislabel dismissals. **Fix:**
  leave the outcome unknown unless the source states it.
- `scripts/fetch_fc_procedural_history.py:472-488,529-542` — **High:** A failed
  RE fetch returns `error="no_re_data"`, but the default writer still upserts
  placeholder values; a later update can overwrite good data, and a normal run
  can make the record appear fetched. **Fix:** treat errors as failures and do
  not upsert them.
- `scripts/daily_intake.py:371-374` — **Medium:** A partition is marked fully
  consumed before processing imported cases finishes. Processing failures do
  not clear the marker, so a later unchanged-ETag run can skip failed cases.
  **Fix:** mark consumption only after processing succeeds, or retry unprocessed
  cases independently of the partition ETag.
- `scripts/discover_recent_case_themes.py:150-155` — **Medium:** A matching
  provision section can qualify statute evidence without matching the expected
  instrument, so an unrelated statute with the same section can support a theme.
  **Fix:** require both the expected instrument and section.
- `scripts/export_fc_activity_package.py:298-315` — **Medium:** The
  `--classification-or-entry-regex` path does not implement OR semantics;
  earlier classification filters can exclude rows before matching entry IDs
  are unioned. **Fix:** build each predicate branch independently, combine
  with OR, then apply shared filters.
- `scripts/extract_irpa_irpr_references.py:38-46` — **Medium, possible:** A
  citation match spanning the prefix/current chunk boundary can yield a
  negative chunk-relative start offset. **Fix:** detect cross-boundary matches
  and calculate offsets against the owning source text.
- `scripts/import_a2aj_full.py:244-250` — **High:** The active importer
  imports `Decision` from `backend.database`, where the reviewed model module
  defines `Case` but no `Decision`; the per-record path therefore fails instead
  of importing. **Fix:** use the supported `Case`/ingestion contract and test a
  bounded write.
- `scripts/import_statutes.py:483-490,694-705` — **High:** Historical version
  records can use an XML snapshot/PIT date as the effective-in-force date, rather
  than the PIT index’s explicit effective date. **Fix:** pass and preserve the
  in-force date separately from snapshot provenance.
- `scripts/ingest_hf_fc_activity.py:54,230-233` — **Medium:** The non-null
  default `--source-file` can cause resolution to fail before `--download` or
  the legacy-file fallback is reached. **Fix:** resolve/download a missing
  target path without requiring it to exist first.
- `scripts/import_seed_cases_from_a2aj_api.py:95-105` — **Medium:** Dataset
  inference recognizes SCC/FCA/FC but not RAD/RPD, so refugee-division searches
  may be unfiltered and accept a wrong-court candidate. **Fix:** recognize and
  validate RAD/RPD results before import.
- `scripts/fc_activity_backlog.py:313` — **Medium:** `max(args.max_requests, …)`
  makes the requested request limit a minimum, not a ceiling. **Fix:** enforce
  the user-supplied maximum and stop when it is exhausted.
- `scripts/fill_paragraph_search.py:63,79-83` — **Low:** Zero/negative batch
  sizes or limits are not consistently rejected and can silently do no work or
  fail in SQL. **Fix:** require positive values.
- `scripts/link_citation_pinpoints.py:18-20,40` — **Medium:** A cited paragraph
  range such as “12-13” can be parsed as only paragraph 12. **Fix:** resolve
  both endpoints or mark ranges unsupported rather than truncating.
- `scripts/load_note_links.py:58-61` — **Medium:** Validation checks
  `citation_key` but not `other_citation_key`; malformed rows can raise
  `KeyError`. **Fix:** validate both before lookup and count malformed rows.
- `scripts/load_position_tags.py:35-43,53-54,83-88` — **Low:** Valid JSON with
  non-object shapes, invalid ID types, or a negative limit can raise uncaught
  errors or silently omit files. **Fix:** validate shapes/types and require a
  nonnegative limit.
- `scripts/link_refined_citations.py:33-35,60-70` — **Low:** Nonpositive
  `--batch-size`/`--limit` values can silently skip work or fail. **Fix:**
  validate positive values.
- `scripts/load_core150_layers.py:208-209,229` — **Medium:** `--min-match`
  accepts negative or non-finite values, potentially disabling alignment
  rejection. **Fix:** require a finite value in `[0,1]`.
- `scripts/evaluate_data_quality.py:94-102` — **Low:** The invalid-offset audit
  does not check whether `offset_end` exceeds source-text length. **Fix:**
  validate upper bounds using the correct source/chunk coordinate system.
- `scripts/import_a2aj_full.py:160-162` — **Low:** A zero sample size can cause
  division by zero in the success-rate report. **Fix:** require a positive
  sample size.
- `scripts/deduplicate_a2aj.py:5-8,73-104` — **Low:** Its description promises
  case-name/date fallback matching, but the demo only matches normalized
  citation plus date. **Fix:** implement and test that fallback or correct the
  description.

## Data-safety risks

- `scripts/ingest_synthetic_cases.py:57-74` — **High:** Database lookup and
  `/ingest` POSTs run at module import time, with no dry-run or explicit-write
  switch. **Fix:** move execution behind `main()` and require an explicit
  write flag/test target.
- `scripts/import_a2aj_full.py:241-276,325-344` — **High:** The import
  mode writes unless `--dry-run` is supplied; counters increase before the DB
  insert and failed sessions are not explicitly rolled back/closed in the
  per-case path. **Fix:** default to dry-run, make writes opt-in, count only
  successful commits, and rollback failures.
- `scripts/extract_citation_network.py:27-57` — **High:** The default run
  extracts case citations and writes database results; there is no dry-run,
  undo, or explicit apply gate. **Fix:** require dry-run/preflight followed by
  explicit apply and provide a recoverable run ledger.
- `scripts/extract_a2aj_case_citations_resumable.py:31-35,52-63,88-107` —
  **High:** Timeout/worker-error cases can be marked processed and then excluded
  from future pending work. The same worker also targets RPD and SCC data,
  outside the FC/SCC/FCA project scope. **Fix:** mark complete only on success,
  offer retry for failures, and restrict its cohort to the approved courts.
- `scripts/import_canlaw_staging.py:18` — **High:** The default court selection
  includes RPD while this project is scoped to FC/SCC/FCA. **Fix:** remove RPD
  from defaults and enforce the allowed-court set before any merge request.
- `scripts/import_a2aj_decisions.py:6-13,113-162` — **Medium:** This
  read-only proof of concept samples and reports across RPD/RAD and other
  Canadian courts, contrary to the project’s scope even though it does not write
  to the database. **Fix:** limit sampling and reporting to FC/SCC/FCA.
- `scripts/import_a2aj_full.py:28-37,325-344` — **Medium, possible (currently
  blocked by the importer bug above):** Its target-court set explicitly includes
  RAD and RPD as well as FC/FCA/SCC; if the import bug is repaired, it can write
  out-of-scope records. **Fix:** remove RAD/RPD from the target set and reject
  them at selection and destination boundaries.
- `scripts/ingest_synthetic_cases.py:12-32` — **Medium:** Its synthetic FC
  fixtures explicitly describe RPD/RAD decisions and outcomes, despite the
  project rule excluding those divisions from test/sample material. **Fix:**
  remove those references or retire the fixture script.
- `scripts/evaluate_case_structure.py:138-153` — **Medium:** The evaluation
  accepts external RPD extracts, so it can include out-of-scope material in
  evaluation results. **Fix:** remove the RPD input path and keep evaluation
  fixtures within FC/SCC/FCA.
- `scripts/extract_fc_citation_evidence.py:164-174` — **Medium, possible:**
  FC-only filtering is optional, so the default export can include citation
  evidence from non-FC rows if present. **Fix:** make the FC filter mandatory
  for this FC-focused export.
- `scripts/fill_paragraph_search.py:9-10` — **High:** The documented undo
  deletes all matching RAD paragraph-search rows, not only rows added by this
  script, and explicitly describes an out-of-scope court. **Fix:** remove the
  RAD path and undo only run-owned row IDs.
- `scripts/embed_a2aj_cases.py:35-52,53-80` — **High:** Invoking the script
  immediately spends on OpenAI and writes chunks/case vectors; the printed cost
  is an estimate, not a hard spend ceiling, and there is no dry-run/apply gate.
  **Fix:** disable this OpenAI path under current project policy; otherwise
  require explicit approval, dry-run, hard budget, and bounded cohort first.
- `scripts/embed_openai_chunks.py:498-519,595-615` — **High:** Apply is the
  default unless `--dry-run` is supplied; an explicit cohort, run directory,
  lock, and budget exist, but the script still sends case text to prohibited
  OpenAI. An unrestricted `--source-type`/case-ID cohort can also include
  out-of-scope rows. **Fix:** disable OpenAI calls under current policy and
  require a court-allowlisted cohort if the policy changes.
- `scripts/index_legislation.py:499-517,552-574` — **Medium:** Default
  indexing deletes the old sections and commits a replacement; a parse yielding
  zero sections can erase a prior index. **Fix:** retain old rows on empty or
  invalid parses and require explicit replace mode.
- `scripts/extract_irpa_irpr_references.py:27,59-109` — **Medium:** Without
  `--dry-run`, per-case reference rows are deleted and rebuilt; there is no
  undo, and a partial run can leave only some cases replaced. **Fix:** default
  to dry-run and journal the before-state or use an atomic, resumable
  replacement.
- `scripts/link_refined_citations.py:37-51` — **High:** `--revert --yes`
  commits an update even without `--apply`, clearing targets and setting
  `unresolved=True` for every row at that version, including rows not changed by
  this script. **Fix:** make revert dry-run by default, require `--apply`, and
  track/restore only script-owned row changes.
- `scripts/link_citation_pinpoints.py:42-45,98-103` — **Medium:** A citation
  with no paragraph target can have an existing `target_chunk_id` overwritten.
  **Fix:** require both targets to be null or preserve/reconcile the existing
  chunk target.
- `scripts/load_core150_layers.py:90-94,114-137,164-168,181-197` — **High:**
  Layer commits are separate, so later failures leave partial results; undo can
  delete an identical pre-existing issue-map row because it identifies rows by
  content, not run ownership. **Fix:** record inserted IDs/ownership and make
  partial completion explicit or use one transaction where feasible.
- `scripts/load_case_frames.py:11-12`, `scripts/load_issue_maps.py:9-10`,
  `scripts/load_position_tags.py:9-10` — **High:** Documented undo instructions
  drop whole tables and can erase unrelated data. **Fix:** provide scoped
  row-owned undo; do not recommend table drops except for a verified dedicated
  empty table.
- `scripts/fill_paragraph_search.py:10-11` — **Medium:** Its broad RAD undo is
  only safe when no pre-existing RAD rows exist, a condition not enforced by
  the script. **Fix:** track inserted chunk IDs/run ownership and restrict all
  use to FC/SCC/FCA.
- `scripts/flag_weak_short_form_links.py:42,104-108,140-155` — **High:** The
  backup can overwrite an existing file and omits the prior `unresolved` value;
  revert always writes `False`. **Fix:** create backups exclusively, store all
  changed values, and restore them conditionally.
- `scripts/fix_junk_judges.py:179-183`, `scripts/fix_own_caption_links.py:161-165`,
  `scripts/fix_self_citations.py:146-152` — **High:** `--expected-count` is
  documented as required but omission does not block `--apply`. **Fix:** make
  the count mandatory for writes.
- `scripts/fix_french_metadata.py:65-70` — **Medium, opt-in:** `--include-outcomes`
  can replace populated outcome fields when derived values differ. **Fix:**
  preserve populated fields individually or show each proposed replacement and
  require explicit confirmation.
- `scripts/fc_activity_backlog.py:254,393-402` — **Medium:** Database commits
  precede undo-ledger writes; a crash between them can leave committed rows
  without a ledger entry. **Fix:** record run ownership transactionally or make
  committed inserts reconcilable after a crash.
- `scripts/ingest_hf_fc_activity.py:171-218` — **Medium:** Reingestion can
  overwrite case fields and delete an existing classification without
  reconciling source-owned document removals; `upserts` counts only new cases.
  **Fix:** report create/update/delete counts and make classification
  invalidation/reconciliation explicit.
- `scripts/ingest_canlii_seed_cases.py:444-503` — **Medium, possible:** A
  failure during the `/ingest` POST can enter the A2AJ fallback even if the
  server committed the first request but the response was lost. **Fix:** limit
  fallback to fetch/parse errors and use idempotency keys or verify first-post
  status.
- `scripts/load_issue_maps.py:9-10` — **Medium:** A documented table-drop undo
  may remove unrelated issue-map/question data; the loader also fills missing
  case links. **Fix:** undo only recorded insertions/changes.
- `scripts/load_note_links.py:9-13` — **Low:** The hand-written SQL undo is
  scoped by a source label, but the script does not verify that the label is
  exclusive to this run. **Fix:** use a run-specific ownership marker or
  recorded inserted IDs.

## Security risks

- `scripts/embed_a2aj_cases.py:7,38` and
  `scripts/embed_openai_chunks.py:22,600-613` — **High:** Both read
  `OPENAI_API_KEY` and send decision text to OpenAI. This violates the project’s
  current no-OpenAI rule and exposes source text to an external provider.
  `scripts/ingest_a2aj_api.py:41,97-101` separately reads an optional key from
  `--api-key-env` (default `A2AJ_API_KEY`). **Fix:** disable the OpenAI scripts;
  keep any approved source API credentials scoped to the expected host.
- `scripts/ingest_a2aj_api.py:97-107,136,159-160,211-216` — **High, possible:**
  When a key is configured, it is attached to the caller-supplied API URL and
  reused for a server-provided absolute pagination URL without an origin check.
  A malicious/misconfigured endpoint could receive the key. **Fix:** require
  HTTPS and an allowlisted origin; strip credentials and reject cross-origin
  pagination/redirects.
- `scripts/fetch_fc_procedural_history.py:70-78` and
  `scripts/ingest_canlii_seed_cases.py:44-48,429` — **Medium, possible:**
  The scripted collectors identify as desktop Chrome 126 on Windows rather
  than identifying the collector, which may be treated as a spoofed user agent.
  **Fix:** use an honest application-specific UA with contact information and
  respect source terms/rate limits.
- `scripts/fc_portal_collector.py:187-193` — **Medium:** If the robots check
  fails, the code returns `True` and proceeds despite the comment calling this
  conservative. **Fix:** fail closed when robots rules cannot be checked, or
  require an explicit documented override.
- `scripts/fetch_position_texts.py:20-25,41-45` — **Medium, possible:**
  Input IDs are interpolated into both a URL and a filesystem path; a crafted
  ID could escape the output directory. **Fix:** validate the expected case-ID
  format and verify resolved output paths remain beneath `--out`.
- `scripts/download_reference_library.py:139-145` — **Medium, possible if
  manifest input is untrusted:** URLs are fetched with redirects and no visible
  host/private-address restriction. A crafted manifest could target unintended
  or internal hosts. **Fix:** allowlist source hosts and validate every
  redirect destination.
- `scripts/ingest_canlii_seed_cases.py:6,168-169` — The importer reports a
  403 anti-bot response as an error; no challenge bypass was found in this
  script or the other reviewed scrapers.

## Performance

- `scripts/fc_portal_collector.py:430-438,484-485` — **Medium:** The delay is
  applied after listing pages, not between optional detail requests. **Fix:**
  pace every HTTP request.
- `scripts/download_reference_library.py:140-149` — **Medium:** Each response
  is buffered wholly in memory without a visible size cap. **Fix:** stream to a
  temporary file with a size limit, then atomically replace the destination.
- `scripts/discover_recent_case_themes.py:273-289` — **Medium:** The default
  report materializes all cases in the date window and may issue per-case
  evidence queries. **Fix:** page results and batch/prefetch related evidence.
- `scripts/judge_reconciliation_report.py:74-75,206-210` — **Medium:** It can
  materialize all case ORM objects, including large `full_text` values.
  **Fix:** select only needed columns, defer text unless required, and batch.
- `scripts/ingest_a2aj_citation_network.py:35-49` — **Medium:** It accumulates
  the full selected Parquet content in memory before ingestion. **Fix:** ingest
  bounded batches transactionally.
- `scripts/ingest_a2aj_api.py:110-124,159-160` and
  `scripts/ingest_a2aj_parquet.py:142-150` — **Medium:** `/ingest` POSTs have
  no explicit timeout. **Fix:** use a configurable timeout for each POST.
- `scripts/fc_activity_backlog.py:237-244` — **Low:** Per-entry existence
  checks can create many DB round trips for large histories. **Fix:** preload
  identities per case or batch the checks.
- `scripts/fc_activity_laptop.py:221-225` — **Low:** Duplicate IMM IDs in the
  input can be fetched repeatedly in one run. **Fix:** deduplicate while
  preserving input order.
- `scripts/evaluate_fc_activity_deterministic.py:456-474` — **Medium, possible
  large-cohort cost:** `--resolved-only` loads/classifies candidates before
  sampling, potentially doing more work than the requested sample. **Fix:**
  document the cost or use bounded preselection where equivalent.

## Dead code / cleanup

- `scripts/embed_openai_chunks.py:94-110` — **Low:** `fit_batch_to_budget()` is
  defined but unused; remove it or use it as the single budget-selection path.
- `scripts/fc_activity_extractors.py:718,1226-1229` — **Low:** `_MOTION_NOTICE`
  and `UNRULED_OUTCOMES` appear unused; remove or use them.
- `scripts/import_a2aj_full.py:16-26` and
  `scripts/import_statutes.py:18-36` — **Low:** Unused imports/constants remain.
  Remove them or wire them into the implementation.
- `scripts/deduplicate_a2aj.py` is a mock-data demonstration rather than an
  active database deduplication command. Keep its demo-only status explicit.
- No definite replacement/supersession relationship was established among the
  reviewed scripts.

## Suggestions

- Make all write workflows dry-run by default, require an explicit apply/confirm
  for data changes, and print selected/inserted/updated/deleted counts before
  and after. Preserve a run-owned, verifiable undo path for every overwrite or
  delete.
- Enforce the FC/SCC/FCA allowlist at both selection and write boundaries;
  remove RPD/RAD from defaults, examples, and undo paths.
- Keep API credentials origin-scoped, make network timeouts and request pacing
  consistent, and preserve failed work as retryable instead of marking it
  complete.
- Report limitations honestly: no database state, external API behavior, or
  runtime results were inspected in this source-only review.
