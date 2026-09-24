# Discussion Units: case 13410

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **50**
- Continuity pairs: **49**
- Discussion Units: **5**
- Paragraph source hashes: **50**
- Sub-themes: **15**

## 13410:1 · paragraphs 0-2

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `8f5c80636d0fa078e04671a72b25b54a2f2daf345135bda2f0f1b11e60d59c57`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13410:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, application, decision, general, january, reasons, respondent, allowed`
- Display key terms: `january, allowed`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: january, allowed Rule/authority context: [1] This is an application for judicial review of the decision of Valerie Hazlett Parker, a Member of the Social Security Tribunal – Appeal Division [hereinafter referred to as the SST-AD], pursuant to section 58 of the  Operative outcome context: [2] For the reasons that follow, this application is allowed. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4660697` offsets `190-201`; context: [1] This is an application for judicial review of the decision of Valerie Hazlett Parker, a Member of the Social Security Tribunal – Appeal Division [hereinafter referred to as the SST-AD], pursuant to section 58 of the Department of Employment and Social Development Act, S.
- Evidence: `disposition` cue `allowed` at chunk `4660698` offsets `53-60`; context: [2] For the reasons that follow, this application is allowed.

#### Section text

Canada (Attorney General) v. Hoffman
Court (s) Database
Federal Court Decisions
Date
2015-12-04
Neutral citation
2015 FC 1348
File numbers
T-303-15
Notes
A correction was made on January 7, 2016
Decision Content
Date: 20151204
Docket: T-303-15
Citation: 2015 FC 1348
Ottawa, Ontario, December 4, 2015
PRESENT: The Honourable Mr. Justice Manson
BETWEEN:
ATTORNEY GENERAL OF CANADA
Applicant
and
KATHERINE HOFFMAN
Respondent
JUDGMENT AND REASONS

[1] This is an application for judicial review of the decision of Valerie Hazlett Parker, a Member of the Social Security Tribunal – Appeal Division [hereinafter referred to as the SST-AD], pursuant to section 58 of the Department of Employment and Social Development Act, S.C. 2005, c 34 [DESDA]. The decision was communicated to the Applicant on January 29, 2015, and grants the Respondent leave to appeal the decision of the Social Security Tribunal – General Division [hereinafter referred to as the SST-GD] dated October 22, 2014, on the basis that the Respondent has presented a reasonable ground upon which the proposed appeal might succeed.

[2] For the reasons that follow, this application is allowed.


## 13410:2 · paragraphs 3-4

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `28509019b15c2d0f2d8a1ef069d769311d0f019f9177bb5c874f0cb22aad5fec`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13410:2:subtheme:1 · paragraphs 3-4

- Raw key terms: `following, respondent, anxiety, application, applied, august, background, benefits`
- Display key terms: `following, anxiety, applied, august, background, benefits`
- Argument roles: `reasoning_application`
- Explanation: Observed roles: reasoning_application Display terms: following, anxiety, applied, august, background, benefits Application context: Background [3] The Respondent applied for Canada Pension Plan, RSC 1985, c C-8 [the CPP] disability benefits in 2010. Evidence spans paragraphs 3-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `4660698` offsets `95-102`; context: Background [3] The Respondent applied for Canada Pension Plan, RSC 1985, c C-8 [the CPP] disability benefits in 2010.

#### Section text

I. Background [3] The Respondent applied for Canada Pension Plan, RSC 1985, c C-8 [the CPP] disability benefits in 2010. She described her main disabling condition as being hospitalized for 6 weeks following a nervous breakdown in June 1991. The Respondent stated she was also hospitalized in February 1996, following a second nervous breakdown.

[4] The Respondent’s initial application included the following documentation:
a) Medical Report of Dr. Jeff King dated August 4, 2010. The report states that she is unable to work due to pervasive anxiety and refers to the 1996 hospitalization. It states that her anxiety is somewhat controlled by Paxil.

## 13410:3 · paragraphs 5-26

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d14c6cfe26e67851194fabe6a5194b020d80e2d3e42fdf8ccd0e7cd0d4a163f3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13410:3:subtheme:1 · paragraphs 5-6

