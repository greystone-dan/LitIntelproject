# Discussion Units: case 25170

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **73**
- Continuity pairs: **72**
- Discussion Units: **6**
- Paragraph source hashes: **73**
- Sub-themes: **19**

## 25170:1 · paragraphs 0-13

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `537b869846f796c6e961fe1dea073cfe9c7c97602ba984c112074beb027c5991`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25170:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `applicant, refugee, canada, cetinkaya, claimed, decision, ercan, immigration`
- Display key terms: `refugee, cetinkaya, claimed, ercan`
- Argument roles: `governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, party_position, reasoning_application Display terms: refugee, cetinkaya, claimed, ercan Position/evidence statements: He claimed refugee protection against Turkey because he fears persecution and harm from the Turkish police based on his race and nationality, his political opinion, and his membership in a particular social group. | [3] The Applicant claims that his family is known by the police to support Kurdish rights. Rule/authority context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S. Application context: He claimed refugee protection against Turkey because he fears persecution and harm from the Turkish police based on his race and nationality, his political opinion, and his membership in a particular social group. Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5184971` offsets `27-38`; context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `party_position` cue `claimed` at chunk `5184972` offsets `95-102`; context: He claimed refugee protection against Turkey because he fears persecution and harm from the Turkish police based on his race and nationality, his political opinion, and his membership in a particular social group.
- Evidence: `reasoning_application` cue `because` at chunk `5184972` offsets `137-144`; context: He claimed refugee protection against Turkey because he fears persecution and harm from the Turkish police based on his race and nationality, his political opinion, and his membership in a particular social group.
- Evidence: `party_position` cue `claims` at chunk `5184973` offsets `18-24`; context: [3] The Applicant claims that his family is known by the police to support Kurdish rights.

#### 25170:1:subtheme:2 · paragraphs 4-13

- Raw key terms: `applicant, because, demonstrations, evidence, found, police, attended, basis`
- Display key terms: `because, demonstrations, police, attended, basis`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: because, demonstrations, police, attended, basis Position/evidence statements: He claims he attended various protests to condemn human rights abuses against Kurds committed by Turkish people and authorities. | On the same day, he crossed the Canadian border and claimed refugee protection in Canada. Rule/authority context: DECISION UNDER REVIEW Application context: He was forced to leave middle school after two years because of oppression and raids on Kurdish villages by security forces and gendarmes. | [8] The RPD noted that, during the hearing, the Applicant said he had been beaten by authorities because he participated in demonstrations. Evidence spans paragraphs 4-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `5184974` offsets `165-172`; context: He was forced to leave middle school after two years because of oppression and raids on Kurdish villages by security forces and gendarmes.
- Evidence: `party_position` cue `claims` at chunk `5184975` offsets `142-148`; context: He claims he attended various protests to condemn human rights abuses against Kurds committed by Turkish people and authorities.
- Evidence: `party_position` cue `claimed` at chunk `5184976` offsets `195-202`; context: On the same day, he crossed the Canadian border and claimed refugee protection in Canada.
- Evidence: `governing_rule` cue `UNDER` at chunk `5184976` offsets `610-615`; context: DECISION UNDER REVIEW
- Evidence: `evidence_fact` cue `found that` at chunk `5184977` offsets `12-22`; context: [7] The RPD found that the Applicant did not have a subjective fear of persecution at the hands of the police and security forces in Turkey and there was no objective basis for his fear of persecution at the hands of the police.
- Evidence: `evidence_fact` cue `evidence` at chunk `5184978` offsets `186-194`; context: It noted that he had not provided documentary evidence that he had participated in these demonstrations.
- Evidence: `reasoning_application` cue `because` at chunk `5184978` offsets `97-104`; context: [8] The RPD noted that, during the hearing, the Applicant said he had been beaten by authorities because he participated in demonstrations.
- Evidence: `counterargument_limitation` cue `but` at chunk `5184978` offsets `385-388`; context: The RPD said he alleged in his PIF narrative, his Declaration and his Claim Form that he was tortured and beaten while he was in detention, but did not corroborate these allegations.
- Evidence: `reasoning_application` cue `because` at chunk `5184979` offsets `276-283`; context: The Declaration also said he was arrested, verbally and physically abused, and tortured by the police in 1998 because of his participation in demonstrations.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5184979` offsets `324-332`; context: Although the Applicant’s PIF mentions a number of incidents after 1998, the Applicant’s Declaration mentions only one incident, which occurred in 1998.
- Evidence: `evidence_fact` cue `evidence` at chunk `5184980` offsets `227-235`; context: The RPD found no persuasive evidence that the Applicant had not been given sufficient space, time or opportunity to complete his story, and noted that the Applicant had signed the document indicating that it was complete, true and correct, and that a line had been drawn through the remaining space for his story.
- Evidence: `evidence_fact` cue `evidence` at chunk `5184981` offsets `73-81`; context: [11] The RPD concluded that the Applicant had not persuaded it, with the evidence he had adduced, that he had attended the protests, demonstrations and Newroz celebrations after 1998 as he had alleged in his PIF.
- Evidence: `reasoning_application` cue `because` at chunk `5184981` offsets `700-707`; context: The RPD rejected his explanation that he did not seek medical attention after the torture because there were no physical signs.
- Evidence: `party_position` cue `submitted` at chunk `5184982` offsets `63-72`; context: [12] The RPD found that the affidavit the Applicant’s wife had submitted did not provide details about his arrest or attendance at protests.
- Evidence: `evidence_fact` cue `found that` at chunk `5184982` offsets `13-23`; context: [12] The RPD found that the affidavit the Applicant’s wife had submitted did not provide details about his arrest or attendance at protests.
- Evidence: `reasoning_application` cue `Because` at chunk `5184982` offsets `377-384`; context: Because he had not participated in demonstrations, the RPD found that the police would have no interest in him, so there was no objective basis for his fear of persecution.
- Evidence: `party_position` cue `claimed` at chunk `5184983` offsets `275-282`; context: The Applicant knew about the Canadian refugee process because other members of his family had successfully claimed in Canada.
- Evidence: `evidence_fact` cue `found that` at chunk `5184983` offsets `18-28`; context: [13] The RPD also found that the Applicant had delayed leaving Turkey for ten years after his arrest and beating in 1998, the only beating it accepted he had suffered.
- Evidence: `reasoning_application` cue `because` at chunk `5184983` offsets `222-229`; context: The Applicant knew about the Canadian refugee process because other members of his family had successfully claimed in Canada.

#### Section text

Cetinkaya v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2012-01-04
Neutral citation
2012 FC 8
File numbers
IMM-3362-11
Decision Content
Federal Court
Cour fédérale
Date: 20120104
Docket: IMM-3362-11
Citation: 2012 FC 8
Ottawa, Ontario, January 4, 2012
PRESENT: The Honourable Mr. Justice Russell
BETWEEN:
ERCAN CETINKAYA
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT
INTRODUCTION

[1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (Act) for judicial review of the decision of the Refugee Protection Division (RPD) of the Immigration and Refugee Board, dated 27 April 2011 (Decision), which refused the Applicant’s claim for protection as a Convention refugee or person in need of protection under sections 96 and 97 of the Act
BACKGROUND

[2] The Applicant, Ercan Cetinkaya, is Kurdish and a citizen of Turkey. He is 38 years old. He claimed refugee protection against Turkey because he fears persecution and harm from the Turkish police based on his race and nationality, his political opinion, and his membership in a particular social group.

[3] The Applicant claims that his family is known by the police to support Kurdish rights. He says many of his family members have been detained on several occasions for asserting their Kurdish identity. Also, several of his family members have successfully claimed refugee status in Canada since the 1990s.

[4] The Applicant says he was insulted and humiliated on a regular basis by his teachers when he was in school. He was forced to leave middle school after two years because of oppression and raids on Kurdish villages by security forces and gendarmes. He also says he was discriminated against, physically mistreated, and punished by his superior officers during his 18 month compulsory military service from 1992 to 1994.

[5] The Applicant says he was an active supporter of pro-Kurdish political parties such as the HADEP and the DTP while he lived in Turkey. He claims he attended various protests to condemn human rights abuses against Kurds committed by Turkish people and authorities. Beginning in November 1998, when the Applicant was first detained while he attended a protest organized by the pro-Kurdish political party HADEP, he says he was detained by police on six separate occasions while attending such events, mistreated, beaten and kicked, and, at times, tortured in detention. He says some of these incidents coincided with demonstrations in support of Kurdish rights around Kurdish Newroz (new year) celebrations in March of 2008 and 2009 (Newroz Demonstrations). When he was detained during the Newroz Demonstrations, the Applicant says he was severely beaten and subjected to falaka or flogging the soles of a victim’s feet. When he was detained in 2008, the police threatened to kill him.

[6] With the financial help of his brother, the Applicant obtained a visa for the United States and went to Detroit, Michigan on 22 July 2009. On the same day, he crossed the Canadian border and claimed refugee protection in Canada. At that time, he produced a handwritten declaration (Declaration) and completed “the Claim for Refugee Protection form (Claim Form). The Applicant also filed a Personal Information Form (PIF) on 13 August 2009. The RPD heard his refugee claim on 11 April 2011 and made its Decision on 27 April 2011. The RPD gave the Applicant notice of the Decision on 29 April 2011.
DECISION UNDER REVIEW

[7] The RPD found that the Applicant did not have a subjective fear of persecution at the hands of the police and security forces in Turkey and there was no objective basis for his fear of persecution at the hands of the police. The RPD found that he was not a credible witness and that there was no persuasive evidence the Applicant faced more than a generalized risk on return.

[8] The RPD noted that, during the hearing, the Applicant said he had been beaten by authorities because he participated in demonstrations. It noted that he had not provided documentary evidence that he had participated in these demonstrations. The RPD said he alleged in his PIF narrative, his Declaration and his Claim Form that he was tortured and beaten while he was in detention, but did not corroborate these allegations. The RPD said that at the hearing, the Applicant admitted that he was only beaten when he was asked to explain his failure to corroborate his allegations. The RPD found that the Applicant had attempted to mislead it into believing that he had been tortured by police while he had been detained.

[9] The RPD noted that in his Declaration, the Applicant indicated that he had attended demonstrations organized by the legal Kurdish civil organizations since 1997. The Declaration also said he was arrested, verbally and physically abused, and tortured by the police in 1998 because of his participation in demonstrations. Although the Applicant’s PIF mentions a number of incidents after 1998, the Applicant’s Declaration mentions only one incident, which occurred in 1998. Because no specific dates were listed in the Claim Form, the RPD did not accept the Applicant’s argument at the hearing that form indicates several occurrences over a period of time.

[10] The RPD asked the Applicant to explain the omissions from his POE statement, but rejected his explanation that the immigration officer had taken away the document before he completed his story. The RPD found no persuasive evidence that the Applicant had not been given sufficient space, time or opportunity to complete his story, and noted that the Applicant had signed the document indicating that it was complete, true and correct, and that a line had been drawn through the remaining space for his story.

[11] The RPD concluded that the Applicant had not persuaded it, with the evidence he had adduced, that he had attended the protests, demonstrations and Newroz celebrations after 1998 as he had alleged in his PIF. The Applicant had not produced documentary evidence to substantiate the claims he had made in his PIF. He did not produce documentary evidence to indicate that he participated in the pro-Kurdish protests he claimed to have attended, medical reports to indicate that he was tortured, or media reports to indicate that the protests had happened on the days he said he participated and was arrested. The RPD rejected his explanation that he did not seek medical attention after the torture because there were no physical signs.

[12] The RPD found that the affidavit the Applicant’s wife had submitted did not provide details about his arrest or attendance at protests. Further, the documents he provided after the hearing did not indicate he had participated in demonstrations. The RPD found that he had not attended demonstrations after 1998 and that he had fabricated these events to bolster his claim. Because he had not participated in demonstrations, the RPD found that the police would have no interest in him, so there was no objective basis for his fear of persecution.

[13] The RPD also found that the Applicant had delayed leaving Turkey for ten years after his arrest and beating in 1998, the only beating it accepted he had suffered. The Applicant knew about the Canadian refugee process because other members of his family had successfully claimed in Canada. The RPD rejected his explanation for the delay (that he did not have finances) saying that he had not mentioned this in his PIF. There was also no persuasive documentary evidence showing his father had sent money to help him get out of Turkey. Further, his testimony that his wife had a successful cosmetics business also demonstrated that it was implausible that he did not have the finances to leave Turkey. The PRD also rejected his explanation that he could not travel without his family. It said that they were not targeted and he eventually left them behind anyway. On the basis of these findings, the RPD found that the Applicant did not have a subjective fear of persecution in Turkey and there was no objective basis for his fear. It also found that there was no persuasive evidence which established a risk to him beyond that faced by all citizens in Turkey.
STATUTORY PROVISIONS

## 25170:2 · paragraphs 14-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1afa787942b8d7d07b1bc1aed96b8aae444b11923c17d351f682ace7847843d8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25170:2:subtheme:1 · paragraphs 14-14

- Raw key terms: `accepted, adequate, against, alors, appartenance, applicable, article, autres`
- Display key terms: `accepted, adequate, against, alors, appartenance, applicable, article, autres`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: accepted, adequate, against, alors, appartenance, applicable, article, autres Application context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subj Evidence spans paragraphs 14-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `5184984` offsets `2981-2987`; context: ISSUES
- Evidence: `reasoning_application` cue `because` at chunk `5184984` offsets `1000-1007`; context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning ­ of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care
Définition de « réfugié »
96.

#### Section text

[14] The following provisions of the Act are applicable in these proceedings:
Convention refugee
96. A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political
opinion,
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries;
[…]
Person in Need of Protection
97. (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning ­ of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care
Définition de « réfugié »
96. A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
[…]
Personne à protéger
97. (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
ISSUES

## 25170:3 · paragraphs 15-58

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `8262bc293958a65e0f8a1bb078ac0da7e59b1c356227738bf93d7e329f890c83`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25170:3:subtheme:1 · paragraphs 15-16

- Raw key terms: `review, standard, adopt, analysis, applicable, applicant, applied, brunswick`
- Display key terms: `review, standard, adopt, analysis, applicable, applied, brunswick`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: review, standard, adopt, analysis, applicable, applied, brunswick Rule/authority context: STANDARD OF REVIEW | [16] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9, held that a standard of review analysis need not be conducted in every instance. Application context: Whether the RPD applied the wrong test for torture; c. Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5184985` offsets `40-46`; context: [15] The Applicant raises the following issues:
a.
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `5184985` offsets `278-296`; context: STANDARD OF REVIEW
- Evidence: `reasoning_application` cue `applied` at chunk `5184985` offsets `129-136`; context: Whether the RPD applied the wrong test for torture;
c.
- Evidence: `issue` cue `question` at chunk `5184986` offsets `220-228`; context: Instead, where the standard of review applicable to a particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review.
- Evidence: `governing_rule` cue `standard of review` at chunk `5184986` offsets `86-104`; context: [16] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9, held that a standard of review analysis need not be conducted in every instance.

