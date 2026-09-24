# Discussion Units: case 26616

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **71**
- Continuity pairs: **70**
- Discussion Units: **6**
- Paragraph source hashes: **71**
- Sub-themes: **21**

## 26616:1 · paragraphs 0-0

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `af505e532ab2d3c9897e2b926fc6d377578dcad830a2fc6d4f85401b0deaab8f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26616:1:subtheme:1 · paragraphs 0-0

- Raw key terms: `applicant, bethany, canada, citation, citizenship, content, court, database`
- Display key terms: `bethany, citation, content, database`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: bethany, citation, content, database No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 0-0. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

Smith v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2012-11-02
Neutral citation
2012 FC 1283
File numbers
IMM-5699-11
Notes
Digest
Decision Content
Date: 20121102
Docket: IMM-5699-11
Citation: 2012 FC 1283
Ottawa, Ontario, November 2, 2012
PRESENT: The Honourable Mr. Justice Mosley
BETWEEN:
BETHANY LANAE SMITH
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

## 26616:2 · paragraphs 1-12

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3467e240b18a6caf365d5b5c3a3508d20eec3597674ade82ef57a5034d5de7b2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26616:2:subtheme:1 · paragraphs 1-5

- Raw key terms: `says, applicant, orientation, sexual, smith, superiors, another, army`
- Display key terms: `says, orientation, sexual, smith, superiors, another, army`
- Argument roles: `evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position, reasoning_application Display terms: says, orientation, sexual, smith, superiors, another, army Position/evidence statements: She does not claim to be a conscientious objector but did not want to be placed in an area of combat operations. Rule/authority context: This is her application for judicial review of the second decision, brought under section 72 of the Immigration and Refugee Protection Act, SC 2001, c 27 (hereafter IRPA). Application context: She sought protection in Canada from alleged persecution and the alleged threat of physical harm from her peers and superiors in the Army because of her sexual orientation. Evidence spans paragraphs 1-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `5251089` offsets `378-388`; context: In two decisions, the Immigration and Refugee Board, Refugee Protection Division, found that she is not a Convention refugee or a person in need of protection.
- Evidence: `governing_rule` cue `under` at chunk `5251089` offsets `532-537`; context: This is her application for judicial review of the second decision, brought under section 72 of the Immigration and Refugee Protection Act, SC 2001, c 27 (hereafter IRPA).
- Evidence: `reasoning_application` cue `because` at chunk `5251089` offsets `261-268`; context: She sought protection in Canada from alleged persecution and the alleged threat of physical harm from her peers and superiors in the Army because of her sexual orientation.
- Evidence: `party_position` cue `claim` at chunk `5251092` offsets `560-565`; context: She does not claim to be a conscientious objector but did not want to be placed in an area of combat operations.

#### 26616:2:subtheme:2 · paragraphs 6-10

- Raw key terms: `board, applicant, claim, decision, evidence, protection, state, afforded`
- Display key terms: `protection, state, afforded`
- Argument roles: `disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue Display terms: protection, state, afforded Rule/authority context: DECISION UNDER REVIEW: Operative outcome context: The claim was denied by the Refugee Protection Division (hereafter “the Board”) in February 2009 on the grounds that the applicant had not established a serious risk of persecution or rebutted the presumption of state pr Evidence spans paragraphs 6-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5251094` offsets `572-579`; context: Justice de Montigny found that the Board Member had erred in several respects in determining whether the applicant had an objective basis for her fear of persecution and in determining whether state protection would be afforded her.
- Evidence: `evidence_fact` cue `found that` at chunk `5251094` offsets `499-509`; context: Justice de Montigny found that the Board Member had erred in several respects in determining whether the applicant had an objective basis for her fear of persecution and in determining whether state protection would be afforded her.
- Evidence: `disposition` cue `denied` at chunk `5251094` offsets `118-124`; context: The claim was denied by the Refugee Protection Division (hereafter “the Board”) in February 2009 on the grounds that the applicant had not established a serious risk of persecution or rebutted the presumption of state protection.
- Evidence: `issue` cue `question` at chunk `5251095` offsets `203-211`; context: At this hearing, the Minister of Public Safety and Emergency Preparedness intervened to present evidence, question the claimant and make submissions.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251095` offsets `193-201`; context: At this hearing, the Minister of Public Safety and Emergency Preparedness intervened to present evidence, question the claimant and make submissions.
- Evidence: `governing_rule` cue `UNDER` at chunk `5251096` offsets `405-410`; context: DECISION UNDER REVIEW:
- Evidence: `evidence_fact` cue `evidence` at chunk `5251097` offsets `181-189`; context: [9] At the outset of his extensive reasons for decision, the Board Member discussed the process that was followed at the hearing to ensure that the claimant could fully present her evidence in a calm and reassuring atmosphere.
- Evidence: `evidence_fact` cue `testimony` at chunk `5251098` offsets `178-187`; context: The credibility findings were based on alleged inconsistencies in the applicant’s testimony and her PIF, on the vagueness of some of her answers, the lack of evidence in support of her claim, and the lack of explanations of certain situations, mainly regarding why she did not seek help.

#### 26616:2:subtheme:3 · paragraphs 11-12

- Raw key terms: `applicant, board, credibility, found, testimony, account, acquire, advanced`
- Display key terms: `credibility, testimony, account, acquire, advanced`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: credibility, testimony, account, acquire, advanced Application context: [11] The Board found that the applicant’s credibility was undermined with respect to whether she had experienced harassment during her advanced individual training because of conflicts between her Personal Information Fo Evidence spans paragraphs 11-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5251099` offsets `85-92`; context: [11] The Board found that the applicant’s credibility was undermined with respect to whether she had experienced harassment during her advanced individual training because of conflicts between her Personal Information Form (“PIF”) and her testimony.
- Evidence: `evidence_fact` cue `found that` at chunk `5251099` offsets `15-25`; context: [11] The Board found that the applicant’s credibility was undermined with respect to whether she had experienced harassment during her advanced individual training because of conflicts between her Personal Information Form (“PIF”) and her testimony.
- Evidence: `reasoning_application` cue `because` at chunk `5251099` offsets `164-171`; context: [11] The Board found that the applicant’s credibility was undermined with respect to whether she had experienced harassment during her advanced individual training because of conflicts between her Personal Information Form (“PIF”) and her testimony.
- Evidence: `evidence_fact` cue `testimony` at chunk `5251100` offsets `301-310`; context: It did not find the testimony of the applicant and her documentary and expert evidence to be trustworthy and convincing evidence.

#### Section text

[1] The applicant, Ms. Bethany Smith, is a 23 year-old American citizen, a member of the United States Army and a lesbian. She sought protection in Canada from alleged persecution and the alleged threat of physical harm from her peers and superiors in the Army because of her sexual orientation. In two decisions, the Immigration and Refugee Board, Refugee Protection Division, found that she is not a Convention refugee or a person in need of protection. This is her application for judicial review of the second decision, brought under section 72 of the Immigration and Refugee Protection Act, SC 2001, c 27 (hereafter IRPA).
BACKGROUND:

[2] The applicant disclosed her sexual orientation while in high school. At the age of 18, in October 2006, she was recruited into the US Army as a mechanic. She did not disclose her orientation at that time and says she did not know how gays and lesbians were treated by the Army prior to joining it. Ms. Smith alleges that during advanced training and following posting to her unit at Fort Campbell, Kentucky, she was harassed, mentally and physically abused, and threatened.

[3] Matters became worse when she was seen holding hands with another woman off-base. She says that she received threatening notes (over 100 in five months) but showed them to no one as she believed she could not trust anyone, including her superiors whom she viewed as complicit in her persecution.

[4] The applicant says that she tried to be discharged by telling her superiors about her sexual orientation, but to no avail. When her superiors became aware of the situation, she says they started treating her harshly and giving her assignments that were incompatible with her physical abilities. She says that she was warned by a superior to tone down her personal life and to stop attracting attention to herself. She says that her superiors did not want to discharge her until after she had been deployed to and served a tour in Afghanistan. She does not claim to be a conscientious objector but did not want to be placed in an area of combat operations.

[5] Ms. Smith says that on September 9, 2007, fearing that her life was in danger, she fled from the base with another soldier. After she left the base she says she received a call threatening to “kick a hole in her face” and a text message saying she should be killed by a firing squad for having deserted.

