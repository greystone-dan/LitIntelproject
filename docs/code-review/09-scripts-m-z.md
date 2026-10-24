# Code review 9/11 — scripts m–z and service scripts

**Review date:** 2026-10-24
**Base:** `main` at `d2bcb41ea1e424024fabd3bc5c19028d75ebf6e2`
**Scope:** All 68 regular files directly under `scripts/` whose names begin m–z, plus all six files in `scripts/service/`. All 74 files were read; none were skipped. This was a source-only review: no script, database, network request, or paid API was run.

## Summary

The most serious issues are that `--retag --dry-run` deletes and commits tag data, several mutating jobs are not restricted to FC/FCA/SCC and can include RPD/RAD, and service cleanup kills processes without establishing ownership. Several scripts can also send data to OpenAI despite the project’s no-OpenAI rule; estimates in a number of paid paths are not hard spend limits. Other findings concern recovery files, resume state, output paths, and unbounded reads.

In the table, **DB read-only** means the script only reads the database; **DB insert-only** means it adds rows; **DB overwrite** includes update/delete/truncate or other replacement; **file overwrite** means it creates or replaces local output/state. Conditional flags identify opt-in or delegated behavior.

## Script inventory and risk flags

| Script | One-line purpose | Risk flags |
|---|---|---|
| `scripts/map_fc_seed_to_local_cases.py` | Match seed rows to local cases and export the mapping. | DB read-only; file overwrite. |
| `scripts/measure_refined_pinpoints.py` | Compare stored and newly refined citation pinpoint metrics. | DB read-only; optional file overwrite. |
| `scripts/merge_argument_lists.py` | Merge argument lists using sentence-transformer similarity. | File overwrite; possible model-weight download. |
| `scripts/package_discussion_units_llm.py` | Prepare or send a discussion-unit model request and save results. | File overwrite; spends money / reads keys with `--send`. |
| `scripts/plan_self_citation_cleanup.py` | Classify self-citation candidates without changing database rows. | DB read-only; optional file overwrite. |
| `scripts/populate_fc_gold_case_ids.py` | Add mapped case IDs to the FC gold CSV. | File overwrite; defaults to replacing its input. |
| `scripts/prepare_discussion_units_cohort.py` | Build reports and model-request files for a fixed cohort. | DB read-only; file overwrite; creates ledger if absent. |
| `scripts/prepare_treatment_teacher_batch.py` | Prepare a teacher request and estimate its cost. | File overwrite; no API call or key read in this script. |
| `scripts/profile_reader.py` | Profile reader-data construction and the HTTP route. | DB read-only; writes profiling output; HTTP GET. |
| `scripts/quick_search_engine.py` | Embed a query and search local case-chunk embeddings. | DB read-only; spends money / reads OpenAI key. |
| `scripts/reacquire_source_html.py` | Fetch and validate source HTML, optionally saving snapshots and provenance. | Network GET; DB read-only by default; DB overwrite/insert with `--apply`; file overwrite. |
| `scripts/rebuild_citations_controlled.py` | Rebuild citation rows for a bounded cohort with recovery artifacts. | DB read-only by default; DB overwrite only with confirmed `--apply`; file overwrite. |
| `scripts/recompute_citation_metrics.py` | Preview sample metrics or recompute stored metrics. | DB read-only by default; DB overwrite with `--apply`. |
| `scripts/reextract_statute_references.py` | Compare, replace, or restore statute-reference rows. | DB read-only by default; DB overwrite with confirmed apply/restore; writes backup/detail files. |
| `scripts/refresh_recent_5000_artifact.py` | Preview or refresh the derived recent-case embedding table. | DB read-only by default; DB overwrite with `--apply` and confirmation. |
| `scripts/refresh_site.ps1` | Stop local site/tunnel processes and restart them. | Process control; file/log writes. |
| `scripts/regenerate_docs.py` | Regenerate generated references and synchronize the backend inventory. | Generated-file overwrite. |
| `scripts/remove_redundant_judge_links.py` | Identify and remove redundant FC/FCA judge links, with undo support. | DB read-only by default; DB overwrite with `--apply`; recovery file. |
| `scripts/remove_self_case_citations.py` | Find and delete self-caption citation rows. | DB read-only by default; DB overwrite with `--apply`; no recovery export. |
| `scripts/remove_self_citations.py` | Export and optionally delete exact citation self-links. | DB read-only by default; DB overwrite with `--apply`; export file overwrite. |
| `scripts/repair_glued_word_sections.py` | Correct statute sections inferred from glued text. | DB read-only by default; DB overwrite with apply/undo; undo-file overwrite. |
| `scripts/repair_range_word_sections.py` | Correct statute sections misread from ranges or lists. | DB read-only by default; DB overwrite with `--apply`; no undo file. |
| `scripts/report_fc_activity_coverage.py` | Produce Federal Court Activity coverage metrics. | DB read-only; refuses to replace an existing output. |
| `scripts/report_fc_activity_motion_unknowns.py` | Summarize unknown motion-event patterns from a JSON report. | File overwrite; no DB/API access evident. |
| `scripts/report_incomplete_short_form_anchors.py` | Report incomplete anchors for unresolved short citations. | DB read-only; optional file overwrite. |
| `scripts/report_unresolved_citation_shapes.py` | Group unresolved citations and report resolution signals. | DB read-only; optional file overwrite. |
| `scripts/resolve_citation_targets.py` | Link unresolved citations to local cases. | DB read-only with `--dry-run`; otherwise DB overwrite (dry-run is opt-in); optional log append. |
| `scripts/resolve_short_citation_targets.py` | Link stored case names and short forms to candidate authorities. | DB read-only with `--dry-run`; otherwise DB overwrite (dry-run is opt-in). |
| `scripts/resplit_paragraph_chunks.py` | Replace paragraph chunks and rebase related references and indexes. | DB read-only by default; DB overwrite with apply/undo; recovery/output-file overwrite. |
| `scripts/review_fc_activity_local.py` | Review one Activity entry with the configured text-generation provider. | File overwrite; provider may be external/read credentials (configuration-dependent). |
| `scripts/run_case_intelligence_request.py` | Submit a case-intelligence request and save the response. | Hosted default spends money / reads key; file overwrite. |
| `scripts/run_citation_rebuild_progress.py` | Launch citation rebuilds in batches and report progress. | Delegated DB overwrite when child apply is enabled; state/output writes. |
| `scripts/run_discussion_units_cohort.py` | Run a manifest of cases through a discussion-unit runner. | Delegated file/ledger overwrite; spends money / reads keys if `--send` is used. |
| `scripts/run_fc_activity_openai_structured_pilot.py` | Prepare or submit a sampled FC Activity extraction pilot. | DB read-only; spends money / reads key with `--send`; checkpoint/output overwrite. |
| `scripts/run_jobs.py` | Run configured interval jobs in a separate process. | Conditional delegated writes, network access, or key use. |
| `scripts/run_live_analysis_mocks.py` | Score synthetic live-analysis documents, optionally resolving against the library. | DB read-only when enabled; no direct DB write or paid call evident. |
| `scripts/run_local_paragraph_summary_baseline.py` | Generate bounded paragraph summaries and save a report. | DB read-only; file overwrite; provider may spend money/read keys depending on configuration. |
| `scripts/run_local_with_tunnel.ps1` | Start the local API and Cloudflare tunnel, or tunnel to an existing API. | Starts network-facing processes; CLI credentials may be configured externally. |
| `scripts/run_model_paragraph_experiment.py` | Send selected case text to OpenAI for segmentation and analysis. | DB read-only; spends money / reads key; report and ledger overwrite. |
| `scripts/run_outcome_checker.py` | Preview outcome-check costs or send confirmed requests and record results. | DB read-only; spends money / reads key with confirmation; output append. |
| `scripts/run_overnight.py` | Run or resume selected acquisition, enrichment, pipeline, or test jobs. | State overwrite; delegated DB/network/key effects depend on selected jobs. |
| `scripts/run_position_tags_library.py` | Export position tags for eligible library cases. | DB read-only; per-case and summary file overwrite; selection includes RPD/RAD/IAD. |
| `scripts/run_scc_text_only.py` | Run SCC text-only processing with per-case state. | DB overwrite by default; state-file overwrite. |
| `scripts/run_treatment_teacher_batch.py` | Send teacher batches to OpenAI and save validation results. | Spends money / reads key; output-file overwrite. |
| `scripts/run_v2_pipeline.py` | Run or resume selected case-processing stages. | DB overwrite by default; state/report overwrite; source-network access. |
| `scripts/run_v2_pipeline_case.py` | Fetch one case’s source HTML, process it, and write comparisons. | DB overwrite; network GET from case URL; report overwrite. |
| `scripts/run_v2_text_only_fast.py` | Run processing stages for non-SCC cases and save state. | DB overwrite by default; state-file overwrite. |
| `scripts/sample_pinpoint_forms.py` | Read parquet decisions and report pinpoint shapes/parser matches. | Source read; no DB write, paid API, or key use evident. |
| `scripts/sample_statute_extraction.py` | Sample database cases, extract statute references, and write JSONL. | DB read-only; output-file overwrite. |
| `scripts/scheduled_intake_daemon.py` | Periodically discover A2AJ decisions and log intake runs. | Network access; DB insert for run records; logs append; admits RAD/RPD. |
| `scripts/score_position_holder.py` | Score position-holder predictions against labels or a review sheet. | Input read; optional output-file overwrite. |
| `scripts/score_search_gold.py` | Score search results against configured gold queries. | DB read-only; optional output-file overwrite. |
| `scripts/search_gold_queries.json` | Store gold queries and expected citations/oracle patterns. | Static input; no execution side effects. |
| `scripts/seed_tour_fixture.py` | Add synthetic tour cases, process them, and run follow-up scripts. | DB insert and delegated DB overwrite; requires `--yes`; subprocess side effects. |
| `scripts/select_discussion_unit_cohort.py` | Select a bounded cohort using priority IDs and inbound citations. | DB read-only; output-file overwrite. |
| `scripts/setup_cloudflare_tunnel.ps1` | Create or route a Cloudflare tunnel and write its config. | Config overwrite; Cloudflare CLI authentication is local/external. |
| `scripts/start_remote_control.ps1` | Start a Claude Remote Control session. | Starts a CLI; credential/billing behavior is external and configuration-dependent. |
| `scripts/study_name_only_context.py` | Report context for unlinked name-only citations. | DB read-only; output-file overwrite. |
| `scripts/tag_cases.py` | Insert deterministic tags and tagging-status rows for pending cases. | DB insert normally; DB overwrite/delete with `--retag`; dry-run is opt-in. |
| `scripts/tag_cases_v2.py` | Apply the V2 tagger to pending cases. | DB insert normally; DB overwrite/delete with `--retag`; dry-run is opt-in. |
| `scripts/tag_cases_v3.py` | Apply the V3 tagger to pending cases. | DB insert/status overwrite; DB delete with `--retag`; dry-run is opt-in. |
| `scripts/top_unlinked_cited.py` | Rank unlinked case citations by frequency and gap category. | DB read-only; output CSV overwrite. |
| `scripts/train_learned_positions.py` | Train position-tag weights and optionally save them. | Training-input read; model-file overwrite with `--write`; input includes RAD/RPD/IAD. |
| `scripts/train_learned_roles.py` | Train paragraph-role weights. | Model-file overwrite by default. |
| `scripts/train_role_correction.py` | Train role-correction weights and report metrics. | Training-input read; model-file overwrite with `--write`. |
| `scripts/unlink_impossible_citation_targets.py` | Find, unlink, log, or restore impossible citation targets. | DB read-only by default; DB overwrite with explicit apply; undo log; default courts FC/FCA/SCC. |
| `scripts/verify_citation_extraction.py` | Audit extracted citations from fixtures or sampled database cases. | DB read-only; report overwrite; optional OpenAI spend/key use. |
| `scripts/verify_fc_case_existence.py` | Check case numbers against external Federal Court endpoints. | External requests; output-file overwrite and possible input deletion if paths match. |
| `scripts/service/install_daily_intake.ps1` | Register the daily intake scheduled task. | Task registration/overwrite; no configured retry policy. |
| `scripts/service/install_site_service.ps1` | Register and start the site supervisor task. | Task registration/overwrite; stops/starts task. |
| `scripts/service/run_daily_intake.ps1` | Run an intake pass and log output. | Starts Python job; log-file overwrite/append; fixed venv path. |
| `scripts/service/run_site.ps1` | Supervise the app and Cloudflare tunnel. | Starts/stops processes; log-file overwrite/append; broad process termination. |
| `scripts/service/uninstall_daily_intake.ps1` | Stop and unregister the intake task. | Task stop/unregister. |
| `scripts/service/uninstall_site_service.ps1` | Remove the site task and stop matching processes. | Task stop/unregister; broad process termination. |

