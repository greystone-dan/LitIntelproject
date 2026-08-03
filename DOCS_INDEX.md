# Documentation Index And Nighttime Patch Checklist

Last updated: 2026-08-03

## Purpose

This file defines which documents are authoritative for current operations,
which are historical, and what to update during a nighttime patch.

## Documentation Authority

Current operational sources of truth:

1. `SYSTEM_OVERVIEW.txt`
- Plain-language architecture, data layers, collection status, and workflow state.

2. `CHANGELOG.md`
- Implementation milestones, newly added endpoints, and latest test baseline.

3. `OVERNIGHT.md`
- Operational runbook for preflight, run, resume, logging, and lock handling.

4. `MASTER_IDEAS.md`
- Long-term feature backlog and prioritization input.

Historical context (read with caution):

1. `docs/history/AI_HANDOFF.md`
2. `docs/history/AI_STAGE_SUMMARY_2026-07-31.md`
3. `docs/history/PROJECT_NOTES.md`

These files are useful for lineage and rationale but may contain stale counts,
older endpoint lists, or outdated test totals.

## Cleanup Status (2026-08-03)

1. Historical handoff docs were moved from repository root to `docs/history/`.
2. Local backup snapshots and runtime overnight state directories are now ignored for cleaner commits.
3. Root documentation should prioritize `README.md`, `SYSTEM_OVERVIEW.txt`, `OVERNIGHT.md`, and `CHANGELOG.md`.

## Nighttime Patch Checklist

Quick command sequence:

```powershell
./venv/Scripts/python.exe -m pytest -q
./venv/Scripts/python.exe scripts/run_overnight.py --profile safe --preflight
```

Before patch:

1. Run tests and capture baseline:
- `./venv/Scripts/python.exe -m pytest -q`

2. Confirm documentation alignment:
- New/changed endpoints listed in `CHANGELOG.md`.
- If behavior changed, update `SYSTEM_OVERVIEW.txt` summary language.
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
