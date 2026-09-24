# Discussion Units: case 24696

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **40**
- Continuity pairs: **39**
- Discussion Units: **2**
- Paragraph source hashes: **40**
- Sub-themes: **9**

## 24696:1 · paragraphs 0-38

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f77d105c5e7038f7cab697b00b4083bdd1817d84e904a2e98f7106a5f70cb3f5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24696:1:subtheme:1 · paragraphs 0-8

- Raw key terms: `decision, refugee, appeal, applicants, protection, review, court, division`
- Display key terms: `refugee, protection, review, division`
- Argument roles: `disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, reasoning_application Display terms: refugee, protection, review, division Rule/authority context: The essence of the case before the Court is the following: which entity does what, when, and according to which principles of the legislation and the case law? | [3] The RAD is a specialized quasi-judicial body, whose members have the powers of a commissioner under section 111 of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA]. Application context: The RAD’s analysis must therefore be concerned with the justification, transparency and intelligibility within the decision-making process and not be a reassessment of the evidence. Operative outcome context: The RAD dismissed this appeal on October 18, 2013. Evidence spans paragraphs 0-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `principles` at chunk `5161306` offsets `907-917`; context: The essence of the case before the Court is the following: which entity does what, when, and according to which principles of the legislation and the case law?
- Evidence: `governing_rule` cue `under` at chunk `5161308` offsets `98-103`; context: [3] The RAD is a specialized quasi-judicial body, whose members have the powers of a commissioner under section 111 of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA].
- Evidence: `evidence_fact` cue `evidence` at chunk `5161309` offsets `65-73`; context: [4] If the RPD does not provide reasons in its assessment of the evidence, the RAD must intervene following its own review; if the RPD misinterprets the legislation, the RAD must also intervene.
- Evidence: `governing_rule` cue `under` at chunk `5161310` offsets `430-435`; context: Introduction [6] This is an application for judicial review made under subsection 72(1) of the IRPA of a decision by the RAD of the Immigration and Refugee Board dated October 18, 2013, dismissing the applicants’ appeal of the RPD’s decision denying their claim to be recognized as Convention refugees or persons in need of protection under sections 96 and 97 of the IRPA.
- Evidence: `disposition` cue `dismissed` at chunk `5161312` offsets `66-75`; context: The RAD dismissed this appeal on October 18, 2013.
- Evidence: `evidence_fact` cue `evidence` at chunk `5161313` offsets `269-277`; context: Decision under review [11] First, the RAD noted that there was no need to hold a hearing in the present matter since the applicants had not presented any new evidence according to the requirements of subsection 110(4).
- Evidence: `governing_rule` cue `under` at chunk `5161313` offsets `120-125`; context: Decision under review [11] First, the RAD noted that there was no need to hold a hearing in the present matter since the applicants had not presented any new evidence according to the requirements of subsection 110(4).
- Evidence: `evidence_fact` cue `evidence` at chunk `5161314` offsets `579-587`; context: The RPD is better situated to make factual findings owing to its extensive exposure to the evidence, the advantage of hearing testimony viva voce, and its familiarity with the case as a whole (Housen v Nikolaisen, 2002 SCC 33, [2002] 2 SCR 235).
- Evidence: `governing_rule` cue `standard of review` at chunk `5161314` offsets `77-95`; context: [12] The RAD went on to examine the RAD’s role as an appeal tribunal and the standard of review applicable to questions of fact and questions of mixed fact and law as well as to pure questions of law.
- Evidence: `reasoning_application` cue `therefore` at chunk `5161314` offsets `758-767`; context: The RAD’s analysis must therefore be concerned with the justification, transparency and intelligibility within the decision-making process and not be a reassessment of the evidence.

#### 24696:1:subtheme:2 · paragraphs 9-11

- Raw key terms: `applicants, court, jurisdiction, review, appeal, decision, division, facts`
- Display key terms: `jurisdiction, review, division, facts`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: jurisdiction, review, division, facts Position/evidence statements: Positions of the parties [18] The applicant submits that the RAD’s decision is unreasonable since the RAD analyzed the RPD’s decision as part of a standard of review analysis. | [19] The applicants submit that Parliament, in creating the RAD, intended to create an appeal division with broad, unlimited jurisdiction; restricting the RAD’s review powers would amount to reproducing the work already  Rule/authority context: Referrals Renvoi (2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that (2) Elle ne peut procéder au renvoi que si elle estime, à la fois : (a) the decision  | [17] A reviewing court may avoid a full standard of review analysis if previous jurisprudence has satisfactorily resolved the issue (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190, at paras 57 and 62). Application context: It therefore concluded that their fear of being persecuted should they have to return to live in Cuba was not in fact a reasonable fear. Evidence spans paragraphs 9-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `5161315` offsets `446-451`; context: Issue [14] Did the RAD err in applying the standard of reasonableness to the RPD’s findings?
- Evidence: `evidence_fact` cue `determined that` at chunk `5161315` offsets `49-64`; context: [13] Regarding the merits of the appeal, the RAD determined that the RPD did not err in its application to the facts of the concept of persecution.
- Evidence: `governing_rule` cue `under` at chunk `5161315` offsets `4402-4407`; context: Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `reasoning_application` cue `therefore` at chunk `5161315` offsets `309-318`; context: It therefore concluded that their fear of being persecuted should they have to return to live in Cuba was not in fact a reasonable fear.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5161315` offsets `4379-4385`; context: Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `issue` cue `issue` at chunk `5161316` offsets `126-131`; context: [17] A reviewing court may avoid a full standard of review analysis if previous jurisprudence has satisfactorily resolved the issue (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190, at paras 57 and 62).
- Evidence: `party_position` cue `submits` at chunk `5161316` offsets `694-701`; context: Positions of the parties [18] The applicant submits that the RAD’s decision is unreasonable since the RAD analyzed the RPD’s decision as part of a standard of review analysis.
- Evidence: `governing_rule` cue `standard of review` at chunk `5161316` offsets `40-58`; context: [17] A reviewing court may avoid a full standard of review analysis if previous jurisprudence has satisfactorily resolved the issue (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190, at paras 57 and 62).
- Evidence: `party_position` cue `submit` at chunk `5161317` offsets `20-26`; context: [19] The applicants submit that Parliament, in creating the RAD, intended to create an appeal division with broad, unlimited jurisdiction; restricting the RAD’s review powers would amount to reproducing the work already being done by the Federal Court.

