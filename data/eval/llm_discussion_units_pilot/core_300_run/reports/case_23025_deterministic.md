# Discussion Units: case 23025

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **27**
- Continuity pairs: **26**
- Discussion Units: **3**
- Paragraph source hashes: **27**
- Sub-themes: **8**

## 23025:1 · paragraphs 0-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3c080bf891b7a00034836763ff4bcf6bdd0006905580a6368d376c694ea01903`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23025:1:subtheme:1 · paragraphs 0-7

- Raw key terms: `applicant, account, following, friend, alleged, amendment, appeal, august`
- Display key terms: `account, following, friend, alleged, amendment, august`
- Argument roles: `evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position, reasoning_application Display terms: account, following, friend, alleged, amendment, august Position/evidence statements: The applicant also claims that he was beaten and reprimanded by his own family. | [7] In his initial account, the applicant claims that he left Pakistan for Canada, without first trying to travel to another country. Rule/authority context: Introduction [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA), for judicial review of a decision by the Refugee Appeal Division (RAD) confirming  | [9] Following a hearing on October 8, 2013, the RPD found that the applicant is not a “refugee” or a “person in need of protection” under sections 96 and 97 of the IRPA because of his lack of credibility concerning the e Application context: [9] Following a hearing on October 8, 2013, the RPD found that the applicant is not a “refugee” or a “person in need of protection” under sections 96 and 97 of the IRPA because of his lack of credibility concerning the e Evidence spans paragraphs 0-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5079342` offsets `508-519`; context: Introduction [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA), for judicial review of a decision by the Refugee Appeal Division (RAD) confirming the determination of the Refugee Protection Division (RPD), that the applicant is not a “Convention refugee” or a “person in need of protection” within the meaning of sections 96 and 97 of the IRPA.
- Evidence: `party_position` cue `claims` at chunk `5079345` offsets `155-161`; context: The applicant also claims that he was beaten and reprimanded by his own family.
- Evidence: `party_position` cue `claims` at chunk `5079347` offsets `42-48`; context: [7] In his initial account, the applicant claims that he left Pakistan for Canada, without first trying to travel to another country.
- Evidence: `evidence_fact` cue `found that` at chunk `5079349` offsets `52-62`; context: [9] Following a hearing on October 8, 2013, the RPD found that the applicant is not a “refugee” or a “person in need of protection” under sections 96 and 97 of the IRPA because of his lack of credibility concerning the essential elements of his claim.
- Evidence: `governing_rule` cue `under` at chunk `5079349` offsets `132-137`; context: [9] Following a hearing on October 8, 2013, the RPD found that the applicant is not a “refugee” or a “person in need of protection” under sections 96 and 97 of the IRPA because of his lack of credibility concerning the essential elements of his claim.
- Evidence: `reasoning_application` cue `because` at chunk `5079349` offsets `169-176`; context: [9] Following a hearing on October 8, 2013, the RPD found that the applicant is not a “refugee” or a “person in need of protection” under sections 96 and 97 of the IRPA because of his lack of credibility concerning the essential elements of his claim.

#### 23025:1:subtheme:2 · paragraphs 8-10

