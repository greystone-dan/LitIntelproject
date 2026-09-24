# Discussion Units: case 10323

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **30**
- Continuity pairs: **29**
- Discussion Units: **4**
- Paragraph source hashes: **30**
- Sub-themes: **14**

## 10323:1 · paragraphs 0-7

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `245dde5b5ba07b6fc5fd96ac8f81149e41fa169691a859b95987d1fb48a40a4f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10323:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `applicants, because, china, daughter, canada, children, decision, notice`
- Display key terms: `because, china, daughter, children, notice`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: because, china, daughter, children, notice Position/evidence statements: They claim that Ms. | The Applicants submitted to the RAD that the medical note was relevant because it showed that Ms. Rule/authority context: The Applicants have now applied under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] for judicial review of the RAD’s decision. Application context: They entered Canada on October 3, 2015 and sought refugee protection, claiming that they would be persecuted in China because Ms. | They wanted to have additional children but were prevented from doing so because of China’s one-child policy. Operative outcome context: The Applicants appealed the RPD’s decision to the Refugee Appeal Division [RAD] of the IRB; but in a decision dated August 10, 2016, the RAD dismissed the appeal and confirmed the RPD’s decision that the Applicants were  | The RPD also noted that the one-child policy law in China had changed to allow couples to have two children, and that because the adult Applicants would be allowed to have a second child it was reasonable to expect that  Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4518901` offsets `786-791`; context: The Applicants have now applied under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] for judicial review of the RAD’s decision.
- Evidence: `reasoning_application` cue `because` at chunk `4518901` offsets `241-248`; context: They entered Canada on October 3, 2015 and sought refugee protection, claiming that they would be persecuted in China because Ms.
- Evidence: `counterargument_limitation` cue `however` at chunk `4518901` offsets `343-350`; context: Their claims were rejected, however, by the Refugee Protection Division [RPD] of the Immigration and Refugee Board [IRB] in a decision dated April 7, 2016.
- Evidence: `disposition` cue `dismissed` at chunk `4518901` offsets `612-621`; context: The Applicants appealed the RPD’s decision to the Refugee Appeal Division [RAD] of the IRB; but in a decision dated August 10, 2016, the RAD dismissed the appeal and confirmed the RPD’s decision that the Applicants were neither Convention refugees nor persons in need of protection.
- Evidence: `party_position` cue `claim` at chunk `4518902` offsets `204-209`; context: They claim that Ms.
- Evidence: `reasoning_application` cue `because` at chunk `4518902` offsets `162-169`; context: They wanted to have additional children but were prevented from doing so because of China’s one-child policy.
- Evidence: `evidence_fact` cue `determined that` at chunk `4518903` offsets `71-86`; context: It determined that the documents submitted by the Applicants were not genuine and that their allegations were not credible.
- Evidence: `reasoning_application` cue `because` at chunk `4518903` offsets `452-459`; context: In particular, the RPD found that since the US visa application had been submitted before the authorities allegedly attended at the Applicants’ home on July 30, 2015, this seriously undermined the adult Applicants’ allegations that they decided to leave China because they had received a second sterilization notice and a notice suspending their daughter from school.
- Evidence: `disposition` cue `allowed` at chunk `4518903` offsets `716-723`; context: The RPD also noted that the one-child policy law in China had changed to allow couples to have two children, and that because the adult Applicants would be allowed to have a second child it was reasonable to expect that they would not be required to be sterilized upon return to China.
- Evidence: `party_position` cue `submitted` at chunk `4518904` offsets `565-574`; context: The Applicants submitted to the RAD that the medical note was relevant because it showed that Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4518904` offsets `123-131`; context: [4] The Applicants appealed to the RAD on April 22, 2016, claiming that the RPD had erred in finding that: the Applicants’ evidence was not credible; the sterilization notices were fraudulent; the daughter’s suspension notice was fraudulent; and that the adult Applicants would not face a risk of forced sterilization due to China’s two-child policy.
- Evidence: `reasoning_application` cue `because` at chunk `4518904` offsets `621-628`; context: The Applicants submitted to the RAD that the medical note was relevant because it showed that Ms.

#### 10323:1:subtheme:2 · paragraphs 5-6

- Raw key terms: `applicants, because, evidence, medical, abortions, accepted, addition, addressing`
- Display key terms: `because, medical, abortions, accepted, addition, addressing`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: because, medical, abortions, accepted, addition, addressing Application context: ” The RAD accepted the medical note into evidence because it contained information that arose after the RPD decision and was relevant to the matter. | As to whether the RPD made an improper credibility finding because Ms. Operative outcome context: [5] The RAD dismissed the Applicants’ appeal in a decision dated August 10, 2016. Evidence spans paragraphs 5-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4518905` offsets `1294-1300`; context: Although the LifeNews article post-dated the RPD decision, it was not accepted into evidence by the RAD because it contained information that was available prior to the RPD decision and it contained “a great deal of conjecture” that was irrelevant to the determinative issues.
- Evidence: `evidence_fact` cue `evidence` at chunk `4518905` offsets `313-321`; context: After reviewing its appellate role in light of the Federal Court of Appeal’s decision in Canada (Citizenship and Immigration) v Huruglica, 2016 FCA 93, 396 DLR (4th) 527 [Huruglica], the RAD proceeded to assess the Applicants’ new evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4518905` offsets `926-933`; context: ” The RAD accepted the medical note into evidence because it contained information that arose after the RPD decision and was relevant to the matter.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4518905` offsets `740-746`; context: ” The RAD further noted that: “a document’s ‘newness’ cannot be tested solely by the date of its creation; what is important is the event or circumstance sought to be proved by the evidence.
- Evidence: `disposition` cue `dismissed` at chunk `4518905` offsets `12-21`; context: [5] The RAD dismissed the Applicants’ appeal in a decision dated August 10, 2016.
- Evidence: `issue` cue `whether` at chunk `4518906` offsets `93-100`; context: As to whether the RPD made an improper credibility finding because Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4518906` offsets `29-37`; context: [6] After addressing the new evidence, the RAD summarized the Applicant’s submissions.
- Evidence: `reasoning_application` cue `because` at chunk `4518906` offsets `146-153`; context: As to whether the RPD made an improper credibility finding because Ms.

#### 10323:1:subtheme:3 · paragraphs 7-7

- Raw key terms: `abortion, acknowledged, adult, agreed, applicants, authorities, burden, certificates`
- Display key terms: `abortion, acknowledged, adult, agreed, authorities, burden, certificates`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: abortion, acknowledged, adult, agreed, authorities, burden, certificates Evidence spans paragraphs 7-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4518907` offsets `369-376`; context: As to whether the RPD had erred in determining that the adult Applicants would not face forced sterilization in China due to the onset of the two-child policy, the RAD reviewed the RPD’s findings in this regard and concluded that it agreed with the RPD that there was no persuasive evidence that they would be sterilized if they had two children.
- Evidence: `evidence_fact` cue `evidence` at chunk `4518907` offsets `645-653`; context: As to whether the RPD had erred in determining that the adult Applicants would not face forced sterilization in China due to the onset of the two-child policy, the RAD reviewed the RPD’s findings in this regard and concluded that it agreed with the RPD that there was no persuasive evidence that they would be sterilized if they had two children.