#### 24696:1:subtheme:3 · paragraphs 12-13

- Raw key terms: `decisions, question, review, standard, acceptable, according, against, analysis`
- Display key terms: `decisions, question, review, standard, acceptable, according, against, analysis`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: decisions, question, review, standard, acceptable, according, against, analysis Position/evidence statements: [20] In turn, the respondent argues that the statement of the RAD that its role is not to reassess the evidence is entirely consistent with the standard of reasonableness. Rule/authority context: Analysis [21] The question of law raised in this matter is the following: against which standard of review are the RPD’s findings of facts reviewable before the RAD? | [22] To identify the appropriate standard of review for the RAD’s examination of decisions of the RPD, the first question is what jurisdiction the RAD has. Evidence spans paragraphs 12-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5161318` offsets `266-273`; context: According to the respondent, the RAD’s role is not to reassess the evidence, but to determine whether, in light of the evidence, the decision rendered is within a range of possible, acceptable outcomes.
- Evidence: `party_position` cue `argues` at chunk `5161318` offsets `29-35`; context: [20] In turn, the respondent argues that the statement of the RAD that its role is not to reassess the evidence is entirely consistent with the standard of reasonableness.
- Evidence: `evidence_fact` cue `evidence` at chunk `5161318` offsets `103-111`; context: [20] In turn, the respondent argues that the statement of the RAD that its role is not to reassess the evidence is entirely consistent with the standard of reasonableness.
- Evidence: `governing_rule` cue `standard of review` at chunk `5161318` offsets `743-761`; context: Analysis [21] The question of law raised in this matter is the following: against which standard of review are the RPD’s findings of facts reviewable before the RAD?
- Evidence: `counterargument_limitation` cue `but` at chunk `5161318` offsets `249-252`; context: According to the respondent, the RAD’s role is not to reassess the evidence, but to determine whether, in light of the evidence, the decision rendered is within a range of possible, acceptable outcomes.
- Evidence: `issue` cue `question` at chunk `5161319` offsets `113-121`; context: [22] To identify the appropriate standard of review for the RAD’s examination of decisions of the RPD, the first question is what jurisdiction the RAD has.
- Evidence: `governing_rule` cue `standard of review` at chunk `5161319` offsets `33-51`; context: [22] To identify the appropriate standard of review for the RAD’s examination of decisions of the RPD, the first question is what jurisdiction the RAD has.

#### 24696:1:subtheme:4 · paragraphs 14-26

- Raw key terms: `appeal, tribunal, court, intervention, judicial, decision, made, professions`
- Display key terms: `intervention, judicial, made, professions`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: intervention, judicial, made, professions Position/evidence statements: [23] In applying the rules of interpretation to the relevant provisions in this matter (Rizzo & Rizzo Shoes Ltd, [1998] 1 SCR 27), such as to subsection 111(1) of the IRPA, the Court agrees with the applicants that Parli Rule/authority context: [81] The Supreme Court and this Court have repeatedly instructed the following: the appeal tribunal may in principle rectify any error in law in the decision under appeal or any palpable and overriding error in the deter | [82] This then is the standard against which the Tribunal des professions must examine the decisions before it under appeal. Application context: [26] In Parizeau, above, the Court of Appeal of Quebec made the following observations on the standard of intervention to be applied by administrative appeal tribunals: [translation] | [63] The Tribunal des professions sided with this approach and now applies the analytical process for judicial review when identifying its intervention standard. Operative outcome context: In this regard, the Court finds the reasoning in Parizeau c Barreau du Québec, 2011 QCCA 1498, [2011] RJQ 1506, presented by the applicants in support of their application, persuasive and instructive (the Supreme Court o | Even if it is true that the entry or re-entry of a person on the Roll of the Order of Advocates is not automatic, it is also not an outright privilege the granting of which can be denied in an authoritarian or capricious Evidence spans paragraphs 14-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5161320` offsets `383-390`; context: [23] In applying the rules of interpretation to the relevant provisions in this matter (Rizzo & Rizzo Shoes Ltd, [1998] 1 SCR 27), such as to subsection 111(1) of the IRPA, the Court agrees with the applicants that Parliament seems to have wanted to confer a broad power of intervention on the RAD, thus allowing the RAD to dispose of the merits of appeals and not only to determine whether the RPD’s decision was made in a reasonable manner as submitted by the Member in the present matter.
- Evidence: `party_position` cue `submitted` at chunk `5161320` offsets `445-454`; context: [23] In applying the rules of interpretation to the relevant provisions in this matter (Rizzo & Rizzo Shoes Ltd, [1998] 1 SCR 27), such as to subsection 111(1) of the IRPA, the Court agrees with the applicants that Parliament seems to have wanted to confer a broad power of intervention on the RAD, thus allowing the RAD to dispose of the merits of appeals and not only to determine whether the RPD’s decision was made in a reasonable manner as submitted by the Member in the present matter.
- Evidence: `evidence_fact` cue `evidence` at chunk `5161322` offsets `172-180`; context: [25] The Court agrees that an appeal before the RAD is not an appeal de novo; the IRPA restricts the power of the RAD, in comparison to that of the IAD, to considering new evidence and to holding a hearing only in exceptional cases (see subsections 110(4) and 110(6) of the IRPA).
- Evidence: `counterargument_limitation` cue `However` at chunk `5161322` offsets `281-288`; context: However, the Court cannot accept that, as a result of these limitations, Parliament intended to confer on the RAD a similar jurisdiction as to that of a judicial review body.
- Evidence: `disposition` cue `dismissed` at chunk `5161322` offsets `757-766`; context: In this regard, the Court finds the reasoning in Parizeau c Barreau du Québec, 2011 QCCA 1498, [2011] RJQ 1506, presented by the applicants in support of their application, persuasive and instructive (the Supreme Court of Canada dismissed the application for leave to appeal from this judgment on March 15, 2012: 2012 CanLII 12782 (SCC)).
- Evidence: `reasoning_application` cue `applied` at chunk `5161323` offsets `125-132`; context: [26] In Parizeau, above, the Court of Appeal of Quebec made the following observations on the standard of intervention to be applied by administrative appeal tribunals:
[translation]
- Evidence: `reasoning_application` cue `applies` at chunk `5161324` offsets `67-74`; context: [63] The Tribunal des professions sided with this approach and now applies the analytical process for judicial review when identifying its intervention standard.
- Evidence: `reasoning_application` cue `apply` at chunk `5161326` offsets `45-50`; context: [75] Having said that, if these instructions apply when the legislator has provided for the right to appeal the decision of a specialized administrative tribunal before a generalized court (and that is what all these decisions of the Supreme Court are concerned with), do they also apply when the hearing of the appeal is assigned to another, also specialized, administrative body?
- Evidence: `counterargument_limitation` cue `however` at chunk `5161326` offsets `895-902`; context: Do these dynamics and the resulting requirement come into the play in the second case, however, when the appeal body is also an administrative one?
- Evidence: `governing_rule` cue `under` at chunk `5161328` offsets `158-163`; context: [81] The Supreme Court and this Court have repeatedly instructed the following: the appeal tribunal may in principle rectify any error in law in the decision under appeal or any palpable and overriding error in the determination of the facts or in the application of the law (if it was correctly identified) to the facts.
- Evidence: `governing_rule` cue `under` at chunk `5161329` offsets `111-116`; context: [82] This then is the standard against which the Tribunal des professions must examine the decisions before it under appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `5161331` offsets `506-514`; context: Moreover, the Tribunal would also be justified in intervening if the final assessing decision made by the Applications Committee does not agree with the facts revealed by the evidence.
- Evidence: `disposition` cue `denied` at chunk `5161331` offsets `1088-1094`; context: Even if it is true that the entry or re-entry of a person on the Roll of the Order of Advocates is not automatic, it is also not an outright privilege the granting of which can be denied in an authoritarian or capricious manner.
- Evidence: `evidence_fact` cue `evidence` at chunk `5161332` offsets `677-685`; context: A palpable and overriding error is an error that, in its undeniability -- and therefore not a difference of opinion on the assessment of the evidence --, determines the outcome of the dispute in that the conclusion of the trier of fact, that is, the result of his or her decision, cannot hold water, thus, ipso facto, making the decision unreasonable.
- Evidence: `reasoning_application` cue `therefore` at chunk `5161332` offsets `614-623`; context: A palpable and overriding error is an error that, in its undeniability -- and therefore not a difference of opinion on the assessment of the evidence --, determines the outcome of the dispute in that the conclusion of the trier of fact, that is, the result of his or her decision, cannot hold water, thus, ipso facto, making the decision unreasonable.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5161332` offsets `817-823`; context: A palpable and overriding error is an error that, in its undeniability -- and therefore not a difference of opinion on the assessment of the evidence --, determines the outcome of the dispute in that the conclusion of the trier of fact, that is, the result of his or her decision, cannot hold water, thus, ipso facto, making the decision unreasonable.

#### 24696:1:subtheme:5 · paragraphs 27-32

- Raw key terms: `appeal, decision, court, tribunal, error, judicial, overriding, palpable`
- Display key terms: `error, judicial, overriding, palpable`
- Argument roles: `counterargument_limitation, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, reasoning_application Display terms: error, judicial, overriding, palpable Application context: However, this is the appellate-level standard of intervention that a specialized appeal tribunal such as the RAD must apply when reviewing a decision and not the judicial review standard of reasonableness. Evidence spans paragraphs 27-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5161333` offsets `43-51`; context: [27] In the matter at bar, even though the question raised concerns a different appeal tribunal from the one in Parizeau, the reasoning of the Court of Appeal of Quebec is highly relevant.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5161333` offsets `418-424`; context: It cannot engage in a form of judicial review as the Member did in this case.
- Evidence: `issue` cue `whether` at chunk `5161334` offsets `541-548`; context: When analyzing a decision of the RPD, the RAD must not merely determine whether it was made in a reasonable manner, but, rather, analyze whether the RPD relied on a wrong principle of law or misassessed the facts to the point of making a palpable and overriding error (Housen, above).
- Evidence: `counterargument_limitation` cue `but` at chunk `5161334` offsets `585-588`; context: When analyzing a decision of the RPD, the RAD must not merely determine whether it was made in a reasonable manner, but, rather, analyze whether the RPD relied on a wrong principle of law or misassessed the facts to the point of making a palpable and overriding error (Housen, above).
- Evidence: `reasoning_application` cue `apply` at chunk `5161335` offsets `243-248`; context: However, this is the appellate-level standard of intervention that a specialized appeal tribunal such as the RAD must apply when reviewing a decision and not the judicial review standard of reasonableness.
- Evidence: `counterargument_limitation` cue `However` at chunk `5161335` offsets `125-132`; context: However, this is the appellate-level standard of intervention that a specialized appeal tribunal such as the RAD must apply when reviewing a decision and not the judicial review standard of reasonableness.
- Evidence: `counterargument_limitation` cue `but` at chunk `5161337` offsets `119-122`; context: In all of these cases, the specialization of the decision-maker, a factor that exists at the administrative but not at the judicial level, weighs in favour of the judicial appellate body showing a measure of deference to the administrative decision-maker.

