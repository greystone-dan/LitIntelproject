# Federal Court Activity Worker Runbook

Last reviewed: 2026-09-25

## Purpose and Boundary

This runbook defines the preparation contract for running Federal Court activity
collection independently of the public CaseLibrary website. It covers discovery,
staging, classification, checkpoints, and operator recovery. It does not authorize
Oracle tenancy access, VM creation, canonical database writes, or hosting of
protected/personal data.

FC activity is a separate research layer. It is not a judgment, judgment text,
legal outcome, or replacement for the canonical case-ingestion path. Discovery,
detail retrieval, document capture, classification, and canonical import remain
distinct states.

## Intended Topology

```text
Federal Court portal/API
        |
        v
Oracle worker (future, approval-gated)
  discovery -> JSONL/SQLite staging -> deterministic classification
        |
        v
bounded artifact review and checkpoint backup
        |
        v
separately approved, exclusive database import
```

The first deployment should run acquisition and staging only. Keep the public
website and its database outside the worker until an operator has approved the
import contract, credentials, network controls, and writer ownership.

## Current Components

| Stage | Component | Output/boundary |
| --- | --- | --- |
| Portal listing/detail discovery | `scripts/fc_portal_collector.py` | JSONL staging; checkpointed, delayed, retried, robots-aware; no canonical DB write |
| Procedural history | `scripts/fetch_fc_procedural_history.py` | Sequential per-IMM activity retrieval; 2,000 ms default minimum delay plus jitter; bounded API attempts; `--write-activity` targets only `fc_activity_*` |
| Activity normalization | `backend/fc_activity.py` | Stable source keys and document/event normalization |
| Classification | `scripts/classify_fc_activity.py` | Deterministic classification; DB write requires explicit `--write` |
| Deterministic evaluation | `scripts/evaluate_fc_activity_deterministic.py` | Bounded coverage and delay metrics; no database write |
| Local review probe | `scripts/review_fc_activity_local.py` | One evidence-constrained, abstaining review; never writes production facts |
| Dataset import | `scripts/ingest_hf_fc_activity.py` | FC activity tables only; use dry-run and exclusive writer control |

Never describe an identifier or detail page as a captured judgment unless a
validated document payload and provenance evidence exist.

## Bounded Local Checks

Run from the repository root with the project interpreter:

```powershell
.\venv\Scripts\python.exe scripts\fc_portal_collector.py --help
.\venv\Scripts\python.exe scripts\fetch_fc_procedural_history.py --help
.\venv\Scripts\python.exe scripts\classify_fc_activity.py --help
.\venv\Scripts\python.exe -m pytest tests\test_classify_fc_activity.py tests\test_hf_fc_activity_ingest.py -q
```

Before any live collection, confirm the intended output path and use a small
page/record limit. Review the JSONL or SQLite staging artifact before any
import. The Court does not publish a robots policy; our collector therefore
uses its own sequential delay, jitter, retry, and request-budget controls.

The 2026-09-25 decision-portal discovery check was inconclusive: both an
IMM-only and a default-prefix one-page/five-record attempt exited with
`Scanned=0 Written=0` and produced no JSONL or checkpoint artifact. This is not
FC Activity evidence and is outside the activity-only path.

The correct FC Activity endpoint path was then validated with a bounded
sequential dry-run. Five candidates were attempted and 63 activity records were
returned with exit code 0. The endpoint was reached, no database write occurred,
and the fetcher did not expose output/checkpoint paths for that dry-run.

The endpoint adapter is now available through an explicit `--write-activity`
flag. It uses a stable IMM-based case key, stable IMM/entry document hashes,
retains endpoint document identifiers when present, and writes only
`fc_activity_cases` and `fc_activity_documents`. It does not write
`fc_procedural_history` or canonical `cases` in that mode. The next step is a
bounded live Activity-only write followed by count and rerun-deduplication checks.

