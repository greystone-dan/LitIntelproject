# Discussion Units: case 22164

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **54**
- Continuity pairs: **53**
- Discussion Units: **4**
- Paragraph source hashes: **54**
- Sub-themes: **14**

## 22164:1 · paragraphs 0-20

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a69f9670f64c9c16e704ff1eeabd4a83cc9fa4170dd6d671cd8e10ab81b52899`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22164:1:subtheme:1 · paragraphs 0-9

- Raw key terms: `applicants, gang, guatemala, canada, city, decided, decision, police`
- Display key terms: `gang, guatemala, city, decided, police`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: gang, guatemala, city, decided, police Rule/authority context: [1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board) dated January 7, 2009 concluding that the applicant, a Guatemalan citizen,  | The applicants were warned not to report the gang under pain of death. Application context: The applicants arrived in Canada on November 2, 2006 seeking refugee protection because of an alleged fear of persecution or death at the hands of a Guatemalan mara or gang. Evidence spans paragraphs 0-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5039521` offsets `282-293`; context: [1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board) dated January 7, 2009 concluding that the applicant, a Guatemalan citizen, is not a Convention refugee or a person in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, S.
- Evidence: `reasoning_application` cue `because` at chunk `5039522` offsets `157-164`; context: The applicants arrived in Canada on November 2, 2006 seeking refugee protection because of an alleged fear of persecution or death at the hands of a Guatemalan mara or gang.
- Evidence: `governing_rule` cue `under` at chunk `5039524` offsets `166-171`; context: The applicants were warned not to report the gang under pain of death.
- Evidence: `governing_rule` cue `under` at chunk `5039528` offsets `179-184`; context: Decision under review

#### 22164:1:subtheme:2 · paragraphs 10-12

- Raw key terms: `applicants, board, because, address, adequate, alleged, alternatively, convention`
- Display key terms: `because, address, adequate, alleged, alternatively, convention`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: because, address, adequate, alleged, alternatively, convention Rule/authority context: [12] The Board held that the applicants are not persons in need of protection because the risk that they feared was a generalized one, which is excluded from protection under subsection 97(1)(b)(ii) of IRPA, or alternati Application context: [11] The Board determined that the applicants are not Convention refugees because the fear alleged by the applicants had no nexus to any of the grounds in the Convention refugee definition. | [12] The Board held that the applicants are not persons in need of protection because the risk that they feared was a generalized one, which is excluded from protection under subsection 97(1)(b)(ii) of IRPA, or alternati Evidence spans paragraphs 10-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5039530` offsets `35-40`; context: [10] The Board did not address the issue of the applicants’ credibility.
- Evidence: `evidence_fact` cue `determined that` at chunk `5039531` offsets `15-30`; context: [11] The Board determined that the applicants are not Convention refugees because the fear alleged by the applicants had no nexus to any of the grounds in the Convention refugee definition.
- Evidence: `reasoning_application` cue `because` at chunk `5039531` offsets `74-81`; context: [11] The Board determined that the applicants are not Convention refugees because the fear alleged by the applicants had no nexus to any of the grounds in the Convention refugee definition.
- Evidence: `governing_rule` cue `under` at chunk `5039532` offsets `169-174`; context: [12] The Board held that the applicants are not persons in need of protection because the risk that they feared was a generalized one, which is excluded from protection under subsection 97(1)(b)(ii) of IRPA, or alternatively that the applicants failed to show that the state of Guatemala was unable or unwilling to provide them with adequate state protection.
- Evidence: `reasoning_application` cue `because` at chunk `5039532` offsets `78-85`; context: [12] The Board held that the applicants are not persons in need of protection because the risk that they feared was a generalized one, which is excluded from protection under subsection 97(1)(b)(ii) of IRPA, or alternatively that the applicants failed to show that the state of Guatemala was unable or unwilling to provide them with adequate state protection.

#### 22164:1:subtheme:3 · paragraphs 13-14

- Raw key terms: `board, business, faced, owners, risk, small, applicants, basis`
- Display key terms: `business, faced, owners, risk, small, basis`
- Argument roles: `evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, reasoning_application Display terms: business, faced, owners, risk, small, basis Rule/authority context: The Board held that the risk the applicants experienced was generalized, rather then individualized or personalized, and therefore excluded the applicants from protection under subsection 97(1)(b) of IRPA. Application context: The Board held that the risk the applicants experienced was generalized, rather then individualized or personalized, and therefore excluded the applicants from protection under subsection 97(1)(b) of IRPA. Evidence spans paragraphs 13-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `5039533` offsets `15-25`; context: [13] The Board found that Guatemala was facing an epidemic of gang violence perpetrated by maras, which target business owners and bus operators on a daily basis.
- Evidence: `governing_rule` cue `under` at chunk `5039534` offsets `364-369`; context: The Board held that the risk the applicants experienced was generalized, rather then individualized or personalized, and therefore excluded the applicants from protection under subsection 97(1)(b) of IRPA.
- Evidence: `reasoning_application` cue `therefore` at chunk `5039534` offsets `314-323`; context: The Board held that the risk the applicants experienced was generalized, rather then individualized or personalized, and therefore excluded the applicants from protection under subsection 97(1)(b) of IRPA.