#### 24696:1:subtheme:6 · paragraphs 33-33

- Raw key terms: `abdul, admin, body, canada, case, citizenship, emergency, follows`
- Display key terms: `abdul, admin, body, case, emergency, follows`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: abdul, admin, body, case, emergency, follows Evidence spans paragraphs 33-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5161339` offsets `53-58`; context: [32] This case law is all the more important for the issue in this case, as it refuses to give subsection 67(2) the meaning that the IAD has similar jurisdiction as that of a judicial review body (see Canada (Minister of Citizenship and Immigration) v Abdul, 2009 FC 967, 3 Admin LR (5th) 181; Mendoza v Canada (Minister of Public Safety and Emergency Preparedness), 2007 FC 934).

#### 24696:1:subtheme:7 · paragraphs 34-36

- Raw key terms: `applicant, role, above, added, adopt, ahir, appeal, approach`
- Display key terms: `role, above, added, adopt, ahir, approach`
- Argument roles: `governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, party_position, reasoning_application Display terms: role, above, added, adopt, ahir, approach Position/evidence statements: [28] The applicant submits that the only role of the IAD in a challenge of the legal validity of the visa officer’s decision is to determine the reasonableness of the officer’s decision on excessive demand at the time th Rule/authority context: [29] In my view the applicant has mischaracterized the role of the IAD in an appeal under subsection 67(2) of IRPA. Application context: The IAD therefore exceeded its jurisdiction by not limiting itself to assessing the reasonableness of the officer’s decision at the time it was made. Evidence spans paragraphs 34-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submits` at chunk `5161340` offsets `19-26`; context: [28] The applicant submits that the only role of the IAD in a challenge of the legal validity of the visa officer’s decision is to determine the reasonableness of the officer’s decision on excessive demand at the time that the decision is made.
- Evidence: `reasoning_application` cue `therefore` at chunk `5161340` offsets `253-262`; context: The IAD therefore exceeded its jurisdiction by not limiting itself to assessing the reasonableness of the officer’s decision at the time it was made.
- Evidence: `governing_rule` cue `under` at chunk `5161341` offsets `84-89`; context: [29] In my view the applicant has mischaracterized the role of the IAD in an appeal under subsection 67(2) of IRPA.

#### 24696:1:subtheme:8 · paragraphs 37-38

- Raw key terms: `hearing, above, acceptable, adjudges, advantage, against, agrees, allowed`
- Display key terms: `hearing, above, acceptable, adjudges, advantage, against, agrees, allowed`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue Display terms: hearing, above, acceptable, adjudges, advantage, against, agrees, allowed Operative outcome context: Conclusion [34] For all of the above reasons, the applicants’ application for judicial review is allowed and the matter is referred back for reconsideration by a differently constituted panel of the RAD. Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5161343` offsets `448-455`; context: However, the RAD must nonetheless perform its own assessment of all of the evidence in order to determine whether the RPD relied on a wrong principle of law or misassessed the facts to the point of making a palpable and overriding error.
- Evidence: `evidence_fact` cue `testimony` at chunk `5161343` offsets `305-314`; context: The RPD is better situated to draw such conclusions as it is the tribunal of first instance, the trier of facts, having the advantage of hearing testimony viva voce (Housen, above).
- Evidence: `counterargument_limitation` cue `However` at chunk `5161343` offsets `342-349`; context: However, the RAD must nonetheless perform its own assessment of all of the evidence in order to determine whether the RPD relied on a wrong principle of law or misassessed the facts to the point of making a palpable and overriding error.
- Evidence: `disposition` cue `allowed` at chunk `5161343` offsets `1199-1206`; context: Conclusion [34] For all of the above reasons, the applicants’ application for judicial review is allowed and the matter is referred back for reconsideration by a differently constituted panel of the RAD.

