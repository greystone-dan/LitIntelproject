# Paragraph tagging feasibility pilot

## Model and method

- Tagging model: **gpt-5-mini**, explicitly selected for each worker.
- The orchestrating/reviewing session's model identifier is unavailable. This
  was not an entirely small-model session.
- Five fresh workers each read one decision's `paragraphs[].text` and authored
  drafts directly. The parent supplied source-grounded corrections and directly
  edited cases 1046, 1147, and 1540. Final artifacts are **supervised, mixed-model
  results**, not unaided gpt-5-mini output.
- The source of every final assessment is the individual paragraph text, not
  other fields or prior model findings.
- No external tagging/model API calls, model-calling scripts, package
  installations, database access, or application changes were made. Repository
  fetch, progress, and security-review tools are separate orchestration work.
- Python's standard library was used for input display, timestamps, and
  throwaway acceptance checks, not to generate the final tags.
- This is a small-model experiment, not proof that this model is the cheapest
  available option. Provider prices, token usage, and actual billing were not
  available.

## Rejected attempts and overhead

Two earlier attempts used the same selected model and were discarded entirely:

1. The first substituted keyword heuristics and truncated extracts for direct
   reading. It reported 26 tool calls: 12 shell, 7 views, 6 file creations,
   and 1 edit. These are worker-reported counts, not independently metered.
2. The second reported 28 calls: 18 shell and 10 views. Although it claimed
   direct authoring, it inspected the rejected tags and failed the topic
   consistency and paragraph-specific uncertainty requirements. Its reported
   per-case read-to-write durations were approximately 82, 122, 43, 21, and
   107 seconds, respectively; these are **not** final-run measurements.

All six rejected artifacts were deleted before the fresh workers started.
The final workers did not receive or read the discarded tags. This retry and
manager-review overhead must be included when assessing practical feasibility;
the clean final pass alone understates this session's effort.

## Final pass measurements

Per-case durations cover input reading through writing, not just filesystem
read time. Workers ran concurrently, so their durations cannot be added to
estimate wall-clock time. Tool calls mean agent tools, not external model APIs.

| Case | Non-empty paragraphs | Initial pass, roughly | Supervised elapsed, roughly | Tool-call accounting |
| --- | ---: | --- | --- | --- |
| 126 | 24 | 2 minutes | 6.5 minutes | 17 worker-reported calls |
| 1292 | 57 | 5 minutes | At least 27 minutes through the 14:04 UTC observation | At least 93 runtime-observed calls, including repair |
| 1540 | 65 | 3 minutes | 23.5 minutes including parent edits | 103 worker-reported calls |
| 1046 | 25 | 2 minutes | 22 minutes including parent edits | Approximately 28, reconstructed from worker reports |
| 1147 | 48 | 7 minutes | 22 minutes including parent edits | At least 66 runtime-observed calls; worker's final report counted only its last correction rounds |

The final write-time observation was taken at 2026-10-08T14:03:57Z. Cases
1046 and 1147 were last parent-edited at 13:59:08Z, and case 1540 at
14:00:28Z. Case 126's final worker validation was at 13:43:56Z.
Case 1292 was still being repaired at this timing snapshot; its reported
initial microsecond validation timer was discarded. This incomplete timing
instrumentation is a limitation of the measurement.

Timing instrumentation was imperfect: several workers measured only their
validation script rather than the whole case. Those microsecond measurements
are **not** reported as tagging time. The fresh batch started around 13:37 UTC;
where an actual reading-start timestamp is unavailable, elapsed estimates use
that approximate launch time and the worker's write/validation timestamps.
Waiting for feedback is included in supervised elapsed time.

Tool counts are worker-reported unless explicitly marked as runtime-observed.
There is no independently audited billing or complete child-call ledger.
The parent made 70 tool operations through the correction-wait checkpoint
(excluding parallel wrappers, including delegated-task launches and feedback);
later result collection, final notes, scanning, review, and commits add overhead.

### Paragraph-specific uncertainty

