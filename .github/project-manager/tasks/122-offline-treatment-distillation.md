# Task: Offline treatment distillation

Status: deferred
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Use a tightly bounded OpenAI teacher-labeling process to discover treatment-language examples, then produce local artifacts that run without external AI at runtime.

Why now: The product requirement is explicit: external AI may assist development within an approximately $10 budget, but the deployed contextual layer must run offline and preserve citation evidence.

Owner surface: `backend/contextual_authority/`, bounded teacher/export scripts, local artifacts under approved evaluation paths, focused tests, and documentation.

Commit allowed: yes

Push allowed: yes

Dependencies: Phase 0 context units, deterministic observations, weak-supervision voting substrate, OpenAI configuration conventions, bounded evaluation fixtures.

Risk boundary: No secrets in source or logs; no unbounded API calls; no canonical database mutation; no runtime API dependency; no automatic publication of teacher labels; no legal merits conclusions.

Smallest falsifiable check: A bounded fixture can be converted into a redacted teacher-label request contract and then consumed by a local deterministic artifact without requiring a network call.

Acceptance criteria:

- Define an offline-first teacher example/label contract with provenance and budget metadata.
- Add a dry-run request builder that never calls OpenAI by default.
- Add a local distillation/evaluation path that can consume reviewed labels without external AI.
- Keep treatment labels citation-linked, evidence-span based, and explicitly provisional until reviewed.
- Add tests for redaction, budget accounting, no-network default, and deterministic local output.
- Update canonical and Swimm documentation with the teacher-versus-runtime boundary.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, and task evidence.

Rollback/recovery: Remove only the teacher contract, bounded scripts, local fixture artifacts, tests, and docs. Never expose credentials or rewrite canonical evidence.

Evidence: Phase 0, deterministic observations, and weak-supervision agreement substrate are complete. Combined contextual/citation regression passed with 166 tests. Explore confirmed existing OpenAI configuration, budget, dry-run, JSONL, and audit-report patterns in `scripts/verify_citation_extraction.py` and `scripts/embed_openai_chunks.py`. Online research found eyecite (BSD-2-Clause) and LexNLP (AGPL-3.0) useful for citation extraction but no clearly licensed ready-made authority-treatment lexicon; Blackstone (Apache-2.0) is a UK-focused legal NLP model, and LegalBench is an evaluation collection rather than a treatment lexicon. Added citation-centered fixture generation with second-half-by-chunk sampling, a bounded asymmetric window with twice as much post-citation context, richer legal-context sampling signals, and a no-network, hard-capped teacher batch preparation command; focused contract tests now pass (12). A bounded 100-row database-backed fixture was generated at `data/eval/treatment_teacher_candidate_100.jsonl`; all citation spans reconstruct exactly, and the prepared no-network request reports 100 examples, `network_called: false`, and estimated cost `$0.004269`. The fixture and preparation limits were raised to 2,500, including a larger 25,000-row read-only candidate pool so second-half filtering does not stop at the old 1,000-row ceiling. The resulting `data/eval/treatment_teacher_candidate_2500.jsonl` contains 2,500 rows: all citation spans reconstruct exactly, all source hashes and `review_required` labels are present, and all eight signal families are represented. The prepared `data/eval/treatment_teacher_batch_2500.json` reports 2,500 examples, `network_called: false`, and estimated cost `$0.177979`. Added the approved bounded sender with exact-span validation, unique phrase-offset repair, duplicate-label rejection, response checkpointing, and a current user-approved hard spend ceiling of `$3` for this session. Paid evidence: the initial 500-example attempt spent `$0.0260969` but produced truncated JSON; the refined samples spent `$0.0080464` for 80 examples and `$0.0086738` for 90 examples, yielding 42 and 53 valid labels respectively. The offset-1,000 sample spent `$0.0095115` for 70 examples and yielded 44 valid labels, including supportive, absent, and distinguishing treatments. No canonical database writes occurred; runtime publication remains blocked pending review and local distillation.

## Hypothesis

If a small, redacted teacher-labeled fixture is versioned with exact evidence spans and budget accounting, then treatment cues can be distilled into a local runtime artifact without requiring OpenAI after development.

## Plan

1. Delegate a bounded read-only inventory of OpenAI/configuration and evaluation conventions.
2. Implement teacher request contracts, redaction, budget accounting, and dry-run-only request generation.
3. Implement local rule distillation/evaluation over reviewed labels without network access.
4. Validate budget, provenance, no-network, and exact-span invariants.
5. Update canonical and Swimm documentation; request approval before any paid API invocation.

## Execution Checkpoints

- Delegation: Explore completed a read-only repository inventory; online research checked eyecite, LexNLP, Blackstone, LegalBench, Legal-BERT/LexGLUE availability, Canada Justice Laws, and CanLII access. No files changed and no external API was called.
- Implementation: Added `scripts/build_treatment_teacher_fixture.py`, `scripts/prepare_treatment_teacher_batch.py`, and `backend/contextual_authority/teacher_contract.py`; no OpenAI call made.
- Documentation: `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md` updated.
- Recovery: no API request or model training run until explicit final preflight approval.

## Completion

Completion recorded: no

Summary: Offline treatment distillation is deferred at the provisional review checkpoint. The teacher contract, paid raw-response evidence, source-revalidated distillation report, and fixture-backed human review packet remain preserved for later adjudication at `data/eval/treatment_distillation_candidate.json`, `data/eval/treatment_distillation_review_packet.json`, and `data/eval/treatment_distillation_review_packet.md`. No treatment label, rule, or model is runtime-active.

Validation: `pytest tests/test_teacher_contract.py -q` passed (14); explicit compilation passed; `git diff --check` passed. The site refresh started the local API and tunnel; its wrapper timed out while the long-running tunnel continued. Paid calls used only the approved development runner and stayed below the user’s `$3` hard cap. The distillation report and separate review packet were generated read-only. The packet contains 19 repeated rules and 90 priority labels, including all absent/distinguishing labels and repaired-span cases; every item now includes fixture-backed decision context with citation and treatment offsets, and remains `runtime_publishable: false`.

Residual risk: Teacher labels can be wrong or overconfident; every label must remain provisional and reviewable.

Next recommended task: Resume only when a human-reviewed treatment subset is available; begin with the preserved packet and do not make further paid teacher calls until the review gap and treatment-label balance are addressed.