- Raw key terms: `credibility, applicant, assessment, each, findings, found, accepted, accounts`
- Display key terms: `credibility, assessment, each, findings, accepted, accounts`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: credibility, assessment, each, findings, accepted, accounts Rule/authority context: [11] After analyzing the respective roles of the RPD and RAD, the RAD stated that the standard of review applicable to findings by the RPD is reasonableness. Application context: Statutory provisions [14] The following statutory provisions of the IRPA apply to the determination of the applicant’s refugee status: Convention refugee Définition de « réfugié » 96. Evidence spans paragraphs 8-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5079350` offsets `255-261`; context: More specifically, the RAD stated that it must extend deference to the RPD’s findings concerning issues of credibility and the assessment of evidence in the context of the appeal before it (RAD decision, at paragraph 44).
- Evidence: `evidence_fact` cue `evidence` at chunk `5079350` offsets `299-307`; context: More specifically, the RAD stated that it must extend deference to the RPD’s findings concerning issues of credibility and the assessment of evidence in the context of the appeal before it (RAD decision, at paragraph 44).
- Evidence: `governing_rule` cue `standard of review` at chunk `5079350` offsets `86-104`; context: [11] After analyzing the respective roles of the RPD and RAD, the RAD stated that the standard of review applicable to findings by the RPD is reasonableness.
- Evidence: `evidence_fact` cue `found that` at chunk `5079351` offsets `13-23`; context: [12] The RAD found that the RPD did not commit any error in its assessment of the applicant’s credibility and it analyzed each of the RPD’s findings.
- Evidence: `evidence_fact` cue `found that` at chunk `5079352` offsets `74-84`; context: [13] Given all of the contradictions in the applicant’s accounts, the RAD found that the RPD did not err in its assessments of the applicant’s credibility.
- Evidence: `reasoning_application` cue `apply` at chunk `5079352` offsets `233-238`; context: Statutory provisions [14] The following statutory provisions of the IRPA apply to the determination of the applicant’s refugee status:
Convention refugee
Définition de « réfugié »
96.

#### 23025:1:subtheme:3 · paragraphs 11-13

- Raw key terms: `appeal, minister, based, canada, circumstances, citizenship, credibility, decision`
- Display key terms: `based, circumstances, credibility`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: based, circumstances, credibility Rule/authority context: The applicant did not submit any new evidence before the RAD that could justify holding a hearing under subsection 110(6) of the IRPA. | [19] As the statutory and jurisprudential framework surrounding the RAD’s role reveals, an appeal to the RAD may attract variable standards of deference, in particular where a decision under appeal to the RAD is based on Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5079353` offsets `307-315`; context: 1) and (2), a person or the Minister may appeal, in accordance with the rules of the Board, on a question of law, of fact or of mixed law and fact, to the Refugee Appeal Division against a decision of the Refugee Protection Division to allow or reject the person’s claim for refugee protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `5079353` offsets `91-99`; context: [15] Concerning the role of the RAD, the holding of a hearing and the admissibility of the evidence, the following statutory provisions of the IRPA are relevant:
Appeal
Appel
110.
- Evidence: `governing_rule` cue `under` at chunk `5079353` offsets `4767-4772`; context: The applicant did not submit any new evidence before the RAD that could justify holding a hearing under subsection 110(6) of the IRPA.
- Evidence: `evidence_fact` cue `record` at chunk `5079354` offsets `184-190`; context: [18] According to subsection 111(1) of the IRPA, the RAD may, depending on the circumstances, substitute the RPD determination for that that should have been made, after analyzing the record.
- Evidence: `governing_rule` cue `under` at chunk `5079355` offsets `185-190`; context: [19] As the statutory and jurisprudential framework surrounding the RAD’s role reveals, an appeal to the RAD may attract variable standards of deference, in particular where a decision under appeal to the RAD is based on credibility findings (Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 at paragraphs 54-55 (Huruglica); Yetna v Canada (Minister of Citizenship and Immigration), 2014 FC 858 at paragraph 17 (Yetna); G.

#### 23025:1:subtheme:4 · paragraphs 14-17

- Raw key terms: `above, appeal, decision, justice, assessing, considerable, credibility, deference`
- Display key terms: `above, justice, assessing, considerable, credibility, deference`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: above, justice, assessing, considerable, credibility, deference Position/evidence statements: The RPD has the considerable advantage of hearing testimony viva voce and assessing the credibility of witnesses and the probative value of the evidence submitted by the parties (Alvarez v Canada (Minister of Citizenship Application context: [40] My colleague Justice Phelan would have preferred in Huruglica, above, to apply the standard of reasonableness to questions of credibility (paragraph 37). Evidence spans paragraphs 14-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5079356` offsets `126-132`; context: [20] As a result, in its analysis, the RAD may show a certain level of deference towards the RPD’s findings, when credibility issues are involved.
- Evidence: `party_position` cue `submitted` at chunk `5079356` offsets `300-309`; context: The RPD has the considerable advantage of hearing testimony viva voce and assessing the credibility of witnesses and the probative value of the evidence submitted by the parties (Alvarez v Canada (Minister of Citizenship and Immigration), 2014 FC 702 at paragraph 33; Alyafi, above, at paragraph 12).
- Evidence: `evidence_fact` cue `testimony` at chunk `5079356` offsets `197-206`; context: The RPD has the considerable advantage of hearing testimony viva voce and assessing the credibility of witnesses and the probative value of the evidence submitted by the parties (Alvarez v Canada (Minister of Citizenship and Immigration), 2014 FC 702 at paragraph 33; Alyafi, above, at paragraph 12).
- Evidence: `reasoning_application` cue `apply` at chunk `5079358` offsets `78-83`; context: [40] My colleague Justice Phelan would have preferred in Huruglica, above, to apply the standard of reasonableness to questions of credibility (paragraph 37).

#### 23025:1:subtheme:5 · paragraphs 18-19

- Raw key terms: `advantage, assessment, conclusion, credibility, enjoys, particular, reaching, above`
- Display key terms: `advantage, assessment, conclusion, credibility, enjoys, particular, reaching, above`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: advantage, assessment, conclusion, credibility, enjoys, particular, reaching, above Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5079360` offsets `98-104`; context: [55] In conducting its assessment, it can recognize and respect the conclusion of the RPD on such issues as credibility and/or where the RPD enjoys a particular advantage in reaching such a conclusion but it is not restricted, as an appellate court is, to intervening on facts only where there is a “palpable and overriding error”.
- Evidence: `evidence_fact` cue `evidence` at chunk `5079361` offsets `331-339`; context: Locke in Yetna, above, at paragraph 17, “[s]ave for cases in which the credibility of a witness is critical or determinative, or where the RPD enjoys a particular advantage over the RAD in reaching a specific conclusion, the RAD owes no deference toward the RPD’s assessment of the evidence”.

#### 23025:1:subtheme:6 · paragraphs 20-23

- Raw key terms: `applicant, account, amendments, applied, cbsa, claim, concerning, court`
- Display key terms: `account, amendments, applied, cbsa, concerning`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: account, amendments, applied, cbsa, concerning Rule/authority context: [23] The applicant’s credibility is central to his claim for protection under sections 96 and 97 of the IRPA before the Immigration and Refugee Board. | In this regard, the result before the RAD would have been the same, regardless of the standard of review it applied. Application context: The Court believes that the standard of review issue itself, applied by the RAD towards the RPD decision, is not determinative in this case. | In this regard, the result before the RAD would have been the same, regardless of the standard of review it applied. Evidence spans paragraphs 20-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5079362` offsets `198-203`; context: The Court believes that the standard of review issue itself, applied by the RAD towards the RPD decision, is not determinative in this case.
- Evidence: `governing_rule` cue `under` at chunk `5079362` offsets `72-77`; context: [23] The applicant’s credibility is central to his claim for protection under sections 96 and 97 of the IRPA before the Immigration and Refugee Board.
- Evidence: `reasoning_application` cue `applied` at chunk `5079362` offsets `212-219`; context: The Court believes that the standard of review issue itself, applied by the RAD towards the RPD decision, is not determinative in this case.
- Evidence: `evidence_fact` cue `record` at chunk `5079363` offsets `21-27`; context: [24] The applicant’s record contains numerous contradictions and omissions, in particular between his initial account, as set out in his BOC, and the amendments made to his BOC after being summoned by the Canada Border Services Agency (CBSA) concerning significant gaps in his statements.
- Evidence: `governing_rule` cue `standard of review` at chunk `5079365` offsets `180-198`; context: In this regard, the result before the RAD would have been the same, regardless of the standard of review it applied.
- Evidence: `reasoning_application` cue `applied` at chunk `5079365` offsets `202-209`; context: In this regard, the result before the RAD would have been the same, regardless of the standard of review it applied.

#### Section text

Sajad v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2014-11-21
Neutral citation
2014 FC 1107
File numbers
IMM-926-14
Decision Content
Date: 20141121
Docket: IMM-926-14
Citation: 2014 FC 1107
[UNREVISED ENGLISH CERTIFIED TRANSLATION]
Ottawa, Ontario, November 21, 2014
PRESENT: The Honourable Mr. Justice Shore
BETWEEN:
ZEESHAN SAJAD
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Introduction [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA), for judicial review of a decision by the Refugee Appeal Division (RAD) confirming the determination of the Refugee Protection Division (RPD), that the applicant is not a “Convention refugee” or a “person in need of protection” within the meaning of sections 96 and 97 of the IRPA.
II. Facts [2] In his written account, the applicant alleged the following facts.

[3] The applicant is a Pakistani citizen of Sunni Muslim origin.

[4] In his first account, as set out in his Basis of Claim (BOC) form dated August 19, 2013, the applicant alleged that his friend, who is of Shia Muslim origin, became pregnant with his child in 2012. In an amendment to his BOC, dated October 1, 2013, the applicant instead claimed that his friend became pregnant with his child in 2010.

[5] When the parents of the applicant’s friend found out that she was pregnant, they became furious and went looking for the applicant. The applicant also claims that he was beaten and reprimanded by his own family.

[6] Following these events, the applicant fled to Islamabad for six months and then left Pakistan.

[7] In his initial account, the applicant claims that he left Pakistan for Canada, without first trying to travel to another country. In his amendment to his BOC, the applicant claims that he left Pakistan for the United Kingdom and that he stayed there for twenty-nine months, that is, from March 17, 2011, to August 8, 2013, before arriving in Canada.

[8] The applicant states that his fear of persecution is based on the threats from his family and his friend’s family.

[9] Following a hearing on October 8, 2013, the RPD found that the applicant is not a “refugee” or a “person in need of protection” under sections 96 and 97 of the IRPA because of his lack of credibility concerning the essential elements of his claim.
III. Impugned decision [10] In a decision dated January 28, 2014, the RAD found that there was no need for a hearing under subsection 110(6) of the IRPA because the applicant had not submitted any new evidence in his appeal.

[11] After analyzing the respective roles of the RPD and RAD, the RAD stated that the standard of review applicable to findings by the RPD is reasonableness. More specifically, the RAD stated that it must extend deference to the RPD’s findings concerning issues of credibility and the assessment of evidence in the context of the appeal before it (RAD decision, at paragraph 44).

[12] The RAD found that the RPD did not commit any error in its assessment of the applicant’s credibility and it analyzed each of the RPD’s findings.

[13] Given all of the contradictions in the applicant’s accounts, the RAD found that the RPD did not err in its assessments of the applicant’s credibility.
IV. Statutory provisions [14] The following statutory provisions of the IRPA apply to the determination of the applicant’s refugee status:
Convention refugee
Définition de « réfugié »
96. A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
96. A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
Person in need of protection
Personne à protéger
97. (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
97. (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
(2) A person in Canada who is a member of a class of persons prescribed by the regulations as being in need of protection is also a person in need of protection.
(2) A également qualité de personne à protéger la personne qui se trouve au Canada et fait partie d’une catégorie de personnes auxquelles est reconnu par règlement le besoin de protection.

[15] Concerning the role of the RAD, the holding of a hearing and the admissibility of the evidence, the following statutory provisions of the IRPA are relevant:
Appeal
Appel
110. (1) Subject to subsections (1.1) and (2), a person or the Minister may appeal, in accordance with the rules of the Board, on a question of law, of fact or of mixed law and fact, to the Refugee Appeal Division against a decision of the Refugee Protection Division to allow or reject the person’s claim for refugee protection.
110. (1) Sous réserve des paragraphes (1.1) et (2), la personne en cause et le ministre peuvent, conformément aux règles de la Commission, porter en appel — relativement à une question de droit, de fait ou mixte — auprès de la Section d’appel des réfugiés la décision de la Section de la protection des réfugiés accordant ou rejetant la demande d’asile.
Procedure
Fonctionnement
(3) Subject to subsections (3.1), (4) and (6), the Refugee Appeal Division must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division, and may accept documentary evidence and written submissions from the Minister and the person who is the subject of the appeal and, in the case of a matter that is conducted before a panel of three members, written submissions from a representative or agent of the United Nations High Commissioner for Refugees and any other person described in the rules of the Board.
(3) Sous réserve des paragraphes (3.1), (4) et (6), la section procède sans tenir d’audience en se fondant sur le dossier de la Section de la protection des réfugiés, mais peut recevoir des éléments de preuve documentaire et des observations écrites du ministre et de la personne en cause ainsi que, s’agissant d’une affaire tenue devant un tribunal constitué de trois commissaires, des observations écrites du représentant ou mandataire du Haut-Commissariat des Nations Unies pour les réfugiés et de toute autre personne visée par les règles de la Commission.
Evidence that may be presented
Éléments de preuve admissibles
(4) On appeal, the person who is the subject of the appeal may present only evidence that arose after the rejection of their claim or that was not reasonably available, or that the person could not reasonably have been expected in the circumstances to have presented, at the time of the rejection.
(4) Dans le cadre de l’appel, la personne en cause ne peut présenter que des éléments de preuve survenus depuis le rejet de sa demande ou qui n’étaient alors pas normalement accessibles ou, s’ils l’étaient, qu’elle n’aurait pas normalement présentés, dans les circonstances, au moment du rejet.
Hearing
Audience
(6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
(6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause;
(b) that is central to the decision with respect to the refugee protection claim; and
b) sont essentiels pour la prise de la décision relative à la demande d’asile;
(c) that, if accepted, would justify allowing or rejecting the refugee protection claim.
c) à supposer qu’ils soient admis, justifieraient que la demande d’asile soit accordée ou refusée, selon le cas.
Decision
Décision
111. (1) After considering the appeal, the Refugee Appeal Division shall make one of the following decisions:
(a) confirm the determination of the Refugee Protection Division;
(b) set aside the determination and substitute a determination that, in its opinion, should have been made; or
(c) refer the matter to the Refugee Protection Division for re-determination, giving the directions to the Refugee Protection Division that it considers appropriate.
111. (1) La Section d’appel des réfugiés confirme la décision attaquée, casse la décision et y substitue la décision qui aurait dû être rendue ou renvoie, conformément à ses instructions, l’affaire à la Section de la protection des réfugiés.
V. Issues [16] The following issues arise in this application:
(a) Did the RAD err in applying the standard of reasonableness to the RPD’s credibility findings?
(b) Did the RAD err in confirming the RPD’s findings regarding the applicant’s lack of credibility?
VI. Analysis [17] First, a hearing can only be held before the RAD when an appellant raises new documentary evidence that is the subject of subsection 110(4) of the IRPA. The applicant did not submit any new evidence before the RAD that could justify holding a hearing under subsection 110(6) of the IRPA. The RAD appropriately based its analysis on the record that was before the RPD.

[18] According to subsection 111(1) of the IRPA, the RAD may, depending on the circumstances, substitute the RPD determination for that that should have been made, after analyzing the record. It is logical to find that the RAD, as the appeal tribunal, exercises a specialized jurisdiction that is equal to or greater than that of the RPD at trial. Otherwise, the creation of a specialized appeal tribunal for refugee determination would serve no purpose (Alyafi v Canada (Minister of Citizenship and Immigration), 2014 FC 952 at paragraph 12 (Alyafi)).

[19] As the statutory and jurisprudential framework surrounding the RAD’s role reveals, an appeal to the RAD may attract variable standards of deference, in particular where a decision under appeal to the RAD is based on credibility findings (Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 at paragraphs 54-55 (Huruglica); Yetna v Canada (Minister of Citizenship and Immigration), 2014 FC 858 at paragraph 17 (Yetna); G.L.N.N. v Canada (Minister of Citizenship and Immigration), 2014 FC 859 at paragraphs 18-20).

[20] As a result, in its analysis, the RAD may show a certain level of deference towards the RPD’s findings, when credibility issues are involved. The RPD has the considerable advantage of hearing testimony viva voce and assessing the credibility of witnesses and the probative value of the evidence submitted by the parties (Alvarez v Canada (Minister of Citizenship and Immigration), 2014 FC 702 at paragraph 33; Alyafi, above, at paragraph 12). In this regard, Justice Yvan Roy stated the following in Spasoja v Canada (Minister of Citizenship and Immigration), 2014 FC 913:
[translation]

[39] If the appeal discussed in sections 110 and 111 of the Act must be dealt with as an appeal and not quasi-judicial review, this does not mean that it will be an opportunity for a new trial or a reconsideration of the matter in its entirety. The Court of Appeal of Quebec makes a very attractive proposition in Parizeau, above, that the appeal of an administrative decision before another administrative tribunal should be treated like any other appeal:
. . .

[40] My colleague Justice Phelan would have preferred in Huruglica, above, to apply the standard of reasonableness to questions of credibility (paragraph 37). With respect, I am still concerned with the blurring of lines. It seems to be preferable to focus on the standard of palpable and overriding error on appeals on questions of fact. There is nothing new in proposing that an appeal tribunal show deference when a body whose decision is being appealed flows from considerable discretion such as assessing credibility. The law is clear: the RAD does not hear witnesses except in very exceptional and specific cases. The credibility to be given to the witnesses heard by the RPD is its responsibility and the RAD, on appeal, must show deference (Lensen v Lensen, [1987] 2 SCR 672; R v Burke, [1996] 1 SCR 474).
[Emphasis added.]

[21] In a recent decision (Huruglica, above), Justice Michael L. Phelan identified the RAD’s power of intervention when it is dealing with an appeal of an RPD decision:

[55] In conducting its assessment, it can recognize and respect the conclusion of the RPD on such issues as credibility and/or where the RPD enjoys a particular advantage in reaching such a conclusion but it is not restricted, as an appellate court is, to intervening on facts only where there is a “palpable and overriding error”.

[22] Furthermore, according to Justice George J. Locke in Yetna, above, at paragraph 17, “[s]ave for cases in which the credibility of a witness is critical or determinative, or where the RPD enjoys a particular advantage over the RAD in reaching a specific conclusion, the RAD owes no deference toward the RPD’s assessment of the evidence”.

[23] The applicant’s credibility is central to his claim for protection under sections 96 and 97 of the IRPA before the Immigration and Refugee Board. The Court believes that the standard of review issue itself, applied by the RAD towards the RPD decision, is not determinative in this case.

[24] The applicant’s record contains numerous contradictions and omissions, in particular between his initial account, as set out in his BOC, and the amendments made to his BOC after being summoned by the Canada Border Services Agency (CBSA) concerning significant gaps in his statements. Namely, as raised by the RAD, the applicant presented contradictory information regarding the following:
(a) The year in which his friend apparently became pregnant with his child, which was the purported trigger for his fear. The applicant first stated that it was in 2012, and then that it was in 2010;
(b) The applicant’s itinerary after leaving Pakistan. The applicant first stated that he left directly from Pakistan for Canada, and then stated that he stayed for more than two years in England, passing through Ireland, to finally come to Canada in 2013.

[25] It is only after being made aware of the information obtained by the CBSA concerning his stay in England, during an interview on September 5, 2013, that the applicant contradicted the information that he provided in his initial BOC. The applicant’s amendments to his account directly affect the very basis of his claim.

[26] The Court finds that the RAD validly showed deference to the RPD’s credibility findings. In this regard, the result before the RAD would have been the same, regardless of the standard of review it applied.


## 23025:2 · paragraphs 24-25

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `cf6cf86670183286d0489d01ff378b2fd074580736d803481d7f0662da0b2533`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23025:2:subtheme:1 · paragraphs 24-25

- Raw key terms: `adjudges, anderson, application, cause, certification, certified, citizenship, conclusion`
- Display key terms: `adjudges, anderson, certification, certified, conclusion`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: adjudges, anderson, certification, certified, conclusion Operative outcome context: Consequently, the application must be dismissed. Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5079365` offsets `441-449`; context: There is no question for certification.
- Evidence: `disposition` cue `dismissed` at chunk `5079365` offsets `318-327`; context: Consequently, the application must be dismissed.

#### Section text

VII. Conclusion [27] The intervention of the Court is not warranted. Consequently, the application must be dismissed.
JUDGMENT
THE COURT ORDERS AND ADJUDGES that
1. The application for judicial review is dismissed;
2. There is no question for certification.
“Michel M.J. Shore”
Judge
Certified true translation
Janine Anderson, Translator
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-926-14
STYLE OF CAUSE:
ZEESHAN SAJAD v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Montréal, QuEbec
DATE OF HEARING:
NOVEMBER 19, 2014


## 23025:3 · paragraphs 26-26

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5c4c455b5f7911d7178b0c2a4577b4d92564ee59916d74c9259c9393833b307e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23025:3:subtheme:1 · paragraphs 26-26

- Raw key terms: `appearances, applicant, attorney, canada, dated, deputy, general, judgment`
- Display key terms: `dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 26-26. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
SHORE J.
DATED:
November 21, 2014
APPEARANCES:
Stéphanie Valois
FOR THE APPLICANT
Yaël Levy
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Stéphanie Valois
Montréal, Quebec
FOR THE APPLICANT
William F. Pentney
Deputy Attorney General of Canada
Montréal, Quebec
FOR THE RESPONDENT