#### Section text

Alvarez v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2014-07-17
Neutral citation
2014 FC 702
File numbers
IMM-7218-13
Decision Content
Date: 20140717
Docket: IMM-7218-13
Citation: 2014 FC 702
[UNREVISED ENGLISH CERTIFIED TRANSLATION]
Montréal, Quebec, July 17, 2014
PRESENT: Shore J.
BETWEEN:
ISMAEL GARCIA ALVAREZ
PILAR DE LA CARIDAD MORENO FLEITES
Applicants
and
MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Preliminary remarks [1] To quote Einstein, if you can’t explain it to a 12-year-old, you don’t understand it yourself. A great deal of ink and hundreds of words will be wasted unless we ensure that we understand the crux of the matter we are discussing and clarify the role of the Refugee Appeal Division [RAD]. The essence of the case before the Court is the following: which entity does what, when, and according to which principles of the legislation and the case law?

[2] What is the RAD’s role in relation to the Refugee Protection Division [RPD] and to the Federal Court?

[3] The RAD is a specialized quasi-judicial body, whose members have the powers of a commissioner under section 111 of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA].

[4] If the RPD does not provide reasons in its assessment of the evidence, the RAD must intervene following its own review; if the RPD misinterprets the legislation, the RAD must also intervene.

[5] The Court notes that the anatomy of the RAD depends on its jurisdiction, and its jurisdiction depends entirely on the statute that has given it its mandate to exist and to act as a specialized quasi-judicial tribunal that also has the authority to investigate, an authority the Federal Court judge (like the Immigration Appeal Division [IAD]).does not have
II. Introduction [6] This is an application for judicial review made under subsection 72(1) of the IRPA of a decision by the RAD of the Immigration and Refugee Board dated October 18, 2013, dismissing the applicants’ appeal of the RPD’s decision denying their claim to be recognized as Convention refugees or persons in need of protection under sections 96 and 97 of the IRPA.
III. Facts [7] The principal applicant, Ismael Garcia Alvarez, and his wife, Pilar de la Caridad Moreno Fleites, are citizens of Cuba. They both arrived in Canada on January 27, 2013, and claimed refugee protection on February 15, 2013.

