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

## Missed pinpoints (2012 FC 319 paragraph 44, 2026-10-07)

Paragraph 44 cites Lubana (`2003 FCT 116, 2003 FCJ No 162 at para 12`) and Santos (`2004 FC 937, [2004] FCJ No 1149 at para 15`). Neither the live table nor refine v1 kept the pinpoints. Causes and fixes in `backend/citation_refine/cases.py`:

- **Quicklaw numbers without periods or brackets.** `[2004] FCJ No 1149` and `2003 FCJ No 162` were never read as parallel citations (the pattern demanded a literal full stop). They now join the chain, so the pinpoint after them is kept.
- **Carswell numbers** (`2007 CarswellNat 950 at para 42`) are now parallel citations too.
- **Pinpoint after a clause** (`, where she said at para 134:`, `, Justice Mosley noted at para 43`, `, the Court stated at p. 358`) is attached to the citation just before it. The row text still ends at the citation.
- **Name and year** (`Singh 2020 at para 26`) resolves to the case declared as `[Singh 2020]` or the one with that year.

Measured on 140 FC/FCA decisions (spread over 2002 to 2026; sample of live full text, refine run locally): rows with a pinpoint 913 to 990. Of the places where a pinpoint phrase follows a citation in the same clause, 13 of 114 were kept before and 32 of 62 after (the rest are mostly "At paragraph 5 of that decision" and "above" forms that name no citation). On 2012 FC 319 the rows with a pinpoint went from 14 of 54 to 27 of 50.

## Audit of what v2 misses, by type (2026-10-11)

Sample: 372 FC, FCA and SCC decisions from 2005 on (live full text, refine run locally, no database writes). Each type has an independent regex detector; a hit counts as covered when a refined row overlaps it. Old code is `origin/main` before this change.

| Type | Detector hits missed, before | After |
|---|---|---|
| Neutral citations (2020 FC 350, [2006] FCA 425) | 46 | 2 |
| Reporters (SCR, FCR, W.W.R., O.A.C., C.C.E.L. and others) | 395 | 32 |
| Quicklaw, Carswell, CIRB | 21 | 1 |
| Rows with a pinpoint | 4,284 | 4,530 |
| Pass-one short forms (noise removed, not lost) | 4,966 | 4,168 |

Statute and regulation references are 95.5% covered; the rest are "the Act" never defined (statute-layer work, not built here).

Fixes (all in `backend/citation_refine/`, deterministic):
- A cite that shares a year-less key with the decision itself was wrongly dropped as a self-citation; it now counts only when no differing year-bearing key is present.
- Joined cites ("A, [1983] 2 SCR 60; R. v. McClure, 2001 SCC 14") are split; a cite that starts mid-sentence is no longer merged with the narrative words before it.
- Bracketed neutral forms ("[2006] FCA 425"), reporters without a volume, more reporters and tribunals.
- Name-and-year, name-straight-before-pinpoint and "supra / cited above / précitée / ci-dessus" forms resolve to the case; bracketed aliases may contain digits ("[Singh 2020]").
- Noise rules: a short form that is a party of the decision's own title, a person named with a given name ("Dr. Gillian Frank", "Bryan A. Garner"), and place words (river, lake, township) are no longer cases.

Hand-checked precision on random rows: case and neutral rows about 98 to 100%; short forms with a pinpoint about 100%; short forms without a pinpoint 77 to 85% before the noise rules above (not re-measured after). Still missed: litigant or firm names in subject position with no cue, "Name, above" with no earlier anchor, "At paragraph 5 of that decision". Rows stored by the earlier 6,000-decision test rebuild do not have these fixes until a rebuild.

## "Of that decision" pinpoints and unanchored "Name, above" (2026-10-11)

Same 372-decision sample as the audit above (FC, FCA, SCC from 2005 on, local run, no database writes). Two new rules in step `C2_backrefs`:

- **"At paragraph 43 of that decision"** (also "of the same case", "of this judgment", "au paragraphe 5 de cette décision") becomes a short form with that pinpoint, anchored to the case cited just before (at most 600 characters back). "The decision" alone is not used: it usually means the decision under review. Only 4 genuine cases in the sample, all read by hand and correct.
- **"Plavix, cited above, at para 67"** when the decision never gives the full citation: kept as a name-only short form with its pinpoint, flagged `unanchored` (confidence 0.6, nothing to link). Statute and rule names ("Official Languages Act, supra"), one-word sentence starters ("The above") and names ending in Court, Board or Decision are left out.