#### 25170:3:subtheme:2 · paragraphs 17-18

- Raw key terms: `canada, citizenship, court, held, immigration, minister, paragraph, aguebor`
- Display key terms: `paragraph, aguebor`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: paragraph, aguebor Rule/authority context: [17] In Elmi v Canada (Minister of Citizenship and Immigration) 2008 FC 773, at paragraph 21, Justice Max Teitelbaum held that findings of credibility are central to the RPD’s finding of fact and are therefore to be eval Application context: [17] In Elmi v Canada (Minister of Citizenship and Immigration) 2008 FC 773, at paragraph 21, Justice Max Teitelbaum held that findings of credibility are central to the RPD’s finding of fact and are therefore to be eval Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5184987` offsets `711-716`; context: The standard of review on the first issue is reasonableness.
- Evidence: `governing_rule` cue `standard of review` at chunk `5184987` offsets `231-249`; context: [17] In Elmi v Canada (Minister of Citizenship and Immigration) 2008 FC 773, at paragraph 21, Justice Max Teitelbaum held that findings of credibility are central to the RPD’s finding of fact and are therefore to be evaluated on a standard of review of reasonableness.
- Evidence: `reasoning_application` cue `therefore` at chunk `5184987` offsets `200-209`; context: [17] In Elmi v Canada (Minister of Citizenship and Immigration) 2008 FC 773, at paragraph 21, Justice Max Teitelbaum held that findings of credibility are central to the RPD’s finding of fact and are therefore to be evaluated on a standard of review of reasonableness.

#### 25170:3:subtheme:3 · paragraphs 19-20

- Raw key terms: `above, applicant, attract, canada, court, dunsmuir, generally, held`
- Display key terms: `above, attract, dunsmuir, generally`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: above, attract, dunsmuir, generally Rule/authority context: The standard of review on the second issue is reasonableness. | The standard of review on the third issue is reasonableness. Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5184989` offsets `29-36`; context: [19] The determination as to whether a particular act, such as the falaka the Applicant alleges, falls within the definition of torture approved by the Supreme Court of Canada calls for the application of the law to the facts before the RPD.
- Evidence: `governing_rule` cue `standard of review` at chunk `5184989` offsets `396-414`; context: The standard of review on the second issue is reasonableness.
- Evidence: `issue` cue `Whether` at chunk `5184990` offsets `5-12`; context: [20] Whether or not the Applicant was tortured in Turkey is purely a finding of fact.
- Evidence: `governing_rule` cue `standard of review` at chunk `5184990` offsets `234-252`; context: The standard of review on the third issue is reasonableness.

#### 25170:3:subtheme:4 · paragraphs 21-23

