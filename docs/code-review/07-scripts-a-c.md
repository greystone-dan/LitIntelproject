# Code review 07: scripts `_`, `a`–`c`

## Summary

Static review of all 64 regular files directly under `scripts/` whose names start with `_`, `a`, `b`, or `c`. The most important issues are a `chunk_cases.py` path where `--dry-run` still deletes database data, several default-writing or all-court database jobs, and OpenAI calls despite the project prohibition. The crawler also masks browser automation and waits on Cloudflare challenges.

Reviewed source snapshot: `b3ec917`, based on fetched `main` at `d2bcb41`.

No scripts were executed; no database, API, or `.env` was accessed. No in-scope file was omitted.

Risk flags below describe database or external-service behavior. `read-only` means no database mutation (a script may still write local report or fixture files); `insert-only` and `overwrites data` describe database changes.

## Script inventory

| Script | Purpose | Risk flags |
| --- | --- | --- |
| `scripts/__init__.py` | Package marker for importable script helpers. | read-only |
| `scripts/a2aj_case_importer.py` | Forecast new A2AJ cases by court; its displayed target list includes RAD and RPD. | read-only; network |
| `scripts/acquire_case_html.py` | Fetch and store canonical source HTML. | overwrites data; network |
| `scripts/adjudicate_fc_metadata.py` | Send FC/FCA decision text for metadata adjudication; optionally persist metadata. | spends money; reads keys; overwrites data |
| `scripts/agent_harness.py` | Manage run evidence and execute requested subprocess commands. | read-only (DB); executes commands |
| `scripts/agent_policy.py` | Print a policy decision for a requested operation. | read-only |
| `scripts/aggregate_recorded_costs.py` | Aggregate evaluation-artifact costs into a Markdown report. | read-only (DB); writes a report |
| `scripts/analyze_unlinked_citations.py` | Analyze citation references without a resolved target. | read-only |
| `scripts/apply_judge_aliases.py` | Propose, insert, prune, or revert judge aliases. | overwrites data |
| `scripts/audit_discussion_unit_structure.py` | Audit retained Discussion Unit reports for structural risks. | read-only |
| `scripts/audit_fc_activity_motion_unknowns_openai.py` | Request OpenAI subtype suggestions for unknown FC motions. | spends money; reads keys |
| `scripts/audit_fc_activity_openai.py` | Request an OpenAI audit of sampled FC Activity events. | spends money; reads keys |
| `scripts/audit_fc_metadata_extraction.py` | Audit FC metadata extraction coverage and quality. | read-only |
| `scripts/audit_paragraph_chunks.py` | Inspect paragraph-chunk structure. | read-only |
| `scripts/audit_self_citations.py` | Audit stored citation self-links. | read-only |
| `scripts/backfill_case_metadata_outcomes.py` | Re-extract metadata for cases with full text. | overwrites data |
| `scripts/backfill_case_outcomes.py` | Populate missing versioned outcome rows. | insert-only |
| `scripts/backfill_case_tags_v3.py` | Add V3 legal tags; optionally clear and retag a taxonomy version. | insert-only; overwrites data |
| `scripts/backfill_fc_case_metadata.py` | Extract FC metadata and optionally update stored metadata. | overwrites data |
| `scripts/backfill_judge_profiles.py` | Create judge profiles and case links; optionally merge duplicates. | insert-only; overwrites data |
| `scripts/backfill_panel_judges.py` | Create/link panel-member judge profiles; defaults to SCC. | insert-only |
| `scripts/backfill_rpd_header.py` | Re-extract RPD judge and place-of-hearing fields. | overwrites data |
| `scripts/backfill_statute_instrument_keys.py` | Fill missing statute instrument keys. | overwrites data |
| `scripts/backfill_statute_provisions.py` | Derive provision fields from stored pinpoints. | overwrites data |
| `scripts/benchmark_case_citations.py` | Measure case-citation extraction on bounded samples. | read-only |
| `scripts/benchmark_citation_resolution.py` | Measure citation occurrence resolution on bounded samples. | read-only |
| `scripts/browser_smoke.py` | Smoke-check the Data Explorer in a browser. | read-only; network |
| `scripts/build_alert_digest.py` | Render a saved-search digest from input data. | read-only |
| `scripts/build_case_fingerprints.py` | Add missing case fingerprints. | insert-only |
| `scripts/build_changelog.py` | Build the About-page changelog from cached and GitHub records. | read-only (DB); reads keys; network |
| `scripts/build_citation_sample_candidate.py` | Build a proposed citation-extraction sample. | read-only |
| `scripts/build_core_immigration_set.py` | Select an A2AJ immigration prototype set; can write CSV output in dry-run mode. | read-only |
| `scripts/build_discussion_unit_priority_lists.py` | Build Discussion Unit review-priority lists. | read-only |
| `scripts/build_fc_activity_audit_report.py` | Render an FC Activity audit report from package files. | read-only |
| `scripts/build_fc_citation_gold_template.py` | Generate an FC citation annotation template. | read-only |
| `scripts/build_fc_citation_seed.py` | Normalize Federal Court citation seed data. | read-only |
| `scripts/build_fc_metadata_gold_set.py` | Select FC metadata gold-set cases. | read-only |
| `scripts/build_five_case_citation_gold_candidate.py` | Build a five-case citation review fixture. | read-only |
| `scripts/build_mason_argument_citation_fixture.py` | Build an argument/citation fixture. | read-only |
| `scripts/build_mason_citation_review_ledger.py` | Render a citation review ledger. | read-only |
| `scripts/build_paragraph_cited_by.py` | Build paragraph-level cited-by links. | insert-only; overwrites data |
| `scripts/build_position_layers.py` | Build per-paragraph position-layer files. | read-only |
| `scripts/build_position_preview.py` | Build compact decision position-preview files. | read-only |
| `scripts/build_position_preview_lf.py` | Build position previews from LF proof-of-concept runs. | read-only |
| `scripts/build_position_tags.py` | Build learned position-tag files. | read-only |
| `scripts/build_refined_citations.py` | Build versioned second-pass case citations. | insert-only; overwrites data |
| `scripts/build_statute_demand_report.py` | Report statute and instrument demand. | read-only |
| `scripts/build_treatment_distillation.py` | Distill treatment labels from review artifacts. | read-only |
| `scripts/build_treatment_review_packet.py` | Build treatment review files. | read-only |
| `scripts/build_treatment_teacher_fixture.py` | Build a treatment annotation fixture. | read-only |
| `scripts/chat_demo.py` | Run an opt-in, localhost-only Ollama chat demo. | read-only; local model |
| `scripts/check_argument_lists.py` | Score arguments in an exported case-frame list. | read-only |
| `scripts/check_generated_docs.py` | Check generated documentation against its sources. | read-only |
| `scripts/check_saved_searches.py` | Evaluate saved searches and optionally persist alerts. | insert-only; overwrites data |
| `scripts/check_site_tour.py` | Exercise the site tour in a browser. | read-only; network |
| `scripts/check_tour_window.py` | Walk through the site-tour window in a browser. | read-only; network |
| `scripts/chunk_cases.py` | Create canonical case chunks, optionally replacing existing chunks. | insert-only; overwrites data |
| `scripts/classify_case_types.py` | Classify decisions with deterministic rules. | insert-only; overwrites data |
| `scripts/classify_fc_activity.py` | Classify Federal Court Activity records and optionally persist results. | insert-only; overwrites data |
| `scripts/compare_eval_runs.py` | Compare two model-evaluation runs. | read-only |
| `scripts/compare_pipeline_case.py` | Compare one case across pipeline-derived layers. | read-only |
| `scripts/crawl_canlii.py` | Crawl CanLII case pages and cited cases into local JSONL/checkpoint files. | read-only (DB); network |
| `scripts/curate_a2aj_cases.py` | Select and import 25 FC refugee-risk evaluation cases. | insert-only |
| `scripts/curate_a2aj_immigration_cases.py` | Select and import an FC immigration dataset. | insert-only |

