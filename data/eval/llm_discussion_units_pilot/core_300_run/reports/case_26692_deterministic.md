# Discussion Units: case 26692

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **58**
- Continuity pairs: **57**
- Discussion Units: **4**
- Paragraph source hashes: **58**
- Sub-themes: **16**

## 26692:1 · paragraphs 0-4

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7d99636ee1db92cfcc96f00e4c01681689e3ce93e5811a068b84b6713e6c9b8c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26692:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, canada, immigration, india, kaur, parmjit, persecution, actions`
- Display key terms: `india, kaur, parmjit, persecution, actions`
- Argument roles: `evidence_fact`
- Explanation: Observed roles: evidence_fact Display terms: india, kaur, parmjit, persecution, actions Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `testimony` at chunk `5254514` offsets `189-198`; context: [2] The Refugee Protection Division of the Immigration and Refugee Board of Canada (the Board) rejected her claim for protection after finding that her “basic story” was not plausible, her testimony was not credible, and her actions in the 17 months following her departure from India demonstrated a lack of subjective fear of persecution.

#### 26692:1:subtheme:2 · paragraphs 3-4

- Raw key terms: `application, board, chairperson, claimants, claims, consider, disagree, dismissed`
- Display key terms: `chairperson, claims, consider, disagree, dismissed`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: chairperson, claims, consider, disagree, dismissed Rule/authority context: She also submits that the Board erred by failing to properly consider her psychologist’s report, the Chairperson’s Guidelines on Women Refugee Claimants Fearing Gender-Related Persecution [Guidelines] and her claims unde Operative outcome context: For the reasons that follow, this application is dismissed. Evidence spans paragraphs 3-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5254515` offsets `286-291`; context: She also submits that the Board erred by failing to properly consider her psychologist’s report, the Chairperson’s Guidelines on Women Refugee Claimants Fearing Gender-Related Persecution [Guidelines] and her claims under section 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA].
- Evidence: `disposition` cue `dismissed` at chunk `5254516` offsets `65-74`; context: For the reasons that follow, this application is dismissed.

#### Section text

Kaur v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2012-11-28
Neutral citation
2012 FC 1379
File numbers
IMM-424-12
Notes
Reported Decision
Decision Content
Date: 20121128
Docket: IMM-424-12
Citation: 2012 FC 1379
Ottawa, Ontario, November 28, 2012
PRESENT: THE CHIEF JUSTICE
BETWEEN:
PARMJIT KAUR
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] The Applicant, Ms. Parmjit Kaur, is a citizen of India. Among other things, she alleges that she would face a serious risk of persecution, including physical harm and death, if she were required to return to India.

[2] The Refugee Protection Division of the Immigration and Refugee Board of Canada (the Board) rejected her claim for protection after finding that her “basic story” was not plausible, her testimony was not credible, and her actions in the 17 months following her departure from India demonstrated a lack of subjective fear of persecution.

[3] Ms. Kaur submits that the Board erred in reaching these findings. She also submits that the Board erred by failing to properly consider her psychologist’s report, the Chairperson’s Guidelines on Women Refugee Claimants Fearing Gender-Related Persecution [Guidelines] and her claims under section 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA].

[4] I disagree. For the reasons that follow, this application is dismissed.


## 26692:2 · paragraphs 5-54

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6e194eaefe83c9cb2971831ec89a127b4eee90e98f5fdb0e876914765de3fcf5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26692:2:subtheme:1 · paragraphs 5-8

- Raw key terms: `allegedly, home, kaur, police, arrested, hizbul, however, mujahideen`
- Display key terms: `allegedly, home, kaur, police, arrested, hizbul, however, mujahideen`
- Argument roles: `counterargument_limitation, governing_rule, party_position`
- Explanation: Observed roles: counterargument_limitation, governing_rule, party_position Display terms: allegedly, home, kaur, police, arrested, hizbul, however, mujahideen Position/evidence statements: She claims that she was suspected of having knowledge about the Hizbul Mujahideen and that she was beaten and humiliated at the police station. | She claimed refugee protection on October 29, 2010. Rule/authority context: The Decision under Review Evidence spans paragraphs 5-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `However` at chunk `5254517` offsets `379-386`; context: However, Salina and her brother were arrested.
- Evidence: `party_position` cue `claims` at chunk `5254518` offsets `86-92`; context: She claims that she was suspected of having knowledge about the Hizbul Mujahideen and that she was beaten and humiliated at the police station.
- Evidence: `counterargument_limitation` cue `However` at chunk `5254518` offsets `275-282`; context: However, once others in the community began to learn that she had been detained by the police, she began to be subjected to various forms of harassment and abuse that she submits amount to persecution.
- Evidence: `party_position` cue `claimed` at chunk `5254519` offsets `233-240`; context: She claimed refugee protection on October 29, 2010.
- Evidence: `governing_rule` cue `under` at chunk `5254519` offsets `298-303`; context: The Decision under Review

#### 26692:2:subtheme:2 · paragraphs 9-11

