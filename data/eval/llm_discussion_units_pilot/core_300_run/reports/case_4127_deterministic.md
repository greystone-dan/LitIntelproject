# Discussion Units: case 4127

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **77**
- Continuity pairs: **76**
- Discussion Units: **5**
- Paragraph source hashes: **77**
- Sub-themes: **20**

## 4127:1 · paragraphs 0-6

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2ca1d722c6fbc3ed48934c226932a9b5601dde9b1f87fbfbfdf51b2c1db02126`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4127:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `canada, immigration, imprisonment, refugee, risk, applicant, assessment, cambodia`
- Display key terms: `imprisonment, refugee, risk, assessment, cambodia`
- Argument roles: `evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, reasoning_application Display terms: imprisonment, refugee, risk, assessment, cambodia Rule/authority context: His family resettled here in 1984 as permanent residents, having been selected under the Indochinese Designated Class, a program in existence from 1978 to 1997 to aid in the resettlement of south-east Asian "boat people" | In December 1997, he was declared by the Minister to be a danger to the public under subsection 70(5) and section 46 of the former Immigration Act, R. Application context: Kim applied for a Pre-Removal Risk Assessment ("PRRA") under subsection 112(1) of the Immigration and Refugee Protection Act, S. | [4] The PRRA officer considered the application under section 97 of IRPA only, because of the operation of paragraph 112(3)(b): 112(3) Refugee protection may not result from an application for protection if the person 11 Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4240200` offsets `333-338`; context: His family resettled here in 1984 as permanent residents, having been selected under the Indochinese Designated Class, a program in existence from 1978 to 1997 to aid in the resettlement of south-east Asian "boat people" fleeing strife in Cambodia, Laos and Vietnam.
- Evidence: `governing_rule` cue `under` at chunk `4240201` offsets `237-242`; context: In December 1997, he was declared by the Minister to be a danger to the public under subsection 70(5) and section 46 of the former Immigration Act, R.
- Evidence: `governing_rule` cue `under` at chunk `4240202` offsets `104-109`; context: Kim applied for a Pre-Removal Risk Assessment ("PRRA") under subsection 112(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `reasoning_application` cue `applied` at chunk `4240202` offsets `53-60`; context: Kim applied for a Pre-Removal Risk Assessment ("PRRA") under subsection 112(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `governing_rule` cue `under` at chunk `4240203` offsets `48-53`; context: [4] The PRRA officer considered the application under section 97 of IRPA only, because of the operation of paragraph 112(3)(b):
112(3) Refugee protection may not result from an application for protection if the person
112(3) L'asile ne peut être conféré au demandeur dans les cas suivants :
(b) is determined to be inadmissible on grounds of serious criminality with respect to a conviction in Canada punished by a term of imprisonment of at least two years or with respect to a conviction outside Canada for an offence that, if committed in Canada, would constitute an offence under an Act of Parliament punishable by a maximum term of imprisonment of at least 10 years;
b) il est interdit de territoire pour grande criminalité pour déclaration de culpabilité au Canada punie par un emprisonnement d'au moins deux ans ou pour toute déclaration de culpabilité à l'extérieur du Canada pour une infraction qui, commise au Canada, constituerait une infraction à une loi fédérale punissable d'un emprisonnement maximal d'au moins dix ans;
The officer also declined to consider humanitarian and compassionate factors as, in her opinion, they did not fall within the mandate of the pre-removal risk assessment.
- Evidence: `reasoning_application` cue `because` at chunk `4240203` offsets `79-86`; context: [4] The PRRA officer considered the application under section 97 of IRPA only, because of the operation of paragraph 112(3)(b):
112(3) Refugee protection may not result from an application for protection if the person
112(3) L'asile ne peut être conféré au demandeur dans les cas suivants :
(b) is determined to be inadmissible on grounds of serious criminality with respect to a conviction in Canada punished by a term of imprisonment of at least two years or with respect to a conviction outside Canada for an offence that, if committed in Canada, would constitute an offence under an Act of Parliament punishable by a maximum term of imprisonment of at least 10 years;
b) il est interdit de territoire pour grande criminalité pour déclaration de culpabilité au Canada punie par un emprisonnement d'au moins deux ans ou pour toute déclaration de culpabilité à l'extérieur du Canada pour une infraction qui, commise au Canada, constituerait une infraction à une loi fédérale punissable d'un emprisonnement maximal d'au moins dix ans;
The officer also declined to consider humanitarian and compassionate factors as, in her opinion, they did not fall within the mandate of the pre-removal risk assessment.
- Evidence: `evidence_fact` cue `evidence` at chunk `4240204` offsets `187-195`; context: She was of the opinion that there is insufficient evidence that Cambodian state authorities have any interest in the applicant.

#### 4127:1:subtheme:2 · paragraphs 6-6

- Raw key terms: `applicant, believed, consequentially, cruel, danger, evidence, exist, found`
- Display key terms: `believed, consequentially, cruel, danger, exist`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: believed, consequentially, cruel, danger, exist Evidence spans paragraphs 6-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `4240205` offsets `256-262`; context: ISSUES
- Evidence: `evidence_fact` cue `found that` at chunk `4240205` offsets `32-42`; context: [6] The officer consequentially found that there was insufficient evidence that the applicant would be subjected to a danger, believed on substantial grounds to exist, of torture or to a risk to life or a risk of cruel and unusual treatment or punishment.

#### Section text

Kim v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2005-04-01
Neutral citation
2005 FC 437
File numbers
IMM-1868-04
Decision Content
Date: 20050401
Docket: IMM-1868-04
Citation: 2005 FC 437
Ottawa, Ontario, this 1st day of April, 2005
Present: The Honourable Mr. Justice Mosley
BETWEEN:
RITH KIM
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
THE SOLICITOR GENERAL OF CANADA
Respondents
REASONS FOR ORDER AND ORDER

[1] Mr. Rith Kim is a 33-year-old Cambodian national who arrived in Canada at the age of 12. He has never been declared a refugee in Canada, but the office of the United Nations High Commissioner for Refugees ("UNHCR") accepted him as a mandate refugee. His family resettled here in 1984 as permanent residents, having been selected under the Indochinese Designated Class, a program in existence from 1978 to 1997 to aid in the resettlement of south-east Asian "boat people" fleeing strife in Cambodia, Laos and Vietnam. Mr. Kim has never received Canadian citizenship.

[2] Mr. Kim was convicted in Canada of a number of criminal offences, and was sentenced to five-and-a-half years imprisonment (concurrent sentences) in 1997. In December 1997, he was declared by the Minister to be a danger to the public under subsection 70(5) and section 46 of the former Immigration Act, R.S.C. 1985 c. I-2. He was ordered deported in March 1998, but was in prison at the time.

[3] Upon completion of his sentence in 2003, Mr. Kim applied for a Pre-Removal Risk Assessment ("PRRA") under subsection 112(1) of the Immigration and Refugee Protection Act, S.C. 2001 ["IRPA"]. He alleged that as an ex-criminal, he would be at risk of imprisonment, torture, and ill-treatment in Cambodia.
THE OFFICER'S DECISION

[4] The PRRA officer considered the application under section 97 of IRPA only, because of the operation of paragraph 112(3)(b):
112(3) Refugee protection may not result from an application for protection if the person
112(3) L'asile ne peut être conféré au demandeur dans les cas suivants :
(b) is determined to be inadmissible on grounds of serious criminality with respect to a conviction in Canada punished by a term of imprisonment of at least two years or with respect to a conviction outside Canada for an offence that, if committed in Canada, would constitute an offence under an Act of Parliament punishable by a maximum term of imprisonment of at least 10 years;
b) il est interdit de territoire pour grande criminalité pour déclaration de culpabilité au Canada punie par un emprisonnement d'au moins deux ans ou pour toute déclaration de culpabilité à l'extérieur du Canada pour une infraction qui, commise au Canada, constituerait une infraction à une loi fédérale punissable d'un emprisonnement maximal d'au moins dix ans;
The officer also declined to consider humanitarian and compassionate factors as, in her opinion, they did not fall within the mandate of the pre-removal risk assessment.

[5] The officer found the risk to Mr. Kim from mob violence or police and security forces was not likely, on a balance of probabilities. She was of the opinion that there is insufficient evidence that Cambodian state authorities have any interest in the applicant.

[6] The officer consequentially found that there was insufficient evidence that the applicant would be subjected to a danger, believed on substantial grounds to exist, of torture or to a risk to life or a risk of cruel and unusual treatment or punishment.
ISSUES

## 4127:2 · paragraphs 7-60

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `013e8bfb6a4dbeb2c7d00a423cc654aed47a135df598cd094f768464671d6503`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4127:2:subtheme:1 · paragraphs 7-8

- Raw key terms: `determination, officer, prra, review, standard, according, administrative, applicant`
- Display key terms: `determination, officer, prra, review, standard, according, administrative`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: determination, officer, prra, review, standard, according, administrative Rule/authority context: Did the PRRA officer err in failing to consider and make a determination under section 25 of IRPA? | [8] To date there has been no comprehensive determination of the standard of review appropriate to the different aspects of PRRA officer decisions according to the pragmatic and functional approach. Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4240206` offsets `18-24`; context: [7] The following issues were argued before me:
1.
- Evidence: `evidence_fact` cue `evidence` at chunk `4240206` offsets `349-357`; context: Did the PRRA officer err in ignoring significant evidence?
- Evidence: `governing_rule` cue `under` at chunk `4240206` offsets `644-649`; context: Did the PRRA officer err in failing to consider and make a determination under section 25 of IRPA?
- Evidence: `governing_rule` cue `standard of review` at chunk `4240207` offsets `65-83`; context: [8] To date there has been no comprehensive determination of the standard of review appropriate to the different aspects of PRRA officer decisions according to the pragmatic and functional approach.