- Raw key terms: `accident, company, following, hospital, hospitalization, insurance, king, letter`
- Display key terms: `accident, company, following, hospital, hospitalization, insurance, king, letter`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: accident, company, following, hospital, hospitalization, insurance, king, letter Position/evidence statements: [6] The Respondent submits that there was an additional hospitalization in 1996. Evidence spans paragraphs 5-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4660700` offsets `1538-1544`; context: The letter states that there are too many psychiatric issues in this patient to be dealt with in one interview, but gives a preliminary diagnosis of post traumatic stress disorder, chronic anxiety disorder, major depression which was being treated by Paxil, whiplash injury, and high stress.
- Evidence: `evidence_fact` cue `record` at chunk `4660700` offsets `8-14`; context: [5] The record also includes the following medical documentation:
a) Hospital Records of Dr.
- Evidence: `party_position` cue `submits` at chunk `4660701` offsets `19-26`; context: [6] The Respondent submits that there was an additional hospitalization in 1996.
- Evidence: `counterargument_limitation` cue `However` at chunk `4660701` offsets `81-88`; context: However, no hospital records have been provided.

#### 13410:3:subtheme:2 · paragraphs 7-11

- Raw key terms: `decision, respondent, applicant, application, considered, contributions, december, disability`
- Display key terms: `considered, contributions, december, disability`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application Display terms: considered, contributions, december, disability Rule/authority context: The Respondent’s application was considered under the late applicant provision, subsection 44(1)(b)(ii), to see if she satisfied the minimum contributory requirements for a CPP Disability Pension at an earlier time in he | [11] An explanation of the decision under appeal was filed with the OCRT. Application context: [7] The application was denied on October 13, 2010, because the Respondent had insufficient CPP contributions to qualify for a Disability Pension. Operative outcome context: [7] The application was denied on October 13, 2010, because the Respondent had insufficient CPP contributions to qualify for a Disability Pension. Evidence spans paragraphs 7-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4660702` offsets `52-59`; context: [7] The application was denied on October 13, 2010, because the Respondent had insufficient CPP contributions to qualify for a Disability Pension.
- Evidence: `disposition` cue `denied` at chunk `4660702` offsets `24-30`; context: [7] The application was denied on October 13, 2010, because the Respondent had insufficient CPP contributions to qualify for a Disability Pension.
- Evidence: `evidence_fact` cue `Record` at chunk `4660703` offsets `39-45`; context: [8] On June 13, 2011, the Respondent’s Record of Earnings indicated that due to a credit split, CPP contributions were allocated to her record for the years 1983 and 1985 to 1991, inclusive.
- Evidence: `governing_rule` cue `under` at chunk `4660703` offsets `235-240`; context: The Respondent’s application was considered under the late applicant provision, subsection 44(1)(b)(ii), to see if she satisfied the minimum contributory requirements for a CPP Disability Pension at an earlier time in her contributory period.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4660704` offsets `59-67`; context: Although the Respondent now qualified for benefits, she was not considered disabled as of the MQP in December 31, 1997.
- Evidence: `governing_rule` cue `under` at chunk `4660706` offsets `36-41`; context: [11] An explanation of the decision under appeal was filed with the OCRT.

#### 13410:3:subtheme:3 · paragraphs 12-15

- Raw key terms: `respondent, appeal, filed, hearing, sst-gd, additional, adjourned, advised`
- Display key terms: `filed, hearing, sst-gd, additional, adjourned, advised`
- Argument roles: `evidence_fact, governing_rule, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position Display terms: filed, hearing, sst-gd, additional, adjourned, advised Position/evidence statements: The hearing was adjourned since the Respondent indicated there were notes not yet submitted. Rule/authority context: [13] On April 1, 2013, the Respondent’s appeal was transferred to the SST-GD, pursuant to the Jobs Growth and Long-Term Prosperity Act. Evidence spans paragraphs 12-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submitted` at chunk `4660707` offsets `149-158`; context: The hearing was adjourned since the Respondent indicated there were notes not yet submitted.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4660708` offsets `78-89`; context: [13] On April 1, 2013, the Respondent’s appeal was transferred to the SST-GD, pursuant to the Jobs Growth and Long-Term Prosperity Act.
- Evidence: `evidence_fact` cue `testimony` at chunk `4660710` offsets `255-264`; context: First, the information filed was sufficient to allow a decision to be made without the testimony of the Appellant.

#### 13410:3:subtheme:4 · paragraphs 16-22

