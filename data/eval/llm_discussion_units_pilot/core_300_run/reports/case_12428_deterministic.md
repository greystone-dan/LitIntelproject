# Discussion Units: case 12428

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **36**
- Continuity pairs: **35**
- Discussion Units: **4**
- Paragraph source hashes: **36**
- Sub-themes: **10**

## 12428:1 · paragraphs 0-16

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f0ca2ea8780073e147d57404d4c907e3b0debd2bc26567b595154fbfdd50c9f0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12428:1:subtheme:1 · paragraphs 0-7

- Raw key terms: `applicant, decision, husband, march, political, appeal, because, cambodia`
- Display key terms: `husband, march, political, because, cambodia`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: husband, march, political, because, cambodia Position/evidence statements: They claimed refugee protection soon after. Rule/authority context: Introduction [1] This is an application for leave to commence an application for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] of a decision of Stephen J. Application context: [3] She is at risk of persecution because of her husband’s political activities. | RPD Decision [8] In its decision dated August 15, 2013, the RPD denied the Applicant’s refugee claim because it did not find the Applicant’s allegations of persecution of her husband, and by extension to herself, credibl Operative outcome context: Gallagher of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board of Canada, dated March 19, 2014, which upheld the decision of the Refugee Protection Division [RPD] determining that the Applicant was n | RPD Decision [8] In its decision dated August 15, 2013, the RPD denied the Applicant’s refugee claim because it did not find the Applicant’s allegations of persecution of her husband, and by extension to herself, credibl Evidence spans paragraphs 0-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4620423` offsets `521-532`; context: Introduction [1] This is an application for leave to commence an application for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] of a decision of Stephen J.
- Evidence: `disposition` cue `upheld` at chunk `4620423` offsets `766-772`; context: Gallagher of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board of Canada, dated March 19, 2014, which upheld the decision of the Refugee Protection Division [RPD] determining that the Applicant was neither a Convention Refugee nor a person in need of protection within the meaning of sections 96 and 97 of IRPA.
- Evidence: `reasoning_application` cue `because` at chunk `4620424` offsets `34-41`; context: [3] She is at risk of persecution because of her husband’s political activities.
- Evidence: `party_position` cue `claimed` at chunk `4620428` offsets `125-132`; context: They claimed refugee protection soon after.
- Evidence: `reasoning_application` cue `because` at chunk `4620428` offsets `324-331`; context: RPD Decision [8] In its decision dated August 15, 2013, the RPD denied the Applicant’s refugee claim because it did not find the Applicant’s allegations of persecution of her husband, and by extension to herself, credible.
- Evidence: `disposition` cue `denied` at chunk `4620428` offsets `287-293`; context: RPD Decision [8] In its decision dated August 15, 2013, the RPD denied the Applicant’s refugee claim because it did not find the Applicant’s allegations of persecution of her husband, and by extension to herself, credible.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620430` offsets `123-131`; context: Contested Decision [11] The Applicant did not present new evidence nor did she request an oral hearing.

#### 12428:1:subtheme:2 · paragraphs 8-16