#### 22164:1:subtheme:4 · paragraphs 15-19

- Raw key terms: `applicants, board, protection, state, held, adequate, democratic, evidence`
- Display key terms: `protection, state, adequate, democratic`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: protection, state, adequate, democratic Application context: The applicants claim for protection was therefore dismissed. Operative outcome context: The applicants claim for protection was therefore dismissed. Evidence spans paragraphs 15-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5039535` offsets `114-119`; context: [15] The Board held that even if the applicants were not excluded by subsection 97(1)(b) of IRPA, a determinative issue in this case is the adequacy of state protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039536` offsets `595-603`; context: The Board held that the applicants failed to rebut the presumption of adequate state protection with “clear and convincing” evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039537` offsets `33-41`; context: [17] A review of the documentary evidence led the Board to place a heavy burden on the applicants to show that they took reasonable steps to obtain state protection.
- Evidence: `reasoning_application` cue `therefore` at chunk `5039539` offsets `295-304`; context: The applicants claim for protection was therefore dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `5039539` offsets `305-314`; context: The applicants claim for protection was therefore dismissed.

#### 22164:1:subtheme:5 · paragraphs 20-20

- Raw key terms: `accepted, adequate, against, alors, article, autres, avail, avait`
- Display key terms: `accepted, adequate, against, alors, article, autres, avail, avait`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: accepted, adequate, against, alors, article, autres, avail, avait Application context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subj Evidence spans paragraphs 20-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `5039540` offsets `2070-2076`; context: ISSUES
- Evidence: `reasoning_application` cue `because` at chunk `5039540` offsets `550-557`; context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not
have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning
of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the
protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard
of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.

#### Section text

Rodriguez Perez v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2009-10-14
Neutral citation
2009 FC 1029
File numbers
IMM-646-09
Decision Content
Date: 20091014
Docket: IMM-646-09
Citation: 2009 FC 1029
Ottawa, Ontario, October 14, 2009
PRESENT: The Honourable Mr. Justice Kelen
BETWEEN:
HENRY SOTERO RODRIGUEZ PEREZ;
MARVIN ROLANDAO RODRIGUEZ PEREZ
Applicants
and
THE MINISTER OF
CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board) dated January 7, 2009 concluding that the applicant, a Guatemalan citizen, is not a Convention refugee or a person in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (the IRPA).
FACTS

[2] The applicants are twenty-six and thirty year old brothers respectively. The applicants arrived in Canada on November 2, 2006 seeking refugee protection because of an alleged fear of persecution or death at the hands of a Guatemalan mara or gang.

[3] The applicants opened a grocery store in Guatemala City in September 2005. In April 2006 the store was robbed by five gang members while one of the applicants was present. The applicants decided not to report the robbery to the police.

[4] In May 2006 the same gang returned and proceeded to extort the applicants in return for keeping the store open. The applicants were warned not to report the gang under pain of death. The applicants decided not to report the extortion to the police out of fear for their lives and dutifully paid the weekly extortion fee for about a month.

[5] In the beginning of June 2006 the applicants decided to stop paying the gang since the payments were consuming almost half their revenues. The store was closed and the applicants returned to their home town of El Camalote, Gualan, Zapaca, which is about four hours by bus from Guatemala City.

[6] A week after moving to their home town one of the applicants received a phone call from an unidentified caller who told them that the gang knows where the applicants live and is expecting the applicants to continue paying gang’s extortion fees.

[7] The applicants contacted the chief of police in Gualan who promised to contact the police in Guatemala City, but he warned the applicants that if the complaint involved a mara gang, not much will be done.

[8] Fearing their safety, the applicants left Guatemala and travelled through the United States to Canada where they made a claim for refugee status on November 2, 2006.
Decision under review

[9] On January 7, 2009, the Board concluded that the applicants were not Convention refugees or persons in need of protection.

[10] The Board did not address the issue of the applicants’ credibility. Thus it is presumed to be true.

[11] The Board determined that the applicants are not Convention refugees because the fear alleged by the applicants had no nexus to any of the grounds in the Convention refugee definition.

[12] The Board held that the applicants are not persons in need of protection because the risk that they feared was a generalized one, which is excluded from protection under subsection 97(1)(b)(ii) of IRPA, or alternatively that the applicants failed to show that the state of Guatemala was unable or unwilling to provide them with adequate state protection.

[13] The Board found that Guatemala was facing an epidemic of gang violence perpetrated by maras, which target business owners and bus operators on a daily basis. Being a victim of crime and violence at the hands of the maras in Guatemala was a daily risk for small business owners who faced extortion demands or the prospects of criminal violence.

[14] The Board referred to the submissions of the applicants’ counsel that the risk faced by the claimants “is a risk that is faced by small business owners and is not an individualized risk”. The Board held that the risk the applicants experienced was generalized, rather then individualized or personalized, and therefore excluded the applicants from protection under subsection 97(1)(b) of IRPA.

[15] The Board held that even if the applicants were not excluded by subsection 97(1)(b) of IRPA, a determinative issue in this case is the adequacy of state protection.

[16] The Board reviewed the law governing the presumption of state protection. It stated that local failures to provide effective policing do not amount to inadequate protection. Relying upon the decision of the Federal Court of Appeal in Kadenko v. Canada (Solicitor General) (1996), 143 D.L.R. (4th) 532, the Board stated that "the more democratic the state's institutions, the more the claimant must have done to exhaust all the courses of action open to him or her". The Board held that the applicants failed to rebut the presumption of adequate state protection with “clear and convincing” evidence.

[17] A review of the documentary evidence led the Board to place a heavy burden on the applicants to show that they took reasonable steps to obtain state protection. The documentary evidence indicated that Guatemala is a democratic state with functioning political and judicial systems, democratic institutions, and an official apparatus that provides a measure of protection to its citizens including a criminal justice system. The Board noted that Guatemala has been at the forefront of criminal reform efforts in South America and has been making strong efforts to combat the maras.

[18] The Board held that since the applicants only sought the help of the local police detachment, and not the assistance of any other law enforcement authority or government assistance agency, they could not show that they had reasonably taken steps to seek internal state protection.

[19] The Board held that since adequate state protection is available to the claimants in Guatemala the applicants do not, on the balance of probabilities, face the risk to life or a risk to cruel and unusual treatment or punishment, were they to return. The applicants claim for protection was therefore dismissed.
LEGISLATION

[20] I reproduce s. 97 of IRPA for convenience:
97. (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not
have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning
of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the
protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard
of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
97. (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au
sens de l’article premier de la Convention contre la torture;
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans
le cas suivant :
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires
de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
ISSUES

## 22164:2 · paragraphs 21-45

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `8204841b7b8391ce1f725a3041345814c519d56927242e6cead114541c0ac443`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22164:2:subtheme:1 · paragraphs 21-22

- Raw key terms: `board, issues, review, standard, accorded, accordingly, analysis, applicants`
- Display key terms: `issues, review, standard, accorded, accordingly, analysis`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: issues, review, standard, accorded, accordingly, analysis Rule/authority context: STANDARD OF REVIEW Application context: Accordingly, the deference to be accorded to the Board’s factual findings mandates that the issues in question be reviewed on a standard of reasonableness. Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5039541` offsets `30-36`; context: [21] The applicants raise two issues:
1.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039541` offsets `94-102`; context: Did the Board err in law in that it misconstrued the evidence before it and/or misinterpreted s.
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `5039541` offsets `237-255`; context: STANDARD OF REVIEW
- Evidence: `issue` cue `issues` at chunk `5039542` offsets `350-356`; context: Accordingly, the deference to be accorded to the Board’s factual findings mandates that the issues in question be reviewed on a standard of reasonableness.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5039542` offsets `258-269`; context: Accordingly, the deference to be accorded to the Board’s factual findings mandates that the issues in question be reviewed on a standard of reasonableness.

