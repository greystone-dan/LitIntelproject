# Discussion Units: case 31963

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **23**
- Continuity pairs: **22**
- Discussion Units: **3**
- Paragraph source hashes: **23**
- Sub-themes: **7**

## 31963:1 · paragraphs 0-19

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b5fa573482168a59b6ca4b2b405d7acc22d5d66227321c5ca2541679a7351352`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 31963:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `applicant, prison, board, canada, state, states, united, clark-erskine`
- Display key terms: `prison, state, states, united, clark-erskine`
- Argument roles: `disposition, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, party_position, reasoning_application Display terms: prison, state, states, united, clark-erskine Position/evidence statements: He had been in Indiana State Prison where he claimed he was abused, beaten and denied his psychiatric medicines. Application context: [3] The Board found that the Applicant’s various crimes, including his escape from prison, were not of sufficient gravity to fall within Article 1(F)(b) and therefore not sufficient to exclude his application. Operative outcome context: He had been in Indiana State Prison where he claimed he was abused, beaten and denied his psychiatric medicines. Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claimed` at chunk `5488621` offsets `187-194`; context: He had been in Indiana State Prison where he claimed he was abused, beaten and denied his psychiatric medicines.
- Evidence: `evidence_fact` cue `record` at chunk `5488621` offsets `44-50`; context: [2] The Applicant has an extensive criminal record in both the United States and Canada.
- Evidence: `disposition` cue `denied` at chunk `5488621` offsets `221-227`; context: He had been in Indiana State Prison where he claimed he was abused, beaten and denied his psychiatric medicines.
- Evidence: `evidence_fact` cue `found that` at chunk `5488622` offsets `14-24`; context: [3] The Board found that the Applicant’s various crimes, including his escape from prison, were not of sufficient gravity to fall within Article 1(F)(b) and therefore not sufficient to exclude his application.
- Evidence: `reasoning_application` cue `therefore` at chunk `5488622` offsets `157-166`; context: [3] The Board found that the Applicant’s various crimes, including his escape from prison, were not of sufficient gravity to fall within Article 1(F)(b) and therefore not sufficient to exclude his application.
- Evidence: `evidence_fact` cue `found that` at chunk `5488623` offsets `60-70`; context: [4] As to prison conditions in the United States, the Board found that U.

#### 31963:1:subtheme:2 · paragraphs 5-7

- Raw key terms: `board, applicant, claim, prison, state, abuses, address, adequate`
- Display key terms: `prison, state, abuses, address, adequate`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: prison, state, abuses, address, adequate Application context: As to the Applicant’s personalized claim of torture and cruel and unusual punishment, the Board only concludes that incarceration as punishment for criminal offences is not cruel or unusual. Evidence spans paragraphs 5-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5488624` offsets `211-216`; context: Since the only institution at issue was the Indiana state prison, the reference suggests state involvement in his mistreatment.
- Evidence: `reasoning_application` cue `concludes` at chunk `5488626` offsets `311-320`; context: As to the Applicant’s personalized claim of torture and cruel and unusual punishment, the Board only concludes that incarceration as punishment for criminal offences is not cruel or unusual.

#### 31963:1:subtheme:3 · paragraphs 8-10