- Raw key terms: `applicant, decision, review, appeal, applied, fact, irpa, respondent`
- Display key terms: `review, applied, fact, irpa`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: review, applied, fact, irpa Position/evidence statements: Parties’ Submissions [16] The Applicant first submits that the applicable standard of review to be applied by the RAD is that of correctness and not of reasonableness. | [17] The Respondent argues, however, that the RAD applied the correct standard of review, namely reasonableness, because, as per sections 110 and 111 of IRPA, the RAD may allow an appeal if it is satisfied that there is  Rule/authority context: [12] The RAD first discusses the applicable standard of review to the RPD decision. | The RAD is of the opinion that the RPD reasonably concluded that the Applicant had not shown, on a balance of probabilities, that her or her husband had been targeted by the Cambodian People’s Party [CPP] and that the Ap Application context: According to the RAD, its assessment of the RPD determination of the Applicant’s credibility attracts the reasonableness standard, as applied by the Federal Court in evaluating RPD decisions related to credibility. | [15] The RAD finally concludes that the RPD analysis of the Applicant’s testimony and corroborative evidence reasonable. Evidence spans paragraphs 8-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4620431` offsets `479-486`; context: The RAD objective is therefore to “review the RPD decision for the “existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and the law”.
- Evidence: `governing_rule` cue `standard of review` at chunk `4620431` offsets `44-62`; context: [12] The RAD first discusses the applicable standard of review to the RPD decision.
- Evidence: `reasoning_application` cue `applied` at chunk `4620431` offsets `218-225`; context: According to the RAD, its assessment of the RPD determination of the Applicant’s credibility attracts the reasonableness standard, as applied by the Federal Court in evaluating RPD decisions related to credibility.
- Evidence: `issue` cue `issue` at chunk `4620432` offsets `29-34`; context: [13] The RAD frames the core issue of its review as follows: did the RPD reach a conclusion on the credibility of the claimant, which is “unreasonable”?
- Evidence: `governing_rule` cue `under` at chunk `4620432` offsets `620-625`; context: The RAD is of the opinion that the RPD reasonably concluded that the Applicant had not shown, on a balance of probabilities, that her or her husband had been targeted by the Cambodian People’s Party [CPP] and that the Applicant and her husband’s travel are inconsistent with what would be expected if they were in fact at risk of persecution or persons in need of protection under sections 96 and 97 of IRPA.
- Evidence: `party_position` cue `submits` at chunk `4620434` offsets `339-346`; context: Parties’ Submissions [16] The Applicant first submits that the applicable standard of review to be applied by the RAD is that of correctness and not of reasonableness.
- Evidence: `evidence_fact` cue `testimony` at chunk `4620434` offsets `72-81`; context: [15] The RAD finally concludes that the RPD analysis of the Applicant’s testimony and corroborative evidence reasonable.
- Evidence: `governing_rule` cue `standard of review` at chunk `4620434` offsets `367-385`; context: Parties’ Submissions [16] The Applicant first submits that the applicable standard of review to be applied by the RAD is that of correctness and not of reasonableness.
- Evidence: `reasoning_application` cue `concludes` at chunk `4620434` offsets `21-30`; context: [15] The RAD finally concludes that the RPD analysis of the Applicant’s testimony and corroborative evidence reasonable.
- Evidence: `party_position` cue `argues` at chunk `4620435` offsets `20-26`; context: [17] The Respondent argues, however, that the RAD applied the correct standard of review, namely reasonableness, because, as per sections 110 and 111 of IRPA, the RAD may allow an appeal if it is satisfied that there is an error of law, error of fact or error of mixed fact and law with the RPD decision.
- Evidence: `governing_rule` cue `standard of review` at chunk `4620435` offsets `70-88`; context: [17] The Respondent argues, however, that the RAD applied the correct standard of review, namely reasonableness, because, as per sections 110 and 111 of IRPA, the RAD may allow an appeal if it is satisfied that there is an error of law, error of fact or error of mixed fact and law with the RPD decision.
- Evidence: `reasoning_application` cue `applied` at chunk `4620435` offsets `50-57`; context: [17] The Respondent argues, however, that the RAD applied the correct standard of review, namely reasonableness, because, as per sections 110 and 111 of IRPA, the RAD may allow an appeal if it is satisfied that there is an error of law, error of fact or error of mixed fact and law with the RPD decision.
- Evidence: `party_position` cue `submits` at chunk `4620436` offsets `27-34`; context: [18] The Applicant further submits that the RAD erred when it went beyond the content of the RPD decision and looked at the documentation pertaining to the political situation in Cambodia as this was not addressed in the RPD decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620437` offsets `117-125`; context: [19] The Respondent replies by saying that the RAD did not err by referring to the country documentation included in evidence before the RPD.
- Evidence: `governing_rule` cue `standard of review` at chunk `4620438` offsets `109-127`; context: [21] In terms of new arguments, the Respondent first states that in the event that the RAD applied the wrong standard of review with respect to the credibility of the Applicant under appeal, it has no bearing on the results, which in turn means that it would be useless to send the matter back to be re-examined.
- Evidence: `reasoning_application` cue `applied` at chunk `4620438` offsets `91-98`; context: [21] In terms of new arguments, the Respondent first states that in the event that the RAD applied the wrong standard of review with respect to the credibility of the Applicant under appeal, it has no bearing on the results, which in turn means that it would be useless to send the matter back to be re-examined.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620439` offsets `308-316`; context: [22] The Respondent adds that Justice Shore’s decisions in Eng v Canada (Minister of Citizenship and Immigration), 2014 FC 711 [Eng] and Alvarez v Canada (Minister of Citizenship and Immigration), 2014 FC 702 [Alvarez] suggesting that the RAD must conduct its own independent analysis of the totality of the evidence that was before the RPD and come to its own conclusions contradict the wording of section 110 of IRPA, since this section created a right of appeal for certain refugee claimants, where the appellant before the RAD has the burden to raise specific questions of fact, of law or of mixed law and fact.

#### Section text

Yin v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2014-12-12
Neutral citation
2014 FC 1209
File numbers
IMM-2845-14
Decision Content
Date: 20141212
Docket: IMM-2845-14
Citation: 2014 FC 1209
Ottawa, Ontario, December 12, 2014
PRESENT: The Honourable Mr. Justice S. Noël
BETWEEN:
SAROM YIN
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Introduction [1] This is an application for leave to commence an application for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] of a decision of Stephen J. Gallagher of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board of Canada, dated March 19, 2014, which upheld the decision of the Refugee Protection Division [RPD] determining that the Applicant was neither a Convention Refugee nor a person in need of protection within the meaning of sections 96 and 97 of IRPA.
II. Facts [2] The Applicant is a 57 year old citizen of Cambodia.

[3] She is at risk of persecution because of her husband’s political activities.

[4] The Applicant’s husband was beaten by thugs on June 2, 2012 after his decision to stand for elected office for the Cambodian National Rescue Party [CNRP].

[5] Following the accusations from the police that he was holding illegal political meetings at his home, he was forced into retirement from his public service job at the Ministry of Finance and Economy.

[6] The Applicant’s husband received a number of high ranking members of the CNRP at his residence in March 2013. Four policemen came and threatened to charge him with the crime of holding an illegal political meeting.

[7] The Applicant and her husband fled Cambodia and arrived on May 22, 2013 in Canada, where their three children live. They claimed refugee protection soon after. The Applicant’s husband passed away on June 20, 2013.
III. RPD Decision [8] In its decision dated August 15, 2013, the RPD denied the Applicant’s refugee claim because it did not find the Applicant’s allegations of persecution of her husband, and by extension to herself, credible.

[9] The Applicant filed an appeal of this decision to the RAD on December 9, 2013.

[10] The RAD rendered a negative decision on March 26, 2014.
IV. Contested Decision [11] The Applicant did not present new evidence nor did she request an oral hearing.

[12] The RAD first discusses the applicable standard of review to the RPD decision. According to the RAD, its assessment of the RPD determination of the Applicant’s credibility attracts the reasonableness standard, as applied by the Federal Court in evaluating RPD decisions related to credibility. The RAD objective is therefore to “review the RPD decision for the “existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and the law”. This understanding flows from Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 [Dunsmuir]”.

[13] The RAD frames the core issue of its review as follows: did the RPD reach a conclusion on the credibility of the claimant, which is “unreasonable”? In answering this question, the RAD listed the different credibility findings the RPD made. The RAD is of the opinion that the RPD reasonably concluded that the Applicant had not shown, on a balance of probabilities, that her or her husband had been targeted by the Cambodian People’s Party [CPP] and that the Applicant and her husband’s travel are inconsistent with what would be expected if they were in fact at risk of persecution or persons in need of protection under sections 96 and 97 of IRPA.

[14] The RAD subsequently analyses the background documentation of the political situation in Cambodia and finds that the “general thrust of the background documentation is that there is significant corruption and cronyism in Cambodia, but little targeting of opponents […] which is inconsistent with the Applicant’s allegations” (RAD decision at para 6).

[15] The RAD finally concludes that the RPD analysis of the Applicant’s testimony and corroborative evidence reasonable. The RPD decision therefore “falls within the range of possible, acceptable outcomes which are defensible in respect of the facts and the law” (RAD decision at para 24).
V. Parties’ Submissions [16] The Applicant first submits that the applicable standard of review to be applied by the RAD is that of correctness and not of reasonableness. The Applicant grounds its position on the decision of The Halifax Regional Municipality v Anglican Diocesan Centre Corporation, 2010 NSCA 38, where the Court of Appeal stated that “the Board, itself an administrative tribunal under a statutory regime, does not immerse itself in Dunsmuir’s standard of review analysis that governs a court’s judicial review. The Board should do what the statute tells it to do”. The Applicant then states that based on sections 110, 111, 111.1, 171 of IRPA, section 159.91 of the Immigration and Refugee Protection Regulations, SOR/2002-227 and section 24 of the Refugee Appeal Division Rules, SOR/2012-257 [RAD Rules], the legislator intended for the RAD to apply a correctness standard, particularly because section 111 of IRPA states that the tribunal will refer a case back to the RPD for re-determination, only when it finds that the decision is wrong in fact or in mixed law and fact. Therefore, a right to an appeal and not a right to a judicial review was created. Therefore, because the RAD applied the wrong standard of review, the intervention of this Court is warranted.

[17] The Respondent argues, however, that the RAD applied the correct standard of review, namely reasonableness, because, as per sections 110 and 111 of IRPA, the RAD may allow an appeal if it is satisfied that there is an error of law, error of fact or error of mixed fact and law with the RPD decision. It can only substitute its opinion or return the matter for re-determination when such an error is made. The Respondent adds that an appeal to the RAD is a ““true appeal” in the sense that the appellate body is bound by the findings of fact and of mixed fact and law of a lower tribunal absent a demonstrable error” (Respondent’s memorandum at para 31). An appeal to the RAD is therefore not a hearing de novo.

[18] The Applicant further submits that the RAD erred when it went beyond the content of the RPD decision and looked at the documentation pertaining to the political situation in Cambodia as this was not addressed in the RPD decision. The Applicant also argues that the RAD erred by not providing the Applicant with a hearing to address its concerns about the political context in Cambodia.

[19] The Respondent replies by saying that the RAD did not err by referring to the country documentation included in evidence before the RPD. He is of the opinion that the Applicant did not demonstrate any reviewable error. Further, the RAD did not exceed its jurisdiction when it referred itself to the documentary evidence, as it was part of the RPD record.
VI. Defendant’s Further Memorandum [20] The Respondent begins by reiterating the same arguments as in their original submissions. A few new arguments are also added.

[21] In terms of new arguments, the Respondent first states that in the event that the RAD applied the wrong standard of review with respect to the credibility of the Applicant under appeal, it has no bearing on the results, which in turn means that it would be useless to send the matter back to be re-examined.

[22] The Respondent adds that Justice Shore’s decisions in Eng v Canada (Minister of Citizenship and Immigration), 2014 FC 711 [Eng] and Alvarez v Canada (Minister of Citizenship and Immigration), 2014 FC 702 [Alvarez] suggesting that the RAD must conduct its own independent analysis of the totality of the evidence that was before the RPD and come to its own conclusions contradict the wording of section 110 of IRPA, since this section created a right of appeal for certain refugee claimants, where the appellant before the RAD has the burden to raise specific questions of fact, of law or of mixed law and fact.

## 12428:2 · paragraphs 17-32

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5630c1918e44d2c8c52398f0d2c24da5088ee7588d30d30444ee3a09c2172725`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12428:2:subtheme:1 · paragraphs 17-18

