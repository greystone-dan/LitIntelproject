# Discussion Units: case 23126

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **64**
- Continuity pairs: **63**
- Discussion Units: **5**
- Paragraph source hashes: **64**
- Sub-themes: **14**

## 23126:1 · paragraphs 0-2

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `19a6f4495e8b1a112cb9d86cabd44e5382b46f9c066aab5d398697b964b1df87`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23126:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, application, balasubramaniam, decision, immigration, parthipan, reasons, april`
- Display key terms: `balasubramaniam, parthipan, april`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: balasubramaniam, parthipan, april Rule/authority context: [1] This is an application by Parthipan Balasubramaniam (the Applicant), pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of the decision of the Immigr Operative outcome context: [2] For the reasons that follow this application is dismissed. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5084248` offsets `73-84`; context: [1] This is an application by Parthipan Balasubramaniam (the Applicant), pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of the decision of the Immigration and Refugee Board (the Board) rendered on April 5, 2012, wherein the Board concluded that the Applicant does not have a well-founded fear of persecution and is not a person in need of protection as contemplated by sections 96 and 97 of the IRPA.
- Evidence: `disposition` cue `dismissed` at chunk `5084249` offsets `52-61`; context: [2] For the reasons that follow this application is dismissed.

#### Section text

Balasubramaniam v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2013-06-21
Neutral citation
2013 FC 698
File numbers
IMM-4243-12
Decision Content
Date: 20130621
Docket: IMM-4243-12
Citation: 2013 FC 698
Ottawa, Ontario, June 21, 2013
PRESENT: The Honourable Mr. Justice Scott
BETWEEN:
PARTHIPAN BALASUBRAMANIAM
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT
I. Introduction

[1] This is an application by Parthipan Balasubramaniam (the Applicant), pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of the decision of the Immigration and Refugee Board (the Board) rendered on April 5, 2012, wherein the Board concluded that the Applicant does not have a well-founded fear of persecution and is not a person in need of protection as contemplated by sections 96 and 97 of the IRPA.

[2] For the reasons that follow this application is dismissed.


## 23126:2 · paragraphs 3-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e7fc431416271de4627ea8e347ad2a806a4f33cd4768574261bad04c988fedf4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23126:2:subtheme:1 · paragraphs 3-8

- Raw key terms: `applicant, home, ltte, army, brothers, brought, camp, claims`
- Display key terms: `home, ltte, army, brothers, brought, camp, claims`
- Argument roles: `disposition, party_position, reasoning_application`
- Explanation: Observed roles: disposition, party_position, reasoning_application Display terms: home, ltte, army, brothers, brought, camp, claims Position/evidence statements: He claims that his abductors suspected he had ties with the Liberation Tigers of Tamil Eelam [LTTE] because he had an uncle who had been forced to join the LTTE. | [6] The Applicant also claims the Sri Lankan Army picked him up at his home in April 2009 and brought him to the Pampaimadu army camp. Application context: He claims that his abductors suspected he had ties with the Liberation Tigers of Tamil Eelam [LTTE] because he had an uncle who had been forced to join the LTTE. Operative outcome context: When he denied the allegations, he was tortured. Evidence spans paragraphs 3-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `5084251` offsets `350-356`; context: He claims that his abductors suspected he had ties with the Liberation Tigers of Tamil Eelam [LTTE] because he had an uncle who had been forced to join the LTTE.
- Evidence: `reasoning_application` cue `because` at chunk `5084251` offsets `447-454`; context: He claims that his abductors suspected he had ties with the Liberation Tigers of Tamil Eelam [LTTE] because he had an uncle who had been forced to join the LTTE.
- Evidence: `party_position` cue `claims` at chunk `5084253` offsets `23-29`; context: [6] The Applicant also claims the Sri Lankan Army picked him up at his home in April 2009 and brought him to the Pampaimadu army camp.
- Evidence: `disposition` cue `denied` at chunk `5084253` offsets `209-215`; context: When he denied the allegations, he was tortured.

#### 23126:2:subtheme:2 · paragraphs 9-13

- Raw key terms: `applicant, family, canada, detained, allegedly, alleges, claims, group`
- Display key terms: `family, detained, allegedly, alleges, claims, group`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: family, detained, allegedly, alleges, claims, group Position/evidence statements: [9] In early December 2010, the Applicant claims his family home was once again invaded, this time by the Karuna group, who accused the Applicant of providing food and shelter to the LTTE with the help of his relatives l | The Applicant claims the agent took all his travel documents from him in Guatemala. Rule/authority context: They allegedly told him that under the Emergency Laws, he could be detained for 10 years if they suspected he was connected to the LTTE. Evidence spans paragraphs 9-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5084255` offsets `104-112`; context: [8] In March 2010, the Criminal Investigation Department [CID] purportedly came to his home in order to question the Applicant and his family on why the Army was interested in him.
- Evidence: `governing_rule` cue `under` at chunk `5084255` offsets `210-215`; context: They allegedly told him that under the Emergency Laws, he could be detained for 10 years if they suspected he was connected to the LTTE.
- Evidence: `party_position` cue `claims` at chunk `5084256` offsets `42-48`; context: [9] In early December 2010, the Applicant claims his family home was once again invaded, this time by the Karuna group, who accused the Applicant of providing food and shelter to the LTTE with the help of his relatives living abroad.
- Evidence: `evidence_fact` cue `evidence` at chunk `5084256` offsets `327-335`; context: They told the Applicant that he was being watched and would be killed if they discovered any evidence that he was assisting the LTTE.
- Evidence: `party_position` cue `claims` at chunk `5084257` offsets `363-369`; context: The Applicant claims the agent took all his travel documents from him in Guatemala.
- Evidence: `party_position` cue `claim` at chunk `5084258` offsets `147-152`; context: He did not claim asylum in any of the countries he traveled through.
- Evidence: `party_position` cue `contends` at chunk `5084259` offsets `19-27`; context: [12] The Applicant contends that members of the Karuna group visited his family after his departure for Canada.

#### 23126:2:subtheme:3 · paragraphs 14-14

- Raw key terms: `adduced, applicant, basis, board, contemplated, convention, credibility, determinative`
- Display key terms: `adduced, basis, contemplated, convention, credibility, determinative`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: adduced, basis, contemplated, convention, credibility, determinative Evidence spans paragraphs 14-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5084260` offsets `181-187`; context: The determinative issues were the credibility of the evidence adduced and the objective basis of the Applicant’s prospective fear.
- Evidence: `evidence_fact` cue `determined that` at chunk `5084260` offsets `15-30`; context: [13] The Board determined that the Applicant is neither a Convention refugee nor a person in need of protection as contemplated by sections 96 and 97 of the IRPA.

#### Section text

II. Facts

[3] The Applicant is a 28 year old Sri Lankan citizen of Tamil ethnicity. He grew up in the Vavuniya district of Northern Sri Lanka. His parents, who are farmers, continue to live in the family home in Poonthoddam, Vavuniya, with his two brothers and his sister.

