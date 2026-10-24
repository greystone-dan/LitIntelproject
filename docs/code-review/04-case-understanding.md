# Code Review 4/11: Case Understanding

## Summary

Reviewed all 30 in-scope backend paths on the `main` base commit `d2bcb41`; the five files under `backend/case_types/` were included. Scope is Federal Court, Federal Court of Appeal, and Supreme Court of Canada only. No source code, tests, configuration, or generated documentation was changed. No reviewed path was found sending uploaded or typed user text to an external model or service. Workbench notes and tracked-file data are persisted under a demo identity, and deployment-level upload spooling and request-log retention were not assessed.

All in-scope files were read; none could not be finished.

## Bugs

- `/home/runner/work/LitIntelproject/LitIntelproject/backend/case_frame.py:131-133,247-248` — **Medium.** `build_frame` records Crown-applicant cases as `"crown"`, but `CaseFrame.text()` treats every known value other than `"yes"` as an individual applicant. This misdescribes Crown criminal proceedings, including in-scope appellate courts. Add a separate Crown branch or omit that generic sentence for `"crown"`.
- `/home/runner/work/LitIntelproject/LitIntelproject/backend/case_frame_store.py:24-32,56-60`; `/home/runner/work/LitIntelproject/LitIntelproject/backend/case_comparison.py:57-58` — **Low.** The comparison logic accepts `denied` and `refused`, but `RESULT_WORDS` does not. A stored outcome with either value therefore produces no Result line. Add display labels for both.
- `/home/runner/work/LitIntelproject/LitIntelproject/backend/case_frame_plus.py:276-278` — **Low.** The raw regex uses `\\bIRCC\\b`, matching literal backslash-b text rather than word boundaries. An introduction identified only by “IRCC” can be classified as “not an immigration matter.” Use `\bIRCC\b`.
- `/home/runner/work/LitIntelproject/LitIntelproject/backend/case_summary_card.py:210-218,231-236` — **Low.** When the disposition paragraph is also the most-cited paragraph, the duplicate-selection branch adds the second rule but returns without preserving its citation count. Update the selected item’s count when merging the citation rule.
- `/home/runner/work/LitIntelproject/LitIntelproject/backend/case_types/taxonomy.py:240-245` — **Medium.** The contempt pattern contains literal backspace characters around `contempt`, not regex word-boundary escapes, so normal occurrences do not match. Replace them with `\b`.
- `/home/runner/work/LitIntelproject/LitIntelproject/backend/case_processing.py:162-180` — **Possible, Low.** `stage_order or STAGE_ORDER` makes an explicit empty list run every stage. If `[]` is meant to request no stages, default only when `stage_order is None`.

## Privacy / security risks

- `/home/runner/work/LitIntelproject/LitIntelproject/backend/workbench.py:100-115,379-388`; `/home/runner/work/LitIntelproject/LitIntelproject/backend/pages/workbench.py:133-135` — **Possible, Medium.** Workbench ownership is a deterministic slug of a typed name stored in a client cookie; anyone can sign in using another demo user’s name and access that bucket. The page warns that sign-in is not real authentication and says not to enter sensitive data, but notes and tracked-file information are still stored. Use authenticated server-issued identities, or keep the feature clearly non-private and restrict it to disposable demo data.
- `/home/runner/work/LitIntelproject/LitIntelproject/backend/routes.py:2479-2481` (call site outside the listed file set); `/home/runner/work/LitIntelproject/LitIntelproject/backend/discussion_units_sandbox.py:72-85` — **Possible, Medium.** The ordinary `/cases/{case_id}/paragraph-assessments` endpoint calls the sandbox loader with `enforce_cohort=False`, bypassing its default 300-case cohort check and exposing experimental assessment roles/explanations by case ID. Put the endpoint behind the development/sandbox gate and enforce cohort membership on every serving path. Deployment-level access controls were not assessed.
- `/home/runner/work/LitIntelproject/LitIntelproject/backend/workbench.py:572-576` — **Possible, Low.** The CSV formula guard checks only the first character. A value with leading whitespace/control characters before a formula marker may still be interpreted as a formula by some spreadsheet software. Guard the first non-whitespace/control character and add fixtures for prefixed formulas.

No external model or service call with user-provided text was identified in the reviewed analysis, memo, de-identification, or Workbench modules. This source review does not establish whether a server, proxy, or multipart parser spools or logs request bodies; those deployment limits are also noted in `/home/runner/work/LitIntelproject/LitIntelproject/docs/reports/privacy-security-review.md:21-26,75-89`.

## Data-correctness risks

- `/home/runner/work/LitIntelproject/LitIntelproject/backend/live_analysis.py:42-56` — **Medium.** DOCX extraction iterates `document.paragraphs` only, omitting paragraph text in tables. Citations or analysis-relevant content in a memo’s tables are silently absent from the returned text and evidence offsets. Traverse document body blocks in order and include table-cell paragraphs while preserving source offsets.
- `/home/runner/work/LitIntelproject/LitIntelproject/backend/legal_tagger.py:225-230,334-355` — **Medium.** Outcome rules search the entire document and create a case-level outcome tag when any matching phrase appears. A passage reporting an earlier proceeding’s outcome can therefore label the current decision incorrectly. Derive outcome tags from the current court’s operative disposition; retain other matches only as mention-level evidence.
- `/home/runner/work/LitIntelproject/LitIntelproject/backend/case_processing.py:12,122-156,162-180`; `/home/runner/work/LitIntelproject/LitIntelproject/backend/legal_tagger_v3.py:1,11-12,42-47`; `/home/runner/work/LitIntelproject/LitIntelproject/SYSTEM_REFERENCE.md:713-719` — **Medium.** The V3 tagger describes itself as inactive and requires the proposal to remain `proposed`, but the default processing order runs `tags_v3`, deletes/replaces that taxonomy’s rows, and the module declares the same version active. This writes review-only mention tags by default, contrary to the documented review-only status and the requirement that experimental features be off by default. Keep the stage opt-in and do not mark the taxonomy active until reviewed.

## Performance

- `/home/runner/work/LitIntelproject/LitIntelproject/backend/case_summary_card.py:78-99,265-280` — **Low.** `_numbered_paragraphs()` traverses the same formatted blocks once for every tag. Compute the verified paragraph list once before iterating tags and reuse it.

## Dead code / cleanup

No high-confidence dead-code finding was established in this bounded review. Versioned tagger layers have distinct contracts; broader caller reachability was not audited.

## Suggestions

- Add focused regression fixtures for Crown-role wording, denied/refused result display, IRCC-only classification, contempt matching, duplicate summary-card selections, and outcomes mentioned only for another proceeding.
- Add DOCX table-extraction coverage and a test that confirms the configured text cap includes every separator.
- Keep extracted mention signals visibly distinct from holdings and dispositions, and keep experimental assessment endpoints behind the same cohort/development gate as the sandbox UI.
- Continue treating de-identification as a human-reviewed aid, not a guarantee of anonymity; the existing privacy review documents its coverage limits.