- Raw key terms: `appeal, respondent, accordance, addition, adds, appellant, assess, because`
- Display key terms: `accordance, addition, adds, appellant, assess, because`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: accordance, addition, adds, appellant, assess, because Position/evidence statements: [23] The Respondent further submits that: “it should be noted that the subsection 110(1) indicated that the appeal must be in accordance with the RAD Rules of practice. Application context: [24] The Respondent also adds that because the RPD is the trier of fact at first instance, it has the benefit of seeing the claimant and witnesses, whereas an appeal to the RAD is, by contrast, a paper process. Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submits` at chunk `4620440` offsets `28-35`; context: [23] The Respondent further submits that:
“it should be noted that the subsection 110(1) indicated that the appeal must be in accordance with the RAD Rules of practice.
- Evidence: `evidence_fact` cue `record` at chunk `4620440` offsets `421-427`; context: In addition, RAD Rule 3(3)(g)(ii) imposes the onus on the appellant of identifying the specific location of the error within the RPD record.
- Evidence: `issue` cue `issues` at chunk `4620441` offsets `313-319`; context: The RPD is therefore in a better position than the RAD to assess testimonial, factual and evidentiary issues with perhaps the exception where the RAD holds a hearing.
- Evidence: `reasoning_application` cue `because` at chunk `4620441` offsets `35-42`; context: [24] The Respondent also adds that because the RPD is the trier of fact at first instance, it has the benefit of seeing the claimant and witnesses, whereas an appeal to the RAD is, by contrast, a paper process.

#### 12428:2:subtheme:2 · paragraphs 19-20

- Raw key terms: `appropriate, question, respondent, review, standard, states, appeal, apply`
- Display key terms: `appropriate, question, review, standard, states, apply`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: appropriate, question, review, standard, states, apply Rule/authority context: The RAD has the necessary degree of expertise to determine the appropriate standard of review to apply on appeal of a RPD decision. | This militates in favour of deference to the RAD on a question such as to the appropriate standard of review. Application context: [25] With regards of the role of the RAD on appeal of a RPD decision, the Respondent states that the RAD decision to apply the reasonableness standard in reviewing the RPD decision is a question closely tied to its funct Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4620442` offsets `186-194`; context: [25] With regards of the role of the RAD on appeal of a RPD decision, the Respondent states that the RAD decision to apply the reasonableness standard in reviewing the RPD decision is a question closely tied to its function and process.
- Evidence: `governing_rule` cue `standard of review` at chunk `4620442` offsets `554-572`; context: The RAD has the necessary degree of expertise to determine the appropriate standard of review to apply on appeal of a RPD decision.
- Evidence: `reasoning_application` cue `apply` at chunk `4620442` offsets `117-122`; context: [25] With regards of the role of the RAD on appeal of a RPD decision, the Respondent states that the RAD decision to apply the reasonableness standard in reviewing the RPD decision is a question closely tied to its function and process.
- Evidence: `issue` cue `question` at chunk `4620443` offsets `271-279`; context: This militates in favour of deference to the RAD on a question such as to the appropriate standard of review.
- Evidence: `governing_rule` cue `standard of review` at chunk `4620443` offsets `307-325`; context: This militates in favour of deference to the RAD on a question such as to the appropriate standard of review.

