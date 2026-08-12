# 35k Citation Extraction Runbook

Last updated: 2026-08-10

Purpose: run a full deterministic citation/statute extraction refresh across the full 35,902-case corpus with safe preflight, resumability, and post-run verification.

## Scope

This runbook targets:

1. Case-citation rebuild
2. Statute/instrument extraction rebuild (including IRPA/IRPR section forms)
3. Citation metrics recompute

It does not require hosted AI calls.

## Pre-Run Checks

Run from repo root:

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --profile safe --jobs citations --preflight
```

Expected:

1. `preflight=ok`
2. Database reachable
3. Script and interpreter present
4. Disk check passes

Optional focused extractor sanity (already green at time of update):

```powershell
.\venv\Scripts\python.exe -m pytest -q tests/test_citations.py -k "irpa or statute_reference_matches"
```

## Baseline Snapshot (Before Run)

```powershell
.\venv\Scripts\python.exe -c "from sqlalchemy import select, func; from backend.database import SessionLocal, Case, CaseChunk, Citation, StatuteReference, CitationMetrics; s=SessionLocal(); print(f'cases_total={int(s.scalar(select(func.count(Case.id))) or 0)}'); print(f'cases_with_text_or_summary={int(s.scalar(select(func.count(Case.id)).where((Case.full_text.is_not(None)) | (Case.summary.is_not(None)))) or 0)}'); print(f'chunk_rows={int(s.scalar(select(func.count(CaseChunk.id))) or 0)}'); print(f'citation_rows={int(s.scalar(select(func.count(Citation.id))) or 0)}'); print(f'statute_reference_rows={int(s.scalar(select(func.count(StatuteReference.id))) or 0)}'); print(f'citation_metrics_rows={int(s.scalar(select(func.count(CitationMetrics.case_id))) or 0)}'); s.close()"
```

## Optional Canary

Small tail-range canary before full launch:

```powershell
.\venv\Scripts\python.exe -m scripts.extract_citation_network --cases --statutes --batch-size 50 --cases-start-after-id 35850
```

## Full 35k Launch

Preferred launch path (tracked, lock-protected, resumable):

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --profile safe --jobs citations --continue-on-error
```

What this invokes for citations job:

- `python -m scripts.extract_citation_network --cases --chunks --statutes --metrics --batch-size 500`

Notes:

1. `--cases` rebuilds `citations` from case text (deletes and re-inserts per case).
2. `--chunks` rebuilds chunk-scoped citations.
3. `--statutes` with chunks enabled rebuilds `statute_references` from chunks.
4. `--metrics` recomputes citation metrics for all cases.

## Resume After Interruption

Resume latest run:

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --resume --continue-on-error
```

Resume by explicit run id:

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --resume <RUN_ID> --continue-on-error
```

Run artifacts are under `data/overnight_runs/<run-id>/`.

## Post-Run Verification

1. Check job state in `data/overnight_runs/<run-id>/state.json`.
2. Confirm no failed status for `citations`.
3. Re-run baseline snapshot command and compare deltas.
4. Spot-check citation pass for a known IRPA case in UI/API:
   - `/citation-pass`
   - `/cases/{case_id}/citation-pass`

## Contention And Safety

1. Do not run other PostgreSQL-writing bulk jobs concurrently.
2. If lock conflicts occur, verify active jobs before using `--force-unlock`.
3. If a process stalls, terminate that process first, then resume via run_overnight.