The Activity writer treats a complete `(re_no, docno)` pair as the primary
document identity within a case and skips repeated identities before insert;
entries missing either key retain entry-hash deduplication. This protects
resumable runs from endpoint responses that repeat a registry document with
different text or hashes. Conflicting content for an existing complete identity
is preserved as the first captured row and remains a review signal.

The derived classification remains nested in `classification_json` and includes
evidence-linked judge observations grouped by `leave`, `motion`, `hearing`, and
`final_decision`; structured challenged-decision maker and subject fields; and
a conservative lifecycle status of `closed`, `abeyance`, `active`, or
`unknown`. `active` is inferred only from substantive activity without a
terminal signal and carries lower confidence; age alone never closes a record.
Explicit no-appearance wording is excluded from held-hearing signals. The
evaluator reports denominators and coverage for these fields before bulk
reclassification or local-LLM review.

## Full-Inventory Classification Recovery

The deterministic classifier writes only to `fc_activity_classifications` and
keeps its source-case relationship inside the FC Activity layer. A full local
inventory run is bounded by `--batch-size` and records an atomic JSON checkpoint
only after each database batch commits. The database version check is the
authoritative skip guard: rows already carrying `fc_activity_v5` are skipped on
rerun, including when the process stopped after a commit but before its
checkpoint was replaced. Use `--force` only for an intentional full
reclassification.

The approximately 300k run command is documented here but was not executed as
part of this change:

```powershell
.\venv\Scripts\python.exe -u scripts\classify_fc_activity.py --all --write --batch-size 500 --state-file data\overnight_runs\fc-activity-classification-v5\state.json --resume
```

Keep the state file with the run artifacts and resume the same file after an
interruption. A stale checkpoint is safe to replay because current-version
rows are skipped; missing or older-version rows remain eligible. Verify
source-case and classification counts, and inspect version/source-layer
distributions after the run. `FCActivityCase.source_type`, `source_name`, and
`source_id` are nullable. The HF A2AJ importer sets them only for rows it
directly imports, and mirrors that known provenance to an existing
classification row. Existing rows without source evidence remain unknown.
This layer remains separate from canonical `cases` and
`fc_procedural_history`; analytics must group by FC Activity source fields and
cover the full `fc_activity_cases` inventory without a canonical-case join.
The read-only `/api/fc-activity/analytics` endpoint accepts `source_type` and
returns `source_counts`; use `source_type=a2aj` when reviewing the A2AJ
reference layer separately.

The 2026-09-27 real-data checkpoint classified five records as a smoke test and
evaluated a seeded 100-record cross-year sample without database writes. The
sample contained 84 `closed` and 16 `active` lifecycle states, 32% final-
decision judge-stage coverage, 67% unknown decision subjects, and 2% valid
filing/removal and motion/removal intervals. The evaluator's seeded sampling
path uses set-based cohort splitting; the prior list-membership implementation
was O(N2) on the full inventory and was corrected before this checkpoint.

The coverage-improvement rerun identified 21 explicit `refugee_protection`
subjects from Refugee Appeal/RPD/RAD/CRDD and bilingual refugee-section
wording. The classifier intentionally leaves rows without an explicit subject
marker as `unknown` rather than inferring from a generic immigration context.
The same pass recognizes explicit month-first removal dates such as `on Monday
January 31, 2023`. This improved event-level evidence without changing the
sample's 2% valid delay rate because no additional complete interval resulted.

The judge-coverage pass added explicit French `Monsieur/Madame le juge` and
English `BEFORE The Honourable ... Justice` forms, including initials and
hearing-metadata delimiters. In the same seeded sample, judge-identified cases
rose from 43 to 63; final-decision coverage rose from 32% to 42%,
hearing-stage coverage from 1% to 6%, and motion-stage coverage reached 2%.
Silent hearing dockets remain unknown rather than being inferred.