#### 4127:2:subtheme:2 · paragraphs 9-10

- Raw key terms: `appeal, clause, court, judicial, legislation, privative, provisions, purpose`
- Display key terms: `clause, judicial, legislation, privative, provisions, purpose`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: clause, judicial, legislation, privative, provisions, purpose Rule/authority context: On the contrary, there is specific provision for matters under IRPA to be subjected to judicial review by this Court. Application context: Some degree of judicial oversight is therefore contemplated, but not a full-fledged appeal. Evidence spans paragraphs 9-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4240208` offsets `45-53`; context: [9] Four factors must be considered for each question at issue in judicial review proceedings: the existence of any privative clause or statutory right of appeal; the purpose(s) of the legislation as a whole and the provisions at issue in particular; the nature of the question - being law, fact or mixed fact and law; and the expertise of the tribunal relative to that of the reviewing court with regard to the questions at issue: Law Society of New Brunswick v.
- Evidence: `issue` cue `question` at chunk `4240209` offsets `483-491`; context: (1) Judicial review by the Federal Court with respect to any matter - a decision, determination or order made, a measure taken or a question raised - under this Act is commenced by making an application for leave to the Court.
- Evidence: `governing_rule` cue `under` at chunk `4240209` offsets `184-189`; context: On the contrary, there is specific provision for matters under IRPA to be subjected to judicial review by this Court.
- Evidence: `reasoning_application` cue `therefore` at chunk `4240209` offsets `822-831`; context: Some degree of judicial oversight is therefore contemplated, but not a full-fledged appeal.
- Evidence: `counterargument_limitation` cue `However` at chunk `4240209` offsets `245-252`; context: However, IRPA also imposes the additional hurdle of the necessity for leave to bring the application:
72.

#### 4127:2:subtheme:3 · paragraphs 11-13

- Raw key terms: `decision, persons, prra, assessment, beings, canada's, consideration, cruel`
- Display key terms: `persons, prra, assessment, beings, canada's, consideration, cruel`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: persons, prra, assessment, beings, canada's, consideration, cruel Rule/authority context: [13] The purpose of requiring a PRRA analysis is ultimately to honour Canada's international obligations under the Convention Against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment. Application context: Kim's case, he is excluded from refugee consideration because of the operation of paragraph 112(3)(b). | Given this specific context, I find that two purposes under paragraphs 3(2)(d) and (e) above are particularly engaged in the "risk assessment" portion of a PRRA decision: to offer safe haven to persons at risk of torture Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4240210` offsets `180-188`; context: The purpose as a whole of the legislation in question is set out in section 3 of IRPA; the purpose of the PRRA assessment provisions as they relate to refugee determination are particularly addressed in subsection 3(2):
3(2) The objectives of this Act with respect to refugees are
(2) S'agissant des réfugiés, la présente loi a pour objet :
(a) to recognize that the refugee program is in the first instance about saving lives and offering protection to the displaced and persecuted;
a) de reconnaître que le programme pour les réfugiés vise avant tout à sauver des vies et à protéger les personnes de la persécution;
(b) to fulfil Canada's international legal obligations with respect to refugees and affirm Canada's commitment to international efforts to provide assistance to those in need of resettlement;
b) de remplir les obligations en droit international du Canada relatives aux réfugiés et aux personnes déplacées et d'affirmer la volonté du Canada de participer aux efforts de la communauté internationale pour venir en aide aux personnes qui doivent se réinstaller;
c) to grant, as a fundamental expression of Canada's humanitarian ideals, fair consideration to those who come to Canada claiming persecution;
c) de faire bénéficier ceux qui fuient la persécution d'une procédure équitable reflétant les idéaux humanitaires du Canada;
(d) to offer safe haven to persons with a well-founded fear of persecution based on race, religion, nationality, political opinion or membership in a particular social group, as well as those at risk of torture or cruel and unusual treatment or punishment;
d) d'offrir l'asile à ceux qui craignent avec raison d'être persécutés du fait de leur race, leur religion, leur nationalité, leurs opinions politiques, leur appartenance à un groupe social en particulier, ainsi qu'à ceux qui risquent la torture ou des traitements ou peines cruels et inusités;
(e) to establish fair and efficient procedures that will maintain the integrity of the Canadian refugee protection system, while upholding Canada's respect for the human rights and fundamental freedoms of all human beings;
e) de mettre en place une procédure équitable et efficace qui soit respectueuse, d'une part, de l'intégrité du processus canadien d'asile et, d'autre part, des droits et des libertés fondamentales reconnus à tout être humain;
(f) to support the self-sufficiency and the social and economic well-being of refugees by facilitating reunification with their family members in Canada;
f) d'encourager l'autonomie et le bien-être socioéconomique des réfugiés en facilitant la réunification de leurs familles au Canada;
(g) to protect the health and safety of Canadians and to maintain the security of Canadian society; and
g) de protéger la santé des Canadiens et de garantir leur sécurité;
(h) to promote international justice and security by denying access to Canadian territory to persons, including refugee claimants, who are security risks or serious criminals.
- Evidence: `reasoning_application` cue `because` at chunk `4240211` offsets `75-82`; context: Kim's case, he is excluded from refugee consideration because of the operation of paragraph 112(3)(b).
- Evidence: `governing_rule` cue `under` at chunk `4240212` offsets `105-110`; context: [13] The purpose of requiring a PRRA analysis is ultimately to honour Canada's international obligations under the Convention Against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment.
- Evidence: `reasoning_application` cue `I find` at chunk `4240212` offsets `234-240`; context: Given this specific context, I find that two purposes under paragraphs 3(2)(d) and (e) above are particularly engaged in the "risk assessment" portion of a PRRA decision: to offer safe haven to persons at risk of torture or cruel and unusual treatment or punishment, as well as upholding Canada's respect for the human rights and fundamental freedoms of all human beings.

#### 4127:2:subtheme:4 · paragraphs 14-15

- Raw key terms: `determination, different, particular, protection, prra, question, questions, situation`
- Display key terms: `determination, different, particular, protection, prra, question, questions, situation`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: determination, different, particular, protection, prra, question, questions, situation Rule/authority context: 25: [T]he establishment of Convention refugee status or the status of a "person in need of protection" pursuant to sections 96 and 97 of the Act is based on specific requirements that must be established by the claimant. Application context: In practice, it is therefore clear that the determination of the status of "refugee" or of a "person in need of protection" does not depend on "the consideration of numerous interests simultaneously, and the promulgation | While this is ultimately a question of mixed fact and law, there must be a preliminary determination of what the law pertaining to cruel and unusual treatment and to section 25 of IRPA actually is before it can be applie Evidence spans paragraphs 14-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4240213` offsets `553-561`; context: Thus, the application of these provisions is directly related to the personal situation of each claimant and the particular conditions of the country in question at the time that the claim for asylum or protection is brought before the Board.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4240213` offsets `282-293`; context: 25:
[T]he establishment of Convention refugee status or the status of a "person in need of protection" pursuant to sections 96 and 97 of the Act is based on specific requirements that must be established by the claimant.
- Evidence: `reasoning_application` cue `therefore` at chunk `4240213` offsets `662-671`; context: In practice, it is therefore clear that the determination of the status of "refugee" or of a "person in need of protection" does not depend on "the consideration of numerous interests simultaneously, and the promulgation of solutions which concurrently balance benefits and costs for many different parties".
- Evidence: `issue` cue `issues` at chunk `4240214` offsets `9-15`; context: [15] The issues raised on this judicial review fall into different categories.
- Evidence: `evidence_fact` cue `evidence` at chunk `4240214` offsets `351-359`; context: The third issue goes to the assessment of evidence.
- Evidence: `reasoning_application` cue `applied` at chunk `4240214` offsets `727-734`; context: While this is ultimately a question of mixed fact and law, there must be a preliminary determination of what the law pertaining to cruel and unusual treatment and to section 25 of IRPA actually is before it can be applied to the facts as found.

#### 4127:2:subtheme:5 · paragraphs 16-20