Measured: "name + above/supra" mentions not covered by any row 65 of 359 to 5 (the 5 are correct exclusions: a statute, a "JUDGMENT For the Reasons above", "the Supreme Court cited above"). 64 unanchored rows in the sample; on 45 read by hand 43 were real references and the 2 wrong ones ("The above", "the Supreme Court cited above") are now excluded. Rows with a pinpoint 4,530 to 4,599.

Not built: litigant, person and firm names in subject position with no cue word. Any rule loose enough to catch them also catches real cases, so they stay out until there is a way to tell them apart.

## More short forms: "Name, at para N" and "Name, above" variants (2026-10-12)

Sample: 372 FC, FCA and SCC decisions from 2005 on, drawn at random from the open A2AJ dataset (124 per court, seed 11), refine run locally, no database writes. Neutral and reporter citations are already saturated here (7 uncovered hits left across 12,500 detector hits, and the decision's own header citation is correctly dropped), so this round targets short forms. Code is `backend/citation_refine/cases.py`.

What was being lost:
- Pass one reads "Kirkbi, at para. 43" and ", above, at para 16" as reporter-only fragments; validation then drops them, and the rules that should have kept the short form were blocked by the fragment sitting on the same words. Those fragments are now replaced by the better row.
- "Name, above" variants: a court in brackets ("Slattery (T.D.), above"), parentheses ("Apotex (cited above)", "Friends of the West Country Assn. (above)"), names with "Inc." or lowercase connectors ("Haskett v Equifax Canada Inc., above").
- A neutral cite that defines its own short name ("2000 SCC 31 [Firearms Reference]") now anchors later "Firearms Reference, above".
- Courts shorten a long first party to its first two words ("Husky Oil", "Deans Knight", "Mikisew Cree"); that is now a usable short name for "Name, at para N".

Not added on purpose: names that are an affidavit, factum, record, report, code or "principles" ("Poliquin Affidavit, above"), names that start right after an apostrophe or hyphen, and the bare litigant or firm names with no cue word.

Measured (uncovered mentions, detector-based):

| | Before | After |
|---|---|---|
| "Name, above / supra" mentions of cases not covered by a row (346 hits) | 26 | 12 |
| "Name, at para N" where Name is a case cited in that decision (2,149 hits) | 453 | 161 |
| Refined rows in the sample | 21,064 | 21,342 |

388 rows are new (326 name-pinpoint, 60 above/supra, 2 pinpoint-first). Hand check of the new rows against the surrounding text: 90 of 90 sampled "Name, at para N" rows are genuine references to a cited case, and 59 of the 60 "above / supra" rows are (the one exception is a text citation, "Lederman and Bryant, supra", a book rather than a case). A first pass produced 11 "X Affidavit, above" rows and two bad truncations ("l'Immigration (supra)"); both are now excluded and covered by tests. Remaining misses are mostly names that are too ambiguous to add without a cue (single common words, surnames of litigants).

## Short names taken from either party, and "(CLAO)" definitions (2026-10-12)

Same 372-decision sample as above, measured against the code after PR 496. "Name, at para N" where Name is part of a case cited in the decision and has no refined row: 161 of 2,149 before, 86 after. Refined rows 21,351 to 21,445 (116 new rows: 97 "Name, at para N", 17 bare mentions of a defined name, 2 other).

- **Short names from either party.** Courts shorten "Rio Tinto Alcan Inc. v. Carrier Sekani Tribal Council" to "Carrier Sekani", "Alberta v. Hutterian Brethren of Wilson Colony" to "Hutterian Brethren", "Ontario v. Criminal Lawyers’ Association of Ontario" to "Criminal Lawyers’ Association", "R. v. Paré" to "Paré", and "Prud’homme v. Prud’homme" to "Prud’homme". The leading capitalised words of each party (two, or three when the party has exactly three) and the surname of an "R. v. X" case now count as short names for "Name, at para N". Generic words (Court, Board, Attorney General and so on) never start a short name, and the existing weak-short-form check still applies.
- **Bare acronym definitions.** "(CLAO)" right after a citation now defines a short name like "[CLAO]" and "(“CLAO”)" already did. Court, reporter and database markers such as (SCC), (CanLII), (QL) are never treated as definitions.
- **Pass-one fragments.** A pass-one short form that is the first or last word of the same name (for example "homme" from "Prud’homme") is replaced instead of blocking the better row.

Hand check of the new rows (about 100 of the 116 read in context): all were genuine references to a cited case. One rule was tried and removed: stripping "Inc." and "Ltd." before the acronym test made a litigant of the decision itself ("AIC Limited") match every time its name appeared, so that stays as before.

What is left (86): names that are not part of any cited case name (an institution cited by a name the decision never gives), "Reference" and similar generic words, a few multi-case parentheticals, and abbreviations that were never defined, such as "CPR" for a railway. None has a safe rule on this sample.
