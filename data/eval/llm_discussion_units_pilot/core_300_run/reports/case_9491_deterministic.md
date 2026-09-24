# Discussion Units: case 9491

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **31**
- Continuity pairs: **30**
- Discussion Units: **4**
- Paragraph source hashes: **31**
- Sub-themes: **8**

## 9491:1 · paragraphs 0-7

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1de3872834b5ba3d2716bc103e81f765202453796890d138d8fd78ec32dad180`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9491:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `applicant, canada, casino, court, decision, decisions, general, hideq`
- Display key terms: `casino, decisions, hideq`
- Argument roles: `disposition, reasoning_application`
- Explanation: Observed roles: disposition, reasoning_application Display terms: casino, decisions, hideq Application context: [3] He applied for CPP disability benefits in October 2010. Operative outcome context: The application was denied both initially and upon reconsideration. Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `4479889` offsets `7-14`; context: [3] He applied for CPP disability benefits in October 2010.
- Evidence: `disposition` cue `denied` at chunk `4479889` offsets `80-86`; context: The application was denied both initially and upon reconsideration.

#### 9491:1:subtheme:2 · paragraphs 4-5

- Raw key terms: `appeal, court, decision, hideq, leave, sst-ad, above, alleged`
- Display key terms: `hideq, leave, sst-ad, above, alleged`
- Argument roles: `counterargument_limitation, disposition, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, issue Display terms: hideq, leave, sst-ad, above, alleged Operative outcome context: The respondent takes issue with the remedy being sought, arguing that if the application is granted the appropriate remedy would be to remit that matter back to the SST-AD for re-determination of the leave to appeal ques Evidence spans paragraphs 4-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4479890` offsets `207-212`; context: The respondent takes issue with the remedy being sought, arguing that if the application is granted the appropriate remedy would be to remit that matter back to the SST-AD for re-determination of the leave to appeal question.
- Evidence: `disposition` cue `granted` at chunk `4479890` offsets `278-285`; context: The respondent takes issue with the remedy being sought, arguing that if the application is granted the appropriate remedy would be to remit that matter back to the SST-AD for re-determination of the leave to appeal question.
- Evidence: `issue` cue `whether` at chunk `4479891` offsets `264-271`; context: The SST-GD decision has been considered in the process of assessing whether the SST-AD committed a reviewable error or rendered an unreasonable decision.
- Evidence: `counterargument_limitation` cue `However` at chunk `4479891` offsets `84-91`; context: However, as noted above the decision before this Court is that of the SST-AD denying Mr.

#### 9491:1:subtheme:3 · paragraphs 6-7

- Raw key terms: `appeal, application, decision, issue, leave, sst-ad, basis, chance`
- Display key terms: `leave, sst-ad, basis, chance`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: leave, sst-ad, basis, chance Application context: Having considered the party’s written and oral submissions I can find no basis to interfere with the SST-AD’s decision and therefore dismiss the application for judicial review. Evidence spans paragraphs 6-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `4479892` offsets `463-468`; context: Issue
- Evidence: `reasoning_application` cue `therefore` at chunk `4479892` offsets `404-413`; context: Having considered the party’s written and oral submissions I can find no basis to interfere with the SST-AD’s decision and therefore dismiss the application for judicial review.
- Evidence: `issue` cue `issue` at chunk `4479893` offsets `13-18`; context: [7] The sole issue raised in this application is whether the SST-AD decision denying leave to appeal was unreasonable.

#### Section text

Hideq v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2017-05-03
Neutral citation
2017 FC 439
File numbers
T-2069-15
Decision Content
Date: 20170503
Docket: T-2069-15
Citation: 2017 FC 439
Ottawa, Ontario, May 3, 2017
PRESENT: The Honourable Mr. Justice Gleeson
BETWEEN:
ZAKI HIDEQ
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS
I. Overview

[1] The applicant, Mr. Hideq arrived in Canada from Lebanon in 1993 and was employed here between 1994 and 1998 in a variety of positions. In 1998 he began work as a door person and then in 2000 as a valet at “Casino Windsor”.

[2] In 2000, he was involved in a car accident at the Casino Windsor underground parking garage. As a result of the accident he indicated he suffered from neck, back and foot pain. Due to functional limitations relating to the injuries suffered he was subsequently assigned to the Casino Windsor security department until he was laid off in 2004. He was involved in a second car accident in 2005 where he suffered a variety of injuries including to his shoulder, neck and back.

[3] He applied for CPP disability benefits in October 2010. The application was denied both initially and upon reconsideration. He appealed the negative decisions. The Social Security Tribunal General Division General [SST-GD] dismissed the appeal. He was subsequently denied leave to appeal the negative SST-GD decision to the Social Security Tribunal – Appeal Division [SST-AD]. It is that decision that is before the Court for judicial review.

[4] Mr. Hideq is seeking an Order from this Court reversing the SST-AD decision and directing the payment of CPP disability benefits retroactive to the onset of his initial application. The respondent takes issue with the remedy being sought, arguing that if the application is granted the appropriate remedy would be to remit that matter back to the SST-AD for re-determination of the leave to appeal question.

[5] Mr. Hideq’s written submissions focus on alleged errors in the SST-GD decision. However, as noted above the decision before this Court is that of the SST-AD denying Mr. Hideq leave to appeal. The SST-GD decision has been considered in the process of assessing whether the SST-AD committed a reviewable error or rendered an unreasonable decision.

[6] Section 58 of the Department of Employment and Social Development Act, SC 2005, c 34 [DESDA] identifies the grounds of appeal from an SST-GD decision and provides that the SST-AD shall refuse to grant leave where it is satisfied the appeal has no reasonable chance of success. Having considered the party’s written and oral submissions I can find no basis to interfere with the SST-AD’s decision and therefore dismiss the application for judicial review.
II. Issue

[7] The sole issue raised in this application is whether the SST-AD decision denying leave to appeal was unreasonable.


## 9491:2 · paragraphs 8-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `8b5b031d098adf602303cd8fc53cb12bda5a68655a0f84ae0e615c5f9040ac96`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9491:2:subtheme:1 · paragraphs 8-13

- Raw key terms: `canada, attorney, general, amended, applicant, application, cause, named`
- Display key terms: `amended, named`
- Argument roles: `counterargument_limitation, governing_rule`
- Explanation: Observed roles: counterargument_limitation, governing_rule Display terms: amended, named Rule/authority context: However, pursuant to section 257 of the Jobs, Growth and Long-Term Prosperity Act, SC 2012, c 19, the matter was transferred to the SST-GD in April 2013. Evidence spans paragraphs 8-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4479896` offsets `124-135`; context: However, pursuant to section 257 of the Jobs, Growth and Long-Term Prosperity Act, SC 2012, c 19, the matter was transferred to the SST-GD in April 2013.
- Evidence: `counterargument_limitation` cue `However` at chunk `4479896` offsets `115-122`; context: However, pursuant to section 257 of the Jobs, Growth and Long-Term Prosperity Act, SC 2012, c 19, the matter was transferred to the SST-GD in April 2013.

