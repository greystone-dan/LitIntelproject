# Task: 100-case OpenAI loose structured FC Activity pilot

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Test whether a permissive JSON response lets the model identify FC Activity fields and relationships more completely than the strict schema.
Why now: The strict run improved semantic decision fields but underfilled filing dates and produced far fewer motion rows than deterministic extraction; rigid required properties may be constraining useful interpretation.
Owner surface: Existing review-only OpenAI FC Activity pilot runner, with an explicit permissive `json_object` response mode.
Dependencies: Fixed IMM-15 report, strict 100-case artifact, OpenAI credentials, and existing checkpoint/cost controls.
Risk boundary: Exactly 100 requests, same seed and cases, `gpt-4.1-nano`, hard budget USD 1.00, no database writes, no automatic fact promotion, new output/checkpoint paths only.
Smallest falsifiable check: Compile and dry-run the loose mode, then send one smoke request and verify valid JSON parsing before the 100-case run.
Acceptance criteria:
- The prompt still names all desired fields and supplies the same source text.
- The response uses JSON object mode without strict required-property/type enforcement.
- The run records parse failures, usage, spend, and `database_written=false`.
- Results are compared with strict output and deterministic coverage on the identical 100 cases.
Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; artifacts under `data/eval/`.
Rollback/recovery: Delete only loose pilot artifacts and checkpoint; do not modify Activity or canonical tables.
Commit allowed: yes
Push allowed: yes
Evidence:
- Delegated read-only review recommended `json_object` as the smallest permissive machine-readable change.
- Added `--response-mode loose`; strict mode remains available unchanged.
- Loose smoke initially exposed an omitted `case` wrapper; the parser now normalizes that wrapper while retaining supplied identity checks and records the omission.
- The same 100-case sample completed 100/100 after bounded truncation retries, with `database_written=false`, 214,990 total tokens, and `$0.0381952` spend.
- Loose coverage was filing date 2/100, decision type 38/100, decision date 73/100, any judge 82/100, and motion-bearing cases 82/100, versus strict 83/100, 85/100, 86/100, 76/100, and 32/100.
- Loose output contained 118 motion rows versus 76 strict and 332 deterministic motion events.
Files changed: `scripts/run_fc_activity_openai_structured_pilot.py`, this task record, and bounded loose pilot artifacts under `data/eval/`.
Focused validation: compilation and dry-run passed; loose smoke passed after wrapper normalization; bounded 100-case run completed with zero final failures; final `git diff --check` pending.
Residual risk: Loose output is more semantically expansive but underfills deterministic dates and can omit the case wrapper or stage objects. Judge and motion precision remain unreviewed, and retries were needed for output truncation.
Next bounded task: Review a stratified sample of loose/strict/deterministic disagreements for precision before scaling.