#### Section text

Guo v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2017-03-27
Neutral citation
2017 FC 317
File numbers
IMM-3701-16
Decision Content
Date: 20170327
Docket: IMM-3701-16
Citation: 2017 FC 317
Ottawa, Ontario, March 27, 2017
PRESENT: The Honourable Mr. Justice Boswell
BETWEEN:
HAILING GUO
CHANGGUO LI
XINRUI LI
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] The Applicants, Hailing Guo, her husband Changguo Li, and their 12 year old daughter Xinrui Li, are citizens of China. They entered Canada on October 3, 2015 and sought refugee protection, claiming that they would be persecuted in China because Ms. Guo and Mr. Li had breached China’s family planning policies. Their claims were rejected, however, by the Refugee Protection Division [RPD] of the Immigration and Refugee Board [IRB] in a decision dated April 7, 2016. The Applicants appealed the RPD’s decision to the Refugee Appeal Division [RAD] of the IRB; but in a decision dated August 10, 2016, the RAD dismissed the appeal and confirmed the RPD’s decision that the Applicants were neither Convention refugees nor persons in need of protection. The Applicants have now applied under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] for judicial review of the RAD’s decision.
I. Background

[2] Ms. Guo and Mr. Li were married in August 2003; their daughter was born in May 2004. They wanted to have additional children but were prevented from doing so because of China’s one-child policy. They claim that Ms. Guo was forced to have two abortions and both she and her husband received sterilization notices which required either Ms. Guo or her husband to attend for sterilization. They also claim that officials attended at their residence on July 30, 2015, and delivered a second sterilization notice as well as a notice suspending their daughter from school. As a result of these notices, the Applicants went into hiding at the house of Ms. Guo’s uncle. The Applicants subsequently arranged for a smuggler to assist with their departure from China. The smuggler obtained a visa for the Applicants to travel to the United States and they arrived in Los Angeles on October 1, 2015; they arrived in Canada two days later and made a claim for refugee protection.

[3] The RPD rejected the Applicants’ claims for refugee protection. It determined that the documents submitted by the Applicants were not genuine and that their allegations were not credible. In particular, the RPD found that since the US visa application had been submitted before the authorities allegedly attended at the Applicants’ home on July 30, 2015, this seriously undermined the adult Applicants’ allegations that they decided to leave China because they had received a second sterilization notice and a notice suspending their daughter from school. The RPD also noted that the one-child policy law in China had changed to allow couples to have two children, and that because the adult Applicants would be allowed to have a second child it was reasonable to expect that they would not be required to be sterilized upon return to China.

[4] The Applicants appealed to the RAD on April 22, 2016, claiming that the RPD had erred in finding that: the Applicants’ evidence was not credible; the sterilization notices were fraudulent; the daughter’s suspension notice was fraudulent; and that the adult Applicants would not face a risk of forced sterilization due to China’s two-child policy. The Applicants provided new evidence to the RAD; notably, a medical note which indicated that Ms. Guo was pregnant and the estimated due date was December 16, 2016, and an article from LifeNews.com. The Applicants submitted to the RAD that the medical note was relevant because it showed that Ms. Guo may still face sterilization so that she does not have a third child, and that the LifeNews article indicated that couples who have reached their quota of two children are still at risk of forced sterilizations.
II. The RAD’s Decision

