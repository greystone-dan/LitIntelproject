# Task: Portable saved-search alert digest

Task: Implement issue #121 without sending alerts.
Why now: Recorded alerts need portable, traceable research summaries.
Owner surface: Saved-search digest presentation and read-only adapters.
Commit allowed: yes
Push allowed: yes
Dependencies: Existing saved-search alerts and reader-extracted outcome metadata.
Risk boundary: No database operations during implementation/validation, dotenv or credential reads, network, migrations, dependencies, deployment, or changes to existing checks.
Smallest falsifiable check: `python -m pytest tests/test_alert_digest.py -q` (local dependency availability permitting).
Acceptance criteria: Pure JSON/HTML/text builder; exact >=5 / >=20 percentage-point shift threshold with counts; offline CLI; mocked read-only GET routes preceding parameterized routes; existing behavior preserved.
Docs/generated references: SYSTEM_REFERENCE.md; .swm/1.oi7rhqp2.sw.md; API/script generators and appendix embedder.
Rollback/recovery: Revert only this change; no data writes or schema changes.
Evidence:
- Managed-worker inventory returned structured field/route/test findings. Bounded worker review found null discovery timestamps could escape CLI error handling; repaired with a regression test.
- `python -m unittest tests.test_alert_digest tests.test_build_alert_digest -v`: 9 passed under the session-only offline guard.
- Focused pytest (builder, CLI, saved-search routes/checker) and full `python -m pytest -q` with all three CI deselects were attempted: blocked before collection, `No module named pytest`.
- `python -m py_compile` passed for builder, routes, CLI and the three touched test modules; `git diff --check` passed.
- CLI `--help` and offline manual html/text/json output-file checks, exact-threshold counts, and invalid timestamp exit 2 passed.
- `python scripts/generate_script_catalog.py` regenerated the script reference. Existing appendix-generator helper regenerated only the affected script appendix, preserving unrelated baseline embedded documentation.
- `python scripts/generate_api_reference.py` blocked: missing FastAPI. `python scripts/check_generated_docs.py` blocked: missing FastAPI and SQLAlchemy; no API reference hand edits.
- Canonical doc updated: SYSTEM_REFERENCE.md. Swimm updated: .swm/1.oi7rhqp2.sw.md. Added local link targets verified.
- No database connections, dotenv or credential reads, dependency downloads, deployments, commits or pushes. Progress-tool unavailable; complete pre-edit checklist reported in chat. Parent retains final review.
Status: blocked

Files changed: backend/alert_digest.py; backend/routes.py; scripts/build_alert_digest.py; scripts/generate_script_catalog.py; tests/test_alert_digest.py; tests/test_build_alert_digest.py; tests/test_saved_search_routes.py; SYSTEM_REFERENCE.md; docs/SCRIPT_CATALOG.generated.md; .swm/1.oi7rhqp2.sw.md; this record.
Residual risk: FastAPI integration and full suite unverified; generated API reference does not yet include the new routes. No available dependency-equipped runtime was found, and network installs are forbidden.
Next bounded task: Parent review in an existing dependency-equipped offline environment: run focused/full mocked pytest, regenerate API reference, check generated docs, then regenerate affected embedded API appendix.

Hypothesis: Deduplicated decision cohorts with explicit Minister losses produce a shift only at the required sample sizes and exact integer threshold, without altering saved-search state.
