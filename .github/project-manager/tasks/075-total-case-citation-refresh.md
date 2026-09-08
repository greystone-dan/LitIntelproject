# Total Case Citation Refresh

Status: blocked
Created: 2026-09-07
Updated: 2026-09-07

Task: Run the approved total extraction-only refresh for case-to-case citations, monitor durable progress, and preserve evidence for later independent target resolution.

Why now: The extractor and controlled replacement runner passed the one-case recheck and five-case cohort. The user authorized the full refresh.

Owner surface: `scripts/rebuild_citations_controlled.py`

Commit allowed: yes

Push allowed: yes

Dependencies: PostgreSQL connectivity, 61,216 text-bearing cases, exclusive citation-writer access, and the committed runner at `329586e`.

Risk boundary: Replace only `Citation` rows through the `case_citations` stage for the frozen text-bearing cohort. Do not run target resolution, short-form target resolution, metrics, statutes, metadata, tags, chunks, source writes, or external lookups.

Smallest falsifiable check: The runner must create a frozen 61,216-case state, advance completed case checkpoints with zero invalid direct short anchors, and finish with `target_resolution=deferred` and `metrics=deferred`.

Acceptance criteria:

- The approved all-case command runs under the exclusive runner lock.
- State and comparison artifacts show clean progress and no systemic failures.
- Every completed case has valid direct same-decision short-form anchor offsets when short forms are present.
- Resolution and metrics remain deferred throughout this task.
- Baseline, state, comparison, and any failure evidence remain in the run directory.
- Canonical documentation and the relevant Swimm walkthrough record the actual terminal result before completion.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/system-map.ovnldklv.sw.md`, `.swm/4.9nn3id9f.sw.md`.

Rollback/recovery: Stop the runner on systemic errors or invalid-anchor failures. Preserve the run directory and restore only affected source-case citations through a separately reviewed recovery command; do not resolve targets or recompute metrics.

Evidence: Preflight worktree was clean and the target run directory was absent. A first count probe used the wrong import path and was corrected before execution. The approved command is `& .\\venv\\Scripts\\python.exe scripts\\rebuild_citations_controlled.py --all --limit 61216 --run-dir data\\overnight_runs\\citation-extraction-all-20260907 --apply --confirm-citation-rebuild`. The run stopped at durable state `updated_at=2026-09-07T12:38:10.012757+00:00` with `1,295` completed, zero failed-state cases, `1,296` comparison rows, `target_resolution=deferred`, and `metrics=deferred`. It terminated when `atomic_write_json` received `PermissionError: [WinError 5] Access is denied` replacing `state.json`; `state.json.tmp`, baseline, and comparison artifacts are retained. Post-stop check found zero runner processes and no active rebuild lock. Comparison investigation found `12,446 -> 12,455` full/name/neutral rows and `27,455 -> 10,880` short rows across completed cases. `11,781` full/name/neutral rows retained an identical kind/text/normalized signature, but a direct complete-document extraction check found valid external reported decisions downgraded or truncated: for example, `David Bull Laboratories (Can.) Inc. v. Pharmacia Inc., [1995] 1 F.C. 588` becomes a truncated `case_name`, while the standalone phrase extracts as a complete `case` row. The same behavior affects `R. v. Turpin, [1989] 1 S.C.R. 1296`, `Suresh v. Canada (Minister of Citizenship and Immigration), [2002] 1 S.C.R. 3`, and `Kaberuka v. Canada (Minister of Citizenship and Immigration), [1995] 3 F.C. 252`. None are source-case self citations. This blocks resumption because missing complete reported anchors can also suppress later valid short forms.

Next checkpoint: Repair and test the context-sensitive full/reported-citation extraction regression, then restore affected processed-case citation rows from baseline or rerun only the repaired cohort after reviewing a clean comparison. Separately diagnose the Windows state-file replacement failure before any full-run resume. Do not run resolution or metrics.