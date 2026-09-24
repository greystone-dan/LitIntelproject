# Discussion Units: case 24275

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **47**
- Continuity pairs: **46**
- Discussion Units: **4**
- Paragraph source hashes: **47**
- Sub-themes: **15**

## 24275:1 · paragraphs 0-17

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6a97d026859d3624fbcffe579290c36491cd510e6380cb7b5fe4a73488fc14dc`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24275:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `applicant, decision, immigration, annis, application, august, board, canada`
- Display key terms: `annis, august`
- Argument roles: `governing_rule`
- Explanation: Observed roles: governing_rule Display terms: annis, august Rule/authority context: [1] This is an application for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] of an August 24, 2012 decision by the Immigration and Refugee Board that the ap Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5141253` offsets `47-58`; context: [1] This is an application for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] of an August 24, 2012 decision by the Immigration and Refugee Board that the applicant was neither a Convention refugee, nor a person in need of protection, pursuant to sections 96 and 97 of the IRPA.

#### 24275:1:subtheme:2 · paragraphs 2-6

- Raw key terms: `applicant, broke, canada, house, just, partner, poland, problems`
- Display key terms: `broke, house, just, partner, poland, problems`
- Argument roles: `counterargument_limitation, disposition`
- Explanation: Observed roles: counterargument_limitation, disposition Display terms: broke, house, just, partner, poland, problems Operative outcome context: [2] For the reasons which follow, the application is dismissed. | She was initially granted a six-month visa extension, but she says that her family discouraged her from applying for a further extension and told her to just stay on illegally. Evidence spans paragraphs 2-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `5141254` offsets `53-62`; context: [2] For the reasons which follow, the application is dismissed.
- Evidence: `counterargument_limitation` cue `However` at chunk `5141255` offsets `337-344`; context: However the applicant remained with him until 2006, notwithstanding physical injuries including a broken nose, broken arms and legs and problems with one of her ears.
- Evidence: `disposition` cue `granted` at chunk `5141258` offsets `106-113`; context: She was initially granted a six-month visa extension, but she says that her family discouraged her from applying for a further extension and told her to just stay on illegally.

#### 24275:1:subtheme:3 · paragraphs 7-9

- Raw key terms: `decision, family, provided, sent, toronto, advice, advised, alcohol`
- Display key terms: `family, provided, sent, toronto, advice, advised, alcohol`
- Argument roles: `evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, party_position, reasoning_application Display terms: family, provided, sent, toronto, advice, advised, alcohol Position/evidence statements: While she was there the Refugee Law Office provided her advice and she submitted an application for refugee status on October 7, 2009. Application context: [7] The applicant did not discover that it was possible to apply for asylum until she was stopped by the police, apparently for jaywalking, and sent to immigration detention. Evidence spans paragraphs 7-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submitted` at chunk `5141259` offsets `391-400`; context: While she was there the Refugee Law Office provided her advice and she submitted an application for refugee status on October 7, 2009.
- Evidence: `reasoning_application` cue `apply` at chunk `5141259` offsets `59-64`; context: [7] The applicant did not discover that it was possible to apply for asylum until she was stopped by the police, apparently for jaywalking, and sent to immigration detention.
- Evidence: `evidence_fact` cue `evidence` at chunk `5141260` offsets `440-448`; context: She provided evidence of a Family Court decision from 2009 terminating her and Mr.

#### 24275:1:subtheme:4 · paragraphs 10-16

