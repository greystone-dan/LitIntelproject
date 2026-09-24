# Discussion Units: case 20898

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **50**
- Continuity pairs: **49**
- Discussion Units: **8**
- Paragraph source hashes: **50**
- Sub-themes: **10**

## 20898:1 · paragraphs 0-1

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c8804749719d1eadae0530c622dc0f44b917a39cc6ba95c2a559387f493553b1`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20898:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `canada, decision, federal, applicant, application, attorney, beaudry, bustamante`
- Display key terms: `federal, beaudry, bustamante`
- Argument roles: `governing_rule`
- Explanation: Observed roles: governing_rule Display terms: federal, beaudry, bustamante Rule/authority context: [1] This is an application for judicial review pursuant to section 18. Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4985903` offsets `47-58`; context: [1] This is an application for judicial review pursuant to section 18.

#### Section text

Valdivia De Bustamante v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2008-10-03
Neutral citation
2008 FC 1111
File numbers
T-1583-06
Decision Content
Date: 20081003
Docket: T-1583-06
Citation: 2008 FC 1111
Ottawa, Ontario, October 3, 2008
PRESENT: The Honourable Mr. Justice Beaudry
BETWEEN:
ELSA VALDIVIA DE BUSTAMANTE
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review pursuant to section 18.1 of the Federal Courts Act, R.S., 1985, c. F-7, of a decision of the Review Tribunal dated July 26, 2006, regarding the Canada Pension Plan and Old Age Security.


## 20898:2 · paragraphs 2-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5528c2f1c51759bdb5150084338d42da4d44ec8750dd6f4ed32b623ec0dad0c2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20898:2:subtheme:1 · paragraphs 2-12