[8] On July 10, 2013, the RPD rejected their refugee protection claim deeming that they had failed to establish a serious possibility of persecution within the meaning of section 96 of the IRPA or the existence of dangers or risks within the meaning of section 97 of the IRPA.

[9] The applicants appealed this decision before the RAD. The RAD dismissed this appeal on October 18, 2013.

[10] On November 12, 2013, the applicant filed this application for judicial review against that decision.
IV. Decision under review [11] First, the RAD noted that there was no need to hold a hearing in the present matter since the applicants had not presented any new evidence according to the requirements of subsection 110(4).

[12] The RAD went on to examine the RAD’s role as an appeal tribunal and the standard of review applicable to questions of fact and questions of mixed fact and law as well as to pure questions of law. Relying on the decision in Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399, the RAD stated that, except for questions of law or questions of natural justice, the members of the RAD had to show deference to the decisions of the RPD by applying the standard of reasonableness. The RPD is better situated to make factual findings owing to its extensive exposure to the evidence, the advantage of hearing testimony viva voce, and its familiarity with the case as a whole (Housen v Nikolaisen, 2002 SCC 33, [2002] 2 SCR 235). The RAD’s analysis must therefore be concerned with the justification, transparency and intelligibility within the decision-making process and not be a reassessment of the evidence.

