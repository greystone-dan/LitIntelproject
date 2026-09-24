# Discussion Units: case 23995

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **26**
- Continuity pairs: **25**
- Discussion Units: **2**
- Paragraph source hashes: **26**
- Sub-themes: **5**

## 23995:1 · paragraphs 0-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ab76af3bd5a02637c75578a1824880e91a272557e3aba1972eb002f9014a8635`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23995:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `applicant, decision, canada, immigration, reasons, accident, accordingly, alleges`
- Display key terms: `accident, accordingly, alleges`
- Argument roles: `disposition, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, reasoning_application Display terms: accident, accordingly, alleges Rule/authority context: [1] The applicant seeks to set aside a decision of the Refugee Protection Division of the Immigration and Refugee Board of Canada (the Board) that the applicant is neither a Convention refugee nor a person in need of pro Application context: Accordingly, the application is granted. Operative outcome context: Accordingly, the application is granted. Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5126329` offsets `228-239`; context: [1] The applicant seeks to set aside a decision of the Refugee Protection Division of the Immigration and Refugee Board of Canada (the Board) that the applicant is neither a Convention refugee nor a person in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA).
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5126331` offsets `63-74`; context: Accordingly, the application is granted.
- Evidence: `disposition` cue `granted` at chunk `5126331` offsets `95-102`; context: Accordingly, the application is granted.

#### 23995:1:subtheme:2 · paragraphs 4-6

- Raw key terms: `applicant, board, credibility, evidence, finding, absence, alone, assessment`
- Display key terms: `credibility, finding, absence, alone, assessment`
- Argument roles: `counterargument_limitation, evidence_fact`
- Explanation: Observed roles: counterargument_limitation, evidence_fact Display terms: credibility, finding, absence, alone, assessment Evidence spans paragraphs 4-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `however` at chunk `5126332` offsets `150-157`; context: In this case however, the Board’s assessment of credibility is flawed.
- Evidence: `evidence_fact` cue `evidence` at chunk `5126333` offsets `51-59`; context: [5] The Board emphasized the lack of corroborating evidence that the applicant’s stepfather is a tribal police officer and that her mother is paralyzed.
- Evidence: `evidence_fact` cue `evidence` at chunk `5126334` offsets `147-155`; context: [6] There is no general requirement for corroboration and it would be an error to make a credibility finding based on the absence of corroborative evidence alone: Dundar v Canada (Citizenship and Immigration), 2007 FC 1026, paras 19-22.

#### 23995:1:subtheme:3 · paragraphs 7-21

- Raw key terms: `board, applicant, police, evidence, protection, state, testimony, canada`
- Display key terms: `police, protection, state, testimony`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: police, protection, state, testimony Evidence spans paragraphs 7-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5126335` offsets `34-42`; context: [7] If there is a valid reason to question the claimant’s credibility, the Board may draw a negative inference from a failure to provide corroborative evidence that would reasonably be expected.
- Evidence: `evidence_fact` cue `evidence` at chunk `5126335` offsets `151-159`; context: [7] If there is a valid reason to question the claimant’s credibility, the Board may draw a negative inference from a failure to provide corroborative evidence that would reasonably be expected.
- Evidence: `evidence_fact` cue `record` at chunk `5126336` offsets `14-20`; context: [8] Here, the record contains a photograph of a woman in a wheelchair, apparently the applicant’s mother.
- Evidence: `evidence_fact` cue `testimony` at chunk `5126337` offsets `144-153`; context: First, the veracity of the applicant’s testimony as to her mother’s disability was not raised or challenged during the hearing.
- Evidence: `evidence_fact` cue `testimony` at chunk `5126338` offsets `149-158`; context: Plausibility findings should only be made in the clearest of cases, when the applicant’s testimony is outside of the realm of what could reasonably be expected or when the documentary evidence demonstrates that the events could not have taken place as alleged.
- Evidence: `evidence_fact` cue `testimony` at chunk `5126339` offsets `229-238`; context: Refugee claimants come from diverse backgrounds and the events described in their testimony are often far removed from the ordinary life experience of Canadians.
- Evidence: `evidence_fact` cue `evidence` at chunk `5126344` offsets `314-322`; context: Refugee protection is intended for exceptional circumstances, where a claimant can produce clear and convincing evidence that state protection is inadequate, on a balance of probabilities: Flores Carrillo v Canada (Minister of Citizenship and Immigration), 2008 FCA 94.
- Evidence: `evidence_fact` cue `evidence` at chunk `5126345` offsets `33-41`; context: [17] The applicant provided such evidence, in stating that the police considered her complaints a “family matter” and that the Traditional Authority sent her away with the instruction to obey her family.
- Evidence: `evidence_fact` cue `found that` at chunk `5126346` offsets `15-25`; context: [18] The Board found that if the applicant’s story was true, she could have gone to the police commissioner or hired a lawyer, despite the applicant’s testimony that she was not aware of other avenues for assistance.
- Evidence: `evidence_fact` cue `testimony` at chunk `5126347` offsets `39-48`; context: [19] The Board ignored the applicant’s testimony that it was shameful to seek police protection from rape.
- Evidence: `evidence_fact` cue `evidence` at chunk `5126348` offsets `55-63`; context: [20] The Board fairly considered the country condition evidence which provides that spousal rape is illegal in Namibia and that forced marriage is contrary to the Constitution.
- Evidence: `counterargument_limitation` cue `but` at chunk `5126348` offsets `195-198`; context: This is relevant, but not determinative in analyzing state protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `5126349` offsets `61-69`; context: [21] The Board selectively quoted from the country condition evidence, ignoring statements that women in Namibia may be forced into marrying a family member or a deceased family member’s husband.