- Raw key terms: `applicant, husband, canada, applied, citizenship, period, security, visa`
- Display key terms: `husband, applied, period, security, visa`
- Argument roles: `disposition, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, reasoning_application Display terms: husband, applied, period, security, visa Rule/authority context: The applicant therefore had to wait until 2004 to have the minimum ten years of residence required to be eligible for a partial pension under section 3 of the Old Age Security Act, R. | [11] On October 24, 2003, she filed a fourth application for Old Age Security (OAS) as well as for the Guaranteed Income Supplement (GIS) benefits under the Act. Application context: She also applied for a social insurance card. | [7] In 1996, the applicant’s spouse applied for the first time for Old Age Security on her behalf, but this was refused because the husband was already receiving full pension. Operative outcome context: On March 3, 1980, the applicant’s spouse, the late Ramon Bustamante, immigrated to Canada and was granted citizenship in 1986. Evidence spans paragraphs 2-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `4985904` offsets `204-211`; context: She also applied for a social insurance card.
- Evidence: `disposition` cue `granted` at chunk `4985905` offsets `168-175`; context: On March 3, 1980, the applicant’s spouse, the late Ramon Bustamante, immigrated to Canada and was granted citizenship in 1986.
- Evidence: `reasoning_application` cue `applied` at chunk `4985909` offsets `36-43`; context: [7] In 1996, the applicant’s spouse applied for the first time for Old Age Security on her behalf, but this was refused because the husband was already receiving full pension.
- Evidence: `governing_rule` cue `under` at chunk `4985910` offsets `291-296`; context: The applicant therefore had to wait until 2004 to have the minimum ten years of residence required to be eligible for a partial pension under section 3 of the Old Age Security Act, R.
- Evidence: `reasoning_application` cue `because` at chunk `4985910` offsets `90-97`; context: [8] In 1997, her husband filed a second application on behalf of his wife and was refused because the applicant’s second visa was dated 1994 and not 1986.
- Evidence: `reasoning_application` cue `applied` at chunk `4985911` offsets `54-61`; context: [9] Following the death of her husband, the applicant applied for welfare (Solidarité sociale du Québec) in May 1998.
- Evidence: `reasoning_application` cue `therefore` at chunk `4985912` offsets `112-121`; context: She therefore applied a third time and was refused because she had not yet met the ten-year qualifying period.
- Evidence: `governing_rule` cue `under` at chunk `4985913` offsets `147-152`; context: [11] On October 24, 2003, she filed a fourth application for Old Age Security (OAS) as well as for the Guaranteed Income Supplement (GIS) benefits under the Act.

#### 20898:2:subtheme:2 · paragraphs 13-24

- Raw key terms: `applicant, july, minister, august, canada, decision, heinz, tribunal`
- Display key terms: `july, august, heinz`
- Argument roles: `counterargument_limitation, disposition, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, issue, reasoning_application Display terms: july, august, heinz Application context: The interview took place in French and one of the applicant’s sons, Heinz, acted as an interpreter because the applicant speaks only Spanish. Operative outcome context: [16] On March 3, 2005, the Minister of Human Resources and Social Development (the Minister) notified the applicant that her application had been allowed. | [22] In its decision dated July 26, 2006, the Tribunal dismissed the applicant’s appeal and upheld the Minister’s decision. Evidence spans paragraphs 13-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4985914` offsets `122-129`; context: [12] On November 26, 2003, an investigation was initiated by the Programme de la sécurité du revenu in order to determine whether the applicant was eligible for OAS and GIS benefits.
- Evidence: `reasoning_application` cue `because` at chunk `4985915` offsets `178-185`; context: The interview took place in French and one of the applicant’s sons, Heinz, acted as an interpreter because the applicant speaks only Spanish.
- Evidence: `counterargument_limitation` cue `However` at chunk `4985918` offsets `155-162`; context: However, she was only given a partial pension, namely 10/40ths of the full pension, as well as the Guaranteed Income Supplement beginning in September 2004.
- Evidence: `disposition` cue `allowed` at chunk `4985918` offsets `146-153`; context: [16] On March 3, 2005, the Minister of Human Resources and Social Development (the Minister) notified the applicant that her application had been allowed.
- Evidence: `disposition` cue `dismissed` at chunk `4985924` offsets `55-64`; context: [22] In its decision dated July 26, 2006, the Tribunal dismissed the applicant’s appeal and upheld the Minister’s decision.

#### Section text

I. Factual background

[2] The applicant, Elsa Valdivia De Bustamante, is a widow, retired, born on May 8, 1926, in Arequipa, Peru. She came to Canada for the first time in 1970 with a visitor’s visa to visit her son. She also applied for a social insurance card.

[3] After a stay of about two months in Canada, she returned to Peru. On March 3, 1980, the applicant’s spouse, the late Ramon Bustamante, immigrated to Canada and was granted citizenship in 1986. He died on February 7, 1998, in Montréal.

[4] The applicant arrived in Canada in 1986 to join her husband, after receiving a permanent resident visa after her son, Julio Ernesto, sponsored her. This sponsorship was valid for a ten-year period.

[5] The applicant and her husband have six children who came to Canada at different times, but all received Canadian citizenship status.

[6] In August 1994, the applicant’s sponsorship was replaced when her husband sponsored her. She then obtained a second valid visa for a ten-year period, until 2004. The applicant was conferred citizenship in 1998.

[7] In 1996, the applicant’s spouse applied for the first time for Old Age Security on her behalf, but this was refused because the husband was already receiving full pension.

[8] In 1997, her husband filed a second application on behalf of his wife and was refused because the applicant’s second visa was dated 1994 and not 1986. The applicant therefore had to wait until 2004 to have the minimum ten years of residence required to be eligible for a partial pension under section 3 of the Old Age Security Act, R.S. 1985, c. O-9 (the Act).

[9] Following the death of her husband, the applicant applied for welfare (Solidarité sociale du Québec) in May 1998. She also received benefits from the Régie des rentes du Québec as a surviving spouse.

[10] In 2002, she received a letter explaining to her that she could qualify for Old Age Security benefits. She therefore applied a third time and was refused because she had not yet met the ten-year qualifying period.

[11] On October 24, 2003, she filed a fourth application for Old Age Security (OAS) as well as for the Guaranteed Income Supplement (GIS) benefits under the Act. In that application, she stated that she had arrived in Canada on July 25, 1986, and that she had obtained Canadian Citizenship in 1998. She did not mention any period of absence from Canada after her arrival in 1986.

[12] On November 26, 2003, an investigation was initiated by the Programme de la sécurité du revenu in order to determine whether the applicant was eligible for OAS and GIS benefits.

[13] In December 2003, there was an unscheduled visit to the applicant’s home. The interview took place in French and one of the applicant’s sons, Heinz, acted as an interpreter because the applicant speaks only Spanish.

[14] Following this investigation, she was sent a questionnaire so that she could provide all of the details about her departures from and arrivals to Canada between July 25, 1986, and August 29, 1994.

[15] On October 1, 2004, the matter was the subject of new assessment of the applicant’s residence.

[16] On March 3, 2005, the Minister of Human Resources and Social Development (the Minister) notified the applicant that her application had been allowed. However, she was only given a partial pension, namely 10/40ths of the full pension, as well as the Guaranteed Income Supplement beginning in September 2004.

[17] A minimum period of ten years of residence in Canada is required to qualify for a partial pension. According to the Minister, the applicant satisfied this requirement in August 2004.

[18] An application to reconsider was sent to the Minister to have the calculation begin in July 1996 rather than August 2004.

[19] On April 29, 2005, the Minister confirmed the decision dated March 3, 2005.

[20] On July 1, 2005, her son Heinz contested this decision.

[21] On June 21, 2006, a Review Tribunal (Tribunal) was convened in Montréal. The applicant’s son, Heinz, represented his mother and a French-Spanish interpreter was in attendance.

[22] In its decision dated July 26, 2006, the Tribunal dismissed the applicant’s appeal and upheld the Minister’s decision.

[23] The applicant alleges that the Tribunal erred in failing to accept that for the purposes of the Act she had been a resident of Canada since July 1986.


## 20898:3 · paragraphs 25-30

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `67d98e0127e7ca1874b5308eb6ce244bd8fe514266c9ca9cd52f43a9563285a8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20898:3:subtheme:1 · paragraphs 25-30