## Bugs

- **High — `scripts/chunk_cases.py:936-953`.** The case-ID path runs before the dry-run check, and `args.replace_existing or True` is always true. Therefore `--dry-run --case-id ...` still deletes and rebuilds chunks, even without `--replace-existing`. Handle dry-run before either write path and pass the flag through without `or True`.
- **Medium — `scripts/crawl_canlii.py:645-649`.** The JSONL record is appended before the checkpoint is updated. A stop/crash between those operations leaves the citation eligible for retry and can duplicate the output row. Make output idempotent by a stable key or reconcile the output file when resuming.
- **Medium — `scripts/crawl_canlii.py:578-582`.** An invalid seed URL is marked `skip` and saved to the checkpoint before the `--dry-run` branch. Keep dry-run read-only by deferring checkpoint updates until an actual run.
- **Medium — `scripts/audit_fc_activity_motion_unknowns_openai.py:122-153,168-180`.** On resume, projected cost covers only pending batches, not checkpoint `spent_usd`; the actual-spend check occurs only after a request has already been billed. Include prior spend and a conservative per-request maximum in preflight, or remove the OpenAI call under current policy.
- **Medium — `scripts/audit_fc_activity_openai.py:155-169`.** The configured budget is compared with estimated cost only after the OpenAI response, so it is not a hard pre-call cap. Use a conservative token-based preflight ceiling or remove the provider call under current policy.
- **Low — `scripts/a2aj_case_importer.py:206,211-226`.** The help text advertises an `import` action, but only `assess` invokes work; other arguments print usage. Make this explicitly assessment-only or dispatch the advertised import command.