- Raw key terms: `analysis, applicant, applied, canada, court, decision, paragraph, reasonableness`
- Display key terms: `analysis, applied, paragraph, reasonableness`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: analysis, applied, paragraph, reasonableness Application context: The adequacy of reasons is therefore subsumed into the analysis of the reasonableness of the Decision as a whole. | [23] The Applicant says that the RPD applied an incorrect test for torture, and that the transcript does not support the RPD’s finding that he admitted he was beaten but not tortured. Evidence spans paragraphs 21-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5184991` offsets `219-226`; context: [21] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.
- Evidence: `reasoning_application` cue `therefore` at chunk `5184992` offsets `389-398`; context: The adequacy of reasons is therefore subsumed into the analysis of the reasonableness of the Decision as a whole.
- Evidence: `evidence_fact` cue `Record` at chunk `5184993` offsets `276-282`; context: He points to the exchange at the hearing which occurs at page 298 of the Certified Tribunal Record.
- Evidence: `reasoning_application` cue `applied` at chunk `5184993` offsets `37-44`; context: [23] The Applicant says that the RPD applied an incorrect test for torture, and that the transcript does not support the RPD’s finding that he admitted he was beaten but not tortured.

#### 25170:3:subtheme:5 · paragraphs 24-28

- Raw key terms: `applicant, says, tortured, unreasonable, provided, testified, based, conclusion`
- Display key terms: `says, tortured, unreasonable, provided, testified, based, conclusion`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: says, tortured, unreasonable, provided, testified, based, conclusion Application context: [24] The Applicant says that the RPD applied the wrong test for torture when it said that, if he had been tortured, he would have been very severely hurt. | [26] The Applicant says that it was unreasonable for the RPD to reject his testimony that he was tortured solely because he did not provide a medical report reflecting his injuries. Evidence spans paragraphs 24-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5184994` offsets `411-418`; context: 1:
For the purposes of this Convention, the term "torture" means any act by which severe pain or suffering, whether physical or mental, is intentionally inflicted on a person for such purposes as obtaining from him or a third person information or a confession, punishing him for an act he or a third person has committed or is suspected of having committed, or intimidating or coercing him or a third person, or for any reason based on discrimination of any kind, when such pain or suffering is inflicted by or at the instigation of or with the consent or acquiescence of a public official or other person acting in an official capacity.
- Evidence: `reasoning_application` cue `applied` at chunk `5184994` offsets `37-44`; context: [24] The Applicant says that the RPD applied the wrong test for torture when it said that, if he had been tortured, he would have been very severely hurt.
- Evidence: `evidence_fact` cue `testimony` at chunk `5184996` offsets `75-84`; context: [26] The Applicant says that it was unreasonable for the RPD to reject his testimony that he was tortured solely because he did not provide a medical report reflecting his injuries.
- Evidence: `reasoning_application` cue `because` at chunk `5184996` offsets `113-120`; context: [26] The Applicant says that it was unreasonable for the RPD to reject his testimony that he was tortured solely because he did not provide a medical report reflecting his injuries.
- Evidence: `evidence_fact` cue `evidence` at chunk `5184997` offsets `390-398`; context: This, he says, shows that the RPD’s conclusion he had not provided evidence documenting protests was unreasonable.
- Evidence: `reasoning_application` cue `therefore` at chunk `5184997` offsets `508-517`; context: These documents show his testimony was consistent with other evidence therefore the RPD should not have found him not credible.
- Evidence: `counterargument_limitation` cue `but` at chunk `5184998` offsets `729-732`; context: The Applicant also points out that he did not change his story between the Claim Form and his PIF, but only provided more details when he was given an opportunity to do so.

#### 25170:3:subtheme:6 · paragraphs 29-31

- Raw key terms: `applicant, says, canada, citizenship, claimant, decision, finding, immigration`
- Display key terms: `says, finding`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: says, finding Position/evidence statements: ) He argues that the RPD’s findings are based on mere speculation or conjecture as opposed to reasonable inference and the Decision should be quashed because the finding was not based on the evidence provided. Application context: ) He argues that the RPD’s findings are based on mere speculation or conjecture as opposed to reasonable inference and the Decision should be quashed because the finding was not based on the evidence provided. Operative outcome context: ) He argues that the RPD’s findings are based on mere speculation or conjecture as opposed to reasonable inference and the Decision should be quashed because the finding was not based on the evidence provided. Evidence spans paragraphs 29-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5184999` offsets `222-229`; context: The purpose of the POE interview is to assess whether the individual is eligible and/or admissible to initiate a refugee claim.
- Evidence: `party_position` cue `argues` at chunk `5185000` offsets `528-534`; context: ) He argues that the RPD’s findings are based on mere speculation or conjecture as opposed to reasonable inference and the Decision should be quashed because the finding was not based on the evidence provided.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185000` offsets `39-47`; context: [30] The Applicant says that the sworn evidence of a claimant should be presumed true unless specifically disbelieved on adequate grounds (see Armson v Canada (Minister of Citizenship and Immigration), [1989] FCJ No 800 (FCA); Alfonso v Canada (Minister of Citizenship and Immigration) 2007 FC 51; Singh v Canada (Minister of Citizenship and Immigration) 2006 FC 709; Mahmood v Canada (Minister of Citizenship and Immigration) 2005 FC 1526; and Hussein v Canada (Minister of Citizenship and Immigration), [1998] FCJ No 853.
- Evidence: `reasoning_application` cue `because` at chunk `5185000` offsets `673-680`; context: ) He argues that the RPD’s findings are based on mere speculation or conjecture as opposed to reasonable inference and the Decision should be quashed because the finding was not based on the evidence provided.
- Evidence: `disposition` cue `quashed` at chunk `5185000` offsets `665-672`; context: ) He argues that the RPD’s findings are based on mere speculation or conjecture as opposed to reasonable inference and the Decision should be quashed because the finding was not based on the evidence provided.

#### 25170:3:subtheme:7 · paragraphs 32-37