- Raw key terms: `board, issue, kaur, actions, allegations, arrival, asylum, basic`
- Display key terms: `kaur, actions, allegations, arrival, asylum, basic`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: kaur, actions, allegations, arrival, asylum, basic Position/evidence statements: Kaur’s actions following her departure from India demonstrated a lack of subjective fear, because (i) she failed to claim asylum in the United States during the 16 months that she lived there, and (ii) she failed to clai Application context: Kaur’s actions following her departure from India demonstrated a lack of subjective fear, because (i) she failed to claim asylum in the United States during the 16 months that she lived there, and (ii) she failed to clai Evidence spans paragraphs 9-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5254520` offsets `74-79`; context: [8] At the outset of its decision, the Board identified the determinative issue as being the credibility of Ms.
- Evidence: `issue` cue `issue` at chunk `5254521` offsets `23-28`; context: [9] In discussing this issue, the Board began by explaining why it had determined that her “basic story” was implausible.
- Evidence: `evidence_fact` cue `determined that` at chunk `5254521` offsets `71-86`; context: [9] In discussing this issue, the Board began by explaining why it had determined that her “basic story” was implausible.
- Evidence: `party_position` cue `claim` at chunk `5254522` offsets `146-151`; context: Kaur’s actions following her departure from India demonstrated a lack of subjective fear, because (i) she failed to claim asylum in the United States during the 16 months that she lived there, and (ii) she failed to claim refugee protection in Canada immediately upon her arrival in this country.
- Evidence: `reasoning_application` cue `because` at chunk `5254522` offsets `120-127`; context: Kaur’s actions following her departure from India demonstrated a lack of subjective fear, because (i) she failed to claim asylum in the United States during the 16 months that she lived there, and (ii) she failed to claim refugee protection in Canada immediately upon her arrival in this country.

#### 26692:2:subtheme:3 · paragraphs 12-17

- Raw key terms: `board, kaur, allegations, finding, findings, absence, adverse, applicable`
- Display key terms: `kaur, allegations, finding, findings, absence, adverse, applicable`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: kaur, allegations, finding, findings, absence, adverse, applicable Rule/authority context: Kaur’s claims under section 97 of the IRPA were the same as those she advanced in relation to her claim under section 96, the Board summarily rejected her claims under section 97, without further discussion. | [13] The standard of review applicable to the Board’s findings with respect to Ms. Evidence spans paragraphs 12-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5254523` offsets `153-159`; context: Kaur’s allegations involved how a woman in India may be treated as a result of certain types of rumours, the Board observed that the issues raised in her application were relevant to the Guidelines.
- Evidence: `evidence_fact` cue `evidence` at chunk `5254523` offsets `255-263`; context: However, in the absence of credible evidence that Ms.
- Evidence: `counterargument_limitation` cue `However` at chunk `5254523` offsets `219-226`; context: However, in the absence of credible evidence that Ms.
- Evidence: `governing_rule` cue `under` at chunk `5254524` offsets `119-124`; context: Kaur’s claims under section 97 of the IRPA were the same as those she advanced in relation to her claim under section 96, the Board summarily rejected her claims under section 97, without further discussion.
- Evidence: `governing_rule` cue `standard of review` at chunk `5254525` offsets `9-27`; context: [13] The standard of review applicable to the Board’s findings with respect to Ms.
- Evidence: `evidence_fact` cue `testimony` at chunk `5254526` offsets `133-142`; context: Kaur submitted that the Board erred by finding that two aspects of her allegations were implausible and by finding that her testimony was not credible.
- Evidence: `evidence_fact` cue `found that` at chunk `5254528` offsets `176-186`; context: The Board found that it was not plausible that the police would tell Ms.

#### 26692:2:subtheme:4 · paragraphs 18-24

- Raw key terms: `board, kaur, respect, based, fear, finding, findings, psychologist`
- Display key terms: `kaur, respect, based, fear, finding, findings, psychologist`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: kaur, respect, based, fear, finding, findings, psychologist Rule/authority context: Indeed, it is entirely consistent with the jurisprudence of this Court involving claims of a similar or shorter duration. Application context: [18] I am satisfied that it was entirely reasonable for the Board to conclude, based on the foregoing findings, that Ms. Evidence spans paragraphs 18-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5254529` offsets `624-631`; context: In particular, when asked at the outset of the Board's hearing whether she had ever experienced harassment or mistreatment on public transportation in India, Ms.
- Evidence: `evidence_fact` cue `testimony` at chunk `5254529` offsets `65-74`; context: Kaur’s testimony was not credible was reasonable.
- Evidence: `evidence_fact` cue `testimony` at chunk `5254530` offsets `154-163`; context: Kaur’s principal allegations and testimony were not credible.
- Evidence: `reasoning_application` cue `conclude` at chunk `5254530` offsets `69-77`; context: [18] I am satisfied that it was entirely reasonable for the Board to conclude, based on the foregoing findings, that Ms.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5254532` offsets `389-402`; context: Indeed, it is entirely consistent with the jurisprudence of this Court involving claims of a similar or shorter duration.
- Evidence: `evidence_fact` cue `record` at chunk `5254533` offsets `35-41`; context: [21] However, I would note for the record that the mere failure to claim refugee protection in Canada for a period of a few weeks after the claimant’s arrival in this country would not normally constitute a reasonable basis, in and of itself, for making a finding of lack of subjective fear, particularly when, as here, the applicant sought the assistance of counsel during that period.
- Evidence: `evidence_fact` cue `evidence` at chunk `5254534` offsets `113-121`; context: Kaur submitted that the Board erred by disregarding, failing to properly address or misapprehending the evidence set forth in the report of her psychologist, in the course of reaching its adverse findings with respect to her credibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `5254535` offsets `270-278`; context: The Board then referred to the psychologist’s evidence regarding her symptoms of Post-Traumatic Stress Disorder [PTSD] and observed that such evidence “does not mean that her symptoms are necessarily resulting from the reasons [that she identified].