[13] Regarding the merits of the appeal, the RAD determined that the RPD did not err in its application to the facts of the concept of persecution. The RAD noted that the RPD reasonably concluded that the problems experienced by the applicants did not rise to the level required to constitute persecution. It therefore concluded that their fear of being persecuted should they have to return to live in Cuba was not in fact a reasonable fear.
V. Issue [14] Did the RAD err in applying the standard of reasonableness to the RPD’s findings?
VI. Relevant statutory provisions [15] The following provisions of the IRPA are applicable in these proceedings:
110. (3) Subject to subsections (3.1), (4) and (6), the Refugee Appeal Division must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division, and may accept documentary evidence and written submissions from the Minister and the person who is the subject of the appeal and, in the case of a matter that is conducted before a panel of three members, written submissions from a representative or agent of the United Nations High Commissioner for Refugees and any other person described in the rules of the Board.
110. (3) Sous réserve des paragraphes (3.1), (4) et (6), la section procède sans tenir d’audience en se fondant sur le dossier de la Section de la protection des réfugiés, mais peut recevoir des éléments de preuve documentaire et des observations écrites du ministre et de la personne en cause ainsi que, s’agissant d’une affaire tenue devant un tribunal constitué de trois commissaires, des observations écrites du représentant ou mandataire du Haut-Commissariat des Nations Unies pour les réfugiés et de toute autre personne visée par les règles de la Commission.
…
[…]
(4) On appeal, the person who is the subject of the appeal may present only evidence that arose after the rejection of their claim or that was not reasonably available, or that the person could not reasonably have been expected in the circumstances to have presented, at the time of the rejection.
(4) Dans le cadre de l’appel, la personne en cause ne peut présenter que des éléments de preuve survenus depuis le rejet de sa demande ou qui n’étaient alors pas normalement accessibles ou, s’ils l’étaient, qu’elle n’aurait pas normalement présentés, dans les circonstances, au moment du rejet.
…
[…]
(6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
(6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause;
(b) that is central to the decision with respect to the refugee protection claim; and
b) sont essentiels pour la prise de la décision relative à la demande d’asile;
(c) that, if accepted, would justify allowing or rejecting the refugee protection claim.
c) à supposer qu’ils soient admis, justifieraient que la demande d’asile soit accordée ou refusée, selon le cas.
…
[…]
111. (1) After considering the appeal, the Refugee Appeal Division shall make one of the following decisions:
111. (1) La Section d’appel des réfugiés confirme la décision attaquée, casse la décision et y substitue la décision qui aurait dû être rendue ou renvoie, conformément à ses instructions, l’affaire à la Section de la protection des réfugiés.
(a) confirm the determination of the Refugee Protection Division;
(b) set aside the determination and substitute a determination that, in its opinion, should have been made; or
(c) refer the matter to the Refugee Protection Division for re-determination, giving the directions to the Refugee Protection Division that it considers appropriate.
Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
b) qu’elle ne peut confirmer la décision attaquée ou casser la décision et y substituer la décision qui aurait dû être rendue sans tenir une nouvelle audience en vue du réexamen des éléments de preuve qui ont été présentés à la Section de la protection des réfugiés.
…
[…]
162. (1) Each Division of the Board has, in respect of proceedings brought before it under this Act, sole and exclusive jurisdiction to hear and determine all questions of law and fact, including questions of jurisdiction.
162. (1) Chacune des sections a compétence exclusive pour connaître des questions de droit et de fait — y compris en matière de compétence — dans le cadre des affaires dont elle est saisie.
VII. Standard of review [16] The issue before the Court in this case is whether the RAD erred in its choice of which standard of review to apply against the RPD’s decision.