- Raw key terms: `prra, court, officer, deference, expertise, fact, facts, level`
- Display key terms: `prra, officer, deference, expertise, fact, facts, level`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: prra, officer, deference, expertise, fact, facts, level Rule/authority context: [19] Combining and balancing all of these factors, I conclude that in the judicial review of PRRA decisions the appropriate standard of review for questions of fact should generally be patent unreasonableness, for questi | 6, Justice Phelan found: The standard of review of credibility findings, which is at the heart of this PRRA decision, is patent unreasonableness. Application context: [19] Combining and balancing all of these factors, I conclude that in the judicial review of PRRA decisions the appropriate standard of review for questions of fact should generally be patent unreasonableness, for questi Evidence spans paragraphs 16-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4240215` offsets `83-91`; context: [16] The expertise of the PRRA officer is variable, depending on the nature of the question considered.
- Evidence: `issue` cue `issue` at chunk `4240216` offsets `497-502`; context: A higher degree of deference is necessary only when the decision-making body has, in some way, a greater expertise than the reviewing court and the particular issue pertains to this greater expertise: Moreau-Bérubé v.
- Evidence: `governing_rule` cue `standard of review` at chunk `4240218` offsets `124-142`; context: [19] Combining and balancing all of these factors, I conclude that in the judicial review of PRRA decisions the appropriate standard of review for questions of fact should generally be patent unreasonableness, for questions of mixed law and fact, reasonableness simpliciter, and for questions of law, correctness.
- Evidence: `reasoning_application` cue `conclude` at chunk `4240218` offsets `53-61`; context: [19] Combining and balancing all of these factors, I conclude that in the judicial review of PRRA decisions the appropriate standard of review for questions of fact should generally be patent unreasonableness, for questions of mixed law and fact, reasonableness simpliciter, and for questions of law, correctness.
- Evidence: `governing_rule` cue `standard of review` at chunk `4240219` offsets `115-133`; context: 6, Justice Phelan found:
The standard of review of credibility findings, which is at the heart of this PRRA decision, is patent unreasonableness.

#### 4127:2:subtheme:6 · paragraphs 21-22

- Raw key terms: `appropriate, officer, prra, review, standard, agreement, analysis, application`
- Display key terms: `appropriate, officer, prra, review, standard, agreement, analysis`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: appropriate, officer, prra, review, standard, agreement, analysis Rule/authority context: [21] There has also been previous agreement in this Court that when a question of law has been decided by a PRRA officer, the appropriate standard of review is correctness: Singh v. | [22] Finally, I also note Justice Martineau's opinion that the appropriate standard of review for the decision of a PRRA officer is reasonableness simpliciter when the decision is considered "globally and as a whole", wh Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4240220` offsets `70-78`; context: [21] There has also been previous agreement in this Court that when a question of law has been decided by a PRRA officer, the appropriate standard of review is correctness: Singh v.
- Evidence: `governing_rule` cue `standard of review` at chunk `4240220` offsets `138-156`; context: [21] There has also been previous agreement in this Court that when a question of law has been decided by a PRRA officer, the appropriate standard of review is correctness: Singh v.
- Evidence: `governing_rule` cue `standard of review` at chunk `4240221` offsets `75-93`; context: [22] Finally, I also note Justice Martineau's opinion that the appropriate standard of review for the decision of a PRRA officer is reasonableness simpliciter when the decision is considered "globally and as a whole", which I take to mean the application of the relevant law to the facts as found by the officer: Figurado, supra.

#### 4127:2:subtheme:7 · paragraphs 23-27