#### 9491:2:subtheme:2 · paragraphs 14-24

- Raw key terms: `assessment, sst-gd, sst-ad, vocational, appeal, hideq, leave, reasonably`
- Display key terms: `assessment, sst-gd, sst-ad, vocational, hideq, leave, reasonably`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: assessment, sst-gd, sst-ad, vocational, hideq, leave, reasonably Application context: Hideq’s application for leave to appeal the SST-AD correctly articulated and applied the test it was to apply at paras 6 and 7 of the decision: (6) Subsection 58(1) of the Department of Employment and Social Development  Operative outcome context: (7) The Applicant must satisfy me that the reasons for appeal fall within any of the grounds of appeal and that appeal has a reasonable chance of success, before leave can be granted. | Leave to appeal should normally be granted where this review of the underlying record demonstrates the evidence was not appropriately considered (Joseph v Canada (Attorney General), 2017 FC 391 at paras 43 and 44, citing Evidence spans paragraphs 14-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4479899` offsets `525-532`; context: Hideq’s application for leave to appeal the SST-AD correctly articulated and applied the test it was to apply at paras 6 and 7 of the decision:
(6) Subsection 58(1) of the Department of Employment and Social Development Act (DSEDA] sets out the grounds of appeal as being limited to the following:
(a) The General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) The General Division erred in law in making its decision, whether or not the error appears on the face of the record;
(c) The General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `evidence_fact` cue `record` at chunk `4479899` offsets `577-583`; context: Hideq’s application for leave to appeal the SST-AD correctly articulated and applied the test it was to apply at paras 6 and 7 of the decision:
(6) Subsection 58(1) of the Department of Employment and Social Development Act (DSEDA] sets out the grounds of appeal as being limited to the following:
(a) The General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) The General Division erred in law in making its decision, whether or not the error appears on the face of the record;
(c) The General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `reasoning_application` cue `applied` at chunk `4479899` offsets `101-108`; context: Hideq’s application for leave to appeal the SST-AD correctly articulated and applied the test it was to apply at paras 6 and 7 of the decision:
(6) Subsection 58(1) of the Department of Employment and Social Development Act (DSEDA] sets out the grounds of appeal as being limited to the following:
(a) The General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) The General Division erred in law in making its decision, whether or not the error appears on the face of the record;
(c) The General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `disposition` cue `granted` at chunk `4479899` offsets `930-937`; context: (7) The Applicant must satisfy me that the reasons for appeal fall within any of the grounds of appeal and that appeal has a reasonable chance of success, before leave can be granted.
- Evidence: `evidence_fact` cue `record` at chunk `4479900` offsets `75-81`; context: [14] In applying this test the SST-AD is expected to review the underlying record and determine if the SST-GD failed to account for any evidence, or if it misconstrued or overlooked evidence.
- Evidence: `disposition` cue `granted` at chunk `4479900` offsets `227-234`; context: Leave to appeal should normally be granted where this review of the underlying record demonstrates the evidence was not appropriately considered (Joseph v Canada (Attorney General), 2017 FC 391 at paras 43 and 44, citing Griffin v Canada (Attorney General), 2016 FC 874 at para 20 [Griffin] and Karadeolian v Canada (Attorney General), 2016 FC 615 at paras 9 and 10).
- Evidence: `evidence_fact` cue `evidence` at chunk `4479901` offsets `240-248`; context: However in advancing oral submissions his counsel relied on a single alleged error in the consideration and treatment of the evidence before the SST-GD and the SST-AD’s failure to recognize this error in considering the leave application.
- Evidence: `counterargument_limitation` cue `However` at chunk `4479901` offsets `115-122`; context: However in advancing oral submissions his counsel relied on a single alleged error in the consideration and treatment of the evidence before the SST-GD and the SST-AD’s failure to recognize this error in considering the leave application.
- Evidence: `evidence_fact` cue `evidence` at chunk `4479909` offsets `196-204`; context: It is not the role and function of a reviewing court to reweigh and reconsider the evidence and substitute its own view of a preferable outcome (Griffin at paras 14, 23).

#### 9491:2:subtheme:3 · paragraphs 25-27

- Raw key terms: `para, required, sst-ad, sst-gd, acceptable, addressed, adopted, advanced`
- Display key terms: `para, required, sst-ad, sst-gd, acceptable, addressed, adopted, advanced`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: para, required, sst-ad, sst-gd, acceptable, addressed, adopted, advanced Application context: I am similarly unable to conclude that the SST-AD conclusion that these grounds failed to disclose a reasonable chance of success on appeal was unreasonable. Evidence spans paragraphs 25-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4479910` offsets `806-811`; context: Hideq also took issue with the content of certain expert medical reports that had been placed before the SST-GD but again the SST-AD reasonably concluded that any medical information excluded from these reports could have been addressed through secondary reports being placed before the SST-GD and that this ground of appeal did not disclose any error on the part of the SST-GD.
- Evidence: `evidence_fact` cue `found that` at chunk `4479910` offsets `393-403`; context: The SST-AD reasonably found that it was not the role of the Appeal Division to reweigh evidence and that the SST-GD had considered and addressed the cumulative effect of Mr.
- Evidence: `reasoning_application` cue `conclude` at chunk `4479910` offsets `238-246`; context: I am similarly unable to conclude that the SST-AD conclusion that these grounds failed to disclose a reasonable chance of success on appeal was unreasonable.

#### Section text

III. Standard of Review

[8] The SST-AD’s decision denying leave is to be reviewed against a standard of reasonableness (Tracey v Canada (Attorney General), 2015 FC 1300 at paras 17-23 [Tracey], Canada (Attorney General) v Hoffman, 2015 FC 1348 at para 27 [Hoffman], see also: Atkinson v Canada (Attorney General), 2014 FCA 187 at paras 24-26). In applying this standard the SST-AD is owed high level of deference (Hoffman at para 33).
IV. Legislative Framework

[9] For ease of reference, relevant portions of the Canada Pension Plan, RSC 1985, c C-8 and the DESDA are reproduced at Appendix A to this Judgment and Reasons.

[10] Mr. Hideq’s denial of disability benefits was appealed to the Office of the Commissioner of Review Tribunals. However, pursuant to section 257 of the Jobs, Growth and Long-Term Prosperity Act, SC 2012, c 19, the matter was transferred to the SST-GD in April 2013.
V. Preliminary Matter

[11] Respondent’s counsel relies on Federal Court Rules, SOR/98-199 [the Rules] in submitting that the application incorrectly names the Minister of Employment and Social Development, Social Security Tribunal as the named respondents in this application. The respondent requests that the style of cause be amended to reflect the Attorney General of Canada as the respondent. The applicant does not oppose the amendment.

[12] Sub-rule 303(1)(a) of the Rules requires that the applicant name every person “directly affected by the order sought in the application, other than a tribunal in respect of which the application is brought”. The Social Security Tribunal has been improperly named as a respondent. It has also been held that government departments are not legal entities and similarly cannot be named as parties. (Gravel v Canada (Attorney General), 2011 FC 832 at paras 5 and 6). The style of cause is amended naming the Attorney General of Canada as the sole respondent.
VI. Analysis

[13] In considering Mr. Hideq’s application for leave to appeal the SST-AD correctly articulated and applied the test it was to apply at paras 6 and 7 of the decision:
(6) Subsection 58(1) of the Department of Employment and Social Development Act (DSEDA] sets out the grounds of appeal as being limited to the following:
(a) The General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) The General Division erred in law in making its decision, whether or not the error appears on the face of the record;
(c) The General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
(7) The Applicant must satisfy me that the reasons for appeal fall within any of the grounds of appeal and that appeal has a reasonable chance of success, before leave can be granted.