- Raw key terms: `appeal, leave, respondent, reports, sst-ad, tribunal, december, decision`
- Display key terms: `leave, reports, sst-ad, december`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: leave, reports, sst-ad, december Position/evidence statements: The Respondent submits that the contents of these reports had been known to all parties. Rule/authority context: Hoffman is precluded from work due to her disability; b) An appeal is requested pursuant to ss. | Standard of Review [22] On April 1, 2013, the SST-AD replaced the Pension Appeal Board [PAB] pursuant to sections 223, 224, and 225 of the Jobs, Growth and Long-Term Prosperity Act, 2012 c 19. Application context: [23] Under the former provisions of the Canada Pension Plan Act, RSC 1985, c C-8, s 83, a party could apply in writing for leave to appeal to the PAB. Operative outcome context: [16] On October 22, 2014, the SST-GD dismissed the Respondent’s appeal with reasons. | [19] Since leave was granted by the SST-AD, the Respondent has also discovered that the physical reports from the 1996 hospitalization were not part of the SST record used by all Tribunal Members who made a decision on t Evidence spans paragraphs 16-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4660711` offsets `37-46`; context: [16] On October 22, 2014, the SST-GD dismissed the Respondent’s appeal with reasons.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4660712` offsets `309-320`; context: Hoffman is precluded from work due to her disability;
b) An appeal is requested pursuant to ss.
- Evidence: `party_position` cue `submits` at chunk `4660714` offsets `379-386`; context: The Respondent submits that the contents of these reports had been known to all parties.
- Evidence: `evidence_fact` cue `record` at chunk `4660714` offsets `160-166`; context: [19] Since leave was granted by the SST-AD, the Respondent has also discovered that the physical reports from the 1996 hospitalization were not part of the SST record used by all Tribunal Members who made a decision on the Respondent’s file.
- Evidence: `counterargument_limitation` cue `However` at chunk `4660714` offsets `242-249`; context: However, they were outlined in the Respondent’s submissions dated September 5, 2014, as well as in the leave application.
- Evidence: `disposition` cue `granted` at chunk `4660714` offsets `21-28`; context: [19] Since leave was granted by the SST-AD, the Respondent has also discovered that the physical reports from the 1996 hospitalization were not part of the SST record used by all Tribunal Members who made a decision on the Respondent’s file.
- Evidence: `disposition` cue `granted` at chunk `4660715` offsets `53-60`; context: [20] On January 29, 2015, the SST-AD Tribunal Member granted leave to appeal.
- Evidence: `evidence_fact` cue `determined that` at chunk `4660716` offsets `16-31`; context: [21] The SST-AD determined that the SST-GD had based its decision on an erroneous finding of fact made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4660716` offsets `551-569`; context: Standard of Review [22] On April 1, 2013, the SST-AD replaced the Pension Appeal Board [PAB] pursuant to sections 223, 224, and 225 of the Jobs, Growth and Long-Term Prosperity Act, 2012 c 19.
- Evidence: `disposition` cue `granted` at chunk `4660716` offsets `522-529`; context: The Tribunal Member concluded that there was a reasonable chance of success on appeal and granted the application.
- Evidence: `governing_rule` cue `Under` at chunk `4660717` offsets `5-10`; context: [23] Under the former provisions of the Canada Pension Plan Act, RSC 1985, c C-8, s 83, a party could apply in writing for leave to appeal to the PAB.
- Evidence: `reasoning_application` cue `apply` at chunk `4660717` offsets `102-107`; context: [23] Under the former provisions of the Canada Pension Plan Act, RSC 1985, c C-8, s 83, a party could apply in writing for leave to appeal to the PAB.

#### 13410:3:subtheme:5 · paragraphs 23-24

- Raw key terms: `appeal, decision, error, general, leave, made, whether, acted`
- Display key terms: `error, leave, made, whether, acted`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: error, leave, made, whether, acted Rule/authority context: [25] After April 1, 2013, pursuant to section 58 of the DESDA, leave to appeal a decision of the SST-GD may be granted only where the applicant satisfied the SST-AD their appeal has a “reasonable chance of success” on on Application context: [24] Judicial review of the PAB decision granting or refusing leave to appeal involved the determination of two issues: 1) whether the correct test had been applied; and 2) whether a legal or factual error had been made  Operative outcome context: [25] After April 1, 2013, pursuant to section 58 of the DESDA, leave to appeal a decision of the SST-GD may be granted only where the applicant satisfied the SST-AD their appeal has a “reasonable chance of success” on on Evidence spans paragraphs 23-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4660718` offsets `112-118`; context: [24] Judicial review of the PAB decision granting or refusing leave to appeal involved the determination of two issues: 1) whether the correct test had been applied; and 2) whether a legal or factual error had been made in determining whether an arguable case was raised.
- Evidence: `reasoning_application` cue `applied` at chunk `4660718` offsets `157-164`; context: [24] Judicial review of the PAB decision granting or refusing leave to appeal involved the determination of two issues: 1) whether the correct test had been applied; and 2) whether a legal or factual error had been made in determining whether an arguable case was raised.
- Evidence: `issue` cue `whether` at chunk `4660719` offsets `481-488`; context: [25] After April 1, 2013, pursuant to section 58 of the DESDA, leave to appeal a decision of the SST-GD may be granted only where the applicant satisfied the SST-AD their appeal has a “reasonable chance of success” on one or more grounds of appeal identified in subsection 58(1):
a) The General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
b) The General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
c) The General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `evidence_fact` cue `record` at chunk `4660719` offsets `533-539`; context: [25] After April 1, 2013, pursuant to section 58 of the DESDA, leave to appeal a decision of the SST-GD may be granted only where the applicant satisfied the SST-AD their appeal has a “reasonable chance of success” on one or more grounds of appeal identified in subsection 58(1):
a) The General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
b) The General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
c) The General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4660719` offsets `26-37`; context: [25] After April 1, 2013, pursuant to section 58 of the DESDA, leave to appeal a decision of the SST-GD may be granted only where the applicant satisfied the SST-AD their appeal has a “reasonable chance of success” on one or more grounds of appeal identified in subsection 58(1):
a) The General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
b) The General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
c) The General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `disposition` cue `granted` at chunk `4660719` offsets `111-118`; context: [25] After April 1, 2013, pursuant to section 58 of the DESDA, leave to appeal a decision of the SST-GD may be granted only where the applicant satisfied the SST-AD their appeal has a “reasonable chance of success” on one or more grounds of appeal identified in subsection 58(1):
a) The General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
b) The General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
c) The General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.

#### 13410:3:subtheme:6 · paragraphs 25-26

- Raw key terms: `appeal, decision, granting, leave, sst-ad, test, above, accordingly`
- Display key terms: `granting, leave, sst-ad, above, accordingly`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: granting, leave, sst-ad, above, accordingly Rule/authority context: [26] In Tracey, above, Justice Roussel held that the two-step analysis adopted by this Court under the former regime should no longer guide this Court when reviewing a decision of the SST-AD on an application for leave t | [27] Accordingly, the test for granting leave to appeal from the SST-GD to the SST-AD and the standard of review to be applied to the SST-AD’s decision is reasonableness. Application context: [27] Accordingly, the test for granting leave to appeal from the SST-GD to the SST-AD and the standard of review to be applied to the SST-AD’s decision is reasonableness. Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4660720` offsets `310-317`; context: There should only be one step in the analysis and that is, the determination of whether the SST-AD’s decision granting or refusing leave to appeal was reasonable.
- Evidence: `governing_rule` cue `under` at chunk `4660720` offsets `93-98`; context: [26] In Tracey, above, Justice Roussel held that the two-step analysis adopted by this Court under the former regime should no longer guide this Court when reviewing a decision of the SST-AD on an application for leave to appeal.
- Evidence: `governing_rule` cue `standard of review` at chunk `4660721` offsets `94-112`; context: [27] Accordingly, the test for granting leave to appeal from the SST-GD to the SST-AD and the standard of review to be applied to the SST-AD’s decision is reasonableness.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4660721` offsets `5-16`; context: [27] Accordingly, the test for granting leave to appeal from the SST-GD to the SST-AD and the standard of review to be applied to the SST-AD’s decision is reasonableness.

#### Section text

[5] The record also includes the following medical documentation:
a) Hospital Records of Dr. Woolnough, dated June 3-July 18, 1991. The record states that the Respondent was hospitalized following an altercation with her husband in which she suffered severe trauma to her wrist, and she may be in the early stages of a psychotic illness;
b) Medical Report of Dr. Surti, dated January 3, 1992, stating that the Respondent has started back to work as a housecleaner and there is no evidence of depression or psychosis;
c) Medical Report of Dr. Surti, dated July 13, 1992, stating that the Respondent does not appear to be depressed, is not suicidal, and does not require any psychotropic medication;
d) Medical Report of Dr. Power, dated January 17, 2001, stating that the Respondent’s mood and anxiety levels have been stable and she is coping well. She is taking Paxil, which the doctor recommends she continue;
e) Medical Report of Dr. King, dated July 13, 2011, stating that the Respondent has a controlled level of anxiety and is taking Paxil once per day. The letter also states that the Respondent’s recurrent anxiety is such that it can be disabling at times;
f) Medical Report of Dr. Surapaneni, dated January 6, 2012, following a car accident in which the Respondent was injured in February 2011. The letter refers to a past overdose for which the Respondent was treated, as well as the 1991 hospitalization. The Respondent was suicidal in the past due to a history of abuse. The letter states that there are too many psychiatric issues in this patient to be dealt with in one interview, but gives a preliminary diagnosis of post traumatic stress disorder, chronic anxiety disorder, major depression which was being treated by Paxil, whiplash injury, and high stress. The letter also states that she is considered unfit to work due to trauma;
g) Medical Report of Dr. Ligate, dated March 5, 2012, prepared for insurance company following car accident. The report states that her tests indicated that she has severe depression and moderate anxiety. The diagnosis includes a pain disorder associated with psychological factors and PTSD, which may have been exacerbated by her car accident.

[6] The Respondent submits that there was an additional hospitalization in 1996. However, no hospital records have been provided. There is, however, mention of the 1996 hospitalization in Dr. King’s letter of August 4, 2010. The psychiatric assessment of March 5, 2012, which was conducted for the insurance company following her accident, also states that she was admitted to Grand River Hospital in 1996 for 10 days, at which time she was prescribed and started taking Paxil.

[7] The application was denied on October 13, 2010, because the Respondent had insufficient CPP contributions to qualify for a Disability Pension. The Respondent requested reconsideration of this decision.

[8] On June 13, 2011, the Respondent’s Record of Earnings indicated that due to a credit split, CPP contributions were allocated to her record for the years 1983 and 1985 to 1991, inclusive. The Respondent’s application was considered under the late applicant provision, subsection 44(1)(b)(ii), to see if she satisfied the minimum contributory requirements for a CPP Disability Pension at an earlier time in her contributory period. The Applicant determined the Respondent last met the contributory requirements in December 31, 1997, and this was the end of her Minimum Qualifying Period (MQP).

[9] The Applicant reconsidered and confirmed its decision. Although the Respondent now qualified for benefits, she was not considered disabled as of the MQP in December 31, 1997.

[10] The Respondent appealed the Applicant’s decision to the Office of the Commissioner of Review Tribunals (OCRT).

[11] An explanation of the decision under appeal was filed with the OCRT.

[12] The OCRT scheduled an in person hearing for January 15, 2013. The hearing was adjourned since the Respondent indicated there were notes not yet submitted.

[13] On April 1, 2013, the Respondent’s appeal was transferred to the SST-GD, pursuant to the Jobs Growth and Long-Term Prosperity Act.

[14] On February 10, 2014, the Applicant filed its Notice of Readiness to proceed to a hearing.

[15] On August 6, 2014, the SST-GD advised the parties the Tribunal intended to decide the appeal on the basis of the documents and submissions filed, for two reasons. First, the information filed was sufficient to allow a decision to be made without the testimony of the Appellant. Second, the SST-GD stated that “most medical interventions are well past the MQP date of December 31, 1997.” The SST-GD gave the parties until September 5, 2014 to file additional documents or submissions. The Respondent’s counsel filed written submissions with the SST-GD.

[16] On October 22, 2014, the SST-GD dismissed the Respondent’s appeal with reasons. The SST-GD determined the Respondent was not disabled since she “had work capacity at the time of her MQP in that she was young and physically well. Her mental status was maintained with medication.” The SST-GD explained some medical reports and assessments relating to the motor vehicle accident (MVA) of January 25, 2011 were not addressed “since the MVA did not occur until more than 13 years after the MQP of December 31, 1997.”

[17] The Respondent sought leave to appeal the SST-GD decision to the SST-AD. The grounds of appeal were outlined as follows:
a) The appeal has a reasonable chance for success, given the multiple medical reports stating that Ms. Hoffman is precluded from work due to her disability;
b) An appeal is requested pursuant to ss. 58(1)(c) – the General Division based its decision on an erroneous finding of fact made in a perverse and capricious manner;
c) Dr. Surti’s December 1992 report stated she was disabled mentally and this was contrary to the SST-GD’s conclusion that the Respondent retained the capacity to work;
d) The SST-GD decision is flawed and contains nothing to indicate in the Analysis that the tribunal paid any attention to the multiple other reports supporting a finding of disability for Ms. Hoffman prior to her MQP date of December 31, 1997.

[18] The Respondent acknowledges that the submission that Dr. Sutri had declared the Respondent mentally disabled in December of 1992 was incorrect, and that Dr. Sutri had in fact stated the Respondent was not mentally disabled at the time.

[19] Since leave was granted by the SST-AD, the Respondent has also discovered that the physical reports from the 1996 hospitalization were not part of the SST record used by all Tribunal Members who made a decision on the Respondent’s file. However, they were outlined in the Respondent’s submissions dated September 5, 2014, as well as in the leave application. The Respondent submits that the contents of these reports had been known to all parties.

[20] On January 29, 2015, the SST-AD Tribunal Member granted leave to appeal.

[21] The SST-AD determined that the SST-GD had based its decision on an erroneous finding of fact made in a perverse or capricious manner or without regard for the material before it. The decision states that the SST-GD was required to provide sufficient reasons for their decision, yet failed to give any explanation for discounting reports penned prior to the Respondent’s MQP date, that stated the Respondent was unable to work. The Tribunal Member concluded that there was a reasonable chance of success on appeal and granted the application.
II. Standard of Review [22] On April 1, 2013, the SST-AD replaced the Pension Appeal Board [PAB] pursuant to sections 223, 224, and 225 of the Jobs, Growth and Long-Term Prosperity Act, 2012 c 19. At that time, the SST-AD inherited the PAB’s jurisdiction with respect to applications for leave to appeal.

[23] Under the former provisions of the Canada Pension Plan Act, RSC 1985, c C-8, s 83, a party could apply in writing for leave to appeal to the PAB. While the legislation did not specify the test applicable for granting leave to appeal, the jurisprudence of this Court required that the party seeking leave to appeal raise an arguable case (Tracey v Canada (Attorney General), 2015 FC 1300 [Tracey] at para 13; Belo-Alves v Canada (Attorney General), 2014 FC 1100 at para 64).

[24] Judicial review of the PAB decision granting or refusing leave to appeal involved the determination of two issues: 1) whether the correct test had been applied; and 2) whether a legal or factual error had been made in determining whether an arguable case was raised. The first issue was reviewable on a standard of correctness. The second issue was determined on a reasonableness standard (Callihoo v Canada (Attorney General), [2000] FCJ No 612 at para 15).

[25] After April 1, 2013, pursuant to section 58 of the DESDA, leave to appeal a decision of the SST-GD may be granted only where the applicant satisfied the SST-AD their appeal has a “reasonable chance of success” on one or more grounds of appeal identified in subsection 58(1):
a) The General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
b) The General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
c) The General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.

[26] In Tracey, above, Justice Roussel held that the two-step analysis adopted by this Court under the former regime should no longer guide this Court when reviewing a decision of the SST-AD on an application for leave to appeal. There should only be one step in the analysis and that is, the determination of whether the SST-AD’s decision granting or refusing leave to appeal was reasonable. Counsel for the parties agreed that this should be the applicable test and I agree (Tracey, at paras 17, 21 & 22).

[27] Accordingly, the test for granting leave to appeal from the SST-GD to the SST-AD and the standard of review to be applied to the SST-AD’s decision is reasonableness.


## 13410:4 · paragraphs 27-48

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0d411c62f44a6709c1a831e622be412da17c33f365c6d46a87daa90d2de75d6e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13410:4:subtheme:1 · paragraphs 27-31

- Raw key terms: `disability, subsection, applicant, considered, disabled, made, person, prolonged`
- Display key terms: `disability, subsection, considered, disabled, made, person, prolonged`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: disability, subsection, considered, disabled, made, person, prolonged Rule/authority context: Issue [28] Did the SST-AD Member fail to reasonably apply the leave test under section 58 of the DESDA and was the decision granting leave to appeal reasonable? | To qualify for the disability pension, an applicant must: a) Be under 65 years of age; b) Not be in receipt of the CPP retirement pension; c) Be disabled; and d) Have made valid contributions to the CPP for not less than Application context: Issue [28] Did the SST-AD Member fail to reasonably apply the leave test under section 58 of the DESDA and was the decision granting leave to appeal reasonable? | Because the Respondent’s application was considered under the late applicant provision, subsection 44(1)(b)(ii), she must also show that she has been continuously disabled up to the present time. Evidence spans paragraphs 27-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `4660721` offsets `176-181`; context: Issue [28] Did the SST-AD Member fail to reasonably apply the leave test under section 58 of the DESDA and was the decision granting leave to appeal reasonable?
- Evidence: `evidence_fact` cue `record` at chunk `4660721` offsets `901-907`; context: (1) The only grounds of appeal are that
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `governing_rule` cue `under` at chunk `4660721` offsets `249-254`; context: Issue [28] Did the SST-AD Member fail to reasonably apply the leave test under section 58 of the DESDA and was the decision granting leave to appeal reasonable?
- Evidence: `reasoning_application` cue `apply` at chunk `4660721` offsets `228-233`; context: Issue [28] Did the SST-AD Member fail to reasonably apply the leave test under section 58 of the DESDA and was the decision granting leave to appeal reasonable?
- Evidence: `governing_rule` cue `under` at chunk `4660722` offsets `170-175`; context: To qualify for the disability pension, an applicant must:
a) Be under 65 years of age;
b) Not be in receipt of the CPP retirement pension;
c) Be disabled; and
d) Have made valid contributions to the CPP for not less than the Minimum Qualifying Period (MQP).
- Evidence: `governing_rule` cue `under` at chunk `4660723` offsets `205-210`; context: Because the Respondent’s application was considered under the late applicant provision, subsection 44(1)(b)(ii), she must also show that she has been continuously disabled up to the present time.
- Evidence: `reasoning_application` cue `Because` at chunk `4660723` offsets `153-160`; context: Because the Respondent’s application was considered under the late applicant provision, subsection 44(1)(b)(ii), she must also show that she has been continuously disabled up to the present time.
- Evidence: `reasoning_application` cue `applies` at chunk `4660725` offsets `31-38`; context: [33] A high level of deference applies when this Court is reviewing the SST-AD’s interpretation of its own statute (Tracey; Alberta (Information and Privacy Commissioner) v Alberta Teachers' Association, 2011 SCC 61 at paras 30, 39).

#### 13410:4:subtheme:2 · paragraphs 32-34

- Raw key terms: `applicant, decision, member, appeal, appears, argues, considered, desda`
- Display key terms: `appears, argues, considered, desda`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: appears, argues, considered, desda Position/evidence statements: The Applicant argues that the decision is unreasonable because it does not specify whether leave is being granted pursuant to any other grounds apart from subsection 58(1)(c), and also not specify consideration of subsec | [36] The Applicant also argues that the Tribunal Member did not apply the test reasonably. Rule/authority context: Therefore, on the face of the decision, the Tribunal Member appears to have considered the relevant test under section 58 of the DESDA. | [35] The Member’s SST-AD decision states that she is granting leave to appeal based on an erroneous finding of fact made in a perverse or capricious manner, or without regard to the material before it, pursuant to subsec Application context: Therefore, on the face of the decision, the Tribunal Member appears to have considered the relevant test under section 58 of the DESDA. | The Applicant argues that the decision is unreasonable because it does not specify whether leave is being granted pursuant to any other grounds apart from subsection 58(1)(c), and also not specify consideration of subsec Operative outcome context: The Applicant argues that the decision is unreasonable because it does not specify whether leave is being granted pursuant to any other grounds apart from subsection 58(1)(c), and also not specify consideration of subsec Evidence spans paragraphs 32-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4660726` offsets `239-246`; context: She also states that she must decide whether the Applicant has put forward a ground of appeal that has a reasonable chance of success on appeal.
- Evidence: `governing_rule` cue `under` at chunk `4660726` offsets `452-457`; context: Therefore, on the face of the decision, the Tribunal Member appears to have considered the relevant test under section 58 of the DESDA.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4660726` offsets `347-356`; context: Therefore, on the face of the decision, the Tribunal Member appears to have considered the relevant test under section 58 of the DESDA.
- Evidence: `issue` cue `whether` at chunk `4660727` offsets `331-338`; context: The Applicant argues that the decision is unreasonable because it does not specify whether leave is being granted pursuant to any other grounds apart from subsection 58(1)(c), and also not specify consideration of subsection 58(2).
- Evidence: `party_position` cue `argues` at chunk `4660727` offsets `262-268`; context: The Applicant argues that the decision is unreasonable because it does not specify whether leave is being granted pursuant to any other grounds apart from subsection 58(1)(c), and also not specify consideration of subsection 58(2).
- Evidence: `governing_rule` cue `pursuant to` at chunk `4660727` offsets `202-213`; context: [35] The Member’s SST-AD decision states that she is granting leave to appeal based on an erroneous finding of fact made in a perverse or capricious manner, or without regard to the material before it, pursuant to subsection 58(1)(c) of the DESDA.
- Evidence: `reasoning_application` cue `because` at chunk `4660727` offsets `303-310`; context: The Applicant argues that the decision is unreasonable because it does not specify whether leave is being granted pursuant to any other grounds apart from subsection 58(1)(c), and also not specify consideration of subsection 58(2).
- Evidence: `counterargument_limitation` cue `However` at chunk `4660727` offsets `480-487`; context: However, the grounds set out in subsection 58(1) are not conjunctive, and therefore the SST-AD is not required to refer to all the section 58 or subsection 58(2) grounds in granting leave.
- Evidence: `disposition` cue `granted` at chunk `4660727` offsets `354-361`; context: The Applicant argues that the decision is unreasonable because it does not specify whether leave is being granted pursuant to any other grounds apart from subsection 58(1)(c), and also not specify consideration of subsection 58(2).
- Evidence: `party_position` cue `argues` at chunk `4660728` offsets `24-30`; context: [36] The Applicant also argues that the Tribunal Member did not apply the test reasonably.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660728` offsets `373-381`; context: When paragraphs 5 and 6 are compared with the Tribunal Member’s comments in paragraph 7 that “various medical professionals reached different conclusions about the [Respondent’s] capacities at different times” and the SST-GD’s decision “was dependent, at least in part, on how this evidence was weighed” it appears the application may have been considered the basis of the “old test” (arguable case).
- Evidence: `reasoning_application` cue `apply` at chunk `4660728` offsets `64-69`; context: [36] The Applicant also argues that the Tribunal Member did not apply the test reasonably.