- Raw key terms: `applicant, board, hearing, since, witness, advised, alberta, allow`
- Display key terms: `hearing, since, witness, advised, alberta, allow`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: hearing, since, witness, advised, alberta, allow Application context: The Board refused to hear the witness because the Applicant had indicated at the hearing that he would not be calling a witness. Evidence spans paragraphs 8-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5488627` offsets `37-43`; context: [8] The Applicant raises a number of issues including whether he was singled out for persecution, errors of law in considering whether torture or cruel and unusual punishment had been inflicted, and error in concluding state protection was available.
- Evidence: `reasoning_application` cue `because` at chunk `5488629` offsets `133-140`; context: The Board refused to hear the witness because the Applicant had indicated at the hearing that he would not be calling a witness.

#### 31963:1:subtheme:4 · paragraphs 11-18

- Raw key terms: `applicant, board, justice, natural, witness, because, breach, decision`
- Display key terms: `justice, natural, witness, because, breach`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: justice, natural, witness, because, breach Position/evidence statements: [13] The Respondent acknowledges that a breach of natural justice occurred but contends that the evidence would have made no difference because the witness was from the Schizophrenic Society of Alberta and the Applicant  Application context: The reasons for not calling a witness were explained, the arrival of the witness was unexpected and it was unfair to deny this evidence because the Applicant was mistaken about whether his witness was available. | [13] The Respondent acknowledges that a breach of natural justice occurred but contends that the evidence would have made no difference because the witness was from the Schizophrenic Society of Alberta and the Applicant  Operative outcome context: [17] For these reasons, this judicial review will be granted, the original Board decision quashed and the matter referred back to a differently constituted panel of the Board for a new determination. Evidence spans paragraphs 11-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5488630` offsets `281-288`; context: The reasons for not calling a witness were explained, the arrival of the witness was unexpected and it was unfair to deny this evidence because the Applicant was mistaken about whether his witness was available.
- Evidence: `evidence_fact` cue `evidence` at chunk `5488630` offsets `231-239`; context: The reasons for not calling a witness were explained, the arrival of the witness was unexpected and it was unfair to deny this evidence because the Applicant was mistaken about whether his witness was available.
- Evidence: `reasoning_application` cue `because` at chunk `5488630` offsets `240-247`; context: The reasons for not calling a witness were explained, the arrival of the witness was unexpected and it was unfair to deny this evidence because the Applicant was mistaken about whether his witness was available.
- Evidence: `issue` cue `issue` at chunk `5488631` offsets `18-23`; context: [12] There was no issue of prejudice advanced by the Respondent and it is impossible to discern any other legitimate reason for refusing to hear the testimony.
- Evidence: `evidence_fact` cue `testimony` at chunk `5488631` offsets `149-158`; context: [12] There was no issue of prejudice advanced by the Respondent and it is impossible to discern any other legitimate reason for refusing to hear the testimony.
- Evidence: `party_position` cue `contends` at chunk `5488632` offsets `79-87`; context: [13] The Respondent acknowledges that a breach of natural justice occurred but contends that the evidence would have made no difference because the witness was from the Schizophrenic Society of Alberta and the Applicant is not schizophrenic.
- Evidence: `evidence_fact` cue `evidence` at chunk `5488632` offsets `97-105`; context: [13] The Respondent acknowledges that a breach of natural justice occurred but contends that the evidence would have made no difference because the witness was from the Schizophrenic Society of Alberta and the Applicant is not schizophrenic.
- Evidence: `reasoning_application` cue `because` at chunk `5488632` offsets `136-143`; context: [13] The Respondent acknowledges that a breach of natural justice occurred but contends that the evidence would have made no difference because the witness was from the Schizophrenic Society of Alberta and the Applicant is not schizophrenic.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5488633` offsets `78-87`; context: [14] The difficulty with the Respondent’s position is that the witness, in an affidavit filed in this judicial review, says that he intended to address the Board on the nature of bi-polar disorder, the efficacy of medications in treating this disorder and the state of the mentally ill held in jails in Canada and the United States.
- Evidence: `reasoning_application` cue `conclude` at chunk `5488634` offsets `27-35`; context: [15] It is not possible to conclude that the Applicant’s case is hopeless and that the breach of natural justice should be ignored because the result is inevitably the refusal of the application for protection (as occurred in cases such as Gonzalez v.
- Evidence: `counterargument_limitation` cue `However` at chunk `5488635` offsets `258-265`; context: However, where a breach of natural justice occurs, absent a clear indication that a rehearing would be no more than an exercise of form over substance, the Court should err on the side of upholding procedural fairness.
- Evidence: `disposition` cue `granted` at chunk `5488636` offsets `53-60`; context: [17] For these reasons, this judicial review will be granted, the original Board decision quashed and the matter referred back to a differently constituted panel of the Board for a new determination.

#### 31963:1:subtheme:5 · paragraphs 19-19

- Raw key terms: `certification, question`
- Display key terms: `certification, question`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: certification, question Evidence spans paragraphs 19-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5488638` offsets `17-25`; context: [19] There is no question for certification.