## Data-safety risks

- **High — `scripts/backfill_case_metadata_outcomes.py:34-49`.** The script has no dry-run/apply option and replaces the entire `reader_extracted` object for every full-text case. It has no undo file or before/after row counts. Add a dry-run default, an expected-count/apply gate and a backup; merge only intended fields so existing extracted values are not silently lost.
- **High — `scripts/backfill_case_tags_v3.py:38-60`.** Normal execution writes unless `--dry-run` is supplied; `--retag` deletes all current-version tags and statuses without a backup or undo path. Make apply explicit, generate an undo artifact before deletion, and report planned and actual counts. The dry-run check does precede this delete in the in-scope entry point.
- **High — `scripts/acquire_case_html.py:122-147,157-188`.** The default is a live fetch/write run (`--dry-run` is opt-in), selects up to 1,000,000 cases when no limit is supplied, and replaces `Case.source_html` and snapshot metadata even when HTML already exists unless `--missing-html-only` is set. Require explicit apply, cap or require `--limit`, and preserve a prior snapshot/undo path. Also clarify that current `--dry-run` still fetches and appends quarantine records.
- **High — `scripts/backfill_judge_profiles.py:46-80,83-130,141-153`.** `--dry-run` is opt-in, so the default backfill writes; `--merge-duplicates` can relink and delete duplicate profiles, with no undo artifact or expected-count gate. Make writes explicit and preserve deleted profiles/links for a verified undo.
- **Medium — `scripts/backfill_case_outcomes.py:19-31,54-61`.** The CLI writes unless `--dry-run` is supplied and has no undo path. It also defaults to selecting up to one million cases in one materialized list. Make apply explicit, use keyset batches and add a row-count/undo plan.
- **High — `scripts/backfill_rpd_header.py:64-67,84-97`.** This script explicitly updates RPD cases, outside the stated FC/SCC/FCA scope. Do not run it under this project scope; exclude RPD from any shared backfill invocation or move it behind a separate approved workflow.
- **Medium — all-court selection paths:** `scripts/backfill_case_metadata_outcomes.py:34-38`, `scripts/backfill_case_outcomes.py:25-31`, `scripts/backfill_case_tags_v3.py:67-73`, `scripts/backfill_judge_profiles.py:83-88`, `scripts/acquire_case_html.py:130-136`, `scripts/chunk_cases.py:832-845`, `scripts/classify_case_types.py:53-59`, `scripts/build_case_fingerprints.py:31-58`, `scripts/build_refined_citations.py:161-168`, `scripts/build_paragraph_cited_by.py:29-32`, `scripts/backfill_statute_instrument_keys.py:30-35`, and `scripts/backfill_statute_provisions.py:29-37` have no enforced FC/SCC/FCA-only boundary; several default to all courts. They can therefore process RPD/RAD records if such rows are present. Add a shared court allowlist at the query boundary and reject unfiltered runs where appropriate. `scripts/backfill_panel_judges.py:59-64,98-104` also accepts arbitrary court values, although its default is SCC. `scripts/apply_judge_aliases.py:39-76,159-187` proposes and writes aliases across all profiles, including groups flagged as cross-court.
- **Medium — `scripts/apply_judge_aliases.py:135-138` and `scripts/classify_case_types.py:46-49`.** `--revert` deletes every rule alias or every current-taxonomy label, respectively, without a dry-run/count confirmation or undo file. Require a printed preview and expected count, and preserve an undo artifact before committing.
- **Medium — `scripts/build_refined_citations.py:143-160`.** `--revert --yes` permanently deletes the version’s refined rows and statuses without a backup or pre-delete preview. Add an export/undo path and show the matching counts before confirmation.
- **High — `scripts/curate_a2aj_cases.py:42-70` and `scripts/curate_a2aj_immigration_cases.py:356-394,397-450`.** Both import rows marked `a2aj_unverified` directly into canonical `Case` records with no default dry-run; the second has an opt-in `--dry-run`, while the first has none. They print selected/imported totals only after processing and provide no undo artifact. Keep unverified source rows staged until vetted, and add a plan-only default, expected-count gate and reversible import manifest.