[4] In July 2008, the Applicant was abducted by people he alleges were members of the Eelam People’s Democratic Party [EPDP]. They came to his family home in a white van and brought him to an unknown location where they questioned, beat and tortured him for five or six days. The Applicant was injured to his eyesight as a result of the incident. He claims that his abductors suspected he had ties with the Liberation Tigers of Tamil Eelam [LTTE] because he had an uncle who had been forced to join the LTTE. The Applicant explained that he had never met this uncle and that he was killed in 2007.

[5] The Applicant’s two younger brothers were also said to have been taken and beaten by the EPDP in 2008. They have not experienced any problems since then.

[6] The Applicant also claims the Sri Lankan Army picked him up at his home in April 2009 and brought him to the Pampaimadu army camp. There they accused him of supporting and recruiting for the LTTE. When he denied the allegations, he was tortured. He was released after five days.

[7] The army allegedly visited the Applicant at his home on a number of other occasions after his detention. Twice he was taken back to the army camp to be interrogated. They told him that they still believed he was an LTTE supporter and that they could make him disappear.

[8] In March 2010, the Criminal Investigation Department [CID] purportedly came to his home in order to question the Applicant and his family on why the Army was interested in him. They allegedly told him that under the Emergency Laws, he could be detained for 10 years if they suspected he was connected to the LTTE. The family had no choice but to pay 100,000 Sri Lankan rupees to prevent his detention.

[9] In early December 2010, the Applicant claims his family home was once again invaded, this time by the Karuna group, who accused the Applicant of providing food and shelter to the LTTE with the help of his relatives living abroad. They told the Applicant that he was being watched and would be killed if they discovered any evidence that he was assisting the LTTE.

[10] After this last incident, the Applicant and his family decided that he was no longer safe in Sri Lanka. They sold a portion of their land to finance the C$30,000.00 cost of fleeing to Canada. With the assistance of an agent, the Applicant alleges he left Sri Lanka on January 25, 2011 and travelled with his own passport after bribing customs. The Applicant claims the agent took all his travel documents from him in Guatemala.

[11] The Applicant was detained in Mexico for four months and in the U.S.A. for two months before arriving in Canada in September 2011. He did not claim asylum in any of the countries he traveled through.

[12] The Applicant contends that members of the Karuna group visited his family after his departure for Canada. Upon discovering that the Applicant had fled the country, they beat his father in front of his mother and then detained him at their camp. His mother had to arrange for someone to pay 50,000 rupees in exchange for his release. Members of the Karuna group allegedly continue to harass the Applicant’s family and neighbours over his whereabouts. The Applicant alleges to be at greater risk of harm upon return now that he has fled and claimed refugee status in Canada.
III. Impugned decision

[13] The Board determined that the Applicant is neither a Convention refugee nor a person in need of protection as contemplated by sections 96 and 97 of the IRPA. The determinative issues were the credibility of the evidence adduced and the objective basis of the Applicant’s prospective fear.
A. Negative credibility findings

## 23126:3 · paragraphs 15-60

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4eab6d8f8c096947b5137ca14c975a43ca2eb2587c595f47e6c2938f153392d6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23126:3:subtheme:1 · paragraphs 15-16

- Raw key terms: `alleged, applicant, army, board, evidence, failed, having, karuna`
- Display key terms: `alleged, army, failed, having, karuna`
- Argument roles: `counterargument_limitation, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, party_position, reasoning_application Display terms: alleged, army, failed, having, karuna Position/evidence statements: (i) The Board was not provided with a passport or documents related to arrangements for his travel to Canada or proof of the land transaction his father made to finance his trip; (j) The Applicant failed to provide objec Application context: The Board found that the JP could have written about the other incidents without implicating the army; (e) The Applicant said his family went to the JP for all their needs but was unable to provide any examples of other  Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claim` at chunk `5084261` offsets `3176-3181`; context: (i) The Board was not provided with a passport or documents related to arrangements for his travel to Canada or proof of the land transaction his father made to finance his trip;
(j) The Applicant failed to provide objective evidence that he lived in Sri Lanka until January 2011; and
(k) The Applicant was detained for four months in Mexico and two months in the United States and failed to claim asylum in those countries.
- Evidence: `evidence_fact` cue `found that` at chunk `5084261` offsets `98-108`; context: [14] The Board based its negative credibility findings on a number of observations:
(a) The Board found that information provided by the Justice of the Peace’s [JP] letter regarding the July 6, 2008 abduction and the motive and timing of the Applicant’s departure were inconsistent with the narrative in his Personal Information Form [PIF]:
(i) The JP’s letter stated that the incident happened on July 6, 2008 and was committed by “unknown persons”, while the PIF did not provide a specific date and specified the EPDP as the perpetrators;
(ii) Although the Applicant stated that the JP knew his family personally, including all of the Applicant’s experiences, the letter did not provide any details about the incidents involving the army, the CID or members of the Karuna group;
(iii) The JP’s letter did not mention that two and a half years lapsed between the July 6, 2008 abduction and the Applicant’s decision to flee abroad, but could imply that the Applicant made his decision to go abroad soon after the July 6, 2008 incident; and
(iv) Contrary to the Applicant’s PIF, the JP’s letter specifies that the Applicant fled after having more problems with the same group of unknown persons that abducted him on July 6, 2008.
- Evidence: `reasoning_application` cue `because` at chunk `5084261` offsets `1973-1980`; context: The Board found that the JP could have written about the other incidents without implicating the army;
(e) The Applicant said his family went to the JP for all their needs but was unable to provide any examples of other situations when they had sought his assistance;
(f) While the Applicant indicated that his family may have been suspected of having ties with the LTTE because his uncle had been forced to join them, he failed to adequately explain why he was the only member of his family being forced to flee;
(g) The Board found that the if he had been arrested on suspicion of helping the LTTE he would not have been released from detention unless the army was satisfied he had no LTTE ties;
(h) The Applicant was unable to provide any corroborative objective evidence regarding his alleged detentions and torture by the army, the CID or the Karuna group purported to have occurred after the July 2008 incident.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5084261` offsets `546-554`; context: [14] The Board based its negative credibility findings on a number of observations:
(a) The Board found that information provided by the Justice of the Peace’s [JP] letter regarding the July 6, 2008 abduction and the motive and timing of the Applicant’s departure were inconsistent with the narrative in his Personal Information Form [PIF]:
(i) The JP’s letter stated that the incident happened on July 6, 2008 and was committed by “unknown persons”, while the PIF did not provide a specific date and specified the EPDP as the perpetrators;
(ii) Although the Applicant stated that the JP knew his family personally, including all of the Applicant’s experiences, the letter did not provide any details about the incidents involving the army, the CID or members of the Karuna group;
(iii) The JP’s letter did not mention that two and a half years lapsed between the July 6, 2008 abduction and the Applicant’s decision to flee abroad, but could imply that the Applicant made his decision to go abroad soon after the July 6, 2008 incident; and
(iv) Contrary to the Applicant’s PIF, the JP’s letter specifies that the Applicant fled after having more problems with the same group of unknown persons that abducted him on July 6, 2008.
- Evidence: `evidence_fact` cue `evidence` at chunk `5084262` offsets `100-108`; context: [15] The Board concluded that the Applicant “failed to provide sufficient, credible and trustworthy evidence to establish that he experienced what he [had] alleged regarding the army, the CID and the Karuna” (Applicant’s Record, Board’s Reasons, para 42).

#### 23126:3:subtheme:2 · paragraphs 17-21

- Raw key terms: `applicant, board, lanka, noted, para, persecution, protection, reasons`
- Display key terms: `lanka, noted, para, persecution, protection`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: lanka, noted, para, persecution, protection Rule/authority context: The Board thus found that the Applicant could not be considered a person in need of protection under subsection 97(1) of the IRPA on the basis of this threat. Evidence spans paragraphs 17-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5084263` offsets `160-167`; context: [16] Despite its credibility concerns related to the Applicant’s claim of being targeted by the army and other pro-government groups, the Board then considered whether the Applicant, as a young Tamil male originating from the north “would face a reasonable chance of persecution for a Convention ground if returned” to Sri Lanka (Applicant’s Record, Board’s Reasons, para 53).
- Evidence: `evidence_fact` cue `Record` at chunk `5084263` offsets `342-348`; context: [16] Despite its credibility concerns related to the Applicant’s claim of being targeted by the army and other pro-government groups, the Board then considered whether the Applicant, as a young Tamil male originating from the north “would face a reasonable chance of persecution for a Convention ground if returned” to Sri Lanka (Applicant’s Record, Board’s Reasons, para 53).
- Evidence: `evidence_fact` cue `Record` at chunk `5084264` offsets `245-251`; context: [17] Citing a 2010 report from the United Nations Commissioner for Refugees [UNHCR], the Board noted that since the end of the civil war “general conditions in Sri Lanka no longer justify protection based simply on Tamil ethnicity” (Applicant’s Record, Board’s Reasons, para 52).
- Evidence: `evidence_fact` cue `Record` at chunk `5084265` offsets `171-177`; context: [18] With respect to the situation faced by returning asylum seekers, the Board noted that “there [are] conflicting reports about the treatment of returnees” (Applicant’s Record, Board’s Reasons, para 56).
- Evidence: `evidence_fact` cue `evidence` at chunk `5084266` offsets `38-46`; context: [19] The Board also noted documentary evidence indicating an increase in reports of abductions for the purpose of extortion in the north of Sri Lanka, but determined that these incidents were criminal rather than political in nature and that the risk was faced by citizens perceived as having money.
- Evidence: `governing_rule` cue `under` at chunk `5084266` offsets `487-492`; context: The Board thus found that the Applicant could not be considered a person in need of protection under subsection 97(1) of the IRPA on the basis of this threat.
- Evidence: `counterargument_limitation` cue `but` at chunk `5084266` offsets `151-154`; context: [19] The Board also noted documentary evidence indicating an increase in reports of abductions for the purpose of extortion in the north of Sri Lanka, but determined that these incidents were criminal rather than political in nature and that the risk was faced by citizens perceived as having money.