[6] The applicant entered Canada on September 11, 2007 and filed her refugee claim on October 16, 2007. The claim was denied by the Refugee Protection Division (hereafter “the Board”) in February 2009 on the grounds that the applicant had not established a serious risk of persecution or rebutted the presumption of state protection. An application for judicial review was granted by Justice de Montigny in Smith v Canada (Minister of Citizenship and Immigration), 2009 FC 1194. Justice de Montigny found that the Board Member had erred in several respects in determining whether the applicant had an objective basis for her fear of persecution and in determining whether state protection would be afforded her.

[7] Upon redetermination, the Board conducted a new hearing on August 11-12 and October 8, 2010. At this hearing, the Minister of Public Safety and Emergency Preparedness intervened to present evidence, question the claimant and make submissions. In a decision rendered on June 6, 2011, the Board again rejected the claim. That decision is the subject of this application.

[8] The applicant says that if she returns to the US, she will be court-martialled, will not be given a fair trial and will be punished for trying to leave an environment where her life was in danger. She says that the process by which she would be prosecuted and punished does not constitute a fair and independent judicial determination and thus, state protection would not be afforded to her.
DECISION UNDER REVIEW:

[9] At the outset of his extensive reasons for decision, the Board Member discussed the process that was followed at the hearing to ensure that the claimant could fully present her evidence in a calm and reassuring atmosphere. The Member indicated that he had carefully read and considered the Chairperson’s Guideline 4 - Women Refugee Claimants Fearing Gender-Related Persecution (hereafter the Gender Guideline), the United Nations High Commissioner for Refugees Guidance Note on refugee claims relating to sexual orientation and gender identity (hereafter the UNHCR Guidance Note), and a presentation and article by Professor Nicole LaViolette: Sexual Orientation, Gender Identity and the Refugee Determination Process, (Ottawa: Immigration and Refugee Board, March 2010) [LaViolette 2010], and Nicole LaViolette, “Independent human rights documentation and sexual minorities: an ongoing challenge for the Canadian refugee determination process” (2009) 13 Int’l JHR 437 [LaViolette 2009].

[10] The Board rejected the applicant’s claim on two grounds: credibility and state protection. The credibility findings were based on alleged inconsistencies in the applicant’s testimony and her PIF, on the vagueness of some of her answers, the lack of evidence in support of her claim, and the lack of explanations of certain situations, mainly regarding why she did not seek help.

[11] The Board found that the applicant’s credibility was undermined with respect to whether she had experienced harassment during her advanced individual training because of conflicts between her Personal Information Form (“PIF”) and her testimony. Discrepancies in the applicant’s testimony with respect to her experience while at Fort Campbell were found to have undermined her credibility: when and how her peers found out about her sexual orientation; what she might or might not have told a female doctor about assaults against her person; whether she was indeed harassed; whether her superiors knew about her harassment; whether she asked to be discharged on the ground of her sexual orientation; and what made her leave Fort Campbell. The Board also found that the applicant could have applied for and obtained a discharge from military service based on her sexual orientation after her arrival in Canada.

[12] The Board summarised the applicable law with regards to state protection. It noted that the US is a constitutional democracy with stable institutions. The Board took into account its conclusions on the applicant’s credibility in determining the existence of state protection. It did not find the testimony of the applicant and her documentary and expert evidence to be trustworthy and convincing evidence. The Board instead preferred the evidence of the one expert provided by the Minister’s counsel. It found that it would not have been unreasonable for the applicant to take further steps to acquire the protection of her state.