## Security risks

- **High — `scripts/adjudicate_fc_metadata.py:10,108-117,133-145`; `scripts/audit_fc_activity_openai.py:13-14,145-160`; `scripts/audit_fc_activity_motion_unknowns_openai.py:12-13,142-153,168-180`.** These scripts call OpenAI. `adjudicate_fc_metadata.py` sends decision text even without `--apply`; that flag only controls database writes. OpenAI is prohibited by the project rules, so remove/disable these provider calls and use a permitted non-AI review path. The key names read by this scope are `OPENAI_API_KEY`, `GITHUB_TOKEN`, and `GH_TOKEN`; the latter two are used by `build_changelog.py:64-70` for GitHub API access.
- **Medium — `scripts/crawl_canlii.py:424-440,448-454`.** The crawler impersonates a desktop Chrome browser, hides `navigator.webdriver`, waits through Cloudflare challenge pages, and errors only if the challenge remains. Remove anti-detection behavior and stop immediately when challenged; use an access method permitted by the source.
- **Medium — `scripts/acquire_case_html.py:56-70`.** The initial source host is allowlisted, but redirects are followed without validating the destination. A redirect from an allowed host could send the worker to an unintended host. Disable redirects or validate every redirect target before fetching it.
- **Possible, medium — `scripts/crawl_canlii.py:570-575`.** Any input beginning with `http` is accepted as a browser URL; the destination is not restricted to CanLII. An untrusted citation file could make the browser request an internal or unrelated host. Require HTTPS and an explicit CanLII hostname allowlist.
- **Possible, medium — `scripts/agent_harness.py:196-200` and `scripts/agent_policy.py:20-27`.** The harness executes caller-supplied commands but does not consult the separate policy helper, and its timeout defaults to `None`. If the harness is intended to enforce that policy, call it before execution and require a bounded timeout.

## Performance

- **Medium — `scripts/analyze_unlinked_citations.py:150-155`.** The read-only analysis sets `statement_timeout` to `0` before full-table counts and scans, allowing queries to run without a database time limit. Use a bounded timeout and expose a resumable/capped scan.
- **Medium — `scripts/benchmark_citation_resolution.py:68-73,209-225`.** The benchmark materializes the full target inventory and linearly scans it for every alias term. `--limit` bounds source cases, not targets, so runtime can grow roughly with targets × citation terms. Build indexed citation/title lookups and document or cap target inventory size.
- **Medium — `scripts/agent_harness.py:196-200,237-240`.** A command can run indefinitely when `--timeout` is omitted. Give command execution a conservative default and retain an explicit, validated override.
- **Possible, low — `scripts/adjudicate_fc_metadata.py:65-73,113-117`.** The OpenAI client has no explicit request timeout and loops over the requested case limit. If this script is retained for an allowed provider, set a timeout and bound request count; under current policy, remove the API call instead.

## Dead code / cleanup

- **Low — `scripts/crawl_canlii.py:397-405`.** `build_scraper()` is not called; the active path uses `BrowserSession`. The helper references `cloudscraper` without importing it and would fail if called. Remove it or make it a tested, supported fetch path.

## Suggestions

- Standardize every database writer on plan-only by default, explicit `--apply`, a positive bounded limit, expected-count confirmation, before/after counts and an undo artifact for updates/deletes.
- Enforce the FC/SCC/FCA allowlist inside each query, not only in example commands; reject unfiltered and out-of-scope court values.
- Keep API calls, local-file outputs and database writes as separate modes. Under the present policy, do not retain an OpenAI `--send` escape hatch.
- Run targeted tests for the two dry-run defects before changing either script; this report itself is static and includes no test or runtime claims.