[14] In applying this test the SST-AD is expected to review the underlying record and determine if the SST-GD failed to account for any evidence, or if it misconstrued or overlooked evidence. Leave to appeal should normally be granted where this review of the underlying record demonstrates the evidence was not appropriately considered (Joseph v Canada (Attorney General), 2017 FC 391 at paras 43 and 44, citing Griffin v Canada (Attorney General), 2016 FC 874 at para 20 [Griffin] and Karadeolian v Canada (Attorney General), 2016 FC 615 at paras 9 and 10).

[15] Mr. Hideq’s written submissions focused exclusively on a variety of concerns relating to the SST-GD decision. However in advancing oral submissions his counsel relied on a single alleged error in the consideration and treatment of the evidence before the SST-GD and the SST-AD’s failure to recognize this error in considering the leave application.

[16] Mr. Hideq argues that the SST-AD unreasonably concluded that the SST-GD appropriately considered a comprehensive rehabilitation and vocational assessment concluding that Mr. Hideq was totally disabled from any occupation for which he would be seen as reasonably suited by education, training or experience. He submitted that the SST-GD treatment of this report was an erroneous finding made without regard for the material before it and this report in actuality raised a ground of appeal that had a reasonable chance of success.

[17] In its decision the SST-GD sets out an extensive summary of Mr. Hideq’s medical and work history. That review includes a summary of the rehabilitation and vocational assessment at paragraph 49 of the SST-GD decision where it is stated:

[49] On October 12, 2017, in a comprehensive rehabilitation and vocational assessment, a psychometrist and rehabilitation specialist, J. Kobayashi, stated that from a rehabilitative perspective, given a combination of factors, i.e., physical restrictions and limited English skills, the Appellant remains totally disabled from any occupation for which he would be seen as reasonably suited by education, training and experience.

[18] Having acknowledged the rehabilitation and vocational assessment, the SST-GD then concluded at paragraph 83 that:

[83] Lastly the psychometrist, J. Kobayashi, in her comprehensive assessment on October 12, 2007, opined the Appellant, from a rehabilitative perspective, was totally disabled from any occupation for which he would be seen as reasonably suited by education training and experience. The Tribunal gives less weight to this statement as from a real world perspective, the Appellant was clearly able to describe his conditions and was able to answer any questions, exhibiting good language skills,; he is still young, and his education is such that he could easily be retrained in some occupation that would be suitable for his limitations; he also has good experience, based on the types of employment that he had, including having partnered in the ownership and operation of a business.

[19] I am unpersuaded by Mr. Hideq’s submissions. Contrary to the submissions of Mr. Hideq’s counsel, the vocational assessment was not uncontradicted. There were three medical reports, one in December 2005, a second in June 2007 and a third in May 2009 all expressing the view that Mr. Hideq, despite his undisputed disabilities, retained a capacity to work. In placing less weight on the vocational report, the SST-GD articulated its rationale for coming to the conclusion it did.