#### 26692:2:subtheme:5 · paragraphs 25-30

- Raw key terms: `court, alberta, decisions, halifax, kaur, newfoundland, nurses, supreme`
- Display key terms: `alberta, decisions, halifax, kaur, newfoundland, nurses, supreme`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: alberta, decisions, halifax, kaur, newfoundland, nurses, supreme Rule/authority context: [28] In each of those more recent decisions, the Supreme Court essentially reiterated its teaching in Dunsmuir, above at para 48, that the reasonableness standard of review contemplates a level of deference that “imports | [29] Moreover, in Newfoundland Nurses, Alberta Teachers and Halifax, the Supreme Court elaborated upon the degree of deference and respect that is required when a Court is reviewing an administrative decision on a reason Evidence spans paragraphs 25-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5254536` offsets `130-137`; context: [24] On its face, this treatment of the psychologist’s report suggests that it may only have been taken into account in assessing whether it provided corroboration for Ms.
- Evidence: `governing_rule` cue `standard of review` at chunk `5254540` offsets `154-172`; context: [28] In each of those more recent decisions, the Supreme Court essentially reiterated its teaching in Dunsmuir, above at para 48, that the reasonableness standard of review contemplates a level of deference that “imports respect for the decision-making process of adjudicative bodies with regard to both the facts and the law” (Mowat, above at para 29; Newfoundland Nurses, above at para 11; Alberta Teachers, above at paras 53-54; and Halifax, above at para 51).
- Evidence: `governing_rule` cue `standard of review` at chunk `5254541` offsets `229-247`; context: [29] Moreover, in Newfoundland Nurses, Alberta Teachers and Halifax, the Supreme Court elaborated upon the degree of deference and respect that is required when a Court is reviewing an administrative decision on a reasonableness standard of review.

#### 26692:2:subtheme:6 · paragraphs 31-32

- Raw key terms: `above, basis, court, decision, justice, speaking, abella, acceptable`
- Display key terms: `above, basis, justice, speaking, abella, acceptable`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: above, basis, justice, speaking, abella, acceptable Rule/authority context: ” She also noted that it is not necessary for an administrative tribunal’s reasons to address “all the arguments, statutory provisions, jurisprudence or other details the reviewing judge would have preferred,” to withsta Evidence spans paragraphs 31-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5254542` offsets `908-915`; context: Rather, reasons will be sufficient if they allow the reviewing court to understand why the decision was made and permit the court to determine whether the conclusion is within a range of acceptable outcomes.
- Evidence: `evidence_fact` cue `record` at chunk `5254542` offsets `1101-1107`; context: Justice Abella added that “courts should not substitute their own reasons, but they may, if they find it necessary, look to the record for the purposes of assessing the reasonableness of the outcome.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5254542` offsets `636-649`; context: ” She also noted that it is not necessary for an administrative tribunal’s reasons to address “all the arguments, statutory provisions, jurisprudence or other details the reviewing judge would have preferred,” to withstand a review under a reasonableness standard.
- Evidence: `counterargument_limitation` cue `but` at chunk `5254542` offsets `1048-1051`; context: Justice Abella added that “courts should not substitute their own reasons, but they may, if they find it necessary, look to the record for the purposes of assessing the reasonableness of the outcome.

#### 26692:2:subtheme:7 · paragraphs 33-34

- Raw key terms: `basis, court, above, address, administrative, aside, board, circumstances`
- Display key terms: `basis, above, address, administrative, aside, circumstances`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: basis, above, address, administrative, aside, circumstances Rule/authority context: [33] In my view, this recent jurisprudence from the Supreme Court has significantly reduced the scope for setting aside decisions of the Board on the basis that it did not consider or did not sufficiently consider the co Evidence spans paragraphs 33-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5254544` offsets `133-140`; context: [32] In Halifax, above at paras 45-49, Justice Cromwell, speaking for a unanimous Court, stated that “the reviewing court should ask whether there was any reasonable basis on the law or the evidence” for the conclusion reached by the administrative tribunal.
- Evidence: `evidence_fact` cue `evidence` at chunk `5254544` offsets `190-198`; context: [32] In Halifax, above at paras 45-49, Justice Cromwell, speaking for a unanimous Court, stated that “the reviewing court should ask whether there was any reasonable basis on the law or the evidence” for the conclusion reached by the administrative tribunal.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5254545` offsets `29-42`; context: [33] In my view, this recent jurisprudence from the Supreme Court has significantly reduced the scope for setting aside decisions of the Board on the basis that it did not consider or did not sufficiently consider the contents of a psychologist’s report.

#### 26692:2:subtheme:8 · paragraphs 35-39

- Raw key terms: `adverse, credibility, basis, board, finding, reasonable, report, conclusion`
- Display key terms: `adverse, credibility, basis, finding, reasonable, report, conclusion`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: adverse, credibility, basis, finding, reasonable, report, conclusion Rule/authority context: [37] For example, the fact that the report may, as in this case, state that an applicant’s PTSD, or other condition, causes the applicant to be fragile, confused, anxious, distressed or emotional during questioning, or t Evidence spans paragraphs 35-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5254546` offsets `427-435`; context: This is true even if the evidence in question is not specifically mentioned, or is only partially addressed, in the Board’s decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `5254546` offsets `60-68`; context: [34] If the Court can ascertain any reasonable basis in the evidence for the Board’s adverse credibility findings, or if those findings can be said to be rationally supported, for example, on the basis of confirmed and important inconsistencies, contradictions or omissions [ICOs] in the evidence, those findings should ordinarily withstand the Court’s review (Dunsmuir, above at para 41).
- Evidence: `evidence_fact` cue `evidence` at chunk `5254547` offsets `97-105`; context: [35] Where the Board has based an adverse credibility finding upon ICOs in a refugee applicant’s evidence, that finding will ordinarily enable the Court to determine why the finding was made.
- Evidence: `evidence_fact` cue `record` at chunk `5254548` offsets `232-238`; context: [36] The fact that there may be something in the psychologist’s report which provides an alternative potential explanation for all or some of the ICOs will not change the fact that those ICOs, once confirmed through a review of the record, provide a reasonable basis, or rational support, for the Board’s adverse credibility finding and its ultimate conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5254549` offsets `233-238`; context: [37] For example, the fact that the report may, as in this case, state that an applicant’s PTSD, or other condition, causes the applicant to be fragile, confused, anxious, distressed or emotional during questioning, or to dissociate under stress, ordinarily would not reasonably explain a failure to mention an important aspect of the applicant’s story in his or her PIF.
- Evidence: `evidence_fact` cue `evidence` at chunk `5254550` offsets `496-504`; context: That is to say, this would be inconsistent with the Supreme Court’s position that reviewing courts should not interfere when there is any reasonable basis in the evidence for the conclusion reached by the Board, or when the decision can be rationally supported.

#### 26692:2:subtheme:9 · paragraphs 40-43

- Raw key terms: `board, kaur, adverse, course, credibility, decision, evidence, finding`
- Display key terms: `kaur, adverse, course, credibility, finding`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: kaur, adverse, course, credibility, finding Evidence spans paragraphs 40-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5254551` offsets `646-653`; context: However, the Board’s failure to explicitly mention in its decision whether it considered those conditions in making its adverse credibility finding did not deprive that decision of either its rational support or a reasonable basis in the evidence.
- Evidence: `evidence_fact` cue `testimony` at chunk `5254551` offsets `491-500`; context: Kaur’s testimony was contradictory and continued to grow throughout the course of the hearing.
- Evidence: `counterargument_limitation` cue `However` at chunk `5254551` offsets `579-586`; context: However, the Board’s failure to explicitly mention in its decision whether it considered those conditions in making its adverse credibility finding did not deprive that decision of either its rational support or a reasonable basis in the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5254553` offsets `92-100`; context: Kaur submitted that the Board erred by concluding that, in the absence of credible evidence that she faced gender-based persecution in India, the Guidelines were not applicable to her situation.

#### 26692:2:subtheme:10 · paragraphs 44-45

- Raw key terms: `board, guidelines, however, allegations, applicable, assessment, binding, claims`
- Display key terms: `guidelines, however, allegations, applicable, assessment, binding, claims`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: guidelines, however, allegations, applicable, assessment, binding, claims Evidence spans paragraphs 44-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5254555` offsets `83-89`; context: Kaur’s allegations raised issues that are relevant to the Guidelines.
- Evidence: `counterargument_limitation` cue `However` at chunk `5254555` offsets `127-134`; context: However, given that it found those allegations to be not credible, it concluded that the Guidelines were not applicable to her situation.
- Evidence: `counterargument_limitation` cue `However` at chunk `5254556` offsets `91-98`; context: However, they are not law, nor are they binding for the Board.

