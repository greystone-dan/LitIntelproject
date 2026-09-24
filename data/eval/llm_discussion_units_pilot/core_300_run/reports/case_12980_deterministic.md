# Discussion Units: case 12980

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **27**
- Continuity pairs: **26**
- Discussion Units: **1**
- Paragraph source hashes: **27**
- Sub-themes: **11**

## 12980:1 · paragraphs 0-26

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `418f5d9887adf60887933cd792c253bd91643bb463d74650f9fd81012bc74867`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12980:1:subtheme:1 · paragraphs 0-0

- Raw key terms: `appeal, applicant, applicants, application, aside, background, berger, board`
- Display key terms: `aside, background, berger`
- Argument roles: `governing_rule`
- Explanation: Observed roles: governing_rule Display terms: aside, background, berger Rule/authority context: Nature of the Application [1] This application for judicial review, brought pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] seeks to set aside the June 8, 2015 decision of Evidence spans paragraphs 0-0. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4642786` offsets `591-602`; context: Nature of the Application [1] This application for judicial review, brought pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] seeks to set aside the June 8, 2015 decision of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board of Canada [IRB] , dismissing the applicants’ appeal from the Refugee Protection Division [RPD] of the IRB.

#### 12980:1:subtheme:2 · paragraphs 1-2

- Raw key terms: `allegations, applicants, counsel, incompetence, addition, advancing, against, arguing`
- Display key terms: `allegations, incompetence, addition, advancing, against, arguing`
- Argument roles: `disposition, party_position`
- Explanation: Observed roles: disposition, party_position Display terms: allegations, incompetence, addition, advancing, against, arguing Position/evidence statements: [2] In addition to arguing that the RAD committed a reviewable error on the merits, the applicants submit that the incompetence of their counsel before the RAD prejudiced their position and caused a breach of natural jus Operative outcome context: [3] The RAD counsel was granted intervener status and permitted to file written representations as well as provide oral submissions responding only to the allegations of solicitor negligence/incompetence. Evidence spans paragraphs 1-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submit` at chunk `4642787` offsets `99-105`; context: [2] In addition to arguing that the RAD committed a reviewable error on the merits, the applicants submit that the incompetence of their counsel before the RAD prejudiced their position and caused a breach of natural justice.
- Evidence: `disposition` cue `granted` at chunk `4642788` offsets `24-31`; context: [3] The RAD counsel was granted intervener status and permitted to file written representations as well as provide oral submissions responding only to the allegations of solicitor negligence/incompetence.

#### 12980:1:subtheme:3 · paragraphs 3-4

- Raw key terms: `applicants, events, pakistan, adequate, ahmadi, alleged, alternatives, angered`
- Display key terms: `events, pakistan, adequate, ahmadi, alleged, alternatives, angered`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: events, pakistan, adequate, ahmadi, alleged, alternatives, angered Evidence spans paragraphs 3-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4642789` offsets `18-23`; context: [5] The events at issue began when the applicants returned from the United States to Pakistan in June, 2014.
- Evidence: `evidence_fact` cue `evidence` at chunk `4642790` offsets `339-347`; context: RPD Decision [7] The RPD rejected the applicants’ claim after finding: (1) the applicants’ evidence relating to the events alleged was neither credible nor reliable; (2) adequate state protection existed in Pakistan; (3) no nexus to a Convention ground existed and the applicants faced a generalized rather than personalized risk; and (4) viable Internal Flight Alternatives [IFA] existed in Islamabad and Karachi.

#### 12980:1:subtheme:4 · paragraphs 5-7

- Raw key terms: `applicants, protection, decision, evidence, notes, risk, state, agents`
- Display key terms: `protection, notes, risk, state, agents`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: protection, notes, risk, state, agents Position/evidence statements: [9] On the question of IFA, the RPD rejected the PA’s claim that the Taliban were targeting him. Rule/authority context: RAD Decision under Review [10] The RAD confirmed the RPD’s decision that the applicants are neither Convention refugees nor persons in need of protection based on the IFA finding only. Evidence spans paragraphs 5-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4642791` offsets `331-337`; context: The RPD also identifies a number of instances where evidence was not included in the PA’s narrative that was directly relevant to issues such as state protection and personal risk, information that one would reasonably expect to be contained in the narrative in light of the PA’s burden.
- Evidence: `evidence_fact` cue `evidence` at chunk `4642791` offsets `35-43`; context: [8] In determining the applicants’ evidence was not credible or reliable the RPD notes that there was no evidence linking the PA’s reports of attempted assault with his earlier expression on religion.
- Evidence: `issue` cue `question` at chunk `4642792` offsets `11-19`; context: [9] On the question of IFA, the RPD rejected the PA’s claim that the Taliban were targeting him.
- Evidence: `party_position` cue `claim` at chunk `4642792` offsets `54-59`; context: [9] On the question of IFA, the RPD rejected the PA’s claim that the Taliban were targeting him.
- Evidence: `evidence_fact` cue `found that` at chunk `4642792` offsets `121-131`; context: After doing so, the RPD found that any potential agents of harm were local and there was no persuasive evidence that potential agents of harm had influence anywhere in Pakistan.
- Evidence: `governing_rule` cue `under` at chunk `4642792` offsets `451-456`; context: RAD Decision under Review [10] The RAD confirmed the RPD’s decision that the applicants are neither Convention refugees nor persons in need of protection based on the IFA finding only.
- Evidence: `counterargument_limitation` cue `but` at chunk `4642793` offsets `466-469`; context: The RAD notes that the applicants’ Memorandum challenged the RPD’s credibility findings as well as the RPD’s conclusions on state protection, nexus and generalized risk but did not make any submissions on IFA.