The stabilized classification also contains stage-aware `milestone_rollups`,
challenged-decision `decision_maker_type`, `underlying_tribunal` and
`underlying_tribunal_type`, and `decision_subject`. Hearing evidence is
classified as `scheduled`, `held`, `reserved`, or `not_held`; bilingual
negation remains negative evidence and is not emitted as a positive hearing
event. The evaluator's `analytics` object provides queryable dimension counts,
and `--gold-set PATH` adds seeded field-level coverage, accuracy, and
disagreement metrics from a JSON review set. These remain report-only until
semantics and review gates stabilize; no migration or API exposure is implied.

The existing local text-generation abstraction is permitted only for a bounded
offline/local review suggestion containing source evidence and an explicit
abstain option. It must not write data or promote a suggestion to a production
fact. A provider-unavailable or nonconforming response is recorded as a
blocker. The configured local Ollama service was verified on 2026-09-27 with
installed model `qwen3:4b`; the bounded probe returned source-linked JSON after
the default model was corrected. Reproduce the bounded probe with:

```powershell
$env:TEXT_GENERATION_PROVIDER = "local"
.\venv\Scripts\python.exe scripts\review_fc_activity_local.py --text "Order granting a motion to stay removal, heard by Justice Example on 10-MAY-2024."
```

The harvester waits at least 2 seconds between IMM candidates by default, with
optional positive jitter, and enforces a hard request-attempt budget including
retries. Adaptive collection is explicit: use `--adaptive-delay` with a
`--batch-size` (20 is the default) to report checkpoints, pause on a fetch
issue, and back off the inter-candidate delay. `--issue-pause-ms` defaults to
5,000 and `--backoff-factor` defaults to 2.0, capped by `--max-delay-ms`.
A separate `--diagnostic-allow-sub-2000ms-delay` switch permits a shorter
starting delay, such as 100 ms, only for a bounded diagnostic or explicitly
reviewed run. Keep the request budget and stop on budget exhaustion, repeated
server failures, or uncertain database state.

Use `--log-file PATH` to mirror the live console output to a line-buffered UTF-8
log. In another PowerShell window, monitor it with:

```powershell
Get-Content .\data\raw\fc\activity-20260925.log -Wait
```

The log includes candidate progress, endpoint warnings, adaptive pauses,
backoff changes, batch checkpoints, and final API-attempt totals.

Classification is offline and deterministic when run against local staged input.
Use `--dry-run` where supported. `--write` and any canonical import are separate
operator actions and must not run concurrently with another PostgreSQL writer.

## Deterministic Evaluation Checkpoint

Run the bounded classifier evaluation before treating Activity events as
management statistics:

```powershell
.\venv\Scripts\python.exe -m pytest tests\test_classify_fc_activity.py tests\test_evaluate_fc_activity_deterministic.py tests\test_audit_fc_activity_openai.py -q
.\venv\Scripts\python.exe scripts\evaluate_fc_activity_deterministic.py --sample-size 100 --recent-years 7 --recent-share 0.7 --seed 20260925 --output data\eval\fc_activity_deterministic_evaluation_20260925.json
```

The report is read-only and records event coverage, year weighting, unknowns,
ambiguities, and evidence completeness. Derived events remain observations
over raw Activity documents. A source `DOC_DT` must not be promoted to a filing,
hearing, or decision date without explicit semantic wording; missing evidence
is not evidence that a disposition did not occur.

For bounded model feedback, generate a larger deterministic report when broad
sampling is needed (for example, `--sample-size 1000`). The report includes
bounded source-document excerpts; `scripts/audit_fc_activity_openai.py` uses
those excerpts for review-only feedback and never promotes model output. A
review batch must record its seed, sample overlap, actual token cost, and
`database_written: false`. Only repeated source-supported gaps become
deterministic rules. Explicit filed or served notices of appearance are emitted
as `appearance_filed` with subtype `notice_of_appearance`.

For a human-readable review, export a bounded cohort and build the companion
report:

```powershell
.\venv\Scripts\python.exe scripts\export_fc_activity_package.py --output data\copilot_exports\fc_activity_manual_audit_10_20260927 --limit 10 --per-year 1 --sample-seed 20260927 --cohort-name manual-audit-10
.\venv\Scripts\python.exe scripts\build_fc_activity_audit_report.py --package data\copilot_exports\fc_activity_manual_audit_10_20260927 --output data\copilot_exports\fc_activity_manual_audit_10_20260927\audit_report.md
```

The Markdown report presents each case summary, deterministic findings, linked
source text, and explicit audit gaps. Its JSON companion is suitable for
programmatic review. A missing classification remains a review condition, not
evidence that no procedural history exists.

Decision-date semantics remain separate in extracted Activity events. When a
decision entry contains both an explicit rendered/order date and a later filed
date, `event_date` selects the rendered/order date, `filing_date` retains the
explicit filed date, and `source_document_date` remains the registry `DOC_DT`.
Filing dates remain preferred for filing, motion, and stay events. These are
Activity observations only and do not rewrite canonical judgment dates.

The originating-application subject classifier also recognizes only explicit
subject markers: SPR/SAR/PRRA and French refugee-protection sections map to
`refugee_protection`; `H&C` and Humanitarian Migration map to
`humanitarian_and_compassionate`; Express Entry and explicit family/spousal
program wording map to `permanent_residence`; and Visitor's Visa maps to
`temporary_residence`. Generic visa-office, IRCC, CBSA, or IRB references
remain `unknown` when the underlying immigration subject is not stated.
In the seeded 500-case run weighted toward 2010-present, these rules reduced
unknown subjects from 335 to 304 without changing evidence completeness or
decision-maker coverage.

Subject and decision-maker evidence is selected across the full linked Activity
history, not only the first originating-application entry. The originating
entry remains authoritative for application type, decision date, and parsed
maker text; later explicit records may fill `decision_subject` or
`decision_maker_type` and expose their supporting document identifiers and
text. On the seeded 1,000-case run weighted toward 2010-present, this reduced
subject unknowns from 658 to 547 and decision-maker unknowns from 237 to 130,
with event counts and evidence completeness unchanged. Generic institutional
references still do not infer a legal subject.

The Activity report distinguishes `decision_subject_availability` as
`explicit_subject`, `generic_institution_only`, or `no_subject_evidence`.
Examples of useful generic labels include `IRCC CPC OTTAWA`, `VISA OFFICE,
UKRAINE`, `Canadian Embassy Mexico`, `IRB (IAD)`, `CBSA`, `MPSEP`, `GTEC`, and
French `Agence des Services Frontaliers du Canada`. These labels are retained
in `decision_subject_label` when no legal subject is stated. In the final
1,000-case audit, 461 cases had explicit subjects, 437 had generic institutional
evidence only, and 8 had no subject evidence; the latter are mostly service,
receipt, or opaque office-code entries and remain unknown by design.

Leave decisions use the VBA-derived priority model from
`scripts/fetch_fc_procedural_history.py`. Explicit granted/refused wording is
selected first, including registry shorthand such as `Result - leave granted`,
`Leave dismissed`, and French `Demande d'autorisation refusée`. If an eligible
leave application has no observed outcome, the classifier keeps
`leave_decision.result = unknown` but exposes `leave_context.status = pending`.
Discontinued, withdrawn, administratively terminated, direct-review, and later
judicial-review inferred-grant states remain distinct and evidence-linked.

On the fixed 1,000-case sample, the change converted 14 prior unknown leave
results into explicit outcomes (7 granted and 7 refused). It produced 104
pending leave applications, while 302 cases were categorized as inferred or
not applicable. Event counts did not change.

For stay statistics, explicit `removal has been cancelled`, `removal was
cancelled`, and equivalent English wording is classified as an implicit granted
stay with source evidence and rule `stay_cancellation`. Treat this as a
procedural signal requiring review: cancellation wording may describe an
administrative change rather than a judicial stay, and bilingual equivalents
remain an evaluation gap.