#### 12428:2:subtheme:3 · paragraphs 21-22

- Raw key terms: `credibility, decision, respondent, standard, applied, applies, argues, based`
- Display key terms: `credibility, standard, applied, applies, argues, based`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: credibility, standard, applied, applies, argues, based Position/evidence statements: [27] In the case at bar, the Respondent argues that because the RPD decision related to an issue of credibility, which is a question of fact, the reasonableness standard applies. | [28] The Respondent also submits that based on recent jurisprudence of this Court, even though the wrong standard of review has been applied by the RAD, deference is owed by the RAD to the RPD when it comes to questions  Rule/authority context: [28] The Respondent also submits that based on recent jurisprudence of this Court, even though the wrong standard of review has been applied by the RAD, deference is owed by the RAD to the RPD when it comes to questions  Application context: [27] In the case at bar, the Respondent argues that because the RPD decision related to an issue of credibility, which is a question of fact, the reasonableness standard applies. | [28] The Respondent also submits that based on recent jurisprudence of this Court, even though the wrong standard of review has been applied by the RAD, deference is owed by the RAD to the RPD when it comes to questions  Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4620444` offsets `91-96`; context: [27] In the case at bar, the Respondent argues that because the RPD decision related to an issue of credibility, which is a question of fact, the reasonableness standard applies.
- Evidence: `party_position` cue `argues` at chunk `4620444` offsets `40-46`; context: [27] In the case at bar, the Respondent argues that because the RPD decision related to an issue of credibility, which is a question of fact, the reasonableness standard applies.
- Evidence: `reasoning_application` cue `because` at chunk `4620444` offsets `52-59`; context: [27] In the case at bar, the Respondent argues that because the RPD decision related to an issue of credibility, which is a question of fact, the reasonableness standard applies.
- Evidence: `party_position` cue `submits` at chunk `4620445` offsets `25-32`; context: [28] The Respondent also submits that based on recent jurisprudence of this Court, even though the wrong standard of review has been applied by the RAD, deference is owed by the RAD to the RPD when it comes to questions of credibility.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4620445` offsets `54-67`; context: [28] The Respondent also submits that based on recent jurisprudence of this Court, even though the wrong standard of review has been applied by the RAD, deference is owed by the RAD to the RPD when it comes to questions of credibility.
- Evidence: `reasoning_application` cue `applied` at chunk `4620445` offsets `133-140`; context: [28] The Respondent also submits that based on recent jurisprudence of this Court, even though the wrong standard of review has been applied by the RAD, deference is owed by the RAD to the RPD when it comes to questions of credibility.

