# Task: Improve deterministic FC Activity judge recognition

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Add deterministic recognition for Chief Justice and Associate Justice title forms.
Why now: Judge coverage is 75.1% on the fixed 1,000-case sample, and evaluation data contains named judges using title forms absent from the current whitelist.
Owner surface: `scripts/classify_fc_activity.py` judge-name extraction and focused classifier tests.
Dependencies: Existing procedural event extraction and fixed FC Activity evaluation sample.
Risk boundary: High-precision title aliases only; preserve existing evidence-linked observations and avoid broad name guessing.
Smallest falsifiable check: Focused regression test for Chief Justice Crampton and Associate Justice Smith must fail before the change and pass after it.
Acceptance criteria:
- Chief Justice and Associate Justice forms extract only the name.
- Existing Justice, Madam Justice, and French judge forms remain unchanged.
- Focused tests pass and the fixed evaluator reports judge coverage change.
- Relevant Swimm and canonical documentation record the measured result.
Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`.
Rollback/recovery: Revert only the title aliases and regression test; no data or database changes.
Commit allowed: yes
Push allowed: yes
Evidence: Read-only review identified repeated Chief Justice Crampton/Lutfy records and confirmed the title alternation did not match them. Added `chief justice` and `associate justice` aliases with a focused regression test. The classifier suite passed 63 tests. The regenerated fixed 1,000-case IMM-15 report increased any-judge coverage from 751/1,000 (75.1%) to 811/1,000 (81.1%), gaining 60 cases; new evidence is stage-linked final-decision text such as `Order rendered by Chief Justice Crampton`.
Files changed: `scripts/classify_fc_activity.py`, `tests/test_classify_fc_activity.py`, this task record, and the post-change evaluation artifact under `data/eval/`.
Focused validation: `python -m pytest tests/test_classify_fc_activity.py -q` passed (`63 passed`); the fixed 1,000-case read-only evaluator completed with `database_written=false`.
Residual risk: Other judicial title/order-language variants may remain; coverage gain is not an accuracy proof, although the new matches are evidence-linked exact-title observations.
Next bounded task: Review residual unmatched judge-title patterns after measuring this change.