- Raw key terms: `panel, found, applicant, claimant, evidence, member, poland, police`
- Display key terms: `poland, police`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: poland, police Position/evidence statements: However, Poland was making efforts to improve police responsiveness, and although counsel had submitted material from Amnesty International, Freedom House, the European Police Action Centre on Violence Against Women, and Rule/authority context: The panel again reviewed the extensive jurisprudence governing IFAs, including the insufficiency of arguments that claimants had no friends or family in the region, or could not find suitable work there, or might be bett | [16] The panel member then examined a “compelling reasons” submission of the applicant under section 108 of IRPA. Application context: [14] The panel did not accept the applicant’s explanation of why she had delayed requesting police documents until just prior to the hearing, or her explanation that some reports could not be provided because officers we | Accordingly, the panel found that under the circumstances it would not be objectively unreasonable for her to relocate to Warsaw. Evidence spans paragraphs 10-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5141262` offsets `394-400`; context: The determinative issues were delay in claiming, state protection, and internal flight alternative (IFA).
- Evidence: `evidence_fact` cue `found that` at chunk `5141263` offsets `22-32`; context: [11] The panel member found that the delay in claiming asylum was inconsistent with a person living in fear of persecution to fail to seek asylum as soon as possible.
- Evidence: `counterargument_limitation` cue `but` at chunk `5141263` offsets `257-260`; context: The claimant’s family may have provided her with poor, and moreover unscrupulous, advice, but she was aware of her illegal status and took no steps to regularize it.
- Evidence: `evidence_fact` cue `evidence` at chunk `5141264` offsets `59-67`; context: [12] The panel member reviewed the law and the applicant’s evidence on state protection.
- Evidence: `counterargument_limitation` cue `although` at chunk `5141264` offsets `740-748`; context: Prosecutions were being brought against persons convicted of domestic violence who could be sentenced to a maximum five years in prison, although sentences tended to be more lenient.
- Evidence: `party_position` cue `submitted` at chunk `5141265` offsets `368-377`; context: However, Poland was making efforts to improve police responsiveness, and although counsel had submitted material from Amnesty International, Freedom House, the European Police Action Centre on Violence Against Women, and the UN Committee on the Elimination of Discrimination Against Women, this documentation was five to seven years old.
- Evidence: `evidence_fact` cue `evidence` at chunk `5141265` offsets `102-110`; context: The panel referred to documentary evidence acknowledging that the police could be reluctant to intervene in domestic disputes and that protection for women in abusive situations was sometimes insufficient.
- Evidence: `reasoning_application` cue `because` at chunk `5141266` offsets `201-208`; context: [14] The panel did not accept the applicant’s explanation of why she had delayed requesting police documents until just prior to the hearing, or her explanation that some reports could not be provided because officers were changing jobs, or her claim that Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5141267` offsets `621-629`; context: However, there was no evidence of a special relationship between Tadeusz and the police in Warsaw that would suggest she would not be accorded police protection if this was requested from Warsaw authorities.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5141267` offsets `205-218`; context: The panel again reviewed the extensive jurisprudence governing IFAs, including the insufficiency of arguments that claimants had no friends or family in the region, or could not find suitable work there, or might be better off in Canada economically, physically, or emotionally than they would be in their own country.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5141267` offsets `985-996`; context: Accordingly, the panel found that under the circumstances it would not be objectively unreasonable for her to relocate to Warsaw.
- Evidence: `counterargument_limitation` cue `However` at chunk `5141267` offsets `599-606`; context: However, there was no evidence of a special relationship between Tadeusz and the police in Warsaw that would suggest she would not be accorded police protection if this was requested from Warsaw authorities.
- Evidence: `evidence_fact` cue `evidence` at chunk `5141268` offsets `345-353`; context: On that point, the panel concluded that there was no persuasive evidence that conditions in Poland had changed such that the “compelling reasons” exception should apply.
- Evidence: `governing_rule` cue `under` at chunk `5141268` offsets `87-92`; context: [16] The panel member then examined a “compelling reasons” submission of the applicant under section 108 of IRPA.
- Evidence: `reasoning_application` cue `applied` at chunk `5141268` offsets `149-156`; context: She noted that subparagraph (1)(e) applied to cases in which a person would have been a refugee but the country conditions originally causing this no longer existed.

#### 24275:1:subtheme:5 · paragraphs 17-17