- Raw key terms: `evidence, applicant, found, based, credible, documentary, lack, reasonable`
- Display key terms: `based, credible, documentary, lack, reasonable`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: based, credible, documentary, lack, reasonable Rule/authority context: [33] The RPD was under an obligation to consider the evidence that it found was credible, but its reasons do not show that it did so. Application context: A tribunal must be careful when rendering a decision based on a lack of plausibility because refugee claimants come from diverse cultures, and actions which appear implausible when judged from Canadian standards might be Operative outcome context: The reasonable credibility finding was determinative, so this application should be dismissed. Evidence spans paragraphs 32-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5185002` offsets `30-36`; context: [32] In addition to the above issues, the RPD’s reasons do not clearly show why it found he was not credible.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185002` offsets `423-431`; context: , if the facts as presented are outside the realm of what could reasonably be expected, or where the documentary evidence demonstrates that the events could not have happened in the manner asserted by the claimant.
- Evidence: `reasoning_application` cue `because` at chunk `5185002` offsets `610-617`; context: A tribunal must be careful when rendering a decision based on a lack of plausibility because refugee claimants come from diverse cultures, and actions which appear implausible when judged from Canadian standards might be plausible when considered from within the claimant’s milieu.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185003` offsets `53-61`; context: [33] The RPD was under an obligation to consider the evidence that it found was credible, but its reasons do not show that it did so.
- Evidence: `governing_rule` cue `under` at chunk `5185003` offsets `17-22`; context: [33] The RPD was under an obligation to consider the evidence that it found was credible, but its reasons do not show that it did so.
- Evidence: `counterargument_limitation` cue `but` at chunk `5185003` offsets `90-93`; context: [33] The RPD was under an obligation to consider the evidence that it found was credible, but its reasons do not show that it did so.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185004` offsets `54-62`; context: [34] Finally, the Applicant says that the RPD ignored evidence put before it after the hearing which contained a copy of the money transfer and the Applicant’s father’s affidavit confirming that the Applicant had lacked the finances to leave Turkey earlier.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185005` offsets `100-108`; context: [35] The Respondent says that the Applicant’s submissions essentially ask the court to re-weigh the evidence.
- Evidence: `disposition` cue `dismissed` at chunk `5185005` offsets `369-378`; context: The reasonable credibility finding was determinative, so this application should be dismissed.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185006` offsets `136-144`; context: The RPD found the Applicant had not provided documentary evidence corroborating his torture allegation and his attendance at the demonstrations, and he had omitted significant details form his POE statement.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185007` offsets `37-45`; context: [37] Given the lack of corroborating evidence and the omission of any events after 1998 in the Claim Form, the RPD was not persuaded that the Applicant attended protests, demonstrations and Newroz celebrations after 1998 as alleged in his PIF.

#### 25170:3:subtheme:8 · paragraphs 38-47

- Raw key terms: `applicant, evidence, canada, credibility, immigration, claim, finding, minister`
- Display key terms: `credibility, finding`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: credibility, finding Position/evidence statements: The evidence before the RPD, including any post-hearing documentary evidence the Applicant submitted, only demonstrates that such events took place, and not the Applicant’s attendance. | The Respondent argues that as the finder of fact, it was open to the RPD to reject the Applicant’s explanation (Hevia v Canada (Minister of Citizenship and Immigration) 2010 FC 472 at paragraph 14; Sinan v Canada (Minist Application context: The RPD Did not Apply the Wrong Test for Torture | Without his testimony, which the RPD reasonably concluded was not credible, there was no evidence on which the RPD could conclude the Applicant had gone to the protests. Evidence spans paragraphs 38-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5185008` offsets `105-111`; context: [38] The Applicant has not overcome the RPD’s credibility concerns: his arguments focus on very specific issues and fail to take into account the evidence as a whole, which the RPD found to be insufficient.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185008` offsets `146-154`; context: [38] The Applicant has not overcome the RPD’s credibility concerns: his arguments focus on very specific issues and fail to take into account the evidence as a whole, which the RPD found to be insufficient.
- Evidence: `reasoning_application` cue `Apply` at chunk `5185008` offsets `389-394`; context: The RPD Did not Apply the Wrong Test for Torture
- Evidence: `issue` cue `issue` at chunk `5185009` offsets `13-18`; context: [39] On this issue, the Applicant has misinterpreted the RPD’s reasons, which were reasonable in light of the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185009` offsets `110-118`; context: [39] On this issue, the Applicant has misinterpreted the RPD’s reasons, which were reasonable in light of the evidence.
- Evidence: `party_position` cue `submitted` at chunk `5185010` offsets `226-235`; context: The evidence before the RPD, including any post-hearing documentary evidence the Applicant submitted, only demonstrates that such events took place, and not the Applicant’s attendance.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185010` offsets `29-37`; context: [40] There was no persuasive evidence before the RPD that the Applicant had participated in any of the events he described after 1998.
- Evidence: `reasoning_application` cue `conclude` at chunk `5185010` offsets `441-449`; context: Without his testimony, which the RPD reasonably concluded was not credible, there was no evidence on which the RPD could conclude the Applicant had gone to the protests.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185011` offsets `627-635`; context: The lack of corroborating evidence in the present case only acted to substantiate the adverse findings the RPD had already made.
- Evidence: `evidence_fact` cue `testimony` at chunk `5185012` offsets `151-160`; context: Differences between a claimant’s POE statements and testimony are enough to justify a negative credibility finding when the contradictions are central to the claim (see Cienfuegos v Canada (Minister of Citizenship and Immigration) 2009 FC 1262 at paragraphs 1, 20 and 21).
- Evidence: `party_position` cue `argues` at chunk `5185013` offsets `355-361`; context: The Respondent argues that as the finder of fact, it was open to the RPD to reject the Applicant’s explanation (Hevia v Canada (Minister of Citizenship and Immigration) 2010 FC 472 at paragraph 14; Sinan v Canada (Minister of Citizenship and Immigration) 2004 FC 87 at paragraph 10).
- Evidence: `evidence_fact` cue `evidence` at chunk `5185013` offsets `58-66`; context: [43] It was open to the RPD to consider this inconsistent evidence, and though the Applicant attempted to explain the inconsistency the RPD did not accept his explanations and provided reasons why: the Declaration was handwritten and signed, declaring it complete, true and correct, and a line was drawn across the blank space on the page.
- Evidence: `party_position` cue `submitted` at chunk `5185014` offsets `70-79`; context: [44] The Respondent also says that the RPD’s handling of the evidence submitted after the hearing is immaterial because the evidence speaks only to the Applicant’s delay in leaving Turkey, while the RPD concluded that the Applicant had fabricated elements of the story which went beyond delay in leaving.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185014` offsets `61-69`; context: [44] The Respondent also says that the RPD’s handling of the evidence submitted after the hearing is immaterial because the evidence speaks only to the Applicant’s delay in leaving Turkey, while the RPD concluded that the Applicant had fabricated elements of the story which went beyond delay in leaving.
- Evidence: `reasoning_application` cue `because` at chunk `5185014` offsets `112-119`; context: [44] The Respondent also says that the RPD’s handling of the evidence submitted after the hearing is immaterial because the evidence speaks only to the Applicant’s delay in leaving Turkey, while the RPD concluded that the Applicant had fabricated elements of the story which went beyond delay in leaving.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185016` offsets `1808-1816`; context: Also, there is no persuasive evidence before the panel that the claimant was not given sufficient space, time or the opportunity to complete his story at the POE as alleged.
- Evidence: `reasoning_application` cue `Because` at chunk `5185016` offsets `435-442`; context: Because he participated in these demonstrations, he was arrested, and verbally and physically abused, and tortured by the police in the year 1998.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5185016` offsets `689-697`; context: Although the claimant’s PIF narrative lists a number of incidents after 1998 when he was arrested and mistreated by the police after 1998, the claimant’s story given in his own handwriting at the POE does indicate that to be so after 1998.
- Evidence: `counterargument_limitation` cue `but` at chunk `5185017` offsets `164-167`; context: [47] As paragraph 9 of the Decision makes clear, the RPD says that the Applicant attempted to explain the absence of medical documents by admitting “he was beaten, but never tortured by the Turkish police while in detention, as alleged in his PIF narrative and the port of entry note (POE) documents.

#### 25170:3:subtheme:9 · paragraphs 48-50

- Raw key terms: `applicant, counsel, hearing, never, testimony, tortured, absence, accept`
- Display key terms: `hearing, never, testimony, tortured, absence, accept`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: hearing, never, testimony, tortured, absence, accept Application context: [49] When it comes to the Claim Form, the RPD again rejects counsel’s submission that this document makes it clear that the Applicant was tortured by the police several times as unreasonable because “in that document the Evidence spans paragraphs 48-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5185018` offsets `288-296`; context: But we have here a fundamental mistake of fact that is used to question the Applicant’s credibility regarding the absence of medical documents.
- Evidence: `evidence_fact` cue `record` at chunk `5185018` offsets `12-18`; context: [48] As the record shows, and as counsel for the Respondent had to concede in the hearing before me, the Applicant never said that he had not been tortured.
- Evidence: `reasoning_application` cue `because` at chunk `5185019` offsets `191-198`; context: [49] When it comes to the Claim Form, the RPD again rejects counsel’s submission that this document makes it clear that the Applicant was tortured by the police several times as unreasonable because “in that document the claimant failed to provide any dates indicating when he was arrested and tortured by the police and the claimant admitted he was never tortured by the police.
- Evidence: `evidence_fact` cue `testimony` at chunk `5185020` offsets `300-309`; context: Wu's statements at the POE and his testimony at the hearing, I accept that the Board should be careful not to place undue reliance on the POE statements.

#### 25170:3:subtheme:10 · paragraphs 51-56

- Raw key terms: `applicant, police, correct, explanation, serious, tortured, true, abused`
- Display key terms: `police, correct, explanation, serious, tortured, true, abused`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: police, correct, explanation, serious, tortured, true, abused Rule/authority context: What his signature on this document attests to is that he “[believes] it to be true and [knows] it is of the same force and effect as if made under oath. Application context: [52] In addition, the Applicant’s explanation is considered not reasonable by the RPD because the “claimant admitted he was never tortured by the police. | ” Torture is a serious word and, accordingly to all the evidence before the RPD, it happened to the Applicant. Evidence spans paragraphs 51-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5185021` offsets `222-229`; context: The purpose of the POE interview is to assess whether an individual is eligible and/or admissible to initiate a refugee claim.
- Evidence: `issue` cue `question` at chunk `5185022` offsets `484-492`; context: It is the RPD who says he was not tortured, based upon a very mistaken view of what torture is:
M: So why I am trying to ask you this question.
- Evidence: `reasoning_application` cue `because` at chunk `5185022` offsets `86-93`; context: [52] In addition, the Applicant’s explanation is considered not reasonable by the RPD because the “claimant admitted he was never tortured by the police.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185023` offsets `825-833`; context: ” Torture is a serious word and, accordingly to all the evidence before the RPD, it happened to the Applicant.
- Evidence: `reasoning_application` cue `accordingly` at chunk `5185023` offsets `802-813`; context: ” Torture is a serious word and, accordingly to all the evidence before the RPD, it happened to the Applicant.
- Evidence: `governing_rule` cue `under` at chunk `5185025` offsets `377-382`; context: What his signature on this document attests to is that he “[believes] it to be true and [knows] it is of the same force and effect as if made under oath.
- Evidence: `reasoning_application` cue `because` at chunk `5185026` offsets `316-323`; context: The claim for protection form indicates that the Applicant “was prosecuted and tortured by Turkish police many times because of my Kurdish identity.

#### 25170:3:subtheme:11 · paragraphs 57-58

- Raw key terms: `applicant, decision, else, everything, finding, tortured, admission, admitted`
- Display key terms: `else, everything, finding, tortured, admission, admitted`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: else, everything, finding, tortured, admission, admitted Application context: Because this finding underpins everything else in the Decision, it must be returned for reconsideration. Evidence spans paragraphs 57-58. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5185027` offsets `244-252`; context: An over-reliance on the Claim Form which, at question 49, tell applicants to “Please answer in few words.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185027` offsets `34-42`; context: [57] The finding that there is no evidence to support the Applicant’s post-1998 encounters with the police is crucial for everything else that follows in the Decision.
- Evidence: `reasoning_application` cue `Because` at chunk `5185028` offsets `120-127`; context: Because this finding underpins everything else in the Decision, it must be returned for reconsideration.