[5] The RAD dismissed the Applicants’ appeal in a decision dated August 10, 2016. After reviewing its appellate role in light of the Federal Court of Appeal’s decision in Canada (Citizenship and Immigration) v Huruglica, 2016 FCA 93, 396 DLR (4th) 527 [Huruglica], the RAD proceeded to assess the Applicants’ new evidence. The RAD referenced this Court’s decision in Olowolaiyemo v Canada (Citizenship and Immigration), 2015 FC 895 at para 19, [2016] 1 FCR 557: “new evidence may be accepted by the RAD either if it arose after the rejection of the claim or if it was not reasonably available or the person could not have been expected to have presented it at the time of the rejection.” The RAD further noted that: “a document’s ‘newness’ cannot be tested solely by the date of its creation; what is important is the event or circumstance sought to be proved by the evidence.” The RAD accepted the medical note into evidence because it contained information that arose after the RPD decision and was relevant to the matter. Although the LifeNews article post-dated the RPD decision, it was not accepted into evidence by the RAD because it contained information that was available prior to the RPD decision and it contained “a great deal of conjecture” that was irrelevant to the determinative issues.

[6] After addressing the new evidence, the RAD summarized the Applicant’s submissions. As to whether the RPD made an improper credibility finding because Ms. Guo failed to adduce her outpatient medical booklet to corroborate her two abortions, the RAD respected the RPD’s negative credibility finding in this regard, noting that her testimony confirmed that the abortions had been listed in the booklet and there was no reasonable explanation as to why it was not provided. In addition, the RAD deferred to the RPD’s negative credibility finding arising from the Applicants’ failure to provide the detailed summary reports from the hospital, noting that “the RPD had the opportunity to hear and observe the principal Appellant’s evidence.”

[7] With respect to the abortion certificates, the sterilization notices, and the school suspension notice, the RAD acknowledged and respected the RPD’s findings that these were not genuine; it also respected the RPD’s finding that the Applicants were not required to be sterilized by the authorities in China, and their child had not been suspended from school. As to whether the RPD had erred in determining that the adult Applicants would not face forced sterilization in China due to the onset of the two-child policy, the RAD reviewed the RPD’s findings in this regard and concluded that it agreed with the RPD that there was no persuasive evidence that they would be sterilized if they had two children. The RAD concluded that the Applicants had not satisfied their burden to prove that they were Convention refugees or persons in need of protection.
III. Issues

## 10323:2 · paragraphs 8-26

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3d8c174943a06f3f48d369dc5f37c2c8fd8a3e7a2503b0815f761530a88f19b8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10323:2:subtheme:1 · paragraphs 8-9

- Raw key terms: `admit, article, decision, evidence, lifenews, refusing, review, standard`
- Display key terms: `admit, article, lifenews, refusing, review, standard`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: admit, article, lifenews, refusing, review, standard Rule/authority context: [8] The Applicants raise the following issues: What is the appropriate standard of review? | Additionally, “as long as the process and the outcome fit comfortably with the principles of justification, transparency and intelligibility, it is not open to a reviewing court to substitute its own view of a preferable Application context: Did the RAD apply the wrong standard of review of the RPD’s decision and fail to independently assess the evidence before it? | Accordingly, the Court should not intervene if the RAD’s decision is justifiable, transparent, and intelligible, and it must determine “whether the decision falls within a range of possible, acceptable outcomes which are Evidence spans paragraphs 8-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4518908` offsets `39-45`; context: [8] The Applicants raise the following issues:
What is the appropriate standard of review?
- Evidence: `evidence_fact` cue `evidence` at chunk `4518908` offsets `156-164`; context: Did the RAD err in refusing to admit the LifeNews article as new evidence?
- Evidence: `governing_rule` cue `standard of review` at chunk `4518908` offsets `71-89`; context: [8] The Applicants raise the following issues:
What is the appropriate standard of review?
- Evidence: `reasoning_application` cue `apply` at chunk `4518908` offsets `178-183`; context: Did the RAD apply the wrong standard of review of the RPD’s decision and fail to independently assess the evidence before it?
- Evidence: `issue` cue `whether` at chunk `4518909` offsets `239-246`; context: Accordingly, the Court should not intervene if the RAD’s decision is justifiable, transparent, and intelligible, and it must determine “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law”: Dunsmuir v New Brunswick, 2008 SCC 9 at para 47, [2008] 1 SCR 190.
- Evidence: `evidence_fact` cue `evidence` at chunk `4518909` offsets `1075-1083`; context: Additionally, “as long as the process and the outcome fit comfortably with the principles of justification, transparency and intelligibility, it is not open to a reviewing court to substitute its own view of a preferable outcome”; and it is also not “the function of the reviewing court to reweigh the evidence”: Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at paras 59 and 61, [2009] 1 SCR 339.
- Evidence: `governing_rule` cue `principles` at chunk `4518909` offsets `852-862`; context: Additionally, “as long as the process and the outcome fit comfortably with the principles of justification, transparency and intelligibility, it is not open to a reviewing court to substitute its own view of a preferable outcome”; and it is also not “the function of the reviewing court to reweigh the evidence”: Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at paras 59 and 61, [2009] 1 SCR 339.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4518909` offsets `103-114`; context: Accordingly, the Court should not intervene if the RAD’s decision is justifiable, transparent, and intelligible, and it must determine “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law”: Dunsmuir v New Brunswick, 2008 SCC 9 at para 47, [2008] 1 SCR 190.

#### 10323:2:subtheme:2 · paragraphs 10-12