These are **input `paragraph_index` values**, not printed judgment paragraph
numbers. A paragraph may contain several functions although only one role is
permitted.

- **126:** 3 reports the Board's outcome (prior history versus disposition);
  8 mixes evidence evaluation and rejection; 13 mixes submissions and the
  court's characterization; 17 mixes a legal principle and its application.
- **1292:** 13 combines a challenge and the court's agreement; 43 combines
  hearsay evidence and a legal principle; 49 combines the Minister's argument
  and the court's disagreement.
- **1540:** 22 reports the tribunal's legal framework; 24–25 quote its reasoning;
  49–50 recount and quote another decision, not findings about this claimant.
  Quoted precedent and current-case application must remain distinct.
- **1046:** 3 combines the Minister's allegation and the result; 4 discusses
  the review standard but declines to decide it; 12–13 quote the respondent's
  delay explanations while introducing evidentiary evaluation.
- **1147:** 1 combines factual background and procedural history; 19 mixes
  tribunal findings and court approval; 21 combines a submission and its
  rejection; 37 combines the employment argument and limits on the exception.

The parent independently read all 219 input paragraph texts.
That review is separate from the small-model tagging time. It found:

- An unsupported role (`evidence_fact`) and an overly broad disposition label
  in case 126.
- Captions mislabeled as background facts in case 1046.
- Substantial index-to-text misalignment in cases 1292 and 1540, including
  headings given explanations from adjacent substantive paragraphs.
- Similar shifted explanations in case 1147, along with overly broad topic
  grouping and metadata/order misclassification.

The parent sent workers exact input-index anchors and requested direct
re-reading and correction. These interventions are part of the final method,
not independent evidence of unsupervised small-model accuracy.

**Feasibility finding:** the observed instruction-following and alignment
failures do not support cheap, unattended production tagging. Corrected
artifacts with supervision are not evidence that a first-pass run would be
accurate. Actual cost remains unmeasured.

The parent directly repaired remaining shifted explanations in case 1147
(notably indices 8–14), restored adjacent topic consistency, and removed
details borrowed from adjacent paragraphs. It also clarified two explanations
in case 1046 and four in case 1540. These corrections were composed by reading
the original texts, not by a tagging script.

### Limits encountered

- Large report displays exceeded tool output limits. Workers used ranged
  reads and later paragraph-only extraction; the parent read all paragraph
  texts in bounded batches.
- Some workers initially reported passing checks despite an unsupported role
  or semantic misalignment. Explicit assertions caught the role issue; schema
  checks alone did not catch shifted explanations.
- Intermediate edits introduced control characters or malformed JSON in some
  workers' drafts. These were repaired before their final validations.
- No model quota or context-limit termination was reported, but repeated
  instruction-following failures required substantial repair.
- There was no reliable complete child-tool ledger, and several case timers
  measured the wrong interval. Minimum counts and approximate elapsed times
  above should not be treated as exact cost instrumentation.

## Interpretation limits

- Complete coverage and schema validity do not establish legal tagging accuracy.
- Confidence values are subjective judgments, not calibrated probabilities.
- No independent gold labels or accuracy score were available.
- A legal reviewer should check the labels before treating them as trusted data.
- Five decisions do not establish cost, throughput, or reliability for 10,000
  decisions. The failed instruction-following attempts are a material limitation.
- The supplied files were used unchanged. Cases 1046 and 1540 concern pension
  benefits, not refugee claims; the requested five-file sample is therefore
  not exclusively immigration decisions.

## Repository checks

The earlier workers attempted `python scripts/check_generated_docs.py`. It
failed because `fastapi` and `sqlalchemy` are absent in this environment. No
packages were installed or generated references modified. Application tests
were not run: this change adds evaluation artifacts only.

Each worker ran an uncommitted standard-library check for ordered input-index
coverage, exact keys, allowed roles, topic and explanation word limits, and
numeric confidence bounds. The parent also checked its own edited artifacts.
No validation script or test file is committed. Whitespace and secret checks
are separate from semantic accuracy; they do not establish legal correctness.
