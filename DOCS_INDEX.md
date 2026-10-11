# Documentation Index And Nighttime Patch Checklist

Last updated: 2026-09-28

## Purpose

This file defines which documents are authoritative for current operations,
which are historical, and what to update during a nighttime patch.

## Canonical Workflow Pointer

Current main workflow is the seven-tab immigration litigation intelligence interface,
with Citation Pass retained as the extractor QA surface.

Use this sequence:

1. Run the API.
2. Use `/data-explorer` for About, Case Search, Site Architecture, Citation Intelligence, Judge Profile, FC History, and Legal Themes & Statutes. Judge Profile is the sole active judge workflow; the former visible Data Explorer and Judge Outcomes tabs are retired.
3. Open a result in `/data-explorer` for unified case detail and linked citation context; `/case-reader` is a compatibility redirect for legacy bookmarks.
4. Use `/citation-pass` only when validating extraction behavior or offsets.
5. Use `/live-analysis` for ephemeral DOCX/text-PDF review without database writes.
6. Re-run focused verification and then update explainer docs and changelog.

Primary explainer docs:

1. `SYSTEM_REFERENCE.md` is the canonical current architecture and functionality reference.
2. `README.md` is the concise entrypoint and operating workflow.
3. `CHANGELOG.md` records what changed and verification notes.
4. `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md` is the Swimm walkthrough map,
   improvement queue, and future project-manager handoff contract.
5. `.github/copilot-instructions.md` defines repository-level agent guardrails,
   ownership boundaries, and validation expectations.
6. `.github/project-manager/README.md` explains the workspace project-manager
    agent, durable task records, status, and escalation rules.
7. `docs/reports/privacy-security-review.md` is the scoped privacy/security
   review for live document analysis and de-identification; current route
   behavior remains authoritative in code and `SYSTEM_REFERENCE.md`.
8. `docs/BACKGROUND_JOBS.md` documents the separate, disabled-by-default interval
   runner, JSON config, DB-free locks, scheduling, cleanup and exit codes. It
   does not change web startup or replace the overnight runbook.

## Active Vs Legacy Locations

Active implementation and operations:

1. Root docs (`README.md`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`)
2. Active backend modules under `backend/` (excluding `backend/legacy/`)
3. Isolated side-project utilities under `side_projects/` when the task explicitly concerns non-core datasets

Legacy/reference-only areas:

1. `legacy/` (archived artifacts and legacy workflow references)
2. `backend/legacy/` (deprecated or parked runtime modules)
3. `docs/history/` (historical notes and prior snapshots)

## Documentation Authority

Current operational sources of truth:

1. `SYSTEM_REFERENCE.md`
- Canonical current system functionality, architecture, data model, API map, operations, limitations, and review posture.

2. `CHANGELOG.md`
- Implementation milestones, newly added endpoints, and latest test baseline.

3. `OVERNIGHT.md`
- Repository atlas plus operational runbook for ownership, preflight, run,
  resume, logging, and lock handling.

4. `MASTER_IDEAS.md`
- Long-term feature backlog and prioritization input.

5. `ROADMAP.md`
- Forward-looking phased delivery plan for missing features, QA, and release readiness.

6. `docs/history/AI_HANDOFF_2026-09-02_root.md`
- Archived detailed working handoff (moved out of the repo root). It is time-bound; defer to `SYSTEM_REFERENCE.md` for active architecture and status.

7. `docs/CLAUDE_ACTIVITY_PROJECT_SETUP.md`
- Portable Claude Project setup, Activity data contract, commands, prompts, evidence rules, and implementation acceptance criteria.

8. `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`
- Read-only comparison of the current JRU Beta VBA extraction/validation logic with the active Python FC Activity pipeline.

9. `WORK_HISTORY.md`
- Generated time-spent ledger from the reviewable Chronicle session and day exports.

10. `docs/EVALUATION_COSTS.md`
- Generated report-level estimated-cost ledger for persisted evaluation artifacts; it is not provider billing.

11. `docs/STILL_TO_DO.md`
- Consolidated remaining product work, known accuracy gaps, operational debt, deferred research, and next-task decision gates.

12. `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`
- Swimm mapping plan and future manager-agent contract; it does not override
	the canonical architecture or generated references.

12. `side_projects/luck_of_the_draw_iii/README.md`
- Scope and run instructions for the isolated Luck of the Draw III dataset import/export utility.

13. `docs/reports/id-iad-coverage-design.md`
- Design-only proposal for ID/IAD decisions relevant to CBSA hearings; source, access, legal-taxonomy, and licence claims not directly verified are explicitly marked unverified.

## Hand-Written Documentation Inventory

The following inventory covers hand-written Markdown and text documents under
`docs/`, including historical and proposal documents retained for context.
Generated references are not hand-edit targets; `*.generated.md` outputs and
the generated `docs/EVALUATION_COSTS.md` report are intentionally excluded from
this inventory.

| Document | One-line description |
| --- | --- |
| `docs/ANALYST_QUICK_START.md` | Quick start for analysts using the active research interface. |
| `docs/ARCHITECTURE.md` | System architecture overview and backend module inventory. |
| `docs/BACKGROUND_JOBS.md` | Optional interval-job runner configuration, scheduling, and recovery. |
| `docs/CHANGE_MANAGEMENT.md` | Repository change-management rules and review workflow. |
| `docs/CITATION_REFINEMENT.md` | Citation and statute refinement methodology and workflow. |
| `docs/CITATION_REFINEMENT_RESULTS.md` | Citation-refinement results from real-decision evaluation. |
| `docs/CLAUDE_ACTIVITY_PROJECT_SETUP.md` | Setup and evidence contract for the Claude Activity project. |
| `docs/CLOUDFLARE_TUNNEL_SETUP.md` | Cloudflare tunnel setup, with standalone refresh retained as fallback only. |
| `docs/CONFIGURATION_REFERENCE.md` | Application configuration variables and defaults. |
| `docs/DAILY_INTAKE.md` | Daily source-intake workflow and checks. |
| `docs/DATA_SOURCE_REGISTER.md` | Register of data sources, provenance, and acquisition notes. |
| `docs/DEPLOYMENT_COMMANDS.md` | Deployment, status, and recovery command guidance for operators. |
| `docs/DEPLOYMENT_DOCKER.md` | Optional Docker build and local run instructions. |
| `docs/DISCUSSION_UNITS_WEEKLY_REVIEW.md` | Weekly review process for Discussion Units work. |
| `docs/DOC_AUDIT.md` | Documentation audit observations and follow-up notes. |
| `docs/EXTRACTION_35K_RUNBOOK.md` | Bounded full-corpus citation extraction procedure. |
| `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md` | Comparison of FC Activity Beta VBA and Python pipeline behavior. |
| `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md` | Federal Court Activity worker operating procedure. |
| `docs/LOCAL_DEPLOYMENT_SETUP.md` | Local Remote Control session setup and deployment workflow. |
| `docs/LONG_TERM_INTELLIGENCE_VISION.md` | Deferred long-term citation-treatment and argument-intelligence direction. |
| `docs/METRICS_DICTIONARY.md` | Definitions for application and evaluation metrics. |
| `docs/NEXT_STEPS.md` | Near-term work notes and proposed next actions. |
| `docs/OFFLINE_MODEL_EVALUATION.md` | Offline model evaluation inputs, process, and interpretation. |
| `docs/OPERATIONAL_RECOVERY_GUIDE.md` | Recovery guidance for application, jobs, data, tests, and Git workflows. |
| `docs/OPERATIONS_LOGGING.md` | Operational logging conventions and relevant log locations. |
| `docs/PARAGRAPH_CITED_BY.md` | Paragraph-level “cited by” batch-job design and use. |
| `docs/RESEARCH_UI_GUIDE.md` | Guide to active research UI workflows and boundaries. |
| `docs/SECURITY_DEPENDENCIES.md` | Dependency scanning and software-bill-of-materials guidance. |
| `docs/SECURITY_HEADERS.md` | Optional security response-header configuration and limits. |
| `docs/SITE_RECOVERY.md` | Site and tunnel recovery using the Windows `iLitSite` task. |
| `docs/STILL_TO_DO.md` | Consolidated remaining product work, debt, and decision gates. |
| `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md` | Swimm walkthrough map and project-manager handoff workflow. |
| `docs/TAGGING_V2_CORE_WHITELIST_DRAFT.md` | Draft whitelist for the V2 core-tagging layer. |
| `docs/TESTING_MATRIX.md` | Test-surface map and validation matrix. |
| `docs/about/AGENT-NOTES.md` | Implementation notes for the About page. |
| `docs/government-readiness/README.md` | Index and scope for the government-readiness document pack. |
| `docs/government-readiness/ai-use-statement.md` | Draft statement describing the system's AI use. |
| `docs/government-readiness/data-classification.md` | Data classification notes for government-readiness review. |
| `docs/government-readiness/data-flow.md` | Data-flow summary for government-readiness review. |
| `docs/government-readiness/logging-and-retention.md` | Logging and retention considerations for readiness review. |
| `docs/government-readiness/pia-inputs.md` | Fact-sheet inputs for a privacy-impact assessment. |
| `docs/government-readiness/subprocessors.md` | Third-party services and subprocessors inventory. |
| `docs/history/AI_HANDOFF.md` | Superseded project handoff retained as historical context. |
| `docs/history/AI_HANDOFF_2026-09-02_root.md` | Dated, superseded root handoff retained for lineage. |
| `docs/history/AI_STAGE_SUMMARY_2026-07-31.md` | Historical project-stage snapshot from 2026-07-31. |
| `docs/history/FC_CITATION_REBUILD_IMPLEMENTATION.md` | Superseded Federal Court citation-rebuild implementation notes. |
| `docs/history/FORMATTING_IMPROVEMENTS.md` | Superseded decision-formatting implementation notes. |
| `docs/history/PROJECT_NOTES.md` | Superseded project checkpoints and milestone commentary. |
| `docs/history/README.md` | Guide to the historical documentation archive. |
| `docs/proposed-migrations/embedding-per-model-tables.md` | Proposal for per-model embedding tables. |
| `docs/reports/accessibility-audit.md` | Accessibility findings for research and citation HTML builders. |
| `docs/reports/authority-treatment-design.md` | Design proposal for citation authority-treatment intelligence. |
| `docs/reports/backend-unused-code.md` | Inventory of unused backend code and duplicate logic. |
| `docs/reports/baseline-lint-and-audit.md` | Initial Ruff and pip-audit baseline report. |
| `docs/reports/cbsa-readiness-checklist.md` | Readiness checklist for CBSA hearings and litigation research. |
| `docs/reports/id-iad-coverage-design.md` | Design proposal for ID/IAD decision coverage. |
| `docs/reports/local-query-embeddings.md` | Local query-embedding provider and locality report. |
| `docs/reports/memo-missing-authority.md` | Proposal for identifying missing and contrary authorities. |
| `docs/reports/open-pr-review-2.md` | Point-in-time review report for issue #69. |
| `docs/reports/open-pr-review.md` | Point-in-time review of PRs #28, #29, #32, and #34. |
| `docs/reports/overruling-risk.md` | Provisional seed-based overruling-risk indicator report. |
| `docs/reports/privacy-security-review.md` | Scoped privacy and security review of live analysis and de-identification. |
| `docs/reports/query-performance-review.md` | Query-performance review report for issue #56. |
| `docs/reports/test-coverage.md` | Pytest coverage baseline and interpretation. |
| `docs/history/SYSTEM_OVERVIEW_2026-08-12.txt` | Historical system-overview snapshot from 2026-08-12. |
| `docs/proposed-migrations/indexes.py.txt` | Proposed index migration source retained as a text artifact. |
| `docs/proposed-migrations/embedding-per-model-tables.py.txt` | Proposed embedding-table migration source retained as a text artifact. |

## Task-Specific Review Reports

- `docs/reports/baseline-lint-and-audit.md` records the first non-blocking
  Ruff and pip-audit results and their scope. The checks and their artifact
  behavior are defined by `.github/workflows/quality.yml`.
- `docs/reports/open-pr-review.md` records the read-only, point-in-time review
  of PRs #28, #29, #32, and #34, including immutable source citations,
  migration/route interactions, untested paths, and review limitations. It is
  evidence for that review only; it does not replace current GitHub checks or
  the authoritative source code and migrations.
- `docs/reports/overruling-risk.md` documents the provisional, seed-based
  overruling-risk indicator, assignment semantics, limits, and extension steps.
- `docs/reports/local-query-embeddings.md` documents the opt-in query embedding
  provider, query-data locality signal, and vector-dimension compatibility
  boundary; current behavior remains authoritative in code and
  `SYSTEM_REFERENCE.md`.

Historical context (read with caution):

1. `docs/history/AI_HANDOFF.md`
2. `docs/history/AI_STAGE_SUMMARY_2026-07-31.md`
3. `docs/history/PROJECT_NOTES.md`

These files are useful for lineage and rationale but may contain stale counts,
older endpoint lists, or outdated test totals.

## Documentation Ownership Map

Use one owner per kind of knowledge. Swimm is the connected explanation and
rationale layer; repository files remain authoritative where tooling, deployment,
or reproducibility requires a source-controlled artifact.

| Knowledge type | Primary owner | Repository role |
| --- | --- | --- |
| Current system behavior and boundaries | `SYSTEM_REFERENCE.md` | Concise current-state authority |
| Product direction and delivery sequence | `ROADMAP.md`, `MASTER_IDEAS.md` | Roadmap and backlog inputs |
| Architecture rationale and design decisions | Swimm: Architecture Decisions and Design Rationale | Linkable decision context; implementation remains in code/migrations |
| Technical debt and improvement opportunities | Swimm: Technical Debt Register and Improvement Queue | Connected prioritization register; execution lives in task records |
| Evaluation definitions and quality metrics | Swimm: Evaluation Framework and Quality Metrics | Metric semantics and gates; reports remain under `data/eval/` |
| API and schema contracts | Generated references and their source code/migrations | Never hand-edit generated outputs |
| Operational procedures | `OVERNIGHT.md` and focused `docs/` runbooks | Executable operational guidance |
| Feature research guidance | `docs/RESEARCH_UI_GUIDE.md` and linked Swimm UI walkthrough | User-facing workflow and implementation map |
| Multi-step execution evidence | `.github/project-manager/tasks/` | Short-lived or durable task records |
| Historical lineage | `docs/history/` | Reference only; never current authority |

## Consolidation Rules

1. Before creating a Markdown document, identify its knowledge type and link to
    the existing owner instead when the content is explanatory or rationale.
2. Do not duplicate live counts, API contracts, schema details, or operational
    commands across Swimm and repository docs.
3. Keep root documents short and role-specific; move historical material to
    `docs/history/` only after links and current references are checked.
4. Prefer updating an existing owner document over creating another similarly
    named file.
5. Do not delete or rename documents during consolidation until replacement
    coverage and incoming references have been verified.

## Cleanup Status (2026-08-07)

1. Active architecture authority now lives in root `SYSTEM_REFERENCE.md`; historical handoffs remain under `docs/history/`.
2. Research-facing work is currently centered on `/data-explorer`, including its inline case reader and linked citation review; `/case-reader` is a compatibility redirect for legacy bookmarks, `/citation-pass` remains the extractor QA surface, and `/live-analysis` is the ephemeral document reader.
3. Case-to-case resolution is now a separate local database pass after extraction; do not recombine it with extraction.
4. Live Analysis reads uploaded DOCX/text-PDF bytes in memory only; local citation resolution is batched and read-only.
5. Root documentation should prioritize `README.md`, `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, and `CHANGELOG.md`.

## Nighttime Patch Checklist

### Automatic documentation check

`.github/workflows/documentation-sync.yml` runs on every push and pull request.
It executes `scripts/check_generated_docs.py`, which regenerates the API, schema,
and script-catalog references into a temporary directory, ignores generator
timestamps, and fails when the checked-in generated outputs drift. It does not
publish or update Swimm walkthroughs automatically.

Quick command sequence:

```powershell
./venv/Scripts/python.exe -m pytest -q
./venv/Scripts/python.exe scripts/run_overnight.py --profile safe --preflight
```

Before patch:

1. Run tests and capture baseline:
- `./venv/Scripts/python.exe -m pytest -q`

2. Confirm documentation alignment:
- New/changed system behavior is described in `SYSTEM_REFERENCE.md`.
- New/changed endpoints are listed in `CHANGELOG.md`.
- If operational flow changed, update `OVERNIGHT.md`.

3. Verify migration and script notes when relevant:
- Alembic changes reflected in changelog entry.
- New maintenance scripts reflected in `OVERNIGHT.md` or a dedicated doc.

After patch:

1. Re-run tests and record pass count in `CHANGELOG.md`.
2. Add a concise milestone block in `CHANGELOG.md`.
3. Keep historical docs unchanged unless adding explicit "historical snapshot" labels.
4. If feature backlog changed, append to `MASTER_IDEAS.md`.

## Notation Standards

1. Use explicit endpoint paths (for example, `/citation-map/issues/dashboard`).
2. Record bounded parameter behavior where relevant.
3. Record validation rules when they affect API responses.
4. Include CSV export routes beside their JSON route counterparts.
5. Keep milestone statements factual and test-backed.