#### 26692:2:subtheme:11 · paragraphs 46-50

- Raw key terms: `kaur, section, board, allegations, credible, found, guidelines, claim`
- Display key terms: `kaur, section, allegations, credible, guidelines`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: kaur, section, allegations, credible, guidelines Rule/authority context: Kaur’s claims under section 97 | Kaur submitted that the Board failed to assess her claim under section 97 of the IRPA. Application context: However, none of those problems applied to Ms. Evidence spans paragraphs 46-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5254557` offsets `290-296`; context: However, once again, the issues discussed in that section of the Guidelines were not relevant to Ms.
- Evidence: `reasoning_application` cue `applied` at chunk `5254557` offsets `174-181`; context: However, none of those problems applied to Ms.
- Evidence: `counterargument_limitation` cue `However` at chunk `5254557` offsets `142-149`; context: However, none of those problems applied to Ms.
- Evidence: `issue` cue `issues` at chunk `5254558` offsets `250-256`; context: Kaur did, in fact, raise issues relevant to the Guidelines.
- Evidence: `governing_rule` cue `under` at chunk `5254559` offsets `430-435`; context: Kaur’s claims under section 97
- Evidence: `governing_rule` cue `under` at chunk `5254560` offsets `75-80`; context: Kaur submitted that the Board failed to assess her claim under section 97 of the IRPA.
- Evidence: `governing_rule` cue `under` at chunk `5254561` offsets `112-117`; context: Kaur under section 97.

#### 26692:2:subtheme:12 · paragraphs 51-54

- Raw key terms: `board, claims, section, above, allegations, analysis, kaur, made`
- Display key terms: `claims, section, above, allegations, analysis, kaur, made`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: claims, section, above, allegations, analysis, kaur, made Rule/authority context: [50] The Board is not obliged to conduct a separate analysis under section 97 in each case. | Kaur in support of her claims under section 97 were the same as those that she advanced in support of her claims under section 96, the Board was under no obligation to undertake a second analysis of those claims under se Application context: [53] Accordingly, this application is dismissed. Operative outcome context: [53] Accordingly, this application is dismissed. Evidence spans paragraphs 51-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `5254562` offsets `92-99`; context: Whether it has an obligation to do so will depend on the particular circumstances of each case (Kandiah v Canada (Minister of Citizenship and Immigration), 2005 FC 181 at para 16, 137 ACWS (3d) 604).
- Evidence: `evidence_fact` cue `evidence` at chunk `5254562` offsets `326-334`; context: Where no claims have been made or evidence adduced that would warrant such a separate analysis, one will not be required (Brovina v Canada (Minister of Citizenship and Immigration), 2004 FC 635 at paras 17-18, 254 FTR 244; Velez, above at paras 48-51).
- Evidence: `governing_rule` cue `under` at chunk `5254562` offsets `61-66`; context: [50] The Board is not obliged to conduct a separate analysis under section 97 in each case.
- Evidence: `evidence_fact` cue `found that` at chunk `5254563` offsets `286-296`; context: Kaur in support of her claims under section 97 were the same as those that she advanced in support of her claims under section 96, the Board was under no obligation to undertake a second analysis of those claims under section 97, once it had found that her allegations were not credible.
- Evidence: `governing_rule` cue `under` at chunk `5254563` offsets `74-79`; context: Kaur in support of her claims under section 97 were the same as those that she advanced in support of her claims under section 96, the Board was under no obligation to undertake a second analysis of those claims under section 97, once it had found that her allegations were not credible.
- Evidence: `governing_rule` cue `under` at chunk `5254564` offsets `452-457`; context: Kaur’s credibility as a witness, or (ii) reconsider her allegations a second time, in the context of making its assessment of her claims under section 97.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5254565` offsets `5-16`; context: [53] Accordingly, this application is dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `5254565` offsets `38-47`; context: [53] Accordingly, this application is dismissed.