- Raw key terms: `convention, czesak, found, issues, need, neither, panel, person`
- Display key terms: `convention, czesak, issues, need, neither, person`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: convention, czesak, issues, need, neither, person Evidence spans paragraphs 17-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5141269` offsets `106-112`; context: Issues
- Evidence: `evidence_fact` cue `found that` at chunk `5141269` offsets `15-25`; context: [17] The panel found that Ms.

#### Section text

Czesak v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2013-11-14
Neutral citation
2013 FC 1149
File numbers
IMM-9539-12
Decision Content
Date: 20131114
Docket:
IMM-9539-12
Citation: 2013 FC 1149
Ottawa, Ontario, November 14, 2013
PRESENT: The Honourable Mr. Justice Annis
BETWEEN:
MARIA CZESAK
(a.k.a. MARIA CZESLAWA CZESAK)
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT
Introduction

[1] This is an application for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] of an August 24, 2012 decision by the Immigration and Refugee Board that the applicant was neither a Convention refugee, nor a person in need of protection, pursuant to sections 96 and 97 of the IRPA.

[2] For the reasons which follow, the application is dismissed.
Factual background

[3] The applicant was born in Poland in 1958. The applicant married in 1979 and had three children from this marriage. It ended in 1988, at which point the applicant formed a new relationship with a common law partner Tadeusz Poniewierski, with whom she had three additional children. The relationship with Mr. Poniewierski was abusive. However the applicant remained with him until 2006, notwithstanding physical injuries including a broken nose, broken arms and legs and problems with one of her ears.

[4] The applicant called the police many times but they just told her to resolve her own marital problems. Her second partner shared a pigeon-breeding hobby with the chief of the village police force and drank with other police officers. He was once arrested after assaulting her, but was released on probation. She finally broke up with him, but he did not move away. He continued to come by her house frequently to harass her.

[5] Ms. Czesak visited Canada from September 2005 to March 2006. When she returned to Poland, her ex-partner met her at the Warsaw airport, forced his way into the car and came back to her house with her. There, he broke the door and windows, punched her son, and pushed her down the stairs, knocking her out.

[6] She flew to Canada in July 2006 on another visitor’s six-month visa and never left. She was initially granted a six-month visa extension, but she says that her family discouraged her from applying for a further extension and told her to just stay on illegally. They did not meet the financial criteria to sponsor her.

[7] The applicant did not discover that it was possible to apply for asylum until she was stopped by the police, apparently for jaywalking, and sent to immigration detention. Her family did not pay bail, despite promising to do so. She remained in detention for three months until the Toronto Bail Program assisted her. While she was there the Refugee Law Office provided her advice and she submitted an application for refugee status on October 7, 2009.

[8] She has not seen her ex-partner since 2006 but was advised that he called her mother in Canada in May or June 2009 looking for her. He continues to visit her house in Poland and threaten her relatives there. She collected some documentation of the problems, but her ex-partner stole those papers from her house. She asked her children still in Poland and her youngest child’s guardian to obtain records but they could not. She provided evidence of a Family Court decision from 2009 terminating her and Mr. Poniewierski’s parental rights over their children. Her counsel sent at least four requests to Poland, in English and translated into Polish, with signed consent forms, which did not result in further documentation being provided.

[9] Ms Czesak now lives in difficult circumstances in Toronto and has been assessed by a social worker with the Barbara Schlifer Clinic as withdrawn and possibly traumatized. Doctors’ assessments note that she suffers from back pain, post-traumatic headaches, memory loss, blackouts, depression and probably alcohol dependency.
Contested decision

[10] At the hearing, the panel member accepted that Ms. Czesak had been “abused over a lengthy period of her second marriage” and noted that she had taken into account the Women Refugee Claimants Fearing Gender-Related Persecution guidelines issued by the Chairperson [the “Gender Guidelines”] and the medical reports in making allowances for memory lapses and lack of focus. The determinative issues were delay in claiming, state protection, and internal flight alternative (IFA).

[11] The panel member found that the delay in claiming asylum was inconsistent with a person living in fear of persecution to fail to seek asylum as soon as possible. The claimant’s family may have provided her with poor, and moreover unscrupulous, advice, but she was aware of her illegal status and took no steps to regularize it. The panel drew an adverse inference and found that her credibility was undermined. However, I do not find that the rejection of refugee status is based on delay or the applicant’s general credibility.

[12] The panel member reviewed the law and the applicant’s evidence on state protection. It found that there was insufficient clear and convincing evidence to rebut the presumption that Poland was incapable of protecting its citizens. The panel carried out an extensive review of the evidence on lack of state protection, noting that Poland was making serious efforts to protect women, particularly since joining the European Union, and that there was clear and convincing evidence that these efforts were adequate. Poland had adopted an Act on Counteracting Violence in the Family on November 5, 2005. Prosecutions were being brought against persons convicted of domestic violence who could be sentenced to a maximum five years in prison, although sentences tended to be more lenient. The number of victims’ claims was increasing every year. For the latest statistics in 2007, it was reported that police conducted 81,403 interventions related to domestic violence. Of that number the justice ministry stated that 15,404 were convicted and that at year’s end 4,500 individuals were serving jail sentences for domestic violence crimes, demonstrating that the country acts to combat crime.

[13] Police misconduct was a problem, but was also being addressed. The panel referred to documentary evidence acknowledging that the police could be reluctant to intervene in domestic disputes and that protection for women in abusive situations was sometimes insufficient. However, Poland was making efforts to improve police responsiveness, and although counsel had submitted material from Amnesty International, Freedom House, the European Police Action Centre on Violence Against Women, and the UN Committee on the Elimination of Discrimination Against Women, this documentation was five to seven years old. The panel found that the claimant had provided no persuasive evidence that her ex-partner had connections with the police which could prevent her from accessing state protection.

[14] The panel did not accept the applicant’s explanation of why she had delayed requesting police documents until just prior to the hearing, or her explanation that some reports could not be provided because officers were changing jobs, or her claim that Mr. Poniewierski had stolen documents from her house when he realized she wanted to remain in Canada. The panel similarly found unreasonable her waiting until two weeks prior to the hearing to obtain medical documents, when she had filed her claim for asylum in 2009.

[15] The panel next considered the city of Warsaw, 300-400 kilometres from Ms. Czesak’s former place of residence in Poland, as an Internal Flight Alternative (IFA). The panel again reviewed the extensive jurisprudence governing IFAs, including the insufficiency of arguments that claimants had no friends or family in the region, or could not find suitable work there, or might be better off in Canada economically, physically, or emotionally than they would be in their own country. The claimant testified that her persecutor had family in Warsaw and knew the city well, as he used to work there. However, there was no evidence of a special relationship between Tadeusz and the police in Warsaw that would suggest she would not be accorded police protection if this was requested from Warsaw authorities. The panel concluded that the claimant had not proven that she was at risk to life or of cruel and unusual treatment due to inadequate state protection in the potential IFA area. Accordingly, the panel found that under the circumstances it would not be objectively unreasonable for her to relocate to Warsaw.

[16] The panel member then examined a “compelling reasons” submission of the applicant under section 108 of IRPA. She noted that subparagraph (1)(e) applied to cases in which a person would have been a refugee but the country conditions originally causing this no longer existed.. On that point, the panel concluded that there was no persuasive evidence that conditions in Poland had changed such that the “compelling reasons” exception should apply. The panel nonetheless examined the nature of the claimant’s experiences. It determined that “atrocious” and “appalling” were terms defined in jurisprudence as “extremely savage or wicked” and “shocking, unpleasant”. It decided that the facts in case at hand were not of the same order as the brutal circumstances related in jurisprudence which courts had found constituted a compelling exception.

[17] The panel found that Ms. Czesak was neither a Convention refugee nor a person in need of protection.
Issues

## 24275:2 · paragraphs 18-43

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d23a0a0f1221493964991162983218fdac41a936aac17ab600bc3f1c6b955747`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24275:2:subtheme:1 · paragraphs 18-19