- Raw key terms: `applicants, article, conjecture, evidence, lifenews, relevant, accept, according`
- Display key terms: `article, conjecture, lifenews, relevant, accept, according`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: article, conjecture, lifenews, relevant, accept, according Position/evidence statements: [10] The Applicants contend that the RAD erred in failing to accept the LifeNews article as new evidence. | [11] The Respondent argues that the RAD reasonably found that the LifeNews article did not meet the test for new evidence because it was merely a compilation of statistics derived from easily available sources along with Rule/authority context: Did the RAD apply the wrong standard of review of the RPD’s decision and fail to independently assess the evidence before it? Application context: According to the Applicants, the information in this article constitutes “new evidence” because, not only does it provide insight into the state of China’s family planning policy after implementation of the two-child pol | [11] The Respondent argues that the RAD reasonably found that the LifeNews article did not meet the test for new evidence because it was merely a compilation of statistics derived from easily available sources along with Evidence spans paragraphs 10-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4518910` offsets `260-265`; context: They say the article is not based on conjecture since it is based on reputable sources such as the US Department of State and is directly relevant to the issue of whether the inception of the two-child policy will alleviate the risk of sterilization faced by the adult Applicants upon return to China.
- Evidence: `party_position` cue `contend` at chunk `4518910` offsets `20-27`; context: [10] The Applicants contend that the RAD erred in failing to accept the LifeNews article as new evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4518910` offsets `96-104`; context: [10] The Applicants contend that the RAD erred in failing to accept the LifeNews article as new evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4518910` offsets `496-503`; context: According to the Applicants, the information in this article constitutes “new evidence” because, not only does it provide insight into the state of China’s family planning policy after implementation of the two-child policy in early 2016, but it also constitutes recent information that could not have been provided to the RPD.
- Evidence: `counterargument_limitation` cue `but` at chunk `4518910` offsets `647-650`; context: According to the Applicants, the information in this article constitutes “new evidence” because, not only does it provide insight into the state of China’s family planning policy after implementation of the two-child policy in early 2016, but it also constitutes recent information that could not have been provided to the RPD.
- Evidence: `issue` cue `issue` at chunk `4518911` offsets `266-271`; context: [11] The Respondent argues that the RAD reasonably found that the LifeNews article did not meet the test for new evidence because it was merely a compilation of statistics derived from easily available sources along with conjecture which did not address the central issue in this case.
- Evidence: `party_position` cue `argues` at chunk `4518911` offsets `20-26`; context: [11] The Respondent argues that the RAD reasonably found that the LifeNews article did not meet the test for new evidence because it was merely a compilation of statistics derived from easily available sources along with conjecture which did not address the central issue in this case.
- Evidence: `evidence_fact` cue `found that` at chunk `4518911` offsets `51-61`; context: [11] The Respondent argues that the RAD reasonably found that the LifeNews article did not meet the test for new evidence because it was merely a compilation of statistics derived from easily available sources along with conjecture which did not address the central issue in this case.
- Evidence: `reasoning_application` cue `because` at chunk `4518911` offsets `122-129`; context: [11] The Respondent argues that the RAD reasonably found that the LifeNews article did not meet the test for new evidence because it was merely a compilation of statistics derived from easily available sources along with conjecture which did not address the central issue in this case.
- Evidence: `evidence_fact` cue `evidence` at chunk `4518912` offsets `97-105`; context: [12] In this case, it was reasonable for the RAD to refuse to accept the LifeNews article as new evidence.
- Evidence: `governing_rule` cue `standard of review` at chunk `4518912` offsets `686-704`; context: Did the RAD apply the wrong standard of review of the RPD’s decision and fail to independently assess the evidence before it?
- Evidence: `reasoning_application` cue `apply` at chunk `4518912` offsets `670-675`; context: Did the RAD apply the wrong standard of review of the RPD’s decision and fail to independently assess the evidence before it?

#### 10323:2:subtheme:3 · paragraphs 13-14

- Raw key terms: `according, applicants, assessment, claim, credibility, findings, independent, submissions`
- Display key terms: `according, assessment, credibility, findings, independent, submissions`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: according, assessment, credibility, findings, independent, submissions Evidence spans paragraphs 13-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4518913` offsets `128-134`; context: [13] The Applicants maintain that the RAD failed to conduct an independent assessment of the evidence and merely reiterated the issues identified by the RPD and the Applicants’ corresponding submissions.
- Evidence: `evidence_fact` cue `evidence` at chunk `4518913` offsets `93-101`; context: [13] The Applicants maintain that the RAD failed to conduct an independent assessment of the evidence and merely reiterated the issues identified by the RPD and the Applicants’ corresponding submissions.
- Evidence: `counterargument_limitation` cue `but` at chunk `4518913` offsets `609-612`; context: They draw the Court’s attention to Madava v Canada (Citizenship and Immigration), 2017 FC 149, [2017] FCJ No 148 [Madava], where the Court determined that the RAD in that case had not conducted its own assessment of the claim but, rather, merely referred to specific findings made by the RPD and simply endorsed those findings.

#### 10323:2:subtheme:4 · paragraphs 15-16