- Raw key terms: `applicant, canada, decision, tribunal, period, absence, absent, july`
- Display key terms: `period, absence, absent, july`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: period, absence, absent, july Application context: The Tribunal wrote the following at page 7 of the decision: The most likely explanation is that the Appellant lost her right to reside in Canada because she was absent for too long and could not return legally. Operative outcome context: [26] The Tribunal determined that the applicant had not satisfied the burden of proof that she had for her appeal to be allowed. Evidence spans paragraphs 25-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4985926` offsets `9-14`; context: [24] The issue is whether the Tribunal erred in upholding the Minister’s decision to use September 1994 as the date that the applicant’s permanent residence began in Canada.
- Evidence: `evidence_fact` cue `determined that` at chunk `4985928` offsets `18-33`; context: [26] The Tribunal determined that the applicant had not satisfied the burden of proof that she had for her appeal to be allowed.
- Evidence: `disposition` cue `allowed` at chunk `4985928` offsets `120-127`; context: [26] The Tribunal determined that the applicant had not satisfied the burden of proof that she had for her appeal to be allowed.
- Evidence: `evidence_fact` cue `evidence` at chunk `4985929` offsets `173-181`; context: [27] The Tribunal states that the absence was not related to a reason personal to the applicant, but rather related to her daughter’s medical condition and that there is no evidence supporting a finding that it was impossible for the applicant to return to Canada during that period.
- Evidence: `reasoning_application` cue `because` at chunk `4985930` offsets `453-460`; context: The Tribunal wrote the following at page 7 of the decision:
The most likely explanation is that the Appellant lost her right to reside in Canada because she was absent for too long and could not return legally.

#### Section text

II. Issues

[24] The issue is whether the Tribunal erred in upholding the Minister’s decision to use September 1994 as the date that the applicant’s permanent residence began in Canada.
III. Relevant legislation

[25] The relevant legislation is in Annex A at the end of these reasons.
IV. Impugned decision

[26] The Tribunal determined that the applicant had not satisfied the burden of proof that she had for her appeal to be allowed. According to the Tribunal, the applicant had allegedly been absent from Canada for 27 of 35 months between July 1986 and June 1989. This “showed that she did not in fact intend to settle permanently in Canada; in fact, she was absent for 27 months of the initial 35‑month period, which only shows that she was passing through Canada and did not reside here” (page 6, Tribunal decision).

[27] The Tribunal states that the absence was not related to a reason personal to the applicant, but rather related to her daughter’s medical condition and that there is no evidence supporting a finding that it was impossible for the applicant to return to Canada during that period.

[28] The Tribunal adds that the period between July 1989 and August 28, 1994, cannot be considered as a period of residence in Canada. The explanation given by the applicant to justify her absence was not accepted. She had alleged that she had been obliged to return to Peru while awaiting a new entry visa. The Tribunal wrote the following at page 7 of the decision:
The most likely explanation is that the Appellant lost her right to reside in Canada because she was absent for too long and could not return legally.

## 20898:4 · paragraphs 31-31

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `39473dbf5fca7b56465eef773d3f0dd5f895eb19aae4d0af10edaf9efe83ecb2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20898:4:subtheme:1 · paragraphs 31-31