## 26616:3 · paragraphs 13-16

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `936b51bafdbe6f70085600046514240b93d992303166c82e78184cce2861b3d3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26616:3:subtheme:1 · paragraphs 13-15

- Raw key terms: `applicant, board, found, military, concluded, different, discharged, ground`
- Display key terms: `military, concluded, different, discharged, ground`
- Argument roles: `evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, reasoning_application Display terms: military, concluded, different, discharged, ground Rule/authority context: [15] The Board also considered the effect of the repeal of the “Don’t Ask, Don’t Tell” policy, which occurred while the decision was under reserve, as a change of circumstances undermining the opinion evidence presented  Application context: The Board declined to consider the Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982, being Schedule B to the Canada Act 1982 (UK), 1982, c 11 (hereafter the Charter) and the Convention for th Evidence spans paragraphs 13-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `5251101` offsets `15-25`; context: [13] The Board found that the applicant could have sought further assistance from the US military (considering the Don’t Harass Policy and the Uniform Code of Military Justice, 10 USC, Ch.
- Evidence: `evidence_fact` cue `found that` at chunk `5251102` offsets `304-314`; context: The Board also found that the military justice system of the US was adequate.
- Evidence: `reasoning_application` cue `because` at chunk `5251102` offsets `784-791`; context: The Board declined to consider the Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982, being Schedule B to the Canada Act 1982 (UK), 1982, c 11 (hereafter the Charter) and the Convention for the Protection of Human Rights and Fundamental Freedoms, 4 November 1950, 213 UNTS 221 at 223, Eur TS 5, CETS 5 [European Convention of Human Rights] for the purpose of its state protection analysis because those instruments were not applicable to US laws.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251103` offsets `201-209`; context: [15] The Board also considered the effect of the repeal of the “Don’t Ask, Don’t Tell” policy, which occurred while the decision was under reserve, as a change of circumstances undermining the opinion evidence presented by the applicant.
- Evidence: `governing_rule` cue `under` at chunk `5251103` offsets `133-138`; context: [15] The Board also considered the effect of the repeal of the “Don’t Ask, Don’t Tell” policy, which occurred while the decision was under reserve, as a change of circumstances undermining the opinion evidence presented by the applicant.

#### 26616:3:subtheme:2 · paragraphs 16-16

- Raw key terms: `adequate, analysis, applicant, board, claimant, consider, context, credibility`
- Display key terms: `adequate, analysis, consider, context, credibility`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: adequate, analysis, consider, context, credibility Evidence spans paragraphs 16-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `5251104` offsets `364-370`; context: ISSUES:
- Evidence: `evidence_fact` cue `evidence` at chunk `5251104` offsets `309-317`; context: [16] The applicant says that, in reaching his decision, the Board Member erred by making unreasonable negative credibility findings without sensitivity to the context the claimant found herself in, erred in failing to provide adequate reasons or analysis, made erroneous findings of fact not supported by the evidence and failed to properly consider the evidence.

#### Section text

[13] The Board found that the applicant could have sought further assistance from the US military (considering the Don’t Harass Policy and the Uniform Code of Military Justice, 10 USC, Ch. 47 (hereafter the UCMJ)) and that she could have made further steps to be discharged on the ground of her orientation. The Board also found that the applicant could have moved to a different city and attempted to clarify the situation with the US military, with the help of a non-governmental organization or a lawyer if necessary. The Board concluded that on a balance of probabilities the applicant did not rebut the presumption of state protection and that the applicant did not take all reasonable steps to obtain state protection.

[14] The Board concluded that if the applicant were to be arrested upon return to the USA, the prosecution that would result would not amount to persecution as she would be in no different position than any other member of the military charged with absence without leave and/or desertion. The Board also found that the military justice system of the US was adequate. The Board declined to consider the Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982, being Schedule B to the Canada Act 1982 (UK), 1982, c 11 (hereafter the Charter) and the Convention for the Protection of Human Rights and Fundamental Freedoms, 4 November 1950, 213 UNTS 221 at 223, Eur TS 5, CETS 5 [European Convention of Human Rights] for the purpose of its state protection analysis because those instruments were not applicable to US laws.

[15] The Board also considered the effect of the repeal of the “Don’t Ask, Don’t Tell” policy, which occurred while the decision was under reserve, as a change of circumstances undermining the opinion evidence presented by the applicant. The US military was subject to the” Don’t Ask, Don’t Tell” policy, enacted as US federal law, from 1993 to September 2011. Under that policy, discrimination and harassment on the ground of sexual orientation were prohibited but openly gay, lesbian or bisexual persons were discharged from duty on the theory that such relationships were incompatible with military service. The law prohibited inquiries (the “don’t ask” part) or disclosure (“don’t tell”) about homosexual or bisexual orientation and relationships. The statute (10 USC § 654) was found to be unconstitutional by the US District Court in September 2010. A bill to repeal the policy was enacted by Congress in December 2010 and brought into force in September 2011.

[16] The applicant says that, in reaching his decision, the Board Member erred by making unreasonable negative credibility findings without sensitivity to the context the claimant found herself in, erred in failing to provide adequate reasons or analysis, made erroneous findings of fact not supported by the evidence and failed to properly consider the evidence.
ISSUES:

## 26616:4 · paragraphs 17-67

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9cc74912d41c1594889e055a75088a17d3aba9e0b252301746b5b2e327499fda`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26616:4:subtheme:1 · paragraphs 17-18

- Raw key terms: `credibility, issues, protection, standard, state, against, analysis, application`
- Display key terms: `credibility, issues, protection, standard, state, against, analysis`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: credibility, issues, protection, standard, state, against, analysis Rule/authority context: ANALYSIS: Standard of review; | [18] The prior jurisprudence has satisfactorily determined the standard to be applied to the issues in this matter which are questions of fact or of mixed fact and law. Application context: Did the Board err in failing to apply the Charter and international human rights instruments in its state protection analysis? | [18] The prior jurisprudence has satisfactorily determined the standard to be applied to the issues in this matter which are questions of fact or of mixed fact and law. Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5251105` offsets `9-15`; context: [17] The issues raised on this application are as follows:
1.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251105` offsets `290-298`; context: Did the Board disregard important expert evidence?
- Evidence: `governing_rule` cue `Standard of review` at chunk `5251105` offsets `372-390`; context: ANALYSIS:
Standard of review;
- Evidence: `reasoning_application` cue `apply` at chunk `5251105` offsets `151-156`; context: Did the Board err in failing to apply the Charter and international human rights instruments in its state protection analysis?
- Evidence: `issue` cue `issues` at chunk `5251106` offsets `93-99`; context: [18] The prior jurisprudence has satisfactorily determined the standard to be applied to the issues in this matter which are questions of fact or of mixed fact and law.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5251106` offsets `15-28`; context: [18] The prior jurisprudence has satisfactorily determined the standard to be applied to the issues in this matter which are questions of fact or of mixed fact and law.
- Evidence: `reasoning_application` cue `applied` at chunk `5251106` offsets `78-85`; context: [18] The prior jurisprudence has satisfactorily determined the standard to be applied to the issues in this matter which are questions of fact or of mixed fact and law.

#### 26616:4:subtheme:2 · paragraphs 19-25

- Raw key terms: `board, applicant, based, credibility, evidence, findings, contradictions, adverse`
- Display key terms: `based, credibility, findings, contradictions, adverse`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: based, credibility, findings, contradictions, adverse Position/evidence statements: [21] The applicant contends that the Board’s credibility findings are erroneous for several reasons: they are contrary to the Board’s 2009 decision which was made closer in time to the incidents underlying the refugee cl | [22] The applicant argues that the Board did not evaluate the plausibility of her story in light of the extensive documentary and opinion evidence submitted on the situation of homosexuals in the US military. Application context: She contends that the Board failed to properly apply the Gender Guideline and the UNHCR Guidance Note in its analysis. | She told no one about it because only a week remained in her training and it was unlikely that anything would be done prior to her departure. Evidence spans paragraphs 19-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5251107` offsets `136-143`; context: [19] Reasonableness is based on the existence of justification, transparency and intelligibility within the decision-making process and whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law: Dunsmuir, above, at para 47; and Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 59.
- Evidence: `evidence_fact` cue `testimony` at chunk `5251108` offsets `129-138`; context: [20] The Board based its principal adverse credibility findings on three points: contradictions between the applicant’s previous testimony in 2008, the narrative in her PIF and her testimony in the 2010 hearings; implausibilities in her evidence; and an inability to answer certain questions related to asserted memory problems.
- Evidence: `party_position` cue `contends` at chunk `5251109` offsets `19-27`; context: [21] The applicant contends that the Board’s credibility findings are erroneous for several reasons: they are contrary to the Board’s 2009 decision which was made closer in time to the incidents underlying the refugee claim and in which the Board did not make an adverse credibility finding; the findings are based on ordinary memory problems such as an inability to recall the names of individuals; the inconsistencies relied upon do not amount to serious or significant contradictions; they conflate recollections of several events; different descriptions of harassment were improperly characterized as inconsistent; and the Board engaged in microscopic examination of the applicant’s evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251109` offsets `687-695`; context: [21] The applicant contends that the Board’s credibility findings are erroneous for several reasons: they are contrary to the Board’s 2009 decision which was made closer in time to the incidents underlying the refugee claim and in which the Board did not make an adverse credibility finding; the findings are based on ordinary memory problems such as an inability to recall the names of individuals; the inconsistencies relied upon do not amount to serious or significant contradictions; they conflate recollections of several events; different descriptions of harassment were improperly characterized as inconsistent; and the Board engaged in microscopic examination of the applicant’s evidence.
- Evidence: `party_position` cue `argues` at chunk `5251110` offsets `19-25`; context: [22] The applicant argues that the Board did not evaluate the plausibility of her story in light of the extensive documentary and opinion evidence submitted on the situation of homosexuals in the US military.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251110` offsets `138-146`; context: [22] The applicant argues that the Board did not evaluate the plausibility of her story in light of the extensive documentary and opinion evidence submitted on the situation of homosexuals in the US military.
- Evidence: `reasoning_application` cue `apply` at chunk `5251110` offsets `256-261`; context: She contends that the Board failed to properly apply the Gender Guideline and the UNHCR Guidance Note in its analysis.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251111` offsets `476-484`; context: However, if the evidence before the Board does not support the credibility findings, or if the contradictions or implausibilities relied upon by the Board are insignificant and do not relate to the claim, this Court should intervene.
- Evidence: `counterargument_limitation` cue `However` at chunk `5251111` offsets `460-467`; context: However, if the evidence before the Board does not support the credibility findings, or if the contradictions or implausibilities relied upon by the Board are insignificant and do not relate to the claim, this Court should intervene.
- Evidence: `evidence_fact` cue `testimony` at chunk `5251112` offsets `244-253`; context: [24] In this matter, some of the alleged inconsistencies identified by the Board relate to events that the applicant described in her PIF, remembered in greater detail in the first hearing (in November 2008) and was unable to recall during her testimony in the second series of hearings (in August and November 2010).
- Evidence: `counterargument_limitation` cue `however` at chunk `5251112` offsets `447-454`; context: In this case, however, the differences were more pronounced.
- Evidence: `reasoning_application` cue `because` at chunk `5251113` offsets `433-440`; context: She told no one about it because only a week remained in her training and it was unlikely that anything would be done prior to her departure.

#### 26616:4:subtheme:3 · paragraphs 26-27

- Raw key terms: `applicant, asked, because, board, given, member, name, orientation`
- Display key terms: `asked, because, given, name, orientation`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: asked, because, given, name, orientation Rule/authority context: The applicant gave the same explanation when asked why she had not contacted the Army from Canada to request a discharge by reason of her orientation under the Don’t Ask, Don’t Tell policy while it was still in effect. Application context: She explained that she preferred not to remember the soldiers’ names because it was a difficult time in her life. | She could not remember whether he had verbally abused her but assumed that the physical abuse was because he had discovered that she was a lesbian. Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5251114` offsets `540-547`; context: In his analysis, the Board Member considered whether that was a reasonable response, in light of the Chairperson’s Gender Guideline, given that no evidence had been presented that the applicant suffered from a psychological disorder or had been the victim of sexual violence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251114` offsets `90-98`; context: [26] The Member carefully reviewed several other areas of difficulty with the applicant’s evidence.
- Evidence: `reasoning_application` cue `because` at chunk `5251114` offsets `450-457`; context: She explained that she preferred not to remember the soldiers’ names because it was a difficult time in her life.
- Evidence: `issue` cue `whether` at chunk `5251115` offsets `146-153`; context: She could not remember whether he had verbally abused her but assumed that the physical abuse was because he had discovered that she was a lesbian.
- Evidence: `governing_rule` cue `under` at chunk `5251115` offsets `1018-1023`; context: The applicant gave the same explanation when asked why she had not contacted the Army from Canada to request a discharge by reason of her orientation under the Don’t Ask, Don’t Tell policy while it was still in effect.
- Evidence: `reasoning_application` cue `because` at chunk `5251115` offsets `221-228`; context: She could not remember whether he had verbally abused her but assumed that the physical abuse was because he had discovered that she was a lesbian.

#### 26616:4:subtheme:4 · paragraphs 28-34

- Raw key terms: `member, applicant, board, evidence, conclusion, canada, charter, credibility`
- Display key terms: `conclusion, charter, credibility`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: conclusion, charter, credibility Position/evidence statements: [33] The applicant contends that the Board Member erred in law when he declined to apply the Canadian Charter of Rights and Freedoms and international legal instruments as sources of law to evaluate the availability of s | [34] The applicant submits that the Member’s analysis was in error given the direction in s 3 of the IRPA that the Act is to be construed and applied in a manner that furthers domestic and international interests. Rule/authority context: This, the applicant argues, led to the Member’s decision not to rely upon the expert evidence relating to state protection under the US system. | In particular, it requires that decisions taken under the Act be consistent with the Charter and comply with the international human rights instruments to which Canada is signatory. Application context: Did the Board err in failing to apply the Charter and international human rights instruments in its state protection analysis? | [33] The applicant contends that the Board Member erred in law when he declined to apply the Canadian Charter of Rights and Freedoms and international legal instruments as sources of law to evaluate the availability of s Evidence spans paragraphs 28-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `However` at chunk `5251116` offsets `198-205`; context: However he did not understand why she had not used the notes to tell someone in the line of authority at her base about what was happening.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251117` offsets `45-53`; context: [29] When confronted with the expert opinion evidence on remedies available to US military personnel at the time – zero tolerance policies towards harassment and UCMJ provisions against assault, military attorney services, the possibility of declaring a homosexual orientation, whistle-blower protections for complaining to the Inspector General, the possibility of contacting a member of Congress – the applicant explained that as a nineteen-year old private she was not aware of any of these remedies.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251118` offsets `547-555`; context: This conclusion was open to him based on the conflict in the evidence presented.
- Evidence: `evidence_fact` cue `testimony` at chunk `5251119` offsets `65-74`; context: [31] Before coming to the overall conclusion that the claimant’s testimony was not plausible, the Board Member noted that he had considered the recommendation to exercise caution in LaViolette 2009 and LaViolette 2010 when making credibility determinations in refugee claims related to sexual orientation and gender identity.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251120` offsets `190-198`; context: ” The discrepancies in the applicant’s evidence sufficiently support the conclusion of a lack of credibility which the Board Member reached and falls within that margin of appreciation.
- Evidence: `reasoning_application` cue `apply` at chunk `5251120` offsets `593-598`; context: Did the Board err in failing to apply the Charter and international human rights instruments in its state protection analysis?
- Evidence: `party_position` cue `contends` at chunk `5251121` offsets `19-27`; context: [33] The applicant contends that the Board Member erred in law when he declined to apply the Canadian Charter of Rights and Freedoms and international legal instruments as sources of law to evaluate the availability of state protection to her and others similarly situated in the US The Board Member noted that opinion evidence submitted by the applicant was to the effect that the US Military Justice system does not respect the requirements of the European Convention of Human Rights and the Charter.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251121` offsets `319-327`; context: [33] The applicant contends that the Board Member erred in law when he declined to apply the Canadian Charter of Rights and Freedoms and international legal instruments as sources of law to evaluate the availability of state protection to her and others similarly situated in the US The Board Member noted that opinion evidence submitted by the applicant was to the effect that the US Military Justice system does not respect the requirements of the European Convention of Human Rights and the Charter.
- Evidence: `governing_rule` cue `under` at chunk `5251121` offsets `835-840`; context: This, the applicant argues, led to the Member’s decision not to rely upon the expert evidence relating to state protection under the US system.
- Evidence: `reasoning_application` cue `apply` at chunk `5251121` offsets `83-88`; context: [33] The applicant contends that the Board Member erred in law when he declined to apply the Canadian Charter of Rights and Freedoms and international legal instruments as sources of law to evaluate the availability of state protection to her and others similarly situated in the US The Board Member noted that opinion evidence submitted by the applicant was to the effect that the US Military Justice system does not respect the requirements of the European Convention of Human Rights and the Charter.
- Evidence: `party_position` cue `submits` at chunk `5251122` offsets `19-26`; context: [34] The applicant submits that the Member’s analysis was in error given the direction in s 3 of the IRPA that the Act is to be construed and applied in a manner that furthers domestic and international interests.
- Evidence: `governing_rule` cue `under` at chunk `5251122` offsets `262-267`; context: In particular, it requires that decisions taken under the Act be consistent with the Charter and comply with the international human rights instruments to which Canada is signatory.
- Evidence: `reasoning_application` cue `applied` at chunk `5251122` offsets `142-149`; context: [34] The applicant submits that the Member’s analysis was in error given the direction in s 3 of the IRPA that the Act is to be construed and applied in a manner that furthers domestic and international interests.

#### 26616:4:subtheme:5 · paragraphs 35-37

- Raw key terms: `canadian, court, canada, domestic, foreign, human, hunt, judicial`
- Display key terms: `canadian, domestic, foreign, human, hunt, judicial`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: canadian, domestic, foreign, human, hunt, judicial Rule/authority context: [35] In the first judicial review concerning this applicant, Smith, above, at paras 84-86, Justice de Montigny found that the Member in the first Board decision had erred in failing to consider whether the applicant, as  Application context: In R v Hape, 2007 SCC 26, [2007] 2 SCR 292 [R v Hape], the Supreme Court clarified that Charter scrutiny does not apply to the laws of other states. Evidence spans paragraphs 35-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5251123` offsets `194-201`; context: [35] In the first judicial review concerning this applicant, Smith, above, at paras 84-86, Justice de Montigny found that the Member in the first Board decision had erred in failing to consider whether the applicant, as a homosexual, would receive equal treatment under the UCMJ.
- Evidence: `evidence_fact` cue `found that` at chunk `5251123` offsets `111-121`; context: [35] In the first judicial review concerning this applicant, Smith, above, at paras 84-86, Justice de Montigny found that the Member in the first Board decision had erred in failing to consider whether the applicant, as a homosexual, would receive equal treatment under the UCMJ.
- Evidence: `governing_rule` cue `under` at chunk `5251123` offsets `264-269`; context: [35] In the first judicial review concerning this applicant, Smith, above, at paras 84-86, Justice de Montigny found that the Member in the first Board decision had erred in failing to consider whether the applicant, as a homosexual, would receive equal treatment under the UCMJ.
- Evidence: `issue` cue `issue` at chunk `5251124` offsets `244-249`; context: [36] As I read those paragraphs and the other decisions cited in Hunt, they stand for the proposition that it is permissible for the Court to receive evidence and hear submissions as to the constitutional status of foreign legislation when the issue arises incidentally in the course of litigation over which the Court has undoubted jurisdiction.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251124` offsets `150-158`; context: [36] As I read those paragraphs and the other decisions cited in Hunt, they stand for the proposition that it is permissible for the Court to receive evidence and hear submissions as to the constitutional status of foreign legislation when the issue arises incidentally in the course of litigation over which the Court has undoubted jurisdiction.
- Evidence: `reasoning_application` cue `apply` at chunk `5251125` offsets `348-353`; context: In R v Hape, 2007 SCC 26, [2007] 2 SCR 292 [R v Hape], the Supreme Court clarified that Charter scrutiny does not apply to the laws of other states.

#### 26616:4:subtheme:6 · paragraphs 38-41

- Raw key terms: `board, justice, military, applicant, claimant, evidence, member, relevant`
- Display key terms: `justice, military, relevant`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: justice, military, relevant Position/evidence statements: He noted that the expert opinions on these subjects submitted by the applicant in this case were based on the theory that the claimant would be punished for having fled the US because her life was in danger due to her se Rule/authority context: In my view, he did not err in declining to consider the application of the Charter to the question of the validity of US military law under that country’s Constitution. | [40] The Board Member took into account that the UCMJ had been found to be adequate when subjected to constitutional scrutiny under American law. Application context: The obligation upon him was to apply the IRPA to the facts of this case in a manner that was consistent with the Charter and those international human rights instruments to which Canada has adhered. | He noted that the expert opinions on these subjects submitted by the applicant in this case were based on the theory that the claimant would be punished for having fled the US because her life was in danger due to her se Evidence spans paragraphs 38-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5251126` offsets `170-178`; context: [38] In the first judicial review, Justice de Montigny did not consider it necessary to pronounce on the constitutionality of the relevant provisions of the UCMJ as that question had not been argued by the parties on the record before him.
- Evidence: `evidence_fact` cue `record` at chunk `5251126` offsets `221-227`; context: [38] In the first judicial review, Justice de Montigny did not consider it necessary to pronounce on the constitutionality of the relevant provisions of the UCMJ as that question had not been argued by the parties on the record before him.
- Evidence: `issue` cue `whether` at chunk `5251127` offsets `197-204`; context: [39] In the decision before the Court in this proceeding, the Member reviewed the arguments presented that the Charter and international human rights instruments could be considered in determining whether the US military justice system would provide adequate protection to the claimant.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251127` offsets `816-824`; context: The issues were whether the applicant had led relevant, reliable and convincing evidence that state protection in the US was inadequate or non-existent and whether she had exhausted all of the remedies available to her before fleeing to Canada to seek protection.
- Evidence: `governing_rule` cue `under` at chunk `5251127` offsets `421-426`; context: In my view, he did not err in declining to consider the application of the Charter to the question of the validity of US military law under that country’s Constitution.
- Evidence: `reasoning_application` cue `apply` at chunk `5251127` offsets `568-573`; context: The obligation upon him was to apply the IRPA to the facts of this case in a manner that was consistent with the Charter and those international human rights instruments to which Canada has adhered.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251128` offsets `649-657`; context: Notwithstanding the opinion evidence to the contrary submitted by the applicant, that was a conclusion reasonably open to the Member to make on the evidence as a whole.
- Evidence: `governing_rule` cue `under` at chunk `5251128` offsets `126-131`; context: [40] The Board Member took into account that the UCMJ had been found to be adequate when subjected to constitutional scrutiny under American law.
- Evidence: `counterargument_limitation` cue `although` at chunk `5251128` offsets `367-375`; context: He concluded that although the US military justice system is different from the Canadian civil justice system, there was adequate recourse in the US for those who felt they had been wronged in the US Army and that the claimant had not exhausted those avenues of recourse.
- Evidence: `party_position` cue `submitted` at chunk `5251129` offsets `417-426`; context: He noted that the expert opinions on these subjects submitted by the applicant in this case were based on the theory that the claimant would be punished for having fled the US because her life was in danger due to her sexual orientation.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251129` offsets `58-66`; context: [41] The Board Member reviewed the documentary and expert evidence provided.
- Evidence: `reasoning_application` cue `because` at chunk `5251129` offsets `541-548`; context: He noted that the expert opinions on these subjects submitted by the applicant in this case were based on the theory that the claimant would be punished for having fled the US because her life was in danger due to her sexual orientation.

#### 26616:4:subtheme:7 · paragraphs 42-45

- Raw key terms: `board, claimant, member, opinion, cannot, claim, court, credibility`
- Display key terms: `opinion, cannot, credibility`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: opinion, cannot, credibility Application context: He took note of Justice de Montigny’s view that this claimant’s situation as a lesbian was very different from that, for example, of a male conscientious objector, because her claim was predicated on being subject to pun | He therefore rejected the reports on discrimination and deficiencies in the US military system as evidence of factors which had pushed the claimant to flee. Evidence spans paragraphs 42-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5251130` offsets `310-317`; context: [42] Donald JM Brown and John M Evans, Judicial Review of Administrative Action in Canada, loose-leaf (consulted on 4 October 2012), (Toronto: Canvasback Publishing, 2012), §10:5450 “Expert and Opinion Evidence”, at pp 10-69-10-70, state that “it is within the discretion of administrative tribunals to decide whether to admit expert evidence, and to determine the weight to be assigned to it.
- Evidence: `evidence_fact` cue `Evidence` at chunk `5251130` offsets `202-210`; context: [42] Donald JM Brown and John M Evans, Judicial Review of Administrative Action in Canada, loose-leaf (consulted on 4 October 2012), (Toronto: Canvasback Publishing, 2012), §10:5450 “Expert and Opinion Evidence”, at pp 10-69-10-70, state that “it is within the discretion of administrative tribunals to decide whether to admit expert evidence, and to determine the weight to be assigned to it.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `5251130` offsets `402-414`; context: ] Nevertheless, while a tribunal need not be bound by expert evidence, it should have valid grounds for rejecting or discounting it, and it cannot act arbitrarily in this regard.
- Evidence: `reasoning_application` cue `because` at chunk `5251132` offsets `369-376`; context: He took note of Justice de Montigny’s view that this claimant’s situation as a lesbian was very different from that, for example, of a male conscientious objector, because her claim was predicated on being subject to punishment not merely for desertion but also for her sexual orientation.
- Evidence: `counterargument_limitation` cue `but` at chunk `5251132` offsets `458-461`; context: He took note of Justice de Montigny’s view that this claimant’s situation as a lesbian was very different from that, for example, of a male conscientious objector, because her claim was predicated on being subject to punishment not merely for desertion but also for her sexual orientation.
- Evidence: `evidence_fact` cue `found that` at chunk `5251133` offsets `12-22`; context: [45] Having found that her claim of having experienced persecution based on sexual orientation was not credible, the Board Member concluded that the opinions describing an environment in which these experiences could have occurred were not relevant.
- Evidence: `reasoning_application` cue `therefore` at chunk `5251133` offsets `253-262`; context: He therefore rejected the reports on discrimination and deficiencies in the US military system as evidence of factors which had pushed the claimant to flee.