#### 12428:2:subtheme:4 · paragraphs 23-24

- Raw key terms: `appeal, applicant, apply, assessed, credibility, decision, findings, namely`
- Display key terms: `apply, assessed, credibility, findings, namely`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: apply, assessed, credibility, findings, namely Rule/authority context: Issues [30] The parties address two main issues in their submissions, namely the applicable standard of review the RAD should apply to the RPD decision on appeal and whether or not the RAD properly assessed the credibili | Standard of Review [32] Several judges of this Court have issued an opinion as to which standard of review this Court should apply to the scope of the review by the RAD on an appeal. Application context: Issues [30] The parties address two main issues in their submissions, namely the applicable standard of review the RAD should apply to the RPD decision on appeal and whether or not the RAD properly assessed the credibili | [31] Having reviewed the submissions, the RPD and the RAD decisions, I find that it will be necessary to deal only with the credibility findings as assessed by the RAD in light of the RPD analysis on these matters. Evidence spans paragraphs 23-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4620446` offsets `297-303`; context: Issues [30] The parties address two main issues in their submissions, namely the applicable standard of review the RAD should apply to the RPD decision on appeal and whether or not the RAD properly assessed the credibility findings of the Applicant.
- Evidence: `evidence_fact` cue `record` at chunk `4620446` offsets `284-290`; context: [29] Finally, the Respondent states that the RAD did not have to give notice to the Applicant that it might examine other documents than those referred to by the RPD in its decision, namely the US Country Reports on Human Rights Practices for Cambodia for 2012, which was part of the record.
- Evidence: `governing_rule` cue `standard of review` at chunk `4620446` offsets `389-407`; context: Issues [30] The parties address two main issues in their submissions, namely the applicable standard of review the RAD should apply to the RPD decision on appeal and whether or not the RAD properly assessed the credibility findings of the Applicant.
- Evidence: `reasoning_application` cue `apply` at chunk `4620446` offsets `423-428`; context: Issues [30] The parties address two main issues in their submissions, namely the applicable standard of review the RAD should apply to the RPD decision on appeal and whether or not the RAD properly assessed the credibility findings of the Applicant.
- Evidence: `issue` cue `issue` at chunk `4620447` offsets `241-246`; context: It will be seen that this issue is wholly determinative of the application for judicial review.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4620447` offsets `485-503`; context: Standard of Review [32] Several judges of this Court have issued an opinion as to which standard of review this Court should apply to the scope of the review by the RAD on an appeal.
- Evidence: `reasoning_application` cue `I find` at chunk `4620447` offsets `69-75`; context: [31] Having reviewed the submissions, the RPD and the RAD decisions, I find that it will be necessary to deal only with the credibility findings as assessed by the RAD in light of the RPD analysis on these matters.
- Evidence: `counterargument_limitation` cue `however` at chunk `4620447` offsets `1494-1501`; context: Other decisions state, however, the opposite, namely that this Court should perhaps apply the reasonableness standard when reviewing the standard of intervention chosen by the RAD in its review of a RPD decision (Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063 [Akuffo] at paras 16 to 26; Djossou, supra at para 18).

#### 12428:2:subtheme:5 · paragraphs 25-26