- Raw key terms: `analysis, issues, review, standard, acceptable, analyze, applicable, applicant`
- Display key terms: `analysis, issues, review, standard, acceptable, analyze, applicable`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: analysis, issues, review, standard, acceptable, analyze, applicable Rule/authority context: Standard of review | [19] The standard of review for all six issues is that of reasonableness. Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5141270` offsets `42-48`; context: [18] The applicant cited no less than six issues for the court to determine as follows:
(1) Did the panel err by failing to follow the Chairperson’s Gender Guidelines?
- Evidence: `evidence_fact` cue `evidence` at chunk `5141270` offsets `321-329`; context: (2) Did the panel err in determining that the applicant’s delay in making the claim was a determinative issue, in light of the medical and psychological evidence?
- Evidence: `governing_rule` cue `Standard of review` at chunk `5141270` offsets `634-652`; context: Standard of review
- Evidence: `issue` cue `issues` at chunk `5141271` offsets `40-46`; context: [19] The standard of review for all six issues is that of reasonableness.
- Evidence: `governing_rule` cue `standard of review` at chunk `5141271` offsets `9-27`; context: [19] The standard of review for all six issues is that of reasonableness.

#### 24275:2:subtheme:2 · paragraphs 20-21

- Raw key terms: `applicant, circumstances, condition, medical, particular, abuse, accepted, case`
- Display key terms: `circumstances, condition, medical, particular, abuse, accepted, case`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: circumstances, condition, medical, particular, abuse, accepted, case Application context: [20] I find there to be only one serious issue of contention, relating to whether the IFA in Warsaw is reasonable in light of the applicant’s particular circumstances and her very difficult medical condition. | It was entitled nevertheless to make credibility findings, but in any event I do not conclude that these played a role in the decision. Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5141272` offsets `41-46`; context: [20] I find there to be only one serious issue of contention, relating to whether the IFA in Warsaw is reasonable in light of the applicant’s particular circumstances and her very difficult medical condition.
- Evidence: `reasoning_application` cue `I find` at chunk `5141272` offsets `5-11`; context: [20] I find there to be only one serious issue of contention, relating to whether the IFA in Warsaw is reasonable in light of the applicant’s particular circumstances and her very difficult medical condition.
- Evidence: `evidence_fact` cue `testimony` at chunk `5141273` offsets `267-276`; context: Specific reference was made to them and in the context of this case I am satisfied that the panel was sensitive to the factors which influence the testimony of the applicant who was a victim of persecution.
- Evidence: `reasoning_application` cue `conclude` at chunk `5141273` offsets `501-509`; context: It was entitled nevertheless to make credibility findings, but in any event I do not conclude that these played a role in the decision.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `5141273` offsets `432-444`; context: It was entitled nevertheless to make credibility findings, but in any event I do not conclude that these played a role in the decision.

#### 24275:2:subtheme:3 · paragraphs 22-26