#### Section text

Clark-Erskine v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2007-04-12
Neutral citation
2007 FC 385
File numbers
IMM-5303-06
Decision Content
Date: 20070412
Docket: IMM-5303-06
Citation: 2007 FC 385
Ottawa, Ontario, April 12, 2007
PRESENT: The Honourable Mr. Justice Phelan
BETWEEN:
JEREMY DANIEL CLARK-ERSKINE
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] Mr. Clark-Erskine, the Applicant, is a citizen of the United States who escaped prison in the United States and made a refugee claim six weeks later after he was arrested in Canada for possession of false documents, false passports and stolen property. His refugee claim was rejected by the Immigration and Refugee Board (Board), a critical aspect of the decision is the finding of state protection and the absence of “cruel and unusual treatment and punishment” at the hands of American officials – principally Indiana state corrections officers.
I. BACKGROUND

[2] The Applicant has an extensive criminal record in both the United States and Canada. The crimes are in the nature of fraud and deception. He had been in Indiana State Prison where he claimed he was abused, beaten and denied his psychiatric medicines. The Applicant suffers from epilepsy and bi-polar disorder.

[3] The Board found that the Applicant’s various crimes, including his escape from prison, were not of sufficient gravity to fall within Article 1(F)(b) and therefore not sufficient to exclude his application.

[4] As to prison conditions in the United States, the Board found that U.S. prison conditions can be unacceptably harsh and that mistreatment of prisoners is unfortunately too common. Despite this finding the Board found that adequate state protection was available to him.

[5] The Board went on to find that, in respect of the s. 97 claim, the mistreatment that the Applicant suffered was partly at the hands of other inmates and partly “institutional”. Since the only institution at issue was the Indiana state prison, the reference suggests state involvement in his mistreatment.

[6] The Board then concluded that there was adequate state protection to address abuses by state officials including an ombudsman, his own counsel (generally a public defender) and human rights groups.

[7] A recurring theme of the Applicant’s oral argument is that prison conditions for himself and others with physical and psychiatric conditions were so egregious as to constitute cruel and unusual punishment. As to the Applicant’s personalized claim of torture and cruel and unusual punishment, the Board only concludes that incarceration as punishment for criminal offences is not cruel or unusual.
II. ANALYSIS

[8] The Applicant raises a number of issues including whether he was singled out for persecution, errors of law in considering whether torture or cruel and unusual punishment had been inflicted, and error in concluding state protection was available. Since this matter can be disposed of on the issue of procedural fairness and the matter will be reheard, no comment will be made on these other issues.

[9] On the day of the Applicant’s hearing, he had intended to call at least one witness from the Schizophrenic Society of Alberta. Since the Applicant did not believe that his witness had arrived in time for the hearing, he advised the Board at the immediately preceding pre-hearing conference that he had no witnesses.

[10] When the Board’s hearing opened to the public, the Applicant’s witness was in attendance. The Board refused to hear the witness because the Applicant had indicated at the hearing that he would not be calling a witness. The Board did, at the conclusion of the hearing, allow the witness to speak briefly but indicated that his comments would not be considered by the Board in rendering its decision.

[11] With due respect to the Board, this decision is an obvious denial of natural justice and fairness. The reasons for not calling a witness were explained, the arrival of the witness was unexpected and it was unfair to deny this evidence because the Applicant was mistaken about whether his witness was available.

[12] There was no issue of prejudice advanced by the Respondent and it is impossible to discern any other legitimate reason for refusing to hear the testimony. It was an unreasonable exercise of discretion especially coupled with allowing the witness to speak but refusing, in advance of hearing what was said, to consider the witness’ comments.

