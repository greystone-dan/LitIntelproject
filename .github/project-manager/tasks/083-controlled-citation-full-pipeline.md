# Task: Require controlled citation extraction in full pipeline

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Prevent future automatic full-pipeline runs from using the legacy combined citation rebuild and document the controlled extraction method validated by the 2026-09-07 full run.

Why now: The full citation replacement demonstrated that `scripts/rebuild_citations_controlled.py` is the required safe extraction path, but `run_overnight.py` still includes the legacy combined citation job in automatic enrichment profiles.

Owner surface: `scripts/run_overnight.py`

Commit allowed: yes

Push allowed: yes

Dependencies: `scripts/rebuild_citations_controlled.py`, the completed task 080 extraction evidence, and the extraction runbook.

Risk boundary: Do not automatically launch a destructive full-corpus citation rebuild. Preserve explicit cohort freezing, apply confirmation, locking, checkpoints, and separate target-resolution/metrics phases.

Smallest falsifiable check: `& .\venv\Scripts\python.exe -m pytest tests\test_run_overnight.py -q`

Acceptance criteria:

- Automatic `safe` and `enrich` profiles do not invoke the legacy combined citation rebuild.
- The backfill runbook requires the controlled citation-only runner used for the completed full replacement.
- Canonical and Swimm documentation record that extraction, target resolution, statute work, and metrics remain separate stages.

Docs/generated references: `OVERNIGHT.md`, `docs/EXTRACTION_35K_RUNBOOK.md`, `.swm/4.9nn3id9f.sw.md`, `docs/SCRIPT_CATALOG.generated.md`

Rollback/recovery: Restore the profile entries only after a resumable orchestration wrapper can pass a frozen cohort, unique run directory, explicit confirmation, and resume state to the controlled runner.

Evidence: The bounded repository review found `run_overnight.py` still included the legacy combined citation job in both automatic enrichment profiles, while the validated controlled runner requires a frozen cohort, unique run directory, explicit apply confirmation, lock, and resume state. Removed `citations` from `safe` and `enrich` while preserving explicit compatibility access. Updated `docs/EXTRACTION_35K_RUNBOOK.md`, `OVERNIGHT.md`, and `.swm/4.9nn3id9f.sw.md` to require the controlled method. The combined focused suite passed (`159 passed`), the complete main-project suite passed (`475 passed`), generated documentation is current (`3 references checked`), and `git diff --check` passed. A root-level all-repository pytest attempt was blocked during collection by the unrelated `side_projects/browser_game` import path (`ModuleNotFoundError: tools`).

## Hypothesis

If the legacy citation job is removed from automatic profiles and the runbook names the controlled runner, a profile selection test will prove future full-pipeline runs cannot silently bypass the validated extraction safeguards.

## Plan

1. Remove legacy citation rebuilding from automatic profiles while retaining explicit compatibility access.
2. Update tests and the full extraction runbook.
3. Validate focused operations tests, generated docs, and the complete saved worktree.

## Execution Checkpoints

- Delegation: bounded repository lookup identified the active legacy profile wiring and controlled runner requirements; no files changed.
- Implementation: `scripts/run_overnight.py` and `tests/test_run_overnight.py`.
- Documentation: `OVERNIGHT.md`, `docs/EXTRACTION_35K_RUNBOOK.md`, and `.swm/4.9nn3id9f.sw.md`.
- Recovery: no writer is launched; revert profile membership if a controlled orchestration replacement is later implemented.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-07 | Keep legacy job explicit but remove it from automatic profiles | The controlled runner requires explicit destructive confirmation and durable per-run state | Task 080 full-run evidence |

## Completion

Completion recorded: yes

Summary: Automatic full-pipeline profiles can no longer invoke the legacy combined citation rebuild; the controlled extraction method is now the documented required backfill path.

Validation: Focused suite -> `159 passed`; `pytest tests -q` -> `475 passed`; generated-document check and `git diff --check` passed. Root-level pytest has one unrelated browser-game collection error.

Residual risk: The controlled citation rebuild remains an explicit operator step until a safe orchestrator can provide its required arguments and resume semantics.

Next recommended task: Add first-class controlled citation orchestration only with explicit confirmation and resumable run-directory propagation.
