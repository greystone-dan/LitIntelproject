# Task: Independent FC Activity collector

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

## Task Record

Task: Prepare a resumable, site-independent FC Activity acquisition path suitable for later deployment to an Oracle Always Free VM.

Why now: The project needs FC Activity records collected independently of the research website, with staging, discovery, classification, and recovery behavior understood before cloud execution.

Owner surface: scripts/fc_portal_collector.py and the FC Activity operational runbook

Commit allowed: yes

Push allowed: yes

Dependencies: Existing FC Activity schema and scripts, Federal Court source terms/robots policy, Oracle tenancy access and approved hosting/security decisions for any remote deployment.

Risk boundary: No Oracle account or VM provisioning, no secrets handling, no unbounded live scraping, no concurrent PostgreSQL writers, and no production/protected-data deployment. Staging must remain separate from canonical case records until an explicit import gate.

Smallest falsifiable check: `venv\\Scripts\\python.exe scripts/classify_fc_activity.py --help` followed by the smallest available bounded dry-run against existing staged input.

Acceptance criteria:

- Existing FC discovery, detail staging, classification, checkpoint, retry, rate-limit, and robots behavior are documented.
- A bounded offline or staged validation proves classification does not write canonical data.
- A VM runbook defines architecture, storage, locks, checkpoints, logs, resume, backup, and stop conditions.
- Oracle provisioning remains an explicit approval gate with no credentials or external resources created by this task.
- Relevant canonical documentation and Swimm workflow context are updated.

Docs/generated references: `OVERNIGHT.md`, `docs/DATA_SOURCE_REGISTER.md`, `docs/CONFIGURATION_REFERENCE.md`, relevant FC Activity Swimm walkthrough if available. Generated references unchanged.

Rollback/recovery: Remove only the runbook/task changes; staged files remain outside canonical tables. Stop and delete any future VM only through an explicitly approved operator procedure.

Evidence: Read-only audit completed by Explore. `fc_portal_collector.py --help`, `fetch_fc_procedural_history.py --help`, and `classify_fc_activity.py --help` exited 0. Focused FC Activity tests passed: 20 passed, 0 failed, no warnings. Added the worker runbook, operational/source-register references, and Swimm boundary update. No network collection, database write, Oracle provisioning, or credential handling occurred.

## Hypothesis

If the existing FC Activity collector and classifier are suitable for independent execution, their bounded help/dry-run path will expose checkpoint, delay, retry, robots, and write boundaries without requiring the website or a database writer.

## Plan

1. Validate the current command contracts and locate the narrowest staged/offline fixture.
2. Add the smallest operational documentation and tests needed to make independent execution reproducible.
3. Re-run bounded validation and record the Oracle provisioning approval boundary.

## Execution Checkpoints

- Delegation: Explore performed a read-only audit of FC Activity ownership, scripts, schemas, routes, controls, and deployment gaps.
- Implementation: Pending local validation and documentation.
- Documentation: Pending canonical runbook and Swimm checkpoint.
- Recovery: No remote run, database writer, or long-running scraper started.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-25 | Keep Oracle provisioning approval-gated | Requires tenancy credentials, external resource creation, and unresolved security/hosting approvals. | FC Activity audit report |

## Completion

Completion recorded: yes

Summary: Existing resumable FC Activity acquisition/classification controls were validated and documented for future approval-gated independent deployment.

Validation: Three FC CLI help checks passed; `venv\\Scripts\\python.exe -m pytest tests\\test_classify_fc_activity.py tests\\test_hf_fc_activity_ingest.py -q` passed with 20 tests.

Residual risk: Oracle Always Free limits, ARM64 package compatibility, source terms, and cross-layer FC Activity/canonical-case linking require explicit operational decisions. No remote worker is running.

Next recommended task: Validate the bounded collector/classifier contract, then prepare an operator-run VM bootstrap without secrets.