#### 26616:4:subtheme:8 · paragraphs 46-48

- Raw key terms: `claimant, evidence, expert, member, available, board, opinion, opinions`
- Display key terms: `expert, available, opinion, opinions`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: expert, available, opinion, opinions Application context: Therefore the expert opinions on whether it would have been available if she had sought it out, or whether it would be available in the future, were not relevant. | [47] The Member’s findings in this regard are distinguishable from cases such as Unal v Canada (Minister of Citizenship and Immigration) 2004 FC 518 where the Board was found to have erred in discounting expert reports b Evidence spans paragraphs 46-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5251134` offsets `341-348`; context: Therefore the expert opinions on whether it would have been available if she had sought it out, or whether it would be available in the future, were not relevant.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251134` offsets `66-74`; context: [46] The Board Member also rejected the expert opinion reports as evidence that state protection was unavailable.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5251134` offsets `308-317`; context: Therefore the expert opinions on whether it would have been available if she had sought it out, or whether it would be available in the future, were not relevant.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251135` offsets `457-465`; context: In Unal, for example, there was independent objective evidence including the results of a medical examination that supported the applicant’s personal account and the opinions provided.
- Evidence: `reasoning_application` cue `because` at chunk `5251135` offsets `219-226`; context: [47] The Member’s findings in this regard are distinguishable from cases such as Unal v Canada (Minister of Citizenship and Immigration) 2004 FC 518 where the Board was found to have erred in discounting expert reports because they were based in part on information provided by the claimant, without also assessing and weighing the objective findings by the experts which were specific to the claimant.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251136` offsets `49-57`; context: [48] The Member retained only the expert opinion evidence detailing the remedies which would have been available to the claimant within the US Army, which he used in coming to his credibility determination that it was not plausible that the claimant had been unaware of all of these avenues of recourse.

#### 26616:4:subtheme:9 · paragraphs 49-54

- Raw key terms: `protection, evidence, state, board, claimant, conclusion, court, determine`
- Display key terms: `protection, state, conclusion, determine`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: protection, state, conclusion, determine Position/evidence statements: The Court accepts that the Member might have reached a different conclusion based on the voluminous material submitted by the applicant with respect to the experiences of gays and lesbians in the US military. | [50] As stated by the Federal Court of Appeal in Carillo v Canada (Minister of Citizenship and Immigration) 2008 FCA 94 at paragraph 38, a refugee claimant who asserts that state protection in her country of origin is in Rule/authority context: [16] Reasons may not include all the arguments, statutory provisions, jurisprudence or other details the reviewing judge would have preferred, but that does not impugn the validity of either the reasons or the result und Evidence spans paragraphs 49-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5251137` offsets `469-476`; context: It is not the role of the Court to re-weigh that evidence, however, but to determine whether the Board’s treatment of it was unreasonable.
- Evidence: `party_position` cue `submitted` at chunk `5251137` offsets `284-293`; context: The Court accepts that the Member might have reached a different conclusion based on the voluminous material submitted by the applicant with respect to the experiences of gays and lesbians in the US military.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251137` offsets `433-441`; context: It is not the role of the Court to re-weigh that evidence, however, but to determine whether the Board’s treatment of it was unreasonable.
- Evidence: `counterargument_limitation` cue `however` at chunk `5251137` offsets `443-450`; context: It is not the role of the Court to re-weigh that evidence, however, but to determine whether the Board’s treatment of it was unreasonable.
- Evidence: `issue` cue `whether` at chunk `5251138` offsets `654-661`; context: In other words, if the reasons allow the reviewing court to understand why the tribunal made its decision and permit it to determine whether the conclusion is within the range of acceptable outcomes, the Dunsmuir criteria are met.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5251138` offsets `70-83`; context: [16] Reasons may not include all the arguments, statutory provisions, jurisprudence or other details the reviewing judge would have preferred, but that does not impugn the validity of either the reasons or the result under a reasonableness analysis.
- Evidence: `party_position` cue `asserts` at chunk `5251139` offsets `160-167`; context: [50] As stated by the Federal Court of Appeal in Carillo v Canada (Minister of Citizenship and Immigration) 2008 FCA 94 at paragraph 38, a refugee claimant who asserts that state protection in her country of origin is inadequate or nonexistent bears the evidentiary burden of producing evidence to that effect and the legal burden of persuading the trier of fact that the claim in this respect is founded.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251139` offsets `286-294`; context: [50] As stated by the Federal Court of Appeal in Carillo v Canada (Minister of Citizenship and Immigration) 2008 FCA 94 at paragraph 38, a refugee claimant who asserts that state protection in her country of origin is inadequate or nonexistent bears the evidentiary burden of producing evidence to that effect and the legal burden of persuading the trier of fact that the claim in this respect is founded.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251140` offsets `181-189`; context: [51] The applicable standard of proof is the balance of probabilities and the presumption that state protection is available to the claimant can be rebutted by clear and convincing evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251142` offsets `54-62`; context: [53] It is the Board’s responsibility to consider the evidence and determine what is relevant to the case before it.

#### 26616:4:subtheme:10 · paragraphs 55-61

- Raw key terms: `applicant, member, evidence, board, persecution, protection, state, case`
- Display key terms: `persecution, protection, state, case`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: persecution, protection, state, case Position/evidence statements: [55] The applicant contends that the Member did not properly analyze her situation in light of the Gender Guidelines given that she was a lesbian in the US military. Application context: The Member did not simply pay “lip service” to the Guidelines as the applicant contends but considered how they applied to the case before him. | In those circumstances, it was reasonable for the Board Member to conclude that the presumption of state protection had not been rebutted in this case. Operative outcome context: For that reason, the application is dismissed. Evidence spans paragraphs 55-61. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5251143` offsets `162-170`; context: [54] The Member’s observations in this respect were not framed as a finding that the applicant had an internal flight alternative as is contended but went to the question of whether she had sought other means to obtain protection away from her base.
- Evidence: `party_position` cue `contends` at chunk `5251144` offsets `19-27`; context: [55] The applicant contends that the Member did not properly analyze her situation in light of the Gender Guidelines given that she was a lesbian in the US military.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251144` offsets `255-263`; context: The Guidelines instruct that where the claimant cannot rely on the more typical forms of evidence as “clear and convincing proof” of the failure to provide state protection, reference may need to be made to alternative forms of evidence: Evans v Canada (Minister of Citizenship and Immigration), 2011 FC 444 at paras 14-15.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251145` offsets `233-241`; context: [56] In my view, it is clear from the Member’s reasons for decision that he was alert and sensitive to the context in which the applicant presented her claim – her experience as a lesbian in an environment which was described in the evidence as sexist and homophobic.
- Evidence: `reasoning_application` cue `applied` at chunk `5251145` offsets `380-387`; context: The Member did not simply pay “lip service” to the Guidelines as the applicant contends but considered how they applied to the case before him.
- Evidence: `counterargument_limitation` cue `but` at chunk `5251145` offsets `356-359`; context: The Member did not simply pay “lip service” to the Guidelines as the applicant contends but considered how they applied to the case before him.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251146` offsets `32-40`; context: [57] The applicant presented no evidence that she could not attempt to seek state protection within her country before fleeing to Canada.
- Evidence: `reasoning_application` cue `conclude` at chunk `5251146` offsets `395-403`; context: In those circumstances, it was reasonable for the Board Member to conclude that the presumption of state protection had not been rebutted in this case.
- Evidence: `evidence_fact` cue `testimony` at chunk `5251147` offsets `303-312`; context: The applicant’s testimony was the only evidence going to the specific facts of her claim.
- Evidence: `counterargument_limitation` cue `but` at chunk `5251147` offsets `259-262`; context: That assessment was not microscopic or overzealous but detailed and organized.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251148` offsets `57-65`; context: [59] The Board concluded, taking into account all of the evidence, that there was not relevant, trustworthy and convincing evidence that state protection was unavailable to the applicant in the US The applicant could not establish, as a result, that her fear of persecution was objectively well-founded.
- Evidence: `reasoning_application` cue `because` at chunk `5251148` offsets `507-514`; context: The Board further analyzed the remedies available to her should she return to the US to face charges of being absent without leave and concluded that she had not established that she would be persecuted because she was a lesbian or for fleeing her base ostensibly in fear of her life.
- Evidence: `disposition` cue `dismissed` at chunk `5251149` offsets `230-239`; context: For that reason, the application is dismissed.