## Bugs

- **High — false import accounting:** `scripts/scheduled_intake_daemon.py:276-284` discovers A2AJ records but does not import them; in normal mode it nevertheless records `records_imported=discovered`. Implement and verify ingestion before recording imports, or report zero and label this discovery-only.
- **High — intake lock is not exclusive:** `scripts/scheduled_intake_daemon.py:70-110` uses temp-file replacement, so simultaneous daemons can both replace the lock and proceed. It also clears old locks without checking whether the recorded PID is alive or refreshing the lock. Use exclusive creation, verify process liveness, and adopt a safe heartbeat/stale-lock policy.
- **Medium — retry state suppresses V2 timeouts:** `scripts/tag_cases_v2.py:47-59,99-105` writes a status for a timed-out case, while the pending query excludes any existing status for that taxonomy. Subsequent runs can therefore skip failed cases permanently. Exclude only successful statuses or add an explicit retry/reset path.
- **Medium — rollback can leave false completion state:** `scripts/run_v2_text_only_fast.py:59-70` records completed cases before the batch commit. If a later case fails, the rollback can undo earlier work while their state remains completed. Commit per case or reset uncommitted cases to pending before persisting state.
- **Medium — citation rebuild can resume past an uncommitted case:** `scripts/rebuild_citations_controlled.py:297-309,321-326` appends comparison evidence before validation and commit. If validation fails, recovery at `:128-155` can treat that comparison as completed despite the rolled-back DB transaction. Record completion only after commit and reconcile/ignore comparisons lacking a committed checkpoint.
- **Medium — case-ID filter is not consistently applied:** `scripts/verify_citation_extraction.py:545-547,760-767` treats an empty ID set as no filter and does not pass the CSV restriction to all chunk/existing-citation sampling paths. Apply the selection consistently or reject unsupported filter combinations.
- **Medium — input may be deleted as output:** `scripts/verify_fc_case_existence.py:229-238` removes an existing output before writing results. If input and output resolve to the same path, it deletes the source file. Reject identical resolved paths and write to a temporary output.
- **High — supervisor can stop unrelated processes:** `scripts/service/run_site.ps1:30-35,59-66` kills matching Python/Cloudflare processes without proving they belong to this service, and does not explicitly reap the surviving child when its sibling exits. `scripts/service/uninstall_site_service.ps1:5-11` and `scripts/refresh_site.ps1:7-25` also terminate broad process matches. Track child PIDs and executable paths, stop only owned children, clean up both siblings, and report failed termination.
- **Medium — scheduled-task installers can replace unrelated tasks:** `scripts/service/install_daily_intake.ps1:22-23` and `scripts/service/install_site_service.ps1:21-22` use `Register-ScheduledTask -Force`. Verify task ownership or require confirmation before replacing a task with the same name.
- **High — pipeline writes are the default:** `scripts/tag_cases.py:154-162`, `scripts/tag_cases_v2.py:122-131`, `scripts/tag_cases_v3.py:174-183`, `scripts/run_scc_text_only.py:126-138`, `scripts/run_v2_pipeline.py:173-194`, and `scripts/run_v2_text_only_fast.py:84-92` make dry-run opt-in; a normal invocation writes to the database. `scripts/run_v2_pipeline_case.py` has no dry-run option. Require an explicit `--apply`/confirmation after a default preview, and bound the cohort before writing.
- **Possible, medium — citation regex may not match whitespace:** `scripts/map_fc_seed_to_local_cases.py:110-112` passes `r"\\s+"` to PostgreSQL; depending on PostgreSQL regex interpretation this may match a literal backslash plus `s`, not whitespace. Use `r"\s+"` or `[[:space:]]+` and verify against PostgreSQL.
- **Possible, medium — rebased span may cross a chunk boundary:** `scripts/resplit_paragraph_chunks.py:279-289` rebases a reference’s old span length onto the new chunk containing its start. If the span crosses a new boundary, its end offset may exceed that chunk’s text. Verify the whole span fits before rebasing.
- **Low — capped spelling list stops counting existing spellings:** `scripts/top_unlinked_cited.py:81-82` stops updating a key after 20 distinct spellings, including spellings already in the summary. Continue incrementing existing keys after the distinct-spelling cap.
- **Low — p95 may be understated:** `scripts/score_search_gold.py:52` uses an index formula that falls below common nearest-rank percentiles for some sample sizes. Use and document a standard percentile convention.

