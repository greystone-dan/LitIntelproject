# Code review 3/11 — judges, outcomes, metadata, analytics, FC activity

Reviewed: 2026-10-24  
Baseline: latest fetched `main`, commit `d2bcb41`  
Scope: Federal Court (FC), Federal Court of Appeal (FCA), and Supreme Court of Canada (SCC).

## Summary and method

The main risks are judge identities being merged or activity being assigned by surname/initial alone, inconsistent handling of non-binary outcomes, and FC activity/statute queries whose filters or bounds do not match the result they claim to summarize. Recommendations below are source-review findings, not measurements of live data.

Read all 21 requested modules: `backend/judge_aliases.py`, `backend/judge_normalization.py`, `backend/judge_fc_activity.py`, `backend/judge_issue_record.py`, `backend/metadata.py`, `backend/metadata_outcomes.py`, `backend/metadata_subjects.py`, `backend/outcome_checker.py`, `backend/analytics_service.py`, `backend/fc_activity.py`, `backend/fc_activity_insights.py`, `backend/position_holder.py`, `backend/position_tags.py`, `backend/learned_positions.py`, `backend/statute_consideration.py`, `backend/statute_sections.py`, `backend/statute_versioning.py`, `backend/statutes.py`, `backend/instrument_resolver.py`, `backend/theme_discovery.py`, and `backend/issue_match.py`. No in-scope file was left unread.

This was a read-only source review. No database, live service, external model, or secrets were accessed; no runtime data or query plans were inspected. The reported stored headline/`case_outcomes` discrepancy cannot be verified from source alone: both current projections call `_decide`, so no same-input divergence was identified. Conditional findings are marked **possible**. `git diff --check` was clean; the generated-document check could not run because FastAPI and SQLAlchemy are unavailable in this environment. Tests and CI were not run.

## Bugs

1. **Medium — overlapping FC/FCA service dates can merge different judges.** `backend/judge_normalization.py:263-271` allows a bare FCA name to join an FC cluster when either date-range comparison is within 366 days. The first comparison accepts overlapping dates, and the second also accepts the reverse ordering (FCA service before FC service), despite the stated requirement at lines 224-227 that FC service end before FCA service starts. For example, an FC Simon Noël range ending during Marc Noël’s FCA range can satisfy the first condition and cause the surname-only `Noël J.A.` records to join Simon’s profile. Require FC-before-FCA non-overlap, with any tolerance applied only to the gap.

2. **Medium — same-initial judges can both receive an ambiguous FC activity row.** In `backend/judge_fc_activity.py:18-26,41-55`, conflicts compare only initials, and an initial-only row such as `S. Noël` is accepted for each profile whose given name starts with S. Distinct profiles such as Simon Noël and Sophie Noël are not treated as rivals, so the same activity can inflate both judges’ counts and rates. Treat distinct full given names as conflicting and leave an initial-only row unmatched when it cannot distinguish the profiles.

3. **Medium — the FC dashboard motion query uses a scalar subquery for a cohort.** `backend/fc_activity_insights.py:642-648` embeds the filtered summary-ID query as a scalar subquery inside `IN`. With more than one matching summary ID, PostgreSQL can raise a cardinality error instead of returning motions for the cohort. Use the already-filtered `case_ids` as the motion source IDs, or use a set-valued subquery directly.

4. **Medium — judge motion counts ignore the selected decision body.** `backend/fc_activity_insights.py:214-225,268-275` includes `decision_body` in the judge endpoint’s filters and applies it to leave/merits summary queries, but the motion query filters only by year. A decision-body selection can therefore show motion/stay counts and rates from other cohorts. Restrict motions to source cases in the same filtered summary cohort.

5. **Medium — statute consideration omits older references with no structured section.** `backend/statute_consideration.py:123-130` matches only `StatuteReference.provision_section`. The section library explicitly falls back to the section number in `pinpoint` when that column is empty (`backend/statute_sections.py:35-38`). An in-scope reference such as a legacy IRPA pinpoint `34(1)(f)` with an empty `provision_section` can consequently be absent from consideration totals and case lists. Use the same null-safe fallback expression in both paths, or backfill and verify legacy rows.

6. **Medium — withdrawal can produce a named winner despite an undetermined merits result.** In `backend/metadata_outcomes.py:852-868`, `withdrawn` falls through to government outcome `undetermined` but still assigns `case winner`/`case loser` from the government role. `derive_outcome_detail` separately treats every non-allowed label as an applicant loss at lines 898-904. For a withdrawn FC application with the government as respondent, the metadata winner is the applicant while the dedicated outcome record names the respondent as winner. Preserve `withdrawn` as the disposition, but leave winner/loser unset and outcome status undetermined in both projections.