- Raw key terms: `appeal, case, court, present, regards, review, standard, adhere`
- Display key terms: `case, present, regards, review, standard, adhere`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: case, present, regards, review, standard, adhere Rule/authority context: [33] As such, the standard of review this Court should apply when reviewing the standard of intervention chosen by the RAD in its review of a RPD decision is undecided. | As it is well recognized, in such cases, the standard of review applicable is that of reasonableness. Application context: [33] As such, the standard of review this Court should apply when reviewing the standard of intervention chosen by the RAD in its review of a RPD decision is undecided. Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4620448` offsets `184-192`; context: As noted, this question is not determinative with regards to the case at bar.
- Evidence: `governing_rule` cue `standard of review` at chunk `4620448` offsets `18-36`; context: [33] As such, the standard of review this Court should apply when reviewing the standard of intervention chosen by the RAD in its review of a RPD decision is undecided.
- Evidence: `reasoning_application` cue `apply` at chunk `4620448` offsets `55-60`; context: [33] As such, the standard of review this Court should apply when reviewing the standard of intervention chosen by the RAD in its review of a RPD decision is undecided.
- Evidence: `issue` cue `issue` at chunk `4620449` offsets `395-400`; context: [35] In our case, the central issue raised by the appeal is the credibility of the Applicant.
- Evidence: `governing_rule` cue `standard of review` at chunk `4620449` offsets `177-195`; context: As it is well recognized, in such cases, the standard of review applicable is that of reasonableness.

#### 12428:2:subtheme:6 · paragraphs 27-32

- Raw key terms: `appeal, decision, applicant, evidence, review, application, assessment, based`
- Display key terms: `review, assessment, based`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: review, assessment, based Position/evidence statements: The Applicant submits that this is a reviewable error because the RAD exceeded its jurisdiction. | [41] The parties were invited to submit questions for certification and counsel for the Respondent did suggest the following: What is the scope of the Refugee Appeal Division’s review when considering an appeal of a deci Rule/authority context: In the case at bar, just as in Sajad, no new evidence was presented before the RAD to justify holding a hearing under subsection 110(6). Application context: He therefore rejects the application for judicial review. | [37] In the case at bar, in its decision, the RAD reiterates the RPD credibility conclusions and concludes that the RPD findings were reasonable. Operative outcome context: Conclusion [40] The application for judicial review is dismissed. Evidence spans paragraphs 27-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4620450` offsets `163-168`; context: [36] There are, at the moment, and to my knowledge, four decisions from this Court that maintain the RAD decisions confirming the RPD conclusions when the central issue was that of the credibility of the Applicant.
- Evidence: `evidence_fact` cue `testimony` at chunk `4620450` offsets `360-369`; context: In Njeukam v Canada (Minister of Citizenship and Immigration), 2014 FC 859, the RPD concluded that the Applicant lacked credibility based on her testimony.
- Evidence: `reasoning_application` cue `therefore` at chunk `4620450` offsets `643-652`; context: He therefore rejects the application for judicial review.
- Evidence: `counterargument_limitation` cue `However` at chunk `4620450` offsets `1995-2002`; context: However, in Djossou, supra, Justice Martineau states that he will not judicially impose on the RAD any degree of deference whatsoever to be applied to RPD decisions (at para 91).
- Evidence: `issue` cue `issues` at chunk `4620451` offsets `1179-1185`; context: Whatever the deference to be given by the RAD to RPD credibility findings, the RAD in this case looked at the evidence, dealt with the credibility issues raised by the appeal and concluded that the RPD credibility findings were sound, as its own assessment reveals.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620451` offsets `592-600`; context: The RAD notes that the Applicant’s allegations contradict this documentary evidence.
- Evidence: `reasoning_application` cue `concludes` at chunk `4620451` offsets `97-106`; context: [37] In the case at bar, in its decision, the RAD reiterates the RPD credibility conclusions and concludes that the RPD findings were reasonable.
- Evidence: `party_position` cue `submits` at chunk `4620452` offsets `266-273`; context: The Applicant submits that this is a reviewable error because the RAD exceeded its jurisdiction.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620452` offsets `190-198`; context: [38] The Applicant makes the argument that the RAD went beyond the decision of the RPD and found additional non-credibility reasons to maintain the RPD decision when it examined documentary evidence on Cambodia as they relate to the political context.
- Evidence: `reasoning_application` cue `because` at chunk `4620452` offsets `306-313`; context: The Applicant submits that this is a reviewable error because the RAD exceeded its jurisdiction.
- Evidence: `evidence_fact` cue `record` at chunk `4620453` offsets `166-172`; context: 1), (4) and (6), the Refugee Appeal Division must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division […]”.
- Evidence: `governing_rule` cue `under` at chunk `4620453` offsets `1015-1020`; context: In the case at bar, just as in Sajad, no new evidence was presented before the RAD to justify holding a hearing under subsection 110(6).
- Evidence: `reasoning_application` cue `therefore` at chunk `4620453` offsets `348-357`; context: The RAD could therefore refer to it in making its decision.
- Evidence: `counterargument_limitation` cue `but` at chunk `4620453` offsets `1390-1393`; context: The RAD found that: “the general thrust of the background documentation is that there is significant corruption and cronyism in Cambodia, but little targeting of opponents” which was inconsistent with the applicant’s allegations.
- Evidence: `disposition` cue `dismissed` at chunk `4620453` offsets `1682-1691`; context: Conclusion [40] The application for judicial review is dismissed.
- Evidence: `party_position` cue `submit` at chunk `4620454` offsets `33-39`; context: [41] The parties were invited to submit questions for certification and counsel for the Respondent did suggest the following:
What is the scope of the Refugee Appeal Division’s review when considering an appeal of a decision of the Refugee Protection Division?

#### Section text

[23] The Respondent further submits that:
“it should be noted that the subsection 110(1) indicated that the appeal must be in accordance with the RAD Rules of practice. RAD Rule 3(3)(g)(i) requires the appellant to outline the errors made by the RPD which form the grounds of the appeal. In addition, RAD Rule 3(3)(g)(ii) imposes the onus on the appellant of identifying the specific location of the error within the RPD record. Rule 9(2)(f) imposes a similar obligation on the Minister when he brings and appeal of an RPD decision to the RAD” (Respondent’s further memorandum at para 42).

[24] The Respondent also adds that because the RPD is the trier of fact at first instance, it has the benefit of seeing the claimant and witnesses, whereas an appeal to the RAD is, by contrast, a paper process. The RPD is therefore in a better position than the RAD to assess testimonial, factual and evidentiary issues with perhaps the exception where the RAD holds a hearing.

[25] With regards of the role of the RAD on appeal of a RPD decision, the Respondent states that the RAD decision to apply the reasonableness standard in reviewing the RPD decision is a question closely tied to its function and process. This issue is not a question of law of central importance to the legal system as a whole, it is not a “true jurisdictional issue” and is instead a question connected to the RAD home statute; as such the correctness standard should not apply. The RAD has the necessary degree of expertise to determine the appropriate standard of review to apply on appeal of a RPD decision.