- Raw key terms: `irpa, convention, accepted, class, designated, humanitarian, immigration, jurisdiction`
- Display key terms: `irpa, convention, accepted, class, designated, humanitarian, jurisdiction`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: irpa, convention, accepted, class, designated, humanitarian, jurisdiction Position/evidence statements: [24] The applicant submits that because Mr. Rule/authority context: [26] Regulations made under section 12 IRPA designated the Country of Asylum Class and the Source Country Class (IRP Regulations, sections 146 and 147). | [27] The definition of refugee used by the UNHCR is almost identical to that used under the Refugee Convention and IRPA: Statute on the Office of the United Nations High Commissioner for Refugees, 1950, Article 6B. Application context: [24] The applicant submits that because Mr. | However, the same humanitarian principles applied in 1984 in the Immigration Act and Regulations under which Mr. Evidence spans paragraphs 23-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4240222` offsets `74-83`; context: Kim objects to the admissibility of the affidavit of John R.
- Evidence: `party_position` cue `submits` at chunk `4240223` offsets `19-26`; context: [24] The applicant submits that because Mr.
- Evidence: `reasoning_application` cue `because` at chunk `4240223` offsets `32-39`; context: [24] The applicant submits that because Mr.
- Evidence: `governing_rule` cue `under` at chunk `4240225` offsets `22-27`; context: [26] Regulations made under section 12 IRPA designated the Country of Asylum Class and the Source Country Class (IRP Regulations, sections 146 and 147).
- Evidence: `reasoning_application` cue `applied` at chunk `4240225` offsets `277-284`; context: However, the same humanitarian principles applied in 1984 in the Immigration Act and Regulations under which Mr.
- Evidence: `counterargument_limitation` cue `However` at chunk `4240225` offsets `235-242`; context: However, the same humanitarian principles applied in 1984 in the Immigration Act and Regulations under which Mr.
- Evidence: `governing_rule` cue `under` at chunk `4240226` offsets `82-87`; context: [27] The definition of refugee used by the UNHCR is almost identical to that used under the Refugee Convention and IRPA: Statute on the Office of the United Nations High Commissioner for Refugees, 1950, Article 6B.

#### 4127:2:subtheme:8 · paragraphs 28-36

- Raw key terms: `irpa, person, refugee, respondent, canada, class, designated, submits`
- Display key terms: `irpa, person, refugee, class, designated, submits`
- Argument roles: `disposition, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, party_position, reasoning_application Display terms: irpa, person, refugee, class, designated, submits Position/evidence statements: [30] The respondent submits that Mr. | [32] The respondent submits that Mr. Rule/authority context: Kim argues that he has never lost his status as a person who was displaced and persecuted, so he is not subject to removal under subsection 115(1) of IRPA. | He is not protected from refoulement under subsection 115(1) because he is not recognized as a refugee by another country and is not a protected person under IRPA. Application context: He is not protected from refoulement under subsection 115(1) because he is not recognized as a refugee by another country and is not a protected person under IRPA. | Kim is not a protected person underIRPA because he has never been found to be a Convention refugee either here or in any other country. Operative outcome context: He was granted admission as a landed immigrant, not as a refugee. Evidence spans paragraphs 28-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4240227` offsets `288-293`; context: The rights in issue are fundamental human rights and so the presumption that there was no change is even stronger: R.
- Evidence: `governing_rule` cue `under` at chunk `4240228` offsets `132-137`; context: Kim argues that he has never lost his status as a person who was displaced and persecuted, so he is not subject to removal under subsection 115(1) of IRPA.
- Evidence: `party_position` cue `submits` at chunk `4240229` offsets `20-27`; context: [30] The respondent submits that Mr.
- Evidence: `governing_rule` cue `under` at chunk `4240229` offsets `134-139`; context: He is not protected from refoulement under subsection 115(1) because he is not recognized as a refugee by another country and is not a protected person under IRPA.
- Evidence: `reasoning_application` cue `because` at chunk `4240229` offsets `158-165`; context: He is not protected from refoulement under subsection 115(1) because he is not recognized as a refugee by another country and is not a protected person under IRPA.
- Evidence: `party_position` cue `submits` at chunk `4240231` offsets `20-27`; context: [32] The respondent submits that Mr.
- Evidence: `reasoning_application` cue `because` at chunk `4240231` offsets `77-84`; context: Kim is not a protected person underIRPA because he has never been found to be a Convention refugee either here or in any other country.
- Evidence: `governing_rule` cue `under` at chunk `4240232` offsets `117-122`; context: [33] The transitional provisions of the IRP Regulations specify which people will continue to be considered refugees under IRPA: Regulations section 338.
- Evidence: `reasoning_application` cue `applied` at chunk `4240232` offsets `379-386`; context: Members of the Indochinese Designated Class were exempt from section 7 of the old Regulations and could not have applied under section 4 of the Humanitarian Designated Class Regulations, as these came into force in 1997 at the same time as the Indochinese Designated Class was repealed.
- Evidence: `party_position` cue `submits` at chunk `4240233` offsets `20-27`; context: [34] The respondent submits that Mr.
- Evidence: `reasoning_application` cue `because` at chunk `4240233` offsets `85-92`; context: Kim has no vested rights against removal simply because he came to Canada as part of a designated class for humanitarian purposes.
- Evidence: `disposition` cue `granted` at chunk `4240233` offsets `175-182`; context: He was granted admission as a landed immigrant, not as a refugee.
- Evidence: `party_position` cue `argues` at chunk `4240234` offsets `241-247`; context: Different categories of individuals are treated variously under the Immigration Act scheme, and the respondent argues, this is acceptable: Canada (Minister of Employment and Immigration) v.
- Evidence: `governing_rule` cue `under` at chunk `4240234` offsets `74-79`; context: Kim committed his criminal offences, he became inadmissible under the old Immigration Act and was ordered deported.
- Evidence: `party_position` cue `submits` at chunk `4240235` offsets `20-27`; context: [36] The respondent submits that even if Mr.
- Evidence: `governing_rule` cue `under` at chunk `4240235` offsets `114-119`; context: Kim was found to be a protected person, he would still be deportable under subsection 115(2) of IRPA.

#### 4127:2:subtheme:9 · paragraphs 37-44

- Raw key terms: `canada, class, designated, indochinese, mandate, prra, refugee, refugees`
- Display key terms: `class, designated, indochinese, mandate, prra, refugee, refugees`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: class, designated, indochinese, mandate, prra, refugee, refugees Position/evidence statements: [37] The PRRA officer correctly exercised her jurisdiction to determine whether a person not covered by the non-refoulement provisions might nonetheless be at risk if removed from Canada, the respondent argues. Rule/authority context: People with serious criminal convictions are only entitled to consideration under section 97: IRPA subsections 112(3), 113(d). | The applicant's arguments centre around the proposition that his case is falling through the cracks because Parliament never explicitly acknowledged that members of the Indochinese Designated Class were refugees, either  Application context: The applicant's arguments centre around the proposition that his case is falling through the cracks because Parliament never explicitly acknowledged that members of the Indochinese Designated Class were refugees, either  | That status has not been revoked because of changes in immigration law, but because of his own actions. Evidence spans paragraphs 37-44. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4240236` offsets `72-79`; context: [37] The PRRA officer correctly exercised her jurisdiction to determine whether a person not covered by the non-refoulement provisions might nonetheless be at risk if removed from Canada, the respondent argues.
- Evidence: `party_position` cue `argues` at chunk `4240236` offsets `203-209`; context: [37] The PRRA officer correctly exercised her jurisdiction to determine whether a person not covered by the non-refoulement provisions might nonetheless be at risk if removed from Canada, the respondent argues.
- Evidence: `governing_rule` cue `under` at chunk `4240236` offsets `287-292`; context: People with serious criminal convictions are only entitled to consideration under section 97: IRPA subsections 112(3), 113(d).
- Evidence: `governing_rule` cue `under` at chunk `4240237` offsets `270-275`; context: The applicant's arguments centre around the proposition that his case is falling through the cracks because Parliament never explicitly acknowledged that members of the Indochinese Designated Class were refugees, either under the Immigration Act or under IRPA.
- Evidence: `reasoning_application` cue `because` at chunk `4240237` offsets `150-157`; context: The applicant's arguments centre around the proposition that his case is falling through the cracks because Parliament never explicitly acknowledged that members of the Indochinese Designated Class were refugees, either under the Immigration Act or under IRPA.
- Evidence: `governing_rule` cue `under` at chunk `4240239` offsets `191-196`; context: The only right that he acquired under that class was landed status, which was later converted into permanent resident status by IRPA.
- Evidence: `reasoning_application` cue `because` at chunk `4240239` offsets `326-333`; context: That status has not been revoked because of changes in immigration law, but because of his own actions.
- Evidence: `evidence_fact` cue `evidence` at chunk `4240240` offsets `316-324`; context: Kim really is a person in need of protection, he should have adduced evidence sufficient to convince a PRRA officer of this.
- Evidence: `governing_rule` cue `under` at chunk `4240241` offsets `462-467`; context: Although they are substantially similar, mandate refugees are not treated in the same way as Convention refugees under Canadian law and this is, arguably, not fair.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4240241` offsets `349-357`; context: Although they are substantially similar, mandate refugees are not treated in the same way as Convention refugees under Canadian law and this is, arguably, not fair.
- Evidence: `governing_rule` cue `under` at chunk `4240242` offsets `364-369`; context: Convention refugees must not be refouled because Canada has signed the Refugee Convention, and likewise, those in danger of torture cannot be refouled because of Canada's commitments under the Convention Against Torture.
- Evidence: `reasoning_application` cue `because` at chunk `4240242` offsets `222-229`; context: Convention refugees must not be refouled because Canada has signed the Refugee Convention, and likewise, those in danger of torture cannot be refouled because of Canada's commitments under the Convention Against Torture.
- Evidence: `governing_rule` cue `under` at chunk `4240243` offsets `62-67`; context: Kim is protected from refoulement under section 115 by reason of his membership in the Indochinese Designated Class or his status as a mandate refugee.

#### 4127:2:subtheme:10 · paragraphs 45-52

- Raw key terms: `evidence, officer, prra, decision, minister, address, cambodia, deportees`
- Display key terms: `officer, prra, address, cambodia, deportees`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: officer, prra, address, cambodia, deportees Position/evidence statements: [47] The respondent submits that the PRRA officer examined the pertinent documentary evidence, and found that there was insufficient evidence that the authorities have any interest in Mr. | [48] In response to the allegation concerning the inability of the Cambodian government to supply food to deportees, the respondent submits that there is no evidence that the government is unable to feed those detained. Application context: The officer clearly applied the correct standard as determined in Li. | [52] I do not find, therefore, that the officer improperly ignored evidence of risk to Mr. Evidence spans paragraphs 45-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4240244` offsets `144-149`; context: Canada (Minister of Citizenship and Immigration) 2005 FCA 1 has clarified the law, I will not address this issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `4240244` offsets `233-241`; context: Ignoring evidence
- Evidence: `reasoning_application` cue `applied` at chunk `4240244` offsets `171-178`; context: The officer clearly applied the correct standard as determined in Li.
- Evidence: `evidence_fact` cue `evidence` at chunk `4240245` offsets `50-58`; context: Kim submits that two important pieces of evidence were ignored.
- Evidence: `party_position` cue `submits` at chunk `4240246` offsets `20-27`; context: [47] The respondent submits that the PRRA officer examined the pertinent documentary evidence, and found that there was insufficient evidence that the authorities have any interest in Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4240246` offsets `85-93`; context: [47] The respondent submits that the PRRA officer examined the pertinent documentary evidence, and found that there was insufficient evidence that the authorities have any interest in Mr.
- Evidence: `party_position` cue `submits` at chunk `4240247` offsets `132-139`; context: [48] In response to the allegation concerning the inability of the Cambodian government to supply food to deportees, the respondent submits that there is no evidence that the government is unable to feed those detained.
- Evidence: `evidence_fact` cue `evidence` at chunk `4240247` offsets `157-165`; context: [48] In response to the allegation concerning the inability of the Cambodian government to supply food to deportees, the respondent submits that there is no evidence that the government is unable to feed those detained.
- Evidence: `evidence_fact` cue `record` at chunk `4240248` offsets `60-66`; context: [49] Having reviewed the published reports in the certified record, I agree with the respondent's assessment of the evidence, and agree also that there was no obligation on the PRRA officer to specifically address this point in the decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `4240249` offsets `303-311`; context: It was open to the officer to make a finding that was adverse to the applicant (for instance, that there was no evidence that this was anything more than a politically motivated statement or that in practice this statement had proven to be false), but not to ignore the evidence completely.
- Evidence: `evidence_fact` cue `Record` at chunk `4240250` offsets `303-309`; context: Kim's application letter where he described horrific treatment - likely amounting to torture - by the police when he was just five years old (Tribunal Record at 47-48).
- Evidence: `counterargument_limitation` cue `however` at chunk `4240250` offsets `328-335`; context: Again, however, I do not believe that this amounts to reviewable error, considering the finding that there was no evidence that Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4240251` offsets `67-75`; context: [52] I do not find, therefore, that the officer improperly ignored evidence of risk to Mr.
- Evidence: `reasoning_application` cue `therefore` at chunk `4240251` offsets `20-29`; context: [52] I do not find, therefore, that the officer improperly ignored evidence of risk to Mr.

#### 4127:2:subtheme:11 · paragraphs 53-54