#### 22164:2:subtheme:2 · paragraphs 23-24

- Raw key terms: `canada, court, first, held, justice, para, particular, standard`
- Display key terms: `first, justice, para, particular, standard`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: first, justice, para, particular, standard Rule/authority context: 1, the Supreme Court of Canada held at paragraph 62 that the first step in conducting a standard of review analysis is to “ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of | 11 that interpreting the exclusion of generalized risks of violence under subsection 97(1)(b) of IRPA was an issue of application of law to the particular facts of a case and therefore reviewable on a standard of reasona Application context: 11 that interpreting the exclusion of generalized risks of violence under subsection 97(1)(b) of IRPA was an issue of application of law to the particular facts of a case and therefore reviewable on a standard of reasona Evidence spans paragraphs 23-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5039543` offsets `189-196`; context: 1, the Supreme Court of Canada held at paragraph 62 that the first step in conducting a standard of review analysis is to “ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of (deference) to be accorded with regard to a particular category of question” (see also Khosa v.
- Evidence: `governing_rule` cue `standard of review` at chunk `5039543` offsets `144-162`; context: 1, the Supreme Court of Canada held at paragraph 62 that the first step in conducting a standard of review analysis is to “ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of (deference) to be accorded with regard to a particular category of question” (see also Khosa v.
- Evidence: `issue` cue `issue` at chunk `5039544` offsets `15-20`; context: [24] The first issue touches upon issues of fact, and mixed law and fact.
- Evidence: `governing_rule` cue `under` at chunk `5039544` offsets `241-246`; context: 11 that interpreting the exclusion of generalized risks of violence under subsection 97(1)(b) of IRPA was an issue of application of law to the particular facts of a case and therefore reviewable on a standard of reasonableness following the Federal Court of Appeal decision in Prophète v.
- Evidence: `reasoning_application` cue `therefore` at chunk `5039544` offsets `348-357`; context: 11 that interpreting the exclusion of generalized risks of violence under subsection 97(1)(b) of IRPA was an issue of application of law to the particular facts of a case and therefore reviewable on a standard of reasonableness following the Federal Court of Appeal decision in Prophète v.

#### 22164:2:subtheme:3 · paragraphs 25-26

- Raw key terms: `issue, para, reasonableness, standard, acceptable, adequacy, analysis, board`
- Display key terms: `para, reasonableness, standard, acceptable, adequacy, analysis`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: para, reasonableness, standard, acceptable, adequacy, analysis Rule/authority context: Post-Dunsmuir jurisprudence has held that adequacy of state protection decisions are reviewable under a standard of reasonableness (Eler v. Application context: The second issue is therefore reviewable on a standard of reasonableness. Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5039545` offsets `16-21`; context: [25] The second issue relates to a determination of the adequacy of state protection.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5039545` offsets `142-155`; context: Post-Dunsmuir jurisprudence has held that adequacy of state protection decisions are reviewable under a standard of reasonableness (Eler v.
- Evidence: `reasoning_application` cue `therefore` at chunk `5039545` offsets `571-580`; context: The second issue is therefore reviewable on a standard of reasonableness.
- Evidence: `issue` cue `whether` at chunk `5039546` offsets `200-207`; context: [26] In reviewing the Board’s decision on a reasonableness standard, the Court will consider "the existence of justification, transparency and intelligibility within the decision-making process” and “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, supra, at para.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039546` offsets `680-688`; context: 1: Did the Board err in law in that it misconstrued the evidence before it and/or misinterpreted s.