[26] The Respondent further states that IRPA contains a privative clause at section 162, which gives each division of the Board, including the RAD, exclusive jurisdiction over questions of law, fact and jurisdiction. This militates in favour of deference to the RAD on a question such as to the appropriate standard of review.

[27] In the case at bar, the Respondent argues that because the RPD decision related to an issue of credibility, which is a question of fact, the reasonableness standard applies.

[28] The Respondent also submits that based on recent jurisprudence of this Court, even though the wrong standard of review has been applied by the RAD, deference is owed by the RAD to the RPD when it comes to questions of credibility. The RAD decision should thus stand, even if the wrong standard was applied.

[29] Finally, the Respondent states that the RAD did not have to give notice to the Applicant that it might examine other documents than those referred to by the RPD in its decision, namely the US Country Reports on Human Rights Practices for Cambodia for 2012, which was part of the record.
VII. Issues [30] The parties address two main issues in their submissions, namely the applicable standard of review the RAD should apply to the RPD decision on appeal and whether or not the RAD properly assessed the credibility findings of the Applicant.

[31] Having reviewed the submissions, the RPD and the RAD decisions, I find that it will be necessary to deal only with the credibility findings as assessed by the RAD in light of the RPD analysis on these matters. It will be seen that this issue is wholly determinative of the application for judicial review. Therefore, the question to be answered is as follows:
Did the RAD do a thorough analysis of the Applicant’s claim in light of the credibility findings made by the RPD?
VIII. Standard of Review [32] Several judges of this Court have issued an opinion as to which standard of review this Court should apply to the scope of the review by the RAD on an appeal. In Djossou c Canada (Ministre de la Citoyenneté et de l’Immigration), 2014 CF 1080 at para 18 [Djossou], Justice Martineau explains that many judges are of the opinion that the correctness standard applies (Iyamuremye v Canada (Minister of Citizenship and Immigration), 2014 FC 494 at para 20 [Iyamuremye]; Garcia Alvarez v Canada (Minister of Citizenship and Immigration), 2014 FC 702 at para 17 [Garcia Alvarez]; Eng v Canada (Minister of Citizenship and Immigration), 2014 FC 711 at para 18 [Eng]; Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 at paras 24 to 34 [Huruglica]; Yetna v Canada (Minister of Citizenship and Immigration), 2014 FC 858 [Yetna] at para 14; Spasoja c Canada (Ministre de la Citoyenneté et de l’Immigration), 2014 CF 913 at paras 7 to 9 [Spasoja]). Other decisions state, however, the opposite, namely that this Court should perhaps apply the reasonableness standard when reviewing the standard of intervention chosen by the RAD in its review of a RPD decision (Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063 [Akuffo] at paras 16 to 26; Djossou, supra at para 18).

[33] As such, the standard of review this Court should apply when reviewing the standard of intervention chosen by the RAD in its review of a RPD decision is undecided. As noted, this question is not determinative with regards to the case at bar. I therefore adhere to Justice Martineau’s approach in Djossou, supra at para 37, that until this question is resolved by the Federal Court of Appeal, a pragmatic approach should be used for the determination of the present judicial review.

[34] In the present appeal, the RAD is being asked to deal only with the credibility findings made by the RPD, as the appeal shows. As it is well recognized, in such cases, the standard of review applicable is that of reasonableness.
IX. Analysis A. Did the RAD do a thorough analysis of the Applicant’s appeal in light of the credibility findings made by the RPD? [35] In our case, the central issue raised by the appeal is the credibility of the Applicant. There is currently an ongoing trend in the jurisprudence from this Court with regards to the level of deference the RAD should give to RPD decisions when credibility is the heart of the matter.

[36] There are, at the moment, and to my knowledge, four decisions from this Court that maintain the RAD decisions confirming the RPD conclusions when the central issue was that of the credibility of the Applicant. In Njeukam v Canada (Minister of Citizenship and Immigration), 2014 FC 859, the RPD concluded that the Applicant lacked credibility based on her testimony. Justice Locke states that, in this case, it was right for the RAD to show deference to the RPD credibility finding (at para 19). Justice Locke further adds that the RAD seems to have conducted its own credibility analysis of the Applicant in its decision (at para 20). He therefore rejects the application for judicial review. In Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063, Justice Gagné states that she is of the opinion that “deference is only owed by the RAD to the RPD credibility findings and where the RPD enjoys a particular advantage in reaching its conclusion” (at para 39). Justice Gagné goes on to say that the RAD reviewed and assessed the evidence presented before the RPD and gave proper deference to the RPD credibility findings (at paras 46-48). She also notes that the RAD made its own assessment of the evidence and provided a more detailed analysis than the RPD with regards to the subjective fear of the Applicant of returning to his home country (at para 49). She therefore dismisses the application for judicial review (at para 50). In Allalou v Canada (Minister of Citizenship and Immigration), 2014 FC 1084, Justice Shore arrives at a similar conclusion, where he concludes that because the RPD decision was “solely founded on credibility, the RAD applied the appropriate level of deference towards the RPD determinations of the Applicant’s credibility” (at para 20). Justice Shore concludes, again, in Sajad c Canada (Ministre de la Citoyenneté et de l’Immigration), 2014 CF 1107 that the RAD validly exercised deference to the RPD credibility conclusions (at para 26). However, in Djossou, supra, Justice Martineau states that he will not judicially impose on the RAD any degree of deference whatsoever to be applied to RPD decisions (at para 91). Being prudent, Justice Martineau also does not speculate nor gives a definitive opinion as to the scope of the examination of a RPD decision on appeal to the RAD (Alyafi v Canada (Minister of Citizenship and Immigration), 2014 FC 952 at paras 51-52).

