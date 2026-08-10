# Documentation Index And Nighttime Patch Checklist

Last updated: 2026-08-10

## Purpose

This file defines which documents are authoritative for current operations,
which are historical, and what to update during a nighttime patch.

## Canonical Workflow Pointer

Current main workflow is Citation Pass driven deterministic extraction hardening.

Use this sequence:

1. Run API.
2. Review extraction in `/citation-pass`.
3. Fix parser/rule behavior with tests first.
4. Re-run focused and then broader verification.
5. Update explainer docs and changelog before push.

Primary explainer docs that must stay aligned:

1. `README.md` (entrypoint and operating workflow)
2. `AI_HANDOFF.md` (active implementation state and next actions)
3. `SYSTEM_OVERVIEW.txt` (plain-language status snapshot)
4. `CHANGELOG.md` (what changed and verification notes)

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
- Active implementation handoff for citation stabilization, deployment scaffolding status, and next-agent entry tasks.

Historical context (read with caution):

1. `docs/history/AI_HANDOFF.md`
2. `docs/history/AI_STAGE_SUMMARY_2026-07-31.md`
3. `docs/history/PROJECT_NOTES.md`

These files are useful for lineage and rationale but may contain stale counts,
older endpoint lists, or outdated test totals.

## Cleanup Status (2026-08-07)

1. Active handoff authority now lives in root `AI_HANDOFF.md`; historical handoffs remain under `docs/history/`.
2. Citation stabilization is currently case-to-case first; statute/instrument extraction is tracked separately.
3. Root documentation should prioritize `README.md`, `AI_HANDOFF.md`, `SYSTEM_OVERVIEW.txt`, `OVERNIGHT.md`, and `CHANGELOG.md`.

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
