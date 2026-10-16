# Federal Court decision structure and the printed-headings outline

Measured on 1,760 Federal Court decisions (80 a year, 2004-2025). Rules only, no model calls.

## Layout of an FC decision
- Header block ("Court (s) Database ... Decision Content ..."), then a title line: JUDGMENT AND REASONS (48.8%), REASONS FOR JUDGMENT AND JUDGMENT (29.3%), REASONS FOR ORDER AND ORDER (10.8%).
- Numbered paragraphs `[n]`; headings are short lines between them. In the export 22.5% of headings are glued onto the paragraph line (`II. Analysis A. Question? [9] text`).
- Tail block: "JUDGMENT in IMM-..." / "THIS COURT'S JUDGMENT" (60.5%) or ORDER (23.9%), then counsel; sometimes footnotes after.

## Reading the headings (`backend/contextual_authority/heading_reader.py`)
- Prefixes: roman, letter, digit, (a), or none; glued headings are split from their paragraph.
- A heading must lead to a numbered paragraph (through other headings or list lines).
- Not headings: issue-list items ("There are two issues: 1. ... 2. ..."), statute marginal notes, transcripts (Q./A.), table-of-contents lines, addresses, judge names.
- Each heading gets a standard label (issues, standard, background, decision_under_review, analysis, conclusion, costs, certified_question, submissions ...). "Respondent's submissions" style headings no longer start the Analysis.

## Using them in the outline (`ILIT_OUTLINE_HEADINGS`, default off)
- Printed headings set the section starts; printed sub-headings become the sub-points; numbered list lines are dropped as points.
- Rows the court did not print carry `printed: false`, and the reader shows "inferred" beside them.
- Decisions with fewer than 15 numbered paragraphs (fewer than 4 for the Federal Court of Appeal, where 44% are short) and fewer than 3 printed headings show only the Disposition.

## Check against the sample (section start equals the printed heading's paragraph)
| Section | Before | With headings on |
| --- | --- | --- |
| Analysis | 78% | 93% (98% within one paragraph) |
| Issues | 71% | 76% |
| Disposition | 92% | 92% |

## Supreme Court of Canada and Federal Court of Appeal (flag `ILIT_OUTLINE_HEADINGS`)
Measured on 1,034 SCC and 1,000 FCA decisions.
- SCC paragraphs are numbered "1 text" from 2000 to 2007 and "[1] text" after; the heading reader reads both.
- Separate opinions (`backend/contextual_authority/opinions.py`): the SCC header index ("Dissenting Reasons: (paras. 46 to 123)", 77% of decisions) first, then the reasons' opening lines ("... was delivered by", "Abella J. (dissenting) —"). On indexed decisions the opening lines match the index count in 95%. FCA decisions take the author and concurring judges from the cover block ("REASONS FOR JUDGMENT BY / CONCURRED IN BY").
- A decision with several opinions gets one `opinion` row per opinion (level 0) and its own sections under each. Only the lead opinion has a Disposition; before this, 86% of multi-opinion SCC decisions put it inside a dissent, now 4% do.
- Single sets of reasons get one author row when the header or cover block names the author.