## Data-safety risks

- **High — dry-run can delete tag rows:** `scripts/tag_cases.py:170-192`, `scripts/tag_cases_v2.py:134-143`, and `scripts/tag_cases_v3.py:186-195` delete current-taxonomy tag/status rows and commit for `--retag` before checking `--dry-run`. Thus `--retag --dry-run` is destructive. Move the dry-run/validation gate before all mutations or reject that option combination; add a recovery export before any retag delete.
- **High — mutating jobs can include excluded courts:** Several selectors are global or exclude only SCC rather than enforcing the permitted FC/FCA/SCC set. Examples include the optional/unrestricted court filters in `scripts/tag_cases.py:79-90,154-177`, `scripts/tag_cases_v2.py:129-145`, and `scripts/tag_cases_v3.py:181-203`; all-citation updates in `scripts/resolve_citation_targets.py:198-229,274-276` and `scripts/resolve_short_citation_targets.py:314-369`; all-case metrics in `scripts/recompute_citation_metrics.py:57-58`; all-text selection in `scripts/reextract_statute_references.py:132-139,249-289`; and the default pipelines in `scripts/run_v2_pipeline.py:110-117,182-194` and `scripts/run_v2_text_only_fast.py:41-47,90`. These can read or write RPD/RAD rows. Require an enforced court allowlist and reject out-of-scope IDs, including for case-ID/CSV inputs.
- **High — selected/global writers also lack a court guard:** `scripts/rebuild_citations_controlled.py:187-200` permits `--all` without a court predicate; `scripts/resplit_paragraph_chunks.py:198-215` accepts IDs/CSV selections; `scripts/run_v2_pipeline_case.py:23-40` processes a supplied case ID; and `scripts/refresh_recent_5000_artifact.py:26-47,50-63` selects the latest cases without filtering court. The global self-citation cleanup and statute-repair writers (`scripts/remove_self_case_citations.py:29-60`, `scripts/remove_self_citations.py:35-61`, `scripts/repair_glued_word_sections.py:31-40`, `scripts/repair_range_word_sections.py:27-33`) likewise do not scope rows by court. Apply the same allowlist to these selectors and their write paths.
- **High — explicit RPD/RAD inclusion:** `scripts/run_position_tags_library.py:10,33-49` selects RAD/RPD/IAD, `scripts/train_learned_positions.py:41` treats RAD/RPD/IAD as eligible inputs, and `scripts/scheduled_intake_daemon.py:225` admits RAD/RPD. `scripts/sample_pinpoint_forms.py:3` even documents an RPD sample input. Remove out-of-scope courts from selectors, training, and examples; do not treat an operator-supplied file as permission to expand project scope.
- **High — unreviewed deletes have no recovery path:** `scripts/remove_self_case_citations.py:67-78` deletes in committed chunks without an expected-count guard or export, so failure can leave a partial cleanup with no undo. Require a reviewed count, export exact rows/IDs first, and make the cleanup recoverable.
- **Medium — self-citation export can miss concurrently deleted rows:** `scripts/remove_self_citations.py:37-64` counts and exports matching rows, then deletes using a fresh predicate. A concurrent insert can be deleted without being in the recovery CSV; the export also opens with `"w"` and can replace an earlier backup. Protect the operation in a transaction, delete only exported IDs, and refuse to overwrite backups.
- **Medium — repair lacks undo:** `scripts/repair_range_word_sections.py:45-69` commits updates without preserving old values. Export a collision-protected undo file before applying.
- **Medium — recovery artifacts can be overwritten:** `scripts/repair_glued_word_sections.py:70-74` opens its default undo file with `"w"`; `scripts/resplit_paragraph_chunks.py:300-303` replaces existing per-case undo records. Fail on existing recovery paths or use unique run directories.
- **Medium — negative sample selects almost the whole corpus:** `scripts/reextract_statute_references.py:132-139,278-289` does not require `--sample` to be positive; `--sample -1` uses Python negative slicing and selects all but the last ID. Validate positive sample and batch sizes and enforce the intended limit for each selection mode.
- **Medium — default command overwrites source gold CSV:** `scripts/populate_fc_gold_case_ids.py:44-45,67-71` uses the input as output unless `--out-csv` is provided and writes non-atomically. Default to a separate output, require explicit in-place permission, and use temporary-file replacement.
- **Medium — model weights overwritten without opt-in:** `scripts/train_learned_roles.py:111-121` writes its weights unconditionally, unlike the other training scripts. Add a report-only default and explicit write flag.
- **Medium — all-row metric update has minimal guard:** `scripts/recompute_citation_metrics.py:41,54-58` gates a full metrics rewrite only on `--apply`; add an affected-row preview and an additional confirmation.
- **Low — intake task has no retry policy:** `scripts/service/install_daily_intake.ps1:18-23` sets a three-hour execution cap but no retry policy. Add bounded retries and verify the cap exceeds a normal run duration.
- **Low — service runtime paths and logs are fixed/unbounded:** `scripts/service/run_daily_intake.ps1:11-12,17-23` and `scripts/service/run_site.ps1:17-25,48-54` assume fixed venv/cloudflared paths and show no log rotation. Validate dependencies at install time or make paths configurable; rotate logs by age or size.
- **Medium — recent-5000 refresh has no restore artifact:** `scripts/refresh_recent_5000_artifact.py:66-98` defaults to preview and requires both `--apply` and a confirmation, and it reports pre/post counts. However, apply truncates the existing derived table and provides no backup/undo. Record a rebuild/restore procedure or preserve the prior rows before applying.
- **Possible, low — NULL dates may displace recent cases:** `scripts/refresh_recent_5000_artifact.py:29,55` sorts `date DESC`; PostgreSQL puts NULL dates first for descending order. If `cases.date` is nullable, undated rows can enter the recent-5,000 cohort. Use `NULLS LAST`.

