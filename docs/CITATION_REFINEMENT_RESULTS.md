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

## Bare landmark short forms (step `C4b_landmarks`)

Of the 426 live decisions that mention Vavilov without a Vavilov citation row, 335 are French (cited as `2019 CSC 65`,
fixed above). Most of the English remainder cite it by name only ("Vavilov at para 85") with no full citation anywhere in
the decision, which pass one cannot link because it needs an earlier full citation. Checked on 2025 FC 198, 2025 FC 834 and
2026 FC 736: pass one finds no Vavilov row, the new step finds every mention. The step knows nine fixed landmark names
(Vavilov, Dunsmuir, Khosa, Kanthasamy, Agraira, Newfoundland Nurses, Doré, Mason, Baker) and only fires on
"<Name> at para N" (or French "au para N") that no other row already covers. In 800 random A2AJ decisions it added only 3 rows
(most decisions give the full citation), so it matters mainly for decisions like the ones above.

## Weak pass-one short forms and name-only rows (checked on the stage-1 rows written to the database)

A hand check of 300 random rows from the first 1,000 refined decisions found the new rows (French cites, backrefs, parallel
cites, landmark short forms) sound, but about a third of the pass-one short forms ("case_short", 27% of all rows) point at
the wrong case: a common word is taken as a short name ("Lake" for Lake City Casinos, "Bank" for Royal Bank of Canada v. Radius
Credit Union, "Nation" for Standingready v. Ocean Man First Nation, lowercase "connection", a footnote note "actuellement
disponible seulement en anglais"), and 11% of rows are name-only lines (title-block party names like "JUNIOR HERMAN v. THE",
footnote artifacts like "Hall v. Hill[3"). The refinement now rejects, in `C5_validate` (note `weak_short_form`): a short form
whose alias is lowercase, a generic word, or not whole words of the anchored case's party names, and name-only rows that are a
title-block party line or a footnote artifact. Short forms the decision defines itself ("[Vavilov]") and back-reference rows are
never rejected. On 500 random English FC/FCA decisions this removed about 17% of pass-one short forms; the removed ones read as
junk, with a few real ones lost (for example "O'Leary" written as "Leary", or "Teva Ramipril").

## Defined names and pinpoint-first forms (step `C4c_defined_names`)

Test case: 2026 FC 738 (id 35113). The live extractor missed the short forms "B010" (a trilogy list, "Suresh, Febles, B010") and "CCR" ("Mason and CCR", defined as "[CCR]"), and the pinpoint in "As stated at paragraph 34 of Lozano" (the pinpoint comes before the case name). The refinement already recovered the "at paras 13-14" pinpoint on a parallel cite and a few cites the live run missed. The new step adds bare mentions of a name the decision defines ("[CCR]") or an identifier-like first party ("B010"), and attaches pinpoint-first forms ("paragraph 34 of Lozano", "au paragraphe 34 de Lozano") to the case. On 40 random FC/FCA decisions it added 65 rows; the contexts read by hand were all genuine references (a defined alias mentioned again). "Refugees" (from the department name "Immigration, Refugees and Citizenship Canada") is now rejected as a generic word. Not covered yet: "Khadr 2010 at para 14" (name and year, no neutral cite).

## Linking refined rows and the `CITATIONS_SOURCE` switch

`scripts/link_refined_citations.py` resolves refined rows (neutral, full case, short form) to library cases by the same lookup keys the refinement writes (`identifier_keys` on both sides; French court codes map to English). A key shared by two cases never links; self-citations and name-only rows never link. Dry run by default (counts by kind plus `--examples N`); `--apply` writes `target_case_id` on `citations_refined` only and marks unmatched formal citations unresolved; `--revert --yes` clears the links. The live `citations` table is never touched.

`CITATIONS_SOURCE` (default `legacy`, no change) can be set to `refined`: `/cases/{id}/citations/outgoing` and `/incoming` then read refined rows for decisions with a finished refinement status and fall back to the live rows for every other decision. Not yet switched: citation passages (refined rows carry offsets into the full text, not chunk offsets), paragraph links, cited-by counts and citation metrics, and the reader.

## Noise rules after the stage-1 redo (2026-10-07)

On the 300 redo rows, about 35 of 67 pass-one short forms were a litigant or person named in the decision, not a citation ("Ms. Kostic wrote", "Apotex filed"). New rules in the refinement (not the live extractor): a bare pass-one short form with no pinpoint and no declared alias is dropped when it follows an honorific (Mr., Ms., Dr., Mme, M.) or is followed by a possessive or a litigant verb (argued, submits, alleges, filed, wrote, initiated, testified, signed). On the 47 source decisions of those rows this dropped 11 of 67; 10 read as litigant mentions and 1 ("Martin does not overrule") was a real reference, so "does not" was removed from the verb list. Also: a pass-one neutral row with no year or reporter number is a phrase and is dropped ("Arbour J. stated in Biniaris, at para. 37"), and "Ibid." that follows a bare note number ("14 Ibid.") links to the previous citation only when it is in the note right before (150 characters). The remaining litigant mentions (subject-position names without a verb cue, such as "Tervita", "the Institution") are not caught yet.
