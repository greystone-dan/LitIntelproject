# Task: Salvage usable paragraph assessments

Status: complete
Created: 2026-09-24
Updated: 2026-09-24

## Task Record

Task: Preserve valid partial paragraph assessments from the paused 300-case run.
Why now: The model returned useful indexed rows but the strict all-paragraph contract discarded them when output was truncated or incomplete.
Owner surface: `scripts/package_discussion_units_llm.py` and its focused tests.
Dependencies: Paused paragraph run artifacts and existing paragraph assessment renderer.
Risk boundary: Never fabricate missing assessments; reject malformed JSON, duplicate indices, and indices absent from the source request.
Smallest falsifiable check: `venv\\Scripts\\python.exe -m pytest tests/test_package_discussion_units_llm.py -q`.
Acceptance criteria:
- Valid uniquely indexed subset responses are accepted and rendered.
- Returned rows are ordered by source paragraph order.
- Missing rows remain absent and are not synthesized.
- Duplicate or out-of-source indices still fail.
Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/6.maiixtsw.sw.md`; no generated references require editing.
Rollback/recovery: Revert the parser/test/documentation changes; the paused ledger and raw responses remain unchanged.
Evidence: `venv\\Scripts\\python.exe -m pytest tests/test_package_discussion_units_llm.py -q` passed with 13 tests; offline replay validation and compile/diff checks passed. Updated `SYSTEM_REFERENCE.md` and `.swm/6.maiixtsw.sw.md`.
Commit allowed: yes
Push allowed: yes