#### Section text

I. Background

[5] Ms. Kaur is 30 years old and of Sikh ethnicity. In December 2008, she was visited by a Muslim friend from college (Salina), Salina’s brother and a friend of his. On their way back to their home town from this visit, Salina and the two men were allegedly stopped at a police check. Her brother’s friend, who was suspected to be associated with the Hizbul Mujahideen, escaped. However, Salina and her brother were arrested. During questioning, they informed the police that they and the brother’s friend had stayed at Ms. Kaur’s home.

[6] Later that month, police from Ms. Kaur’s home village allegedly arrested her. She claims that she was suspected of having knowledge about the Hizbul Mujahideen and that she was beaten and humiliated at the police station. After her father paid a bribe, she was released. However, once others in the community began to learn that she had been detained by the police, she began to be subjected to various forms of harassment and abuse that she submits amount to persecution.

[7] The police allegedly raided Ms. Kaur’s home on June 4, 2009, when she was not present. On June 9, 2009, she departed for the United States. She lived in the State of Washington until October 2, 2010, when she came to Canada. She claimed refugee protection on October 29, 2010.
II. The Decision under Review

[8] At the outset of its decision, the Board identified the determinative issue as being the credibility of Ms. Kaur’s allegations.

[9] In discussing this issue, the Board began by explaining why it had determined that her “basic story” was implausible. The Board then discussed various reasons why it found her testimony to be not credible.

[10] The Board noted that Ms. Kaur’s actions following her departure from India demonstrated a lack of subjective fear, because (i) she failed to claim asylum in the United States during the 16 months that she lived there, and (ii) she failed to claim refugee protection in Canada immediately upon her arrival in this country.

[11] Given that Ms. Kaur’s allegations involved how a woman in India may be treated as a result of certain types of rumours, the Board observed that the issues raised in her application were relevant to the Guidelines. However, in the absence of credible evidence that Ms. Kaur faced gender-related persecution in India, the Board stated that those guidelines were not applicable to her situation.

[12] Finally, given its adverse credibility findings and the fact that the allegations in support of Ms. Kaur’s claims under section 97 of the IRPA were the same as those she advanced in relation to her claim under section 96, the Board summarily rejected her claims under section 97, without further discussion.
III. Standard of Review

[13] The standard of review applicable to the Board’s findings with respect to Ms. Kaur’s credibility and her lack of subjective fear is reasonableness. The same is true with respect to the Board’s treatment of the report prepared by Ms. Kaur’s psychologist, the Guidelines and her claims under section 97 of the IRPA. (Dunsmuir v New Brunswick, 2008 SCC 9 at paras 51-55, [2008] 1 SCR 190 [Dunsmuir]; Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at paras 46-47, [2009] 1 SCR 339; and Velez v Canada (Minister of Citizenship and Immigration) 2010 FC 923 at paras 22-23 (available on CanLII) [Velez]).
IV. Analysis
A. The Board’s adverse credibility findings