#### 23126:3:subtheme:3 · paragraphs 22-23

- Raw key terms: `canada, review, standard, accepted, adequate, against, alors, analysis`
- Display key terms: `review, standard, accepted, adequate, against, alors, analysis`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: review, standard, accepted, adequate, against, alors, analysis Rule/authority context: Issues and standard of review A. | [22] The standard of review applicable to the first issue is that of correctness (see Nageem v Canada (Minister of Citizenship and Immigration), 2012 FC 867 at para 14 [Nageem]; Paramsothy v Canada (Minister of Citizensh Application context: (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa r Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5084268` offsets `3320-3326`; context: Issues and standard of review
A.
- Evidence: `evidence_fact` cue `evidence` at chunk `5084268` offsets `3643-3651`; context: Did the Board fail to consider relevant evidence before it?
- Evidence: `governing_rule` cue `standard of review` at chunk `5084268` offsets `3331-3349`; context: Issues and standard of review
A.
- Evidence: `reasoning_application` cue `because` at chunk `5084268` offsets `2315-2322`; context: (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
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
- Evidence: `issue` cue `issue` at chunk `5084269` offsets `52-57`; context: [22] The standard of review applicable to the first issue is that of correctness (see Nageem v Canada (Minister of Citizenship and Immigration), 2012 FC 867 at para 14 [Nageem]; Paramsothy v Canada (Minister of Citizenship and Immigration), 2012 FC 1000 at para 19).
- Evidence: `governing_rule` cue `standard of review` at chunk `5084269` offsets `9-27`; context: [22] The standard of review applicable to the first issue is that of correctness (see Nageem v Canada (Minister of Citizenship and Immigration), 2012 FC 867 at para 14 [Nageem]; Paramsothy v Canada (Minister of Citizenship and Immigration), 2012 FC 1000 at para 19).

#### 23126:3:subtheme:4 · paragraphs 24-25

- Raw key terms: `canada, citizenship, immigration, minister, para, reasonableness, reviewable, standard`
- Display key terms: `para, reasonableness, reviewable, standard`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: para, reasonableness, reviewable, standard Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5084270` offsets `32-40`; context: [23] A credibility finding is a question of fact that is reviewable on a reasonableness standard (see Lawal v Canada (Minister of Citizenship and Immigration), 2010 FC 558 at para 11).
- Evidence: `issue` cue `issue` at chunk `5084271` offsets `15-20`; context: [24] The third issue deals with the Board’s appreciation of the evidence before it and is reviewable on a standard of reasonableness (see Canada (Minister of Citizenship and Immigration) v Gondara, 2011 FC 352 at para 38).
- Evidence: `evidence_fact` cue `evidence` at chunk `5084271` offsets `64-72`; context: [24] The third issue deals with the Board’s appreciation of the evidence before it and is reviewable on a standard of reasonableness (see Canada (Minister of Citizenship and Immigration) v Gondara, 2011 FC 352 at para 38).

#### 23126:3:subtheme:5 · paragraphs 26-40

- Raw key terms: `applicant, board, letter, evidence, para, canada, minister, test`
- Display key terms: `letter, para`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: letter, para Position/evidence statements: [26] The Applicant first contends that the Board applied an incorrect standard for the likelihood of persecution. | [27] The Applicant contends that this error was fatal and cannot be remedied by the fact that the correct test was articulated at other points in the decision. Rule/authority context: more than a mere possibility but not necessarily more than a 50% chance) of persecution if a claimant is returned to their country of origin pursuant to Adjei v Canada (Minister of Employment and Immigration), [1989] 2 F Application context: [26] The Applicant first contends that the Board applied an incorrect standard for the likelihood of persecution. | In Naredo, the Court held that when two tests for determining refugee protection are conflated, one correct, the other incorrect, the decision cannot stand because it is impossible to determine which test was applied to  Evidence spans paragraphs 26-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5084272` offsets `16-21`; context: [25] The fourth issue is reviewable on a standard of correctness (see Innocent v Canada (Minister of Citizenship and Immigration), 2009 FC 1019 at para 36).
- Evidence: `issue` cue `whether` at chunk `5084273` offsets `134-141`; context: The correct test is whether there is a serious possibility (i.
- Evidence: `party_position` cue `contends` at chunk `5084273` offsets `25-33`; context: [26] The Applicant first contends that the Board applied an incorrect standard for the likelihood of persecution.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5084273` offsets `320-331`; context: more than a mere possibility but not necessarily more than a 50% chance) of persecution if a claimant is returned to their country of origin pursuant to Adjei v Canada (Minister of Employment and Immigration), [1989] 2 FC 680 [Adjei].
- Evidence: `reasoning_application` cue `applied` at chunk `5084273` offsets `49-56`; context: [26] The Applicant first contends that the Board applied an incorrect standard for the likelihood of persecution.
- Evidence: `party_position` cue `contends` at chunk `5084274` offsets `19-27`; context: [27] The Applicant contends that this error was fatal and cannot be remedied by the fact that the correct test was articulated at other points in the decision.
- Evidence: `reasoning_application` cue `because` at chunk `5084274` offsets `472-479`; context: In Naredo, the Court held that when two tests for determining refugee protection are conflated, one correct, the other incorrect, the decision cannot stand because it is impossible to determine which test was applied to the facts.
- Evidence: `party_position` cue `submits` at chunk `5084275` offsets `19-26`; context: [28] The Applicant submits that the Board’s treatment of the evidence was “perverse and unreasonable” and presents his submissions based on each piece of evidence evaluated.
- Evidence: `evidence_fact` cue `evidence` at chunk `5084275` offsets `61-69`; context: [28] The Applicant submits that the Board’s treatment of the evidence was “perverse and unreasonable” and presents his submissions based on each piece of evidence evaluated.
- Evidence: `party_position` cue `argues` at chunk `5084276` offsets `19-25`; context: [29] The Applicant argues that the Board erred in making an adverse credibility finding on the basis of what the JP’s letter did not say while ignoring what it did state (see Bagri v Canada (Minister of Citizenship and Immigration), [1999] FCJ No 784, 168 FTR 283 at para 11 [Bagri]; N.
- Evidence: `evidence_fact` cue `evidence` at chunk `5084276` offsets `544-552`; context: What is more, after questioning the JP’s credibility by stating that the Applicant’s father had instructed him what to write in the letter, the Board later preferred the JP’s evidence over the Applicant’s.
- Evidence: `party_position` cue `contends` at chunk `5084277` offsets `24-32`; context: [30] The Applicant also contends that the Board failed to provide any reasons for not accepting the Applicant’s explanation as to why the JP’s letter did not mention the Applicant’s mistreatment at the hands of the army, the CID and the Karuna group (namely, that the JP feared retribution).
- Evidence: `party_position` cue `argues` at chunk `5084279` offsets `27-33`; context: [32] In sum, the Applicant argues that the Board erroneously ignored his own testimony because it faulted the JP’s letter adduced to support his claim.
- Evidence: `evidence_fact` cue `testimony` at chunk `5084279` offsets `77-86`; context: [32] In sum, the Applicant argues that the Board erroneously ignored his own testimony because it faulted the JP’s letter adduced to support his claim.
- Evidence: `reasoning_application` cue `because` at chunk `5084279` offsets `87-94`; context: [32] In sum, the Applicant argues that the Board erroneously ignored his own testimony because it faulted the JP’s letter adduced to support his claim.
- Evidence: `party_position` cue `argues` at chunk `5084280` offsets `190-196`; context: The Applicant argues that the Board committed the same error of impugning the Applicant’s credibility based on what the medical certificate did not say, as it did with the JP’s letter.
- Evidence: `party_position` cue `submits` at chunk `5084281` offsets `19-26`; context: [34] The Applicant submits that the Board erred in concluding that the Applicant had failed to prove that he stayed in Sri Lanka until January 2011.
- Evidence: `evidence_fact` cue `evidence` at chunk `5084281` offsets `333-341`; context: The Applicant asserts that the “absence of evidence is not a sufficient basis to reject uncontradicted evidence which is not inherently implausible” (Applicant’s Record, Board’s Reasons, page 332, para 31).
- Evidence: `evidence_fact` cue `evidence` at chunk `5084282` offsets `113-121`; context: [35] The Applicant maintains that the Board incorrectly stated that he failed to provide objective corroborating evidence for his claim.
- Evidence: `reasoning_application` cue `because` at chunk `5084282` offsets `248-255`; context: The letter from the Applicant’s mother corroborated his story but was improperly given little probative weight because the Board did not find the Applicant credible.
- Evidence: `counterargument_limitation` cue `but` at chunk `5084282` offsets `199-202`; context: The letter from the Applicant’s mother corroborated his story but was improperly given little probative weight because the Board did not find the Applicant credible.
- Evidence: `party_position` cue `claims` at chunk `5084283` offsets `19-25`; context: [36] The Applicant claims that, in finding that the situation for Tamils in Sri Lanka has improved since the war ended the Board selectively relied on dated inapplicable documentary evidence, while ignoring more recent country condition reports submitted by the Applicant.
- Evidence: `evidence_fact` cue `evidence` at chunk `5084283` offsets `182-190`; context: [36] The Applicant claims that, in finding that the situation for Tamils in Sri Lanka has improved since the war ended the Board selectively relied on dated inapplicable documentary evidence, while ignoring more recent country condition reports submitted by the Applicant.
- Evidence: `counterargument_limitation` cue `but` at chunk `5084283` offsets `394-397`; context: For example, the Board accepted information from one source stating that Emergency regulations were relaxed in May 2010, but ignored a more recent report indicating that those regulations were replaced with “equally draconian laws […] to continue the same kind of arbitrary detentions and mistreatment” (Applicant’s Record, page 333, para 35).
- Evidence: `party_position` cue `contends` at chunk `5084284` offsets `28-36`; context: [37] Finally, the Applicant contends that the Board misunderstood the concept of “generalized risk” as it relates to protection claims, by failing to differentiate between a risk faced by Tamils and one faced by all Sri Lankans.
- Evidence: `evidence_fact` cue `evidence` at chunk `5084284` offsets `274-282`; context: The Applicant maintains that “[t]here was no evidence before the panel that all Sri Lankans face extortion”.
- Evidence: `reasoning_application` cue `therefore` at chunk `5084284` offsets `814-823`; context: He should therefore be excluded from protection.
- Evidence: `party_position` cue `submits` at chunk `5084285` offsets `20-27`; context: [38] The Respondent submits that the Board made findings regarding the credibility and plausibility of the evidence which were reasonably open to it based on the record and that the “Applicant’s position simply amounts to a disagreement with the manner the evidence was assessed and weighed” (Respondent’s Memorandum of Argument, para 2).
- Evidence: `evidence_fact` cue `evidence` at chunk `5084285` offsets `107-115`; context: [38] The Respondent submits that the Board made findings regarding the credibility and plausibility of the evidence which were reasonably open to it based on the record and that the “Applicant’s position simply amounts to a disagreement with the manner the evidence was assessed and weighed” (Respondent’s Memorandum of Argument, para 2).
- Evidence: `party_position` cue `asserts` at chunk `5084286` offsets `232-239`; context: After citing a number of examples where the Board correctly articulates the test, namely paragraphs 17, 18, 19, 59 and 62, the Respondent asserts that when you look at the decision as a whole, it is clear that the Board applied the correct standard of proof of a “reasonable chance” or “more than a mere possibility”.
- Evidence: `reasoning_application` cue `applied` at chunk `5084286` offsets `45-52`; context: [39] The Respondent maintains that the Board applied the correct test for refugee protection.

#### 23126:3:subtheme:6 · paragraphs 41-42

- Raw key terms: `applicant, board, credibility, finding, respondent, applicable, argument, attention`
- Display key terms: `credibility, finding, applicable, argument, attention`
- Argument roles: `evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position, reasoning_application Display terms: credibility, finding, applicable, argument, attention Position/evidence statements: [41] While the Applicant claims that the Board made a credibility finding based on what the JP’s letter did not say, the Respondent insists that this is incorrect. Rule/authority context: [40] The Respondent also notes that when the Board stated, at paragraph 53 of its decision, that it “finds on a balance of probabilities that the authorities would not have an interest in pursuing [the Applicant] and fin Application context: The Respondent maintains that, because the “Board did not believe the Applicant, it reasonably required corroborative documents, which the Applicant failed to provide” (Respondent’s Memorandum of Argument, para 25). Evidence spans paragraphs 41-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `legal test` at chunk `5084287` offsets `468-478`; context: [40] The Respondent also notes that when the Board stated, at paragraph 53 of its decision, that it “finds on a balance of probabilities that the authorities would not have an interest in pursuing [the Applicant] and finds on a balance of probabilities that he is not a person who would attract undue attention or reprisal from militant organizations or security forces if returned to his family”, it was making a credibility finding and not describing the applicable legal test.
- Evidence: `party_position` cue `claims` at chunk `5084288` offsets `25-31`; context: [41] While the Applicant claims that the Board made a credibility finding based on what the JP’s letter did not say, the Respondent insists that this is incorrect.
- Evidence: `evidence_fact` cue `found that` at chunk `5084288` offsets `259-269`; context: The Board looked at the JP’s letter, the medical documents and the letter from the mother, and found that they were inconsistent with the Applicant’s story, or at least, that they did not corroborate his claims of continuous targeting.
- Evidence: `reasoning_application` cue `because` at chunk `5084288` offsets `431-438`; context: The Respondent maintains that, because the “Board did not believe the Applicant, it reasonably required corroborative documents, which the Applicant failed to provide” (Respondent’s Memorandum of Argument, para 25).

#### 23126:3:subtheme:7 · paragraphs 43-55

- Raw key terms: `board, applicant, credibility, evidence, para, respondent, because, canada`
- Display key terms: `credibility, para, because`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: credibility, para, because Position/evidence statements: The Respondent asserts that, contrary to what the Applicant submits, “the Board did not have to accept [the Applicant’s] uncontradicted testimony [on this issue] if it is not “consistent with the probabilities affecting  | [43] Finally, the Respondent argues that the Board did not err in assigning little weight to the Applicant’s mother’s letter given the Applicant’s general lack of credibility. Rule/authority context: Did the Board err in applying the wrong standard of proof in its analysis of the objective component of the fear of persecution invoked by the Applicant under section 96 of the IRPA? | “The jurisprudence is clear in stating that the Board's credibility and plausibility analysis is central to its role as trier of facts and that, accordingly, its findings in this regard should be given significant defere Application context: The Respondent also argues that, because the “Board did not have credible, claimant specific evidence to find that the Applicant possessed a fear of persecution, […] [t]he Board was not obligated to go through the fruitl | It therefore concluded that such a risk, even if real for the Applicant, would still be faced by others generally. Evidence spans paragraphs 43-55. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5084289` offsets `19-27`; context: [42] Regarding the question of when the Applicant left Sri Lanka, the Board noted that Mr.
- Evidence: `party_position` cue `asserts` at chunk `5084289` offsets `211-218`; context: The Respondent asserts that, contrary to what the Applicant submits, “the Board did not have to accept [the Applicant’s] uncontradicted testimony [on this issue] if it is not “consistent with the probabilities affecting the case as a whole”” (Respondent’s Memorandum of Argument, para 28).
- Evidence: `evidence_fact` cue `evidence` at chunk `5084289` offsets `137-145`; context: Balasubramaniam did not provide any objective evidence that he remained in Sri Lanka until January 2011.
- Evidence: `party_position` cue `argues` at chunk `5084290` offsets `29-35`; context: [43] Finally, the Respondent argues that the Board did not err in assigning little weight to the Applicant’s mother’s letter given the Applicant’s general lack of credibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `5084290` offsets `456-464`; context: The Board did not ignore relevant evidence
- Evidence: `party_position` cue `submits` at chunk `5084291` offsets `20-27`; context: [44] The Respondent submits that the Board did not ignore the country conditions evidence adduced by the Applicant.
- Evidence: `evidence_fact` cue `evidence` at chunk `5084291` offsets `81-89`; context: [44] The Respondent submits that the Board did not ignore the country conditions evidence adduced by the Applicant.
- Evidence: `reasoning_application` cue `because` at chunk `5084291` offsets `316-323`; context: The Respondent also argues that, because the “Board did not have credible, claimant specific evidence to find that the Applicant possessed a fear of persecution, […] [t]he Board was not obligated to go through the fruitless exercise of considering the objective aspect of [the Applicant’s] claim by reviewing the documentary evidence in detail” (Respondent’s Memorandum of Argument, para 33).
- Evidence: `governing_rule` cue `under` at chunk `5084292` offsets `674-679`; context: Did the Board err in applying the wrong standard of proof in its analysis of the objective component of the fear of persecution invoked by the Applicant under section 96 of the IRPA?
- Evidence: `reasoning_application` cue `therefore` at chunk `5084292` offsets `314-323`; context: It therefore concluded that such a risk, even if real for the Applicant, would still be faced by others generally.
- Evidence: `reasoning_application` cue `apply` at chunk `5084293` offsets `65-70`; context: [46] The Court agrees with the Respondent that the Board did not apply an incorrect standard of proof for a “well-founded fear of persecution” in its section 96 analysis.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5084295` offsets `76-89`; context: “The jurisprudence is clear in stating that the Board's credibility and plausibility analysis is central to its role as trier of facts and that, accordingly, its findings in this regard should be given significant deference” (see Lin v Canada (Minister of Citizenship and Immigration), 2008 FC 1052, [2008] FCJ No 1329 at para 13).
- Evidence: `reasoning_application` cue `accordingly` at chunk `5084295` offsets `216-227`; context: “The jurisprudence is clear in stating that the Board's credibility and plausibility analysis is central to its role as trier of facts and that, accordingly, its findings in this regard should be given significant deference” (see Lin v Canada (Minister of Citizenship and Immigration), 2008 FC 1052, [2008] FCJ No 1329 at para 13).
- Evidence: `evidence_fact` cue `evidence` at chunk `5084296` offsets `179-187`; context: [49] While the Board accepted that the Applicant’s story was internally consistent, its negative credibility finding was primarily based on inconsistencies with the corroborating evidence he adduced.
- Evidence: `party_position` cue `argues` at chunk `5084297` offsets `19-25`; context: [50] The Applicant argues that the Board’s negative credibility finding is unreasonable because it was based on what the JP’s letter and medical certificate failed to state (see Bagri, cited above, at para 11).
- Evidence: `reasoning_application` cue `because` at chunk `5084297` offsets `88-95`; context: [50] The Applicant argues that the Board’s negative credibility finding is unreasonable because it was based on what the JP’s letter and medical certificate failed to state (see Bagri, cited above, at para 11).
- Evidence: `evidence_fact` cue `determined that` at chunk `5084298` offsets `46-61`; context: [51] Given its credibility finding, the Board determined that the Applicant had not adduced sufficient corroborative evidence to support his claim of being tortured and harassed at the hands of the army, the CID and the Karuna group on the suspicion that he had LTTE ties.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5084298` offsets `278-291`; context: “The jurisprudence holds that where a claimant’s story is found to be flawed because of credibility findings, the lack of documentary corroboration is a valid consideration for the purposes of further assessing credibility” (see Matsko v Canada (Minister of Citizenship and Immigration), 2008 FC 691 at para 14).
- Evidence: `reasoning_application` cue `because` at chunk `5084298` offsets `350-357`; context: “The jurisprudence holds that where a claimant’s story is found to be flawed because of credibility findings, the lack of documentary corroboration is a valid consideration for the purposes of further assessing credibility” (see Matsko v Canada (Minister of Citizenship and Immigration), 2008 FC 691 at para 14).
- Evidence: `evidence_fact` cue `evidence` at chunk `5084299` offsets `79-87`; context: [52] The Board decided to assign little weight to another piece of documentary evidence which corroborated the Applicant’s claim, his mother’s letter.
- Evidence: `reasoning_application` cue `because` at chunk `5084299` offsets `453-460`; context: The Applicant argues that the Board erred by preferring the JP’s letter to the mother’s, simply because the latter came from a relative.
- Evidence: `counterargument_limitation` cue `but` at chunk `5084299` offsets `822-825`; context: This Court’s role is not to reweigh the evidence but to ensure that the conclusion drawn by the board was one that was reasonably available.
- Evidence: `party_position` cue `argues` at chunk `5084300` offsets `19-25`; context: [53] The Applicant argues that the Board relied on dated information in evaluating current conditions in the North of Sri Lanka while ignoring more current reports.
- Evidence: `reasoning_application` cue `because` at chunk `5084300` offsets `540-547`; context: The Respondent further contends that, given the Board’s credibility findings, it was not even obliged to conduct a serious analysis of the objective country condition reports because they are not, by themselves, a sufficient basis on which the Board can uphold a claim (see Rahaman, cited above).
- Evidence: `evidence_fact` cue `evidence` at chunk `5084301` offsets `66-74`; context: [54] The Respondent is correct in stating that a lack of credible evidence regarding the subjective element of a section 96 claim is a fatal flaw (see Rodriguez v Canada (Minister of Citizenship and Immigration), 2002 FCT 292 at para 33; Tabet-Zatla v Canada (Minister of Citizenship and Immigration), [1999] FCJ No 1778 at para 6 (TD)).
- Evidence: `reasoning_application` cue `because` at chunk `5084301` offsets `515-522`; context: The case at bar can be distinguished from the decision in Yaliniz v Canada (Minister of Employment & Immigration), [1988] FCJ No 248, 7 Imm LR (2d) 163, cited by the Applicant, because here the Board found that the Applicant had fabricated the major portion of his claim (see Board’s Reasons, para 30).

#### 23126:3:subtheme:8 · paragraphs 56-60

- Raw key terms: `board, court, evidence, applicant, canada, citizenship, extortion, generalized`
- Display key terms: `extortion, generalized`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: extortion, generalized Position/evidence statements: [57] The Applicant, relying on the principle set out in Cepeda-Gutierrez v Canada (Minister of Citizenship and Immigration), [1998] FCJ No 1425, 157 FTR 35, also claimed that the Board committed a reviewable error when i Application context: The Board accepted that the Applicant had been a victim of abduction and extortion in 2008, and might very well again be in the future, but found that this risk was a generalized one and therefore did not meet one of the Operative outcome context: [59] The Court consequently finds that the application is dismissed as the Board’s decision is reasonable. Evidence spans paragraphs 56-60. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5084302` offsets `442-447`; context: 97 issue as well.
- Evidence: `evidence_fact` cue `evidence` at chunk `5084302` offsets `70-78`; context: [55] The Board, however, was still required to consider the objective evidence for its section 97 analysis.
- Evidence: `evidence_fact` cue `evidence` at chunk `5084303` offsets `82-90`; context: [56] The Court is of the opinion that the Board adequately assessed the objective evidence for the purpose of its section 97 analysis.
- Evidence: `reasoning_application` cue `therefore` at chunk `5084303` offsets `515-524`; context: The Board accepted that the Applicant had been a victim of abduction and extortion in 2008, and might very well again be in the future, but found that this risk was a generalized one and therefore did not meet one of the conditions found in subparagraph 97(1)(b)(ii) of the IRPA.
- Evidence: `party_position` cue `claimed` at chunk `5084304` offsets `162-169`; context: [57] The Applicant, relying on the principle set out in Cepeda-Gutierrez v Canada (Minister of Citizenship and Immigration), [1998] FCJ No 1425, 157 FTR 35, also claimed that the Board committed a reviewable error when it failed to explain why it preferred two reports from 2010, one from the UNHCR and another from the Danish Immigration Services rather than documentation he submitted which dates from 2011 and establishes that Tamils returning to Sri Lanka are more greatly exposed to a risk of torture and extortion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5084304` offsets `605-613`; context: It is trite law that the Board is not obligated to comment on every single piece of evidence adduced by a refugee claimant as long as it properly dealt with the evidence (see Florea v Canada (Minister of Employment and Immigration), (FCA), [1993] FCJ No 598 (available on QL)).
- Evidence: `evidence_fact` cue `evidence` at chunk `5084305` offsets `78-86`; context: It cited evidence that extortion has been on the rise in the north and east of Sri Lanka and that the targets are usually people perceived as wealthy.
- Evidence: `disposition` cue `dismissed` at chunk `5084306` offsets `58-67`; context: [59] The Court consequently finds that the application is dismissed as the Board’s decision is reasonable.

#### Section text

[14] The Board based its negative credibility findings on a number of observations:
(a) The Board found that information provided by the Justice of the Peace’s [JP] letter regarding the July 6, 2008 abduction and the motive and timing of the Applicant’s departure were inconsistent with the narrative in his Personal Information Form [PIF]:
(i) The JP’s letter stated that the incident happened on July 6, 2008 and was committed by “unknown persons”, while the PIF did not provide a specific date and specified the EPDP as the perpetrators;
(ii) Although the Applicant stated that the JP knew his family personally, including all of the Applicant’s experiences, the letter did not provide any details about the incidents involving the army, the CID or members of the Karuna group;
(iii) The JP’s letter did not mention that two and a half years lapsed between the July 6, 2008 abduction and the Applicant’s decision to flee abroad, but could imply that the Applicant made his decision to go abroad soon after the July 6, 2008 incident; and
(iv) Contrary to the Applicant’s PIF, the JP’s letter specifies that the Applicant fled after having more problems with the same group of unknown persons that abducted him on July 6, 2008.
(b) The medical certificate also indicates that the abduction occurred on July 6, 2008 and was perpetrated by “unknown persons”;
(c) The Applicant failed to properly explain the discrepancies between his PIF, the JP’s letter and the medical certificate;
(d) The Applicant’s explanation for why the JP only mentioned the July 2008 incident in his letter was not compelling. The Board found that the JP could have written about the other incidents without implicating the army;
(e) The Applicant said his family went to the JP for all their needs but was unable to provide any examples of other situations when they had sought his assistance;
(f) While the Applicant indicated that his family may have been suspected of having ties with the LTTE because his uncle had been forced to join them, he failed to adequately explain why he was the only member of his family being forced to flee;
(g) The Board found that the if he had been arrested on suspicion of helping the LTTE he would not have been released from detention unless the army was satisfied he had no LTTE ties;
(h) The Applicant was unable to provide any corroborative objective evidence regarding his alleged detentions and torture by the army, the CID or the Karuna group purported to have occurred after the July 2008 incident. The Board gave little probative weight to the Applicant’s mother’s letter:
(i) Due to credibility concerns regarding the Applicant and;
(ii) The absence of details and of any medical or other corroborative documents regarding the attack on the Applicant’s father.
(i) The Board was not provided with a passport or documents related to arrangements for his travel to Canada or proof of the land transaction his father made to finance his trip;
(j) The Applicant failed to provide objective evidence that he lived in Sri Lanka until January 2011; and
(k) The Applicant was detained for four months in Mexico and two months in the United States and failed to claim asylum in those countries.

[15] The Board concluded that the Applicant “failed to provide sufficient, credible and trustworthy evidence to establish that he experienced what he [had] alleged regarding the army, the CID and the Karuna” (Applicant’s Record, Board’s Reasons, para 42). The Board did not find that the Applicant was suspected of having ties with the LTTE in the past or that he would be suspected of having such ties were he to be returned to Sri Lanka.
B. Lack of objective basis for prospective fear

[16] Despite its credibility concerns related to the Applicant’s claim of being targeted by the army and other pro-government groups, the Board then considered whether the Applicant, as a young Tamil male originating from the north “would face a reasonable chance of persecution for a Convention ground if returned” to Sri Lanka (Applicant’s Record, Board’s Reasons, para 53).

[17] Citing a 2010 report from the United Nations Commissioner for Refugees [UNHCR], the Board noted that since the end of the civil war “general conditions in Sri Lanka no longer justify protection based simply on Tamil ethnicity” (Applicant’s Record, Board’s Reasons, para 52).

[18] With respect to the situation faced by returning asylum seekers, the Board noted that “there [are] conflicting reports about the treatment of returnees” (Applicant’s Record, Board’s Reasons, para 56). After considering the documentary evidence, the Board ultimately found that returnees are not being specifically targeted. While the evidence did show that some returnees setting up businesses had been harassed and targeted for extortion, the Board felt that the Applicant would be able to return to his former occupation as a tutor without facing more than a mere possibility of persecution. The Board also noted that the Applicant would not, on a balance of probabilities, be suspected of having links to the LLTE if returned to Sri Lanka.

[19] The Board also noted documentary evidence indicating an increase in reports of abductions for the purpose of extortion in the north of Sri Lanka, but determined that these incidents were criminal rather than political in nature and that the risk was faced by citizens perceived as having money. The Board found the risk to be a generalized one faced by a large number of other citizens. The Board thus found that the Applicant could not be considered a person in need of protection under subsection 97(1) of the IRPA on the basis of this threat.

[20] Ultimately, the Board concluded that the Applicant does not have a well-founded fear of persecution and is not a person in need of protection as contemplated by sections 96 and 97 of the IRPA.
IV. Legislation

[21] Section 96 and subsection 97(1) of the IRPA provide as follows:
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
V. Issues and standard of review
A. Issues
1. Did the Board err in applying the wrong standard of proof in its analysis of the objective component of the fear of persecution invoked by the Applicant under section 96 of the IRPA?
2. Was the Board’s credibility assessment reasonable?
3. Did the Board fail to consider relevant evidence before it?
4. Did the Board err in its understanding of generalized risk?
B. Standard of review

[22] The standard of review applicable to the first issue is that of correctness (see Nageem v Canada (Minister of Citizenship and Immigration), 2012 FC 867 at para 14 [Nageem]; Paramsothy v Canada (Minister of Citizenship and Immigration), 2012 FC 1000 at para 19).

[23] A credibility finding is a question of fact that is reviewable on a reasonableness standard (see Lawal v Canada (Minister of Citizenship and Immigration), 2010 FC 558 at para 11).

[24] The third issue deals with the Board’s appreciation of the evidence before it and is reviewable on a standard of reasonableness (see Canada (Minister of Citizenship and Immigration) v Gondara, 2011 FC 352 at para 38).

[25] The fourth issue is reviewable on a standard of correctness (see Innocent v Canada (Minister of Citizenship and Immigration), 2009 FC 1019 at para 36).
VI. Parties’ submissions
A. Applicant’s submissions
1. Incorrect test

[26] The Applicant first contends that the Board applied an incorrect standard for the likelihood of persecution. The correct test is whether there is a serious possibility (i.e. more than a mere possibility but not necessarily more than a 50% chance) of persecution if a claimant is returned to their country of origin pursuant to Adjei v Canada (Minister of Employment and Immigration), [1989] 2 FC 680 [Adjei]. The Applicant cites a number of instances in the decision where the Board incorrectly evaluates the Applicant’s chances of persecution on a balance of probabilities standard namely paragraphs 20, 53 and 57 of the Board’s decision.

[27] The Applicant contends that this error was fatal and cannot be remedied by the fact that the correct test was articulated at other points in the decision. The Applicant relies on the Federal Court of Appeal’s decision in Naredo v Canada (Minister of Employment & Immigration), [1981] FCJ No 1130 (CA) [Naredo]. In Naredo, the Court held that when two tests for determining refugee protection are conflated, one correct, the other incorrect, the decision cannot stand because it is impossible to determine which test was applied to the facts.
2. Credibility findings

[28] The Applicant submits that the Board’s treatment of the evidence was “perverse and unreasonable” and presents his submissions based on each piece of evidence evaluated.
a. The letter from the Justice of Peace

[29] The Applicant argues that the Board erred in making an adverse credibility finding on the basis of what the JP’s letter did not say while ignoring what it did state (see Bagri v Canada (Minister of Citizenship and Immigration), [1999] FCJ No 784, 168 FTR 283 at para 11 [Bagri]; N.N.N. v Canada (Minister of Citizenship and Immigration), 2009 FC 1281 at para 73). What is more, after questioning the JP’s credibility by stating that the Applicant’s father had instructed him what to write in the letter, the Board later preferred the JP’s evidence over the Applicant’s.

[30] The Applicant also contends that the Board failed to provide any reasons for not accepting the Applicant’s explanation as to why the JP’s letter did not mention the Applicant’s mistreatment at the hands of the army, the CID and the Karuna group (namely, that the JP feared retribution).

[31] Finally, the fact that JP’s letter said that “unknown persons” in a white van abducted the Applicant does not contradict his claim that members of the EPDP were involved; the information is just less specific.

[32] In sum, the Applicant argues that the Board erroneously ignored his own testimony because it faulted the JP’s letter adduced to support his claim.
b. The medical certificate

[33] The Applicant also posits that the Board failed to provide any reasons for rejecting the Applicant’s explanation as to why the doctor did not name the EPDP in his letter. The Applicant argues that the Board committed the same error of impugning the Applicant’s credibility based on what the medical certificate did not say, as it did with the JP’s letter.
c. Timing of the Applicant’s departure from Sri Lanka

[34] The Applicant submits that the Board erred in concluding that the Applicant had failed to prove that he stayed in Sri Lanka until January 2011. The Board did not provide adequate reasons for not accepting the Applicant’s uncontradicted sworn statement that he left in January of 2011. The Applicant asserts that the “absence of evidence is not a sufficient basis to reject uncontradicted evidence which is not inherently implausible” (Applicant’s Record, Board’s Reasons, page 332, para 31).
d. The mother’s letter

[35] The Applicant maintains that the Board incorrectly stated that he failed to provide objective corroborating evidence for his claim. The letter from the Applicant’s mother corroborated his story but was improperly given little probative weight because the Board did not find the Applicant credible. In doing so, the Board erred by assessing the mother’s letter as “self serving” evidence (see Ugalde v Canada (Minister of Public Safety and Emergency Preparedness), 2011 FC 458 at paras 25-28).
3. The Board ignored relevant evidence

[36] The Applicant claims that, in finding that the situation for Tamils in Sri Lanka has improved since the war ended the Board selectively relied on dated inapplicable documentary evidence, while ignoring more recent country condition reports submitted by the Applicant. For example, the Board accepted information from one source stating that Emergency regulations were relaxed in May 2010, but ignored a more recent report indicating that those regulations were replaced with “equally draconian laws […] to continue the same kind of arbitrary detentions and mistreatment” (Applicant’s Record, page 333, para 35).
4. Generalized risk

[37] Finally, the Applicant contends that the Board misunderstood the concept of “generalized risk” as it relates to protection claims, by failing to differentiate between a risk faced by Tamils and one faced by all Sri Lankans. The Applicant maintains that “[t]here was no evidence before the panel that all Sri Lankans face extortion”. In fact, the allegation is to the effect that the only evidence before the Board dealt with the targeting of Tamils by militant groups supporting the government (Applicant’s Record, page 333, para 36). The Board, according to the Applicant, incorrectly concluded that the risk of extortion he could potentially face upon his return would be attributable to his having perceived wealth, since he his returning from Canada and that this risk is faced by all citizens. He should therefore be excluded from protection.
B. Respondent’s submissions

[38] The Respondent submits that the Board made findings regarding the credibility and plausibility of the evidence which were reasonably open to it based on the record and that the “Applicant’s position simply amounts to a disagreement with the manner the evidence was assessed and weighed” (Respondent’s Memorandum of Argument, para 2).
1. Correct test

[39] The Respondent maintains that the Board applied the correct test for refugee protection. After citing a number of examples where the Board correctly articulates the test, namely paragraphs 17, 18, 19, 59 and 62, the Respondent asserts that when you look at the decision as a whole, it is clear that the Board applied the correct standard of proof of a “reasonable chance” or “more than a mere possibility”. The Respondent cites Newfoundland and Labrador Nurses' Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62, [2011] 3 SCR 708 at para 16, in support of this global assessment approach.

[40] The Respondent also notes that when the Board stated, at paragraph 53 of its decision, that it “finds on a balance of probabilities that the authorities would not have an interest in pursuing [the Applicant] and finds on a balance of probabilities that he is not a person who would attract undue attention or reprisal from militant organizations or security forces if returned to his family”, it was making a credibility finding and not describing the applicable legal test.
2. Credibility findings

[41] While the Applicant claims that the Board made a credibility finding based on what the JP’s letter did not say, the Respondent insists that this is incorrect. The Board looked at the JP’s letter, the medical documents and the letter from the mother, and found that they were inconsistent with the Applicant’s story, or at least, that they did not corroborate his claims of continuous targeting. The Respondent maintains that, because the “Board did not believe the Applicant, it reasonably required corroborative documents, which the Applicant failed to provide” (Respondent’s Memorandum of Argument, para 25).

[42] Regarding the question of when the Applicant left Sri Lanka, the Board noted that Mr. Balasubramaniam did not provide any objective evidence that he remained in Sri Lanka until January 2011. The Respondent asserts that, contrary to what the Applicant submits, “the Board did not have to accept [the Applicant’s] uncontradicted testimony [on this issue] if it is not “consistent with the probabilities affecting the case as a whole”” (Respondent’s Memorandum of Argument, para 28).

[43] Finally, the Respondent argues that the Board did not err in assigning little weight to the Applicant’s mother’s letter given the Applicant’s general lack of credibility. The Respondent relies on Nasim v Canada (Minister of Citizenship and Immigration), 2001 FCT 1199 (CanLII) and Waheed v Canada (Minister of Citizenship and Immigration), 2003 FCT 329 (CanLII), among other decisions, in support of his position.
3. The Board did not ignore relevant evidence

[44] The Respondent submits that the Board did not ignore the country conditions evidence adduced by the Applicant. It acknowledged the problems that continue to prevail and remarked that the situation was not perfect. The Board decides how it weighs the evidence adduced before it. The Respondent also argues that, because the “Board did not have credible, claimant specific evidence to find that the Applicant possessed a fear of persecution, […] [t]he Board was not obligated to go through the fruitless exercise of considering the objective aspect of [the Applicant’s] claim by reviewing the documentary evidence in detail” (Respondent’s Memorandum of Argument, para 33). The Respondent cites Rahaman v Canada (Minister of Citizenship

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 23126:4 · paragraphs 61-62

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `43314ee4aed39b75880029af635488eeef6e03d4784e1a7840514a54af56cd20`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23126:4:subtheme:1 · paragraphs 61-62

- Raw key terms: `andr, application, balasubramaniam, cause, certify, citizenship, court, date`
- Display key terms: `andr, balasubramaniam, certify, date`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: andr, balasubramaniam, certify, date Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that this application for judicial review is dismissed and that there is no question of general importance to certify. Evidence spans paragraphs 61-62. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5084306` offsets `217-225`; context: JUDGMENT
THIS COURT’S JUDGMENT is that this application for judicial review is dismissed and that there is no question of general importance to certify.
- Evidence: `disposition` cue `dismissed` at chunk `5084306` offsets `186-195`; context: JUDGMENT
THIS COURT’S JUDGMENT is that this application for judicial review is dismissed and that there is no question of general importance to certify.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that this application for judicial review is dismissed and that there is no question of general importance to certify.
"André F.J. Scott"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-4243-12
STYLE OF CAUSE: PARTHIPAN BALASUBRAMANIAM
v
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: May 13, 2013
REASONS FOR 

## 23126:5 · paragraphs 63-63

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a999f8e4a0055138d3f3cf555c509f951608cf4372ab30c0b8b1cd37250bd316`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23126:5:subtheme:1 · paragraphs 63-63

- Raw key terms: `appearances, applicant, associates, attorney, barbara, canada, dated, deputy`
- Display key terms: `associates, barbara, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: associates, barbara, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 63-63. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: SCOTT J.
DATED: June 21, 2013
APPEARANCES:
Barbara Jackman
Meghan Wilson
FOR THE APPLICANT
Monmi Goswami
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Jackman, Nazami & Associates
Toronto, Ontario
FOR THE APPLICANT
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
FOR THE RESPONDENT