#### 26616:4:subtheme:11 · paragraphs 62-63

- Raw key terms: `court, general, importance, protection, serious, agent, answer, appeal`
- Display key terms: `importance, protection, serious, agent, answer`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: importance, protection, serious, agent, answer Evidence spans paragraphs 62-63. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5251150` offsets `344-352`; context: Canada (Minister of Citizenship and Immigration), 2004 FCA 89 at paragraph 11, the threshold for certification was articulated as: “is there a serious question of general importance which would be dispositive of an appeal”.
- Evidence: `evidence_fact` cue `determined that` at chunk `5251150` offsets `511-526`; context: Canada (Minister of Citizenship and Immigration), 2006 FCA 68, the Court of Appeal determined that a certified question must lend itself to a generic approach leading to an answer of general application.
- Evidence: `evidence_fact` cue `evidence` at chunk `5251151` offsets `320-328`; context: Can a Board member discount expert evidence on the ground that it may refer to information provided by the applicant?

#### 26616:4:subtheme:12 · paragraphs 64-65

- Raw key terms: `application, board, case, factual, question, analysis, appeal, basis`
- Display key terms: `case, factual, question, analysis, basis`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: case, factual, question, analysis, basis Evidence spans paragraphs 64-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5251152` offsets `15-23`; context: [63] The first question would not be dispositive of an appeal as the Board did not fetter its discretion in this instance.
- Evidence: `issue` cue `question` at chunk `5251153` offsets `16-24`; context: [64] The second question is also fact dependent.
- Evidence: `counterargument_limitation` cue `but` at chunk `5251153` offsets `158-161`; context: The decision in this case turned on the Board’s credibility analysis that discounted not the expert opinions but the factual basis upon which they were predicated.