- Raw key terms: `cruel, punishment, treatment, unusual, allard, america, among, amount`
- Display key terms: `cruel, punishment, treatment, unusual, allard, america, among, amount`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: cruel, punishment, treatment, unusual, allard, america, among, amount Evidence spans paragraphs 53-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4240252` offsets `162-169`; context: Kim submits that the PRRA officer erred in finding that she did not have jurisdiction to consider humanitarian and compassionate ("H & C") factors as to whether he would be at risk of cruel or unusual treatment or punishment contrary to section 12 of the Charter.
- Evidence: `evidence_fact` cue `found that` at chunk `4240253` offsets `52-62`; context: [54] In the criminal context, the Supreme Court has found that cruel or unusual treatment or punishment is, among other things, treatment that is so excessive that it outrages standards of decency, treatment that is grossly disproportionate to the offence, shocks the conscience of Canadians, or is simply unacceptable: R v.

#### 4127:2:subtheme:12 · paragraphs 55-56

- Raw key terms: `factors, humanitarian, applicant, apply, argues, based, canada, canepa`
- Display key terms: `factors, humanitarian, apply, argues, based, canepa`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: factors, humanitarian, apply, argues, based, canepa Position/evidence statements: [56] The respondent submits that the Charter is not engaged, based on the evidence before the PRRA officer. Rule/authority context: The jurisprudence cited by the applicant does not apply to the consideration of humanitarian and compassionate factors in this context. Application context: The jurisprudence cited by the applicant does not apply to the consideration of humanitarian and compassionate factors in this context. Evidence spans paragraphs 55-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4240254` offsets `81-88`; context: [55] Humanitarian or personal factors are to be considered in a determination of whether cruel or unusual treatment will occur: Canepa v.
- Evidence: `party_position` cue `submits` at chunk `4240255` offsets `20-27`; context: [56] The respondent submits that the Charter is not engaged, based on the evidence before the PRRA officer.
- Evidence: `evidence_fact` cue `evidence` at chunk `4240255` offsets `74-82`; context: [56] The respondent submits that the Charter is not engaged, based on the evidence before the PRRA officer.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4240255` offsets `112-125`; context: The jurisprudence cited by the applicant does not apply to the consideration of humanitarian and compassionate factors in this context.
- Evidence: `reasoning_application` cue `apply` at chunk `4240255` offsets `158-163`; context: The jurisprudence cited by the applicant does not apply to the consideration of humanitarian and compassionate factors in this context.

#### 4127:2:subtheme:13 · paragraphs 57-60

- Raw key terms: `officer, consider, factors, respondent, submits, application, consideration, found`
- Display key terms: `officer, consider, factors, submits, consideration`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: officer, consider, factors, submits, consideration Position/evidence statements: [57] There is no indication, the respondent submits, that Mr. | Only if the officer had found the facts necessary to support one or more of these categories of harm would section 12 of the Charter have been engaged, the respondent argues. Rule/authority context: Kim made no H & C application, so the officer had no obligation to consider any factors apart from those under section 97. Application context: Kim submits that it was improper for the officer to decline to consider H & C factors given the general mandate to apply them found in subsection 25(1) of IRPA: Zolotareva v. | [60] The respondent submits that this case is distinguishable because Mr. Evidence spans paragraphs 57-60. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4240256` offsets `162-170`; context: Kim's application requested consideration on these grounds or that the PRRA officer considered this question.
- Evidence: `party_position` cue `submits` at chunk `4240256` offsets `44-51`; context: [57] There is no indication, the respondent submits, that Mr.
- Evidence: `party_position` cue `argues` at chunk `4240257` offsets `368-374`; context: Only if the officer had found the facts necessary to support one or more of these categories of harm would section 12 of the Charter have been engaged, the respondent argues.
- Evidence: `evidence_fact` cue `found that` at chunk `4240257` offsets `17-27`; context: [58] The officer found that there was, on the balance of probabilities, no reason to believe that Mr.
- Evidence: `reasoning_application` cue `apply` at chunk `4240258` offsets `165-170`; context: Kim submits that it was improper for the officer to decline to consider H & C factors given the general mandate to apply them found in subsection 25(1) of IRPA: Zolotareva v.
- Evidence: `party_position` cue `submits` at chunk `4240259` offsets `20-27`; context: [60] The respondent submits that this case is distinguishable because Mr.
- Evidence: `governing_rule` cue `under` at chunk `4240259` offsets `179-184`; context: Kim made no H & C application, so the officer had no obligation to consider any factors apart from those under section 97.
- Evidence: `reasoning_application` cue `because` at chunk `4240259` offsets `62-69`; context: [60] The respondent submits that this case is distinguishable because Mr.

#### Section text

[7] The following issues were argued before me:
1. Did the PRRA officer err in determining that Mr. Kim was not a person described in section 115(1) of IRPA and that she had jurisdiction to make the assessment?
2. Did the PRRA officer err in applying the wrong legal standard in determining risk?
3. Did the PRRA officer err in ignoring significant evidence?
4. Did the PRRA officer err in failing to consider humanitarian and compassionate circumstances of the applicant in her assessment of whether Mr. Kim would suffer cruel and unusual treatment in being removed?
5. Did the PRRA officer err in failing to consider and make a determination under section 25 of IRPA?
STANDARD OF REVIEW

[8] To date there has been no comprehensive determination of the standard of review appropriate to the different aspects of PRRA officer decisions according to the pragmatic and functional approach. The intention of Parliament regarding the level of deference that Courts should show to the decisions of administrative tribunals is central to this inquiry: Pushpanathan v. Canada (Minister of Citizenship and Immigration), [1998] 1 S.C.R. 982.

[9] Four factors must be considered for each question at issue in judicial review proceedings: the existence of any privative clause or statutory right of appeal; the purpose(s) of the legislation as a whole and the provisions at issue in particular; the nature of the question - being law, fact or mixed fact and law; and the expertise of the tribunal relative to that of the reviewing court with regard to the questions at issue: Law Society of New Brunswick v. Ryan, [2003] 1 S.C.R. 247; Dr. Q. v. College of Physicians and Surgeons of British Columbia, [2003] 1 S.C.R. 226.
1. Right of appeal/ privative clause

[10] There is no statutory right of appeal from the decisions of PRRA officers. Nor is there a preclusive or privative clause. On the contrary, there is specific provision for matters under IRPA to be subjected to judicial review by this Court. However, IRPA also imposes the additional hurdle of the necessity for leave to bring the application:
72. (1) Judicial review by the Federal Court with respect to any matter - a decision, determination or order made, a measure taken or a question raised - under this Act is commenced by making an application for leave to the Court.
72. (1) Le contrôle judiciaire par la Cour fédérale de toute mesure - décision, ordonnance, question ou affaire - prise dans le cadre de la présente loi est subordonné au dépôt d'une demande d'autorisation.
Some degree of judicial oversight is therefore contemplated, but not a full-fledged appeal. On the whole, this factor is inconclusive.
2. Purpose of the legislation and provisions in question

[11] In most instances, a PRRA decision would take into account largely the same factors as are considered in a refugee determination. The purpose as a whole of the legislation in question is set out in section 3 of IRPA; the purpose of the PRRA assessment provisions as they relate to refugee determination are particularly addressed in subsection 3(2):
3(2) The objectives of this Act with respect to refugees are
(2) S'agissant des réfugiés, la présente loi a pour objet :
(a) to recognize that the refugee program is in the first instance about saving lives and offering protection to the displaced and persecuted;
a) de reconnaître que le programme pour les réfugiés vise avant tout à sauver des vies et à protéger les personnes de la persécution;
(b) to fulfil Canada's international legal obligations with respect to refugees and affirm Canada's commitment to international efforts to provide assistance to those in need of resettlement;
b) de remplir les obligations en droit international du Canada relatives aux réfugiés et aux personnes déplacées et d'affirmer la volonté du Canada de participer aux efforts de la communauté internationale pour venir en aide aux personnes qui doivent se réinstaller;
c) to grant, as a fundamental expression of Canada's humanitarian ideals, fair consideration to those who come to Canada claiming persecution;
c) de faire bénéficier ceux qui fuient la persécution d'une procédure équitable reflétant les idéaux humanitaires du Canada;
(d) to offer safe haven to persons with a well-founded fear of persecution based on race, religion, nationality, political opinion or membership in a particular social group, as well as those at risk of torture or cruel and unusual treatment or punishment;
d) d'offrir l'asile à ceux qui craignent avec raison d'être persécutés du fait de leur race, leur religion, leur nationalité, leurs opinions politiques, leur appartenance à un groupe social en particulier, ainsi qu'à ceux qui risquent la torture ou des traitements ou peines cruels et inusités;
(e) to establish fair and efficient procedures that will maintain the integrity of the Canadian refugee protection system, while upholding Canada's respect for the human rights and fundamental freedoms of all human beings;
e) de mettre en place une procédure équitable et efficace qui soit respectueuse, d'une part, de l'intégrité du processus canadien d'asile et, d'autre part, des droits et des libertés fondamentales reconnus à tout être humain;
(f) to support the self-sufficiency and the social and economic well-being of refugees by facilitating reunification with their family members in Canada;
f) d'encourager l'autonomie et le bien-être socioéconomique des réfugiés en facilitant la réunification de leurs familles au Canada;
(g) to protect the health and safety of Canadians and to maintain the security of Canadian society; and
g) de protéger la santé des Canadiens et de garantir leur sécurité;
(h) to promote international justice and security by denying access to Canadian territory to persons, including refugee claimants, who are security risks or serious criminals.
h) de promouvoir, à l'échelle internationale, la sécurité et la justice par l'interdiction du territoire aux personnes et demandeurs d'asile qui sont de grands criminels ou constituent un danger pour la sécurité.

[12] However, in Mr. Kim's case, he is excluded from refugee consideration because of the operation of paragraph 112(3)(b). Consequently, only those purposes specifically related to protected persons apply to this particular PRRA decision.

[13] The purpose of requiring a PRRA analysis is ultimately to honour Canada's international obligations under the Convention Against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment. Given this specific context, I find that two purposes under paragraphs 3(2)(d) and (e) above are particularly engaged in the "risk assessment" portion of a PRRA decision: to offer safe haven to persons at risk of torture or cruel and unusual treatment or punishment, as well as upholding Canada's respect for the human rights and fundamental freedoms of all human beings.

