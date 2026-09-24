# Discussion Units: case 22183

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **1300**
- Continuity pairs: **1299**
- Discussion Units: **60**
- Paragraph source hashes: **1300**
- Sub-themes: **235**

## 22183:1 · paragraphs 0-19

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f86c42d637e452afdb7503c42fee6045d2b823b29e4a120bd1bf2a93893ec650`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `lilly, canada, canadian, collectively, company, patents, referred, apotex`
- Display key terms: `lilly, canadian, collectively, company, patents, referred, apotex`
- Argument roles: `governing_rule`
- Explanation: Observed roles: governing_rule Display terms: lilly, canadian, collectively, company, patents, referred, apotex Rule/authority context: [1] The plaintiffs in this action claim that their rights under eight Canadian patents were infringed when Apotex Inc. | [2] Lilly sold dosage forms of cefaclor in Canada under the registered name of Ceclor®. Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5040247` offsets `58-63`; context: [1] The plaintiffs in this action claim that their rights under eight Canadian patents were infringed when Apotex Inc.
- Evidence: `governing_rule` cue `under` at chunk `5040248` offsets `50-55`; context: [2] Lilly sold dosage forms of cefaclor in Canada under the registered name of Ceclor®.

#### 22183:1:subtheme:2 · paragraphs 5-6

- Raw key terms: `parties, action, although, apotex, application, canada, ceclor, cefaclor`
- Display key terms: `action, although, apotex, ceclor, cefaclor`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: action, although, apotex, ceclor, cefaclor Rule/authority context: [5] Although this action was instituted nearly twelve years ago, the dispute between the parties as to whether or not the sale by Apotex of a generic version of Ceclor® in Canada would infringe the patents at issue start Evidence spans paragraphs 5-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040251` offsets `103-110`; context: [5] Although this action was instituted nearly twelve years ago, the dispute between the parties as to whether or not the sale by Apotex of a generic version of Ceclor® in Canada would infringe the patents at issue started earlier, with the filing of an application under the Patented Medicines (Notice of Compliance) Regulations, SOR/93-133 (PM (NOC) Regulations) by Lilly and Shionogi on June 23, 1993.
- Evidence: `governing_rule` cue `under` at chunk `5040251` offsets `266-271`; context: [5] Although this action was instituted nearly twelve years ago, the dispute between the parties as to whether or not the sale by Apotex of a generic version of Ceclor® in Canada would infringe the patents at issue started earlier, with the filing of an application under the Patented Medicines (Notice of Compliance) Regulations, SOR/93-133 (PM (NOC) Regulations) by Lilly and Shionogi on June 23, 1993.
- Evidence: `issue` cue `issues` at chunk `5040252` offsets `251-257`; context: [6] Despite the fact that for the most part of this period, the parties have been intensively litigating the matter, neither the discovery process nor any other steps taken in this long period of time succeeded in significantly reducing the number of issues involved or to focus the debate at trial.

#### 22183:1:subtheme:3 · paragraphs 7-19

- Raw key terms: `evidence, cefaclor, lilly, apotex, court, patent, action, canada`
- Display key terms: `cefaclor, lilly, apotex, patent, action`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: cefaclor, lilly, apotex, patent, action Rule/authority context: This entails that they filed nearly one thousand pages of submissions (including those filed with respect to the counterclaim), not counting the various submissions filed in respect of a number of objections which had to | Common General Knowledge (Principles) 95 4. Evidence spans paragraphs 7-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040253` offsets `52-58`; context: [7] Given the amount of evidence filed and the many issues involved, the parties’ counsel made a real effort in attempting to consign all their arguments in writing.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040253` offsets `24-32`; context: [7] Given the amount of evidence filed and the many issues involved, the parties’ counsel made a real effort in attempting to consign all their arguments in writing.
- Evidence: `governing_rule` cue `under` at chunk `5040253` offsets `396-401`; context: This entails that they filed nearly one thousand pages of submissions (including those filed with respect to the counterclaim), not counting the various submissions filed in respect of a number of objections which had to be taken under reserve to avoid delaying the trial.
- Evidence: `issue` cue `issues` at chunk `5040254` offsets `228-234`; context: This is only partially reflected in these reasons which are, unfortunately, too long despite the fact that the Court could not really do justice to all the issues raised.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040254` offsets `308-316`; context: It was simply not possible or even desirable to refer to all the evidence and the hundreds of cases put forth by the parties.
- Evidence: `evidence_fact` cue `Evidence` at chunk `5040255` offsets `406-414`; context: The Evidence 16
3.
- Evidence: `governing_rule` cue `Principles` at chunk `5040255` offsets `547-557`; context: Common General Knowledge (Principles) 95
4.
- Evidence: `counterargument_limitation` cue `But` at chunk `5040255` offsets `3380-3383`; context: Apotex’s “But For” Scenarios with Respect to Causation 793
12.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040258` offsets `131-138`; context: It remained so for several years, however, by 1997, when Apotex came to market, it was definitely in decline, having been overtaken by other antibiotics.
- Evidence: `evidence_fact` cue `Evidence` at chunk `5040261` offsets `386-394`; context: The Evidence
- Evidence: `evidence_fact` cue `evidence` at chunk `5040262` offsets `30-38`; context: [16] An important part of the evidence in this trial is a long list of facts agreed to by the parties that are applicable both to the main action and the counterclaim.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040264` offsets `266-275`; context: Her testimony mainly served the purpose of entering into evidence, as well as offering a brief explanation of, documents filed in relation to Apotex’s submission for its Apo-cefaclor product.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040265` offsets `77-85`; context: [19] Various important exhibits discussed throughout the trial were put into evidence in the course of Dr.

#### Section text

Eli Lilly and Company v. Apotex inc.
Court (s) Database
Federal Court Decisions
Date
2009-10-01
Neutral citation
2009 FC 991
File numbers
T-1321-97
Decision Content
Date: 20091001
Docket: T-1321-97
Citation: 2009 FC 991
Ottawa, Ontario, October 1, 2009
PRESENT: The Honourable Justice Johanne Gauthier
BETWEEN:
ELI LILLY AND COMPANY
and ELI LILLY CANADA INC.
Plaintiffs
and
APOTEX INC.
Defendant
AND BETWEEN:
APOTEX INC.
Plaintiff by Counterclaim
(Defendant)
- and -
ELI LILLY AND COMPANY
and ELI LILLY CANADA INC.
Defendants by Counterclaim
(Plaintiffs)
and
SHIONOGI & CO. LTD.
Defendant by Counterclaim
REASONS FOR JUDGMENT AND JUDGMENT

[1] The plaintiffs in this action claim that their rights under eight Canadian patents were infringed when Apotex Inc. (Apotex) imported bulk cefaclor into Canada for use in the various Apo-cefaclor dosage forms they sold after January, 1997. The plaintiff Eli Lilly and Company (Lilly U.S.) is the owner of these eight patents. Eli Lilly Canada Inc. (Lilly Canada) is a wholly owned subsidiary of Lilly U.S. incorporated under the laws of Ontario and it alleges that it has rights under the patentee, which is contested by Apotex. These plaintiffs will collectively be referred to as “Lilly”.

[2] Lilly sold dosage forms of cefaclor in Canada under the registered name of Ceclor®. This medicine was put on the market in 1980.[1]

[3] The following four patents, all filed on February 1, 1979, were issued to, and were continuously owned by, Lilly U.S. (the Lilly patents):
a. Canadian Letters Patent No. 1,133,007 (“the ‘007 Patent”), issued October 5, 1982, expired October 5, 1999;
b. Canadian Letters Patent No. 1,146,536 (“the ‘536 Patent”), issued May 17, 1983, expired May 17, 2000;
c. Canadian Letters Patent No. 1,133,468 (“the ‘468 Patent”), issued October 12, 1982, expired October 12, 1999; and,
d. Canadian Letters Patent No. 1,150,725 (“the ‘725 Patent”), issued July 26, 1983, expired July 26, 2000.[2]
The patents referred to in paras. b, c and d will collectively be referred to as “the Lilly process patents”.

[4] The other four relevant patents were issued to Shionogi & Co. Ltd., a Japanese pharmaceutical company, (Shionogi) on the dates indicated below:
a. Canadian Letters Patent No. 1,095,026 (“the ‘026 Patent”), issued February 3, 1981, expired February 3, 1998;
b. Canadian Letters Patent No. 1,132,547 (“the ‘547 Patent”), issued September 28, 1982, expired September 28, 1999;
c. Canadian Letters Patent No. 1,136,132 (“the ‘132 Patent”), issued November 23, 1982, expired November 23, 1999; and,
d. Canadian Letters Patent No. 1,144,924 (“the ‘924 Patent”), issued April 19, 1983, expired April 19, 2000.[3]
While all have the same filing date of February, 1976 (when the original application was filed in Canada), three of these patents resulted from the filing of divisional applications, which will be further discussed below. These patents will be collectively referred to as the “Shionogi patents”. Lilly U.S. became the owner of the Shionogi patents by way of assignment dated April 27, 1995 which was registered in Canada on August 24, 1995.

[5] Although this action was instituted nearly twelve years ago, the dispute between the parties as to whether or not the sale by Apotex of a generic version of Ceclor® in Canada would infringe the patents at issue started earlier, with the filing of an application under the Patented Medicines (Notice of Compliance) Regulations, SOR/93-133 (PM (NOC) Regulations) by Lilly and Shionogi on June 23, 1993.[4] Earlier, the issue had also been raised when Apotex sought a compulsory licence with respect to cefaclor and certain Lilly patents related thereto in 1986.

[6] Despite the fact that for the most part of this period, the parties have been intensively litigating the matter, neither the discovery process nor any other steps taken in this long period of time succeeded in significantly reducing the number of issues involved or to focus the debate at trial.

[7] Given the amount of evidence filed and the many issues involved, the parties’ counsel made a real effort in attempting to consign all their arguments in writing. This entails that they filed nearly one thousand pages of submissions (including those filed with respect to the counterclaim), not counting the various submissions filed in respect of a number of objections which had to be taken under reserve to avoid delaying the trial. The Court thanks each counsel involved for their effort in reducing the number of those objections that remained outstanding in the end.

[8] Despite all this goodwill, the Court was left with a daunting task. This is only partially reflected in these reasons which are, unfortunately, too long despite the fact that the Court could not really do justice to all the issues raised. It was simply not possible or even desirable to refer to all the evidence and the hundreds of cases put forth by the parties.[5]

[9] At the end of the process, one must wonder where the system failed for the Court is convinced that there has to be a better way to achieve the objectives set out in section 3 of the Federal Court Rules, SOR/98-106 (the Rules), which seeks to achieve the just, most expeditious and least expensive determination of every proceeding on its merits.
INDEX
Heading Para. No.
1. General Background 10
2. The Evidence 16
3. Lilly Canada’s Lack of Standing 75
4. Patent Construction 87
4.1. Person Skilled in the Art 91
4.2. Common General Knowledge (Principles) 95
4.3. The ‘007 Patent 106
4.4. The Lilly Process Patents 144
4.4.1. The ‘536 Patent 145
4.4.2. The ‘725 Patent 164
4.4.3. The ‘468 Patent 170
4.5. The Shionogi Patents 175
4.5.1. Common Disclosure 177
4.5.2. The ‘547 Patent 184
4.5.3. The ‘924 Patent 188
4.5.4. The ‘132 Patent 192
4.5.5. The ‘026 Patent 199
5. Infringement
5.1. Burden 211
5.2. Statutory and Common Law Presumptions 212
5.3. Lupin Process 224
5.4. Kyong Bo Process 257
5.4.1. Existence of a License 263
5.5. Importation 270
5.6. The Exception Under Subsection 55.2(1) of the Patent Act 342
6. Invalidity 347
6.1. Standard of Review and Burden of Proof 348
7. Inherency and Lack of Subject Matter
7.1. Shionogi Patents 371
7.2. Lilly Patents 380
8. Anticipation
8.1. The Legal Test 391
8.2. The ‘007 Patent 399
8.3. The Lilly Process Patents 409
8.4. The Shionogi Patents 411
9. Obviousness
9.1. The Legal Test 412
9.2. The ‘007 Patent (Claim 17) 426
9.2.1. The Person Skilled in the Art 428
9.2.2. Relevant Common General Knowledge 429
9.2.3. Rydon, Coe and Ramirez 432
9.2.4. The Inventive Concept 438
9.2.5. The Difference Between the Common General Knowledge and
the Above-mentioned Publications and the Inventive Concept 439
9.2.6. Would these differences be obvious to the person skilled in
the art? 441
9.3. The Lilly Process Patents
9.3.1. Identify the Skilled Addressee 476
9.3.2. The Relevant Common General Knowledge 477
9.3.3. The Dreux Article and Other Prior Art 484
9.3.4. The Inventive Concept 489
9.3.5. The Differences between the Prior Art Including Common
General Knowledge and the Inventive Concept of the Claims 491
9.3.6. Do these differences constitute steps which would have been
obvious or do they require any degree of invention? 496
9.4. The Shionogi Patents 512
9.4.1. The Person Skilled in the Art 515
9.4.2. Common General Knowledge 516
9.4.3. Contested Art 532
9.4.3.1. Cocker 533
9.4.3.2. Chauvette Application 538
9.4.3.3. Kishi 539
9.4.4. The Inventive Concept 544
9.4.5. The Differences between the Prior Art and the Inventive
Concept
9.4.5.1. The ‘547 Patent 547
9.4.5.2. The ‘924 Patent 549
9.4.5.3. The ‘132 Patent 552
9.4.5.4. The ‘026 Patent 554
9.4.6. Are these differences inventive? 557
10. Lack of Utility – Sound Prediction – Inoperability 583
10.1. The Lilly Patents 585
10.2. The Shionogi Patents 604
10.3. Deficiency of Specification and Ambiguity 613
11. Remedies and Costs
11.1. Disentitlement and Set-off 626
11.2. Remedies 646
11.3. Exemplary/Punitive Damages 657
11.4. Interest 665
11.5. Costs 676
12. Apotex’s Counterclaim 683
12.1. Relevant Statutory Provisions 718
12.2. The Framework of Inquiry into Apotex’s Counterclaim 720
12.3. Is Apotex’s Counterclaim Time-Barred? 728
12.4. Apotex’s Claim for Damages 754
12.5. The Applicable Evidentiary Standard 757
12.6. Background 771
12.7. Apotex’s “But For” Scenarios with Respect to Causation 793
12.7.1. Scenarios 1 and 2: Apotex Obtains a Licence from
Shionogi or Lilly 803
12.7.2. Scenario 3: Apotex Practices the Shionogi Process and
is not sued 835
12.7.3. Scenarios 4 and 5: Apotex Practices the Shionogi and
Lilly Processes and is Sued by Shionogi and Lilly 840
12.8. Is there a loss resulting from the assignment under the most
likely “but for” world scenario? 842
12.9. Increased Cost of Legal Bulk Cefaclor 849
12.10. Infringement Liability 853
12.10.1. The Lilly Patents 855
12.10.2. The Shionogi Patents 861
12.11. Costs 882
1. General Background

[10] It is not disputed that penicillin is the oldest of the β-lactam compounds, having first been discovered in 1928. Semi-synthetic penicillin came later. The β-lactam molecule per se is a small square molecule that is highly reactive, to which, in penicillin, a five-membered ring is attached, whereas in cephalosporin (which includes cefaclor) the β-lactam is attached to a six-membered ring containing sulfur. There are different types of β-lactam depending on their side-chain, such as penicillin V (Pen V) and penicillin G (Pen G).

[11] Cephalosporins were first discovered in 1948. Semi-synthetic cephalosporins were prepared by altering the naturally produced compounds for greater anti-bacterial activity. Like penicillins, cephalosporins are bactericidal and exhibit similar modes of action. Cephalosporins are classified based on their generation. First generation cephalosporins, such as cephalexin (another Lilly product), have good activity against gram positive bacteria and more modest activity against gram negative. Second generation cephalosporins, such as cefaclor, have better activity against gram negative bacteria. Third generation cephalosporins, such as cephotaxim, ceftazidine and ceftriaxone, were less active than the first generation but have good activity against Enterobacteriaceae.

[12] Shortly after it was introduced in the market by Lilly, Ceclor® was a very successful drug. It remained so for several years, however, by 1997, when Apotex came to market, it was definitely in decline, having been overtaken by other antibiotics.

[13] The basic patent on the compound Cefaclor or the class of second generation cephalosporins to which it belongs (7-χ-aminoacyl-3-halo-3-cephem carboxylic acid or ester compound) is patent 1,016,537 (the ‘537 patent) filed on February 22, 1974 and issued in Canada on August 30, 1977. It expired August 30, 1994. It was also owned by Lilly U.S., having been discovered by Dr. Chauvette, a member of its β-lactam research team. Cefaclor was specifically disclosed in an example and the process to prepare it, or an obvious chemical equivalent, was claimed. Other claims dealt with other 7-χ-acylamino-3-chloro-3-cephem compounds prepared by those processes.

[14] It is not disputed that although the disclosure of the ‘007 patent directly refers to the preparation of a cephalosporin compound using the kinetically controlled complexes claimed in the patent, the claims do not expressly refer to such use. Also, none of the claims in the Lilly process patents or the Shionogi patents are directly claiming a process to make cefaclor itself. As a matter of fact, and as will be explained in more detail later on, these patents more generally relate to the making of what all experts agree was a key intermediate compound (the 3-hydroxy-3-cephem compound)[6] if one were to make cefaclor. The steps required to make cefaclor from this key intermediate were disclosed in the ‘537 patent.

[15] An important part of the debate relates to processes involved in the transformation of a penicillin molecule into a cephalosporin molecule. Penicillin molecules could be synthetically produced at very low cost whereas the original starting material used by Dr. Chauvette to make cefaclor or other second generation cephalosporins described in his patent was very expensive.
2. The Evidence

[16] An important part of the evidence in this trial is a long list of facts agreed to by the parties that are applicable both to the main action and the counterclaim. To avoid excessive duplication, the Court will attempt to avoid repeating those admitted facts which are relevant to both actions, with the understanding that the totality of said facts were considered in the course of the determination of both actions.

[17] In the infringement action Lilly produced six factual witnesses: Dr. Stephanie Parra, Mr. Thomas Lee Pytynia, Ms. Debbie Rassos, Dr. Larry Blaszczak, Dr. Robin Cooper and Mr. John Gardner.

[18] Dr. Parra is acting manager of the general direct quality division one at Health Canada. Her division is responsible for evaluating data submitted to support the quality of drug submissions made to the department including chemistry and manufacturing data. Her testimony mainly served the purpose of entering into evidence, as well as offering a brief explanation of, documents filed in relation to Apotex’s submission for its Apo-cefaclor product.[7] This included particularly the “open” and “closed” portions of the relevant Drug Master Files (DMFs) submitted by Apotex’s suppliers, Lupin Laboratories Ltd. of India (Lupin) and Kyong Bo Chemical Ltd. of South Korea (Kyong Bo).

[19] Various important exhibits discussed throughout the trial were put into evidence in the course of Dr. Parra’s testimony, such as the Comprehensive Summary regarding Apo-cefaclor (TX-124), the open and closed portions of Kyong Bo’s DMF (TX-126; TX-129), Apotex’s notifiable change for new source (TX-157) and letters from the Department of Justice to Gowlings Lafleur Henderson LLP with information provided by Lupin attached (TX-167; TX-168).

## 22183:2 · paragraphs 20-32

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `28d464ffa6329f9fd5b919730930a718ac25c2643bc7a75360ba91fcfbba9e93`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:2:subtheme:1 · paragraphs 20-22

- Raw key terms: `canada, information, introduced, lilly, regulatory, supplier, testified, various`
- Display key terms: `information, introduced, lilly, regulatory, supplier, testified, various`
- Argument roles: `evidence_fact`
- Explanation: Observed roles: evidence_fact Display terms: information, introduced, lilly, regulatory, supplier, testified, various Evidence spans paragraphs 20-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040268` offsets `327-335`; context: She introduced in evidence, among other things, Lilly Canada’s process information filed in relation to its New Drug Submission (NDS) (TX-208; TX-209) for Ceclor® as well as a portion of its 1979 NDS (TX-115).

#### 22183:2:subtheme:2 · paragraphs 23-30

- Raw key terms: `apotex, evidence, lilly, testimony, used, patent, process, referred`
- Display key terms: `apotex, lilly, testimony, used, patent, process, referred`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: apotex, lilly, testimony, used, patent, process, referred Rule/authority context: Her testimony was put forth in support of Apotex’s defence pursuant to s. Application context: However, I fail to see how Rule 248 can apply when it is the Court which determined that the requested documents were not relevant. Evidence spans paragraphs 23-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040269` offsets `642-647`; context: In the course of his testimony on this issue, Apotex formulated a number of objections to hearsay evidence.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040269` offsets `624-633`; context: In the course of his testimony on this issue, Apotex formulated a number of objections to hearsay evidence.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040269` offsets `119-126`; context: However, he did not testify in this capacity but rather to explain his relationship with a graduate student in chemistry from the University of Modena, Alberto Spaggiari.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040270` offsets `367-375`; context: Blaszczak offered evidence as to how Lilly structured its research operations with regard to cefaclor, particularly the de facto merging of the process research and development and discovery groups (he was part of the latter) when Lilly requested that the discovery chemists thoroughly consider the problem posed by the production of cefaclor on a commercial scale.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040271` offsets `424-433`; context: The content of his testimony will be discussed in more detail when assessing the allegations of invalidity of the Shionogi patents.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040272` offsets `359-367`; context: Although Lilly produced a copy of his thirty-year-old lab notebook (TX-1799), Apotex objected to this evidence being used to counter the arguments of Apotex’s experts with regard to invalidity.
- Evidence: `reasoning_application` cue `apply` at chunk `5040272` offsets `705-710`; context: However, I fail to see how Rule 248 can apply when it is the Court which determined that the requested documents were not relevant.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040272` offsets `257-265`; context: Although Lilly produced a copy of his thirty-year-old lab notebook (TX-1799), Apotex objected to this evidence being used to counter the arguments of Apotex’s experts with regard to invalidity.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040273` offsets `122-130`; context: Cooper, I accepted as credible the evidence of these witnesses.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040275` offsets `232-241`; context: Her testimony was put forth in support of Apotex’s defence pursuant to s.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040275` offsets `287-298`; context: Her testimony was put forth in support of Apotex’s defence pursuant to s.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040276` offsets `95-104`; context: He provided testimony on product development at Apotex.

#### 22183:2:subtheme:3 · paragraphs 31-32

- Raw key terms: `apotex, cefaclor, commercial, defence, patent, quantities, relevant, testimony`
- Display key terms: `apotex, cefaclor, commercial, defence, patent, quantities, relevant, testimony`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: apotex, cefaclor, commercial, defence, patent, quantities, relevant, testimony Rule/authority context: Again, this testimony was offered in support of Apotex’s defence pursuant to s. Evidence spans paragraphs 31-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040277` offsets `666-672`; context: On cross-examination, Lilly’s counsel focused on the accuracy of records which are not relevant to the issues the Court must decide today, given that if infringement is established, the damages will be assessed by reference.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040277` offsets `471-480`; context: Again, this testimony was offered in support of Apotex’s defence pursuant to s.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040277` offsets `524-535`; context: Again, this testimony was offered in support of Apotex’s defence pursuant to s.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040278` offsets `432-441`; context: Fahner’s testimony was to introduce in evidence, and explain the significance of, spreadsheets (TX-1559; TX-1560; TX-1561) he prepared representing compilations of quantities of cefaclor which Apotex claims is covered by the defence provided for at s.

#### Section text

[20] Dr. Parra also explained the meaning of a “notifiable change” and the various levels ascribed thereto, which correspond to greater or lesser regulatory filing requirements. A change of supplier for example is classified as a level 2 notifiable change and will receive an objection letter if Health Canada has an objection to the proposed change.[8] In this matter, before approving the change of supplier notified by Apotex (from Kyong Bo to Lupin), Health Canada requested additional information by way of a document called a “Clarifax” (TX-152) to which Apotex replied by a letter dated June 21, 1997 with an attachment explaining the source of the starting material and a full diagram representing the synthetic route used to make 7-amino-3-chloro-3-cephem-4-carboxylic acid esters (7-ACCA) (TX-150).

[21] Mr. Pytynia was in-house counsel for Lilly U.S. between May 1977 and December 31, 2007. He testified mainly about the relationship between Lilly U.S. and Lilly Canada, including particularly their licensing and distribution agreements. He introduced various documents which will be referred to later on, such as the 1991 licensing agreement between Lilly U.S. and Lilly Canada (TX-109), the 1995 patent and trademark licence amendment (TX-110), the Master Supply and Distribution Agreement between the said two companies (TX-112) as well as the Authorization to grant sub-licences from Lilly U.S. to Lilly Canada (TX-113).

[22] Ms. Rassos is the senior regulatory affairs manager at Lilly Canada, a position she has held for two and a half years. She had no direct knowledge of any of the events relevant to the proceedings and testified only to the documentation she found in Lilly Canada’s regulatory records concerning cefaclor. She introduced in evidence, among other things, Lilly Canada’s process information filed in relation to its New Drug Submission (NDS) (TX-208; TX-209) for Ceclor® as well as a portion of its 1979 NDS (TX-115). It was made clear during her cross-examination that her testimony with respect to the identity of Lilly Canada’s supplier during the 1979 and 2000 period is solely based on the said documentation for she had no independent knowledge of such matters.[9]

[23] Dr. Blaszczak is one of the inventors listed in the Lilly patents in suit, with the exception of the ‘536 patent. However, he did not testify in this capacity but rather to explain his relationship with a graduate student in chemistry from the University of Modena, Alberto Spaggiari. This student had solicited Dr. Blaszczak’s supervision in conducting research in β-lactam chemistry with the view of preparing dual action cephalosporins. This led to Dr. Blaszczak collaborating with Mr. Spaggiari as a co-author for a scientific article referred to here as the Spaggiari paper published in 2004. In the course of his testimony on this issue, Apotex formulated a number of objections to hearsay evidence. While the objections were largely justified in this regard, none of this evidence is relevant to the issues upon which this judgment turns.

[24] On cross-examination, Dr. Blaszczak was referred to a 1978 cefaclor progress report (TX-211) and questioned as to his role in relation with it. He was also probed as to the process used by Lilly in the late 1970’s, particularly the transition to triphenyl phosphite (TPP) chloride (Cl) complex and the comparative yields achieved. Finally, Dr. Blaszczak offered evidence as to how Lilly structured its research operations with regard to cefaclor, particularly the de facto merging of the process research and development and discovery groups (he was part of the latter) when Lilly requested that the discovery chemists thoroughly consider the problem posed by the production of cefaclor on a commercial scale.

[25] Dr. Cooper was working with Lilly’s research team at the relevant time. He was already a world-renowned expert in cephalosporin chemistry. He was presented as a factual witness to relate any attempts he made back in the early 1970’s to cyclicize the thiazoline azetidinone compound he discovered (Cooper compound), which is used as starting material in the process described in the Shionogi patents. The content of his testimony will be discussed in more detail when assessing the allegations of invalidity of the Shionogi patents.

[26] Mr. Gardner is a chemist who performed the experiment described in example nine of the ‘007 patent (characterised as a side chain cleavage using the tri-p-chloro phenyl phosphite chlorine complex) while at Lilly in the late summer, early fall of 1978. Although Lilly produced a copy of his thirty-year-old lab notebook (TX-1799), Apotex objected to this evidence being used to counter the arguments of Apotex’s experts with regard to invalidity. Mainly, Apotex argues that Rule 248 of the Federal Courts Rules precludes this evidence from being introduced as Apotex sought to obtain all these lab notebooks during the discovery and its requests went unheeded. However, I fail to see how Rule 248 can apply when it is the Court which determined that the requested documents were not relevant.[10] That said, in order to avoid further peripheral debates, the Court does not consider this evidence to be necessary to reach its findings.

[27] Subject to what I said about Ms. Rassos and my further comments in respect of Dr. Cooper, I accepted as credible the evidence of these witnesses.

[28] Apotex presented eight fact witnesses in the main action: Ms. Julie Carrière, Mr. Donald Barber, Mr. Gordon Fahner, Dr. Bernard Sherman, Mr. John Hems, Mr. Rajeev Patil, Mr. Vilas Satpute and Mr. Haracharan (Harry) Singh.

[29] Ms. Carrière is Apotex’s director of quality assurance and she testified about the regulatory context which requires Apotex to conduct tests and analyses of the bulk chemicals it uses in making pharmaceutical formulations. Her testimony was put forth in support of Apotex’s defence pursuant to s. 55.2 of the Patent Act, R.S.C. 1985, c. P-4. In cross-examination, she explained that the related compounds which must be tested referred to the synthetic or degradation impurities which have been previously identified in the New Drug Submission or Notifiable Change. She also agreed that these related compounds may change from supplier to supplier, depending upon the processes used, which may create a need for different analytical techniques.[11] Finally, Ms. Carrière agreed that apart from the regulatory obligation, testing is beneficial to Apotex for it must ensure that the products it puts on the market are safe and of good quality, otherwise its sales might suffer.

[30] Mr. Barber has been the formulation development manager at Apotex since 1998. He provided testimony on product development at Apotex. He explained in detail the various testing required to develop a commercially viable product, which includes the formulation stages, the scaling up of a process or formulation that is thought to be workable on an industrial scale and the testing or evaluation of the formulation so produced. The raw material testing is ongoing throughout the process.

[31] He noted that whenever Apotex switches to a different supplier for an active pharmaceutical ingredient (API), evaluations, both chemical and physical, are repeated and a “good amount” of the formulation development work must also be repeated. Mr. Barber discussed how, with regard to cefaclor, such work started as early as 1991. He identified several exhibits relating to quantities of cefaclor which have not been sold or used for commercial purposes. Again, this testimony was offered in support of Apotex’s defence pursuant to s. 55.2 of the Patent Act. On cross-examination, Lilly’s counsel focused on the accuracy of records which are not relevant to the issues the Court must decide today, given that if infringement is established, the damages will be assessed by reference. The accuracy of Apotex’s records in this regard can be contested at the reference stage, in accordance with the Court’s reasons below on the proper scope of the exemption.

[32] Mr. Fahner has been Apotex’s Vice-President of Finance since 2003, having held the position of Director of Finance at the relevant period. He testified twice in the course of the main action. Firstly, Mr. Fahner testified as to the inventory tracking system at Apotex and the gradual evolution of this system from a paper-based system to an electronic SAP system in the 1999 to 2001 timeframe. The main purpose of Mr. Fahner’s testimony was to introduce in evidence, and explain the significance of, spreadsheets (TX-1559; TX-1560; TX-1561) he prepared representing compilations of quantities of cefaclor which Apotex claims is covered by the defence provided for at s. 55.2 of the Patent Act. Also, Mr. Fahner explained the significance of another spreadsheet he prepared (TX-1759) which represents a summary of raw cefaclor quantities purchased by Apotex primarily for commercial use as well as prices paid for said cefaclor.

## 22183:3 · paragraphs 33-67

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `dd1b2158286fbeabc33363f1d965439b3d3ab4e5933e0512ad715fa0b809ef08`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:3:subtheme:1 · paragraphs 33-35

- Raw key terms: `apotex, cefaclor, cross-examination, fahner, order, quantities, relevant, testified`
- Display key terms: `apotex, cefaclor, cross-examination, fahner, order, quantities, relevant, testified`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: apotex, cefaclor, cross-examination, fahner, order, quantities, relevant, testified Evidence spans paragraphs 33-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040279` offsets `649-655`; context: Inconsistencies were also identified with regards to the summary of raw cefaclor quantities (TX-1759) and various purchase orders, which again, in a context where a reference will take place, are not germane to the issues presently at hand.
- Evidence: `issue` cue `question` at chunk `5040280` offsets `217-225`; context: (contained in Glopec-36) which called into question Mr.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040280` offsets `19-28`; context: [34] Following the testimony of Mr.

#### 22183:3:subtheme:2 · paragraphs 36-40

- Raw key terms: `sherman, apotex, cefaclor, correspondence, fouillade, process, regard, agreement`
- Display key terms: `sherman, apotex, cefaclor, correspondence, fouillade, process, regard, agreement`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: sherman, apotex, cefaclor, correspondence, fouillade, process, regard, agreement Evidence spans paragraphs 36-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040282` offsets `20-25`; context: [36] Except for the issue relating to the Tektrade invoices in respect of which the Court will make no finding, the evidence of the aforementioned witnesses was accepted.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040282` offsets `116-124`; context: [36] Except for the issue relating to the Tektrade invoices in respect of which the Court will make no finding, the evidence of the aforementioned witnesses was accepted.
- Evidence: `issue` cue `issues` at chunk `5040283` offsets `421-427`; context: Sherman as to intellectual property issues.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040285` offsets `327-336`; context: He was also questioned as to why the agreement with Lupin (TX-1656) was not in the original affidavit of documents he signed (TX-327) and why no Notifiable Change had been filed by Apotex for this new process.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040286` offsets `79-88`; context: Sherman’s testimony in respect of matters where he was directly involved as opposed to those where others were directly involved such as Ms.

#### 22183:3:subtheme:3 · paragraphs 41-50

- Raw key terms: `lupin, process, testified, cefaclor, apotex, canada, documents, glopec`
- Display key terms: `lupin, process, testified, cefaclor, apotex, documents, glopec`
- Argument roles: `evidence_fact, governing_rule`
- Explanation: Observed roles: evidence_fact, governing_rule Display terms: lupin, process, testified, cefaclor, apotex, documents, glopec Rule/authority context: Satpute were heard under reserve of general objections (generally referred to as voir dire by the parties) which will be discussed in the section regarding infringement. | This filing was made under reserve of an objection that the documents therein are not proof of their contents but rather only of the existence of such communications with the U. Evidence spans paragraphs 41-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5040287` offsets `72-77`; context: Satpute were heard under reserve of general objections (generally referred to as voir dire by the parties) which will be discussed in the section regarding infringement.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040288` offsets `468-477`; context: With regard to cefaclor, a certain amount of such correspondence related thereto was introduced in the course of his testimony (Glopec 1-14; 28-33).
- Evidence: `evidence_fact` cue `testimony` at chunk `5040291` offsets `275-284`; context: Patil’s handwriting in the margins and which prompted testimony about the interaction Mr.
- Evidence: `evidence_fact` cue `found that` at chunk `5040293` offsets `903-913`; context: Also when he was asked to find batch records for the 7-ACCA so produced, for which the plant manager and the R&D department would have created a template a few weeks before coming to Canada, he found that these documents no longer existed.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040295` offsets `46-55`; context: [49] Finally, the parties filed by consent an affidavit of Leslie Sands, Director of regulatory affairs at Lupin Pharmaceuticals Inc.
- Evidence: `governing_rule` cue `under` at chunk `5040295` offsets `219-224`; context: This filing was made under reserve of an objection that the documents therein are not proof of their contents but rather only of the existence of such communications with the U.

#### 22183:3:subtheme:4 · paragraphs 51-52

- Raw key terms: `apotex, experts, infringement, issue, lilly, patents, process, question`
- Display key terms: `apotex, experts, infringement, lilly, patents, process, question`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: apotex, experts, infringement, lilly, patents, process, question Evidence spans paragraphs 51-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040297` offsets `12-20`; context: [51] On the question of infringement of the Shionogi patents by the use of the Kyong Bo process, Lilly called Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040297` offsets `162-170`; context: Anthony Barrett while Apotex responded with the evidence of Dr.
- Evidence: `issue` cue `issue` at chunk `5040298` offsets `29-34`; context: [52] A much more contentious issue concerns the infringement of the Lilly patents, particularly whether the Lupin process described in the Health Canada file fell within the scope of the monopoly of the plaintiffs.

#### 22183:3:subtheme:5 · paragraphs 53-54

- Raw key terms: `abandon, adopted, alleged, always, amount, arguments, aspect, assessing`
- Display key terms: `abandon, adopted, alleged, always, amount, arguments, aspect, assessing`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: abandon, adopted, alleged, always, amount, arguments, aspect, assessing Evidence spans paragraphs 53-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040299` offsets `755-760`; context: The Court used considerable caution in assessing the weight to be given to this evidence, but in the end, considering the construction of the claims at issue adopted, most of these experiments and the comments relating thereto became somewhat irrelevant.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040299` offsets `683-691`; context: The Court used considerable caution in assessing the weight to be given to this evidence, but in the end, considering the construction of the claims at issue adopted, most of these experiments and the comments relating thereto became somewhat irrelevant.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040299` offsets `693-696`; context: The Court used considerable caution in assessing the weight to be given to this evidence, but in the end, considering the construction of the claims at issue adopted, most of these experiments and the comments relating thereto became somewhat irrelevant.

#### 22183:3:subtheme:6 · paragraphs 55-57

- Raw key terms: `evidence, barrett, hanessian, issues, lilly, patents, respect, shionogi`
- Display key terms: `barrett, hanessian, issues, lilly, patents, respect, shionogi`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue Display terms: barrett, hanessian, issues, lilly, patents, respect, shionogi Operative outcome context: [56] Also, with respect to the infringement of the Lilly process patents, the Court granted leave to both parties to file expert evidence on issues arising from the testimony of Mr. Evidence spans paragraphs 55-57. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040301` offsets `152-158`; context: In the end, these issues were settled without the need for a ruling.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040301` offsets `124-132`; context: [55] There was a lengthy debate about the admissibility of tests performed ex parte and how tests must be introduced in the evidence.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `5040301` offsets `203-215`; context: Nevertheless, it is important to note that pre-trial scheduling orders setting deadlines for the reporting of test results, absent an express indication to the contrary, must not be construed to constitute a waiver of any requirement that may exist regarding notice of testing to be performed pre-trial.
- Evidence: `issue` cue `issues` at chunk `5040302` offsets `141-147`; context: [56] Also, with respect to the infringement of the Lilly process patents, the Court granted leave to both parties to file expert evidence on issues arising from the testimony of Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040302` offsets `129-137`; context: [56] Also, with respect to the infringement of the Lilly process patents, the Court granted leave to both parties to file expert evidence on issues arising from the testimony of Mr.
- Evidence: `disposition` cue `granted` at chunk `5040302` offsets `84-91`; context: [56] Also, with respect to the infringement of the Lilly process patents, the Court granted leave to both parties to file expert evidence on issues arising from the testimony of Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040303` offsets `74-82`; context: [57] Turning now to the validity phase of the trial, Apotex relied on the evidence of Drs.

#### 22183:3:subtheme:7 · paragraphs 58-59

- Raw key terms: `baldwin, evidence, lilly, process, respect, addressed, admitted, allegations`
- Display key terms: `baldwin, lilly, process, respect, addressed, admitted, allegations`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: baldwin, lilly, process, respect, addressed, admitted, allegations Evidence spans paragraphs 58-59. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040304` offsets `157-163`; context: McClelland also addressed issues relating to all the Lilly process patents and Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040304` offsets `292-300`; context: In response, Lilly relied upon the evidence of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040305` offsets `74-82`; context: [59] In respect of infringement by the Lupin process, the Court found the evidence of Dr.

#### 22183:3:subtheme:8 · paragraphs 60-62

- Raw key terms: `court, expert, respect, apotex, evidence, experts, mcclelland, modro`
- Display key terms: `expert, respect, apotex, experts, mcclelland, modro`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: expert, respect, apotex, experts, mcclelland, modro Application context: McClelland because of his vast experience acting as an expert in patent cases he was somewhat less spontaneous than other Apotex experts. Evidence spans paragraphs 60-62. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040306` offsets `316-322`; context: Baldwin to be particularly well qualified to opine on the issues of fact covered in his report.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040307` offsets `215-223`; context: Generally the Court had no difficulties with their credibility although, the Court was more cautious with the evidence of Dr.
- Evidence: `reasoning_application` cue `because` at chunk `5040307` offsets `242-249`; context: McClelland because of his vast experience acting as an expert in patent cases he was somewhat less spontaneous than other Apotex experts.
- Evidence: `counterargument_limitation` cue `although` at chunk `5040307` offsets `168-176`; context: Generally the Court had no difficulties with their credibility although, the Court was more cautious with the evidence of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040308` offsets `587-595`; context: 68 to the effect that “expert evidence should be seen as the independent product of the expert uninfluenced as to form or content by the exigencies of litigation: Whitehouse v Jordan [1981] 1 WLR 246 at 256, per Lord Wilberforce” (emphasis added).

#### 22183:3:subtheme:9 · paragraphs 63-67

- Raw key terms: `evidence, respect, court, chemistry, credible, hunter, chivers, claims`
- Display key terms: `respect, chemistry, credible, hunter, chivers, claims`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: respect, chemistry, credible, hunter, chivers, claims Evidence spans paragraphs 63-67. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040309` offsets `354-359`; context: Hunter in respect of the testing performed and found his evidence credible in respect of the common general knowledge about 31P NMR and the impact of various factors on the ppm chemical shift at the relevant time, his evidence was not as useful considering the construction of the claims at issue adopted by the Court.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040309` offsets `47-55`; context: [63] Although the Court generally accepted the evidence of Dr.
- Evidence: `issue` cue `issue` at chunk `5040310` offsets `57-62`; context: [64] Again, in view of the construction of the claims at issue, most of the evidence of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040310` offsets `76-84`; context: [64] Again, in view of the construction of the claims at issue, most of the evidence of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040311` offsets `651-659`; context: His evidence, in respect of the ‘007 patent, like that of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040312` offsets `394-402`; context: [19] These two experts were equally credible which made the task of the Court particularly difficult considering that their evidence is often contradictory.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040313` offsets `74-82`; context: Olah, McClelland and Martin’s evidence in respect of the Lilly process patents and the Shionogi patents illustrate difficulties the Court faced in this case and which are unfortunately not uncommon.

#### Section text

[33] On cross-examination it became apparent that some of the material included in the spreadsheets was in fact material that had been acquired post-patent expiry and thus is not relevant for the purposes of this proceeding. On this basis, Apotex undertook to have Mr. Fahner revise said spreadsheets to ensure that they only include quantities relevant to the allegation of infringement. This was provided by Apotex on May 12, 2008. Inconsistencies were also identified with regards to the summary of raw cefaclor quantities (TX-1759) and various purchase orders, which again, in a context where a reference will take place, are not germane to the issues presently at hand. Finally, Mr. Fahner also identified a spreadsheet representing international sales of Apo-cefaclor (TX-1747) and confirmed that no sales had occurred in the United States.

[34] Following the testimony of Mr. Singh, which will be discussed below, Apotex re-called Mr. Fahner to testify with regard to certain invoices emanating from Tektrade Ltd. (contained in Glopec-36) which called into question Mr. Fahner’s earlier testimony. Mr. Fahner testified that the relevant invoices (# TTL-981006-02 and TTL-981006-3) were not in Apotex’s records, that the cefaclor quantities represented therein had not been received by Apotex and that no payment had been made to Tektrade Ltd. in relation thereto. Lilly objected to Mr. Fahner being called back to testify, but on June 17, 2008, the Court ruled that it would exercise its discretion and allow said testimony, noting that Lilly did not suffer any prejudice in light of the bifurcation order for the issue of the quantum of damages, save perhaps in losing what was indeed a very able cross-examination of Mr. Singh by counsel for Lilly.

[35] Mr. Hems is the Director of Regulatory Affairs at Apotex. He testified as to the regulatory requirements which Apotex must meet in order to offer a drug on the market and the process used to meet these requirements. He oversaw the process for seeking approval for cefaclor, which began in 1993 with the filing of the original drug submission (TX-1761; TX-1762) and explained the analysis of the API which is necessary for such submissions. Mr. Hems also explained what a DMF contains and the portions of said files which Apotex may gain access to and how it may gain access to them.

[36] Except for the issue relating to the Tektrade invoices in respect of which the Court will make no finding, the evidence of the aforementioned witnesses was accepted.

[37] Dr. Sherman is the Chairman and Chief Executive Officer of Apotex. In this phase of the trial, he testified as to Apotex’s practices with regard to the sourcing of APIs, particularly cefaclor. He explained that, around the time where Apotex received its NOC for cefaclor, it hired an in house lawyer named Brigitte Fouillade, who has since passed away. Her role was to advise Dr. Sherman as to intellectual property issues. Referring to correspondence addressed to Ms. Fouillade from Kyong Bo dated October 10, 1997 (TX-662), Dr. Sherman explained that Kyong Bo represented to Apotex that it had rights to use the Shionogi process.

[38] With regard to Lupin, Dr. Sherman testified that while no formal agreement was entered into at first, it is his understanding that Ms. Fouillade attempted to ensure that the material supplied was not infringing. Ms. Fouillade developed a flow sheet for such a non-infringing process and, relying on correspondence between Ms. Fouillade and Mr. Singh (TX-679), explained that she was to ensure that this process was followed even if the cefaclor so produced was more costly, which is why Apotex then entered into a formal agreement.

[39] On cross-examination, Dr. Sherman was led to explain the reasons for which Apotex limited its choice of Lilly patents in its compulsory licence application (TX-265) and the reason which led him to terminate said licence (TX-267). He was also questioned as to why the agreement with Lupin (TX-1656) was not in the original affidavit of documents he signed (TX-327) and why no Notifiable Change had been filed by Apotex for this new process. He was also thoroughly questioned with regard to his answers on discovery pertaining to Lupin process information and communications between Lupin and Apotex. Finally, he also attempted to explain price variations for bulk cefaclor purchased, from Lupin and Kyong Bo.

[40] Generally, the Court has no problem with the credibility of Dr. Sherman’s testimony in respect of matters where he was directly involved as opposed to those where others were directly involved such as Ms. Fouillade. It is obvious and understandable that Dr. Sherman did not recall factual details and appeared sometimes to be offering explanations based on common sense and written documentation. The Court was certainly surprised by his candour when he noted that he did not read correspondence from his lawyers (there was simply too much of it) and he entirely relied on them when signing affidavits (it is not clear if he even read them all).[12]

[41] The testimonies of Mr. Singh, Mr. Patil and Mr. Satpute were heard under reserve of general objections (generally referred to as voir dire by the parties) which will be discussed in the section regarding infringement. Still, it is useful to briefly note what their testimonies relate to.

[42] Mr. Singh is the owner of Glopec International Inc. (Glopec), a company which imports and distributes raw pharmaceutical ingredients in both Canada and the United States. Glopec represents Indian manufacturers, such as Lupin, taking care not only of selling their products in Canada but also filing their regulatory materials with Health Canada. With regard to cefaclor, a certain amount of such correspondence related thereto was introduced in the course of his testimony (Glopec 1-14; 28-33). Also, Mr. Singh had in his files a certain amount of correspondence between Glopec and Apotex (addressed to Ms. Fouillade) regarding the process used by Lupin in the summer of 1997 and the subsequent development with Lupin of a non-infringing process (Glopec 16-26), as well as related correspondence with Lupin (Glopec 27; 35).[13]

[43] Mr. Singh also testified as to a big order of 7,500 kg of cefaclor passed by Apotex to be manufactured using the so-developed process. When Apotex was invoiced for bulk cefaclor manufactured by Lupin, these invoices were issued by Tektrade Ltd. (Glopec 36), a trading company owned by his in-laws in India and which Mr. Singh represents in Canada. Mr. Singh explained how the prices represented in these invoices were set and how payments are processed from Apotex through Tektrade Ltd. and finally to Lupin. While much of his cross-examination focused on these same points, counsel for Lilly was able to identify a rather large discrepancy between Tektrade Ltd. invoices and the data compiled by Apotex as to quantities received, which, as mentioned above, prompted Apotex to recall Mr. Fahner to testify on this point.

[44] Mr. Patil is the Vice-President of Regulatory Affairs at Lupin. At the relevant period, he was a senior manager within the same department. He was tasked with the registration of the companies’ products (DMFs), which include dosage form and API (bulk), the study of regulatory requirements in countries to which Lupin exports and compliance with these requirements. Mr. Patil testified as to how the registration and other requirements were performed at Lupin as well as what they generally entailed, with a particular focus on communications with Health Canada concerning cefaclor both directly from Lupin and via Glopec (which were tendered as Patil 1-6; TX-337; Glopec 4-5; 10). These documents came into the possession of Mr. Patil following a request made to Health Canada in 2008 to provide them as Lupin’s records had been largely lost in a flood in 2005 (some files still existed at the Bombay office while others were salvaged).

[45] Mr. Patil also testified as to the locations where cefaclor and 7-ACCA are manufactured. Correspondence between Lupin and Glopec was also tendered, for example Patil 8 (but also Patil 9; TX-158), which contained Mr. Patil’s handwriting in the margins and which prompted testimony about the interaction Mr. Patil had with the research and development (R&D) department (the letter was addressed to Dr. Gutpa, the chief of the R&D department) of Lupin regarding Apotex’s request for cefaclor produced using a third process. Concerning this third process, Mr. Patil testified as to a mix up in the correspondence in 1999, specifically an incorrect flow sheet depicting the manufacture of 7-ACCA appended thereto (see, for example, Patil 10).

[46] Mr. Satpute is the Vice-President of API manufacturing at Lupin’s Mandideep facilities. At the relevant period (1996-1999), he was the senior manager of Lupin’s Ankleshwai facility, which manufactured ethambutol, vitamin B-6 and two intermediates, 7-ADCA and 7-ACCA. After 1999, he took up this same role but at the Mandideep facilities where cephalexin, cefadroxil, cefaclor, ceftriaxone and cefatoxime are manufactured. Mr. Satpute testified as to the process used at the Ankleshwai facility to manufacture 7-ACCA and its subsequent transformation to cefaclor at Mandideep and the delay this entails.

[47] He testified that initially, in 1996, Lupin used a process which began with Pen V acid. Sometime in 1997, Lupin did trial batches and a few commercial ones to validate a new process starting with Pen G before reverting in 1998 to Pen V acid but using a third process which was slightly different from the one used in 1996 (particularly at what is described as step V in some of Lupin’s documents) to fulfill what he qualified as a “one of the biggest orders we received”. Mr. Satpute explained the implementation of this third process, the fact that it produced substantially lower yields (about 60 percent of the yields of the previous Pen V acid process used) and the use of chlorine (Cl) gas and TPP. Also when he was asked to find batch records for the 7-ACCA so produced, for which the plant manager and the R&D department would have created a template a few weeks before coming to Canada, he found that these documents no longer existed. It is not clear if anybody verified the files of the R&D department for the data relating to this process.

[48] Once this order was filled, Mr. Satpute testified that Lupin reverted to the Pen G process validated in the latter part of 1997. Documents referred to in the course of Mr. Satpute’s cross-examination were marked Satpute 1-3.

[49] Finally, the parties filed by consent an affidavit of Leslie Sands, Director of regulatory affairs at Lupin Pharmaceuticals Inc., a subsidiary of Lupin operating in the United States (TX-340). This filing was made under reserve of an objection that the documents therein are not proof of their contents but rather only of the existence of such communications with the U.S. Food and Drug Administration. The Court agrees with Apotex in this respect.

[50] In the main action, the parties filed 33 expert reports dealing with the infringement and invalidity allegations. They are listed in Chart A[14] attached hereto with the names of the experts, dates, subject matter and exhibit numbers, together with their area of expertise and a brief summary of their qualifications.

[51] On the question of infringement of the Shionogi patents by the use of the Kyong Bo process, Lilly called Dr. Anthony Barrett while Apotex responded with the evidence of Dr. Stephen Hanessian who touches on the issue of infringement of all the patents in issue mostly to support Apotex’s arguments with regard to importation (A-10). Both experts were properly qualified to opine on these issues. Their evidence in that respect was not contradicted. The Court accepts the evidence of Dr. Barrett in respect of the Kyong Bo process. While the relevance of Dr. Hanessian’s evidence will be discussed in the section dealing with importation.

[52] A much more contentious issue concerns the infringement of the Lilly patents, particularly whether the Lupin process described in the Health Canada file fell within the scope of the monopoly of the plaintiffs. Lilly’s main expert witnesses[15] in this respect were Drs. Miller and Baldwin. While Dr. Hunter[16] and Mr. Moraski reported and commented on the results of numerous experiments conducted by both sides in relation to this question, particularly with the use of 31P Nuclear Magnetic Resonance (31P NMR) Spectroscopy. Apotex’s experts on this question were Drs. Modro, McClelland and Cowley. Dr. Chase also testified about the tests he performed.

[53] An inordinate amount of time was spent discussing the results of the various experiments performed by both sides as well as their respective alleged flaws. It is clear that most of these experiments involved a certain amount of subjectivity (for example, what is yellow vs. light or faint yellow, or what is cooled vs. ice cooled or cooled with ice salt, what is room temperature, etc.) and that really none of the tests performed were perfect. For various reasons, choices were made with respect to temperature and equipment. Many things can and do go wrong in laboratories (broken valves, etc.). The Court used considerable caution in assessing the weight to be given to this evidence, but in the end, considering the construction of the claims at issue adopted, most of these experiments and the comments relating thereto became somewhat irrelevant. With respect to those that remain relevant, such as reactions carried out on cephalosporin substrate with or without a halogen scavenger, individual tests were not considered in isolation, in the sense that the Court always looked to confirm if the results were supported by other evidence on the record.

[54] The one positive aspect of the testing is that it led to the abandon of some of the arguments and helped focus the debate.

[55] There was a lengthy debate about the admissibility of tests performed ex parte and how tests must be introduced in the evidence. In the end, these issues were settled without the need for a ruling. Nevertheless, it is important to note that pre-trial scheduling orders setting deadlines for the reporting of test results, absent an express indication to the contrary, must not be construed to constitute a waiver of any requirement that may exist regarding notice of testing to be performed pre-trial.

[56] Also, with respect to the infringement of the Lilly process patents, the Court granted leave to both parties to file expert evidence on issues arising from the testimony of Mr. Satpute. Dr. Barrett (E-15), who had only previously been dealing with the Shionogi patents, and Dr. Hanessian (A-20) testified in respect of the various processes allegedly used by Lupin.

[57] Turning now to the validity phase of the trial, Apotex relied on the evidence of Drs. McClelland, Hanessian and Martin in respect of the Shionogi patents while Lilly responded with the evidence of Dr. Barrett and that of Mr. Murphy, who focused on the prosecution of the Shionogi patents and the unity of invention practice of the Canadian Patent Office.

[58] In respect of the Lilly patents, Drs. Modro, Chivers, Olah and McClelland discussed the validity of the ‘007 patent while Dr. McClelland also addressed issues relating to all the Lilly process patents and Dr. Olah opined in respect of the ‘536 patent. In response, Lilly relied upon the evidence of Dr. Baldwin who discussed all of the Lilly patents and Dr. Hunter who focussed on certain allegations in respect of the ‘007 patent. Mr. Murphy also discussed the prosecution of the Lilly patents and the unity of invention practice in relation thereto.

[59] In respect of infringement by the Lupin process, the Court found the evidence of Dr. Baldwin and Dr. Miller particularly helpful. Despite Apotex’s attempts to challenge their credibility on the basis that they had worked as a consultants for Lilly from time to time and the university where Dr. Miller teaches received some grants from Lilly, the Court is satisfied that they gave their evidence in a straightforward, unbiased manner. In that respect, the Court notes that early in his testimony, Dr. Baldwin readily admitted that the kinetic complex must have formed when one carried out some of the experiments in the prior art.

[60] In respect of the validity of the Lilly patents, like the House of Lords in Synthon BV v. Smithkline Beecham plc, [2005] UKHL 59, [2006] 1 All ER 685 (Synthon), who described him as one of the foremost organic chemists in the world, the Court found Dr. Baldwin to be particularly well qualified to opine on the issues of fact covered in his report. In fact, he was the only expert witness that was properly qualified to opine on the common general knowledge of the posita to whom the Lilly process patents were addressed and how said posita would read those patents or the relevant prior art.

[61] Drs. Modro, Olah and McClelland were all properly qualified to opine in respect of the ‘007 patent. Generally the Court had no difficulties with their credibility although, the Court was more cautious with the evidence of Dr. McClelland because of his vast experience acting as an expert in patent cases he was somewhat less spontaneous than other Apotex experts.

[62] It is obvious, and Drs. Modro and Martin readily admitted it, that Ivor Hughes and Dr. Stewart from his office played a very significant role in the drafting of the reports (presumably all of them except maybe for that of Dr. McClelland). Normally there is nothing wrong with being assisted by one’s lawyer in drafting one’s report but despite the Court’s flexibility in that respect, one must not lose sight of the principle expressed in National Justice Compania Riviera S.A. v. Prudential Assurance Co. (“the Ikarian Reefer”), [1993] 2 Lloyd’s Rep. 68 to the effect that “expert evidence should be seen as the independent product of the expert uninfluenced as to form or content by the exigencies of litigation: Whitehouse v Jordan [1981] 1 WLR 246 at 256, per Lord Wilberforce” (emphasis added). Certainly the more the lawyers are involved the more careful an expert must be in reviewing the text proposed to ensure that it truly reflects his or her views. There was some evidence in this case that the review, by Apotex’s experts particularly, was not as careful as one would expect.

[63] Although the Court generally accepted the evidence of Dr. Hunter in respect of the testing performed and found his evidence credible in respect of the common general knowledge about 31P NMR and the impact of various factors on the ppm chemical shift at the relevant time, his evidence was not as useful considering the construction of the claims at issue adopted by the Court. With respect to the validity of the ‘007 patent (E-18), the Court notes that Dr. Hunter’s PhD is in inorganic chemistry. His evidence was given the same weight as that of Dr. Chivers’ in respect of the said patent.

[64] Again, in view of the construction of the claims at issue, most of the evidence of Dr. Cowley was not particularly useful. In respect of the view he expressed in para. 27 of his report (A-9), the Court preferred the opinion of Dr. Hunter which was corroborated by the tests performed, including those of Dr. Chase. The Court was unimpressed by his evidence with respect to the Spaggiari article.[17]

[65] As mentioned, Dr. Chivers, like Dr. Hunter, has a PhD in inorganic chemistry[18] with particular expertise in chemistry involving various elements including phosphorus. He testified in a straightforward, clear and credible manner. It is evident that he had initially also been asked to comment on the validity of the ‘536 patent, a matter in respect of which he was clearly not qualified, but the report he filed when he took the stand was heavily redacted, probably in response to Lilly’s objection that th

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 22183:4 · paragraphs 68-76

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `293335d11ac015dbfe6834a1813c37c27505a7a6ef44d33cd931992ffe198d55`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:4:subtheme:1 · paragraphs 68-71

- Raw key terms: `patent, respect, cephalosporin, chemistry, cross-examination, evidence, experience, olah`
- Display key terms: `patent, respect, cephalosporin, chemistry, cross-examination, experience, olah`
- Argument roles: `counterargument_limitation, evidence_fact`
- Explanation: Observed roles: counterargument_limitation, evidence_fact Display terms: patent, respect, cephalosporin, chemistry, cross-examination, experience, olah Evidence spans paragraphs 68-71. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040314` offsets `171-178`; context: However, he has no experience whatsoever with respect to β-lactams or cephalosporin chemistry.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040316` offsets `84-92`; context: Baldwin’s evidence in respect of the ‘536 patent to that of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040317` offsets `22-30`; context: McClelland’s evidence in respect of the Lilly process patents and the Shionogi patents falls pretty much in the same category especially when one considers that he should know better given his vast experience in litigation.

#### 22183:4:subtheme:2 · paragraphs 72-73

- Raw key terms: `another, expert, role, according, addressed, agree, alone, appear`
- Display key terms: `another, expert, role, according, addressed, agree, alone, appear`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: another, expert, role, according, addressed, agree, alone, appear Application context: [72] This is a problem because one’s willingness to offer an opinion without an appropriate basis to do so can impact on the overall credibility of a witness otherwise qualified to opine on another issue for it can raise Evidence spans paragraphs 72-73. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040318` offsets `198-203`; context: [72] This is a problem because one’s willingness to offer an opinion without an appropriate basis to do so can impact on the overall credibility of a witness otherwise qualified to opine on another issue for it can raise some doubt as to the existence of a proper basis for the other portion of his opinion or as to whether the expert really understood his role.
- Evidence: `reasoning_application` cue `because` at chunk `5040318` offsets `23-30`; context: [72] This is a problem because one’s willingness to offer an opinion without an appropriate basis to do so can impact on the overall credibility of a witness otherwise qualified to opine on another issue for it can raise some doubt as to the existence of a proper basis for the other portion of his opinion or as to whether the expert really understood his role.
- Evidence: `issue` cue `question` at chunk `5040319` offsets `595-603`; context: This puts in question Dr.

#### 22183:4:subtheme:3 · paragraphs 74-75

- Raw key terms: `action, apotex, canada, evidence, lilly, parties, standing, a-11`
- Display key terms: `action, apotex, lilly, standing, a-11`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: action, apotex, lilly, standing, a-11 Rule/authority context: (4th) 241 (Laboratoires Servier) that read as follows: The test for who qualifies as a person claiming under a patentee is not simply whether the patentee has consented to the person being joined as a plaintiff in an act Application context: It also brought to light that there may be a loophole in the regulations or at least in how they are applied. Evidence spans paragraphs 74-75. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040320` offsets `13-18`; context: [74] Another issue on which the parties presented expert evidence was on pharmaceutical regulatory affairs, particularly the filing of NDSs and DMFs and the requirements for keeping these filings up to date.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040320` offsets `57-65`; context: [74] Another issue on which the parties presented expert evidence was on pharmaceutical regulatory affairs, particularly the filing of NDSs and DMFs and the requirements for keeping these filings up to date.
- Evidence: `reasoning_application` cue `applied` at chunk `5040320` offsets `621-628`; context: It also brought to light that there may be a loophole in the regulations or at least in how they are applied.
- Evidence: `issue` cue `whether` at chunk `5040321` offsets `425-432`; context: (4th) 241 (Laboratoires Servier) that read as follows:
The test for who qualifies as a person claiming under a patentee is not simply whether the patentee has consented to the person being joined as a plaintiff in an action; nor is it enough to demonstrate that two parties are related.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040321` offsets `773-781`; context: In each case, the facts must demonstrate a credible and legally sufficient basis for claiming under a patentee
[…]
As noted above, the mere existence of a corporate affiliation is not conclusive evidence of a right under s.
- Evidence: `governing_rule` cue `under` at chunk `5040321` offsets `394-399`; context: (4th) 241 (Laboratoires Servier) that read as follows:
The test for who qualifies as a person claiming under a patentee is not simply whether the patentee has consented to the person being joined as a plaintiff in an action; nor is it enough to demonstrate that two parties are related.

#### 22183:4:subtheme:4 · paragraphs 76-76

- Raw key terms: `above-noted, admitted, agreement, canada, case, ceclor, cefaclor, certain`
- Display key terms: `above-noted, admitted, agreement, case, ceclor, cefaclor, certain`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: above-noted, admitted, agreement, case, ceclor, cefaclor, certain Evidence spans paragraphs 76-76. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040322` offsets `338-343`; context: 56-63; 83-84) that Lilly Canada is a wholly owned subsidiary, but also that it had an express licence to both the Lilly and Shionogi Patents at issue in this case.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040322` offsets `143-152`; context: [76] Lilly Canada does not disagree with the above-noted statements, it simply says that in this case it has not only established, through the testimony of Mr.

#### Section text

[68] Dr. Olah is an imminent scientist. Among his many outstanding achievements, he has won a Nobel Prize in 1994 for his work on positively charged compounds of carbons. However, he has no experience whatsoever with respect to β-lactams or cephalosporin chemistry. Despite this, he was asked to opine on the validity of the ‘536 patent on the basis of publications provided to him by Ivor Hughes, one of Apotex’s counsel at the time. Like other experts acting for Apotex, his report includes a description of the addressee of these patents which appear to be meant to fit his credentials.

[69] In cross-examination, he could not name a reagent used in cephalosporin chemistry – the type of chemistry discussed in the ‘536 patent. This may explain why he appeared as a reluctant witness who even refused to answer some questions during his cross-examination until offered a choice between withdrawing his report and answering the questions put to him. It may also explain comments such as: “I wouldn’t stick out my reputation one way or another to argue that the few ppm one way or the other is a fundamentally different situation.”[20]

[70] In such a case, it is easy to understand why the Court preferred Dr. Baldwin’s evidence in respect of the ‘536 patent to that of Dr. Olah, and why time spent on examination and cross-examination of a witness that is not “the right expert for the job” is almost always time lost for all concerned.

[71] Dr. McClelland’s evidence in respect of the Lilly process patents and the Shionogi patents falls pretty much in the same category especially when one considers that he should know better given his vast experience in litigation.

[72] This is a problem because one’s willingness to offer an opinion without an appropriate basis to do so can impact on the overall credibility of a witness otherwise qualified to opine on another issue for it can raise some doubt as to the existence of a proper basis for the other portion of his opinion or as to whether the expert really understood his role.[21]

[73] Dr. Martin is another distinguished organic chemist expert in his field which includes lactams but he has no experience whatsoever in β-lactam chemistry let alone cephalosporin chemistry – a prerequisite of the posita to whom the Shionogi patents are addressed according to para. 12 of his report. In an attempt to compensate for his “obvious” inability to see through the eyes of such posita, Dr. Martin testified that in the claimed reactions in fact the β-lactam molecule remains a spectator. The Court cannot agree and as argued by Lilly, this is a clear use of hindsight. This puts in question Dr. Martin’s understanding of his role particularly as he also offered comments on other issues that appear to go beyond his expertise and personal knowledge (conferences given by Kishi and the invention not claimed in the Shionogi patents).

[74] Another issue on which the parties presented expert evidence was on pharmaceutical regulatory affairs, particularly the filing of NDSs and DMFs and the requirements for keeping these filings up to date. For this purpose, Lilly called upon Ms. Azzarello who filed one report (E-7) and Apotex relied on the testimony of Ms. Wehner, who did likewise (A-11). This evidence provided some background for the debate on the evidentiary value of the information provided to Health Canada by the foreign suppliers of Apotex. It also brought to light that there may be a loophole in the regulations or at least in how they are applied. According to Ms. Wehner, it is known that foreign suppliers do not always abide by the regulations and file up-to-date information about their processes. Also changes are sometimes implemented before receiving Health Canada approval. I understand that this may have an impact on the ultimate safety of the product because the testing performed on the API by the Canadian sponsor may need to be adapted[22] to the process used to manufacture it. Clearly this is a matter for the regulator, not a Court dealing with an infringement action. That said, in the end, this evidence was not particularly useful.
3. Lilly Canada’s Lack of Standing

[75] Apotex argues that Lilly Canada has not proven its standing to sue. It alleges that a bare assertion of a corporate relationship is not sufficient. In that respect, it relies on two statements made by Justice Judith Snider in Laboratoires Servier v. Apotex Inc., 2008 FC 825, 67 C.P.R. (4th) 241 (Laboratoires Servier) that read as follows:
The test for who qualifies as a person claiming under a patentee is not simply whether the patentee has consented to the person being joined as a plaintiff in an action; nor is it enough to demonstrate that two parties are related. In each case, the facts must demonstrate a credible and legally sufficient basis for claiming under a patentee
[…]
As noted above, the mere existence of a corporate affiliation is not conclusive evidence of a right under s. 55(1) of the Patent Act. There must be something more. That something more has consistently been described in the jurisprudence as a license or some other arrangement (for example, a lease, an assignment, or a sale) that would give the affiliate the right to use the patent.
[paras. 70 and 82]

[76] Lilly Canada does not disagree with the above-noted statements, it simply says that in this case it has not only established, through the testimony of Mr. Pytynia (Transcript Volume 7, pp. 56-63; 83-84) that Lilly Canada is a wholly owned subsidiary, but also that it had an express licence to both the Lilly and Shionogi Patents at issue in this case. It has also been admitted that Lilly Canada has been selling Ceclor® (cefaclor) in Canada since 1980. Lilly Canada made specific references to various exhibits filed during the hearing to support its position, particularly an agreement executed and effective as of January 1, 1991 between Lilly U.S. and Lilly Canada (TX-109) where:
Lilly represents and warrants that for Canada, it has the exclusive right to grant licenses to enable the licensee to make, have made, use and sell certain products, including the right to use within Canada, certain patents, trademarks
[…]
relating to such products and to their preparation, manufacture, processing and packaging.

## 22183:5 · paragraphs 77-147

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b5044f75c9dbd33c6858c127b7e37b87cd584c305e947eb97d823f774a354f47`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:5:subtheme:1 · paragraphs 77-83

- Raw key terms: `canada, lilly, agreement, patents, granted, patent, amended, having`
- Display key terms: `lilly, agreement, patents, granted, patent, amended, having`
- Argument roles: `disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue Display terms: lilly, agreement, patents, granted, patent, amended, having Rule/authority context: 2: Lilly further grants to Lilly Canada a non-exclusive sublicense (without right of further sublicense except as further granted in writing by Lilly) under the Canadian patent applications and patents listed in Schedule | Normally, it should thus not be contentious that Lilly Canada has proper standing pursuant to subs. Operative outcome context: 2: Lilly further grants to Lilly Canada a non-exclusive sublicense (without right of further sublicense except as further granted in writing by Lilly) under the Canadian patent applications and patents listed in Schedule | According to Apotex, the result of this amendment is simply that licences to the Lilly or Shionogi patents were no longer granted to Lilly Canada. Evidence spans paragraphs 77-83. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5040323` offsets `316-321`; context: 2:
Lilly further grants to Lilly Canada a non-exclusive sublicense (without right of further sublicense except as further granted in writing by Lilly) under the Canadian patent applications and patents listed in Schedule “A”
[…]
to make, have made, use or sell, and/or import Lilly Products whose preparation is covered by the patent applications and patents.
- Evidence: `disposition` cue `granted` at chunk `5040323` offsets `287-294`; context: 2:
Lilly further grants to Lilly Canada a non-exclusive sublicense (without right of further sublicense except as further granted in writing by Lilly) under the Canadian patent applications and patents listed in Schedule “A”
[…]
to make, have made, use or sell, and/or import Lilly Products whose preparation is covered by the patent applications and patents.
- Evidence: `issue` cue `issue` at chunk `5040324` offsets `61-66`; context: 8 and 9 of Schedule A, the four Lilly patents at issue here are listed.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040324` offsets `166-177`; context: Normally, it should thus not be contentious that Lilly Canada has proper standing pursuant to subs.
- Evidence: `disposition` cue `granted` at chunk `5040325` offsets `361-368`; context: According to Apotex, the result of this amendment is simply that licences to the Lilly or Shionogi patents were no longer granted to Lilly Canada.
- Evidence: `governing_rule` cue `under` at chunk `5040327` offsets `386-391`; context: The January 1, 1995 agreement expressly states:
WHEREAS the parties desire to maintain the rights, licenses and sublicenses granted by the AGREEMENT while also recognizing that the parties will receive full compensation under the Master Supply and Distribution and Manufacturing or other Agreements.
- Evidence: `disposition` cue `granted` at chunk `5040327` offsets `290-297`; context: The January 1, 1995 agreement expressly states:
WHEREAS the parties desire to maintain the rights, licenses and sublicenses granted by the AGREEMENT while also recognizing that the parties will receive full compensation under the Master Supply and Distribution and Manufacturing or other Agreements.
- Evidence: `governing_rule` cue `under` at chunk `5040328` offsets `166-171`; context: [82] It is also worth noting that the 1991 agreement was further amended on April 9, 1998 (TX-113) giving Lilly Canada the right to further sub-licence a third party under some of the patents covered by the agreement, in conformity with s.
- Evidence: `disposition` cue `granted` at chunk `5040328` offsets `322-329`; context: More particularly, the amendment refers to the licence granted under the 1991 agreement for cefaclor and:
grants to Lilly Canada the right to sub-license the following licenses granted to it under the [1991] License Agreement (collectively, the “Licenses”) for cefaclor: (i) licenses granted under patent rights of Lilly U.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040329` offsets `34-42`; context: [83] Having considered all of the evidence, the Court is satisfied that Lilly Canada has properly established its standing based on an express licence from the patentee.

#### 22183:5:subtheme:2 · paragraphs 84-86

- Raw key terms: `patent, patentee, appeal, canada, case, claim, claiming, court`
- Display key terms: `patent, patentee, case, claiming`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: patent, patentee, case, claiming Rule/authority context: had an unwritten licence to all the patents held by companies under the control of Glaxo Wellcome Inc. | [85] In fact, Lilly Canada argues that in the past, the Federal Court of Appeal has accepted less than an exclusive or non-exclusive licence as evidence of a right to claim under the patentee. Application context: The agreement between it and the patentee did not make any specific reference to the patents or rights of any kind thereunder, leading Justice Paul Rouleau to conclude that the plaintiff had no standing to sue for infrin Evidence spans paragraphs 84-86. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040330` offsets `31-36`; context: [84] Before concluding on this issue, it is worth quoting a passage from the decision of the Federal Court of Appeal in Apotex Inc.
- Evidence: `governing_rule` cue `under` at chunk `5040330` offsets `522-527`; context: had an unwritten licence to all the patents held by companies under the control of Glaxo Wellcome Inc.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040331` offsets `144-152`; context: [85] In fact, Lilly Canada argues that in the past, the Federal Court of Appeal has accepted less than an exclusive or non-exclusive licence as evidence of a right to claim under the patentee.
- Evidence: `governing_rule` cue `under` at chunk `5040331` offsets `173-178`; context: [85] In fact, Lilly Canada argues that in the past, the Federal Court of Appeal has accepted less than an exclusive or non-exclusive licence as evidence of a right to claim under the patentee.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040331` offsets `610-618`; context: The agreement between it and the patentee did not make any specific reference to the patents or rights of any kind thereunder, leading Justice Paul Rouleau to conclude that the plaintiff had no standing to sue for infringement.

#### 22183:5:subtheme:3 · paragraphs 87-96

- Raw key terms: `court, claims, construe, para, patent, patents, skilled, canada`
- Display key terms: `claims, construe, para, patent, patents, skilled`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: claims, construe, para, patent, patents, skilled Position/evidence statements: 21 (Shire), the Court “is not to construe a claim without knowing where disputes between the parties lie. | [89] To these more general principles, one should also add that the Court adopts and will apply Justice Denis Pelletier’s statement regarding claim differentiation in Halford v. Rule/authority context: The principles of construction are well-established. | [89] To these more general principles, one should also add that the Court adopts and will apply Justice Denis Pelletier’s statement regarding claim differentiation in Halford v. Application context: Be it sufficient to say that “[t]he key to purposive construction is therefore the identification by the court, with the assistance of the skilled reader, of the particular words and phrases in the claims that describe w | [89] To these more general principles, one should also add that the Court adopts and will apply Justice Denis Pelletier’s statement regarding claim differentiation in Halford v. Evidence spans paragraphs 87-96. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040333` offsets `110-115`; context: [87] Before considering the allegations of infringement and invalidity, the Court must construe the claims at issue in this proceeding.
- Evidence: `governing_rule` cue `principles` at chunk `5040333` offsets `140-150`; context: The principles of construction are well-established.
- Evidence: `reasoning_application` cue `therefore` at chunk `5040333` offsets `538-547`; context: Be it sufficient to say that “[t]he key to purposive construction is therefore the identification by the court, with the assistance of the skilled reader, of the particular words and phrases in the claims that describe what the inventor considered to be the “essential” elements of his invention.
- Evidence: `issue` cue `issue` at chunk `5040334` offsets `335-340`; context: ” This is particularly important in cases such as this one, where a large number of claims in eight distinct patents are at issue.
- Evidence: `party_position` cue `claim` at chunk `5040334` offsets `150-155`; context: 21 (Shire), the Court “is not to construe a claim without knowing where disputes between the parties lie.
- Evidence: `party_position` cue `claim` at chunk `5040335` offsets `142-147`; context: [89] To these more general principles, one should also add that the Court adopts and will apply Justice Denis Pelletier’s statement regarding claim differentiation in Halford v.
- Evidence: `governing_rule` cue `principles` at chunk `5040335` offsets `27-37`; context: [89] To these more general principles, one should also add that the Court adopts and will apply Justice Denis Pelletier’s statement regarding claim differentiation in Halford v.
- Evidence: `reasoning_application` cue `apply` at chunk `5040335` offsets `90-95`; context: [89] To these more general principles, one should also add that the Court adopts and will apply Justice Denis Pelletier’s statement regarding claim differentiation in Halford v.
- Evidence: `party_position` cue `claims` at chunk `5040337` offsets `359-365`; context: [91] With respect to the ‘007 patent, although the disclosure discusses, among other things, the utility of the new class of halogenating compounds in the chemistry of cephalosporins, the Court is satisfied that the art to which the patent relates is wider than the chemistry of cephalosporins for the patent covers the kinetic complexes (compound by process claims) and processes to make them.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040339` offsets `504-513`; context: Baldwin, who was actively working in that field at the time, described those researchers in his testimony.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040340` offsets `661-669`; context: ”[29] That said, this finding will have little impact on the evaluation of their evidence, given that, as mentioned when discussing the weight given to the expert evidence, Apotex’s experts who commented on the Lilly process patents would not meet either description as there is no evidence that any of them had a particular interest in cephalosporins prior to their involvement in this litigation.
- Evidence: `governing_rule` cue `Principles` at chunk `5040340` offsets `1275-1285`; context: Common General Knowledge (Principles)
- Evidence: `evidence_fact` cue `evidence` at chunk `5040341` offsets `82-90`; context: [95] During the trial, the Court noted on several occasions that there was little evidence to establish that the numerous publications, patents, applications relied upon by various experts were part of the common general knowledge of the posita at the relevant time.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040341` offsets `467-470`; context: While this was to a certain extent cured through the cross-examinations, it remains that too little attention was given to such matters which are of prime importance, not only to construe the claims, but also to assess the prior art put forth to establish invalidity.

#### 22183:5:subtheme:4 · paragraphs 97-99

- Raw key terms: `knowledge, noted, para, becomes, difficult, evidence, find, form`
- Display key terms: `knowledge, noted, para, becomes, difficult, find, form`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: knowledge, noted, para, becomes, difficult, find, form Rule/authority context: There appears to be adequate authority in the jurisprudence for such a test. Application context: A piece of particular knowledge as disclosed in a scientific paper does not become common general knowledge merely because it is widely read, and still less because it is widely circulated. | 27: In reviewing the prior art I have also been persuaded by counsel for the plaintiff that an objective test should be applied to determine whether the hypothetical skilled workman in the art could be reasonably assumed Evidence spans paragraphs 97-99. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040343` offsets `910-918`; context: On the other hand, common general knowledge is a different concept derived from a commonsense approach to the practical question of what would in fact be known to an appropriately skilled addressee – the sort of man, good at his job, that could be found in real life.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040343` offsets `1502-1510`; context: As to the former, it is clear that individual patent specifications and their contents do not normally form part of the relevant common general knowledge, though there may be specifications which are so well known amongst those versed in the art that upon evidence of that state of affairs they form part of such knowledge, and also there may occasionally be particular industries (such as that of colour photography) in which the evidence may show that all specifications form part of the relevant knowledge.
- Evidence: `reasoning_application` cue `because` at chunk `5040343` offsets `2361-2368`; context: A piece of particular knowledge as disclosed in a scientific paper does not become common general knowledge merely because it is widely read, and still less because it is widely circulated.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040343` offsets `619-626`; context: 188 at 193) concept of patent law that each and every specification, of the last 50 years, however unlikely to be looked at and in whatever language written, is part of the relevant public knowledge if it is resting anywhere in the shelves of the Patent Office.
- Evidence: `issue` cue `whether` at chunk `5040344` offsets `265-272`; context: 27:
In reviewing the prior art I have also been persuaded by counsel for the plaintiff that an objective test should be applied to determine whether the hypothetical skilled workman in the art could be reasonably assumed to have knowledge of such prior art.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040344` offsets `462-470`; context: No evidence was produced by the defendants to show that the ordinary skilled workman should be assumed to have been aware of all of this prior art.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5040344` offsets `428-441`; context: There appears to be adequate authority in the jurisprudence for such a test.
- Evidence: `reasoning_application` cue `applied` at chunk `5040344` offsets `244-251`; context: 27:
In reviewing the prior art I have also been persuaded by counsel for the plaintiff that an objective test should be applied to determine whether the hypothetical skilled workman in the art could be reasonably assumed to have knowledge of such prior art.

#### 22183:5:subtheme:5 · paragraphs 100-103

- Raw key terms: `time, addressee, given, relevant, become, common, during, evidence`
- Display key terms: `time, addressee, given, relevant, become, common, during`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: time, addressee, given, relevant, become, common, during Evidence spans paragraphs 100-103. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040346` offsets `482-489`; context: In order to establish whether something is common general knowledge, the first and most important step is to look at the sources from which the skilled addressee could acquire his information.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040346` offsets `783-791`; context: The publication at or before the relevant date of other documents such as patent specifications may be to some extent prima facie evidence tending to show that the statements contained in them were part of the common knowledge, but is far from complete proof, as the statements may well have been discredited or forgotten or merely
ignored.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040346` offsets `881-884`; context: The publication at or before the relevant date of other documents such as patent specifications may be to some extent prima facie evidence tending to show that the statements contained in them were part of the common knowledge, but is far from complete proof, as the statements may well have been discredited or forgotten or merely
ignored.
- Evidence: `issue` cue `issue` at chunk `5040347` offsets `1063-1068`; context: Such experts could not rely on their own experience and memories of these publications and they opined on the validity of various process patents at issue simply on the basis of the written material provided to them.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040347` offsets `278-286`; context: However, he did not testify[31] and no evidence was given as to how the search for this literature was conducted.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040347` offsets `239-246`; context: However, he did not testify[31] and no evidence was given as to how the search for this literature was conducted.

#### 22183:5:subtheme:6 · paragraphs 104-105

- Raw key terms: `action, anticipation, assessing, availability, basis, because, certain, circumstances`
- Display key terms: `action, anticipation, assessing, availability, basis, because, certain, circumstances`
- Argument roles: `counterargument_limitation, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, reasoning_application Display terms: action, anticipation, assessing, availability, basis, because, certain, circumstances Application context: [104] The distinction between common general knowledge and prior art which is part of the state of the art for the purpose of assessing anticipation and obviousness tends to diminish in modern times because of the sophis Evidence spans paragraphs 104-105. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040350` offsets `497-503`; context: 483) is still very relevant when one considers issues such as obviousness, where mosaicing is permitted in certain circumstances.
- Evidence: `reasoning_application` cue `because` at chunk `5040350` offsets `199-206`; context: [104] The distinction between common general knowledge and prior art which is part of the state of the art for the purpose of assessing anticipation and obviousness tends to diminish in modern times because of the sophistication of search engines and the availability of electronic publications and databases.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `5040350` offsets `310-322`; context: Nevertheless, the degree to which a particular publication was “generally regarded as a good basis for further action” (General Tire, at p.

#### 22183:5:subtheme:7 · paragraphs 106-107

- Raw key terms: `claims, compound, example, process, above, alkoxy, alkyl, amounts`
- Display key terms: `claims, compound, example, process, above, alkoxy, alkyl, amounts`
- Argument roles: `counterargument_limitation, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, issue, party_position Display terms: claims, compound, example, process, above, alkoxy, alkyl, amounts Position/evidence statements: [107] The Court will use claims 1 and 17, as their construction has been a subject of dispute between the parties. Evidence spans paragraphs 106-107. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040352` offsets `51-56`; context: [106] The claims of the ‘007 patent that remain at issue are claims 1, 4 (dependent on claims 1, 2 or 3), 13 (dependent on claims 8, 9 or 10), 17 (dependent on claims 8, 9 or 10) and 18 (dependent on claims 8, 9 or 10).
- Evidence: `party_position` cue `claims` at chunk `5040353` offsets `25-31`; context: [107] The Court will use claims 1 and 17, as their construction has been a subject of dispute between the parties.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040353` offsets `600-607`; context: However, to better understand claim 17, one must look, for example, as to how it would read if one used the process described in claim 8.

#### 22183:5:subtheme:8 · paragraphs 108-109

- Raw key terms: `claim, claims, compound, elements, essential, formula, absorptions, acid`
- Display key terms: `claims, compound, elements, essential, formula, absorptions, acid`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: claims, compound, elements, essential, formula, absorptions, acid Evidence spans paragraphs 108-109. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040354` offsets `68-73`; context: [108] It is also useful to reproduce claim 6 which, although not at issue, has been referred to by all parties when discussing the essential elements of claims 1 and 4 in particular.

#### 22183:5:subtheme:9 · paragraphs 110-120

- Raw key terms: `disclosure, compounds, described, reaction, triaryl, phosphite, prior, product`
- Display key terms: `disclosure, compounds, described, reaction, triaryl, phosphite, prior, product`
- Argument roles: `counterargument_limitation, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, party_position, reasoning_application Display terms: disclosure, compounds, described, reaction, triaryl, phosphite, prior, product Position/evidence statements: [110] The parties disagree, however, on whether or not the specific solvent described in claim 17 is an essential element of that claim. Rule/authority context: Unlike the prior art triaryl phosphite dichlorides, however, the present compounds efficiently halogenate under mild conditions both enolic groups to form the corresponding vinyl halides and, in the presence of base, ami Application context: Therefore, the dot (●) in the general formula used for example in claims 1 and 17 (dependent on claim 8, 9, or 10): is used simply to designate that equivalent amounts of halogen and phosphite reagent are combined chemic Evidence spans paragraphs 110-120. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040356` offsets `40-47`; context: [110] The parties disagree, however, on whether or not the specific solvent described in claim 17 is an essential element of that claim.
- Evidence: `party_position` cue `claim` at chunk `5040356` offsets `89-94`; context: [110] The parties disagree, however, on whether or not the specific solvent described in claim 17 is an essential element of that claim.
- Evidence: `counterargument_limitation` cue `although` at chunk `5040357` offsets `315-323`; context: 14 to mean that:
although anhydrous organic solvents are generally preferred, trace amounts of water, such as that often found in commercially available solvents, can be tolerated.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5040361` offsets `328-337`; context: Therefore, the dot (●) in the general formula used for example in claims 1 and 17 (dependent on claim 8, 9, or 10):
is used simply to designate that equivalent amounts of halogen and phosphite reagent are combined chemically and in a way that can be distinguished from that in the prior art compounds which typically have been drawn without the dot.
- Evidence: `governing_rule` cue `under` at chunk `5040362` offsets `470-475`; context: Unlike the prior art triaryl phosphite dichlorides, however, the present compounds efficiently halogenate under mild conditions both enolic groups to form the corresponding vinyl halides and, in the presence of base, amido functions to form the corresponding imino halides.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040362` offsets `416-423`; context: Unlike the prior art triaryl phosphite dichlorides, however, the present compounds efficiently halogenate under mild conditions both enolic groups to form the corresponding vinyl halides and, in the presence of base, amido functions to form the corresponding imino halides.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040364` offsets `192-199`; context: However, except for claims 18 and 8, where the reaction temperature for carrying out the process of the claims described therein is stated as “about -70 to about 0º C” and, to some extent, claims 17 and 27, which specifically refer to the solvent being an aromatic hydrocarbon or halogenated hydrocarbon[40], none of the claims include elements directed to stabilizing or improving the formation of the kinetically controlled product of the reaction described in the claims.

#### 22183:5:subtheme:10 · paragraphs 121-123

- Raw key terms: `claim, properties, reaction, adopt, claims, construing, controlled, covers`
- Display key terms: `properties, reaction, adopt, claims, construing, controlled, covers`
- Argument roles: `counterargument_limitation, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, reasoning_application Display terms: properties, reaction, adopt, claims, construing, controlled, covers Application context: It is clear that claim 6 is more limited in scope than claim 1 because it covers only a subset of the compound, i. Evidence spans paragraphs 121-123. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040367` offsets `472-477`; context: [44] Although these two claims are not at issue, as mentioned in Hoffmann (2005) and Halford, they can be useful in construing the claims at issue.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040367` offsets `435-443`; context: [44] Although these two claims are not at issue, as mentioned in Hoffmann (2005) and Halford, they can be useful in construing the claims at issue.
- Evidence: `reasoning_application` cue `because` at chunk `5040368` offsets `139-146`; context: It is clear that claim 6 is more limited in scope than claim 1 because it covers only a subset of the compound, i.

#### 22183:5:subtheme:11 · paragraphs 124-128

- Raw key terms: `court, controlled, kinetically, product, complex, compound, disclosure, kinetic`
- Display key terms: `controlled, kinetically, product, complex, compound, disclosure, kinetic`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: controlled, kinetically, product, complex, compound, disclosure, kinetic Application context: 7 ppm (or any other data included in claim 6) when applied to the kinetically controlled product of the reaction between TPP and Cl. Evidence spans paragraphs 124-128. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040370` offsets `89-95`; context: [124] Having considered the specification as a whole, the Court can now address the main issues raised by the parties (see para.
- Evidence: `reasoning_application` cue `applied` at chunk `5040371` offsets `342-349`; context: 7 ppm (or any other data included in claim 6) when applied to the kinetically controlled product of the reaction between TPP and Cl.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040373` offsets `15-23`; context: [127] There is evidence from Dr.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040373` offsets `424-427`; context: McClelland states that:
This is criteria, but the basic term, “kinetic complex,” as used in the patent, indicates that it’s not stable in regards to what its half-life is, and that it would convert to the thermodynamic complex with time.

#### 22183:5:subtheme:12 · paragraphs 129-131

- Raw key terms: `claimed, compounds, compound, disclosure, distinguish, fact, focus, formula`
- Display key terms: `claimed, compounds, compound, disclosure, distinguish, fact, focus, formula`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: claimed, compounds, compound, disclosure, distinguish, fact, focus, formula Position/evidence statements: 15 of his affidavit (TX-1764) he states that: [t]he skilled chemist would understand from the patent that these criteria such as the 31P NMR chemical shift and the IR are to be employed to distinguish the novel kinetic p Evidence spans paragraphs 129-131. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040375` offsets `710-718`; context: This does not however answer the question of law as to whether these elements are included in claim 1 as essential elements of the monopoly described therein.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040375` offsets `691-698`; context: This does not however answer the question of law as to whether these elements are included in claim 1 as essential elements of the monopoly described therein.
- Evidence: `party_position` cue `claimed` at chunk `5040376` offsets `310-317`; context: 15 of his affidavit (TX-1764) he states that:
[t]he skilled chemist would understand from the patent that these criteria such as the 31P NMR chemical shift and the IR are to be employed to distinguish the novel kinetic product […] claimed in the Patent from the prior art, i.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040376` offsets `89-98`; context: 15 of his affidavit (TX-1764) he states that:
[t]he skilled chemist would understand from the patent that these criteria such as the 31P NMR chemical shift and the IR are to be employed to distinguish the novel kinetic product […] claimed in the Patent from the prior art, i.

#### 22183:5:subtheme:13 · paragraphs 132-136

- Raw key terms: `compound, court, patent, apotex, articles, claim, claimed, claims`
- Display key terms: `compound, patent, apotex, articles, claimed, claims`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: compound, patent, apotex, articles, claimed, claims Position/evidence statements: Hunter’s evidence credible in that respect and gave it much weight, but more importantly because this evidence has little impact, if any, on the Court’s conclusion in respect of the construction of claims 1 and 4. Rule/authority context: The only discussion of a new or distinct use of the kinetically controlled compound is in contradistinction with the prior art triaryl phosphite dihalides and it concerns their ability to efficiently halogenate under mil Application context: It is therefore not useful to elaborate further on this. | Gorenstein’s evidence, to the effect that it was well-known and part of the general common knowledge at the relevant time, that 31P NMR shifts were susceptible to variations of several ppm (more than the ±1 ppm advanced  Evidence spans paragraphs 132-136. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040378` offsets `464-469`; context: That said, to avoid any collateral debate, the Court did in fact consider this information to determine if it would have any impact on the construction at issue and concluded that it would not.
- Evidence: `reasoning_application` cue `therefore` at chunk `5040378` offsets `509-518`; context: It is therefore not useful to elaborate further on this.
- Evidence: `issue` cue `issue` at chunk `5040379` offsets `480-485`; context: Hunter had already addressed this very issue in a prior affidavit.
- Evidence: `party_position` cue `claims` at chunk `5040379` offsets `774-780`; context: Hunter’s evidence credible in that respect and gave it much weight, but more importantly because this evidence has little impact, if any, on the Court’s conclusion in respect of the construction of claims 1 and 4.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040379` offsets `102-110`; context: Gorenstein’s evidence, to the effect that it was well-known and part of the general common knowledge at the relevant time, that 31P NMR shifts were susceptible to variations of several ppm (more than the ±1 ppm advanced by some of Apotex’s experts) for a given compound as a result of very many variables,[53] was not proper reply evidence because Dr.
- Evidence: `reasoning_application` cue `because` at chunk `5040379` offsets `429-436`; context: Gorenstein’s evidence, to the effect that it was well-known and part of the general common knowledge at the relevant time, that 31P NMR shifts were susceptible to variations of several ppm (more than the ±1 ppm advanced by some of Apotex’s experts) for a given compound as a result of very many variables,[53] was not proper reply evidence because Dr.
- Evidence: `counterargument_limitation` cue `But` at chunk `5040379` offsets `508-511`; context: But this conclusion is of no moment, given that the Court found Dr.
- Evidence: `governing_rule` cue `under` at chunk `5040382` offsets `433-438`; context: The only discussion of a new or distinct use of the kinetically controlled compound is in contradistinction with the prior art triaryl phosphite dihalides and it concerns their ability to efficiently halogenate under mild conditions both enolic groups and their “utility” in preparing known 3-halocephem antibiotics of the formula described on p.

#### 22183:5:subtheme:14 · paragraphs 137-143

- Raw key terms: `claim, described, patent, process, element, essential, patents, solvent`
- Display key terms: `described, patent, process, element, essential, patents, solvent`
- Argument roles: `counterargument_limitation, disposition, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, issue Display terms: described, patent, process, element, essential, patents, solvent Operative outcome context: Here it is worth pointing out again that one of the main purposes of establishing what is essential in that claim is to determine what element cannot be varied in an allegedly infringing product. Evidence spans paragraphs 137-143. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040383` offsets `57-64`; context: [137] With respect to claim 17, the Court must determine whether or not the particular solvent (an aromatic or halogenated hydrocarbon) is an essential element of the claim.
- Evidence: `issue` cue `question` at chunk `5040384` offsets `463-471`; context: To ask the question is to answer it, which answer is obviously no.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5040384` offsets `301-307`; context: Here it is worth pointing out again that one of the main purposes of establishing what is essential in that claim is to determine what element cannot be varied in an allegedly infringing product.
- Evidence: `disposition` cue `varied` at chunk `5040384` offsets `311-317`; context: Here it is worth pointing out again that one of the main purposes of establishing what is essential in that claim is to determine what element cannot be varied in an allegedly infringing product.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5040385` offsets `240-246`; context: The disclosure cannot be used to rewrite a claim.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040387` offsets `122-125`; context: [141] It may well be that the claim is invalid for lack of novelty or inventiveness or that it is not patentably distinct but that is not to be decided at this stage.

#### 22183:5:subtheme:15 · paragraphs 144-147

- Raw key terms: `patents, process, antibiotics, cephalosporin, cephalosporins, claims, compounds, kukolja`
- Display key terms: `patents, process, antibiotics, cephalosporin, cephalosporins, claims, compounds, kukolja`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: patents, process, antibiotics, cephalosporin, cephalosporins, claims, compounds, kukolja Application context: It is therefore another object of the present invention to provide processes for one step reduction/halogenation conversions of C-7 acylamino cephalosporin sulfoxides to 7-amino cephalosporins or depending on the cephalo Evidence spans paragraphs 144-147. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040390` offsets `294-299`; context: That said, and given that the construction of the claims in the patents raises no substantial issue, the Court will only discuss the ‘536 patent in some detail, for this is the most comprehensive, and will briefly deal with the other two patents.
- Evidence: `reasoning_application` cue `therefore` at chunk `5040393` offsets `1120-1129`; context: It is therefore another object of the present invention to provide processes for one step reduction/halogenation conversions of C-7 acylamino cephalosporin sulfoxides to 7-amino cephalosporins or depending on the cephalosporin starting materials and the amounts of reagents employed C-7 acylamino halogenated cephalosporins or C-7 amino halogenated cephalosporins.

#### Section text

[77] In the said agreement, Lilly U.S. appoints Lilly Canada as its authorized distributor of all Lilly U.S. products in Canada (which includes Ceclor®) and at s. 1.2:
Lilly further grants to Lilly Canada a non-exclusive sublicense (without right of further sublicense except as further granted in writing by Lilly) under the Canadian patent applications and patents listed in Schedule “A”
[…]
to make, have made, use or sell, and/or import Lilly Products whose preparation is covered by the patent applications and patents.

[78] At pp. 8 and 9 of Schedule A, the four Lilly patents at issue here are listed. Normally, it should thus not be contentious that Lilly Canada has proper standing pursuant to subs. 55(1) of the Patent Act, at least in respect of those patents.

[79] Apotex, however, says that on January 1, 1995, the 1991 agreement was amended (TX-110) to delete the various schedules which, according to Mr. Pytynia, was done to avoid having to keep them up to date which was found to be difficult. According to Apotex, the result of this amendment is simply that licences to the Lilly or Shionogi patents were no longer granted to Lilly Canada.

[80] This, according to Apotex, makes particular sense[23] in respect of the Shionogi patents, given that none of the material purchased by Lilly Canada was made by the processes protected thereunder and that Lilly Canada never actually made, purchased or sold any of the actual compounds claimed in the patents in suit. Apotex also discards the impact of the General Supply and Distribution Agreement, filed as TX-112, on the basis that Lilly Canada’s role as distributor appears to be based on an agreement that says nothing about patent rights, nor does it characterize Lilly Canada as an agent and expressly disclaims any other rights flowing between the parties.

[81] The Court agrees with the plaintiff that such an interpretation of the 1991 agreement as amended through time leads to an absurd result and is simply incorrect. The January 1, 1995 agreement expressly states:
WHEREAS the parties desire to maintain the rights, licenses and sublicenses granted by the AGREEMENT while also recognizing that the parties will receive full compensation under the Master Supply and Distribution and Manufacturing or other Agreements.

[82] It is also worth noting that the 1991 agreement was further amended on April 9, 1998 (TX-113) giving Lilly Canada the right to further sub-licence a third party under some of the patents covered by the agreement, in conformity with s. 1.2 of the 1991 agreement. More particularly, the amendment refers to the licence granted under the 1991 agreement for cefaclor and:
grants to Lilly Canada the right to sub-license the following licenses granted to it under the [1991] License Agreement (collectively, the “Licenses”) for cefaclor: (i) licenses granted under patent rights of Lilly U.S. (including, without limitation, the patents listed in Schedule A hereto).
Said schedule made specific reference to three of the Lilly Patents in suit (the only ones missing are the ‘007 and ‘026, the latter having expired by that time).

[83] Having considered all of the evidence, the Court is satisfied that Lilly Canada has properly established its standing based on an express licence from the patentee.

[84] Before concluding on this issue, it is worth quoting a passage from the decision of the Federal Court of Appeal in Apotex Inc. v. Wellcome Foundation Ltd., [2001] 1 F.C. 495 (2000), 262 N.R. 137 (Apotex (2000)), where, after observing that the trial judge, Justice Howard Wetston, had committed no error in his analysis and conclusion, and that based on the unwritten licensing practices of the Glaxo Wellcome Inc. group of companies, Glaxo Wellcome Inc. had an unwritten licence to all the patents held by companies under the control of Glaxo Wellcome Inc. of the United Kingdom, Justice Marshall Rothstein noted, at para. 99, that:
It is perhaps not uncalled for to observe that this is not a case in which the alleged licensee is alone in advancing its claim for the patent infringement. Here, the patentee is also before the Court as a co-Plaintiff supporting the claim of GWI. It is difficult to conceive of what more is necessary to prove the existence of a licence than to have the licensor and licensee both attesting to the validity of the license. Where both the patentee and the person claiming under the patentee are before the Court, are affiliated as being owned by the same parent and have an identity of interest in the litigation – with the patentee supporting the person claiming under the patentee – it is, to say the least, surprising that technical questions of status to sue would be advanced as a defence to infringement.

[85] In fact, Lilly Canada argues that in the past, the Federal Court of Appeal has accepted less than an exclusive or non-exclusive licence as evidence of a right to claim under the patentee. For example, in Signalisation de Montreal Inc. v. Services de Béton Universels Ltée (1992), [1993] 1 F.C. 341 p, 147 N.R. 241, the Court accepted that the plaintiff whose standing was contested was a sales representative of the patentee’s product in Canada. The agreement between it and the patentee did not make any specific reference to the patents or rights of any kind thereunder, leading Justice Paul Rouleau to conclude that the plaintiff had no standing to sue for infringement. In reversing the decision of the trial judge, the Court of Appeal said, among other things, that:
In my view, a person ‘claiming under’ the patentee is a person who derives his rights to use the patented invention, at whatever degree, from the patentee. The right to use an invention is one of the monopoly to which is conferred by a patent. When a breach of that right is asserted by a person who can trace his title in direct line back to the patentee that person is ‘claiming under’ the patentee. It matters not by what technical means the acquisition of the right to use may have taken place. It may be a straightforward assignment or a license. It may, as I have indicated, be a sale of an article embodying the invention. It may also be a lease thereof. What matters is that the claimant asserts a right in the monopoly in that the source of that right may be traced back to the patentee. This is the case with the appellant here.
[Footnotes omitted, para. 24]

[86] There is no doubt here that Lilly Canada derives its rights from the patentee, Lilly U.S.
4. Patent Construction

[87] Before considering the allegations of infringement and invalidity, the Court must construe the claims at issue in this proceeding. The principles of construction are well-established. They are set out in Free World Trust v. Electro Santé Inc. 2000 SCC 66, [2000] 2 S.C.R. 1024 (Free World Trust), and Whirlpool Corp. v. Camco Inc. 2000 SCC 67, [2000] 2 S.C.R. 1067 (Whirlpool). Since those decisions were issued, much has been written by this Court on this topic. Be it sufficient to say that “[t]he key to purposive construction is therefore the identification by the court, with the assistance of the skilled reader, of the particular words and phrases in the claims that describe what the inventor considered to be the “essential” elements of his invention.”[24] As to the further details of what date the claims are to be construed, using what criteria, what resources, through whose eyes and what is made of the resulting construction, the Court adopts and refers to paras. 32-48 of Justice Roger Hughes’ decision in Pfizer Canada Inc. v. Canada (Minister of Health), 2005 FC 1725, 285 F.T.R. 1.

[88] As noted in Shire Biochem Inc. v. Canada (Minister of Health), 2008 FC 538, 328 F.T.R. 123, at para. 21 (Shire), the Court “is not to construe a claim without knowing where disputes between the parties lie.” This is particularly important in cases such as this one, where a large number of claims in eight distinct patents are at issue. As previously noted, all of the patents in this case were issued before October 1, 1989 and are thus subject to the pre October 1, 1989 version of the Patent Act (s. 29 of the post October 1, 1989 version of the Patent Act). They are to be construed as of their respective dates of issuance.

[89] To these more general principles, one should also add that the Court adopts and will apply Justice Denis Pelletier’s statement regarding claim differentiation in Halford v. Seed Hawks Inc., 2004 FC 88, 246 F.T.R. 1 (Halford), affirmed, 2006 FCA 275, 275 D.L.R. (4th) 556 at para. 110, where he quoted the following passage from D.M.I., Inc. v. Deere & Co., 755 F. 2d 1570, 225 U.S.P.Q. (BNA) 236 (U.S. Cir.):
The district Court said ‘As a general rule a limitation cannot be read into a claim to avoid infringement’…Where, as here, the limitation sought to be ‘read into’ a claim already appears in another claim, the rule is far more than ‘general.’ It is fixed. It is long and well established. It enjoys an immutable and universally applicable status comparatively rare among rules of Law.

[90] The Court will also rely on the following passage from The Canadian Law and Practice Relating to Letters Patent for Inventions by Harold G. Fox (Fox) ,[25] which was recently quoted by Justice Snider in Hoffmann-Laroche Ltd. v. Mayne Pharma (Canada) Inc., 2005 FC 814, 41 C.P.R. (4th) 505 (Hoffmann (2005)), at para. 43:
Each part of the specification must be effectively construed and, if it is at all possible, each claim must be construed independently of the others and be given an effective and distinct meaning. The court will not be inclined to construe two claims in a specification as identical, for if one claim bears the same meaning as another it does not bear an effective meaning.
[Emphasis is in the original.]
4.1. Person Skilled in the Art

[91] With respect to the ‘007 patent, although the disclosure discusses, among other things, the utility of the new class of halogenating compounds in the chemistry of cephalosporins, the Court is satisfied that the art to which the patent relates is wider than the chemistry of cephalosporins for the patent covers the kinetic complexes (compound by process claims) and processes to make them. Thus, the Court accepts Apotex’s view that the addressee of the patent would have a Ph.D. in organic or medicinal chemistry with 3-5 years experience in carrying out organic transformations and knowledge of organophosphorus compounds as well as the use of 31P NMR (see para. 119 of Apotex’s memorandum on infringement).

[92] That said, with respect to the Shionogi patents and the Lilly process patents, the Court finds that the addressee is a person with a Ph.D. in organic or medicinal chemistry, with 3-5 years experience in organic synthesis and heterocyclic chemistry, particularly in β-lactam chemistry and penicillin or cephalosporin compounds.[26]

[93] Insofar as the Shionogi patents are concerned, there is little dispute between the parties in that respect even if Dr. Hanessian appears to prefer the word “focus” to describe the experience of the person skilled in the art in the β-lactam antibiotic field. It is apparent that at the relevant time, this kind of chemistry was only conducted by, and of interest to, very specialized research teams. Dr. Baldwin, who was actively working in that field at the time, described those researchers in his testimony.[27]

[94] The views of Apotex’s experts such as Dr. Olah (with respect to the ‘536 patent) and Dr. McClelland (who deals with the Lilly process patents as well as the Shionogi patents)[28] regarding the particular addressee of the process patents appear to be designed to suit the particular characteristics of their own expertise, rather than that of the true addressee. The Court cannot accept the view that the addressee of the Lilly process patents is the same person to whom the ‘007 patent is addressed, but who “would in addition likely be interested in cephalosporin compounds.”[29] That said, this finding will have little impact on the evaluation of their evidence, given that, as mentioned when discussing the weight given to the expert evidence, Apotex’s experts who commented on the Lilly process patents would not meet either description as there is no evidence that any of them had a particular interest in cephalosporins prior to their involvement in this litigation. They have failed to establish in their affidavit the basis on which they are qualified to comment on how a person skilled in the art (hereinafter posita) at the relevant time would construe the patents and what common general knowledge these persons would possess.
4.2. Common General Knowledge (Principles)

[95] During the trial, the Court noted on several occasions that there was little evidence to establish that the numerous publications, patents, applications relied upon by various experts were part of the common general knowledge of the posita at the relevant time. While this was to a certain extent cured through the cross-examinations, it remains that too little attention was given to such matters which are of prime importance, not only to construe the claims, but also to assess the prior art put forth to establish invalidity. This is particularly significant when, like in this case, one is considering older patents issued at a time when a posita did not have the benefit of electronic versions of scientific publications and could not use the internet or other sophisticated research tools to locate relevant information.

[96] The very general statements made recently by the Supreme Court of Canada that “[c]ommon general knowledge means knowledge generally known by persons skilled in the relevant art at the relevant time” (Apotex Inc. v. Sanofi-Synthelabo Canada Inc., 2008 SCC 61, [2008] 3 S.C.R. 265 (Sanofi)) or that a posita is expected to be “reasonably diligent in keeping up with advances in the field to which the patent relates” and that their common knowledge “undergoes continuous evolution and growth” (Whirlpool, para. 74) must be read together with other classic comments that are still applicable.[30]

[97] As noted in General Tire & Rubber Co. v. Firestone Tyre & Rubber Co. Ltd, [1972] RPC 457, [1971] FSR 417 (U.K.C.A.) (General Tire) at pp. 482-483 (of the RPC):
The common general knowledge imputed to such an addressee must, of course, be carefully distinguished from what in patent law is regarded as public knowledge. This distinction is well explained in Halsbury's Law of England, Vol. 29, para. 63. As regards patent specifications it is the somewhat artificial (see per Lord Reid in the Technograph case [1971] F.S.R. 188 at 193) concept of patent law that each and every specification, of the last 50 years, however unlikely to be looked at and in whatever language written, is part of the relevant public knowledge if it is resting anywhere in the shelves of the Patent Office. On the other hand, common general knowledge is a different concept derived from a commonsense approach to the practical question of what would in fact be known to an appropriately skilled addressee – the sort of man, good at his job, that could be found in real life.
The two classes of documents which call for consideration in relation to common general knowledge in the instant case were individual patent specifications and “widely read publications”.
As to the former, it is clear that individual patent specifications and their contents do not normally form part of the relevant common general knowledge, though there may be specifications which are so well known amongst those versed in the art that upon evidence of that state of affairs they form part of such knowledge, and also there may occasionally be particular industries (such as that of colour photography) in which the evidence may show that all specifications form part of the relevant knowledge.
As regards scientific papers generally, it was said by Luxmoore, J. in British Acoustic Films (53 R.P.C. 221 at 250):
“In my judgment it is not sufficient to prove common general knowledge that a particular disclosure is made in an article, or series of articles, in a scientific journal, no matter how wide the circulation of that journal may be, in the absence of any evidence that the disclosure is accepted generally by those who are engaged in the art to which the disclosure relates. A piece of particular knowledge as disclosed in a scientific paper does not become common general knowledge merely because it is widely read, and still less because it is widely circulated. Such a piece of knowledge only becomes general knowledge when it is generally known and accepted without question by the bulk of those who are engaged in the particular art; in other words, when it becomes part of their common stock of knowledge relating to the art.” And a little later, distinguishing between what has been written and what has been used, he said:
"It is certainly difficult to appreciate how the use of something which has in fact never been used in a particular art can ever be held to be common general knowledge in the art."
Those passages have often been quoted, and there has not been cited to us any case in which they have been criticised. We accept them as correctly stating in general the law on this point, though reserving for further consideration whether the words “accepted without question” may not be putting the position rather high: for the purposes of this case we are disposed, without wishing to put forward any full definition, to substitute the words “generally regarded as a good basis for further action.”

[98] In Mahurkar v. Vas-Cath of Canada Ltd. (1988), 16 F.T.R. 48, 18 C.P.R. (3d) 417, Justice Barry Strayer noted, at para. 27:
In reviewing the prior art I have also been persuaded by counsel for the plaintiff that an objective test should be applied to determine whether the hypothetical skilled workman in the art could be reasonably assumed to have knowledge of such prior art. There appears to be adequate authority in the jurisprudence for such a test. No evidence was produced by the defendants to show that the ordinary skilled workman should be assumed to have been aware of all of this prior art. Frankly I find it difficult to believe that several of the items of prior art would have been present to the mind of the ordinary skilled workman in 1981.
[Emphasis added]

[99] Furthermore, as noted by Justice Karen Sharlow in Janssen-Ortho Inc. v. Novopharm Ltd., 2007 FCA 217, 366 N.R. 290, at para. 25 (citing factors developed by Justice Hughes in Janssen-Ortho Inc. v. Novopharm Ltd., 2006 FC 1234, 301 F.T.R. 166 (Janssen-Ortho (2006)):
Not all knowledge is found in print form. On the other hand, not all knowledge that has been written down becomes part of the knowledge that a person of ordinary skill in the art is expected to know or find.

[100] With respect to the proof required to establish common general knowledge, this passage from Simon Thorley et al., Terrell on the Law of Patents, 16th ed. (London: Sweet & Maxwell, 2006) (Terrell), at 6-39 is relevant:
Proof of common knowledge is given by witnesses competent to speak upon the matter, who, to supplement their own recollections, may refer to standard works upon the subject which were published at the time and which were known to them. In order to establish whether something is common general knowledge, the first and most important step is to look at the sources from which the skilled addressee could acquire his information.
The publication at or before the relevant date of other documents such as patent specifications may be to some extent prima facie evidence tending to show that the statements contained in them were part of the common knowledge, but is far from complete proof, as the statements may well have been discredited or forgotten or merely
ignored. Evidence may, however, be given to prove that such statements did become part of the common knowledge.
[Footnotes omitted.]

[101] In the presen

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 22183:6 · paragraphs 148-155

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `dd58bb2316359320236695ae57ba0329a05e8e88cbe06c60c6657fb48e81110b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:6:subtheme:1 · paragraphs 148-153

- Raw key terms: `kinetic, known, patent, present, process, products, antibiotic, chloride`
- Display key terms: `kinetic, known, patent, present, process, products, antibiotic, chloride`
- Argument roles: `reasoning_application`
- Explanation: Observed roles: reasoning_application Display terms: kinetic, known, patent, present, process, products, antibiotic, chloride Application context: 17, it also mentions that, because the reduction process claimed produces Cl or Br as a by-product, “[i]n order to prevent undesirable side reactions between the halogen by-product and the cephalosporin product, a haloge | [153] After providing 96 examples, the 70-page disclosure concludes with a list of 52 claims. Evidence spans paragraphs 148-153. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `5040396` offsets `719-726`; context: 17, it also mentions that, because the reduction process claimed produces Cl or Br as a by-product, “[i]n order to prevent undesirable side reactions between the halogen by-product and the cephalosporin product, a halogen scavenger is used in the reaction mixture to react with or inactivate the chlorine or bromine as it is formed.
- Evidence: `reasoning_application` cue `concludes` at chunk `5040399` offsets `58-67`; context: [153] After providing 96 examples, the 70-page disclosure concludes with a list of 52 claims.

#### 22183:6:subtheme:2 · paragraphs 154-155

- Raw key terms: `acylamino, alkoxy, alkyl, amino, amounts, anhydrous, aspects, below`
- Display key terms: `acylamino, alkoxy, alkyl, amino, amounts, anhydrous, aspects, below`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: acylamino, alkoxy, alkyl, amino, amounts, anhydrous, aspects, below Evidence spans paragraphs 154-155. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040400` offsets `91-96`; context: [154] For the purpose of considering what aspects of the construction of the claims are at issue here, it is sufficient to reproduce claims, 1, 9, 10 and 11.

#### Section text

[148] On p. 5, the disclosure says that the “products formed in the present process are known antibiotic compounds or intermediates thereto.”

[149] As in the ‘007 patent, at p. 9 one can read that:
The dot (●) in the general formula used to represent the kinetically controlled products employed in the present processes is used simply to designate that equivalent amounts of halogen and triaryl phosphite are combined chemically and in a way that can be distinguished from that in the thermodynamically stable derivatives that have been known in the art and which typically have been drawn without the dot [e.g. (PHO)3PCl2]. The exact molecular form of the triaryl phosphite-halogen kinetic complexes […] has not been established definitively […].

[150] The specification then discusses in detail the preparation of the kinetically controlled products, the solvents to be used, the reaction conditions, some properties distinguishing the kinetic product and the thermodynamic product when TPP and Cl are reacted in methylene chloride, including the data found in Table 1 of the patent which is identical to the one discussed earlier in respect of the ‘007 patent. It deals with temperatures and preferred conditions for the formation of the kinetically controlled products and their stabilization in a tertiary amine base as well as details of temperatures for carrying out the processes and chemical reactions claimed in the patent. At p. 17, it also mentions that, because the reduction process claimed produces Cl or Br as a by-product, “[i]n order to prevent undesirable side reactions between the halogen by-product and the cephalosporin product, a halogen scavenger is used in the reaction mixture to react with or inactivate the chlorine or bromine as it is formed.” The term “halogen scavenger” is defined and various such scavengers are discussed. Further details (such as quantities, etc.) as to how to use the kinetic product to effect one or a combination of the reactions claimed are also given.

[151] On p. 35, there is a discussion of how “[t]he triaryl phosphite-halogen complexes utilized as reducing agents in the present process are also potent halogenating agents” and how “[t]he multiple reactivity of the triaryl phosphite-halogen kinetic complexes is exploited in each of several alternate embodiments of the present invention.” At pp. 46-47, the inventor particularly mentions that:
combining the […] reduction/-enol-imino halogenation (Scheme III above [found on p. 36 of the patent]), using a triaryl phosphite-chlorine complex, with subsequent alcoholysis of the resulting imino chloride constitutes an improved method of preparation of 7-amino-3-chloro-3-cephem-4-carboxylic acid esters [7-ACCA] from the corresponding 7-acylamino-3-hydroxy-3-cephem-4-carboxylic acid ester sulfoxides. Prior to this invention the total 3-function conversion was effected either in 3 separate steps, that is reduction, chlorination and side chain cleavage or in two steps, either combining reduction and chlorination (see U.S. Patent No. 4,115,643) with subsequent side chain cleavage or by combining chlorination and side chain cleavage after reduction of the sulfoxide entity, for example, using the method disclosed in U.S. Patent No. 4,044,002. With the discovery of the present process the reduction, chlorination and cleavage conversion can be executed in excellent yields in one reaction vessel without isolation of intermediates.

[152] This is said to be of particular significance, given that the 3-halocephem nucleus ester “can be acylated using conventional acylation techniques and subsequently deesterified to provide known antibiotic compounds [particularly cefaclor]” (p. 47, lines 6-14).

[153] After providing 96 examples, the 70-page disclosure concludes with a list of 52 claims.

[154] For the purpose of considering what aspects of the construction of the claims are at issue here, it is sufficient to reproduce claims, 1, 9, 10 and 11.

[155] Claim 1:
A process for reducing a cephalosporin sulfoxide to the corresponding cephalosporin which comprises reacting said cephalosporin sulfoxide with a triaryl phosphite-halogen complex of the formula
wherein X is Cl or Br, and Z is hydrogen, halo, C1-C4 alkyl or C1-C4 alkoxy, which is the kinetically controlled product of the reaction of equivalent amounts of a triaryl phosphite of the formula
and chlorine or bromine in an inert organic solvent,
in the presence of at least 1 equivalent of a halogen scavenger per equivalent of cephalosporin sulfoxide in a substantially anhydrous inert organic solvent at a temperature of about 30°C. or below;
provided that
(a) about 1.0 to about 1.3 equivalents of the triarylphosphite-halogen complex per equivalent of cephalosporin sulfoxide are employed when the reduction of the sulfoxide group is the only reaction desired,
(b) about 2 to about 3 equivalents of the triarylphosphite-halogen complex per equivalent of cephalosporin sulfoxide are employed when the cephalosporin sulfoxide is a 3-hydroxy cephalosporin sulfoxide and it is desired to simultaneously reduce the sulfoxide and halogenate the 3-position, or the cephalosporin sulfoxide is a 7-acylamino cephalosporin sulfoxide and it is desired to simultaneously reduce the sulfoxide group and convert the acylamino group to an imino halide group, and
(c) about 3 to about 5 equivalents of the triaryl phosphite-halogen complex per equivalent of cephalosporin sulfoxide are employed when the cephalosporin sulfoxide is a 3-hydroxy-7-acylamino cephalosporin sulfoxide and it is desired to simultaneously reduce the sulfoxide group, halogenate the 3-position, and convert the acylamino group to an imino halide group; and further provided that when the cephalosporin sulfoxide has a free amino, hydroxy or carboxy group on the C-7 substituent, those groups are first protected by conventional amino, hydroxy or carboxy protecting groups.[[59]]

## 22183:7 · paragraphs 156-181

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f45bba6f45775b2bb0277c62a571b4f2d363ef223d56e729237c71a186069784`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:7:subtheme:1 · paragraphs 156-163

- Raw key terms: `claim, claims, dependent, described, process, solvent, wherein, cephalosporin`
- Display key terms: `claims, dependent, described, process, solvent, wherein, cephalosporin`
- Argument roles: `counterargument_limitation, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, reasoning_application Display terms: claims, dependent, described, process, solvent, wherein, cephalosporin Application context: There is little doubt that a person skilled in the art with a mind willing to understand would simply disregard this apparent contradiction and would understand claim 11 to apply only to processes wherein X is Cl. | It applies in the context of a two step process (or imino halide formation process). Evidence spans paragraphs 156-163. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040402` offsets `65-70`; context: [156] There is no dispute as to the meaning of this claim and no issue as to whether or not certain elements described therein are essential.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040403` offsets `324-327`; context: Claim 6 is dependent on claim 1 but includes specific halogen scavengers.
- Evidence: `reasoning_application` cue `apply` at chunk `5040405` offsets `379-384`; context: There is little doubt that a person skilled in the art with a mind willing to understand would simply disregard this apparent contradiction and would understand claim 11 to apply only to processes wherein X is Cl.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040406` offsets `238-241`; context: ” Claim 16 is dependent on claims 1 and 15 but further limits the solvent to methylene chloride.
- Evidence: `reasoning_application` cue `applies` at chunk `5040407` offsets `858-865`; context: It applies in the context of a two step process (or imino halide formation process).
- Evidence: `reasoning_application` cue `concludes` at chunk `5040409` offsets `39-48`; context: [163] From all of the above, the Court concludes that the invention is alternative or improved[61] processes as opposed to new processes for transforming cephalosporin sulfoxides.

#### 22183:7:subtheme:2 · paragraphs 164-168

- Raw key terms: `claim, process, chloride, claims, covers, dependent, described, imino`
- Display key terms: `process, chloride, claims, covers, dependent, described, imino`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: process, chloride, claims, covers, dependent, described, imino Evidence spans paragraphs 164-168. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040410` offsets `20-25`; context: [164] The claims at issue here are claims 1 (the only independent claim in the patent), 16, 22 to 27 and 30.
- Evidence: `issue` cue `issue` at chunk `5040411` offsets `281-286`; context: There is only one claim at issue (claim 30) that includes a reference to the various characteristics of the specific kinetically controlled product described therein (all the characteristics found in Table 1, reproduced at p.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040414` offsets `99-102`; context: [168] Claim 22 covers the process of claim 15 where X is Cl while claim 23 covers the same process but where Z is hydrogen and X can be either Cl or Br.

#### 22183:7:subtheme:3 · paragraphs 169-171

- Raw key terms: `claims, patent, process, cephalosporin, claim, construction, contains, court`
- Display key terms: `claims, patent, process, cephalosporin, construction, contains`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: claims, patent, process, cephalosporin, construction, contains Evidence spans paragraphs 169-171. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040415` offsets `193-198`; context: [169] For reasons already given in respect of claims 18 and 34 of the ‘536 patent, the Court does not need to determine the essential elements of claim 30, given that it will not deal with the issue of infringement for such claim.
- Evidence: `issue` cue `issue` at chunk `5040416` offsets `195-200`; context: The claims at issue are dependent claims 2, 7 and 17-20, as well as claim 8.

#### 22183:7:subtheme:4 · paragraphs 172-175

- Raw key terms: `alternative, claim, claimed, claims, complex, dependent, described, kinetic`
- Display key terms: `alternative, claimed, claims, complex, dependent, described, kinetic`
- Argument roles: `issue, party_position`
- Explanation: Observed roles: issue, party_position Display terms: alternative, claimed, claims, complex, dependent, described, kinetic Position/evidence statements: [172] Here again, and for reasons similar to those expressed in respect of the ‘007 patent, the Court does not consider the 31P NMR shift of the TPP and Cl complex (and the other properties described in Table 1) to be an Evidence spans paragraphs 172-175. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040418` offsets `408-413`; context: The only claims at issue that specifically referred to such properties are claim 8 and its dependent claims (one alternative in claims 17-20).
- Evidence: `party_position` cue `claim` at chunk `5040418` offsets `242-247`; context: [172] Here again, and for reasons similar to those expressed in respect of the ‘007 patent, the Court does not consider the 31P NMR shift of the TPP and Cl complex (and the other properties described in Table 1) to be an essential element of claim 1 or its dependent claims that make no reference to such properties when describing the kinetic product to be used in the claimed processes.

#### 22183:7:subtheme:5 · paragraphs 176-181

- Raw key terms: `cephem, cyclization, disclosure, invention, reaction, reactions, ring, acid`
- Display key terms: `cephem, cyclization, disclosure, invention, reaction, reactions, ring, acid`
- Argument roles: `counterargument_limitation, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, party_position, reasoning_application Display terms: cephem, cyclization, disclosure, invention, reaction, reactions, ring, acid Position/evidence statements: He identified four distinct groups of claims and requested amendments. Application context: Also, because the construction of the claims at issue in each of these patents raises little dispute, my review will be brief. | [177] The disclosure starts with the following: “[t]his invention relates to the cyclization to form cephem ring, and the intermediates therefore. Evidence spans paragraphs 176-181. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040422` offsets `327-332`; context: Thereafter, four divisional applications were filed on October 19 and 22, 1979, resulting in the issuance of the four patents at issue.
- Evidence: `party_position` cue `claims` at chunk `5040422` offsets `165-171`; context: He identified four distinct groups of claims and requested amendments.
- Evidence: `reasoning_application` cue `because` at chunk `5040422` offsets `879-886`; context: Also, because the construction of the claims at issue in each of these patents raises little dispute, my review will be brief.
- Evidence: `reasoning_application` cue `therefore` at chunk `5040423` offsets `136-145`; context: [177] The disclosure starts with the following: “[t]his invention relates to the cyclization to form cephem ring, and the intermediates therefore.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040425` offsets `563-566`; context: Another factor which restrict Y to the scope given above is found not in the halogenation but in the following reactions, i.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5040427` offsets `237-246`; context: Therefore, the reactions practically be done as simply as one step reaction (see Examples 2(2) and (3), and Examples 9 to 17 of Part III Cyclization).

#### Section text

[156] There is no dispute as to the meaning of this claim and no issue as to whether or not certain elements described therein are essential. What is clear is that the claim requires the following elements: (i) cephalosporin sulfoxide; (ii) kinetic complex as defined by the formula and the reaction of equivalent amounts of the components described therein; (iii) at least one equivalent of halogen scavenger per equivalent of cephalosporin sulfoxide; (iv) an anhydrous inert organic solvent; (v) a temperature of 30º C or below; and, (vi) that certain quantities of kinetic complex be used depending on how many steps one wishes to perform.

[157] Claim 4 is dependent on claims 1 and 3 and specifies the various substituents on the cephalosporin sulfoxide starting material involved in the reaction. Claim 5 is dependent on claims 1, 2 and 3 and limits the starting material to 3-cephem sulfoxide or 3-exomethylene cepham sulfoxide. Claim 6 is dependent on claim 1 but includes specific halogen scavengers. Claim 8 is dependent on claims 1 or 2 with a more specific temperature range.

[158] Claims 9, 10 and 11 read as follows:
9. The process of claim 1 wherein X is Br.
10. The process of claim 9 wherein Z is hydrogen.
11. The process of claims 1, 2 or 10 wherein X is Cl.

[159] There was an argument raised by Apotex as to how one could construe claim 11, given its reference to claim 10, which itself refers to claim 9, wherein X is Br, whereas according to claim 11, X is Cl. There is little doubt that a person skilled in the art with a mind willing to understand would simply disregard this apparent contradiction and would understand claim 11 to apply only to processes wherein X is Cl. The reference to claim 10 being understood to refer to the process where Z is hydrogen.

[160] Claim 14 is dependent on claims 1, 12, and 13 “wherein the tertiary amine base is pyridine.” Claim 15 is the process of claim 1 where the “solvent is an aromatic or halogenated hydrocarbon.” Claim 16 is dependent on claims 1 and 15 but further limits the solvent to methylene chloride. Claim 17 is dependent on claims 1 and 3 but limits the acyl group R3. Claim 18 covers a one step reduction process only using a TPP and Cl complex having the characteristic of +3.7 ppm signal (again, as per the new convention) and specific infrared data described in the claim. While claim 20 (dependent on claims 1 and 19) covers a two step process (reduction of sulfoxide/halogenation of the enol chlorination) using a TPP and Cl complex as a reagent, claim 21 (dependent on claims 1, 19 or 20) deals again with the two steps described above using the TPP and Cl complex but in the presence of a tertiary base. Claim 22 is another claim dependent on claims 1 and 19 which covers specific halogen scavengers.

[161] Claim 27 is dependent on claims 1, 19, 20, or 25, which deals with situations where X is Cl and it appears to be somewhat redundant in respect of claim 20, which already refers to the use of TPP and Cl complexes. Claim 30 is dependent on the process of claim 1 for specific cephalosporins with the use of pyridine as a tertiary amine base. Claim 31 is dependent on claims 1 and 19 for specific cephalosporins wherein the inert organic solvent is an aromatic or halogenated hydrocarbon. Claim 32 (dependent on claims 19, 20, or 31 and thus, claim 1) further limits the solvent to methylene chloride. Claim 33 is dependent on claims 19 or 20 and claim 1, with a specific acyl group. Claim 34,[60] like claim 18, includes a description of the characteristics of the TPP and Cl complex to be used in the process such as infrared data and 31P NMR shift. It applies in the context of a two step process (or imino halide formation process).

[162] As with the construction of claim 1 in the ‘007 patent, the Court does not find that the 31P NMR shift of +3.7 ppm and presumably the IR data described in Table 1 of the ‘536 patent are essential elements of any of the claims which simply refer to the kinetically controlled product of the reaction of a triaryl phosphite and Cl or Br in an inert organic solvent. This is particularly clear when one considers that claim 18 (dependent on claim 1) only has two distinguishing features – these two properties.

[163] From all of the above, the Court concludes that the invention is alternative or improved[61] processes as opposed to new processes for transforming cephalosporin sulfoxides. It consists mainly in the use of the kinetically controlled product described therein as the reagent and in the fact that said reagent may be used to make up to three reactions or steps in one pot.
4.4.2. The ‘725 Patent

[164] The claims at issue here are claims 1 (the only independent claim in the patent), 16, 22 to 27 and 30. The patent is entitled “Process for Halogenation of β-lactam Compounds”. The ‘725 patent claims a process again requiring the use of the kinetically controlled product of the reaction of equivalent amounts of defined triaryl phosphite and Cl or Br as halogenating agents to convert the 3-hydroxy group at the 3-position of a cephem ring to a halo group as well as a process using the same kinetic product to convert a class of halides to corresponding amino halides (two of the three steps already described in respect of the ’536 patent). Again, on p. 28, the specification notes that “[c]ombining the aforedescribed enol-halogenation/imino-halogenation process, where X is Cl, with subsequent alcoholysis of the resulting imino chloride constitutes an improved method of preparation of the 7-amino-3-chloro-3-cephem-4-carboxylic acid esters”. It is then mentioned, on p. 29, that this is of particular significance given that the 3-halocephem nucleus esters “can be acylated using conventional acylation techniques and subsequently deesterified to provide known antibiotic[s]”, such as cefaclor.

[165] Forty-eight examples are then provided and the patent ends with 30 claims, some of which include the alcoholysis step after the formation of the imino chloride products is complete (see for example claim 27, a process claim dependent on claim 16). There is only one claim at issue (claim 30) that includes a reference to the various characteristics of the specific kinetically controlled product described therein (all the characteristics found in Table 1, reproduced at p. 8, except the half-life).

[166] Claim 1 covers the process described previously using the kinetic complex made in a substantially anhydrous inert organic solvent at a temperature below about 30º C in a prescribed ratio depending if one desires to simply halogenate the enol of formula V (about 1.0 to about 1.3 equivalents of triarylphosphite-halogen complex per equivalent of cephalosporin starting material) or to also carry out imino-halogenation (about 2.0 to about 3.0 equivalents of triarylphosphite-halogen complex per equivalent of cephalosporin starting material). The imino-halogenation must also be carried out “in the presence of about 1.0 to about 1.2 equivalents of a tertiary amine base per equivalent of [kinetic complex].”

[167] Claim 16 is dependent on claim 15 which covers the process of claim 1 for preparing 7-imino halide-3-halo-3-cephem from 7-acylamino-3-hydroxy-3-cephem. Claim 16 covers said process where the kinetic complex is TPP and Cl.

[168] Claim 22 covers the process of claim 15 where X is Cl while claim 23 covers the same process but where Z is hydrogen and X can be either Cl or Br. Claims 24 and 25 depend on claim 15 but limit the type of solvents (aromatic or halogenated hydrocarbon and methylene chloride respectively). Claim 26 is dependent on claim 15 or 16 and specifies the acyl group.

[169] For reasons already given in respect of claims 18 and 34 of the ‘536 patent, the Court does not need to determine the essential elements of claim 30, given that it will not deal with the issue of infringement for such claim. Furthermore, as there are no other disagreements as to the construction of any of the other claims at issue, there is little more to say other than this patent also relates to an alternative or improved process (one or two steps in one pot) where the key feature is the use of the kinetically controlled product of the reaction described therein as reagent.
4.4.3. The ‘468 Patent

[170] This process patent is entitled “Process for Preparation of Penicillin and Cephalosporin Imino-Halides”. The patent contains only two independent
claims, i.e. claims 1 and 8. The claims at issue are dependent claims 2, 7 and 17-20, as well as claim 8.

[171] The disclosure starts by making it clear that the process for “the cleavage of the C-6 or C-7 acylamino group to provide the corresponding C-6 or C-7 amino compounds which are reacylated […]” is known. Thus, the specification states on p. 2 that “an object of the present invention [is] to provide a new process for preparing penicillin and cephalosporin imino halides”, more precisely “to provide a high yielding method of preparing C-6 and C-7 imino halides of penicillin and cephalosporin respectively using novel triaryl phosphite-halogen kinetic complexes”. As this is the last of the three steps covered in the ‘536 patent and of the two steps covered in the ‘725 patent, it contains many similar details about the process itself and about the reagent and its preparation. The disclosure gives thirty examples and ends with 20 claims. The Court will not review the specific wording of any of those claims as there is no dispute between the parties as to their construction.

[172] Here again, and for reasons similar to those expressed in respect of the ‘007 patent, the Court does not consider the 31P NMR shift of the TPP and Cl complex (and the other properties described in Table 1) to be an essential element of claim 1 or its dependent claims that make no reference to such properties when describing the kinetic product to be used in the claimed processes. The only claims at issue that specifically referred to such properties are claim 8 and its dependent claims (one alternative in claims 17-20). As was noted in respect of claims 18 and 34 of the ‘536 patent, even if it is likely that these elements are essential elements of those claims, there was no argument presented in that respect. There is no need to make a judicial determination of this issue.

[173] Claim 7 is dependent on claim 5 or 6 and includes the optional alcoholysis step discussed earlier. Claims 17-20 are all dependent on claim 1 or 8. Claim 17 specifies a particular range of temperature, while claim 18 includes specific types of solvents. Claim 19 is limited to certain types of cephalosporins and claim 20 specifies that the halogenating compound in claim 1 or 8 is stabilized by a tertiary amine base.

[174] Once again, it is quite clear that the invention is an alternative or improved process, whose key feature is the use of the triaryl phosphite-halogen kinetic complex.
4.5. The Shionogi Patents

[175] Initially, Shionogi filed an application on February 9, 1976 to obtain a patent covering all the processes described therein, including the compounds obtained from some of these processes. This first application claimed a priority date based on the filing of the Japanese applications (February/March, 1975).

[176] During the patent examination process, the Patent Examiner noted that the application contained more than one invention. He identified four distinct groups of claims and requested amendments. Thereafter, four divisional applications were filed on October 19 and 22, 1979, resulting in the issuance of the four patents at issue. Thus, they all have an identical disclosure;[62] only their claims vary as each now covers a separate portion of the overall synthetic pathway described in the specification which deals with the overall cyclization of the 6-membered ring structure with the concurrent introduction of an OH substituent at the 3-position of the ring that allows for the subsequent conversion of the substituent to Cl. Except in respect of the ‘026 patent where an issue of construction is raised, the content of such disclosure will only be discussed once. Also, because the construction of the claims at issue in each of these patents raises little dispute, my review will be brief.[63]
4.5.1. Common Disclosure

[177] The disclosure starts with the following: “[t]his invention relates to the cyclization to form cephem ring, and the intermediates therefore. More specifically, it relates to a compound” of the formula:
where “the substituents can be combined to form an azetidinothiazoline bicyclic ring; and their enamine derivatives, and to the processes for the cyclization to form cephem ring
through the said intermediates shown above by the reactions representable by the following reaction scheme”:

[178] At p. 2 it is noted that:
Many trials for synthesizing 3-cephem ring in large scale have been reported, but no factory produce cephalosporins by synthesizing nucleus except for cephalexin.[[64]] This invention provides mild cyclization to form 3-hydroxy-3-cephem compounds through 4-mercaptoazetidinone derivatives.
Efforts to cyclize a type of compounds of the formula (2) or (3) where Y is other than hydroxy or a substituted amino resulted in unsatisfactory results. However, when Y is a group which promotes enolization to form a double bond toward the exo-position, the cyclization took place smoothly to form the objective 3-hydroxy-3-cephem compound (4).
The 3-hydroxy-3-cephem compound (4) is a useful intermediates for synthesizing useful cephem compounds (e.g. recently developed 3-methoxy-7-(α-phenylglycinamido)-3-cephem-4-carboxylic acid [this is cefaclor], 3-chloro-7-(α-phenylglycinamido)-3-cephem-4-carboxylic acid, 3-bromo-7-(2-thienylacetamido)-3-cephem-4-carboxylic acid).

[179] On p. 17, line 23 to p. 18, line 14 of the disclosure, one finds that:
Halogenation of compounds representable by the formula (1) provided Y is other than amino took place smoothly in some cases and with difficulty in other cases. Main difficulty was the position where the halogen atoms was introduced. In other words, the priority of the desired position to other position in the molecule for halogenation was rather small, and it differs from a compound to other. Another factor which restrict Y to the scope given above is found not in the halogenation but in the following reactions, i.e. i) ease of deprotection to give a compound (I) where Y is hydroxy; and ii) ability to cyclize giving the desired cephem compound (4). The compounds representable by formula (1) provided Y is other than hydroxy cyclized unefficiently or insignificantly. From these observations, Y is restricted to include a hydroxy and substituted amino, as is explained above.
The deprotection 2) of the compound (2) can be carried out by treating the compound (2) with aqueous acid for the thiazolino-azetidine compound, and by treating the compound (2) where R is a carbonic acyl, with a Lewis acid.
The decomposition of the azetidinothiazoline compound with an aqueous acid is a new generic reaction for obtaining the 4-mercapto-3-carboxylic acylamino-2-oxoazetidine derivatives according to the reaction scheme
[Depicted on the said page.]

[180] On p. 22 of the disclosure after discussing the reactions claimed in the ‘026 patent,[65] one finds that:
[t]he final product is a 3-hydroxy-3-cephem-4-carboxylic acid or 3-oxocepham-4-carboxylic acid (4). In some instances, the substituents at position 3 or 7 on the cephem ring change during the reaction or working up, and as a result, the corresponding substituents in the starting and produced materials differ each other. If desired, such substituents can be recovered or transformed into other required one by conventional methods. Such cases are also included in the scope of the present invention.

[181] And at p. 23, also concerning the ‘026 patent, that:
The halogenation 1), deprotection 2). and cyclization 3) can be carried out in one pot, namely without isolating intermediates, and even without removing each reaction solvents. Therefore, the reactions practically be done as simply as one step reaction (see Examples 2(2) and (3), and Examples 9 to 17 of Part III Cyclization).
[See also p. 33, lines 6-12.]

## 22183:8 · paragraphs 182-189

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c07f978c45dff24ea97b64996ffa8e3ffb7f80b7ad7409260d86f9a28146545c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:8:subtheme:1 · paragraphs 182-187

- Raw key terms: `claim, claimed, claims, patent, process, processes, cleavage, compound`
- Display key terms: `claimed, claims, patent, process, processes, cleavage, compound`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: claimed, claims, patent, process, processes, cleavage, compound Application context: [184] This patent, like the other three Shionogi patents, is entitled “Cyclization to Form Cephem Ring and Intermediates Therefore” and the disclosure ends with eight claims. Evidence spans paragraphs 182-187. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040429` offsets `370-375`; context: As mentioned, given that sufficiency was not an issue in respect of these patents.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5040430` offsets `121-130`; context: [184] This patent, like the other three Shionogi patents, is entitled “Cyclization to Form Cephem Ring and Intermediates Therefore” and the disclosure ends with eight claims.

#### 22183:8:subtheme:2 · paragraphs 188-189

- Raw key terms: `acylating, acyl, agent, amine, azetidinone, c1-20, c2-12, c2-20`
- Display key terms: `acylating, acyl, agent, amine, azetidinone, c1-20, c2-12, c2-20`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: acylating, acyl, agent, amine, azetidinone, c1-20, c2-12, c2-20 Evidence spans paragraphs 188-189. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040434` offsets `20-25`; context: [188] The claims at issue are 3-4, 8-9, 12, 27, 31 and 37.

#### Section text

[182] The disclosure further indicates that the products of the claimed reactions (except for the 3-hydroxy or 3-oxo) are novel. The lengthy disclosure includes various details relevant to the carrying out of these processes and the preferred modes particularly the
reasoning behind the choice of substituents and other products to be used such as acids, solvents, etc.

[183] One also finds the following statement at p. 33: “this invention provides the higher yielding and simpler process from less expensive penicillins to give valuable key intermediates, the 3-hydroxy-3-cephem-compounds.” Numerous examples are given in respect of each of the processes claimed in the individual patents. As mentioned, given that sufficiency was not an issue in respect of these patents. It is not useful to discuss further these examples or the details given.
4.5.2. The ‘547 Patent

[184] This patent, like the other three Shionogi patents, is entitled “Cyclization to Form Cephem Ring and Intermediates Therefore” and the disclosure ends with eight claims. The claims being pursued at trial are claims 1 (independent claim), 3, 5 and 7-8 (dependent claims).

[185] Those claims are directed to processes[66] for preparing hydroxylated compounds from exomethylene compounds (penicillin derived compound, including the Cooper compound), via oxidative cleavage of the unsaturated bond of the exomethylene group and to the resulting compounds.

[186] Claim 1 can be summarized as follows:
A process for preparing
By subjecting[[67]]
To oxidation followed by cleavage of the thus produced ozonide.

[187] The target compound of claim 1 is the compound claimed in claim 8. Claim 3 is dependent on claims 2 and 1 and relates to the specific use of ozone as the oxidizing material. Claim 5 is dependent on claims 1 and 4, and covers the reduction of the ozonide using specific reducing agents described therein. Claim 7 is dependent on claims 6 and 1 and covers the process of claim 1 in the presence of the specific solvents described therein.
4.5.3. The ‘924 Patent

[188] The claims at issue are 3-4, 8-9, 12, 27, 31 and 37. These claims are generally directed to processes for acylating azetidinone compounds and subsequently forming an enamine azetidinone.

[189] Claim 1 can be simplified as follows. A process for preparing:
by reacting
(Enol form) (Keto form)
with an acylating agent to introduce the C2-12 carbonic acyl, the C1-20 sulfonyl group, and if required, subjecting such compound to a C2-20 disubstituted amine to give the amine compound.

## 22183:9 · paragraphs 190-207

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `010cb3037bbcd62e96fc9350d78f0f6f79076a1b6af8a60a9eee242f8fefec40`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:9:subtheme:1 · paragraphs 190-192

- Raw key terms: `benzyl, claim, claims, compound, covers, dependent, morpholino, patent`
- Display key terms: `benzyl, claims, compound, covers, dependent, morpholino, patent`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: benzyl, claims, compound, covers, dependent, morpholino, patent No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 190-192. This is a deterministic evidence summary, not a legal conclusion.

#### 22183:9:subtheme:2 · paragraphs 193-196

- Raw key terms: `claim, process, compound, compounds, dependent, specific, therein, benzhydryloxy`
- Display key terms: `process, compound, compounds, dependent, specific, therein, benzhydryloxy`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: process, compound, compounds, dependent, specific, therein, benzhydryloxy Evidence spans paragraphs 193-196. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040439` offsets `84-89`; context: [193] Of the 76 claims in this patent, only claims 15, 22, 29, 34, 38 and 58 are at issue.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040439` offsets `247-250`; context: Claim 15 specifies that the halogenating reagent is Cl, Br or iodine, whereas claim 22 is the process of claim 1 but for preparing specific compounds described therein.

#### 22183:9:subtheme:3 · paragraphs 197-203

- Raw key terms: `described, compound, disclosure, represented, acid, claim, claims, cyclization`
- Display key terms: `described, compound, disclosure, represented, acid, claims, cyclization`
- Argument roles: `counterargument_limitation, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, party_position, reasoning_application Display terms: described, compound, disclosure, represented, acid, claims, cyclization Position/evidence statements: [197] There was some dispute between the parties as to the meaning of “Hal” in the two independent claims, 1 and 24. Application context: [198] Having considered the specification as a whole, including the various claims which specify which Hal is covered, the Court concludes that fluorine is included in the halogen (Hal) described in the formulas in claim Evidence spans paragraphs 197-203. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040443` offsets `298-303`; context: Although this is not determinative in any way, given the specific wording of claims 29 and 58, which restrict the definition of “Hal” to a specific halogen other than fluorine, the issue is whether or not claims 1 and 24 would include fluorine as “Hal” in the formula described in the said claims.
- Evidence: `party_position` cue `claims` at chunk `5040443` offsets `99-105`; context: [197] There was some dispute between the parties as to the meaning of “Hal” in the two independent claims, 1 and 24.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040443` offsets `117-125`; context: Although this is not determinative in any way, given the specific wording of claims 29 and 58, which restrict the definition of “Hal” to a specific halogen other than fluorine, the issue is whether or not claims 1 and 24 would include fluorine as “Hal” in the formula described in the said claims.
- Evidence: `reasoning_application` cue `concludes` at chunk `5040444` offsets `129-138`; context: [198] Having considered the specification as a whole, including the various claims which specify which Hal is covered, the Court concludes that fluorine is included in the halogen (Hal) described in the formulas in claims 1 and 24, although it is evident that this is not the preferred halogen and would be so understood by a posita.

#### 22183:9:subtheme:4 · paragraphs 204-207

- Raw key terms: `acid, claim, cyclization, aqueous, compound, compounds, group, hanessian`
- Display key terms: `acid, cyclization, aqueous, compound, compounds, group, hanessian`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue Display terms: acid, cyclization, aqueous, compound, compounds, group, hanessian Operative outcome context: [207] There is no evidence of any allowed R substituent that would not permit cyclization when one considers the “one pot” or “two pot” method or the fact that the removal of the thiol substituent can be done during cycl Evidence spans paragraphs 204-207. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040450` offsets `383-388`; context: He does not raise any difficulty or issue with the construction of this claim.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040452` offsets `147-154`; context: However, he noted that the disclosure contains examples where the R substituent in C or D does not equal H but can be removed effectively in a “one pot” or “two pot”[71] operation through treatment with acid[72] for the purpose of cyclization.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040453` offsets `18-26`; context: [207] There is no evidence of any allowed R substituent that would not permit cyclization when one considers the “one pot” or “two pot” method or the fact that the removal of the thiol substituent can be done during cyclization[73] as a preliminary reaction that will enable the R substituent to become H and thus arriving at compounds A or B.
- Evidence: `disposition` cue `allowed` at chunk `5040453` offsets `34-41`; context: [207] There is no evidence of any allowed R substituent that would not permit cyclization when one considers the “one pot” or “two pot” method or the fact that the removal of the thiol substituent can be done during cyclization[73] as a preliminary reaction that will enable the R substituent to become H and thus arriving at compounds A or B.

#### Section text

[190] Claim 3 is dependent on claims 2 and 1 and covers the process where the selected compound is treated with the sulfonylating reagent mentioned therein. Claim 4 (dependent on claims 2 and 1) covers the process for preparing an acylated or sulfonylated azetidinothiazoline. Claim 8 claims a process of further reacting the acylated or sulfonylated compound of claim 1 with dialkylamine, including piperidino and morpholino. Claim 9 is dependent on claim 8 and deals with a specific substituted amino. Claim 12 (dependent on claims 10, 8 and 1) claims the same process wherein R’ is benzyl, X includes the carboxy protecting group benzyhydryloxy and the substituted amine is morpholino.

[191] Claim 27 covers a compound prepared by the process in claim 1 where specific functional groups are as defined in claim 1, whereas claim 31 covers a compound prepared by the process in claim 4 (which is dependent on claims 2 and 1) where specific functional groups are as defined in claim 4. Claim 37 covers a compound prepared by the process in claim 35 (which is dependent on claims 10, 8 and 1) wherein R’ is benzyl; Y” is a morpholino and, when prepared by the process of claim 12 (dependent on claims 10, 8 and 1), X is a p-nitrobenzyloxy, 2,2,2-trichloroethoxy, benzyloxy.
4.5.4. The ‘132 Patent

[192] The parties have agreed that the halogenation described in the ‘132 patent can generally be referred to as an allylic halogenation.

[193] Of the 76 claims in this patent, only claims 15, 22, 29, 34, 38 and 58 are at issue. Claims 15 and 22 are dependent on claim 1. Claim 15 specifies that the halogenating reagent is Cl, Br or iodine, whereas claim 22 is the process of claim 1 but for preparing specific compounds described therein.

[194] Claim 29 is a compound claim dependent on independent claim 24, which generally describes the compounds made using the process claimed in the previous claims (the formula in claim 24 is the same formula as in claim 1) with the same substituents. Claim 34 is another dependent claim, and, like claim 29, it claims a compound with specific substituents described therein.

[195] Claim 38, which is dependent upon claim 36 (and claim 1), covers a specific process involving treating a compound shown in claim 36 with particular substituents with a halogenating reagent which includes Br. The said compound includes a thiazoline β-lactam, in which the Y is a morpholino, the group R is benzyl and the group X may be benzhydryloxy.

[196] Finally, claim 58 covers the compound according to claim 56 prepared by the process of claim 38, where Y is a morpholino, Hal is a Br and X is one of three compounds listed therein, which includes benzhydryloxy.

[197] There was some dispute between the parties as to the meaning of “Hal” in the two independent claims, 1 and 24. Although this is not determinative in any way, given the specific wording of claims 29 and 58, which restrict the definition of “Hal” to a specific halogen other than fluorine, the issue is whether or not claims 1 and 24 would include fluorine as “Hal” in the formula described in the said claims. The disclosure is quite clear at p. 8 that “[h]alogen which may be represented by Hal in the formulae can be a chlorine, bromine, iodine, or fluorine, in which chlorine and bromine are most preferable.”

[198] Having considered the specification as a whole, including the various claims which specify which Hal is covered, the Court concludes that fluorine is included in the halogen (Hal) described in the formulas in claims 1 and 24, although it is evident that this is not the preferred halogen and would be so understood by a posita.
4.5.5. The ‘026 Patent

[199] The ‘026 patent has five claims. Generally, the claims of this patent relate to the two steps described in the disclosure as the deprotection and cyclization. The claims being pursued at trial were claims 1, 2 and 4. Claim 1 covers a process for preparing a 3-hydroxy-3-cephem[68] (or its keto tautomer) (A and B below) and an azetidinone enol[69] (or its keto tautomer) (C and D below).

[200] Claim 1 reads as follows:
1. A process for preparing a compound represented by the following formulas:
Wherein A and B are, independently, hydrogen, substituted or unsubstituted alkanoyl, substituted or unsubstituted aralkanoyl or substituted or unsubstituted aroyl, which substituents are such as to not affect the cephem ring formation ability of the compound;
X is a hydroxy or carboxy-protecting group;
Hal is halogen; and R is hydrogen, alkoxycarbonyl, cycloalkyl-methoxycarbonyl, aralkoxycarbonyl, aryl-, benzothiazolyl-, furyl-, thienyl-, pyrryl-, oxazolyl-, isoxazolyl-, oxadiazolyl-, oxatriazolyl-, pyrazolyl-, imidazolyl-, triazolyl-, tetrazolyl-, pyridyl-, pyrimidyl-, pyrazinyl-, pyridazinyl-, or triazinylthio each being optionally substituted by halogen, alkyl containing from 1 to 3 carbon atoms, hydroxy, aminomethyl or alkoxy containing from 1 to 3 carbon atoms, which comprises:
1) treating an enamine of a compound represented by the formula:
wherein A, B, R, X and Hal are defined above and the broken line between A and R constitutes a combining together of A, B and R when R and B are hydrogens and A is a carboxylic acyl with a disbustituted amino containing from 2 to 20 carbon atoms, with the action of an aqueous acid.
2) cyclizing a compound of the formula:
wherein, A and B are as defined above by treating a selected compound of above formula x with an acid, base, or solvent, if required in the presence of a catalizer to prepare selected compounds of formulas (A) or (B).

[201] The starting compound described therein (keto compound) can have a thiazoline ring present or not. In the absence of the thiazoline ring, the sulfur group is independently protected with a thiol substituent (R). In the disclosure, at p. 8, R is described as a thiol substituent which is “easily removable without adverse effect on the other part of the molecule prior or during cyclization reaction” (emphasis added). “It is needless to use the isolated starting material (3) for the reaction” (p. 20, lines 27-28, see also p. 33, lines 6-18).

[202] As a first step, the enamine of the keto compound is treated with an aqueous acid, the result of which is the hydrolysis of the disubstituted enamine group (which is in effect the only reaction expressly described therein). Where a thiazoline ring is present, the experts are in agreement that the first step will also open the thiazoline ring leading to the formation of the compounds represented by C or D where R = H. When a thiazoline ring is not present, depending on the substituent used to independently protect the sulfur group, the first step may or may not result in the deprotection of the sulfur substituent. Where it does, the result is the same as above, that is compound C or D where R = H. Where it does not, R is unchanged.

[203] The step described in para. 2 of claim 1 is the cyclization of the compound described therein (C or D where R=H). This takes place by reacting the said compound with either an acid, a base or a solvent (and optionally, a catalyst) to produce the key intermediate described in the disclosure, that is the 3-hydroxy-3-cephem (represented as A or B).

[204] Dr. Hanessian, who is the only expert for Apotex qualified to opine on how a posita would read this claim, simply describes this as reacting an azetidinone-thiazoline with an aqueous acid to form an azetidinone enol, which is further reacted with an acid, base or solvent (with an optional catalyst) to give the 3-hydroxy-3-cephem compound. He does not raise any difficulty or issue with the construction of this claim.

[205] Dr. McClelland, whom has no relevant experience with cephem compounds and cephalosporins, noted that Dr. Hanessian’s was the literal interpretation he had first adopted but he felt this was not accurate on closer examination of the substances. Dr. McClelland testified to the effect that this cyclization step, on his interpretation of the claim, would not take place when R is a group that cannot be removed through treatment with an aqueous acid. This would mean that for such compound the ending material of the claimed process would be the compounds represented as C or D.[70]

[206] Dr. Barrett, in the course of his cross-examination, agreed that in order to cyclize (second reaction covered in claim 1), R had to equal H. However, he noted that the disclosure contains examples where the R substituent in C or D does not equal H but can be removed effectively in a “one pot” or “two pot”[71] operation through treatment with acid[72] for the purpose of cyclization. This would, as shown in example 2. – III, deprotect the sulfur group (with R becoming H) and allow for cyclization to take place (see also p. 18, lines 7-10, p. 19, line 28 to p. 21, line 19 of the disclosure).

[207] There is no evidence of any allowed R substituent that would not permit cyclization when one considers the “one pot” or “two pot” method or the fact that the removal of the thiol substituent can be done during cyclization[73] as a preliminary reaction that will enable the R substituent to become H and thus arriving at compounds A or B.

## 22183:10 · paragraphs 208-216

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `8fa6e47e2fdcdd088a579c1e87aa73e5aef1ed2f240a7054c6b4d3cd41bee849`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:10:subtheme:1 · paragraphs 208-208

- Raw key terms: `based, cases, claimed, compounds, conclude, evidentiary, lead, patent`
- Display key terms: `based, cases, claimed, compounds, conclude, evidentiary, lead, patent`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: based, cases, claimed, compounds, conclude, evidentiary, lead, patent Application context: [208] Based on the evidentiary record before me and on my review of the patent, I conclude that a posita would understand that in all cases the processes claimed in the ‘026 patent can lead to compounds A or B. Evidence spans paragraphs 208-208. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `record` at chunk `5040454` offsets `31-37`; context: [208] Based on the evidentiary record before me and on my review of the patent, I conclude that a posita would understand that in all cases the processes claimed in the ‘026 patent can lead to compounds A or B.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040454` offsets `82-90`; context: [208] Based on the evidentiary record before me and on my review of the patent, I conclude that a posita would understand that in all cases the processes claimed in the ‘026 patent can lead to compounds A or B.

#### 22183:10:subtheme:2 · paragraphs 209-210

- Raw key terms: `reaction, although, apotex, appreciated, argument, because, below, burden`
- Display key terms: `reaction, although, apotex, appreciated, argument, because, below, burden`
- Argument roles: `counterargument_limitation, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, reasoning_application Display terms: reaction, although, apotex, appreciated, argument, because, below, burden Application context: [210] Like the ‘132 patent, the “Hal” is halogen in claim 1 and would be understood by a person skilled in the art to include fluorine because of the definition on p. Evidence spans paragraphs 209-210. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040455` offsets `36-41`; context: [209] In any event, this particular issue of whether or not the product of the reaction will be compounds A or B need only be determined in relation to Apotex’s argument that the Shionogi patents lack subject matter and constitute improper divisional,[74] which for the reasons described below, are rejected.
- Evidence: `reasoning_application` cue `because` at chunk `5040456` offsets `135-142`; context: [210] Like the ‘132 patent, the “Hal” is halogen in claim 1 and would be understood by a person skilled in the art to include fluorine because of the definition on p.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040456` offsets `188-196`; context: Although again it would be readily appreciated by such a person that this is not the preferred halogen to be used (leaving group in the reaction).

#### 22183:10:subtheme:3 · paragraphs 211-215

- Raw key terms: `product, patent, substance, apotex, canada, first, lilly, meaning`
- Display key terms: `product, patent, substance, apotex, first, lilly, meaning`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: product, patent, substance, apotex, first, lilly, meaning Rule/authority context: First, the presumption of infringement arising under s. | [215] In my view, by changing “substance” to “product”, the legislator was simply ensuring that the Canadian provision would be applied in accordance with its obligations pursuant to NAFTA. Application context: [215] In my view, by changing “substance” to “product”, the legislator was simply ensuring that the Canadian provision would be applied in accordance with its obligations pursuant to NAFTA. Operative outcome context: 1 In an action for infringement of a patent granted for a process for obtaining a new product, any product that is the same as the new product shall, in the absence of proof to the contrary, be considered to have been pr Evidence spans paragraphs 211-215. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040457` offsets `214-219`; context: [211] It is not disputed that the Plaintiff must establish on a balance of probabilities that the processes used by Apotex’s suppliers included all of the essential elements of one or more claims of the patents at issue.
- Evidence: `governing_rule` cue `under` at chunk `5040458` offsets `139-144`; context: First, the presumption of infringement arising under s.
- Evidence: `disposition` cue `granted` at chunk `5040458` offsets `243-250`; context: 1 In an action for infringement of a patent granted for a process for obtaining a new product, any product that is the same as the new product shall, in the absence of proof to the contrary, be considered to have been produced by the patented process.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040461` offsets `171-182`; context: [215] In my view, by changing “substance” to “product”, the legislator was simply ensuring that the Canadian provision would be applied in accordance with its obligations pursuant to NAFTA.
- Evidence: `reasoning_application` cue `applied` at chunk `5040461` offsets `128-135`; context: [215] In my view, by changing “substance” to “product”, the legislator was simply ensuring that the Canadian provision would be applied in accordance with its obligations pursuant to NAFTA.

#### 22183:10:subtheme:4 · paragraphs 216-216

- Raw key terms: `apply, cefaclor, claimed, compounds, court, covered, issue, make`
- Display key terms: `apply, cefaclor, claimed, compounds, covered, make`
- Argument roles: `issue, party_position, reasoning_application`
- Explanation: Observed roles: issue, party_position, reasoning_application Display terms: apply, cefaclor, claimed, compounds, covered, make Position/evidence statements: Thus, the Court could only apply the presumption to the making of the new compounds covered in the Shionogi patents or to the products claimed in the ‘007 patent. Application context: Thus, the Court could only apply the presumption to the making of the new compounds covered in the Shionogi patents or to the products claimed in the ‘007 patent. Evidence spans paragraphs 216-216. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040462` offsets `29-34`; context: [216] None of the patents at issue are processes to make cefaclor per se.
- Evidence: `party_position` cue `claimed` at chunk `5040462` offsets `209-216`; context: Thus, the Court could only apply the presumption to the making of the new compounds covered in the Shionogi patents or to the products claimed in the ‘007 patent.
- Evidence: `reasoning_application` cue `apply` at chunk `5040462` offsets `101-106`; context: Thus, the Court could only apply the presumption to the making of the new compounds covered in the Shionogi patents or to the products claimed in the ‘007 patent.

#### Section text

[208] Based on the evidentiary record before me and on my review of the patent, I conclude that a posita would understand that in all cases the processes claimed in the ‘026 patent can lead to compounds A or B.

[209] In any event, this particular issue of whether or not the product of the reaction will be compounds A or B need only be determined in relation to Apotex’s argument that the Shionogi patents lack subject matter and constitute improper divisional,[74] which for the reasons described below, are rejected.

[210] Like the ‘132 patent, the “Hal” is halogen in claim 1 and would be understood by a person skilled in the art to include fluorine because of the definition on p. 8 of the disclosure. Although again it would be readily appreciated by such a person that this is not the preferred halogen to be used (leaving group in the reaction).
5. Infringement
5.1. Burden

[211] It is not disputed that the Plaintiff must establish on a balance of probabilities that the processes used by Apotex’s suppliers included all of the essential elements of one or more claims of the patents at issue.
5.2. Statutory and Common Law Presumptions

[212] Lilly argues that in this particular case, they have the benefit of two presumptions. First, the presumption of infringement arising under s. 55.1 of the Patent Act, which reads as follows:
55.1 In an action for infringement of a patent granted for a process for obtaining a new product, any product that is the same as the new product shall, in the absence of proof to the contrary, be considered to have been produced by the patented process.
[Emphasis added.]
55.1 Dans une action en contrefaçon d’un brevet accordé pour un procédé relatif à un nouveau produit, tout produit qui est identique au nouveau produit est, en l’absence de preuve contraire, réputé avoir été produit par le procédé breveté.

[213] According to Lilly, the word “product” (« produit ») was substituted with the word “substance” (same in French) as a result of an amendment in 1993[75] in order to give effect to para. 1709(11)(a) of the North American Free Trade Agreement Between the Government of Canada, the Government of Mexico and the Government of the United States, 17 December 1992, Can.T.S. 1994 No. 2, 32 I.L.M 289 (NAFTA). Lilly says that the Courts have yet to interpret the meaning of “new product” and it submits that it is a product that has not been sold on the market before. To that end, it refers to various dictionary definitions of the word “product.” According to Lilly, cefaclor, which was first sold in Canada in 1980,[76] was thus not even a product when the Lilly and Shionogi patent applications were filed and they relate to processes for the production of such new products.

[214] The Court cannot accept this argument. As noted by Apotex, the words “product” and “substance” were used interchangeably by the Supreme Court of Canada in (Harvard College v. Canada (Commissioner of Patents), 2002 SCC 76, [2002] 4 S.C.R. 45 (Harvard College (2002)). The word “product” must be given the same meaning as it received throughout the Patent Act. It is used in the definition of “invention.”

[215] In my view, by changing “substance” to “product”, the legislator was simply ensuring that the Canadian provision would be applied in accordance with its obligations pursuant to NAFTA. “Substance” appears to be a more restrictive expression that could, for example, hardly apply to a new hairdryer, whereas the presumption is meant to apply to any new product.

[216] None of the patents at issue are processes to make cefaclor per se. Thus, the Court could only apply the presumption to the making of the new compounds covered in the Shionogi patents or to the products claimed in the ‘007 patent.

## 22183:11 · paragraphs 217-282

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c21077f7972e2c91290948297c1647bc4dd244e119b08ee879e507731f3f4dee`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:11:subtheme:1 · paragraphs 217-223

- Raw key terms: `process, apotex, court, lilly, evidence, presumption, apply, case`
- Display key terms: `process, apotex, lilly, presumption, apply, case`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: process, apotex, lilly, presumption, apply, case Rule/authority context: With respect to the ‘007 patent, for reasons given below under anticipation, the Court finds that these compounds are not new products. | Contrary to what was argued by Apotex, the Court does not believe that it is necessary for a plaintiff to go around the world using means available under various foreign legal systems to obtain the information it can use Application context: [217] As will be discussed, there is no need to apply this presumption to determine the merits of the infringement allegations in respect of the Kyong Bo process and the Shionogi patents. | [218] Lilly also asked the Court to apply the common law presumption discussed in Hoffmann-La Roche Ltd. Evidence spans paragraphs 217-223. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5040463` offsets `245-250`; context: With respect to the ‘007 patent, for reasons given below under anticipation, the Court finds that these compounds are not new products.
- Evidence: `reasoning_application` cue `apply` at chunk `5040463` offsets `48-53`; context: [217] As will be discussed, there is no need to apply this presumption to determine the merits of the infringement allegations in respect of the Kyong Bo process and the Shionogi patents.
- Evidence: `issue` cue `whether` at chunk `5040464` offsets `558-565`; context: ’s assertion that the burden of proving what process was used by its supplier was on Apotex, as:
at common law the rule has always been that when the subject matter of an allegation lies particularly within the knowledge of one of the parties that party must prove it, whether it be an affirmative or negative character.
- Evidence: `reasoning_application` cue `apply` at chunk `5040464` offsets `36-41`; context: [218] Lilly also asked the Court to apply the common law presumption discussed in Hoffmann-La Roche Ltd.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040465` offsets `30-38`; context: [219] In that case, there was evidence that Apotex had written to its supplier, asking it not to voluntarily give information to the plaintiff.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040466` offsets `325-333`; context: Moreover, given the special contractual undertaking of Lupin to assist Apotex (see TX-1656), Apotex was in a much better position to provide admissible and credible evidence as to the process actually used by Lupin.
- Evidence: `governing_rule` cue `under` at chunk `5040467` offsets `593-598`; context: Contrary to what was argued by Apotex, the Court does not believe that it is necessary for a plaintiff to go around the world using means available under various foreign legal systems to obtain the information it can use in a case in order to benefit from the presumption.
- Evidence: `reasoning_application` cue `apply` at chunk `5040467` offsets `373-378`; context: [221] Had I been satisfied that Lilly had taken reasonable steps to obtain this information, for example by pursuing a motion to obtain further information about the process actually used once TX-1656 was produced (after the filing of their initial motion), rather than relying on an undertaking from Apotex to look through their file, the Court would have been willing to apply this presumption given the particular circumstances of this case.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040468` offsets `302-310`; context: [222] Apotex’s failure to advise Lilly and the Court that Lupin was willing to disclose the details of its process subject to proper protection of the confidentiality of the information contained in the said documentation will be discussed further when assessing costs and the admissibility of certain evidence produced to defend the allegation of infringement.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040469` offsets `159-167`; context: [223] Needless to say, even if Lilly cannot benefit from this common law presumption, it can still rely on inferences that can reasonably be made based on the evidence produced to establish certain facts.

#### 22183:11:subtheme:2 · paragraphs 224-226

- Raw key terms: `apotex, cefaclor, imported, least, lupin, used, admit, admitted`
- Display key terms: `apotex, cefaclor, imported, least, lupin, used, admit, admitted`
- Argument roles: `counterargument_limitation, governing_rule`
- Explanation: Observed roles: counterargument_limitation, governing_rule Display terms: apotex, cefaclor, imported, least, lupin, used, admit, admitted Rule/authority context: [225] Apotex admitted[79] that in respect of at least the receiving lot numbers described in the Request to admit, and except for the quantities used for testing and other regulatory purposes pursuant to subs. Evidence spans paragraphs 224-226. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040470` offsets `99-107`; context: Although the exact amount of material received from that supplier will be ascertained through the reference, it appears that Apotex imported at least 8,650kg and maybe as much as 10,000kg of cefaclor made by Lupin.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040471` offsets `192-203`; context: [225] Apotex admitted[79] that in respect of at least the receiving lot numbers described in the Request to admit, and except for the quantities used for testing and other regulatory purposes pursuant to subs.

#### 22183:11:subtheme:3 · paragraphs 227-229

- Raw key terms: `apotex, cefaclor, june, however, infringes, lilly, patents, respect`
- Display key terms: `apotex, cefaclor, june, however, infringes, lilly, patents, respect`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: apotex, cefaclor, june, however, infringes, lilly, patents, respect Position/evidence statements: [228] For reasons that follow, the Court has come to the conclusion that Lilly has established on a balance of probabilities that the cefaclor received by Apotex between May 23, 1997 and June 3, 1998[80] infringes the fo Rule/authority context: This letter and other documents similar to it were all produced under reserve of Lilly’s objection (voir dire). Evidence spans paragraphs 227-229. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040473` offsets `1508-1513`; context: However, there is no indication that it was used at any time before the expiration of all the patents at issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040473` offsets `90-98`; context: Barrett summarizes the various processes described in the evidence filed by the parties.
- Evidence: `governing_rule` cue `under` at chunk `5040473` offsets `1960-1965`; context: This letter and other documents similar to it were all produced under reserve of Lilly’s objection (voir dire).
- Evidence: `counterargument_limitation` cue `However` at chunk `5040473` offsets `1403-1410`; context: However, there is no indication that it was used at any time before the expiration of all the patents at issue.
- Evidence: `party_position` cue `claims` at chunk `5040474` offsets `228-234`; context: [228] For reasons that follow, the Court has come to the conclusion that Lilly has established on a balance of probabilities that the cefaclor received by Apotex between May 23, 1997 and June 3, 1998[80] infringes the following claims in the Lilly patents:
1.

#### 22183:11:subtheme:4 · paragraphs 230-232

- Raw key terms: `apotex, court, evidence, lilly, process, above, arguments, baldwin`
- Display key terms: `apotex, lilly, process, above, arguments, baldwin`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: apotex, lilly, process, above, arguments, baldwin Application context: [232] With respect to Process “B” and Process “C”, there is insufficient evidence for the Court to conclude that either was used to produce the cefaclor shipped to Apotex during the period between May 23, 1997 and Octobe Evidence spans paragraphs 230-232. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040476` offsets `333-338`; context: Having carefully examined the arguments and the evidence referred to in Apotex’s memorandum on infringement (part V) and considering its construction of the claims at issue, the Court is convinced (as was, apparently, Apotex’s in-house counsel back in 1997) that Process “A” infringes the claims referred to above.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040476` offsets `214-222`; context: Having carefully examined the arguments and the evidence referred to in Apotex’s memorandum on infringement (part V) and considering its construction of the claims at issue, the Court is convinced (as was, apparently, Apotex’s in-house counsel back in 1997) that Process “A” infringes the claims referred to above.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040477` offsets `539-547`; context: The Court notes, however, that what was represented to the FDA corroborates at least to some extent the evidence of Lilly’s experts.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040478` offsets `73-81`; context: [232] With respect to Process “B” and Process “C”, there is insufficient evidence for the Court to conclude that either was used to produce the cefaclor shipped to Apotex during the period between May 23, 1997 and October, 1998.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040478` offsets `99-107`; context: [232] With respect to Process “B” and Process “C”, there is insufficient evidence for the Court to conclude that either was used to produce the cefaclor shipped to Apotex during the period between May 23, 1997 and October, 1998.

#### 22183:11:subtheme:5 · paragraphs 233-239

- Raw key terms: `lilly, lupin, apotex, process, evidence, information, minister, order`
- Display key terms: `lilly, lupin, apotex, process, information, order`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: lilly, lupin, apotex, process, information, order Position/evidence statements: Although Lilly specifically refers to Lupin’s undertaking to provide Apotex with information and evidence in respect of the contract process (Process “E”), Lilly did not seek an order compelling Apotex to obtain such inf Rule/authority context: [233] This conclusion remains true whether or not the Court accepts or rejects all or any of the evidence presented under reserve of Lilly’s objections (voir dire). | Although Lilly specifically refers to Lupin’s undertaking to provide Apotex with information and evidence in respect of the contract process (Process “E”), Lilly did not seek an order compelling Apotex to obtain such inf Evidence spans paragraphs 233-239. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040479` offsets `35-42`; context: [233] This conclusion remains true whether or not the Court accepts or rejects all or any of the evidence presented under reserve of Lilly’s objections (voir dire).
- Evidence: `evidence_fact` cue `evidence` at chunk `5040479` offsets `97-105`; context: [233] This conclusion remains true whether or not the Court accepts or rejects all or any of the evidence presented under reserve of Lilly’s objections (voir dire).
- Evidence: `governing_rule` cue `under` at chunk `5040479` offsets `116-121`; context: [233] This conclusion remains true whether or not the Court accepts or rejects all or any of the evidence presented under reserve of Lilly’s objections (voir dire).
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040482` offsets `242-251`; context: [236] On March 10, 2000, Lilly obtained an Order[84] from Justice James Hugessen enjoining Apotex to request from its suppliers and the Minister of Health copies of its suppliers’ DMFs in support of its NDS for Apo-cefaclor and to provide an affidavit stating that it had made such requests.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040483` offsets `52-61`; context: [237] Shortly thereafter, Lilly received an amended affidavit of documents from Apotex which included the 1998 agreement between Apotex and Lupin which expressly stipulates that the said supplier would assist Apotex in providing “information and evidence necessary to show that it has used the process of appendix A”.
- Evidence: `party_position` cue `argue` at chunk `5040484` offsets `520-525`; context: Although Lilly specifically refers to Lupin’s undertaking to provide Apotex with information and evidence in respect of the contract process (Process “E”), Lilly did not seek an order compelling Apotex to obtain such information on the basis that they were, as they now argue, under their possession and control.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040484` offsets `347-355`; context: Although Lilly specifically refers to Lupin’s undertaking to provide Apotex with information and evidence in respect of the contract process (Process “E”), Lilly did not seek an order compelling Apotex to obtain such information on the basis that they were, as they now argue, under their possession and control.
- Evidence: `governing_rule` cue `under` at chunk `5040484` offsets `527-532`; context: Although Lilly specifically refers to Lupin’s undertaking to provide Apotex with information and evidence in respect of the contract process (Process “E”), Lilly did not seek an order compelling Apotex to obtain such information on the basis that they were, as they now argue, under their possession and control.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040484` offsets `250-258`; context: Although Lilly specifically refers to Lupin’s undertaking to provide Apotex with information and evidence in respect of the contract process (Process “E”), Lilly did not seek an order compelling Apotex to obtain such information on the basis that they were, as they now argue, under their possession and control.

#### 22183:11:subtheme:6 · paragraphs 240-242

- Raw key terms: `lilly, lupin, process, used, apotex, essentially, information, letter`
- Display key terms: `lilly, lupin, process, used, apotex, essentially, information, letter`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: lilly, lupin, process, used, apotex, essentially, information, letter Rule/authority context: Thus the letter only enclosed information about the process developed by Lupin pursuant to the March 15, 1998 agreement. Application context: 232 and 248 of the Federal Courts Rules as well as on the evidentiary principle of spoliation because the destruction of Lupin’s manufacturing records[87] and of the files of Mr. Evidence spans paragraphs 240-242. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040486` offsets `87-94`; context: [240] Thereafter, Lilly asked at each new session[85] of its examination for discovery whether Apotex had received any reply to its letter to Lupin and whether it had any information or documentation regarding the process they used.
- Evidence: `issue` cue `issue` at chunk `5040487` offsets `150-155`; context: Lilly raised no particular issue or objection in that respect.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040487` offsets `1244-1253`; context: This letter and its attachments never found their way into Apotex’s affidavit of documents.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040487` offsets `961-972`; context: Thus the letter only enclosed information about the process developed by Lupin pursuant to the March 15, 1998 agreement.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040487` offsets `186-193`; context: However, it appears that at some stage, it took legal steps in the United States to obtain about the Lupin process from Lupin’s American subsidiary.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040488` offsets `112-120`; context: [242] It is in this context that Lilly raised their objections in respect of the admissibility of any viva voce evidence and documentary evidence presented to establish what process was actually used by Lupin after March, 1998 or failed attempts by Lupin to update their Health Canada DMF.
- Evidence: `reasoning_application` cue `because` at chunk `5040488` offsets `420-427`; context: 232 and 248 of the Federal Courts Rules as well as on the evidentiary principle of spoliation because the destruction of Lupin’s manufacturing records[87] and of the files of Mr.

#### 22183:11:subtheme:7 · paragraphs 243-244

- Raw key terms: `according, court, file, leave, lilly, parties, a-20, additional`
- Display key terms: `according, file, leave, lilly, a-20, additional`
- Argument roles: `disposition, evidence_fact, governing_rule`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule Display terms: according, file, leave, lilly, a-20, additional Rule/authority context: When the Court pointed out that Apotex could seek leave pursuant to Rule 232 to file the documents that according to Lilly were under its possession and control, Apotex indicated that it felt no need to do so. Operative outcome context: It is in that context that leave was granted to file additional expert evidence from Dr. Evidence spans paragraphs 243-244. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040489` offsets `148-159`; context: When the Court pointed out that Apotex could seek leave pursuant to Rule 232 to file the documents that according to Lilly were under its possession and control, Apotex indicated that it felt no need to do so.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040490` offsets `116-124`; context: [244] On the other hand, the Court offered[90] to Lilly to suspend the trial so that steps could be taken to obtain evidence in India if necessary.
- Evidence: `disposition` cue `granted` at chunk `5040490` offsets `400-407`; context: It is in that context that leave was granted to file additional expert evidence from Dr.

#### 22183:11:subtheme:8 · paragraphs 245-260

- Raw key terms: `evidence, process, apotex, court, respect, lilly, used, canada`
- Display key terms: `process, apotex, respect, lilly, used`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: process, apotex, respect, lilly, used Rule/authority context: [245] The absence of evidence establishing that either Process “D” or Process “E” infringes on any of the patents at issue means that prior to gaining any knowledge of the July 4 letter or of the evidence presented under | [247] Thus, in my opinion, the main difference for Lilly between the case it thought it had to meet before trial and after it learned of the July 4, 2000 letter and the evidence taken under reserve is that, with respect  Application context: [248] Also, because of Apotex’s failure to disclose the July 4, 2000 letter, Lilly was deprived of an opportunity to change its tactics and to use whatever means were available to obtain or verify what process Lupin effe | [249] Had Lilly lost their action because of this, I would have had no hesitation in awarding them all their costs on a solicitor-client basis as of July 5, 2000. Evidence spans paragraphs 245-260. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040491` offsets `117-122`; context: [245] The absence of evidence establishing that either Process “D” or Process “E” infringes on any of the patents at issue means that prior to gaining any knowledge of the July 4 letter or of the evidence presented under reserve, Lilly’s only argument, with respect to the period after the signing of the March, 1998 contract, was that Process “E” was too inefficient to be commercially viable.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040491` offsets `21-29`; context: [245] The absence of evidence establishing that either Process “D” or Process “E” infringes on any of the patents at issue means that prior to gaining any knowledge of the July 4 letter or of the evidence presented under reserve, Lilly’s only argument, with respect to the period after the signing of the March, 1998 contract, was that Process “E” was too inefficient to be commercially viable.
- Evidence: `governing_rule` cue `under` at chunk `5040491` offsets `215-220`; context: [245] The absence of evidence establishing that either Process “D” or Process “E” infringes on any of the patents at issue means that prior to gaining any knowledge of the July 4 letter or of the evidence presented under reserve, Lilly’s only argument, with respect to the period after the signing of the March, 1998 contract, was that Process “E” was too inefficient to be commercially viable.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040491` offsets `688-695`; context: However, prior to trial, Lilly had not served on Apotex any expert report supporting this position including the inefficiency of Process “E”.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040493` offsets `169-177`; context: [247] Thus, in my opinion, the main difference for Lilly between the case it thought it had to meet before trial and after it learned of the July 4, 2000 letter and the evidence taken under reserve is that, with respect to Process “D”, which Dr.
- Evidence: `governing_rule` cue `under` at chunk `5040493` offsets `184-189`; context: [247] Thus, in my opinion, the main difference for Lilly between the case it thought it had to meet before trial and after it learned of the July 4, 2000 letter and the evidence taken under reserve is that, with respect to Process “D”, which Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040494` offsets `478-486`; context: Also, there is insufficient evidence before me to conclude that the manufacturing documentation, which Mr.
- Evidence: `reasoning_application` cue `because` at chunk `5040494` offsets `12-19`; context: [248] Also, because of Apotex’s failure to disclose the July 4, 2000 letter, Lilly was deprived of an opportunity to change its tactics and to use whatever means were available to obtain or verify what process Lupin effectively used after March, 1998.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040494` offsets `269-276`; context: In that respect, however, the Court notes that given that it had failed to do so after learning of the contract and the undertaking in it, this remains only a possibility rather than a probability.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040495` offsets `248-256`; context: That said, this is not what happens here and I do not believe that all the viva voce evidence objected to is inadmissible.
- Evidence: `reasoning_application` cue `because` at chunk `5040495` offsets `34-41`; context: [249] Had Lilly lost their action because of this, I would have had no hesitation in awarding them all their costs on a solicitor-client basis as of July 5, 2000.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040496` offsets `137-145`; context: [250] In effect, having carefully examined the relevant extracts from the transcripts of the examination for discovery, the Court cannot conclude that Rule 248 applies here.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040497` offsets `104-112`; context: [251] In any event, even if the Court were to apply this rule, it would not mean that all the viva voce evidence of Mr.
- Evidence: `reasoning_application` cue `apply` at chunk `5040497` offsets `46-51`; context: [251] In any event, even if the Court were to apply this rule, it would not mean that all the viva voce evidence of Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040498` offsets `54-62`; context: [252] In my view, it could not be used to exclude the evidence of Mr.
- Evidence: `counterargument_limitation` cue `although` at chunk `5040498` offsets `380-388`; context: It would not exclude his evidence that such process, although not as efficient as Process “A”, still produced a yield than enabled them to fulfill this order.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040499` offsets `122-130`; context: Singh had no personal knowledge of the process actually used by Lupin and even if the documentary evidence they produced was admissible, it would have no probative value in respect of the process used by Lupin during that period.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040501` offsets `329-337`; context: 18 of the said decision:
Spoliation in law does not occur merely because evidence has been destroyed.
- Evidence: `reasoning_application` cue `because` at chunk `5040501` offsets `321-328`; context: 18 of the said decision:
Spoliation in law does not occur merely because evidence has been destroyed.
- Evidence: `counterargument_limitation` cue `although` at chunk `5040501` offsets `824-832`; context: This presumption is rebuttable by other evidence through which the alleged spoliator proves that his actions, although intentional, were not aimed at affecting the litigation, or through which the party either proves his case or repels the case against him.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040502` offsets `673-681`; context: However, in this case I truly do not believe that it would be in the best interests of justice to totally put aside the viva voce evidence of Mr.
- Evidence: `reasoning_application` cue `apply` at chunk `5040502` offsets `53-58`; context: [256] First, it is evident that spoliation could not apply to the destruction of the files of Mr.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040502` offsets `543-550`; context: However, in this case I truly do not believe that it would be in the best interests of justice to totally put aside the viva voce evidence of Mr.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040504` offsets `194-205`; context: [258] Also, Apotex admitted[95] at least in respect of the receiving lot numbers described in the Request to admit, and except for the quantities used for testing and other regulatory purposes, pursuant to subs.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040505` offsets `29-37`; context: [259] Lilly presented expert evidence from Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040506` offsets `34-42`; context: [260] Although there is no direct evidence from a Kyong Bo representative that it indeed used the processes described in Health Canada’s file to produce the material shipped to Apotex at the relevant time, the Court is satisfied that in this case, it can reasonably infer that it was so used.

#### 22183:11:subtheme:9 · paragraphs 261-262

- Raw key terms: `apotex, canada, lilly, respect, acts, allegation, balance, based`
- Display key terms: `apotex, lilly, respect, acts, allegation, balance, based`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: apotex, lilly, respect, acts, allegation, balance, based Evidence spans paragraphs 261-262. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040507` offsets `154-159`; context: [261] Having carefully considered the evidence, I am satisfied that the cefaclor made by Kyong Bo for use by Apotex in Canada infringes all the claims in issue in the ‘547 patent.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040507` offsets `38-46`; context: [261] Having carefully considered the evidence, I am satisfied that the cefaclor made by Kyong Bo for use by Apotex in Canada infringes all the claims in issue in the ‘547 patent.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040507` offsets `414-417`; context: There again, not only are the steps in the patented process used but the starting and resulting compounds claimed (compound by process claims), for example, at claim 58 of the ‘132 patent, are necessarily produced during the Kyong Bo process.

#### 22183:11:subtheme:10 · paragraphs 263-276

- Raw key terms: `apotex, court, canadian, case, process, importation, infringement, patents`
- Display key terms: `apotex, canadian, case, process, importation, infringement, patents`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: apotex, canadian, case, process, importation, infringement, patents Rule/authority context: [270] Apotex’s main defence[101] in respect of the allegations of infringement of the Shionogi patents[102] is that the importation and use of products in Canada which one made abroad by a process patented in Canada cann | [274] Second, Apotex submits that, should the Court feel compelled to follow the general principles set out in the Canadian case law, it should at least restrict their application to cases that meet the statutory limitat Application context: Fouillade that Kyong Bo’s position was that it had the right to use the processes covered by the Shionogi patents because of a licence obtained from Shionogi itself. | , and that the so-called “Saccharin doctrine” was applied by Justice Snider in Pfizer Canada Inc. Evidence spans paragraphs 263-276. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040509` offsets `223-228`; context: In fact, the Court expressed its surprise during the final argument that Apotex’s counsel insisted on pursuing this issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040509` offsets `74-82`; context: [263] With respect to the argument that Kyong Bo was licensed, very scant evidence was produced by Apotex.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040510` offsets `27-36`; context: [264] Apotex relies on the testimony of Dr.
- Evidence: `reasoning_application` cue `because` at chunk `5040510` offsets `204-211`; context: Fouillade that Kyong Bo’s position was that it had the right to use the processes covered by the Shionogi patents because of a licence obtained from Shionogi itself.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040511` offsets `15-23`; context: [265] The only evidence produced as to how Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040514` offsets `90-98`; context: [268] Without ever explaining or referring to the above admission, Apotex argued that the evidence of Dr.
- Evidence: `governing_rule` cue `under` at chunk `5040516` offsets `247-252`; context: [270] Apotex’s main defence[101] in respect of the allegations of infringement of the Shionogi patents[102] is that the importation and use of products in Canada which one made abroad by a process patented in Canada cannot constitute infringement under the Canadian Patent Act.
- Evidence: `reasoning_application` cue `applied` at chunk `5040517` offsets `304-311`; context: , and that the so-called “Saccharin doctrine” was applied by Justice Snider in Pfizer Canada Inc.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040518` offsets `163-171`; context: First, the Court should conclude that Canadian courts were incorrect in following English precedents such as Elmslie v.
- Evidence: `governing_rule` cue `principles` at chunk `5040520` offsets `89-99`; context: [274] Second, Apotex submits that, should the Court feel compelled to follow the general principles set out in the Canadian case law, it should at least restrict their application to cases that meet the statutory limitations now applicable in the United Kingdom Patents Act 1977 (U.

#### 22183:11:subtheme:11 · paragraphs 277-278

- Raw key terms: `canadian, importation, infringement, issue, abroad, address, apotex, appears`
- Display key terms: `canadian, importation, infringement, abroad, address, apotex, appears`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: canadian, importation, infringement, abroad, address, apotex, appears Evidence spans paragraphs 277-278. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040523` offsets `35-40`; context: [277] Given the importance of this issue, and the fact that many of Apotex’s arguments have not been recently canvassed by this Court,[109] I will address the issue of infringement by importation in more detail than may normally be required.
- Evidence: `issue` cue `issue` at chunk `5040524` offsets `84-89`; context: [278] While there appears to be only a dozen or so Canadian cases dealing with this issue, the concept of infringement of a process patent (or process claims) by importation and use or sale in Canada of a product manufactured abroad was first described as a settled question of law more than a century ago.

#### 22183:11:subtheme:12 · paragraphs 279-280

- Raw key terms: `auer, boursier, cases, cited, court, elmslie, heyden, illuminant`
- Display key terms: `auer, boursier, cases, cited, elmslie, heyden, illuminant`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: auer, boursier, cases, cited, elmslie, heyden, illuminant Rule/authority context: 26: Before leaving this question of infringement I ought, perhaps, to refer to the contention made on behalf of the defendant that under any circumstances he would at least be entitled to import for use or sale illuminan Application context: [280] The English cases cited above were again applied two years later by the Divisional Court of the Chancery Division of the Ontario High Court of Justice in Toronto Auer Light Company Limited v. Evidence spans paragraphs 279-280. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040525` offsets `239-247`; context: 26:
Before leaving this question of infringement I ought, perhaps, to refer to the contention made on behalf of the defendant that under any circumstances he would at least be entitled to import for use or sale illuminant appliances made in a foreign country in accordance with the process protected by the plaintiffs' patent.
- Evidence: `governing_rule` cue `under` at chunk `5040525` offsets `346-351`; context: 26:
Before leaving this question of infringement I ought, perhaps, to refer to the contention made on behalf of the defendant that under any circumstances he would at least be entitled to import for use or sale illuminant appliances made in a foreign country in accordance with the process protected by the plaintiffs' patent.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040525` offsets `558-565`; context: With that view, however, I cannot agree.
- Evidence: `reasoning_application` cue `applied` at chunk `5040526` offsets `47-54`; context: [280] The English cases cited above were again applied two years later by the Divisional Court of the Chancery Division of the Ontario High Court of Justice in Toronto Auer Light Company Limited v.

#### 22183:11:subtheme:13 · paragraphs 281-282

- Raw key terms: `anilin, badische, bindschedler, clearly, country, decision, exercising, fabrik`
- Display key terms: `anilin, badische, bindschedler, clearly, country, exercising, fabrik`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: anilin, badische, bindschedler, clearly, country, exercising, fabrik Application context: [281] Given that Apotex says that this reasoning, if applied in Canada, raises an issue of extraterritorial application of our Patent Act, it is also worth mentioning that this very same issue was considered in England m Evidence spans paragraphs 281-282. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040527` offsets `82-87`; context: [281] Given that Apotex says that this reasoning, if applied in Canada, raises an issue of extraterritorial application of our Patent Act, it is also worth mentioning that this very same issue was considered in England more than a hundred years ago.
- Evidence: `reasoning_application` cue `applied` at chunk `5040527` offsets `53-60`; context: [281] Given that Apotex says that this reasoning, if applied in Canada, raises an issue of extraterritorial application of our Patent Act, it is also worth mentioning that this very same issue was considered in England more than a hundred years ago.

#### Section text

[217] As will be discussed, there is no need to apply this presumption to determine the merits of the infringement allegations in respect of the Kyong Bo process and the Shionogi patents. With respect to the ‘007 patent, for reasons given below under anticipation, the Court finds that these compounds are not new products.

[218] Lilly also asked the Court to apply the common law presumption discussed in Hoffmann-La Roche Ltd. v. Apotex Inc. (1983), 41 O.R. (2d) 84, 145 D.L.R. (3d) 270 (H.C.) (aff’d (1984), 47 O.R. (2d) 287, 11 D.L.R. (4th) 320 (C.A.)), in which Justice Walsh confirmed Hoffmann-La Roche Ltd.’s assertion that the burden of proving what process was used by its supplier was on Apotex, as:
at common law the rule has always been that when the subject matter of an allegation lies particularly within the knowledge of one of the parties that party must prove it, whether it be an affirmative or negative character.
[para. 23]

[219] In that case, there was evidence that Apotex had written to its supplier, asking it not to voluntarily give information to the plaintiff. Also, it had manoeuvred to ensure that all process information would be sent to its counsel directly with no copy being sent to Apotex.

[220] According to Lilly, Lupin was actually willing to cooperate in this case and Apotex knew this, but did not disclose it to the plaintiffs or to the Court. Moreover, given the special contractual undertaking of Lupin to assist Apotex (see TX-1656), Apotex was in a much better position to provide admissible and credible evidence as to the process actually used by Lupin.

[221] Had I been satisfied that Lilly had taken reasonable steps to obtain this information, for example by pursuing a motion to obtain further information about the process actually used once TX-1656 was produced (after the filing of their initial motion), rather than relying on an undertaking from Apotex to look through their file, the Court would have been willing to apply this presumption given the particular circumstances of this case. Contrary to what was argued by Apotex, the Court does not believe that it is necessary for a plaintiff to go around the world using means available under various foreign legal systems to obtain the information it can use in a case in order to benefit from the presumption.[77]

[222] Apotex’s failure to advise Lilly and the Court that Lupin was willing to disclose the details of its process subject to proper protection of the confidentiality of the information contained in the said documentation will be discussed further when assessing costs and the admissibility of certain evidence produced to defend the allegation of infringement.

[223] Needless to say, even if Lilly cannot benefit from this common law presumption, it can still rely on inferences that can reasonably be made based on the evidence produced to establish certain facts. This is perfectly in line with the statement made in Whirlpool.[78]
5.3. Lupin Process

[224] Apotex received cefaclor made by Lupin from about May 23, 1997 until at least October, 1998. Although the exact amount of material received from that supplier will be ascertained through the reference, it appears that Apotex imported at least 8,650kg and maybe as much as 10,000kg of cefaclor made by Lupin.

[225] Apotex admitted[79] that in respect of at least the receiving lot numbers described in the Request to admit, and except for the quantities used for testing and other regulatory purposes pursuant to subs. 55.2(1) of the Patent Act, the bulk cefaclor imported from Lupin was used in the manufacture of its Apo-cefaclor product.

[226] In light of the Confidentiality Order issued in this matter, the Court will give few details of the processes used by Apotex’s suppliers.

[227] In his report (E-15), Dr. Barrett summarizes the various processes described in the evidence filed by the parties. I will use his nomenclature:
Process “A” – Process described in Lupin’s filing with Health Canada. It is also described in the material filed by Lupin in 1996 with the Federal Drug Administration (FDA) (U.S. health authority). It is a process whereby cefaclor is synthesized from Pen V acid. The manufacturing process described in letters dated June 21, 1997 and August, 20, 1997 (TX-150; TX-158-TX-159) filed in response to a Health Canada request for clarification in respect of the process used by Lupin to make its 7-ACCA, is similar if not identical to the manufacturing process described by Lupin in its FDA filings in 1996. [Omitted.]
Process “B” – A process described in an update filed by Lupin with the FDA in November, 1997. It is a process whereby cefaclor is synthesized from Pen [omitted]. It appears from TX-167 and TX-168 filed by Dr. Parra of Health Canada, that in June, 1999, Lupin updated its DMF disclosing a process which is similar (if not identical) to the one described in the FDA filing of 1997. According to Dr. Barrett, this process infringes the Shionogi patents.
Process “C” – Another process described in a further update filed by Lupin with the FDA in 2000, which, according to Dr. Barrett uses both the Shionogi and the Lilly processes (a mixture). However, there is no indication that it was used at any time before the expiration of all the patents at issue.
Process “D” – Another process starting from Pen [omitted].
Whereas all those reactions were described simply as step V of Process “A” – they are now shown as step V(a) and step V(b). [Omitted.]
It is described in a document allegedly attached to various versions of a letter dated October 27, 1997 from Mr. Patil to Mr. Singh which was never filed by Mr. Singh with Health Canada. This letter and other documents similar to it were all produced under reserve of Lilly’s objection (voir dire). According to Mr. Satpute, this process (or at least the new process used in 1998) was only used to produce one very large order sometime early in 1998.
Process “E” – A process described in the appendix to the contract for the sale and manufacture of cefaclor between Apotex and Lupin, dated March 15, 1998 (TX-1656). According to this schematic outline, it starts from Pen [omitted].

[228] For reasons that follow, the Court has come to the conclusion that Lilly has established on a balance of probabilities that the cefaclor received by Apotex between May 23, 1997 and June 3, 1998[80] infringes the following claims in the Lilly patents:
1. The ‘007 patent: claims 1, 4, 8-13, and 17-18.
2. The ‘536 patent: claims 1, 4,[81] 11, 14 and 16.
3. The ‘728 patent: claims 1, 15, 16, 20, and 25-27.
4. The ‘468 patent: claims 1, 2 and 7.

[229] However, the plaintiffs have not met their burden in respect of the cefaclor shipped to Apotex as of June 4, 1998.

[230] In respect of the period ending on June 3, 1998, the Court is satisfied that the plaintiffs have established that Lupin was using Process “A”, described above. Having carefully examined the arguments and the evidence referred to in Apotex’s memorandum on infringement (part V) and considering its construction of the claims at issue, the Court is convinced (as was, apparently, Apotex’s in-house counsel back in 1997) that Process “A” infringes the claims referred to above. The Court accepts and prefers the evidence of Drs. Baldwin and Miller who both concluded that Lupin was using a kinetic complex covered by the Lilly patents (as opposed to the thermodynamic product of the reactions between TPP and Cl in dichloromethane (methylene chloride)) to perform the reactions described in the Lupin process.[82]

[231] Although TX-150, TX-158 and TX-159 do not specifically refer to the use of a halogen scavenger, the Court is persuaded that, as explained by Dr. Baldwin,[83] without such scavenger, the reactions in step V of Process “A” could not be successfully performed. As mentioned, the correspondence filed by Lupin with the FDA is not proof that what is represented to be used was effectively used to make the cefaclor shipped to Apotex. The Court notes, however, that what was represented to the FDA corroborates at least to some extent the evidence of Lilly’s experts. Also, once the evidence of Mr. Satpute is considered, it becomes clear that except for the special order made in 1998, there was only one process which started from Pen V acid used at Lupin’s plant in 1997. The Court understands from Mr. Satpute’s evidence that apart from the special order referred to above, the plant used the same processes to fulfill all its orders.

[232] With respect to Process “B” and Process “C”, there is insufficient evidence for the Court to conclude that either was used to produce the cefaclor shipped to Apotex during the period between May 23, 1997 and October, 1998. The arguments presented by Lilly in that respect are purely speculative.

[233] This conclusion remains true whether or not the Court accepts or rejects all or any of the evidence presented under reserve of Lilly’s objections (voir dire).

[234] It is clear that as of March 15, 1998, Lupin had agreed to change the process it had used until then to make cefaclor for Apotex. Apotex’s position has always been that it presumed that Process “E” was used at least after that date.

[235] I do not intend to refer to all the circumstances referred to in the parties’ submissions. I will simply mention some salient points of the background relevant to this debate (voir dire).

[236] On March 10, 2000, Lilly obtained an Order[84] from Justice James Hugessen enjoining Apotex to request from its suppliers and the Minister of Health copies of its suppliers’ DMFs in support of its NDS for Apo-cefaclor and to provide an affidavit stating that it had made such requests. After writing to the Minister and to Lupin, Dr. Sherman swore such an affidavit stating that the Minister had refused to disclose the closed portion of the DMF, that he had received no response from Lupin and that Apotex did not have the ability to compel its suppliers to provide the said information.

[237] Shortly thereafter, Lilly received an amended affidavit of documents from Apotex which included the 1998 agreement between Apotex and Lupin which expressly stipulates that the said supplier would assist Apotex in providing “information and evidence necessary to show that it has used the process of appendix A”.

[238] On May 4, 2000, Lilly filed another motion seeking an order compelling the Minister of Health to produce all portions of Apotex’s NDS relating to Apo-cefaclor including any DMFs relating to Apotex’s suppliers’ processes for preparing cefaclor. Although Lilly specifically refers to Lupin’s undertaking to provide Apotex with information and evidence in respect of the contract process (Process “E”), Lilly did not seek an order compelling Apotex to obtain such information on the basis that they were, as they now argue, under their possession and control.

[239] Upon confirmation that no response had been obtained from Lupin, on July 5, 2000, Justice Hugessen issued an order enjoining the Minister to produce the materials sought by Lilly. As a result, Lilly became aware of the details of Process “A” and of the fact that no update had been filed by Lupin until 1999 (Process “B”).

[240] Thereafter, Lilly asked at each new session[85] of its examination for discovery whether Apotex had received any reply to its letter to Lupin and whether it had any information or documentation regarding the process they used. Dr. Sherman continued to say that he had received no response from Lupin and essentially that he assumed that they were using the contract process (Process “E”).

[241] In 2006 and thereafter, Apotex indicated in their trial chart(s) that they expected to present witnesses from Lupin. Lilly raised no particular issue or objection in that respect. However, it appears that at some stage, it took legal steps in the United States to obtain about the Lupin process from Lupin’s American subsidiary. As a result, and among other things, it obtained copy of a letter from Lupin Laboratories to Ivor Hughes dated July 4, 2000 which indicates that Lupin knew of Lilly’s motion which was set to be heard on July 5, 2000[86] and understood that Lilly was seeking information concerning the process they used to make cefaclor. It also appears that Lupin thought that Apotex was already in possession of the closed portion of their DMF as well as the information exchanged in 1997 about the manufacture of the 7-ACCA (presumably TX-150; TX-158; TX-159). Thus the letter only enclosed information about the process developed by Lupin pursuant to the March 15, 1998 agreement. The letter also includes an authorization to use the said information upon certain conditions which included ensuring that it would be protected by a confidentiality order. This letter and its attachments never found their way into Apotex’s affidavit of documents. They were not filed as exhibits in the trial, although a copy was shown to the Court and Lilly included the letter itself in its written submissions on the voir dire.

[242] It is in this context that Lilly raised their objections in respect of the admissibility of any viva voce evidence and documentary evidence presented to establish what process was actually used by Lupin after March, 1998 or failed attempts by Lupin to update their Health Canada DMF. Essentially, Lilly relies on paras. 232 and 248 of the Federal Courts Rules as well as on the evidentiary principle of spoliation because the destruction of Lupin’s manufacturing records[87] and of the files of Mr. Patil which were lost in a flood in 2005.[88]

[243] As mentioned, the parties filed extensive submissions in respect of these objections. When the Court pointed out that Apotex could seek leave pursuant to Rule 232 to file the documents that according to Lilly were under its possession and control, Apotex indicated that it felt no need to do so.[89]

[244] On the other hand, the Court offered[90] to Lilly to suspend the trial so that steps could be taken to obtain evidence in India if necessary. According to Lilly, this would be useless given that the best evidence – the documentation on the manufacturing of individual batches – were destroyed. Both parties thus remain entrenched in their initial position. It is in that context that leave was granted to file additional expert evidence from Dr. Barrett (E-15) and Dr. Hanessian (A-20).

[245] The absence of evidence establishing that either Process “D” or Process “E” infringes on any of the patents at issue means that prior to gaining any knowledge of the July 4 letter or of the evidence presented under reserve, Lilly’s only argument, with respect to the period after the signing of the March, 1998 contract, was that Process “E” was too inefficient to be commercially viable. Also, it appears that Lilly thought that the Health Canada filing would provide sufficient evidence in this case given that there were, according to them, only two commercially viable processes (the Shionogi and the Lilly patented processes) and Lupin had filed no updates with Health Canada. However, prior to trial, Lilly had not served on Apotex any expert report supporting this position including the inefficiency of Process “E”.[91]

[246] After learning of Process “D” Lilly’s position remained that Process “E” and Process “D” were inefficient and not commercially viable and that there was no time to implement either processes in the timeframe discussed in TX-1671.

[247] Thus, in my opinion, the main difference for Lilly between the case it thought it had to meet before trial and after it learned of the July 4, 2000 letter and the evidence taken under reserve is that, with respect to Process “D”, which Dr. Barrett described as different from Process “E” while Dr. Hanessian described it simply as an improvement over Process “E”,[92] Apotex could now counter Lilly’s allegations of inefficiencies by referring to Lilly’s own NDS documentation submitted to Health Canada on June 23, 1978 to obtain its NOC for Ceclor® (TX-208).

[248] Also, because of Apotex’s failure to disclose the July 4, 2000 letter, Lilly was deprived of an opportunity to change its tactics and to use whatever means were available to obtain or verify what process Lupin effectively used after March, 1998. In that respect, however, the Court notes that given that it had failed to do so after learning of the contract and the undertaking in it, this remains only a possibility rather than a probability. Also, there is insufficient evidence before me to conclude that the manufacturing documentation, which Mr. Satpute could not find in 2008, would have all been available at that time. Evidently, the files of Mr. Patil should have remained intact until 2005.

[249] Had Lilly lost their action because of this, I would have had no hesitation in awarding them all their costs on a solicitor-client basis as of July 5, 2000. That said, this is not what happens here and I do not believe that all the viva voce evidence objected to is inadmissible.

[250] In effect, having carefully examined the relevant extracts from the transcripts of the examination for discovery, the Court cannot conclude that Rule 248 applies here.

[251] In any event, even if the Court were to apply this rule, it would not mean that all the viva voce evidence of Mr. Singh, Mr. Satpute and Mr. Patil would become inadmissible. It could only affect the evidence relating to the details of the process used after March 15, 1998 that differs from Process “E”.

[252] In my view, it could not be used to exclude the evidence of Mr. Satpute that sometime in early in 1998 Lupin took the necessary steps to adopt a process different from Process “A” and Process “B”[93] to fulfill a very large order of the magnitude provided for in the March 15, 1998 contract of which he had no knowledge. It would not exclude his evidence that such process, although not as efficient as Process “A”, still produced a yield than enabled them to fulfill this order. When the Court heard and saw this witness, it found his testimony very credible. The transcript of this evidence was read several times and this only confirmed my first impression. This evidence is, in itself, sufficient to convince me that the shipments made as of June 4, 1998, were not manufactured using Process “A” or Process “B”. There is no need for the Court to determine which process (Process “D” or Process “E”) was used.

[253] Mr. Patil and Mr. Singh had no personal knowledge of the process actually used by Lupin and even if the documentary evidence they produced was admissible, it would have no probative value in respect of the process used by Lupin during that period. In effect, there is a contradiction between some of the correspondence, particularly the October 27, 1997 letter and Mr. Satpute’s testimony, which I prefer. None of this evidence can have, or would have had, an impact on my findings.

[254] In the circumstances, there is no need to discuss further the application of paras. 232 and 248 of the Rules.

[255] Finally, with respect to spoliation and the residual discretion of the Court in such matters, the law is well summarized by the Alberta Court of Appeal in McDougall v. Black & Decker Canada Inc., 2008 ABCA 353, 62 C.P.C. (6th) 293. As noted at para. 18 of the said decision:
Spoliation in law does not occur merely because evidence has been destroyed. Rather, it occurs where a party has intentionally destroyed evidence relevant to ongoing or contemplated litigation in circumstances where a reasonable inference can be drawn that the evidence was destroyed to affect the litigation. Once this is demonstrated, a presumption arises that the evidence would have been unfavourable to the party destroying it. This presumption is rebuttable by other evidence through which the alleged spoliator proves that his actions, although intentional, were not aimed at affecting the litigation, or through which the party either proves his case or repels th

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 22183:12 · paragraphs 283-290

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `54e5955abb868487c2a8c5a1b6151653fa0ea7544d2543cfabcec6cf7156bb64`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:12:subtheme:1 · paragraphs 283-283

- Raw key terms: `abroad, acts, against, applied, basis, bought, cannot, case`
- Display key terms: `abroad, acts, against, applied, basis, bought, cannot, case`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: abroad, acts, against, applied, basis, bought, cannot, case Rule/authority context: The Court refused to do so, on the basis that the principles laid down in Elmslie and Von Heyden and applied in Saccharin could not be extended to a case where the defendant had neither imported into nor sold in England  Application context: The Court refused to do so, on the basis that the principles laid down in Elmslie and Von Heyden and applied in Saccharin could not be extended to a case where the defendant had neither imported into nor sold in England  Evidence spans paragraphs 283-283. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `principles` at chunk `5040529` offsets `534-544`; context: The Court refused to do so, on the basis that the principles laid down in Elmslie and Von Heyden and applied in Saccharin could not be extended to a case where the defendant had neither imported into nor sold in England the product made abroad using the patented process.
- Evidence: `reasoning_application` cue `applied` at chunk `5040529` offsets `585-592`; context: The Court refused to do so, on the basis that the principles laid down in Elmslie and Von Heyden and applied in Saccharin could not be extended to a case where the defendant had neither imported into nor sold in England the product made abroad using the patented process.

#### 22183:12:subtheme:2 · paragraphs 284-285

- Raw key terms: `english, principle, abroad, accordance, acts, albeit, apotex, appellant`
- Display key terms: `english, principle, abroad, accordance, acts, albeit, apotex, appellant`
- Argument roles: `counterargument_limitation, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, reasoning_application Display terms: english, principle, abroad, accordance, acts, albeit, apotex, appellant Application context: ), simply because it was referred to in Monsanto Canada Inc. Evidence spans paragraphs 284-285. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040530` offsets `146-153`; context: Contrary to Apotex’s assertion, however, they focused only on the acts taking place within their jurisdiction to determine if there was any conduct which constituted infringement.
- Evidence: `reasoning_application` cue `because` at chunk `5040531` offsets `181-188`; context: ), simply because it was referred to in Monsanto Canada Inc.

#### 22183:12:subtheme:3 · paragraphs 286-290

- Raw key terms: `case, decision, house, importation, lords, patents, ampicillin, apotex`
- Display key terms: `case, house, importation, lords, patents, ampicillin, apotex`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: case, house, importation, lords, patents, ampicillin, apotex Rule/authority context: The latter is probably the last decision to apply the principles at issue given that, shortly after it was rendered, the Patents Act, 1977 was adopted. Application context: The latter is probably the last decision to apply the principles at issue given that, shortly after it was rendered, the Patents Act, 1977 was adopted. | [288] The reasoning in this case is, in my view, particularly instructive because the defendants vigorously contested that the Saccharin case was still good law in light of the amendments to the Patents Act, 1949 (U. Evidence spans paragraphs 286-290. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040532` offsets `331-336`; context: The latter is probably the last decision to apply the principles at issue given that, shortly after it was rendered, the Patents Act, 1977 was adopted.
- Evidence: `governing_rule` cue `principles` at chunk `5040532` offsets `317-327`; context: The latter is probably the last decision to apply the principles at issue given that, shortly after it was rendered, the Patents Act, 1977 was adopted.
- Evidence: `reasoning_application` cue `apply` at chunk `5040532` offsets `307-312`; context: The latter is probably the last decision to apply the principles at issue given that, shortly after it was rendered, the Patents Act, 1977 was adopted.
- Evidence: `reasoning_application` cue `because` at chunk `5040534` offsets `74-81`; context: [288] The reasoning in this case is, in my view, particularly instructive because the defendants vigorously contested that the Saccharin case was still good law in light of the amendments to the Patents Act, 1949 (U.
- Evidence: `reasoning_application` cue `because` at chunk `5040536` offsets `49-56`; context: [290] Apotex noted that this case is not helpful because the Courts were really dealing with a colourable imitation of the patented product, ampicillin.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040536` offsets `391-398`; context: However, this was treated by all judges as a separate ground.

#### Section text

[283] As the Saccharin case is at the center of the debate, it is of interest to mention the decision in Saccharin Corporation v. Reitmeyer & Co., [1900] 2 Ch. 659, (1900) 17 R.P.C. 606. There, the patent owner, who had successfully obtained a declaration of infringement against the importer in the first Saccharin case, was seeking a similar declaration against the English commission merchant who had originally bought the saccharin in Germany and sold it to the English importer. The Court refused to do so, on the basis that the principles laid down in Elmslie and Von Heyden and applied in Saccharin could not be extended to a case where the defendant had neither imported into nor sold in England the product made abroad using the patented process. Justice Cozens-Hardy reached this conclusion on the basis that, “[n]ow, it is plain that a Patent is of local force. It cannot and does not profess to interfere with or control acts done abroad […]” (p. 611, lines 40-41 of the R.P.C.).

[284] It could not be clearer that English Courts felt bound by the very principle Apotex seeks to now rely upon. Contrary to Apotex’s assertion, however, they focused only on the acts taking place within their jurisdiction to determine if there was any conduct which constituted infringement.

[285] There are three other English decisions that must be briefly mentioned. The first, Pfizer Corporation v. Ministry of Health, [1965] AC 512, [1965] 1 All ER 450 (H.L.), simply because it was referred to in Monsanto Canada Inc. (albeit in a different context) and indicates that Lord Upjohn, after re-examining the validity of the doctrine both “on principle and on authority”, concluded:
[…] where an importer imports into this country, articles manufactured abroad but in accordance with a British patent for the purpose of distributing them and selling them in this country, he quite plainly is using and exercising the patent, and he thereby infringes the appellant’s patent […]
[p. 469(D) of the All ER]

[286] The other two decisions are Beecham Group Limited v. Bristol Laboratories Limited and another, [1967] RPC 406, [1967] FSR 283 (CA.) and the final decision on the merits rendered nearly ten years later by the House of Lords ([1978] RPC 153) (Beecham Group). The latter is probably the last decision to apply the principles at issue given that, shortly after it was rendered, the Patents Act, 1977 was adopted.

[287] The English Court of Appeal (Lord Justice Alfred Thompson Denning writing the main reasons) reversed the decision of the High Court judge and issued an interlocutory injunction to prevent the importation of hetacillin. In the Court of Appeal’s view, the plaintiff had established a prima facie case of infringement of his English patents protecting, in particular, the process for making ampicillin, an intermediate compound which was then transformed into hetacillin by the addition of acetone (see particularly the concurring reasons of Lord Justice Russell, at p. 417 of the RPC).

[288] The reasoning in this case is, in my view, particularly instructive because the defendants vigorously contested that the Saccharin case was still good law in light of the amendments to the Patents Act, 1949 (U.K.), 12, 13 & 14 Geo. VI, c. 87, which clearly required that the claims define the scope of the invention. Thus, the defendants argued, only patents claiming a product could be infringed by importation of such products into England. As in the present case, it was also argued that the “Saccharin doctrine”, if followed, had the potential to yield extraordinary results[111] and uncertainty, leaving competitors uncertain as to what they are entitled to do.

[289] These arguments are remarkably similar to those made before me by Apotex; they were ultimately rejected on the merits, by Justice Falconer in the first instance, by the Court of Appeal and by the House of Lords.

[290] Apotex noted that this case is not helpful because the Courts were really dealing with a colourable imitation of the patented product, ampicillin. That is true. The plaintiffs in Beecham Group also raised an argument based on the fact that hetacillin was a colourable imitation because once it was used by a potential patient as an antibiotic it reverted to ampicillin in the stomach. However, this was treated by all judges as a separate ground. In the decision of the House of Lords, Lord Diplock also made it clear that the doctrine of infringement by importation, applied in Saccharin, was not an extension of the pith and marrow doctrine. It was a distinct concept standing on its own (see p. 200-201).

## 22183:13 · paragraphs 291-293

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e9743ecb77fe0daa87f6b5a190d232da6715cbafc07529de36cb495be5e2c0d6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:13:subtheme:1 · paragraphs 291-293

- Raw key terms: `diplock, lord, patent, abroad, article, claimed, country, done`
- Display key terms: `diplock, lord, patent, abroad, article, claimed, country, done`
- Argument roles: `counterargument_limitation, disposition, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, reasoning_application Display terms: diplock, lord, patent, abroad, article, claimed, country, done Rule/authority context: [291] The House of Lords also confirmed that the Patents Act, 1949 did not contain any changes that justified setting aside the principles applied in Saccharin and Wilderman. Application context: [291] The House of Lords also confirmed that the Patents Act, 1949 did not contain any changes that justified setting aside the principles applied in Saccharin and Wilderman. Operative outcome context: 199: The monopoly granted by a patent is limited territorially to the United Kingdom and the Isle of Man and the corresponding prohibition is limited to acts done within those territorial limits. Evidence spans paragraphs 291-293. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `principles` at chunk `5040537` offsets `128-138`; context: [291] The House of Lords also confirmed that the Patents Act, 1949 did not contain any changes that justified setting aside the principles applied in Saccharin and Wilderman.
- Evidence: `reasoning_application` cue `applied` at chunk `5040537` offsets `139-146`; context: [291] The House of Lords also confirmed that the Patents Act, 1949 did not contain any changes that justified setting aside the principles applied in Saccharin and Wilderman.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040538` offsets `343-350`; context: The wide words of the grant and prohibition[[112]] were, however, treated as entitling the patentee to prohibit the obtaining from abroad and selling in this country an article manufactured abroad by the patented process, even though the article was of a kind that was not new and consequently of itself could not be, and was not, claimed as an invention in the specification.
- Evidence: `disposition` cue `granted` at chunk `5040538` offsets `108-115`; context: 199:
The monopoly granted by a patent is limited territorially to the United Kingdom and the Isle of Man and the corresponding prohibition is limited to acts done within those territorial limits.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040539` offsets `798-805`; context: This extreme extension of the doctrine was, however, rejected by Tomlin, J.

#### Section text

[291] The House of Lords also confirmed that the Patents Act, 1949 did not contain any changes that justified setting aside the principles applied in Saccharin and Wilderman. Lord Diplock noted that the need to describe and ascertain the nature of the invention in the letters patent was made a condition of the grant from 1700 onwards. To end the specification with a distinct statement of the invention claimed was made statutory in 1883, at which point Lord Diplock noted the practice to have already become widespread (p.198).

[292] Lord Diplock describes the reasoning behind Elmslie and Von Heyden as follows at p. 199:
The monopoly granted by a patent is limited territorially to the United Kingdom and the Isle of Man and the corresponding prohibition is limited to acts done within those territorial limits. The wide words of the grant and prohibition[[112]] were, however, treated as entitling the patentee to prohibit the obtaining from abroad and selling in this country an article manufactured abroad by the patented process, even though the article was of a kind that was not new and consequently of itself could not be, and was not, claimed as an invention in the specification.
[Emphasis added.]

[293] With respect to the extraordinary results which would flow from the unbridled application of the “Saccharin doctrine”, it appears that the House of Lords, like Lord Justice Denning in 1967, found comfort in the application of the limitations set out in Wilderman. Lord Diplock explained, at p. 201:
My Lords, if logic were the sole guide to the law of patents such an extension of the doctrine of infringing importation might be difficult to resist. In effect it would mean that in respect of any article sold in this country, anything done in the course of its manufacture which would constitute an infringement of a United Kingdom patent if done in this country would constitute a like infringement if before importation it had been done abroad. This extreme extension of the doctrine was, however, rejected by Tomlin, J. in Wilderman v. F.W. Berk & Co. Ltd. (1925) 42 R.P.C. 79, where in relation to a claim for the infringing importation of an article in the course of whose manufacture abroad a patented apparatus had been used, he expressed the view that the use of the patented process or apparatus must have played an important part in the manufacture of the imported article.

## 22183:14 · paragraphs 294-303

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3fbdd5ef441d31f9b5a4b5d9abb19ad3bd85264b252f4e7b69f8eb6e76ac0b1c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:14:subtheme:1 · paragraphs 294-295

- Raw key terms: `appeal, claims, court, product, pure, abroad, accepted, allow`
- Display key terms: `claims, product, pure, abroad, accepted, allow`
- Argument roles: `counterargument_limitation, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, party_position, reasoning_application Display terms: claims, product, pure, abroad, accepted, allow Position/evidence statements: 1 (Hoffmann-LaRoche), the Supreme Court of Canada issued its well-known decision that, contrary to what was then the English practice, no product by process claim could be issued in Canada for a known product, even thoug Rule/authority context: [295] Turning back now to Canadian jurisprudence on the matter. Application context: [294] Finally, it is interesting to note that in that case, the House of Lords refused to decide if the doctrine should also apply to pure product claims, which extension had been accepted by the trial judge and the Cour Evidence spans paragraphs 294-295. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `apply` at chunk `5040540` offsets `125-130`; context: [294] Finally, it is interesting to note that in that case, the House of Lords refused to decide if the doctrine should also apply to pure product claims, which extension had been accepted by the trial judge and the Court of Appeal.
- Evidence: `issue` cue `issue` at chunk `5040541` offsets `616-621`; context: As this involved an appeal in respect of a decision of the Commissioner of Patents refusing to allow the proposed product by process claims, the Supreme Court of Canada was not required to discuss the issue of infringement of a pure process patent or process claims, by the importation of a product (not covered by the patent) made abroad using the patented process.
- Evidence: `party_position` cue `claim` at chunk `5040541` offsets `322-327`; context: 1 (Hoffmann-LaRoche), the Supreme Court of Canada issued its well-known decision that, contrary to what was then the English practice, no product by process claim could be issued in Canada for a known product, even though the process itself was new.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5040541` offsets `35-48`; context: [295] Turning back now to Canadian jurisprudence on the matter.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `5040541` offsets `782-794`; context: Nevertheless, while dealing with the main issue before it, Chief Justice Patrick Kerwin, writing for the majority, considered the decision of the Court of Appeal of England and Wales in Von Heyden, as well as two Canadian decisions, Auer and Toronto Auer Light and expressly noted that “there seems to be no reason to doubt the correctness of these decisions.

#### 22183:14:subtheme:2 · paragraphs 296-299

- Raw key terms: `canadian, legislation, patent, above, cases, concluded, court, courts`
- Display key terms: `canadian, legislation, patent, above, cases, concluded, courts`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue Display terms: canadian, legislation, patent, above, cases, concluded, courts Rule/authority context: legislation, Apotex’s argument that the distinctions between Canadian and British law should render British jurisprudence of little assistance on this issue is unpersuasive. | 13: I have been able to discover no such difference between the ambit of an English patent for an invention and the ambit of the monopoly granted under the Canadian Patent Act as would warrant reaching a conclusion when  Operative outcome context: 13: I have been able to discover no such difference between the ambit of an English patent for an invention and the ambit of the monopoly granted under the Canadian Patent Act as would warrant reaching a conclusion when  Evidence spans paragraphs 296-299. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040542` offsets `292-297`; context: legislation, Apotex’s argument that the distinctions between Canadian and British law should render British jurisprudence of little assistance on this issue is unpersuasive.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5040542` offsets `249-262`; context: legislation, Apotex’s argument that the distinctions between Canadian and British law should render British jurisprudence of little assistance on this issue is unpersuasive.
- Evidence: `counterargument_limitation` cue `notwithstanding` at chunk `5040542` offsets `328-343`; context: Put plainly, notwithstanding the differences between Canadian and British patent laws, our Courts continue to look to British jurisprudence to inform the analysis of our intellectual property laws.
- Evidence: `issue` cue `question` at chunk `5040543` offsets `629-637`; context: 13:
I have been able to discover no such difference between the ambit of an English patent for an invention and the ambit of the monopoly granted under the Canadian Patent Act as would warrant reaching a conclusion when this question arises under the Canadian Act different from that reached in respect of an English patent.
- Evidence: `governing_rule` cue `under` at chunk `5040543` offsets `550-555`; context: 13:
I have been able to discover no such difference between the ambit of an English patent for an invention and the ambit of the monopoly granted under the Canadian Patent Act as would warrant reaching a conclusion when this question arises under the Canadian Act different from that reached in respect of an English patent.
- Evidence: `disposition` cue `granted` at chunk `5040543` offsets `542-549`; context: 13:
I have been able to discover no such difference between the ambit of an English patent for an invention and the ambit of the monopoly granted under the Canadian Patent Act as would warrant reaching a conclusion when this question arises under the Canadian Act different from that reached in respect of an English patent.
- Evidence: `governing_rule` cue `under` at chunk `5040544` offsets `133-138`; context: [298] The learned judge also noted that he was unable to ascertain any relevant difference between the Canadian legislation that was under consideration in Auer and he concluded based on comity that he should follow Auer, noting that it had also been the subject of the obiter mentioned above in Hoffmann-LaRoche.
- Evidence: `counterargument_limitation` cue `although` at chunk `5040545` offsets `321-329`; context: Also, although there is a reference to the Badische Anilin und Soda Fabrik decisions (see above) in the editorial note of the Canadian Patent Reporter for Rhone-Poulenc, at 194, it does not appear that these cases were brought to the attention of the Court.

#### 22183:14:subtheme:3 · paragraphs 300-302

- Raw key terms: `canada, decision, court, gilbert, importation, issue, justice, made`
- Display key terms: `gilbert, importation, justice, made`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: gilbert, importation, justice, made Application context: In that case, the Court had to determine if the “Saccharin doctrine” should be applied to the importation of tetracycline in Canada. Evidence spans paragraphs 300-302. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040546` offsets `281-286`; context: This particular product was not covered by the patent at issue but it was made using a patented process for making chlortetracycline,[115] to which a dechlorination method was then applied to obtain tetracycline.
- Evidence: `evidence_fact` cue `found that` at chunk `5040546` offsets `867-877`; context: But having expressed some concern in respect of the application of the doctrine to processes that are merely incidental, the learned judge did apply the “Saccharin doctrine”, as he found that the product used as an intermediary was of importance.
- Evidence: `reasoning_application` cue `applied` at chunk `5040546` offsets `170-177`; context: In that case, the Court had to determine if the “Saccharin doctrine” should be applied to the importation of tetracycline in Canada.
- Evidence: `issue` cue `issue` at chunk `5040547` offsets `122-127`; context: [301] Between 1966 and 1991, it appears that the Exchequer Court of Canada and the Federal Court of Canada considered the issue quite settled.

#### 22183:14:subtheme:4 · paragraphs 303-303

- Raw key terms: `absence, aktiengesellschaft, although, another, arguments, bruning, canada, canadian`
- Display key terms: `absence, aktiengesellschaft, although, another, arguments, bruning, canadian`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: absence, aktiengesellschaft, although, another, arguments, bruning, canadian Application context: ” but concludes that he does not “see any reasonable grounds for so doing. Evidence spans paragraphs 303-303. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040549` offsets `224-229`; context: (2d) 105, Justice Frank Collier again faced the same issue, where the Canadian defendant imported isohalothane, a product made in the United States by a process patented in Canada.
- Evidence: `reasoning_application` cue `concludes` at chunk `5040549` offsets `723-732`; context: ” but concludes that he does not “see any reasonable grounds for so doing.

#### Section text

[294] Finally, it is interesting to note that in that case, the House of Lords refused to decide if the doctrine should also apply to pure product claims, which extension had been accepted by the trial judge and the Court of Appeal. The Court felt that it did not have the benefit of full arguments (see also the reasons of Lord Simon of Glaisdale on this point, p. 204).

[295] Turning back now to Canadian jurisprudence on the matter. In 1955, in Hoffmann-LaRoche & Co. v. Canada (Commissioner of Patents), [1955] S.C.R. 414; 23 C.P.R. 1 (Hoffmann-LaRoche), the Supreme Court of Canada issued its well-known decision that, contrary to what was then the English practice, no product by process claim could be issued in Canada for a known product, even though the process itself was new. As this involved an appeal in respect of a decision of the Commissioner of Patents refusing to allow the proposed product by process claims, the Supreme Court of Canada was not required to discuss the issue of infringement of a pure process patent or process claims, by the importation of a product (not covered by the patent) made abroad using the patented process. Nevertheless, while dealing with the main issue before it, Chief Justice Patrick Kerwin, writing for the majority, considered the decision of the Court of Appeal of England and Wales in Von Heyden, as well as two Canadian decisions, Auer and Toronto Auer Light and expressly noted that “there seems to be no reason to doubt the correctness of these decisions.”[113]

[296] While accepting that Canadian patent law differs from British legislation, and that Canadian patent law was originally modeled on U.S. legislation, Apotex’s argument that the distinctions between Canadian and British law should render British jurisprudence of little assistance on this issue is unpersuasive. Put plainly, notwithstanding the differences between Canadian and British patent laws, our Courts continue to look to British jurisprudence to inform the analysis of our intellectual property laws.

[297] There is also little doubt that the Exchequer Court of Canada and the Supreme Court of Canada were fully aware of these differences between English and Canadian legislation. The best example of this is Union Carbide Canada Ltd. v. Trans-Canadian Feeds Ltd., [1966] Ex.C.R. 884 (Union Carbide), where President Wilbur Jackett,[114] having reviewed the cases of Elmslie and Von Heyden, said at para. 13:
I have been able to discover no such difference between the ambit of an English patent for an invention and the ambit of the monopoly granted under the Canadian Patent Act as would warrant reaching a conclusion when this question arises under the Canadian Act different from that reached in respect of an English patent.

[298] The learned judge also noted that he was unable to ascertain any relevant difference between the Canadian legislation that was under consideration in Auer and he concluded based on comity that he should follow Auer, noting that it had also been the subject of the obiter mentioned above in Hoffmann-LaRoche.

[299] President Jackett appeared unaware of the then recent decision of Justice Noël in Rhone-Poulenc S.A. v. Micro Chemicals Ltd., [1964] Ex.C.R. 819, 44 C.R.R. 193 (Rhone-Poulenc), where, on the basis of the same authorities, the latter had concluded that the principle was now accepted by our Courts (para. 49). Also, although there is a reference to the Badische Anilin und Soda Fabrik decisions (see above) in the editorial note of the Canadian Patent Reporter for Rhone-Poulenc, at 194, it does not appear that these cases were brought to the attention of the Court.

[300] The term “Saccharin doctrine” per se came to the forefront in American Cyanamid Co.. In that case, the Court had to determine if the “Saccharin doctrine” should be applied to the importation of tetracycline in Canada. This particular product was not covered by the patent at issue but it was made using a patented process for making chlortetracycline,[115] to which a dechlorination method was then applied to obtain tetracycline. Thus, the patented process was not the last step in making the product ultimately imported and used in Canada. The learned judge does not specifically refer to the decision in Wilderman (he says simply “there are also a number of cases”, para. 41). But having expressed some concern in respect of the application of the doctrine to processes that are merely incidental, the learned judge did apply the “Saccharin doctrine”, as he found that the product used as an intermediary was of importance.

[301] Between 1966 and 1991, it appears that the Exchequer Court of Canada and the Federal Court of Canada considered the issue quite settled. In Rhone-Poulenc v. Gilbert (1967), 35 Fox Pat. C. 174 (aff’d, [1968] S.C.R. 950, 69 D.L.R. (2d) 353) (Gilbert), Justice Arthur Thurlow, after referring to the decision of President Jackett in Union Carbide, stated that in the absence of any expression of opinion to the contrary by the Supreme Court of Canada, he regarded the point as settled in this Court.

[302] In Leesona Corp. v. Giltex Hosiery Ltd. (1971), 2 C.P.R. (2d) 211, [1971] F.C.J. No. 1006 (QL), Justice Roderick Kerr followed Justice Thurlow’s decision in Gilbert and even issued an interlocutory injunction to prevent the importation into Canada of certain products made abroad according to patented processes. Reference was also made to the then recent decision of Lord Justice Denning in Beecham Group.

[303] Nevertheless, three years later in Farbwerke Hoechst Aktiengesellschaft, vormals Meister Lucius & Bruning v. Halocarbon (Ontario) Ltd., [1974] 2 F.C. 266, 15 C.P.R. (2d) 105, Justice Frank Collier again faced the same issue, where the Canadian defendant imported isohalothane, a product made in the United States by a process patented in Canada. It was then used to manufacture another product at the defendant’s plant in Ontario. Although Justice Collier did not go into the details of the arguments presented, he notes in his reasons, at para. 10, that the Court “was invited by Mr. Hughes [as he then was] to distinguish, on a number of grounds, the Union Carbide case and the cases referred to by Jackett P.” but concludes that he does not “see any reasonable grounds for so doing.” It is important to mention that in his decision, Justice Collier specifically echoed the comments of Justice Thurlow in Gilbert and stated that in the absence of any expression of opinion to the contrary by the Supreme Court of Canada, he regarded the point as settled.

## 22183:15 · paragraphs 304-314

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `518b9f3784884cdfbabb2ee324415931d1ef6c6a49299878229ef33b0963ccf7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:15:subtheme:1 · paragraphs 304-307

- Raw key terms: `canadian, court, doctrine, infringement, justice, patent, process, saccharin`
- Display key terms: `canadian, doctrine, infringement, justice, patent, process, saccharin`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: canadian, doctrine, infringement, justice, patent, process, saccharin Position/evidence statements: [307] Applying the “Saccharin doctrine” as qualified by Wilderman, the Court concluded that there was infringement of the process claims by the importation of trimethoprim. Rule/authority context: This strongly suggests that the Supreme Court considered the issue of infringement by importation settled by the existing jurisprudence. Application context: It will therefore not be dealt with. | , which it found questionable because of the absence of a direct reference to the limitation of the doctrine as set out in Wilderman. Operative outcome context: [304] This decision was reversed by the Federal Court of Appeal and the plaintiff appealed to the Supreme Court of Canada, which allowed the appeal ([1979] 2 S. | any act which interferes with the full enjoyment of the monopoly granted to the patentee is an infringement”. Evidence spans paragraphs 304-307. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040550` offsets `819-824`; context: This strongly suggests that the Supreme Court considered the issue of infringement by importation settled by the existing jurisprudence.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5040550` offsets `880-893`; context: This strongly suggests that the Supreme Court considered the issue of infringement by importation settled by the existing jurisprudence.
- Evidence: `reasoning_application` cue `therefore` at chunk `5040550` offsets `729-738`; context: It will therefore not be dealt with.
- Evidence: `disposition` cue `allowed` at chunk `5040550` offsets `129-136`; context: [304] This decision was reversed by the Federal Court of Appeal and the plaintiff appealed to the Supreme Court of Canada, which allowed the appeal ([1979] 2 S.
- Evidence: `reasoning_application` cue `because` at chunk `5040551` offsets `530-537`; context: , which it found questionable because of the absence of a direct reference to the limitation of the doctrine as set out in Wilderman.
- Evidence: `disposition` cue `granted` at chunk `5040552` offsets `1091-1098`; context: any act which interferes with the full enjoyment of the monopoly granted to the patentee is an infringement”.
- Evidence: `party_position` cue `claims` at chunk `5040553` offsets `130-136`; context: [307] Applying the “Saccharin doctrine” as qualified by Wilderman, the Court concluded that there was infringement of the process claims by the importation of trimethoprim.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040553` offsets `207-215`; context: As mentioned by Apotex, there was evidence in that case that traces of MTBP and TAA (the intermediate compounds) were found in the final product sold by the defendant in Canada.

#### 22183:15:subtheme:2 · paragraphs 308-309

- Raw key terms: `apotex, court, doctrine, advanced, appeal, appealed, applicable, application`
- Display key terms: `apotex, doctrine, advanced, appealed, applicable`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, reasoning_application Display terms: apotex, doctrine, advanced, appealed, applicable Rule/authority context: However, more recent jurisprudence further undermines the argument advanced by Apotex. Application context: [309] These Canadian decisions are, in my view, sufficient for this Court to conclude that the “Saccharin doctrine” as qualified by Wilderman is applicable to the case at bar. Operative outcome context: [308] It is worth noting that Apotex appealed the decision of Justice MacKay, which was varied on an unrelated issue ((1995), 100 F. Evidence spans paragraphs 308-309. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040554` offsets `111-116`; context: [308] It is worth noting that Apotex appealed the decision of Justice MacKay, which was varied on an unrelated issue ((1995), 100 F.
- Evidence: `disposition` cue `varied` at chunk `5040554` offsets `88-94`; context: [308] It is worth noting that Apotex appealed the decision of Justice MacKay, which was varied on an unrelated issue ((1995), 100 F.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5040555` offsets `197-210`; context: However, more recent jurisprudence further undermines the argument advanced by Apotex.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040555` offsets `77-85`; context: [309] These Canadian decisions are, in my view, sufficient for this Court to conclude that the “Saccharin doctrine” as qualified by Wilderman is applicable to the case at bar.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040555` offsets `176-183`; context: However, more recent jurisprudence further undermines the argument advanced by Apotex.

#### 22183:15:subtheme:3 · paragraphs 310-314

- Raw key terms: `canada, monsanto, para, monopoly, patent, patented, process, court`
- Display key terms: `monsanto, para, monopoly, patent, patented, process`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, reasoning_application Display terms: monsanto, para, monopoly, patent, patented, process Rule/authority context: , the Supreme Court of Canada articulated broad principles related to the interpretation of the rights granted under the Patent Act. | [311] Several of these principles are relevant to the issue of infringement by importation. Application context: Therefore, what is prohibited is "any act that interferes with the full enjoyment of the monopoly granted to the patentee": H. | The appellants have not infringed the process claim because they have not used the claimed method to produce their canola crop. Operative outcome context: , the Supreme Court of Canada articulated broad principles related to the interpretation of the rights granted under the Patent Act. | 42 is to define the exclusive rights granted to the patent holder. Evidence spans paragraphs 310-314. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040556` offsets `452-459`; context: The basic principle in determining whether the defendant has "used" a patented invention is whether the inventor has been deprived, in whole or in part, directly or indirectly, of the full enjoyment of the monopoly conferred by the patent.
- Evidence: `governing_rule` cue `principles` at chunk `5040556` offsets `77-87`; context: , the Supreme Court of Canada articulated broad principles related to the interpretation of the rights granted under the Patent Act.
- Evidence: `disposition` cue `granted` at chunk `5040556` offsets `132-139`; context: , the Supreme Court of Canada articulated broad principles related to the interpretation of the rights granted under the Patent Act.
- Evidence: `issue` cue `issue` at chunk `5040557` offsets `54-59`; context: [311] Several of these principles are relevant to the issue of infringement by importation.
- Evidence: `governing_rule` cue `principles` at chunk `5040557` offsets `23-33`; context: [311] Several of these principles are relevant to the issue of infringement by importation.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5040558` offsets `385-394`; context: Therefore, what is prohibited is "any act that interferes with the full enjoyment of the monopoly granted to the patentee": H.
- Evidence: `disposition` cue `granted` at chunk `5040558` offsets `270-277`; context: 42 is to define the exclusive rights granted to the patent holder.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5040559` offsets `123-136`; context: with reference to British jurisprudence:
Thus, in Saccharin Corp.
- Evidence: `reasoning_application` cue `because` at chunk `5040560` offsets `761-768`; context: The appellants have not infringed the process claim because they have not used the claimed method to produce their canola crop.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040560` offsets `700-707`; context: This proposition does not assist the respondent, however.

#### Section text

[304] This decision was reversed by the Federal Court of Appeal and the plaintiff appealed to the Supreme Court of Canada, which allowed the appeal ([1979] 2 S.C.R. 929, 104 D.L.R. (3d) 51) and specifically reinstated the decision of Justice Collier in respect of the impugned process claim. At p. 941 (of the S.C.R.), Justice Louis-Philippe Pigeon, who delivered the reasons for the majority, noted:
At the hearing in this Court, counsel for the respondent raised the contention that the importation of a product manufactured outside Canada did not infringe a Canadian patent for the process whereby it is manufactured elsewhere, but counsel for the appellant was informed that no reply to that submission was required. It will therefore not be dealt with.
This strongly suggests that the Supreme Court considered the issue of infringement by importation settled by the existing jurisprudence.

[305] Undeterred, Apotex mounted a new charge before Justice Andrew MacKay in Wellcome Foundation Ltd. v. Apotex Inc., 47 F.T.R. 81, 39 C.P.R. (3d) 289 (Wellcome (1991)), raising arguments very similar to those discussed at length in its memorandum before this Court. It contested the validity of the “Saccharin doctrine” per se, based among other things on the differences between the English and Canadian patent statutes.[116] It also contested the findings of Justice Noël in American Cyanamid Co., which it found questionable because of the absence of a direct reference to the limitation of the doctrine as set out in Wilderman.

[306] Prompted by these arguments and the fact that this was indeed only the second reported case involving a process patent for an intermediate compound (B-methoxy-a-(3,4,5-trimethoxybenzylidene) propionitrile, or MTBP and B-anilino-a-(3,4,5-trimethoxybenzyl) acrylonitrile, or TAA), Justice MacKay addressed the point in more detail than his predecessors. Particularly, with respect to the basis of the doctrine in the Canadian legislation, the learned judge stated at para. 59:
I also reject the defendant's submission that the differences in the Canadian Act from the English statute do not support the application of the Saccharin doctrine. The “exclusive right” of “vending” seems to me to be broad enough to encompass situations such as that in this case. This point as well was noted in American Cyanamid, at 168. The effect of the granting provision, now section 44 of the Patent Act, may be summarized, as it was by O'Halloran J.A. in Skelding v. Daly, (1941), 1 C.P.R. 266 at 273 (B.C.C.A.), as intending that “... any act which interferes with the full enjoyment of the monopoly granted to the patentee is an infringement”.
[Emphasis added.]

[307] Applying the “Saccharin doctrine” as qualified by Wilderman, the Court concluded that there was infringement of the process claims by the importation of trimethoprim. As mentioned by Apotex, there was evidence in that case that traces of MTBP and TAA (the intermediate compounds) were found in the final product sold by the defendant in Canada.

[308] It is worth noting that Apotex appealed the decision of Justice MacKay, which was varied on an unrelated issue ((1995), 100 F.T.R. 320 n, 60 C.P.R. 3(d) 135). Surprisingly, it seems that Apotex did not contest the application of the doctrine by Justice MacKay before the Court of Appeal even though this point was clearly determinative in respect of the findings of infringement.

[309] These Canadian decisions are, in my view, sufficient for this Court to conclude that the “Saccharin doctrine” as qualified by Wilderman is applicable to the case at bar. However, more recent jurisprudence further undermines the argument advanced by Apotex.

[310] In Monsanto Canada Inc., the Supreme Court of Canada articulated broad principles related to the interpretation of the rights granted under the Patent Act. At para. 58, Chief Justice Beverly McLachlin and Justice Morris Fish, speaking for the majority, summarize seven such principles:
1. "Use" or "exploiter", in their ordinary dictionary meaning, denote utilization with a view to production or advantage.
2. The basic principle in determining whether the defendant has "used" a patented invention is whether the inventor has been deprived, in whole or in part, directly or indirectly, of the full enjoyment of the monopoly conferred by the patent.
3. If there is a commercial benefit to be derived from the invention, it belongs to the patent holder.
4. It is no bar to a finding of infringement that the patented object or process is a part of or composes a broader unpatented structure or process, provided the patented invention is significant or important to the defendant's activities that involve the unpatented structure.
5. Possession of a patented object or an object incorporating a patented feature may constitute "use" of the object's stand-by or insurance utility and thus constitute infringement.
6. Possession, at least in commercial circumstances, raises a rebuttable presumption of "use".
7. While intention is generally irrelevant to determining whether there has been "use" and hence infringement, the absence of intention to employ or gain any advantage from the invention may be relevant to rebutting the presumption of use raised by possession.
[Emphasis added.]

[311] Several of these principles are relevant to the issue of infringement by importation. First, with regards to the question of “use”, the Court must ask itself: “did the defendant’s activity deprive the inventor in whole or in part, directly or indirectly, of full enjoyment of the monopoly conferred by law?” (Emphasis omitted, Monsanto Canada Inc., para. 35; see also Free World Trust, para. 43). This is exactly the question all the British cases cited above, going back to Elmslie, Von Heyden and Saccharin, meant to answer when they concluded that the importation, use or sale of products made abroad by way of the patented process constitutes infringement.

[312] Moreover, the meaning and purpose of s. 42 of the Patent Act, as described at para. 34 of the Monsanto Canada Inc. decision, is perfectly in line with the views adopted by Justice MacKay in Wellcome (1991):
[t]he purpose of s. 42 is to define the exclusive rights granted to the patent holder. These rights are the rights to full enjoyment of the monopoly granted by the patent. Therefore, what is prohibited is "any act that interferes with the full enjoyment of the monopoly granted to the patentee": H. G. Fox, The Canadian Law and Practice Relating to Letters Patent for Inventions (4th ed. 1969), at p. 349;
[Monsanto Canada Inc., para. 34.]

[313] This approach to a patent’s monopoly was discussed by the majority in Monsanto Canada Inc. with reference to British jurisprudence:
Thus, in Saccharin Corp. v. Anglo-Continental Chemical Works, Ld. (1900), 17 R.P.C. 307 (H.C.J.), the court stated, at p. 319:
By the sale of saccharin, in the course of the production of which the patented process is used, the Patentee is deprived of some part of the whole profit and advantage of the invention, and the importer is indirectly making use of the invention.
[para. 44]

[314] It is also worth nothing that even the minority in Monsanto Canada Inc. appear to be in agreement with the “Saccharin doctrine”. As Justice Louise Arbour stated, at para. 155:
It is well established that the use or sale of unpatented subject matter may still infringe a patent where the unpatented subject matter is made employing a patented process: Saccharin Corp. v. Anglo-Continental Chemical Works, Ld. (1900), 17 R.P.C. 307 (H.C.J.); F. Hoffmann-Laroche, supra, at p. 415; Wellcome Foundation Ltd. v. Apotex Inc. (1991), 39 C.P.R. (3d) 289 (F.C.T.D.); American Cyanamid Co. v. Charles E. Frosst & Co. (1965), 29 Fox Pat. C. 153 (Ex. Ct.). This proposition does not assist the respondent, however. The appellants have not infringed the process claim because they have not used the claimed method to produce their canola crop.
[Emphasis in the original.]

## 22183:16 · paragraphs 315-326

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d15cb40c5f961ce26740d9ff4acb2a148f2ba3d44012e73fdf79d3d609c3bc05`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:16:subtheme:1 · paragraphs 315-316

- Raw key terms: `apotex, address, argument, arguments, assistance, canada, consider, court`
- Display key terms: `apotex, address, argument, arguments, assistance, consider`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: apotex, address, argument, arguments, assistance, consider Rule/authority context: did not specifically address the issue of territoriality, the principles laid out therein are of assistance in evaluating Apotex’s argument. Evidence spans paragraphs 315-316. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040561` offsets `79-84`; context: did not specifically address the issue of territoriality, the principles laid out therein are of assistance in evaluating Apotex’s argument.
- Evidence: `governing_rule` cue `principles` at chunk `5040561` offsets `108-118`; context: did not specifically address the issue of territoriality, the principles laid out therein are of assistance in evaluating Apotex’s argument.
- Evidence: `issue` cue `question` at chunk `5040562` offsets `124-132`; context: [316] Both Lilly and Apotex have raised various policy reasons in support of their respective positions with respect to the question of infringement by importation.

#### 22183:16:subtheme:2 · paragraphs 317-321

- Raw key terms: `process, apotex, application, argument, canada, court, importation, jurisprudence`
- Display key terms: `process, apotex, argument, importation, jurisprudence`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: process, apotex, argument, importation, jurisprudence Rule/authority context: jurisprudence regarding this issue (which were considered by the Court), was followed by legislative changes seeking to close significant gaps resulting from these decisions. | [318] In sum, the Court agrees with Lilly that it is now too late to turn back the clock on the application of the general principles set out in the above-mentioned Canadian case law. Evidence spans paragraphs 317-321. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040563` offsets `55-60`; context: approach to this issue should be preferred is not convincing.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5040563` offsets `141-154`; context: jurisprudence regarding this issue (which were considered by the Court), was followed by legislative changes seeking to close significant gaps resulting from these decisions.
- Evidence: `governing_rule` cue `principles` at chunk `5040564` offsets `123-133`; context: [318] In sum, the Court agrees with Lilly that it is now too late to turn back the clock on the application of the general principles set out in the above-mentioned Canadian case law.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5040565` offsets `238-251`; context: Process Patent Amendment Act and/or the EPC, as well as the jurisprudence that has interpreted these instruments.

#### 22183:16:subtheme:3 · paragraphs 322-325

- Raw key terms: `patent, apotex, aware, bills, court, importation, infringement, made`
- Display key terms: `patent, apotex, aware, bills, importation, infringement, made`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: patent, apotex, aware, bills, importation, infringement, made Rule/authority context: [325] What Apotex seeks in this Court is a re-writing of Canadian patent laws in order to limit the application of over a century’s worth of jurisprudence. Application context: This principle applies also where the process used abroad has not produced the finished product that is imported but an intermediate that falls within the claims of the patent. Evidence spans paragraphs 322-325. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040568` offsets `493-498`; context: None of these changes address the issue before the Court.
- Evidence: `reasoning_application` cue `applies` at chunk `5040569` offsets `623-630`; context: This principle applies also where the process used abroad has not produced the finished product that is imported but an intermediate that falls within the claims of the patent.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5040571` offsets `141-154`; context: [325] What Apotex seeks in this Court is a re-writing of Canadian patent laws in order to limit the application of over a century’s worth of jurisprudence.

#### 22183:16:subtheme:4 · paragraphs 326-326

- Raw key terms: `actually, advantage, ambiguity, another, bears, benefit, burden, canada`
- Display key terms: `actually, advantage, ambiguity, another, bears, benefit, burden`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: actually, advantage, ambiguity, another, bears, benefit, burden Application context: 90] Justice Snider concludes that “[i]n sum, there must be a strong link established between the use of the patented process or product and the product sold into Canada. Evidence spans paragraphs 326-326. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040572` offsets `135-142`; context: [326] As mentioned earlier, Justice Snider, in Pfizer, made a very useful summary of factors that a Court should consider to determine whether or not the patented process plays an important part in the manufacture of the imported products:
- The importance of the product or process to the final product sold into Canada.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040572` offsets `1144-1152`; context: Where the same patented product is used repetitively through the production of the non-patented end product, there may be clearer evidence that the advantage of the patentee has been impaired.
- Evidence: `reasoning_application` cue `concludes` at chunk `5040572` offsets `1670-1679`; context: 90]
Justice Snider concludes that “[i]n sum, there must be a strong link established between the use of the patented process or product and the product sold into Canada.

#### Section text

[315] While mindful that Monsanto Canada Inc. did not specifically address the issue of territoriality, the principles laid out therein are of assistance in evaluating Apotex’s argument.

[316] Both Lilly and Apotex have raised various policy reasons in support of their respective positions with respect to the question of infringement by importation. There is no need to discuss them here except to say such arguments are matters for Parliament to consider, not this Court.

[317] Apotex’s argument that the U.S. approach to this issue should be preferred is not convincing. It is worth noting that much of the U.S. jurisprudence regarding this issue (which were considered by the Court), was followed by legislative changes seeking to close significant gaps resulting from these decisions.

[318] In sum, the Court agrees with Lilly that it is now too late to turn back the clock on the application of the general principles set out in the above-mentioned Canadian case law. Importation of products made abroad that are the subject of patented process claims in Canada is prohibited. This prohibition is widely recognized and is well-settled law in Canada.

[319] Apotex’s second argument with respect to infringement by importation seeks to limit the application of the “Saccharin doctrine” as qualified by Wilderman based on the U.S. Process Patent Amendment Act and/or the EPC, as well as the jurisprudence that has interpreted these instruments.

[320] First, it is worth mentioning that even though Parliament has had opportunities to intervene in this respect, it appears never to have felt the need to do so even after Canada became a party to the NAFTA and the Agreement on Trade-Related Aspects of Intellectual Property Rights (TRIPS)[117] agreements.

[321] In NAFTA, para. 1709(5)(b) reads:
where the subject matter of a patent is a process, the patent shall confer on the patent owner the right to prevent other persons from using that process and from using, selling, or importing at least the product obtained directly by that process, without the patent owner's consent. [Emphasis added.] Para. 28(1)(b) of TRIPS is nearly identical. It reads: where the subject matter of a patent is a process,
[a patent shall confer on its owner the exclusive right] to prevent third parties not having the owner’s consent from the act of using the process, and from the acts of: using, offering for sale, selling, or importing for these purposes at least the product obtained directly by that process.
[Emphasis added.]

[322] Parliament adopted two bills with respect to the implementation of these agreements. The first, An Act to Implement the North American Free Trade Agreement, S.C. 1993, c. 44, sets out at s. 189 and following, the changes to the Patent Act made necessary by this agreement. The second, An Act to Implement the Agreement Establishing the World Trade Organization, S.C. 1994, c. 47, deals with necessary modifications to the Patent Act at ss. 141 and 142. None of these changes address the issue before the Court.

[323] It can be reasonably assumed that the legislator was well aware of the state of patent law in Canada before it presented these bills. The relevant law at that time was summarized in Fox, at pp. 391 and 392, as follows:
In considering infringement it is well to remember that it is not only manufacture that is forbidden to others than the patentee, but use and sale as well. For this reason infringement is committed by the importation of infringing articles made abroad, as well as importation and use in the country of articles or products made abroad on a patented machine or by a patented process. This principle applies also where the process used abroad has not produced the finished product that is imported but an intermediate that falls within the claims of the patent. In other words, it is none the less an infringement that the article or substance produced and sold which is manufactured by the use of the patented process is subjected to certain other processes. But this concept must be considered with care: it does not apply in a case of de minimis. If there is an act committed in Canada by the defendant in derogation of the patentee’s rights there is infringement.
[Footnotes omitted.]

[324] It is also reasonable to assume that Parliament was well aware of the relevant statutory provisions referred to by Apotex.

[325] What Apotex seeks in this Court is a re-writing of Canadian patent laws in order to limit the application of over a century’s worth of jurisprudence. While European and U.S. statutory provisions may be of assistance in analyzing Canadian laws, they cannot serve to displace the well-settled jurisprudence on infringement by importation.

[326] As mentioned earlier, Justice Snider, in Pfizer, made a very useful summary of factors that a Court should consider to determine whether or not the patented process plays an important part in the manufacture of the imported products:
- The importance of the product or process to the final product sold into Canada. Where the use is incidental, non-essential or could readily be substituted (such as the Italian scissors example), a Court might be less inclined to find infringement.
- Whether the final product actually contains all or part of the patented product. Where the patented product can actually be identified in the product sold into Canada, there may be a strong case for a finding of infringement.
- The stage at which the patented product or process is used. For example, use of a process as a preliminary step of a lengthy production process may lead to a conclusion that the patentee has suffered little deprivation.
- The number of instances of use made of the patented product or process. Where the same patented product is used repetitively through the production of the non-patented end product, there may be clearer evidence that the advantage of the patentee has been impaired.
- The strength of the evidence demonstrating that, if carried out or used in Canada, the product or process would constitute infringement. On this point, my opinion would be that, where there is ambiguity in the evidence, the benefit of the doubt should go to the party using the product or process. This is, perhaps, simply another way of expressing the established principle that the patentee bears the burden of proving infringement.
[para. 90]
Justice Snider concludes that “[i]n sum, there must be a strong link established between the use of the patented process or product and the product sold into Canada.” (para. 91.)

## 22183:17 · paragraphs 327-419

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ceffb91b64a7e8fbf0325416051befc39798f59222314db32ce024b68486f143`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:17:subtheme:1 · paragraphs 327-345

- Raw key terms: `cefaclor, used, process, lilly, apotex, canada, fact, lupin`
- Display key terms: `cefaclor, used, process, lilly, apotex, fact, lupin`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: cefaclor, used, process, lilly, apotex, fact, lupin Rule/authority context: On this basis, I will now proceed to apply these principles to the facts of this case. | The Exemption Under Subsection 55. Application context: The Courts in Beecham Group were able to conclude to infringement despite the fact that the final ingredient imported in England no longer contained the compound made using the patented processes. | [329] For these reasons, not only do I conclude that the Court cannot redefine and limit the test applicable in Canada with respect to infringement by importation and use, but also that I should not do so. Evidence spans paragraphs 327-345. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040573` offsets `197-204`; context: There is nothing in what she proposed that prevents the Court from also considering whether the imported product was obtained directly from the patented process or whether the compound made by the patented process was materially changed or has become a trivial or non-essential component of the imported product.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040574` offsets `121-129`; context: The Courts in Beecham Group were able to conclude to infringement despite the fact that the final ingredient imported in England no longer contained the compound made using the patented processes.
- Evidence: `governing_rule` cue `principles` at chunk `5040575` offsets `255-265`; context: On this basis, I will now proceed to apply these principles to the facts of this case.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040575` offsets `39-47`; context: [329] For these reasons, not only do I conclude that the Court cannot redefine and limit the test applicable in Canada with respect to infringement by importation and use, but also that I should not do so.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5040575` offsets `63-69`; context: [329] For these reasons, not only do I conclude that the Court cannot redefine and limit the test applicable in Canada with respect to infringement by importation and use, but also that I should not do so.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040582` offsets `26-34`; context: [336] On the whole of the evidence, it is clear that the Shionogi and Lilly processes were more efficient (and therefore less costly) than any other alternative discussed in any of the publications referred to by the experts or used by Lupin.
- Evidence: `reasoning_application` cue `therefore` at chunk `5040582` offsets `111-120`; context: [336] On the whole of the evidence, it is clear that the Shionogi and Lilly processes were more efficient (and therefore less costly) than any other alternative discussed in any of the publications referred to by the experts or used by Lupin.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040583` offsets `63-71`; context: [337] In fact, in respect of the Lilly process, there is clear evidence that to change what is described in Lupin’s documentation simply as step V (although it involves three distinct reactions) resulted in an increase of almost 50% of the price of cefaclor.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040586` offsets `44-52`; context: [340] Having considered and weighed all the evidence, I conclude that, as a matter of fact, Lilly’s patented process was an “important” part of the method used by Lupin to make the cefaclor that was used by Apotex in Canada.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040586` offsets `56-64`; context: [340] Having considered and weighed all the evidence, I conclude that, as a matter of fact, Lilly’s patented process was an “important” part of the method used by Lupin to make the cefaclor that was used by Apotex in Canada.
- Evidence: `governing_rule` cue `Under` at chunk `5040587` offsets `300-305`; context: The Exemption Under Subsection 55.
- Evidence: `governing_rule` cue `under` at chunk `5040588` offsets `244-249`; context: 2(1) It is not an infringement of a patent for any person to make, construct, use or sell the patented invention solely for uses reasonably related to the development and submission of information required under any law of Canada, a province or a country other than Canada that regulates the manufacture, construction, use or sale of any product.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040589` offsets `87-96`; context: Carrière’s testimony, the in-process sampling and the reserve samples were not set aside simply to meet government requirements but also for internal quality controls (which addresses business, not regulatory, imperatives).
- Evidence: `reasoning_application` cue `apply` at chunk `5040589` offsets `370-375`; context: Lilly argues that in light of this dual purpose, the exemption cannot apply to such material.
- Evidence: `governing_rule` cue `under` at chunk `5040591` offsets `367-372`; context: Fahner[124] as a result of his cross-examination and attached to a letter from counsel for Apotex dated May 12, 2008, shall be the subject of the reference in order to determine what quantities properly fall under the above-mentioned categories.

#### 22183:17:subtheme:2 · paragraphs 346-349

- Raw key terms: `invalidity, parties, proof, burden, common, patents, standard, thus`
- Display key terms: `invalidity, proof, burden, common, patents, standard, thus`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: invalidity, proof, burden, common, patents, standard, thus Rule/authority context: Standard of Review and Burden of Proof Evidence spans paragraphs 346-349. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040592` offsets `54-59`; context: [346] Both parties recognize that this is not a major issue in this case and thus there is nothing more to say.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `5040593` offsets `280-298`; context: Standard of Review and Burden of Proof

#### 22183:17:subtheme:3 · paragraphs 350-352

- Raw key terms: `asserting, invalidity, party, patent, argues, canada, commissioner, court`
- Display key terms: `asserting, invalidity, patent, argues, commissioner`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: asserting, invalidity, patent, argues, commissioner Position/evidence statements: In so doing, the party attacking validity must establish that the patent, or claims within a patent, do not meet the requirements for patentability under the Patent Act (i. Rule/authority context: […] In the circumstances, I think the appropriate standard of review of these issues, which largely raise mixed questions of law and fact, is reasonableness simpliciter, i. | In so doing, the party attacking validity must establish that the patent, or claims within a patent, do not meet the requirements for patentability under the Patent Act (i. Application context: Furthermore, Lilly argues that deference is owed, and that the standard of reasonableness should apply. Evidence spans paragraphs 350-352. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040596` offsets `273-278`; context: Lilly argues that Apotex must prove that the decision of the Commissioner of Patents to approve the patents at issue was unreasonable.
- Evidence: `governing_rule` cue `standard of review` at chunk `5040596` offsets `1108-1126`; context: […]
In the circumstances, I think the appropriate standard of review of these issues, which largely raise mixed questions of law and fact, is reasonableness simpliciter, i.
- Evidence: `reasoning_application` cue `apply` at chunk `5040597` offsets `323-328`; context: Furthermore, Lilly argues that deference is owed, and that the standard of reasonableness should apply.
- Evidence: `party_position` cue `claims` at chunk `5040598` offsets `300-306`; context: In so doing, the party attacking validity must establish that the patent, or claims within a patent, do not meet the requirements for patentability under the Patent Act (i.
- Evidence: `governing_rule` cue `under` at chunk `5040598` offsets `371-376`; context: In so doing, the party attacking validity must establish that the patent, or claims within a patent, do not meet the requirements for patentability under the Patent Act (i.

#### 22183:17:subtheme:4 · paragraphs 353-355

- Raw key terms: `administrative, court, fact, patent, principles, without, years, accordingly`
- Display key terms: `administrative, fact, patent, principles, without, years, accordingly`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: administrative, fact, patent, principles, without, years, accordingly Rule/authority context: [354] The approach to validity, assessing claims against the requirements of the Patent Act, without reference to principles of administrative law, has been the standard judicial practice for more than a hundred years. | The fact that the bulk of the jurisprudence since Wellcome (2002) has considered invalidity without resort to administrative law principles buttresses this conclusion. Application context: 59 of the Patent Act which speaks of “any fact or default which by this Act or by law renders the patent void” and directs the Court to “take cognizance of that pleading and of the facts and decide accordingly. Evidence spans paragraphs 353-355. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `accordingly` at chunk `5040599` offsets `253-264`; context: 59 of the Patent Act which speaks of “any fact or default which by this Act or by law renders the patent void” and directs the Court to “take cognizance of that pleading and of the facts and decide accordingly.
- Evidence: `governing_rule` cue `principles` at chunk `5040600` offsets `114-124`; context: [354] The approach to validity, assessing claims against the requirements of the Patent Act, without reference to principles of administrative law, has been the standard judicial practice for more than a hundred years.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5040601` offsets `340-353`; context: The fact that the bulk of the jurisprudence since Wellcome (2002) has considered invalidity without resort to administrative law principles buttresses this conclusion.

#### 22183:17:subtheme:5 · paragraphs 356-357

- Raw key terms: `administrative, analysis, commissioner, decision, grant, invalidity, wellcome, above`
- Display key terms: `administrative, analysis, commissioner, grant, invalidity, wellcome, above`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: administrative, analysis, commissioner, grant, invalidity, wellcome, above Rule/authority context: [357] Furthermore, despite having imported administrative law principles into the invalidity analysis, neither Wellcome (2002) and Monsanto Canada Inc. Application context: actually applies concepts such as the degree of deference owed to the decision of the Commissioner to grant the patents at issue. Evidence spans paragraphs 356-357. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040602` offsets `542-548`; context: alleged infringer) raising similar issues but in very different contexts.
- Evidence: `issue` cue `issue` at chunk `5040603` offsets `275-280`; context: actually applies concepts such as the degree of deference owed to the decision of the Commissioner to grant the patents at issue.
- Evidence: `governing_rule` cue `principles` at chunk `5040603` offsets `62-72`; context: [357] Furthermore, despite having imported administrative law principles into the invalidity analysis, neither Wellcome (2002) and Monsanto Canada Inc.
- Evidence: `reasoning_application` cue `applies` at chunk `5040603` offsets `161-168`; context: actually applies concepts such as the degree of deference owed to the decision of the Commissioner to grant the patents at issue.
- Evidence: `counterargument_limitation` cue `notwithstanding` at chunk `5040603` offsets `291-306`; context: In fact, notwithstanding the above referenced paragraphs of these decisions, the term “reasonableness” is not even used in assessing invalidity.

#### 22183:17:subtheme:6 · paragraphs 358-360

- Raw key terms: `reasons, administrative, canada, commissioner, decision, grant, invalidity, para`
- Display key terms: `administrative, commissioner, grant, invalidity, para`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: administrative, commissioner, grant, invalidity, para Application context: In this case, the Defendants argue that the patent is invalid because it was both obvious and anticipated. | [359] Such an attitude is understandable for there are a number of reasons why an administrative law approach to invalidity is almost impossible to apply without further guidance from Canada’s highest Court. Evidence spans paragraphs 358-360. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040604` offsets `284-289`; context: In discussing the issue of validity, Justice Snider stated:
Once a patent is issued, there is a presumption that, in the absence of evidence to the contrary, the patent is valid (Patent Act, s.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040604` offsets `398-406`; context: In discussing the issue of validity, Justice Snider stated:
Once a patent is issued, there is a presumption that, in the absence of evidence to the contrary, the patent is valid (Patent Act, s.
- Evidence: `reasoning_application` cue `because` at chunk `5040604` offsets `830-837`; context: In this case, the Defendants argue that the patent is invalid because it was both obvious and anticipated.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040604` offsets `957-964`; context: 72]
Having made this observation, however, nowhere in her reasons does Justice Snider engage in anything resembling a reasonableness review akin to that which was set out in Dunsmuir v.
- Evidence: `reasoning_application` cue `apply` at chunk `5040605` offsets `148-153`; context: [359] Such an attitude is understandable for there are a number of reasons why an administrative law approach to invalidity is almost impossible to apply without further guidance from Canada’s highest Court.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5040606` offsets `225-231`; context: Indeed, a patent’s prosecution history cannot be reviewed in construing the claims of a patent (Merck & Co.

#### 22183:17:subtheme:7 · paragraphs 361-367

- Raw key terms: `court, patent, evidence, review, commissioner, applied, canada, decision`
- Display key terms: `patent, review, commissioner, applied`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: patent, review, commissioner, applied Position/evidence statements: [364] Parties challenging validity have always been free, subject to the applicable rules of evidence, to put forth any evidence that may serve to undermine the validity of a patent’s claims. Rule/authority context: [365] In the Harvard College (2000) decision, Chief Justice Isaac referred by analogy to appeals from decisions of the Registrar of Trade-Marks under s. | [366] To be certain, administrative law principles have been applied to certain decisions of the Commissioner of Patents (See e. Application context: [362] A court engaged in judicial review, regardless of the standard applied, is usually limited to only considering the evidence that was before the decision-maker (Gosselin v. | In such cases, standards of review only apply where there is no new evidence that could have affected the decision of the Registrar. Evidence spans paragraphs 361-367. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040607` offsets `51-58`; context: [361] A reasonableness review involves determining whether a decision falls within a range of possible acceptable outcomes on the basis of the evidence before the original decision maker (Dunsmuir, para.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040607` offsets `143-151`; context: [361] A reasonableness review involves determining whether a decision falls within a range of possible acceptable outcomes on the basis of the evidence before the original decision maker (Dunsmuir, para.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040607` offsets `437-445`; context: Although the Supreme Court of Canada left the door open in Free World Trust (para.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040608` offsets `121-129`; context: [362] A court engaged in judicial review, regardless of the standard applied, is usually limited to only considering the evidence that was before the decision-maker (Gosselin v.
- Evidence: `reasoning_application` cue `applied` at chunk `5040608` offsets `69-76`; context: [362] A court engaged in judicial review, regardless of the standard applied, is usually limited to only considering the evidence that was before the decision-maker (Gosselin v.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040609` offsets `49-57`; context: [363] There is no statutory requirement that the evidence before the Commissioner of Patents be provided to the Federal Court in the context of an infringement action.
- Evidence: `party_position` cue `claims` at chunk `5040610` offsets `184-190`; context: [364] Parties challenging validity have always been free, subject to the applicable rules of evidence, to put forth any evidence that may serve to undermine the validity of a patent’s claims.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040610` offsets `93-101`; context: [364] Parties challenging validity have always been free, subject to the applicable rules of evidence, to put forth any evidence that may serve to undermine the validity of a patent’s claims.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040611` offsets `270-278`; context: In such cases, standards of review only apply where there is no new evidence that could have affected the decision of the Registrar.
- Evidence: `governing_rule` cue `under` at chunk `5040611` offsets `144-149`; context: [365] In the Harvard College (2000) decision, Chief Justice Isaac referred by analogy to appeals from decisions of the Registrar of Trade-Marks under s.
- Evidence: `reasoning_application` cue `apply` at chunk `5040611` offsets `242-247`; context: In such cases, standards of review only apply where there is no new evidence that could have affected the decision of the Registrar.
- Evidence: `governing_rule` cue `principles` at chunk `5040612` offsets `40-50`; context: [366] To be certain, administrative law principles have been applied to certain decisions of the Commissioner of Patents (See e.
- Evidence: `reasoning_application` cue `applied` at chunk `5040612` offsets `61-68`; context: [366] To be certain, administrative law principles have been applied to certain decisions of the Commissioner of Patents (See e.
- Evidence: `governing_rule` cue `principles` at chunk `5040613` offsets `217-227`; context: However, where administrative law principles have been applied to decisions of the Commissioner of Patents, it has been in the context where these are amenable to judicial review and not pursuant to s.
- Evidence: `reasoning_application` cue `applied` at chunk `5040613` offsets `238-245`; context: However, where administrative law principles have been applied to decisions of the Commissioner of Patents, it has been in the context where these are amenable to judicial review and not pursuant to s.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040613` offsets `183-190`; context: However, where administrative law principles have been applied to decisions of the Commissioner of Patents, it has been in the context where these are amenable to judicial review and not pursuant to s.

#### 22183:17:subtheme:8 · paragraphs 368-369

- Raw key terms: `departure, invalidity, absent, action, administrative, alone, analysis, analytic`
- Display key terms: `departure, invalidity, absent, action, administrative, alone, analysis, analytic`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: departure, invalidity, absent, action, administrative, alone, analysis, analytic Rule/authority context: [369] In sum, the importation of administrative law principles into the assessment of invalidity has not been thoroughly canvassed by appellate authorities and would constitute a significant departure from the Supreme Co Operative outcome context: But, in the context of an action for infringement where a defence of invalidity is raised, that is not the essential point of departure: the claims stand alone to determine if the monopoly granted meets the test set out  Evidence spans paragraphs 368-369. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `granted` at chunk `5040614` offsets `337-344`; context: But, in the context of an action for infringement where a defence of invalidity is raised, that is not the essential point of departure: the claims stand alone to determine if the monopoly granted meets the test set out in the Act, for example in respect of utility, novelty and inventiveness.
- Evidence: `governing_rule` cue `principles` at chunk `5040615` offsets `52-62`; context: [369] In sum, the importation of administrative law principles into the assessment of invalidity has not been thoroughly canvassed by appellate authorities and would constitute a significant departure from the Supreme Court of Canada’s well-established jurisprudence concerning pleas of invalidity.

#### 22183:17:subtheme:9 · paragraphs 370-373

- Raw key terms: `matter, shionogi, subject, apotex, application, lack, patent, patents`
- Display key terms: `matter, shionogi, subject, apotex, lack, patent, patents`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: matter, shionogi, subject, apotex, lack, patent, patents Rule/authority context: It also submits that the Shionogi patents lack subject matter and that if there is anything novel and inventive in the original application, it would be the overall synthetic pathway that was not claimed in any of the Sh | Applicant must restrict his claims to a single subject matter under section 38 of the Act. Evidence spans paragraphs 370-373. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040616` offsets `243-248`; context: [370] Thus, in these proceedings, the merits of Apotex’s defence will be assessed on the basis that the defendant must establish on a balance of probabilities any fact which by virtue of the Patent Act or by law renders invalid the patents at issue, keeping in mind the applicable presumption as to their validity.
- Evidence: `governing_rule` cue `under` at chunk `5040617` offsets `384-389`; context: It also submits that the Shionogi patents lack subject matter and that if there is anything novel and inventive in the
original application, it would be the overall synthetic pathway that was not claimed in any of the Shionogi patents under review.
- Evidence: `governing_rule` cue `under` at chunk `5040619` offsets `552-557`; context: Applicant must restrict his claims to a single subject matter under section 38 of the Act.

#### 22183:17:subtheme:10 · paragraphs 374-376

- Raw key terms: `apotex, application, canada, case, commissioner, consolboard, court, divisional`
- Display key terms: `apotex, case, commissioner, consolboard, divisional`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: apotex, case, commissioner, consolboard, divisional Application context: Accordingly, on February 25, 1957, a divisional application was filed. | The Court has considered the said cross-examination[130] and finds that there is insufficient evidence to conclude that this case is distinguishable from the one before the Supreme Court of Canada in Consolboard (1981). Evidence spans paragraphs 374-376. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5040620` offsets `553-564`; context: Accordingly, on February 25, 1957, a divisional application was filed.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040621` offsets `629-638`; context: Murphy’s affidavit (E-20))
- Evidence: `evidence_fact` cue `evidence` at chunk `5040622` offsets `216-224`; context: The Court has considered the said cross-examination[130] and finds that there is insufficient evidence to conclude that this case is distinguishable from the one before the Supreme Court of Canada in Consolboard (1981).
- Evidence: `reasoning_application` cue `conclude` at chunk `5040622` offsets `228-236`; context: The Court has considered the said cross-examination[130] and finds that there is insufficient evidence to conclude that this case is distinguishable from the one before the Supreme Court of Canada in Consolboard (1981).

#### 22183:17:subtheme:11 · paragraphs 377-378

- Raw key terms: `ascertaining, classes, court, designed, device, directed, falls, lack`
- Display key terms: `ascertaining, classes, designed, device, directed, falls, lack`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: ascertaining, classes, designed, device, directed, falls, lack Rule/authority context: […] This enquiry, in the English cases usually discussed under the heading of obviousness, is directed to ascertaining whether […] its production was sufficiently important and worthy to entitle it to the grant of monopo Evidence spans paragraphs 377-378. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040623` offsets `17-22`; context: [377] Beyond the issue of whether or not the Shionogi applications resulted from a proper divisional, there was some dispute between the parties as to what it means for a patent to “lack subject matter”[131].
- Evidence: `issue` cue `whether` at chunk `5040624` offsets `100-107`; context: [378] However, Fox also speaks of a more restrictive meaning which in sum directs the inquiry as to whether the production of the device or process “was obvious or involved the exercise of the inventive faculty.
- Evidence: `governing_rule` cue `under` at chunk `5040624` offsets `269-274`; context: […] This enquiry, in the English cases usually discussed under the heading of obviousness, is directed to ascertaining whether […] its production was sufficiently important and worthy to entitle it to the grant of monopoly rights.

#### 22183:17:subtheme:12 · paragraphs 379-383

- Raw key terms: `apotex, patent, argument, claim, lilly, patents, process, complex`
- Display key terms: `apotex, patent, argument, lilly, patents, process, complex`
- Argument roles: `counterargument_limitation, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, party_position, reasoning_application Display terms: apotex, patent, argument, lilly, patents, process, complex Position/evidence statements: [134] As indicated when discussing obviousness, the Court is satisfied that there is at least one valid (unobvious)[135] claim at issue in each patent that is infringed. Rule/authority context: [379] Certainly, the heading which one chooses to present one’s argument cannot change the fact that one cannot have “two kicks at the can”[133] by simply presenting its position under distinct headings. Application context: [381] In respect of the first argument, having reviewed the case law submitted by Apotex,[136] the Court has no hesitation to conclude that it has no application whatsoever here. Evidence spans paragraphs 379-383. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040625` offsets `411-416`; context: [134] As indicated when discussing obviousness, the Court is satisfied that there is at least one valid (unobvious)[135] claim at issue in each patent that is infringed.
- Evidence: `party_position` cue `claim` at chunk `5040625` offsets `402-407`; context: [134] As indicated when discussing obviousness, the Court is satisfied that there is at least one valid (unobvious)[135] claim at issue in each patent that is infringed.
- Evidence: `governing_rule` cue `under` at chunk `5040625` offsets `179-184`; context: [379] Certainly, the heading which one chooses to present one’s argument cannot change the fact that one cannot have “two kicks at the can”[133] by simply presenting its position under distinct headings.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040627` offsets `126-134`; context: [381] In respect of the first argument, having reviewed the case law submitted by Apotex,[136] the Court has no hesitation to conclude that it has no application whatsoever here.
- Evidence: `counterargument_limitation` cue `although` at chunk `5040629` offsets `73-81`; context: In effect, as explained earlier, although Apotex uses the expression “subject matter”, to refer to the inventiveness, what Apotex is really saying is that there is only one invention, the allegedly new kinetic compound, and, by claiming it in the ‘007 patent, Lilly was not entitled to the Lilly process patents.

#### 22183:17:subtheme:13 · paragraphs 384-386

- Raw key terms: `argument, lilly, patent, apotex, application, applications, because, claim`
- Display key terms: `argument, lilly, patent, apotex, applications, because`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: argument, lilly, patent, apotex, applications, because Rule/authority context: The defendant also ought to know that, as indicated by the Supreme Court of Canada in Whirlpool and Sanofi, the inquiry of double patenting is directed to the claims and not to the disclosure of the various patents under Application context: [385] I say “modified double patenting” because Apotex ought to know that the ‘007 patent application, which was filed on the same day as the applications for the process patents (presumed date of the invention claimed g | Thus to accept Apotex’s argument would mean that, because Lilly complied with this practice, instead of filing an application that would necessarily raise an objection and result in a request for amendment – the filing o Evidence spans paragraphs 384-386. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040630` offsets `184-192`; context: In my view, it also calls into question longstanding Patent Office practices.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040631` offsets `240-248`; context: [385] I say “modified double patenting” because Apotex ought to know that the ‘007 patent application, which was filed on the same day as the applications for the process patents (presumed date of the invention claimed given the absence of evidence in respect of an earlier date), is not prior art that can be used to support an argument of double patenting (obviousness).
- Evidence: `governing_rule` cue `under` at chunk `5040631` offsets `588-593`; context: The defendant also ought to know that, as indicated by the Supreme Court of Canada in Whirlpool and Sanofi, the inquiry of double patenting is directed to the claims and not to the disclosure of the various patents under review.
- Evidence: `reasoning_application` cue `because` at chunk `5040631` offsets `40-47`; context: [385] I say “modified double patenting” because Apotex ought to know that the ‘007 patent application, which was filed on the same day as the applications for the process patents (presumed date of the invention claimed given the absence of evidence in respect of an earlier date), is not prior art that can be used to support an argument of double patenting (obviousness).
- Evidence: `evidence_fact` cue `evidence` at chunk `5040632` offsets `37-45`; context: [386] There is uncontradicted expert evidence (Affidavit of Mr.
- Evidence: `reasoning_application` cue `because` at chunk `5040632` offsets `435-442`; context: Thus to accept Apotex’s argument would mean that, because Lilly complied with this practice, instead of filing an application that would necessarily raise an objection and result in a request for amendment – the filing of divisional applications, its process patents can now be challenged on a basis that would not have otherwise been open to Apotex (Consolboard (1981)).

#### 22183:17:subtheme:14 · paragraphs 387-389

- Raw key terms: `different, divisional, double, improper, issued, merck, patent, patenting`
- Display key terms: `different, divisional, double, improper, issued, merck, patent, patenting`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: different, divisional, double, improper, issued, merck, patent, patenting Evidence spans paragraphs 387-389. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040633` offsets `122-130`; context: (FCA), the Federal Court of Appeal reviewed, albeit in a different context, the question of an improper divisional and its consequences at paras.
- Evidence: `evidence_fact` cue `found that` at chunk `5040633` offsets `299-309`; context: In fact, it found that the concept of double patenting provides for an adequate remedy in the event that more than one patent is issued for the same invention.

#### 22183:17:subtheme:15 · paragraphs 390-394

- Raw key terms: `canada, disclosure, document, prior, respect, anticipation, court, sanofi`
- Display key terms: `disclosure, document, prior, respect, anticipation, sanofi`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue Display terms: disclosure, document, prior, respect, anticipation, sanofi Rule/authority context: [390] The valid claims of these patents do not overlap and as discussed under obviousness, there is at least one unobvious claim at issue in each of them. Operative outcome context: However, at this stage of the inquiry (disclosure), the skilled person is not allowed to conduct experimentation as there is no room for trial and error, the prior art is simply to be read for the purposes of understandi Evidence spans paragraphs 390-394. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040636` offsets `132-137`; context: [390] The valid claims of these patents do not overlap and as discussed under obviousness, there is at least one unobvious claim at issue in each of them.
- Evidence: `governing_rule` cue `under` at chunk `5040636` offsets `72-77`; context: [390] The valid claims of these patents do not overlap and as discussed under obviousness, there is at least one unobvious claim at issue in each of them.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040640` offsets `152-159`; context: However, at this stage of the inquiry (disclosure), the skilled person is not allowed to conduct experimentation as there is no room for trial and error, the prior art is simply to be read for the purposes of understanding it.
- Evidence: `disposition` cue `allowed` at chunk `5040640` offsets `230-237`; context: However, at this stage of the inquiry (disclosure), the skilled person is not allowed to conduct experimentation as there is no room for trial and error, the prior art is simply to be read for the purposes of understanding it.

#### 22183:17:subtheme:16 · paragraphs 395-396

- Raw key terms: `disclosure, issue, advantages, although, authorities, beloit, best, canada`
- Display key terms: `disclosure, advantages, although, authorities, beloit, best`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: disclosure, advantages, although, authorities, beloit, best Evidence spans paragraphs 395-396. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040641` offsets `200-205`; context: 205 (Beloit), General Tire and Free World Trust is still relevant on the issue of disclosure, but the Beloit test has been refined in respect of enablement (see Sanofi paras.
- Evidence: `issue` cue `issue` at chunk `5040642` offsets `373-378`; context: If the latter, should the prior disclosure include only the essential elements of the claim at issue or all of the elements described in the said claim?
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040642` offsets `496-504`; context: Although these were duly considered, there is no need for a lengthy review of the authorities cited therein.

#### 22183:17:subtheme:17 · paragraphs 397-400

- Raw key terms: `claim, necessarily, apotex, claimed, compound, court, described, directed`
- Display key terms: `necessarily, apotex, claimed, compound, described, directed`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: necessarily, apotex, claimed, compound, described, directed Application context: This argument must also be rejected, not only because it is not in line with the inquiry at hand, but also because it leads to an absurd result. Evidence spans paragraphs 397-400. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040643` offsets `76-83`; context: [397] As mentioned, the inquiry the Court must carry out seeks to determine whether or not the matter performed in the prior art would necessarily constitute infringement.
- Evidence: `reasoning_application` cue `because` at chunk `5040644` offsets `382-389`; context: This argument must also be rejected, not only because it is not in line with the inquiry at hand, but also because it leads to an absurd result.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040644` offsets `434-437`; context: This argument must also be rejected, not only because it is not in line with the inquiry at hand, but also because it leads to an absurd result.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040646` offsets `124-133`; context: Baldwin quite early in his testimony that the kinetic complex would necessarily have been formed when Rydon did this particular experiment.

#### 22183:17:subtheme:18 · paragraphs 401-405

- Raw key terms: `compound, court, abbott, claims, described, fact, anticipated, applied`
- Display key terms: `compound, abbott, claims, described, fact, anticipated, applied`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: compound, abbott, claims, described, fact, anticipated, applied Rule/authority context: This is a perfect analogy and direct application of the principles established and applied by the Federal Court of Appeal in Abbott (2006) [142] at para. | But even if I were wrong in this regard, I would apply the principles stated and applied by my colleague Justice Hughes in Abbott (2008) at paras. Application context: This is a perfect analogy and direct application of the principles established and applied by the Federal Court of Appeal in Abbott (2006) [142] at para. | But even if I were wrong in this regard, I would apply the principles stated and applied by my colleague Justice Hughes in Abbott (2008) at paras. Evidence spans paragraphs 401-405. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `5040647` offsets `6-13`; context: [401] Whether one knew that the kinetic compound was formed or not is irrelevant, as is the fact that this compound would disappear if not stabilized or used quickly.
- Evidence: `governing_rule` cue `principles` at chunk `5040647` offsets `223-233`; context: This is a perfect analogy and direct application of the principles established and applied by the Federal Court of Appeal in Abbott (2006) [142] at para.
- Evidence: `reasoning_application` cue `applied` at chunk `5040647` offsets `250-257`; context: This is a perfect analogy and direct application of the principles established and applied by the Federal Court of Appeal in Abbott (2006) [142] at para.
- Evidence: `issue` cue `whether` at chunk `5040648` offsets `31-38`; context: [402] There was a debate as to whether or not the claims could be anticipated if the prior art did not clearly disclose the fact that the fastest forming compound of this reaction was a halogenating compound.
- Evidence: `governing_rule` cue `principles` at chunk `5040648` offsets `326-336`; context: But even if I were wrong in this regard, I would apply the principles stated and applied by my colleague Justice Hughes in Abbott (2008) at paras.
- Evidence: `reasoning_application` cue `apply` at chunk `5040648` offsets `316-321`; context: But even if I were wrong in this regard, I would apply the principles stated and applied by my colleague Justice Hughes in Abbott (2008) at paras.
- Evidence: `counterargument_limitation` cue `But` at chunk `5040648` offsets `267-270`; context: But even if I were wrong in this regard, I would apply the principles stated and applied by my colleague Justice Hughes in Abbott (2008) at paras.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040649` offsets `152-160`; context: The Court finds that on the whole of the evidence (with particular consideration of the testimony of Dr.
- Evidence: `governing_rule` cue `under` at chunk `5040651` offsets `56-61`; context: [405] The Court notes that in Abbott (2006), the claims under review also described the compound found to have been anticipated as an antibiotic.
- Evidence: `reasoning_application` cue `because` at chunk `5040651` offsets `219-226`; context: This, I believe, is because the claims in Abbott (2006), like the claim here, are not “use” claims and the reference to halogen compounds or antibiotics is simply descriptive of the claimed compound.

#### 22183:17:subtheme:19 · paragraphs 406-409

- Raw key terms: `anticipated, apotex, aromatic, claim, halogenated, process, rydon, solvent`
- Display key terms: `anticipated, apotex, aromatic, halogenated, process, rydon, solvent`
- Argument roles: `counterargument_limitation, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, party_position, reasoning_application Display terms: anticipated, apotex, aromatic, halogenated, process, rydon, solvent Position/evidence statements: [406] The parties are agreed that if claims 1 and 8 are anticipated, the only other claim of the ‘007 patent which requires a determination is claim 17. Rule/authority context: [143] However, in its additional submissions dealing specifically with the implications of Sanofi, Apotex does not discuss at all these patents under the heading of anticipation. Application context: [408] Apotex argued that the use of an aromatic of halogenated solvent is not inventive and that therefore, “there is no distinct patentable subject matter. | 57, Apotex appears to argue that the Lilly process patents were anticipated simply because the triaryl phosphite-halogen compound, which is one of the essential elements in all the claims in these patents, was not novel. Evidence spans paragraphs 406-409. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `5040652` offsets `37-43`; context: [406] The parties are agreed that if claims 1 and 8 are anticipated, the only other claim of the ‘007 patent which requires a determination is claim 17.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040653` offsets `178-185`; context: However, in that experiment, the ratio of Cl to TPP was 1:2, and as such this process could not infringe the process described in claim 17, which requires the use of equivalent amounts of those two substances.
- Evidence: `reasoning_application` cue `therefore` at chunk `5040654` offsets `97-106`; context: [408] Apotex argued that the use of an aromatic of halogenated solvent is not inventive and that therefore, “there is no distinct patentable subject matter.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040654` offsets `231-234`; context: ” It may well be that this essential element of claim 17 is not inventive, but that inquiry is distinct from the one being carried out to determine if the invention as claimed therein is novel.
- Evidence: `governing_rule` cue `under` at chunk `5040655` offsets `409-414`; context: [143] However, in its additional submissions dealing specifically with the implications of Sanofi, Apotex does not discuss at all these patents under the heading of anticipation.
- Evidence: `reasoning_application` cue `because` at chunk `5040655` offsets `128-135`; context: 57, Apotex appears to argue that the Lilly process patents were anticipated simply because the triaryl phosphite-halogen compound, which is one of the essential elements in all the claims in these patents, was not novel.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040655` offsets `271-278`; context: [143] However, in its additional submissions dealing specifically with the implications of Sanofi, Apotex does not discuss at all these patents under the heading of anticipation.

#### 22183:17:subtheme:20 · paragraphs 410-412

- Raw key terms: `patents, apotex, claims, none, obviousness, process, shionogi, subject`
- Display key terms: `patents, apotex, claims, none, obviousness, process, shionogi, subject`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: patents, apotex, claims, none, obviousness, process, shionogi, subject Rule/authority context: The Legal Test Evidence spans paragraphs 410-412. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040656` offsets `292-297`; context: [410] In the event that this is not so, the Court has carefully reviewed all of the prior art cited in respect of the Lilly process patents as well as Apotex’s expert reports and finds that there is not one single prior art document that discloses all the essential elements of the claims at issue in these process patents.
- Evidence: `governing_rule` cue `Legal Test` at chunk `5040657` offsets `313-323`; context: The Legal Test

#### 22183:17:subtheme:21 · paragraphs 413-415

- Raw key terms: `court, inquiry, obvious, obviousness, relevant, canada, claim, common`
- Display key terms: `inquiry, obvious, obviousness, relevant, common`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: inquiry, obvious, obviousness, relevant, common Rule/authority context: [413] In Sanofi, the Supreme Court of Canada reviewed the legal principles applicable to obviousness and took the opportunity to provide practical guidelines as to the approach that should be adopted in an obviousness in | The Court will be guided in that respect by the principles set out in paras. Application context: [414] In Sanofi, the Supreme Court of Canada also closed the debate as to whether the “obvious to try” test should be applied in Canada and if so, in what circumstances (generally paras. Evidence spans paragraphs 413-415. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040659` offsets `976-984`; context: 23:
In the result I would restate the Windsurfing questions thus:
(1) (a) Identify the notional "person skilled in the art";
(b) Identify the relevant common general knowledge of that person;
(2) Identify the inventive concept of the claim in question or if that cannot readily be done, construe it;
(3) Identify what, if any, differences exist between the matter cited as forming part of the "state of the art" and the inventive concept of the claim or the claim as construed;
(4) Viewed without any knowledge of the alleged invention as claimed, do those differences constitute steps which would have been obvious to the person skilled in the art or do they require any degree of invention?
- Evidence: `governing_rule` cue `principles` at chunk `5040659` offsets `64-74`; context: [413] In Sanofi, the Supreme Court of Canada reviewed the legal principles applicable to obviousness and took the opportunity to provide practical guidelines as to the approach that should be adopted in an obviousness inquiry.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5040659` offsets `996-1002`; context: 23:
In the result I would restate the Windsurfing questions thus:
(1) (a) Identify the notional "person skilled in the art";
(b) Identify the relevant common general knowledge of that person;
(2) Identify the inventive concept of the claim in question or if that cannot readily be done, construe it;
(3) Identify what, if any, differences exist between the matter cited as forming part of the "state of the art" and the inventive concept of the claim or the claim as construed;
(4) Viewed without any knowledge of the alleged invention as claimed, do those differences constitute steps which would have been obvious to the person skilled in the art or do they require any degree of invention?
- Evidence: `issue` cue `whether` at chunk `5040660` offsets `74-81`; context: [414] In Sanofi, the Supreme Court of Canada also closed the debate as to whether the “obvious to try” test should be applied in Canada and if so, in what circumstances (generally paras.
- Evidence: `governing_rule` cue `principles` at chunk `5040660` offsets `250-260`; context: The Court will be guided in that respect by the principles set out in paras.
- Evidence: `reasoning_application` cue `applied` at chunk `5040660` offsets `118-125`; context: [414] In Sanofi, the Supreme Court of Canada also closed the debate as to whether the “obvious to try” test should be applied in Canada and if so, in what circumstances (generally paras.

#### 22183:17:subtheme:22 · paragraphs 416-417

- Raw key terms: `individual, mosaicing, prior, application, authors, citation, common, confronted`
- Display key terms: `individual, mosaicing, prior, authors, citation, common, confronted`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: individual, mosaicing, prior, authors, citation, common, confronted Evidence spans paragraphs 416-417. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040662` offsets `69-74`; context: [416] Before turning to the application of the law to the patents at issue, it is worth saying a few words about “mosaicing” as this illustrates what one needs to establish before the Court can consider together individual prior art publications that are not necessarily part of the common general knowledge.
- Evidence: `issue` cue `Whether` at chunk `5040663` offsets `303-310`; context: Whether he would do so is a question of fact.

#### 22183:17:subtheme:23 · paragraphs 418-419

- Raw key terms: `common, considered, find, general, itself, justice, knowledge, light`
- Display key terms: `common, considered, find, itself, justice, knowledge, light`
- Argument roles: `counterargument_limitation, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, reasoning_application Display terms: common, considered, find, itself, justice, knowledge, light Application context: This will be particularly likely where the pleaded prior art encourages him to do so because it expressly cross-refers to other material. Evidence spans paragraphs 418-419. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040664` offsets `249-257`; context: 66:
When any piece of prior art is considered for the purposes of an obviousness attack, the question asked is ‘what would the skilled addressee think and do on the basis of this disclosure’?
- Evidence: `reasoning_application` cue `because` at chunk `5040664` offsets `674-681`; context: This will be particularly likely where the pleaded prior art encourages him to do so because it expressly cross-refers to other material.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040664` offsets `727-734`; context: However, I do not think it is limited to cases where there is an express cross-reference.
- Evidence: `issue` cue `question` at chunk `5040665` offsets `1450-1458`; context: The question whether it is obvious to read two documents together is one to be considered in the light of the particular circumstances of each case.

#### Section text

[327] I do not take Justice Snider’s list to be exhaustive or to limit in any way the test applicable in Canada. There is nothing in what she proposed that prevents the Court from also considering whether the imported product was obtained directly from the patented process or whether the compound made by the patented process was materially changed or has become a trivial or non-essential component of the imported product. In fact, these concepts are very close to those she used, her list is obviously more detailed as our test is more flexible and as mentioned, this is rightly so.

[328] The value of our approach is that it can be adapted to new circumstances. The Courts in Beecham Group were able to conclude to infringement despite the fact that the final ingredient imported in England no longer contained the compound made using the patented processes. It was the flexibility of the test that enabled them to do so and to look at what happened in the stomachs of the patients who actually bought and used the pills made by the defendant.

[329] For these reasons, not only do I conclude that the Court cannot redefine and limit the test applicable in Canada with respect to infringement by importation and use, but also that I should not do so. On this basis, I will now proceed to apply these principles to the facts of this case.

[330] In respect of the Shionogi patents, it is not disputed that if the Kyong Bo process had been carried out in Canada, it would have infringed the Shionogi patents.[118]

[331] It was also clear, in my view, that Lupin used the process covered by the Lilly patents until 1998.[119]

[332] The only real difficulty in applying the test in this case arises from the fact that making cefaclor is a very complex process[120], involving more steps than what was required to make the various compounds previously discussed in the case law. But this alone should not prevent the application of the doctrine. Certainly technical complexity should not enable a party to deprive in whole or in part, directly or indirectly, of the full enjoyment of the monopoly conferred by a patent.

[333] It is not disputed that there are other steps (chemical reactions) that take place after Lupin and Kyong Bo obtained either the 3-chloro-cephem or the 3-hydroxy-cephem compounds (which are the end compounds of the patented processes) to make cefaclor. Nor is it contested that the 3-chloro-cephem and the 3-hydroxy-cephem are changed into an ultimately different chemical compound (cefaclor) by these additional steps.

[334] All the experts agreed that there was no known method to make cefaclor without going through the 3-hydroxy-cephem compound.

[335] None of the experts opine that either patented process was a trivial or unessential part of the processes used by Kyong Bo or Lupin (Process “A”) to produce the cefaclor used by Apotex in Canada.

[336] On the whole of the evidence, it is clear that the Shionogi and Lilly processes were more efficient (and therefore less costly) than any other alternative discussed in any of the publications referred to by the experts or used by Lupin.[121]

[337] In fact, in respect of the Lilly process, there is clear evidence that to change what is described in Lupin’s documentation simply as step V (although it involves three distinct reactions) resulted in an increase of almost 50% of the price of cefaclor.[122]

[338] As discussed, the disclosure of the Lilly process patents expressly states that the inventions are particularly useful to make cefaclor. This is the very purpose for which their teachings were used here.

[339] Apotex relied heavily on a 1978 progress report from Lilly’s research team working on cefaclor (TX-211). Interestingly it states, at p. 3 that:
The two most difficult steps in the cefaclor synthesis, in terms of time and effort expended, are the exomethylene ring expansion (Dr. T.S. Chou) and the enol chlorination (79284 → 112069). Very few processes have been as extensively investigated as these two synthetic steps for cefaclor.

[340] Having considered and weighed all the evidence, I conclude that, as a matter of fact, Lilly’s patented process was an “important” part of the method used by Lupin to make the cefaclor that was used by Apotex in Canada.

[341] I have also concluded that the Shionogi process was a crucial, thus obviously important, part of the Kyong Bo process for making cefaclor. Without it, Kyong Bo could not have used the total synthetic pathway described in its technical documentation filed with Health Canada.
5.6. The Exemption Under Subsection 55.2(1) of the Patent Act

[342] Subsection 55.2(1) provides:
55.2(1) It is not an infringement of a patent for any person to make, construct, use or sell the patented invention solely for uses reasonably related to the development and submission of information required under any law of Canada, a province or a country other than Canada that regulates the manufacture, construction, use or sale of any product.
55.2(1) Il n’y a pas contrefaçon de brevet lorsque l’utilisation, la fabrication, la construction ou la vente d’une invention brevetée se justifie dans la seule mesure nécessaire à la préparation et à la production du dossier d’information qu’oblige à fournir une loi fédérale, provinciale ou étrangère réglementant la fabrication, la construction,
l’utilisation ou la vente d’un produit.
It is admitted that this defence was included in the particulars filed by Apotex but Lilly argues that the statement of defence was never amended and thus it was not properly pleaded. There is no dispute that Lilly was fully aware that Apotex would rely on this exemption. Although strictly speaking Lilly is correct, it is obvious that in the present circumstances there is no good reason to deprive Apotex of the right to raise this defence.

[343] The only substantive argument advanced by Lilly is that, based on Ms. Carrière’s testimony, the in-process sampling and the reserve samples were not set aside simply to meet government requirements but also for internal quality controls (which addresses business, not regulatory, imperatives). Lilly argues that in light of this dual purpose, the exemption cannot apply to such material. Lilly also says that Apotex has not established that its records are consistent and complete and that the quantities set out in the documentation prepared by Mr. Fahner were only used for the purposes set out in subs. 55.2(1) of the Patent Act.

[344] The argument that this exemption should be strictly construed has been rejected by the Federal Court of Appeal in Merck & Co. v. Apotex Inc., 2006 FCA 323, [2007] 3 F.C.R. 588 (Merck & Co. (FCA)) (paras. 103-104). In that decision and in Laboratoires Servier the Courts did not limit the exemption solely to material actually provided to a regulator. What is critical here is that the Court is satisfied that the materials purported to have been used for research and development formulation, reserve samples and in-process sampling were not sold or used for any similar purpose.[123] The fact that these quantities could serve a dual purpose is, in my view, irrelevant.

[345] As for the actual amount of bulk cefaclor covered by the exemption, the Court agrees that the exact quantities described in the document prepared by Mr. Fahner[124] as a result of his cross-examination and attached to a letter from counsel for Apotex dated May 12, 2008, shall be the subject of the reference in order to determine what quantities properly fall under the above-mentioned categories. This being, the amounts described in this document represent the maximum quantities which can be considered for the purpose of the exemption (187 kilos).

[346] Both parties recognize that this is not a major issue in this case and thus there is nothing more to say.
6. Invalidity

[347] It has been agreed that as all of the patents in suit have now expired, there is no need to deal with the portion of the counter-claim seeking a declaration that said patents are void. All findings concerning invalidity are thus made in the context of the main action.
6.1. Standard of Review and Burden of Proof

[348] It is common ground between the parties that Apotex, as the party attacking the validity of Lilly’s patents, bears the burden of proof with respect to invalidity. Such is the effect of subs. 43(2) and s. 59 of the Patent Act.

[349] Nor do the parties disagree on the applicable standard of proof. As the Supreme Court of Canada recently confirmed, “there is only one civil standard of proof at common law and that is proof on a balance of probabilities.” (F.H. v. McDougall, 2008 SCC 53, [2008] 3 S.C.R. 41, at para. 40).

[350] While agreeing on the onus and the standard of proof with respect to invalidity, Lilly and Apotex disagree on what a party asserting invalidity must prove. Lilly argues that Apotex must prove that the decision of the Commissioner of Patents to approve the patents at issue was unreasonable. In support of this proposition, Lilly relies on the following passage from Apotex Inc. v. Wellcome Foundation Ltd., 2002 SCC 77, [2002] 4 S.C.R. 153 (Wellcome (2002)):
Unlike the Harvard Mouse case (Harvard College v. Canada (Commissioner of Patents), [2002] 4 S.C.R. 45, 2002 SCC 76), released concurrently, these appeals are not limited to a question of law (i.e., the statutory limits of patentable subject matter). On that issue, the standard is correctness. The issue here is one of mixed fact and law, namely, was the Commissioner properly satisfied the claimed invention met the statutory test of utility? Fact finding generally commands deference, but here Parliament has provided an unfettered right of appeal to the Federal Court (Patent Act, s. 42).
[…]
In the circumstances, I think the appropriate standard of review of these issues, which largely raise mixed questions of law and fact, is reasonableness simpliciter, i.e., that the Commissioner's decision must withstand a somewhat probing examination (Canada (Director of Investigation and Research) v. Southam Inc., [1997] 1 S.C.R. 748, at para. 56).
[Emphasis added. Paras. 42 and 44.[125]]

[351] In effect, relying on Wellcome (2002), Lilly argues that s. 59 of the Patent Act requires a party asserting invalidity to engage in a form of judicial review of the Commissioner’s “decision” to grant an impugned patent. Furthermore, Lilly argues that deference is owed, and that the standard of reasonableness should apply.

[352] In Whirlpool, the Supreme Court of Canada put plainly the task faced by a party asserting invalidity: “The burden was on the appellants to prove on a balance of probabilities, that the patent was invalid” (para. 92). In so doing, the party attacking validity must establish that the patent, or claims within a patent, do not meet the requirements for patentability under the Patent Act (i.e. obviousness, utility, etc.). This requires one to examine the claims of a patent, properly constructed, against the requirements of the Patent Act (see Free World Trust at paras. 24-27).

[353] This is perfectly in line with the wording in s. 59 of the Patent Act which speaks of “any fact or default which by this Act or by law renders the patent void” and directs the Court to “take cognizance of that pleading and of the facts and decide accordingly.”

[354] The approach to validity, assessing claims against the requirements of the Patent Act, without reference to principles of administrative law, has been the standard judicial practice for more than a hundred years.

[355] It cannot be presumed that just two years after Free World Trust and Whirlpool, the Supreme Court of Canada sought to drastically modify the law with respect to invalidity in an implicit fashion with its decision in Wellcome (2002). One would expect such a shift to be done clearly and in express terms. The fact that the bulk of the jurisprudence since Wellcome (2002) has considered invalidity without resort to administrative law principles buttresses this conclusion. (See Laboratoires Servier, para. 225; M.K. Plastics Corp. v. Plasticair Inc., 2007 FC 574, 61 C.P.R. (4th) 1, para. 105.)

[356] Although it is clear that in Wellcome (2002), the Court was dealing with an action of infringement and a defence of invalidity in its administrative law analysis, the Supreme Court references s. 42[126] (now s. 41) of the Patent Act, which deals with the right to appeal from a decision of the Commissioner to refuse the grant of a patent to the Federal Court. The defence of invalidity and appeal from a refusal by the Commissioner to grant a patent implicates different actors (putative patentee v. alleged infringer) raising similar issues but in very different contexts.

[357] Furthermore, despite having imported administrative law principles into the invalidity analysis, neither Wellcome (2002) and Monsanto Canada Inc. actually applies concepts such as the degree of deference owed to the decision of the Commissioner to grant the patents at issue. In fact, notwithstanding the above referenced paragraphs of these decisions, the term “reasonableness” is not even used in assessing invalidity.

[358] A telling example of the unease created by those decisions can be found in Jay-Lor International Inc. v. Penta Farm Systems Ltd., 2007 FC 358, 59 C.P.R. (4th) 228, where Justice Snider was confronted with a patent infringement claim and defence of invalidity. In discussing the issue of validity, Justice Snider stated:
Once a patent is issued, there is a presumption that, in the absence of evidence to the contrary, the patent is valid (Patent Act, s. 43(2)). The onus is thus on the Defendants to show that the Commissioner of Patents erred in allowing the patent (Monsanto Canada Inc. v. Schmeiser, 2004 SCC 34 at para. 24, [2004] 1 S.C.R. 902; Apotex Inc. v. Wellcome Foundation Ltd., 2002 SCC 77, [2002] 4 S.C.R. 153 at paras. 43-44, 21 C.P.R. (4th) 499). In this case, the Defendants argue that the patent is invalid because it was both obvious and anticipated. I will consider each of these arguments.
[para. 72]
Having made this observation, however, nowhere in her reasons does Justice Snider engage in anything resembling a reasonableness review akin to that which was set out in Dunsmuir v. New Brunswick, 2008 SCC 9, [2008] 1 S.C.R. 190 (Dunsmuir). In fact, the words “deference” and “reasonableness” (in an administrative law sense) appear nowhere in the decision, nor is there any reference (beyond the above quote) to the decision of the Commissioner to grant the patent at issue.[127]

[359] Such an attitude is understandable for there are a number of reasons why an administrative law approach to invalidity is almost impossible to apply without further guidance from Canada’s highest Court.

[360] In effect, it is unclear what would be the subject of this judicial review. A decision by the Commissioner to grant a patent comes with no reasons, no explanation, and no context. Indeed, a patent’s prosecution history cannot be reviewed in construing the claims of a patent (Merck & Co. (FCA), para. 53).

[361] A reasonableness review involves determining whether a decision falls within a range of possible acceptable outcomes on the basis of the evidence before the original decision maker (Dunsmuir, para. 47). If, as Wellcome (2002) suggests, the Commissioner’s decision to grant a patent is owed some matter of deference, how would a reviewing court assess reasonableness without access to the material considered by the decision-maker? Although the Supreme Court of Canada left the door open in Free World Trust (para. 67) as to whether prosecution history can be relevant for a purpose other than defining the scope of the grant of the monopoly, it has never been used for the purpose of deciphering the Commissioner’s reasons for granting a patent.

[362] A court engaged in judicial review, regardless of the standard applied, is usually limited to only considering the evidence that was before the decision-maker (Gosselin v. Canada (Attorney General), 2006 FC 3, 289 F.T.R. 7, paras. 12-13). This has not been the case when courts are engaged in examining allegations of invalidity, with respect to a patent.

[363] There is no statutory requirement that the evidence before the Commissioner of Patents be provided to the Federal Court in the context of an infringement action. Furthermore, nothing in s. 59 of the Patent Act limits a party challenging the validity of a patent to the evidence that was put before the Commissioner of Patents.

[364] Parties challenging validity have always been free, subject to the applicable rules of evidence, to put forth any evidence that may serve to undermine the validity of a patent’s claims. Standards of review are neither useful nor designed to address situations where the evidentiary record before the Court is different than the one before another decision-maker.

[365] In the Harvard College (2000) decision, Chief Justice Isaac referred by analogy to appeals from decisions of the Registrar of Trade-Marks under s. 56 of the Trade-Marks Act, R.S.C. 1985, c. T-13. In such cases, standards of review only apply where there is no new evidence that could have affected the decision of the Registrar. If the Court concludes that there is such evidence, then the Court must exercise its discretion de novo. It should be noted that the Registrar of Trade-Marks must give reasons for his or her decision, which can then be the subject of an assessment by the Court.

[366] To be certain, administrative law principles have been applied to certain decisions of the Commissioner of Patents (See e.g. Genencor International, Inc. v. Canada (Commissioner of Patents), 2008 FC 608, [2009] 1 F.C.R. 361 (reviewing a decision of the Commissioner on a re-examination under ss. 48.1 – 48.5 of the Patent Act); Pason Systems Corp. v. Canada (Commissioner of Patents), 2006 FC 753, [2007] 2 F.C.R. 269 (reviewing a decision of the Commissioner in respect of alleged clerical corrections under s. 8 of the Patent Act); and, Dow Chemical Co. v. Canada (Attorney General), 2007 FC 1236, 63 C.P.R. (4th) 89).

[367] With respect of some of the decisions of the Commissioner, a statutory right of appeal to the Federal Court is provided (see s. 19.2, subs. 20(15) and s. 41 of the Patent Act). However, where administrative law principles have been applied to decisions of the Commissioner of Patents, it has been in the context where these are amenable to judicial review and not pursuant to s. 59 and subs. 60(1) of the Patent Act.

[368] It may very well be that the material effect or consequence of a finding of invalidity is that the Commissioner “erred” in granting a patent. But, in the context of an action for infringement where a defence of invalidity is raised, that is not the essential point of departure: the claims stand alone to determine if the monopoly granted meets the test set out in the Act, for example in respect of utility, novelty and inventiveness.

[369] In sum, the importation of administrative law principles into the assessment of invalidity has not been thoroughly canvassed by appellate authorities and would constitute a significant departure from the Supreme Court of Canada’s well-established jurisprudence concerning pleas of invalidity. Absent further clarification on how the concept of deference is to be integrated into the established invalidity analysis, the Court is reluctant to employ administrative law principles in its analytic framework in this regard.

[370] Thus, in these proceedings, the merits of Apotex’s defence will be assessed on the basis that the defendant must establish on a balance of probabilities any fact which by virtue of the Patent Act or by law renders invalid the patents at issue, keeping in mind the applicable presumption as to their validity.
7. Inherency and Lack of Subject Matter
7.1. Shionogi Patents

[371] Apotex argues that the Commissioner of Patents did not force Shionogi to file 

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 22183:18 · paragraphs 420-435

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `169291d76beeb6090975930aed48b14834c6dc09ac419ed0c20a37c7d2ea3214`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:18:subtheme:1 · paragraphs 420-423

- Raw key terms: `article, date, evidence, knowledge, post, relevant, review, used`
- Display key terms: `article, date, knowledge, post, relevant, review, used`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, reasoning_application Display terms: article, date, knowledge, post, relevant, review, used Rule/authority context: For example, one cannot simply assume that because there is no mention of the invention under review in the article, its author was unaware of such developments. Application context: For example, one cannot simply assume that because there is no mention of the invention under review in the article, its author was unaware of such developments. Evidence spans paragraphs 420-423. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040667` offsets `129-137`; context: [421] It is evident that in certain specific circumstances, literature published after the filing date[148] can be considered as evidence of what was commonly known or what was part of the state of the art at the relevant time.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040669` offsets `59-67`; context: [423] The Court agrees that this may constitute admissible evidence if introduced by an expert, but one must be careful not to cross the line and treat such art on the same footing as prior art.
- Evidence: `governing_rule` cue `under` at chunk `5040669` offsets `283-288`; context: For example, one cannot simply assume that because there is no mention of the invention under review in the article, its author was unaware of such developments.
- Evidence: `reasoning_application` cue `because` at chunk `5040669` offsets `238-245`; context: For example, one cannot simply assume that because there is no mention of the invention under review in the article, its author was unaware of such developments.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040669` offsets `96-99`; context: [423] The Court agrees that this may constitute admissible evidence if introduced by an expert, but one must be careful not to cross the line and treat such art on the same footing as prior art.

#### 22183:18:subtheme:2 · paragraphs 424-435

- Raw key terms: `posita, rydon, apotex, patent, acknowledged, court, described, discussed`
- Display key terms: `posita, rydon, apotex, patent, acknowledged, described, discussed`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: posita, rydon, apotex, patent, acknowledged, described, discussed Position/evidence statements: [429] The Court is satisfied that it has been established that the posita would be familiar with the aromatic and hydrocarbon solvents discussed in claim 17, including methylene chloride and chlorobenzene. Rule/authority context: [425] The Court will now apply these principles to the patents under review. Application context: [425] The Court will now apply these principles to the patents under review. | [157] Lilly, however, contests that they form part of the posita’s common general knowledge because of the differences of opinion between the experts as to their meaning and exactly what they teach. Evidence spans paragraphs 424-435. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040670` offsets `91-98`; context: [424] Also, in the absence of evidence from or about the authors, how is the Court to know whether what they did was what a posita (objective test) would have done before the filing date?
- Evidence: `evidence_fact` cue `evidence` at chunk `5040670` offsets `30-38`; context: [424] Also, in the absence of evidence from or about the authors, how is the Court to know whether what they did was what a posita (objective test) would have done before the filing date?
- Evidence: `governing_rule` cue `principles` at chunk `5040671` offsets `37-47`; context: [425] The Court will now apply these principles to the patents under review.
- Evidence: `reasoning_application` cue `apply` at chunk `5040671` offsets `25-30`; context: [425] The Court will now apply these principles to the patents under review.
- Evidence: `party_position` cue `claim` at chunk `5040675` offsets `148-153`; context: [429] The Court is satisfied that it has been established that the posita would be familiar with the aromatic and hydrocarbon solvents discussed in claim 17, including methylene chloride and chlorobenzene.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040678` offsets `412-420`; context: The plaintiffs also argued that Apotex failed to provide any direct evidence in that respect.
- Evidence: `reasoning_application` cue `because` at chunk `5040678` offsets `237-244`; context: [157] Lilly, however, contests that they form part of the posita’s common general knowledge because of the differences of opinion between the experts as to their meaning and exactly what they teach.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040678` offsets `158-165`; context: [157] Lilly, however, contests that they form part of the posita’s common general knowledge because of the differences of opinion between the experts as to their meaning and exactly what they teach.

#### Section text

[420] There was also some debate as to the use of post art, which warrants some comments.

[421] It is evident that in certain specific circumstances, literature published after the filing date[148] can be considered as evidence of what was commonly known or what was part of the state of the art at the relevant time. For instance, the Sammes article,[149] which purports to review recent chemistry of the β-lactam antibiotics, though published after the relevant date, could be used to establish what a diligent search in the relevant field would have uncovered.[150] In effect, it expressly states that the literature discussed therein was selected from what was published up to the beginning of 1974[151] and was intended to complement recent books and reviews that were published well before the filing date (which were not all discussed by the experts)[152]. At the end of the trial, the parties were agreed that the literature referred therein would be part of the common general knowledge of the addressee of all the process patents.

[422] Apotex argues that Tseng and Michalski can be used to show what the posita would have learned from reproducing the experiments set out in Rydon and in Coe, with the benefit of 31P NMR spectroscopy.

[423] The Court agrees that this may constitute admissible evidence if introduced by an expert, but one must be careful not to cross the line and treat such art on the same footing as prior art. For example, one cannot simply assume that because there is no mention of the invention under review in the article, its author was unaware of such developments. Once a patent application is filed, inventors will often more freely discuss their findings with colleagues and friends outside of their institution and not necessarily in the context of public conferences. Thus, it may be very difficult to ascertain if indeed the author of a post art publication really did his work without knowledge of the invention. This was obviously one of the main considerations for setting the date of the invention as the relevant date for the obviousness inquiry in the pre-1989 era.[153]

[424] Also, in the absence of evidence from or about the authors, how is the Court to know whether what they did was what a posita (objective test) would have done before the filing date? Were the authors super skilled? Were they inventive? Did they go beyond what would be routinely done by a posita? Did they have a special motivation to do the things they did? All this to say that the probative weight of this evidence will depend on the circumstances, particularly on the evidence of the expert using it and often on whether it is used simply to corroborate an opinion reached independently by an expert available for cross-examination by the other party.

[425] The Court will now apply these principles to the patents under review.
9.2. The ‘007 Patent (Claim 17)

[426] Apotex submits that it has established that the kinetic complex would necessarily be produced using the method described in Rydon, reacting one to one equivalents of Cl and TPP.[154] Thus, a posita practising the method of the prior art or routine variations of it with the benefit of 31P NMR spectroscopy[155] would easily discover that it produces the so-called kinetic product.

[427] Apotex adds that it would be more or less self-evident to a posita that aromatic or halogenated hydrocarbon solvents (such as methylene chloride or chlorobenzene) could successfully be used in such a process.
9.2.1. The Person Skilled in the Art

[428] I shall use the definition of the posita found at para. 92.
9.2.2. Relevant Common General Knowledge

[429] The Court is satisfied that it has been established that the posita would be familiar with the aromatic and hydrocarbon solvents discussed in claim 17, including methylene chloride and chlorobenzene. The posita would equally be aware of the properties of such solvents.[156]

[430] A posita would also be familiar with 31P NMR spectroscopy and would have a working knowledge of how to use it to identify phosphorus compounds, if and when necessary.

[431] Disproportionation is a general type of chemical process which would be known to the posita.
9.2.3. Rydon, Coe and Ramirez

[432] It is clear that Rydon and Coe are part of the relevant prior art, for these publications are expressly acknowledged as such in the patent.[157] Lilly, however, contests that they form part of the posita’s common general knowledge because of the differences of opinion between the experts as to their meaning and exactly what they teach. The plaintiffs also argued that Apotex failed to provide any direct evidence in that respect. Given the admission contained in the patent, such debate is futile and it can have no impact on my conclusion regarding the obviousness inquiry.

[433] Apotex and its experts spent much time explaining why they believe that what is called the thermodynamic product and described as a dihalide ((PhO)3PCl2) in the ‘007 patent is in fact, in their view, the monohalide ((PhO)4PCl) discussed in Rydon, while the kinetic compound would be the dihalide. Drs. Modro and Olah also explained how they understood the various reactions taking place including how, in their view, the thermodynamic product resulted from a disproportionation of the kinetic product.

[434] For our purposes, determining the stoichiometry of the thermodynamic product is a debate that need not be settled, especially when one considers that Dr. McClelland did not appear to agree with the views of Drs. Modro, Chivers and Olah and testified during his cross-examination that in any event, the nature of the thermodynamic is still not well understood today. Dr. Chivers also acknowledged that two experts could read Rydon differently. In that respect, Dr. Baldwin wisely said that he did not really know the answer. For him, these publications were difficult to read and understand and there is no indication that the authors recognized the significance of “first formed intermediate”.

[435] It is acknowledged by all that Rydon, Coe, Ramirez or any other publication that will be discussed in relation to the ‘007 patent, do not refer to, or even mention, disproportionation to explain the relationship between the monohalide and the dihalide described in Rydon. With respect to the various mechanisms at play, including the reaction between Cl and TPP, Dr. Hunter noted that one would need to do a Ph.D. on the subject to fully understand them.

## 22183:19 · paragraphs 436-705

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3f5270c12a7b82f51312f46837e0765080d825e6871e326aa4206d6a1aba7a09`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:19:subtheme:1 · paragraphs 436-450

- Raw key terms: `rydon, solvent, apotex, reaction, respect, aromatic, court, dihalide`
- Display key terms: `rydon, solvent, apotex, reaction, respect, aromatic, dihalide`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: rydon, solvent, apotex, reaction, respect, aromatic, dihalide Application context: [447] One would think that, if a solvent is obvious for any reason, it is sufficient to conclude the present inquiry in respect of this element of the inventive concept. | [450] Having carefully examined the evidence and considered the motivation for as well as the details of how the inventors made their discovery, the Court concludes that Apotex has not established on a balance of probabi Evidence spans paragraphs 436-450. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040683` offsets `951-959`; context: 3053 of Rydon, which is the only synthesis known in hexane in evidence before the Court.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040689` offsets `90-98`; context: [443] At first, the Court was sympathetic to this argument, but on a closer review of the evidence, the Court realized that it may well have been influenced by knowledge gained from the ‘007 patent.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040692` offsets `204-212`; context: [446] First, with respect to the skilled addressee’s knowledge of solvents suitable for cephalosporin chemistry, given the definition of the skilled addressee in the ‘007 patent, it is not clear how this evidence would be relevant.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040693` offsets `88-96`; context: [447] One would think that, if a solvent is obvious for any reason, it is sufficient to conclude the present inquiry in respect of this element of the inventive concept.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040695` offsets `74-82`; context: [449] Apotex certainly did not explain how the Court should deal with the evidence of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040696` offsets `36-44`; context: [450] Having carefully examined the evidence and considered the motivation for as well as the details of how the inventors made their discovery, the Court concludes that Apotex has not established on a balance of probabilities that it would be more or less self-evident that the use of an aromatic or halogenated hydrocarbon solvent to carry out the reaction described in at p.
- Evidence: `reasoning_application` cue `concludes` at chunk `5040696` offsets `155-164`; context: [450] Having carefully examined the evidence and considered the motivation for as well as the details of how the inventors made their discovery, the Court concludes that Apotex has not established on a balance of probabilities that it would be more or less self-evident that the use of an aromatic or halogenated hydrocarbon solvent to carry out the reaction described in at p.

#### 22183:19:subtheme:2 · paragraphs 451-483

- Raw key terms: `product, rydon, tseng, evidence, posita, reaction, ramirez, respect`
- Display key terms: `product, rydon, tseng, posita, reaction, ramirez, respect`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: product, rydon, tseng, posita, reaction, ramirez, respect Rule/authority context: [479] It was also known in 1978 that various phosphorus compounds (including PCl5) could reduce sulfoxides in general (as opposed to the more complex cephem cephalosporin sulfoxides under review). Application context: [451] In my view, this is sufficient to conclude that claim 17 is not obvious. | 5 ppm shift (in deuterated chloroform) he obtained from the reaction of Cl and TPP without solvent was “likely to be” that of tetraphenoxyphosphorane because it was similar to the shift reported for that substance by Nes Evidence spans paragraphs 451-483. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040697` offsets `83-90`; context: For whether or not one could actually identify the compound formed through the use of 31P NMR spectroscopy is irrelevant if Rydon in fact taught away from the use of the claimed solvent.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040697` offsets `40-48`; context: [451] In my view, this is sufficient to conclude that claim 17 is not obvious.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040698` offsets `72-80`; context: [452] However, as this matter may go further, it is worth reviewing the evidence in respect of what the posita would learn through the allegedly routine use of such technology.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040701` offsets `60-68`; context: [455] To determine what weight should be attributed to such evidence (particularly the post art) the Court will quickly review how Apotex’s experts used this information.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040706` offsets `11-19`; context: [460] This evidence is not particularly helpful to determine if, through the use of this technology and by simply repeating the process set out in Rydon (Example B, p.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040707` offsets `217-225`; context: The Court accepts this evidence and notes that it is somewhat corroborated by Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040708` offsets `35-43`; context: [462] However, there is no similar evidence in respect of the method and the temperature used by the authors of Michalski when they reacted the TPP with the halogen.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040709` offsets `29-37`; context: [463] That said, there is no evidence that the method used (31P NMR) for the experiments performed in Ramirez was not in accordance with the practice of positas as of the filing date.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040710` offsets `29-37`; context: [464] Certainly, there is no evidence that a posita would, as a matter of routine, take and analyze 31P NMR spectras of the product of the reaction over a period of 23 hours.
- Evidence: `reasoning_application` cue `because` at chunk `5040713` offsets `399-406`; context: 5 ppm shift (in deuterated chloroform) he obtained from the reaction of Cl and TPP without solvent was “likely to be” that of tetraphenoxyphosphorane because it was similar to the shift reported for that substance by Nesterov in what Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040714` offsets `23-31`; context: [468] There is also no evidence that Ramirez or Tseng[178] discuss the disproportionation mechanism referred to by Drs.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040717` offsets `115-123`; context: [471] Sanofi teaches that in some circumstances, the means by which the inventor reached the invention may provide evidence in support of a particular conclusion on obviousness.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040718` offsets `108-115`; context: However, the path followed by the inventor does not shed much new light in respect of claim 17 of the ‘007 patent.
- Evidence: `governing_rule` cue `under` at chunk `5040725` offsets `182-187`; context: [479] It was also known in 1978 that various phosphorus compounds (including PCl5) could reduce sulfoxides in general (as opposed to the more complex cephem cephalosporin sulfoxides under review).
- Evidence: `counterargument_limitation` cue `However` at chunk `5040727` offsets `295-302`; context: However, PCl3 could not be used alone to perform such cleavage.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040729` offsets `104-113`; context: Baldwin’s affidavit would be heightened by the fact that the literature reported that usual methods for reducing sulfoxides would not work with cephalosporins.

#### 22183:19:subtheme:3 · paragraphs 484-488

- Raw key terms: `drabowicz, dreux, reducing, sulfoxides, according, agent, baldwin, common`
- Display key terms: `drabowicz, dreux, reducing, sulfoxides, according, agent, baldwin, common`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: drabowicz, dreux, reducing, sulfoxides, according, agent, baldwin, common Rule/authority context: [484] This article, entitled “Deoxygenation of Sulfoxides under Mild Conditions with a New Reducing Agent: 2-phenoxy-1, 3, 2-benzo-dioxaphosphole” by M. Application context: [488] With respect to Drabowicz,[187] it is acknowledged that the only method described therein that applied directly to penicillins or cephalosporins is found at p. Evidence spans paragraphs 484-488. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040730` offsets `426-433`; context: [183] There was some debate as to whether or not these would be part of the common general knowledge of the posita at the relevant time or even of the state of the art, given that they are not part of the cephalosporin or β-lactam literature.
- Evidence: `governing_rule` cue `under` at chunk `5040730` offsets `58-63`; context: [484] This article, entitled “Deoxygenation of Sulfoxides under Mild Conditions with a New Reducing Agent: 2-phenoxy-1, 3, 2-benzo-dioxaphosphole” by M.
- Evidence: `issue` cue `issue` at chunk `5040731` offsets `114-119`; context: [485] Having carefully considered the content of these publications, the Court need not deal with this particular issue further, given that even if they were part of the common general knowledge, it would have no impact whatsoever on the final determination of the issue of obviousness as the Court accepts Dr.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040731` offsets `321-330`; context: Baldwin’s testimony regarding how it would be understood and used by the posita at the time.
- Evidence: `reasoning_application` cue `applied` at chunk `5040734` offsets `101-108`; context: [488] With respect to Drabowicz,[187] it is acknowledged that the only method described therein that applied directly to penicillins or cephalosporins is found at p.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040734` offsets `232-240`; context: [188] Although it appears at first sight that the reduction of the sulfoxide was done with a phosphorus pentasulfide-pyridine system, Dr.

#### 22183:19:subtheme:4 · paragraphs 489-510

- Raw key terms: `kinetic, complex, reagent, cephalosporin, posita, reaction, steps, chemistry`
- Display key terms: `kinetic, complex, reagent, cephalosporin, posita, reaction, steps, chemistry`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: kinetic, complex, reagent, cephalosporin, posita, reaction, steps, chemistry Application context: The idea did not come to him because of what was generally known or disclosed in the literature. Evidence spans paragraphs 489-510. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040735` offsets `53-58`; context: [489] The inventive concept in each of the claims at issue[190] was the use of the kinetic complex – the fastest forming intermediate of the reaction of equivalent amounts of triaryl phosphite and Cl or Br – to execute the steps described in these various patents, i.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040744` offsets `29-37`; context: [498] Here again, the expert evidence adduced by Apotex to support its position in respect of the Lilly process patents has very little probative value, given that none of the experts who opined on these patents were qualified to discuss what a posita would have found obvious to try.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040746` offsets `123-132`; context: 24(3) of his affidavit, A-13).
- Evidence: `evidence_fact` cue `evidence` at chunk `5040747` offsets `222-230`; context: Baldwin’s evidence was quite clear.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040748` offsets `48-56`; context: [502] The Court was not persuaded by the expert evidence that either the thermodynamic or the kinetic product would be on the list of possible reagents to try.
- Evidence: `reasoning_application` cue `because` at chunk `5040752` offsets `249-256`; context: The idea did not come to him because of what was generally known or disclosed in the literature.

#### 22183:19:subtheme:5 · paragraphs 511-516

- Raw key terms: `common, general, knowledge, chemistry, court, experts, hanessian, patents`
- Display key terms: `common, knowledge, chemistry, experts, hanessian, patents`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: common, knowledge, chemistry, experts, hanessian, patents Application context: As noted earlier, because of their lack of expertise, or even focus on β-lactams, these experts were not qualified to opine on how a posita would read the prior art or what common general knowledge (other than from his P Evidence spans paragraphs 511-516. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040757` offsets `91-96`; context: [511] In view of the foregoing, Apotex has failed to persuade the Court that the claims at issue were obvious.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040759` offsets `180-188`; context: It is in that respect only that the evidence of Drs.
- Evidence: `reasoning_application` cue `because` at chunk `5040759` offsets `255-262`; context: As noted earlier, because of their lack of expertise, or even focus on β-lactams, these experts were not qualified to opine on how a posita would read the prior art or what common general knowledge (other than from his PhD formation in organic chemistry) he would possess.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040759` offsets `510-517`; context: However, their evidence in respect of the common general knowledge of PhD in organic chemistry does not add anything to the evidence of Dr.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040762` offsets `628-635`; context: However, the experts disagree as to what some of these publications taught the posita.

#### 22183:19:subtheme:6 · paragraphs 517-537

- Raw key terms: `cephalosporin, compound, known, posita, evidence, ring, used, bond`
- Display key terms: `cephalosporin, compound, known, posita, ring, used, bond`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: cephalosporin, compound, known, posita, ring, used, bond Rule/authority context: Consequently, he had investigated the oxidation of compound 4 (which is compound 7 in Cooper 2) under various conditions in an effort to chemically duplicate this biosynthetic postulate. Application context: As the Sammes review refers to some patents, this could indeed indicate that this was not considered to be part of the relevant art; however, it may also be that it was simply not reviewed because of the language of the  Evidence spans paragraphs 517-537. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040763` offsets `108-114`; context: [517] β-lactams and cephalosporins were known to be polyfunctional and sensitive molecules that raised many issues relating to selectivity and reactivity.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040766` offsets `205-212`; context: [206] However, at the relevant date, this compound, which is a penicillin derivative, had never been converted to a 6-membered ring cephalosporin.
- Evidence: `governing_rule` cue `under` at chunk `5040770` offsets `249-254`; context: Consequently, he had investigated the oxidation of compound 4 (which is compound 7 in Cooper 2) under various conditions in an effort to chemically duplicate this biosynthetic postulate.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040772` offsets `18-26`; context: [526] There is no evidence from Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040774` offsets `452-460`; context: Barrett’s evidence as to how this would be understood by a posita.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040774` offsets `197-204`; context: It is to be noted, however, that at p.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040777` offsets `157-165`; context: Barrett’s evidence that this was not commonly used in the field of cephalosporin chemistry and research related thereto at the relevant time.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040778` offsets `198-206`; context: It contends that these were not part of the common general knowledge and that no evidence was presented as to why they would be considered either alone or together by a posita, when faced with the problem solved in the Shionogi patents.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040779` offsets `131-138`; context: [215] However, it was established that a short English abstract (number 120652H) was published in volume 81 of the 1974 Chemical Abstracts.
- Evidence: `reasoning_application` cue `because` at chunk `5040780` offsets `373-380`; context: As the Sammes review refers to some patents, this could indeed indicate that this was not considered to be part of the relevant art; however, it may also be that it was simply not reviewed because of the language of the original and the fact that the English abstract was published at a date which was too close to the date on which the revised draft was submitted for publishing.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040780` offsets `317-324`; context: As the Sammes review refers to some patents, this could indeed indicate that this was not considered to be part of the relevant art; however, it may also be that it was simply not reviewed because of the language of the original and the fact that the English abstract was published at a date which was too close to the date on which the revised draft was submitted for publishing.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040781` offsets `216-224`; context: There is little evidence that such an extensive search would be undertaken by a posita, especially considering that there was no motivation to carry out the reaction, given that the compound in the Shionogi patent on which it is carried out was not known.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040782` offsets `40-48`; context: [536] As mentioned earlier, the lack of evidence on Apotex’s part as to how, and through what means, this document was found is troubling.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040782` offsets `139-146`; context: However, the Court is prepared to consider that at least what was described in the abstract was part of the relevant state of the art.

#### 22183:19:subtheme:7 · paragraphs 538-543

- Raw key terms: `apotex, experts, kishi, martin, evidence, patents, published, relevant`
- Display key terms: `apotex, experts, kishi, martin, patents, published, relevant`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: apotex, experts, kishi, martin, patents, published, relevant Application context: Kishi made a presentation at the 9th International Conference on the Chemistry of Natural Products in Ottawa, Canada and another at International Union of Pure and Applied Chemistry (IUPAC) conference on organic synthesi | Yoshito Kishi described above to conclude that the claims of the ‘132 patent and the ‘026 patent were obvious. Evidence spans paragraphs 538-543. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040784` offsets `1105-1110`; context: In any event, having carefully examined this art and the conflicting expert evidence related thereto, the Court does not believe that consideration of this publication[217] would have altered the overall conclusion on the obviousness of the claims at issue in the ‘924 patent.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040784` offsets `324-332`; context: Although Apotex tried to establish through cross-examination that an abstract could have been published in Chemical Abstracts, its failure to refer to such an abstract in the evidence of its experts raises a reasonable inference that it was not so-published at the relevant time.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040784` offsets `149-157`; context: Although Apotex tried to establish through cross-examination that an abstract could have been published in Chemical Abstracts, its failure to refer to such an abstract in the evidence of its experts raises a reasonable inference that it was not so-published at the relevant time.
- Evidence: `reasoning_application` cue `Applied` at chunk `5040785` offsets `194-201`; context: Kishi made a presentation at the 9th International Conference on the Chemistry of Natural Products in Ottawa, Canada and another at International Union of Pure and Applied Chemistry (IUPAC) conference on organic synthesis on August 26-30, 1974 in Louvain-la-Neuve, Belgium.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040786` offsets `134-142`; context: Yoshito Kishi described above to conclude that the claims of the ‘132 patent and the ‘026 patent were obvious.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040787` offsets `183-191`; context: Given that I have found the evidence of Drs.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `5040787` offsets `436-448`; context: Nevertheless, to avoid further debate I will simply comment as follows:
- Evidence: `evidence_fact` cue `evidence` at chunk `5040788` offsets `155-163`; context: There is absolutely no evidence that the particular segments or reactions used by these experts to support their opinions were shown or mentioned by Dr.

#### 22183:19:subtheme:8 · paragraphs 544-545

- Raw key terms: `apotex, claim, clear, concept, each, inventive, issue, patent`
- Display key terms: `apotex, clear, concept, each, inventive, patent`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue Display terms: apotex, clear, concept, each, inventive, patent Rule/authority context: [544] Although it is very clear that the inventive concept is to be assessed in respect of each claim at issue for each patent under review, the Court is satisfied that the issues raised by Apotex can be properly address Operative outcome context: [545] Apotex agreed that if there is any inventive concept in these patents (which it denied), it would be the overall synthetic pathway which is not claimed per se. Evidence spans paragraphs 544-545. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040790` offsets `105-110`; context: [544] Although it is very clear that the inventive concept is to be assessed in respect of each claim at issue for each patent under review, the Court is satisfied that the issues raised by Apotex can be properly addressed without a full description of the inventive concept of each of the claims.
- Evidence: `governing_rule` cue `under` at chunk `5040790` offsets `127-132`; context: [544] Although it is very clear that the inventive concept is to be assessed in respect of each claim at issue for each patent under review, the Court is satisfied that the issues raised by Apotex can be properly addressed without a full description of the inventive concept of each of the claims.
- Evidence: `issue` cue `issue` at chunk `5040791` offsets `549-554`; context: However, even if it is clear from the disclosure[220] of each patent that the overall synthetic pathway, which enables the addressee of each patent to cyclicize a penicillin derivative compound (the Cooper thiazoline compound) into a 6-membered ring cephalosporin, where a hydroxyl is already in place at the 3-position, is included in the inventive concept of at least one claim at issue in each patent; it is not the only relevant element thereof.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040791` offsets `166-173`; context: However, even if it is clear from the disclosure[220] of each patent that the overall synthetic pathway, which enables the addressee of each patent to cyclicize a penicillin derivative compound (the Cooper thiazoline compound) into a 6-membered ring cephalosporin, where a hydroxyl is already in place at the 3-position, is included in the inventive concept of at least one claim at issue in each patent; it is not the only relevant element thereof.
- Evidence: `disposition` cue `denied` at chunk `5040791` offsets `86-92`; context: [545] Apotex agreed that if there is any inventive concept in these patents (which it denied), it would be the overall synthetic pathway which is not claimed per se.

#### 22183:19:subtheme:9 · paragraphs 546-556

- Raw key terms: `disclosure, prior, patent, reaction, claimed, hydroxy, starting, compounds`
- Display key terms: `disclosure, prior, patent, reaction, claimed, hydroxy, starting, compounds`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: disclosure, prior, patent, reaction, claimed, hydroxy, starting, compounds Evidence spans paragraphs 546-556. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040792` offsets `56-61`; context: [546] In effect, the inventive concept of the claims at issue in the following patents also includes:
i.

#### 22183:19:subtheme:10 · paragraphs 557-572

- Raw key terms: `process, shionogi, pathway, cooper, make, posita, compound, overall`
- Display key terms: `process, shionogi, pathway, cooper, make, posita, compound, overall`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: process, shionogi, pathway, cooper, make, posita, compound, overall Application context: Although the fact that very many options were open is obviously not in and of itself sufficient to conclude that an invention is not obvious. | [568] Apotex argued that this evidence has little weight because Dr. Evidence spans paragraphs 557-572. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040803` offsets `80-85`; context: [557] I will first deal with the inventiveness of at least one of the claims at issue in each patent, based on the idea of the overall Shionogi synthetic process described in the disclosure.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040810` offsets `205-213`; context: Although the fact that very many options were open is obviously not in and of itself sufficient to conclude that an invention is not obvious.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040810` offsets `106-114`; context: Although the fact that very many options were open is obviously not in and of itself sufficient to conclude that an invention is not obvious.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040814` offsets `30-38`; context: [568] Apotex argued that this evidence has little weight because Dr.
- Evidence: `reasoning_application` cue `because` at chunk `5040814` offsets `57-64`; context: [568] Apotex argued that this evidence has little weight because Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040815` offsets `142-150`; context: Cooper’s credibility in the course of his cross-examination, the Court finds his evidence credible.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040815` offsets `242-250`; context: Although this evidence is not determinative per se, it certainly supports Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040816` offsets `27-35`; context: [570] Although there is no evidence on which the Court could conclude that cefaclor was “the” priority at Lilly, it was certainly important enough for Lilly to go to Shionogi for help.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040816` offsets `61-69`; context: [570] Although there is no evidence on which the Court could conclude that cefaclor was “the” priority at Lilly, it was certainly important enough for Lilly to go to Shionogi for help.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040817` offsets `62-70`; context: [571] In view of the foregoing, and having considered all the evidence presented, the Court concludes that the Shionogi synthetic pathway was not obvious.
- Evidence: `reasoning_application` cue `concludes` at chunk `5040817` offsets `92-101`; context: [571] In view of the foregoing, and having considered all the evidence presented, the Court concludes that the Shionogi synthetic pathway was not obvious.

#### 22183:19:subtheme:11 · paragraphs 573-574

- Raw key terms: `each, patent, apotex, basic, burden, claim, claimed, claims`
- Display key terms: `each, patent, apotex, basic, burden, claimed, claims`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: each, patent, apotex, basic, burden, claimed, claims Evidence spans paragraphs 573-574. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040819` offsets `102-107`; context: [573] Here, the overall Shionogi process also provides inventiveness to at least one process claim at issue in each of the patents.

#### 22183:19:subtheme:12 · paragraphs 575-581

- Raw key terms: `apotex, known, posita, court, work, barrett, compounds, even`
- Display key terms: `apotex, known, posita, work, barrett, compounds, even`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: apotex, known, posita, work, barrett, compounds, even Application context: Barrett also acknowledges that these generic reactions (except maybe for one) were known and often used in general organic chemistry but he says that this would provide no comfort to the posita because of the delicate na | However, the weight of his evidence was still such that the Court could not conclude that there was a preponderance of evidence in favour of Apotex. Evidence spans paragraphs 575-581. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040821` offsets `589-594`; context: Thus, a posita would expect them to successfully work on the compounds described in the patents at issue even those that had never been made before.
- Evidence: `counterargument_limitation` cue `although` at chunk `5040821` offsets `445-453`; context: They each had been used at least once on similar compounds without destroying the β-lactam molecule (although the yields may have been very low).
- Evidence: `issue` cue `issue` at chunk `5040822` offsets `255-260`; context: Barrett also acknowledges that these generic reactions (except maybe for one) were known and often used in general organic chemistry but he says that this would provide no comfort to the posita because of the delicate nature of the compounds at issue and the serious issues of selectivity they raised.
- Evidence: `reasoning_application` cue `because` at chunk `5040822` offsets `204-211`; context: Barrett also acknowledges that these generic reactions (except maybe for one) were known and often used in general organic chemistry but he says that this would provide no comfort to the posita because of the delicate nature of the compounds at issue and the serious issues of selectivity they raised.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040823` offsets `87-95`; context: Hanessian was a credible witness but the weight of his evidence was diminished by the fact that his opinion only refers to publications given to him by Apotex’s counsel.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040824` offsets `125-133`; context: Barrett was subjected to more than one long and skilful cross-examination and the weight of his evidence was diminished by the fact that some of the points made in his report were shown to have been somewhat overstated (see for example the evidence in respect of para.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040824` offsets `388-396`; context: However, the weight of his evidence was still such that the Court could not conclude that there was a preponderance of evidence in favour of Apotex.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040824` offsets `312-319`; context: However, the weight of his evidence was still such that the Court could not conclude that there was a preponderance of evidence in favour of Apotex.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040825` offsets `464-472`; context: The Court is simply not persuaded by Apotex’s evidence that the posita would be motivated to try this process on the Cooper compound[236] and certainly not that the ozonolysis of this open-ring structure would be expected to work.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040825` offsets `197-205`; context: Although the Court acknowledges that this paper shows that the Cooper thiazoline was stable in the conditions described therein, the Court does not agree that this would have been the only concern for the skilled person.

#### 22183:19:subtheme:13 · paragraphs 582-585

- Raw key terms: `burden, claimed, claims, court, evident, issue, para, patent`
- Display key terms: `burden, claimed, claims, evident, para, patent`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: burden, claimed, claims, evident, para, patent Application context: [582] In respect of the ‘026 patent, after reviewing the evidence several times, the Court had to conclude that it was equally unconvinced by both sides. | [584] With respect to sound prediction, the tripartite test to be applied was set out by the Supreme Court of Canada in Wellcome (2002), at para. Evidence spans paragraphs 582-585. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040828` offsets `414-419`; context: Thus the party bearing the burden on this issue fails.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040828` offsets `57-65`; context: [582] In respect of the ‘026 patent, after reviewing the evidence several times, the Court had to conclude that it was equally unconvinced by both sides.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040828` offsets `98-106`; context: [582] In respect of the ‘026 patent, after reviewing the evidence several times, the Court had to conclude that it was equally unconvinced by both sides.
- Evidence: `issue` cue `issue` at chunk `5040829` offsets `65-70`; context: [583] Apotex argues that several of the claims in the patents at issue are overbroad; they allegedly include claimed embodiments that are inoperable.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040829` offsets `150-158`; context: Although the defendant argues in its memorandum that the patentee had to establish utility at the relevant time or that he could soundly predict that all the embodiments claimed would be useful, it is evident that, as with any other arguments presented to invalidate the patents, the burden of proof here is on the defendant.
- Evidence: `reasoning_application` cue `applied` at chunk `5040830` offsets `66-73`; context: [584] With respect to sound prediction, the tripartite test to be applied was set out by the Supreme Court of Canada in Wellcome (2002), at para.

#### 22183:19:subtheme:14 · paragraphs 586-587

- Raw key terms: `argument, claims, court, determinative, issue, thus, abundance, advised`
- Display key terms: `argument, claims, determinative, thus, abundance, advised`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: argument, claims, determinative, thus, abundance, advised Evidence spans paragraphs 586-587. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040832` offsets `39-44`; context: [586] Given that many of the claims at issue are limited to Z = H,[241] such as claims 20, 21, 27, and 11 (the alternative based on claim 10) of the ‘536 patent, claims 16, 23, 26, 27 and 30 of the ‘725 patent, and claims 8, 17, 19 and 20 of the ‘468 patent, it was not clear at all how such argument could be determinative.
- Evidence: `issue` cue `issue` at chunk `5040833` offsets `92-97`; context: [587] In an abundance of caution, the Court has thus decided to review the evidence on this issue but this should not be taken as implying that such argument could be determinative in any way of the findings in respect of all the claims which were found to be infringed.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040833` offsets `75-83`; context: [587] In an abundance of caution, the Court has thus decided to review the evidence on this issue but this should not be taken as implying that such argument could be determinative in any way of the findings in respect of all the claims which were found to be infringed.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040833` offsets `98-101`; context: [587] In an abundance of caution, the Court has thus decided to review the evidence on this issue but this should not be taken as implying that such argument could be determinative in any way of the findings in respect of all the claims which were found to be infringed.

#### 22183:19:subtheme:15 · paragraphs 588-592

- Raw key terms: `apotex, examples, experts, ortho, patents, reason, reported, respect`
- Display key terms: `apotex, examples, experts, ortho, patents, reason, reported, respect`
- Argument roles: `counterargument_limitation, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, reasoning_application Display terms: apotex, examples, experts, ortho, patents, reason, reported, respect Application context: These data prompted speculation that the ionic complex, (ArO)3P±Cl Cl¯, was in fact the active complex and therefore substitution on the aromatic ring that would stabilize the positive charge on phosphorus should in turn | McClelland insinuated that he could not rely on the examples in the patents because he had not seen the actual lab notebooks concerning these experiments. Evidence spans paragraphs 588-592. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `therefore` at chunk `5040834` offsets `668-677`; context: These data prompted speculation that the ionic complex, (ArO)3P±Cl Cl¯, was in fact the active complex and therefore substitution on the aromatic ring that would stabilize the positive charge on phosphorus should in turn provide a more stable, active reagent.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040835` offsets `53-62`; context: [589] As mentioned, TX-211 was introduced during the testimony of Dr.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040835` offsets `137-145`; context: Although he indicated that he had no reason to believe that the results reported therein were not accurate, it is clear that he was not
personally involved in the experiments discussed, particularly those at the passages referred to by Apotex’s experts.
- Evidence: `reasoning_application` cue `because` at chunk `5040837` offsets `573-580`; context: McClelland insinuated that he could not rely on the examples in the patents because he had not seen the actual lab notebooks concerning these experiments.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040837` offsets `652-659`; context: However, it is clear that he had not seen any lab notes relating to the experiments reported in TX-211 either.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040838` offsets `13-22`; context: [592] In his affidavit (E-19, paras.
- Evidence: `counterargument_limitation` cue `although` at chunk `5040838` offsets `470-478`; context: Baldwin who, although he had not seen any lab notebooks with respect to the examples, represents what a posita would have expected based on the data disclosed in the patents.

#### 22183:19:subtheme:16 · paragraphs 593-595

- Raw key terms: `apotex, court, disclosed, evidence, patents, based, burden, experiments`
- Display key terms: `apotex, disclosed, patents, based, burden, experiments`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: apotex, disclosed, patents, based, burden, experiments Rule/authority context: [595] The Court finds that there was no positive burden on Lilly to independently prove the experiments disclosed in its patents for Apotex abandoned its challenge of their accuracy pursuant to s. Evidence spans paragraphs 593-595. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040839` offsets `1030-1035`; context: Rather, the issue is whether the information provided in the specification is sufficient to explain the functioning of the invention to a person skilled in the art.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040839` offsets `47-55`; context: [593] When Lilly attempted to introduce direct evidence of the work carried out in the patent in respect of example 9 of the ‘007 patent, Apotex objected to the evidence of Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040840` offsets `101-109`; context: [594] In my view, there is no need to even rule on this objection for, after carefully reviewing the evidence, the Court is simply not satisfied that Apotex has met its burden of establishing on a balance of probability that any of the above mentioned compounds were inactive or that their ability to perform the claimed reactions could not be soundly predicted[247] based on the factual data (the examples) disclosed in the patents and the common general knowledge of the posita at the relevant time.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040841` offsets `234-242`; context: Obviously, the evidence of Mr.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040841` offsets `182-193`; context: [595] The Court finds that there was no positive burden on Lilly to independently prove the experiments disclosed in its patents for Apotex abandoned its challenge of their accuracy
pursuant to s.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040841` offsets `295-298`; context: Gardner would have strengthened Lilly’s case but it does not improve Apotex’s.

#### 22183:19:subtheme:17 · paragraphs 596-599

- Raw key terms: `mcclelland, complex, formed, used, a-12, affidavit, celsius, fact`
- Display key terms: `mcclelland, complex, formed, used, a-12, affidavit, celsius, fact`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: mcclelland, complex, formed, used, a-12, affidavit, celsius, fact Application context: He noted that he didn’t know because there were no experiments, at least that he recalled. Evidence spans paragraphs 596-599. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040842` offsets `30-36`; context: [596] This leaves two further issues to be discussed – the orthomethoxy derivative and para.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040842` offsets `117-126`; context: McClelland’s affidavit (A-12).
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040843` offsets `52-61`; context: 111 of his affidavit (A-12) that, according to TX-211, the inventors knew that the triphenylphosphite-chlorine complex employed to perform sulfoxide reduction (‘536 patent), halogenation of the 3-OH to 3-Cl (‘725 patent), and the acylamino conversion (‘468 patent) must be formed at -10º Celsius or lower to work and must be used quickly.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `5040843` offsets `380-392`; context: Nevertheless, the inventors claim the use of such complexes and included in their claims temperatures of up to 30º Celsius.
- Evidence: `reasoning_application` cue `because` at chunk `5040845` offsets `407-414`; context: He noted that he didn’t know because there were no experiments, at least that he recalled.

#### 22183:19:subtheme:18 · paragraphs 600-601

- Raw key terms: `inventor, modro, whether, able, affidavit, allegedly, although, appear`
- Display key terms: `inventor, modro, whether, able, affidavit, allegedly, although, appear`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: inventor, modro, whether, able, affidavit, allegedly, although, appear Evidence spans paragraphs 600-601. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040846` offsets `99-106`; context: Modro does not opine on whether, based on the experiment disclosed in the ‘007 patent (7(F) using tri-o-tolyl to transform a cephalosporin substrate) the inventor could have soundly predicted the usefulness of these other Z substituents at the ortho position.
- Evidence: `issue` cue `issue` at chunk `5040847` offsets `250-255`; context: Modro said that the issue was more precisely whether the kinetic complex – an intermediate which by nature is unstable – would be able, for example, to chlorinate the enol before it reacted further with the chlorine as described in Gloede.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040847` offsets `204-213`; context: [253] Although this does not appear clearly from his affidavit as drafted, Dr.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040847` offsets `157-165`; context: [253] Although this does not appear clearly from his affidavit as drafted, Dr.

#### 22183:19:subtheme:19 · paragraphs 602-603

- Raw key terms: `patent, process, simply, support, allegation, apotex, apposite, appreciate`
- Display key terms: `patent, process, simply, support, allegation, apotex, apposite, appreciate`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: patent, process, simply, support, allegation, apotex, apposite, appreciate Application context: I find that the Defendant has not established that any of the process claims are simply inoperable. Evidence spans paragraphs 602-603. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040848` offsets `34-40`; context: [602] In respect of both of these issues the following comments of Justice MacKay in Wellcome (1991) are particularly apposite:
The Defendant raises doubt about the operability of certain of the reactions when particular reactants are utilized; however, there is no clear proof that any of the reactions will not proceed.
- Evidence: `reasoning_application` cue `I find` at chunk `5040848` offsets `824-830`; context: I find that the Defendant has not established that any of the process claims are simply inoperable.
- Evidence: `counterargument_limitation` cue `however` at chunk `5040848` offsets `245-252`; context: [602] In respect of both of these issues the following comments of Justice MacKay in Wellcome (1991) are particularly apposite:
The Defendant raises doubt about the operability of certain of the reactions when particular reactants are utilized; however, there is no clear proof that any of the reactions will not proceed.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040849` offsets `71-79`; context: [603] In this case the Court is not satisfied that Apotex has provided evidence of sufficient weight to support its allegation that the ‘007 patent or the Lilly process patents contain embodiments that are not useful or whose usefulness could not be soundly predicted by the inventor on the basis of the various experiments described in the patents and the relevant common general knowledge.

#### 22183:19:subtheme:20 · paragraphs 604-606

- Raw key terms: `claims, apotex, compounds, issues, kyong, mcclelland, patent, process`
- Display key terms: `claims, apotex, compounds, issues, kyong, mcclelland, patent, process`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue Display terms: claims, apotex, compounds, issues, kyong, mcclelland, patent, process Rule/authority context: [604] Apotex raises no issue under this heading with respect to the ‘547 patent. Operative outcome context: McClelland and Hanessian’s evidence,[258] it appears that, as of 1975, there was no reliable method that allowed for allylic fluorination reactions to occur and no reagents were listed in the patent to assist the skilled Evidence spans paragraphs 604-606. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040850` offsets `23-28`; context: [604] Apotex raises no issue under this heading with respect to the ‘547 patent.
- Evidence: `governing_rule` cue `under` at chunk `5040850` offsets `29-34`; context: [604] Apotex raises no issue under this heading with respect to the ‘547 patent.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040850` offsets `232-239`; context: [255] However, this is only relevant to claims 3, 8, 9, and 27.
- Evidence: `issue` cue `issues` at chunk `5040851` offsets `190-196`; context: McClelland (A-12)) testified about issues including “difficulties” that would be encountered with compounds covered by claims 15, 22, 29, and 34 when Y is hydroxy (OH).
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040851` offsets `89-98`; context: 94-95 of the affidavit of Dr.
- Evidence: `disposition` cue `allowed` at chunk `5040851` offsets `515-522`; context: McClelland and Hanessian’s evidence,[258] it appears that, as of 1975, there was no reliable method that allowed for allylic fluorination
reactions to occur and no reagents were listed in the patent to assist the skilled person.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5040852` offsets `97-103`; context: [606] As noted above, the Kyong Bo process infringes claims 38, 58 and 15, the validity of which cannot be affected by these arguments.

#### 22183:19:subtheme:21 · paragraphs 607-608

- Raw key terms: `affected, apotex, claims, counsel, issue, respect, a-12, a-15`
- Display key terms: `affected, apotex, claims, respect, a-12, a-15`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: affected, apotex, claims, respect, a-12, a-15 Position/evidence statements: [607] It is not clear why Apotex’s counsel insisted on arguing all of the above mentioned issues given that it was clear that certain claims at issue, which would obviously be infringed if their argument with respect to  Evidence spans paragraphs 607-608. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040853` offsets `90-96`; context: [607] It is not clear why Apotex’s counsel insisted on arguing all of the above mentioned issues given that it was clear that certain claims at issue, which would obviously be infringed if their argument with respect to importation was not accepted, would not be affected by such arguments.
- Evidence: `party_position` cue `claims` at chunk `5040853` offsets `134-140`; context: [607] It is not clear why Apotex’s counsel insisted on arguing all of the above mentioned issues given that it was clear that certain claims at issue, which would obviously be infringed if their argument with respect to importation was not accepted, would not be affected by such arguments.
- Evidence: `issue` cue `issue` at chunk `5040854` offsets `81-86`; context: [608] This brings us to the last patent, the ‘026 patent where all the claims at issue would be affected by the matters raised by Drs.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040854` offsets `685-694`; context: [260] During his testimony, Dr.

#### 22183:19:subtheme:22 · paragraphs 609-613

- Raw key terms: `fluorine, group, leaving, apotex, mcclelland, work, although, assist`
- Display key terms: `fluorine, group, leaving, apotex, mcclelland, work, although, assist`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: fluorine, group, leaving, apotex, mcclelland, work, although, assist Position/evidence statements: [612] Having carefully considered all of the evidence, the Court is not satisfied that Apotex has established on a balance of probability that the use of fluorine in claim 1, particularly with the use of a catalizer[267] Rule/authority context: [613] Under this heading, Apotex raises several complaints to support its argument that the disclosure of the ‘007 patent (the only patent to which this argument applies) is deficient and does not contain all the informa Application context: Hanessian concludes that fluorine, which is not a good leaving group, would not work. | He also notes that, although a posita would not likely choose fluorine because of the inherent danger linked to the use of such halogen, – “[y]ou might destroy your co-workers. Evidence spans paragraphs 609-613. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040855` offsets `123-130`; context: However, despite the lack of examples in respect of iodine and fluorine and the lack of detailed information about chlorine, Dr.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5040856` offsets `170-179`; context: Hanessian states in his affidavit that it requires a good leaving group.
- Evidence: `reasoning_application` cue `concludes` at chunk `5040856` offsets `271-280`; context: Hanessian concludes that fluorine, which is not a good leaving group, would not work.
- Evidence: `reasoning_application` cue `because` at chunk `5040857` offsets `408-415`; context: He also notes that, although a posita would not likely choose fluorine because of the inherent danger linked to the use of such halogen, – “[y]ou might destroy your co-workers.
- Evidence: `counterargument_limitation` cue `although` at chunk `5040857` offsets `357-365`; context: He also notes that, although a posita would not likely choose fluorine because of the inherent danger linked to the use of such halogen, – “[y]ou might destroy your co-workers.
- Evidence: `party_position` cue `claim` at chunk `5040858` offsets `166-171`; context: [612] Having carefully considered all of the evidence, the Court is not satisfied that Apotex has established on a balance of probability that the use of fluorine in claim 1, particularly with the use of a catalizer[267] to assist cyclization, would not work or that such process could not be soundly predicted on the basis of the experiments described in the patent and the common general knowledge about fluorine as a leaving group.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040858` offsets `45-53`; context: [612] Having carefully considered all of the evidence, the Court is not satisfied that Apotex has established on a balance of probability that the use of fluorine in claim 1, particularly with the use of a catalizer[267] to assist cyclization, would not work or that such process could not be soundly predicted on the basis of the experiments described in the patent and the common general knowledge about fluorine as a leaving group.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040859` offsets `328-336`; context: These complaints and all the evidence on which Apotex relies are fully described in its memorandum on validity at paras.
- Evidence: `governing_rule` cue `Under` at chunk `5040859` offsets `6-11`; context: [613] Under this heading, Apotex raises several complaints to support its argument that the disclosure of the ‘007 patent (the only patent to which this argument applies) is deficient and does not contain all the information necessary to enable the posita to practice and use the invention claimed.
- Evidence: `reasoning_application` cue `applies` at chunk `5040859` offsets `162-169`; context: [613] Under this heading, Apotex raises several complaints to support its argument that the disclosure of the ‘007 patent (the only patent to which this argument applies) is deficient and does not contain all the information necessary to enable the posita to practice and use the invention claimed.

#### 22183:19:subtheme:23 · paragraphs 614-622

- Raw key terms: `patent, kinetic, apotex, claim, excess, invention, make, posita`
- Display key terms: `patent, kinetic, apotex, excess, invention, make, posita`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: patent, kinetic, apotex, excess, invention, make, posita Position/evidence statements: [614] As the Court has already indicated that the only valid claim left at issue at this stage is claim 17, these arguments will only be considered in respect of the invention claimed therein, that is, the process to mak | [619] There is thus no need to say much more than that Apotex has failed to convince the Court that a posita armed with all the information contained in the ‘007 patent and its common general knowledge would not be able  Rule/authority context: [615] The applicable principles are well-known. Evidence spans paragraphs 614-622. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040860` offsets `75-80`; context: [614] As the Court has already indicated that the only valid claim left at issue at this stage is claim 17, these arguments will only be considered in respect of the invention claimed
therein, that is, the process to make the kinetic complex in an aromatic hydrocarbon or halogenated hydrocarbon solvent.
- Evidence: `party_position` cue `claim` at chunk `5040860` offsets `61-66`; context: [614] As the Court has already indicated that the only valid claim left at issue at this stage is claim 17, these arguments will only be considered in respect of the invention claimed
therein, that is, the process to make the kinetic complex in an aromatic hydrocarbon or halogenated hydrocarbon solvent.
- Evidence: `governing_rule` cue `principles` at chunk `5040861` offsets `21-31`; context: [615] The applicable principles are well-known.
- Evidence: `counterargument_limitation` cue `fails` at chunk `5040863` offsets `56-61`; context: [617] In a nutshell, Apotex argues that the ‘007 patent fails to disclose the need i) to avoid excess TPP, ii) to make the kinetic complex or use it at -10 ºC, iii) to use the kinetic complex quickly, and iv) that it fails to give sufficient details about the particular species falling within the scope of the claims.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040864` offsets `190-198`; context: In fact, the Court is somewhat surprised that it was pursued given the paucity of the evidence supporting it and the fact that all the experts who tried to make the kinetic complex, following the instructions of the ‘007 patent, succeeded the very first time they
tried (such as Dr.
- Evidence: `party_position` cue `claim` at chunk `5040865` offsets `252-257`; context: [619] There is thus no need to say much more than that Apotex has failed to convince the Court that a posita armed with all the information contained in the ‘007 patent and its common general knowledge would not be able to use the process described at claim 17 successfully to make kinetic complexes.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040865` offsets `321-329`; context: In other words, the evidence relied upon is simply insufficient to meet that burden.

#### 22183:19:subtheme:24 · paragraphs 623-625

- Raw key terms: `kinetic, complex, court, formed, need, product, respect, thermodynamic`
- Display key terms: `kinetic, complex, formed, need, product, respect, thermodynamic`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: kinetic, complex, formed, need, product, respect, thermodynamic Operative outcome context: Most simply conditions for kinetic control are achieved both by lowering the reaction temperature and the temperature of the kinetic product after it is formed, and by minimizing [the] time allowed for thermodynamic equi Evidence spans paragraphs 623-625. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040869` offsets `157-162`; context: [623] With respect to the need to use the kinetic complex quickly and to make it or use it at -10º C or less, the Court has already reviewed, discussing the issue of utility, the passages of TX-211 relied upon by Apotex, and Dr.
- Evidence: `disposition` cue `allowed` at chunk `5040870` offsets `472-479`; context: Most simply conditions for kinetic control are achieved both by lowering the reaction temperature and the temperature of the kinetic product after it is formed, and by minimizing [the] time allowed for thermodynamic equilibrium, such as by utilizing the kinetic product in a subsequent reaction immediately after it has been prepared.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040871` offsets `569-577`; context: [272] The Court certainly agrees with Lilly’s submissions that there is a preponderance of evidence that with knowledge of what is disclosed in the ‘007 patent, it is relatively simple to observe the conversion of the kinetic complex to the thermodynamic product using 31P NMR analysis.

#### 22183:19:subtheme:25 · paragraphs 626-633

- Raw key terms: `apotex, counterclaim, defence, equitable, lilly, set-off, action, conduct`
- Display key terms: `apotex, counterclaim, defence, equitable, lilly, set-off, action, conduct`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: apotex, counterclaim, defence, equitable, lilly, set-off, action, conduct Position/evidence statements: ): For past conduct to be relevant to a refusal of equitable relief under the "clean hands" doctrine, relief to which the party would otherwise be entitled, such conduct must relate directly to the subject matter of the  Rule/authority context: Apotex also argues that, even if its claims under the Competition Act, R. | Defences raised under the doctrine of equitable set-off are not subject to the expiration of limitations periods (see Canada Trustco Mortgage Co. Application context: [629] That said, even if it were possible for the Court to import, as suggested, the evidence filed in the counterclaim, which includes evidence by Shionogi who is not a party to the main action, the Court is of the view Evidence spans paragraphs 626-633. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040872` offsets `254-259`; context: [626] In its written submissions and at oral argument, Apotex argues that Lilly’s conduct in respect of the Shionogi patents should disentitle Lilly from any relief (equitable or otherwise) from its claim of infringement in respect of all the patents at issue.
- Evidence: `governing_rule` cue `under` at chunk `5040872` offsets `305-310`; context: Apotex also argues that, even if its claims under the Competition Act, R.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040873` offsets `229-237`; context: Moreover, Apotex presented no evidence to establish a s.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040875` offsets `85-93`; context: [629] That said, even if it were possible for the Court to import, as suggested, the evidence filed in the counterclaim, which includes evidence by Shionogi who is not a party to the main action, the Court is of the view that Apotex’s counterclaim is without merit because it is time-barred and Apotex failed to establish that it suffered a loss arising from the alleged anti-competitive conduct.
- Evidence: `reasoning_application` cue `because` at chunk `5040875` offsets `265-272`; context: [629] That said, even if it were possible for the Court to import, as suggested, the evidence filed in the counterclaim, which includes evidence by Shionogi who is not a party to the main action, the Court is of the view that Apotex’s counterclaim is without merit because it is time-barred and Apotex failed to establish that it suffered a loss arising from the alleged anti-competitive conduct.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5040876` offsets `36-42`; context: [630] If Apotex’s competition claim cannot stand in the context of its counterclaim, it cannot stand as a defence to Lilly’s claim in the main action.
- Evidence: `governing_rule` cue `under` at chunk `5040877` offsets `315-320`; context: Defences raised under the doctrine of equitable set-off are not subject to the expiration of limitations periods (see Canada Trustco Mortgage Co.
- Evidence: `governing_rule` cue `under` at chunk `5040878` offsets `160-165`; context: [632] The assertion of equitable set-off and disentitlement by Apotex seeks to weigh Lilly’s conduct vis-à-vis Shionogi against Lilly’s claims for infringement under the Patent Act.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5040878` offsets `265-271`; context: For the reasons that follow, I am of the view that in this particular case, Apotex cannot invoke its allegations of anticompetitive behaviour to evade its liability for infringement through disentitlement or equitable set-off.
- Evidence: `party_position` cue `claim` at chunk `5040879` offsets `943-948`; context: ):
For past conduct to be relevant to a refusal of equitable relief under the "clean hands" doctrine, relief to which the party would otherwise be entitled, such conduct must relate directly to the subject matter of the plaintiff's claim, in this case their patent.
- Evidence: `governing_rule` cue `under` at chunk `5040879` offsets `779-784`; context: ):
For past conduct to be relevant to a refusal of equitable relief under the "clean hands" doctrine, relief to which the party would otherwise be entitled, such conduct must relate directly to the subject matter of the plaintiff's claim, in this case their patent.

#### 22183:19:subtheme:26 · paragraphs 634-637

- Raw key terms: `claim, equitable, relief, added, consideration, court, defence, disentitlement`
- Display key terms: `equitable, relief, added, consideration, defence, disentitlement`
- Argument roles: `disposition, governing_rule, issue`
- Explanation: Observed roles: disposition, governing_rule, issue Display terms: equitable, relief, added, consideration, defence, disentitlement Rule/authority context: [637] The principles underlying equitable set-off, including relevant Canadian and English authorities, were canvassed by the Saskatchewan Court of Appeal in Saskatchewan Wheat Pool v. Operative outcome context: The equitable ground must go to the very root of the plaintiff's claim before a set-off will be allowed: British Anzani. Evidence spans paragraphs 634-637. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040880` offsets `222-229`; context: [634] Justice Rothstein (as he then was), framed the relevant inquiry into disentitlement as follows:
It is apparent that it is not any alleged inappropriate conduct of a party that may be relevant in the consideration of whether or not to grant equitable relief.
- Evidence: `governing_rule` cue `principles` at chunk `5040883` offsets `10-20`; context: [637] The principles underlying equitable set-off, including relevant Canadian and English authorities, were canvassed by the Saskatchewan Court of Appeal in Saskatchewan Wheat Pool v.
- Evidence: `disposition` cue `allowed` at chunk `5040883` offsets `715-722`; context: The equitable ground must go to the very root of the plaintiff's claim before a set-off will be allowed: British Anzani.

#### 22183:19:subtheme:27 · paragraphs 638-639

- Raw key terms: `commerce, equitable, federal, impeach, question, set-off, account, added`
- Display key terms: `commerce, equitable, federal, impeach, question, set-off, account, added`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: commerce, equitable, federal, impeach, question, set-off, account, added Evidence spans paragraphs 638-639. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040884` offsets `326-334`; context: ), where the following test was articulated in respect of claims of equitable set-off:
This question must be asked in each case as it arises for decision; and then, from case to case, we shall build up a series of precedents to guide those who come after us.
- Evidence: `counterargument_limitation` cue `But` at chunk `5040884` offsets `493-496`; context: But one thing is quite clear: it is not every cross-claim which can be deducted.
- Evidence: `issue` cue `question` at chunk `5040885` offsets `104-112`; context: [639] While the scope of disentitlement and equitable set-off are different, both defences ask a common question which both Federal Commerce and Visx frame in similar ways: does the unacceptable or unlawful conduct of Lilly go to the root or otherwise serve to impeach its claim and in such circumstances should the liability of Apotex be excused.

#### 22183:19:subtheme:28 · paragraphs 640-642

- Raw key terms: `patents, anticompetitive, apotex, assignment, behaviour, court, impeach, lilly`
- Display key terms: `patents, anticompetitive, apotex, assignment, behaviour, impeach, lilly`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: patents, anticompetitive, apotex, assignment, behaviour, impeach, lilly Evidence spans paragraphs 640-642. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040886` offsets `93-98`; context: [640] There is no dispute in this litigation that Lilly is the owner of all eight patents at issue.

#### 22183:19:subtheme:29 · paragraphs 643-646

- Raw key terms: `apotex, damages, infringement, patent, set-off, allow, claim, claims`
- Display key terms: `apotex, damages, infringement, patent, set-off, allow, claims`
- Argument roles: `counterargument_limitation, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, party_position, reasoning_application Display terms: apotex, damages, infringement, patent, set-off, allow, claims Position/evidence statements: However, to the extent they do so, such claims must be adjudicated within the confines of the Competition Act. Rule/authority context: What Apotex seeks to do vis-à-vis its disentitlement and equitable set-off claims is resurrect its time-barred claim under the Competition Act and give it new life in the context of a patent infringement action. Application context: First, because of the evidentiary issue discussed earlier. Evidence spans paragraphs 643-646. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040889` offsets `257-262`; context: First, because of the evidentiary issue discussed earlier.
- Evidence: `reasoning_application` cue `because` at chunk `5040889` offsets `230-237`; context: First, because of the evidentiary issue discussed earlier.
- Evidence: `governing_rule` cue `under` at chunk `5040890` offsets `230-235`; context: What Apotex seeks to do vis-à-vis its disentitlement and equitable set-off claims is resurrect its time-barred claim under the Competition Act and give it new life in the context of a patent infringement action.
- Evidence: `party_position` cue `claims` at chunk `5040891` offsets `139-145`; context: However, to the extent they do so, such claims must be adjudicated within the confines of the Competition Act.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040891` offsets `99-106`; context: However, to the extent they do so, such claims must be adjudicated within the confines of the Competition Act.

#### 22183:19:subtheme:30 · paragraphs 647-650

- Raw key terms: `court, apotex, elect, right, accounting, action, argues, canada`
- Display key terms: `apotex, elect, right, accounting, action, argues`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: apotex, elect, right, accounting, action, argues Operative outcome context: [648] In past cases, the right to elect has been denied for a variety of reasons; delay in bringing forward the action for infringement (Consolboard (1978)); “misconduct on the part of the patentee” and “the good faith o | Fundamentally, Apotex also argues that the right to elect should be denied as Lilly has not diligently prosecuted this action, which took nearly eleven years to come to trial and is inherently complex. Evidence spans paragraphs 647-650. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040893` offsets `200-207`; context: [647] With regard to the remedy of an accounting of profits, the Federal Court of Appeal has recently reiterated the well established principle that “a trial judge has complete discretion in deciding whether or not to grant this equitable remedy” (Merck & Co.
- Evidence: `disposition` cue `denied` at chunk `5040894` offsets `49-55`; context: [648] In past cases, the right to elect has been denied for a variety of reasons; delay in bringing forward the action for infringement (Consolboard (1978)); “misconduct on the part of the patentee” and “the good faith of an infringer” (Beloit Canada Ltd.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040895` offsets `92-100`; context: [649] Apotex submits that Lilly does not come before this Court with clean hands, given the evidence of its anti-competitive conduct in acquiring title to the Shionogi patents and in attempting to prevent generic entry into the market for dosage form cefaclor.
- Evidence: `disposition` cue `denied` at chunk `5040895` offsets `329-335`; context: Fundamentally, Apotex also argues that the right to elect should be denied as Lilly has not diligently prosecuted this action, which took nearly eleven years to come to trial and is inherently complex.

#### 22183:19:subtheme:31 · paragraphs 651-653

- Raw key terms: `lilly, apotex, case, court, damages, elect, infringement, reasonable`
- Display key terms: `lilly, apotex, case, damages, elect, infringement, reasonable`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: lilly, apotex, case, damages, elect, infringement, reasonable Application context: [651] Although Apotex does not appear to make a distinction between the infringement of the Lilly and the Shionogi patents, the issue of royalties can only apply to the Shionogi patents. Evidence spans paragraphs 651-653. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040897` offsets `128-133`; context: [651] Although Apotex does not appear to make a distinction between the infringement of the Lilly and the Shionogi patents, the issue of royalties can only apply to the Shionogi patents.
- Evidence: `reasoning_application` cue `apply` at chunk `5040897` offsets `156-161`; context: [651] Although Apotex does not appear to make a distinction between the infringement of the Lilly and the Shionogi patents, the issue of royalties can only apply to the Shionogi patents.

#### 22183:19:subtheme:32 · paragraphs 654-656

- Raw key terms: `lilly, action, apotex, court, date, thereafter, accounting, addition`
- Display key terms: `lilly, action, apotex, date, thereafter, accounting, addition`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: lilly, action, apotex, date, thereafter, accounting, addition Evidence spans paragraphs 654-656. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040900` offsets `413-418`; context: It should also be noted that in this case, the last of the patents at issue expired on July 26, 2000.

#### 22183:19:subtheme:33 · paragraphs 657-663

- Raw key terms: `award, damages, para, punitive, action, apotex, court, lilly`
- Display key terms: `award, damages, para, punitive, action, apotex, lilly`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, reasoning_application Display terms: award, damages, para, punitive, action, apotex, lilly Rule/authority context: Applying these principles, the Court concludes that this conduct is more properly dealt with in the context of an award for costs. Application context: 36) Therefore, the Court cannot award punitive damages at this stage as the question of general damages has been bifurcated. | Applying these principles, the Court concludes that this conduct is more properly dealt with in the context of an award for costs. Operative outcome context: Leave in this regard was denied as the conduct alleged in the amended plea, which is of the same nature than that which is advanced today, “is not conduct that can ground an award of punitive or exemplary damages. Evidence spans paragraphs 657-663. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040903` offsets `269-276`; context: (3d) 865, held that “the Court cannot decide whether exemplary damages are required until after it decides whether the general damages were insufficient for punishment and deterrent purposes.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5040903` offsets `493-502`; context: 36) Therefore, the Court cannot award punitive damages at this stage as the question of general damages has been bifurcated.
- Evidence: `governing_rule` cue `principles` at chunk `5040906` offsets `463-473`; context: Applying these principles, the Court concludes that this conduct is more properly dealt with in the context of an award for costs.
- Evidence: `reasoning_application` cue `concludes` at chunk `5040906` offsets `485-494`; context: Applying these principles, the Court concludes that this conduct is more properly dealt with in the context of an award for costs.
- Evidence: `disposition` cue `denied` at chunk `5040907` offsets `341-347`; context: Leave in this regard was denied as the conduct alleged in the amended plea, which is of the same nature than that which is advanced today, “is not conduct that can ground an award of punitive or exemplary damages.
- Evidence: `reasoning_application` cue `apply` at chunk `5040909` offsets `741-746`; context: 72) do not apply to the case at bar.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040909` offsets `265-272`; context: However, this element has already been weighted in affording Lilly with the right to elect for an accounting of Apotex’s profits.

#### 22183:19:subtheme:34 · paragraphs 664-669

- Raw key terms: `interest, damages, para, award, awarded, cannot, compound, court`
- Display key terms: `interest, damages, para, award, awarded, cannot, compound`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: interest, damages, para, award, awarded, cannot, compound Rule/authority context: Unless the Court is awarding interest pursuant to para. | 36(2) on interest accruing under s. Application context: F-7, applies, giving jurisdiction to this Court to include an award of prejudgment interest, at a rate it considers reasonable in the circumstances, on a sum of money representing damages. Operative outcome context: The claim for punitive damages would fail irrespective of whether leave to amend was granted or not. Evidence spans paragraphs 664-669. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040910` offsets `356-363`; context: Lilly’s motion raises concerns with regards to whether it constitutes a collateral attack on the 2003 decision of Prothonotary Aronovitch cited above.
- Evidence: `disposition` cue `granted` at chunk `5040910` offsets `813-820`; context: The claim for punitive damages would fail irrespective of whether leave to amend was granted or not.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040911` offsets `361-372`; context: Unless the Court is awarding interest pursuant to para.
- Evidence: `reasoning_application` cue `applies` at chunk `5040911` offsets `139-146`; context: F-7, applies, giving jurisdiction to this Court to include an award of prejudgment interest, at a rate it considers reasonable in the circumstances, on a sum of money representing damages.
- Evidence: `governing_rule` cue `under` at chunk `5040912` offsets `137-142`; context: 36(2) on interest accruing under s.
- Evidence: `governing_rule` cue `under` at chunk `5040915` offsets `95-100`; context: [669] Justice Major recognized that “the court has the jurisdiction to award compound interest under the court’s general equitable jurisdiction” (para.

#### 22183:19:subtheme:35 · paragraphs 670-672

- Raw key terms: `america, appeal, award, bank, compound, court, interest, para`
- Display key terms: `america, award, bank, compound, interest, para`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: america, award, bank, compound, interest, para Rule/authority context: [670] Bank of America Canada is a contract case and on that basis the Ontario Court of Appeal had concluded that equity did not apply and thus there was no interest payable “by a right other than under [s. Application context: [670] Bank of America Canada is a contract case and on that basis the Ontario Court of Appeal had concluded that equity did not apply and thus there was no interest payable “by a right other than under [s. | [672] What is more, the reasoning of Bank of America Canada has even been applied in British Columbia, where the relevant legislation, the Court Order Interest Act, R. Evidence spans paragraphs 670-672. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040916` offsets `690-695`; context: This decision has led the Courts to re-examine the issue of compound interest.
- Evidence: `governing_rule` cue `under` at chunk `5040916` offsets `196-201`; context: [670] Bank of America Canada is a contract case and on that basis the Ontario Court of Appeal had concluded that equity did not apply and thus there was no interest payable “by a right other than under [s.
- Evidence: `reasoning_application` cue `apply` at chunk `5040916` offsets `128-133`; context: [670] Bank of America Canada is a contract case and on that basis the Ontario Court of Appeal had concluded that equity did not apply and thus there was no interest payable “by a right other than under [s.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040916` offsets `343-350`; context: However, the Supreme Court of Canada held that para.
- Evidence: `reasoning_application` cue `applied` at chunk `5040918` offsets `74-81`; context: [672] What is more, the reasoning of Bank of America Canada has even been applied in British Columbia, where the relevant legislation, the Court Order Interest Act, R.

#### 22183:19:subtheme:36 · paragraphs 673-674

- Raw key terms: `award, awarding, court, courts, established, federal, interest, order`
- Display key terms: `award, awarding, courts, established, federal, interest, order`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: award, awarding, courts, established, federal, interest, order Rule/authority context: [673] In the present circumstances, the Court is not in a position to evaluate whether or not Lilly is entitled to pre-judgment interest as part of its damages for, as mentioned, “any question as to damages suffered by [ | However, this award is conditional upon the reference judge not awarding interest under para. Application context: Therefore, in order to ensure that a form of pre-judgment interest is awarded irrespective of the outcome of the reference, the Court will grant simple pre-judgment interest at the rate to be calculated separately for ea Evidence spans paragraphs 673-674. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040919` offsets `79-86`; context: [673] In the present circumstances, the Court is not in a position to evaluate whether or not Lilly is entitled to pre-judgment interest as part of its damages for, as mentioned, “any question as to damages suffered by [Lilly]” has been bifurcated pursuant to the November 29, 1999 order of Justice Hugessen.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040919` offsets `248-259`; context: [673] In the present circumstances, the Court is not in a position to evaluate whether or not Lilly is entitled to pre-judgment interest as part of its damages for, as mentioned, “any question as to damages suffered by [Lilly]” has been bifurcated pursuant to the November 29, 1999 order of Justice Hugessen.
- Evidence: `governing_rule` cue `under` at chunk `5040920` offsets `781-786`; context: However, this award is conditional upon the reference judge not awarding interest under para.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5040920` offsets `223-232`; context: Therefore, in order to ensure that a form of pre-judgment interest is awarded irrespective of the outcome of the reference, the Court will grant simple pre-judgment interest at the rate to be calculated separately for each year since the infringing activity began at the average annual bank rate established by the Bank of Canada as the minimum rate at which the Bank of Canada makes short-term advances to the banks listed in Schedule 1 of the Bank Act, R.

#### 22183:19:subtheme:37 · paragraphs 675-676

- Raw key terms: `costs, action, amend, among, apotex, appropriate, cites, communications`
- Display key terms: `costs, action, amend, among, apotex, appropriate, cites, communications`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: costs, action, amend, among, apotex, appropriate, cites, communications Evidence spans paragraphs 675-676. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040921` offsets `17-25`; context: [675] As for the question of post-judgment interest, it is well established that the appropriate rate is 5%, not compounded, as established by s.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040922` offsets `524-532`; context: Among these elements, Lilly cites the failure to provide proper documents relating to manufacturing processes, late discovery productions, wasteful experiments rendered necessary by Apotex’s failure to provide proper discovery, lack of notice for testing conducted by Apotex, deficient pleadings, lack of pre-trial cooperation, unnecessary duplication of expert’s evidence and especially the failure to disclose, even to the Court (Justice Hugessen), communications with Lupin concerning its manufacturing processes.

#### 22183:19:subtheme:38 · paragraphs 677-679

- Raw key terms: `apotex, arguments, chosen, court, documents, doubt, earlier, failure`
- Display key terms: `apotex, arguments, chosen, documents, doubt, earlier, failure`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: apotex, arguments, chosen, documents, doubt, earlier, failure Evidence spans paragraphs 677-679. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040923` offsets `339-346`; context: It is difficult to imagine that the file would not have been closely revised in preparation for trial, regardless of whether the July 4, 2000 letter from Lupin was inadvertently filed by a clerk without bringing it to the attention of the lawyers concerned.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040923` offsets `119-127`; context: [677] In respect of the failure to disclose Lupin information and communications, Apotex has chosen not to present any evidence as to how it happened and why this failure was not or could not have been discovered earlier.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040925` offsets `243-250`; context: However, the personal sanctions against counsel for Apotex sought by Lilly are not.

#### 22183:19:subtheme:39 · paragraphs 680-686

- Raw key terms: `apotex, counterclaim, lilly, well, canada, canadian, cefaclor, costs`
- Display key terms: `apotex, counterclaim, lilly, well, canadian, cefaclor, costs`
- Argument roles: `disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue Display terms: apotex, counterclaim, lilly, well, canadian, cefaclor, costs Rule/authority context: [683] On March 9, 2001, Apotex brought a counterclaim against Lilly, seeking damages pursuant to s. Operative outcome context: (collectively, “Lilly”) or both, to allow Eli Lilly and Company to acquire the Canadian patents and patent rights granted to Shionogi under Canadian Letters Patent Nos. Evidence spans paragraphs 680-686. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040926` offsets `43-51`; context: [680] That said, how much more is the real question.
- Evidence: `issue` cue `issue` at chunk `5040927` offsets `150-155`; context: For this reason, the Court will issue a more detailed order after giving an opportunity to the parties to make further submissions in respect of the amount of costs only.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040929` offsets `85-96`; context: [683] On March 9, 2001, Apotex brought a counterclaim against Lilly, seeking damages pursuant to s.
- Evidence: `disposition` cue `granted` at chunk `5040929` offsets `461-468`; context: (collectively, “Lilly”) or both, to allow Eli Lilly and Company to acquire the Canadian patents and patent rights granted to Shionogi under Canadian Letters Patent Nos.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040930` offsets `681-690`; context: Sherman’s testimony in the main action as part of the evidence in the counterclaim.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040931` offsets `20-29`; context: Sherman’s testimony was supplemented by that of two other Apotex employees, Mr.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040932` offsets `589-598`; context: Fahner also touched on Apotex’s rebate practices and the transcript of his testimony in the main action was also included as evidence in the counterclaim by consent of the parties.

#### 22183:19:subtheme:40 · paragraphs 687-691

- Raw key terms: `lilly, shionogi, testified, witness, agreement, called, cefaclor, department`
- Display key terms: `lilly, shionogi, testified, witness, agreement, called, cefaclor, department`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: lilly, shionogi, testified, witness, agreement, called, cefaclor, department Rule/authority context: Also, he testified as to the timing of negotiations between Shionogi and Lilly leading up to the assignment of the Shionogi patents and to his belief that prior to this assignment Lilly held an exclusive licence under th Evidence spans paragraphs 687-691. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040933` offsets `508-514`; context: The Court did not find any of his evidence determinative or even particularly relevant with regard to any of the issues dealt with in these reasons and thus these objections need not be considered further.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040933` offsets `384-393`; context: Many objections were formulated with regard to his testimony.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040935` offsets `20-29`; context: Pytinia’s testimony consisted of identifying documents from Lilly’s records, including the agreements of 1975 and 1995 between Lilly and Shionogi.
- Evidence: `governing_rule` cue `under` at chunk `5040935` offsets `369-374`; context: Also, he testified as to the timing of negotiations between Shionogi and Lilly leading up to the assignment of the Shionogi patents and to his belief that prior to this assignment Lilly held an exclusive licence under these patents.

#### 22183:19:subtheme:41 · paragraphs 692-704

- Raw key terms: `shionogi, apotex, evidence, lilly, court, testimony, respect, tokaji`
- Display key terms: `shionogi, apotex, lilly, testimony, respect, tokaji`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: shionogi, apotex, lilly, testimony, respect, tokaji Rule/authority context: Stringer’s evidence was heard under reserve pending the determination of these objections. | 69(2)(c) of the Competition Act: (2) In any proceedings before the Tribunal or in any prosecution or proceedings before a court under or pursuant to this Act, (c) a record proved to have been in the possession of a parti Application context: [703] The Court is of the view that this provision only applies to evidence tendered in the course of a party’s case in chief. Operative outcome context: McCool denied having ever met Dr. Evidence spans paragraphs 692-704. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040938` offsets `449-456`; context: To determine whether more detailed reasons about this conclusion were necessary, the Court considered the issues on which this decision is based with and without the benefit of Mr.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040938` offsets `54-63`; context: [692] Objections were formulated with respect to this testimony, particularly in respect of matters where Mr.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040940` offsets `649-657`; context: Although Ms.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040941` offsets `349-358`; context: This testimony is in direct contradiction with that of Dr.
- Evidence: `disposition` cue `denied` at chunk `5040941` offsets `433-439`; context: McCool denied having ever met Dr.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040942` offsets `139-148`; context: McCool, were first alluded to in the testimony of Dr.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040943` offsets `151-160`; context: Tokaji was aided in his testimony by an interpreter.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040944` offsets `210-218`; context: He also offered evidence as to Shionogi products being sold through licensing arrangements, particularly with Lilly and Schering-Plough.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040944` offsets `440-448`; context: Although his evidence adds very little to the evidence already included in A-29 and the admitted facts, his testimony was the subject of many objections from Apotex.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040945` offsets `34-42`; context: [699] Again none of the contested evidence is determinative.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040946` offsets `90-98`; context: Tokaji, Apotex sought to introduce in evidence a series of correspondence between Lilly and Shionogi (TX-252 to 259) of which he had no personal knowledge.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040946` offsets `208-215`; context: However, Mr.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040947` offsets `344-353`; context: The sole purpose of his testimony was to shed light on the context of correspondence between Lilly and Shionogi just prior to the assignment which Apotex sought to enter as evidence in the course of the cross-examination of Mr.
- Evidence: `governing_rule` cue `under` at chunk `5040947` offsets `674-679`; context: Stringer’s evidence was heard under reserve pending the determination of these objections.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040948` offsets `115-123`; context: [702] With regard to TX-252 to 259, the Court has come to the conclusion that these exhibits are not admissible in evidence.
- Evidence: `governing_rule` cue `under` at chunk `5040948` offsets `341-346`; context: 69(2)(c) of the Competition Act:
(2) In any proceedings before the Tribunal or in any prosecution or proceedings before a court under or pursuant to this Act,
(c) a record proved to have been in the possession of a participant or on premises used or occupied by a participant or in the possession of an agent of a participant shall be admitted in evidence without further proof thereof and is prima facie proof
(i) that the participant had knowledge of the record and its contents,
(ii) that anything recorded in or by the record as having been done, said or agreed on by any participant or by an agent of a participant was done, said or agreed on as recorded and, where anything is recorded in or by the record as having been done, said or agreed on by an agent of a participant, that it was done, said or agreed on with the authority of that participant, and
(iii) that the record, where it appears to have been written by any participant or by an agent of a participant, was so written and, where it appears to have been written by an agent of a participant, that it was written with the authority of that participant.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040949` offsets `67-75`; context: [703] The Court is of the view that this provision only applies to evidence tendered in the course of a party’s case in chief.
- Evidence: `reasoning_application` cue `applies` at chunk `5040949` offsets `56-63`; context: [703] The Court is of the view that this provision only applies to evidence tendered in the course of a party’s case in chief.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040950` offsets `102-110`; context: [704] Indeed, these documents were known to Apotex well before it attempted to have them entered into evidence on September 22, 2008.

#### 22183:19:subtheme:42 · paragraphs 705-705

- Raw key terms: `account, admissible, apotex, arrived, attempt, authorities, circumstances, cited`
- Display key terms: `account, admissible, apotex, arrived, attempt, authorities, circumstances, cited`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: account, admissible, apotex, arrived, attempt, authorities, circumstances, cited Evidence spans paragraphs 705-705. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5040951` offsets `303-309`; context: This being said, the Court has examined the issues relevant to its determination of the counterclaim both with and without said evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040951` offsets `249-257`; context: The documents marked TX-252 to 259 are not admissible in evidence.

#### Section text

[436] For our purposes, it is sufficient to say that Rydon and Coe teach at least the following:[158]
The reaction between Cl and TPP is quite complex and some mechanisms are still regarded as obscure or not well understood. (Rydon, p. 3044)
Theoretically, [159] the system may contain as many as 45 species, most of which would be in equilibrium (covalent form/ionic form).[160] Depending on the conditions used for the reaction, including temperature, concentration and solvents, different species will be produced “while solubility will play a major role in determining the nature of the solid phase separating from solution.” (Rydon, p. 3045)
The authors reported on and tested nine crystalline solids, six of which were described in Coe as dihalides (see Rydon, p. 3043). Certain compounds prepared by the authors could not be prepared as purified specimens.[161]
Whatever their true nature or stoichiometry, Rydon indicates that:
The reaction of Cl/TPP in a ratio of 1 to 2 in chlorobenzene produces tetraphenoxy-chloride – a monohalide[162] (p. 3052). The reaction of Cl/TPP in a ratio of 1 to 1 without solvent produces triphenoxy-dichloride – a dihalide. (p. 3053, Triphenoxy-dichlorides A) The reaction of Cl/TPP in a ratio of 1 to 1 in hexane produces triphenoxy-dichloride – a dihalide. (p. 3053, Example B) The reaction of Cl/TPP in a 1 to 1 ratio in acetonitrite produces triphenoxy-dichloride – a dihalide. (p. 3053, Triphenoxy-dichlorides C)
With respect to halogenation, Coe only tested the product(s) from the reaction of Cl and TPP without solvent.[163] Rydon notes that the “monohalides may have some advantages over the dihalides previously employed for the preparation of alkyl halides.”[164] (Footnote omitted, p. 3044)

[437] I turn now to the article by Ramirez, who was described by Dr. Olah as a pioneer in 31P NMR spectroscopy. In that article, it appears that the authors were trying to obtain an authentic sample of pentaphenoxyphosphorane and analyze it. In that respect, they were following work that started in 1927 and was pursued by other authors in 1959. Apparently, these attempts produced mixtures of dichlorotriphenoxyphosphorane and other materials, leading the authors to reinvestigate the previously reported mechanisms in Rydon. Though they give few details about their experiments, the Court finds that one can reasonably[165] infer from the reference to the addition of Cl to TPP in hexane solution for the purpose of reinvestigating previously reported synthesis of a triphenylphosphite dichloride (dichlorotriphenoxyphosphorane)[166] that they followed the procedure of Example B on p. 3053 of Rydon, which is the only synthesis known in hexane in evidence before the Court. The authors dried the precipitate obtained and tried in vain to purify it (not part of procedure in Example B). They note that:
All that can be said about this substance is that, in CH2Cl2 solution, it gives only one signal in the 31P nmr spectrum. The chemical shift does not vary significantly in several solvents.
[p. 3509]
The said shift was at -22.8[167] and the authors attributed it to what was “regarded as dichlorotriphenoxyphosphorane”, which is the dihalide referred to in Rydon.[168]
9.2.4. The Inventive Concept

[438] The inventive concept of claim 17 is that the reaction of equimolar amounts of triaryl phosphate and Cl or Br in a halogenated or aromatic hydrocarbon solvent produces an intermediate that is the faster forming product of the reaction: the so-called kinetic complex.
9.2.5. The Differences between the Common General Knowledge and the above-mentioned Publications and the Inventive Concept

[439] In respect of equimolar quantities of Cl and TPP[169], the only solvent used in Rydon and Coe was hexane, which is not an aromatic or halogenated hydrocarbon solvent.

[440] Although, as mentioned, it is evident that the reaction performed in Rydon and Ramirez produced a first formed intermediate, there is no recognition therein that the above-mentioned reaction produces such an intermediate or that such intermediate (first compound) will transform over time into a second compound (final compound).
9.2.6. Would These Differences be Obvious to the Person Skilled in the Art?

[441] Apotex argues that the use of chlorobenzene or methylene chloride (aromatic or halogenated hydrocarbon solvent) was a worthwhile option and that it was self-evident that it ought to work, particularly to perform chemistry on cephalosporins.

[442] According to the defendant, Rydon taught the use of chlorobenzene and the fact that the method used involved non-equivalent amounts of the reactants (a 2:1 ratio) is irrelevant. Choosing a particular solubilizing solvent is not inventive.

[443] At first, the Court was sympathetic to this argument, but on a closer review of the evidence, the Court realized that it may well have been influenced by knowledge gained from the ‘007 patent. Hindsight is the one thing that is particularly important to avoid at this stage of the inquiry.

[444] Uncharacteristically, Apotex’s oral and written arguments were extremely brief on this point (see para. 112 of their memorandum on validity; p. 7 of their representations on reply; and, paras. 60-62 of the submissions on the implications of Sanofi).

[445] They rely essentially on their cross-examination of Dr. Baldwin, who said that one would know the solubility properties required for the use of solvents in cephalosporin chemistry. Also, Apotex’s counsel noted that in Ramirez, whatever product was in the sample used for the 31P NMR analysis was soluble in methylene chloride.

[446] First, with respect to the skilled addressee’s knowledge of solvents suitable for cephalosporin chemistry, given the definition of the skilled addressee in the ‘007 patent, it is not clear how this evidence would be relevant. How and why would a posita, as defined, would come to use the kinetic product to perform chemistry on cephalosporins? Such use, according to the evidence of Dr. Baldwin, was inventive (see below discussion of Lilly process patents).

[447] One would think that, if a solvent is obvious for any reason, it is sufficient to conclude the present inquiry in respect of this element of the inventive concept. Thus, Apotex did not need to show that the use of such solvents was obvious for this type of chemistry.

[448] With respect to the second argument based on Ramirez, the Court notes that the actual reaction between Cl and TPP was carried out in hexane and that none of the experts testified that this publication taught them that the dihalide discussed in Rydon would be produced by carrying out the reaction in methylene chloride.

[449] Apotex certainly did not explain how the Court should deal with the evidence of Dr. Modro, who commented on claim 17 in a manner that appears to contradict Apotex’s current argument that Rydon taught the use of chlorobenzene or an aromatic hydrocarbon solvent to prepare a dihalide. In effect, with full knowledge of what was disclosed in Ramirez and Tseng, Dr. Modro said, at paras. 76 and 77 of his report (A-13), that based on the statement found at p. 3044 of Rydon and the fact that the actual reaction carried out therein resulted in the formation a monohalide (tetraphenoxyphosphorus chloride), this art taught that the use of chlorobenzene does not produce the kinetic product claimed in the ‘007 patent.[170]

[450] Having carefully examined the evidence and considered the motivation for as well as the details of how the inventors made their discovery, the Court concludes that Apotex has not established on a balance of probabilities that it would be more or less self-evident that the use of an aromatic or halogenated hydrocarbon solvent to carry out the reaction described in at p. 3053 of Rydon (Example B) ought to produce the same compound as when done in hexane, particularly that it would produce the dihalide described in Rydon.

[451] In my view, this is sufficient to conclude that claim 17 is not obvious. For whether or not one could actually identify the compound formed through the use of 31P NMR spectroscopy is irrelevant if Rydon in fact taught away from the use of the claimed solvent.

[452] However, as this matter may go further, it is worth reviewing the evidence in respect of what the posita would learn through the allegedly routine use of such technology. This is especially so considering that this evidence and my findings in this respect will be relevant to the inquiry into the obviousness of the Lilly process patents, particularly the aspect of the claimed invention relating to the stabilization of the kinetic product through the use of a tertiary base.

[453] Obviously, Apotex’s first hurdle is to explain the conclusion in Ramirez, which contradicts their argument that one could quickly identify the first formed intermediate of the reaction simply by using the 31P NMR technology.[171]

[454] For that purpose, they rely on the experiments carried out by Dr. Modro, as well as the experiments carried out in Tseng and Michalski.

[455] To determine what weight should be attributed to such evidence (particularly the post art) the Court will quickly review how Apotex’s experts used this information.

[456] Dr. Chivers concluded that a posita would be able to understand and identify the kinetic compound on the basis of the experiments done by Dr. Modro, who performed 31P NMR tests and analyzed the evolution of the spectral information about the products in solution over 23 hours (see A-18, paras. 29-32). Dr. Chivers only referred to Tseng and Michalski to support his view that the thermodynamic compound has the empirical formula of (PhO)4PCl (monohalide). Surprisingly, Dr. Chivers does not discuss the impact of Ramirez at all, even though it would have been part of the prior art available to the posita.[172]

[457] Dr. Modro uses Tseng to confirm his view that: 1) the tetraphenoxyphosphorane (monochloride) is the thermodynamic product described in the ‘007 patent (by comparing the ppm shift obtained by Tseng and the ppm shift disclosed in the ‘007 patent for the thermodynamic product); and, 2) the equilibrium mechanism involved (ionic form versus covalent form which is quite distinct from the disproportionation mechanism discussed earlier). He refers to neither Michalski nor Ramirez.[173]

[458] Dr. Olah is the only expert who refers to Ramirez. He affirms that based on the conclusion of Tseng and Michalski the authors of Ramirez were wrong. Dr. Olah does not explain why, without using the knowledge gained from the ‘007 patent,[174] it would be so evident that both Rydon and Ramirez were wrong in identifying the product of the experiment described at p. 3053 of Rydon (Example B) as a dihalide. As I said, in any event, the stoichiometry of the compounds is not particularly relevant here.

[459] Dr. McClelland refers to the rapid equilibrium phenomenon which was disclosed in Rydon, further explained in Tseng and perfected in Michalski. This phenomenon explains, in his view, the difference in ppm shifts reported for the kinetic product. Again, this relates to the equilibrium between the ionic and the covalent form of the kinetic product, not to its transition to the thermodynamic form (disproportionation).

[460] This evidence is not particularly helpful to determine if, through the use of this technology and by simply repeating the process set out in Rydon (Example B, p. 3053), one would have come to the conclusion that the reaction produces two products (a first, faster forming intermediate and a final product).

[461] Dr. McClelland did say on cross-examination that reversing the order of addition of the reactants, as was done by Tseng, was a routine variation of Rydon’s method (Example B, at p. 3053). The Court accepts this evidence and notes that it is somewhat corroborated by Dr. Blaszczak’s evidence on discovery, when he discusses what was done by Mr. Fisher.[175]

[462] However, there is no similar evidence in respect of the method and the temperature used by the authors of Michalski when they reacted the TPP with the halogen. This was clearly very different from the process disclosed in Rydon and there is no evidence that it was simply a variation that would routinely be carried out by a posita[176] before the date of filing. The Court is not prepared to assume that what was done in Michalski was what a posita would be expected to do if he simply wanted to identify the product formed by the Rydon method, as opposed to embarking on a full research project to elucidate the reaction mechanism of TPP and halogen.[177]

[463] That said, there is no evidence that the method used (31P NMR) for the experiments performed in Ramirez was not in accordance with the practice of positas as of the filing date. In fact, there is no evidence that there was any accepted practice as to when a spectra should be taken – such as before or after attempts to purify a product or within a certain time of having prepared a product.

[464] Certainly, there is no evidence that a posita would, as a matter of routine, take and analyze 31P NMR spectras of the product of the reaction over a period of 23 hours. In fact, this was not done in any of the publications before the Court.

[465] As mentioned earlier, Dr. Modro did carry out this type of experiment on behalf of Apotex. These were done with full knowledge of the teachings of the ‘007 patent. The Court does not accept these experiments as proof of what a posita carrying out routine experimentation at the relevant time would have done.

[466] In fact, it appears that, to attribute a particular ppm shift to a specific compound, one needs to know with some certainty what species is in the sample being tested.

[467] Ramirez, having failed to obtain a purified specimen, tentatively attributed the shift of -22.8 (CH2Cl2) to the product that was “regarded as” dichlorotriphenoxyphosphorane (triphenoxy-dichlorides in Rydon). Meanwhile, Tseng said that the -22.5 ppm shift (in deuterated chloroform) he obtained from the reaction of Cl and TPP without solvent was “likely to be” that of tetraphenoxyphosphorane because it was similar to the shift reported for that substance by Nesterov in what Dr. Baldwin described as an obscure Russian publication. In fact, Dr. Baldwin said that this method was quite suspect. Tseng certainly came to a conclusion in this respect that runs contrary to the teaching of Rydon.

[468] There is also no evidence that Ramirez or Tseng[178] discuss the disproportionation mechanism referred to by Drs. Modro and Olah. There is no indication that they clearly and easily understood what these two experts suggested was obvious.

[469] In fact, it is telling that Tseng, who reported a shift of +7.7 ppm for the compound resulting from the reaction of equivalent amounts of TPP and Cl, attributed the other two shifts he obtained (one of which was the -22.5 ppm shift) to “impurities,” and not to a more stable form of the first compound he obtained.

[470] With respect to motivation, although the work of Ramirez, Tseng and Michalski do support the view that there was an interest in identifying the compounds reported in Rydon, it is not clear that these authors were looking for a halogenating compound. None of their experiments are directed to halogenation or to the properties of the Rydon compounds as halogenating reagents. They more likely resemble those carried out by theoretical chemists interested in the mechanistical reaction of Cl and TPP reported in Coe and Rydon. That said, the Court is ready to assume a certain degree of motivation.

[471] Sanofi teaches that in some circumstances, the means by which the inventor reached the invention may provide evidence in support of a particular conclusion on obviousness.

[472] Such a review will indeed be useful when inquiring into the obviousness of the Lilly process patents. However, the path followed by the inventor does not shed much new light in respect of claim 17 of the ‘007 patent. It mostly corroborates Dr. Baldwin’s view that, contrary to theoretical chemists, practicing synthesis chemists are more interested in the reactivity of compounds than using techniques such as 31P NMR spectroscopy to characterize and identify compounds unless they are motivated to do so by reasons other than just looking for a halogenating compound.

[473] In effect, it appears the inventors were not motivated to use 31P NMR spectroscopy to characterize the products of the reaction of TPP and Cl until they encountered a problem reproducing the experiment where they had successfully chlorinated the enol on which they were working.[179] Until then, they were satisfied to work with whatever product resulted from reacting equivalent amounts of TPP and Cl in the solvent in which they were working on their cephalosporin substrate. Thus, it is the discovery that in certain circumstances the reagent produced by the reaction worked while it was inactive in others, which led to an in-depth study of the products, their stability, method of formation and structure-activity relationship.

[474] Moreover, the use of TPP and Cl was not a step undertaken on the basis of knowledge gained from Coe and Rydon. In effect, the idea to try phosphite as a possible reagent came to a Lilly chemist working in a different department[180] after a discussion with a graduate student at Harvard, who was working on a totally different project but had noted that phosphites were more reactive than phosphines in his hands.

[475] In view of the foregoing, Apotex has not established that by practicing the method described in Example B, p. 3053 of Rydon with the benefit of 31P NMR spectroscopy, it would be more or less evident that the faster forming product of the reaction was an intermediate (of transient nature). It would thus not be more or less evident to the posita that it would be beneficial to stabilize this compound by using a tertiary base.[181]
9.3. The Lilly Process Patents
9.3.1. Identify the Skilled Addressee

[476] I shall use the definition of the posita found at para. 92.
9.3.2. The Relevant Common General Knowledge

[477] The common general knowledge described in respect of the ‘007 patent would be available to the skilled addressee of the Lilly process patents.

[478] The disclosures of these process patents make it very clear that the particular steps or chemistry intended to be performed, i.e. the cephalosporin sulfoxide reduction, the enol chlorination and the imino halide formation were known in the prior art but were performed using other reagents.

[479] It was also known in 1978 that various phosphorus compounds (including PCl5) could reduce sulfoxides in general (as opposed to the more complex cephem cephalosporin sulfoxides under review).

[480] There was a known reagent called the Vilsmeier reagent which was typically made by using PCl3 to transform dimethylformamide. It was also known that PCl5 as well as other compounds such as phosphine, oxalyl chloride and thionyl chloride could be used with dimethylformamide to generate the Vilsmeier reagent. The Vilsmeier reagent is a non phosphorus reagent.

[481] In respect of cephalosporin synthesis, the posita generally knew how to change an OH at the 3-position to a Cl using the Vilsmeier reagent. It was known that this reagent could chlorinate an enol and reduce a sulfoxide. PCl5 could then be used as reagent to cleave the 7-amino side chain. However, PCl3 could not be used alone to perform such cleavage.

[482] The Court is also satisfied that at the relevant time, the posita would naturally view non-cephalosporin publications with some caution. He or she would not simply accept chemical reactions or reagents used in other fields and on less complex molecules as being directly applicable.

[483] With respect to sulfoxide reduction in particular, the natural caution described in Dr. Baldwin’s affidavit would be heightened by the fact that the literat

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 22183:20 · paragraphs 706-714

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `687c1e309f44dda78d96a1b41b5e9074d99620240f93c84d99970262f65a7ebc`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:20:subtheme:1 · paragraphs 706-707

- Raw key terms: `apotex, church, hollis, lilly, ross, shionogi, aidan, although`
- Display key terms: `apotex, church, hollis, lilly, ross, shionogi, aidan, although`
- Argument roles: `counterargument_limitation, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue Display terms: apotex, church, hollis, lilly, ross, shionogi, aidan, although Rule/authority context: Although it is clear that these experts have experience in applying tests with respect to anti-competitive behaviour under the Competition Act, the latter two do not have any particular knowledge or expertise in respect  Evidence spans paragraphs 706-707. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5040952` offsets `433-438`; context: Although it is clear that these experts have experience in applying tests with respect to anti-competitive behaviour under the Competition Act, the latter two do not have any particular knowledge or expertise in respect of the pharmaceutical industry.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5040952` offsets `316-324`; context: Although it is clear that these experts have experience in applying tests with respect to anti-competitive behaviour under the Competition Act, the latter two do not have any particular knowledge or expertise in respect of the pharmaceutical industry.
- Evidence: `issue` cue `whether` at chunk `5040953` offsets `114-121`; context: Hollis, was tasked with defining the relevant market for bulk cefaclor in order to determine whether or not the assignment of the Shionogi patents to Lilly would have had an effect on Lilly’s market power.

#### 22183:20:subtheme:2 · paragraphs 708-710

- Raw key terms: `action, apotex, included, main, mcclelland, physician, used, accountant`
- Display key terms: `action, apotex, included, main, mcclelland, physician, used, accountant`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: action, apotex, included, main, mcclelland, physician, used, accountant Evidence spans paragraphs 708-710. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040954` offsets `243-248`; context: As the herein decision does not turn in any way on evidence of physician prescribing practices in Canada, this issue need not be decided.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040954` offsets `183-191`; context: As the herein decision does not turn in any way on evidence of physician prescribing practices in Canada, this issue need not be decided.
- Evidence: `issue` cue `whether` at chunk `5040955` offsets `378-385`; context: McClelland, who had testified in the main action, filed a report explaining the distinction between the Lilly and Shionogi patents and processes and as to whether or not, as of 2003, there existed other publicly known commercially viable processes that could be used to make bulk cefaclor.
- Evidence: `evidence_fact` cue `testimony` at chunk `5040955` offsets `517-526`; context: His testimony sought to establish one of the main, if not the most important, premises for the economists’ opinions, particularly those of Dr.
- Evidence: `counterargument_limitation` cue `although` at chunk `5040956` offsets `382-390`; context: McClelland also indicated in cross-examination that he had reached the same conclusion when asked by Apotex to carry out the same research in the late 1990’s (1997 or 1998) and that, although not mandated by Apotex to do so, in 1985 anybody carrying out the same research would have probably come to the same conclusion.

#### 22183:20:subtheme:3 · paragraphs 711-714

- Raw key terms: `apotex, evidence, opinion, particularly, antibiotics, cefaclor, decision, expertise`
- Display key terms: `apotex, opinion, particularly, antibiotics, cefaclor, expertise`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: apotex, opinion, particularly, antibiotics, cefaclor, expertise Application context: Cole filed a report on how the damages of Apotex should be calculated and gave some indication as to the licensing rate that should have applied had Shionogi licensed Apotex for the use of its patented processes. Evidence spans paragraphs 711-714. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040957` offsets `816-821`; context: That said, the level of royalties was not an issue on which the Court reached a conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040957` offsets `581-589`; context: Cole’s evidence dealing with royalty rates would have had very little weight, for the comparables he used were questionable and insufficient, and he has little expertise dealing with such matters.
- Evidence: `reasoning_application` cue `applied` at chunk `5040957` offsets `147-154`; context: Cole filed a report on how the damages of Apotex should be calculated and gave some indication as to the licensing rate that should have applied had Shionogi licensed Apotex for the use of its patented processes.
- Evidence: `issue` cue `question` at chunk `5040958` offsets `438-446`; context: Given the basis of my decision this question has not been considered at all; nor has Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040958` offsets `32-40`; context: Gans offered evidence as to how physicians select the medicines they prescribe to patients, particularly antibiotic medication.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040960` offsets `200-208`; context: Once again this evidence was not relevant to the matters on which this decision stands.

#### Section text

[706] Turning now to the experts, Apotex called six expert witnesses and Lilly and Shionogi collectively called two experts witnesses.[286] Among the experts testifying on Apotex’s behalf, three of them, Aidan Hollis, Jeffrey Church and Thomas Ross, were economists (see details of their qualifications in Chart A). Although it is clear that these experts have experience in applying tests with respect to anti-competitive behaviour under the Competition Act, the latter two do not have any particular knowledge or expertise in respect of the pharmaceutical industry.

[707] The first, Dr. Hollis, was tasked with defining the relevant market for bulk cefaclor in order to determine whether or not the assignment of the Shionogi patents to Lilly would have had an effect on Lilly’s market power. Dr. Church and Dr. Ross then sought to establish the competitive effects of the transfer of Shionogi’s patent rights to Lilly and the harm suffered by Apotex as a result of this transfer given its position as a bulk purchaser of cefaclor.

[708] A part of the proposed qualification of Dr. Hollis, which included expertise in prescribing practices, elicited an objection. As the herein decision does not turn in any way on evidence of physician prescribing practices in Canada, this issue need not be decided.

[709] Other experts testifying on Apotex’s behalf included Dr. Robert McClelland, a chemist; Mr. Stephen Cole, a chartered accountant and business valuator; and, Dr. Marvin Gans, a physician specialised in paediatrics. Dr. McClelland, who had testified in the main action, filed a report explaining the distinction between the Lilly and Shionogi patents and processes and as to whether or not, as of 2003, there existed other publicly known commercially viable processes that could be used to make bulk cefaclor. His testimony sought to establish one of the main, if not the most important, premises for the economists’ opinions, particularly those of Dr. Church,[287] which is that only two processes were known to exist for making cefaclor.

[710] At first the Court was somewhat puzzled by Apotex’s position in the counterclaim given that in the main action it had adamantly defended its position that it used a non-infringing process. Dr. McClelland also indicated in cross-examination that he had reached the same conclusion when asked by Apotex to carry out the same research in the late 1990’s (1997 or 1998) and that, although not mandated by Apotex to do so, in 1985 anybody carrying out the same research would have probably come to the same conclusion.

[711] Mr. Cole filed a report on how the damages of Apotex should be calculated and gave some indication as to the licensing rate that should have applied had Shionogi licensed Apotex for the use of its patented processes. Lilly objected to the qualification of Mr. Cole as an expert on the grounds that his opinion did not offer an estimate of damages, which is all an accountant may do in an expert report. Further, Lilly objected to Mr. Cole providing an opinion as to the setting of royalty rates, as Mr. Cole had no expertise in this regard. Indeed, the portion of Mr. Cole’s evidence dealing with royalty rates would have had very little weight, for the comparables he used were questionable and insufficient, and he has little expertise dealing with such matters. That said, the level of royalties was not an issue on which the Court reached a conclusion.

[712] Finally, Dr. Gans offered evidence as to how physicians select the medicines they prescribe to patients, particularly antibiotic medication. This evidence was put forth by Apotex to contest the defendants by counterclaim’s position that the relevant market for the purpose of a s. 45 inquiry was that of dosage form antibiotics of the same class as cefaclor, as opposed to that of bulk cefaclor. Given the basis of my decision this question has not been considered at all; nor has Dr. Gans’ evidence.

[713] Experts testifying on Lilly and Shionogi’s behalf included one economist, Dr. Iain Cockburn and a physician specialised in microbiology, Dr. Donald Low. Dr. Cockburn, who has more expertise than Apotex’s experts with respect to certain pharmaceutical products and licensing practices in the pharmaceutical industry, set out to provide an opinion on the impact of the 1995 Assignment Agreement between Lilly and Shionogi on competition and on Apotex particularly. Dr. Cockburn commented on the main reports of Apotex’s three experts on economics.

[714] Dr. Low provided an opinion concerning antibiotics, particularly cefaclor and its related or competing products and their use in Canada in the treatment of bacterial infections. Once again this evidence was not relevant to the matters on which this decision stands.

## 22183:21 · paragraphs 715-764

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `15b619134484b517d4acf70360cd3504a19d5c971c06c66e83ed1a8e3179b7f7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:21:subtheme:1 · paragraphs 715-717

- Raw key terms: `evidence, expert, analysis, comment, court, economists, need, relevant`
- Display key terms: `expert, analysis, comment, economists, need, relevant`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: expert, analysis, comment, economists, need, relevant Application context: [716] In weighing this expert evidence, the Court applied the factors set out by the Supreme Court of Canada in R. Evidence spans paragraphs 715-717. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040961` offsets `17-25`; context: [715] The expert evidence was the subject of many objections.
- Evidence: `issue` cue `issues` at chunk `5040962` offsets `534-540`; context: 17) For example, the Court does not need expert evidence on issues such as the proper interpretation of the 1975 agreement based on an expert’s analysis of the circumstantial evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040962` offsets `30-38`; context: [716] In weighing this expert evidence, the Court applied the factors set out by the Supreme Court of Canada in R.
- Evidence: `reasoning_application` cue `applied` at chunk `5040962` offsets `50-57`; context: [716] In weighing this expert evidence, the Court applied the factors set out by the Supreme Court of Canada in R.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040963` offsets `27-35`; context: [717] Much of the “expert” evidence given by the economists was really no more than arguments presented in the form of expert evidence.

#### 22183:21:subtheme:2 · paragraphs 718-719

- Raw key terms: `another, apotex, autre, competition, dans, exceeding, follows, part`
- Display key terms: `another, apotex, autre, competition, dans, exceeding, follows, part`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: another, apotex, autre, competition, dans, exceeding, follows, part Rule/authority context: [718] The right of Apotex to seek a remedy before the Federal Court arises under s. Evidence spans paragraphs 718-719. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040964` offsets `2296-2304`; context: (4) Les actions visées au paragraphe (1) se prescrivent :
a) dans le cas de celles qui sont fondées sur un comportement qui va à l’encontre d’une disposition de la partie VI, dans les deux ans qui suivent la dernière des dates suivantes :
(i) soit la date du comportement en question,
(ii) soit la date où il est statué de façon définitive sur la poursuite;
- Evidence: `governing_rule` cue `under` at chunk `5040964` offsets `75-80`; context: [718] The right of Apotex to seek a remedy before the Federal Court arises under s.

#### 22183:21:subtheme:3 · paragraphs 720-721

- Raw key terms: `apotex, appeal, assignment, competition, counterclaim, court, federal, lessening`
- Display key terms: `apotex, assignment, competition, counterclaim, federal, lessening`
- Argument roles: `disposition, governing_rule, issue`
- Explanation: Observed roles: disposition, governing_rule, issue Display terms: apotex, assignment, competition, counterclaim, federal, lessening Rule/authority context: The issue of whether Apotex suffered damages under s. | In response, Lilly and Shionogi contested this assertion and continued to assert that Lilly had an exclusive licence under the Shionogi patents under the terms of the 1975 research and development agreement between them. Operative outcome context: [720] Apotex’s counterclaim was the subject of summary judgment proceedings before trial, resulting in two decisions by the Federal Court of Appeal, which ultimately dismissed the motions for summary judgment. Evidence spans paragraphs 720-721. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040966` offsets `407-415`; context: The question of whether Apotex’s counterclaim is statute-barred was a matter for trial; and
3.
- Evidence: `governing_rule` cue `under` at chunk `5040966` offsets `543-548`; context: The issue of whether Apotex suffered damages under s.
- Evidence: `disposition` cue `dismissed` at chunk `5040966` offsets `166-175`; context: [720] Apotex’s counterclaim was the subject of summary judgment proceedings before trial, resulting in two decisions by the Federal Court of Appeal, which ultimately dismissed the motions for summary judgment.
- Evidence: `issue` cue `question` at chunk `5040967` offsets `555-563`; context: All of this is perhaps understandable given this passage of the reasons of the Federal Court of Appeal, delivered by Justice John Evans:
The question for trial is whether the lessening of competition resulting from the assignment is sufficiently significant as to be undue: see R.
- Evidence: `governing_rule` cue `under` at chunk `5040967` offsets `310-315`; context: In response, Lilly and Shionogi contested this assertion and continued to assert that Lilly had an exclusive licence under the Shionogi patents under the terms of the 1975 research and development agreement between them.

#### 22183:21:subtheme:4 · paragraphs 722-725

- Raw key terms: `competition, apotex, commissioner, conduct, court, decision, nevertheless, part`
- Display key terms: `competition, apotex, commissioner, conduct, nevertheless, part`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: competition, apotex, commissioner, conduct, nevertheless, part Application context: 45 where: i) six persons apply for such an inquiry, based on the belief that such an offence has or is about to committed;[292] or, ii) the Commissioner has reason to believe the same. Evidence spans paragraphs 722-725. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040968` offsets `274-281`; context: The dispute centered on whether a judgment totally dismissing a motion for summary judgment can nevertheless be dispositive in part of the issues to be determined at trial, especially when such determination is not part of the order.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040968` offsets `46-54`; context: [722] As a consequence, and despite extensive evidence presented by Apotex as to elements establishing lessening of competition in itself, let alone undue lessening, a full day of argument was entertained by the Court on the impact of this decision.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `5040968` offsets `346-358`; context: The dispute centered on whether a judgment totally dismissing a motion for summary judgment can nevertheless be dispositive in part of the issues to be determined at trial, especially when such determination is not part of the order.
- Evidence: `issue` cue `whether` at chunk `5040969` offsets `96-103`; context: [723] Nevertheless, nothing in the Federal Court of Appeal’s decision suggests that determining whether or not Lilly and Shionogi’s conduct would unduly lessen competition is either the logical or natural starting point for assessing the merits of Apotex’s counterclaim.
- Evidence: `reasoning_application` cue `apply` at chunk `5040970` offsets `256-261`; context: 45 where: i) six persons apply for such an inquiry, based on the belief that such an offence has or is about to committed;[292] or, ii) the Commissioner has reason to believe the same.

#### 22183:21:subtheme:5 · paragraphs 726-733

- Raw key terms: `lilly, apotex, competition, shionogi, limitation, period, agreement, conduct`
- Display key terms: `lilly, apotex, competition, shionogi, limitation, period, agreement, conduct`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: lilly, apotex, competition, shionogi, limitation, period, agreement, conduct Rule/authority context: Absent proof of damages, therefore, Apotex cannot make out its civil liability claim under sections 36 and 45 of the Competition Act. | For Apotex, “Lilly’s impugned conduct continues to occur on every day thereafter that Lilly asserted against Apotex patent rights obtained pursuant to the agreement between Shionogi and Lilly and when competition was und Application context: Absent proof of damages, therefore, Apotex cannot make out its civil liability claim under sections 36 and 45 of the Competition Act. | For the reasons that follow, the Court concludes not only that the counterclaim is time-barred but also that Apotex has not established either damage or causation. Evidence spans paragraphs 726-733. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040972` offsets `291-298`; context: If Apotex cannot do so, the Court has no reason, nor jurisdiction, to inquire as to whether or not Lilly and Shionogi have conspired to unduly lessen competition.
- Evidence: `governing_rule` cue `under` at chunk `5040972` offsets `1000-1005`; context: Absent proof of damages, therefore, Apotex cannot make out its civil liability claim under sections 36 and 45 of the Competition Act.
- Evidence: `reasoning_application` cue `therefore` at chunk `5040972` offsets `940-949`; context: Absent proof of damages, therefore, Apotex cannot make out its civil liability claim under sections 36 and 45 of the Competition Act.
- Evidence: `issue` cue `whether` at chunk `5040973` offsets `250-257`; context: Then the Court will proceed to examine if Apotex has established that it has suffered a loss or damage, and whether any such injury flows from the alleged anticompetitive acts of Lilly and Shionogi.
- Evidence: `reasoning_application` cue `concludes` at chunk `5040973` offsets `380-389`; context: For the reasons that follow, the Court concludes not only that the counterclaim is time-barred but also that Apotex has not established either damage or causation.
- Evidence: `counterargument_limitation` cue `but` at chunk `5040973` offsets `436-439`; context: For the reasons that follow, the Court concludes not only that the counterclaim is time-barred but also that Apotex has not established either damage or causation.
- Evidence: `reasoning_application` cue `apply` at chunk `5040976` offsets `85-90`; context: [730] Even if the discoverability principle, which Lilly and Shionogi argue does not apply to subs.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5040976` offsets `324-330`; context: Therefore, the limitation period cannot have expired any later than 1999.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040979` offsets `245-256`; context: For Apotex, “Lilly’s impugned conduct continues to occur on every day thereafter that Lilly asserted against Apotex patent rights obtained pursuant to the agreement between Shionogi and Lilly and when competition was unduly lessened thereby.

#### 22183:21:subtheme:6 · paragraphs 734-736

- Raw key terms: `court, conduct, judgment, long, view, ability, accept, action`
- Display key terms: `conduct, long, view, ability, accept, action`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: conduct, long, view, ability, accept, action Rule/authority context: 36(4) so long as it continues to constitute an offence under Part VI of the Competition Act. Application context: Because of the evidential questions to be resolved, this is not the kind of issue on which it would be appropriate to grant summary judgment. Evidence spans paragraphs 734-736. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040980` offsets `661-666`; context: Because of the evidential questions to be resolved, this is not the kind of issue on which it would be appropriate to grant summary judgment.
- Evidence: `reasoning_application` cue `Because` at chunk `5040980` offsets `585-592`; context: Because of the evidential questions to be resolved, this is not the kind of issue on which it would be appropriate to grant summary judgment.
- Evidence: `governing_rule` cue `under` at chunk `5040982` offsets `385-390`; context: 36(4) so long as it continues to constitute an offence under Part VI of the Competition Act.
- Evidence: `counterargument_limitation` cue `However` at chunk `5040982` offsets `225-232`; context: However, in the Court’s view, ongoing conduct can only be qualified as ongoing for the purposes of subs.

#### 22183:21:subtheme:7 · paragraphs 737-738

- Raw key terms: `competition, lessen, offence, unduly, accused, agreement, agrees, another`
- Display key terms: `competition, lessen, offence, unduly, accused, agreement, agrees, another`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: competition, lessen, offence, unduly, accused, agreement, agrees, another Rule/authority context: (4th) 36 (Nova Scotia Pharmaceutical Society), Justice Charles Gonthier, writing for the Court, held that an offence under the predecessor to s. Evidence spans paragraphs 737-738. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040983` offsets `84-92`; context: [737] Thus, crucial to the determination of the applicable limitation period is the question of what conduct may form the basis of the offence which is complained of by Apotex, in this case the offence of conspiracy to unduly lessen competition provided for in s.
- Evidence: `governing_rule` cue `under` at chunk `5040984` offsets `207-212`; context: (4th) 36 (Nova Scotia Pharmaceutical Society), Justice Charles Gonthier, writing for the Court, held that an offence under the predecessor to s.

#### 22183:21:subtheme:8 · paragraphs 739-740

- Raw key terms: `agreement, behaviour, element, inquiry, actually, ascertain, behavioural, competition`
- Display key terms: `agreement, behaviour, element, inquiry, actually, ascertain, behavioural, competition`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: agreement, behaviour, element, inquiry, actually, ascertain, behavioural, competition Evidence spans paragraphs 739-740. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040985` offsets `54-61`; context: [739] The inquiry that must be conducted to ascertain whether the elements of the offence are met is twofold: (i) market structure, “to ascertain the degree of market power of the parties to the agreement”;[305] and, (ii) behaviour of the firms.
- Evidence: `issue` cue `question` at chunk `5040986` offsets `10-18`; context: [740] The question of behaviour, however, is not examined from the standpoint of what effects an agreement actually has, but rather what, at the time at which it is entered into, is its object and what are the likely effects of that object on competition.

#### 22183:21:subtheme:9 · paragraphs 741-742

- Raw key terms: `added, agreement, anything, arrangement, arrived, carry, case, chief`
- Display key terms: `added, agreement, anything, arrangement, arrived, carry, case, chief`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: added, agreement, anything, arrangement, arrived, carry, case, chief Rule/authority context: 449, in which Chief Justice James McRuer held that: [i]n considering whether the agreement or conspiracy comes within the statute, one does not judge the unlawfulness by what was done pursuant to the agreement (although  Evidence spans paragraphs 741-742. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040987` offsets `202-209`; context: 449, in which Chief Justice James McRuer held that:
[i]n considering whether the agreement or conspiracy comes within the statute, one does not judge the unlawfulness by what was done pursuant to the agreement (although this may be evidence of the agreement) but, as I have said, one examines the nature and scope of the agreement as proved and decides whether that agreement, if carried into effect, would prejudice the public interest in free competition to a degree that in fact would be undue.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040987` offsets `365-373`; context: 449, in which Chief Justice James McRuer held that:
[i]n considering whether the agreement or conspiracy comes within the statute, one does not judge the unlawfulness by what was done pursuant to the agreement (although this may be evidence of the agreement) but, as I have said, one examines the nature and scope of the agreement as proved and decides whether that agreement, if carried into effect, would prejudice the public interest in free competition to a degree that in fact would be undue.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040987` offsets `317-328`; context: 449, in which Chief Justice James McRuer held that:
[i]n considering whether the agreement or conspiracy comes within the statute, one does not judge the unlawfulness by what was done pursuant to the agreement (although this may be evidence of the agreement) but, as I have said, one examines the nature and scope of the agreement as proved and decides whether that agreement, if carried into effect, would prejudice the public interest in free competition to a degree that in fact would be undue.
- Evidence: `counterargument_limitation` cue `although` at chunk `5040987` offsets `344-352`; context: 449, in which Chief Justice James McRuer held that:
[i]n considering whether the agreement or conspiracy comes within the statute, one does not judge the unlawfulness by what was done pursuant to the agreement (although this may be evidence of the agreement) but, as I have said, one examines the nature and scope of the agreement as proved and decides whether that agreement, if carried into effect, would prejudice the public interest in free competition to a degree that in fact would be undue.
- Evidence: `issue` cue `whether` at chunk `5040988` offsets `223-230`; context: 529, where Justice Kerwin held that:
[o]nce an agreement is arrived at, whether anything be done to carry it out or not, the matter must be looked at in each case as a question of fact to be determined by the tribunal of fact upon a common sense view as to the direct object of the arrangement complained of.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040988` offsets `464-472`; context: The evidence in these cases of what was done is merely better evidence of that object than would exist where no act in furtherance of the common design had been committed.

#### 22183:21:subtheme:10 · paragraphs 743-744

- Raw key terms: `agreement, competition, lessen, unduly, actions, actual, aetna, anything`
- Display key terms: `agreement, competition, lessen, unduly, actions, actual, aetna, anything`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: agreement, competition, lessen, unduly, actions, actual, aetna, anything Rule/authority context: The strongest evidence of this is that, even if no subsequent actions had been taken pursuant to an agreement, the act of entering into it would still constitute an offence if the other requirements were met. Evidence spans paragraphs 743-744. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5040989` offsets `304-311`; context: Effects may be examined for the purposes of determining whether or not this agreement was likely to unduly lessen competition, but it does not extend the period during which such conduct occurred.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040989` offsets `459-467`; context: The strongest evidence of this is that, even if no subsequent actions had been taken pursuant to an agreement, the act of entering into it would still constitute an offence if the other requirements were met.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5040989` offsets `530-541`; context: The strongest evidence of this is that, even if no subsequent actions had been taken pursuant to an agreement, the act of entering into it would still constitute an offence if the other requirements were met.

#### 22183:21:subtheme:11 · paragraphs 745-747

- Raw key terms: `competition, conspiracy, justice, offence, purposes, subs, thus, whether`
- Display key terms: `competition, conspiracy, justice, offence, purposes, subs, thus, whether`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: competition, conspiracy, justice, offence, purposes, subs, thus, whether Rule/authority context: Behaviour subsequent to the agreement is of no relevance in determining whether there has been an offence and thus cannot be of any relevance for the purposes of limitations under subs. | [747] Thus, for the purposes of evaluating the limitation period under subs. Application context: [745] The question therefore is not whether the conspiracy indeed had this effect but rather only whether or not this conspiracy would have this effect. | Even assuming (although the judge nowhere says so) that proof of an actual lessening of competition might provide support for a finding that there was a conspiracy to that end and that it was directed to an undue lesseni Evidence spans paragraphs 745-747. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5040991` offsets `10-18`; context: [745] The question therefore is not whether the conspiracy indeed had this effect but rather only whether or not this conspiracy would have this effect.
- Evidence: `governing_rule` cue `under` at chunk `5040991` offsets `327-332`; context: Behaviour subsequent to the agreement is of no relevance in determining whether there has been an offence and thus cannot be of any relevance for the purposes of limitations under subs.
- Evidence: `reasoning_application` cue `therefore` at chunk `5040991` offsets `19-28`; context: [745] The question therefore is not whether the conspiracy indeed had this effect but rather only whether or not this conspiracy would have this effect.
- Evidence: `issue` cue `whether` at chunk `5040992` offsets `173-180`; context: [746] The dissenting reasons of Chief Justice Bora Laskin in Aetna make this point in a perhaps more forceful fashion:
[the trial judge] asserted that in order to determine whether the offence charged against the appellants had been committed he was obliged to determine “whether or not there has been any undue lessening of competition”.
- Evidence: `reasoning_application` cue `conclude` at chunk `5040992` offsets `835-843`; context: Even assuming (although the judge nowhere says so) that proof of an actual lessening of competition might provide support for a finding that there was a conspiracy to that end and that it was directed to an undue lessening, the absence of any proof of actual lessening of competition, let alone of an undue lessening, does not conclude the matter against the Crown.
- Evidence: `counterargument_limitation` cue `although` at chunk `5040992` offsets `523-531`; context: Even assuming (although the judge nowhere says so) that proof of an actual lessening of competition might provide support for a finding that there was a conspiracy to that end and that it was directed to an undue lessening, the absence of any proof of actual lessening of competition, let alone of an undue lessening, does not conclude the matter against the Crown.
- Evidence: `governing_rule` cue `under` at chunk `5040993` offsets `65-70`; context: [747] Thus, for the purposes of evaluating the limitation period under subs.

#### 22183:21:subtheme:12 · paragraphs 748-750

- Raw key terms: `apotex, april, assignment, decision, limitation, period, took, absolutely`
- Display key terms: `apotex, april, assignment, limitation, period, took, absolutely`
- Argument roles: `counterargument_limitation, evidence_fact`
- Explanation: Observed roles: counterargument_limitation, evidence_fact Display terms: apotex, april, assignment, limitation, period, took, absolutely Evidence spans paragraphs 748-750. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `5040994` offsets `362-374`; context: Nevertheless, the point from which the limitation period was to be calculated was deemed to be April 1, 1993, and this again, despite the fact that no anti-competitive effects had yet been felt by the plaintiff.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040995` offsets `29-37`; context: [749] There is absolutely no evidence that suggests that Shionogi took part in any decision with regard to the enforcement of its patents in the present proceedings.

#### 22183:21:subtheme:13 · paragraphs 751-764

- Raw key terms: `apotex, lilly, court, claim, patents, action, athey, causation`
- Display key terms: `apotex, lilly, patents, action, athey, causation`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: apotex, lilly, patents, action, athey, causation Rule/authority context: [754] In its Reply to demand for particulars, dated December 10, 2002, Apotex pleaded that: [t]he injuries sustained by Apotex as a consequence of the Plaintiffs’ anti-competitive activity include (a) any monetary liabil | [310] At trial, Apotex did not pursue its claim for the litigation costs incurred in the proceeding under the PM (NOC) Regulations, nor with respect to the claim under item (d), given that it is an admitted fact that Apo Application context: [758] This, Apotex argues, is necessary because the determination of causality and quantification of loss requires a comparison between occurrences in the actual world and a hypothetical “but for world”. | As such, this passage cannot apply to Apotex’s alleged injuries, for which there is no relevant future event. Evidence spans paragraphs 751-764. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5040997` offsets `89-94`; context: [751] Even if I were wrong, as noted earlier, Apotex has raised only one discoverability issue here.
- Evidence: `evidence_fact` cue `evidence` at chunk `5040997` offsets `278-286`; context: Apotex has filed no evidence as to how it construed the amendments made in January, 2001 and how they had come to the vague conclusion referred to in their submission.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5040999` offsets `256-262`; context: The Court agrees with Lilly that equitable set-off is a defence; it cannot be raised in the context of a counter-claim.
- Evidence: `governing_rule` cue `under` at chunk `5041000` offsets `493-498`; context: [754] In its Reply to demand for particulars, dated December 10, 2002, Apotex pleaded that:
[t]he injuries sustained by Apotex as a consequence of the Plaintiffs’ anti-competitive activity include (a) any monetary liability in respect of the Shionogi Patents, (b) the difference between cost to Apotex of acquiring bulk cefaclor in the absence of Lilly’s anti-competitive actions, and the costs it actually incurred, (c) the litigation costs incurred in this proceeding, and in the proceeding under the Patented Medicines (Notice of Compliance) Regulations in respect of the Shionogi Patents, and (d) the lost profits associated with the delay in entering the Canadian and international market for finished dosage forms of cefaclor.
- Evidence: `governing_rule` cue `under` at chunk `5041001` offsets `300-305`; context: [310] At trial, Apotex did not pursue its claim for the litigation costs incurred in the proceeding under the PM (NOC) Regulations, nor with respect to the claim under item (d), given that it is an admitted fact that Apotex faced no such delay.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5041002` offsets `6-17`; context: [756] Pursuant to the bifurcation order of Justice Hughes dated May 8, 2007, Apotex is not required to quantify its loss with respect to potential infringement liability.
- Evidence: `reasoning_application` cue `because` at chunk `5041004` offsets `40-47`; context: [758] This, Apotex argues, is necessary because the determination of causality and quantification of loss requires a comparison between occurrences in the actual world and a hypothetical “but for world”.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041004` offsets `188-191`; context: [758] This, Apotex argues, is necessary because the determination of causality and quantification of loss requires a comparison between occurrences in the actual world and a hypothetical “but for world”.
- Evidence: `reasoning_application` cue `apply` at chunk `5041007` offsets `573-578`; context: As such, this passage cannot apply to Apotex’s alleged injuries, for which there is no relevant future event.
- Evidence: `reasoning_application` cue `apply` at chunk `5041008` offsets `68-73`; context: [762] Instead of standing for the proposition that the Court should apply a relaxed evidentiary standard, Athey stands for the proposition that the well-settled “but for” test is applicable to evaluating causation.
- Evidence: `reasoning_application` cue `apply` at chunk `5041009` offsets `86-91`; context: [763] There is an alternative, but it is not what Apotex argues that the Court should apply here.

#### Section text

[715] The expert evidence was the subject of many objections. The Court will only comment on those that were relevant to the findings on which this decision turns.

[716] In weighing this expert evidence, the Court applied the factors set out by the Supreme Court of Canada in R. v. Mohan, [1994] 2 S.C.R. 9, (1994), 114 D.L.R. (4th) 419 (Mohan). As explained by Justice John Sopinka, speaking for the Court, “[a]dmission of expert evidence depends on the application of the following criteria: (a) relevance; (b) necessity in assisting the trier of fact; (c) the absence of any exclusionary rule; (d) a properly qualified expert.” (para. 17) For example, the Court does not need expert evidence on issues such as the proper interpretation of the 1975 agreement based on an expert’s analysis of the circumstantial evidence. Nor were any of those expert economists qualified to opine on such matters.

[717] Much of the “expert” evidence given by the economists was really no more than arguments presented in the form of expert evidence. The three economists testifying on behalf of Apotex seemed particularly anxious to ensure that this be the first case substantively putting into play the Intellectual Property Enforcement Guidelines recently developed by the Competition Bureau. For reasons that follow there will be no need in this case to comment on the appropriate test to be used in the course of a s. 45 analysis nor on said guidelines.
12.1. Relevant Statutory Provisions

[718] The right of Apotex to seek a remedy before the Federal Court arises under s. 36 of the Competition Act, which reads as follows:
36. (1) Any person who has suffered loss or damage as a result of
(a) conduct that is contrary to any provision of Part VI, or
(b) the failure of any person to comply with an order of the Tribunal or another court under this Act, may, in any court of competent jurisdiction, sue for and recover from the person who engaged in the conduct or failed to comply with the order an amount equal to the loss or damage proved to have been suffered by him, together with any additional amount that the court may allow not exceeding the full cost to him of any investigation in connection with the matter and of proceedings under this section.
[…]
(3) For the purposes of any action under subsection (1), the Federal Court is a court of competent jurisdiction.
(4) No action may be brought under subsection (1),
(a) in the case of an action based on conduct that is contrary to any provision of Part VI, after two years from
(i) a day on which the conduct was engaged in, or
(ii) the day on which any criminal proceedings relating thereto were finally disposed of, whichever is the later;
36. (1) Toute personne qui a subi une perte ou des dommages par suite :
a) soit d’un comportement allant à l’encontre d’une disposition de la partie VI;
b) soit du défaut d’une personne d’obtempérer à une ordonnance rendue par le Tribunal ou un autre tribunal en vertu de la présente loi, peut, devant tout tribunal compétent, réclamer et recouvrer de la personne qui a eu un tel comportement ou n’a pas obtempéré à l’ordonnance une somme égale au montant de la perte ou des dommages qu’elle est reconnue avoir subis, ainsi que toute somme supplémentaire que le tribunal peut fixer et qui n’excède pas le coût total, pour elle, de toute enquête relativement à l’affaire et des procédures engagées en vertu du présent article.
[…]
(3) La Cour fédérale a compétence sur les actions prévues au paragraphe (1).
(4) Les actions visées au paragraphe (1) se prescrivent :
a) dans le cas de celles qui sont fondées sur un comportement qui va à l’encontre d’une disposition de la partie VI, dans les deux ans qui suivent la dernière des dates suivantes :
(i) soit la date du comportement en question,
(ii) soit la date où il est statué de façon définitive sur la poursuite;

[719] The only other relevant provision of the Competition Act (particularly part VI) is s. 45 which reads as follows:
45. (1) Every one who conspires, combines, agrees or arranges with another person
(a) to limit unduly the facilities for transporting, producing, manufacturing, supplying, storing or dealing in any product,
(b) to prevent, limit or lessen, unduly, the manufacture or production of a product or to enhance unreasonably the price thereof,
(c) to prevent or lessen, unduly, competition in the production, manufacture, purchase, barter, sale, storage, rental, transportation or supply of a product, or in the price of insurance on persons or property, or
(d) to otherwise restrain or injure competition unduly, is guilty of an indictable offence and liable to imprisonment for a term not exceeding five years or to a fine not exceeding ten million dollars or to both.
45. (1) Commet un acte criminel et encourt un emprisonnement maximal de cinq ans et une amende maximale de dix millions de dollars, ou l’une de ces peines, quiconque complote, se coalise ou conclut un accord ou arrangement avec une autre personne :
a) soit pour limiter, indûment, les facilités de transport, de production, de fabrication, de fourniture, d’emmagasinage ou de négoce d’un produit quelconque;
b) soit pour empêcher, limiter ou réduire, indûment, la fabrication ou production d’un produit ou pour en élever déraisonnablement le prix;
c) soit pour empêcher ou réduire, indûment, la concurrence dans la production, la fabrication, l’achat, le troc, la vente, l’entreposage, la location, le transport ou la fourniture d’un produit, ou dans le prix d’assurances sur les personnes ou les biens;
d) soit, de toute autre façon, pour restreindre, indûment, la concurrence ou lui causer un préjudice indu.
12.2. The Framework of Inquiry into Apotex’s Counterclaim

[720] Apotex’s counterclaim was the subject of summary judgment proceedings before trial, resulting in two decisions by the Federal Court of Appeal, which ultimately dismissed the motions for summary judgment.[288] The main conclusions discussed by the Federal Court of Appeal in its reasons can be summarized as follows:
1. An assignment of patent rights can implicate s. 45 of the Competition Act;
2. The question of whether Apotex’s counterclaim is statute-barred was a matter for trial; and
3. The issue of whether Apotex suffered damages under s. 36 of the Competition Act was a matter to be determined at trial;
4. The assignment of the Shionogi patents to Lilly lessened competition, though whether such lessening was “undue” was a matter for trial;[289]

[721] In arguing its counterclaim at trial, Apotex focused first and foremost on proving that the assignment of Shionogi’s process patents to Lilly constituted a violation of s. 45 of the Act. In response, Lilly and Shionogi contested this assertion and continued to assert that Lilly had an exclusive licence under the Shionogi patents under the terms of the 1975 research and development agreement between them. All of this is perhaps understandable given this passage of the reasons of the Federal Court of Appeal, delivered by Justice John Evans:
The question for trial is whether the lessening of competition resulting from the assignment is sufficiently significant as to be undue: see R. v. Nova Scotia Pharmaceutical Society, supra at 646 and following.[[290]]

[722] As a consequence, and despite extensive evidence presented by Apotex as to elements establishing lessening of competition in itself, let alone undue lessening, a full day of argument was entertained by the Court on the impact of this decision. The dispute centered on whether a judgment totally dismissing a motion for summary judgment can nevertheless be dispositive in part of the issues to be determined at trial, especially when such determination is not part of the order.

[723] Nevertheless, nothing in the Federal Court of Appeal’s decision suggests that determining whether or not Lilly and Shionogi’s conduct would unduly lessen competition is either the logical or natural starting point for assessing the merits of Apotex’s counterclaim. In the Court’s view, assessing the s. 45 element of Apotex’s counterclaim first is neither desirable, logical, nor in keeping with the framework of the Competition Act.

[724] The administration and enforcement of the Competition Act is the responsibility of the Commissioner of Competition (the Commissioner).[291] The Commissioner causes an inquiry to be made in relation to an alleged breach of s. 45 where: i) six persons apply for such an inquiry, based on the belief that such an offence has or is about to committed;[292] or, ii) the Commissioner has reason to believe the same.[293]

[725] The right of action for recovery of damages provided for in s. 36 of the Competition Act is a special remedy, contained in a part so labelled. Inquiries into the actions of third parties in the context of applying the substantive provisions of the Act, which is usually the purview of the Commissioner, are thus to take place only in cases where it is clear that allegedly anti-competitive conduct has caused a person to suffer loss or damage. The purpose of s. 36 of the Act is not to encourage persons to take the place of the Commissioner and provoke inquiries into the conduct of others. Rather, its serves the purpose of providing a means of indemnification to victims of anti-competitive conduct.[294]

[726] Hence, Apotex must first prove, in accordance with s. 36 of the Competition Act, that it has suffered loss or damage as a result of the conduct which it alleges to be in violation of s. 45 of the Act. If Apotex cannot do so, the Court has no reason, nor jurisdiction, to inquire as to whether or not Lilly and Shionogi have conspired to unduly lessen competition. As noted by Prothonotary Roza Aronovitch:
As a matter of law, proof of loss or damages is an essential element of the cause of action to fix civil liability for breaches of the Competition Act: Price v. Panasonic Canada Inc. (2002) 22 C.P.C. (5th) 379 at paras. 27-28; Culhane v. ATP Aero Training Products Inc., (2005), 39 C.P.C. (4th) 20 at paras. 1-2; and Eli Lilly and Co. v. Apotex (2004), 32 C.P.R. (4th) 195 at para. 6. The issues of liability and damages in respect of the conspiracy allegations are intertwined, and may not be severed. Absent proof of damages, therefore, Apotex cannot make out its civil liability claim under sections 36 and 45 of the Competition Act.[[295]]
[Emphasis added]

[727] Thus, before assessing the merits of Apotex’s counterclaim, the Court must first be satisfied that the counterclaim is not time-barred. Then the Court will proceed to examine if Apotex has established that it has suffered a loss or damage, and whether any such injury flows from the alleged anticompetitive acts of Lilly and Shionogi. For the reasons that follow, the Court concludes not only that the counterclaim is time-barred but also that Apotex has not established either damage or causation. As such, an analysis as to whether the 1995 assignment is contrary to s. 45 of the Competition Act is not required.
12.3. Is Apotex’s Counterclaim Time-Barred?

[728] As no criminal proceedings have been brought in relation to Lilly and Shionogi’s alleged anti-competitive behaviour, subpara. 36(4)(a)(i) of the Competition Act is operative. As such, the Court must determine what constitutes the last day on which conduct alleged to be contrary to s. 45 of the Competition Act was engaged in (Transamerica Life Insurance Co. of Canada v. Canada Life Assurance Co. (1995), 25 O.R. (3d) 106, 41 C.P.C. (3d) 75 (On. Ct. (Gen. Div.)), para. 23).

[729] Lilly and Shionogi both rely on the decision of Justice Judith Snider in Laboratoires Servier where she held that “when we come to the limitation set out in s. 36(4), the provision refers to the day on which the agreement or conspiracy was entered into.” (para. 482). Thus, given that Lilly and Shionogi entered into an agreement for the assignment of patent rights on April 27, 1995, the applicable limitation period expired in 1997.[296]

[730] Even if the discoverability principle, which Lilly and Shionogi argue does not apply to subs. 36(4) of the Competition Act, were applied in the present case, Apotex was aware of the assignment no later than 1997, at which point the agreement was pleaded in Lilly’s statement of claim. Therefore, the limitation period cannot have expired any later than 1999.[297]

[731] Apotex counters that the Court must consider the elements of the offence proscribed by subs. 45(1) of the Competition Act when interpreting its subs. 36(4), an exercise which Justice Snider failed to embark upon in Laboratoires Servier and which leads to the conclusion “that the two year limitation period will run, at the earliest, from conduct flowing from the agreement which constitutes an undue lessening of competition.”[298]

[732] In Apotex’s view, the limitation period should run only from the moment when “Apotex was provided notice that every alternate process that Apotex had employed was asserted by Lilly to be infringing.”[299] This, in its view, occurred only in January, 2001, when Lilly amended its statement of claim to add allegations of infringement of the Lilly patents with regards to bulk cefaclor obtained from Lupin.[300]

[733] Alternatively, Apotex submits that subs. 36(4) of the Competition Act contemplates ongoing conduct. For Apotex, “Lilly’s impugned conduct continues to occur on every day thereafter that Lilly asserted against Apotex patent rights obtained pursuant to the agreement between Shionogi and Lilly and when competition was unduly lessened thereby.”[301] As Lilly continues to assert rights under the Shionogi patents in the main action, the conduct contrary to s. 45 of the Competition Act is ongoing to this day and thus the limitation period has not expired.

[734] This position was explained by Justice Evans in the context of the Federal Court of Appeal’s second decision concerning a motion for summary judgment in respect of Apotex’s counterclaim:
Apotex’s case is that the assignment must be seen in its context: its enhancement of Lilly’s market power, that is, Lilly’s additional ability to act independently of the market by virtue of its ownership of the patents for all known, commercially viable processes for manufacturing cefaclor. On this view, the conspiracy continued as long as the assignment had competition-lessening effect. Because of the evidential questions to be resolved, this is not the kind of issue on which it would be appropriate to grant summary judgment.[[302]]

[735] The assertion that anti-competitive conduct and its effects continue beyond the filing of a statement of claim in an action for infringement and until such time as the Court renders judgment in such action simply does not merit further comment.

[736] This being said, the Court is prepared to accept that conduct contrary to Part VI of the Competition Act may “be an isolated incident or can be ongoing”,[303] depending on which offence is in play in the circumstances. However, in the Court’s view, ongoing conduct can only be qualified as ongoing for the purposes of subs. 36(4) so long as it continues to constitute an offence under Part VI of the Competition Act.

[737] Thus, crucial to the determination of the applicable limitation period is the question of what conduct may form the basis of the offence which is complained of by Apotex, in this case the offence of conspiracy to unduly lessen competition provided for in s. 45 of the Competition Act.

[738] In R. v. Nova Scotia Pharmaceutical Society, [1992] 2 S.C.R. 606, (1992), 93 D.L.R. (4th) 36 (Nova Scotia Pharmaceutical Society), Justice Charles Gonthier, writing for the Court, held that an offence under the predecessor to s. 45 of the Competition Act (para. 32(1)(c) of the Combines Investigation Act, R.S.C. 1970, c. C-23) comprised two material elements:
(1) an agreement entered into by the accused (“Every one who conspires, combines, agrees or arranges with another person”); and
(2) an undue prevention or lessening of competition flowing from this agreement (“to prevent, or lessen, unduly, competition in the production, manufacture, purchase, barter, sale, storage, rental, transportation or supply of a product, or in the price of insurance upon persons or property…”).[[304]]

[739] The inquiry that must be conducted to ascertain whether the elements of the offence are met is twofold: (i) market structure, “to ascertain the degree of market power of the parties to the agreement”;[305] and, (ii) behaviour of the firms. Given that for the purposes of determining the starting point of the limitation period the Court is concerned with conduct, it is the latter element which is of interest here.

[740] The question of behaviour, however, is not examined from the standpoint of what effects an agreement actually has, but rather what, at the time at which it is entered into, is its object and what are the likely effects of that object on competition. As Justice Gonthier explains, “[t]he object of the agreement is without doubt the most important behavioural element of the inquiry”.[306]

[741] Justice Gonthier approvingly cites an earlier decision of the Ontario High Court, R. v. Northern Electric Co., [1955] 3 D.L.R. 449, in which Chief Justice James McRuer held that:
[i]n considering whether the agreement or conspiracy comes within the statute, one does not judge the unlawfulness by what was done pursuant to the agreement (although this may be evidence of the agreement) but, as I have said, one examines the nature and scope of the agreement as proved and decides whether that agreement, if carried into effect, would prejudice the public interest in free competition to a degree that in fact would be undue. To paraphrase what was said by Duff C.J.C. in the Container Materials case, [1942], 1 D.L.R. 529, S.C.R. 147, 77 Can.C.C. 129, and to adapt the language of Kerwin J., one examines the agreement arrived at, no matter whether anything was done under it or not, and determines as a question of fact upon a common sense view the direct object of the arrangement complained of and determines whether that object, if put into effect, would result in an undue prevention or lessening of competition. Persons or corporations might well enter into an unlawful agreement which by reason of enforced circumstances they could not carry out; it would nevertheless be an indictable offence.
[Emphasis added, p. 469-470]

[742] Chief Justice McRuer relies on the decision of the Supreme Court of Canada in R. v. Container Materials Ltd., [1942] S.C.R. 147, [1942] 1 D.L.R. 529, where Justice Kerwin held that:
[o]nce an agreement is arrived at, whether anything be done to carry it out or not, the matter must be looked at in each case as a question of fact to be determined by the tribunal of fact upon a common sense view as to the direct object of the arrangement complained of. The evidence in these cases of what was done is merely better evidence of that object than would exist where no act in furtherance of the common design had been committed.
[Emphasis added, p. 159.]

[743] These cases stand for the proposition that the conduct does not include anything subsequent to the actual conclusion of the agreement, which in this case is nothing other than the assignment concluded by Lilly and Shionogi on April 27, 1995. Effects may be examined for the purposes of determining whether or not this agreement was likely to unduly lessen competition, but it does not extend the period during which such conduct occurred. The strongest evidence of this is that, even if no subsequent actions had been taken pursuant to an agreement, the act of entering into it would still constitute an offence if the other requirements were met.

[744] The Supreme Court of Canada’s decision in R v. Aetna Insurance Co., [1978] 1 S.C.R. 731, (1977), 75 D.L.R. (3d) 332 (Aetna) does not contradict this. Writing for the majority, Justice Roland Ritchie held that the burden that fell upon the crown was to

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 22183:22 · paragraphs 765-772

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ff108c06bff76687d292c4df6388b6de4a2b6a11200b7e6babc79a080a898694`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:22:subtheme:1 · paragraphs 765-768

- Raw key terms: `apotex, para, application, impossibility, abca, applied, applying, approach`
- Display key terms: `apotex, para, impossibility, abca, applied, applying, approach`
- Argument roles: `counterargument_limitation, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, reasoning_application Display terms: apotex, para, impossibility, abca, applied, applying, approach Application context: [765] As Chief Justice McLachlin concludes, its application is exceptional, and is limited to cases where “it would offend basic notions of fairness and justice to deny liability by applying a “but for” approach. | Again, Apotex has not argued that this should be applied here. Evidence spans paragraphs 765-768. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `concludes` at chunk `5041011` offsets `33-42`; context: [765] As Chief Justice McLachlin concludes, its application is exceptional, and is limited to cases where “it would offend basic notions of fairness and justice to deny liability by applying a “but for” approach.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041011` offsets `194-197`; context: [765] As Chief Justice McLachlin concludes, its application is exceptional, and is limited to cases where “it would offend basic notions of fairness and justice to deny liability by applying a “but for” approach.
- Evidence: `reasoning_application` cue `applied` at chunk `5041012` offsets `362-369`; context: Again, Apotex has not argued that this should be applied here.

#### 22183:22:subtheme:2 · paragraphs 769-772

- Raw key terms: `apotex, causation, court, assignment, damages, lilly, order, patents`
- Display key terms: `apotex, causation, assignment, damages, lilly, order, patents`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: apotex, causation, assignment, damages, lilly, order, patents Application context: [770] Therefore, the Court will apply the normal test for causation, keeping in mind the comments on the breadth of the burden to be satisfied as articulated by Justice Major in Athey:[316] Causation need not be determin | In March, 1986, Apotex applied for a compulsory licence with respect to three Lilly Canadian patents, ‘537; ‘532; and ‘725. Evidence spans paragraphs 769-772. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5041015` offsets `204-212`; context: They grapple with the question of assessing the level of compensation required to restore the plaintiff to the position it would have been in the “but for world”.
- Evidence: `issue` cue `question` at chunk `5041016` offsets `409-417`; context: 328, it is “essentially a practical question of fact which can best be answered ordinary common sense”.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5041016` offsets `6-15`; context: [770] Therefore, the Court will apply the normal test for causation, keeping in mind the comments on the breadth of the burden to be satisfied as articulated by Justice Major in Athey:[316]
Causation need not be determined by scientific precision; as Lord Salmon stated in Alphacell Ltd.
- Evidence: `reasoning_application` cue `applied` at chunk `5041018` offsets `118-125`; context: In March, 1986, Apotex applied for a compulsory licence with respect to three Lilly Canadian patents, ‘537; ‘532; and ‘725.

#### Section text

[765] As Chief Justice McLachlin concludes, its application is exceptional, and is limited to cases where “it would offend basic notions of fairness and justice to deny liability by applying a “but for” approach.” (para. 25)

[766] Such special circumstances are not present here. The impossibility of proving the required elements for the application of s. 36 of the Competition Act has not been established by Apotex, who bears the burden of doing so (Barker v. Montfort Hospital, 2007 ONCA 282, (2007), 278 D.L.R. (4th) 215, para. 53). Again, Apotex has not argued that this should be applied here.

[767] Further, as will be discussed below, the fundamental evidentiary problem (see Bowes v. Edmonton (City), 2007 ABCA 347, (2007), 42 M.P.L.R. (4th) 192, para. 235) in this case concerns Apotex’s conduct in the “but for world”, which, even if it constitutes an impossibility, is clearly not one outside Apotex’s control.

[768] Relying on Schwarzkopf v. McLaughlin, 2008 BCSC 730, (2008), 168 A.C.W.S. (3d) 787, Ticketnet Corp. v. Air Canada (1997), 154 D.L.R. (4th) 271, 105 O.A.C. 87 and Les Laboratoires Servier v. Apotex Inc., [2008] EWHC 2347 (Ch), Apotex argues “that if the nature of the harm results in it being hard to prove, that should not redound to the detriment of the harmed party. The court has to do the best it can, with what it has, to come to the findings.”[315]

[769] By relying on these cases, Apotex is putting the cart before the horse. These cases all deal exclusively with assessment of damages, causation having already been established. They grapple with the question of assessing the level of compensation required to restore the plaintiff to the position it would have been in the “but for world”. The Court here is concerned with a different question, which is the impact of the assignment on Apotex’s position, in order to determine whether such restorative action is even warranted. These authorities do not assist the Court in the present circumstances.

[770] Therefore, the Court will apply the normal test for causation, keeping in mind the comments on the breadth of the burden to be satisfied as articulated by Justice Major in Athey:[316]
Causation need not be determined by scientific precision; as Lord Salmon stated in Alphacell Ltd. v. Woodward, [1972] 2 All E.R. 475, at p. 490, and as was quoted by Sopinka J. at p. 328, it is “essentially a practical question of fact which can best be answered ordinary common sense”.
12.6. Background

[771] As noted above, Apotex’s arguments in respect of causation focus on a comparison between the actual conduct of the parties, and a “but for world” as encompassed in a number of hypothetical scenarios, in all of which Shionogi has not assigned its patents rights to Lilly. In order to assess these various “but for world” scenarios, the Court will first look at the actions of the parties in the actual world which are relevant to these scenarios (as opposed to damages or the s. 45 offence proper).

[772] As early as 1986, Apotex appears to have had an interest in producing the drug cefaclor. In March, 1986, Apotex applied for a compulsory licence with respect to three Lilly Canadian patents, ‘537; ‘532; and ‘725.[317] The ‘725 patent is one of the four Lilly patents that was still in force at the date of the assignment.[318] As such, it forms part of what Apotex alleges as Lilly’s post-assignment monopoly over production processes for bulk cefaclor.

## 22183:23 · paragraphs 773-829

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `033964998f88d2455b0cf30012d3fc24901714ac279af7a8b6a99aa50ac37cb7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:23:subtheme:1 · paragraphs 773-783

- Raw key terms: `lilly, apotex, cefaclor, patents, licence, compulsory, form, shionogi`
- Display key terms: `lilly, apotex, cefaclor, patents, licence, compulsory, form, shionogi`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: lilly, apotex, cefaclor, patents, licence, compulsory, form, shionogi Rule/authority context: [776] In May, 1993, Apotex served on Lilly a Notice of Allegation (NOA) pursuant to s. Application context: [325] In essence, the application was dismissed because the listing of the process patents in the Form IV Patent List was not in accordance with s. Operative outcome context: [773] In 1988, Apotex is granted a compulsory licence, the terms of which provide for a royalty of 4% of the net selling price to be paid by Apotex to Lilly. | [778] The PM (NOC) application was dismissed by Justice Sandra Simpson on September 12, 1995 (Eli Lilly and Co. Evidence spans paragraphs 773-783. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `granted` at chunk `5041019` offsets `25-32`; context: [773] In 1988, Apotex is granted a compulsory licence, the terms of which provide for a royalty of 4% of the net selling price to be paid by Apotex to Lilly.
- Evidence: `issue` cue `issue` at chunk `5041020` offsets `455-460`; context: What is intriguing from this fact is that Apotex, in 1986, had the opportunity to request a compulsory licence for all four of the Lilly patents at issue in this case.
- Evidence: `counterargument_limitation` cue `notwithstanding` at chunk `5041021` offsets `155-170`; context: [320] It did so notwithstanding Lilly’s objection.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5041022` offsets `72-83`; context: [776] In May, 1993, Apotex served on Lilly a Notice of Allegation (NOA) pursuant to s.
- Evidence: `reasoning_application` cue `because` at chunk `5041024` offsets `218-225`; context: [325] In essence, the application was dismissed because the listing of the process patents in the Form IV Patent List was not in accordance with s.
- Evidence: `disposition` cue `dismissed` at chunk `5041024` offsets `35-44`; context: [778] The PM (NOC) application was dismissed by Justice Sandra Simpson on September 12, 1995 (Eli Lilly and Co.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041025` offsets `101-109`; context: [779] In the course of the PM (NOC) proceedings, Lilly and Shionogi asserted,[326] relying on expert evidence,[327] that it was not possible for Apotex to manufacture cefaclor without infringing the patents that had been listed in Lilly’s Form IV Patent List and for which Apotex did not hold a compulsory licence.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041027` offsets `158-167`; context: Radomski, counsel for Apotex, indicated in an affidavit that, as of late 1996, it was expected that Apotex would obtain an NOC with respect to cefaclor and advised that it would have to be prepared to face an infringement action brought by Lilly should it enter the market.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041028` offsets `639-647`; context: [331] It should be noted that another agreement entered into by Lilly with a Canadian generic drug manufacturer is in evidence, this time with Novopharm on June 22, 1998 and relating to the supply of bulk cefaclor.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5041028` offsets `259-267`; context: Although the terms and conditions are not clear, this would probably have been an arrangement similar to the one Lilly entered into with Pharmascience on June 30, 1995, which concerned the distribution by Pharmascience of Lilly-manufactured dosage form cefaclor.

#### 22183:23:subtheme:2 · paragraphs 784-796

- Raw key terms: `apotex, bulk, cefaclor, patents, lilly, process, shionogi, kyong`
- Display key terms: `apotex, bulk, cefaclor, patents, lilly, process, shionogi, kyong`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: apotex, bulk, cefaclor, patents, lilly, process, shionogi, kyong Application context: [788] Accordingly, discussions began between Apotex and Lupin with the aim of modifying the process employed by Lupin to avoid infringement of the Lilly patents. | [355] The other four options, while possible, would not therefore, in Apotex’s view, cross the “but for” threshold. Evidence spans paragraphs 784-796. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5041030` offsets `472-479`; context: [334] This letter is seemingly a result of investigations carried out by Apotex starting, at the latest, in December, 1996 into the processes used by its suppliers of bulk cefaclor and whether said processes infringed the Lilly or Shionogi patents.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041033` offsets `120-128`; context: [342] The evidence before the Court indicates that shortly thereafter, in July, 1997, Apotex began inquiring with Lupin as to the processes used to manufacture bulk cefaclor delivered to Apotex.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5041034` offsets `6-17`; context: [788] Accordingly, discussions began between Apotex and Lupin with the aim of modifying the process employed by Lupin to avoid infringement of the Lilly patents.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041037` offsets `45-53`; context: [791] Apotex requested that Kyong Bo provide evidence of the authorization to use the Shionogi patents,[350] which Kyong Bo was not able to provide.
- Evidence: `reasoning_application` cue `therefore` at chunk `5041040` offsets `157-166`; context: [355] The other four options, while possible, would not therefore, in Apotex’s view, cross the “but for” threshold.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041040` offsets `86-89`; context: [794] Apotex argues that scenarios 1 and 2 together would have been most likely in a “but for world”.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041041` offsets `159-167`; context: [795] Before getting into the actual assessment of these proposed scenarios, it is important to note that one must exercise caution when presented with expert evidence based on assumptions provided by counsel and first ensure that these have been fully established independently and that general economic theories are applicable to the factual scenario at bar.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041042` offsets `303-311`; context: For reasons that will be explained, based on the evidence presented by Apotex’s own Chief Executive Officer, this is not a correct assumption in this case.

#### 22183:23:subtheme:3 · paragraphs 797-802

- Raw key terms: `apotex, appears, cefaclor, court, experts, lilly, made, process`
- Display key terms: `apotex, appears, cefaclor, experts, lilly, made, process`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: apotex, appears, cefaclor, experts, lilly, made, process Evidence spans paragraphs 797-802. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5041043` offsets `272-279`; context: Kay was
asked whether this attitude would prevail no matter how much profit could be had and his answer was “[m]ore likely than not”.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041047` offsets `150-158`; context: The evidence does not support that it is more likely than not that Apotex would have been licensed by either Shionogi or Lilly in the “but for world”.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041047` offsets `281-284`; context: The evidence does not support that it is more likely than not that Apotex would have been licensed by either Shionogi or Lilly in the “but for world”.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041048` offsets `19-27`; context: [802] At best, the evidence supports a conclusion that an amalgam of scenarios 4 and 5, which is to say that Apotex, in the “but for world”, would have practised both the Shionogi and Lilly processes and would have been sued by both companies.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041048` offsets `125-128`; context: [802] At best, the evidence supports a conclusion that an amalgam of scenarios 4 and 5, which is to say that Apotex, in the “but for world”, would have practised both the Shionogi and Lilly processes and would have been sued by both companies.

#### 22183:23:subtheme:4 · paragraphs 803-810

- Raw key terms: `lilly, shionogi, cefaclor, market, apotex, bulk, interested, supply`
- Display key terms: `lilly, shionogi, cefaclor, market, apotex, bulk, interested, supply`
- Argument roles: `evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, reasoning_application Display terms: lilly, shionogi, cefaclor, market, apotex, bulk, interested, supply Rule/authority context: [803] Scenarios 1 and 2 are simply two alternatives under a single hypothesis, which is that Apotex would have been licensed in some way in the “but for world”. Application context: Thomas Ross also opines that such competition would occur because, following the expiry of the Canadian patent covering the compound cefaclor, in August, 1994, “Shionogi would have had a strong financial incentive to lic | Sherman, who can be expected to know a lot more about the industry and this particular market than expert economists unfamiliar with the pharmaceutical industry, testified that cefaclor was a less competitive drug than o Evidence spans paragraphs 803-810. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5041049` offsets `52-57`; context: [803] Scenarios 1 and 2 are simply two alternatives under a single hypothesis, which is that Apotex would have been licensed in some way in the “but for world”.
- Evidence: `reasoning_application` cue `because` at chunk `5041050` offsets `68-75`; context: Thomas Ross also opines that such competition would occur because, following the expiry of the Canadian patent covering the compound cefaclor, in August, 1994, “Shionogi would have had a strong financial incentive to licence another firm to use its patents to produce bulk cefaclor for the Canadian market.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041053` offsets `222-230`; context: In addition, no evidence was presented to the effect that anyone was interested in offering Shionogi any such financial incentive.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041054` offsets `398-406`; context: [370] There is no evidence that Novopharm was interested in making this product at any time prior to the conclusion of its licensing and supply agreement with Lilly in 1998.
- Evidence: `reasoning_application` cue `because` at chunk `5041054` offsets `253-260`; context: Sherman, who can be expected to know a lot more about the industry and this particular market than expert economists unfamiliar with the pharmaceutical industry, testified that cefaclor was a less competitive drug than others “because Novopharm would be the only other one with the capability to make it in Canada”.

#### 22183:23:subtheme:5 · paragraphs 811-811

- Raw key terms: `acknowledge, active, agreements, apotex, appears, authorized, aware, canada`
- Display key terms: `acknowledge, active, agreements, apotex, appears, authorized, aware`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: acknowledge, active, agreements, apotex, appears, authorized, aware Evidence spans paragraphs 811-811. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5041057` offsets `282-288`; context: It appears that Apotex’s experts never considered these issues as they did not even seem to have been aware of these facts and certainly did not acknowledge in their reports that there was limited capacity to manufacture or even interest in offering that drug for sale in Canada.

#### 22183:23:subtheme:6 · paragraphs 812-819

- Raw key terms: `shionogi, court, agreement, belief, evidence, lilly, world, anyone`
- Display key terms: `shionogi, agreement, belief, lilly, world, anyone`
- Argument roles: `counterargument_limitation, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, reasoning_application Display terms: shionogi, agreement, belief, lilly, world, anyone Application context: [812] That said, there are two major reasons why the Court cannot conclude that these scenarios are anything other than a mere possibility: (i) Shionogi’s belief that it was bound by an exclusive licence arrangement with | [814] Shionogi says that it would not have licensed anyone in the “but for world” because it is a brand-name drug company which has no history of licensing generic drug manufacturers, be it directly or indirectly. Evidence spans paragraphs 812-819. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `conclude` at chunk `5041058` offsets `66-74`; context: [812] That said, there are two major reasons why the Court cannot conclude that these scenarios are anything other than a mere possibility: (i) Shionogi’s belief that it was bound by an exclusive licence arrangement with Lilly; and, (ii) the fact that Apotex was not seeking to obtain a lawful source of supply.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041059` offsets `23-31`; context: [813] In assessing the evidence in respect of Shionogi’s beliefs, the Court does not need the assistance of an expert for a trier of fact is obviously capable of evaluating the relevant circumstantial evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041060` offsets `319-327`; context: Shionogi has never directly carried out any business outside of Japan, let alone Canada, and there is no evidence that at any time it received a request for licence or that it licensed anyone for the use of its patented process to manufacture bulk cefaclor.
- Evidence: `reasoning_application` cue `because` at chunk `5041060` offsets `82-89`; context: [814] Shionogi says that it would not have licensed anyone in the “but for world” because it is a brand-name drug company which has no history of licensing generic drug manufacturers, be it directly or indirectly.
- Evidence: `reasoning_application` cue `conclude` at chunk `5041061` offsets `65-73`; context: [815] These are indeed reasons that could well lead the Court to conclude that it is unlikely that Shionogi would have licensed anyone in the “but for world” unless it was actively solicited and offered significant financial incentive to do so.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041061` offsets `143-146`; context: [815] These are indeed reasons that could well lead the Court to conclude that it is unlikely that Shionogi would have licensed anyone in the “but for world” unless it was actively solicited and offered significant financial incentive to do so.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041064` offsets `57-65`; context: [818] The Court carefully examined all of the admissible evidence put forth by the parties to establish the facts they rely upon in their arguments.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041065` offsets `512-520`; context: The evidence of Dr.
- Evidence: `reasoning_application` cue `because` at chunk `5041065` offsets `417-424`; context: Apotex, when asked by the Court how this could mean anything other than that Shionogi believed that Lilly had rights in respect of these patents, suggested that Lilly’s advice could have been sought simply because of its longstanding relationship with Shionogi and Lilly’s expertise in this area.

#### 22183:23:subtheme:7 · paragraphs 820-823

- Raw key terms: `belief, respect, court, lilly, shionogi, actual, although, conclude`
- Display key terms: `belief, respect, lilly, shionogi, actual, although, conclude`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: belief, respect, lilly, shionogi, actual, although, conclude Application context: [821] In an abundance of caution, although the Court has ruled that TX-251 to 259 are not in evidence, the Court has considered their impact and whether they would have lead the Court to conclude differently with respect | [822] There is no good reason to conclude that in the “but for world” Shionogi’s belief would have been any different than the belief it held in the actual world. Evidence spans paragraphs 820-823. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041066` offsets `342-347`; context: In its letter to Gowlings LLP, dated June 22, 1993,[377] authorizing the latter to act on its behalf in the PM (NOC) proceedings in respect of the Shionogi patents listed on Lilly’s Form IV patent list, Shionogi mentions that the patents at issue were “licensed to Eli Lilly & Co.
- Evidence: `issue` cue `whether` at chunk `5041067` offsets `145-152`; context: [821] In an abundance of caution, although the Court has ruled that TX-251 to 259 are not in evidence, the Court has considered their impact and whether they would have lead the Court to conclude differently with respect to Shionogi’s belief.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041067` offsets `93-101`; context: [821] In an abundance of caution, although the Court has ruled that TX-251 to 259 are not in evidence, the Court has considered their impact and whether they would have lead the Court to conclude differently with respect to Shionogi’s belief.
- Evidence: `reasoning_application` cue `conclude` at chunk `5041067` offsets `187-195`; context: [821] In an abundance of caution, although the Court has ruled that TX-251 to 259 are not in evidence, the Court has considered their impact and whether they would have lead the Court to conclude differently with respect to Shionogi’s belief.
- Evidence: `reasoning_application` cue `conclude` at chunk `5041068` offsets `33-41`; context: [822] There is no good reason to conclude that in the “but for world” Shionogi’s belief would have been any different than the belief it held in the actual world.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041068` offsets `55-58`; context: [822] There is no good reason to conclude that in the “but for world” Shionogi’s belief would have been any different than the belief it held in the actual world.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041069` offsets `177-185`; context: The evidence in that respect is particularly strong.

#### 22183:23:subtheme:8 · paragraphs 824-827

- Raw key terms: `apotex, licence, shionogi, supply, available, bulk, cefaclor, compulsory`
- Display key terms: `apotex, licence, shionogi, supply, available, bulk, cefaclor, compulsory`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: apotex, licence, shionogi, supply, available, bulk, cefaclor, compulsory Rule/authority context: [380] Obviously, they failed to consider that Apotex held a compulsory licence under the ‘536 patent, the patent on the compound cefaclor, from 1988. Application context: [827] Apotex did not present any evidence that outside of the compulsory licence system, it ever sought a licence in respect of process patents that might apply to a product it wished to commercialise in the Canadian mar Evidence spans paragraphs 824-827. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5041070` offsets `32-39`; context: [824] The Court also considered whether or not Apotex would have accepted a licence if one were available.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041070` offsets `153-161`; context: In effect, Lilly and Shionogi argued that the evidence shows that in any event, Apotex was not interested in obtaining licensed supply.
- Evidence: `governing_rule` cue `under` at chunk `5041072` offsets `339-344`; context: [380] Obviously, they failed to consider that Apotex held a compulsory licence under the ‘536 patent, the patent on the compound cefaclor, from 1988.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041073` offsets `33-41`; context: [827] Apotex did not present any evidence that outside of the compulsory licence system, it ever sought a licence in respect of process patents that might apply to a product it wished to commercialise in the Canadian market.
- Evidence: `reasoning_application` cue `apply` at chunk `5041073` offsets `155-160`; context: [827] Apotex did not present any evidence that outside of the compulsory licence system, it ever sought a licence in respect of process patents that might apply to a product it wished to commercialise in the Canadian market.

#### 22183:23:subtheme:9 · paragraphs 828-829

- Raw key terms: `apotex, kyong, made, shionogi, addressed, agent, already, aside`
- Display key terms: `apotex, kyong, made, shionogi, addressed, agent, already, aside`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: apotex, kyong, made, shionogi, addressed, agent, already, aside Rule/authority context: That in December, 1996 Apotex would only inquire with Kyong Bo as to infringement of the Lilly patents is surprising given that Apotex knew of the Shionogi patents and the fact that Lilly was asserting rights under them  Application context: Sherman testified, Apotex made this choice “not because we were specifically looking for material made by Shionogi’s process. Evidence spans paragraphs 828-829. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5041074` offsets `82-89`; context: [828] It is true that Apotex made inquiries of its various suppliers to determine whether these suppliers were making use of processes patented in Canada.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041074` offsets `185-193`; context: [382] However, there is little evidence as to discussions with Kyong Bo aside from a letter dated December 16, 1996 addressed to Pacific High Tech Canada (a Kyong Bo agent), which discloses Apotex’s concerns about infringing the Lilly patents, and the correspondence of October, 1997, exchanged in the context of defending the infringement suit already instituted by Lilly.
- Evidence: `governing_rule` cue `under` at chunk `5041074` offsets `737-742`; context: That in December, 1996 Apotex would only inquire with Kyong Bo as to infringement of the Lilly patents is surprising given that Apotex knew of the Shionogi patents and the fact that Lilly was asserting rights under them since 1993, when the PM (NOC) proceedings were commenced.
- Evidence: `counterargument_limitation` cue `However` at chunk `5041074` offsets `160-167`; context: [382] However, there is little evidence as to discussions with Kyong Bo aside from a letter dated December 16, 1996 addressed to Pacific High Tech Canada (a Kyong Bo agent), which discloses Apotex’s concerns about infringing the Lilly patents, and the correspondence of October, 1997, exchanged in the context of defending the infringement suit already instituted by Lilly.
- Evidence: `reasoning_application` cue `because` at chunk `5041075` offsets `197-204`; context: Sherman testified, Apotex made this choice “not because we were specifically looking for material made by Shionogi’s process.

#### Section text

[773] In 1988, Apotex is granted a compulsory licence, the terms of which provide for a royalty of 4% of the net selling price to be paid by Apotex to Lilly.[319] In granting the licence, the then Commissioner of Patents specifically references an objection by Lilly to the granting of the licence, as Apotex did not request the inclusion of patents which Lilly deemed essential for the manufacture of the drug cefaclor, particularly, but presumably not limited to, the ‘536 patent, another of the four Lilly patents which comprised Lilly’s alleged monopoly.

[774] This objection is dealt with by the Commissioner of Patents with reference to arguments advanced by Apotex. According to Apotex, the other patents were not essential for the manufacture of cefaclor, which implied that Apotex was content with the patents that it had chosen in its licence application. What is intriguing from this fact is that Apotex, in 1986, had the opportunity to request a compulsory licence for all four of the Lilly patents at issue in this case.

[775] Apotex specifically chose to obtain a licence that did not include all of Lilly’s patents related to the production of bulk cefaclor.[320] It did so notwithstanding Lilly’s objection. Had it done so, the assignment of the Shionogi patents would have had absolutely no effect on Apotex’s ability to lawfully obtain bulk cefaclor for formulation and eventual sale in the form of Apo-cefaclor, at least until it served notice of termination of this licence on December 6, 1996.[321]

[776] In May, 1993, Apotex served on Lilly a Notice of Allegation (NOA) pursuant to s. 5 of the PM (NOC) Regulations in which it alleged that it would not infringe any of the patents listed in the Form IV Patent List submitted by Lilly as Apotex: (i) held a compulsory licence with respect to certain patents listed; and, (ii) it would not infringe the others by making, constructing, using or selling cefaclor capsules or oral suspensions as these patents contain no claim for cefaclor itself nor for its use.[322] It is important to note that in this Form IV Patent List,[323] referred to by Apotex in its NOA, Lilly had listed the Shionogi patents that were assigned to Lilly in 1995.

[777] Following this NOA, Lilly and Shionogi instituted proceedings against Apotex seeking an order prohibiting the Minister of National Health and Welfare from issuing Notices of Compliance (NOC) to Apotex in connection with a variety of cefaclor capsules and oral suspension dosages until the expiration of both the Lilly and Shionogi process patents (the PM (NOC) proceedings).[324]

[778] The PM (NOC) application was dismissed by Justice Sandra Simpson on September 12, 1995 (Eli Lilly and Co. v. Apotex Inc. (1995), 101 F.T.R. 33, 63 C.P.R. (3d) 245).[325] In essence, the application was dismissed because the listing of the process patents in the Form IV Patent List was not in accordance with s. 2 of the Regulations as they do not contain claims for a medicine or a new use for a medicine.

[779] In the course of the PM (NOC) proceedings, Lilly and Shionogi asserted,[326] relying on expert evidence,[327] that it was not possible for Apotex to manufacture cefaclor without infringing the patents that had been listed in Lilly’s Form IV Patent List and for which Apotex did not hold a compulsory licence. At para. 9 of her decision, Justice Simpson notes that this evidence is uncontradicted and that as such it is “reasonable to infer that Apotex plans to infringe the Patents by copying Lilly’s production methodology” and that if this did transpire “it [would] be open to Lilly to seek remedies for infringement at common law.”

[780] On April 27, 1995, just prior to the determination of Lilly and Shionogi’s application for a prohibition order, Lilly and Shionogi concluded the assignment of Shionogi’s process patents to Lilly, along with a concurrent licence-back in favour of Shionogi.[328]

[781] In light of the decision of Justice Simpson and its confirmation by the Federal Court of Appeal, Harry B. Radomski, counsel for Apotex, indicated in an affidavit that, as of late 1996, it was expected that Apotex would obtain an NOC with respect to cefaclor and advised that it would have to be prepared to face an infringement action brought by Lilly should it enter the market.[329]

[782] At some point in time between the institution of these proceedings and its final resolution, somebody at Lilly met with representatives of Apotex[330] to extend the offer of entering into a relationship in respect of cefaclor as well as other products. Although the terms and conditions are not clear, this would probably have been an arrangement similar to the one Lilly entered into with Pharmascience on June 30, 1995, which concerned the distribution by Pharmascience of Lilly-manufactured dosage form cefaclor.[331] It should be noted that another agreement entered into by Lilly with a Canadian generic drug manufacturer is in evidence, this time with Novopharm on June 22, 1998 and relating to the supply of bulk cefaclor.[332]

[783] On December 6, 1996, Dr. Sherman wrote to Lilly to provide the required three-months notice of termination of its compulsory licence.[333]

[784] Kyong Bo had represented to Apotex, by way of letter dated December 16, 1996 addressed to its intermediary, Pacific High Tech Canada, that its process for manufacturing bulk cefaclor did not use the teachings of Canadian patents ‘611, ‘536 and ‘725, all of which belonged to Lilly.[334] This letter is seemingly a result of investigations carried out by Apotex starting, at the latest, in December, 1996 into the processes used by its suppliers of bulk cefaclor and whether said processes infringed the Lilly or Shionogi patents.[335]

[785] On January 17, 1997, Apotex obtained its NOC[336] and promptly began selling dosage-form cefaclor on the Canadian market. Apotex was not delayed in any way by the assignment in its entry into the market. Apotex had received, from a variety of suppliers, experimental quantities of bulk cefaclor as early as March, 1991.[337] In addition, it had already received two shipments of commercial quantities of bulk cefaclor from Kyong Bo.[338]

[786] As predicted, Lilly quickly commenced an infringement action. Its first action was launched on January 23, 1997 but was subsequently discontinued.[339] The present action was commenced on June 18, 1997. In both actions, Lilly alleged infringement of the Shionogi patents.[340] The latter action specifically referred to the Kyong Bo process.[341]

[787] In May, 1997, Apotex began sourcing commercial quantities of bulk cefaclor from another supplier, Lupin.[342] The evidence before the Court indicates that shortly thereafter, in July, 1997, Apotex began inquiring with Lupin as to the processes used to manufacture bulk cefaclor delivered to Apotex.[343] As mentioned earlier, based on Lupin’s responses to these inquiries, Brigitte Fouillade, Apotex’s legal counsel for intellectual property, appears to have come to the conclusion, by September, 1997, that the process employed by Lupin infringed the Lilly patents.[344]

[788] Accordingly, discussions began between Apotex and Lupin with the aim of modifying the process employed by Lupin to avoid infringement of the Lilly patents. Ms. Fouillade suggested that Lupin employ the teachings of a series of expired patents.[345] Lupin agreed that this was indeed feasible, and had in some respects already been done on an experimental scale, but would result in lower yields and thus bulk cefaclor produced in this fashion would be more expensive.[346]

[789] By October 1997, a new process had been worked out by Lupin and Apotex and, accepting that it would be more costly, Apotex asked Glopec, the intermediary between Apotex and Lupin, to provide a price estimate for bulk cefaclor made according to this process.[347] A supply agreement regarding the use of this new process was concluded between Apotex and Lupin in March, 1998.[348]

[790] By October, 1997, at the latest, Apotex appears to have made additional inquiries as to the process employed by Kyong Bo to produce bulk cefaclor delivered to Apotex, particularly in respect of the Shionogi patents. In response, Kyong Bo represented that it employed the Shionogi process, technology which it acquired from Shionogi in 1992 for the production of HCA, an intermediate which is used to produce Ceftibuten, another drug. Kyong Bo also represented that its rights to use the Shionogi process had not been affected by the assignment.[349]

[791] Apotex requested that Kyong Bo provide evidence of the authorization to use the Shionogi patents,[350] which Kyong Bo was not able to provide.[351] Apotex, who had not received supply from Kyong Bo since September, 1997, never again sourced bulk cefaclor from Kyong Bo.[352]

[792] It is an admitted fact that Apotex, aside from its compulsory licence application in the 1980’s, never sought any form of licence for bulk cefaclor from either Shionogi or Lilly, nor has it ever requested its suppliers to do so.[353] Shionogi never licensed any non-Lilly entity for the use of its patents for the production of bulk cefaclor before 1995.[354]
12.7. Apotex’s “But For” Scenarios with Respect to Causation

[793] Against this factual background, Apotex asserts six possible scenarios in a “but for world” where Shionogi did not assign its patents to Lilly:
1. Apotex is licensed, directly or indirectly, by Shionogi;
2. Apotex is licensed, directly or indirectly, by Lilly;
3. Apotex practises the Shionogi patents, without a licence, and is not sued for infringement;
4. Apotex practises the Shionogi patents, without a licence, and is sued for infringement;
5. Apotex practises the Lilly patents, without a licence, and is sued for infringement;
6. Apotex practises the Lilly patents, without a licence, and is not sued for infringement

[794] Apotex argues that scenarios 1 and 2 together would have been most likely in a “but for world”.[355] The other four options, while possible, would not therefore, in Apotex’s view, cross the “but for” threshold. Finally, Apotex argues that scenarios 3 and 4 were more likely than scenarios 5 and 6, the latter being the least likely.[356] At the outset, the Court finds that the need for so many scenarios, which each have various sub-scenarios, is indicative of the degree of speculation required to find that Apotex has been harmed by the assignment.

[795] Before getting into the actual assessment of these proposed scenarios, it is important to note that one must exercise caution when presented with expert evidence based on assumptions provided by counsel and first ensure that these have been fully established independently and that general economic theories are applicable to the factual scenario at bar. One such general theory relied upon by Apotex’s expert is that firms will normally not reject opportunities to make profits.

[796] The assumptions upon which Apotex’s experts rely can be challenged on at least three counts. First, they assume that Apotex would be seeking a licensed source of bulk cefaclor before taking any risk of entering the market with infringing material. For reasons that will be explained, based on the evidence presented by Apotex’s own Chief Executive Officer, this is not a correct assumption in this case.

[797] Second, with respect to the applicability of general economic theory, Mr. Kay made it clear that Apotex’s general corporate policy was to shun what is commonly referred to as “authorized generics” agreements. In the course of his cross-examination Mr. Kay was
asked whether this attitude would prevail no matter how much profit could be had and his answer was “[m]ore likely than not”.[357]

[798] Thirdly, Dr. Church made it clear, and this also appears from the written reports of Apotex’s experts, that a fundamental assumption was that there were only two publicly known legal sources for bulk cefaclor and that all players, including potential buyers (i.e. generic manufacturers) would be aware of that fact.[358] Again such an assumption doesn’t appear to be borne out by the actual facts. Indeed, Dr. Sherman testified that, despite the fact that Apotex was arguably best informed of the situation in the marketplace given its early involvement in attempting to come to market and the obstacles it had faced in this attempt,[359] he didn’t know that he needed a licence and was not looking for licensed supply or even inquiring about which process was being used by its supplier initially.

[799] The Court also notes that Apotex’s expert’s own evaluation of the duopoly price in the “but for world”[360] includes an assumption that the $1,500.00 paid by Apotex was the price of potentially non-infringing bulk cefaclor. It would thus be a third source of legal supply which on its face appears to be contrary to the assumption described by these experts. It certainly contradicts the basic premise which Dr. Church indicated as being necessary to his opinion.

[800] It also appears that the experts were not made aware of the fact that Apotex also argued in the main action that Lilly itself knew of the existence of a third viable process given that it had included it in its own NDS file.[361] It is also important to note that, despite Dr. McClelland’s opinion in the present counterclaim, once Apotex’s own in-house counsel had concluded that the cefaclor they were buying was indeed infringing, Apotex was able to source non-infringing cefaclor within a few months.

[801] Even so, as will be explained, the Court does not agree with Apotex’s evaluation of the likelihood of occurrence of the proposed scenarios. The evidence does not support that it is more likely than not that Apotex would have been licensed by either Shionogi or Lilly in the “but for world”. Nor does the evidence support the assertion that scenario 3, Apotex practising the Shionogi process without being sued, is the next most likely scenario. These scenarios are nothing more than mere possibilities; they do not amount, even taken together, to a real or substantial possibility.

[802] At best, the evidence supports a conclusion that an amalgam of scenarios 4 and 5, which is to say that Apotex, in the “but for world”, would have practised both the Shionogi and Lilly processes and would have been sued by both companies. Furthermore, the Court agrees with Apotex that scenario 6 on its own is so unlikely that it does not merit examination.[362]
12.7.1. Scenarios 1 and 2: Apotex Obtains a Licence from Shionogi or Lilly

[803] Scenarios 1 and 2 are simply two alternatives under a single hypothesis, which is that Apotex would have been licensed in some way in the “but for world”. Dr. Church testified that, “[i]n the absence of the transfer of patent rights, there would have been competition between Lilly and Shionogi, or more accurately its licensee, to supply bulk cefaclor into Canada.”[363]

[804] Dr. Thomas Ross also opines that such competition would occur because, following the expiry of the Canadian patent covering the compound cefaclor, in August, 1994, “Shionogi would have had a strong financial incentive to licence another firm to use its patents to produce bulk cefaclor for the Canadian market.”[364] In response to Shionogi’s entry into this market, Lilly would also proceed with licensing, resulting in profit-maximizing behaviour by each of these players whom “would find it profitable to licence/supply all licensees who request a licence.”[365]

[805] Dr. Cockburn disagreed with the competitive licensing scenario advanced by Apotex’s experts, countering that, even if one assumed that Shionogi would have licensed a third party, which was not admitted,[366] “Shionogi and Lilly would have powerful incentives
to limit the number of competitors in the finished dosage form market. […] [T]hey would have licensed or supplied at most one generic each.”[367] In such a scenario, it is uncertain that Apotex would be one of the two beneficiaries of such a licence.

[806] While contesting this position, Apotex’s experts counter that, should Shionogi and Lilly each have licensed only one generic in the “but for world”, Apotex would have been the most likely recipient of such a licence:
As the leading distributor of generics, Apotex would easily have been the most attractive partner for Shionogi to licence. Consequently, even if Shionogi restricted itself to a single licence, it could easily have been to supply Apotex.[[368]]

[807] It should be noted that neither Dr. Ross nor Dr. Church have any expertise with regard to Japanese firms in general and had very limited information as to Shionogi’s business practices in particular. In addition, no evidence was presented to the effect that anyone was interested in offering Shionogi any such financial incentive. Presumably Shionogi would not offer licences unless there was a demand for them.

[808] In that respect Dr. Sherman, who can be expected to know a lot more about the industry and this particular market than expert economists unfamiliar with the pharmaceutical industry, testified that cefaclor was a less competitive drug than others “because Novopharm would be the only other one with the capability to make it in Canada”.[369] Also, it was not a major product.[370] There is no evidence that Novopharm was interested in making this product at any time prior to the conclusion of its licensing and supply agreement with Lilly in 1998.

[809] Further, as explained by Dr. Sherman, companies such as Pharmascience would not be in the market for bulk cefaclor for want of manufacturing capacity. If Pharmascience had been interested in any way to this drug, they would have needed a supplier of dosage form cefaclor.[371]

[810] Dr. Sherman certainly indicates that, had Apotex not entered the market, it may well have been that, regardless of the patent situation,[372] no other generic would have been interested in manufacturing dosage form cefaclor. In the circumstances, one cannot simply assume that what Lilly did to counteract the “illegal” entry of Apotex in the market for dosage form cefaclor is a simple reflection of what it would have done had there been competition from Shionogi in the bulk cefaclor market.

[811] In effect, Lilly’s active marketing and their willingness to enter into authorized generic agreements for several drugs (cefaclor being only one of them) may well explain delayed entry of other generics into the market. It appears that Apotex’s experts never considered these issues as they did not even seem to have been aware of these facts and certainly did not acknowledge in their reports that there was limited capacity to manufacture or even interest in offering that drug for sale in Canada.

[812] That said, there are two major reasons why the Court cannot conclude that these scenarios are anything other than a mere possibility: (i) Shionogi’s belief that it was bound by an exclusive licence arrangement with Lilly; and, (ii) the fact that Apotex was not seeking to obtain a lawful source of supply.

[813] In assessing the evidence in respect of Shionogi’s beliefs, the Court does not need the assistance of an expert for a trier of fact is obviously capable of evaluating the relevant circumstantial evidence.[373] (Mohan) It must also be noted that Dr. Church, for example, offers such an evaluation which is based on selective information and as such is incomplete in any event.

[814] Shionogi says that it would not have licensed anyone in the “but for world” because it is a brand-name drug company which has no history of licensing generic drug manufacturers, be it directly or indirectly. Shionogi has never directly carried out any business outside of Japan, let alone Canada, and there is no evidence that at any time it received a request for licence or that it licensed anyone for the use of its patented process to manufacture bulk cefaclor. Moreover, Shionogi points to its 100 year old relationship w

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 22183:24 · paragraphs 830-876

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f313a71039a9cb34cbde27bc78974154033b74b63799c5cbd6af324d9f4a544d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:24:subtheme:1 · paragraphs 830-838

- Raw key terms: `shionogi, apotex, court, process, sherman, bulk, cefaclor, evidence`
- Display key terms: `shionogi, apotex, process, sherman, bulk, cefaclor`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: shionogi, apotex, process, sherman, bulk, cefaclor Position/evidence statements: [838] Had the Court concluded differently in this respect, this scenario would still not be deemed more likely than not as the Court is not convinced that the evidence supports Apotex’s claim that the exclusive use of th Rule/authority context: [387] [Emphasis added] Again this defies the fact that, independently of the assignment, Lilly was asserting rights under these patents, which is a fact which Dr. | Sherman explained that if Shionogi would have tried to charge Apotex more than a few percent, Apotex would have resisted, sending the parties to litigation:[388] if they wanted to enforce the patent to try and get a high Application context: [830] Nor was it made on the belief that Kyong Bo had a licence: THE COURT: Did you choose that supplier because it had a licence? | Sherman testified that: to the extent that there were other patentees with other processes, there would generally not be a need to deal with them, because one would expect they would not be enforced in Canada or would be Evidence spans paragraphs 830-838. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `5041076` offsets `105-112`; context: [830] Nor was it made on the belief that Kyong Bo had a licence:
THE COURT: Did you choose that supplier because it had a licence?
- Evidence: `evidence_fact` cue `testimony` at chunk `5041077` offsets `218-227`; context: Sherman’s own previous testimony indicates that such representations were made much later, that is in October, 1997.
- Evidence: `governing_rule` cue `under` at chunk `5041078` offsets `758-763`; context: [387]
[Emphasis added]
Again this defies the fact that, independently of the assignment, Lilly was asserting rights under these patents, which is a fact which Dr.
- Evidence: `reasoning_application` cue `because` at chunk `5041078` offsets `544-551`; context: Sherman testified that:
to the extent that there were other patentees with other processes, there would generally not be a need to deal with them, because one would expect they would not be enforced in Canada or would be available for licensing.
- Evidence: `governing_rule` cue `under` at chunk `5041079` offsets `505-510`; context: Sherman explained that if Shionogi would have tried to charge Apotex more than a few percent, Apotex would have resisted, sending the parties to litigation:[388]
if they wanted to enforce the patent to try and get a higher royalty, they would have been faced with the prospect of litigation with us and perhaps having their patents invalidated at litigation, and it wouldn’t have been worth very much to them under those circumstances.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041080` offsets `11-19`; context: [834] This evidence suggests that for Apotex, obtaining a licence for bulk cefaclor was an option of last resort.
- Evidence: `reasoning_application` cue `conclude` at chunk `5041080` offsets `299-307`; context: ”[390] This evidence is simply not sufficient for the Court to conclude that “but for” the assignment of the Shionogi patents, Apotex would have sought licensed supply.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041080` offsets `314-317`; context: ”[390] This evidence is simply not sufficient for the Court to conclude that “but for” the assignment of the Shionogi patents, Apotex would have sought licensed supply.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041081` offsets `363-371`; context: In addition, there is little evidence before the Court as to what led Apotex to begin sourcing bulk cefaclor from Lupin in May, 1997 other than because they had likely been approached by Lupin.
- Evidence: `reasoning_application` cue `because` at chunk `5041081` offsets `478-485`; context: In addition, there is little evidence before the Court as to what led Apotex to begin sourcing bulk cefaclor from Lupin in May, 1997 other than because they had likely been approached by Lupin.
- Evidence: `reasoning_application` cue `conclude` at chunk `5041082` offsets `175-183`; context: The Court cannot conclude that Apotex believed Lupin to be using the Shionogi process or again that such facts had become important or relevant in Apotex’s mind.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041083` offsets `179-187`; context: The evidence supports the conclusion that Apotex was interested in supply, not supply manufactured using a particular process.
- Evidence: `party_position` cue `claim` at chunk `5041084` offsets `186-191`; context: [838] Had the Court concluded differently in this respect, this scenario would still not be deemed more likely than not as the Court is not convinced that the evidence supports Apotex’s claim that the exclusive use of the Shionogi process would not attract an action for infringement.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041084` offsets `159-167`; context: [838] Had the Court concluded differently in this respect, this scenario would still not be deemed more likely than not as the Court is not convinced that the evidence supports Apotex’s claim that the exclusive use of the Shionogi process would not attract an action for infringement.

#### 22183:24:subtheme:2 · paragraphs 839-847

- Raw key terms: `apotex, shionogi, world, lilly, court, conclude, evidence, scenario`
- Display key terms: `apotex, shionogi, world, lilly, conclude, scenario`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: apotex, shionogi, world, lilly, conclude, scenario Rule/authority context: Is there a loss resulting from the assignment under the most likely “but for world” scenario? | In his view, “under that logic or that assumption, there would be no damages, I think. Application context: The Court can only conclude that in the “but for world”, Apotex would have also faced an action for infringement, the only difference being that this action would be brought by both Lilly and Shionogi, just as with the P | [840] As explained above, the Court cannot conclude that in the “but for world” it would be likely that Apotex would have sourced bulk cefaclor manufactured using only one process, be it Shionogi’s or Lilly’s. Evidence spans paragraphs 839-847. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041085` offsets `422-427`; context: As mentioned, the evidence is overwhelming that Lilly believed (again, rightly or wrongly) that it had an exclusive licence to the patents at issue and no good reason was offered to assert that Shionogi would be any less of a willing partner in their enforcement.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041085` offsets `43-51`; context: [839] Specifically, there is absolutely no evidence or explanation offered to support the proposition that, in the “but for world”, enforcement of Shionogi’s patent rights would have not proceeded in precisely the same fashion as it did in the course of the PM (NOC) proceedings.
- Evidence: `reasoning_application` cue `conclude` at chunk `5041085` offsets `563-571`; context: The Court can only conclude that in the “but for world”, Apotex would have also faced an action for infringement, the only difference being that this action would be brought by both Lilly and Shionogi, just as with the PM (NOC) proceedings.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041085` offsets `116-119`; context: [839] Specifically, there is absolutely no evidence or explanation offered to support the proposition that, in the “but for world”, enforcement of Shionogi’s patent rights would have not proceeded in precisely the same fashion as it did in the course of the PM (NOC) proceedings.
- Evidence: `reasoning_application` cue `conclude` at chunk `5041086` offsets `43-51`; context: [840] As explained above, the Court cannot conclude that in the “but for world” it would be likely that Apotex would have sourced bulk cefaclor manufactured using only one process, be it Shionogi’s or Lilly’s.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041087` offsets `328-336`; context: As explained above, there is no evidence that would lead the Court to conclude that such an action would not be conducted in the same fashion as the PM (NOC) proceedings with regard to infringement of the Shionogi patents.
- Evidence: `governing_rule` cue `under` at chunk `5041087` offsets `571-576`; context: Is there a loss resulting from the assignment under the most likely “but for world” scenario?
- Evidence: `reasoning_application` cue `conclude` at chunk `5041087` offsets `366-374`; context: As explained above, there is no evidence that would lead the Court to conclude that such an action would not be conducted in the same fashion as the PM (NOC) proceedings with regard to infringement of the Shionogi patents.
- Evidence: `reasoning_application` cue `conclude` at chunk `5041088` offsets `775-783`; context: 00[393], it paid more for its bulk cefaclor in the actual world than in the “but for world”; and,
ii) That its potential liabilities as a result of infringement are greater in the actual world than in the “but for world”;
For the reasons that follow, the Court cannot conclude that Apotex suffered any damage as a result of this assignment.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041089` offsets `41-49`; context: [843] Before looking specifically at the evidence relied upon by Apotex to support the above allegations, it is important to look at what Apotex’s experts had to say in cross-examination about potential losses in a scenario where Apotex did not seek or obtain a licence in the “but for world” from Shionogi (directly or indirectly).
- Evidence: `counterargument_limitation` cue `but` at chunk `5041089` offsets `278-281`; context: [843] Before looking specifically at the evidence relied upon by Apotex to support the above allegations, it is important to look at what Apotex’s experts had to say in cross-examination about potential losses in a scenario where Apotex did not seek or obtain a licence in the “but for world” from Shionogi (directly or indirectly).
- Evidence: `evidence_fact` cue `found that` at chunk `5041092` offsets `61-71`; context: Cole, he was asked to assume that the Court found that there was anti-competitive conduct and that Apotex had infringed and as such was liable to pay damages.
- Evidence: `governing_rule` cue `under` at chunk `5041092` offsets `340-345`; context: In his view, “under that logic or that assumption, there would be no damages, I think.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041092` offsets `259-262`; context: He was then asked to consider the scenario where this Court also held that in the “but for world”, Apotex would not enter into a licensing agreement.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041093` offsets `19-27`; context: [847] Despite this evidence, Apotex nonetheless maintains that it has suffered a loss measured against scenarios 4 and 5, where it is evident that it would not be a licensee of either Shionogi or Lilly.

#### 22183:24:subtheme:3 · paragraphs 848-850

- Raw key terms: `apotex, bulk, cefaclor, court, legal, loss, established, paid`
- Display key terms: `apotex, bulk, cefaclor, legal, loss, established, paid`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: apotex, bulk, cefaclor, legal, loss, established, paid Application context: [850] The Court knows that in any event even if the price of the legal bulk cefaclor in the “but for world” was relevant here, Apotex has failed to provide the Court with sufficient evidence to conclude that it has suffe Evidence spans paragraphs 848-850. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5041094` offsets `35-42`; context: [848] The court will first examine whether or not Apotex has established a loss in respect of the costs paid for the bulk cefaclor, given that, in accordance with Justice Hughes’ judgment referred to earlier, the Court must be in a position to quantify Apotex’s loss in that respect.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041096` offsets `182-190`; context: [850] The Court knows that in any event even if the price of the legal bulk cefaclor in the “but for world” was relevant here, Apotex has failed to provide the Court with sufficient evidence to conclude that it has suffered a loss.
- Evidence: `reasoning_application` cue `conclude` at chunk `5041096` offsets `194-202`; context: [850] The Court knows that in any event even if the price of the legal bulk cefaclor in the “but for world” was relevant here, Apotex has failed to provide the Court with sufficient evidence to conclude that it has suffered a loss.

#### 22183:24:subtheme:4 · paragraphs 851-851

- Raw key terms: `actual, address, apotex, appear, appears, asked, bulk, cefaclor`
- Display key terms: `actual, address, apotex, appear, appears, asked, bulk, cefaclor`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: actual, address, apotex, appear, appears, asked, bulk, cefaclor Evidence spans paragraphs 851-851. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041097` offsets `40-45`; context: [851] Apotex’s experts only address the issue of price differential between the monopoly price[397] and the duopoly price in the “but for world”.

#### 22183:24:subtheme:5 · paragraphs 852-855

- Raw key terms: `apotex, lilly, argues, argument, charged, church, competition, damages`
- Display key terms: `apotex, lilly, argues, argument, charged, church, competition, damages`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, reasoning_application Display terms: apotex, lilly, argues, argument, charged, church, competition, damages Rule/authority context: However, it is crucial to remember that, pursuant to s. Application context: Considering their testimony, one can reasonably infer that it did not do so because, according to the experts, Apotex would not have suffered any loss. Evidence spans paragraphs 852-855. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `testimony` at chunk `5041098` offsets `28-37`; context: [852] While in reply to the testimony of Dr.
- Evidence: `reasoning_application` cue `because` at chunk `5041098` offsets `616-623`; context: Considering their testimony, one can reasonably infer that it did not do so because, according to the experts, Apotex would not have suffered any loss.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5041099` offsets `242-253`; context: However, it is crucial to remember that, pursuant to s.
- Evidence: `counterargument_limitation` cue `However` at chunk `5041099` offsets `201-208`; context: However, it is crucial to remember that, pursuant to s.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041101` offsets `13-21`; context: [855] Little evidence was presented to support Apotex’s argument aside from a single page from a single report of a single expert, Dr.

#### 22183:24:subtheme:6 · paragraphs 856-860

- Raw key terms: `court, apotex, church, framework, damages, evidence, explain, part`
- Display key terms: `apotex, church, framework, damages, explain, part`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: apotex, church, framework, damages, explain, part Application context: Church volunteered what the Court has come to realize are some very serious limitations to his approach: [The Court]: So you are telling me you could have calculated this precisely but you didn’t because you weren’t aske | It therefore cannot have been intended to apply in the only plausible “but for world” scenario here, which does not involve any licensing by Shionogi. Evidence spans paragraphs 856-860. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `5041102` offsets `297-304`; context: Church volunteered what the Court has come to realize are some very serious limitations to his approach:
[The Court]: So you are telling me you could have calculated this precisely but you didn’t because you weren’t asked.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041103` offsets `75-83`; context: [857] First, the Court finds this to be a particularly obscure part of the evidence of this expert and Apotex made no effort whatsoever to explain para.
- Evidence: `reasoning_application` cue `therefore` at chunk `5041104` offsets `155-164`; context: It therefore cannot have been intended to apply in the only plausible “but for world” scenario here, which does not involve any licensing by Shionogi.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041106` offsets `67-75`; context: [860] The Court is not ready to reach any conclusion based on this evidence.

#### 22183:24:subtheme:7 · paragraphs 861-865

- Raw key terms: `world, apotex, lilly, shionogi, actual, because, court, patentee`
- Display key terms: `world, apotex, lilly, shionogi, actual, because, patentee`
- Argument roles: `evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, reasoning_application Display terms: world, apotex, lilly, shionogi, actual, because, patentee Rule/authority context: [861] In the “but for world” Shionogi and Lilly would be co-plaintiffs and they would advance, like they did in the actual world, that Lilly is licensed or at the very least has rights under the patentee, pursuant to sub | [864] Presumably, although this was not argued, for Apotex, it has more strength in the “but for world” because Lilly would have had to establish that it indeed had rights under the patentee. Application context: That is, Apotex should only pay a reasonable royalty because the Shionogi patents were not used or commercialized in Canada. | [864] Presumably, although this was not argued, for Apotex, it has more strength in the “but for world” because Lilly would have had to establish that it indeed had rights under the patentee. Evidence spans paragraphs 861-865. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5041107` offsets `185-190`; context: [861] In the “but for world” Shionogi and Lilly would be co-plaintiffs and they would advance, like they did in the actual world, that Lilly is licensed or at the very least has rights under the patentee, pursuant to subs.
- Evidence: `evidence_fact` cue `testimony` at chunk `5041108` offsets `206-215`; context: Sherman in his testimony and this in the eventuality that Apotex deemed it appropriate to present such an offer.
- Evidence: `reasoning_application` cue `because` at chunk `5041109` offsets `165-172`; context: That is, Apotex should only pay a reasonable royalty because the Shionogi patents were not used or commercialized in Canada.
- Evidence: `governing_rule` cue `under` at chunk `5041110` offsets `172-177`; context: [864] Presumably, although this was not argued, for Apotex, it has more strength in the “but for world” because Lilly would have had to establish that it indeed had rights under the patentee.
- Evidence: `reasoning_application` cue `because` at chunk `5041110` offsets `104-111`; context: [864] Presumably, although this was not argued, for Apotex, it has more strength in the “but for world” because Lilly would have had to establish that it indeed had rights under the patentee.

#### 22183:24:subtheme:8 · paragraphs 866-875

- Raw key terms: `court, apotex, lilly, shionogi, even, evidence, infringement, likely`
- Display key terms: `apotex, lilly, shionogi, even, infringement, likely`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: apotex, lilly, shionogi, even, infringement, likely Position/evidence statements: In addition, they submit that to recognize the type of argument put forth here by Apotex would amount to providing it with an insurance policy covering its acts of infringement. Rule/authority context: [868] The Court in the “but for world” would apply the general principles discussed in the main reasons, including the following comments of Justice Rothstein in Apotex (2000), at para. | [869] In the context of such an infringement action it is, in my view, as likely as not that the Court would conclude that Lilly does indeed have rights under the patentee. Application context: [866] I say “speculate” because, had there not been an assignment, the evidence before the Court would probably be very different. | [868] The Court in the “but for world” would apply the general principles discussed in the main reasons, including the following comments of Justice Rothstein in Apotex (2000), at para. Evidence spans paragraphs 866-875. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041112` offsets `387-392`; context: proceedings with Lilly and there could even be a judgment dealing with the issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041112` offsets `71-79`; context: [866] I say “speculate” because, had there not been an assignment, the evidence before the Court would probably be very different.
- Evidence: `reasoning_application` cue `because` at chunk `5041112` offsets `24-31`; context: [866] I say “speculate” because, had there not been an assignment, the evidence before the Court would probably be very different.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041112` offsets `541-544`; context: There would also likely be little evidence, if any, with respect to agreement(s) entered into by Shionogi and Lilly with third parties, as in the “but for world” Apotex would probably not have been entitled to make inquiries in that respect.
- Evidence: `evidence_fact` cue `record` at chunk `5041113` offsets `144-150`; context: [867] Although this also calls for speculation, one could assume that the Court in the “but for world” would have the benefit of an evidentiary record similar to the one in the main action but adding elements of the counterclaim.
- Evidence: `governing_rule` cue `principles` at chunk `5041114` offsets `63-73`; context: [868] The Court in the “but for world” would apply the general principles discussed in the main reasons, including the following comments of Justice Rothstein in Apotex (2000), at para.
- Evidence: `reasoning_application` cue `apply` at chunk `5041114` offsets `45-50`; context: [868] The Court in the “but for world” would apply the general principles discussed in the main reasons, including the following comments of Justice Rothstein in Apotex (2000), at para.
- Evidence: `governing_rule` cue `under` at chunk `5041115` offsets `153-158`; context: [869] In the context of such an infringement action it is, in my view, as likely as not that the Court would conclude that Lilly does indeed have rights under the patentee.
- Evidence: `reasoning_application` cue `conclude` at chunk `5041115` offsets `109-117`; context: [869] In the context of such an infringement action it is, in my view, as likely as not that the Court would conclude that Lilly does indeed have rights under the patentee.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041118` offsets `380-388`; context: Sherman’s evidence, this reasoning rings particularly true in the case at hand.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041119` offsets `47-55`; context: [873] Furthermore, Apotex has not provided any evidence whatsoever indicating that the profits it would have had to disgorge would likely be less than the damages which could be awarded to Lilly had it elected to seek damages instead of an accounting of profits.
- Evidence: `party_position` cue `submit` at chunk `5041121` offsets `135-141`; context: In addition, they submit that to recognize the type of argument put forth here by Apotex would amount to providing it with an insurance policy covering its acts of infringement.
- Evidence: `reasoning_application` cue `because` at chunk `5041121` offsets `628-635`; context: In reply,[412] Apotex notes that these concerns fail to take into account the fact that Apotex only had to enter the market at risk because of the unlawful arrangement between Shionogi and Lilly.

#### 22183:24:subtheme:9 · paragraphs 876-876

- Raw key terms: `apotex, assert, asserted, based, bulk, business, cefaclor, concluded`
- Display key terms: `apotex, assert, asserted, based, bulk, business, cefaclor, concluded`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: apotex, assert, asserted, based, bulk, business, cefaclor, concluded Evidence spans paragraphs 876-876. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5041122` offsets `129-136`; context: [876] Indeed, the evidence established that Apotex made a business decision to purchase its bulk cefaclor without inquiring into whether or not it infringed any patent it knew, or ought to have known, was being asserted by Lilly and Shionogi as relevant to the manufacture of bulk cefaclor.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041122` offsets `18-26`; context: [876] Indeed, the evidence established that Apotex made a business decision to purchase its bulk cefaclor without inquiring into whether or not it infringed any patent it knew, or ought to have known, was being asserted by Lilly and Shionogi as relevant to the manufacture of bulk cefaclor.

#### Section text

[830] Nor was it made on the belief that Kyong Bo had a licence:
THE COURT: Did you choose that supplier because it had a licence?
[DR. SHERMAN]: No.
[…]
THE COURT: […] Were you looking for a manufacturer that had a licence?
[DR. SHERMAN]: No.
[…]
[W]e were not looking for a manufacturer with a licence. At the time we were simply looking for sources that could supply. We did not know that one was needed.[384] At the time we were simply looking for sources that could supply. This particular source appeared to be a good supplier and was offering material and told us that they had an arrangement with Shionogi, but it is not because we were specifically looking for material made by Shionogi's process.[385]

[831] The Court notes that Dr. Sherman’s recollection about having been told that they had an arrangement with Shionogi appears to be slightly out of synch. In effect, the correspondence and Dr. Sherman’s own previous testimony indicates that such representations were made much later, that is in October, 1997. As soon as it was further investigated by Mrs. Fouillade, at the request of Dr. Sherman, it was quickly realized that this was not so.

[832] In any event, the approach that would have been taken by Apotex at the time is described by Dr. Sherman, when he testified on discovery that “[t]he most likely scenario would be that we simply would have used the [Shionogi] processes without any royalty at all or any discussion.”[386] While this was not as eloquently repeated by Dr. Sherman at trial, it was not contradicted. In fact, Dr. Sherman testified that:
to the extent that there were other patentees with other processes, there would generally not be a need to deal with them, because one would expect they would not be enforced in Canada or would be available for licensing.[387]
[Emphasis added]
Again this defies the fact that, independently of the assignment, Lilly was asserting rights under these patents, which is a fact which Dr. Sherman should have been aware of.

[833] In any event, it appears that Apotex was not prepared to pay much for such a licence. Dr. Sherman explained that if Shionogi would have tried to charge Apotex more than a few percent, Apotex would have resisted, sending the parties to litigation:[388]
if they wanted to enforce the patent to try and get a higher royalty, they would have been faced with the prospect of litigation with us and perhaps having their patents invalidated at litigation, and it wouldn’t have been worth very much to them under those circumstances.[[389]]

[834] This evidence suggests that for Apotex, obtaining a licence for bulk cefaclor was an option of last resort. At trial, Dr. Sherman testified that “[i]f and when it became necessary, we could get a license, if that were appropriate.”[390] This evidence is simply not sufficient for the Court to conclude that “but for” the assignment of the Shionogi patents, Apotex would have sought licensed supply.
12.7.2. Scenario 3: Apotex Practises the Shionogi Process and is not sued

[835] This scenario poses a number of evidentiary difficulties. First, and most obvious, Apotex’s conduct demonstrates that it was willing to obtain bulk cefaclor without regard to the method used to produce it. As noted above, the decision to source Kyong Bo was not dependent on the fact that it was practising a particular method. In addition, there is little evidence before the Court as to what led Apotex to begin sourcing bulk cefaclor from Lupin in May, 1997 other than because they had likely been approached by Lupin.[391]

[836] It is clear that Apotex inquired about Lupin’s process in July, 1997, at which point it had already received at least three shipments of bulk cefaclor. The Court cannot conclude that Apotex believed Lupin to be using the Shionogi process or again that such facts had become important or relevant in Apotex’s mind.

[837] The Court does not find it credible that, absent the assignment, Apotex would have made a conscious effort to source only bulk cefaclor made using the Shionogi process. The evidence supports the conclusion that Apotex was interested in supply, not supply manufactured using a particular process.

[838] Had the Court concluded differently in this respect, this scenario would still not be deemed more likely than not as the Court is not convinced that the evidence supports Apotex’s claim that the exclusive use of the Shionogi process would not attract an action for infringement.

[839] Specifically, there is absolutely no evidence or explanation offered to support the proposition that, in the “but for world”, enforcement of Shionogi’s patent rights would have not proceeded in precisely the same fashion as it did in the course of the PM (NOC) proceedings. As mentioned, the evidence is overwhelming that Lilly believed (again, rightly or wrongly) that it had an exclusive licence to the patents at issue and no good reason was offered to assert that Shionogi would be any less of a willing partner in their enforcement. The Court can only conclude that in the “but for world”, Apotex would have also faced an action for infringement, the only difference being that this action would be brought by both Lilly and Shionogi, just as with the PM (NOC) proceedings.
12.7.3. Scenarios 4 and 5: Apotex Practises the Shionogi and Lilly Processes and is Sued by Shionogi and Lilly

[840] As explained above, the Court cannot conclude that in the “but for world” it would be likely that Apotex would have sourced bulk cefaclor manufactured using only one process, be it Shionogi’s or Lilly’s. Thus, scenarios four or five cannot represent what would have occurred in the “but for world” as they are premised on Apotex practising only one of the processes.

[841] Most likely is a “but for world” where Apotex practised both the Shionogi and Lilly processes to varying degrees, exactly as what has transpired in the actual world. Apotex has admitted that it is very unlikely that in the “but for world” Lilly would not seek to enforce its patent rights. As explained above, there is no evidence that would lead the Court to conclude that such an action would not be conducted in the same fashion as the PM (NOC) proceedings with regard to infringement of the Shionogi patents.
12.8. Is there a loss resulting from the assignment under the most likely “but for world” scenario?

[842] Based on the foregoing, the only difference between the actual world and the only likely “but for world” scenario is that Shionogi is also a party to the action for infringement. Apotex’s submissions in respect of its loss in such a scenario (see scenarios 4 and 5 in Chart B) are not particularly clear.[392] When read together with paras 282 and 283 of its memorandum, it appears that Apotex alleges:
i) That should the Court set the “but for” price for bulk cefaclor at anything less than US$1,500.00[393], it paid more for its bulk cefaclor in the actual world than in the “but for world”; and,
ii) That its potential liabilities as a result of infringement are greater in the actual world than in the “but for world”;
For the reasons that follow, the Court cannot conclude that Apotex suffered any damage as a result of this assignment.

[843] Before looking specifically at the evidence relied upon by Apotex to support the above allegations, it is important to look at what Apotex’s experts had to say in cross-examination about potential losses in a scenario where Apotex did not seek or obtain a licence in the “but for world” from Shionogi (directly or indirectly).

[844] First, Dr. Church said “[…] what I would agree with is that [if] you can establish that in the “but for” world, Apotex would not have received supply from either Shionogi or from Lilly then Apotex would not have been harmed.”[394]

[845] This was also the view of Dr. Ross:
[Counsel for Lilly]: You will agree with me that if it chose another company to license and not Apotex then there would have been no impact on Apotex as a result of the 1995 agreement?
[Dr. Ross]: I think that is right. Let us just be clear. Absent the ’95 agreement, they would have licensed someone else?
[Counsel for Lilly]: Right.
[Dr. Ross]: Now you bring in the ’95 agreement so there is nobody licensed, what is the effect of Apotex. That is correct.
[Counsel for Lilly]: So you agree there would have been no impact on Apotex?
[Dr. Ross]: Right.[[395]]

[846] As for Mr. Cole, he was asked to assume that the Court found that there was anti-competitive conduct and that Apotex had infringed and as such was liable to pay damages. He was then asked to consider the scenario where this Court also held that in the “but for world”, Apotex would not enter into a licensing agreement. In his view, “under that logic or that assumption, there would be no damages, I think. There would be no damages. […] That is a fair assumption.”[396]

[847] Despite this evidence, Apotex nonetheless maintains that it has suffered a loss measured against scenarios 4 and 5, where it is evident that it would not be a licensee of either Shionogi or Lilly.

[848] The court will first examine whether or not Apotex has established a loss in respect of the costs paid for the bulk cefaclor, given that, in accordance with Justice Hughes’ judgment referred to earlier, the Court must be in a position to quantify Apotex’s loss in that respect.
12.9. Increased Cost of Legal Bulk Cefaclor

[849] The Court is not satisfied that Apotex has established by any standard that it would have contracted for its bulk cefaclor in the “but for world” at any price less than it paid in the actual world. In effect the price it paid for infringing material (all but the cefaclor produced by Lupin in 1998) could not be affected by the prices for legal bulk cefaclor whatever they may have been in the “but for world”. The Court understands that it is exactly for that reason that Apotex’s experts made the admissions referred to above and concluded that Apotex suffered no loss in said context.

[850] The Court knows that in any event even if the price of the legal bulk cefaclor in the “but for world” was relevant here, Apotex has failed to provide the Court with sufficient evidence to conclude that it has suffered a loss.

[851] Apotex’s experts only address the issue of price differential between the monopoly price[397] and the duopoly price in the “but for world”. It appears that they were never asked to precisely determine if there was a difference between the actual price paid and the duopoly price in the “but for world” for they appear content with a mere range of possible prices for legal bulk cefaclor in the “but for world”: US$ 860.00 to US$ 1,500.00.[398]

[852] While in reply to the testimony of Dr. Cockburn, Dr. Church and Dr. Hollis submitted that the price of US$ 1,150.00 charged by Lilly to Novopharm could be a more precise estimate, they did not renege on their initial proposition. During oral argument, Apotex’s counsel suggested that the Court should adopt the price of $1,150.00 which is very near the mid-range used by its own experts. The Court is not satisfied that it should do so. Apotex had the burden of establishing its loss; it could have easily asked its experts to do so. Considering their testimony, one can reasonably infer that it did not do so because, according to the experts, Apotex would not have suffered any loss.
12.10. Infringement Liability

[853] Apotex argues[399] that allowing Lilly to retain damages that it could only recover by virtue of rights that were unlawfully obtained would amount to an unjust enrichment or unjustified benefit. However, it is crucial to remember that, pursuant to s. 36, the inquiry is directed to the actual damage suffered by the plaintiff, who can only recover “an amount equal to the loss or damage proved to have been suffered by him.”[400]

[854] In respect of the Shionogi patents, Apotex says that in the “but for world” it would only be liable to pay damages that would be “no greater than a reasonable royalty rate.”[401] Apotex also argues that in respect of the Lilly patents, although they were not the subject of the assignment, its potential liability would still have been less in the “but for world” given that Lilly would have faced competition from Shionogi. Thus, the lost profit Lilly would be claiming would be less.[402]
12.10.1. The Lilly Patents

[855] Little evidence was presented to support Apotex’s argument aside from a single page from a single report of a single expert, Dr. Church,[403] which is barely answered by Shionogi and Lilly. Therein, Dr. Church offers a formula, [pm – p]qA, wherein pm “is the price Lilly lost as a monopolist”;[404] p “is the price Lilly would have charged for bulk cefaclor had there been competition”;[405] and, qA is Apotex’s quantity of sales (dosage form).

[856] When asked by the Court to explain the relevance of this formula and how it could be used, Dr. Church volunteered what the Court has come to realize are some very serious limitations to his approach:
[The Court]: So you are telling me you could have calculated this precisely but you didn’t because you weren’t asked.
[Dr. Church]: No, I was not asked and I couldn’t – you know, perhaps I might have been able to calculate these things, but you know, it was not part of the remit. It was just what I was asked to do is come up with a framework.
[The Court]: Why do you say “might”? It is just, you know, you might? How will I do it if you say you might?
[Dr. Church]: My lady, I apologize. I mean, I wasn’t asked to do that.
[The Court]: Okay, that is fine. So your answer is you haven’t, you could have or you might have been able to do it, but you weren’t asked.
[Dr. Church]: Right, right. I mean, what I have is a framework to show that they could have been damaged.[[406]]
[Emphasis added]

[857] First, the Court finds this to be a particularly obscure part of the evidence of this expert and Apotex made no effort whatsoever to explain para. 283 of its memorandum. It appears to be predicated on an assumption that Lilly’s profit on bulk cefaclor is relevant to the quantification of the infringement damages in the main action.

[858] Second, as mentioned earlier, this framework is inconsistent with positions taken at trial by Dr. Church himself as well as other Apotex experts. It therefore cannot have been intended to apply in the only plausible “but for world” scenario here, which does not involve any licensing by Shionogi.

[859] In any event, Dr. Church’s proposed framework only serves the purpose of establishing that Apotex could have been harmed, not that it was in fact the case. Even though the assessment of the quantum was bifurcated, Apotex still had the burden of establishing that it did suffer damages, not simply that it “could” have suffered damages. Apotex has done nothing more than offer speculation to the Court in that respect.

[860] The Court is not ready to reach any conclusion based on this evidence.
12.10.2. The Shionogi Patents

[861] In the “but for world” Shionogi and Lilly would be co-plaintiffs and they would advance, like they did in the actual world, that Lilly is licensed or at the very least has rights under the patentee, pursuant to subs. 55(1) of the Patent Act.

[862] The Court has not been persuaded that there is even a real or substantial possibility that Shionogi, in such a scenario, would agree to settle for the low royalty fee alluded to by Dr. Sherman in his testimony and this in the eventuality that Apotex deemed it appropriate to present such an offer.[407]

[863] This means that the only argument left is the same one that was raised in the actual world against Lilly. That is, Apotex should only pay a reasonable royalty because the Shionogi patents were not used or commercialized in Canada.[408] It was rejected despite a thoroughly developed presentation.

[864] Presumably, although this was not argued, for Apotex, it has more strength in the “but for world” because Lilly would have had to establish that it indeed had rights under the patentee.

[865] This brings us back to the 1975 agreement and the relationship between the two plaintiffs in a “but for world” and requires that the Court speculate as to what decision a Court would render in the “but for world”.

[866] I say “speculate” because, had there not been an assignment, the evidence before the Court would probably be very different. For example, there would likely not exist any correspondence between Lilly and Shionogi in respect of a possible assignment.[409] Shionogi could well have been involved in the U.S. proceedings with Lilly and there could even be a judgment dealing with the issue. There would also likely be little evidence, if any, with respect to agreement(s) entered into by Shionogi and Lilly with third parties, as in the “but for world” Apotex would probably not have been entitled to make inquiries in that respect.[410]

[867] Although this also calls for speculation, one could assume that the Court in the “but for world” would have the benefit of an evidentiary record similar to the one in the main action but adding elements of the counterclaim. For example, there would also be evidence in the “but for world” that Dr. Gorman of Lilly sought Shionogi’s help in developing “a method to economically synthesize the 3-halo cephalosporin,”[411] in June, 1974 and that prior to the presumed date of invention (February, 1975) Dr. Cooper met with Shionogi’s research team to give them details of Lilly’s research including details of the so-called Cooper thiazoline compound which is a starting material for the Shionogi process.

[868] The Court in the “but for world” would apply the general principles discussed in the main reasons, including the following comments of Justice Rothstein in Apotex (2000), at para. 99:
It is perhaps not uncalled for to observe that this is not a case in which the alleged licensee is alone in advancing its claim for patent infringement. Here, the patentee is also before the Court as a co-plaintiff supporting the claim of GWI. It is difficult to conceive of what more is necessary to prove the existence of a licence than to have the licensor and licensee both attesting to the validity of the licence.

[869] In the context of such an infringement action it is, in my view, as likely as not that the Court would conclude that Lilly does indeed have rights under the patentee.

[870] Thus, even if the Court was entitled to speculate as much as Apotex suggests it should, the Court has not been persuaded that Apotex would not be exposed to exactly the same conclusions that were reached in the main action.

[871] Moreover, even if one were to assume that Lilly had no such rights, Shionogi could very well be entitled to an accounting of profits from Apotex. In such a case, the measure of restitution is the defendant’s gain, rather than the plaintiff’s loss (Monsanto Canada Inc. v. Rivett, 2009 FC 317, [2009] F.C.J. No. 410 (QL) , para. 21 (Monsanto Canada Inc. v. Rivett) and Bayer Aktiengesellschaft v. Apotex Inc. (2001), 10 C.P.R. (4th) 151 (Ont. S.C.J.); aff’d (2002), 16 C.P.R. (4th) 417 (Ont. C.A., where the Court rejected Apotex’s argument that the wronged party should not be unjustly enriched by awarding it a sum in excess of its actual loss).

[872] As noted by Justice Russel Zinn in Monsanto Canada Inc. v. Rivett, if this option was not open to Shionogi “it would be too easy for a defendant to say “Catch me if you can.” If caught, the defendant would be required to pay the sum he would have paid to use the patent in any event. When not caught, he is left with a windfall”. (para. 23) When one considers Dr. Sherman’s evidence, this reasoning rings particularly true in the case at hand.

[873] Furthermore, Apotex has not provided any evidence whatsoever indicating that the profits it would have had to disgorge would likely be less than the damages which could be awarded to Lilly had it elected to seek damages instead of an accounting of profits

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 22183:25 · paragraphs 877-883

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `532e0521ec1317400a9ea247fd0ca7467b852570f0c0924204a1d3bde22c3bec`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:25:subtheme:1 · paragraphs 877-880

- Raw key terms: `apotex, court, infringement, loss, right, adopted, answer, argues`
- Display key terms: `apotex, infringement, loss, right, adopted, answer, argues`
- Argument roles: `reasoning_application`
- Explanation: Observed roles: reasoning_application Display terms: apotex, infringement, loss, right, adopted, answer, argues Application context: Would Apotex say that it suffered a loss because it is now exposed to being sued for infringement? Evidence spans paragraphs 877-880. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `5041125` offsets `377-384`; context: Would Apotex say that it suffered a loss because it is now exposed to being sued for infringement?

#### 22183:25:subtheme:2 · paragraphs 881-883

- Raw key terms: `costs, case, trial, above, answered, arguments, assess, assessed`
- Display key terms: `costs, case, trial, above, answered, arguments, assess, assessed`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: costs, case, trial, above, answered, arguments, assess, assessed Evidence spans paragraphs 881-883. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5041127` offsets `120-126`; context: [881] After careful consideration, I have come to the conclusion that it would be inappropriate to comment on the other issues raised in this case, particularly whether or not there was a violation of s.
- Evidence: `counterargument_limitation` cue `however` at chunk `5041128` offsets `298-305`; context: It is clear, however, that certain circumstances referred to in the above mentioned representations warrant an award of costs beyond what is normally provided for.

#### Section text

[877] Thus, even if Apotex had established a loss in respect of its infringement liability, the Court would not have been persuaded that it arose as a result of the assignment.[413]

[878] Finally, one must not lose sight of the fact that the Competition Act was adopted to protect the public interest. Its goal is not to protect the rights of those who choose to act in a manner contrary to the law. What Apotex argues here is that it has the right to infringe at the lowest possible cost.

[879] It was made very clear when the Court, trying to clarify Apotex’s position, solicited its view on the following hypothetical scenario: what if a patentee, a small company with little means to enforce its patents, decides to sell at fair-market value its patent to a bigger company whose policy is to strictly enforce its patents. Would Apotex say that it suffered a loss because it is now exposed to being sued for infringement? To this, counsel for Apotex responded that “the answer would be yes”.[414]

[880] This simply cannot be right.

[881] After careful consideration, I have come to the conclusion that it would be inappropriate to comment on the other issues raised in this case, particularly whether or not there was a violation of s. 45 of the Competition Act. This raises some important novel questions that should not be answered by way of obiter comments.[415]
12.11. Costs

[882] Lilly and Shionogi made extensive representations to support their claim for solicitor-client costs in this case. Having considered all the arguments and the factors set out in Rule 400, the Court has concluded that this is not a case where solicitor-client costs are warranted. It is clear, however, that certain circumstances referred to in the above mentioned representations warrant an award of costs beyond what is normally provided for. Thus, costs of all services rendered prior to trial will be assessed on the basis of the top of the scale of Column III of Tariff B while services rendered after the trial started will be assessed on the basis of the top of the scale of Column IV of the said Tariff.

[883] The defendants by counterclaim are entitled to assess costs of two counsel as well as reasonable expert witness fees and disbursements for the expert witnesses who testified at trial.


## 22183:26 · paragraphs 884-885

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7522db6bfeaa430f09e2909d6468d700f3a4758749ae6bdcd9ffa32a1dfa5ad5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:26:subtheme:1 · paragraphs 884-885

- Raw key terms: `parties, a-10, a-11, a-12, a-13, a-14, a-15, a-17`
- Display key terms: `a-10, a-11, a-12, a-13, a-14, a-15, a-17`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: a-10, a-11, a-12, a-13, a-14, a-15, a-17 No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 884-885. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
For the Reasons set out herein, following the trial of this action, this Court adjudges and declares as follows:
At least one valid claim in each of the following patents:
Canadian Letters Patent No. 1,133,007; Canadian Letters Patent No. 1,146,536; Canadian Letters Patent No. 1,133,468 ; Canadian Letters Patent No. 1,150,725; Canadian Letters Patent No. 1,095,026; Canadian Letters Patent No. 1,132,547; Canadian Letters Patent No. 1,136,132; Canadian Letters Patent No. 1,144,924;
have been infringed by the defendant, Apotex Inc. by their importation, manufacture, export, sale and offers for sale of cefaclor in Canada;
The plaintiffs are entitled to elect either an accounting of profits of the defendant or all damages sustained by reason of sales directly lost as a result of the infringement by the defendant of the above-mentioned claims of the Lilly patents (‘007, ‘536, ‘468, ‘725 patents) or Shionogi patents (‘026, ‘547, ‘132, ‘924 patents). Such damages will be assessed by reference preceded by discovery if requested;
The defendant shall be entitled to deduct up to a maximum of 187 kilos of bulk cefaclor pursuant to subs. 55.2(1) of the Patent Act. The exact quantity to be assessed by reference in accordance with my reasons;
The plaintiffs are entitled to pre-judgment interest on the award of damages (if elected), not compounded, at a rate to be calculated separately for each year since infringing activity began at the average annual bank rate established by the Bank of Canada as the minimum rate at which it makes short-term advances to the banks listed in Schedule 1 of the Bank Act, R.S.C. 1985, c. B-1. However, such award is conditional upon the reference judge not awarding interest under paragraph 36(4)(f) of the Federal Courts Act;
In the event that the plaintiffs elect an accounting of profits, interest shall be determined by the reference judge;
The plaintiffs are entitled to post-judgment interest, not compounded, at the rate of five percent (5%) per annum, as established by s. 4 of the Interest Act, R.S.C. c. I-15. This interest shall commence upon the final assessment of the monetary damage amount or profits amount, until then pre-judgment interest shall prevail;
The plaintiffs are entitled to their costs which will be the subject of a distinct order. The parties shall within thirty (30) days hereof make submissions as to the amount of said costs in the manner set out in my reasons;
The defendant’s counterclaim is hereby dismissed, with costs to be assessed in accordance with my reasons.
“Johanne Gauthier”
Judge
CHART “A”
Infringement
Name
Subject Matter
Date
Exhibit number
Terms of qualification
Brief Bio Note
1
Anthony G.M. Barrett
Lilly infringement in chief – Kyong Bo process
October 19, 2007
E-1
Expert in chemistry, organic chemistry, in particular beta-lactam chemistry including cephalosporins and penicillins; chemistry research techniques, organic and medicinal compound synthesis, manufacturing, manipulation and antibiotic mechanisms and activity; experimental and analytical chemistry testing, techniques and interpretation, including analysis and interpretation and chemical compound properties, compound and structure analysis and identification.
Dr. Anthony Barrett is Professor of organic chemistry and synthetic chemistry at Imperial College of Science, Technology and Medicine (UK). He obtained his PhD in 1975. Over the course of his career, he has also taught at Northwestern University and Colorado State. He was named a Fellow of the Royal Society (UK) in 2003. He is a specialist in the synthesis of beta-lactams and has studied penicillins and cephalosporins since the 1970’s. He has published extensively in this field over three decades. He is the author of over 330 publications.
2
Marvin Miller
Lilly infringement in chief – Lupin process (experiments)
October 8, 2007
E-2
Expert in: 1) chemistry, organic chemistry, medicinal chemistry, in particular beta-lactam chemistry including cephalosporins and penicillins; 2) chemistry research techniques, organic and medicinal compound synthesis, manufacturing, manipulation and antibiotic mechanisms and activity; 3) experimental and analytical chemistry testing, techniques and interpretation, including NMR, IR and LC/MS, analysis and interpretation and chemical compound properties, compound and structure analysis and identification.
Professor and former Chair of the Department of Chemistry and Biochemistry at the University of Notre Dame, Indiana. PhD in bio-organic chemistry, Cornell University, 1976. Post-doctoral research at UC Berkeley. Extensive experience in the organic chemistry and synthesis of beta-lactams. Has been Editor for a variety of research journals. Author or co-author of over 225 peer-reviewed publications.
3
Marvin Miller
Lilly infringement in chief – Lupin process
October 19, 2007
E-3
See above.
See above.
4
Garrett Moraski
Lilly infringement in chief – Lupin process –experiments (Testing)
October 19, 2007
E-4
Expert in experimental and analytical chemistry research techniques, practices, instruments and documentation, and NMR and IR analysis.
Hold a B.Sc in chemistry (1997) from the University of Notre Dame. He is currently Research Technician and Lab Manager in the laboratory of Dr. Miller at the University of Notre Dame. Four years experience as a research assistant at Pfizer and several more years as a researcher at a pharmaceutical start-up. Has actively participated in Dr. Miller’s research activities and been listed as co-author in several peer-reviewed publications.
5
Brian Hunter
Lilly infringement in chief – Lupin process – P NMR and IR spectra data regarding kinetic complex
October 22, 2007
E-5
A chemist with a focus on the utilization of nuclear magnetic resonance and infrared spectroscopy to study molecular behaviour in a variety of systems.
Emeritus professor of chemistry and chemical engineering at Queen’s University, Kingston. Ret’d 2001. PhD obtained from University of Western Ontario, 1969. National Research Council Fellow at University College in London 1969-1971. Research and teaching specialty in the utilization of nuclear magnetic resonance (NMR) spectroscopy, including phosphorous NMR, to study molecular behavior. Has provided advice in the interpretation of NMR spectra across all fields of chemistry. Author of a textbook entitled Modern NMR Spectroscopy: a Guide for Chemists (2nd ed. 1993).
6
Jack Baldwin
Lilly infringement in chief – Lupin process
October 19, 2007
E-6
Expert in: 1) chemistry, organic chemistry, medicinal chemistry, in particular beta-lactam chemistry including cephalosporins and penicillins; 2) chemistry research techniques, organic and medicinal compound synthesis, in particular beta-lactam synthesis, manufacturing, manipulation and antibiotic mechanisms and activity; 3) experimental techniques and interpretation as used by chemists in this field in the course of their work.
Sir Baldwin is Professor of Chemistry at Oxford University (ret’d. 2005) and was Professor of Chemistry at the Massachusetts Institute of Technology from 1972-1978. He obtained his PhD from Imperial College in 1964. He has been a Fellow of the Royal Society since 1978, and was recognized for contribution to chemistry with a Knighthood in 1997. Throughout his distinguished career he has been particularly interested in the synthesis of beta-lactam antibiotics, especially penicillins and cephalosporins, and is familiar with industrial work in this area.
7
Diane Azzarello
Lilly infringement in chief – Health Canada regulatory requirements
October 19, 2007
E-7
Expert in regulatory affairs, including preparation and filing of new drug submissions and any other matter covered within her report.
Ms. Azzarello is an Ontario-licensed pharmacist with over two decades experience in the pharmaceutical industry in clinical research, sales, and regulatory affairs. She is a past Director of regulatory affairs for Upjohn Canada, and has acted since 1996 as President of Market Access Strategic Regulatory Services Inc., a consultancy, where she advises innovator and generic companies on the filing of drug submissions with Health Canada.
8
Garrett C. Moraski
Lilly infringement reply – testing of February 21, 2008 in response to Dr. Cowley and Dr. McClelland (Under reserve of a general objection)
February 28, 2008
E-8
See above.
See above.
9
Garrett C. Moraski
Lilly infringement reply – Dr. Hunter and Miller testing. Completed by new exhibit E-9a on June 20, 2008
January 18, 2008
E-9
See above.
See above.
10
Garrett C. Moraski
Lilly infringement reply – Re Dr. Chase testing
April 19, 2008
E-10
See above.
See above.
11
David Gorenstein
Lilly infringement reply – Lupin process (Under reserve of a general objection)
March 19, 2008
E-11
Expert with respect to the development and application of NMR spectroscopy to biological systems, and an expert chemist who has carried out extensive research in the chemistry of phosphorous compounds and organophosphorous chemistry.
Dr. Gorenstein is Associate Dean of Research at the School of Medicine of the University of Texas. He is also a Professor in the Departments of Biochemistry and Molecular Biology, and Neurosciences and Cell Biology. His research interests include the development and application of NMR spectroscopy to biological systems (including 31P NMR), and he is Director of the Gulf Coast Consortium in Magnetic Resonance, an NMR facility shared by several regional universities and Dow Chemical. For nearly two decades he has served as editor of the journal published by the International Society of Magnetic Resonance and also edits on online NMR textbook. He is the author of over 245 publications including a 1984 article entitled “Phosphorous-31 NMR Principles and Applications,” and has extensive teaching and training experience in NMR spectroscopy. He has also conducted extensive research into the chemistry of phosphorous compounds over the past 40 years.
12
Anthony G.M. Barrett
Lilly sur-reply – infringement – Lupin process – (by leave but under reserve of objection – with respect to certain paragraphs)
June 15, 2008
E-15
See above.
See above.
13
Brian K. Hunter
Lilly reply – infringement Lilly patents – reply to McClelland report of January 18, 2008 and Cowley report of January 17, 2008 (Under reserve of objection: see TX-343 to TX-344)
March 20, 2008
E-17
See above.
See above.
14
Brian K. Hunter
Lilly supplemental reply – infringement – Apotex April 2008 testing at University of Toronto (Dr. Chase)
April 20, 2008
E-16
See above.
See above.
15
Tomasz A. Modro
Apotex infringement responding – P NMR spectra testing in South Africa
May 7, 2008
A-6
An expert in organic chemistry of phosphorous, sulfur and silicon, as well as in the area of physical organic chemistry, and an expert in carrying out experimental reactions involving the chemistry of phosphorous.
Dr. Tomasz Modro received his PhD in Organophosphorous Chemistry in 1962 from the Polish Academy of Sciences and his Habilitation from the University of Lodz in 1969. In 1974, he joined the Department of Chemistry of the University of Toronto, as Lecturer and later Assistant Professor. In 1979, he joined the Department of Chemistry at the University of Cape Town and in 1987 he joined the University of Pretoria as Professor of Chemistry and Director of the Centre for Heteroatom Chemistry, where he has been Professor Emeritus since 2002.
Dr. Modro specializes in the area of heteroatom chemistry involving the organic chemistry of phosphorous, sulfur and silicon, and the synthesis and use of novel organophosphorous compounds in chemical transformations. He has been recognized as an international leader in his field by the National Research Foundation (South Africa) and is a member of both the Royal Society (South Africa) and the South African Academy of Sciences. He has published over 210 papers.
16
Preston Allen Chase
Apotex infringement responding - Testing at the University of Toronto
April 11 and 17, 2008
TX-1626 C, D, E, F, G, H.
An expert in organophosphorous chemistry, the chemistry of reactions involving organic compounds.
Dr. Chase is a Research Associate at the University of Toronto. He received PhD in April 2003 from the University of Calgary and is past NSERC fellowship holder. After obtaining his PhD, he undertook post-doctoral research at the University of Utrecht (Netherlands). From 2006 to 2008, he has been at the University of Windsor, where he focuses on chemistry related to his PhD work as well as phosphorous and nitrogen chemistry. He has extensive experience carrying out reactions involving organophosphorous compounds and has published a number of papers dealing with such compounds.
17
Robert A. McClelland
Apotex infringement responding – Lupin process
January 18, 2008
TX-1764
Expert in physical, organic, biological and medicinal chemistry including the synthesis properties and use of organophosphorus compounds in chemical reactions.
Dr. McClelland is Professor Emeritus at the University of Toronto. He obtained his PhD in chemistry from the University of Toronto in 1969 and has been a faculty member there since 1973. His research activities are in the areas of physical organic, biological and medicinal chemistry. He is a Fellow of the Royal Society (Canada) and has received awards from the Canadian Society for Chemistry for his work in organic chemistry.
18
Robert A. McClelland
Apotex infringement responding – Testing at the University of Toronto
May 6, 2008
TX-1765
See above.
See above.
19
Alan H. Cowley
Apotex infringement responding – ‘007 patent and addressee of ‘536 patent
January 17, 2008
A-9
Research chemist with expertise in the preparation, structures and patterns of reactivity of compounds of the non-metallic elements, phosphorous chemistry and the use and evaluation of 31P NMR spectroscopy.
Dr. Cowley is a Fellow of the Royal Society (UK) and occupies the Robert J. Welch Chair in Chemistry at the University of Texas at Austin. He was awarded a PhD in inorganic chemistry from the University of Manchester, UK, in 1958. He joined the faculty at the University of Texas (Austin) in 1962 and was made full professor in 1970. His major research interests have been the preparation, structure and patterns of reactivity of compounds of the non-metallic elements, with a focus on phosphorous chemistry.
20
Stephen Hanessian
Apotex infringement responding – General comments
January 22, 2008
A-10
Expert in organic, bio-organic and medicinal chemistry, including specifically the chemistry of synthetic penicillins and beta-lactam antibiotic compounds and the development of synthetic chemical processes.
Dr. Stephen Hanessian is the McConnell Professor of Chemistry at the University of Montreal, where he joined the Faculty in 1969, and has been since 2000 Adjunct Professor in Chemistry and Chemical Biology at the University of California, Irvine, where he directs a graduate program in pharmaceutical sciences and medicinal chemistry.
Dr. Hanessian’s research interests are in the total synthesis of natural products, including the synthesis of amonoglycoside antibiotics and synthetic penicillins, as well as medicinal chemistry, drug design and the development of new synthetic methods. He has published over 465 papers in these fields. His contributions have been recognized by a Fellowship in the Royal Society (Canada) and membership in the Order of Canada.
21
Stephen Hanessian
Apotex responding to E-15 – (by leave) -infringement – Lupin processes
July 2, 2008
A-20
See above.
See above.
22
Sue E. Wehner
Apotex infringement responding – Health Canada regulatory requirements
January 22, 2008
A-11
Expert in pharmaceutical regulatory affairs, including the preparation and filing of new drug submissions; the evaluation of drug master files; and the regulatory practices and procedures, guidelines, policies and requirements of Health Canada regarding pharmaceutical practice.
Ms. Wehner is the founder and President of Med-Script Associates, a consultancy specializing in regulatory affairs in Canada, the US, and Europe, as well as R&D in product development and clinical and bioequivalence studies. She has over 30 years experience in this area and has filed new and abbreviated drug submissions for many drugs.
Validity
23
Robert A. McClelland
Apotex in chief – validity
October 19, 2007
A-12
See above.
See above.
24
Tomasz A. Modro
Apotex in chief – validity of ‘007 patent
October 19, 2007
A-13
See above.
See above.
25
Tomasz A. Modro
Apotex in chief – validity – affidavit concerning testing (TX-1774 A to M, L and M being under reserve of objection)
June 2, 2008
A-14
See above.
See above.
26
Stephen Hanessian
Apotex in chief – validity – Shionogi patents
October 19, 2007
A-15
See above.
See above.
27
Stephen F. Martin
Apotex in chief – validity – Shionogi patents
October 19, 2007
A-17
Expert in synthetic organic chemistry, heterocyclic chemistry and bio-organic chemistry, including specifically the design and development of synthetic models and their application to the synthesis of heterocyclic compounds including lactams and the total synthesis of complex natural products.
Dr. Martin is the M. June and J. Virgil Waggoner regents Chair of Chemistry at the University of Texas at Austin, where he has been on faculty since 1974. He is also Adjunct Professor at the University of Texas School of Medicine. He obtained a PhD from Princeton University in 1972, where he specialized in heterocyclic chemistry. Over the course of his career Dr. Martin has been extensively engaged in the design and development of synthetic methods and their application to the synthesis of heterocyclic compounds and the total synthesis of natural products. He is the author of over 250 publications in the fields of synthetic organic chemistry and heterocyclic chemistry, some of which deal with lactams (not including β-lactam) and pre-date 1975.
28
Tristram Chivers
Apotex in chief – validity – Lilly ‘007 patent
October 19, 2007
A-18
Expert in inorganic synthetic chemistry, particularly the chemistry involving the elements sulfur and phosphorous, and in the use of 31P NMR spectroscopic techniques.
Dr. Chivers obtained his PhD in chemistry from the University of Durham (UK) in 1964 and has been a faculty member in the Department of Chemistry, University of Calgary, since 1969. His research has focused on inorganic chemistry, particularly as it involves the elements sulfur, selenium, tellurium, boron, and phosphorous. He is the author of over 300 journal articles. His work has been recognized through various awards and he was made a Fellow of the Royal Society (Canada) in 1991.
29
George Andrew Olah
Apotex in chief – invalidity of Lilly ‘536 and ‘007 patents
October 18, 2007
A-19
Expert in the area of organic and organosulfur chemistry as well as the area of physical organic chemistry including the synthesis of novel ionic organic compounds and their use in other chemical transformations, as well as hydrocarbon chemistry and synthetic reagents and methods.
Dr. Olah is Director of the Loker Hydrocarbon Research Institute and Distinguished Professor of Organic Chemistry at the University of Southern California, Los Angeles, where he has been a faculty member since 1977. He obtained his PhD in chemistry from the Technical University in Budapest (1949) and is a past head of the Department of Organic Chemistry at the Institute of the Hungarian Academy of Sciences, past Professor at the Western Reserve University (now Case Western). He was also a research scientist with Dow for 7 years. His research activities are in the areas of organic and organosulfur chemistry and the synthesis of novel ionic organic compounds and their use in other chemical transformations, as well as hydrocarbon chemistry and synthetic reagents and methods. He has published over 1300 peer-reviewed articles and is a member of numerous learned societies. He was awarded a Nobel Prize in 1994 for his work on positivel

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 22183:27 · paragraphs 886-887

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4fa93103bce08f45be695263c8b1c65da18f6d5708937b3fc0fbde4afd213039`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:27:subtheme:1 · paragraphs 886-887

- Raw key terms: `ibid, lrta`
- Display key terms: `ibid, lrta`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: ibid, lrta No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 886-887. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

[2] Ibid., LRTA # 1 and 51.

[3] Ibid., LRTA # 9 and 50.

## 22183:28 · paragraphs 888-899

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b9c2e6e3f53c9bb395344071a191d70be27f0eab6617df12f6962cf2a4b5416b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:28:subtheme:1 · paragraphs 888-892

- Raw key terms: `case, patents, agreed, applicable, application, april, because, canada`
- Display key terms: `case, patents, agreed, applicable, april, because`
- Argument roles: `disposition, evidence_fact, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, reasoning_application Display terms: case, patents, agreed, applicable, april, because Application context: [4] The application was dismissed because the patents did not meet the criteria set out in the PM (NOC) regulations applicable at that time. Operative outcome context: [4] The application was dismissed because the patents did not meet the criteria set out in the PM (NOC) regulations applicable at that time. Evidence spans paragraphs 888-892. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `5041133` offsets `34-41`; context: [4] The application was dismissed because the patents did not meet the criteria set out in the PM (NOC) regulations applicable at that time.
- Evidence: `disposition` cue `dismissed` at chunk `5041133` offsets `24-33`; context: [4] The application was dismissed because the patents did not meet the criteria set out in the PM (NOC) regulations applicable at that time.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041134` offsets `30-38`; context: [5] Having considered all the evidence and the case law submitted, including all the prior art, the Court was guided by the comments of the Supreme Court of Canada in R.

#### 22183:28:subtheme:2 · paragraphs 893-899

- Raw key terms: `apotex, court, evidence, expert, lilly, reasons, allegedly, answer`
- Display key terms: `apotex, expert, lilly, allegedly, answer`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: apotex, expert, lilly, allegedly, answer Rule/authority context: [14] Chart A also includes under the heading Competition the eight expert reports filed in the counterclaim. Evidence spans paragraphs 893-899. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041138` offsets `20-25`; context: [9] That said, this issue is not relevant to the present findings.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041140` offsets `30-38`; context: [11] In this case there is no evidence that those responsible for such testing at Apotex were aware of the fact that Lupin allegedly changed its process in 1998 or at any other time.
- Evidence: `evidence_fact` cue `found that` at chunk `5041141` offsets `220-230`; context: Also, the Court initially worked using the electronic version of the revised transcripts until it was found that as these were not in PDF format pagination was not reliable.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041141` offsets `377-380`; context: In footnotes to these reasons I refer to the paper version of the revised transcript but there may still be some inaccuracies.
- Evidence: `governing_rule` cue `under` at chunk `5041143` offsets `27-32`; context: [14] Chart A also includes under the heading Competition the eight expert reports filed in the counterclaim.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041144` offsets `40-48`; context: [15] In reply, Lilly also presented the evidence of Dr.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041144` offsets `67-70`; context: Gorenstein but as will be discussed later on, this expert evidence was not considered by the Court.

#### Section text

[4] The application was dismissed because the patents did not meet the criteria set out in the PM (NOC) regulations applicable at that time.

[5] Having considered all the evidence and the case law submitted, including all the prior art, the Court was guided by the comments of the Supreme Court of Canada in R. v. R.E.M., 2008 SCC 51, [2008] S.C.R. 3, particularly at para. 43.

[6] And then the 3-chloro-3-cephem compound in the case of the Lilly process patents.

[7] See Facts agreed to by the parties, LRTA # 81.

[8] Transcript of April 21, 2008 contains a typographical error at p. 179, line 2.

[9] That said, this issue is not relevant to the present findings.

[10] See Eli Lilly and Co. v. Apotex Inc. (2000), 8 C.P.R. (4th) 413, 99 A.C.W.S. (3d) 319 (Eli Lilly (2000)), aff’d, 2001 FCA 141, 12 C.P.R. (4th) 127 (Eli Lilly (2001)). Request made by Apotex after these decisions were issued should have been the subject of a motion to obtain an answer if there were valid reasons to argue that there was no res judicata.

[11] In this case there is no evidence that those responsible for such testing at Apotex were aware of the fact that Lupin allegedly changed its process in 1998 or at any other time.

[12] At this point, it must be said that the parties used different versions of the transcripts in their submissions. Also, the Court initially worked using the electronic version of the revised transcripts until it was found that as these were not in PDF format pagination was not reliable. In footnotes to these reasons I refer to the paper version of the revised transcript but there may still be some inaccuracies. See Cross-examination of Dr. Sherman, May 6, 2008, p. 157 line 2 to p. 158, line 1; cross-examination of Dr. Sherman, September 3, 2008, p. 90, line 24 to p. 91, line 17, p. 95, lines 3-12, and p. 96, line 5 to p. 97, line 16.

[13] It should be noted that this should not be described as complete files given that Singh indicated that he did not archive or keep his files intact.

[14] Chart A also includes under the heading Competition the eight expert reports filed in the counterclaim.

[15] In reply, Lilly also presented the evidence of Dr. Gorenstein but as will be discussed later on, this expert evidence was not considered by the Court.

## 22183:29 · paragraphs 900-900

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4d0889585bd0ac6c4a599ed2027e2df81a3ddd92bf7f7ee4d6794a50e3d469f4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:29:subtheme:1 · paragraphs 900-900

- Raw key terms: `avoid, collateral, considered, court, debate, determined, e-17, evidence`
- Display key terms: `avoid, collateral, considered, debate, determined, e-17`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: avoid, collateral, considered, debate, determined, e-17 Evidence spans paragraphs 900-900. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041145` offsets `156-161`; context: Simply to avoid any further collateral debate on this issue, the Court found that this evidence was not necessary to make the findings relevant to the issues to be determined.
- Evidence: `evidence_fact` cue `found that` at chunk `5041145` offsets `173-183`; context: Simply to avoid any further collateral debate on this issue, the Court found that this evidence was not necessary to make the findings relevant to the issues to be determined.

#### Section text

[16] The paragraphs objected to in E-17 (see TX-343; TX-344) were not considered by the Court at all. Simply to avoid any further collateral debate on this issue, the Court found that this evidence was not necessary to make the findings relevant to the issues to be determined.

## 22183:30 · paragraphs 901-912

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `826273ffefd800077c227cb48fb16f64ebefecc40c85f8dca908639ad964595c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:30:subtheme:1 · paragraphs 901-904

- Raw key terms: `court, addressee, adopted, although, amides, apotex, appears, april`
- Display key terms: `addressee, adopted, although, amides, apotex, appears, april`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: addressee, adopted, although, amides, apotex, appears, april Rule/authority context: Barrett was working, as of 1976, under the supervision of a posita – Sir Derek Barton – and he studied cephalosporin chemistry earlier in the 1970s (see examination of Dr. Application context: But given that neither Apotex nor Lilly raised this issue in respect of both experts maybe because of their particular knowledge of phosphorus compounds, the Court gave some weight to their evidence. Evidence spans paragraphs 901-904. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041147` offsets `196-201`; context: But given that neither Apotex nor Lilly raised this issue in respect of both experts maybe because of their particular knowledge of phosphorus compounds, the Court gave some weight to their evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041147` offsets `334-342`; context: But given that neither Apotex nor Lilly raised this issue in respect of both experts maybe because of their particular knowledge of phosphorus compounds, the Court gave some weight to their evidence.
- Evidence: `reasoning_application` cue `because` at chunk `5041147` offsets `235-242`; context: But given that neither Apotex nor Lilly raised this issue in respect of both experts maybe because of their particular knowledge of phosphorus compounds, the Court gave some weight to their evidence.
- Evidence: `governing_rule` cue `under` at chunk `5041148` offsets `182-187`; context: Barrett was working, as of 1976, under the supervision of a posita – Sir Derek Barton – and he studied cephalosporin chemistry earlier in the 1970s (see examination of Dr.

#### 22183:30:subtheme:2 · paragraphs 905-912

- Raw key terms: `apotex, para, fact, hanessian, lilly, made, necessary, patents`
- Display key terms: `apotex, para, fact, hanessian, lilly, made, necessary, patents`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: apotex, para, fact, hanessian, lilly, made, necessary, patents Application context: Baldwin made these comments while discussing the Lilly process patents, they obviously apply more generally. Evidence spans paragraphs 905-912. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5041150` offsets `207-213`; context: Hanessian and Barrett (A-20 and E-15, respectively), the weight of the evidence of those two experts in respect of issues within their expertise, has not been diminished by the fact that they accepted to opine on matters on which it is not clear they had the necessary expertise (manufacturing practices).
- Evidence: `evidence_fact` cue `evidence` at chunk `5041150` offsets `163-171`; context: Hanessian and Barrett (A-20 and E-15, respectively), the weight of the evidence of those two experts in respect of issues within their expertise, has not been diminished by the fact that they accepted to opine on matters on which it is not clear they had the necessary expertise (manufacturing practices).
- Evidence: `evidence_fact` cue `Affidavit` at chunk `5041155` offsets `30-39`; context: [26] See, among other things, Affidavit of Dr.
- Evidence: `reasoning_application` cue `apply` at chunk `5041156` offsets `172-177`; context: Baldwin made these comments while discussing the Lilly process patents, they obviously apply more generally.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5041156` offsets `72-80`; context: Although Dr.

#### Section text

[17] A. Spaggiari, L.C. Blaszczak & F. Prati, “Low-Temperature Deacylation of N-Monosubstituated Amides” (2004) 6 Organic Letters 3885.

[18] This appears to be in direct contradiction with the description of the addressee of the ‘007 patent adopted by Apotex in their memorandum. But given that neither Apotex nor Lilly raised this issue in respect of both experts maybe because of their particular knowledge of phosphorus compounds, the Court gave some weight to their evidence.

[19] Although the Court is not persuaded that either expert qualified as posita in the 1970s, they certainly qualified shortly thereafter. Also, Dr. Barrett was working, as of 1976, under the supervision of a posita – Sir Derek Barton – and he studied cephalosporin chemistry earlier in the 1970s (see examination of Dr. Barrett, April 22, 2009, p. 15, lines 18-23 and p. 19, lines 1-19).

[20] Cross-examination of Dr. Olah, June 24, 2008, p. 92, line 18 to p. 93, line 1. Unlike Dr. McClelland and Dr. Chivers, Dr. Olah does not say in his report that a difference of more than one ppm means different kinetic complexes.

[21] Given the very special circumstances surrounding the filing of the two reports of Drs. Hanessian and Barrett (A-20 and E-15, respectively), the weight of the evidence of those two experts in respect of issues within their expertise, has not been diminished by the fact that they accepted to opine on matters on which it is not clear they had the necessary expertise (manufacturing practices).

[22] Here it appears that nobody at Apotex verified if any such changes were necessary despite the fact that Apotex knew that Lupin was bound to change its process by contract.

[23] Apotex did not explain how this would make any sense in respect of the Lilly patents, simply stating that Lilly and Lilly Canada “muffed up” when they made this amendment and must suffer the consequences.

[24] See Whirlpool at para. 45, and Free World Trust at para. 31(e).

[25] 4th ed. (Toronto: Carswell, 1969) at 219.

[26] See, among other things, Affidavit of Dr. Hanessian (A-10; A-15), para. 7; Affidavit of Dr. Martin (A-17), para. 12; Apotex’s memorandum on infringement, para. 172.

[27] See transcript of April 28, 2008, p. 231 line 23 to p. 232 line 4. Although Dr. Baldwin made these comments while discussing the Lilly process patents, they obviously apply more generally.

[28] For Dr. Olah, see A-19, para. 8 and for Dr. McClelland, see A-12, para. 7. See also Dr. Chivers (A-18) at para. 6.

## 22183:31 · paragraphs 913-919

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `bd7cb25ba29fd66fb224ef65edbbdf41c4a201231c6f9961455413a21c8ef7ea`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:31:subtheme:1 · paragraphs 913-919

- Raw key terms: `case, claim, court, infringement, specifically, another, apotex, appeal`
- Display key terms: `case, infringement, specifically, another, apotex`
- Argument roles: `evidence_fact`
- Explanation: Observed roles: evidence_fact Display terms: case, infringement, specifically, another, apotex Evidence spans paragraphs 913-919. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041160` offsets `169-177`; context: [31] No explanation was given for this, even if the Court had expressed its keen interest in hearing his version of the events that will be discussed when reviewing the evidence in respect of infringement of the Lupin material and voir dire.

#### Section text

[29] See Apotex memorandum on infringement at para. 120.

[30] In Generics (UK) Ltd. v. Daiichi Pharmaceutical Co. Ltd. & another, [2009] EWCA Civ 646 (Daiichi), at paras. 23-28, the Court of Appeal of England and Wales also felt the need to review the law as to the common general knowledge of the posita.

[31] No explanation was given for this, even if the Court had expressed its keen interest in hearing his version of the events that will be discussed when reviewing the evidence in respect of infringement of the Lupin material and voir dire.

[32] Who only had expertise in lactams, not β-lactams.

[33] In the case of claims 4 and 13, specifically the TPP.

[34] In the case of claim 4, Cl only.

[35] In the case of claim 17, specifically an aromatic or halogenated hydrocarbon solvent.

## 22183:32 · paragraphs 920-931

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `21f45a426fdfb7bc125471453b3384563369de944a3da551df56557435e0a8a5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:32:subtheme:1 · paragraphs 920-931

- Raw key terms: `evidence, claim, nature, patent, phosphite, table, affidavit, although`
- Display key terms: `nature, patent, phosphite, table, affidavit, although`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: nature, patent, phosphite, table, affidavit, although Application context: [36] Although Apotex focused its argument only on the 31P NMR shift given for this kinetically controlled product in methylene chloride (CH2Cl2), its position should in theory apply to all the other characteristics (exce | [44] Because the unstable or transient nature of the claimed compound is already conveyed by the reference to the kinetically controlled product, which is defined as the fastest forming compound of the reaction, as well  Evidence spans paragraphs 920-931. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `apply` at chunk `5041165` offsets `176-181`; context: [36] Although Apotex focused its argument only on the 31P NMR shift given for this kinetically controlled product in methylene chloride (CH2Cl2), its position should in theory apply to all the other characteristics (except half-life) found in table 1 for the kinetically controlled product and included claim 6.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041167` offsets `26-34`; context: [38] This prior art is in evidence here, the proper citations (and exhibit numbers) being D.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041168` offsets `9-17`; context: [39] The evidence does not establish that the person skilled in the art would understand the general formula with a ● or this reference to a cationic character to mean that the formula limits the nature of the chemical bonding between the triaryl phosphite and the halogens in any particular way or that it limits itself to a particular covalent form or ionic form or a particular equilibrium mixture, if any.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `5041169` offsets `21-30`; context: 10 of Affidavit of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041170` offsets `748-756`; context: 7 and -22 ppm will be used throughout the evidence presented to the Court.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041171` offsets `217-226`; context: 124, line 17), see also the affidavit of Dr.
- Evidence: `reasoning_application` cue `Because` at chunk `5041173` offsets `5-12`; context: [44] Because the unstable or transient nature of the claimed compound is already conveyed by the reference to the kinetically controlled product, which is defined as the fastest forming compound of the reaction, as well as the ● in the formulas included in various claims, there is no mention of the half-life in any of these claims.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041175` offsets `50-58`; context: [46] Having particularly reviewed and weighed the evidence singled out by Apotex in the footnotes of their memorandum and during their oral arguments, the Court notes, among other things, that not all of this evidence can be given weight or can even be considered for the purpose of construction.

#### Section text

[36] Although Apotex focused its argument only on the 31P NMR shift given for this kinetically controlled product in methylene chloride (CH2Cl2), its position should in theory apply to all the other characteristics (except half-life) found in table 1 for the kinetically controlled product and included claim 6.

[37] See claim 1.

[38] This prior art is in evidence here, the proper citations (and exhibit numbers) being D.G. Coe, S.R. Landauer & H.N. Rydon, “The Organic Chemistry of Phosphorous. Part II.* The Action of Triphenyl Phosphite Dihalides on Alcohols: Two Further New Methods for the Preparation of Alkyl Halides.” (1954) J. Chem. Soc. 2281 (TX-1562, hereinafter “Coe”) and H.N. Rydon & B.L. Tonge, “The Organic Chemistry of Phosphorus. Part III.* The Nature of the Compounds of Triaryl Phosphites and the Halogens.” (1956) J. Chem. Soc. 3043 (TX-1564, hereinafter “Rydon”).

[39] The evidence does not establish that the person skilled in the art would understand the general formula with a ● or this reference to a cationic character to mean that the formula limits the nature of the chemical bonding between the triaryl phosphite and the halogens in any particular way or that it limits itself to a particular covalent form or ionic form or a particular equilibrium mixture, if any.

[40] See para. 10 of Affidavit of Dr. Baldwin (E-19).

[41] See the note at the bottom of Table 1, p. 8 of the ‘007 patent. In the patent and in some of the prior art, such as the articles by Ramirez (F. Ramirez, A.J. Bigler & C.P. Smith, "Pentaphenoxyphosphorane" (1968) 90 J. Am. Chem. Soc. 3507 (TX-1596)), Tseng (Chien K. Tseng, “Reinvestigation of Diahalotriphenoxyphosphoranes” (1979), 44 J. Org. Chem. 2793 (TX-1764C)) and Michalski (Jan Michalski, Marek Pakulski & Aleksandra Skowroński, “Reaction of Triphenyl Phosphite with Elemental Bromine and Chlorine” (1980) 45 J. Org. Chem. 3122 (TX-1764D)), the authors used an old convention and refer to -3.7 or -7 or -4.5 and +22. Since then, the convention has changed and in this judgment the figure of +3.7 and -22 ppm will be used throughout the evidence presented to the Court.

[42] Dr. McClelland testified that he was surprised that the 31P NMR shift was the same and felt this to be inconsistent (Examination of Dr. McClelland, May 27, 2008, p. 123, line 18 to p. 124, line 17), see also the affidavit of Dr. Chivers (A-18), para. 22).

[43] Once again Table 1, p. 8 of the patent refers to +22.7 ppm but, as noted above, this convention was changed and the new convention is adopted in these reasons.

[44] Because the unstable or transient nature of the claimed compound is already conveyed by the reference to the kinetically controlled product, which is defined as the fastest forming compound of the reaction, as well as the ● in the formulas included in various claims, there is no mention of the half-life in any of these claims.

[45] See William L. Hayhurst, Q.C., “The Art of Claiming and Reading a Claim” in Gordon F. Henderson et al., eds., Patent Laws of Canada (Scarborough: Carswell, 1994) 177 (Hayhurst).

[46] Having particularly reviewed and weighed the evidence singled out by Apotex in the footnotes of their memorandum and during their oral arguments, the Court notes, among other things, that not all of this evidence can be given weight or can even be considered for the purpose of construction. Certainly, explanations as to the subjective understanding of the inventor are not relevant. This is particularly so when the Court is not even satisfied that the quotes referred to (see exhibit A-16 – extracts of Blaszczak discovery) are properly used or understood.

[47] Although this is a somewhat surprising statement, see cross-examination of Dr. McClelland, May 12, 2008, p. 149, lines 14-18, this passage was specifically referred to in Lilly’s closing arguments and no request for amendment was made in that respect. It corroborates the statement in the disclosure that this is a term of the art.

## 22183:33 · paragraphs 932-936

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e805eecadb72848dc557025515a34ab5a122ccbcb5b672a50e84c72e44c53d6b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:33:subtheme:1 · paragraphs 932-936

- Raw key terms: `lines, mcclelland, cross-examination, line, patent, a-12, absolutely, affidavit`
- Display key terms: `lines, mcclelland, cross-examination, line, patent, a-12, absolutely, affidavit`
- Argument roles: `evidence_fact`
- Explanation: Observed roles: evidence_fact Display terms: lines, mcclelland, cross-examination, line, patent, a-12, absolutely, affidavit Evidence spans paragraphs 932-936. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041178` offsets `246-255`; context: It is interesting that in his affidavit on validity (A-12), Dr.

#### Section text

[48] Cross-examination of Dr. McClelland, May 12, 2008, p. 158, lines 4-8.

[49] As did Apotex’s counsel in their cross-examination of Lilly’s experts. Dr. McClelland agreed that chemical shift values at +6 ppm indicates the presence of the kinetically controlled product claimed in claim 1. It is interesting that in his affidavit on validity (A-12), Dr. McClelland states at para. 38, “[t]he negative signal at -6.3 ppm is clearly due to the unstable “kinetic product” claimed as being a novel compound in the ‘007 patent. The peaks at +22 to +23 that grow in as this unstable compound reacts are clearly the thermodynamic product.” In that respect, he appears to have absolutely no difficulty understanding claim 1 and applying it to a kinetic complex, which is not characterized by a signal at +3.7 ppm.

[50] See p. 5, lines 1 and 2: “are used synonymously and likewise are to be distinguished from those triaryl phosphite dihalides of the prior art”.

[51] See also examination in-chief of Dr. McClelland, May 8, 2008, p. 174, line 25 to p. 176 line 18.

[52] See ‘007 patent p. 2, line 25 to p. 3, line 14; p. 4, lines 20-28; p. 7, lines 18-21; and, p. 9, lines 1-5.

## 22183:34 · paragraphs 937-952

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `25ce948ce769371888b9197f1a2ff02810a60bdd403f037c2e0553d28dd02574`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:34:subtheme:1 · paragraphs 937-943

- Raw key terms: `affidavit, evidence, abandoned, although, amend, amount, apotex, appears`
- Display key terms: `affidavit, abandoned, although, amend, amount, apotex, appears`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: affidavit, abandoned, although, amend, amount, apotex, appears Application context: [55] Were it not for the (●) in the general formula and the reference to kinetically controlled products, these words, per se, could apply to the thermodynamic compounds or the so-called prior art triaryl phosphite dihal Evidence spans paragraphs 937-943. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041182` offsets `9-18`; context: [53] His affidavit, E-11, and all evidence relating thereto have not been considered.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041183` offsets `26-34`; context: [54] It is clear from the evidence of Dr.
- Evidence: `reasoning_application` cue `apply` at chunk `5041184` offsets `133-138`; context: [55] Were it not for the (●) in the general formula and the reference to kinetically controlled products, these words, per se, could apply to the thermodynamic compounds or the so-called prior art triaryl phosphite dihalides.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `5041188` offsets `174-183`; context: [59] This is the one pot (one reaction) process where the kinetic complex is used to sequentially modify the groups at positions 1, 3, and 7 of the cephalosporin system (see Affidavit of Dr.

#### 22183:34:subtheme:2 · paragraphs 944-946

- Raw key terms: `appears, arguments, characteristics, claims, construction, court, cross-examination, dealt`
- Display key terms: `appears, arguments, characteristics, claims, construction, cross-examination, dealt`
- Argument roles: `issue, party_position`
- Explanation: Observed roles: issue, party_position Display terms: appears, arguments, characteristics, claims, construction, cross-examination, dealt Position/evidence statements: [60] The parties did not present any arguments in respect of the construction of claims 18 and 34, particularly as to whether or not the specific characteristics described therein would be essential elements of those cla Evidence spans paragraphs 944-946. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5041189` offsets `118-125`; context: [60] The parties did not present any arguments in respect of the construction of claims 18 and 34, particularly as to whether or not the specific characteristics described therein would be essential elements of those claims.
- Evidence: `party_position` cue `claims` at chunk `5041189` offsets `81-87`; context: [60] The parties did not present any arguments in respect of the construction of claims 18 and 34, particularly as to whether or not the specific characteristics described therein would be essential elements of those claims.

#### 22183:34:subtheme:3 · paragraphs 947-952

- Raw key terms: `compound, disclosure, line, apotex, application, certificate, claims, common`
- Display key terms: `compound, disclosure, line, apotex, certificate, claims, common`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: compound, disclosure, line, apotex, certificate, claims, common Evidence spans paragraphs 947-952. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041192` offsets `35-40`; context: [63] Also Apotex did not raise any issue with respect to the sufficiency of the disclosure.

#### Section text

[53] His affidavit, E-11, and all evidence relating thereto have not been considered.

[54] It is clear from the evidence of Dr. McClelland that in fact a small difference of about 5% in the amount of covalent versus ionic species in the equilibrium represented by the weighted average given by the 31P NMR would explain the distinction between a +3.7 ppm reading and a +7 or +8 ppm reading.

[55] Were it not for the (●) in the general formula and the reference to kinetically controlled products, these words, per se, could apply to the thermodynamic compounds or the so-called prior art triaryl phosphite dihalides.

[56] Although still included in the final version of the statement of defence, during the trial Apotex abandoned the argument it had initially raised in respect of the filing of improper divisional applications. It would certainly be good practice to amend pleadings before trial to ensure that they truly reflect each party’s position.

[57] It appears that all these inventors were part of Lilly’s β-lactam research group.

[58] Also referred to later in these reasons as “one pot”.

[59] This is the one pot (one reaction) process where the kinetic complex is used to sequentially modify the groups at positions 1, 3, and 7 of the cephalosporin system (see Affidavit of Dr. Baldwin (E-6), paras. 64-68).

[60] The parties did not present any arguments in respect of the construction of claims 18 and 34, particularly as to whether or not the specific characteristics described therein would be essential elements of those claims. The Court does not have to make a determination in that respect, given that the Court only needs to find that one of the claims is infringed for Lilly to succeed. For reasons that will be explained later on, the Court is satisfied that other claims were infringed, there is thus no need to discuss claims 18 and 34 any further.

[61] The expression “improved processes” is used here in the sense of s. 2 of the Patent Act where “invention” is defined. It is not referring to an “improvement” of a patented process dealt with at s. 32 of the Act.

[62] It appears, however, that Dr. Hanessian failed to realize this even after having examined the patents (cross-examination of Dr. Hanessian, May 15, 2008, p. 76 line 25 to p. 84 line 13).

[63] Also Apotex did not raise any issue with respect to the sufficiency of the disclosure.

[64] It should be noted that this is likely a rough translation of the Japanese application.

[65] Other parts of this common disclosure in effect concern only one of the patents: p. 8, lines 5-15 (‘026); p. 9, line 21 (‘026); p. 10, lines 19-20 (‘026); p. 14, lines 25-29 (‘026); p. 15, lines 15-17 (‘547); p. 15, lines 17-19 (‘924); p. 15, line 23 to p. 18, line 6 (‘132); p. 18, line 7 to p. 23, line 11 (‘026); p. 23, line 21 to p. 35, line 12 (‘547); p. 35, line 13 to p. 47, line 7 (‘132); p. 51, line 1 to p. 66, line 26 (‘026); p. 67 (‘026); and, p. 69, line 24 to p. 76 (‘547).

[66] Both the process and compound by process claims include several variants.

[67] Certificate of correction was issued to add the dotted line representing the thiazoline.

[68] Figures A and B represent the same compound, which are in equilibrium between the enol and keto forms.

## 22183:35 · paragraphs 953-953

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7559044ff2a31a1acff862ea5357602688863d48e130d04b9d1130e846b60df4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:35:subtheme:1 · paragraphs 953-953

- Raw key terms: `compound, equilibrium, mixture, represent`
- Display key terms: `compound, equilibrium, mixture, represent`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: compound, equilibrium, mixture, represent No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 953-953. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

[69] Again, C and D represent the same compound or an equilibrium mixture of the two.

## 22183:36 · paragraphs 954-961

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `acfa8a22f262ea06a42c1a251f23f65f24de026e08858d071709b96a6f46c9dd`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:36:subtheme:1 · paragraphs 954-961

- Raw key terms: `apotex, disclosure, line, para, used, according, acid, acids`
- Display key terms: `apotex, disclosure, line, para, used, according, acid, acids`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: apotex, disclosure, line, para, used, according, acid, acids No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 954-961. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

[70] This was confirmed by Dr. Barrett on cross-examination, June 19, 2008, p. 61, lines 9-22.

[71] Ibid., p. 61, line 9 to p. 62, line 10.

[72] It is clear that the acids used to cyclicize include the Lewis acids which will remove R substituents other than H described in the disclosure before proceeding to cyclicize the compounds.

[73] Inasmuch as para. 1 does not expressly refer to the opening of the thiazoline ring when present by the aqueous acid used to treat the enamine, there was no need to refer to the removal of any remaining thiol substituent other than H prior to cyclization through the use of appropriate acid. In my view, both would be understood by the posita, especially given the explicit reference to same in the disclosure.

[74] See correspondence from counsel for Lilly dated November 18, 2008 and its reply from counsel for Apotex dated November 25, 2008; argument in chief of counsel for Apotex, October 31, 2008, p. 161, line 2-19; p. 179, line 22 to p. 180, line 3; argument in reply of counsel for Apotex, November 4, 2008, p. 69, line 5 to p. 70, line 5.

[75] According to s. 78.2 of the Patent Act, it appears that the version of its s. 55.1 amended by s. 193 of the North American Free Trade Agreement Implementation Act, S.C. 1993, c. 44 is applicable to patents issued before 1989.

[76] See Facts agreed to by the parties, LRTA # 44(e).

[77] See para. 239 of Apotex's memorandum on infringement; the Court does not agree that SmithKline Beecham Pharma Inc. v. Apotex Inc. (2001), 267 N.R. 101, 10 C.P.R. (4th) 338 (F.C.A.), at para. 33 or Pfizer Canada Inc. v. Apotex Inc., 2003 FC 1428, 245 F.T.R. 243, at para. 15, stand for this proposition.

## 22183:37 · paragraphs 962-962

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4ad86bff995a691518f1c14dfc55bb9c70226b796bd16845edec667b00904096`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:37:subtheme:1 · paragraphs 962-962

- Raw key terms: `lilly, memorandum, para`
- Display key terms: `lilly, memorandum, para`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: lilly, memorandum, para No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 962-962. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

[78] See Lilly memorandum, para. 102.

## 22183:38 · paragraphs 963-991

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0ec93ebf21eeb76db287daf18169e148d6a4a740aff7e5150d53a6e01d215157`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:38:subtheme:1 · paragraphs 963-991

- Raw key terms: `apotex, court, process, lilly, although, counsel, evidence, kyong`
- Display key terms: `apotex, process, lilly, although, kyong`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application Display terms: apotex, process, lilly, although, kyong Rule/authority context: 184, where Lord Justice Patrick Russell, on behalf of the English Court of Appeal, said “[i]n our judgment, this extension of the principles laid down in Elmslie v. Application context: All the parties confirmed that these agreed facts applied to both the main action and the counterclaim. | [102] It also applies to the Lilly patents but as discussed in respect of those patents, Apotex also vigorously contested that its supplier used the patented processes abroad. Operative outcome context: [91] For this reason, the Court did not consider the portions of E-15 dealing with the viability of Process “E” (objection 61A granted) Evidence spans paragraphs 963-991. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `Record` at chunk `5041208` offsets `40-46`; context: [79] Request to admit LRTA # 115, Trial Record, Tab 24, p.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041210` offsets `31-39`; context: [81] The Court disregarded the evidence based on the Ladas & Parry letter (June 12, 1996) which was not entered in evidence.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041213` offsets `82-91`; context: [84] Lilly’s motion included a request for the production of a better and further affidavit including documentation regarding the processes by which Apotex’s cefaclor was manufactured but it appears that this request was abandoned upon Apotex’s undertaking to look for whatever additional documentation within its power, possession and control fell in certain categories described in the Order.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041218` offsets `45-53`; context: [89] Despite the Court urging that they file evidence to explain the non-filing of the letter, Apotex’s counsel only provided a verbal explanation – a secretary in the counsel office filed the letter thinking that it had been seen by the lawyers concerned.
- Evidence: `disposition` cue `granted` at chunk `5041220` offsets `127-134`; context: [91] For this reason, the Court did not consider the portions of E-15 dealing with the viability of Process “E” (objection 61A granted)
- Evidence: `evidence_fact` cue `Record` at chunk `5041224` offsets `39-45`; context: [95] Request to admit LRTA # 84, Trial Record, Tab 24, p.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041227` offsets `28-36`; context: [98] Lilly objected to this evidence on the basis that it constitutes double hearsay and, although Ms.
- Evidence: `reasoning_application` cue `applied` at chunk `5041229` offsets `104-111`; context: All the parties confirmed that these agreed facts applied to both the main action and the counterclaim.
- Evidence: `reasoning_application` cue `applies` at chunk `5041231` offsets `14-21`; context: [102] It also applies to the Lilly patents but as discussed in respect of those patents, Apotex also vigorously contested that its supplier used the patented processes abroad.
- Evidence: `evidence_fact` cue `found that` at chunk `5041232` offsets `43-53`; context: [103] The first English case where a Court found that a defendant had infringed an English patent covering a process for making an intermediate compound (ortho-toluene-sulpho-chloride) when it imported and sold in England a final product (saccharin) manufactured abroad.
- Evidence: `governing_rule` cue `principles` at chunk `5041232` offsets `499-509`; context: 184, where Lord Justice Patrick Russell, on behalf of the English Court of Appeal, said “[i]n our judgment, this extension of the principles laid down in Elmslie v.
- Evidence: `counterargument_limitation` cue `however` at chunk `5041232` offsets `604-611`; context: (We should however mention in passing that the reference to ortho-toluene-sulpho-chloride being “contained in” saccharin at p.

#### Section text

[79] Request to admit LRTA # 115, Trial Record, Tab 24, p. 34.

[80] See TX-1671 and TX-1654.

[81] The Court disregarded the evidence based on the Ladas & Parry letter (June 12, 1996) which was not entered in evidence. Thus, I have decided not to make any conclusions with respect to claim 6 which deals with specific halogen scavengers having a six-ring carbon atoms such as cyclohexene.

[82] An experiment by Dr. Modro also confirms that the thermodynamic product could not perform these reactions.

[83] See also Dr. Miller’s report (E-3).

[84] Lilly’s motion included a request for the production of a better and further affidavit including documentation regarding the processes by which Apotex’s cefaclor was manufactured but it appears that this request was abandoned upon Apotex’s undertaking to look for whatever additional documentation within its power, possession and control fell in certain categories described in the Order.

[85] At one such session, Ivor Hughes was present.

[86] In fact, Lupin’s counsel was present at the hearing on July 5, 2000.

[87] It appears that Lupin did not keep its manufacturing data for more than two years after the production of the material.

[88] Some papers were recovered and an attempt was made to reconstruct part of those files.

[89] Despite the Court urging that they file evidence to explain the non-filing of the letter, Apotex’s counsel only provided a verbal explanation – a secretary in the counsel office filed the letter thinking that it had been seen by the lawyers concerned. Unfortunately, Mr. Sarkis, from Ivor Hughes office, was deleted from Apotex’s list of witnesses.

[90] Although it is clear that the manufacturing plant documentation was destroyed, it has not been established to my satisfaction that there was no relevant documents in the files of the R&D department.

[91] For this reason, the Court did not consider the portions of E-15 dealing with the viability of Process “E” (objection 61A granted)

[92] Two reagents for two-pot process instead of three reagents and a three-pot process.

[93] Given that it started from Pen V.

[94] Given the exculpatory nature of the schematic outline attached to the July 4, 2000 letter, Lilly proposed an explanation that the Court cannot accept for it is purely speculative.

[95] Request to admit LRTA # 84, Trial Record, Tab 24, p. 33.

[96] Cross-examination of Dr. Hanessian, May 15, 2008, p. 163, line 1 to p. 164, line 8.

[97] In addition to the presumption of good faith, Kyong Bo was legally obliged to disclose the process it used to produce the cefaclor sold in Canada and had to update its file in that respect whenever changes were to be made.

[98] Lilly objected to this evidence on the basis that it constitutes double hearsay and, although Ms. Fouillade is deceased, there is no evidence that a person with personal knowledge from Kyong Bo, such as Seung-Ho An, could not testify.

[99] Although it would not be sufficient in law to prove that Apotex believed that Kyong Bo had a licence, the Court is not satisfied that Apotex has even established that much.

[100] See Facts agreed to by the parties, ARTA # 295. All the parties confirmed that these agreed facts applied to both the main action and the counterclaim.

[101] More than 30 pages were devoted to this argument in Apotex’s memorandum and it was the one argument on which Apotex’s counsel spent the most time in its oral argument.

[102] It also applies to the Lilly patents but as discussed in respect of those patents, Apotex also vigorously contested that its supplier used the patented processes abroad.

[103] The first English case where a Court found that a defendant had infringed an English patent covering a process for making an intermediate compound (ortho-toluene-sulpho-chloride) when it imported and sold in England a final product (saccharin) manufactured abroad. See also Beecham Group Ltd. v. Bristol Laboratories Ltd., [1978] RPC 153, [1977] F.S.R. 215 at p. 184, where Lord Justice Patrick Russell, on behalf of the English Court of Appeal, said “[i]n our judgment, this extension of the principles laid down in Elmslie v. Boursier and Von Heyden v. Neustadt was sound and correct. (We should however mention in passing that the reference to ortho-toluene-sulpho-chloride being “contained in” saccharin at p. 319, line 3, is a loose phrase, in that, after the further chemical reaction, it did not have a separate existence in terms of its chemical structure, as Buckley, J. plainly appreciated.)”

[104] To this effect, Apotex cites Brown v. Duchesme, 60 U.S. 183, 15 L. Ed. 595 (1856); Dowagiac Mfg. Co. v. Minnesota Moline Plow Co., 235 U.S. 641, 35 S. Ct. 221 (1915); Deepsouth Packing Co. v. Laitram Corp., 406 U.S. 518, 92 S. Ct. 1700 (1972); and, Microsoft Corp. v. AT&T Corp., 550 U.S. 437, 127 S. Ct. 1746 (2007).

[105] 5 October 1973, subs. 64(2).

[106] Process Patent Amendment Act, 35 U.S.C. § 271(g).

[107] See footnote 11 of Apotex’s memorandum on infringement.

## 22183:39 · paragraphs 992-992

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fbb60ea3c9cc686357f38ba1830ee24d582e833ed07017012a654dca0c60bf81`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:39:subtheme:1 · paragraphs 992-992

- Raw key terms: `abandoned, apotex, appeal, court, decision, dismissed, following, however`
- Display key terms: `abandoned, apotex, dismissed, following, however`
- Argument roles: `counterargument_limitation, disposition`
- Explanation: Observed roles: counterargument_limitation, disposition Display terms: abandoned, apotex, dismissed, following, however Operative outcome context: The Court notes that Apotex did try to intervene in the appeal of Justice Snider’s decision, however, their motion was dismissed and the appeal was ultimately abandoned. Evidence spans paragraphs 992-992. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `however` at chunk `5041237` offsets `167-174`; context: The Court notes that Apotex did try to intervene in the appeal of Justice Snider’s decision, however, their motion was dismissed and the appeal was ultimately abandoned.
- Evidence: `disposition` cue `dismissed` at chunk `5041237` offsets `193-202`; context: The Court notes that Apotex did try to intervene in the appeal of Justice Snider’s decision, however, their motion was dismissed and the appeal was ultimately abandoned.

#### Section text

[108] See para. 104 and following of Apotex’s memorandum on infringement. The Court notes that Apotex did try to intervene in the appeal of Justice Snider’s decision, however, their motion was dismissed and the appeal was ultimately abandoned.

## 22183:40 · paragraphs 993-1002

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9d6a1e91df24e2dfd89e48f3fd88e3cdca8437085b52fbc9aaa3f083f0cafc97`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:40:subtheme:1 · paragraphs 993-997

- Raw key terms: `made, process, apotex, justice, lord, patent, patented, patentee`
- Display key terms: `made, process, apotex, justice, lord, patent, patented, patentee`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: made, process, apotex, justice, lord, patent, patented, patentee Evidence spans paragraphs 993-997. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5041239` offsets `145-152`; context: [110] In this decision, it is interesting to note that Lord Atkinson, while concurring with the majority, wrote separate reasons with respect to whether to construe the exclusive right or privilege of the patentee in a process patent, as to include the exclusive right to sell articles made by others situated elsewhere.

#### 22183:40:subtheme:2 · paragraphs 998-1002

- Raw key terms: `claim, process, agreement, among, annex, apotex, appears, april`
- Display key terms: `process, agreement, among, annex, apotex, appears, april`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: process, agreement, among, annex, apotex, appears, april Operative outcome context: [114] It should be noted that among all the judges confronted with these issues, President Jackett appears to have been the most sympathetic to arguments similar to those raised by Apotex in respect of territoriality and Evidence spans paragraphs 998-1002. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5041243` offsets `73-79`; context: [114] It should be noted that among all the judges confronted with these issues, President Jackett appears to have been the most sympathetic to arguments similar to those raised by Apotex in respect of territoriality and the limited monopoly granted by a process claim.
- Evidence: `disposition` cue `granted` at chunk `5041243` offsets `242-249`; context: [114] It should be noted that among all the judges confronted with these issues, President Jackett appears to have been the most sympathetic to arguments similar to those raised by Apotex in respect of territoriality and the limited monopoly granted by a process claim.

#### Section text

[109] Apotex suggests that this has in fact never occurred and that there is a need for a thorough analysis.

[110] In this decision, it is interesting to note that Lord Atkinson, while concurring with the majority, wrote separate reasons with respect to whether to construe the exclusive right or privilege of the patentee in a process patent, as to include the exclusive right to sell articles made by others situated elsewhere. This entails that the arguments now proposed by Apotex were considered by the Lordships before they rendered their majority decision confirming the Court of Appeal.

[111] The example referred to at trial was the use of a hammer made according to a patented process for the assembly of a railway car could be found to be infringing. In Pfizer, Justice Snider referred to the use of patented scissors to cut the cloth of an Italian suit imported into Canada.

[112] The grant and prohibition is summarized by Lord Diplock as follows: “The grant is of “full power, sole privilege and authority” to “make, use, exercise and vend the said invention within our United Kingdom…” and to “have and enjoy the whole profit and advantage from time to time accruing by reason of the said invention.” The corresponding prohibition is the observation of the grant. It is expressed to be imposed “that the patentee may have and enjoy the sole use and exercise and the full benefit of the invention…”; and commands all Her Majesty’s subjects in the United Kingdom “that they do not at any time … either directly or indirectly make use of or put in practice the said invention nor in anywise imitate the same.”” (p.198).

[113] This was very clearly interpreted by Justice Noël in American Cyanamid Co. c. Charles E. Frosst & Co., [1965] 2 Ex.C.R. 355, 47 C.P.R. 215 (American Cyanamid Co.), at para. 40, as meaning that the sale of a product made in accordance with a patented process would infringe a process patent even though the patent contained no claim to the product.

[114] It should be noted that among all the judges confronted with these issues, President Jackett appears to have been the most sympathetic to arguments similar to those raised by Apotex in respect of territoriality and the limited monopoly granted by a process claim.

[115] This was the only product covered by a Canadian patent. But, by the time it was imported into Canada, it had been transformed into tetracycline.

[116] See paras. 55-57.

[117] Annex 1C of the Marrakesh Agreement Establishing the World Trade Organization, 15 April 1994.

[118] Given that Kyong Bo infringed at least one claim in each of the Shionogi patents, the Court will simply use the expression “Shionogi process” to refer to all these infringed claims in each of the patents.

## 22183:41 · paragraphs 1003-1010

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `dd18cd04fc4128f17d2064de95fe4dfac75618da72ee9aadc82b0324153d48fb`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:41:subtheme:1 · paragraphs 1003-1009

- Raw key terms: `court, apotex, lupin, make, patent, process, satisfied, versus`
- Display key terms: `apotex, lupin, make, patent, process, satisfied, versus`
- Argument roles: `counterargument_limitation, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, reasoning_application Display terms: apotex, lupin, make, patent, process, satisfied, versus Application context: We therefore conclude that the patent is valid. Evidence spans paragraphs 1003-1009. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `although` at chunk `5041248` offsets `238-246`; context: It is important to note here that although the Court is satisfied that claim 17 of the ‘007 patent was infringed, this finding is not very relevant here given that the infringement of the process patents per se is sufficient.
- Evidence: `reasoning_application` cue `therefore` at chunk `5041254` offsets `348-357`; context: We therefore conclude that the patent is valid.

#### 22183:41:subtheme:2 · paragraphs 1010-1010

- Raw key terms: `appeal, applicable, arguments, canada, case, chief, college, comments`
- Display key terms: `applicable, arguments, case, chief, college, comments`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: applicable, arguments, case, chief, college, comments Rule/authority context: On the other hand, the standard of review applicable to an appeal under s. Evidence spans paragraphs 1010-1010. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041255` offsets `105-110`; context: [126] It is worth mentioning that none of the parties in Wellcome (2002) presented any arguments on this issue.
- Evidence: `governing_rule` cue `standard of review` at chunk `5041255` offsets `135-153`; context: On the other hand, the standard of review applicable to an appeal under s.

#### Section text

[119] Here again the Court will use the expression “the Lilly process” given that the Lupin process infringes all of the Lilly process patents including particularly the ‘536 patent (triple combination). It is important to note here that although the Court is satisfied that claim 17 of the ‘007 patent was infringed, this finding is not very relevant here given that the infringement of the process patents per se is sufficient. In fact, infringement of the ‘536 patent would be sufficient to support the Court’s reasoning here.

[120] Both the Kyong Bo and Lupin processes have been described by the experts in a variety of depictions, more or less grouping various chemical reactions. For example, see, for the Kyong Bo process, TX-129, the closed portion of Kyong Bo’s DMF, versus the one in the Kyong Bo process chart (W-18).

[121] To make the cefaclor shipped to Apotex as of June, 1998.

[122] Using either the prices of $840 and $1250 per kg or the disputed invoice prices of $1070 versus $1500 per kg (see TX-1671; TX-1759; TX-1050; TX-1062; TX-1082; TX-1105; TX-1123; TX-1126; TX-1131; TX-1134; TX-1137; TX-1144; TX-1151; TX-1156; TX-1161; TX-1166; TX-1171; TX-1180; TX-1193).

[123] Such as samples to pharmacists or doctors.

[124] The Court is not satisfied that the details of the quantities were sufficiently explored during the trial for it to make a final determination in this respect.

[125] See also Monsanto Canada Inc., where the Supreme Court of Canada held: “Monsanto’s patent has already been issued, and the onus is thus on Schmeiser to show that the Commissioner erred in allowing the patent: Apotex Inc. v. Wellcome Foundation Ltd., [2002] 4 S.C.R. 153, 2002 SCC 77, at paras. 42-44. He has failed to discharge that onus. We therefore conclude that the patent is valid.” (para. 24)

[126] It is worth mentioning that none of the parties in Wellcome (2002) presented any arguments on this issue. On the other hand, the standard of review applicable to an appeal under s. 42 was the subject of debate in Harvard College (2002). It was an issue on which the majority of the Federal Court of Appeal and the dissenting Chief Justice Julius Isaac disagreed. (Harvard College v. Canada (Commissioner of Patents) [2000] 4 F.C. 528, 223 F.T.R. 320, (Harvard College (2000)) see paras. 43-63; paras. 179-186). The decision of the Supreme Court of Canada in that case was issued on the same day as its decision in Wellcome (2002). This could explain the Court’s comments in the latter case.

## 22183:42 · paragraphs 1011-1030

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3131206e8d79a6096592babc8f5912e422fa01c0ae9e46a858f89b00cae5efbd`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:42:subtheme:1 · paragraphs 1011-1026

- Raw key terms: `apotex, claim, claims, patent, patents, applications, canada, divisional`
- Display key terms: `apotex, claims, patent, patents, applications, divisional`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, party_position, reasoning_application Display terms: apotex, claims, patent, patents, applications, divisional Position/evidence statements: The Court is also satisfied that the target compounds of claims 31 and 37 (claims 4 and 12 cover the first step) of the ‘924 patent can be used as starting compounds for the process in the ‘132 patent. | , even though there was only one invention, it is evident that the Court was prepared to invalidate the product claims but not the process claims. Application context: [135] No case law was cited to support the principle that two inventions are identical simply because they derive their inventiveness from the same idea. Operative outcome context: The Court even granted a certain delay to the applicant to amend its process claims to take into account what it had decided in respect of the product claims. Evidence spans paragraphs 1011-1026. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `5041257` offsets `388-394`; context: The Court is also satisfied that the target compounds of claims 31 and 37 (claims 4 and 12 cover the first step) of the ‘924 patent can be used as starting compounds for the process in the ‘132 patent.
- Evidence: `counterargument_limitation` cue `however` at chunk `5041257` offsets `171-178`; context: I note, however, that the Court is satisfied that the target compounds of the ‘547 patent can be used as starting compounds for the ‘924 patent, which is not disputed.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041259` offsets `619-628`; context: Murphy’s affidavit (E-20), at paras.
- Evidence: `reasoning_application` cue `because` at chunk `5041264` offsets `94-101`; context: [135] No case law was cited to support the principle that two inventions are identical simply because they derive their inventiveness from the same idea.
- Evidence: `party_position` cue `claims` at chunk `5041268` offsets `153-159`; context: , even though there was only one invention, it is evident that the Court was prepared to invalidate the product claims but not the process claims.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041268` offsets `160-163`; context: , even though there was only one invention, it is evident that the Court was prepared to invalidate the product claims but not the process claims.
- Evidence: `disposition` cue `granted` at chunk `5041268` offsets `203-210`; context: The Court even granted a certain delay to the applicant to amend its process claims to take into account what it had decided in respect of the product claims.

#### 22183:42:subtheme:2 · paragraphs 1027-1030

- Raw key terms: `para, affirmed, anticipation, apotex, appeal, appears, based, binnie`
- Display key terms: `para, affirmed, anticipation, apotex, appears, based, binnie`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: para, affirmed, anticipation, apotex, appears, based, binnie Evidence spans paragraphs 1027-1030. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041272` offsets `202-207`; context: [143] Again, this appears to be based on the notion that the inquiry in respect of anticipation is directed to the patented invention or inventive concept as opposed to what is covered by the claims at issue.

#### Section text

[127] More recently, in Sanofi-Aventis Canada Inc. v. Apotex Inc., 2009 FC 676, at paras. 75-76, Justice Snider noted that the burden on defendants such as Apotex in infringement cases “is not one that can easily be defined by judicial review standards” and that “[f]or the most part, the decision of the Commissioner is simply not relevant to the determination before [her].”

[128] In respect of Dr. McClelland’s views that there exists a disconnect between the various patents, as mentioned, there is no need to discuss it in any detail. I note, however, that the Court is satisfied that the target compounds of the ‘547 patent can be used as starting compounds for the ‘924 patent, which is not disputed. The Court is also satisfied that the target compounds of claims 31 and 37 (claims 4 and 12 cover the first step) of the ‘924 patent can be used as starting compounds for the process in the ‘132 patent. The compounds of claim 58 (made using the process of claim 38) of the ‘132 patent can be used as starting compounds to carry out the reactions covered in the ‘026 patent, which, as mentioned, lead to 3-hydroxy-3-cephem.

[129] See Canada (Commissioner of Patents) v. Farbwerke Hoechst Aktien-Gesellschaft Vormals Meister Lucius & Bruning, [1964] S.C.R. 49 (Farbwerke) where indeed the Commissioner’s decision refusing the filing of divisional applications was the subject of the appeal.

[130] Although Shionogi could have chosen to claim all of the steps in a single application and restrict itself to one patent only, it is evident that it would not have been able to claim the compounds produced by processes that it claims in its divisional applications or to include dependent claims covering each of the steps. It would have been left with a limited monopoly that could easily be designed around. As always, this is the difficult choice that all applicants face when filing amendments required by the Manual of Patent Office Practice (MOPOD) (see Ch. 10 of its 1979 version, discussed in Mr. Murphy’s affidavit (E-20), at paras. 11-22).

[131] See correspondence from counsel for Lilly dated November 18, 2008 and its reply from counsel for Apotex dated November 25, 2008.

[132] As noted, there was no specific statutory provision dealing with obviousness in the old act and Courts used the definition of “invention” to add inventiveness as a requirement to qualify as an invention.

[133] Albeit in a different context, see Laboratoires Servier v. Apotex Inc., 2009 FCA 222, [2009] F.C.J. No. 821 (QL) (Servier (2009)) at para. 69.

[134] In my view, Consolboard (1981) teaches that patents resulting from the forced filing of divisional applications cannot be challenged on the basis of double patenting. This may explain why Apotex abandoned its allegations of double patenting.

[135] No case law was cited to support the principle that two inventions are identical simply because they derive their inventiveness from the same idea.

[136] Riello Canada, Inc. v Lambert (1986), 3 F.T.R. 23, 8 C.I.P.R. 286; Scott Paper Co. v. Minnesota Mining and Manufacturing Co. (1981), 53 C.P.R. (2d) 26, [1981] F.C.J. No. 5 (QL) (T.D.); and, Pfizer Canada Inc. v. Apotex Inc., 2005 FC 1421, 282 F.T.R. 8.

[137] For example, Rule 60(1) of the Patent Regulations (as in force at the time) provided that a patent that does not contain a claim broader in scope than any other claim in the application was deemed to be directed at more than one invention.

[138] Opening statement on validity of counsel for Apotex, June 2, 2008, p. 32 lines 18-22; p. 33 lines 14-23 (Lilly patents); p. 41 lines 14-16 (Shionogi patents).

[139] In Merrell Dow Pharmaceuticals Inc., even though there was only one invention, it is evident that the Court was prepared to invalidate the product claims but not the process claims. The Court even granted a certain delay to the applicant to amend its process claims to take into account what it had decided in respect of the product claims. See also the comments in Servier (2009) at para. 63.

[140] Claim 1 includes all triaryl phosphites mixed with Br or Cl while the prior art document on which Apotex relies only deals with triphenyl phosphite and Cl.

[141] Examination-in-chief of Dr. Baldwin, June 25, 2008, p. 28, line 19 to p. 29, line 1.

[142] As in Abbott (2006), stabilization or maintenance of the compound in solution is not an essential element of any of the claims of the ‘007 patent.

[143] Again, this appears to be based on the notion that the inquiry in respect of anticipation is directed to the patented invention or inventive concept as opposed to what is covered by the claims at issue.

[144] See also Pfizer Canada Inc. v. Apotex Inc., 2008 FCA 8, 72 C.P.R. (4th) 141 at para. 29.

[145] This oft-cited publication was expressly referred to by Justice Ian Binnie in Free World Trust to define common general knowledge at para. 44.

[146] For his review of the law of enablement in Webber v. Vestas-Celtic Wind Technology Ltd., [2007] EWHC 2636 (Pat.) and for having been affirmed by the Court of Appeal of England and Wales, particularly with regard to the “obvious to try” test in Generics (U.K.) Ltd. and others v. H. Lundbeck Als, [2008] EWCA Civ. 311, 101 BMLR 52.

## 22183:43 · paragraphs 1031-1031

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6f4cebddd543c9d92ce458553ff21249d75d6b0ecc60dd962d8575a8fcb721a4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:43:subtheme:1 · paragraphs 1031-1031

- Raw key terms: `appeal, comments, court, daiichi, england, paras, wales`
- Display key terms: `comments, daiichi, england, paras, wales`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: comments, daiichi, england, paras, wales No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 1031-1031. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

[147] See also the Court of Appeal of England and Wales’ comments in Daiichi (at paras. 26-28).

## 22183:44 · paragraphs 1032-1056

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `01b5e2590dae9b4548c28084658d0c0cf614b78467cfc27e713220284bd6d6c2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:44:subtheme:1 · paragraphs 1032-1038

- Raw key terms: `absence, chemistry, date, evidence, filing, invention, presumed, priority`
- Display key terms: `absence, chemistry, date, filing, invention, presumed, priority`
- Argument roles: `counterargument_limitation, evidence_fact`
- Explanation: Observed roles: counterargument_limitation, evidence_fact Display terms: absence, chemistry, date, filing, invention, presumed, priority Evidence spans paragraphs 1032-1038. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041277` offsets `122-130`; context: [148] In the pre-October 1, 1989 Act, the key date for obviousness was the date of the invention, which in the absence of evidence establishing an earlier date was presumed to be the priority filing date, if any, or the filing date.
- Evidence: `counterargument_limitation` cue `although` at chunk `5041281` offsets `130-138`; context: , Cephalosporins and Penicillins; Chemistry and Biology, (New York: Academic Press, 1972), although some chapters were attached to Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041282` offsets `141-149`; context: [153] Again, the filing date (including that of the priority application, if any) is just a presumed date of the invention in the absence of evidence to the contrary.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041283` offsets `56-59`; context: [154] One must remember that a claim can be anticipated but not obvious.

#### 22183:44:subtheme:2 · paragraphs 1039-1054

- Raw key terms: `court, cross-examination, june, patent, chivers, lilly, line, address`
- Display key terms: `cross-examination, june, patent, chivers, lilly, line, address`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue Display terms: cross-examination, june, patent, chivers, lilly, line, address Operative outcome context: [155] Lilly noted that it was not clear that experimentation was allowed in this context. Evidence spans paragraphs 1039-1054. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041284` offsets `122-127`; context: The Court need not address this issue here given the findings made on the overall issue.
- Evidence: `disposition` cue `allowed` at chunk `5041284` offsets `65-72`; context: [155] Lilly noted that it was not clear that experimentation was allowed in this context.
- Evidence: `counterargument_limitation` cue `however` at chunk `5041288` offsets `21-28`; context: Olah noted however that this was speculative and was never established.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041299` offsets `113-121`; context: Chivers’ original report was amended to address Lilly’s objection about duplicate evidence.

#### 22183:44:subtheme:3 · paragraphs 1055-1056

- Raw key terms: `apotex, accept, acted, affidavit, applied, argument, available, basis`
- Display key terms: `apotex, accept, acted, affidavit, applied, argument, available, basis`
- Argument roles: `counterargument_limitation, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, reasoning_application Display terms: apotex, accept, acted, affidavit, applied, argument, available, basis Application context: However, the Court did not understand that this argument applied only if the ppm shift of the kinetic complex was an essential element of the claim properly construed. Evidence spans paragraphs 1055-1056. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `5041300` offsets `204-211`; context: However, the Court did not understand that this argument applied only if the ppm shift of the kinetic complex was an essential element of the claim properly construed.
- Evidence: `counterargument_limitation` cue `However` at chunk `5041300` offsets `147-154`; context: However, the Court did not understand that this argument applied only if the ppm shift of the kinetic complex was an essential element of the claim properly construed.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041301` offsets `172-181`; context: 3(d) of his affidavit).

#### Section text

[148] In the pre-October 1, 1989 Act, the key date for obviousness was the date of the invention, which in the absence of evidence establishing an earlier date was presumed to be the priority filing date, if any, or the filing date.

[149] Peter G. Sammes, “Recent Chemistry of the β-Lactam Antibiotics” (1976) 76 Chemical Reviews 113 (TX-194).

[150] Obviously, that does not mean that anything not found in Sammes would necessarily be excluded from the common general knowledge or from the state of the art.

[151] However, an addendum was added. It is clear that the article now refers to publications in 1974, with some even dated 1975, presumably published before the revised manuscript was received on January 28, 1975.

[152] This included Edwin H. Flynn, ed., Cephalosporins and Penicillins; Chemistry and Biology, (New York: Academic Press, 1972), although some chapters were attached to Dr. Barrett’s report (E-14) (see also TX-196).

[153] Again, the filing date (including that of the priority application, if any) is just a presumed date of the invention in the absence of evidence to the contrary.

[154] One must remember that a claim can be anticipated but not obvious. See for example SmithKline Beecham Pharma Inc. v. Apotex Inc., 2001 FC 770, [2001] 4 F.C. 518, aff’d 2002 FCA 216, [2003] 1 F.C. 118 (C.A.) particularly at para. 22 of the FCA.

[155] Lilly noted that it was not clear that experimentation was allowed in this context. The Court need not address this issue here given the findings made on the overall issue.

[156] As the posita does not have to have any particular knowledge of β-lactam or cephalosporin chemistry, the Court does not accept that such person would know which solvents are suitable for chemistry on cephalosporin substrates (see also cross-examination of Dr. Olah, June 24, 2008, p. 205 line 1 - p. 206 line 17).

[157] Shire, at para. 24: “[t]he patent begins by acknowledging that certain things are already known and constitute, in patent language, prior art. Such an acknowledgement by the patentee is considered a binding admission as to prior art […].”

[158] The Court will include here all information that could be relevant not only to the ‘007 patent but to the Lilly process patents in order to review these publications only once.

[159] Dr. Olah noted however that this was speculative and was never established. Cross-examination of Dr. Olah, June 24, 2008, p. 142, lines 9-15.

[160] For example, “the covalent triphenoxy dihalide may be expected to be in equilibrium with all or any of the six possible ionic forms.” (Rydon, p. 3045)

[161] None of the experts who tested the reaction of TPP and Cl succeeded in crystallizing pure specimens of the kinetic complex. The ‘007 patent indicates that the kinetic complex could not be isolated.

[162] The method used by the authors to mix Cl and TPP in all their experiments was to slowly pass Cl gas through TPP (bubbling through).

[163] One experiment was performed in situ, diluting TPP in alcohol.

[164] According to Dr. Modro, this teaching is contrary to what is taught in the ‘007 patent.

[165] See Dr. Hunter report (E-18) at para. 33 where he says that this is how he understood Ramirez. The Court did consider his cross-examination on June 23, pp. 198-200 on this point. See also the cross-examination of Dr. Chivers, June 11, 2008, p. 97 to p. 98, line 4.

[166] Apotex did not point to any experiment in Richard Anschütz & William O. Emery, “Ueber die Einwirkung von Phosphortichlorid auf Salicylsäure und auf Phenol” (1889) 253 Annalen der Chemie 105, which is cited (in German only) where Cl and TPP are mixed in a hexane solution. The Court infers from this that there was no such experiment.

[167] Following the new convention.

[168] A form of triphenylphosphite dichloride, cross-examination of Dr. Hunter, June 23, 2008, at p. 203, lines 11-15. Cross-examination of Dr. Chivers, June 11, 2008, p. 96, line 17 to p. 97, line 1.

[169] The order of addition is not relevant to claim 17, although for the purpose of enablement, one can gather from the disclosure that the preferred method is to add TPP to Cl.

[170] The Court notes that Dr. Chivers’ original report was amended to address Lilly’s objection about duplicate evidence. In particular, paras. 49 and 50, which were to the same effect as those Dr. Modro referred to above were deleted. Dr. Chivers had apparently reached that conclusion with full knowledge of Tseng and Michalski’s work.

[171] As mentioned, the Court did not accept Apotex’s proposed construction that all claims were limited to a complex exhibiting a +3.7 ppm shift. However, the Court did not understand that this argument applied only if the ppm shift of the kinetic complex was an essential element of the claim properly construed.

[172] Again, this shows that this expert did not carry out research in that respect and simply acted on the basis of documents provided to him (listed at para. 3(d) of his affidavit). There is no explanation for why Apotex did not give him that publication which was obviously available to Dr. Olah.

## 22183:45 · paragraphs 1057-1057

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `abbdcedd12a1779fee7c346e9723f190cf98e70e276671145a0a382677815913`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:45:subtheme:1 · paragraphs 1057-1057

- Raw key terms: `among, apotex, counsel, provided, publications`
- Display key terms: `among, apotex, provided, publications`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: among, apotex, provided, publications No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 1057-1057. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

[173] Again, these were not among the publications provided to him by Apotex’s counsel.

## 22183:46 · paragraphs 1058-1079

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2eae55be023e03ea1011d2ca6dd2e857a3c34f6f55b341500165561d13d63a67`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:46:subtheme:1 · paragraphs 1058-1073

- Raw key terms: `process, cephalosporin, reduction, a-21, baldwin, disclosure, elevated, forms`
- Display key terms: `process, cephalosporin, reduction, a-21, baldwin, disclosure, elevated, forms`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: process, cephalosporin, reduction, a-21, baldwin, disclosure, elevated, forms No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 1058-1073. This is a deterministic evidence summary, not a legal conclusion.

#### 22183:46:subtheme:2 · paragraphs 1074-1079

- Raw key terms: `chemistry, patents, cannot, confirmed, general, modro, process, thermodynamic`
- Display key terms: `chemistry, patents, cannot, confirmed, modro, process, thermodynamic`
- Argument roles: `counterargument_limitation, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, reasoning_application Display terms: chemistry, patents, cannot, confirmed, modro, process, thermodynamic Application context: [193] Although this comment appears to apply to general organic chemistry (Dr. Evidence spans paragraphs 1074-1079. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041319` offsets `234-239`; context: It is well understood that the exercise should normally be carried out for each claim at issue but the Court is satisfied having done the exercise that the results here would be the same.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041319` offsets `240-243`; context: It is well understood that the exercise should normally be carried out for each claim at issue but the Court is satisfied having done the exercise that the results here would be the same.
- Evidence: `reasoning_application` cue `apply` at chunk `5041322` offsets `39-44`; context: [193] Although this comment appears to apply to general organic chemistry (Dr.

#### Section text

[174] There is no indication that Dr. Olah was told not to use such knowledge.

[175] A-21, tab 33, p. 124 and tab 35, p. 147.

[176] Dr. Chivers was careful to describe the work in Michalski as simply being “similar” to the Rydon process.

[177] See other publications which also bear Dr. Michalski’s name, listed in footnotes 3a) and b) of TX-1764D. It is also somewhat surprising that Dr. Modro did not refer to Dr. Michalski’s work considering that they worked closely and published together earlier in the former’s career.

[178] The authors confirmed Rydon’s views with respect to equilibria (ionic versus covalent forms) of species involved in the reaction.

[179] See Lilly Process Research and Development Division Progress Report (TX-211), p. 7; and L.D. Hatfield et al. “Application of Phosphorus-Halogen Compounds in Cleavage of the 7-Amide Group of Cephalosporins” in G.I. Gregory, ed., Recent advances in the chemistry of β-Lactam Antibiotics (London: The Royal Society of Chemistry, 1980) 109 at 118 (TX-221, also reproduced in a different form in TX-220).

[180] In 1976, a general request for help and suggestions of possible reagents to try was sent by Dr. Hatfield’s team (see A-21, tab 21, p. 97).

[181] As mentioned, these findings are relevant to the next inquiry in respect of the Lilly process patents.

[182] “Reduction of ∆3 Cephalosporin Sulfoxides”, (3 October 1968) (TX-1584). A patent discussed in the disclosure of the ‘536 patent, expressly relied upon by Apotex’s experts and which, according to the defendant, forms part of the common general knowledge.

[183] The only two other phosphites mentioned in this review are TPP (used alone), which was found to reduce the dimethyl sulfoxides at elevated temperatures and chlorophospholane.

[184] Although Drabowicz is cited in “Cephalosporin Reduction Process”, U.S. Patent No. 4223133 (1 February 1979) (TX-1783A), it is not clear if this was art which was cited by the examiner or the inventor as there is no reference to this publication in the disclosure of this patent per se.

[185] One crystal.

[186] This was established by E.H. Amonodo-Neizer, et al. in an article published in 1965 (J. Chem. Soc.) 4296, where the reduction was done at an elevated temperature. Dr. Baldwin testified that a posita would be quite weary of heating cephalosporin sulfoxide.

[187] TX-1783A.

[188] (1976) Tetrahedron Lett. 971.

[189] Cross-examination of Dr. Baldwin, June 25, 2009, p. 218, line 16; p. 219, line 7.

[190] Rather than going through each claim individually, the Court describes the general inventive concept of the claims in the process patents. It is well understood that the exercise should normally be carried out for each claim at issue but the Court is satisfied having done the exercise that the results here would be the same.

[191] Dr. Modro’s experiments confirmed that the thermodynamic compound or final product of this reaction cannot perform the three steps covered in the ‘536 patent. The disclosure of the patents also makes it clear that the thermodynamic cannot perform the other reactions set out in the ‘725 and the ‘468 patents.

[192] Coe and Rydon only discuss halogenation of simple alcohols.

[193] Although this comment appears to apply to general organic chemistry (Dr. McClelland has no experience in β-lactam chemistry), it is still relevant.

[194] Dr. Modro’s own experiment confirmed that the thermodynamic cannot be used instead of the kinetic complex in the cephalosporin chemistry described in the process patents.

[195] These scientists were very experienced in the chemistry of cephalosporins. (A-21, tab 6, p. 149, lines 1 and 2.)

## 22183:47 · paragraphs 1080-1099

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1e24a327893717c9c6a0ef1878b408a4dee5bda22f54a559d0cb28d0c1001b53`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:47:subtheme:1 · paragraphs 1080-1099

- Raw key terms: `barrett, a-21, cross-examination, lines, used, affidavit, apotex, april`
- Display key terms: `barrett, a-21, cross-examination, lines, used, affidavit, apotex, april`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: barrett, a-21, cross-examination, lines, used, affidavit, apotex, april Application context: Barrett’s views were not considered, the Court would be left with a void as there would be insufficient evidence for me to conclude that retrosynthesis was commonly used by the posita in this context. Evidence spans paragraphs 1080-1099. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041332` offsets `10-19`; context: [203] See affidavit of Dr.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041333` offsets `234-243`; context: 50, lines 3-12; affidavit of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041343` offsets `30-38`; context: [214] Apotex objected to this evidence on the basis that it constituted hearsay.
- Evidence: `reasoning_application` cue `conclude` at chunk `5041343` offsets `323-331`; context: Barrett’s views were not considered, the Court would be left with a void as there would be insufficient evidence for me to conclude that retrosynthesis was commonly used by the posita in this context.

#### Section text

[196] See A-21, tab 32.

[197] See A-21, tab 21, p. 97 and A-16, tab 4.

[198] See A-21, tab 19, p. 91.

[199] See A-21, tab 80; TX-211, TX-220 and TX-221.

[200] Cross-examination of Dr. Baldwin, April 28, 2008, p. 219, lines 12-15.

[201] This is only relevant to the choice of base employed in the claimed reaction. As this is not controversial, it will not be discussed further.

[202] As per their final written submissions.

[203] See affidavit of Dr. Barrett (E-14), paras. 42-51 and 116.

[204] See examination-in-chief of Dr. Barrett, April 22, 2008, p. 42, line 19 to p. 43, line 24; cross-examination of Dr. Barrett, June 18, 2008, p. 71, lines 18-20; cross-examination of Dr. Barrett, June 17, 2008, p. 50, lines 3-12; affidavit of Dr. Barrett (E-14), paras. 27, 29 and 40.

[205] Dr. Morin, like Dr. Cooper, was a research chemist at Lilly.

[206] See patent, TX-147.

[207] Common disclosure p. 2.

[208] Allylic bromination is a specific type of allylic halogenation.

[209] Ozone is a electrophilic agent.

[210] Dr. Barrett indicated that this compound was not suitable for the type of chemistry described in the Shionogi process. It could only be used to make a compound that did not require a side chain.

[211] See cross-examination of Dr. Barrett, June 18, 2008, p. 54, lines 8-13.

[212] See Sammes, p. 143.

[213] It is generally agreed that retrosynthesis means moving backward from the desired molecule by sequentially breaking key bonds and/or changing functionality in a stepwise process that ultimately leads to the desired precursor molecule.

[214] Apotex objected to this evidence on the basis that it constituted hearsay. The Court rejects this for it is exactly what expert evidence, in this context, seeks to provide. In any event, if Dr. Barrett’s views were not considered, the Court would be left with a void as there would be insufficient evidence for me to conclude that retrosynthesis was commonly used by the posita in this context. Dr. McClelland’s views were given no weight in that respect.

[215] Apotex did not provide a translation of this document or of the two other German publications its experts relied upon. Obviously, this is contrary to the rules of the Court and to an express direction given at one of the trial management conferences. The weight of the experts’ opinion based on those documents is diminished by the fact that the Court could not properly review the documents. The English documents used by Dr. Barrett are not the same as the German ones.

## 22183:48 · paragraphs 1100-1116

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9e803d4e08e5bbca0edef4f9f876e3a4897d8a24ffbac4694c44490cf2ab8d54`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:48:subtheme:1 · paragraphs 1100-1102

- Raw key terms: `abstracted, abstracts, amount, appears, application, cephem, chauvette, chemical`
- Display key terms: `abstracted, abstracts, amount, appears, cephem, chauvette, chemical`
- Argument roles: `evidence_fact, governing_rule`
- Explanation: Observed roles: evidence_fact, governing_rule Display terms: abstracted, abstracts, amount, appears, cephem, chauvette, chemical Rule/authority context: [218] See TX-1610 and TX-1611 which were filed under reserve of an objection. Evidence spans paragraphs 1100-1102. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041345` offsets `15-23`; context: [216] From the evidence presented, it appears that there could be a delay of 5 months, if not more, between the publication of an application for a patent and its reporting in Chemical Abstracts, depending on the amount of material to be abstracted in the given period.
- Evidence: `governing_rule` cue `under` at chunk `5041347` offsets `47-52`; context: [218] See TX-1610 and TX-1611 which were filed under reserve of an objection.

#### 22183:48:subtheme:2 · paragraphs 1103-1116

- Raw key terms: `compound, court, shionogi, claimed, cross-examination, footnote, given, june`
- Display key terms: `compound, shionogi, claimed, cross-examination, footnote, given, june`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: compound, shionogi, claimed, cross-examination, footnote, given, june Application context: 378 where the reasoning applied to product claims was applied to process claims. | [231] That very same principle was applied in a modified way in Shell Oil (at pp. Evidence spans paragraphs 1103-1116. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5041348` offsets `145-152`; context: Martin and his own belief as to whether Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041351` offsets `106-114`; context: Hanessian’s evidence, the Court prefers Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041355` offsets `125-133`; context: 146, line 5; The Court notes that there is no evidence as to the obviousness or expectation of success of all these reasonable approaches which presumably all involved known chemical reactions.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041355` offsets `357-360`; context: Hanessian’s reasoning, they were thus all trivial variations but only one did work?
- Evidence: `reasoning_application` cue `applied` at chunk `5041359` offsets `95-102`; context: 378 where the reasoning applied to product claims was applied to process claims.
- Evidence: `counterargument_limitation` cue `although` at chunk `5041359` offsets `202-210`; context: In the same manner, a compound that was not made, although it was disclosed as part of a class, can be subsequently claimed if the patent discloses in its regard a certain advantage over the other members of the class.
- Evidence: `reasoning_application` cue `applied` at chunk `5041360` offsets `35-42`; context: [231] That very same principle was applied in a modified way in Shell Oil (at pp.

#### Section text

[216] From the evidence presented, it appears that there could be a delay of 5 months, if not more, between the publication of an application for a patent and its reporting in Chemical Abstracts, depending on the amount of material to be abstracted in the given period.

[217] Dr. Chauvette reacted a 3-hydroxy cephem (the target compound of the overall synthetic process) with a sulfonyl Cl and then used a fluoride salt to effect a substitution to form a 3 fluoro cephem.

[218] See TX-1610 and TX-1611 which were filed under reserve of an objection. These documents are both inadmissible.

[219] The content of footnote 22 in TX-1609 is hearsay. Its content is contrary to the practice described by Dr. Martin and his own belief as to whether Dr. Kishi reads his lectures. The Court is not persuaded that this paper was read in its entirety at any of these conferences.

[220] See Servier (2009) (at para. 58) which confirms that the Court can refer to the disclosure to determine the inventive concept when same is not readily discernable from the claims.

[221] The usefulness or utility of the new compounds referred to in all the Shionogi patents, including compounds A, B, C, and D of the ‘026 patent is not contested, except for certain substituents that will be discussed in a distinct section.

[222] If one had to consider the Chauvette application, for reasons given when discussing Dr. Hanessian’s evidence, the Court prefers Dr. Barrett’s evidence that the 3-hydroxy cephem would not be considered by the posita as a compound that would give relevant information about the reactivity of the Shionogi starting compounds (open ring structure).

[223] It is not disputed that said disclosure gives sufficient detail to enable the posita to use each claimed step in the context of this overall pathway. See also footnote 128.

[224] During his cross-examination, he simply acknowledged that if one of his graduate students came up with such a scheme he would deserve a raise (June 19, 2008, p. 152). In fact, his answer at p. 129, lines 5-12 (June 19, 2008) that “if someone skilled in the art were given the final compound and the starting material and was said devise a synthetic method, it’s not unreasonable or unlikely that amongst many approaches that this [the Shionogi process] could perhaps be one of the approaches that a person could come up with”, appears to seriously weaken, if not directly contradict, Apotex’s position.

[225] Interestingly even if it presumably relates to his field of expertise, Dr. McClelland admitted that he was not aware of any of the Lilly patents (or the kinetic complex) before getting involved in a litigation for Apotex sometime in 1996/1997.

[226] Cross-examination of Dr. Hanessian, June 19, 2008, p. 145, line 21 to p. 146, line 5; The Court notes that there is no evidence as to the obviousness or expectation of success of all these reasonable approaches which presumably all involved known chemical reactions. What if, following Dr. Hanessian’s reasoning, they were thus all trivial variations but only one did work?

[227] This is evident from the fact, among other things, that Dr. Kukolja continued to search for a solution even after Shionogi had developed its process at Lilly’s request and expense.

[228] As was Dr. Blaszczak.

[229] See footnote 128.

[230] See Canada (Commissioner of Patents) v. Ciba Ltd., [1959] S.C.R. 378 where the reasoning applied to product claims was applied to process claims. In the same manner, a compound that was not made, although it was disclosed as part of a class, can be subsequently claimed if the patent discloses in its regard a certain advantage over the other members of the class. Such advantage need not be claimed in order for it to support the inventiveness of what is actually claimed (Sanofi, para. 31).

[231] That very same principle was applied in a modified way in Shell Oil (at pp. 550-552 of the S.C.R.). In that case, the only reason for which the use had to be included in the claim was that the compound per se was not novel; had its use not been claimed, it would have been anticipated.

[232] In contrast, see for example the answer given by Dr. Barrett in his cross-examination on June 18, 2008, p. 28, line 9 to p. 29, line 4.

## 22183:49 · paragraphs 1117-1117

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `318237e62d5f7af11e258b494139471919e293fa9319b4c313e93861f87be995`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:49:subtheme:1 · paragraphs 1117-1117

- Raw key terms: `cross-examination, june, line`
- Display key terms: `cross-examination, june, line`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: cross-examination, june, line No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 1117-1117. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

[233] Cross-examination, June 5, 2008, p. 244, line 4 to p. 245, line 6.

## 22183:50 · paragraphs 1118-1132

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d0c2020c9c3fb08ca8835e9b327cecf12e140c1161dbe13e4b1a7dcaa9e2f30d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:50:subtheme:1 · paragraphs 1118-1130

- Raw key terms: `modro, patent, respect, para, court, earlier, even, examples`
- Display key terms: `modro, patent, respect, para, earlier, even, examples`
- Argument roles: `evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, reasoning_application Display terms: modro, patent, respect, para, earlier, even, examples Rule/authority context: 61 of his affidavit (A-12), when he refers to the quantities of reactants or the reaction conditions under which they are combined. Application context: McClelland’s argument also appears to apply to the Lilly process patents but, as mentioned earlier, little weight, if any, was given to this portion of his evidence. | Modro, those substituents could introduce new effects because of their close proximity to the reaction centre. Evidence spans paragraphs 1118-1130. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041366` offsets `166-174`; context: McClelland’s argument also appears to apply to the Lilly process patents but, as mentioned earlier, little weight, if any, was given to this portion of his evidence.
- Evidence: `governing_rule` cue `under` at chunk `5041366` offsets `420-425`; context: 61 of his affidavit (A-12), when he refers to the quantities of reactants or the reaction conditions under which they are combined.
- Evidence: `reasoning_application` cue `apply` at chunk `5041366` offsets `48-53`; context: McClelland’s argument also appears to apply to the Lilly process patents but, as mentioned earlier, little weight, if any, was given to this portion of his evidence.
- Evidence: `reasoning_application` cue `because` at chunk `5041368` offsets `77-84`; context: Modro, those substituents could introduce new effects because of their close proximity to the reaction centre.

#### 22183:50:subtheme:2 · paragraphs 1131-1132

- Raw key terms: `claimed, compounds, addressed, although, apotex, argues, basis, cannot`
- Display key terms: `claimed, compounds, addressed, although, apotex, argues, basis, cannot`
- Argument roles: `counterargument_limitation, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, issue, party_position Display terms: claimed, compounds, addressed, although, apotex, argues, basis, cannot Position/evidence statements: Modro and McClelland questioned the operability of some of the compounds, they never directly addressed the issue of whether or not, at the relevant time, on the basis of the examples found in the patents, the inventors  Evidence spans paragraphs 1131-1132. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041376` offsets `128-133`; context: Modro and McClelland questioned the operability of some of the compounds, they never directly addressed the issue of whether or not, at the relevant time, on the basis of the examples found in the patents, the inventors could objectively predict the utility of all the meta, para, and ortho Z substituents claimed in the patents.
- Evidence: `party_position` cue `claimed` at chunk `5041376` offsets `326-333`; context: Modro and McClelland questioned the operability of some of the compounds, they never directly addressed the issue of whether or not, at the relevant time, on the basis of the examples found in the patents, the inventors could objectively predict the utility of all the meta, para, and ortho Z substituents claimed in the patents.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5041377` offsets `227-233`; context: The defendant cannot here state that the compounds were inoperable if they provided yields lower than the preferred embodiments.

#### Section text

[234] I truly believe that the use of hot tubbing would have been particularly useful here.

[235] The Court accepts here the views of Dr. Barrett.

[236] As opposed to the isomerized compound described in Cooper 2.

[237] Dr. McClelland’s argument also appears to apply to the Lilly process patents but, as mentioned earlier, little weight, if any, was given to this portion of his evidence. The Court also agrees with Lilly that this argument was not properly pleaded in the defence in respect of the Lilly process patents. See para. 61 of his affidavit (A-12), when he refers to the quantities of reactants or the reaction conditions under which they are combined. In this context, it is evident that what Dr. McClelland is referring to is the nature of the reactant not what he refers to in para. 61. However, his para. 62 which deals with sound prediction i.e. for the compounds which are not the subject of examples in the patent the wording of 62 is wide enough to encompass this argument.

[238] With respect to Dr. Modro’s opinion, one must note that the ‘007 patent in addition to the examples discussed earlier, contains examples in respect of all the Z variants – Z = H, see examples 1, 2, 3, 4, 6, 7A-E; Halo, see examples 9 and 10; Chloro, C1-C4 alkyl, see examples 5 and 7F; C1-C4 alkoxy, see example 7G.

[239] According to Dr. Modro, those substituents could introduce new effects because of their close proximity to the reaction centre. They could “block the reaction centre, slow down the reaction, or even trigger some completely new reactions.” (examination-in-chief of Dr. Modro, June 4, 2008, p. 89, line 20 to p. 90, line 4)

[240] The Z equals OCH3 in para position.

[241] See para. 275 of Lilly’s memorandum on validity. From this it seems that the validity of claim 17 of the ‘007 patent could be impacted.

[242] Even if, since 2001, Dr. Modro did perform about 60 experiments in respect of those patents.

[243] In that respect, Dr. Modro particularly referred to an article from Dr. Gloede published in 1994 (J. Gloede, “Halogenation of ortho-Substituted Aryl Phosphites” (1994) 64 Russian Journal of General Chemistry 1203, TX-1592 (Gloede))

[244] Dr. Modro said that he had concerns that were confirmed by what was reported in TX-211. Amazingly he did not mention the experiments disclosed in the ‘007 patent that directly deal with many of those substituents.

[245] For Dr. McClelland, see June 9, 2008, p. 78-91. For Dr. Modro, see June 5, 2008, p. 80, line 10 to p. 89, line 24.

[246] Although Dr. Baldwin acknowledged that the tert-butoxy and tert-butyl groups would be the bulkier substituent and that the bulkier the group, the more likely its steric effect. He did not change his view that this was a relatively small substituent.

[247] Although Drs. Modro and McClelland questioned the operability of some of the compounds, they never directly addressed the issue of whether or not, at the relevant time, on the basis of the examples found in the patents, the inventors could objectively predict the utility of all the meta, para, and ortho Z substituents claimed in the patents.

[248] It is worth noting that throughout these proceedings, Apotex argues that the higher yields provided by the preferred compounds were not to be considered by the Court as these higher yields were not claimed. The defendant cannot here state that the compounds were inoperable if they provided yields lower than the preferred embodiments.

## 22183:51 · paragraphs 1133-1136

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `56c7f215c01ba73451793980b5fc72511b1fcca45c8b252bd9aa76f9931797e5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:51:subtheme:1 · paragraphs 1133-1136

- Raw key terms: `mcclelland, complex, cross-examination, evidence, june, kinetic, line, actually`
- Display key terms: `mcclelland, complex, cross-examination, june, kinetic, line, actually`
- Argument roles: `counterargument_limitation, evidence_fact`
- Explanation: Observed roles: counterargument_limitation, evidence_fact Display terms: mcclelland, complex, cross-examination, june, kinetic, line, actually Evidence spans paragraphs 1133-1136. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041378` offsets `10-18`; context: [249] The evidence provided by Apotex’s experts may have been sufficient to put an allegation of invalidity in play in the context of an NOC proceeding but it is certainly not sufficient to meet the burden of proving on a preponderance of evidence that these compounds were not useful or that their usefulness could not be soundly predicted.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041378` offsets `152-155`; context: [249] The evidence provided by Apotex’s experts may have been sufficient to put an allegation of invalidity in play in the context of an NOC proceeding but it is certainly not sufficient to meet the burden of proving on a preponderance of evidence that these compounds were not useful or that their usefulness could not be soundly predicted.
- Evidence: `evidence_fact` cue `found that` at chunk `5041379` offsets `114-124`; context: [250] The argument with respect to the reversed order of addition will not be dealt with given that the Court has found that the kinetic complex would form using the process described in Coe and Rydon and Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041381` offsets `169-177`; context: This was further corroborated by the evidence of Mr.

#### Section text

[249] The evidence provided by Apotex’s experts may have been sufficient to put an allegation of invalidity in play in the context of an NOC proceeding but it is certainly not sufficient to meet the burden of proving on a preponderance of evidence that these compounds were not useful or that their usefulness could not be soundly predicted. Many of the cases referred to by Apotex were decisions made in the context of NOC proceedings.

[250] The argument with respect to the reversed order of addition will not be dealt with given that the Court has found that the kinetic complex would form using the process described in Coe and Rydon and Dr. McClelland indicated during his cross-examination that this would simply reduce the yields and would not make the compound inactive.

[251] See cross-examination of Dr. McClelland, June 9, 2008, p. 108, line 20 to p. 109, line 1.

[252] Dr. McClelland has agreed that there is no reason to believe that the kinetic complex cannot be prepared at room temperature. This was further corroborated by the evidence of Mr. Moraski who introduced experiments performed where the kinetic complex was actually prepared at room temperature and 0º Celsius. (Examination-in-chief of Mr. Moraski, June 20, 2008, p. 16, line 24 to p. 18, line 5; E-9)

## 22183:52 · paragraphs 1137-1145

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `051235008f7d9cff13d600ec297a32aff852ce213fa5e85a9f597be5d4e204f5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:52:subtheme:1 · paragraphs 1137-1139

- Raw key terms: `affidavit, a-12, a-13, admitted, apotex, baldwin, certain, complex`
- Display key terms: `affidavit, a-12, a-13, admitted, apotex, baldwin, certain, complex`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: affidavit, a-12, a-13, admitted, apotex, baldwin, certain, complex Evidence spans paragraphs 1137-1139. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041382` offsets `120-125`; context: Modro admitted during his cross-examination that the formation of a kinetic complex was not the issue as it would necessarily form.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041382` offsets `175-184`; context: 70 of his affidavit (A-13), he only deals with the final product (the thermodynamic).
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041384` offsets `94-103`; context: McClelland’s affidavit (A-12).

#### 22183:52:subtheme:2 · paragraphs 1140-1145

- Raw key terms: `cross-examination, june, mcclelland, claims, hanessian, line, lines, para`
- Display key terms: `cross-examination, june, mcclelland, claims, hanessian, line, lines, para`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: cross-examination, june, mcclelland, claims, hanessian, line, lines, para Evidence spans paragraphs 1140-1145. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041385` offsets `66-71`; context: Barrett, there is no issue with respect to the argument when thiazoline is in place such as in claims 4, 10, 12, 31, 35, and 37.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041386` offsets `115-123`; context: 363, refers to claims 22 and 34 but there appears to be no evidence from their experts in relation to these two claims.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041386` offsets `88-91`; context: 363, refers to claims 22 and 34 but there appears to be no evidence from their experts in relation to these two claims.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `5041387` offsets `6-15`; context: [258] Affidavit of Dr.

#### Section text

[253] In any event, Dr. Modro admitted during his cross-examination that the formation of a kinetic complex was not the issue as it would necessarily form. In para. 70 of his affidavit (A-13), he only deals with the final product (the thermodynamic).

[254] Dr. Baldwin noted that considering the data disclosed in Gloede without testing, one could not say for certain which reaction would happen first but this presumes that one knows that this further reaction takes place. (See examination-in-chief of Dr. Baldwin, June 25, 2008, p. 14, line 6 to p. 15, line 18)

[255] See paras. 354-358 of Apotex memorandum on validity; paras. 151-153 of Dr. McClelland’s affidavit (A-12).

[256] As noted during the examination of Dr. Barrett, there is no issue with respect to the argument when thiazoline is in place such as in claims 4, 10, 12, 31, 35, and 37. See also cross-examination of Dr. McClelland, June 9, 2008, p. 177, line 20 to p. 178, line 20.

[257] Apotex, in its memorandum on invalidity, at para. 363, refers to claims 22 and 34 but there appears to be no evidence from their experts in relation to these two claims.

[258] Affidavit of Dr. McClelland (A-12), paras. 167-170; affidavit of Dr. Hanessian (A-15), para. 94.

[259] See cross-examination of Dr. McClelland, June 9, 2008, p. 211, lines 5-11; p. 219, line 13 to p. 220, line 5.

[260] Jerry March, Advanced Organic Chemistry: Reactions, Mechanisms, and Structure (New York: McGraw-Hill, 1968) at 294 (TX-1618).

[261] Cross-examination of Dr. Hanessian, June 19, 2008, p. 141, lines 1-9.

## 22183:53 · paragraphs 1146-1153

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6dbc667bf1f2a7520d0249c553cb0a1cc59d85aa4387f9d3cf67588c731b7174`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:53:subtheme:1 · paragraphs 1146-1151

- Raw key terms: `lines, cross-examination, june, mcclelland, avoid, barrett, claim, court`
- Display key terms: `lines, cross-examination, june, mcclelland, avoid, barrett`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: lines, cross-examination, june, mcclelland, avoid, barrett No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 1146-1151. This is a deterministic evidence summary, not a legal conclusion.

#### 22183:53:subtheme:2 · paragraphs 1152-1153

- Raw key terms: `remains, adopted, claim, clear, considering, construction, court, differentiation`
- Display key terms: `remains, adopted, clear, considering, construction, differentiation`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: remains, adopted, clear, considering, construction, differentiation Evidence spans paragraphs 1152-1153. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5041397` offsets `35-40`; context: [268] It is not clear if this last issue is now moot given that only one process claim remains.

#### Section text

[262] Cross-examination of Dr. McClelland, June 10, 2008, p. 37, lines 6-22.

[263] Ibid., p. 38, lines 6-12.

[264] Cross-examination of Dr. McClelland, June 10, 2008, p. 39, lines 17-20.

[265] Cross-examination of Dr. Barrett, June 18, 2008, p. 322, lines 7-8.

[266] The Court understands here that normally only persons having specialized knowledge of fluorine would use such product. Such persons would know how to manipulate the product to avoid its inherent danger.

[267] See claim 1 as well as the disclosure, p. 20, line 21 to p. 21, line 8.

[268] It is not clear if this last issue is now moot given that only one process claim remains.

[269] Considering the construction adopted by the Court, this is the only differentiation that remains relevant.

## 22183:54 · paragraphs 1154-1161

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d6c819683119b6e7c017e25938655551c336ef52ea3985e6012e13aa154d0dca`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:54:subtheme:1 · paragraphs 1154-1161

- Raw key terms: `alternative, paras, advanced, affected, against, alliedsignal, apotex, appeal`
- Display key terms: `alternative, paras, advanced, affected, against, alliedsignal, apotex`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: alternative, paras, advanced, affected, against, alliedsignal, apotex Rule/authority context: 112(b) reads as follows: “The Defendant, Plaintiff by Counterclaim therefore claims: […] b) damages pursuant to section 36 of the Competition Act to be paid to Apotex and/or in the alternative to be set-off against any a Application context: 112(b) reads as follows: “The Defendant, Plaintiff by Counterclaim therefore claims: […] b) damages pursuant to section 36 of the Competition Act to be paid to Apotex and/or in the alternative to be set-off against any a Evidence spans paragraphs 1154-1161. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5041402` offsets `112-123`; context: 112(b) reads as follows: “The Defendant, Plaintiff by Counterclaim therefore claims: […] b) damages pursuant to section 36 of the Competition Act to be paid to Apotex and/or in the alternative to be set-off against any award of damages awarded against Apotex;”
- Evidence: `reasoning_application` cue `therefore` at chunk `5041402` offsets `79-88`; context: 112(b) reads as follows: “The Defendant, Plaintiff by Counterclaim therefore claims: […] b) damages pursuant to section 36 of the Competition Act to be paid to Apotex and/or in the alternative to be set-off against any award of damages awarded against Apotex;”

#### Section text

[270] As mentioned earlier, the one alternative in claim 17 referring to claim 10 is to be considered a stand-alone claim which could not be affected, in any event, by the argument advanced.

[271] In Rydon, which is discussed in the disclosure, the authors report that such a 2:1 ratio will only produce a monochloride.

[272] See paras. 18-21 of E-19.

[273] Para. 112(b) reads as follows: “The Defendant, Plaintiff by Counterclaim therefore claims: […] b) damages pursuant to section 36 of the Competition Act to be paid to Apotex and/or in the alternative to be set-off against any award of damages awarded against Apotex;”

[274] See AlliedSignal Inc. v. Du Pont Canada Inc. (1998), 142 F.T.R. 241, 78 C.P.R. (3d) 129, at paras. 21 and 24.

[275] This matter proceeded twice before the Federal Court of Appeal on summary judgment motions as well as once with regard to an appeal of an order of a Prothonotary.

[276] In fact, two of the Lilly patents expired after all of the Shionogi patents had expired.

[277] see TX-686.

## 22183:55 · paragraphs 1162-1252

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a4ef50dac9d2e2735e2adad4eb9889e3841d251b9ab6ce35942706317c1be6d1`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:55:subtheme:1 · paragraphs 1162-1213

- Raw key terms: `para, ibid, apotex, lilly, competition, lrta, srta, appeal`
- Display key terms: `para, ibid, apotex, lilly, competition, lrta, srta`
- Argument roles: `disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, reasoning_application Display terms: para, ibid, apotex, lilly, competition, lrta, srta Rule/authority context: 10(1)(b)(iii); In this case it is under the latter provision that an investigation could have been prompted following a complaint which was filed by Apotex in September, 2002. | It is important to be reminded that for proceedings conducted under the Competition Act, somewhat exceptional tools are provided for under that Act (see subs. Application context: [285] Because of the late disclosure of the allegation of meetings between Lilly and Apotex, and the fact that no other participant was clearly identified, Lilly was not in a position to call witnesses other than Mr. Operative outcome context: [307] Varied on appeal but not on this point as it was not pursued by the appellant, 2000 BCCA 463, (2000), B. Evidence spans paragraphs 1162-1213. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041414` offsets `242-250`; context: McCool to rebut Apotex’s evidence in this regard (i.
- Evidence: `reasoning_application` cue `Because` at chunk `5041414` offsets `6-13`; context: [285] Because of the late disclosure of the allegation of meetings between Lilly and Apotex, and the fact that no other participant was clearly identified, Lilly was not in a position to call witnesses other than Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041418` offsets `402-410`; context: 22) that was presumed by the Court of Appeal to have been made in light of both the 1995 and 1975 agreements, despite the comments of Justice Hugessen to the effect that there was both conflict and lack of clarity in the evidence as to the forseeability and reach of the 1975 agreement which could only be resolved after a full trial (2004 FC 1445, [2005] 2 F.
- Evidence: `governing_rule` cue `under` at chunk `5041422` offsets `50-55`; context: 10(1)(b)(iii); In this case it is under the latter provision that an investigation could have been prompted following a complaint which was filed by Apotex in September, 2002.
- Evidence: `governing_rule` cue `under` at chunk `5041423` offsets `203-208`; context: It is important to be reminded that for proceedings conducted under the Competition Act, somewhat exceptional tools are provided for under that Act (see subs.
- Evidence: `disposition` cue `Varied` at chunk `5041436` offsets `6-12`; context: [307] Varied on appeal but not on this point as it was not pursued by the appellant, 2000 BCCA 463, (2000), B.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5041438` offsets `141-152`; context: [309] Lilly’s information as to the process actually used by Lupin was based on the closed portion of the Health Canada file it had received pursuant to an order of Justice Hugessen.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5041455` offsets `190-201`; context: Ltd, the owners of the Lilly and Shionogi patents, were joined to the proceedings pursuant to subs.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `5041456` offsets `64-73`; context: [327] See Facts agreed to by the parties, SRTA # 19(b); TX-644, Affidavit of Thomas L.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `5041458` offsets `10-19`; context: [329] See Affidavit of Harry B.

#### 22183:55:subtheme:2 · paragraphs 1214-1252

- Raw key terms: `ibid, para, lrta, agreed, apotex, dated, facts, line`
- Display key terms: `ibid, para, lrta, agreed, apotex, dated, facts, line`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: ibid, para, lrta, agreed, apotex, dated, facts, line Rule/authority context: [348] See TX-1656; While the agreement is silent on pricing, Apotex appears to have paid US$ 1 500 per kilogram of bulk cefaclor manufactured under it (see TX-1759), versus US$ 860 – 1 150 earlier. Evidence spans paragraphs 1214-1252. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5041459` offsets `44-51`; context: [330] Although there is a controversy as to whether or not Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041462` offsets `294-302`; context: 133, line 12) However, the only evidence the Court has as to these assurances are contained in the letter from Pacific High Tech Canada, which is dated 10 days later than the notice of termination of the compulsory licence (see next para.
- Evidence: `counterargument_limitation` cue `However` at chunk `5041462` offsets `276-283`; context: 133, line 12) However, the only evidence the Court has as to these assurances are contained in the letter from Pacific High Tech Canada, which is dated 10 days later than the notice of termination of the compulsory licence (see next para.
- Evidence: `governing_rule` cue `under` at chunk `5041477` offsets `142-147`; context: [348] See TX-1656; While the agreement is silent on pricing, Apotex appears to have paid US$ 1 500 per kilogram of bulk cefaclor manufactured under it (see TX-1759), versus US$ 860 – 1 150 earlier.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041492` offsets `82-91`; context: dated December 14, 2007 (Exhibit JC-2 of his affidavit of April 19, 2008 (A-24)), p.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `5041493` offsets `6-15`; context: [364] Affidavit-in-chief of Dr.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041494` offsets `76-85`; context: Church, dated March 28, 2008 (Exhibit JC-1 of his affidavit of March 31, 2008 (A-31)), para.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041495` offsets `116-124`; context: patents (TX-228), while the evidence shows that patent applications were filed in other jurisdictions (see TX-233; Examination in chief of Mr.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041496` offsets `17-26`; context: [367] Responding affidavit of Dr.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041497` offsets `76-85`; context: Church, dated March 28, 2008 (Exhibit JC-1 of his affidavit of March 31, 2008 (A-31)), para.

#### Section text

[278] See subs. 36(7) of the Federal Courts Act.

[279] The equivalent of para. 36(4)(b) of the Federal Courts Act, para. 2(2)(b) of the Judgment Interest Act and subs. 2(c) of the Court Order Interest Act.

[280] See also Sands Motor Hotel Ltd. v. Edmonton (City), 2005 ABCA 402, 376 A.R. 365, paras. 31-32.

[281] See its para. 1(b).

[282] Apotex’s second fresh as amended statement of defence and counterclaim, para. 110

[283] This agreement was consigned in a letter addressed to the Court from counsel for Apotex, dated October 22, 2008.

[284] Among other things, those present at the meeting in June, 1974 were deceased and this fact was conveyed to Mr. Wada contemporaneously and in the course of his employment.

[285] Because of the late disclosure of the allegation of meetings between Lilly and Apotex, and the fact that no other participant was clearly identified, Lilly was not in a position to call witnesses other than Mr. McCool to rebut Apotex’s evidence in this regard (i.e. the testimony of Dr. Sherman and Mr. Kay).

[286] Apotex agreed that Shionogi would not have to call its own expert economists and could rely on Dr. Cockburn even if this expert was originally appointed only by Lilly. This had the impact of shortening the trial.

[287] See transcript of October 6, 2008, p. 183, line 18 to p. 184, line 3.

[288] 2003 FC 1171, (2003), 28 C.P.R. (4th) 37, reversed on appeal (2004 FCA 232, (2004), 240 D.L.R. (4th) 679) and sent back before the Federal Court: 2004 FC 1445, [2005] 2 F.C.R. 225, decision again reversed on appeal (2005 FCA 361, [2006] 2 F.C.R. 477).

[289] This was in fact held to have been a finding of Justice James Hugessen in the decision being appealed to the Federal Court of Appeal (2004 FC 1445, [2005] 2 F.C.R. 225, para. 22) that was presumed by the Court of Appeal to have been made in light of both the 1995 and 1975 agreements, despite the comments of Justice Hugessen to the effect that there was both conflict and lack of clarity in the evidence as to the forseeability and reach of the 1975 agreement which could only be resolved after a full trial (2004 FC 1445, [2005] 2 F.C.R. 225, para. 25)

[290] 2005 FCA 361, [2006] 2 F.C.R. 477, para. 39.

[291] Competition Act, para. 7(1)(a).

[292] Ibid., paras. 9(1)(c) and 10(1)(a).

[293] Ibid., c. 10(1)(b)(iii); In this case it is under the latter provision that an investigation could have been prompted following a complaint which was filed by Apotex in September, 2002. In addition, one of the experts testifying on Apotex’s behalf, Dr. Church, contacted the Competition Bureau following the first decision of Justice Hugessen on the summary judgment motions to alert them of this decision which he felt was inconsistent with the positions expressed by the Competition Bureau in its Intellectual Property Enforcement Guidelines (Cross-examination of Dr. Church, September 9, 2008, p. 73, line 3 to p. 77, line 12). The Commissioner did not cause such an inquiry to be made in this regard.

[294] This is in addition to other remedies available to such a plaintiff at common law and which are subject to different time limitations. It is important to be reminded that for proceedings conducted under the Competition Act, somewhat exceptional tools are provided for under that Act (see subs. 69(2)). The central role of the Commissioner is also demonstrated by the fact that the 2-year limitation under s. 36 will only start to run the day original proceedings are finally disposed of when such proceedings are instituted.

[295] Eli Lilly and Co. et al. v. Apotex Inc. (December 21, 2006), Ottawa T-1321-97 (F.C.); confirmed on appeal, 2007 FC 367, (2007), 156 A.C.W.S. (3d) 807; The Court notes that in addition to the cases cited by Prothonotary Aronovitch, this same principle was re-affirmed by two more recent cases: Harmegnies v. Toyota Canada, 2007 QCCS 539, J.E. 2007-842 (affirmed on appeal, 2008 QCCA 380, J.E. 2008-584), paras. 38; 50-51 and A.P.I. Alarm Inc. v. D’Arterio, [2009] O.J. No. 1599 (QL) (On. Sup. Ct.), para. 20.

[296] Written submission of Eli Lilly and Company and Eli Lilly Canada, Inc. (Competition Phase), paras. 292, 295-297; memorandum of argument of the defendant by counterclaim, Shionogi & Co. Ltd. (Re: Competition), paras. 118; 121-124.

[297] Ibid., Lilly paras. 298-303, Shionogi paras. 125-130.

[298] Memorandum of argument of the defendant, Apotex Inc. (Re : Competition), para. 302.

[299] Ibid., para. 306.

[300] Lilly amended statement of claim, January 11, 2001, para. 28.

[301] Memorandum of argument of the defendant, Apotex Inc. (Re: Competition), para. 313.

[302] 2005 FCA 361, [2006] 2 F.C.R. 477, para. 52.

[303] See 351694 Ontario Ltd. v. Paccar of Canada Ltd., 2004 FC 1565, (2004), 264 F.T.R. 12, para. 18.

[304] Nova Scotia Pharmaceutical Society, para. 72.

[305] Ibid., para. 99.

[306] Ibid., para. 106.

[307] Varied on appeal but not on this point as it was not pursued by the appellant, 2000 BCCA 463, (2000), B.C.A.C 1.

[308] Memorandum of argument of the defendant, Apotex Inc. (Re: Competition) para. 306.

[309] Lilly’s information as to the process actually used by Lupin was based on the closed portion of the Health Canada file it had received pursuant to an order of Justice Hugessen.

[310] See ruling contained in the transcript of the hearing held December 9, 2008.

[311] See Facts admitted to by the parties, LRTA # 82.

[312] Memorandum of argument of the defendant, Apotex Inc. (Re: Competition), para. 155.

[313] Ibid., para. 273.

[314] Resurfice Corp., at para. 25

[315] Oral submissions of counsel for Apotex, November 6, 2008, p. 20 lines 14-18.

[316] At para. 16.

[317] See Facts agreed to by the parties, LRTA # 150 and SRTA # 15(a); TX-265.

[318] Ibid., LRTA # 51.

[319] Ibid., LRTA # 151, SRTA 15(b); TX-266.

[320] Dr. Sherman testified that this choice was probably made by Apotex’s counsel at the time. (Cross-examination of Dr. Sherman, May 6, 2008 p. 125, lines 11-20) In the cross-examination of Dr. McClelland, Lilly pursued a line of questioning which could explain this decision (Cross-examination of Dr. McClelland, September 8, 2008, p. 52, line 18 to p. 53, line 19).

[321] See Facts agreed to by the parties, LRTA # 155, SRTA 15(c); TX-267.

[322] Ibid., SRTA # 17(b); TX-241.

[323] Ibid., LRTA 156; TX-118.

[324] Ibid., SRTA # 19(a); LRTA 160; TX-645; TX-246; TX-247.

[325] Ibid., SRTA # 19(c); confirmed on appeal, (1996), 199 N.R. 4, 68 C.P.R. (3d) 126.

[326] The applicant in these proceedings was Eli Lilly Canada Inc. Eli Lilly and Company and Shionogi & Co. Ltd, the owners of the Lilly and Shionogi patents, were joined to the proceedings pursuant to subs. 6(4) of the Regulations, having previously consented to the inclusion of their patents on the Form IV patent lists filed by Eli Lilly Canada Inc. pursuant to subs. 4(1) of the Regulations.

[327] See Facts agreed to by the parties, SRTA # 19(b); TX-644, Affidavit of Thomas L. Emmick sworn June 17, 1993.

[328] Ibid., ARTA # 220, LRTA # 205, SRTA # 48; TX-227 and TX-228.

[329] See Affidavit of Harry B. Radomski, sworn November 13, 2003 (TX-641), para. 4.

[330] Although there is a controversy as to whether or not Dr. Sherman ever met with Mr. McCool, it is uncontradicted that at least one such meeting took place between Mr. McCool and Mr. Kay.

[331] See TX-1684.

[332] See TX-261.

[333] The Court notes that Dr. Sherman testified that presumably it is assurances from Kyong Bo that it did not use the Lilly process that prompted Apotex to terminate the compulsory licence. (Cross-examination of Dr. Sherman, May 6, 2008, p. 132, line 22 to p. 133, line 12) However, the only evidence the Court has as to these assurances are contained in the letter from Pacific High Tech Canada, which is dated 10 days later than the notice of termination of the compulsory licence (see next para.).

[334] See TX-662; Facts agreed to by the parties, LRTA # 1; TX-334.

[335] See Facts agreed to by the parties, SRTA # 83(a) and (b).

[336] Ibid., LRTA 46; TX-119.

[337]Ibid, LRTA # 82; TX-651.

[338] Ibid., LRTA # 83, SRTA # 31; TX-1759.

[339] See TX-686.

[340] See Facts agreed to by the parties, SRTA # 70(a) and (c).

[341] See Statement of Claim dated June 18, 1997, para. 26.

[342] See Facts agreed to by the parties, LRTA # 83, SRTA # 31; TX-1759.

[343] See Glopec-16; Glopec-17.

[344] See Glopec-20.

[345] Ibid.; Glopec-23.

[346] See Glopec-22; Glopec-25.

[347] See TX-679.

[348] See TX-1656; While the agreement is silent on pricing, Apotex appears to have paid US$ 1 500 per kilogram of bulk cefaclor manufactured under it (see TX-1759), versus US$ 860 – 1 150 earlier. The cost for the bulk cefaclor contained in a 500 mg dose sold amounts, in the Court’s calculation, to US$ 0.75, compared with US$ 0.43 when the price was US$ 860 per kilogram. Such a dose would be sold in Canada by Apotex at a price of approximately CAN$ 1.50 (or between US$ 1.12 and US$ 0.97, calculated using the highest and lowest average monthly exchange rates posted for the November, 1996 to October, 1998 period) and distribution costs at Apotex represent 2 to 3 % of sales (Examination of Dr. Sherman, September 3, 2008, p. 40 lines 22-23; Re-examination of Mr. Fahner, September 3, 2008, p. 247 lines 8-9).

[349] See TX-662.

[350] See TX-663.

[351] See TX-664.

[352] See TX-1759.

[353] See Facts agreed to by the parties, LRTA # 93, 94, 95, 96, 100, 101, 103, 104, 108; SRTA # 72, 73, 74(b), 74(f), 75(a), 75(c), 76(a), 77(a).

[354] Ibid., ARTA 295.

[355] Submissions of Counsel for Apotex, November 6, 2008, p. 39 lines 5-12.

[356] Ibid., p. 39 line 14 – p. 40 line 21.

[357] Cross-examination of Mr. Kay, September 3, 2008, p. 214 line 4.

[358] See transcript of October 6, 2008, p. 183, line 12 to p. 184, line 3.

[359] Such as the PMNOC proceeding and the opinion of Mr. Radomski that an infringement suit would be imminent upon market entry.

[360] A price reflecting competition between Lilly and Shionogi in the bulk cefaclor market.

[361] See memorandum of the defendant Apotex Inc. (Re: infringement), para. 453.

[362] Submissions of Counsel for Apotex, November 6, 2008, p. 36 lines 20-23; p. 40 lines 12-14.

[363] Report-in-chief of Dr. Church. dated December 14, 2007 (Exhibit JC-2 of his affidavit of April 19, 2008 (A-24)), p. 29.

[364] Affidavit-in-chief of Dr. Ross, sworn December 14, 2007 (A-27), para. 34.

[365] Reply report of Dr. Church, dated March 28, 2008 (Exhibit JC-1 of his affidavit of March 31, 2008 (A-31)), para. 52); see also Affidavit-in-chief of Dr. Ross, Ibid., para. 34.

[366] It should be noted that the assignment concerns only Shionogi’s Canadian and U.S. patents (TX-228), while the evidence shows that patent applications were filed in other jurisdictions (see TX-233; Examination in chief of Mr. Takayuki Wada, September 15, 2008, p. 192, line 14 to p. 193, line 7), the Court has not been presented any evidence pertaining to Shionogi’s licensing behaviour in jurisdictions unaffected by the assignment.

[367] Responding affidavit of Dr. Cockburn, sworn February 27, 2008 (E-22), para. 111.

[368] Reply report of Dr. Church, dated March 28, 2008 (Exhibit JC-1 of his affidavit of March 31, 2008 (A-31)), para. 49; see also Affidavit-in-chief of Dr. Ross, sworn December 14, 2007 (A-27), para. 59.

## 22183:56 · paragraphs 1253-1269

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c65070502f476eeb60ccb0f6bdc0aa27ceb08658272e6d632d8be75ecf0a8687`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:56:subtheme:1 · paragraphs 1253-1269

- Raw key terms: `september, lines, cefaclor, examination, patents, sherman, apotex, cross-examination`
- Display key terms: `september, lines, cefaclor, examination, patents, sherman, apotex, cross-examination`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: september, lines, cefaclor, examination, patents, sherman, apotex, cross-examination Application context: [381] Obviously, this comment applies to patents owned by parties other than the originator or innovator, who was on the Canadian market with a competing product, given that, “[t]he corporate policy at Apotex was not in  Evidence spans paragraphs 1253-1269. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041502` offsets `110-118`; context: [373] In the same manner, even if the experts had the necessary expertise, which is contested, no such expert evidence is necessary to construe the decision of the Federal Court of Appeal in these proceedings or the 1975 agreement.
- Evidence: `reasoning_application` cue `applies` at chunk `5041510` offsets `30-37`; context: [381] Obviously, this comment applies to patents owned by parties other than the originator or innovator, who was on the Canadian market with a competing product, given that, “[t]he corporate policy at Apotex was not in favour of licensing in branded generics because our success was predicated on our ability to develop all of these generics independently.

#### Section text

[369] Re-examination of Dr. Sherman, September 3, 2008, p. 166 lines 19-22; see also Cross-examination of Dr. Sherman, September 3, 2008, p. 133 lines 17-25.

[370] The demand for dosage form cefaclor, by the time generic entry occurred, was in decline.

[371] This is not the market that Apotex experts thought was relevant nor is it the basis of their opinion.

[372] In his view, “[t]he patents were irrelevant.” (Cross-examination of Dr. Sherman, September 3, 2008 p. 134 line 7).

[373] In the same manner, even if the experts had the necessary expertise, which is contested, no such expert evidence is necessary to construe the decision of the Federal Court of Appeal in these proceedings or the 1975 agreement.

[374] One must not forget that their business for selling dosage cefaclor in Japan was worth approximately US$ 900 million annually.

[375] Cross-examination of Dr. Hollis, September 5, 2008, p. 95 lines 14-21.

[376] See memorandum of argument of the defendant, Apotex Inc. (Re: competition) paras. 242-269; written submission of Eli Lilly and Company and Eli Lilly Canada Inc. (competition phase) paras. 117-126; memorandum of argument of the defendant by counterclaim, Shionogi & Co. Ltd. paras. 25-43.

[377] TX-244.

[378] Ibid.

[379] See, for example, the examination of Mr. Pytynia, September 15, 2008, p. 17, lines 14-17; TX-237, 238, 240.

[380] Thereafter Dr. Ross simply assumed that Shionogi immediately pursued the opportunity offered by Lilly to assign its patents. If one accepts the assumption that Shionogi would be eager to commercialize its patents, it would have made good sense for Shionogi to start planning or to take steps before the expiration of the cefaclor patent and certainly immediately upon its expiration. In fact, Lilly approached Shionogi only several months later.

[381] Obviously, this comment applies to patents owned by parties other than the originator or innovator, who was on the Canadian market with a competing product, given that, “[t]he corporate policy at Apotex was not in favour of licensing in branded generics because our success was predicated on our ability to develop all of these generics independently.” (Examination of Jack Kay, September 3, 2008, p. 183 lines 8-12)

[382] See Facts agreed to by the parties, SRTA # 83(a) and (b).

[383] Examination of Dr. Sherman, September 3, 2008, p. 30 lines 6-8. This despite Dr. Sherman’s professed preference for a process whose patent holder is not the originator: “if there were patents in the hands of other people, such as Shionogi, which is often the case, and they were not the originator in Canada, if we wanted to use material made by that process, it would stand to reason that either they would have no reason to object or they would be glad to licence it” (Examination of Dr. Sherman, September 3, 2008, p. 32 lines 7-13).

[384] It is worth mentioning that Dr. Church, when asked to explain why and if it was truly important for his opinion that there would be only two known commercial processes, made it clear that it was crucial in the scenario he assumed as a basis for his opinion that all buyers of cefaclor know that there were only two commercially viable processes to make bulk cefaclor. (See Transcript of October 6, 2008, p. 183, line 18 to p. 184, line 2.)

[385] Examination of Dr. Sherman, September 3, 2008, p. 29 line 5 – p. 30 line 8.

## 22183:57 · paragraphs 1270-1280

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a9999a1faaad3f48c046da24ec0d6eb19ed1321bb5af2cae373caef686a77b46`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:57:subtheme:1 · paragraphs 1270-1280

- Raw key terms: `lines, september, apotex, cross-examination, sherman, discovery, july, line`
- Display key terms: `lines, september, apotex, cross-examination, sherman, discovery, july, line`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: lines, september, apotex, cross-examination, sherman, discovery, july, line No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 1270-1280. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

[386] Discovery of Dr. Sherman, July 11, 2006, p. 342 line 24 - p. 343 line 1.

[387] Cross-examination of Dr. Sherman, September 3, 2008, p. 67, lines 18-23.

[388] This seems to diminish the value of Dr. Ross’s theory as to Shionogi’s financial incentives to licence companies like Apotex. It is certainly clear that Dr. Ross did not consider this.

[389] Discovery of Dr. Sherman, July 11, 2006, p. 343 lines 7-11.

[390] Examination of Dr. Sherman, September 3, 2008, p. 33 lines 20-21.

[391] Along with many other suppliers whom had also submitted samples to Apotex (see Facts agreed to by the parties, LRTA #82).

[392] Counsel for Apotex, November 6, 2008 p. 114, line 15 to p. 134, line 6.

[393] See the tables at para. 294 of Apotex’s memorandum.

[394] Cross-examination of Dr. Church, September 9, 2008, p. 149, lines 17-21.

[395] Cross-examination of Dr. Ross, September 11, 2008, p. 160, lines 6-19.

[396] Cross-examination of Mr. Cole, September 10, 2008, p. 111 lines 15-25.

## 22183:58 · paragraphs 1281-1288

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2dc814227db7f2b1650257e34a4385adf2dfa30efbddafba853b8ed7106019de`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:58:subtheme:1 · paragraphs 1281-1288

- Raw key terms: `apotex, church, ibid, para, a-24, accounting, affidavit, apply`
- Display key terms: `apotex, church, ibid, para, a-24, accounting, affidavit, apply`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: apotex, church, ibid, para, a-24, accounting, affidavit, apply Application context: [402] This would obviously only apply if Lilly elected to seek damages based on its own profits instead of seeking an accounting of Apotex’s profits. Evidence spans paragraphs 1281-1288. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `apply` at chunk `5041531` offsets `32-37`; context: [402] This would obviously only apply if Lilly elected to seek damages based on its own profits instead of seeking an accounting of Apotex’s profits.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5041532` offsets `76-85`; context: Church, December 14, 2007 (Exhibit JC-2 of his affidavit of April 19, 2008 (A-24)), p.

#### Section text

[397] A price Apotex never had to pay given that it bought infringing bulk cefaclor until 1998 at which time the legal bulk cefaclor was obtained from a third source (Lupin).

[398] Examination of Dr. Church, September 9, 2008, p. 31, lines 4-7; cross-examination of Dr. Church, September 9, 2008, p. 160, lines 7-8 and p. 232, lines 22-24.

[399] See memorandum of argument of the defendant, Apotex Inc. (Re: Competition), para. 287.

[400] Other common law remedies exist where unjust enrichment may be more relevant.

[401] Ibid., para. 282.

[402] This would obviously only apply if Lilly elected to seek damages based on its own profits instead of seeking an accounting of Apotex’s profits.

[403] Report-in-chief of Dr. Church, December 14, 2007 (Exhibit JC-2 of his affidavit of April 19, 2008 (A-24)), p. 31.

[404] Ibid.

## 22183:59 · paragraphs 1289-1289

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4dc33dfc790bba073a14399719282e147c80ee3c2a7383f5ec488e3c3f718a16`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:59:subtheme:1 · paragraphs 1289-1289

- Raw key terms: `ibid`
- Display key terms: `ibid`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: ibid No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 1289-1289. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

[405] Ibid.

## 22183:60 · paragraphs 1290-1299

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d121b3e2dced2970aaf59bd4ad11fb8ae3c5b3fcfa1b16c663dae440d3499c3a`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22183:60:subtheme:1 · paragraphs 1290-1298

- Raw key terms: `apotex, competition, argument, assessment, defendant, line, memorandum, para`
- Display key terms: `apotex, competition, argument, assessment, line, memorandum, para`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule Display terms: apotex, competition, argument, assessment, line, memorandum, para Rule/authority context: [410] There would be no counterclaim under the Competition Act in the “but for world”. Evidence spans paragraphs 1290-1298. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5041538` offsets `67-75`; context: [409] Such as the correspondence Apotex sought to have admitted as evidence (TX-252 to 259).
- Evidence: `governing_rule` cue `under` at chunk `5041539` offsets `37-42`; context: [410] There would be no counterclaim under the Competition Act in the “but for world”.
- Evidence: `counterargument_limitation` cue `but` at chunk `5041542` offsets `667-670`; context: It is perfectly true that his decision is made in the context of a pre-existing breach of contract by the seller, in the sense that the breach of contract provided the occasion upon which the buyer makes his market judgment; but even if there had been no breach at all it would have still been possible for the buyer to have made the same decision.

#### 22183:60:subtheme:2 · paragraphs 1299-1299

- Raw key terms: `appeal, become, court, determine, exhausted, issues, keep, material`
- Display key terms: `become, determine, exhausted, issues, keep, material`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: become, determine, exhausted, issues, keep, material Evidence spans paragraphs 1299-1299. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5041544` offsets `72-78`; context: [415] The Court will keep all the material necessary to determine these issues until the rights of appeal have been exhausted in order to stand ready to determine them should it become necessary to do so.

#### Section text

[406] Cross-examination of Dr. Church, September 9, 2008, p. 215, line 18 to p. 216, line 12.

[407] The Court infers from Dr. Sherman’s qualified statement in that respect that Apotex would make an assessment at that stage.

[408] Memorandum of argument of the defendant, Apotex Inc. (Re: competition), para. 282.

[409] Such as the correspondence Apotex sought to have admitted as evidence (TX-252 to 259).

[410] There would be no counterclaim under the Competition Act in the “but for world”.

[411] Examination of Mr. Wada, September 15, 2008, p. 165, lines 17-18.

[412] Memorandum of argument of the defendant, Apotex Inc. (Re: competition), para. 287.

[413] In fact, albeit in a different context, Apotex’s decision is analogous to what was characterized by Justice Goff in Koch Marine Inc. v. D’Amica Societa di Navigazione A.R.L. ( The “Elena D’Amico”), [1980] 1 Lloyd’s L.R. 75 (Q.B. Comm. Div.) as a decision which results in the rupture of the causal link between a breach and a loss: “an independent decision, independent of the breach, made by the buyer on his assessment of the market. It is perfectly true that his decision is made in the context of a pre-existing breach of contract by the seller, in the sense that the breach of contract provided the occasion upon which the buyer makes his market judgment; but even if there had been no breach at all it would have still been possible for the buyer to have made the same decision.” (emphasis added, p. 89).

[414] Transcript of November 13, 2008, p. 201 line 19-20.

[415] The Court will keep all the material necessary to determine these issues until the rights of appeal have been exhausted in order to stand ready to determine them should it become necessary to do so.