#### Section text

[15] The Applicant raises the following issues:
a. Whether the RPD erred in finding that he was not credible;
b. Whether the RPD applied the wrong test for torture;
c. Whether the RPD’s finding that he was tortured, was reasonable;
d. Whether the RPD’s reasons were inadequate.
STANDARD OF REVIEW

[16] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9, held that a standard of review analysis need not be conducted in every instance. Instead, where the standard of review applicable to a particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review. Only where this search proves fruitless must the reviewing court undertake a consideration of the four factors comprising the standard of review analysis.

[17] In Elmi v Canada (Minister of Citizenship and Immigration) 2008 FC 773, at paragraph 21, Justice Max Teitelbaum held that findings of credibility are central to the RPD’s finding of fact and are therefore to be evaluated on a standard of review of reasonableness. Further, in Hou v Canada (Minister of Citizenship and Immigration) 2005 FC 1586, Justice John O’Keefe held at paragraph 23 that the standard of review on a finding of credibility was patent unreasonableness. Also, in Aguebor v Canada (Minister of Citizenship and Immigration), [1993] FCJ No 732 (FCA) the Federal Court of Appeal held that the standard of review on a credibility finding is reasonableness. The standard of review on the first issue is reasonableness.

[18] In Suresh v Canada (Minister of Citizenship and Immigration) 2002 SCC 1, the Supreme Court of Canada held at paragraph 43 that torture includes
the unlawful use of psychological or physical techniques to intentionally inflict severe pain and suffering on another, when such pain or suffering is inflicted by or with the consent of public officials.

[19] The determination as to whether a particular act, such as the falaka the Applicant alleges, falls within the definition of torture approved by the Supreme Court of Canada calls for the application of the law to the facts before the RPD. As the Supreme Court of Canada held in Dunsmuir, above, at paragraph 51, this type of question will generally attract the standard of reasonableness. The standard of review on the second issue is reasonableness.

[20] Whether or not the Applicant was tortured in Turkey is purely a finding of fact. In Dunsmuir, above, at paragraph 51, the Supreme Court of Canada held that findings of fact will generally attract the reasonableness standard. The standard of review on the third issue is reasonableness.

[21] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.” See Dunsmuir, above, at paragraph 47, and Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at paragraph 59. Put another way, the Court should intervene only if the Decision was unreasonable in the sense that it falls outside the “range of possible, acceptable outcomes which are defensible in respect of the facts and law.”

[22] Recently, the Supreme Court of Canada held in Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board) 2011 SCC 62 that inadequacy of reasons does not provide a stand-alone basis for quashing a decision (see paragraph 14). The Supreme Court of Canada held that reasons are to be reviewed with the outcome as an organic exercise. The adequacy of reasons is therefore subsumed into the analysis of the reasonableness of the Decision as a whole.
ARGUMENTS
The Applicant
The RPD Applied the Wrong Test for Torture

[23] The Applicant says that the RPD applied an incorrect test for torture, and that the transcript does not support the RPD’s finding that he admitted he was beaten but not tortured. He points to the exchange at the hearing which occurs at page 298 of the Certified Tribunal Record.

[24] The Applicant says that the RPD applied the wrong test for torture when it said that, if he had been tortured, he would have been very severely hurt. He cites the Convention against Torture and other Cruel, Inhuman or Degrading Treatment or Punishment, December 10, 1984, [1987] Can TS No 36, Art. 1:
For the purposes of this Convention, the term "torture" means any act by which severe pain or suffering, whether physical or mental, is intentionally inflicted on a person for such purposes as obtaining from him or a third person information or a confession, punishing him for an act he or a third person has committed or is suspected of having committed, or intimidating or coercing him or a third person, or for any reason based on discrimination of any kind, when such pain or suffering is inflicted by or at the instigation of or with the consent or acquiescence of a public official or other person acting in an official capacity. It does not include pain or suffering arising only from, inherent in or incidental to lawful sanctions.

[25] The Applicant says that there is no requirement for a victim of torture to be severely hurt and have signs of torture. In this case, the Applicant testified that he was deprived of sleep and water, and subjected to falaka on several occasions. This was sufficient to meet the test for torture.
The RPD’s Finding the Applicant was not Tortured was Unreasonable.

[26] The Applicant says that it was unreasonable for the RPD to reject his testimony that he was tortured solely because he did not provide a medical report reflecting his injuries. He says he provided a reasonable explanation for his failure to present documentary evidence confirming his arrests and mistreatment by the police as he testified that he was too afraid of the police and that attending a hospital to record his injuries would have worsened his situation. He did not admit at the hearing that he was not tortured, this was the RPD’s statement, not his.
The RPD’s Credibility Finding was Unreasonable

[27] The Applicant also says that the RPD’s National Documentation Package for Turkey shows that many Kurds are arrested during demonstrations around Newroz celebrations. The documents he presented after the hearing also show that Newroz celebrations occurred around the time he says he was arrested, detained, and beaten. This, he says, shows that the RPD’s conclusion he had not provided evidence documenting protests was unreasonable. These documents show his testimony was consistent with other evidence therefore the RPD should not have found him not credible.

[28] The RPD’s conclusion he was not credible, based on the lack of detail in the Claim Form, was also unreasonable. The Applicant testified that at the time of his POE interview the immigration officer had told him that they would stop the intake of information until his brother confirmed their relationship. Though his brother provided the confirmation, the interview was not continued. The Applicant’s Claim Form indicates that he said “I was prosecuted (sic) and tortured by Turkish police many times,” not just during the 1998 event which was specifically mentioned in his handwritten narrative, completed at the same time. The Applicant also points out that he did not change his story between the Claim Form and his PIF, but only provided more details when he was given an opportunity to do so.

[29] The Applicant says that it is an error for the RPD to impugn a claimant’s credibility on the sole ground that the information provided at the POE interview lacks details. The purpose of the POE interview is to assess whether the individual is eligible and/or admissible to initiate a refugee claim. The POE statement is not a part of the claim itself and consequently should not be expected to contain all of the details of a claim. For this point, the Applicant relies on RKL v Canada (Minister of Citizenship and Immigration) 2003 FCT 116.

[30] The Applicant says that the sworn evidence of a claimant should be presumed true unless specifically disbelieved on adequate grounds (see Armson v Canada (Minister of Citizenship and Immigration), [1989] FCJ No 800 (FCA); Alfonso v Canada (Minister of Citizenship and Immigration) 2007 FC 51; Singh v Canada (Minister of Citizenship and Immigration) 2006 FC 709; Mahmood v Canada (Minister of Citizenship and Immigration) 2005 FC 1526; and Hussein v Canada (Minister of Citizenship and Immigration), [1998] FCJ No 853.) He argues that the RPD’s findings are based on mere speculation or conjecture as opposed to reasonable inference and the Decision should be quashed because the finding was not based on the evidence provided.

[31] He further says that the RPD misstated the facts in finding that he had delayed leaving Turkey for 10 years after the 1998 event. The Applicant testified that the 2008 incident was the first time that the police specifically threatened his life, and only after this event did he make the decision to leave the country.
The RPD’s Reasons Were Inadequate

[32] In addition to the above issues, the RPD’s reasons do not clearly show why it found he was not credible. In Valtchev v Canada (Minister of Citizenship and Immigration) 2001 FCT 776, Justice Francis Muldoon said, at paragraph 7, that
plausibility findings should be made only in the clearest of cases, i.e., if the facts as presented are outside the realm of what could reasonably be expected, or where the documentary evidence demonstrates that the events could not have happened in the manner asserted by the claimant. A tribunal must be careful when rendering a decision based on a lack of plausibility because refugee claimants come from diverse cultures, and actions which appear implausible when judged from Canadian standards might be plausible when considered from within the claimant’s milieu.

[33] The RPD was under an obligation to consider the evidence that it found was credible, but its reasons do not show that it did so. It failed to provide reasons for the conclusion that there is no objective basis for the Applicant’s claim. The Applicant also says that the RPD did not fulfill its obligation to explain why it disagreed with evidence that went against its conclusions. The RPD did not address in its reasons the country condition evidence he presented, so the reasons are inadequate.

[34] Finally, the Applicant says that the RPD ignored evidence put before it after the hearing which contained a copy of the money transfer and the Applicant’s father’s affidavit confirming that the Applicant had lacked the finances to leave Turkey earlier. The RPD failed to explain why it ignored this evidence or why it did not find it persuasive.
The Respondent

[35] The Respondent says that the Applicant’s submissions essentially ask the court to re-weigh the evidence. The RPD reasonably found that the Applicant was not credible based on the omissions from his POE statement, the lack of documentary evidence, and the delay in leaving Turkey. The reasonable credibility finding was determinative, so this application should be dismissed.
The RPD’s Credibility Finding was Reasonable

