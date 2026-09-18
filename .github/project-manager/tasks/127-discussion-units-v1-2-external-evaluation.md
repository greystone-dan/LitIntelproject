Task: Improve Discussion Unit V1.2 precision and expand external evaluation packets.
Why now: External review of case 677 found overinclusive party-position and limitation cues and a broad multi-function sub-theme; more cases are needed before accepting changes.
Owner surface: backend/contextual_authority/subthemes.py and its focused tests; evaluation packet generation and OneDrive review handoff.
Dependencies: Existing V1.1 tests, case packets 677/1093/1171/18674, deterministic inspector, and data/copilot_review/.
Risk boundary: Offline and additive only. No database writes, migrations, network calls, runtime activation, or changes to canonical judgment data.
Smallest falsifiable check: Run focused sub-theme tests and regenerate a bounded multi-case packet set; any new role cue must reduce false positives without losing explicit advocacy or disposition cues.
Acceptance criteria: V1.2 cue precision is covered by positive/negative tests; four populated evaluation cases have regenerated Markdown and JSON packets; a single OneDrive prompt identifies all source files, immutable-input rules, review questions, and chat output contract; focused validation passes. Additional local candidates that produced empty packets are excluded rather than counted.
Docs/generated references: SYSTEM_REFERENCE.md, relevant .swm walkthrough, data/eval/discussion_units_external_review_prompt.txt, data/copilot_review/README.md.
Rollback/recovery: Revert only the V1.2 source/test/docs/task changes; preserve existing V1.1 packets and external handoff files.
Evidence: Delegated inspection identified the V1.2 owner logic and existing packet workflow. Updated `backend/contextual_authority/subthemes.py` and `tests/test_subthemes_v1.py` for procedural claim suppression, retained explicit advocacy claims, procedural although suppression, and bounded soft-contrast context. Regenerated V2 packets for cases 677, 1093, 1171, and 18674 with chunk_set=paragraph; all have non-empty paragraph inputs and zero canonical/contextual writes. Replaced `data/eval/discussion_units_external_review_prompt.txt` with a single absolute-OneDrive-path prompt requiring the complete response to be pasted into chat. Updated `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md`. Focused validation: `pytest tests/test_subthemes_v1.py tests/test_discussion_unit_inspector.py -q` -> 15 passed; packet contract check -> passed for all four cases; `git diff --check` -> passed.
Status: complete
Commit allowed: yes
Push allowed: yes
