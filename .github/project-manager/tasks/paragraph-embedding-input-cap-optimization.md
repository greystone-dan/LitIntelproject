# Task: Improve paragraph embedding request density

Status: in-progress
Created: 2026-09-30
Updated: 2026-09-30

Task: Remove the next evidenced request-density bottleneck without paid execution or reduced paragraph coverage.
Why now: Packed 5,000 benchmark used 53 requests and 5,107 inputs, averaging about 96 inputs per request; the local 100-input cap likely stops requests before the token cap.
Owner surface: `scripts/embed_openai_chunks.py`.
Commit allowed: no
Push allowed: no
Dependencies: Existing packed runner, focused offline tests, public provider/installed SDK input-limit evidence, saved benchmark ledger.
Risk boundary: No API embedding calls, live database scan/write, full-cohort launch, second worker, secret reads, model/schema/chunk changes, or reduced safety/accounting. Preserve previous commit/push prohibition.
Smallest falsifiable check: `venv/Scripts/python.exe -m pytest tests/test_openai_chunk_embeddings.py -q` with a >100-input request regression and an offline token-length replay.
Acceptance criteria:
- Verify supported request-input limit and improve request density without exceeding per-input or aggregate-token limits.
- Preserve paragraph-only null-vector scope, one unchanged row/vector per paragraph, weighted pooling, one worker, no voluntary pacing and restart/budget guards.
- Pass focused offline tests and replay historical input lengths without claiming a live throughput improvement.
- Update canonical documentation and Swimm; pass managed evidence gate.
Harness criteria: Supported input density and offline regression; existing safety contracts; documentation and evidence checkpoint.
Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/5.b49ftjal.sw.md`; generated references only through generators if needed.
Rollback/recovery: Restore former configurable input count; no persistent vectors or source rows will change in this task.
Evidence: Prior benchmark summary: 5,000 saved paragraphs, 5,107 inputs, 1,977,872 tokens, 53 successful requests, 104.625 seconds. This is baseline evidence, not a newly launched run.
Files changed: This task record; implementation/documentation pending worker report.
Delegated work: Bounded request-limit verification and minimal input-density implementation; structured report required. No worker-paid execution or task-record edits.
Focused validation: Pending.
Residual risk: Larger request latency and actual server behavior require a separately authorized live benchmark. No speedup guarantee.
Next bounded task: If offline acceptance passes, request approval for a bounded larger-input live benchmark before full rollout.

## Hypothesis

If a documented provider-supported input count above 100 permits token-limited packing, a conservative larger default will reduce requests on an offline replay while all current coverage/recovery tests still pass.

## Alternatives

- Larger packed requests: low complexity and no concurrency/accounting changes; selected if supported limit is verified.
- Two coordinated in-flight requests: may overlap latency, but increases state/retry/accounting complexity; defer until request density is exhausted.
- Asynchronous Batch API: potentially useful for offline backfill cost and capacity, but requires a separate reconciliation workflow and paid-operation approval; deferred.

## Execution Checkpoints

- Manager created the task and will create a harness with declared acceptance criteria before delegation.

## Completion

Completion recorded: no
Summary: Pending bounded implementation and offline acceptance; no paid launch authorized.