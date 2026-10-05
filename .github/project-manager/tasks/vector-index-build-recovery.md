# Task: Diagnose slow vector index and select recovery

Status: blocked
Created: 2026-10-01
Updated: 2026-10-01

## Task Record

Task: Compare continuing the active HNSW build with a resource-bounded restart.
Why now: Repeated read-only samples show very slow, variable progress and disk waits.
Owner surface: Vector-index operations in scripts/ and OVERNIGHT.md.
Commit allowed: no
Push allowed: no
Dependencies: Active PostgreSQL builder, migration 0028, local RAM and pgvector support.
Risk boundary: No cancellation, PostgreSQL restart, global tuning, replacement index, paid operation, or canonical data mutation without explicit approval.
Smallest falsifiable check: Read-only progress, pg_settings, index catalog and OS resource inspection.
Acceptance criteria:
- Explain observed evidence and limits without asserting unverified builder settings.
- Compare continuation, tuned HNSW restart, and an alternative index strategy.
- Give a bounded recommendation and approval boundary; preserve the running build.
Docs/generated references: OVERNIGHT.md; .swm/5.b49ftjal.sw.md; migration 0028 (read-only).
Rollback/recovery: Diagnosis changes documentation only. A canceled build cannot resume its graph; saved embeddings must remain intact.
Evidence: Authorized cleanup stopped only Steam/steamwebhelper/claude. Free RAM rose from 1.33 to 2.68 GiB of 11.84 GiB. Manager read-only SQL at 16:40:58 confirmed original PID 47696 active, 189,348/241,571 blocks, 1,526,693 tuples, IO/DataFileRead, no blockers. OVERNIGHT.md and .swm/5.b49ftjal.sw.md updated. No build canceled or database setting changed.
Files changed: This task record; OVERNIGHT.md; .swm/5.b49ftjal.sw.md.
Delegated work: Explore diagnosis and cleanup execution worker returned outcome_unknown. Read-only execution worker succeeded. Manager verified remaining processes and performed bounded recovery of authorized cleanup; no unverified worker actions assumed.
Focused validation: Read-only SQL and Windows RAM/process checks passed; documentation diff check pending.
Residual risk: Diagnostic-session settings do not reveal another backend's session-local overrides.
Next bounded task: Approve and prepare a tuned rebuild only after assessing memory and build support.

## Hypothesis

If the HNSW graph outgrew a small build-memory allowance, read-only resource/settings evidence and available notices will support disk-intensive construction; current progress alone cannot prove that cause.

## Plan

1. Delegate bounded migration, monitor and resource diagnosis.
2. Compare options and independently verify the decisive live evidence.
3. Update operational and Swimm guidance, recording any approval blocker.

## Completion

Completion recorded: no
Summary: Memory cleanup completed. Full tuned-restart recommendation remains blocked on verified resource/build-support diagnosis; restart not authorized.
Validation: Same builder active and unblocked after cleanup; available RAM increased. Speedup unverified.
Residual risk: No reliable total-build ETA from loading-phase counters.
Next recommended task: Resource-bounded recovery decision.