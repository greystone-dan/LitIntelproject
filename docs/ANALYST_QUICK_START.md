# iLit Analyst Quick Start

For a first research task, use the active **Data Explorer** at `/data-explorer`.
iLit helps navigate stored Canadian immigration decisions and research signals;
it is not a legal citator, an official court record, or legal advice. Verify
important findings against authoritative sources.

## Find and read a case

1. In **Research → Case search**, enter a case name or citation, such as
   `Vavilov` or `2019 SCC 65`. Suggestions appear after two characters. Search
   starts with title/citation matching; open **Advanced options** to filter by
   court, year, judge, decision or government outcome, or Minister/government
   party. Turn on full-decision-text search only when you need text matches.
2. Open a result. Check the title, citation, court, date, source, and available
   text before relying on it. Choose chunk breakdown or full text to read the
   decision. Yellow marks are case citations; purple marks are statutes and
   regulations; green marks are tags. Open a linked authority only after
   checking its identity: a link means a local match, not that the cited
   proposition is correct.

## Note up with Citation Intelligence

In **Research → Citation Intelligence**, search for a case or select one from
Case Search. Review its citing decisions and citation counts, then use the
Timeline to narrow stored citation evidence to a year. Outcomes, Courts/Judges,
Statutes, and evidence/table views provide additional context where available.
Open citing decisions and read the passages yourself. Counts are stored
mentions, not distinct controlling authorities; a year trend or outcome
association does not establish how a court treated an authority or that it
caused an outcome.

## Judge profiles and Federal Court activity

- **Judge Profile** is the only active judge workflow; the standalone Judge
  Outcomes view is retired. Search a judge by name to see known aliases, linked
  decisions, and outcome/year information. The profile summarizes government
  wins, classified decisions, all linked decisions, and government win rate:
  government wins ÷ classified decisions, with unclassified decisions excluded.
  Its optional Minister filter narrows the linked decisions; it does not report
  an individual Minister's performance. Treat the profile as a way to find
  records, not to infer bias or assume complete judicial coverage.
- In **FC History**, enter an IMM number (for example, `IMM-1234-19`) to view
  available Federal Court leave/judicial-review procedural history and activity
  context. The activity summary provides an annual filed-case chart, top
  registry locations, recorded case classes, and filing tracks for a selected
  filing location. These are bounded aggregations of activity fields, not
  official reasons, proof that a judgment was captured, or measures of
  procedural success. A shared IMM number alone does not prove records concern
  the same proceeding.

## Check citations in a memo

Open `/memo-citation-check`, choose a DOCX or text-based PDF (up to 10 MB), and
select **Analyze document**. The page lists detected authorities, which ones
match the local library, treatment information when available, and commonly
cited authorities on the same issues that were not found in the draft. These
are context leads, not recommendations. Scanned PDFs are not OCR'd. The page
describes this upload as temporary and not stored, logged, or sent to external
services. A missing authority is a lead to investigate, not a required
citation; treatment labels and citation matches must be checked against the
decisions.

## Read outcomes and win rates carefully

Outcome labels are derived research classifications based on disposition and
party-role evidence. A government win describes the government side's recorded
outcome, not the merits of a case. In Judge Profile, only records labelled
government `won` or `lost` count as classified for the win-rate calculation.
Other values—including `mixed`, `undetermined`, or missing—are counted as
unclassified and excluded from the rate. Unclassified is not itself a loss or
proof that a case was undecided; check the decision for its recorded outcome.

The government win rate is government wins ÷ classified decisions. Unclassified
decisions remain in the total decision count but are excluded from the rate.
Always report the numerator, classified denominator, total and unclassified
counts, and the cohort/time scope; small denominators, source gaps, and
classification error can distort comparisons. A Minister filter scopes cases
or linked decisions; it does not create an individual Minister's performance
rate. Rates are not proof of causation, judicial bias, or legal merit.

## What this tool does not do

iLit does not decide what the law requires, validate a legal proposition,
replace an authoritative source, or guarantee complete or official case
coverage. It does not establish that a citation is good law, that an outcome
was caused by a cited authority or a judge, or that a suggested authority must
be used. It does not provide legal advice. Treat its links, classifications,
counts, and suggestions as starting points for verification.

For current interface details and limitations, see the
[Research UI Guide](RESEARCH_UI_GUIDE.md).