[14] As noted by Justice Martineau in Umba v. Canada (Minister of Citizenship and Immigration) (2004), 257 F.T.R. 169 in the context of Refugee Protection Board hearings at para. 25:
[T]he establishment of Convention refugee status or the status of a "person in need of protection" pursuant to sections 96 and 97 of the Act is based on specific requirements that must be established by the claimant. Thus, the application of these provisions is directly related to the personal situation of each claimant and the particular conditions of the country in question at the time that the claim for asylum or protection is brought before the Board. In practice, it is therefore clear that the determination of the status of "refugee" or of a "person in need of protection" does not depend on "the consideration of numerous interests simultaneously, and the promulgation of solutions which concurrently balance benefits and costs for many different parties". In my opinion, it is more a decision establishing the rights between the parties [...] than it is a polycentric decision.
I agree with this analysis. Balancing competing policy concerns ought not enter into a PRRA analysis any more than a Refugee Protection Board analysis. This factor points towards less deference.
3. Nature of the questions in dispute

[15] The issues raised on this judicial review fall into different categories. The first question is whether the PRRA officer had jurisdiction to do an assessment of Mr. Kim's case for protection. This is clearly a question of law, as is the determination of the appropriate legal standard, the second issue. The third issue goes to the assessment of evidence. This is a factual determination. The fourth and fifth questions require an assessment of whether a particular law is applicable to Mr. Kim's situation. While this is ultimately a question of mixed fact and law, there must be a preliminary determination of what the law pertaining to cruel and unusual treatment and to section 25 of IRPA actually is before it can be applied to the facts as found.
4. Expertise of the decision-maker

[16] The expertise of the PRRA officer is variable, depending on the nature of the question considered. With respect to country conditions, PRRA officers can be said to have extensive expertise. They are required to do research to assess the level of protection and other country conditions for each application. As noted in the Citizenship and Immigration Canada Manual for PRRA officers, PP-03 "Pre-removal Risk Assessment (PPRA)" at 11.02, "One of the implicit assumptions about PRRA is that the PRRA decision-maker will become, over time and through experience, very knowledgeable on many countries." As such, a significant degree of deference should be given to conclusions on country conditions. Furthermore, with respect to other facts necessary to complete the assessment, the Court is in no better position than the PRRA officer, and if an oral interview is conducted, is arguably in a worse position to determine the facts. A high degree of deference should be shown to this sort of expertise.

[17] By contrast, the PRRA officers do not have the same level of expertise regarding questions of law as does this Court. While the officer receives training on the relevant law, he or she need not have a general legal background, and likely has familiarity with only the IRPA and IRP Regulations as they relate to his or her functions. A higher degree of deference is necessary only when the decision-making body has, in some way, a greater expertise than the reviewing court and the particular issue pertains to this greater expertise: Moreau-Bérubé v. New Brunswick (Judicial Council), [2002] 1 S.C.R. 249 at para. 50. This is not the case here. In my view, very little deference ought to be shown to the expertise of PRRA officers on such legal questions as determination of jurisdiction or interpretation of the relevant law. Finally, as discussed below, I do not find that an exercise of discretion is relevant to any aspect of a PRRA decision, so no additional deference needs to be accorded to the decision-maker on that account.

[18] When it comes to the application of the law to the facts, the PRRA officer has some training and experience, but not the same level of expertise as a Court. Particularly, for those questions of mixed fact and law in which the officer is dealing with law outside his or her training and everyday experience, little deference should be shown. Somewhat more deference should nonetheless be shown in cases where the PRRA officer is dealing with questions of mixed fact and law for which they can be expected to have some knowledge, training, and experience, such as the application of the legal definition of protected person to the facts of a given case.

[19] Combining and balancing all of these factors, I conclude that in the judicial review of PRRA decisions the appropriate standard of review for questions of fact should generally be patent unreasonableness, for questions of mixed law and fact, reasonableness simpliciter, and for questions of law, correctness. I am fortified in my conclusions by the positions taken by my colleagues in other recent PRRA decisions.

[20] In Tekie v. Canada (Minister of Citizenship and Immigration) 2005 FC 27 at para. 6, Justice Phelan found:
The standard of review of credibility findings, which is at the heart of this PRRA decision, is patent unreasonableness. With respect to findings on specific facts, the Federal Court Act s. 18.1(4)(d) sets the standard as "an erroneous finding of fact made in a perverse or capricious manner or without regard for the material before it".
In Figurado v. Canada 2005 FC 347 at para. 51, Justice Martineau agreed that the standard of review for findings of fact by a PRRA officer is that found in paragraph 18.1(4)(d) of the Federal Courts Act, R.S.C. 1985, c. F-7, as amended. Findings of fact are not to be made in a perverse or capricious manner or without regard to the material before the tribunal. This is equivalent to a standard of review of patent unreasonableness.