#### 22164:2:subtheme:4 · paragraphs 27-35

- Raw key terms: `risk, applicants, business, generalized, board, owners, faced, justice`
- Display key terms: `risk, business, generalized, owners, faced, justice`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: risk, business, generalized, owners, faced, justice Position/evidence statements: [28] The applicants submit that the Board erred in finding that the risk faced by the applicants from the maras was a generalized risk in Guatemala. | [29] The applicants argue that subsection 97(1)(b)(ii) of IRPA requires that the risk be “personalized”, but not necessarily “individualized”. Rule/authority context: Vickram is consistent with the general principle that wealth, or perceived wealth, on its own, is not sufficient to ground a claim under subsection 97(1)(b) on the basis that criminals tend to target all those who they p | The fact that they share the same risk as other persons similarly situated does not make their risk a “personalized risk” subject to protection under section 97. Application context: Since small business owners are one of the groups primarily targeted by maras, the applicants are at more risk than the general population, and therefore the risk to them is personalized. | In my view the fact that the applicants are more at risk because they are small business owners does not transform a generalized risk of criminal violence to a personalized risk. Evidence spans paragraphs 27-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5039547` offsets `10-15`; context: [27] This issue I would restate as “Did the Board unreasonably find that the applicants faced a “generalized risk” of injury not “personalized” to only small business owners in Guatemala?
- Evidence: `party_position` cue `submit` at chunk `5039548` offsets `20-26`; context: [28] The applicants submit that the Board erred in finding that the risk faced by the applicants from the maras was a generalized risk in Guatemala.
- Evidence: `party_position` cue `argue` at chunk `5039549` offsets `20-25`; context: [29] The applicants argue that subsection 97(1)(b)(ii) of IRPA requires that the risk be “personalized”, but not necessarily “individualized”.
- Evidence: `reasoning_application` cue `therefore` at chunk `5039549` offsets `287-296`; context: Since small business owners are one of the groups primarily targeted by maras, the applicants are at more risk than the general population, and therefore the risk to them is personalized.
- Evidence: `counterargument_limitation` cue `but` at chunk `5039549` offsets `105-108`; context: [29] The applicants argue that subsection 97(1)(b)(ii) of IRPA requires that the risk be “personalized”, but not necessarily “individualized”.
- Evidence: `party_position` cue `argue` at chunk `5039550` offsets `270-275`; context: In this case, the applicants argue that the Board expressly determined that the applicants were at greater risk by virtue of being business owners.
- Evidence: `evidence_fact` cue `determined that` at chunk `5039550` offsets `301-316`; context: In this case, the applicants argue that the Board expressly determined that the applicants were at greater risk by virtue of being business owners.
- Evidence: `governing_rule` cue `under` at chunk `5039551` offsets `426-431`; context: Vickram is consistent with the general principle that wealth, or perceived wealth, on its own, is not sufficient to ground a claim under subsection 97(1)(b) on the basis that criminals tend to target all those who they perceive as relatively wealthy (see also my decision in Hardat Ramotar et al.
- Evidence: `reasoning_application` cue `because` at chunk `5039551` offsets `108-115`; context: In my view the fact that the applicants are more at risk because they are small business owners does not transform a generalized risk of criminal violence to a personalized risk.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039552` offsets `355-363`; context: 16 of her reasons that being a member of a particular economic sector does not transform generalized risk of criminal violence against the applicant to personal risk:
¶16 The applicant referred to a passage of the documentary evidence which confirms that bus fare collectors are frequently subject to extortion by the Gang.
- Evidence: `counterargument_limitation` cue `However` at chunk `5039552` offsets `453-460`; context: However, the Board examined this country documentation and found it to clearly indicate the prevalence of gang related violence in a variety of sectors.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039554` offsets `207-215`; context: There is no evidence that the maras personally targeted the applicants or that they face a greater risk then other small business owners or persons perceived to be relatively wealthy (Pineda v.
- Evidence: `reasoning_application` cue `because` at chunk `5039554` offsets `47-54`; context: [34] In this case the applicants were targeted because they owned a small business.
- Evidence: `governing_rule` cue `under` at chunk `5039555` offsets `695-700`; context: The fact that they share the same risk as other persons similarly situated does not make their risk a “personalized risk” subject to protection under section 97.
- Evidence: `reasoning_application` cue `because` at chunk `5039555` offsets `261-268`; context: [35] I am of the view that if the risk to violence or injury or crime is a generalized risk faced by all citizens of the country who are seen as relatively wealthy by the criminals, the fact that a specific number of individuals may be targeted more frequently because of their wealth, does not mean that they are not subject to a “generalized risk” of violence.

#### 22164:2:subtheme:5 · paragraphs 36-40

- Raw key terms: `protection, state, evidence, board, apparatus, applicants, citizens, court`
- Display key terms: `protection, state, apparatus, citizens`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: protection, state, apparatus, citizens Position/evidence statements: [37] The applicants submit in the alternative that the Board’s determination on the issue of state protection was unreasonable in that it contradicted other factual findings made by the Board and the objective evidence o | The applicant contends that Guatemala is simply unable to protect its population from the maras, and that placing too heavy a burden on the applicants to rebut the presumption of state protection is inappropriate. Evidence spans paragraphs 36-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `5039556` offsets `106-111`; context: Issue No.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039556` offsets `96-104`; context: [36] In my view the decision of the Board in this regard was reasonably open to it based on the evidence.
- Evidence: `issue` cue `issue` at chunk `5039557` offsets `84-89`; context: [37] The applicants submit in the alternative that the Board’s determination on the issue of state protection was unreasonable in that it contradicted other factual findings made by the Board and the objective evidence on the record.
- Evidence: `party_position` cue `submit` at chunk `5039557` offsets `20-26`; context: [37] The applicants submit in the alternative that the Board’s determination on the issue of state protection was unreasonable in that it contradicted other factual findings made by the Board and the objective evidence on the record.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039557` offsets `210-218`; context: [37] The applicants submit in the alternative that the Board’s determination on the issue of state protection was unreasonable in that it contradicted other factual findings made by the Board and the objective evidence on the record.
- Evidence: `party_position` cue `contends` at chunk `5039558` offsets `326-334`; context: The applicant contends that Guatemala is simply unable to protect its population from the maras, and that placing too heavy a burden on the applicants to rebut the presumption of state protection is inappropriate.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039558` offsets `47-55`; context: [38] The applicant states that the documentary evidence is inconsistent with the Board’s finding that “Guatemala has a functioning political and judicial system” and “an official apparatus that provides a measure of protection to its citizens including a criminal justice system and a functioning police force”.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039560` offsets `346-354`; context: While the presumption of state protection may be rebutted, this can only occur where the refugee claimant provides "clear and convincing" evidence confirming the state's inability to provide protection.

#### 22164:2:subtheme:6 · paragraphs 41-45

- Raw key terms: `protection, canada, justice, para, state, court, democratic, inadequate`
- Display key terms: `protection, justice, para, state, democratic, inadequate`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: protection, justice, para, state, democratic, inadequate Evidence spans paragraphs 41-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5039561` offsets `264-272`; context: [41] In Kadenko, supra, the Federal Court of Appeal held that in order to rebut the presumption of state protection, refugee claimants must make "reasonable efforts" at seeking out state protection, and that the burden on the claimant increases where the state in question is democratic (see also L.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039562` offsets `314-322`; context: 16-30 on the distinctions between “burden of proof, standard of proof and quality of evidence".
- Evidence: `counterargument_limitation` cue `But` at chunk `5039562` offsets `927-930`; context: But this in no way alters the standard of proof.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039563` offsets `70-78`; context: [43] Consequently, the applicants had to adduce relevant and reliable evidence with sufficient probative value that satisfies the trier of fact on a balance of probabilities that the state protection is inadequate (Carillo, supra, at para.
- Evidence: `evidence_fact` cue `found that` at chunk `5039565` offsets `157-167`; context: It found that while the protection offered by Guatemala was not perfect, it was nevertheless adequate.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `5039565` offsets `234-246`; context: It found that while the protection offered by Guatemala was not perfect, it was nevertheless adequate.

#### Section text

[21] The applicants raise two issues:
1. Did the Board err in law in that it misconstrued the evidence before it and/or misinterpreted s. 97(1) (b) of IRPA?
2. Was the Board’s determination of the issue of state protection unreasonable?
STANDARD OF REVIEW

[22] As a result of the Supreme Court of Canada’s decision in Dunsmuir v. New Brunswick, 2008 SCC 9, [2008] S.C.J. No. 9 (QL), it is clear that reviewing courts must confine their analysis to two standards of review, those of reasonableness and correctness. Accordingly, the deference to be accorded to the Board’s factual findings mandates that the issues in question be reviewed on a standard of reasonableness.

[23] In Dunsmuir v. New Brunswick, 2008 SCC 9, 372 N.R. 1, the Supreme Court of Canada held at paragraph 62 that the first step in conducting a standard of review analysis is to “ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of (deference) to be accorded with regard to a particular category of question” (see also Khosa v. Canada (MCI), 2009 SCC 12, per Justice Binnie at para. 53).

[24] The first issue touches upon issues of fact, and mixed law and fact. In Acosta v. Canada (MCI), 2009 FC 213, [2009] F.C.J. No. 270 (QL), Justice Gauthier held at para. 11 that interpreting the exclusion of generalized risks of violence under subsection 97(1)(b) of IRPA was an issue of application of law to the particular facts of a case and therefore reviewable on a standard of reasonableness following the Federal Court of Appeal decision in Prophète v. Canada (MCI), 2009 FCA 31, para. 7. The first issue is therefore reviewable on a standard of reasonableness.

[25] The second issue relates to a determination of the adequacy of state protection. This is a question of mixed law and fact. Post-Dunsmuir jurisprudence has held that adequacy of state protection decisions are reviewable under a standard of reasonableness (Eler v. Canada (Minister of Citizenship and Immigration), 2008 FC 334, per Justice Dawson at para. 6; Pacasum v. Canada (Minister of Citizenship and Immigration), 2008 FC 822, per Justice de Montigny at para. 18; Velasquez v. Canada (MCI), 2009 FC 109, per Justice de Montigny at para. 13). The second issue is therefore reviewable on a standard of reasonableness.

[26] In reviewing the Board’s decision on a reasonableness standard, the Court will consider "the existence of justification, transparency and intelligibility within the decision-making process” and “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, supra, at para. 47, Khosa, supra, at para. 59). The Court will only intervene if the decision falls outside the "range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, supra, at para. 47, Khosa, supra, at para. 59).
ANALYSIS
Issue No. 1: Did the Board err in law in that it misconstrued the evidence before it and/or misinterpreted s. 97(1) (b) of IRPA?

[27] This issue I would restate as “Did the Board unreasonably find that the applicants faced a “generalized risk” of injury not “personalized” to only small business owners in Guatemala?”

[28] The applicants submit that the Board erred in finding that the risk faced by the applicants from the maras was a generalized risk in Guatemala.

[29] The applicants argue that subsection 97(1)(b)(ii) of IRPA requires that the risk be “personalized”, but not necessarily “individualized”. Since small business owners are one of the groups primarily targeted by maras, the applicants are at more risk than the general population, and therefore the risk to them is personalized.

[30] The applicants seek to distinguish Vickram v. Canada (MCI), 2007 FC 457, per Justice de Montigny, on the basis that the Board in that case made the express determination that the applicant faced a generalized risk of criminal activity. In this case, the applicants argue that the Board expressly determined that the applicants were at greater risk by virtue of being business owners.

[31] There is no basis for distinguishing Vickram. In my view the fact that the applicants are more at risk because they are small business owners does not transform a generalized risk of criminal violence to a personalized risk. There is no inconsistency in the Board’s reasons in that regard. Vickram is consistent with the general principle that wealth, or perceived wealth, on its own, is not sufficient to ground a claim under subsection 97(1)(b) on the basis that criminals tend to target all those who they perceive as relatively wealthy (see also my decision in Hardat Ramotar et al. v. Canada (MCI), 2009 FC 362, at para. 31 and Louis-Jacques Michaud v. Canada (MCI), 2009 FC 886, at para. 38 to 41).

[32] Justice Gauthier recently dealt with the same argument in Acosta, supra, in the context of bus operators, and held at para. 16 of her reasons that being a member of a particular economic sector does not transform generalized risk of criminal violence against the applicant to personal risk:
¶16 The applicant referred to a passage of the documentary evidence which confirms that bus fare collectors are frequently subject to extortion by the Gang. However, the Board examined this country documentation and found it to clearly indicate the prevalence of gang related violence in a variety of sectors. It is no more unreasonable to find that a particular group that is targeted, be it bus fare collectors or other victims of extortion and who do not pay, faces generalized violence than to reach the same conclusion in respect of well known wealthy business men in Haiti who were clearly found to be at a heightened risk of facing the violence prevalent in that country [emphasis added].

[33] I agree with Justice Gauthier’s view in Acosta.

[34] In this case the applicants were targeted because they owned a small business. The telephone harassment and threats after they shut down their business were a continuation of the extortion. There is no evidence that the maras personally targeted the applicants or that they face a greater risk then other small business owners or persons perceived to be relatively wealthy (Pineda v. Canada (MCI), 2007 FC 365, per Justice de Montigny).

[35] I am of the view that if the risk to violence or injury or crime is a generalized risk faced by all citizens of the country who are seen as relatively wealthy by the criminals, the fact that a specific number of individuals may be targeted more frequently because of their wealth, does not mean that they are not subject to a “generalized risk” of violence. The fact that the persons at risk are those perceived to be relatively wealthy, and can be seen as a subset of the general population, means that they are exposed to a “generalized risk”. The fact that they share the same risk as other persons similarly situated does not make their risk a “personalized risk” subject to protection under section 97. A finding otherwise would “open the floodgates” in that all Guatemalans who are relatively wealthy, or perceived as being relatively wealthy, could seek protection under section 97 of IRPA.

[36] In my view the decision of the Board in this regard was reasonably open to it based on the evidence.
Issue No. 2: Was the Board’s determination of the issue of state protection unreasonable?

[37] The applicants submit in the alternative that the Board’s determination on the issue of state protection was unreasonable in that it contradicted other factual findings made by the Board and the objective evidence on the record.

[38] The applicant states that the documentary evidence is inconsistent with the Board’s finding that “Guatemala has a functioning political and judicial system” and “an official apparatus that provides a measure of protection to its citizens including a criminal justice system and a functioning police force”. The applicant contends that Guatemala is simply unable to protect its population from the maras, and that placing too heavy a burden on the applicants to rebut the presumption of state protection is inappropriate.

[39] In Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689, the Supreme Court of Canada held that refugee protection is a form of "surrogate protection" intended only in cases where protections from the home state are unavailable.

[40] Further, the Court held that except in situations where there has been a complete breakdown of the state apparatus, there exists a general presumption that a state is capable of protecting its citizens. While the presumption of state protection may be rebutted, this can only occur where the refugee claimant provides "clear and convincing" evidence confirming the state's inability to provide protection. Such evidence can include testimony of similarly situated individuals let down by the state protection arrangement, or the refugee claimant's own testimony of past incidents in which state protection was not provided (see Ward, supra, at 724-725).

[41] In Kadenko, supra, the Federal Court of Appeal held that in order to rebut the presumption of state protection, refugee claimants must make "reasonable efforts" at seeking out state protection, and that the burden on the claimant increases where the state in question is democratic (see also L.G.S. v. Canada (MCI). 2004 FC 731, per Justice Mactavish where she held at para. 22 that a claimant need not show that they exhausted absolutely all avenues of protection).

[42] The Federal Court of Appeal recently clarified the presumption of state protection in Carillo v. Canada (MCI), 2008 FCA 94, 69 Imm. L.R. (3d) 309, per Justice Létourneau. The Court engaged in a detailed discussion at paras. 16-30 on the distinctions between “burden of proof, standard of proof and quality of evidence". The Court held that the “heavy burden” to rebut the presumption of adequate state protection in democratic societies, as referred to in Hinzman v. Canada (MCI), 2007 FCA 171, per Justice Sexton, at paragraph 57, was simply an acknowledgement of the difficulty of furnishing sufficient evidence in such circumstances:
¶26 I think our colleague, as was La Forest J. in the Ward case, referred to the quality of the evidence that needs to be adduced to convince the trier of fact of the inadequate state protection. In other words, it is more difficult in some cases than others to rebut the presumption. But this in no way alters the standard of proof. In this respect, I fully agree with the finding of the judge that La Forest J. in Ward was referring to the quality of the evidence necessary to rebut the presumption and not to a higher standard of proof.

[43] Consequently, the applicants had to adduce relevant and reliable evidence with sufficient probative value that satisfies the trier of fact on a balance of probabilities that the state protection is inadequate (Carillo, supra, at para. 30).

[44] In the case at bar the only steps taken by the applicants to seek state protection was contacting the Gualan local police who in turn contacted the Guatemala City police. It is trite law that the refusal of local police to offer protection does not constitute inadequate state protection, unless the refusal of the local police can be linked to a larger pattern of inability to offer protection in the particular circumstances (Zhuravlvev v. Canada (MCI), [2000] 4 F.C. 3, per Justice Pelletier at para. 31).

[45] The Board found the steps taken by the applicant to be insufficient in light of Guatemala’s progress against gang violence and democratic character. It found that while the protection offered by Guatemala was not perfect, it was nevertheless adequate. (The Board cited as authorities this Court’s decisions in Zalazali v. Canada (MEI), [1991] 3 F.C. 605 (F.C.A.), per Justice Décary at para. 21; and Canada (MEI) v. Villafranca (2009), 18 Imm. L.R. (2d) 130 (F.C.A.), per Justice Hugessen.)

## 22164:3 · paragraphs 46-51

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a7be290504bb287ece0a985642eb1cc45bfbaf455c5e5e3fd5322ff219c3f085`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22164:3:subtheme:1 · paragraphs 46-49

- Raw key terms: `board, evidence, police, analysis, applicants, corruption, documentary, either`
- Display key terms: `police, analysis, corruption, documentary, either`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: police, analysis, corruption, documentary, either Application context: This is highlighted by the more recent documentary evidence produced by the applicant which describes the inability of the Guatemalan authorities to tackle gang violence because of systemic corruption and lack of resourc | Accordingly, it was reasonably open to the Board to find either that there is, or there is not, adequate state protection in Guatemala. Evidence spans paragraphs 46-49. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039566` offsets `133-141`; context: I am troubled by the staleness of some of the documentary evidence that the Board cites.
- Evidence: `reasoning_application` cue `because` at chunk `5039566` offsets `334-341`; context: This is highlighted by the more recent documentary evidence produced by the applicant which describes the inability of the Guatemalan authorities to tackle gang violence because of systemic corruption and lack of resources.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039567` offsets `265-273`; context: The viva voce evidence by the applicants indicates that the efficacy of Guatemalan police is at worst mixed:
PRESIDING MEMBER: Are you saying that the police in Guatemala are successful in catching the maras?
- Evidence: `evidence_fact` cue `evidence` at chunk `5039568` offsets `21-29`; context: [48] The documentary evidence is that state protection in Guatemala is lacking.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5039568` offsets `991-1002`; context: Accordingly, it was reasonably open to the Board to find either that there is, or there is not, adequate state protection in Guatemala.
- Evidence: `evidence_fact` cue `evidence` at chunk `5039569` offsets `9-17`; context: [49] The evidence on the record allows for a determination either way.

#### 22164:3:subtheme:2 · paragraphs 50-51

- Raw key terms: `certified, question, advised, agrees, appeal, application, case, court`
- Display key terms: `certified, question, advised, agrees, case`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: certified, question, advised, agrees, case Operative outcome context: [50] For these reasons the application for judicial review is dismissed. Evidence spans paragraphs 50-51. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `QUESTION` at chunk `5039570` offsets `83-91`; context: CERTIFIED QUESTION
- Evidence: `disposition` cue `dismissed` at chunk `5039570` offsets `62-71`; context: [50] For these reasons the application for judicial review is dismissed.
- Evidence: `issue` cue `question` at chunk `5039571` offsets `76-84`; context: [51] Both parties advised the Court that this case does not raise a serious question of general importance which ought to be certified for an appeal.

#### Section text

[46] The Board’s analysis in regard to state protection is rather general. I am troubled by the staleness of some of the documentary evidence that the Board cites. This is highlighted by the more recent documentary evidence produced by the applicant which describes the inability of the Guatemalan authorities to tackle gang violence because of systemic corruption and lack of resources. The applicants also adduced evidence that shows public frustration with police protection.

[47] While the Board’s reasons leave much to be desired in terms of analysis, its ultimate conclusion cannot be held to be unreasonable. The Board pointed to several avenues of redress which the applicants could have pursued besides the local police. The viva voce evidence by the applicants indicates that the efficacy of Guatemalan police is at worst mixed:
PRESIDING MEMBER: Are you saying that the police in Guatemala are successful in catching the maras?
CLAIMANT: They are on the news you can see it every day and you can see that they catch the occasional one but as well as seeing them catch several of them you also see murders happening all over the place by these people.

[48] The documentary evidence is that state protection in Guatemala is lacking. The Board’s National Documentation Package for Guatemala provided a Response to Information Request dated March 2, 2007 with respect to “Measures for protecting the population from criminal gangs”. The document stated:
Corruption within the police force and a lack of resources complicate the battle against criminal gangs. President Berger himself has acknowledged the failure of Guatemala’s 22,000 national police officers to control the criminal gangs, which reportedly have as many as 60,000 members.
While this evidence suggests that state protection in Guatemala is inadequate, other evidence on the record that the police are taking measures to protect the population from criminal gangs including the deployment of the soldiers on the streets to re-establish security from criminal gangs, the arrest of gang members, surveillance measures, and the creation of a special hotline for reporting extortion. Accordingly, it was reasonably open to the Board to find either that there is, or there is not, adequate state protection in Guatemala.

[49] The evidence on the record allows for a determination either way. In my view, the decision of the Board lies in the range of acceptable outcomes.

[50] For these reasons the application for judicial review is dismissed.
CERTIFIED QUESTION

[51] Both parties advised the Court that this case does not raise a serious question of general importance which ought to be certified for an appeal. The Court agrees.


## 22164:4 · paragraphs 52-53

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e74198801b8a10a711a89f236324506e3a4b1d09e88afd6d61c613283626c2f6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22164:4:subtheme:1 · paragraphs 52-53

- Raw key terms: `judgment, kelen, adjudges, appearances, applicants, application, attorney, barrister`
- Display key terms: `kelen, adjudges, barrister`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: kelen, adjudges, barrister Operative outcome context: JUDGMENT THIS COURT ORDERS AND ADJUDGES that: The application for judicial review is dismissed. Evidence spans paragraphs 52-53. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `5039571` offsets `253-262`; context: JUDGMENT
THIS COURT ORDERS AND ADJUDGES that:
The application for judicial review is dismissed.

#### Section text

JUDGMENT
THIS COURT ORDERS AND ADJUDGES that:
The application for judicial review is dismissed.
“Michael A. Kelen”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-646-09
STYLE OF CAUSE: HENRY SOTERO RODRIGUEZ PEREZ, MARVIN ROLANDO RODRIGUEZ PEREZ v. THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: September 29, 2009
REASONS FOR JUDGMENT
AND JUDGMENT: KELEN J.
DATED: October 14, 2009
APPEARANCES:
D. Clifford Luyt
FOR THE APPLICANTS
Manuel Mendelzon
FOR THE RESPONDENT
SOLICITORS OF RECORD:
D. Clifford Luyt
Barrister and Solicitor
FOR THE APPLICANTS
John H. Sims, Q.C.
Deputy Attorney General of Canada
FOR THE RESPONDENT