[17] A reviewing court may avoid a full standard of review analysis if previous jurisprudence has satisfactorily resolved the issue (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190, at paras 57 and 62). In the matter at bar, the Court does not find that a full standard of review analysis is required since the Court has repeatedly held that the standard of review for such questions of law is that of correctness (Budhai v Canada (Attorney General), 2002 FCA 298, [2003] 2 FC 57, at para 22; Canada (Attorney General) v Hunter, 2013 FCA 12 at para 4; see also Edmonton (Police Service) v Furlong, 2013 ABCA 121, 50 Admin LR (5th) 259).
VIII. Positions of the parties [18] The applicant submits that the RAD’s decision is unreasonable since the RAD analyzed the RPD’s decision as part of a standard of review analysis. The applicants argue that the RAD should rather have performed its own legal analysis of the facts and not simply reiterate the RPD’s decision without exercising its jurisdiction in this regard.

[19] The applicants submit that Parliament, in creating the RAD, intended to create an appeal division with broad, unlimited jurisdiction; restricting the RAD’s review powers would amount to reproducing the work already being done by the Federal Court.

[20] In turn, the respondent argues that the statement of the RAD that its role is not to reassess the evidence is entirely consistent with the standard of reasonableness. According to the respondent, the RAD’s role is not to reassess the evidence, but to determine whether, in light of the evidence, the decision rendered is within a range of possible, acceptable outcomes. In relation to the RPD, the RAD does not have any special expertise when it comes to interpreting the facts or the evidence. The RAD’s expertise is to dispose of pure questions of law. Consequently, the RAD must review the RPD’s decision against a standard of reasonableness.
IX. Analysis [21] The question of law raised in this matter is the following: against which standard of review are the RPD’s findings of facts reviewable before the RAD?. Apart from the brief conclusion on this topic in a recent decision, Iyamuremye v Canada (Minister of Citizenship and Immigration), 2014 FC 494, at paragraph 40, there are no decisions to date that analyze in depth the standard of review applicable to decisions before the RAD.

[22] To identify the appropriate standard of review for the RAD’s examination of decisions of the RPD, the first question is what jurisdiction the RAD has.

[23] In applying the rules of interpretation to the relevant provisions in this matter (Rizzo & Rizzo Shoes Ltd, [1998] 1 SCR 27), such as to subsection 111(1) of the IRPA, the Court agrees with the applicants that Parliament seems to have wanted to confer a broad power of intervention on the RAD, thus allowing the RAD to dispose of the merits of appeals and not only to determine whether the RPD’s decision was made in a reasonable manner as submitted by the Member in the present matter.

[24] Subsection 111(1) defines the RAD’s jurisdiction in the following terms:
After considering the appeal, the Refugee Appeal Division shall make one of the following decisions:
(a) confirm the determination of the Refugee Protection Division;
(b) set aside the determination and substitute a determination that, in its opinion, should have been made; or
(c) refer the matter to the Refugee Protection Division for redetermination, giving the directions to the Refugee Protection Division that it considers appropriate. [Emphasis added.]

[25] The Court agrees that an appeal before the RAD is not an appeal de novo; the IRPA restricts the power of the RAD, in comparison to that of the IAD, to considering new evidence and to holding a hearing only in exceptional cases (see subsections 110(4) and 110(6) of the IRPA). However, the Court cannot accept that, as a result of these limitations, Parliament intended to confer on the RAD a similar jurisdiction as to that of a judicial review body. The Court does not feel that Parliament had such a restriction in mind. In this regard, the Court finds the reasoning in Parizeau c Barreau du Québec, 2011 QCCA 1498, [2011] RJQ 1506, presented by the applicants in support of their application, persuasive and instructive (the Supreme Court of Canada dismissed the application for leave to appeal from this judgment on March 15, 2012: 2012 CanLII 12782 (SCC)).

[26] In Parizeau, above, the Court of Appeal of Quebec made the following observations on the standard of intervention to be applied by administrative appeal tribunals:
[translation]

[63] The Tribunal des professions sided with this approach and now applies the analytical process for judicial review when identifying its intervention standard. Indeed, this is what it did in the present case.

[64] With the greatest respect, this view of the appeal role of the Tribunal des professions raises serious questions, as the Court itself noted in Laliberté c. Huneault.
. . .