[20] In considering the application for leave to appeal the SST-AD also undertook a detailed consideration of each of the identified grounds of appeal, including the treatment of the vocational assessment. The SST-AD acknowledged that the SST-GD may not have referred extensively to the vocational assessment but found the SST-GD articulated its reasons for assigning said vocational assessment less weight.

[21] The SST-AD reasonably concluded that the appeal did not have a reasonable chance of success on this ground. It is not the role and function of a reviewing court to reweigh and reconsider the evidence and substitute its own view of a preferable outcome (Griffin at paras 14, 23).

[22] While Mr. Hideq’s counsel focused solely on the vocational assessment in arguing that the SST-AD decision was unreasonable, I have also considered the remaining grounds for appeal advanced before the SST-AD. I am similarly unable to conclude that the SST-AD conclusion that these grounds failed to disclose a reasonable chance of success on appeal was unreasonable. The SST-AD reasonably found that it was not the role of the Appeal Division to reweigh evidence and that the SST-GD had considered and addressed the cumulative effect of Mr. Hideq’s disabilities in rendering its decision, citing express statements in the SST-GD to support this conclusion. It further reasonably concluded that Mr. Hideq’s psychological state was considered as were his attempts at self-employment. Mr. Hideq also took issue with the content of certain expert medical reports that had been placed before the SST-GD but again the SST-AD reasonably concluded that any medical information excluded from these reports could have been addressed through secondary reports being placed before the SST-GD and that this ground of appeal did not disclose any error on the part of the SST-GD. Finally the SST-AD concluded that the real world context that the SST-GD is required to consider in assessing an individual’s work capacity was adopted in this case (Villani v Canada (Attorney General), 2001 FCA 248 at para 39).

[23] In summary the SST-AD and SST-GD decisions reflect the required elements of justification, transparency and intelligibility and falls within the range of possible, acceptable outcomes defensible in respect of the facts and law (Dunsmuir v New Brunswick, 2008 SCC 9 at para 47).

[24] The parties did not seek costs and none will be awarded.


## 9491:3 · paragraphs 28-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2db306e9785d0ecfafd57b11a69aba4f2b9dea721e635d88ebcdce6340125c24`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9491:3:subtheme:1 · paragraphs 28-29