[13] The Respondent acknowledges that a breach of natural justice occurred but contends that the evidence would have made no difference because the witness was from the Schizophrenic Society of Alberta and the Applicant is not schizophrenic. The Respondent argues that the breach of natural justice would have no effect, the decision would be the same – the result is inevitable.

[14] The difficulty with the Respondent’s position is that the witness, in an affidavit filed in this judicial review, says that he intended to address the Board on the nature of bi-polar disorder, the efficacy of medications in treating this disorder and the state of the mentally ill held in jails in Canada and the United States. These are subjects potentially relevant to the Applicant’s claim of mistreatment in the Indiana state prison.

[15] It is not possible to conclude that the Applicant’s case is hopeless and that the breach of natural justice should be ignored because the result is inevitably the refusal of the application for protection (as occurred in cases such as Gonzalez v. Canada (Minister of Employment and Immigration) (F.C.A.), [1991] F.C.J. No. 408 (QL); Konadu v. Canada (Minister of Employment and Immigration) (F.C.A.), [1991] A.C.F. No. 330 (QL)). As noted in Mobil Oil Canada Ltd. v. Canada-Newfoundland Offshore Petroleum Board, [1994] 1 S.C.R. 202, where the result was inevitable, it is a rare case where breaches of natural justice can or, more importantly, should be ignored.

[16] In concluding that this case is not so weak as to be hopeless, the Court is not suggesting that the case has merit (even if that were within the Court’s jurisdiction to say) nor does it suggest that the Board’s other conclusions are necessarily flawed. However, where a breach of natural justice occurs, absent a clear indication that a rehearing would be no more than an exercise of form over substance, the Court should err on the side of upholding procedural fairness.
III. CONCLUSION

[17] For these reasons, this judicial review will be granted, the original Board decision quashed and the matter referred back to a differently constituted panel of the Board for a new determination.

[18] The Applicant was self-represented here and did a commendable job on his own behalf. It is acknowledged that the Applicant suffers from a bi-polar disorder, a common feature of which is anti-social or inappropriate behaviour. The Court does not have the power to order that counsel be appointed for the Applicant, but the Court trusts that Alberta legal aid officials would be open to considering a new application for the appointment of counsel for this Applicant.

[19] There is no question for certification.


## 31963:2 · paragraphs 20-21

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f52b3725ec4b1d9230a138be230fa91e858473f461f600730abdf6d69b6e92f3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 31963:2:subtheme:1 · paragraphs 20-21

- Raw key terms: `alberta, application, april, back, board, cause, citizenship, clark-erskine`
- Display key terms: `alberta, april, back, clark-erskine`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: alberta, april, back, clark-erskine No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
IT IS ORDERED THAT this application for judicial review will be granted, the original Board decision quashed and the matter referred back to a differently constituted panel of the Board for a new determination.
“Michael L. Phelan”
Judge
FEDERAL COURT
NAMES OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-5303-06

STYLE OF CAUSE: JEREMY DANIEL CLARK-ERSKINE
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Edmonton, Alberta
DATE OF HEARING: April 10, 2007
REASONS FOR 

## 31963:3 · paragraphs 22-22

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f3f743eb3473f81c91a48f97a1e55c8e213430ff9abca5c7b680805aef54737c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 31963:3:subtheme:1 · paragraphs 22-22

- Raw key terms: `alberta, appearances, applicant, april, attorney, audain, camille, canada`
- Display key terms: `alberta, april, audain, camille`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: alberta, april, audain, camille No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 22-22. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: Phelan J.
DATED: April 12, 2007
APPEARANCES:
Mr. Jeremy Daniel Clark-Erskine
FOR THE APPLICANT
Ms. Camille Audain
FOR THE RESPONDENT
SOLICITORS OF RECORD:
SELF-REPRESENTED
FOR THE APPLICANT
MR. JOHN H. SIMS, Q.C.
Deputy Attorney General of Canada
Edmonton, Alberta
FOR THE RESPONDENT