#### 26616:4:subtheme:13 · paragraphs 66-67

- Raw key terms: `above, accordingly, addressed, appeal, appropriate, certify, consider, court`
- Display key terms: `above, accordingly, addressed, appropriate, certify, consider`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: above, accordingly, addressed, appropriate, certify, consider Application context: [66] Accordingly, I do not consider it appropriate to certify any of the proposed questions. Evidence spans paragraphs 66-67. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5251154` offsets `15-20`; context: [65] The third issue was addressed by the Federal Court of Appeal in Hinzman, above.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5251155` offsets `5-16`; context: [66] Accordingly, I do not consider it appropriate to certify any of the proposed questions.

#### Section text

[17] The issues raised on this application are as follows:
1. Did the Board make unreasonable credibility findings?
2. Did the Board err in failing to apply the Charter and international human rights instruments in its state protection analysis?
3. Did the Board disregard important expert evidence?
4. Did the Board make unreasonable state protection findings?
ANALYSIS:
Standard of review;

[18] The prior jurisprudence has satisfactorily determined the standard to be applied to the issues in this matter which are questions of fact or of mixed fact and law. Such questions generally attract the reasonableness standard: Dunsmuir v New Brunswick, 2008 SCC 9 at para 51. The availability of state protection is a question of mixed fact and law and thus is reviewable for reasonableness: Hinzman v Canada (Minister of Citizenship and Immigration), 2007 FCA 171 at para 38. Issues of credibility, a question of fact, are also reviewable against a standard of reasonableness: Berhane v Canada (Minister of Citizenship and Immigration), 2011 FC 510 at para 24.

