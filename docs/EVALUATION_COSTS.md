# Evaluation Cost Ledger

Last generated: 2026-09-28T16:31:23.673997+00:00

This report aggregates one report-level recorded estimate per non-dry-run JSON artifact under `data/eval/`.
It is an estimated-cost ledger, not an OpenAI invoice or provider billing export.

## Measurement Method

- Fields are selected in this order: `spent_usd`, `actual_cost_usd`, `cost_usd`, `estimated_cost_usd`, `cost`.
- Artifacts with status `dry_run`, `dry_run_ready`, `prep`, or `request` are excluded from the total.
- Per-request artifacts under an `requests/` directory are excluded when a report-level artifact exists.
- Comparison artifacts ending in `_aggregate.json` are excluded because they restate earlier report costs.
- A `.checkpoint.json` artifact is excluded when its finalized non-checkpoint counterpart exists.
- Estimates use the rates recorded by each producing script; they are not retroactively repriced.

## Total

- Report-level artifacts: 86
- Recorded estimated spend: $4.042849 USD
- Excluded dry-run/preparation estimates: 14 artifacts / $0.271532 USD
- Unmeasured: runtime embedding calls, overnight operations without cost artifacts, and any provider billing not persisted in these reports.

## Artifacts

| Artifact | Cost field | Estimated USD |
| --- | --- | ---: |
| `citation_openai_audit_report.json` | `openai_audit.summary.spent_usd` | $0.000396 |
| `citation_sample_iteration1_ai_suggestions.json` | `cost_estimate.estimated_cost_usd` | $0.015931 |
| `discussion_units_external_review_v1_2_api_response.json` | `cost` | $0.006140 |
| `discussion_units_external_review_v3_api_response.json` | `actual_cost_usd` | $0.003774 |
| `discussion_units_external_review_v4_api_response.json` | `metadata.cost_usd` | $0.005314 |
| `fc_activity_openai_audit_20260925.json` | `usage.estimated_cost_usd` | $0.001548 |
| `fc_activity_openai_feedback_batch_20260927_seed1.json` | `usage.estimated_cost_usd` | $0.006995 |
| `fc_activity_openai_feedback_batch_20260927_seed2.json` | `usage.estimated_cost_usd` | $0.007001 |
| `fc_activity_openai_feedback_batch_20260927_seed3.json` | `usage.estimated_cost_usd` | $0.008316 |
| `fc_activity_openai_feedback_batch_20260927_seed4.json` | `usage.estimated_cost_usd` | $0.015017 |
| `fc_activity_openai_loose_pilot_100_20260928.json` | `spent_usd` | $0.038195 |
| `fc_activity_openai_loose_pilot_100_checkpoint_20260928.json` | `spent_usd` | $0.038195 |
| `fc_activity_openai_loose_pilot_100_smoke_20260928.json` | `spent_usd` | $0.000563 |
| `fc_activity_openai_loose_pilot_100_smoke_checkpoint_20260928.json` | `spent_usd` | $0.000563 |
| `fc_activity_openai_mini_loose_pilot_100_20260928.json` | `spent_usd` | $0.173650 |
| `fc_activity_openai_mini_loose_pilot_100_checkpoint_20260928.json` | `spent_usd` | $0.173650 |
| `fc_activity_openai_motion_review_20260928.json` | `usage.estimated_cost_usd` | $0.001456 |
| `fc_activity_openai_structured_pilot_100_20260928.json` | `spent_usd` | $0.039341 |
| `fc_activity_openai_structured_pilot_100_checkpoint_20260928.json` | `spent_usd` | $0.076582 |
| `fc_activity_openai_structured_pilot_100_compact_20260928.json` | `spent_usd` | $0.035072 |
| `fc_activity_openai_structured_pilot_100_compact_checkpoint_20260928.json` | `spent_usd` | $0.039341 |
| `fc_activity_openai_structured_pilot_100_schema_20260928.json` | `spent_usd` | $0.035574 |
| `fc_activity_openai_structured_pilot_100_schema_checkpoint_20260928.json` | `spent_usd` | $0.035574 |
| `fc_activity_openai_structured_schema_smoke_20260928.json` | `spent_usd` | $0.000266 |
| `fc_activity_openai_structured_schema_smoke_checkpoint_20260928.json` | `spent_usd` | $0.000266 |
| `fc_activity_openai_structured_smoke_1_20260928.json` | `spent_usd` | $0.000563 |
| `fc_activity_openai_structured_smoke_1_checkpoint_20260928.json` | `spent_usd` | $0.000563 |
| `fc_activity_openai_structured_smoke_1_compact_20260928.json` | `spent_usd` | $0.000247 |
| `fc_activity_openai_structured_smoke_1_compact_checkpoint_20260928.json` | `spent_usd` | $0.000247 |
| `five_case_citation_ai_triage_all_suggestions.json` | `cost_estimate.estimated_cost_usd` | $0.008905 |
| `five_case_citation_ai_triage_suggestions.json` | `cost_estimate.estimated_cost_usd` | $0.000530 |
| `llm_discussion_units_pilot/case_35868_paragraphs_0_9_qwen3_result.json` | `spent_usd` | $0.000000 |
| `llm_discussion_units_pilot/core_300_run/ledger.json` | `cases.62.spent_usd` | $0.002623 |
| `llm_discussion_units_pilot/mason_argument_citation_30_result.json` | `spent_usd` | $0.005731 |
| `llm_discussion_units_pilot/mason_argument_citation_all_result.json` | `spent_usd` | $0.029339 |
| `llm_discussion_units_pilot/mason_argument_citation_analysis_result.json` | `spent_usd` | $0.002612 |
| `llm_discussion_units_pilot/mason_argument_citation_compact_canary_result.json` | `spent_usd` | $0.003452 |
| `llm_discussion_units_pilot/mason_argument_citation_compact_result.json` | `spent_usd` | $0.031543 |
| `llm_discussion_units_pilot/mason_argument_citation_late_result.json` | `spent_usd` | $0.001233 |
| `llm_discussion_units_pilot/mason_argument_citation_result.json` | `spent_usd` | $0.002236 |
| `llm_discussion_units_pilot/mason_argument_citation_single_result.json` | `spent_usd` | $0.036629 |
| `llm_discussion_units_pilot/mason_case_intelligence_result.json` | `spent_usd` | $0.398022 |
| `llm_discussion_units_pilot/mason_case_intelligence_result_2usd.json` | `spent_usd` | $0.413526 |
| `llm_discussion_units_pilot/mason_case_intelligence_result_exhaustive.json` | `spent_usd` | $0.470200 |
| `llm_discussion_units_pilot/mason_case_intelligence_result_exhaustive_compact.json` | `spent_usd` | $0.432228 |
| `llm_discussion_units_pilot/mason_scc_2023_llm_only_window_01_result_request.json` | `response.usage.estimated_cost_usd` | $0.001738 |
| `llm_discussion_units_pilot/mason_scc_2023_llm_only_window_02_result_request.json` | `response.usage.estimated_cost_usd` | $0.002045 |
| `llm_discussion_units_pilot/mason_scc_2023_llm_only_window_03a1_result_request.json` | `response.usage.estimated_cost_usd` | $0.000136 |
| `llm_discussion_units_pilot/mason_scc_2023_llm_only_window_03a2_result_request.json` | `response.usage.estimated_cost_usd` | $0.000916 |
| `llm_discussion_units_pilot/mason_scc_2023_llm_only_window_03b_result_request.json` | `response.usage.estimated_cost_usd` | $0.001192 |
| `llm_discussion_units_pilot/mason_scc_2023_window_01_result_request.json` | `response.usage.estimated_cost_usd` | $0.001661 |
| `llm_discussion_units_pilot/mason_scc_2023_window_02_result_request.json` | `response.usage.estimated_cost_usd` | $0.002375 |
| `llm_discussion_units_pilot/mason_scc_2023_window_03a1_result_request.json` | `response.usage.estimated_cost_usd` | $0.000111 |
| `llm_discussion_units_pilot/mason_scc_2023_window_03a2_result_request.json` | `response.usage.estimated_cost_usd` | $0.001046 |
| `llm_discussion_units_pilot/mason_scc_2023_window_03b_result_request.json` | `response.usage.estimated_cost_usd` | $0.001363 |
| `llm_discussion_units_pilot/paragraph_level_300_run/ledger.json` | `cases.62.spent_usd` | $0.003667 |
| `reports/core_immigration_statute_openai_audit_gpt41.json` | `openai_audit.summary.spent_usd` | $0.015714 |
| `reports/core_immigration_statute_openai_audit_gpt4o.json` | `openai_audit.summary.spent_usd` | $0.016074 |
| `reports/core_immigration_statute_openai_audit_gpt5.json` | `openai_audit.summary.spent_usd` | $0.073686 |
| `reports/fc_additional_500_audit_batch1.json` | `openai_audit.summary.spent_usd` | $0.054573 |
| `reports/fc_additional_500_audit_batch1_postpatch2.json` | `openai_audit.summary.spent_usd` | $0.052282 |
| `reports/fc_additional_500_audit_batch2.json` | `openai_audit.summary.spent_usd` | $0.054853 |
| `reports/fc_additional_500_audit_batch2_postpatch2.json` | `openai_audit.summary.spent_usd` | $0.051768 |
| `reports/fc_additional_500_audit_batch3.json` | `openai_audit.summary.spent_usd` | $0.056021 |
| `reports/fc_additional_500_audit_batch3_postpatch2.json` | `openai_audit.summary.spent_usd` | $0.054888 |
| `reports/fc_additional_500_audit_batch4.json` | `openai_audit.summary.spent_usd` | $0.058079 |
| `reports/fc_additional_500_audit_batch4_postpatch2.json` | `openai_audit.summary.spent_usd` | $0.057574 |
| `reports/fc_additional_500_audit_batch5.json` | `openai_audit.summary.spent_usd` | $0.057908 |
| `reports/fc_additional_500_audit_batch5_postpatch2.json` | `openai_audit.summary.spent_usd` | $0.054273 |
| `reports/fc_additional_500_statute_openai_audit_gpt4o.json` | `openai_audit.summary.spent_usd` | $0.029077 |
| `reports/fc_priority_audit_gpt41mini_fulltext.json` | `openai_audit.summary.spent_usd` | $0.252643 |
| `reports/fc_priority_audit_gpt41mini_postpatch_50.json` | `openai_audit.summary.spent_usd` | $0.043334 |
| `reports/fc_priority_audit_gpt41mini_postpatch_batch1.json` | `openai_audit.summary.spent_usd` | $0.084999 |
| `reports/fc_priority_audit_gpt41mini_postpatch_batch2.json` | `openai_audit.summary.spent_usd` | $0.056683 |
| `reports/fc_priority_audit_gpt41mini_postpatch_batch3.json` | `openai_audit.summary.spent_usd` | $0.082964 |
| `reports/fc_priority_audit_smoke.json` | `openai_audit.summary.spent_usd` | $0.001065 |
| `reports/fc_priority_audit_smoke_gpt41mini.json` | `openai_audit.summary.spent_usd` | $0.004580 |
| `reports/fc_priority_audit_smoke_gpt41mini_lines.json` | `openai_audit.summary.spent_usd` | $0.003808 |
| `stored_case_to_case_openai_audit_1000.json` | `openai_audit.summary.spent_usd` | $0.136624 |
| `stored_citation_openai_audit_report.json` | `openai_audit.summary.spent_usd` | $0.000556 |
| `treatment_teacher_result_100_offset1000.json` | `spent_usd` | $0.009511 |
| `treatment_teacher_result_100_offset1500.json` | `spent_usd` | $0.009384 |
| `treatment_teacher_result_100_offset500.json` | `spent_usd` | $0.008674 |
| `treatment_teacher_result_100_v2.json` | `spent_usd` | $0.008046 |
| `treatment_teacher_result_500.json` | `spent_usd` | $0.026097 |
| `treatment_teacher_result_500_v2.json` | `spent_usd` | $0.011714 |