#### 13410:4:subtheme:3 · paragraphs 35-36

- Raw key terms: `applicant, decision, disability, evidence, member, required, sst-ad, sst-gd`
- Display key terms: `disability, required, sst-ad, sst-gd`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: disability, required, sst-ad, sst-gd Rule/authority context: [37] The Applicant’s position is that the reasons suggest the SST-AD Tribunal Member failed to exercise her discretion properly pursuant to subsection 58(2). | [38] Moreover, the Applicant states that it was an error for the SST-AD to determine whether the SST-GD “based its decision on an erroneous finding of fact” without first considering the legal test for disability specifi Evidence spans paragraphs 35-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4660729` offsets `176-183`; context: Before concluding whether the SST-GD had ignored any evidence material to the ultimate issue, the Member was required to examine the evidence and the SST-GD’s reasons for decision keeping in mind: (i) the new leave test; (ii) the test for CPP disability outlined in subsection 42(2); and (iii) the nature of an SST-AD appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660729` offsets `211-219`; context: Before concluding whether the SST-GD had ignored any evidence material to the ultimate issue, the Member was required to examine the evidence and the SST-GD’s reasons for decision keeping in mind: (i) the new leave test; (ii) the test for CPP disability outlined in subsection 42(2); and (iii) the nature of an SST-AD appeal.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4660729` offsets `128-139`; context: [37] The Applicant’s position is that the reasons suggest the SST-AD Tribunal Member failed to exercise her discretion properly pursuant to subsection 58(2).
- Evidence: `issue` cue `whether` at chunk `4660730` offsets `85-92`; context: [38] Moreover, the Applicant states that it was an error for the SST-AD to determine whether the SST-GD “based its decision on an erroneous finding of fact” without first considering the legal test for disability specified in subsection 42(2) of the CPP and the common law.
- Evidence: `evidence_fact` cue `record` at chunk `4660730` offsets `331-337`; context: The Tribunal Member was required to consider whether the record contained evidence to support the SST-GD’s conclusion that the Respondent was not disabled at MQP.
- Evidence: `governing_rule` cue `legal test` at chunk `4660730` offsets `187-197`; context: [38] Moreover, the Applicant states that it was an error for the SST-AD to determine whether the SST-GD “based its decision on an erroneous finding of fact” without first considering the legal test for disability specified in subsection 42(2) of the CPP and the common law.

#### 13410:4:subtheme:4 · paragraphs 37-38

- Raw key terms: `applicant, decision, evidence, leave, member, tribunal, analyse, appropriately`
- Display key terms: `leave, analyse, appropriately`
- Argument roles: `disposition, evidence_fact, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position Display terms: leave, analyse, appropriately Position/evidence statements: [40] Finally, the Applicant argues that the SST-AD’s Tribunal Member’s obligation to give reasons arises from subsection 58(4) of the DESDA. Operative outcome context: [39] As well, the Applicant’s position is that the Tribunal Member erred in assessing evidence and information material to assessing whether leave should be granted. Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4660731` offsets `133-140`; context: [39] As well, the Applicant’s position is that the Tribunal Member erred in assessing evidence and information material to assessing whether leave should be granted.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660731` offsets `86-94`; context: [39] As well, the Applicant’s position is that the Tribunal Member erred in assessing evidence and information material to assessing whether leave should be granted.
- Evidence: `disposition` cue `granted` at chunk `4660731` offsets `157-164`; context: [39] As well, the Applicant’s position is that the Tribunal Member erred in assessing evidence and information material to assessing whether leave should be granted.
- Evidence: `party_position` cue `argues` at chunk `4660732` offsets `28-34`; context: [40] Finally, the Applicant argues that the SST-AD’s Tribunal Member’s obligation to give reasons arises from subsection 58(4) of the DESDA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660732` offsets `235-243`; context: A review of the Leave Decision illustrates the Tribunal Member did not analyse the law or the evidence in a meaningful way.

#### 13410:4:subtheme:5 · paragraphs 39-44

- Raw key terms: `decision, member, reasons, respondent, basis, evidence, parties, provide`
- Display key terms: `basis, provide`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: basis, provide Evidence spans paragraphs 39-44. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4660733` offsets `148-154`; context: Reasons should be responsive to the live issues presented by the case and the parties’ key arguments.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660736` offsets `72-80`; context: [44] Here, however, the Member has failed to articulate in any way what evidence she relied upon in deciding that the Respondent had a reasonable chance of success on appeal, based on the evidence and reasons before the SST-GD, as of the relevant date of December 31, 1997.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660737` offsets `21-29`; context: [45] In finding that evidence “penned prior to the MQP” may have been ignored, the Tribunal Member neglects to recognize the record contains no medical evidence describing the Respondent’s condition in 1997 and except for one report in 2001, there is no other medical evidence in the record describing her condition until 2010.