[37] In the case at bar, in its decision, the RAD reiterates the RPD credibility conclusions and concludes that the RPD findings were reasonable. A reading of the RAD decision shows that it read the transcript of the RPD hearing, the documentation filed and that it reassessed the credibility findings of the RPD. It even went further than the RPD in its analysis of the political context in Cambodia by comparing the Applicant’s allegations to the US Country Reports on Human Rights Practices for Cambodia for 2012. The RAD notes that the Applicant’s allegations contradict this documentary evidence. It is also based on this last evaluation that the RAD confirmed the RPD conclusions. The RAD assessment therefore goes further than simply confirming the RPD decision. The RAD conducted its own examination of the record before the RPD in making its decision. This situation is therefore very similar to the four cases identified above, where this Court confirmed the RAD decision and rejected the application for judicial review. Whatever the deference to be given by the RAD to RPD credibility findings, the RAD in this case looked at the evidence, dealt with the credibility issues raised by the appeal and concluded that the RPD credibility findings were sound, as its own assessment reveals. I, therefore, conclude that the RAD, by doing its review and own assessment of the evidence, did assume fully its role as an appellate tribunal and did show the required deference to the credibility findings made by the RPD.

[38] The Applicant makes the argument that the RAD went beyond the decision of the RPD and found additional non-credibility reasons to maintain the RPD decision when it examined documentary evidence on Cambodia as they relate to the political context. The Applicant submits that this is a reviewable error because the RAD exceeded its jurisdiction. She also argues that when she filed her appeal she did not know that she had to address matters not discussed in the RPD decision. She further submits that the RAD erred because it did not provide the Applicant with a hearing to address its concerns about the political context in Cambodia. I disagree with the Applicant for the reasons below.

[39] First, subsection 110(3) states that “Subject to subsections (3.1), (4) and (6), the Refugee Appeal Division must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division […]”. The documentation regarding the political context in Cambodia was part of the record before the RPD. The RAD could therefore refer to it in making its decision. Is it not the role of an appellate tribunal to look at the record and assess the evidence in light of the arguments made? Obviously, the answer is affirmative. The Applicant is also wrong in arguing that the RAD erred by not providing the Applicant with a hearing to address its concerns about the political context in Cambodia. As Justice Shore explains in Sajad, supra, a hearing can only be held before the RAD when an Applicant raises new documentary evidence as referred to in subsection 110(4) of IRPA. In the case at bar, just as in Sajad, no new evidence was presented before the RAD to justify holding a hearing under subsection 110(6). I also add that consulting the documentation was directly related to the arguments made on appeal. They are based on the Cambodia political climate which is not supported by some of the background documentation. The RAD found that: “the general thrust of the background documentation is that there is significant corruption and cronyism in Cambodia, but little targeting of opponents” which was inconsistent with the applicant’s allegations. The RAD, thus, committed no error by referring itself to the documentary evidence as part of the record of the RPD and not holding a hearing.
X. Conclusion [40] The application for judicial review is dismissed. I find reasonable the RAD assessment of the RPD credibility findings on appeal and I therefore conclude that the RAD has shown proper deference of the RPD credibility findings.

[41] The parties were invited to submit questions for certification and counsel for the Respondent did suggest the following:
What is the scope of the Refugee Appeal Division’s review when considering an appeal of a decision of the Refugee Protection Division?

[42] For the reasons mentioned above, it will not be necessary to deal with it.


## 12428:3 · paragraphs 33-34

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `341366d10f10591d528c450eccc0290fca5314e1b882d9461b8ddfa4565fbae3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12428:3:subtheme:1 · paragraphs 33-34

- Raw key terms: `application, cause, certified, citizenship, court, date, dated, december`
- Display key terms: `certified, date, dated, december`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: certified, date, dated, december Operative outcome context: Gallagher, dated March 19, 2014, is dismissed. Evidence spans paragraphs 33-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4620455` offsets `236-244`; context: No question of general importance will be certified.
- Evidence: `disposition` cue `dismissed` at chunk `4620455` offsets `222-231`; context: Gallagher, dated March 19, 2014, is dismissed.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that:
The application for judicial review of the decision of Stephen J. Gallagher, dated March 19, 2014, is dismissed. No question of general importance will be certified.
"Simon Noël"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-2845-14
STYLE OF CAUSE:
SAROM YIN v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Montréal, Quebec
DATE OF HEARING:
December 4, 2014


## 12428:4 · paragraphs 35-35

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4d399733dc12add4a958b9a8281280021d99e52d3789eaff03cf47cde4fa4657`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12428:4:subtheme:1 · paragraphs 35-35

- Raw key terms: `appearances, applicant, attorney, canada, dated, december, deputy, general`
- Display key terms: `dated, december, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: dated, december, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 35-35. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
NOËL S. J.
DATED:
December 12, 2014
APPEARANCES:
Styliani Markaki
For The Applicant
Michèle Joubert
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Styliani Markaki
Attorney
Montreal, Quebec
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
FOR THE RESPONDENT
