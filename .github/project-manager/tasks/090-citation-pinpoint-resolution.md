Task:
Link explicit case-citation paragraph pinpoints to the cited case's stored paragraph evidence in the active reader, without reopening citation target resolution or unresolved-name matching.

Why now:
The prior target-resolution process linked citation rows to target cases, but it did not link `at para. N` references to target paragraph chunks. The reader already exposed `target_paragraph` and `target_chunk_text`, but the target chunk map was never populated, so paragraph previews remained empty.

Owner surface:
scripts/link_citation_pinpoints.py

Dependencies:
backend/database.py, alembic/versions/0024_citation_target_paragraph.py, case_chunks, citations

Risk boundary:
Update only already target-resolved citation rows with an explicit paragraph pinpoint and exactly one matching paragraph chunk. Preserve citation extraction, target resolution, source offsets, and case-vs-statute separation.

Smallest falsifiable check:
.\venv\Scripts\python.exe scripts\link_citation_pinpoints.py

Acceptance criteria:
- A resolved citation with `at para. N` stores the matching target paragraph and chunk IDs.
- Paragraph ranges stored on chunks are respected when locating a pinpoint.
- Only exactly-one matches are updated; missing or ambiguous chunks remain unchanged.
- The active reader can project the stored target chunk text.
- Focused citation/API tests and the full dry-run pass.

Docs/generated references:
- SYSTEM_REFERENCE.md
- .swm/4.9nn3id9f.sw.md

Rollback/recovery:
The backfill is idempotent because it selects only rows with a null target paragraph. If rollback is required, clear only the rows recorded by the bounded run using their citation IDs; do not rerun citation extraction or target resolution.

Evidence:
- Migration `0024_citation_target_paragraph` added nullable `target_paragraph` and `target_chunk_id` fields and was applied successfully.
- The set-based `scripts/link_citation_pinpoints.py` dry-run completed: `inspected=276864`, `linked=183010`, `missing_chunk=93854`, `invalid=0`.
- Apply completed successfully: `updated=183010`.
- Read-only integrity verification: `183010` rows have both fields; all linked chunks are `chunk_set='paragraph'`, paragraph ranges match, and case mismatches are `0`.
- Focused validation: `tests/test_citations.py tests/test_api.py -q` -> `185 passed, 1 warning`; compilation passed.

Status:
complete

Summary:
Added a set-based database backfill for already target-resolved citations. It stores the first explicit paragraph pinpoint and the uniquely matching target paragraph chunk, without reopening target resolution or extraction.

Residual risk:
`93854` eligible citations had no unique matching paragraph chunk and remain unlinked. Multi-paragraph forms such as ranges or lists still store only the first extracted paragraph because the durable schema currently supports one target paragraph and one target chunk per citation.

Next bounded task:
Add explicit multi-paragraph storage and matching only after the single-paragraph backfill is reviewed against reader requirements.

Commit allowed: yes
Push allowed: yes
