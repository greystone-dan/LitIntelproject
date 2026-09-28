# Task: FC Activity coverage improvement

Status: complete
Created: 2026-09-27
Updated: 2026-09-27

Task: Improve deterministic FC Activity intelligence using large real-data samples, prioritizing decision-subject/tribunal extraction, judge-stage coverage, hearing semantics, and procedural-delay coverage.

Why now: The seeded 100-record real-data report works end to end but reports 88% unknown decision subjects and 2% removal-delay coverage, so the output is not yet a dependable management-statistics layer.

Owner surface: `scripts/classify_fc_activity.py`, `scripts/evaluate_fc_activity_deterministic.py`, focused Activity tests, and bounded evaluation artifacts.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing `fc_activity_cases`/`fc_activity_documents`, deterministic classifier, local Ollama `qwen3:4b` review probe, and existing gold-template workflow.

Risk boundary: Preserve raw Activity records and canonical judgment/citation/statute layers. No schema/API change, bulk database write, external/paid model call, or automatic LLM promotion. All model output remains evidence-linked review only.

Hypothesis: If deterministic rules are expanded from patterns observed in a large real-data sample, and each new rule is validated against source evidence plus a bounded gold set, unknown rates and event coverage will improve without reducing traceability.

Smallest falsifiable check: Run a bounded real-data sample, quantify unknown/coverage dimensions and evidence completeness, add tests for the highest-volume missing patterns, then rerun the same report and compare metrics.

Acceptance criteria:
- Real-data coverage report is reproducible at a larger bounded sample with explicit denominators.
- Decision-maker/tribunal and subject extraction improves on reviewed real examples without inventing values.
- Delay and hearing signals distinguish missing data from unsupported inference.
- Local LLM is used only for bounded candidate review of deterministic gaps and cannot write production facts.
- Focused tests, compilation, canonical documentation, and Swimm walkthrough are updated.

Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`; `.swm/fc-ingest-source-pipeline.sw.md`; real reports under `data/eval/`; no schema migration.

Rollback/recovery: Revert only classifier/evaluator/tests/docs/task changes from this task. Delete new bounded evaluation artifacts if needed. Do not touch raw Activity tables or prior reports.

Evidence: Delegated real-data pattern review identified explicit Refugee Appeal
Division/RPD/RAD/CRDD, PRRA/ERAR, visa-office, and Immigration Division forms.
Implemented only explicit refugee-protection subject markers and a bounded
decision-maker fallback in `scripts/classify_fc_activity.py`. Added focused
tests for `IRB-RPD` and Refugee Appeal Division wording. Focused classifier
validation passed: 26 tests. The reproducible 100-record evaluator rerun
completed with no database writes: 84 closed, 16 active, 21
`refugee_protection`, 67 unknown subjects, and 2% valid removal-delay
coverage. Canonical documentation updated in `SYSTEM_REFERENCE.md` and
`docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`; Swimm checkpoint updated in
`.swm/fc-ingest-source-pipeline.sw.md`.
The next bounded stay-pattern slice added full English month-name
normalization and explicit `removal ... on [weekday] Month day, year` support,
with a focused positive test. The same real-data rerun completed without
database writes; the new event propagated `2023-01-31` for Activity case
219785, while aggregate valid delay coverage remained 2% because it did not
complete another filing/removal interval. All focused tests now pass: 40.

The judge-coverage slice consumed a bounded real-sample review and added
explicit French `Monsieur/Madame le juge`, English `BEFORE The Honourable ...
Justice`, initials, and hearing-metadata delimiters. Focused classifier tests
passed: 28; the full Activity-focused suite passed: 41. The same seeded
100-record evaluator completed without database writes: judge-identified cases
rose from 43 to 63, final-decision coverage from 32% to 42%, hearing-stage
coverage from 1% to 6%, and motion-stage coverage reached 2%. Hearing unknowns
were preserved where no explicit hearing evidence exists. Canonical and Swimm
documentation were updated in this checkpoint.

Delegated work: Completed bounded real-data pattern review; findings consumed.

Focused validation: `pytest tests/test_classify_fc_activity.py tests/test_evaluate_fc_activity_deterministic.py tests/test_review_fc_activity_local.py -q` passed with 43 tests; then a bounded real-data evaluator run remains the next coverage check.

The workbook-derived date-semantics slice added bounded matching for rendered
Federal Court orders where judge/location text appears between `rendered` and
the date. Decision events now prefer the explicit rendered/order date while
retaining an explicit later `filing_date`; the original Activity `DOC_DT`
remains `source_document_date`. Existing filing-date precedence for stay and
other non-decision events is preserved. The exact Pinard leave-order regression
and the focused Activity classifier/evaluator/review suite pass: 43 tests.
The workbook was read-only reference material and was not modified.

Files changed: `scripts/classify_fc_activity.py`,
`tests/test_classify_fc_activity.py`, `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`,
`.swm/fc-ingest-source-pipeline.sw.md`, and this task record.

Delegated work: Explore performed a read-only inventory of the classifier and
the 500/1000-case evaluation artifacts, identifying high-confidence backlog,
program, institutional-name, and history-selection gaps. No delegated files
were changed.

Focused validation: the identical recent-weighted 1,000-case evaluation used
`recent_years=16`, `recent_share=0.7`, and seed `20261001`; final output is
`data/eval/fc_activity_real_evaluation_20261001_1000_final_iteration.json`.
Subject unknowns fell from 658 to 547, maker unknowns from 237 to 130, event
counts remained unchanged, and evidence completeness remained 6,805. The
focused Activity suite passed 59 tests; `py_compile` and `git diff --check`
also passed.

Residual risk: 547/1000 subjects remain unknown because many Activity records
name only a generic office, agency, or tribunal without stating the underlying
immigration subject. The history-wide selection is explicit-only and must not
infer a subject from institutional identity.

Next bounded task: review the remaining 547 unknown subjects for explicit
application-program wording in linked records, starting with Electronic Travel
Authorization, sponsored-landing, and legacy tribunal formulations; add only
source-backed rules with before/after precision checks.

The recent-weighted 500-case evaluation (`recent_years=16`, `recent_share=0.7`,
seed `20261001`) then consumed explicit originating-application subject gaps.
SPR/SAR/PRRA and French refugee-protection wording added 24 refugee subjects;
H&C/Humanitarian Migration, Express Entry/family-program wording, and
Visitor's Visa added 7 more explicit subjects. Unknown decision subjects fell
from 335/500 to 304/500. Decision-maker unknowns and evidence completeness did
not regress, and the broader Activity validation passed 50 tests. Generic
agency or office references remain unknown by design when they do not state a
subject.

Next bounded task: Build a small reviewed JSON gold set from the seeded Activity
sample so precision/recall can be measured before further rule expansion.

The deeper generic-reference audit added `decision_subject_availability` and
`decision_subject_label`. On the regenerated 1,000-case report, the states are
461 `explicit_subject`, 437 `generic_institution_only`, and 8
`no_subject_evidence`. Representative retained generic labels include IRCC
CPC, visa office/embassy, IRB/IAD, CBSA, MPSEP, GTEC, and French border or
immigration agencies. The remaining eight are primarily receipt/service rows
or opaque legacy office codes; they remain unclassified rather than inferred.
