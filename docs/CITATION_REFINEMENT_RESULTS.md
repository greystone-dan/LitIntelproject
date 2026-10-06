# Citation refinement: results on real decisions (2026-10-06)

Measured on the Federal Court (FC) and Federal Court of Appeal (FCA) decisions in the A2AJ open dataset
(200 French and 200 English decisions per court, random). The reference list is the dataset's own
`cases_cited` field (neutral citations only), so this measures neutral-citation recall, not names or pinpoints.

| Court / language | Pass one recall | Refined recall |
|---|---|---|
| FC, French | 1.2% | 99.9% |
| FC, English | 99.1% | 100% |
| FCA, French | 4.0% | 99.9% |
| FCA, English | 98.2% | 99.8% |

Pass one (the live extractor) misses almost every French citation: `2019 CSC 65`, `2020 CF 895`,
`[2019] 4 RCS 653`, `[1990] 1 C.F. 199`. About 13 of 15 French decisions had no row at all.
The refinement layer already handled those forms. Its one gap was a neutral cite written directly
after an opening parenthesis (`(2004 CF 88)`, `(2013 CAF 733)`), which is how French decisions cite
the lower court; fixed in this change. A French pinpoint (`au paragraphe 13`) was normalised as
`at para. e 13`; also fixed.

Rows refined finds that the reference list lacks are almost all Tax Court cites (`2018 CCI 75`),
which the reference list does not cover; no false neutral cites were seen.
The "dropped" rows (33 in 300 English decisions) were party names from the title block ("Emma Uwase v. THE"),
not citations; no pass-one row went missing without an explanation.

Not measured here: case-name and pinpoint correctness, the 55 ambiguous matches (a resolution issue),
and statute references. `scripts/build_refined_citations.py` writes refined rows beside the live table
(dry run by default, resumable, revertable); nothing reads them yet.
