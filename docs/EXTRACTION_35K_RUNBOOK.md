# Full-Corpus Citation Extraction Runbook

Last updated: 2026-09-07

Purpose: run a full deterministic case-citation replacement across the current corpus with the controlled extraction method, durable recovery evidence, and post-run verification.

## Scope

This runbook targets an ordered pipeline with separate write boundaries:

1. Controlled case-citation replacement
2. Case-to-case target resolution
3. Separately approved statute/instrument extraction and citation metrics recomputation

It does not require hosted AI calls.

Do not use the legacy combined `extract_citation_network --cases --chunks --statutes --metrics` command for a full citation replacement. The automatic `safe` and `enrich` overnight profiles intentionally omit that legacy job. Full-pipeline work must use `scripts/rebuild_citations_controlled.py`, the method validated by the 2026-09-07 all-case run.

## Pre-Run Checks

Run from the repository root:

```powershell
& .\venv\Scripts\python.exe scripts\rebuild_citations_controlled.py --help
& .\venv\Scripts\python.exe -m pytest tests\test_rebuild_citations_controlled.py tests\test_citations.py -q
```

Expected:

1. The controlled runner help exits successfully.
2. Focused runner and extraction tests pass.
3. PostgreSQL is reachable and no competing bulk writer is active.
4. The run directory has enough free disk for baseline, comparison, checkpoint, and state artifacts.

Optional focused extractor sanity (already green at time of update):

```powershell
.\venv\Scripts\python.exe -m pytest -q tests/test_citations.py -k "irpa or statute_reference_matches"
```

## Baseline Snapshot (Before Run)

```powershell
.\venv\Scripts\python.exe -c "from sqlalchemy import select, func; from backend.database import SessionLocal, Case, CaseChunk, Citation, StatuteReference, CitationMetrics; s=SessionLocal(); print(f'cases_total={int(s.scalar(select(func.count(Case.id))) or 0)}'); print(f'cases_with_text_or_summary={int(s.scalar(select(func.count(Case.id)).where((Case.full_text.is_not(None)) | (Case.summary.is_not(None)))) or 0)}'); print(f'chunk_rows={int(s.scalar(select(func.count(CaseChunk.id))) or 0)}'); print(f'citation_rows={int(s.scalar(select(func.count(Citation.id))) or 0)}'); print(f'statute_reference_rows={int(s.scalar(select(func.count(StatuteReference.id))) or 0)}'); print(f'citation_metrics_rows={int(s.scalar(select(func.count(CitationMetrics.case_id))) or 0)}'); s.close()"
```

## Optional Canary

Use a fresh run directory for a one-case dry run before full launch:

```powershell
& .\venv\Scripts\python.exe scripts\rebuild_citations_controlled.py --case-id 615 --limit 1 --run-dir data\overnight_runs\citation-rebuild-canary-<RUN_ID> --dry-run
```

## Full-Corpus Launch

Count and freeze the current text-bearing cohort, choose a fresh run directory, and launch the explicit apply pass:

```powershell
$caseCount = & .\venv\Scripts\python.exe -c "from sqlalchemy import func, select; from backend.database import Case, SessionLocal; s=SessionLocal(); print(s.scalar(select(func.count(Case.id)).where(Case.full_text.is_not(None), Case.full_text != ''))); s.close()"
$runId = Get-Date -Format "yyyyMMdd-HHmmss"
$runDir = "data\overnight_runs\citation-extraction-all-$runId"
& .\venv\Scripts\python.exe -u scripts\rebuild_citations_controlled.py --all --limit $caseCount --run-dir $runDir --apply --confirm-citation-rebuild --progress-every 10
```

Notes:

1. The selected case IDs are frozen in `state.json` before replacement begins.
2. The runner invokes only the `case_citations` processing stage and validates direct short-form anchors before each commit.
3. Baseline, comparison, and checkpoint JSONL files provide recovery evidence.
4. Target resolution, statute extraction, and citation metrics remain deferred and must run as separately validated stages after extraction completes.

## Resume After Interruption

Resume the same frozen cohort and explicit run directory:

```powershell
& .\venv\Scripts\python.exe -u scripts\rebuild_citations_controlled.py --all --limit $caseCount --run-dir $runDir --apply --confirm-citation-rebuild --resume --progress-every 10
```

Do not resume with a different case count or reuse a stale run directory for a new cohort.

## Post-Run Verification

1. Check `state.json` in the selected run directory.
2. Confirm `status=completed`, `stage=case_citations`, `target_resolution=deferred`, and `metrics=deferred`.
3. Re-run baseline snapshot command and compare deltas.
4. Run target resolution as a separate checkpoint and regenerate the unresolved-shape report.
5. Recompute metrics only after resolution succeeds.
6. Spot-check citation pass for a known IRPA case in UI/API:
   - `/citation-pass`
   - `/cases/{case_id}/citation-pass`

## Contention And Safety

1. Do not run other PostgreSQL-writing bulk jobs concurrently.
2. If lock conflicts occur, verify active jobs before using `--force-unlock`.
3. If a process stalls, terminate that process first, inspect its checkpoint evidence, and resume the controlled runner with the same cohort and run directory.