[19] Reasonableness is based on the existence of justification, transparency and intelligibility within the decision-making process and whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law: Dunsmuir, above, at para 47; and Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 59.
Did the Board make unreasonable credibility findings?

[20] The Board based its principal adverse credibility findings on three points: contradictions between the applicant’s previous testimony in 2008, the narrative in her PIF and her testimony in the 2010 hearings; implausibilities in her evidence; and an inability to answer certain questions related to asserted memory problems.

[21] The applicant contends that the Board’s credibility findings are erroneous for several reasons: they are contrary to the Board’s 2009 decision which was made closer in time to the incidents underlying the refugee claim and in which the Board did not make an adverse credibility finding; the findings are based on ordinary memory problems such as an inability to recall the names of individuals; the inconsistencies relied upon do not amount to serious or significant contradictions; they conflate recollections of several events; different descriptions of harassment were improperly characterized as inconsistent; and the Board engaged in microscopic examination of the applicant’s evidence.

[22] The applicant argues that the Board did not evaluate the plausibility of her story in light of the extensive documentary and opinion evidence submitted on the situation of homosexuals in the US military. She contends that the Board failed to properly apply the Gender Guideline and the UNHCR Guidance Note in its analysis. The applicant should not have been expected to share her sexual orientation and the persecution based on her sexuality in an environment widely documented as hostile to homosexuals. Further, she asserts, the Board erred when it stated that the applicant should have contacted the military authorities to obtain evidence of her persecution when it was the military that were her persecutors.

[23] As the respondent notes, credibility findings are highly factual, case specific and depend in part on factors that a reviewing court is unable to consider such as the demeanour of a witness. The Board is entitled to draw inferences based on implausibility, common sense and rationality: Aguebor v Canada (Minister of Employment and Immigration), [1993] FCJ No 732 (FCA) at para 4. It is not for the reviewing court to substitute its view of such matters. However, if the evidence before the Board does not support the credibility findings, or if the contradictions or implausibilities relied upon by the Board are insignificant and do not relate to the claim, this Court should intervene. I am unable to reach such conclusions in this case.

[24] In this matter, some of the alleged inconsistencies identified by the Board relate to events that the applicant described in her PIF, remembered in greater detail in the first hearing (in November 2008) and was unable to recall during her testimony in the second series of hearings (in August and November 2010). Minor differences in testimony given by the same witness at hearings conducted two years apart are to be expected. In this case, however, the differences were more pronounced.

[25] For example, the applicant had written in her PIF that she was continually harassed once her sexual identity was indirectly revealed during her advanced individual training. She also described an incident where she was punched in the head when returning alone to her room. When asked about the incident during the second hearing she stated that it was the only incident experienced during her training. She told no one about it because only a week remained in her training and it was unlikely that anything would be done prior to her departure. Confronted with the inconsistent PIF narrative, the applicant offered no explanation. It was open to the Board to take this inconsistency into account in considering her credibility.

[26] The Member carefully reviewed several other areas of difficulty with the applicant’s evidence. When asked about the circumstances in which her orientation had been disclosed to colleagues at Fort Campbell, the applicant’s answers were taken to be evasive. She could not remember the name of the woman she had been with or those of the two soldiers who had seen them together. She explained that she preferred not to remember the soldiers’ names because it was a difficult time in her life. In his analysis, the Board Member considered whether that was a reasonable response, in light of the Chairperson’s Gender Guideline, given that no evidence had been presented that the applicant suffered from a psychological disorder or had been the victim of sexual violence. Concluding that it was not, the Member found that the applicant’s credibility was undermined with respect to the impact of the disclosure of her sexual orientation. Again, in my view, this was a finding open to the Member.

[27] The applicant testified that she was routinely picked up and thrown to the ground by a fellow soldier in her brigade. She could not remember whether he had verbally abused her but assumed that the physical abuse was because he had discovered that she was a lesbian. At the second hearing, she added that one of her superiors had been present and had witnessed the assault and done nothing, a detail which was not mentioned in her PIF or at the first hearing. She did not remember the superior’s name. She told a female doctor at the base about these assaults but the doctor did not take them seriously, suggesting the soldier was just playing with her. The applicant had taken no steps to identify the doctor or to contact her in an effort to corroborate her story. Her explanation was that she did not want to contact the US Army or let them know where she was. The applicant gave the same explanation when asked why she had not contacted the Army from Canada to request a discharge by reason of her orientation under the Don’t Ask, Don’t Tell policy while it was still in effect. The Board Member thought that the explanation provided was unreasonable given that it was then evident that she was in Canada and seeking protection.

[28] With respect to the threatening notes, the Board Member accepted that it was reasonable for the applicant not to keep them in anticipation of an unforeseen hearing before a tribunal in Canada. However he did not understand why she had not used the notes to tell someone in the line of authority at her base about what was happening. She had testified that she knew she could report the threats and assaults to the authorities. She said she was terrified, did not trust anyone and did not know who might be supporting the people who were writing the threats. This was, in general, the explanation that the applicant provided when asked why she did not tell anyone about what was allegedly going on at that time – not a friend from her former life who was also at the base, her family or anyone in the chain of command.

[29] When confronted with the expert opinion evidence on remedies available to US military personnel at the time – zero tolerance policies towards harassment and UCMJ provisions against assault, military attorney services, the possibility of declaring a homosexual orientation, whistle-blower protections for complaining to the Inspector General, the possibility of contacting a member of Congress – the applicant explained that as a nineteen-year old private she was not aware of any of these remedies. While the Court may have reached a different conclusion, the reasonableness of that explanation was a matter for the Board to determine. The conclusion reached was, on the evidence, within the range of acceptable outcomes.

[30] The Board Member provided the claimant with the opportunity to explain the discrepancy between her accounts of why she ultimately left the base. In her PIF she had written that she had received a written death threat in early July 2007 but at the hearing she said that the written death threat on the day she left was the first one which she had received. Confronted with the contradiction, she gave no explanation. The Board Member concluded that this undermined her credibility. This conclusion was open to him based on the conflict in the evidence presented.

[31] Before coming to the overall conclusion that the claimant’s testimony was not plausible, the Board Member noted that he had considered the recommendation to exercise caution in LaViolette 2009 and LaViolette 2010 when making credibility determinations in refugee claims related to sexual orientation and gender identity. He also recognized that the case law clearly set out that adverse credibility findings should only be made in the clearest of cases and after considering the actions described as they would have appeared from the claimant’s point of view at the time. Nonetheless, he found that the accumulation of problems in her testimony rendered the claimant not credible with respect to her allegations of being threatened and assaulted and with respect to the steps which she took to inform the authorities. It did not assist the applicant’s claim that she offered no documentation or corroborative factual evidence to support her own testimony. Failure to do so when it is reasonable to expect such evidence may have an impact on a claimant’s credibility: Mercado v Canada (Minister of Citizenship and Immigration), 2010 FC 289 at para 32.

[32] As the Supreme Court noted in Dunsmuir at para 47, “Tribunals have a margin of appreciation within the range of acceptable and rational solutions.” The discrepancies in the applicant’s evidence sufficiently support the conclusion of a lack of credibility which the Board Member reached and falls within that margin of appreciation. It is not the role of this Court to re-weigh the evidence that was before the Board even if the Court might have drawn different inferences or found the evidence and explanations offered by the applicant to be plausible.
2. Did the Board err in failing to apply the Charter and international human rights instruments in its state protection analysis?