- Raw key terms: `findings, issue, agree, apparent, appeal, applicants, apply, assessment`
- Display key terms: `findings, agree, apparent, apply, assessment`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: findings, agree, apparent, apply, assessment Application context: [16] In Huruglica, the Federal Court of Appeal determined that the RAD must apply the correctness standard when it reviews the RPD’s findings of law, of fact, and of mixed fact and law which involve no issue as to the cr Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4518915` offsets `92-97`; context: [15] The Applicants fairly point out that the RAD’s conclusory remarks after reviewing each issue were fairly brief.
- Evidence: `counterargument_limitation` cue `However` at chunk `4518915` offsets `117-124`; context: However, it is not unreasonable for the RAD to defer to, agree with, or respect the RPD’s findings and conclusions, provided it is apparent from the RAD’s reasons (as it is in this case) that it exercised independent judgment, conducted its own assessment of the claim, and did not simply endorse the RPD’s findings and conclusions.
- Evidence: `issue` cue `issue` at chunk `4518916` offsets `202-207`; context: [16] In Huruglica, the Federal Court of Appeal determined that the RAD must apply the correctness standard when it reviews the RPD’s findings of law, of fact, and of mixed fact and law which involve no issue as to the credibility of oral testimony:
- Evidence: `evidence_fact` cue `determined that` at chunk `4518916` offsets `47-62`; context: [16] In Huruglica, the Federal Court of Appeal determined that the RAD must apply the correctness standard when it reviews the RPD’s findings of law, of fact, and of mixed fact and law which involve no issue as to the credibility of oral testimony:
- Evidence: `reasoning_application` cue `apply` at chunk `4518916` offsets `76-81`; context: [16] In Huruglica, the Federal Court of Appeal determined that the RAD must apply the correctness standard when it reviews the RPD’s findings of law, of fact, and of mixed fact and law which involve no issue as to the credibility of oral testimony:

#### 10323:2:subtheme:5 · paragraphs 17-18

- Raw key terms: `acws, analysis, appellant, applying, aptly, canada, carefully, carries`
- Display key terms: `acws, analysis, appellant, applying, aptly, carefully, carries`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: acws, analysis, appellant, applying, aptly, carefully, carries Position/evidence statements: Thus, after carefully considering the RPD decision, the RAD carries out its own analysis of the record to determine whether, as submitted by the appellant, the RPD erred…. Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4518917` offsets `113-118`; context: [103] … with respect to findings of fact (and mixed fact and law) such as the one involved here, which raised no issue of credibility of oral evidence, the RAD is to review RPD decisions applying the correctness standard.
- Evidence: `party_position` cue `submitted` at chunk `4518917` offsets `350-359`; context: Thus, after carefully considering the RPD decision, the RAD carries out its own analysis of the record to determine whether, as submitted by the appellant, the RPD erred….
- Evidence: `evidence_fact` cue `evidence` at chunk `4518917` offsets `142-150`; context: [103] … with respect to findings of fact (and mixed fact and law) such as the one involved here, which raised no issue of credibility of oral evidence, the RAD is to review RPD decisions applying the correctness standard.

#### 10323:2:subtheme:6 · paragraphs 19-20

