# Citation resolution inventory readiness

Status: complete
Created: 2026-09-06
Updated: 2026-09-06

Task: Make the case-to-case citation resolution path safe and efficient enough to run across the full case inventory while keeping statute extraction and resolution as a separate layer.
Why now: The repository now separates extraction from target resolution and the SCC run is complete, but the resolution runner still needs a resumable, low-friction path for whole-corpus execution.
Owner surface: `scripts/resolve_citation_targets.py`, `scripts/resolve_short_citation_targets.py`, and the citation-resolution logic in `backend/citations.py`.
Dependencies: Existing citation extraction, local case index, PostgreSQL writer availability, and the current case inventory.
Risk boundary: Keep case citations and statute references separate; do not alter extraction semantics, source offsets, or browser-side evidence handling.
Smallest falsifiable check: Run the focused citation test file and a bounded resolution dry run that demonstrates the script can resume and process a sample of unresolved rows without changing extraction behavior.
Acceptance criteria:
- Resolution scripts can resume mid-run and report progress without restarting the full batch.
- Full-inventory resolution is practical with batched updates and a single-case index.
- Citation extraction behavior remains unchanged for the relevant tests.
- Statute handling remains in its own layer and is not folded into the case-citation resolution path.
Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/blank.dudtv9pz.sw.md`.
Rollback/recovery: Use the same script with `--resume-from-id` or the stored last checkpoint; no destructive DB rollback is required for the bounded dry run.
Evidence: See the evidence section below.
Commit allowed: yes
Push allowed: yes

## Hypothesis

If the resolution scripts build a reusable local citation index and support explicit resume checkpoints, then we can run the whole-corpus case-citation resolution path without repeating expensive scans or losing progress.

## Evidence

- Focused regression: `.\venv\Scripts\python.exe -m pytest tests/test_citations.py -k "local_case_resolution_index or rebuild_citations_for_case_leaves_alias_resolution_for_later_pass" -q` passed with `2 passed, 108 deselected`.
- Bounded dry run: `.\venv\Scripts\python.exe scripts\resolve_citation_targets.py --batch-size 250 --limit 1000 --resume-from-id 0 --dry-run` inspected 1,000 rows, built 84,160 local keys, and made no writes.
- Resume dry run: the same command resumed from `3503962`, inspected the next 1,000 rows, and ended at `3508623`, confirming checkpoint progression without writes.
- Coverage verification: exact lookups found no canonical case rows for `2012 FC 729`, `2010 FC 745`, `2003 CANLII 68792`, or `1993 CANLII 3011`; `1993 CANLII 105` is represented by canonical SCC case `id=35894`, `Canada (Attorney General) v. Ward`, under `[1993] 2 SCR 689`, showing that cross-citation equivalence is required before classifying a target as missing.
- Whole-set write run: `.\venv\Scripts\python.exe scripts\resolve_citation_targets.py --batch-size 250 --resume-from-id 0` completed with `1,631,124` inspected rows reported by the runner and `667,318` links added during the pass; final database verification reports `2,152,332` total citations, `1,188,526` linked, and `963,806` unresolved.
- Safety: the initial 5,000-row attempt was interrupted during a bulk update; the smaller-batch rerun completed with exit code `0`, and the post-run database counts are consistent.
- Documentation checkpoints: `SYSTEM_REFERENCE.md` and `.swm/blank.dudtv9pz.sw.md`.

## Outcome

The case-to-case local resolution layer is inventory-ready: it builds a single reusable case index, resolves ambiguous duplicates conservatively, and supports explicit `--resume-from-id` progress checkpoints without widening into the statute layer.

## Residual risk

The bounded samples produced zero links for the sampled keys because their formal CanLII and Federal Court forms were absent from the local citation index. At least one apparent absence, `1993 CANLII 105`, maps to an existing SCC case through its reported citation `[1993] 2 SCR 689`; a full write run should preserve unresolved rows until reported/CanLII equivalence is implemented or audited.