- Raw key terms: `access, applicant, five, healthcare, july, observes, professional, september`
- Display key terms: `access, five, healthcare, july, observes, professional, september`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: access, five, healthcare, july, observes, professional, september No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 31-31. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

[29] The Tribunal also observes that the applicant did not access the services of a healthcare professional between July 1989 and September 1994, i.e. for more than five years.


## 20898:5 · paragraphs 32-39

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `8405920a074fb9afa0838eee6f5c4aeda9200fa224b0be337f903c4798ec848b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20898:5:subtheme:1 · paragraphs 32-33

- Raw key terms: `review, standard, analysis, appropriate, canada, chhabu, court, determined`
- Display key terms: `review, standard, analysis, appropriate, chhabu, determined`
- Argument roles: `governing_rule`
- Explanation: Observed roles: governing_rule Display terms: review, standard, analysis, appropriate, chhabu, determined Rule/authority context: 296 at paragraphs 20 to 24, where the Federal Court determined in a matter similar to the one at bar that the appropriate standard of review was that of reasonableness simpliciter. Evidence spans paragraphs 32-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `standard of review` at chunk `4985932` offsets `239-257`; context: 296 at paragraphs 20 to 24, where the Federal Court determined in a matter similar to the one at bar that the appropriate standard of review was that of reasonableness simpliciter.

#### 20898:5:subtheme:2 · paragraphs 34-39

- Raw key terms: `court, paragraph, canada, case, circumstances, decision, definition, determination`
- Display key terms: `paragraph, case, circumstances, definition, determination`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: paragraph, case, circumstances, definition, determination Evidence spans paragraphs 34-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4985933` offsets `77-82`; context: explains that
The issue of residency in relation to OAS [Old Age Security] eligibility is one that the Review Tribunal is regularly called upon to determine.
- Evidence: `counterargument_limitation` cue `however` at chunk `4985933` offsets `392-399`; context: In interpreting the definition of residency, however, the Court is equally or better positioned.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4985936` offsets `388-394`; context: The Court must not intervene so long as the administrative tribunal’s decision is reasonable and it cannot substitute its own opinion based only on the ground that it would have made a different determination.

#### Section text

V. Analysis
A. Standard of review

[30] The respondent referred to Canada (Minister of Human Resources Development) v. Chhabu, 2005 FC 1277, 280 F.T.R. 296 at paragraphs 20 to 24, where the Federal Court determined in a matter similar to the one at bar that the appropriate standard of review was that of reasonableness simpliciter.

[31] At paragraph 21 of Chhabu, supra, Layden-Stevenson J. explains that
The issue of residency in relation to OAS [Old Age Security] eligibility is one that the Review Tribunal is regularly called upon to determine. The factual circumstances of each case call for findings that fall within its expertise and thus militate in favour of deference. In interpreting the definition of residency, however, the Court is equally or better positioned.

[32] The Court made the same determination in Canada (Minister of Human Resources Development) v. Leavitt, 2005 FC 664, 272 F.T.R. 241 at paragraph 17 and Kombargi v. Canada (Minister of Social Development), 2006 FC 1511, 306 F.T.R. 202 at paragraph 7.

[33] In the recent decision in Dunsmuir v. New Brunswick, 2008 SCC 9, [2008] 1 S.C.R. 190, the Supreme Court stated that there were now two standards of review: correctness and reasonableness.

[34] Reasonableness mainly concerns the justification of the decision and the intelligibility of the decision-making process, as well as the decision falling within a range of possible, acceptable outcomes which are defensible in respect of the facts and law (Dunsmuir, at paragraph 47). The Court must not intervene so long as the administrative tribunal’s decision is reasonable and it cannot substitute its own opinion based only on the ground that it would have made a different determination. I consider that the appropriate standard in this case is that of reasonableness.
B. Was the Tribunal’s decision reasonable?

[35] The applicant’s primary argument is that she was given a permanent residence visa in July 1986 and in August 1994 as well as her Canadian citizenship in 1998. She considers that the Minister should have started the ten-year period in 1986.

[36] On the respondent’s part, he is of the opinion that these facts are not a determinative factor serving as a basis for saying that a person “resided in Canada” in accordance with subsection 3(2) of the Act, which sets out the circumstances in which a retirement pension is payable to a person. The term “resided”, referred to in paragraph 3(2)(b), is not defined in the Act, but there is a definition in the Regulations. Subsection 21(4) of the Regulations governs cases where any interval of absence from Canada of a person resident in Canada that is temporary is deemed not to have interrupted that person’s residence or presence in Canada. A temporary absence of less than one year does not result in an interruption.

## 20898:6 · paragraphs 40-46

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c27f72cdd857eb957b6a22e7e6fa15137a3a0bd62b6245767153b2a790c54d7d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20898:6:subtheme:1 · paragraphs 40-46

- Raw key terms: `canada, applicant, residence, absence, court, period, tribunal, accepted`
- Display key terms: `residence, absence, period, accepted`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: residence, absence, period, accepted Rule/authority context: 111, at paragraph 58, the Federal Court explained that “residency is a factual issue that requires an examination of the whole context of the individual under scrutiny. Application context: [40] The same applies to the Tribunal’s finding regarding an absence of residence during the period from July 1989 to September 1994. Evidence spans paragraphs 40-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4985939` offsets `168-173`; context: 111, at paragraph 58, the Federal Court explained that “residency is a factual issue that requires an examination of the whole context of the individual under scrutiny.
- Evidence: `governing_rule` cue `under` at chunk `4985939` offsets `242-247`; context: 111, at paragraph 58, the Federal Court explained that “residency is a factual issue that requires an examination of the whole context of the individual under scrutiny.
- Evidence: `issue` cue `whether` at chunk `4985940` offsets `98-105`; context: [38] In Ding, supra, the Court referred to several factors which may be considered in determining whether the residence conditions have been observed: ties in the form of personal property; social ties in Canada; other fiscal ties in Canada (medical coverage, driver's licence, rental lease, tax records, etc); ties in another country; regularity and length of visits to Canada, as well as the frequency and length of absences from Canada; the lifestyle of the person or his establishment here.
- Evidence: `reasoning_application` cue `applies` at chunk `4985942` offsets `14-21`; context: [40] The same applies to the Tribunal’s finding regarding an absence of residence during the period from July 1989 to September 1994.
- Evidence: `evidence_fact` cue `evidence` at chunk `4985943` offsets `228-236`; context: The applicant did not file any evidence to establish that she was permanently residing in Canada between 1989 and 1994.
- Evidence: `evidence_fact` cue `evidence` at chunk `4985944` offsets `9-17`; context: [42] The evidence establishes rather the applicant’s establishment in Canada since 1994.

#### Section text

[37] In Canada (Minister of Human Resources Development) v. Ding, 2005 FC 76, 286 F.T.R. 111, at paragraph 58, the Federal Court explained that “residency is a factual issue that requires an examination of the whole context of the individual under scrutiny.” The respondent states that holding a designated visa under the Immigration Act is not a determinative factor for finding that a person “resided in Canada” in accordance with subsection 3(2) of the Act. In his opinion, even the fact that he is a Canadian citizen is not sufficient to determine a person’s residence in Canada.

[38] In Ding, supra, the Court referred to several factors which may be considered in determining whether the residence conditions have been observed: ties in the form of personal property; social ties in Canada; other fiscal ties in Canada (medical coverage, driver's licence, rental lease, tax records, etc); ties in another country; regularity and length of visits to Canada, as well as the frequency and length of absences from Canada; the lifestyle of the person or his establishment here.

[39] The factors retained by the Tribunal to uphold the Minister’s decision are in my opinion reasonable. The applicant’s absence for a period of about 27 months of a 35-month period justifies an interruption of residence. The dismissal of the applicant’s explanations regarding this absence is not unreasonable.

[40] The same applies to the Tribunal’s finding regarding an absence of residence during the period from July 1989 to September 1994. The fact that the applicant did not have access to the services of healthcare professionals in Quebec between these dates supports this finding.

[41] The change in sponsorship was not accepted by the Tribunal as a reason given by the applicant to establish an involuntary absence from Canada. Again the Court does not see a reviewable error. The applicant did not file any evidence to establish that she was permanently residing in Canada between 1989 and 1994.

[42] The evidence establishes rather the applicant’s establishment in Canada since 1994. She filed income tax returns dating back to 1995. Further, a lease in her name was issued for the period from July 1, 2000 to June 30, 2001 and utility bills were filed for the years 2002 and 2003.

[43] At the hearing the respondents asked that the style of cause be amended so that only the Attorney General of Canada appears therein. This verbal motion is accepted.


## 20898:7 · paragraphs 47-48

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `96390e8b83a92734bd9f3a4eb30f5c0482455a2f5e6cf47381f006e143791639`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20898:7:subtheme:1 · paragraphs 47-48

- Raw key terms: `attorney, canada, cause, date, style, absence, absences, absente`
- Display key terms: `date, style, absence, absences, absente`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: date, style, absence, absences, absente No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 47-48. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THE COURT ORDERS that:
1. The application for judicial review be dismissed without costs;
2. The style of cause be amended so that only the Attorney General of Canada appears therein.
“Michel Beaudry”
Judge
Certified true translation
Kelley Harvey, BA, BCL, LLB
ANNEX A
Section 3 of the Old Age Security Act, R.S. 1985, c. O-9 :
3. (1) Subject to this Act and the regulations, a full monthly pension may be paid to
(a) every person who was a pensioner on July 1, 1977;
(b) every person who
(i) on July 1, 1977 was not a pensioner but had attained twenty-five years of age and resided in Canada or, if that person did not reside in Canada, had resided in Canada for any period after attaining eighteen years of age or possessed a valid immigration visa,
(ii) has attained sixty-five years of age, and
(iii) has resided in Canada for the ten years immediately preceding the day on which that person’s application is approved or, if that person has not so resided, has, after attaining eighteen years of age, been present in Canada prior to those ten years for an aggregate period at least equal to three times the aggregate periods of absence from Canada during those ten years, and has resided in Canada for at least one year immediately preceding the day on which that person’s application is approved; and
(c) every person who
(i) was not a pensioner on July 1, 1977,
(ii) has attained sixty-five years of age, and
(iii) has resided in Canada after attaining eighteen years of age and prior to the day on which that person’s application is approved for an aggregate period of at least forty years.
(2) Subject to this Act and the regulations, a partial monthly pension may be paid for any month in a payment quarter to every person who is not eligible for a full monthly pension under subsection (1) and
(a) has attained sixty-five years of age; and
(b) has resided in Canada after attaining eighteen years of age and prior to the day on which that person’s application is approved for an aggregate period of at least ten years but less than forty years and, where that aggregate period is less than twenty years, was resident in Canada on the day preceding the day on which that person’s application is approved.
(3) The amount of a partial monthly pension, for any month, shall bear the same relation to the full monthly pension for that month as the aggregate period that the applicant has resided in Canada after attaining eighteen years of age and prior to the day on which the application is approved, determined in accordance with subsection (4), bears to forty years.
(4) For the purpose of calculating the amount of a partial monthly pension under subsection (3), the aggregate period described in that subsection shall be rounded to the lower multiple of a year when it is not a multiple of a year.
(5) Once a person’s application for a partial monthly pension has been approved, the amount of monthly pension payable to that person under this Part may not be increased on the basis of subsequent periods of residence in Canada
3. (1) Sous réserve des autres dispositions de la présente loi et de ses règlements, la pleine pension est payable aux personnes suivantes :
a) celles qui avaient la qualité de pensionné au 1er juillet 1977;
b) celles qui, à la fois :
(i) sans être pensionnées au 1er juillet 1977, avaient alors au moins vingt-cinq ans et résidaient au Canada ou y avaient déjà résidé après l’âge de dix-huit ans, ou encore étaient titulaires d’un visa d’immigrant valide,
(ii) ont au moins soixante-cinq ans,
(iii) ont résidé au Canada pendant les dix ans précédant la date d’agrément de leur demande, ou ont, après l’âge de dix-huit ans, été présentes au Canada, avant ces dix ans, pendant au moins le triple des périodes d’absence du Canada au cours de ces dix ans tout en résidant au Canada pendant au moins l’année qui précède la date d’agrément de leur demande;
c) celles qui, à la fois :
(i) n’avaient pas la qualité de pensionné au 1er juillet 1977,
(ii) ont au moins soixante-cinq ans,
(iii) ont, après l’âge de dix-huit ans, résidé en tout au Canada pendant au moins quarante ans avant la date d’agrément de leur demande.
(2) Sous réserve des autres dispositions de la présente loi et de ses règlements, une pension partielle est payable aux personnes qui ne peuvent bénéficier de la pleine pension et qui, à la fois :
a) ont au moins soixante-cinq ans;
b) ont, après l’âge de dix-huit ans, résidé en tout au Canada pendant au moins dix ans mais moins de quarante ans avant la date d’agrément de leur demande et, si la période totale de résidence est inférieure à vingt ans, résidaient au Canada le jour précédant la date d’agrément de leur demande.
(3) Pour un mois donné, le montant de la pension partielle correspond aux n/40 de la pension complète, n étant le nombre total — arrondi conformément au paragraphe (4) — d’années de résidence au Canada depuis le dix-huitième anniversaire de naissance jusqu’à la date d’agrément de la demande.
(4) Le nombre total d’années de résidence au Canada est arrondi au chiffre inférieur.
(5) Les années de résidence postérieures à l’agrément d’une demande de pension partielle ne peuvent influer sur le montant de celle-ci.
Section 20 and subsections 21(1) and (4) of the Old Age Security Regulations, C.R.C., c. 1246, (the Regulations) bear on the definition of “residence in Canada.”
20. For the purpose of enabling the Minister to determine the eligibility of an applicant in respect of residence in Canada, there shall be furnished by the applicant or on his behalf a statement giving full particulars of all periods of residence in Canada and of all absences therefrom relevant to such eligibility.
20. Pour permettre au ministre de décider de l’admissibilité du demandeur, quant à la résidence au Canada, le demandeur ou quelqu’un en son nom doit présenter une déclaration contenant les détails complets de toutes les périodes de résidence au Canada et de toutes les absences de ce pays se rapportant à cette admissibilité.
21. (1) For the purposes of the Act and these Regulations,
(a) a person resides in Canada if he makes his home and ordinarily lives in any part of Canada; and
(b) a person is present in Canada when he is physically present in any part of Canada.
(4) Any interval of absence from Canada of a person resident in Canada that is
(a) of a temporary nature and does not exceed one year,
(b) for the purpose of attending a school or university, or
(c) specified in subsection (5) shall be deemed not to have interrupted that person’s residence or presence in Canada.
21. (1) Aux fins de la Loi et du présent règlement,
a) une personne réside au Canada si elle établit sa demeure et vit ordinairement dans une région du Canada; et
b) une personne est présente au Canada lorsqu’elle se trouve physiquement dans une région du Canada.
(4) Lorsqu’une personne qui réside au Canada s’absente du Canada et que son absence
a) est temporaire et ne dépasse pas un an,
b) a pour motif la fréquentation d’une école ou d’une université, ou
c) compte parmi les absences mentionnées au paragraphe (5), cette absence est réputée n’avoir pas interrompu la résidence ou la présence de cette personne au Canada.
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: T-1583-06
STYLE OF CAUSE : ELSA VALDIVIA DE BUSTAMANTE and
ATTORNEY GENERLA OF CANADA
PLACE OF HEARING: Montréal, Quebec
DATE OF HEARING: October 1, 2008
REASONS FOR 

## 20898:8 · paragraphs 49-49

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7deaeba8c5002b28f7e7bfb1a9d08aa047bb7ea96b94d1a547d89e6de7da59f2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20898:8:subtheme:1 · paragraphs 49-49

- Raw key terms: `appearances, applicant, attorney, beaudry, bustamante, canada, date, deputy`
- Display key terms: `beaudry, bustamante, date, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: beaudry, bustamante, date, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 49-49. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDEMENT: Beaudry J.
DATE OF REASONS: October 3, 2008
APPEARANCES:
Heinz Bustamante FOR THE APPLICANT
(applicant’s son)
Sandra Gruescu FOR THE RESPONDENT
SOLICITORS OF RECORD
n/a FOR THE APPLICANT
John H. Sims, QC FOR THE RESPONDENT
Deputy Attorney General of Canada
Ottawa, Ontario