[36] The RPD’s credibility finding was reasonable based on what was before it. The RPD found the Applicant had not provided documentary evidence corroborating his torture allegation and his attendance at the demonstrations, and he had omitted significant details form his POE statement. The RPD also rejected the Applicant’s explanation for the omission from his POE statement. All of these findings were reasonable, so the RPD’s global credibility finding was also reasonable.

[37] Given the lack of corroborating evidence and the omission of any events after 1998 in the Claim Form, the RPD was not persuaded that the Applicant attended protests, demonstrations and Newroz celebrations after 1998 as alleged in his PIF. As a result, the RPD was not persuaded the police would be interested in the Applicant after 1998 and reasonably concluded that the Applicant’s fear of persecution had no objective basis. The Respondent notes that the RPD also concluded that the 10 year delay in leaving Turkey demonstrated that the Applicant did not have a subjective fear of persecution. The RPD reasonably rejected the Applicant’s explanation, and the conclusion drawn from the delay was reasonable.

[38] The Applicant has not overcome the RPD’s credibility concerns: his arguments focus on very specific issues and fail to take into account the evidence as a whole, which the RPD found to be insufficient. The RPD made its findings in clear unmistakable terms, as required by Hilo v Canada (Minister of Employment and Immigration), [1991] FCJ No 228 (FCA) at paragraph 6.
The RPD Did not Apply the Wrong Test for Torture

[39] On this issue, the Applicant has misinterpreted the RPD’s reasons, which were reasonable in light of the evidence. Given its concerns about his credibility, the RPD asked the Applicant for corroborating evidence. He provided none. The RPD concluded that the lack of corroborating evidence of torture further showed that the Applicant had embellished his claim, and this finding was reasonable in light of the evidence.

[40] There was no persuasive evidence before the RPD that the Applicant had participated in any of the events he described after 1998. The evidence before the RPD, including any post-hearing documentary evidence the Applicant submitted, only demonstrates that such events took place, and not the Applicant’s attendance. Without his testimony, which the RPD reasonably concluded was not credible, there was no evidence on which the RPD could conclude the Applicant had gone to the protests.

[41] The Respondent also says that a lack of acceptable documents without a reasonable explanation constitutes a significant factor in assessing the credibility of a claimant, and may lead to a finding that a claimant has not discharged the burden of his/her claim. The Respondent relies on Syed v Canada (Minister of Citizenship and Immigration), [1998] FCJ No 357; Bin v Canada (Minister of Citizenship and Immigration), 2001 FCT 1246; Nallanathan v Canada (Minister of Citizenship and Immigration), 2001 FCT 326; and Nadarajalingam v Canada (Minister of Citizenship and Immigration), 2001 FCT 444. The lack of corroborating evidence in the present case only acted to substantiate the adverse findings the RPD had already made.

[42] The omission from the Applicant’s Claim Form was not the sole basis for the RPD’s conclusion. Differences between a claimant’s POE statements and testimony are enough to justify a negative credibility finding when the contradictions are central to the claim (see Cienfuegos v Canada (Minister of Citizenship and Immigration) 2009 FC 1262 at paragraphs 1, 20 and 21).

[43] It was open to the RPD to consider this inconsistent evidence, and though the Applicant attempted to explain the inconsistency the RPD did not accept his explanations and provided reasons why: the Declaration was handwritten and signed, declaring it complete, true and correct, and a line was drawn across the blank space on the page. The Respondent argues that as the finder of fact, it was open to the RPD to reject the Applicant’s explanation (Hevia v Canada (Minister of Citizenship and Immigration) 2010 FC 472 at paragraph 14; Sinan v Canada (Minister of Citizenship and Immigration) 2004 FC 87 at paragraph 10).

[44] The Respondent also says that the RPD’s handling of the evidence submitted after the hearing is immaterial because the evidence speaks only to the Applicant’s delay in leaving Turkey, while the RPD concluded that the Applicant had fabricated elements of the story which went beyond delay in leaving.
ANALYSIS

[45] I believe there are several reviewable errors in the Decision that render it unreasonable and require that the matter be sent back for re-determination.

[46] First of all, the RPD makes significant use of the POE notes in arriving at its adverse credibility finding:
11. Furthermore, on July 22, 2009, during his interview with the immigration officer at the POE, the claimant provided reasons in his handwriting for making a refugee claim in Canada. His handwritten document indicates that, since 1997, he was attending demonstrations organised by the legal Kurdish civil organizations. Because he participated in these demonstrations, he was arrested, and verbally and physically abused, and tortured by the police in the year 1998. There are no other incidents mentioned by the claimant besides being detained and tortured until 1998.
12. Although the claimant’s PIF narrative lists a number of incidents after 1998 when he was arrested and mistreated by the police after 1998, the claimant’s story given in his own handwriting at the POE does indicate that to be so after 1998. His counsel submitted during the panel’s questioning that page 8 of the form filled at the POE indicates that he was prosecuted and tortured by the police several times. His counsel’s arguments are not reasonable since, in that document, the claimant failed to provide any dates indicating when he was arrested and tortured by the police and the claimant admitted he was never tortured by the police.
13. When asked to explain omissions in his handwritten story, the claimant blamed the immigration officer for taking his handwritten document before he completed his story on the first day of the interview. His explanation is not reasonable since the handwritten document was signed immediately after he completed his story and then a line was drawn across the page and his signature appears again indicating that he had completed his entire story. Also, there is no persuasive evidence before the panel that the claimant was not given sufficient space, time or the opportunity to complete his story at the POE as alleged. Moreover, at the end of that document, the claimant declared that the information, including his story given at the POE was complete, true and correct.
14. Therefore, based on the evidence adduced, the panel is not persuaded to believe that the claimant attended the protests, the demonstrations and the Newroz celebrations after 1998 as alleged in his PIF narrative and in his testimony. The panel finds that the claimant has fabricated these stories after his interview with the immigration officer at the POE.

[47] As paragraph 9 of the Decision makes clear, the RPD says that the Applicant attempted to explain the absence of medical documents by admitting “he was beaten, but never tortured by the Turkish police while in detention, as alleged in his PIF narrative and the port of entry note (POE) documents.”

[48] As the record shows, and as counsel for the Respondent had to concede in the hearing before me, the Applicant never said that he had not been tortured. I will come to his testimony in this regard later in these reasons. But we have here a fundamental mistake of fact that is used to question the Applicant’s credibility regarding the absence of medical documents.

[49] When it comes to the Claim Form, the RPD again rejects counsel’s submission that this document makes it clear that the Applicant was tortured by the police several times as unreasonable because “in that document the claimant failed to provide any dates indicating when he was arrested and tortured by the police and the claimant admitted he was never tortured by the police.”