#### 12980:1:subtheme:5 · paragraphs 8-10

- Raw key terms: `applicants, argue, counsel, credibility, decision, determination, finding, findings`
- Display key terms: `argue, credibility, determination, finding, findings`
- Argument roles: `issue, party_position, reasoning_application`
- Explanation: Observed roles: issue, party_position, reasoning_application Display terms: argue, credibility, determination, finding, findings Position/evidence statements: Positions of the Parties (1) Applicants [13] The applicants submit the RAD’s decision was: (1) unreasonable; or (2) is the result of a breach of natural justice arising from the incompetence of the intervener, counsel be | [14] The applicants argue that the RAD unreasonably found the RPD’s IFA determination stood on its own. Application context: [12] The RAD then concludes at paragraph 20 of its decision that, “It is clear that the IFA determination stands on its own – that is, it is not influenced by or dependent on other findings, including credibility. Evidence spans paragraphs 8-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4642794` offsets `274-280`; context: Issues and Analysis A.
- Evidence: `party_position` cue `submit` at chunk `4642794` offsets `357-363`; context: Positions of the Parties (1) Applicants [13] The applicants submit the RAD’s decision was: (1) unreasonable; or (2) is the result of a breach of natural justice arising from the incompetence of the intervener, counsel before the RAD.
- Evidence: `reasoning_application` cue `concludes` at chunk `4642794` offsets `18-27`; context: [12] The RAD then concludes at paragraph 20 of its decision that, “It is clear that the IFA determination stands on its own – that is, it is not influenced by or dependent on other findings, including credibility.
- Evidence: `party_position` cue `argue` at chunk `4642795` offsets `20-25`; context: [14] The applicants argue that the RAD unreasonably found the RPD’s IFA determination stood on its own.
- Evidence: `party_position` cue `argue` at chunk `4642796` offsets `39-44`; context: [15] In the alternative the applicants argue that the intervener was negligent or incompetent in failing to (1) request the applicants’ RPD file from RPD counsel and (2) raise an argument before the RAD on IFA.

#### 12980:1:subtheme:6 · paragraphs 11-12

- Raw key terms: `counsel, incompetence, issue, respondent, acws, address, addressed, adviser`
- Display key terms: `incompetence, acws, address, addressed, adviser`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: incompetence, acws, address, addressed, adviser Position/evidence statements: [17] On the issue of incompetent counsel before the RAD, the respondent argues that the jurisprudence demonstrates that clients will be held to the consequences of their choice of adviser (Cove v Canada (Minister of Citi Rule/authority context: [17] On the issue of incompetent counsel before the RAD, the respondent argues that the jurisprudence demonstrates that clients will be held to the consequences of their choice of adviser (Cove v Canada (Minister of Citi Application context: I have therefore not addressed the intervener’s submissions as they relate to the merits of the application. Evidence spans paragraphs 11-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4642797` offsets `12-17`; context: [17] On the issue of incompetent counsel before the RAD, the respondent argues that the jurisprudence demonstrates that clients will be held to the consequences of their choice of adviser (Cove v Canada (Minister of Citizenship and Immigration), 2001 FCT 266 at para 6, 104 ACWS (3d) 761 (TD) [Cove]).
- Evidence: `party_position` cue `argues` at chunk `4642797` offsets `72-78`; context: [17] On the issue of incompetent counsel before the RAD, the respondent argues that the jurisprudence demonstrates that clients will be held to the consequences of their choice of adviser (Cove v Canada (Minister of Citizenship and Immigration), 2001 FCT 266 at para 6, 104 ACWS (3d) 761 (TD) [Cove]).
- Evidence: `evidence_fact` cue `evidence` at chunk `4642797` offsets `643-651`; context: Counsel incompetence will only constitute a breach of natural justice in extraordinary circumstances and an applicant has the burden of establishing (1) that their counsel’s act or omission constituted incompetence without the benefit and wisdom of hindsight, and such incompetence must be sufficiently specific and clearly supported by the evidence and (2) the result would have been different but for the incompetence (Galyas v Canada (Minister of Citizenship and Immigration), 2013 FC 250 at paras 83-84, 429 FTR 1 [Galyas]; Memari v Canada (Minister of Citizenship and Immigration), 2010 FC 1196 at paras 33, 36, 378 FTR 206 [Memari]; R v GDB, [2000] 1 SCR 520 at paras 27-29).
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4642797` offsets `88-101`; context: [17] On the issue of incompetent counsel before the RAD, the respondent argues that the jurisprudence demonstrates that clients will be held to the consequences of their choice of adviser (Cove v Canada (Minister of Citizenship and Immigration), 2001 FCT 266 at para 6, 104 ACWS (3d) 761 (TD) [Cove]).
- Evidence: `counterargument_limitation` cue `but` at chunk `4642797` offsets `697-700`; context: Counsel incompetence will only constitute a breach of natural justice in extraordinary circumstances and an applicant has the burden of establishing (1) that their counsel’s act or omission constituted incompetence without the benefit and wisdom of hindsight, and such incompetence must be sufficiently specific and clearly supported by the evidence and (2) the result would have been different but for the incompetence (Galyas v Canada (Minister of Citizenship and Immigration), 2013 FC 250 at paras 83-84, 429 FTR 1 [Galyas]; Memari v Canada (Minister of Citizenship and Immigration), 2010 FC 1196 at paras 33, 36, 378 FTR 206 [Memari]; R v GDB, [2000] 1 SCR 520 at paras 27-29).
- Evidence: `issue` cue `issue` at chunk `4642798` offsets `34-39`; context: [18] After citing the law on this issue, the respondent did not take a position on whether the counsel incompetence occurred in this case.
- Evidence: `reasoning_application` cue `therefore` at chunk `4642798` offsets `358-367`; context: I have therefore not addressed the intervener’s submissions as they relate to the merits of the application.

#### 12980:1:subtheme:7 · paragraphs 13-15

- Raw key terms: `credibility, decision, findings, analysis, applicants, challenged, correctness, determination`
- Display key terms: `credibility, findings, analysis, challenged, correctness, determination`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: credibility, findings, analysis, challenged, correctness, determination Rule/authority context: Issues [21] The application raises the following issues: (1) What is the applicable standard of review? | [23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and  Application context: [22] The parties submit, and I agree that this Court applies a reasonableness standard of review when reviewing the RAD’s conclusions on its own decision-making process and the RAD’s review of the RPD’s decision (Hurugli | [23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and  Evidence spans paragraphs 13-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4642799` offsets `659-665`; context: Issues [21] The application raises the following issues:
(1) What is the applicable standard of review?
- Evidence: `evidence_fact` cue `evidence` at chunk `4642799` offsets `589-597`; context: He did not request the file from RPD counsel only after determining that the applicants provided him all the information required for the appeal, he assigned carriage of the file to an experienced associate and the decision of the associate not to pursue an IFA argument was a strategic decision based on the evidence that was placed before the RPD and the decision rendered.
- Evidence: `governing_rule` cue `standard of review` at chunk `4642799` offsets `743-761`; context: Issues [21] The application raises the following issues:
(1) What is the applicable standard of review?
- Evidence: `reasoning_application` cue `applies` at chunk `4642799` offsets `1187-1194`; context: [22] The parties submit, and I agree that this Court applies a reasonableness standard of review when reviewing the RAD’s conclusions on its own decision-making process and the RAD’s review of the RPD’s decision (Huruglica v Canada (Minister of Citizenship and Immigration), 2016 FCA 93 at paras 32, 35 [Huruglica]; Ngandu v Canada (Minister of Citizenship and Immigration), 2015 FC 423 at para 12, 34 Imm LR (4th) 68).
- Evidence: `issue` cue `issue` at chunk `4642800` offsets `178-183`; context: [23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and must take a case-by-case approach to the level of deference it owes to the relative weight of testimony and their credibility or lack thereof (Huruglica at paras 37, 69-71, 103).
- Evidence: `evidence_fact` cue `evidence` at chunk `4642800` offsets `207-215`; context: [23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and must take a case-by-case approach to the level of deference it owes to the relative weight of testimony and their credibility or lack thereof (Huruglica at paras 37, 69-71, 103).
- Evidence: `governing_rule` cue `standard of review` at chunk `4642800` offsets `40-58`; context: [23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and must take a case-by-case approach to the level of deference it owes to the relative weight of testimony and their credibility or lack thereof (Huruglica at paras 37, 69-71, 103).
- Evidence: `reasoning_application` cue `apply` at chunk `4642800` offsets `18-23`; context: [23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and must take a case-by-case approach to the level of deference it owes to the relative weight of testimony and their credibility or lack thereof (Huruglica at paras 37, 69-71, 103).
- Evidence: `governing_rule` cue `under` at chunk `4642801` offsets `109-114`; context: [25] There was a link in the RPD’s decision between the credibility findings flowing from the RPD’s analysis under sections 96 and 97, and the IFA determination.

#### 12980:1:subtheme:8 · paragraphs 16-17

- Raw key terms: `provided, taliban, address, advancing, agents, agitating, ahmadi, analysis`
- Display key terms: `provided, taliban, address, advancing, agents, agitating, ahmadi, analysis`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: provided, taliban, address, advancing, agents, agitating, ahmadi, analysis Application context: However, this is clearly incorrect: At line 53 of the Appellant’s BOC, he says, “Later I began receiving threatening phone calls from the Taliban that my days were over because I had changed my faith and because I was ag Evidence spans paragraphs 16-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4642802` offsets `212-217`; context: The applicants contested the RPD’s credibility findings and findings of fact as they related to the issue of the Taliban as agents of persecution, advancing the following submissions to the RAD in their Memorandum:
10.
- Evidence: `evidence_fact` cue `testimony` at chunk `4642802` offsets `774-783`; context: This written testimony is entirely consistent with both the timeline and the details provided at the hearing.
- Evidence: `reasoning_application` cue `because` at chunk `4642802` offsets `679-686`; context: However, this is clearly incorrect: At line 53 of the Appellant’s BOC, he says, “Later I began receiving threatening phone calls from the Taliban that my days were over because I had changed my faith and because I was agitating for Ahmadi faith.
- Evidence: `counterargument_limitation` cue `However` at chunk `4642802` offsets `510-517`; context: However, this is clearly incorrect: At line 53 of the Appellant’s BOC, he says, “Later I began receiving threatening phone calls from the Taliban that my days were over because I had changed my faith and because I was agitating for Ahmadi faith.

#### 12980:1:subtheme:9 · paragraphs 18-22

- Raw key terms: `appeal, appellant, irpa, onus, subsection, court, dhillon, errors`
- Display key terms: `appellant, irpa, onus, subsection, dhillon, errors`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: appellant, irpa, onus, subsection, dhillon, errors Application context: ” That principle should equally apply to the appellant’s onus to identify the errors of the RPD on appeal as discussed in Dhillon at paras 18-20. Evidence spans paragraphs 18-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4642804` offsets `436-441`; context: These factual and credibility findings were directly relevant to the issue of the Taliban as an agent of persecution and the RAD was placed on notice by the applicants that the RPD had misconstrued the contents of the applicant’s BOC as it related to this issue.
- Evidence: `reasoning_application` cue `apply` at chunk `4642808` offsets `395-400`; context: ” That principle should equally apply to the appellant’s onus to identify the errors of the RPD on appeal as discussed in Dhillon at paras 18-20.

#### 12980:1:subtheme:10 · paragraphs 23-24

- Raw key terms: `decision, erred, held, huruglica, para, principle, address, adviser`
- Display key terms: `erred, huruglica, para, principle, address, adviser`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: erred, huruglica, para, principle, address, adviser Position/evidence statements: [33] Indeed, the Federal Court of Appeal in defining the RAD’s role in Huruglica held at para 103 “Thus, after carefully considering the RPD decision, the RAD carries out its own analysis of the record to determine wheth Evidence spans paragraphs 23-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4642809` offsets `215-222`; context: [33] Indeed, the Federal Court of Appeal in defining the RAD’s role in Huruglica held at para 103 “Thus, after carefully considering the RPD decision, the RAD carries out its own analysis of the record to determine whether, as submitted by the appellant, the RPD erred.
- Evidence: `party_position` cue `submitted` at chunk `4642809` offsets `227-236`; context: [33] Indeed, the Federal Court of Appeal in defining the RAD’s role in Huruglica held at para 103 “Thus, after carefully considering the RPD decision, the RAD carries out its own analysis of the record to determine whether, as submitted by the appellant, the RPD erred.
- Evidence: `evidence_fact` cue `record` at chunk `4642809` offsets `195-201`; context: [33] Indeed, the Federal Court of Appeal in defining the RAD’s role in Huruglica held at para 103 “Thus, after carefully considering the RPD decision, the RAD carries out its own analysis of the record to determine whether, as submitted by the appellant, the RPD erred.
- Evidence: `issue` cue `issue` at chunk `4642810` offsets `776-781`; context: [35] In light of my conclusion that the RAD has committed a reviewable error I will not address the issue of counsel competency except to highlight and endorse the submission of the respondent on this question.
- Evidence: `counterargument_limitation` cue `However` at chunk `4642810` offsets `313-320`; context: However, my decision on these facts should not detract from the following principle that emerges from the case-law: appellants before the RAD that fail to specify where and how the RPD erred do so at their peril.

#### 12980:1:subtheme:11 · paragraphs 25-26

- Raw key terms: `barrister, berger, cause, general, gleeson, hearing, intervener, judgment`
- Display key terms: `barrister, berger, gleeson, hearing, intervener`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: barrister, berger, gleeson, hearing, intervener Operative outcome context: The application is granted; 3. Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4642811` offsets `516-524`; context: The making of further IFA submissions on redetermination is a question that falls within the discretion of the RAD to address and will be left there.
- Evidence: `disposition` cue `granted` at chunk `4642811` offsets `824-831`; context: The application is granted;
3.

#### Section text

Ghauri v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2016-05-16
Neutral citation
2016 FC 548
File numbers
IMM-3426-15
Decision Content
Date: 20160516
Docket: IMM-3426-15
Citation: 2016 FC 548
Ottawa, Ontario, May 16, 2016
PRESENT: The Honourable Mr. Justice Gleeson
BETWEEN:
MUHAMMAD HABIB GHAURI,
RIFFAT HABIB, AND
MUHAMMAD SHERDIL GHOURI
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
MAX BERGER
Intervener
JUDGMENT AND REASONS
I. Background A. Nature of the Application [1] This application for judicial review, brought pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] seeks to set aside the June 8, 2015 decision of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board of Canada [IRB] , dismissing the applicants’ appeal from the Refugee Protection Division [RPD] of the IRB. The RPD rejected the applicants’ refugee claim after finding they were neither Convention refugees nor persons in need in protection pursuant to sections 96 and 97 of the IRPA respectively.

[2] In addition to arguing that the RAD committed a reviewable error on the merits, the applicants submit that the incompetence of their counsel before the RAD prejudiced their position and caused a breach of natural justice. In advancing this position the applicants have complied with Chief Justice Crampton’s March 7, 2014 Procedural Protocol regarding Allegations Against Counsel or Other Authorized Representative in Citizenship, Immigration and Protected Person Cases before the Federal Court.

[3] The RAD counsel was granted intervener status and permitted to file written representations as well as provide oral submissions responding only to the allegations of solicitor negligence/incompetence.
B. Facts [4] The applicants are a married couple and their three children. The husband, wife and one of their children are citizens of Pakistan. The other two children were born in the United States while the applicants were living there, and are nationals of the United States.

[5] The events at issue began when the applicants returned from the United States to Pakistan in June, 2014. In discussions with friends in July, 2014, the principal applicant, Mr Ghauri [the PA], a businessman, apparently angered some individuals as a result of supportive and positive comments he made regarding members of the Ahmadi faith. As a result of these comments the PA began to feel ostracized and his business dropped off. Attempted assaults occurred as well as threatening phone calls.

[6] The applicants fled to Canada on valid visas in September, 2014 and requested protection several weeks later. Subsequent to arriving in Canada, the PA learnt that his cousins have said the applicants are infidels and deserve to be punished.
C. RPD Decision [7] The RPD rejected the applicants’ claim after finding: (1) the applicants’ evidence relating to the events alleged was neither credible nor reliable; (2) adequate state protection existed in Pakistan; (3) no nexus to a Convention ground existed and the applicants faced a generalized rather than personalized risk; and (4) viable Internal Flight Alternatives [IFA] existed in Islamabad and Karachi.

[8] In determining the applicants’ evidence was not credible or reliable the RPD notes that there was no evidence linking the PA’s reports of attempted assault with his earlier expression on religion. The RPD also identifies a number of instances where evidence was not included in the PA’s narrative that was directly relevant to issues such as state protection and personal risk, information that one would reasonably expect to be contained in the narrative in light of the PA’s burden.

[9] On the question of IFA, the RPD rejected the PA’s claim that the Taliban were targeting him. After doing so, the RPD found that any potential agents of harm were local and there was no persuasive evidence that potential agents of harm had influence anywhere in Pakistan. The RPD rejected the applicants’ objections to the proposed IFAs of Islamabad and Karachi as the objections failed to satisfy the second prong of the IFA test.
D. RAD Decision under Review [10] The RAD confirmed the RPD’s decision that the applicants are neither Convention refugees nor persons in need of protection based on the IFA finding only.

[11] The RAD notes that the Refugee Appeal Division Rules, SOR/2012-257 [RAD Rules] require that appellants provide in their Memorandum full and detailed submissions regarding the errors that are the grounds of the appeal and the location of those errors in the RPD’s decision (Sub-rule 3(3)(g)). The RAD notes that the applicants’ Memorandum challenged the RPD’s credibility findings as well as the RPD’s conclusions on state protection, nexus and generalized risk but did not make any submissions on IFA.

[12] The RAD then concludes at paragraph 20 of its decision that, “It is clear that the IFA determination stands on its own – that is, it is not influenced by or dependent on other findings, including credibility.” The RAD then concurred with the RPD’s findings on IFA.
II. Issues and Analysis A. Positions of the Parties (1) Applicants [13] The applicants submit the RAD’s decision was: (1) unreasonable; or (2) is the result of a breach of natural justice arising from the incompetence of the intervener, counsel before the RAD.

[14] The applicants argue that the RAD unreasonably found the RPD’s IFA determination stood on its own. The applicants submit that the RPD’s credibility findings were connected to the IFA finding in that had the RPD believed that the applicants had been targeted by the Taliban, the IFA decision would have been very different. An error in the credibility findings would affect the reasonableness of the IFA findings and as such the RAD was obligated to consider the arguments placed before it, including the submission that the RPD erred in its determination that the Taliban did not target the applicants. The failure to do so, the applicants argue, renders the decision unreasonable.

[15] In the alternative the applicants argue that the intervener was negligent or incompetent in failing to (1) request the applicants’ RPD file from RPD counsel and (2) raise an argument before the RAD on IFA.
(2) Respondent [16] The respondent argues that the RAD’s finding that the applicants had viable IFAs was reasonable. The RAD reasonably limited its assessment to the material before the RPD and made the indisputable finding that the applicants did not contest the RPD’s IFA finding which was determinative of the applicants’ claim.

[17] On the issue of incompetent counsel before the RAD, the respondent argues that the jurisprudence demonstrates that clients will be held to the consequences of their choice of adviser (Cove v Canada (Minister of Citizenship and Immigration), 2001 FCT 266 at para 6, 104 ACWS (3d) 761 (TD) [Cove]). Counsel incompetence will only constitute a breach of natural justice in extraordinary circumstances and an applicant has the burden of establishing (1) that their counsel’s act or omission constituted incompetence without the benefit and wisdom of hindsight, and such incompetence must be sufficiently specific and clearly supported by the evidence and (2) the result would have been different but for the incompetence (Galyas v Canada (Minister of Citizenship and Immigration), 2013 FC 250 at paras 83-84, 429 FTR 1 [Galyas]; Memari v Canada (Minister of Citizenship and Immigration), 2010 FC 1196 at paras 33, 36, 378 FTR 206 [Memari]; R v GDB, [2000] 1 SCR 520 at paras 27-29).

[18] After citing the law on this issue, the respondent did not take a position on whether the counsel incompetence occurred in this case.
(3) Intervener [19] The intervener’s submissions go beyond the allegations of negligence/incompetence and address the merits of the application contrary to the February 12, 2016 Order granting intervener status. I have therefore not addressed the intervener’s submissions as they relate to the merits of the application.

[20] The intervener submits that the RAD’s negative decision is not the result of counsel incompetence. The intervener argues that this matter was handled in accordance with his long standing practice in the immigration field and he did so in a competent and professional manner. He did not request the file from RPD counsel only after determining that the applicants provided him all the information required for the appeal, he assigned carriage of the file to an experienced associate and the decision of the associate not to pursue an IFA argument was a strategic decision based on the evidence that was placed before the RPD and the decision rendered.
B. Issues [21] The application raises the following issues:
(1) What is the applicable standard of review?
(2) Did the RAD err in finding that the RPD’s finding on IFA was independent of all other findings the applicants challenged before the RAD, including credibility?
(3) If the RAD decision is reasonable, was the intervener incompetent or negligent before the RAD and did this lead to a breach of natural justice?
C. Analysis (1) What is the applicable standard of review? [22] The parties submit, and I agree that this Court applies a reasonableness standard of review when reviewing the RAD’s conclusions on its own decision-making process and the RAD’s review of the RPD’s decision (Huruglica v Canada (Minister of Citizenship and Immigration), 2016 FCA 93 at paras 32, 35 [Huruglica]; Ngandu v Canada (Minister of Citizenship and Immigration), 2015 FC 423 at para 12, 34 Imm LR (4th) 68). The correctness standard of review applies to the allegations of incompetent or negligent representation as issues of procedural fairness are engaged (Galyas at para 27).

[23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and must take a case-by-case approach to the level of deference it owes to the relative weight of testimony and their credibility or lack thereof (Huruglica at paras 37, 69-71, 103).
(2) Did the RAD err in finding that the RPD’s finding on IFA was independent of all other findings the applicants challenged before the RAD, including credibility? [24] I am of the opinion that the RAD committed a reviewable error in concluding that the “IFA determination stands on its own – that is, it is not influenced by or dependent on other findings, including credibility” (RAD decision at para 20).

[25] There was a link in the RPD’s decision between the credibility findings flowing from the RPD’s analysis under sections 96 and 97, and the IFA determination.

[26] This linkage, in my view, required that the RAD consider and address the RPD’s credibility determinations. The applicants contested the RPD’s credibility findings and findings of fact as they related to the issue of the Taliban as agents of persecution, advancing the following submissions to the RAD in their Memorandum:
10. The RPD at paragraph 23 of the decision impugns the Applicant’s credibility further by stating that the Appellant did not mention the calls from the Taliban in his BOC narrative. However, this is clearly incorrect: At line 53 of the Appellant’s BOC, he says, “Later I began receiving threatening phone calls from the Taliban that my days were over because I had changed my faith and because I was agitating for Ahmadi faith.”
11. This written testimony is entirely consistent with both the timeline and the details provided at the hearing. The Board Member clearly made a mistake in finding that the Appellant did not mention the threatening calls in the BOC, further cementing the Appellant’s argument that the credibility analysis is erroneous.

[27] The PA also provided a statutory declaration to the RAD reiterating his fear of the Taliban in Pakistan.

[28] The RPD’s finding that the Taliban were not the agents of persecution was in my opinion a condition precedent for the RPD’s determination that there would be a viable IFA as the fears and risks did not flow from the Taliban but rather were local in nature. The RAD failed to address the RPD’s factual and credibility determinations underpinning the IFA finding. These factual and credibility findings were directly relevant to the issue of the Taliban as an agent of persecution and the RAD was placed on notice by the applicants that the RPD had misconstrued the contents of the applicant’s BOC as it related to this issue. In the circumstances I am not satisfied that the outcome would have been the same had the RAD considered the credibility findings relevant to the IFA analysis undertaken by the RPD.

[29] I will allow the application for that reason.

[30] However, I wish to make the following comments on the RAD’s role and obligations and an appellant’s onus before the RAD in light of the recent decisions of the Federal Court of Appeal on the RAD. In my view Huruglica at para 103 and Singh v Canada (Minister of Citizenship and Immigration), 2016 FCA 96 at paras 54-55 [Singh] underscore the views expressed by Justice René LeBlanc in Dhillon v Canada (Minister of Citizenship and Immigration), 2015 FC 321 at paras 18-20 [Dhillon], a case which the RAD relied on when interpreting subsection 110(1) of the IRPA and RAD Rule 3(3)(g) in this case.

[31] Subsection 110(1) of the IRPA provides that a person or the Minister may appeal to the RAD against a decision of the RPD, in accordance with the rules of the Board. RAD Rule 3(3)(g) places the onus on the appellant to identify in their Memorandum the errors that are the grounds of the appeal and the location of the errors in the RPD’s decision or in the audio or other electronic recording of the RPD hearing.

[32] The Federal Court of Appeal in Singh, in the context of discussing subsection 110(4) of the IRPA, held at para 55 that “These rules must be respected, and it must be presumed that the explicit choices that were made match the objective pursued. It is not the responsibility of the courts to rewrite such provisions when they are intelligible and unequivocal.” That principle should equally apply to the appellant’s onus to identify the errors of the RPD on appeal as discussed in Dhillon at paras 18-20.

[33] Indeed, the Federal Court of Appeal in defining the RAD’s role in Huruglica held at para 103 “Thus, after carefully considering the RPD decision, the RAD carries out its own analysis of the record to determine whether, as submitted by the appellant, the RPD erred.” This further reinforces the principle that it is the appellant’s responsibility, not the RAD’s, to “establish that the RPD erred in a way that justifies the intervention of the RAD. It is not the RAD’s function to supplement the weaknesses of an appeal before it” (Dhillon at para 20).

[34] Here the applicants alleged to the RAD that the RPD erred in finding the Taliban were not the agents of persecution, and the RAD could not escape its obligations set out in Huruglica at para 103 by relying on the RPD’s IFA finding without more. This was a reviewable error in the circumstances of this case. However, my decision on these facts should not detract from the following principle that emerges from the case-law: appellants before the RAD that fail to specify where and how the RPD erred do so at their peril.
(3) If the RAD’s decision is reasonable, was the intervener incompetent or negligent before the RAD and did this lead to a breach of natural justice? [35] In light of my conclusion that the RAD has committed a reviewable error I will not address the issue of counsel competency except to highlight and endorse the submission of the respondent on this question. Clients will normally be held to the consequences of their choice of adviser (Cove at para 6) and, except in extraordinary circumstances where competency of counsel gives rise to a breach of procedural fairness that compromised the reliability of the result, it is not for the Courts to address issues of competency (Memari at paras 33, 36).
III. Conclusion [36] The matter is returned to the RAD for redetermination, a redetermination that is to consider the RPD’s factual and credibility findings that impact upon or are relevant to the IFA assessment.

[37] The applicants’ counsel requested at the hearing of this matter that should the decision be returned for redetermination that the applicants be permitted to make further submissions on IFA. Sub-rule 29(2) of the Refugee Appeal Division Rules, SOR/2012-257 speaks to a circumstance where a person wishes to advance written submissions not previously provided, requiring that person make an application to the Division in accordance with RAD Rule 37. The making of further IFA submissions on redetermination is a question that falls within the discretion of the RAD to address and will be left there. The parties have not identified a question of general importance.
JUDGMENT
THIS COURT’S JUDGMENT is that:
1. Mr. Max Berger, Barrister and Solicitor is added to the style of cause as an intervener;
2. The application is granted;
3. The matter is returned for redetermination by a differently constituted RAD panel that is to consider the RPD’s factual and credibility findings that impact upon or are relevant to the IFA assessment; and
4. No question is certified.
"Patrick Gleeson"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
Docket:
IMM-3426-15
STYLE OF CAUSE:
MUHAMMAD HABIB GHAURI, RIFFAT HABIB, AND MUHAMMAD SHERDIL GHOURI v THE MINISTER OF CITIZENSHIP AND IMMIGRATION AND MAX BERGER
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
May 2, 2016
JUDGMENT AND REASONS:
GLEESON J.
DATED:
May 16, 2016
APPEARANCES:
Karina Thompson
For The Applicant
Sybil Thompson
For The Respondent
Max Berger
For The Intervener
SOLICITORS OF RECORD:
Karina Thompson
Barrister and Solicitor
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
Max Berger
Barrister and Solicitor
Toronto, Ontario
For The Intervener