- Raw key terms: `attorney, canada, cause, date, general, hearing, record, style`
- Display key terms: `date, hearing, style`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: date, hearing, style No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT IN T-2069-15
THIS COURT’S JUDGMENT is that:
The application is dismissed;
The style of cause is amended to reflect the Attorney General of Canada as the sole respondent; and
No costs are awarded.
"Patrick Gleeson"
Judge
APPENDIX A
Canada Pension Plan, RSC 1985, c C-8
[…]
42(2) For the purposes of this Act,
(a) a person shall be considered to be disabled only if he is determined in prescribed manner to have a severe and prolonged mental or physical disability, and for the purposes of this paragraph,
(i) a disability is severe only if by reason thereof the person in respect of whom the determination is made is incapable regularly of pursuing any substantially gainful occupation, and
(ii) a disability is prolonged only if it is determined in prescribed manner that the disability is likely to be long continued and of indefinite duration or is likely to result in death; and
(b) a person is deemed to have become or to have ceased to be disabled at the time that is determined in the prescribed manner to be the time when the person became or ceased to be, as the case may be, disabled, but in no case shall a person — including a contributor referred to in subparagraph 44(1)(b)(ii) — be deemed to have become disabled earlier than fifteen months before the time of the making of any application in respect of which the determination is made.
[…]
44 (1) Subject to this Part,
[…]
(b) a disability pension shall be paid to a contributor who has not reached sixty-five years of age, to whom no retirement pension is payable, who is disabled and who
(i) has made contributions for not less than the minimum qualifying period,
(ii) is a contributor to whom a disability pension would have been payable at the time the contributor is deemed to have become disabled if an application for a disability pension had been received before the contributor’s application for a disability pension was actually received, or
(iii) is a contributor to whom a disability pension would have been payable at the time the contributor is deemed to have become disabled if a division of unadjusted pensionable earnings that was made under section 55 or 55.1 had not been made;
[…]
60 (1) No benefit is payable to any person under this Act unless an application therefor has been made by him or on his behalf and payment of the benefit has been approved under this Act.
[…]
81 (1) Where
[…]
(b) an applicant is dissatisfied with any decision made under section 60,
[…]
the dissatisfied party or, subject to the regulations, any person on behalf thereof may, within ninety days after the day on which the dissatisfied party was notified in the prescribed manner of the decision or determination, or within such longer period as the Minister may either before or after the expiration of those ninety days allow, make a request to the Minister in the prescribed form and manner for a reconsideration of that decision or determination.
[…]
(2) The Minister shall reconsider without delay any decision or determination referred to in subsection (1) or (1.1) and may confirm or vary it, and may approve payment of a benefit, determine the amount of a benefit or determine that no benefit is payable, and shall notify in writing the party who made the request under subsection (1) or (1.1) of the Minister’s decision and of the reasons for it.
(3) The Minister may, on new facts, rescind or amend a decision made by him or her under this Act.
[…]
82 A party who is dissatisfied with a decision of the Minister made under section 81, including a decision in relation to further time to make a request, or, subject to the regulations, any person on their behalf, may appeal the decision to the Social Security Tribunal established under section 44 of the Department of Employment and Social Development Act.
[…]
42(2) Pour l’application de la présente loi :
a) une personne n’est considérée comme invalide que si elle est déclarée, de la manière prescrite, atteinte d’une invalidité physique ou mentale grave et prolongée, et pour l’application du présent alinéa :
(i) une invalidité n’est grave que si elle rend la personne à laquelle se rapporte la déclaration régulièrement incapable de détenir une occupation véritablement rémunératrice,
(ii) une invalidité n’est prolongée que si elle est déclarée, de la manière prescrite, devoir vraisemblablement durer pendant une période longue, continue et indéfinie ou devoir entraîner vraisemblablement le décès;
b) une personne est réputée être devenue ou avoir cessé d’être invalide à la date qui est déterminée, de la manière prescrite, être celle où elle est devenue ou a cessé d’être, selon le cas, invalide, mais en aucun cas une personne — notamment le cotisant visé au sous-alinéa 44(1)b)(ii) — n’est réputée être devenue invalide à une date antérieure de plus de quinze mois à la date de la présentation d’une demande à l’égard de laquelle la détermination a été faite.
[…]
44 (1) Sous réserve des autres dispositions de la présente partie :
[…]
b) une pension d’invalidité doit être payée à un cotisant qui n’a pas atteint l’âge de soixante-cinq ans, à qui aucune pension de retraite n’est payable, qui est invalide et qui :
(i) soit a versé des cotisations pendant au moins la période minimale d’admissibilité,
(ii) soit est un cotisant à qui une pension d’invalidité aurait été payable au moment où il est réputé être devenu invalide, si une demande de pension d’invalidité avait été reçue avant le moment où elle l’a effectivement été,
(iii) soit est un cotisant à qui une pension d’invalidité aurait été payable au moment où il est réputé être devenu invalide, si un partage des gains non ajustés ouvrant droit à pension n’avait pas été effectué en application des articles 55 et 55.1;
[…]
60 (1) Aucune prestation n’est payable à une personne sous le régime de la présente loi, sauf si demande en a été faite par elle ou en son nom et que le paiement en ait été approuvé selon la présente loi.
[…]
81 (1) Dans les cas où :
[…]
b) un requérant n’est pas satisfait d’une décision rendue en application de l’article 60,
[…]
ceux-ci peuvent, ou, sous réserve des règlements, quiconque de leur part, peut, dans les quatre-vingt-dix jours suivant le jour où ils sont, de la manière prescrite, avisés de la décision ou de l’arrêt, ou dans tel délai plus long qu’autorise le ministre avant ou après l’expiration de ces quatre-vingt-dix jours, demander par écrit à celui-ci, selon les modalités prescrites, de réviser la décision ou l’arrêt.
[…]
(2) Le ministre reconsidère sans délai toute décision ou tout arrêt visé au paragraphe (1) ou (1.1) et il peut confirmer ou modifier cette décision ou arrêt; il peut approuver le paiement d’une prestation et en fixer le montant, de même qu’il peut arrêter qu’aucune prestation n’est payable et il doit dès lors aviser par écrit de sa décision motivée la personne qui a fait la demande en vertu des paragraphes (1) ou (1.1).
3) Le ministre peut, en se fondant sur des faits nouveaux, annuler ou modifier une décision qu’il a lui-même rendue conformément à la présente loi.
[…]
82 La personne qui se croit lésée par une décision du ministre rendue en application de l’article 81, notamment une décision relative au délai supplémentaire, ou, sous réserve des règlements, quiconque de sa part, peut interjeter appel de la décision devant le Tribunal de la sécurité sociale, constitué par l’article 44 de la Loi sur le ministère de l’Emploi et du Développement social.
Department of Employment and Social Development Act, SC 2005, c 34
Appeal — time limit
52 (1) An appeal of a decision must be brought to the General Division in the prescribed form and manner and within,
(a) in the case of a decision made under the Employment Insurance Act, 30 days after the day on which it is communicated to the appellant; and
(b) in any other case, 90 days after the day on which the decision is communicated to the appellant.
(2) The General Division may allow further time within which an appeal may be brought, but in no case may an appeal be brought more than one year after the day on which the decision is communicated to the appellant.
53 (1) The General Division must summarily dismiss an appeal if it is satisfied that it has no reasonable chance of success.
(2) The General Division must give written reasons for its decision and send copies to the appellant and the Minister or the Commission, as the case may be, and any other party.
(3) The appellant may appeal the decision to the Appeal Division.
54 (1) The General Division may dismiss the appeal or confirm, rescind or vary a decision of the Minister or the Commission in whole or in part or give the decision that the Minister or the Commission should have given.
(2) The General Division must give written reasons for its decision and send copies to the appellant and the Minister or the Commission, as the case may be, and any other party.
55 Any decision of the General Division may be appealed to the Appeal Division by any person who is the subject of the decision and any other prescribed person.
56 (1) An appeal to the Appeal Division may only be brought if leave to appeal is granted.
(2) Despite subsection (1), no leave is necessary in the case of an appeal brought under subsection 53(3).
57 (1) An application for leave to appeal must be made to the Appeal Division in the prescribed form and manner and within,
(a) in the case of a decision made by the Employment Insurance Section, 30 days after the day on which it is communicated to the appellant; and
(b) in the case of a decision made by the Income Security Section, 90 days after the day on which the decision is communicated to the appellant.
(2) The Appeal Division may allow further time within which an application for leave to appeal is to be made, but in no case may an application be made more than one year after the day on which the decision is communicated to the appellant.
58 (1) The only grounds of appeal are that
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
(2) Leave to appeal is refused if the Appeal Division is satisfied that the appeal has no reasonable chance of success.
(3) The Appeal Division must either grant or refuse leave to appeal.
(4) The Appeal Division must give written reasons for its decision to grant or refuse leave and send copies to the appellant and any other party.
(5) If leave to appeal is granted, the application for leave to appeal becomes the notice of appeal and is deemed to have been filed on the day on which the application for leave to appeal was filed.
59 (1) The Appeal Division may dismiss the appeal, give the decision that the General Division should have given, refer the matter back to the General Division for reconsideration in accordance with any directions that the Appeal Division considers appropriate or confirm, rescind or vary the decision of the General Division in whole or in part.
(2) The Appeal Division must give written reasons for its decision and send copies to the appellant and any other party.
[…]
66 (1) The Tribunal may rescind or amend a decision given by it in respect of any particular application if
(a) in the case of a decision relating to the Employment Insurance Act, new facts are presented to the Tribunal or the Tribunal is satisfied that the decision was made without knowledge of, or was based on a mistake as to, some material fact; or
(b) in any other case, a new material fact is presented that could not have been discovered at the time of the hearing with the exercise of reasonable diligence.
(2) An application to rescind or amend a decision must be made within one year after the day on which a decision is communicated to the appellant.
(3) Each person who is the subject of a decision may make only one application to rescind or amend that decision.
(4) A decision is rescinded or amended by the same Division that made it.
Modalités de présentation
52 (1) L’appel d’une décision est interjeté devant la division générale selon les modalités prévues par règlement et dans le délai suivant :
a) dans le cas d’une décision rendue au titre de la Loi sur l’assurance-emploi, dans les trente jours suivant la date où l’appelant reçoit communication de la décision;
b) dans les autres cas, dans les quatre-vingt-dix jours suivant la date où l’appelant reçoit communication de la décision.
(2) La division générale peut proroger d’au plus un an le délai pour interjeter appel.
53 (1) La division générale rejette de façon sommaire l’appel si elle est convaincue qu’il n’a aucune chance raisonnable de succès.
(2) Elle rend une décision motivée par écrit et en fait parvenir une copie à l’appelant et, selon le cas, au ministre ou à la Commission, et à toute autre partie.
(3) L’appelant peut en appeler à la division d’appel de cette décision.
54 (1) La division générale peut rejeter l’appel ou confirmer, infirmer ou modifier totalement ou partiellement la décision visée par l’appel ou rendre la décision que le ministre ou la Commission aurait dû rendre.
(2) Elle rend une décision motivée par écrit et en fait parvenir une copie à l’appelant et, selon le cas, au ministre ou à la Commission, et à toute autre partie.
55 Toute décision de la division générale peut être portée en appel devant la division d’appel par toute personne qui fait l’objet de la décision et toute autre personne visée par règlement.
56 (1) Il ne peut être interjeté d’appel à la division d’appel sans permission.
(2) Toutefois, il n’est pas nécessaire d’obtenir une permission dans le cas d’un appel interjeté au titre du paragraphe 53(3).
57 (1) La demande de permission d’en appeler est présentée à la division d’appel selon les modalités prévues par règlement et dans le délai suivant :
a) dans le cas d’une décision rendue par la section de l’assurance-emploi, dans les trente jours suivant la date où l’appelant reçoit communication de la décision;
b) dans le cas d’une décision rendue par la section de la sécurité du revenu, dans les quatre-vingt-dix jours suivant la date où l’appelant reçoit communication de la décision.
(2) La division d’appel peut proroger d’au plus un an le délai pour présenter la demande de permission d’en appeler.
58 (1) Les seuls moyens d’appel sont les suivants :
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
c) elle a fondé sa décision sur une conclusion de fait erronée, tirée de façon abusive ou arbitraire ou sans tenir compte des éléments portés à sa connaissance.
(2) La division d’appel rejette la demande de permission d’en appeler si elle est convaincue que l’appel n’a aucune chance raisonnable de succès.
(3) Elle accorde ou refuse cette permission.
(4) Elle rend une décision motivée par écrit et en fait parvenir une copie à l’appelant et à toute autre partie.
(5) Dans les cas où la permission est accordée, la demande de permission est assimilée à un avis d’appel et celui-ci est réputé avoir été déposé à la date du dépôt de la demande de permission.
59 (1) La division d’appel peut rejeter l’appel, rendre la décision que la division générale aurait dû rendre, renvoyer l’affaire à la division générale pour réexamen conformément aux directives qu’elle juge indiquées, ou confirmer, infirmer ou modifier totalement ou partiellement la décision de la division générale.
(2) Elle rend une décision motivée par écrit et en fait parvenir une copie à l’appelant et à toute autre partie.
[…]
66 (1) Le Tribunal peut annuler ou modifier toute décision qu’il a rendue relativement à une demande particulière :
a) dans le cas d’une décision visant la Loi sur l’assurance-emploi, si des faits nouveaux lui sont présentés ou s’il est convaincu que la décision a été rendue avant que soit connu un fait essentiel ou a été fondée sur une erreur relative à un tel fait;
b) dans les autres cas, si des faits nouveaux et essentiels qui, au moment de l’audience, ne pouvaient être connus malgré l’exercice d’une diligence raisonnable lui sont présentés.
(2) La demande d’annulation ou de modification doit être présentée au plus tard un an après la date où l’appelant reçoit communication de la décision.
(3) Il ne peut être présenté plus d’une demande d’annulation ou de modification par toute partie visée par la décision.
(4) La décision est annulée ou modifiée par la division qui l’a rendue.
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-2069-15
STYLE OF CAUSE:
ZAKI HIDEQ v ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
Windsor, Ontario
DATE OF HEARING:
April 27, 2017


## 9491:4 · paragraphs 30-30

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d23779a1f721fd104225d086c58acec266c00ea3a99051d6ac4ecf98e1989d4f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9491:4:subtheme:1 · paragraphs 30-30

- Raw key terms: `anthony, appearances, applicant, attorney, barile, barrister, canada, dated`
- Display key terms: `anthony, barile, barrister, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: anthony, barile, barrister, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 30-30. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
GLEESON J.
DATED:
MAY 3, 2017
APPEARANCES:
Anthony Barile
For The Applicant
Michael Stevenson
For The Respondent
SOLICITORS OF RECORD:
Anthony Barile
Barrister and Solicitor
Windsor, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Gatineau (Québec)
For The Respondent