- Raw key terms: `applicant, circumstances, analysis, given, panel, personal, reasonableness, state`
- Display key terms: `circumstances, analysis, given, personal, reasonableness, state`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: circumstances, analysis, given, personal, reasonableness, state Position/evidence statements: [24] The applicant’s counsel argues that it would be particularly unreasonable to remove Ms. Application context: [26] Regarding state protection and an IFA in Warsaw, the panel concluded that state protection would be reasonably forthcoming, which as indicated I find an acceptable conclusion in the circumstances. Evidence spans paragraphs 22-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5141274` offsets `163-168`; context: [22] I also reject the applicant’s contention that the panel erred in its analysis of state protection and IFA in its generalized aspect, apart from the remaining issue of its reasonableness given the applicant’s medical condition.
- Evidence: `evidence_fact` cue `evidence` at chunk `5141274` offsets `298-306`; context: As noted, the panel carried out a careful analysis of the law and evidence on these issues.
- Evidence: `issue` cue `issue` at chunk `5141275` offsets `496-501`; context: The panel’s finding that the objective element of section 96 had not been met disposed of the section 97 issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `5141275` offsets `120-128`; context: There was no evidence of a change in country conditions.
- Evidence: `party_position` cue `argues` at chunk `5141276` offsets `29-35`; context: [24] The applicant’s counsel argues that it would be particularly unreasonable to remove Ms.
- Evidence: `reasoning_application` cue `I find` at chunk `5141278` offsets `148-154`; context: [26] Regarding state protection and an IFA in Warsaw, the panel concluded that state protection would be reasonably forthcoming, which as indicated I find an acceptable conclusion in the circumstances.

#### 24275:2:subtheme:4 · paragraphs 27-29

- Raw key terms: `applicant, panel, warsaw, claimant, conclusion, described, noted, relocate`
- Display key terms: `warsaw, conclusion, described, noted, relocate`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: warsaw, conclusion, described, noted, relocate Application context: I find this conclusion to be reasonable on the basis of the evidence before the panel. Evidence spans paragraphs 27-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5141279` offsets `161-168`; context: The applicant did not know whether she could find work to replace her income from summer farm work in her village, but she did not indicate that she could not work.
- Evidence: `evidence_fact` cue `found that` at chunk `5141279` offsets `526-536`; context: Given the freedom of movement within the country and her past mobility, the panel found that it would not be objectively unreasonable for her to relocate to another city, particularly Warsaw.
- Evidence: `reasoning_application` cue `I find` at chunk `5141279` offsets `636-642`; context: I find this conclusion to be reasonable on the basis of the evidence before the panel.

#### 24275:2:subtheme:5 · paragraphs 30-32

- Raw key terms: `applicant, durish, report, koczorowska, medical, psychological, relation, abuse`
- Display key terms: `durish, report, koczorowska, medical, psychological, relation, abuse`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: durish, report, koczorowska, medical, psychological, relation, abuse Position/evidence statements: [30] The applicant claims that the panel was not transparent on this issue in that it relied upon one line of Dr. Application context: I find that the two-page report is considerably more categorical in its conclusions than Dr. Evidence spans paragraphs 30-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5141282` offsets `69-74`; context: [30] The applicant claims that the panel was not transparent on this issue in that it relied upon one line of Dr.
- Evidence: `party_position` cue `claims` at chunk `5141282` offsets `19-25`; context: [30] The applicant claims that the panel was not transparent on this issue in that it relied upon one line of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5141282` offsets `217-225`; context: Moreover, the panel’s review of the medical evidence was limited to Dr.
- Evidence: `reasoning_application` cue `I find` at chunk `5141284` offsets `121-127`; context: I find that the two-page report is considerably more categorical in its conclusions than Dr.

#### 24275:2:subtheme:6 · paragraphs 33-36