[75] Having said that, if these instructions apply when the legislator has provided for the right to appeal the decision of a specialized administrative tribunal before a generalized court (and that is what all these decisions of the Supreme Court are concerned with), do they also apply when the hearing of the appeal is assigned to another, also specialized, administrative body? In the first case, in fact, the dynamics of administrative law find full expression, and the distinction between specialized administrative tribunals, to which Parliament has given the expert task of developing standards in a particular area, and the generalized courts, the guardians of the rule of law, as pointed out earlier (see para. 69), dictates that the matter be dealt with according to the rules of judicial review. Do these dynamics and the resulting requirement come into the play in the second case, however, when the appeal body is also an administrative one? The reasons that justify the deference shown by the courts to specialized administrative tribunals, reasons that flow from the organization and the respective role of the executive and judicial branches of government and respect for legislative intent, are hardly persuasive when the appeal body is also an administrative tribunal and it, too, has a specialized mandate. The case at bar is a good illustration of this.
. . .

[78] All of this, and primarily legislative intent, not to mention the protection of the litigants to whom recourse is available, weighs against treating appeals before the Tribunal des professions as a form of judicial review and also weighs against developing a policy of deference the effect of which would be to turn appeals before this tribunal into pseudo-judicial reviews. In our opinion, the Tribunal des professions does exercise an appeal function and jurisdiction.
. . .

[81] The Supreme Court and this Court have repeatedly instructed the following: the appeal tribunal may in principle rectify any error in law in the decision under appeal or any palpable and overriding error in the determination of the facts or in the application of the law (if it was correctly identified) to the facts. This standard is just as valid for appeals brought before administrative tribunals, and the standard of intervention developed for judicial review can certainly be transposed to quasi-judicial appeals, with the limitations and adjustments imposed by the particular legislation applicable to each case and according to the general rules of administrative law.

[82] This then is the standard against which the Tribunal des professions must examine the decisions before it under appeal. What is more, this is how, for example, the decisions of the Tribunal du travail, when it still existed and sat in appeal on the decisions of the labour commissioners, were approached: see, for example, Vallée c. Hôpital Jean-Talon and Syndicat des enseignants et enseignantes de la banlieue de Québec c. Commission scolaire des Chutes de la Chaudière.
. . .

[89] . . . There is nothing surprising in this: every time a tribunal of first instance (be it judicial or administrative) has considerable discretion over a certain matter, the appeal tribunal commonly shows increased deference.

[90] However, if the assessing decision is made on the basis of incorrect findings of fact, the Tribunal des professions can intervene to rectify these errors, if they influence the outcome of the dispute, and “render the decision it considers should have been rendered in first instance” (article 182.6 of the Professional Code). Moreover, the Tribunal would also be justified in intervening if the final assessing decision made by the Applications Committee does not agree with the facts revealed by the evidence. In both instances, in fact, a palpable and overriding error warranting the Tribunal’s intervention was made. Denying the Tribunal des professions the opportunity, and even the duty, to intervene in such circumstances would be tantamount to allowing the Applications Committee to act in an arbitrary, and not only discretionary, manner, which would violate a principle of fundamental justice. Even if it is true that the entry or re-entry of a person on the Roll of the Order of Advocates is not automatic, it is also not an outright privilege the granting of which can be denied in an authoritarian or capricious manner.

[91] In the end, this is the reading that must be made of the Brousseau decision, while considering how the case law of recent years has developed and adjusted the appellate intervention standard and, particularly, the concept of “palpable and overriding error” with regard to the facts. In this respect, see, for example, H.L. v. Canada (Attorney General), rendered in 2005, Regroupement des CHSLD Christ-Roy (Centre hospitalier, soins longue durée) c. Comité provincial des malades, at para. 55, and P. L. c. Benchetrit, at para. 24. A palpable and overriding error is an error that, in its undeniability -- and therefore not a difference of opinion on the assessment of the evidence --, determines the outcome of the dispute in that the conclusion of the trier of fact, that is, the result of his or her decision, cannot hold water, thus, ipso facto, making the decision unreasonable. [Emphasis added.]

[27] In the matter at bar, even though the question raised concerns a different appeal tribunal from the one in Parizeau, the reasoning of the Court of Appeal of Quebec is highly relevant. As in Parizeau, the Court is of the view that the RAD must be a

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 24696:2 · paragraphs 39-39

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `abddcb586e826dac8e5d6c719606b6e3e57b342768bae51addafaf0334e0a972`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24696:2:subtheme:1 · paragraphs 39-39

- Raw key terms: `appearances, applicants, attorney, canada, cormie, dated, deputy, general`
- Display key terms: `cormie, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: cormie, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 39-39. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
SHORE J.
DATED:
JULY 17, 2014
APPEARANCES:
Stéphanie Valois
FOR THE APPLICANTS
Thomas Cormie
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Stéphanie Valois
Lawyer
Montréal, Quebec
FOR THE APPLICANTS
William F. Pentney
Deputy Attorney General of Canada
Montréal, Quebec
FOR THE RESPONDENT