#### 13410:4:subtheme:6 · paragraphs 45-48

- Raw key terms: `member, respondent, basis, disabled, evidence, given, prior, unclear`
- Display key terms: `basis, disabled, given, prior, unclear`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: basis, disabled, given, prior, unclear Application context: [49] I find that the Tribunal Member failed to reasonably provide any reason(s) to support granting leave on the basis that the SST-GD “may have based its decision on an erroneous finding of fact made in a perverse or ca Operative outcome context: The application for judicial review is granted, and the matter is referred back to a different Tribunal Member for reconsideration in accordance with these reasons. Evidence spans paragraphs 45-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4660739` offsets `30-37`; context: [47] It is also unclear as to whether the Member recognized that Dr.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4660740` offsets `5-13`; context: [48] Evidence subsequent to the end of the MQP is not relevant, given the Applicant did not appear to prove her disability prior to the MQP, and it is unclear on what basis or evidence the Member found that the Respondent has a reasonable chance of success on appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660741` offsets `288-296`; context: [49] I find that the Tribunal Member failed to reasonably provide any reason(s) to support granting leave on the basis that the SST-GD “may have based its decision on an erroneous finding of fact made in a perverse or capricious manner”, given the lack of any transparent or intelligible evidence indicating that the Respondent was disabled as defined by subsection 42(2) of the CPP prior to her MQP of December 31, 1997.
- Evidence: `reasoning_application` cue `I find` at chunk `4660741` offsets `5-11`; context: [49] I find that the Tribunal Member failed to reasonably provide any reason(s) to support granting leave on the basis that the SST-GD “may have based its decision on an erroneous finding of fact made in a perverse or capricious manner”, given the lack of any transparent or intelligible evidence indicating that the Respondent was disabled as defined by subsection 42(2) of the CPP prior to her MQP of December 31, 1997.
- Evidence: `disposition` cue `granted` at chunk `4660741` offsets `504-511`; context: The application for judicial review is granted, and the matter is referred back to a different Tribunal Member for reconsideration in accordance with these reasons.

#### Section text

III. Issue [28] Did the SST-AD Member fail to reasonably apply the leave test under section 58 of the DESDA and was the decision granting leave to appeal reasonable?
IV. Analysis [29] The relevant legislative provisions, subsections 58(1) and 58(2) of the Department of Employment and Social Development Act, SC 2005 c 35 (formerly the Department of Human Resources and Skills Development Act), reads as follows:
Grounds of appeal
58. (1) The only grounds of appeal are that
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
Moyens d’appel
58. (1) Les seuls moyens d’appel sont les suivants :
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
c) elle a fondé sa décision sur une conclusion de fait erronée, tirée de façon abusive ou arbitraire ou sans tenir compte des éléments portés à sa connaissance.
Criteria
(2) Leave to appeal is refused if the Appeal Division is satisfied that the appeal has no reasonable chance of success.
Critère
(2) La division d’appel rejette la demande de permission d’en appeler si elle est convaincue que l’appel n’a aucune chance raisonnable de succès.

[30] Subsection 44(1)(b) of the CPP sets out the eligibility requirements for the CPP disability pension. To qualify for the disability pension, an applicant must:
a) Be under 65 years of age;
b) Not be in receipt of the CPP retirement pension;
c) Be disabled; and
d) Have made valid contributions to the CPP for not less than the Minimum Qualifying Period (MQP).

[31] A person must establish a severe and prolonged disability on or before the end of the MQP. In this case, the Respondent’s MQP is December 31, 1997. Because the Respondent’s application was considered under the late applicant provision, subsection 44(1)(b)(ii), she must also show that she has been continuously disabled up to the present time.

[32] Subsection 42(2)(a) of the CPP defines disability as a physical or mental disability that is severe and prolonged. A person is considered to have a severe disability if he or she is incapable regularly of pursuing any substantially gainful occupation. A disability is prolonged if it is likely to be long continued and of indefinite duration or is likely to result in death.

[33] A high level of deference applies when this Court is reviewing the SST-AD’s interpretation of its own statute (Tracey; Alberta (Information and Privacy Commissioner) v Alberta Teachers' Association, 2011 SCC 61 at paras 30, 39).

[34] In the decision of the SST-AD, the Tribunal Member cites section 58 of the DESDA as setting out the only grounds of appeal that may be considered to grant leave to appeal a decision of the SST-GD. She also states that she must decide whether the Applicant has put forward a ground of appeal that has a reasonable chance of success on appeal. Therefore, on the face of the decision, the Tribunal Member appears to have considered the relevant test under section 58 of the DESDA.

[35] The Member’s SST-AD decision states that she is granting leave to appeal based on an erroneous finding of fact made in a perverse or capricious manner, or without regard to the material before it, pursuant to subsection 58(1)(c) of the DESDA. The Applicant argues that the decision is unreasonable because it does not specify whether leave is being granted pursuant to any other grounds apart from subsection 58(1)(c), and also not specify consideration of subsection 58(2). However, the grounds set out in subsection 58(1) are not conjunctive, and therefore the SST-AD is not required to refer to all the section 58 or subsection 58(2) grounds in granting leave. I am not persuaded that the Member failed to consider subsection 58(1) or subsection 58(2) as alleged by the Applicant.

[36] The Applicant also argues that the Tribunal Member did not apply the test reasonably. When paragraphs 5 and 6 are compared with the Tribunal Member’s comments in paragraph 7 that “various medical professionals reached different conclusions about the [Respondent’s] capacities at different times” and the SST-GD’s decision “was dependent, at least in part, on how this evidence was weighed” it appears the application may have been considered the basis of the “old test” (arguable case).

[37] The Applicant’s position is that the reasons suggest the SST-AD Tribunal Member failed to exercise her discretion properly pursuant to subsection 58(2). Before concluding whether the SST-GD had ignored any evidence material to the ultimate issue, the Member was required to examine the evidence and the SST-GD’s reasons for decision keeping in mind: (i) the new leave test; (ii) the test for CPP disability outlined in subsection 42(2); and (iii) the nature of an SST-AD appeal.

[38] Moreover, the Applicant states that it was an error for the SST-AD to determine whether the SST-GD “based its decision on an erroneous finding of fact” without first considering the legal test for disability specified in subsection 42(2) of the CPP and the common law. The Tribunal Member was required to consider whether the record contained evidence to support the SST-GD’s conclusion that the Respondent was not disabled at MQP.

[39] As well, the Applicant’s position is that the Tribunal Member erred in assessing evidence and information material to assessing whether leave should be granted. A decision which “ignored the evidentiary record” or is based upon ignoring “crucial documentary evidence” or evidence “not appropriately considered” will be one made in a perverse or capricious manner (Canada (AG) v MacLeod (2010), 410 NC 166 (FCA) at para 5; Canada (AG) v McCarthy, [1994] FCJ No 1158 (CA) at para 22; Vincent v Canada (AG), [2007] FCJ No 964 (CA)).

[40] Finally, the Applicant argues that the SST-AD’s Tribunal Member’s obligation to give reasons arises from subsection 58(4) of the DESDA. A review of the Leave Decision illustrates the Tribunal Member did not analyse the law or the evidence in a meaningful way.

[41] Reasons should be understandable, sufficiently detailed and provide a logical basis for the decision. Reasons should be responsive to the live issues presented by the case and the parties’ key arguments. The reasons must be read together with the outcome to determine whether it is reasonable (Newfoundland and Labrador Nurses' Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at paras 14-15).

[42] The SST-AD bases its decision on the SST-GD decision’s failure to provide an explanation for discounting reports that concluded that the Respondent could not work.

[43] The adequacy of reasons is not a stand-alone basis for quashing a decision, and reasons must simply be sufficient to permit the parties to understand why the tribunal made the decision and to enable judicial review of that decision.

[44] Here, however, the Member has failed to articulate in any way what evidence she relied upon in deciding that the Respondent had a reasonable chance of success on appeal, based on the evidence and reasons before the SST-GD, as of the relevant date of December 31, 1997.

[45] In finding that evidence “penned prior to the MQP” may have been ignored, the Tribunal Member neglects to recognize the record contains no medical evidence describing the Respondent’s condition in 1997 and except for one report in 2001, there is no other medical evidence in the record describing her condition until 2010.

[46] The Member does not appear to have considered that while the leave application says Dr. Surapaneni noted “Ms. Hoffman appeared to have symptoms of post-traumatic stress disorder”, but neglected to indicate the report also says this disorder “came on” after she had a motor vehicle accident on February 25, 2011.

[47] It is also unclear as to whether the Member recognized that Dr. Surti’s 1992 note suggests the opposite of what is alleged by the Respondent. Dr. Surti’s note stated that the Respondent is “not disabled” and “not psychotic”.

[48] Evidence subsequent to the end of the MQP is not relevant, given the Applicant did not appear to prove her disability prior to the MQP, and it is unclear on what basis or evidence the Member found that the Respondent has a reasonable chance of success on appeal.

[49] I find that the Tribunal Member failed to reasonably provide any reason(s) to support granting leave on the basis that the SST-GD “may have based its decision on an erroneous finding of fact made in a perverse or capricious manner”, given the lack of any transparent or intelligible evidence indicating that the Respondent was disabled as defined by subsection 42(2) of the CPP prior to her MQP of December 31, 1997.
JUDGMENT
THIS COURT’S JUDGMENT is that:
1. The application for judicial review is granted, and the matter is referred back to a different Tribunal Member for reconsideration in accordance with these reasons.
"Michael D. Manson"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-303-15
STYLE OF CAUSE:
AGC V KATHERINE HOFFMAN
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
November 30, 2015


## 13410:5 · paragraphs 49-49

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `cbf2fc91f7df3889f5c78e2850c0388a6c0a3a47861b577b0d4a53f543cdb370`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13410:5:subtheme:1 · paragraphs 49-49

- Raw key terms: `appearances, applicant, attorney, canada, dalloo, dated, december, deputy`
- Display key terms: `dalloo, dated, december, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: dalloo, dated, december, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 49-49. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND reasons:
MANSON J.
DATED:
December 4, 2015
APPEARANCES:
Laura Dalloo
For The applicant
Randy Knight
For The respondent
SOLICITORS OF RECORD:
Graves Richard Harris LLP
Kitchener, ON
For The applicant
William F. Pentney
Deputy Attorney General of Canada
Gatineau, QC
For The respondent