- Raw key terms: `applicant, koczorowska, because, condition, evidence, medical, mother, noted`
- Display key terms: `koczorowska, because, condition, medical, mother, noted`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: koczorowska, because, condition, medical, mother, noted Application context: Koczorowska specifically opines on the very issue of the applicant’s removal to Poland, stating “I believe that she cannot return to Poland because it will for sure cause deterioration in his (sic) condition. | He advised her to reduce her alcohol consumption because of headaches. Operative outcome context: … Therefore I fully support her request to be granted permanent residence in Canada on humanitarian basis. Evidence spans paragraphs 33-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5141285` offsets `63-68`; context: Koczorowska specifically opines on the very issue of the applicant’s removal to Poland, stating “I believe that she cannot return to Poland because it will for sure cause deterioration in his (sic) condition.
- Evidence: `reasoning_application` cue `because` at chunk `5141285` offsets `159-166`; context: Koczorowska specifically opines on the very issue of the applicant’s removal to Poland, stating “I believe that she cannot return to Poland because it will for sure cause deterioration in his (sic) condition.
- Evidence: `disposition` cue `granted` at chunk `5141285` offsets `273-280`; context: … Therefore I fully support her request to be granted permanent residence in Canada on humanitarian basis.
- Evidence: `issue` cue `issues` at chunk `5141286` offsets `774-780`; context: No mention is made in his report of domestic violence, or domestic violence having contributed to her head injury issues.
- Evidence: `evidence_fact` cue `evidence` at chunk `5141286` offsets `65-73`; context: Stachula were also introduced into evidence.
- Evidence: `reasoning_application` cue `because` at chunk `5141286` offsets `339-346`; context: He advised her to reduce her alcohol consumption because of headaches.
- Evidence: `evidence_fact` cue `evidence` at chunk `5141288` offsets `31-39`; context: [36] In light of the foregoing evidence, including that of Dr.
- Evidence: `reasoning_application` cue `conclude` at chunk `5141288` offsets `131-139`; context: Koczorowska, I am satisfied that it was reasonable for the panel to conclude that the evidence regarding the applicant’s medical condition was inconclusive.

#### 24275:2:subtheme:7 · paragraphs 37-38

- Raw key terms: `evidence, forensic, purpose, validation, view, advocate, applicant, apply`
- Display key terms: `forensic, purpose, validation, view, advocate, apply`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: forensic, purpose, validation, view, advocate, apply Rule/authority context: From that experience, the courts have developed what I would describe as a guarded and cautionary view on conclusions of forensic experts which have not undergone a rigorous validation process under court procedures. Application context: This remark would apply to the report of Dr. Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5141289` offsets `354-359`; context: Koczorowska which went as far as to advocate on the applicant’s behalf in the guise of an opinion on the very issue before the panel.
- Evidence: `evidence_fact` cue `evidence` at chunk `5141289` offsets `101-109`; context: [37] Moreover, I am of the view that decision-makers should be wary of reliance upon forensic expert evidence obtained for the purpose of litigation, unless it is subject to some form of validation.
- Evidence: `reasoning_application` cue `apply` at chunk `5141289` offsets `217-222`; context: This remark would apply to the report of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5141290` offsets `121-129`; context: [38] Our legal system has a long experience in dealing with forensic experts testifying on matters relating to technical evidence for the purpose of assisting courts in their determinations.
- Evidence: `governing_rule` cue `under` at chunk `5141290` offsets `384-389`; context: From that experience, the courts have developed what I would describe as a guarded and cautionary view on conclusions of forensic experts which have not undergone a rigorous validation process under court procedures.

#### 24275:2:subtheme:8 · paragraphs 39-43

- Raw key terms: `reports, relation, applicant, circumstances, dismissed, expert, experts, forensic`
- Display key terms: `reports, relation, circumstances, dismissed, expert, experts, forensic`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: reports, relation, circumstances, dismissed, expert, experts, forensic Rule/authority context: Most importantly, courts are provided the opportunity to assess the reliability of the expert opinions under cross-examination by competent lawyers, often under the direction of their own experts. Application context: In my view therefore, unless there is some means to corroborate either the neutrality or lack of self interest of the expert in relation to the litigation process, they generally should be accorded little weight. | [42] I see no basis therefore, to uphold the applicant’s complaint that the panel was selective or erred in failing to consider medical reports in reliance upon its conclusion that “it would not be unreasonable consideri Operative outcome context: [40] This is not to say that every expert report prepared for litigation should be dismissed as having no, or little, weight. | [43] Accordingly, the application is dismissed. Evidence spans paragraphs 39-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5141291` offsets `382-389`; context: The parties are normally entitled to obtain extensive background information on the drafting of the reports, including production of correspondence between lawyers and experts and knowing whether there are other reports in existence not being relied upon.
- Evidence: `governing_rule` cue `under` at chunk `5141291` offsets `687-692`; context: Most importantly, courts are provided the opportunity to assess the reliability of the expert opinions under cross-examination by competent lawyers, often under the direction of their own experts.
- Evidence: `issue` cue `issues` at chunk `5141292` offsets `461-467`; context: But what the court’s experience with forensic experts does suggest in relation to these reports being proffered before administrative tribunals where there exists no defined procedure to allow for their validation, is that caution should be exercised in accepting them at face value, particularly when they propose to settle important issues to be decided by the tribunal.
- Evidence: `reasoning_application` cue `therefore` at chunk `5141292` offsets `510-519`; context: In my view therefore, unless there is some means to corroborate either the neutrality or lack of self interest of the expert in relation to the litigation process, they generally should be accorded little weight.
- Evidence: `disposition` cue `dismissed` at chunk `5141292` offsets `83-92`; context: [40] This is not to say that every expert report prepared for litigation should be dismissed as having no, or little, weight.
- Evidence: `reasoning_application` cue `therefore` at chunk `5141294` offsets `20-29`; context: [42] I see no basis therefore, to uphold the applicant’s complaint that the panel was selective or erred in failing to consider medical reports in reliance upon its conclusion that “it would not be unreasonable considering all the circumstances including those particular to the claimant for her to seek refuge in another city in Poland, particularly Warsaw”.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5141295` offsets `5-16`; context: [43] Accordingly, the application is dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `5141295` offsets `37-46`; context: [43] Accordingly, the application is dismissed.

#### Section text

[18] The applicant cited no less than six issues for the court to determine as follows:
(1) Did the panel err by failing to follow the Chairperson’s Gender Guidelines?
(2) Did the panel err in determining that the applicant’s delay in making the claim was a determinative issue, in light of the medical and psychological evidence?
(3) Did the panel err in finding that there is state protection for victims of domestic violence in Poland?
(4) Did the panel err in its IFA analysis?
(5) Did the panel err in finding section 108(4) to be not applicable?
(6) Did the panel err in failing to analyze the section 97 risk to the applicant?
Standard of review

[19] The standard of review for all six issues is that of reasonableness. This denotes a deferential standard towards the decision-maker. The decision will be reasonable where the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law (see Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190, at paragraph 47).
Analysis

[20] I find there to be only one serious issue of contention, relating to whether the IFA in Warsaw is reasonable in light of the applicant’s particular circumstances and her very difficult medical condition.

[21] With respect to the other submissions, firstly I reject the submission that the RPD ignored the Gender Guidelines. Specific reference was made to them and in the context of this case I am satisfied that the panel was sensitive to the factors which influence the testimony of the applicant who was a victim of persecution. The panel accepted that she was a victim of abuse and took that into full consideration. It was entitled nevertheless to make credibility findings, but in any event I do not conclude that these played a role in the decision. By and large, the particular circumstances of the claimant relate to her medical condition, which is determined by doctors’ reports and the past living conditions of the claimant.

[22] I also reject the applicant’s contention that the panel erred in its analysis of state protection and IFA in its generalized aspect, apart from the remaining issue of its reasonableness given the applicant’s medical condition. As noted, the panel carried out a careful analysis of the law and evidence on these issues. There was ample evidence to support its conclusions that state protection was available in Poland generally and that a reasonable IFA was available to the applicant in Warsaw in respect of her protection from persecution.

[23] Similarly, I reject the applicant’s arguments with respect to the applicability of subsection 108(4). There was no evidence of a change in country conditions. Additionally, the applicant’s circumstances failed to meet the exceptional level of compelling reasons required for this provision. Similarly, the argument relating to the absence of a separate section 97 analysis is rejected. The panel’s finding that the objective element of section 96 had not been met disposed of the section 97 issue. See Balakumar v Canada (MCI), 2008 FC 20 at para 13; Kaleja v Canada (MCI), 2011 FC 668 at para 34.
Reasonableness of the IFA Given the Personal Circumstances of the Applicant

[24] The applicant’s counsel argues that it would be particularly unreasonable to remove Ms. Czesak to Warsaw in light of her precarious mental state as described by her doctors. This apprehension is related to concerns about a serious possibility of the applicant being persecuted no matter where she lived in Poland. The applicant argues that given her personal circumstances, it would be unreasonable for her to seek refuge in a place outside of the village where she had previously lived while residing in Poland.

[25] In Syvyryn v MCI, 2009 FC 1027, Justice Snider reiterated that domestic violence engages the Gender Guidelines and that an analysis needs to take into account the applicant’s age, gender and personal circumstances in considering the reasonableness of an IFA.

[26] Regarding state protection and an IFA in Warsaw, the panel concluded that state protection would be reasonably forthcoming, which as indicated I find an acceptable conclusion in the circumstances.

[27] The panel also noted that the claimant had previously received social assistance and presumably could obtain the same in Warsaw. The applicant did not know whether she could find work to replace her income from summer farm work in her village, but she did not indicate that she could not work. In terms of support, the panel noted that the applicant was able to come to a foreign country and had little or no support from her family here. Given the freedom of movement within the country and her past mobility, the panel found that it would not be objectively unreasonable for her to relocate to another city, particularly Warsaw. I find this conclusion to be reasonable on the basis of the evidence before the panel.

[28] However, the applicant takes particular exception to the panel’s conclusion that the applicant’s mental state as described by her doctors, did not make it unreasonable for her to relocate to Warsaw.

[29] In its reasons, the panel accepted that the claimant was abused, but noted that psychological intervention could be accessed in Warsaw. Similarly, the panel expressly stated that it considered counsel’s submissions, as well as the medical report of Dr. Durish, which it described as inconclusive, including with respect to a diagnosis of the applicant suffering from Post-Traumatic Stress Disorder.

[30] The applicant claims that the panel was not transparent on this issue in that it relied upon one line of Dr. Durish’s report while ignoring the totality of the report. Moreover, the panel’s review of the medical evidence was limited to Dr. Durish‘s report. Significantly, it failed to mention or consider other medical reports, particularly that of Dr. Maria Koczorowska, a medical psychiatrist.

[31] With regard to these allegations, I am satisfied that Dr. Durish’s report may be described as inconclusive in respect of the applicant’s psychological state in many regards, and not just in relation to her PTSD symptoms. The report speaks to concerns about significant substance abuse, and notes that the applicant somaticizes her trauma symptoms to a significant degree, as well as finding it very difficult to assess her intellectual functioning. It is noted that Dr. Durish’s area of clinical expertise is in the assessment and treatment of trauma, for which she has received considerable postgraduate and professional training.

[32] In relation to Dr. Koczorowska’s report, it states that the applicant was initially seen commencing April 19, 2012. I find that the two-page report is considerably more categorical in its conclusions than Dr. Durish’s report. Dr. Koczorowska describes the applicant as suffering from a severe psychomotor retardation with a diagnosis of major depressive disorder, posttraumatic stress disorder associated with general medical condition and psychological factors linked to post-concussion syndrome.

[33] Moreover, Dr. Koczorowska specifically opines on the very issue of the applicant’s removal to Poland, stating “I believe that she cannot return to Poland because it will for sure cause deterioration in his (sic) condition.… Therefore I fully support her request to be granted permanent residence in Canada on humanitarian basis.” [Emphasis added]

[34] Medical reports from Dr. Stachula were also introduced into evidence. He initially treated the applicant in 2008 when she was involved in a motor vehicle accident. In his summary report of March 21, 2011, he noted that the applicant complained of low back pain and migraine headaches. He advised her to reduce her alcohol consumption because of headaches. He concluded that the patient definitely suffered from a grief reaction after her mother’s death. His view was that her posttraumatic headaches related to her head injury. He states that she apparently was in good health before the accident, but after it took pain and anxiety medication regularly. No mention is made in his report of domestic violence, or domestic violence having contributed to her head injury issues.

[35] It is to be noted that Dr. Koczorowska also indicated that the applicant was doing well until detained by immigration authorities and that her symptoms got worse after her mother died, since which time she had been struggling.

[36] In light of the foregoing evidence, including that of Dr. Koczorowska, I am satisfied that it was reasonable for the panel to conclude that the evidence regarding the applicant’s medical condition was inconclusive.

[37] Moreover, I am of the view that decision-makers should be wary of reliance upon forensic expert evidence obtained for the purpose of litigation, unless it is subject to some form of validation. This remark would apply to the report of Dr. Koczorowska which went as far as to advocate on the applicant’s behalf in the guise of an opinion on the very issue before the panel.

[38] Our legal system has a long experience in dealing with forensic experts testifying on matters relating to technical evidence for the purpose of assisting courts in their determinations. From that experience, the courts have developed what I would describe as a guarded and cautionary view on conclusions of forensic experts which have not undergone a rigorous validation process under court procedures.

[39] Some of these procedures intended to validate expert opinions include the early exchange of reports, by which I mean that normally there is a rebuttal report as a first line of validation. The parties are normally entitled to obtain extensive background information on the drafting of the reports, including production of correspondence between lawyers and experts and knowing whether there are other reports in existence not being relied upon. These procedures are further enhanced by the right to question opposing parties in discovery in relation to issues raised in reports. Most importantly, courts are provided the opportunity to assess the reliability of the expert opinions under cross-examination by competent lawyers, often under the direction of their own experts. In some cases, decision-makers will even involve neutral experts to assist resolution of more controversial points of opposing forensic experts.

[40] This is not to say that every expert report prepared for litigation should be dismissed as having no, or little, weight. But what the court’s experience with forensic experts does suggest in relation to these reports being proffered before administrative tribunals where there exists no defined procedure to allow for their validation, is that caution should be exercised in accepting them at face value, particularly when they propose to settle important issues to be decided by the tribunal. In my view therefore, unless there is some means to corroborate either the neutrality or lack of self interest of the expert in relation to the litigation process, they generally should be accorded little weight.

[41] In this matter, the reports of Drs. Durish and Stachula I would think exhibit more of the required imprimatur of reliability, by the circumstances of the timing and of their involvement with the applicant and their more neutral and objective relation of conditions and guarded opinions that suggest reasonable limits on their diagnoses and prognoses of the applicant’s condition.

[42] I see no basis therefore, to uphold the applicant’s complaint that the panel was selective or erred in failing to consider medical reports in reliance upon its conclusion that “it would not be unreasonable considering all the circumstances including those particular to the claimant for her to seek refuge in another city in Poland, particularly Warsaw”.

[43] Accordingly, the application is dismissed.


## 24275:3 · paragraphs 44-45

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a26f47f3ad1d6df443d207de8c16b3b724be1cdc863c2db94b4a1984d6ed3a8d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24275:3:subtheme:1 · paragraphs 44-45

- Raw key terms: `annis, application, cause, certified, citizenship, court, czesak, czeslawa`
- Display key terms: `annis, certified, czesak, czeslawa`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: annis, certified, czesak, czeslawa Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that the application is dismissed, and no serious question of general importance is certified. Evidence spans paragraphs 44-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5141295` offsets `132-140`; context: JUDGMENT
THIS COURT’S JUDGMENT is that the application is dismissed, and no serious question of general importance is certified.
- Evidence: `disposition` cue `dismissed` at chunk `5141295` offsets `106-115`; context: JUDGMENT
THIS COURT’S JUDGMENT is that the application is dismissed, and no serious question of general importance is certified.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that the application is dismissed, and no serious question of general importance is certified.
"Peter Annis"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-9539-12
STYLE OF CAUSE:
MARIA CZESAK (a.k.a.) MARIA CZESLAWA CZESAK) v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
October 16, 2013
REASONS FOR 

## 24275:4 · paragraphs 46-46

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `29e060d98ef86c8d6384f940a4a30378c723873eb7288bc494bf942151cadada`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24275:4:subtheme:1 · paragraphs 46-46

- Raw key terms: `annis, appearances, applicant, attorney, barristers, canada, dated, deputy`
- Display key terms: `annis, barristers, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: annis, barristers, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 46-46. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND JUDGMENT:
ANNIS J.
DATED:
november 14, 2013
APPEARANCES:
Preevanda K Sapru
For The Applicant
Tamrat Gebeyehu
For The Respondent
SOLICITORS OF RECORD:
Preevanda K Sapru
Barristers & Solicitors
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
