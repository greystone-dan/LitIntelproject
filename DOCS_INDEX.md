# Documentation Index And Nighttime Patch Checklist

Last updated: 2026-08-12

## Purpose

This file defines which documents are authoritative for current operations,
which are historical, and what to update during a nighttime patch.

## Canonical Workflow Pointer

Current main workflow is the six-tab immigration litigation intelligence interface,
with Citation Pass retained as the extractor QA surface.

Use this sequence:

1. Run the API.
2. Use `/data-explorer` for About, Case Search, Citation Intelligence, Judge Outcomes, Judge Profile, and Data Explorer.
3. Use `/case-reader` for unified case detail and linked citation context.
4. Use `/citation-pass` only when validating extraction behavior or offsets.
5. Re-run focused verification and then update explainer docs and changelog.

Primary explainer docs that must stay aligned:

1. `README.md` (entrypoint and operating workflow)
2. `AI_HANDOFF.md` (active implementation state and next actions)
3. `SYSTEM_OVERVIEW.txt` (plain-language status snapshot)
4. `CHANGELOG.md` (what changed and verification notes)

## Active Vs Legacy Locations

Active implementation and operations:

1. Root docs (`README.md`, `AI_HANDOFF.md`, `CHANGELOG.md`, `SYSTEM_OVERVIEW.txt`)
2. Active backend modules under `backend/` (excluding `backend/legacy/`)
3. Isolated side-project utilities under `side_projects/` when the task explicitly concerns non-core datasets

Legacy/reference-only areas:

1. `legacy/` (archived artifacts and legacy workflow references)
2. `backend/legacy/` (deprecated or parked runtime modules)
3. `docs/history/` (historical notes and prior snapshots)

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

5. `ROADMAP.md`
- Forward-looking phased delivery plan for missing features, QA, and release readiness.

6. `AI_HANDOFF.md`
- Active implementation handoff for advanced search, linked-citation resolution, deployment scaffolding status, and next-agent entry tasks.

7. `side_projects/luck_of_the_draw_iii/README.md`
- Scope and run instructions for the isolated Luck of the Draw III dataset import/export utility.

Historical context (read with caution):

1. `docs/history/AI_HANDOFF.md`
2. `docs/history/AI_STAGE_SUMMARY_2026-07-31.md`
3. `docs/history/PROJECT_NOTES.md`

These files are useful for lineage and rationale but may contain stale counts,
older endpoint lists, or outdated test totals.

## Cleanup Status (2026-08-07)

1. Active handoff authority now lives in root `AI_HANDOFF.md`; historical handoffs remain under `docs/history/`.
2. Research-facing work is currently centered on `/data-explorer`, `/case-reader`, and linked citation review; `/citation-pass` remains the extractor QA surface.
3. Case-to-case resolution is now a separate local database pass after extraction; do not recombine it with extraction.
4. Root documentation should prioritize `README.md`, `AI_HANDOFF.md`, `SYSTEM_OVERVIEW.txt`, `OVERNIGHT.md`, and `CHANGELOG.md`.

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
