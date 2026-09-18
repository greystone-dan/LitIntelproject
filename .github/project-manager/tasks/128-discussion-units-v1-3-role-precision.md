Task: Refine remaining Discussion Unit role-cue false positives.
Why now: Four-case external review confirmed V1.2 is useful for low-trust review but identified procedural claim nouns, generic governing-rule under cues, and narrative contrast transitions as remaining precision defects.
Owner surface: backend/contextual_authority/subthemes.py and focused role-cue tests.
Dependencies: V1.2 implementation, four regenerated packets, external review pasted in chat.
Risk boundary: Deterministic, offline, additive evidence layer only. No database writes, migrations, runtime activation, new role taxonomy, or segmentation changes.
Smallest falsifiable check: Add positive and negative exact-context tests for claim nouns, explicit advocacy claims, legal versus corporate under phrases, and argumentative versus narrative contrast; focused tests must pass without losing retained positives.
Acceptance criteria: Role-cue refinements are covered by adversarial tests, existing focused tests remain green, and documentation/task evidence records the distinction between this role slice and the separate 18674 segmentation issue.
Docs/generated references: SYSTEM_REFERENCE.md, .swm/8.upryk5h6.sw.md, data/eval/discussion_units_external_review_prompt.txt.
Rollback/recovery: Revert only task 128 source/test/documentation edits; preserve V1.2 packets and task 127 evidence.
Evidence: Delegated inspection confirmed packet-level false positives for `refugee claims`, `on this claim`, and non-doctrinal `under` phrases; no material contrast-gating defect was found. Implemented V1.3 procedural claim and non-rule `under` gates in `backend/contextual_authority/subthemes.py` with adversarial tests. Focused validation `.venv\Scripts\python.exe -m pytest tests/test_subthemes_v1.py -q` passed with 11 tests; combined focused validation for `tests/test_subthemes_v1.py` and `tests/test_discussion_unit_inspector.py` passed with 16 tests. Regenerated V1.3 packets for cases 677, 1093, 1171, and 18674 using the read-only paragraph inspector; packet contract passed with all nested version fields `1.3`, positive paragraph counts, matching Markdown case IDs, and zero canonical/contextual writes. Updated [SYSTEM_REFERENCE.md](../../../../SYSTEM_REFERENCE.md), [.swm/8.upryk5h6.sw.md](../../../../.swm/8.upryk5h6.sw.md), and [discussion_units_external_review_prompt.txt](../../../data/eval/discussion_units_external_review_prompt.txt). The separate 18674 segmentation issue remains out of scope. Commit allowed: yes. Push allowed: yes.
Status: complete
Commit allowed: yes
Push allowed: yes
Status: complete
Commit allowed: yes
Push allowed: yes