[50] This Court has warned of the dangers of relying upon and using POE notes in this way. In Wu v Canada (Minister of Citizenship and Immigration) 2010 FC 1102, Justice O’Reilly said at paragraph 16:
With respect to the Board's reliance on differences between Mr. Wu's statements at the POE and his testimony at the hearing, I accept that the Board should be careful not to place undue reliance on the POE statements. The circumstances sur

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 25170:4 · paragraphs 59-69

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c397f7fd04849be968d570383b783dca9e6165daba94491aabbbfcc770a8b216`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25170:4:subtheme:1 · paragraphs 59-63

- Raw key terms: `evidence, applicant, celebrations, newroz, police, allegedly, arrested, even`
- Display key terms: `celebrations, newroz, police, allegedly, arrested, even`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: celebrations, newroz, police, allegedly, arrested, even Position/evidence statements: These documents are central and material to the claimant’s claim. Application context: Therefore, based on the evidence adduced, the claimant has not persuasively established that he attended the demonstrations, the protests and the Newroz celebrations after 1998 as alleged. | Although the events were relatively peaceful this year (2007), tensions were high because of the arrests and persecution of dozens of pro-Kurdish politicians, on charges of ties to PKK rebels. Evidence spans paragraphs 59-63. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5185029` offsets `1460-1468`; context: In question 31 in his PIF and on the RPD Screening Form, the claimant was instructed to provide documentary evidence to establish his claim.
- Evidence: `party_position` cue `claim` at chunk `5185029` offsets `662-667`; context: These documents are central and material to the claimant’s claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185029` offsets `266-274`; context: Even if the panel believed that the claimant participated in demonstrations, protests and Newroz celebrations after 1998 (which the panel does not), at the hearing the claimant did not provide any documentary evidence such as hospital records to indicate that he was mistreated and tortured by the police when he was detained by the police after 1998.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5185029` offsets `2221-2230`; context: Therefore, based on the evidence adduced, the claimant has not persuasively established that he attended the demonstrations, the protests and the Newroz celebrations after 1998 as alleged.
- Evidence: `counterargument_limitation` cue `although` at chunk `5185029` offsets `878-886`; context: When asked to explain why he failed to provide documentary evidence to corroborate his claim at the hearing, the claimant admitted that he did not seek medical attention since there was no sign of torture although in his PIF narrative and in his POE documents he mentioned that he was tortured by the police.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185030` offsets `78-86`; context: [60] The RPD also stated that the Applicant failed to provide any documentary evidence such as media reports to indicate that the alleged protests, when he was allegedly arrested, took place on the days the Applicant participated and Kurdish people were arrested for being in the protests.
- Evidence: `counterargument_limitation` cue `However` at chunk `5185030` offsets `290-297`; context: However, the National Documentation package contains evidence demonstrating that every year during Newroz celebrations many Kurdish people are arrested by the police as Kurdish supporters.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185031` offsets `92-100`; context: The evidence demonstrates that:
Newroz day has become a platform for Turkey’s Kurdish minority to demand greater freedoms or demonstrate support for the outlawed Kurdish Worker’s Party.
- Evidence: `reasoning_application` cue `because` at chunk `5185031` offsets `524-531`; context: Although the events were relatively peaceful this year (2007), tensions were high because of the arrests and persecution of dozens of pro-Kurdish politicians, on charges of ties to PKK rebels.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5185031` offsets `442-450`; context: Although the events were relatively peaceful this year (2007), tensions were high because of the arrests and persecution of dozens of pro-Kurdish politicians, on charges of ties to PKK rebels.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185032` offsets `77-85`; context: [62] At paragraph 18 of the Decision, the RPD admitted that the post-hearing evidence does indicate that Newroz Celebrations happened at the same time the Applicant was allegedly arrested by the police.
- Evidence: `counterargument_limitation` cue `However` at chunk `5185032` offsets `203-210`; context: However, the RPD stated that there is no evidence that the Applicant participated in those celebrations and was arrested, detained and mistreated by the police.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185033` offsets `109-117`; context: [63] It is my view, however, that the Applicant provided a reasonable explanation for his failure to present evidence confirming his arrest and mistreatment by the police.
- Evidence: `reasoning_application` cue `because` at chunk `5185033` offsets `371-378`; context: He stated that he was too afraid to go to the hospital to record his injuries after detention because he would have to complain about the actions of the police.

#### 25170:4:subtheme:2 · paragraphs 64-68

- Raw key terms: `evidence, applicant, canada, failed, turkey, address, allegations, because`
- Display key terms: `failed, turkey, address, allegations, because`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: failed, turkey, address, allegations, because Position/evidence statements: [65] In my view, the Applicant’s testimony was entirely consistent with documentary evidence he submitted and in the National Documentation Package. | [68] Also, the failure of the RPD to appropriately address the Applicant’s evidence with regard to the detentions and torture he suffered after 1998 and up to 2008 when he decided to leave and come to Canada, means that  Rule/authority context: Legal amendments since 2005, along with case law since 2008, allowed courts in Turkey to convict demonstrators under the harshest terrorism laws… The vast majority of demonstrators currently being prosecuted under terror | The RPD was under obligation to explain why it ignored evidence which corroborated the Applicant’s allegations. Application context: Then the defendant, by joining the demonstration, is assumed to have acted directly under PKK orders… In fact, demonstrators may be punished more harshly, because while combatants who turn themselves in may receive parti | The Applicant testified that he was detained on the basis of his Kurdish nationality and because he was participating in cultural events (Newroz celebration and a Kurdish wedding). Operative outcome context: Legal amendments since 2005, along with case law since 2008, allowed courts in Turkey to convict demonstrators under the harshest terrorism laws… The vast majority of demonstrators currently being prosecuted under terror Evidence spans paragraphs 64-68. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5185034` offsets `1752-1758`; context: The General Penal Board of the Court of Cassation has held that it is sufficient to show that sympathetic media outlets broadcast the PKK’s “appeals”-speeches by the PKK leadership, calling on the Kurdish population to protest or raise their voices on various issues.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185034` offsets `22-30`; context: [64] The post-hearing evidence demonstrates that, in Turkey, it is a usual practice to arrest members of the Kurdish minority simply for participating in demonstrations or a cultural celebration.
- Evidence: `governing_rule` cue `under` at chunk `5185034` offsets `591-596`; context: Legal amendments since 2005, along with case law since 2008, allowed courts in Turkey to convict demonstrators under the harshest terrorism laws…
The vast majority of demonstrators currently being prosecuted under terrorism law is Kurdish, and the laws are usually invoked in the mainly Kurdish-populated areas of southeast Turkey, or in Adana and Mersin and other cities with large Kurdish populations…
While many of prosecutions discussed in this report involve allegations of stone-throwing or tire-burning at demonstrations, the government’s increasingly harsh punishment of Kurdish demonstrators does not appear to be response to demonstrators’ violent acts, but rather to their perceived ideological support for the PKK….
- Evidence: `reasoning_application` cue `because` at chunk `5185034` offsets `1915-1922`; context: Then the defendant, by joining the demonstration, is assumed to have acted directly under PKK orders…
In fact, demonstrators may be punished more harshly, because while combatants who turn themselves in may receive partial amnesty under the “Effective Repentance” provision in the Turkish Penal Code, there is no such provision to reduce the sentences of peaceful demonstrators who have never taken up arms.
- Evidence: `disposition` cue `allowed` at chunk `5185034` offsets `541-548`; context: Legal amendments since 2005, along with case law since 2008, allowed courts in Turkey to convict demonstrators under the harshest terrorism laws…
The vast majority of demonstrators currently being prosecuted under terrorism law is Kurdish, and the laws are usually invoked in the mainly Kurdish-populated areas of southeast Turkey, or in Adana and Mersin and other cities with large Kurdish populations…
While many of prosecutions discussed in this report involve allegations of stone-throwing or tire-burning at demonstrations, the government’s increasingly harsh punishment of Kurdish demonstrators does not appear to be response to demonstrators’ violent acts, but rather to their perceived ideological support for the PKK….
- Evidence: `party_position` cue `submitted` at chunk `5185035` offsets `96-105`; context: [65] In my view, the Applicant’s testimony was entirely consistent with documentary evidence he submitted and in the National Documentation Package.
- Evidence: `evidence_fact` cue `testimony` at chunk `5185035` offsets `33-42`; context: [65] In my view, the Applicant’s testimony was entirely consistent with documentary evidence he submitted and in the National Documentation Package.
- Evidence: `reasoning_application` cue `because` at chunk `5185035` offsets `238-245`; context: The Applicant testified that he was detained on the basis of his Kurdish nationality and because he was participating in cultural events (Newroz celebration and a Kurdish wedding).
- Evidence: `evidence_fact` cue `evidence` at chunk `5185036` offsets `55-63`; context: [66] While a tribunal need not refer to every piece of evidence presented, the more significant a piece of evidence is, the more likely it is that a failure to make reference to it will result in a finding that the Decision was unreasonable, especially when it appears to be a marked contradiction to a finding of the RPD.
- Evidence: `governing_rule` cue `under` at chunk `5185036` offsets `335-340`; context: The RPD was under obligation to explain why it ignored evidence which corroborated the Applicant’s allegations.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185037` offsets `143-151`; context: [67] The RPD rejected the Applicant’s explanation that he lacked finances to leave Turkey, and stated that there was no persuasive documentary evidence in the form of a bank statement or affidavit from his father to indicate that the Applicant used his brother’s money to leave Turkey.
- Evidence: `counterargument_limitation` cue `However` at chunk `5185037` offsets `286-293`; context: However, the post-hearing evidence contains a copy of the money transfer and the Applicant’s father’s affidavit confirming the Applicant’s testimony.
- Evidence: `party_position` cue `assert` at chunk `5185038` offsets `255-261`; context: [68] Also, the failure of the RPD to appropriately address the Applicant’s evidence with regard to the detentions and torture he suffered after 1998 and up to 2008 when he decided to leave and come to Canada, means that it was unreasonable for the RPD to assert that there was a delay of 10 years before the Applicant came to Canada.
- Evidence: `evidence_fact` cue `evidence` at chunk `5185038` offsets `75-83`; context: [68] Also, the failure of the RPD to appropriately address the Applicant’s evidence with regard to the detentions and torture he suffered after 1998 and up to 2008 when he decided to leave and come to Canada, means that it was unreasonable for the RPD to assert that there was a delay of 10 years before the Applicant came to Canada.

#### 25170:4:subtheme:3 · paragraphs 69-69