## Security risks

- **High — OpenAI calls remain reachable despite the no-OpenAI rule:** API call paths exist in `scripts/package_discussion_units_llm.py:464-478`, `scripts/quick_search_engine.py:33-40`, `scripts/run_case_intelligence_request.py:20-23,103-159` (hosted is the default), `scripts/run_fc_activity_openai_structured_pilot.py:255-280`, `scripts/run_model_paragraph_experiment.py:190-211`, `scripts/run_outcome_checker.py:77-95`, `scripts/run_treatment_teacher_batch.py:269-273`, and `scripts/verify_citation_extraction.py:736,771-776`. Some require send/confirmation flags, but several still read `OPENAI_API_KEY` and submit data to a paid external service. Disable these paths until explicitly authorized; do not rely on an estimated budget as authorization.
- **High — API budgets are estimates, not hard caps:** `scripts/package_discussion_units_llm.py:399-400,464-478` does not use its declared budget to limit a request; `scripts/run_model_paragraph_experiment.py:174-197,211,240-260` does not enforce cumulative actual spend across up to 20 cases; `scripts/run_fc_activity_openai_structured_pilot.py:252-271,273-333` can have up to 10 requests in flight before costs are checked; `scripts/run_treatment_teacher_batch.py:190-202` checks estimates before the call; `scripts/run_outcome_checker.py:67-69,87-100` estimates 60 output tokens while allowing 200; and `scripts/verify_citation_extraction.py:436-466` continues based on estimated cost after receiving actual usage. Enforce a conservative per-call reservation and cumulative cap, or disable paid calls.
- **High — hosted provider runs by default:** `scripts/run_case_intelligence_request.py:103-107,142-159` defaults to hosted OpenAI and can submit as soon as a key is configured, without a separate `--send` confirmation. Default to local and require explicit, approved opt-in; enforce a hard spend limit.
- **Medium — query is sent to OpenAI without a send gate:** `scripts/quick_search_engine.py:33-40,87-94` embeds the supplied search query using OpenAI. Disable this path under the current policy or require explicit authorization and use a local embedding provider.
- **Medium — full case text can be sent to an audit:** `scripts/verify_citation_extraction.py:305-306,736,771-776` can send selected case material to OpenAI; `--audit-max-chars 0` removes the truncation. Enforce a hard maximum payload size and disable the paid audit unless approved.
- **Medium — source URL redirects are not revalidated:** `scripts/reacquire_source_html.py:68-73,86-88` checks the initial host but follows redirects; `scripts/run_v2_pipeline_case.py:23-40` fetches a case-stored URL without the equivalent host allowlist. Validate HTTPS scheme, host, and every redirect before fetching or accepting data.
- **Possible, medium — public tunnel lacks an access-control precondition:** `scripts/setup_cloudflare_tunnel.ps1:95-124` routes a public hostname to the local API without verifying that an access policy/authentication gate is enabled. Require and verify an access-control precondition before routing.
- **Possible, medium — configured review provider may be external:** `scripts/review_fc_activity_local.py` and `scripts/run_local_paragraph_summary_baseline.py:83-98,127-134` delegate to configurable providers. The provider’s network/key behavior was not established from these files. Make provider locality explicit and require a separate guard before any paid or external request.