[21] There has also been previous agreement in this Court that when a question of law has been decided by a PRRA officer, the appropriate standard of review is correctness: Singh v. Canada (Minister of Citizenship and Immigration) [2004] 3 F.C.R. 323 at para. 12 (per Russell J); Gonulcan c. Canada (Ministre de la Citoyenneté et de l'Immigration) 2005 CF 32 (per Teitelbaum J).

[22] Finally, I also note Justice Martineau's opinion that the appropriate standard of review for the decision of a PRRA officer is reasonableness simpliciter when the decision is considered "globally and as a whole", which I take to mean the application of the relevant law to the facts as found by the officer: Figurado, supra.
ARGUMENT & ANALYSIS

[23] As a preliminary matter, Mr. Kim objects to the admissibility of the affidavit of John R. Butt, an immigration official, on the ground that it contains legal argument. In my view, the affidavit explains the historical state and evolution of immigration policy, practices, and programs from the early 1970s onward. The statements do not contain legal argument, but statements about what Mr. Butt understood the state of the law to have been at various points in time. I am alive to the fact that Mr. Butt is one immigration official among many, and that he is simply expressing his opinion and understanding of the relevant facts. The applicant's concerns would have been better addressed by means of a cross-examination on the affidavit (which was not performed), rather than by its exclusion. The affidavit is accepted as filed.
1. Jurisdiction

[24] The applicant submits that because Mr. Kim was found to be a mandate refugee by the UNHCR, and because he was accepted as a member of the Indochinese Designated Class, the PRRA officer should have considered that Mr. Kim is a person described in subsection 115(1) of IRPA, which prohibits the removal of a Convention refugee or protected person, and that the PRRA officer did not, therefore, have jurisdiction to consider the application.

[25] Section 95 of IRPA describes protected persons as those who have been determined to be Convention refugees or are persons "in similar circumstances". Section 12 states that the determination that "a person in similar circumstances" takes into account "Canada's humanitarian tradition with respect to the displaced and the persecuted".

[26] Regulations made under section 12 IRPA designated the Country of Asylum Class and the Source Country Class (IRP Regulations, sections 146 and 147). These are new classes that did not exist at the time that Mr. Kim entered Canada. However, the same humanitarian principles applied in 1984 in the Immigration Act and Regulations under which Mr. Kim was admitted: Immigration Act, section 6, and Regulations, section 3.

[27] The definition of refugee used by the UNHCR is almost identical to that used under the Refugee Convention and IRPA: Statute on the Office of the United Nations High Commissioner for Refugees, 1950, Article 6B.

[28] Although the Indochinese Designated Class ceased to exist in 1997, neither the Immigration Regulations nor IRPA expressly and retroactively disbanded the class recognition: Interpretation Act, section 43; Brosseau v. Alberta Securities Commission, [1989] 1 S.C.R. 301. The rights in issue are fundamental human rights and so the presumption that there was no change is even stronger: R. v. Mercure, [1988] 1 S.C.R. 234.

[29] Mr. Kim argues that he has never lost his status as a person who was displaced and persecuted, so he is not subject to removal under subsection 115(1) of IRPA. He has not been declared a danger to the public under subsection 115(2), and no such determination was made under the precursor section 53 of the Immigration Act: Suresh v. Canada, [2002] 1 S.C.R. 3. Thus, the PRRA officer had no jurisdiction.

[30] The respondent submits that Mr. Kim is neither a Convention refugee nor a protected person. He is not protected from refoulement under subsection 115(1) because he is not recognized as a refugee by another country and is not a protected person under IRPA.

[31] Mandate refugees are recognized as such only by the UNHCR, which is not another country, but an international organization. Mr. Kim entered Canada as a permanent resident and his membership in the Indochinese Designated Class was never predicated on his being a mandate refugee.

[32] The respondent submits that Mr. Kim is not a protected person underIRPA because he has never been found to be a Convention refugee either here or in any other country. The statutory language only envisions members of the Country of Asylum and the Source Country classes being considered a "person in similar circumstances": IRPA sections 95; IRP Regulations sections 146, 147.

[33] The transitional provisions of the IRP Regulations specify which people will continue to be considered refugees under IRPA: Regulations section 338. Mr. Kim does not fit the definition of a person whose refugee status will continue to be recognized under IRPA. Members of the Indochinese Designated Class were exempt from section 7 of the old Regulations and could not have applied under section 4 of the Humanitarian Designated Class Regulations, as these came into force in 1997 at the same time as the Indochinese Designated Class was repealed.

[34] The respondent submits that Mr. Kim has no vested rights against removal simply because he came to Canada as part of a designated class for humanitarian purposes. He was granted admission as a landed immigrant, not as a refugee.

[35] When Mr. Kim committed his criminal offences, he became inadmissible under the old Immigration Act and was ordered deported. Different categories of individuals are treated variously under the Immigration Act scheme, and the respondent argues, this is acceptable: Canada (Minister of Employment and Immigration) v. Chiarelli, [1992] 1 S.C.R. 711. Permanent residents have no explicit statutory protection against removal to a state where they believe their life or freedom would be threatened: Chieu v. Canada (Minister of Citizenship and Immigration), [2002] 1 S.C.R. 84 at 116-117; Suresh v. Canada (Minister of Citizenship and Immigration), [2002] 1 S.C.R. 3.

[36] The respondent submits that even if Mr. Kim was found to be a protected person, he would still be deportable under subsection 115(2) of IRPA.

[37] The PRRA officer correctly exercised her jurisdiction to determine whether a person not covered by the non-refoulement provisions might nonetheless be at risk if removed from Canada, the respondent argues. People with serious criminal convictions are only entitled to consideration under section 97: IRPA subsections 112(3), 113(d).

[38] I must agree with the respondent's position. The applicant's arguments centre around the proposition that his case is falling through the cracks because Parliament never explicitly acknowledged that members of the Indochinese Designated Class were refugees, either under the Immigration A

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 4127:3 · paragraphs 61-71

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f5a3a6d2466f7299028115c831bf8eb66de7e3798da96b46265d368d1c8922dc`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4127:3:subtheme:1 · paragraphs 61-65

- Raw key terms: `factors, officer, address, applicant's, application, assessment, based, case`
- Display key terms: `factors, officer, address, applicant's, assessment, based, case`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule Display terms: factors, officer, address, applicant's, assessment, based, case Rule/authority context: These factors pertain to an application under the humanitarian and compassionate program, rather than this application for protection based on an assessment of pre-determined risk factors, in the country of nationality. Evidence spans paragraphs 61-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4240260` offsets `481-486`; context: These factors pertain to an application under the humanitarian and compassionate program, rather than this application for protection based on an assessment of pre-determined risk factors, in the country of nationality.
- Evidence: `evidence_fact` cue `evidence` at chunk `4240262` offsets `416-424`; context: Here, there is no evidence of a separate H & C application, let alone that such an application was before the officer.
- Evidence: `counterargument_limitation` cue `However` at chunk `4240264` offsets `242-249`; context: However, it does not follow that the two sets of considerations must necessarily be linked in every case.

#### 4127:3:subtheme:2 · paragraphs 66-71

- Raw key terms: `compassionate, humanitarian, officer, canada, citizenship, immigration, minister, application`
- Display key terms: `compassionate, humanitarian, officer`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: compassionate, humanitarian, officer Rule/authority context: [66] The question of whether PRRA officers have an obligation to examine humanitarian and compassionate considerations if the person concerned so requests has not been squarely addressed in the jurisprudence of this Cour | 153, Justice Phelan found that an immigration officer need not consider humanitarian and compassionate factors prior to making a report pursuant to subsections 36(1) and 44(1) of IRPA. Application context: [70] By the same logic, I find that PRRA officers need not consider humanitarian and compassionate factors in making their decisions. Operative outcome context: I denied leave on the underlying PRRA application in that case. | [71] Having found no reviewable error in the decision of the officer, the application for judicial review will be dismissed. Evidence spans paragraphs 66-71. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4240265` offsets `9-17`; context: [66] The question of whether PRRA officers have an obligation to examine humanitarian and compassionate considerations if the person concerned so requests has not been squarely addressed in the jurisprudence of this Court.
- Evidence: `evidence_fact` cue `found that` at chunk `4240265` offsets `341-351`; context: Canada (Minister of Citizenship and Immigration) 2004 FC 67, Justice Phelan found that this question met the low threshold to be accepted as a serious issue but made no further comment.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4240265` offsets `194-207`; context: [66] The question of whether PRRA officers have an obligation to examine humanitarian and compassionate considerations if the person concerned so requests has not been squarely addressed in the jurisprudence of this Court.
- Evidence: `counterargument_limitation` cue `but` at chunk `4240265` offsets `422-425`; context: Canada (Minister of Citizenship and Immigration) 2004 FC 67, Justice Phelan found that this question met the low threshold to be accepted as a serious issue but made no further comment.
- Evidence: `disposition` cue `denied` at chunk `4240265` offsets `453-459`; context: I denied leave on the underlying PRRA application in that case.
- Evidence: `evidence_fact` cue `found that` at chunk `4240268` offsets `107-117`; context: 153, Justice Phelan found that an immigration officer need not consider humanitarian and compassionate factors prior to making a report pursuant to subsections 36(1) and 44(1) of IRPA.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4240268` offsets `223-234`; context: 153, Justice Phelan found that an immigration officer need not consider humanitarian and compassionate factors prior to making a report pursuant to subsections 36(1) and 44(1) of IRPA.
- Evidence: `reasoning_application` cue `I find` at chunk `4240269` offsets `24-30`; context: [70] By the same logic, I find that PRRA officers need not consider humanitarian and compassionate factors in making their decisions.
- Evidence: `disposition` cue `dismissed` at chunk `4240270` offsets `114-123`; context: [71] Having found no reviewable error in the decision of the officer, the application for judicial review will be dismissed.

#### Section text

[61] The officer found as follows:
While the applicant's submissions provide information about his lack of a support network in Cambodia, they also address the applicant's desire to be "given a second chance at life" and becoming a productive member of Canadian society. Whatever factors fall within a humanitarian and compassionate application context, I cannot evaluate as it is not within the mandate of this pre-removal risk assessment. These factors pertain to an application under the humanitarian and compassionate program, rather than this application for protection based on an assessment of pre-determined risk factors, in the country of nationality.

[62] This is clearly a finding of law or jurisdiction, and should be reviewed on a standard of correctness.

[63] I agree with the respondent that Zolotareva is distinguishable. First, Zolotareva did not find a requirement for PRRA officers to consider H & C factors, but that it was permissible for the PRRA officer in that case to represent the Minister for the purpose of the H & C application as well as the PRRA assessment. In that case, the officer was performing the assessment of both applications. Here, there is no evidence of a separate H & C application, let alone that such an application was before the officer.

[64] Zolotareva does not, in fact, address the applicant's underlying argument, which, as I understand it, is that according to subsection 25(1) of IRPA, humanitarian and compassionate factors must be considered by any ministerial delegate if there is a request for examination of the applicant's circumstances. Subsection 25(1) reads as follows:
25. (1) The Minister shall, upon request of a foreign national who is inadmissible or who does not meet the requirements of this Act, and may, on the Minister's own initiative, examine the circumstances concerning the foreign national and may grant the foreign national permanent resident status or an exemption from any applicable criteria or obligation of this Act if the Minister is of the opinion that it is justified by humanitarian and compassionate considerations relating to them, taking into account the best interests of a child directly affected, or by public policy considerations.
25. (1) Le ministre doit, sur demande d'un étranger interdit de territoire ou qui ne se conforme pas à la présente loi, et peut, de sa propre initiative, étudier le cas de cet étranger et peut lui octroyer le statut de résident permanent ou lever tout ou partie des critères et obligations applicables, s'il estime que des circonstances d'ordre humanitaire relatives à l'étranger -- compte tenu de l'intérêt supérieur de l'enfant directement touché -- ou l'intérêt public le justifient.

[65] Risk assessments performed by PRRA officers are often considered by officers who are making H & C determinations. It is also now common practice for the same officer to perform a PRRA and H & C decision based upon the same set of facts. However, it does not follow that the two sets of considerations must necessarily be linked in every case.

[66] The question of whether PRRA officers have an obligation to examine humanitarian and compassionate considerations if the person concerned so requests has not been squarely addressed in the jurisprudence of this Court. In a recent stay application in Sowkey v. Canada (Minister of Citizenship and Immigration) 2004 FC 67, Justice Phelan found that this question met the low threshold to be accepted as a serious issue but made no further comment. I denied leave on the underlying PRRA application in that case.

[67] In another stay application, Justice MacKay noted in obiter that he was not satisfied that a PRRA officer had any responsibility for assessing humanitarian and compassionate considerations: Obando v. Canada (Minister of Citizenship and Immigration) 2003 FCT 668.

[68] The level of discretion that can be exercised by a decision-maker has been the primary concern in recent decisions in this Court as to when humanitarian and compassionate factors should be considered by a removals officer. In brief, the consensus in this Court has been that only a very limited assessment of H & C factors is appropriate in this context: Benitez v. Canada (Minister of Citizenship and Immigration)(2001), 214 F.T.R. 282; Davis v. Canada (Minister of Citizenship and Immigration) [2000] F.C.J. No. 1628; Simoes v. Canada (Minister of Citizenship and Immigration) (2000), 187 F.T.R. 219.

[69] In Correia v. Canada (Minister of Citizenship and Immigration) (2004), 253 F.T.R. 153, Justice Phelan found that an immigration officer need not consider humanitarian and compassionate factors prior to making a report pursuant to subsections 36(1) and 44(1) of IRPA. In particular, he focussed on the low level of discretion accorded to immigration officers under IRPA in making decisions regarding serious criminality and the limited nature of the inquiry.

[70] By the same logic, I find that PRRA officers need not consider humanitarian and compassionate factors in making their decisions. There is no discretion afforded to a PRRA officer in making a risk assessment. Either the officer is satisfied that the risk factors alleged exist and are sufficiently serious to grant protection, or the officer is not satisfied. The PRRA inquiry and decision-making process does not take into account factors other than risk. In any case, there is a better forum for the consideration of humanitarian and compassionate factors: the H & C determination mechanism. I do not find that the officer erred in law by refusing to consider humanitarian and compassionate factors in the context of the PRRA decision.

[71] Having found no reviewable error in the decision of the officer, the application for judicial review will be dismissed.
Questions for certification

## 4127:4 · paragraphs 72-75

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ae0b9bd7f366332336a185c33ab2cb7d9e5d51a0040f2d23163ea23342136aae`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4127:4:subtheme:1 · paragraphs 72-73

- Raw key terms: `applicant, person, question, refugee, appropriate, because, canada, certification`
- Display key terms: `person, question, refugee, appropriate, because, certification`
- Argument roles: `disposition, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, party_position, reasoning_application Display terms: person, question, refugee, appropriate, because, certification Position/evidence statements: [73] The respondent submits that a more appropriate way to phrase this question would be: Is the Applicant, who was granted permanent resident status under the former Indochinese Designated Class Regulations, a "protecte Rule/authority context: [72] The applicant suggested the following question for certification: Is the Applicant a person described in subsection 115(1) of IRPA and not subject to removal from Canada, subject to subsection 115(2), because he is  | [73] The respondent submits that a more appropriate way to phrase this question would be: Is the Applicant, who was granted permanent resident status under the former Indochinese Designated Class Regulations, a "protecte Application context: [72] The applicant suggested the following question for certification: Is the Applicant a person described in subsection 115(1) of IRPA and not subject to removal from Canada, subject to subsection 115(2), because he is  Operative outcome context: [73] The respondent submits that a more appropriate way to phrase this question would be: Is the Applicant, who was granted permanent resident status under the former Indochinese Designated Class Regulations, a "protecte Evidence spans paragraphs 72-73. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4240271` offsets `43-51`; context: [72] The applicant suggested the following question for certification:
Is the Applicant a person described in subsection 115(1) of IRPA and not subject to removal from Canada, subject to subsection 115(2), because he is a person in similar circumstances to a Convention refugee pursuant to paragraph 95(1)(a) of IRPA?
- Evidence: `governing_rule` cue `pursuant to` at chunk `4240271` offsets `278-289`; context: [72] The applicant suggested the following question for certification:
Is the Applicant a person described in subsection 115(1) of IRPA and not subject to removal from Canada, subject to subsection 115(2), because he is a person in similar circumstances to a Convention refugee pursuant to paragraph 95(1)(a) of IRPA?
- Evidence: `reasoning_application` cue `because` at chunk `4240271` offsets `206-213`; context: [72] The applicant suggested the following question for certification:
Is the Applicant a person described in subsection 115(1) of IRPA and not subject to removal from Canada, subject to subsection 115(2), because he is a person in similar circumstances to a Convention refugee pursuant to paragraph 95(1)(a) of IRPA?
- Evidence: `issue` cue `question` at chunk `4240272` offsets `71-79`; context: [73] The respondent submits that a more appropriate way to phrase this question would be:
Is the Applicant, who was granted permanent resident status under the former Indochinese Designated Class Regulations, a "protected person" within the meaning of sections 95 and 115 of the Immigration and Refugee Protection Act?
- Evidence: `party_position` cue `submits` at chunk `4240272` offsets `20-27`; context: [73] The respondent submits that a more appropriate way to phrase this question would be:
Is the Applicant, who was granted permanent resident status under the former Indochinese Designated Class Regulations, a "protected person" within the meaning of sections 95 and 115 of the Immigration and Refugee Protection Act?
- Evidence: `governing_rule` cue `under` at chunk `4240272` offsets `150-155`; context: [73] The respondent submits that a more appropriate way to phrase this question would be:
Is the Applicant, who was granted permanent resident status under the former Indochinese Designated Class Regulations, a "protected person" within the meaning of sections 95 and 115 of the Immigration and Refugee Protection Act?
- Evidence: `disposition` cue `granted` at chunk `4240272` offsets `116-123`; context: [73] The respondent submits that a more appropriate way to phrase this question would be:
Is the Applicant, who was granted permanent resident status under the former Indochinese Designated Class Regulations, a "protected person" within the meaning of sections 95 and 115 of the Immigration and Refugee Protection Act?

#### 4127:4:subtheme:2 · paragraphs 74-75

- Raw key terms: `canada, general, admitted, answers, appeal, applicant's, application, beyond`
- Display key terms: `admitted, answers, applicant's, beyond`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue Display terms: admitted, answers, applicant's, beyond Rule/authority context: What legal effect, if any, has a designation of by the UNHCR as a "mandate refugee" on the determination of whether an individual is a protected person under sections 95, 112, and 115? Operative outcome context: ORDER THIS COURT ORDERS that the application for judicial review is dismissed. Evidence spans paragraphs 74-75. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4240273` offsets `43-51`; context: [74] In my view, the applicant's suggested question is too broad, while the respondent's is too narrow to be of general application.
- Evidence: `governing_rule` cue `under` at chunk `4240273` offsets `439-444`; context: What legal effect, if any, has a designation of by the UNHCR as a "mandate refugee" on the determination of whether an individual is a protected person under sections 95, 112, and 115?
- Evidence: `counterargument_limitation` cue `However` at chunk `4240273` offsets `133-140`; context: However, the two questions phrased as follows would raise questions of law of general application whose answers would be determinative of this appeal:
1.
- Evidence: `disposition` cue `dismissed` at chunk `4240273` offsets `1104-1113`; context: ORDER
THIS COURT ORDERS that the application for judicial review is dismissed.

#### Section text

[72] The applicant suggested the following question for certification:
Is the Applicant a person described in subsection 115(1) of IRPA and not subject to removal from Canada, subject to subsection 115(2), because he is a person in similar circumstances to a Convention refugee pursuant to paragraph 95(1)(a) of IRPA?

[73] The respondent submits that a more appropriate way to phrase this question would be:
Is the Applicant, who was granted permanent resident status under the former Indochinese Designated Class Regulations, a "protected person" within the meaning of sections 95 and 115 of the Immigration and Refugee Protection Act?

[74] In my view, the applicant's suggested question is too broad, while the respondent's is too narrow to be of general application. However, the two questions phrased as follows would raise questions of law of general application whose answers would be determinative of this appeal:
1. What legal effect, if any, has a designation of by the UNHCR as a "mandate refugee" on the determination of whether an individual is a protected person under sections 95, 112, and 115?
2. What legal effect, if any, does a successful application for permanent residence under the former Indochinese Designated Class Regulations have upon a determination of whether an individual is a protected person under sections 95, 112, and 115?
These are question of law, the result of which would have an impact beyond the facts of this case. The status of mandate refugees within the IRPA scheme is a question that warrants scrutiny, as is the question of the legal position occupied by persons admitted to Canada as part of the Indochinese designated class.
ORDER
THIS COURT ORDERS that the application for judicial review is dismissed. The following questions are certified for consideration by the Federal Court of Appeal:
1. What legal effect, if any, has a designation by the UNHCR as a "mandate refugee" on the determination of whether an individual is a protected person under sections 95, 112, and 115?
2. What legal effect, if any, does a successful application for permanent residence under the former Indochinese Designated Class Regulations have upon a determination of whether an individual is a protected person under sections 95, 112, and 115?
" Richard G. Mosley "
F.C.J.
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-1868-04
STYLE OF CAUSE: RITH KIM
AND
THE MINISTER OF CITIZENSHIP AND
IMMIGRATION
THE SOLICITOR GENERAL OF CANADA
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: January 27, 2005
REASONS FOR 

## 4127:5 · paragraphs 76-76

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `cf5578d5e67a60346da947469300d12229e5013e2f485f6aeb032a99b27824c2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4127:5:subtheme:1 · paragraphs 76-76

- Raw key terms: `anshumala, appearances, applicant, april, associates, attorney, canada, dagenais`
- Display key terms: `anshumala, april, associates, dagenais`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: anshumala, april, associates, dagenais No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 76-76. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
AND ORDER BY : The Honourable Mr. Justice Mosley
DATED: April 1, 2005
APPEARANCES:
Ron Poulton FOR THE APPLICANT
Diane Dagenais FOR THE RESPONDENTS
Anshumala Juyal
SOLICITORS OF RECORD:
RON POULTON FOR THE APPLICANT
Mamann & Associates
Toronto, Ontario
JOHN H. SIMS, Q.C. FOR THE RESPONDENTS
Deputy Attorney General of Canada
Toronto, Ontario