[14] Ms. Kaur submitted that the Board erred by finding that two aspects of her allegations were implausible and by finding that her testimony was not credible.

[15] I agree that the Board’s two implausibility findings were not reasonable. The first such finding concerned Ms. Kaur’s statement that, after the police came to her house, she never spoke to her friend Salina again. In my view, it was unreasonable for the Board to find that statement to be implausible. If Ms. Kaur did, in fact, believe that she had been betrayed by her friend Salina, it is entirely understandable that she might not have spoken with her again. Common experience reflects that such behaviour is not uncommon, and certainly is not implausible.

[16] The second implausibility finding concerned Ms. Kaur’s assertion that her source for certain key information in her allegations was the police who arrested her. The Board found that it was not plausible that the police would tell Ms. Kaur that the information they were accusing her of was secured through torture. I respectfully disagree. This finding was unreasonable, particularly in the absence of any discussion of how police in India behave.

[17] However, in my view, the Board’s conclusion that Ms. Kaur’s testimony was not credible was reasonable. That conclusion was based largely on findings that the Board made with respect to (i) inconsistencies and other problems that it identified with respect to Ms. Kaur’s testimony, and (ii) the absence of important aspects of her allegations in the Personal Information Form [PIF] part of her application. The principle findings in this regard were as follows:
i. Her testimony was contradictory and continued to grow throughout the course of the hearing. In particular, when asked at the outset of the Board's hearing whether she had ever experienced harassment or mistreatment on public transportation in India, Ms. Kaur replied in the negative. However, after it was pointed out to her that country documentation indicates that women in India are sometimes harassed on public transportation, she then stated that people would point her out and call her demeaning names. It was only after being asked whether she experienced anything worse than being called names that she mentioned that small children threw stones at her. Later in the hearing, when pressed again on this point, she added that some people had stated that she had no right to live and should be killed. When further pressed, she then stated that “the society threw stones” at her and tried to kill her. These important allegations were not mentioned in Ms. Kaur’s PIF, which simply noted that people called her “by different bad and humiliating names.”
ii. She could not reasonably explain how people who had never seen her before and who did not know her by name were able to associate her with the rumours allegedly going around.

[18] I am satisfied that it was entirely reasonable for the Board to conclude, based on the foregoing findings, that Ms. Kaur’s principal allegations and testimony were not credible. That conclusion was well “within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” and was appropriately justified, transparent and intelligible (Dunsmuir, above at para 47).
B. The Board’s conclusion with respect to subjective fear

[19] Ms. Kaur submitted that the Board’s finding with respect to her absence of subjective fear was unreasonable. I disagree.

[20] That finding was made based on the fact that Ms. Kaur failed to claim refugee protection during the 16 month period that she lived in United States and then failed to claim such protection immediately upon her arrival in Canada. In my view, given the long duration of her stay in the United States, the Board’s finding was not unreasonable. Indeed, it is entirely consistent with the jurisprudence of this Court involving claims of a similar or shorter duration. (See, for example, Duarte v Canada (Minister of Citizenship and Immigration), 2003 FC 988 at paras 14-15, 125 ACWS (3d) 137; Espinosa v Canada (Minister of Citizenship and Immigration), 2003 FC 1324 at para 17, 127 ACWS (3d) 329; Fernando v Canada (Minister of Citizenship and Immigration), 2001 FCT 759 at para 3, 107 ACWS (3d) 115; Castillejos v Canada (Minister of Citizenship and Immigration) (1994), 52 ACWS (3d) 614 at para 12 (available on QL) (TD); and Huerta v Canada (Minister of Employment and Immigration) (1993), 40 ACWS (3d) 487, 157 NR 225 (CA)).

[21] However, I would note for the record that the mere failure to claim refugee protection in Canada for a period of a few weeks after the claimant’s arrival in this country would not normally constitute a reasonable basis, in and of itself, for making a finding of lack of subjective fear, particularly when, as here, the applicant sought the assistance of counsel during that period.
C. The Board’s treatment of the psychologist’s report

[22] Ms. Kaur submitted that the Board erred by disregarding, failing to properly address or misapprehending the evidence set forth in the report of her psychologist, in the course of reaching its adverse findings with respect to her credibility. I disagree.

[23] In its decision, the Board noted that Ms. Kaur had visited a psychologist on two occasions shortly before the hearing and had provided information to the psychologist, which was summarized in the psychologist’s report. The Board then referred to the psychologist’s evidence regarding her symptoms of Post-Traumatic Stress Disorder [PTSD] and observed that such evidence “does not mean that her symptoms are necessarily resulting from the reasons [that she identified].” The Board also noted that the psychologist had obtained the information about what had allegedly occurred in India from Ms. Kaur herself, and that in view of the credibility concerns it had identified with respect to Ms. Kaur’s testimony, it had decided to give no weight to the psychologist’s report, in terms of corroborating those alleged events.

[24] On its face, this treatment of the psychologist’s report suggests that it may only have been taken into account in assessing whether it provided corroboration for Ms. Kaur’s allegations, and may not have been taken into account in assessing Ms. Kaur’s credibility as a witness.