## Performance

- **Medium — coverage report materializes broad data:** `scripts/report_fc_activity_coverage.py:43-52` loads all cases, documents, and classifications as ORM objects, including raw payloads. Stream/batch or aggregate in SQL.
- **Low — parquet limit does not limit input loading:** `scripts/sample_pinpoint_forms.py:116-120` reads the full parquet column before applying `--limit`. Read row groups/batches and stop once the limit is met.
- **Possible, medium — endpoint verifier has no default bound:** `scripts/verify_fc_case_existence.py:52-56,229-248` can check the entire input with retries. Require a limit or bounded batch size for large inputs.
- **Medium — cohort subprocess is not bounded:** `scripts/run_discussion_units_cohort.py:33-61` has no default case-count ceiling or subprocess timeout. Add both to limit runaway work and ensure interruption can be resumed safely.
- **Medium — paragraph-summary token request has no effective ceiling:** `scripts/run_local_paragraph_summary_baseline.py:83-98` accepts an unrestricted `--max-tokens` and may call a configured provider for up to ten paragraphs. Validate a maximum token count and add a spend guard for paid providers.

## Dead code / cleanup

- **Legacy citation job:** `scripts/run_overnight.py:106-120` labels its citation job legacy; the controlled replacement is `scripts/rebuild_citations_controlled.py`, which is intentionally separate from the standard overnight profile. Keep the legacy entry disabled or remove it after callers are confirmed.
- **Possible overlapping taggers:** `scripts/tag_cases.py`, `scripts/tag_cases_v2.py`, and `scripts/tag_cases_v3.py` are parallel versions; V3 describes itself as inactive at `scripts/tag_cases_v3.py:1`. Confirm the canonical runner and document or retire the others; the in-scope files alone do not establish a safe replacement.
- **Site-refresh fallback, not active service path:** `scripts/refresh_site.ps1` is retained as a fallback. `docs/CLOUDFLARE_TUNNEL_SETUP.md:8-12` says the `iLitSite` scheduled task is primary and the fallback must not run while that task is installed.
- No other in-scope file was confirmed dead or superseded from source review alone.

