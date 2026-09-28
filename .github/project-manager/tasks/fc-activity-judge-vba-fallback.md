# Task: Port high-recall VBA judge patterns safely

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Port the useful high-recall judge patterns observed in the Beta VBA while retaining evidence-gated Python extraction.
Why now: The post-Chief/Associate audit found 38 cases with explicit judge-language but no observation, including French titles, Acting Chief Justice, and names preceding Prothonotary.
Owner surface: `_judge_name()` in `scripts/classify_fc_activity.py` and focused classifier fixtures.
Dependencies: Beta workbook read-only VBA inspection and fixed post-change IMM-15 report.
Risk boundary: Add only explicit title/order patterns; do not adopt VBA first-match behavior or broad unqualified name extraction.
Smallest falsifiable check: Representative English, French, acting-chief, and name-before-prothonotary fixtures must extract the intended name while existing tests remain green.
Acceptance criteria:
- Recognize `Madame la juge`, `Monsieur le juge`, `juge en chef`, `Acting Chief Justice`, and `Name, Esq., Prothonotary` forms.
- Preserve evidence-linked event text and existing title behavior.
- Re-run the fixed 1,000-case judge coverage evaluation and inspect remaining unmatched judicial language.
- Update canonical and Swimm documentation with measured results.
Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`.
Rollback/recovery: Revert only the fallback patterns and fixtures; no database or raw-data changes.
Commit allowed: yes
Push allowed: yes
Evidence: Beta `ExtractJudge` searches the first literal `Justice ` anywhere; Python now ports the useful high-recall forms with explicit procedural context. Added French `Madame/Monsieur la/le juge`, `juge en chef`, `Acting Chief Justice`, honourable-title fallback, parenthesized French rendered-by wording, and names before Prothonotary/Protonotaire in rendered-by or oral-directions records. The focused suite passed 64 tests. The fixed 1,000-case IMM-15 report increased any-judge coverage from 751/1,000 (75.1%) to 844/1,000 (84.4%), gaining 93 cases; only five residual records contain judge-related words without a named Federal Court judge.
Files changed: `scripts/classify_fc_activity.py`, `tests/test_classify_fc_activity.py`, this task record, and the post-change evaluation artifact under `data/eval/`.
Focused validation: `python -m pytest tests/test_classify_fc_activity.py -q` passed (`64 passed`); the fixed 1,000-case read-only evaluator completed with `database_written=false`; residual audit found only unnamed presiding-judge references or a citizenship judge outside the target court.
Residual risk: Broader fallback patterns can raise false positives in cited-case narrative; the remaining five records are intentionally left unresolved because four contain only unnamed presiding-judge language and one names a non-Federal-Court citizenship judge. Raw any-judge coverage is not the primary quality denominator: among 853 cases with a decision, hearing, or motion stage, 839 have a judge observation (98.36%); final-decision and hearing stages are both 100% covered.
Next bounded task: Review the remaining unmatched judge-language cases for additional high-precision forms.