#### 23995:1:subtheme:4 · paragraphs 22-24

- Raw key terms: `analysis, applicant, board, immigration, walvis, accept, alternative, application`
- Display key terms: `analysis, walvis, accept, alternative`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: analysis, walvis, accept, alternative Application context: The Board also rejected the applicant’s testimony that her stepfather could find her in Walvis Bay because of his position as a tribal police officer. Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that the application for judicial review is granted. Evidence spans paragraphs 22-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5126350` offsets `175-180`; context: The Board’s analysis of this issue flowed directly from its earlier findings and so it cannot be sustained.
- Evidence: `evidence_fact` cue `found that` at chunk `5126350` offsets `24-34`; context: [22] Finally, the Board found that the applicant had an internal flight alternative in Walvis Bay, a city six hours away from her village by car.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5126350` offsets `233-239`; context: The Board’s analysis of this issue flowed directly from its earlier findings and so it cannot be sustained.
- Evidence: `issue` cue `question` at chunk `5126351` offsets `675-683`; context: There is no question for certification.
- Evidence: `evidence_fact` cue `testimony` at chunk `5126351` offsets `225-234`; context: The Board also rejected the applicant’s testimony that her stepfather could find her in Walvis Bay because of his position as a tribal police officer.
- Evidence: `reasoning_application` cue `because` at chunk `5126351` offsets `284-291`; context: The Board also rejected the applicant’s testimony that her stepfather could find her in Walvis Bay because of his position as a tribal police officer.
- Evidence: `disposition` cue `granted` at chunk `5126351` offsets `503-510`; context: JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is granted.

#### Section text

Ndjavera v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2013-04-30
Neutral citation
2013 FC 452
File numbers
IMM-7018-12
Decision Content
Federal Court
Cour fédérale
Date: 20130430
Docket: IMM-7018-12
Citation: 2013 FC 452
Ottawa, Ontario, April 30, 2013
PRESENT: The Honourable Mr. Justice Rennie
BETWEEN:
EVELINE NDJAVERA
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] The applicant seeks to set aside a decision of the Refugee Protection Division of the Immigration and Refugee Board of Canada (the Board) that the applicant is neither a Convention refugee nor a person in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA).

[2] The applicant is a young woman who alleges she has been forced to marry her stepfather in Namibia. The applicant testified that her mother became paralyzed after a serious accident and that she is now compelled by custom to fulfill her mother’s “wifely role” and ensure that her stepfather’s wealth stays in the family. She testified that her stepfather paid a bride price for her and that he has repeatedly raped her.

[3] For the reasons that follow, the decision is unreasonable. Accordingly, the application is granted.
Credibility

[4] The Board rejected the applicant’s claim on the basis of credibility, a finding that is generally entitled to substantial deference. In this case however, the Board’s assessment of credibility is flawed.

[5] The Board emphasized the lack of corroborating evidence that the applicant’s stepfather is a tribal police officer and that her mother is paralyzed.

[6] There is no general requirement for corroboration and it would be an error to make a credibility finding based on the absence of corroborative evidence alone: Dundar v Canada (Citizenship and Immigration), 2007 FC 1026, paras 19-22.

[7] If there is a valid reason to question the claimant’s credibility, the Board may draw a negative inference from a failure to provide corroborative evidence that would reasonably be expected. Much depends on the type of evidence at issue and whether it relates to a central aspect of the claim. Corroborative evidence is most valuable when it is independently generated by a neutral source. It may be unreasonable to expect a refugee claimant to generate or collect documentation not already available before fleeing. Furthermore, when the alleged assailant controls the documents at issue, as here, it would be unreasonable to expect an applicant to obtain it. In this case, there is no basis to believe that the applicant would have access to her mother’s medical records or her stepfather’s police credentials.

[8] Here, the record contains a photograph of a woman in a wheelchair, apparently the applicant’s mother. Additionally, there is a letter from a friend in Namibia, explaining that the applicant had stayed at her home when fleeing her stepfather’s until her family came and forced her to return. This friend states that the applicant’s stepfather is a police officer. The Board’s reasons are silent with respect to this evidence.

[9] There are two other aspects to the Board’s reasoning regarding corroboration that render it unsound. First, the veracity of the applicant’s testimony as to her mother’s disability was not raised or challenged during the hearing. Second, the fact that the applicant’s stepfather is a tribal police officer was a collateral point, not germane to the applicant’s principle claim for relief.