## Suggestions

1. Apply an enforced FC/FCA/SCC allowlist at the shared selection boundary, including for explicit case IDs, CSV files, training data, and delegated runners.
2. Default database mutators to dry-run, require explicit apply/confirmation for broad writes, and pair every destructive path with a protected backup/undo and before/after counts.
3. Disable OpenAI paths while the no-OpenAI rule is in effect; for any future approved paid provider, require explicit opt-in and a hard cumulative spend cap.
4. For PowerShell supervisors, track child PIDs and executable paths; stop only those children, clean up both siblings on failure, verify task ownership before replacement, and report stop/start failures.
5. Use unique, collision-protected recovery and output paths; make state/checkpoint writes atomic and ensure checkpoint status reflects committed database work.

## Coverage and validation

- All 74 in-scope files were read; none could not be finished. Findings are based on source inspection; providers, the live database, Cloudflare access policy, Windows Task Scheduler, and external services were not runtime-tested.
- GitHub’s run for the initial PR commit was `action_required` with zero jobs and no failed-job logs; that is not evidence of green CI. No CI failure was identified from that run.
- This report-only change does not alter code or tests. `git diff --check` is the relevant content check. `python scripts/check_generated_docs.py` could not complete in this environment because `fastapi` and `sqlalchemy` are not installed; no full test suite or browser check is applicable.
