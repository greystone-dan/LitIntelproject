# Task: 100-case OpenAI mini-model loose FC Activity pilot

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Compare `gpt-4.1-mini` loose JSON extraction against the completed nano loose run on the identical 100-case sample.
Why now: The nano loose run increased semantic judge and motion discovery but needs a higher-capability model test for precision and decision interpretation.
Owner surface: Existing review-only OpenAI FC Activity pilot runner with model override and model-specific pricing.
Dependencies: Fixed IMM-15 report, completed nano loose artifact, OpenAI credentials.
Risk boundary: Exactly 100 requests, same seed and cases, `gpt-4.1-mini`, hard budget USD 1.00, no database writes, no automatic fact promotion, new artifacts only.
Smallest falsifiable check: Compile and dry-run the model override, then run the bounded 100-case comparison.
Acceptance criteria:
- The artifact records `gpt-4.1-mini` and actual usage/spend.
- Prompt, loose response mode, selected cases, and concurrency match the nano comparison.
- Results include failures and are compared on decision fields, judges, and motions.
Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; artifacts under `data/eval/`.
Rollback/recovery: Delete only mini pilot artifacts and checkpoint; do not modify Activity or canonical tables.
Commit allowed: yes
Push allowed: yes
Evidence: Cost estimate from the nano token distribution was approximately `$0.139` for `gpt-4.1-mini`. The model-aware dry-run projected `$0.2966344` at the output ceiling. The bounded run completed 99/100 initially, then completed 100/100 after retrying one malformed JSON response, with `database_written=false`, 222,223 total tokens, and `$0.17365` spend. The current normalized comparison reported mini coverage of filing date 3/100, decision type 2/100, decision date 52/100, any judge 73/100, and motion-bearing cases 47/100, versus nano loose 2/100, 38/100, 73/100, 82/100, and 82/100. A representative mini response was materially richer than those counts suggest: it used alternate nested fields such as `application.filed_date`, included challenged-decision details, hearings, case-management events, five judges, and four motions, but did not consistently use the normalized output vocabulary.
Files changed: `scripts/run_fc_activity_openai_structured_pilot.py`, this task record, and bounded mini pilot artifacts under `data/eval/`.
Focused validation: compilation, model-aware dry-run, bounded API run, one retry, and final artifact inspection passed; final documentation diff check is pending.
Residual risk: The loose comparator undercounts alternate mini structures, so the normalized coverage comparison is not a fair quality ranking. The mini output requires field normalization and manual precision review before conclusions about model superiority.
Next bounded task: Stratified precision review across nano, mini, deterministic, and source evidence.