[25] Ms. Kaur submits that the Board was obliged to specifically consider the psychologist’s report in its assessment of her credibility, and that its failure to demonstrate in its reasons that it did so constitutes a reviewable error.

[26] In support of her position, Ms. Kaur relied upon this Court’s decisions in Csonka v Canada (Minister of Citizenship and Immigration), 2001 FCT 915 at para 29, 107 ACWS (3d) 851 (TD); Khawaja v Canada (The Minister of Citizenship and Immigration) (1999), 172 FTR 287, 92 ACWS (3d) 672; Rudaragi v Canada (Minister of Citizenship and Immigration), 2006 FC 911 at para 6 (available on CanLII); Atay v Canada (Minister of Citizenship and Immigration), 2008 FC 201 at paras 30-32, 165 ACWS (3d) 319; and Mico v Canada (Minister of Citizenship and Immigration), 2011 FC 964 at paras 49-56, 1 Imm. LR (4th) 1 [Mico].

[27] However, all but the last of those decisions predate Dunsmuir, above; and the remaining case (Mico, above) predates the Supreme Court’s decisions in Canada (Canadian Human Rights Commission) v Canada (Attorney General), 2011 SCC 53, [2011] 3 SCR 471 [Mowat]; Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62, [2011] 3 SCR 708 [Newfoundland Nurses]; Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association 2011 SCC 61, [2011] 3 SCR 654 [Alberta Teachers]; and Halifax (Regional Municipality) v Nova Scotia (Human Rights Commission), 2012 SCC 10, [2012] 1 SCR 364 [Halifax].

[28] In each of those more recent decisions, the Supreme Court essentially reiterated its teaching in Dunsmuir, above at para 48, that the reasonableness standard of review contemplates a level of deference that “imports respect for the decision-making process of adjudicative bodies with regard to both the facts and the law” (Mowat, above at para 29; Newfoundland Nurses, above at para 11; Alberta Teachers, above at paras 53-54; and Halifax, above at para 51).

[29] Moreover, in Newfoundland Nurses, Alberta Teachers and Halifax, the Supreme Court elaborated upon the degree of deference and respect that is required when a Court is reviewing an administrative decision on a reasonableness standard of review.

[30] In Newfoundland Nurses, above at paras 12-17, Justice Abella, speaking for a unanimous Court, rejected the proposition that the “adequacy” of reasons is a stand-alone basis for quashing a decision and she endorsed the view that a reviewing court must first seek to supplement reasons before seeking to subvert them. In this regard, she observed that judges should “be cautious about substituting their own view of the proper outcome by designating certain omissions in the reasons to be fateful.” She also noted that it is not necessary for an administrative tribunal’s reasons to address “all the arguments, statutory provisions, jurisprudence or other details the reviewing judge would have preferred,” to withstand a review under a reasonableness standard. Rather, reasons will be sufficient if they allow the reviewing court to understand why the decision was made and permit the court to determine whether the conclusion is within a range of acceptable outcomes. Justice Abella added that “courts should not substitute their own reasons, but they may, if they find it necessary, look to the record for the purposes of assessing the reasonableness of the outcome.”

[31] In Alberta Teachers, above at para 53, Justice Rothstein, speaking for the majority of the Court, stated: “If there exists a reasonable basis upon which the decision maker could have decided as it did, the court must not interfere.”

[32] In Halifax, above at paras 45-49, Justice Cromwell, speaking for a unanimous Court, stated that “the reviewing court should ask whether there was any reasonable basis on the law or the evidence” for the conclusion reached by the administrative tribunal. Stated differently, he observed that “a result reached by an administrative tribunal is reasonable where it can be ‘rationally supported’,” and that a “reasonableness review must focus primarily upon whether there is any basis in reason” for the tribunal’s decision.

[33] In my view, this recent jurisprudence from the Supreme Court has significantly reduced the scope for setting aside decisions of the Board on the basis that it did not consider or did not sufficiently consider the contents of a psychologist’s report. It has also significantly narrowed the range of potential circumstances in which the Board may be said to have an obligation to explicitly consider and address, in its reasons, the contents of a psychologist’s report in making credibility findings.

[34] If the Court can ascertain any reasonable basis in the evidence for the Board’s adverse credibility findings, or if those findings can be said to be rationally supported, for example, on the basis of confirmed and important inconsistencies, contradictions or omissions [ICOs] in the evidence, those findings should ordinarily withstand the Court’s review (Dunsmuir, above at para 41). This is true even if the evidence in question is not specifically mentioned, or is only partially addressed, in the Board’s decision.

[35] Where the Board has based an adverse credibility finding upon ICOs in a refugee applicant’s evidence, that finding will ordinarily enable the Court to determine why the finding was made. If those ICOs are important and confirmed upon a review of the underlying evidentiary record, the Board’s reasons and that record will ordinarily enable the Court to be satisfied that the finding and the ultimate conclusion reached by the Board fall within a range of acceptable outcomes. These determinations should suffice to enable the Board’s finding to withstand scrutiny (Newfoundland Nurses, above at para 16), unless there is something in a psychologist’s report that strongly suggests that the adverse credibility finding is in fact unreasonable.