[10] The Board’s plausibility finding is also unreasonable. Plausibility findings should only be made in the clearest of cases, when the applicant’s testimony is outside of the realm of what could reasonably be expected or when the documentary evidence demonstrates that the events could not have taken place as alleged.

[11] The Board must exercise caution in assessing plausibility: Valtchev v Canada (Minister of Citizenship and Immigration), 2001 FCT 776, para 7. Refugee claimants come from diverse backgrounds and the events described in their testimony are often far removed from the ordinary life experience of Canadians. What appears implausible from a Canadian perspective may be ordinary or expected in other countries. Furthermore, there are many commonly held assumptions regarding domestic violence and gender-based persecution, which is why the Chairperson’s Guidelines on Women Refugee Claimants Fearing Gender-Related Persecution (Gender Guidelines) is a crucial analytical aid.

[12] The applicant testified that her uncle took her young child in order to coerce her into marrying her stepfather. The applicant testified that she unsuccessfully sought assistance from the police and the Traditional Authority to regain custody of her child and stop the forced marriage.

[13] The Board considered it implausible that the applicant would not have done more, namely complaining to the Commissioner of Police or hiring a lawyer to commence legal proceedings. The Board stated that assuming the applicant’s story is true, she did not receive “good service” from the police and should have complained.

[14] The Board erred in making this plausibility finding without adequate regard to the applicant’s age, culture, background and prior experiences: Cooper v Canada (Citizenship and Immigration), 2012 FC 118, para 4. As set out in the Gender Guidelines, a claimant’s steps in seeking state protection must be assessed with regard to “the social, cultural, religious, and economic context in which the claimant finds herself.”
State Protection

[15] The Board’s finding on state protection is closely related to its credibility analysis.

[16] It is a foundational principle of refugee law that states are presumed to be willing and able to provide adequate protection for their citizens: Canada (Attorney General) v Ward, [1993] 2 SCR 689. Refugee protection is intended for exceptional circumstances, where a claimant can produce clear and convincing evidence that state protection is inadequate, on a balance of probabilities: Flores Carrillo v Canada (Minister of Citizenship and Immigration), 2008 FCA 94.

[17] The applicant provided such evidence, in stating that the police considered her complaints a “family matter” and that the Traditional Authority sent her away with the instruction to obey her family.

[18] The Board found that if the applicant’s story was true, she could have gone to the police commissioner or hired a lawyer, despite the applicant’s testimony that she was not aware of other avenues for assistance. The Board emphasized that she hired a lawyer for her refugee claim in Canada, without acknowledging her testimony that this lawyer was provided to her.

[19] The Board ignored the applicant’s testimony that it was shameful to seek police protection from rape. Again this is contrary to the Gender Guidelines: “If, for example, a woman has suffered gender-related persecution in the form of rape, she may be ostracized from her community for seeking protection from the state.”

[20] The Board fairly considered the country condition evidence which provides that spousal rape is illegal in Namibia and that forced marriage is contrary to the Constitution. This is relevant, but not determinative in analyzing state protection. The written law may not always be enforced, especially when it conflicts with deeply held traditions.

[21] The Board selectively quoted from the country condition evidence, ignoring statements that women in Namibia may be forced into marrying a family member or a deceased family member’s husband. The evidence states that marriage is a practice between families, not individuals, and that polygamy is permitted. All of this is highly relevant.
Internal Flight Alternative

[22] Finally, the Board found that the applicant had an internal flight alternative in Walvis Bay, a city six hours away from her village by car. The Board’s analysis of this issue flowed directly from its earlier findings and so it cannot be sustained.

[23] The Board stated that the applicant could reasonably be expected to obtain custody of her child before relocating, relying on its flawed state protection and credibility analysis. The Board also rejected the applicant’s testimony that her stepfather could find her in Walvis Bay because of his position as a tribal police officer. As previously set out, the Board did not accept that her stepfather holds this position.
JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is granted. The matter is referred back to the Immigration Refugee Board for reconsideration before a different member of the Board’s Refugee Protection Division. There is no question for certification.
"Donald J. Rennie"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-7018-12
STYLE OF CAUSE: EVELINE NDJAVERA v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Toronto, ON
DATE OF HEARING: April 23, 2013
REASONS FOR 

## 23995:2 · paragraphs 25-25

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a7f510e9f03e4ce34592aaf6a8b2513d824ad0ef8514f435152c7ae2f8a4eca8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23995:2:subtheme:1 · paragraphs 25-25

- Raw key terms: `appearances, applicant, april, attorney, barrister, canada, dadepo, dated`
- Display key terms: `april, barrister, dadepo, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: april, barrister, dadepo, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 25-25. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: RENNIE J.
DATED: April 30, 2013
APPEARANCES:
Mercy Dadepo
FOR THE APPLICANT
Jeannine Plamondon
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Mercy Dadepo
Barrister & Solicitor
North York, Ontario
FOR THE APPLICANT
William F. Pentney,
Deputy Attorney General of Canada
Toronto, Ontario
FOR THE RESPONDENT