[33] The applicant contends that the Board Member erred in law when he declined to apply the Canadian Charter of Rights and Freedoms and international legal instruments as sources of law to evaluate the availability of state protection to her and others similarly situated in the US The Board Member noted that opinion evidence submitted by the applicant was to the effect that the US Military Justice system does not respect the requirements of the European Convention of Human Rights and the Charter. He concluded that as the incidents cited by the applicant in her claim had allegedly occurred solely in the US, he did not see how the Canadian and European instruments would have legal force in that country. This, the applicant argues, led to the Member’s decision not to rely upon the expert evidence relating to state protection under the US system.

[34] The applicant submits that the Member’s analysis was in error given the direction in s 3 of the IRPA that the Act is to be construed and applied in a manner that furthers domestic and international interests. In particular, it requires that decisions taken under the Act be consistent with the Charter and comply with the international human rights instruments to which Canada is signatory.

[35] In the first judicial review concerning this applicant, Smith, above, at paras 84-86, Justice de Montigny found that the Member in the first Board decision had erred in failing to consider whether the applicant, as a homosexual, would receive equal treatment under the UCMJ. Justice de Montigny noted that a Canadian court could make findings of fact regarding the constitutionality of a foreign law, citing Hunt v T&N plc, [1993] 4 SCR 289 at paras 28-32 (Hunt).

[36] As I read those paragraphs and the other decisions cited in Hunt, they stand for the proposition that it is permissible for the Court to receive evidence and hear submissions as to the constitutional status of foreign legislation when the issue arises incidentally in the course of litigation over which the Court has undoubted jurisdiction. The circumstance envisaged in Hunt was when a Canadian provincial law has extraterritorial application. I do not read s 3 of the IRPA as requiring that the Court make such a determination with regard to a foreign law of another state which has no extraterritorial effect in Canada, as that would be incompatible with judicial comity and sovereignty. The section requires, rather, that the domestic application of IRPA be consistent with the human rights instruments to which Canada is signatory.

[37] In Baker v Canada (Minister of Citizenship and Immigration), [1999] 2 SCR 817 at para 70, the Supreme Court stressed the “important role of international human rights law as an aid in interpreting domestic law” (emphasis added). In R v Hape, 2007 SCC 26, [2007] 2 SCR 292 [R v Hape], the Supreme Court clarified that Charter scrutiny does not apply to the laws of other states. The Federal Court of Appeal, in Amnesty International Canada v Canada (Canadian Forces), 2008 FCA 401 at para 14, agreed that the Charter did not apply to “foreigners, with no attachment whatsoever to Canada or its laws”.

[38] In the first judicial review, Justice de Montigny did not consider it necessary to pronounce on the constitutionality of the relevant provisions of the UCMJ as that question had not been argued by the parties on the record before him. He held that the Board had a duty to determine whether the UCMJ was enforced in a non-discriminatory fashion in the United States, both substantively and procedurally, with respect to military personnel.

[39] In the decision before the Court in this proceeding, the Member reviewed the arguments presented that the Charter and international human rights instruments could be considered in determining whether the US military justice system would provide adequate protection to the claimant. In my view, he did not err in declining to consider the application of the Charter to the question of the validity of US military law under that country’s Constitution. Nor was he required to analyse US law in light of the international instruments. The obligation upon him was to apply the IRPA to the facts of this case in a manner that was consistent with the Charter and those international human rights instruments to which Canada has adhered. The issues were whether the applicant had led relevant, reliable and convincing evidence that state protection in the US was inadequate or non-existent and whether she had exhausted all of the remedies available to her before fleeing to Canada to seek protection. Absent evidence of such efforts it was impossible for the Board to assess the availability of protection for her: Hinzman, Re, 2007 FCA 171 at para 62.

[40] The Board Member took into account that the UCMJ had been found to be adequate when subjected to constitutional scrutiny under American law. The Member observed that the US courts, while fully aware of the international standards, had so far deemed the structural independence and impartiality of the US military justice system to be adequate. He concluded that although the US military justice system is different from the Canadian civil justice system, there was adequate recourse in the US for those who felt they had been wronged in the US Army and that the claimant had not exhausted those avenues of recourse. Notwithstanding the opinion evidence to the contrary submitted by the applicant, that was a conclusion reasonably open to the Member to make on the evidence as a whole.
3. Did the Board disregard important expert evidence?

[41] The Board Member reviewed the documentary and expert evidence provided. Having done so, he concluded that the material concerning discrimination against gays and lesbians in the US Army and concerning the deficiencies of the US military justice system did not constitute relevant, trustworthy, and convincing evidence of the insufficiency of state protection. He noted that the expert opinions on these subjects submitted by the applicant in this case were based on the theory that the claimant would be punished for having fled the US because her life was in danger due to her sexual orientation. When he reached this stage of his analysis, the Member had already found that the allegations of harassment and threats were not credible. He thus retained only the report on US military law by Professor Hansen to guide him in assessing the claimant’s situation.

[42] Donald JM Brown and John M Evans, Judicial Review of Administrative Action in Canada, loose-leaf (consulted on 4 October 2012), (Toronto: Canvasback Publishing, 2012), §10:5450 “Expert and Opinion Evidence”, at pp 10-69-10-70, state that “it is within the discretion of administrative tribunals to decide whether to admit expert evidence, and to determine the weight to be assigned to it. [. . .] Nevertheless, while a tribunal need not be bound by expert evidence, it should have valid grounds for rejecting or discounting it, and it cannot act arbitrarily in this regard. [. . .] However, it is not necessary for a tribunal to make an adverse finding about the credibility of an expert before it can reject the evidence, particularly when the agency is developing policy”. In this instance the governing policy is in flux as the US Congress, Administration and Military come to terms with changing attitudes towards the role of gays and lesbians within American society.

[43] Expert opinions cannot be substituted for a Board Member’s assessment of a claimant’s credibility. The Supreme Court stated in R v Marquard, [1993] 4 SCR 223, [1993] SCJ No 119 (QL) at para 49 that: “A judge or jury who simply accepts an expert's opinion on the credibility of a witness would be abandoning its duty to itself determine the credibility of the witness. Credibility must always be the product of the judge or jury's view of the diverse ingredients it has perceived at trial, combined with experience, logic and an intuitive sense of the matter”.

[44] In this case, the Board Member assessed that the claimant was not credible in asserting that she would face punishment for having fled to save her life from persecution due to her sexual orientation. He took note of Justice de Montigny’s view that this claimant’s situation as a lesbian was very different from that, for example, of a male conscientious objector, because her claim was predicated on being subject to punishment not merely for desertion but also for her sexual orientation. That was an error made by the Board in the first determina

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 26616:5 · paragraphs 68-69

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0e706793d0860efb04d75742e546637a6a9069cf75cad849ad97969f8e5db8e4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26616:5:subtheme:1 · paragraphs 68-69

- Raw key terms: `application, april, bethany, cause, certified, citizenship, court, date`
- Display key terms: `april, bethany, certified, date`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: april, bethany, certified, date Operative outcome context: JUDGMENT IT IS THE JUDGMENT OF THIS COURT that: the application is dismissed; and no questions are certified. Evidence spans paragraphs 68-69. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `5251155` offsets `160-169`; context: JUDGMENT
IT IS THE JUDGMENT OF THIS COURT that:
the application is dismissed; and no questions are certified.

#### Section text

JUDGMENT
IT IS THE JUDGMENT OF THIS COURT that:
the application is dismissed; and no questions are certified.
“Richard G. Mosley”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-5699-11
STYLE OF CAUSE: BETHANY LANAE SMITH
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
PLACE OF HEARING: Ottawa, Ontario
DATE OF HEARING: April 24, 2012
REASONS FOR 

## 26616:6 · paragraphs 70-70

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b3316d6020d901af320e982286aeb1cf83d7ec470520e1143a9a5713de080bb3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26616:6:subtheme:1 · paragraphs 70-70

- Raw key terms: `appearances, applicant, attorney, barrister, canada, collins-williams, craig, dated`
- Display key terms: `barrister, collins-williams, craig, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, collins-williams, craig, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 70-70. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: MOSLEY J.
DATED: November 2, 2012
APPEARANCES:
Jamie Liew
FOR THE APPLICANT
Craig Collins-Williams
FOR THE RESPONDENT
SOLICITORS OF RECORD:
JAMIE LIEW
Barrister & Solicitor
Ottawa, Ontario
FOR THE APPLICANT
MYLES J. KIRVAN
Deputy Attorney General of Canada
Ottawa, Ontario
FOR THE RESPONDENT