When a stay or removal entry explicitly says that removal was `scheduled for`
or `set for` a date, derived stay events retain that normalized
`removal_scheduled_date` and an optional bounded destination phrase. Use these
fields for later filing-to-removal or motion-to-removal delay metrics only;
never replace `DOC_DT` or infer that a scheduled removal occurred.

The report exposes these delay metrics as additive read-only output. A valid
interval requires both explicit anchor and scheduled-removal dates; missing
dates and an anchor after the scheduled removal are counted as separate status
categories rather than coerced into zero or negative delays. In the 2026-09-25
100-record checkpoint, filing-to-removal and motion-to-removal each had three
valid intervals and one ambiguous date-order case.
Each metric also reports `case_count`, `valid_count`, and `coverage_rate`; the
current sample coverage is 3%, so these distributions are not population
estimates.

## External AI Handoff Package

Use `scripts/export_fc_activity_package.py` to give an external AI such as
Claude a reproducible, read-only Activity package without database credentials:

```powershell
.\venv\Scripts\python.exe scripts/export_fc_activity_package.py `
        --output data\copilot_exports\fc_activity_claude_<run-id> --limit 3
```

The exporter refuses to overwrite an existing directory. Remove `--limit` for
the full inventory only after confirming available disk space. The package
contains `cases.jsonl` (case metadata and `raw_payload`), `documents.jsonl`
(procedural entries and `raw_document`), `classifications.jsonl` (complete
deterministic classification rows), and `manifest.json` (counts, joins,
classifier versions, provenance, and limitations). A case limit applies to
case rows; all linked documents and classifications are included. JSONL is
UTF-8 without a BOM.

Claude must treat `cases.jsonl` and `documents.jsonl` as source evidence and
`classifications.jsonl` as derived observations. It must not infer a missing
event from an empty document list, treat an Activity row as a judgment, or
replace source evidence with an untraceable summary. Historical BOM-prefixed
IMM values should be normalized at the package boundary. The exporter performs
no network requests and no database writes.

An OpenAI audit is optional and bounded. Use the approved `gpt-4.1-nano`
sample only with `--send`, keep the budget at or below `$5`, and verify the
output records model, prompt/sample settings, token usage, estimated cost,
findings, and `database_written: false`. The 2026-09-26 checkpoint used 12
records, 75% recent-year weighting, and estimated `$0.001548` spend. Audit
findings currently prioritize clearer final-decision markers and explicit
filing-date labels; they do not authorize canonical writes or replace the
deterministic classifier.

## Future VM Contract

The VM bootstrap must be reproducible and must not contain credentials. It must
record:

- ARM64/x86 architecture and Python/PostgreSQL/pgvector compatibility checks;
- a dedicated non-root worker account and restricted outbound/inbound rules;
- repository revision, interpreter version, dependency lock/checksum evidence;
- separate paths for staging, checkpoints, logs, and temporary downloads;
- filesystem capacity and egress monitoring, with bounded limits and stop rules;
- lock ownership so only one collector or database writer runs at a time;
- atomic checkpoint and artifact backup/restore procedures;
- patching, health checks, log rotation, and decommission steps.

Do not place `.env`, database passwords, API keys, tunnel credentials, or cloud
private keys in the repository, VM image, task record, or staging artifacts.

## Approval Gate

Oracle provisioning requires explicit user approval before account login,
network/resource creation, credential entry, or remote execution. Before that
gate, resolve the intended data classification, authorization model, source
terms, retention, backup, incident response, and whether the worker will ever
write to PostgreSQL. A public cloud VM is not an access-control solution for the
website.

## Recovery and Stop Conditions

Stop the worker when robots policy blocks access, the source format changes,
checkpoint integrity is uncertain, disk/egress limits are approached, repeated
requests fail, or another writer owns the destination. Preserve the raw error,
last checkpoint, command arguments without secrets, and staging hashes. Resume
from the last verified checkpoint after review; do not delete or rewrite source
history to hide a partial run.
