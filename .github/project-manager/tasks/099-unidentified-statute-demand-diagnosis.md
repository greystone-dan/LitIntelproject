# Task: Diagnose unidentified statute demand

Status: complete
Created: 2026-09-15
Updated: 2026-09-15

## Task Record

Task: Identify the recurring authority names and extraction shapes behind the unidentified statute-reference population.

Why now: The live ranking shows 440,266 statute references with no instrument key. Their composition must be understood before adding XML sources or changing extraction rules.

Owner surface: read-only statute extraction demand diagnosis

Commit allowed: yes

Push allowed: yes

Dependencies: statute_references data, backend/statutes.py, backend/citations.py, scripts/index_legislation.py

Risk boundary: Read-only investigation only. Do not run extraction writers, corpus backfills, source downloads, paid APIs, or alter existing rows.

Smallest falsifiable check: Rank unidentified normalized references and raw forms, then classify the top recurring patterns against the registry and existing XML coverage.

Acceptance criteria:

- Exact unidentified row, case, and distinct-reference counts are recorded.
- Top recurring unidentified forms are grouped into actionable extraction/source categories.
- Existing registry and XML coverage are compared without writes.
- One narrow next experiment is selected with a falsifiable validation check.

Docs/generated references: SYSTEM_REFERENCE.md; ROADMAP.md; .swm/4.9nn3id9f.sw.md

Rollback/recovery: No data changes authorized; delete this task record only if the investigation is abandoned.

Evidence: Read-only live inventory found 440,266 unidentified rows across 33,460 cases, with 110,640 normalized forms and 75,804 raw forms. Top recurring forms included Indian Act (4,946), Constitution Act (4,882), Civil Code (4,791), Patent Act (3,731), Federal Court Rules (3,662), and NOC Regulations (2,433). Partitioning found 21,961 IRPA-shaped rows, 4,777 Federal Court Rules-shaped rows, and 34 IRPR-shaped rows that appear recoverable by existing registry identity; 374,028 rows remain other unidentified. No extraction writer, backfill, source download, or paid API ran.

## Hypothesis

If the unidentified population is dominated by recurring named instruments or stable section-form patterns, then a small registry/source/rule slice should recover a measurable share without broad extraction changes.

## Plan

1. Count and rank unidentified normalized and raw reference forms.
2. Classify recurring forms against known instruments and XML coverage.
3. Select one bounded extractor/source experiment.
4. Document findings before any writer is considered.

## Execution Checkpoints

- Delegation: Explore requested a bounded read-only inventory; returned output was not accessible through the harness and is not treated as evidence.
- Direct inventory: Completed against the configured database with summary, normalized-form, raw-form, and category-partition queries.
- Implementation: None authorized.
- Documentation: Pending findings checkpoint.

## Completion

Completion recorded: yes

Summary: The unidentified population is mixed. A recoverable stale/identity gap exists for known IRPA, IRPR, and Federal Court Rules-shaped rows, while the largest remaining population requires authority-name and citation-shape classification before XML prioritization.

Validation: Read-only SQL queries completed successfully; no database writes occurred.

Residual risk: Unidentified rows may include parser failures, generic legal language, unresolved instruments, and stale rows from earlier extraction behavior.

Next recommended task: Run a bounded identity-recovery dry run for known-instrument-shaped rows, then produce a sampled catalogue of the 374,028 other-unidentified rows before adding new XML sources.