[36] The fact that there may be something in the psychologist’s report which provides an alternative potential explanation for all or some of the ICOs will not change the fact that those ICOs, once confirmed through a review of the record, provide a reasonable basis, or rational support, for the Board’s adverse credibility finding and its ultimate conclusion. This is particularly so when the psychologist’s report only provides a partial explanation for some of the ICOs.

[37] For example, the fact that the report may, as in this case, state that an applicant’s PTSD, or other condition, causes the applicant to be fragile, confused, anxious, distressed or emotional during questioning, or to dissociate under stress, ordinarily would not reasonably explain a failure to mention an important aspect of the applicant’s story in his or her PIF. This is especially so when the PIF was prepared with the assistance of counsel. Having regard to the above-mentioned teachings in Newfoundland Nurses, Alberta Teachers and Halifax, it is also not immediately apparent how such psychological conditions might suffice to deprive an adverse credibility finding that was based on flagrant contradictions or important discrepancies of its rational support or to deprive it of any reasonable basis.

[38] In my view, unless there is something in a psychologist’s report which strongly suggests that an adverse credibility finding made by the Board was unreasonable, it would be inconsistent with the Supreme Court’s teachings to require the Board to specifically address the report or anything in the report in making such a finding. That is to say, this would be inconsistent with the Supreme Court’s position that reviewing courts should not interfere when there is any reasonable basis in the evidence for the conclusion reached by the Board, or when the decision can be rationally supported. It would also be inconsistent with the emphasis that the Supreme Court has now repeatedly given to the need for reviewing courts to give respectful deference to the findings of administrative tribunals. This is particularly so with respect to matters of credibility, which “are at the very heart of the task Parliament has chose to leave to the [Board]” (Rahal v Canada (Minister of Citizenship and Immigration), 2012 FC 319 at para 60 (available on CanLII)).

[39] In this case, there was nothing in the psychologist’s report which strongly suggested that the Board’s adverse credibility finding was unreasonable. There was also nothing that would have explained Ms. Kaur’s failure to mention important aspects of her allegations in her PIF, such as that people had tried to kill her and would threaten to do so again in the future. I recognize that psychological conditions described in the report provided a potential explanation for why Ms. Kaur’s testimony was contradictory and continued to grow throughout the course of the hearing. However, the Board’s failure to explicitly mention in its decision whether it considered those conditions in making its adverse credibility finding did not deprive that decision of either its rational support or a reasonable basis in the evidence.

[40] It follows that it was not unreasonable for the Board to have failed to specifically address the psychologist’s report in the course of making its adverse credibility finding. The fact that the Board did in fact mention the psychologist’s report elsewhere in its decision simply served to further insulate the decision from intervention by this Court (Cepeda-Gutierrez v Canada (Minister of Citizenship and Immigration), [1998] FCJ No 1425, at para 28).
D. The Board’s treatment of the Guidelines

[41] Ms. Kaur submitted that the Board erred by concluding that, in the absence of credible evidence that she faced gender-based persecution in India, the Guidelines were not applicable to her situation. I disagree.

[42] This submission was baldly stated in Ms. Kaur’s written submissions and not mentioned at all in the oral submissions made by her counsel.

[43] The Board specifically noted that the nature of Ms. Kaur’s allegations raised issues that are relevant to the Guidelines. However, given that it found those allegations to be not credible, it concluded that the Guidelines were not applicable to her situation.

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 26692:3 · paragraphs 55-56

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0c2d919b29fb03e509cd3ac2ae29b3ddbad651813ba437d9b8e08d5d5745e041`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26692:3:subtheme:1 · paragraphs 55-56

- Raw key terms: `adjuges, application, august, british, cause, certification, chief, citizenship`
- Display key terms: `adjuges, august, british, certification, chief`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: adjuges, august, british, certification, chief Operative outcome context: JUDGMENT THIS COURT ORDERS AND ADJUGES THAT this application is dismissed. Evidence spans paragraphs 55-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5254565` offsets `136-144`; context: There is no question for certification.
- Evidence: `disposition` cue `dismissed` at chunk `5254565` offsets `113-122`; context: JUDGMENT
THIS COURT ORDERS AND ADJUGES THAT this application is dismissed.

#### Section text

JUDGMENT
THIS COURT ORDERS AND ADJUGES THAT this application is dismissed.
There is no question for certification.
“Paul S. Crampton”
Chief Justice
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-424-12
STYLE OF CAUSE: PARMJIT KAUR
v THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
PLACE OF HEARING: Vancouver, British Columbia
DATE OF HEARING: August 21, 2012
REASONS FOR 

## 26692:4 · paragraphs 57-57

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3224efd4c3d438789c572314b8ee408e856125196ff0d51e979d297df9260bda`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26692:4:subtheme:1 · paragraphs 57-57

- Raw key terms: `appearances, applicant, attorney, baldev, barrister, british, canada, colombia`
- Display key terms: `baldev, barrister, british, colombia`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: baldev, barrister, british, colombia No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 57-57. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: Crampton CJ.
DATED: November 28, 2012
APPEARANCES:
Baldev Sandhu
FOR THE APPLICANT
Jennifer Dagsvik
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Baldev Sandhu
Barrister & Solicitor
Vancouver, British Columbia
FOR THE APPLICANT
William F. Pentney
Deputy Attorney General of Canada
Vancouver, British Colombia
FOR THE RESPONDENT