7. **Possible, medium — bilingual FC parquet rows can collapse to a year-only identity.** `normalize_hf_case_record` handles `citation_en`/`citation_fr`, `name_en`/`name_fr`, and bilingual date fields (`backend/fc_activity.py:147-195`), but `load_hf_fc_activity_rows` calls `normalize_fc_activity` directly (`:277-279`). That path reads only unilingual identity fields when building its source key (`:54-75,211-225`). If input rows contain only bilingual names/citations and a year, different cases can receive the same year-only key and later rows are discarded as duplicates. Normalize each parquet row through the bilingual-aware helper before case-key deduplication.

8. **Possible, medium — year analytics can raise when null and known years coexist.** `backend/analytics_service.py:833-841` converts digit-only x-values to integers but leaves `"Unknown"` as a string in the sort key. For `x="year"`, a result containing both a known year and a null year attempts to compare `int` and `str`, raising `TypeError`. Use consistently typed sort keys, such as `(0, int(value))` and `(1, value)`.

## Data-correctness risks

1. **Medium — the same “outcome status” field name has opposite orientations.** `_derive_outcome_fields` sets metadata `"outcome status"` to the government result (`backend/metadata_outcomes.py:852-868`), while `build_case_outcome` stores `CaseOutcome.outcome_status` from the applicant result (`:898-929`). With the government as respondent and an application allowed, the metadata status is `lost` and the dedicated record’s status is `won`. Make the orientation explicit in the field names or use one shared definition; otherwise readers and analytics can interpret the same label as contradictory.

2. **Medium — a combined “median” is an average of subgroup medians.** `backend/judge_fc_activity.py:60-74` rebuilds counts/rates when several activity-name rows are combined, but computes `median_days_hearing_to_judgment` as a weighted average of each row’s median. A weighted average of medians is not the median of the underlying decisions. Retain decision-level durations for the combined profile and calculate the median from them, or rename/document the aggregate as an estimate.

3. **Possible, medium — explicit federal act citations can remain unresolved for SCC decisions.** `backend/instrument_resolver.py:155-160,179-202` strips the federal citation tail before alias lookup. Bare `"privacy act"` is court-scoped to FC/FCA/FCT, while the SCC-specific map contains only `"supreme court act"`. Thus an SCC reference explicitly citing `Privacy Act, R.S.C. 1985, c. P-21` can normalize to an unresolvable bare name. Preserve the citation’s jurisdiction evidence or recognize the explicit federal citation before stripping it.

4. **Medium — annual outcome rates hide the excluded population.** `backend/analytics_service.py:394-435` calculates rates only from `government outcome` values `won` and `lost`, but does not return the all-decision or unclassified/mixed count. The chart can expose the classified denominator, but not how much of that year’s population it excludes. Return coverage counts alongside rates and make the excluded/mixed population visible before comparing years.

5. **Medium — judge profiles count known mixed outcomes as unclassified.** `backend/analytics_service.py:325-340` increments `unclassified` for every value other than `won` or `lost`, including the explicit `mixed` government outcome. The issue-outcome path distinguishes mixed as `other` (`backend/judge_issue_record.py:57-71`). A judge’s profile can therefore understate outcome coverage and label a known mixed ruling as unclassified. Add a separate mixed/other count while keeping it out of the binary win-rate denominator.

## Security risks

No confirmed security vulnerability was identified in the requested modules. `backend/outcome_checker.py` builds an excerpt-based second-opinion prompt; this review did not inspect or invoke any external provider caller.

## Performance

1. **Medium — statute consideration loads and aggregates all matching rows before pagination.** `backend/statute_consideration.py:123-145,164-169` materializes every matching occurrence and outcome, builds all decisions in Python, and only then slices to a page of at most 50. It also calls the version helper per displayed row; `backend/statute_versioning.py:31-43` can issue two queries per call. Large sections can therefore require unbounded memory and up to roughly 100 extra queries for one page. Aggregate/page decisions in SQL where possible and batch-load outcomes and statute versions.

2. **Low — each judge-issue request materializes the full FC baseline.** `backend/judge_issue_record.py:126-135` loads every non-excluded FC decision and loops over its stored issues to build baselines, although the response only needs counts for issues already visible for the requested judge. Keep the all-FC denominator as a SQL count and aggregate only relevant issue labels in SQL or in a bounded result set.

## Dead code / cleanup

**Low — province timeline aggregation is computed and discarded.** `backend/analytics_service.py:608-628` builds `province_counts` and `province_rows`, but the response hardcodes `"province_rows": []` at line 643. If the empty field is intentional compatibility behavior, remove the unused calculation; otherwise return the computed rows and cover the response.

## Suggestions

**Low — apply minimum sample guidance per FC activity rate, not across any one category.** `backend/fc_activity_insights.py:283-310` includes a judge when any of leave, JR, or motion decisions reaches `min_decisions`, while returning each category’s rate independently. A judge with many motions but only one leave decision can therefore show a leave rate based on one case. Keep the counts, but suppress or visibly qualify each rate below its own minimum denominator.
