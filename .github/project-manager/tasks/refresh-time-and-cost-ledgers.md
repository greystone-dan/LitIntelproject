# Task: Refresh time and cost ledgers

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Recalculate retained project time and recorded evaluation spend after the prior ledgers became stale.

Why now: The work-history export stopped at September 1, while Chronicle and evaluation artifacts continued to grow.

Owner surface: Project operations documentation and bounded evaluation-cost reporting.

Commit allowed: yes

Push allowed: yes

Dependencies: Local Chronicle session store, reviewable work-history JSON exports, and `data/eval/` JSON artifacts.

Risk boundary: Time is a five-minute-capped activity proxy, not a timesheet. Money is report-recorded estimated spend, not provider billing. No external calls or evaluation reruns were made.

Smallest falsifiable check: Reconcile regenerated session totals with Chronicle-derived day totals and run the generated-document check.

Acceptance criteria:

- Work-history inputs cover all current workspace sessions through September 28.
- Generated time totals reconcile at session and day level.
- Recorded evaluation-cost aggregation is reproducible and states its deduplication policy.
- Canonical documentation, generated script catalog, and Swimm workflow note are updated.
- Focused tests and documentation checks pass.

Docs/generated references: `WORK_HISTORY.md`; `docs/EVALUATION_COSTS.md`; `DOCS_INDEX.md`; `docs/SCRIPT_CATALOG.generated.md`; `.swm/project-work-history-and-costs.sw.md`.

Rollback/recovery: Restore the prior work-history JSON exports and generated ledger if the Chronicle scope or cost-artifact selection policy is revised.

Evidence: Chronicle query returned 34 workspace sessions through 2026-09-28. Regeneration produced 2,982 turns and 7,387.9 capped day minutes (123.1 hours), with session/day totals reconciled within 0.1 minute. The corrected cost aggregation includes 86 non-dry-run report artifacts totaling $4.042849 estimated USD and explicitly excludes 14 dry-run/preparation artifacts totaling $0.271532. Runtime embeddings, overnight operations without cost artifacts, and provider billing not persisted in reports remain unmeasured. `scripts/check_generated_docs.py` passed and the focused FC Activity suite passed 84 tests.

Validation: `scripts/generate_work_history.py`; `scripts/aggregate_recorded_costs.py`; `scripts/generate_script_catalog.py`; `scripts/check_generated_docs.py`; `pytest tests/test_classify_fc_activity.py tests/test_evaluate_fc_activity_deterministic.py -q`; `git diff --check`.

Residual risk: The cost total is a lower bound on persisted non-dry-run estimates, not invoice-level provider billing. Runtime embedding calls and overnight operations are not retroactively measurable from current artifacts. Chronicle excludes unrecorded terminal, browser, and reading time.

Next recommended task: Reconcile provider billing exports separately if invoice-grade spend is required.