- Raw key terms: `apply, approach, credibility, evidence, fact, findings, huruglica, mixed`
- Display key terms: `apply, approach, credibility, fact, findings, huruglica, mixed`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: apply, approach, credibility, fact, findings, huruglica, mixed Rule/authority context: [23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and  Application context: [23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and  | [18] Furthermore, in cases which raise issues as to the credibility of oral evidence, of which this case is one, the RAD may apply a more deferential approach if “the RPD enjoys a meaningful advantage over the RAD in mak Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4518919` offsets `178-183`; context: [23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and must take a case-by-case approach to the level of deference it owes to the relative weight of testimony and their credibility or lack thereof (Huruglica at paras 37, 69-71, 103).
- Evidence: `evidence_fact` cue `evidence` at chunk `4518919` offsets `207-215`; context: [23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and must take a case-by-case approach to the level of deference it owes to the relative weight of testimony and their credibility or lack thereof (Huruglica at paras 37, 69-71, 103).
- Evidence: `governing_rule` cue `standard of review` at chunk `4518919` offsets `40-58`; context: [23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and must take a case-by-case approach to the level of deference it owes to the relative weight of testimony and their credibility or lack thereof (Huruglica at paras 37, 69-71, 103).
- Evidence: `reasoning_application` cue `apply` at chunk `4518919` offsets `18-23`; context: [23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and must take a case-by-case approach to the level of deference it owes to the relative weight of testimony and their credibility or lack thereof (Huruglica at paras 37, 69-71, 103).
- Evidence: `issue` cue `issues` at chunk `4518920` offsets `39-45`; context: [18] Furthermore, in cases which raise issues as to the credibility of oral evidence, of which this case is one, the RAD may apply a more deferential approach if “the RPD enjoys a meaningful advantage over the RAD in making findings of fact or mixed fact and law” (Huruglica at para 70).
- Evidence: `evidence_fact` cue `evidence` at chunk `4518920` offsets `76-84`; context: [18] Furthermore, in cases which raise issues as to the credibility of oral evidence, of which this case is one, the RAD may apply a more deferential approach if “the RPD enjoys a meaningful advantage over the RAD in making findings of fact or mixed fact and law” (Huruglica at para 70).
- Evidence: `reasoning_application` cue `apply` at chunk `4518920` offsets `125-130`; context: [18] Furthermore, in cases which raise issues as to the credibility of oral evidence, of which this case is one, the RAD may apply a more deferential approach if “the RPD enjoys a meaningful advantage over the RAD in making findings of fact or mixed fact and law” (Huruglica at para 70).

#### 10323:2:subtheme:7 · paragraphs 21-23

- Raw key terms: `applicants, evidence, risk, based, because, child, failed, notices`
- Display key terms: `risk, based, because, child, failed, notices`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: risk, based, because, child, failed, notices Position/evidence statements: [20] The Applicants submit that the RAD’s conclusion that the adult Applicants would be allowed to have a second child in China after the inception of the two-child policy was based on speculation and that, since Ms. Application context: This case is distinguishable from Madava because, in this case, the RAD extensively reviewed the RPD’s findings based on the Applicants’ written submissions as well as the RPD’s record, including the documentary evidence | The Applicants note that the sterilization notices remain outstanding, and that there was no evidence that the two-child policy would apply retroactively and forgive the adult Applicants’ prior violation of the family pl Operative outcome context: [20] The Applicants submit that the RAD’s conclusion that the adult Applicants would be allowed to have a second child in China after the inception of the two-child policy was based on speculation and that, since Ms. Evidence spans paragraphs 21-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4518921` offsets `428-434`; context: The issues raised by the Applicants primarily dealt with the RPD’s negative credibility findings which led it to determine that the Applicants’ testimony was not credible and that their documentary evidence was fraudulent.
- Evidence: `evidence_fact` cue `evidence` at chunk `4518921` offsets `134-142`; context: [19] I am not persuaded by the Applicants’ argument that the RAD unreasonably failed to conduct its own independent assessment of the evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4518921` offsets `185-192`; context: This case is distinguishable from Madava because, in this case, the RAD extensively reviewed the RPD’s findings based on the Applicants’ written submissions as well as the RPD’s record, including the documentary evidence and oral testimony, to support its ultimate determination.
- Evidence: `party_position` cue `submit` at chunk `4518922` offsets `20-26`; context: [20] The Applicants submit that the RAD’s conclusion that the adult Applicants would be allowed to have a second child in China after the inception of the two-child policy was based on speculation and that, since Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4518922` offsets `483-491`; context: The Applicants note that the sterilization notices remain outstanding, and that there was no evidence that the two-child policy would apply retroactively and forgive the adult Applicants’ prior violation of the family planning policy.
- Evidence: `reasoning_application` cue `apply` at chunk `4518922` offsets `524-529`; context: The Applicants note that the sterilization notices remain outstanding, and that there was no evidence that the two-child policy would apply retroactively and forgive the adult Applicants’ prior violation of the family planning policy.
- Evidence: `disposition` cue `allowed` at chunk `4518922` offsets `88-95`; context: [20] The Applicants submit that the RAD’s conclusion that the adult Applicants would be allowed to have a second child in China after the inception of the two-child policy was based on speculation and that, since Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4518923` offsets `62-70`; context: [21] The Respondent says that the RAD reasonably reviewed the evidence concerning the changes to the one-child policy and determined that the Applicants would not face persecution.
- Evidence: `reasoning_application` cue `because` at chunk `4518923` offsets `428-435`; context: In the Respondent’s view, the Applicants speculate that it is “conceivable” they would be persecuted because of the outstanding sterilization notices; but they did not provide any evidence to support this claim, such as how the two-child policy would be implemented.
- Evidence: `counterargument_limitation` cue `but` at chunk `4518923` offsets `478-481`; context: In the Respondent’s view, the Applicants speculate that it is “conceivable” they would be persecuted because of the outstanding sterilization notices; but they did not provide any evidence to support this claim, such as how the two-child policy would be implemented.

#### 10323:2:subtheme:8 · paragraphs 24-25

- Raw key terms: `because, respect, above, acceptable, applicants, application, arguments, case`
- Display key terms: `because, respect, above, acceptable, arguments, case`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: because, respect, above, acceptable, arguments, case Position/evidence statements: Both the RAD and the RPD determined that the sterilization notices were fraudulent; hence, the RAD’s statements about future risks in China, even if speculative as the Applicants contend, are inconsequential because the  Application context: Both the RAD and the RPD determined that the sterilization notices were fraudulent; hence, the RAD’s statements about future risks in China, even if speculative as the Applicants contend, are inconsequential because the  | The RAD’s decision in this case was reasonable because it is transparent and intelligible and falls within the range of possible and acceptable outcomes defensible in respect of the facts and law. Operative outcome context: [23] For the reasons stated above, this application for judicial review is dismissed. Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4518924` offsets `22-27`; context: [22] In my view, this issue is peripheral to the RAD’s ultimate determination that the Applicants were neither Convention refugees nor persons in need of protection.
- Evidence: `party_position` cue `contend` at chunk `4518924` offsets `455-462`; context: Both the RAD and the RPD determined that the sterilization notices were fraudulent; hence, the RAD’s statements about future risks in China, even if speculative as the Applicants contend, are inconsequential because the finding that the Applicants never received sterilization notices undermines their entire claim for protection.
- Evidence: `evidence_fact` cue `determined that` at chunk `4518924` offsets `301-316`; context: Both the RAD and the RPD determined that the sterilization notices were fraudulent; hence, the RAD’s statements about future risks in China, even if speculative as the Applicants contend, are inconsequential because the finding that the Applicants never received sterilization notices undermines their entire claim for protection.
- Evidence: `reasoning_application` cue `because` at chunk `4518924` offsets `484-491`; context: Both the RAD and the RPD determined that the sterilization notices were fraudulent; hence, the RAD’s statements about future risks in China, even if speculative as the Applicants contend, are inconsequential because the finding that the Applicants never received sterilization notices undermines their entire claim for protection.
- Evidence: `reasoning_application` cue `because` at chunk `4518925` offsets `133-140`; context: The RAD’s decision in this case was reasonable because it is transparent and intelligible and falls within the range of possible and acceptable outcomes defensible in respect of the facts and law.
- Evidence: `disposition` cue `dismissed` at chunk `4518925` offsets `75-84`; context: [23] For the reasons stated above, this application for judicial review is dismissed.

#### 10323:2:subtheme:9 · paragraphs 26-26

- Raw key terms: `certification, certified, general, importance, neither, party, proposed, question`
- Display key terms: `certification, certified, importance, neither, proposed, question`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: certification, certified, importance, neither, proposed, question Evidence spans paragraphs 26-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4518926` offsets `30-38`; context: [24] Neither party proposed a question of general importance for certification; so, no such question is certified.

#### Section text

[8] The Applicants raise the following issues:
What is the appropriate standard of review?
Did the RAD err in refusing to admit the LifeNews article as new evidence?
Did the RAD apply the wrong standard of review of the RPD’s decision and fail to independently assess the evidence before it?
Did the RAD err in considering the risk of persecution faced by the Applicants in light of the fact that Ms. Guo was pregnant with her second child?
IV. Analysis
A. Standard of Review

[9] The applicable standard for review of the RAD’s decision is reasonableness (Huruglica at para 35). Accordingly, the Court should not intervene if the RAD’s decision is justifiable, transparent, and intelligible, and it must determine “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law”: Dunsmuir v New Brunswick, 2008 SCC 9 at para 47, [2008] 1 SCR 190. Those criteria are met if “the reasons allow the reviewing court to understand why the tribunal made its decision and permit it to determine whether the conclusion is within the range of acceptable outcomes”: Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at para 16, [2011] 3 SCR 708. Additionally, “as long as the process and the outcome fit comfortably with the principles of justification, transparency and intelligibility, it is not open to a reviewing court to substitute its own view of a preferable outcome”; and it is also not “the function of the reviewing court to reweigh the evidence”: Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at paras 59 and 61, [2009] 1 SCR 339.
B. Did the RAD err in refusing to admit the LifeNews article as new evidence?

[10] The Applicants contend that the RAD erred in failing to accept the LifeNews article as new evidence. They say the article is not based on conjecture since it is based on reputable sources such as the US Department of State and is directly relevant to the issue of whether the inception of the two-child policy will alleviate the risk of sterilization faced by the adult Applicants upon return to China. According to the Applicants, the information in this article constitutes “new evidence” because, not only does it provide insight into the state of China’s family planning policy after implementation of the two-child policy in early 2016, but it also constitutes recent information that could not have been provided to the RPD.

[11] The Respondent argues that the RAD reasonably found that the LifeNews article did not meet the test for new evidence because it was merely a compilation of statistics derived from easily available sources along with conjecture which did not address the central issue in this case. The Respondent notes subsection 29(4) of the Refugee Appeal Division Rules, SOR/2012-257, which requires the RAD to consider “the document’s relevance and probative value.” According to the Respondent, the LifeNews article was not relevant since it was wholly inapplicable to the Applicants’ particular circumstances.

[12] In this case, it was reasonable for the RAD to refuse to accept the LifeNews article as new evidence. Even though the article post-dated the RPD’s decision and was relevant to the Applicants’ claim for protection, the US Department of State report for 2015 referred to in the article contained information that was available prior to the RPD’s decision. Moreover, the conjecture referred to in the article was that of an activist against forced abortions in China who contended that the new policy in China has not ended forced sterilization and sex-selective abortions. The RAD did not err in refusing to admit the LifeNews article as new evidence.
C. Did the RAD apply the wrong standard of review of the RPD’s decision and fail to independently assess the evidence before it?

[13] The Applicants maintain that the RAD failed to conduct an independent assessment of the evidence and merely reiterated the issues identified by the RPD and the Applicants’ corresponding submissions. According to the Applicants, instead of conducting an independent assessment and analysis of the issues, the RAD simply deferred to and respected the RPD’s findings and decision. They draw the Court’s attention to Madava v Canada (Citizenship and Immigration), 2017 FC 149, [2017] FCJ No 148 [Madava], where the Court determined that the RAD in that case had not conducted its own assessment of the claim but, rather, merely referred to specific findings made by the RPD and simply endorsed those findings. The Applicants claim that the RAD failed to scrutinize the RPD’s decision on the standard of correctness and, as a result, its treatment and assessment of the abortion certificates, the sterilization notices, and the school suspension notice, as well as its negative credibility findings, were unreasonable.

[14] The Respondent says the RAD performed an independent and reasonable assessment of the Applicants’ claim. For example, the Respondent notes that the RAD extensively explained the RPD’s finding concerning the birth control booklet and addressed the Applicants’ written submissions to the RAD. According to the Respondent, it was reasonable for the RAD to defer to the RPD’s credibility findings, since the RPD had an advantage as the trier of fact of first instance, and the RAD’s assessment was in line with Huruglica.

[15] The Applicants fairly point out that the RAD’s conclusory remarks after reviewing each issue were fairly brief. However, it is not unreasonable for the RAD to defer to, agree with, or respect the RPD’s findings and conclusions, provided it is apparent from the RAD’s reasons (as it is in this case) that it exercised independent judgment, conducted its own assessment of the claim, and did not simply endorse the RPD’s findings and conclusions.

[16] In Huruglica, the Federal Court of Appeal determined that the RAD must apply the correctness standard when it reviews the RPD’s findings of law, of fact, and of mixed fact and law which involve no issue as to the credibility of oral testimony:

[103] … with respect to findings of fact (and mixed fact and law) such as the one involved here, which raised no issue of credibility of oral evidence, the RAD is to review RPD decisions applying the correctness standard. Thus, after carefully considering the RPD decision, the RAD carries out its own analysis of the record to determine whether, as submitted by the appellant, the RPD erred….

[17] The gist of Huruglica was aptly summarized by Justice Gleeson in Ghauri v Canada (Citizenship and Immigration), 2016 FC 548, 267 ACWS (3d) 423, as follows:

[23] The RAD must apply the correctness standard of review with respect to reviewing findings of law, as well as findings of fact and mixed fact and law of the RPD that raise no issue of credibility of oral evidence and must take a case-by-case approach to the level of deference it owes to the relative weight of testimony and their credibility or lack thereof (Huruglica at paras 37, 69-71, 103).

[18] Furthermore, in cases which raise issues as to the credibility of oral evidence, of which this case is one, the RAD may apply a more deferential approach if “the RPD enjoys a meaningful advantage over the RAD in making findings of fact or mixed fact and law” (Huruglica at para 70).

[19] I am not persuaded by the Applicants’ argument that the RAD unreasonably failed to conduct its own independent assessment of the evidence. This case is distinguishable from Madava because, in this case, the RAD extensively reviewed the RPD’s findings based on the Applicants’ written submissions as well as the RPD’s record, including the documentary evidence and oral testimony, to support its ultimate determination. The issues raised by the Applicants primarily dealt with the RPD’s negative credibility findings which led it to determine that the Applicants’ testimony was not credible and that their documentary evidence was fraudulent. It was reasonable for the RAD to adopt the RPD’s reasoning, while recognizing that the RPD had a meaningful advantage because it had the opportunity to hear and observe the Applicants’ evidence. It is apparent upon review of the RAD’s decision that, while its findings were largely based on the RPD’s numerous negative credibility findings and testimony which was inconsistent with the documentary evidence, the RAD conducted its own assessment of the evidence and arrived at an independent determination of the Applicants’ claims.
D. Did the RAD err in considering the risk of persecution faced by the Applicants in light of the fact that Ms. Guo was pregnant with her second child?

[20] The Applicants submit that the RAD’s conclusion that the adult Applicants would be allowed to have a second child in China after the inception of the two-child policy was based on speculation and that, since Ms. Guo was pregnant with her second child and will reach the two-child quota, there is a risk that she or her husband will be sterilized to prevent the birth of a third child. The Applicants note that the sterilization notices remain outstanding, and that there was no evidence that the two-child policy would apply retroactively and forgive the adult Applicants’ prior violation of the family planning policy.

[21] The Respondent says that the RAD reasonably reviewed the evidence concerning the changes to the one-child policy and determined that the Applicants would not face persecution. According to the Respondent, the Applicants failed to provide the RAD with any evidence that spoke to their alleged future risk of sterilization. In the Respondent’s view, the Applicants speculate that it is “conceivable” they would be persecuted because of the outstanding sterilization notices; but they did not provide any evidence to support this claim, such as how the two-child policy would be implemented. The Respondent states that the only evidence before the RAD was that the one-child policy had been eliminated and the RAD properly proceeded on this basis.

[22] In my view, this issue is peripheral to the RAD’s ultimate determination that the Applicants were neither Convention refugees nor persons in need of protection. The Applicants’ arguments with respect to this issue hinges on there being outstanding sterilization notices. Both the RAD and the RPD determined that the sterilization notices were fraudulent; hence, the RAD’s statements about future risks in China, even if speculative as the Applicants contend, are inconsequential because the finding that the Applicants never received sterilization notices undermines their entire claim for protection.
V. Conclusion

[23] For the reasons stated above, this application for judicial review is dismissed. The RAD’s decision in this case was reasonable because it is transparent and intelligible and falls within the range of possible and acceptable outcomes defensible in respect of the facts and law.

[24] Neither party proposed a question of general importance for certification; so, no such question is certified.


## 10323:3 · paragraphs 27-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `305c77451ec159c254ffa1d1ec84994885331946c5a9b7a6b9592b76d335a8f5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10323:3:subtheme:1 · paragraphs 27-28

- Raw key terms: `application, boswell, cause, certified, changguo, citizenship, court, date`
- Display key terms: `boswell, certified, changguo, date`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: boswell, certified, changguo, date Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that: the application for judicial review is dismissed; and no question of general importance is certified. Evidence spans paragraphs 27-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4518926` offsets `212-220`; context: JUDGMENT
THIS COURT’S JUDGMENT is that: the application for judicial review is dismissed; and no question of general importance is certified.
- Evidence: `disposition` cue `dismissed` at chunk `4518926` offsets `194-203`; context: JUDGMENT
THIS COURT’S JUDGMENT is that: the application for judicial review is dismissed; and no question of general importance is certified.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that: the application for judicial review is dismissed; and no question of general importance is certified.
"Keith M. Boswell"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-3701-16
STYLE OF CAUSE:
HAILING GUO, CHANGGUO LI, XINRUI LI v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
March 1, 2017


## 10323:4 · paragraphs 29-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d02a36811374cf4698c8b498022c2da794c3c096512b84bfb9b7e26661d535ef`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10323:4:subtheme:1 · paragraphs 29-29

- Raw key terms: `appearances, applicants, associates, attorney, barristers, boswell, canada, dated`
- Display key terms: `associates, barristers, boswell, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: associates, barristers, boswell, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 29-29. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
BOSWELL J.
DATED:
march 27, 2017
APPEARANCES:
Stephanie Fung
For The Applicants
Lucan Gregory
For The Respondent
SOLICITORS OF RECORD:
Lewis & Associates
Barristers and Solicitors
Toronto, Ontario
For The Applicants
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