- Raw key terms: `agree, certification, concurs, counsel, court, question`
- Display key terms: `agree, certification, concurs, question`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: agree, certification, concurs, question Evidence spans paragraphs 69-69. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5185039` offsets `31-39`; context: [69] Counsel agree there is no question for certification and the Court concurs.

#### Section text

[59] The RPD goes on to make an alternative finding:
15. Even if the panel believed that the claimant participated in demonstrations, protests and Newroz celebrations after 1998 (which the panel does not), at the hearing the claimant did not provide any documentary evidence such as hospital records to indicate that he was mistreated and tortured by the police when he was detained by the police after 1998. He also did not provide media reports to indicate that the demonstrations, the protests that he allegedly attended took place on the days he was allegedly arrested and mistreated by the police. These documents are central and material to the claimant’s claim.
16. When asked to explain why he failed to provide documentary evidence to corroborate his claim at the hearing, the claimant admitted that he did not seek medical attention since there was no sign of torture although in his PIF narrative and in his POE documents he mentioned that he was tortured by the police.
17. The claimant’s wife’s affidavit does not provide details of the events the claimant allegedly attended and was arrested by the police. Although documentary evidence does indicate the murder of a Turkish-American journalist on January 19, 2007, there is no documentary evidence including his wife’s affidavit that indicates that the claimant attended that demonstration which ended in the killing of the journalist.
18. The onus is on the claimant to establish his claim. In question 31 in his PIF and on the RPD Screening Form, the claimant was instructed to provide documentary evidence to establish his claim. He had ample time to obtain documentary evidence prior to the hearing to establish his claim. His failure to provide, at the hearing, persuasive documentary evidence regarding the demonstrations, the protests and the Newroz celebrations he allegedly attended raises a serious disbelief in the panel’s mind as to whether the claimant participated in those events. Counsel’s post-hearing documents do indicate Newroz celebrations when the claimant was allegedly arrested by the police, but they do not indicate that the claimant participated in those celebrations and was arrested, detained and mistreated by the police.
19. Therefore, based on the evidence adduced, the claimant has not persuasively established that he attended the demonstrations, the protests and the Newroz celebrations after 1998 as alleged. As a result, the panel disbelieves that the claimant attended the events he alleges he attended after 1998. The panel finds that the claimant has fabricated his story about participating in demonstrations, protests and Newroz celebrations after 1998 to bolster his refugee claim.

[60] The RPD also stated that the Applicant failed to provide any documentary evidence such as media reports to indicate that the alleged protests, when he was allegedly arrested, took place on the days the Applicant participated and Kurdish people were arrested for being in the protests. However, the National Documentation package contains evidence demonstrating that every year during Newroz celebrations many Kurdish people are arrested by the police as Kurdish supporters. Even without the Applicant’s submissions, there was reliable evidence before the RPD confirming what he said.

[61] Applicant’s counsel provided post-hearing documents regarding Newroz Celebrations. The evidence demonstrates that:
Newroz day has become a platform for Turkey’s Kurdish minority to demand greater freedoms or demonstrate support for the outlawed Kurdish Worker’s Party. (Page 203 of the CTR)
Newroz is celebrated largely by the country’s Kurdish population, and past celebrations have ended in riot’s [that have] claimed dozens of lives. Although the events were relatively peaceful this year (2007), tensions were high because of the arrests and persecution of dozens of pro-Kurdish politicians, on charges of ties to PKK rebels. (Page 208 of the CTR)

[62] At paragraph 18 of the Decision, the RPD admitted that the post-hearing evidence does indicate that Newroz Celebrations happened at the same time the Applicant was allegedly arrested by the police. However, the RPD stated that there is no evidence that the Applicant participated in those celebrations and was arrested, detained and mistreated by the police.

[63] It is my view, however, that the Applicant provided a reasonable explanation for his failure to present evidence confirming his arrest and mistreatment by the police. The Applicant testified on many occasions that he is afraid of the police and security forces in Turkey. He stated that he was too afraid to go to the hospital to record his injuries after detention because he would have to complain about the actions of the police. He was sure that this made his position even worse. The RPD does not explain why this is not a reasonable explanation.

[64] The post-hearing evidence demonstrates that, in Turkey, it is a usual practice to arrest members of the Kurdish minority simply for participating in demonstrations or a cultural celebration. A Human Rights Watch report dated November 2010 states that
In Turkey, many hundreds of people currently face prosecution, or are serving substantial sentences for terrorism convictions. Their “crime” was to engage in peaceful protest, or to throw stones or burn a tire at a protest. Legal amendments since 2005, along with case law since 2008, allowed courts in Turkey to convict demonstrators under the harshest terrorism laws…
The vast majority of demonstrators currently being prosecuted under terrorism law is Kurdish, and the laws are usually invoked in the mainly Kurdish-populated areas of southeast Turkey, or in Adana and Mersin and other cities with large Kurdish populations…
While many of prosecutions discussed in this report involve allegations of stone-throwing or tire-burning at demonstrations, the government’s increasingly harsh punishment of Kurdish demonstrators does not appear to be response to demonstrators’ violent acts, but rather to their perceived ideological support for the PKK….
The festival of Newroz…often elicited demonstration as well as cultural celebrations.
The Turkish courts considered no obstacle to a conviction that the prosecution has failed to provide evidence of the defendant’s specific intent to support or aid the illegal activities of the PKK. The General Penal Board of the Court of Cassation has held that it is sufficient to show that sympathetic media outlets broadcast the PKK’s “appeals”-speeches by the PKK leadership, calling on the Kurdish population to protest or raise their voices on various issues. Then the defendant, by joining the demonstration, is assumed to have acted directly under PKK orders…
In fact, demonstrators may be punished more harshly, because while combatants who turn themselves in may receive partial amnesty under the “Effective Repentance” provision in the Turkish Penal Code, there is no such provision to reduce the sentences of peaceful demonstrators who have never taken up arms. As a result, peaceful demonstrators with no clear PKK affiliation may be punished more harshly than PKK members who have actually served as guerrilla fighters.

[65] In my view, the Applicant’s testimony was entirely consistent with documentary evidence he submitted and in the National Documentation Package. The Applicant testified that he was detained on the basis of his Kurdish nationality and because he was participating in cultural events (Newroz celebration and a Kurdish wedding). He stated that he was detained and accused of “Kurdish propaganda.” He also stated that in 2008 the police told him that if they see him again at the demonstrations they would not let him go anywhere. 2008 is the year when the Turkish courts approved harsh punishment for people who were “suspected” of being PKK supporters. His life was also threatened in 2008. These were the crucial events that caused him to flee to Canada, not the 1998 encounter with the police when he was tortured.

[66] While a tribunal need not refer to every piece of evidence presented, the more significant a piece of evidence is, the more likely it is that a failure to make reference to it will result in a finding that the Decision was unreasonable, especially when it appears to be a marked contradiction to a finding of the RPD. The RPD was under obligation to explain why it ignored evidence which corroborated the Applicant’s allegations. In my view, the RPD failed to address the country evidence presented by the Applicant and its own National Documentation Package. See Cepeda-Gutierrez v Canada (Minister of Citizenship and Immigration), [1998] FCJ No 1425 and Manitas Vargas v Canada (Minister of Citizenship and Immigration) 2011 FC 543.

[67] The RPD rejected the Applicant’s explanation that he lacked finances to leave Turkey, and stated that there was no persuasive documentary evidence in the form of a bank statement or affidavit from his father to indicate that the Applicant used his brother’s money to leave Turkey. However, the post-hearing evidence contains a copy of the money transfer and the Applicant’s father’s affidavit confirming the Applicant’s testimony. The RPD failed to explain why it ignored this evidence, or why it did not find it persuasive.

[68] Also, the failure of the RPD to appropriately address the Applicant’s evidence with regard to the detentions and torture he suffered after 1998 and up to 2008 when he decided to leave and come to Canada, means that it was unreasonable for the RPD to assert that there was a delay of 10 years before the Applicant came to Canada. The Applicant testified that it was only in 2008 that the police threatened his life. After this, he left the country at the first available opportunity. In the end, the RPD’s assertion of a 10-year delay in leaving Turkey is a mistake of fact that renders the Decision unreasonable.

[69] Counsel agree there is no question for certification and the Court concurs.


## 25170:5 · paragraphs 70-71

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e6e3fc21e635d4d2c5377cdbb4d3ab98146ba2d9cb10e22aba93fa100eca231f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25170:5:subtheme:1 · paragraphs 70-71

- Raw key terms: `allowed, application, cause, certification, cetinkaya, citizenship, constituted, counsel`
- Display key terms: `allowed, certification, cetinkaya, constituted`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: allowed, certification, cetinkaya, constituted No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 70-71. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that
1. The application is allowed. The decision is quashed and returned for reconsideration by a differently constituted RPD.
2. There is no question for certification.
“James Russell”
Judge
FEDERAL COURT
NAME OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-3362-11

STYLE OF CAUSE: ERCAN CETINKAYA
- and -
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: December 8, 2011
REASONS FOR 

## 25170:6 · paragraphs 72-72

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `406c900609901c911d5ce382b7ea0a18f5b29395fb78ee6b6c71abcca36986ce`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25170:6:subtheme:1 · paragraphs 72-72

- Raw key terms: `alla, appearances, applicant, attorney, barrister, canada, dated, deputy`
- Display key terms: `alla, barrister, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: alla, barrister, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 72-72. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: HON. MR. JUSTICE RUSSELL
DATED: January 4, 2012
APPEARANCES:
Alla Kikinova APPLICANT
Julie Waldman RESPONDENT
SOLICITORS OF RECORD:
MICHAEL LOEBACH APPLICANT
Barrister & Solicitor
London, Ontario
Myles J. Kirvan, Q.C. RESPONDENT
Deputy Attorney General of Canada
