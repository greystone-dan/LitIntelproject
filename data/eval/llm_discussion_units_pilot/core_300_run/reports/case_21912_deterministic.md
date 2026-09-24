# Discussion Units: case 21912

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **41**
- Continuity pairs: **40**
- Discussion Units: **3**
- Paragraph source hashes: **41**
- Sub-themes: **11**

## 21912:1 · paragraphs 0-36

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `503815f4777d536a9ef0448e7578956d285853c9ec5aa4db09b15f60c9776215`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21912:1:subtheme:1 · paragraphs 0-9

- Raw key terms: `applicants, mexico, police, board, decision, canada, luisa, maria`
- Display key terms: `mexico, police, luisa, maria`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: mexico, police, luisa, maria Position/evidence statements: [5] The applicants claimed asylum in Canada as persons in need of refugee protection pursuant to sections 96 and 97 of the Act. Rule/authority context: [1] This is an application for judicial review pursuant to section 72 of the Immigration and Refugee Protection Act, S. | [5] The applicants claimed asylum in Canada as persons in need of refugee protection pursuant to sections 96 and 97 of the Act. Application context: The applicants did not report the above threats to the police and did not seek help from any state protection agency in Mexico reasoning that they were afraid because the police were corrupt and some were members of the  Evidence spans paragraphs 0-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5027596` offsets `47-58`; context: [1] This is an application for judicial review pursuant to section 72 of the Immigration and Refugee Protection Act, S.
- Evidence: `party_position` cue `claimed` at chunk `5027600` offsets `19-26`; context: [5] The applicants claimed asylum in Canada as persons in need of refugee protection pursuant to sections 96 and 97 of the Act.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5027600` offsets `85-96`; context: [5] The applicants claimed asylum in Canada as persons in need of refugee protection pursuant to sections 96 and 97 of the Act.
- Evidence: `reasoning_application` cue `because` at chunk `5027600` offsets `287-294`; context: The applicants did not report the above threats to the police and did not seek help from any state protection agency in Mexico reasoning that they were afraid because the police were corrupt and some were members of the mafia.
- Evidence: `evidence_fact` cue `evidence` at chunk `5027602` offsets `53-61`; context: [7] In its ten-page decision, the Board reviewed the evidence as presented.
- Evidence: `governing_rule` cue `under` at chunk `5027604` offsets `278-283`; context: However, the documentation showed that anti-drug and anti-corruption activities and efforts were made under the initiative of former President Fox and intensified by President Calderon, which led to federal and local officials and security personnel being arrested and prosecuted for criminal activities.
- Evidence: `counterargument_limitation` cue `However` at chunk `5027604` offsets `176-183`; context: However, the documentation showed that anti-drug and anti-corruption activities and efforts were made under the initiative of former President Fox and intensified by President Calderon, which led to federal and local officials and security personnel being arrested and prosecuted for criminal activities.

#### 21912:1:subtheme:2 · paragraphs 10-11

- Raw key terms: `applicants, board, issues, presumption, protection, state, viable, alternative`
- Display key terms: `issues, presumption, protection, state, viable, alternative`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: issues, presumption, protection, state, viable, alternative Evidence spans paragraphs 10-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5027605` offsets `311-317`; context: The issues
- Evidence: `evidence_fact` cue `found that` at chunk `5027605` offsets `178-188`; context: The Board also found that there was a viable Internal Flight Alternative (“IFA”) to other cities where the applicants could have relocated.
- Evidence: `issue` cue `issues` at chunk `5027606` offsets `59-65`; context: [11] The applicants raised what I consider to be secondary issues (which I will deal with briefly later).
- Evidence: `counterargument_limitation` cue `However` at chunk `5027606` offsets `106-113`; context: However, I believe the central issue is: “Did the Board err in finding that the applicants were not persons in need of protection?

#### 21912:1:subtheme:3 · paragraphs 12-16

- Raw key terms: `board, evidence, case, corruption, police, state, analysis, applicants`
- Display key terms: `case, corruption, police, state, analysis`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: case, corruption, police, state, analysis Position/evidence statements: [13] The applicants argue that the Board could not use case law to prove particular facts in a particular case such as the situation in Mexico. Rule/authority context: [14] I agree with the respondent that the jurisprudence can form a basis of consideration by a court about general conditions in a country as determined by the jurisprudence without excluding evidence to show change in t | [15] In summary, I believe the Board had the right to invoke the jurisprudence involved, but I do not follow the applicants’ reasoning that the Board did in fact disregard the particular circumstances of their case. Evidence spans paragraphs 12-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5027607` offsets `13-19`; context: [12] The sub-issues raised were: A.
- Evidence: `evidence_fact` cue `evidence` at chunk `5027607` offsets `265-273`; context: Did the Board ignore pertinent evidence about police corruption?
- Evidence: `party_position` cue `argue` at chunk `5027608` offsets `20-25`; context: [13] The applicants argue that the Board could not use case law to prove particular facts in a particular case such as the situation in Mexico.
- Evidence: `evidence_fact` cue `evidence` at chunk `5027608` offsets `230-238`; context: The respondent agrees with this proposition; however, he submits that the documentary evidence concerning the general situation in Mexico relating to the state agencies, the police, the problems with corruption and drug trafficking and efforts to combat these problems can be considered in a case such as the one presented here.
- Evidence: `counterargument_limitation` cue `however` at chunk `5027608` offsets `189-196`; context: The respondent agrees with this proposition; however, he submits that the documentary evidence concerning the general situation in Mexico relating to the state agencies, the police, the problems with corruption and drug trafficking and efforts to combat these problems can be considered in a case such as the one presented here.
- Evidence: `evidence_fact` cue `evidence` at chunk `5027609` offsets `192-200`; context: [14] I agree with the respondent that the jurisprudence can form a basis of consideration by a court about general conditions in a country as determined by the jurisprudence without excluding evidence to show change in these conditions.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5027609` offsets `42-55`; context: [14] I agree with the respondent that the jurisprudence can form a basis of consideration by a court about general conditions in a country as determined by the jurisprudence without excluding evidence to show change in these conditions.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5027610` offsets `65-78`; context: [15] In summary, I believe the Board had the right to invoke the jurisprudence involved, but I do not follow the applicants’ reasoning that the Board did in fact disregard the particular circumstances of their case.
- Evidence: `evidence_fact` cue `evidence` at chunk `5027611` offsets `182-190`; context: The Board ignored pertinent evidence about police corruption

#### 21912:1:subtheme:4 · paragraphs 17-20

- Raw key terms: `decision, made, board, country, error, factual, former, particular`
- Display key terms: `made, country, error, factual, former, particular`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: made, country, error, factual, former, particular Rule/authority context: [17] In its decision the Board referred at length to general documentation and case-law on the question of police and agency corruption and the efforts made by the state under former President Fox and later intensified b | The standard of review Application context: Therefore this argument fails. | This factual mistake is insufficient to change any important issue or decision and therefore has no bearing in the decision which, as we shall see, turns upon the lack of working state protection and IFA. Evidence spans paragraphs 17-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5027612` offsets `95-103`; context: [17] In its decision the Board referred at length to general documentation and case-law on the question of police and agency corruption and the efforts made by the state under former President Fox and later intensified by President Calderon.
- Evidence: `governing_rule` cue `under` at chunk `5027612` offsets `170-175`; context: [17] In its decision the Board referred at length to general documentation and case-law on the question of police and agency corruption and the efforts made by the state under former President Fox and later intensified by President Calderon.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5027612` offsets `242-251`; context: Therefore this argument fails.
- Evidence: `issue` cue `issue` at chunk `5027613` offsets `367-372`; context: This factual mistake is insufficient to change any important issue or decision and therefore has no bearing in the decision which, as we shall see, turns upon the lack of working state protection and IFA.
- Evidence: `evidence_fact` cue `testimony` at chunk `5027613` offsets `208-217`; context: This is correct since the applicant admitted in his testimony that he did not denunciate the attack of May 16, 2007 or the threats of March 15, 2007.
- Evidence: `reasoning_application` cue `therefore` at chunk `5027613` offsets `389-398`; context: This factual mistake is insufficient to change any important issue or decision and therefore has no bearing in the decision which, as we shall see, turns upon the lack of working state protection and IFA.
- Evidence: `governing_rule` cue `standard of review` at chunk `5027614` offsets `3566-3584`; context: The standard of review
- Evidence: `reasoning_application` cue `because` at chunk `5027614` offsets `1101-1108`; context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.

#### 21912:1:subtheme:5 · paragraphs 21-23

- Raw key terms: `questions, standard, canada, citizenship, immigration, minister, reasonableness, acceptable`
- Display key terms: `questions, standard, reasonableness, acceptable`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: questions, standard, reasonableness, acceptable Evidence spans paragraphs 21-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5027616` offsets `443-450`; context: In judicial review, reasonableness is concerned mostly with “the existence of justification, transparency and intelligibility within the decision-making process” and “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, supra, at paragraph 47).

#### 21912:1:subtheme:6 · paragraphs 24-24

- Raw key terms: `applicants, board, concluding, discussion, elaborated, issue, protection, rendered`
- Display key terms: `concluding, discussion, elaborated, protection, rendered`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: concluding, discussion, elaborated, protection, rendered Evidence spans paragraphs 24-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5027619` offsets `56-61`; context: [24] The Board rendered an elaborated discussion of the issue of state protection concluding that the applicants had not sought state protection.

#### 21912:1:subtheme:7 · paragraphs 25-33

- Raw key terms: `immigration, minister, canada, citizenship, protection, state, paragraph, seek`
- Display key terms: `protection, state, paragraph, seek`
- Argument roles: `evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, party_position, reasoning_application Display terms: protection, state, paragraph, seek Position/evidence statements: When adequate protection exists, a claimant cannot claim an objective well-founded fear of persecution (Sarker v. | [29] The applicants submit that the Board in the present case did not refer to or meet this test. Application context: Therefore, refugee protection is not available when the claimant has not made an attempt or made an adequate attempt to first seek state protection in his home country (Ward, supra, at page 724; Hinzman v. Evidence spans paragraphs 25-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claim` at chunk `5027620` offsets `849-854`; context: When adequate protection exists, a claimant cannot claim an objective well-founded fear of persecution (Sarker v.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5027620` offsets `511-520`; context: Therefore, refugee protection is not available when the claimant has not made an attempt or made an adequate attempt to first seek state protection in his home country (Ward, supra, at page 724; Hinzman v.
- Evidence: `evidence_fact` cue `evidence` at chunk `5027621` offsets `113-121`; context: [26] To rebut the presumption of state protection, the claimant must establish relevant, reliable and convincing evidence which satisfies the trier of fact on a balance of probabilities that the state protection is inadequate (Flores Carrillo v.
- Evidence: `evidence_fact` cue `evidence` at chunk `5027622` offsets `716-724`; context: It is recognized in documentary evidence that Mexico still has extensive problems such as state and police corruption, prevalent crime and drug trafficking but it is making efforts to cope with them (De Leon v.
- Evidence: `party_position` cue `submit` at chunk `5027624` offsets `20-26`; context: [29] The applicants submit that the Board in the present case did not refer to or meet this test.

#### 21912:1:subtheme:8 · paragraphs 34-35

- Raw key terms: `board, case, analyzed, applicants, canada, city, claimant, concluding`
- Display key terms: `case, analyzed, city, concluding`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: case, analyzed, city, concluding Evidence spans paragraphs 34-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5027629` offsets `317-324`; context: ), proposes a two-pronged test for a potential IFA: (a) the Board must be satisfied that there is no serious persecution or danger in the city where the IFA is located; and (b) the Board must consider whether the claimant can reasonably, without undue hardship, seek refuge in that city.
- Evidence: `evidence_fact` cue `evidence` at chunk `5027630` offsets `104-112`; context: [35] The Board in this case has analyzed the applicants’ reasons in their opposition to the IFA and the evidence which is quasi-totally speculative, concluding an IFA was open to the applicants.

#### 21912:1:subtheme:9 · paragraphs 36-36

- Raw key terms: `acceptable, based, board, dunsmuir, facts, fall, findings, issue`
- Display key terms: `acceptable, based, dunsmuir, facts, fall, findings`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: acceptable, based, dunsmuir, facts, fall, findings Evidence spans paragraphs 36-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5027631` offsets `80-85`; context: [36] In my view, both findings of the Board on the state protection and the IFA issue are reasonable and fall within the range of acceptable outcomes based upon the facts and the law (Dunsmuir, supra).

#### Section text

Cueto v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2009-08-10
Neutral citation
2009 FC 805
File numbers
IMM-232-09
Decision Content
Federal Court
Cour fédérale
Date: 20090810
Docket: IMM-232-09
Citation: 2009 FC 805
Ottawa, Ontario, this 10th day of August 2009
Present: The Honourable Orville Frenette
BETWEEN:
ARTEMIO VALERIO CUETO
MARIA LUISA MEYA CASTILLO
DAVID SANTIAGO CUETO
LEONARDO SANTIAGO CUETO
Applicants
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT
I. Introduction

[1] This is an application for judicial review pursuant to section 72 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27, (the “Act”) of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the “Board”) rendered on December 31, 2008 determining that the applicants were not Convention refugees nor persons in need of protection pursuant to sections 96 and 97 of the Act.
II. The facts

[2] The principal applicant, Artemio Valerio Cueto, is a 37 year old who with his brothers David and Leonardo, and Leonardo’s wife, Maria Luisa Meya Castillo, are all Mexican citizens. They resided in Veracruz, Mexico. The latter applicants base and rely upon the claim of the principal applicant.

[3] In May 2005, the applicants became close to their cousin, Gabriel Cobos Hernandez, who they believed was an insurance broker. In January 2006, the latter was arrested by the police for drug trafficking and weapons possession. He was identified as a member of a gang believed to be a division of the Sinaloa cartel. He was released from prison in 2006.

[4] The male applicants allege they were pressured by their cousin and members of Sangre Nueva to join the gang. When they refused they were assaulted on May 16, 2007 and injured. They received threats by telephone. The male applicants left Mexico for Canada on June 7, 2007; Maria Luisa followed two months later on August 16, 2007.

[5] The applicants claimed asylum in Canada as persons in need of refugee protection pursuant to sections 96 and 97 of the Act. The applicants did not report the above threats to the police and did not seek help from any state protection agency in Mexico reasoning that they were afraid because the police were corrupt and some were members of the mafia.

[6] The applicants alleged fear of persecution if returned to Mexico.
III. The impugned decision

[7] In its ten-page decision, the Board reviewed the evidence as presented. It also scrutinized the documentary evidence on the situation in Mexico relating to crime, police and state corruption and efforts to combat crime.

[8] The Board found Mexico to be a democratic country that had a functioning police, security forces and judiciary offering responsible law enforcement and order.

[9] The Board acknowledged that Mexico had corruption problems in the police, officials and agencies of the government some of which were on the “payroll” of the drug cartels. However, the documentation showed that anti-drug and anti-corruption activities and efforts were made under the initiative of former President Fox and intensified by President Calderon, which led to federal and local officials and security personnel being arrested and prosecuted for criminal activities. The Board referred to numerous Federal Court decisions which illustrated the measures referred to above.

[10] The Board then considered that the applicants had not sought state protection and had not discharged the burden to rebut the presumption of state protection. The Board also found that there was a viable Internal Flight Alternative (“IFA”) to other cities where the applicants could have relocated.
IV. The issues

[11] The applicants raised what I consider to be secondary issues (which I will deal with briefly later). However, I believe the central issue is: “Did the Board err in finding that the applicants were not persons in need of protection? Particularly, did the Board err in finding that the applicants had not rebutted the presumption of state protection and that a viable IFA existed for them in Mexico?”
V. The sub-issues

[12] The sub-issues raised were: A. Did the Board err in law in supporting specific factual findings with case law? B. Did the Board err in law by not referring to a single document to corroborate its analysis of state protection? C. Did the Board ignore pertinent evidence about police corruption? And D., a factual error was made by the Board.
A. The Board erred in law in supporting specific factual findings with case law

[13] The applicants argue that the Board could not use case law to prove particular facts in a particular case such as the situation in Mexico. The respondent agrees with this proposition; however, he submits that the documentary evidence concerning the general situation in Mexico relating to the state agencies, the police, the problems with corruption and drug trafficking and efforts to combat these problems can be considered in a case such as the one presented here.

[14] I agree with the respondent that the jurisprudence can form a basis of consideration by a court about general conditions in a country as determined by the jurisprudence without excluding evidence to show change in these conditions.

[15] In summary, I believe the Board had the right to invoke the jurisprudence involved, but I do not follow the applicants’ reasoning that the Board did in fact disregard the particular circumstances of their case.
B. The Board erred in law by not referring to a single document to corroborate its analysis of state protection

[16] This submission is plainly erroneous since the Board refers to extensive documentation on this precise point at pages 3, 6 and 9 of its decision.
C. The Board ignored pertinent evidence about police corruption

[17] In its decision the Board referred at length to general documentation and case-law on the question of police and agency corruption and the efforts made by the state under former President Fox and later intensified by President Calderon. Therefore this argument fails.
D. Factual error

[18] The applicants refer to a factual error made by the Board when it stated the principal applicant had reported the May 16, 2007 incident to the police. This is correct since the applicant admitted in his testimony that he did not denunciate the attack of May 16, 2007 or the threats of March 15, 2007. This factual mistake is insufficient to change any important issue or decision and therefore has no bearing in the decision which, as we shall see, turns upon the lack of working state protection and IFA.
VI. Pertinent legislation

[19] Sections 96 and 97 of the Act read as follows:
96. A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
97. (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
(2) A person in Canada who is a member of a class of persons prescribed by the regulations as being in need of protection is also a person in need of protection.
96. A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
97. (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
(2) A également qualité de personne à protéger la personne qui se trouve au Canada et fait partie d’une catégorie de personnes auxquelles est reconnu par règlement le besoin de protection.
VII. The standard of review

[20] To determine a claimant’s risk of return to a particular country is a fact-driven inquiry which calls into play paragraph 18.1(4)(d) of the Federal Courts Act, R.S.C. 1985, c. F-7, which provides this Court may grant relief if it is satisfied a tribunal “based its decision or order on an erroneous finding of fact that it made in a perverse or capricious manner or without regard to the material before it”.

[21] The Supreme Court of Canada in Dunsmuir v. New Brunswick, [2008] 1 S.C.R. 190, and Canada (Minister of Citizenship and Immigration) v. Khosa, 2009 SCC 12, has established that questions of fact or mixed fact and law, are to be governed by the standard of reasonableness. In judicial review, reasonableness is concerned mostly with “the existence of justification, transparency and intelligibility within the decision-making process” and “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, supra, at paragraph 47).

[22] Questions of law are reviewable on a standard of correctness as are questions of procedural fairness (see Chrétien v. Canada (Commission of Enquiry into the Sponsorship Program and Advertising Activities, Gomery Commission), [2008] F.C.J. No. 973 (QL)).

[23] Questions of credibility are to be assessed on the standard of reasonableness (see, for example, Malveda v. Minister of Citizenship and Immigration, 2008 FC 447; Aguirre v. Minister of Citizenship and Immigration, 2008 FC 571; Khokhar v. Minister of Citizenship and Immigration, 2008 FC 449, and Tovar v. Minister of Citizenship and Immigration, 2009 FC 600).
VIII. State protection

[24] The Board rendered an elaborated discussion of the issue of state protection concluding that the applicants had not sought state protection.

[25] There is a presumption that state protection is the responsibility of the state of which the refugee is a citizen (Sanchez v. Minister of Citizenship and Immigration, 2008 FC 134). In Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689, at page 709, the Supreme Court of Canada made it clear that claimants must first address themselves to their home state for protection or to demonstrate that it was objectively unreasonable to have done so, before the responsibility of other states becomes engaged. Therefore, refugee protection is not available when the claimant has not made an attempt or made an adequate attempt to first seek state protection in his home country (Ward, supra, at page 724; Hinzman v. Minister of Citizenship and Immigration, 2007 FCA 171, at paragraphs 52 and 56). When adequate protection exists, a claimant cannot claim an objective well-founded fear of persecution (Sarker v. Minister of Citizenship and Immigration, 2005 FC 353, at paragraph 7; Dannett v. Minister of Citizenship and Immigration, 2006 FC 1363, at paragraphs 34 and 43).

[26] To rebut the presumption of state protection, the claimant must establish relevant, reliable and convincing evidence which satisfies the trier of fact on a balance of probabilities that the state protection is inadequate (Flores Carrillo v. Canada (Minister of Citizenship and Immigration), [2008] 4 F.C.R. 636 (F.C.A.); Granados v. Minister of Citizenship and Immigration, 2009 FC 210; Minister of Public Safety and Emergency Preparedness v. Gunasingam, 2008 FC 181). A subjective reluctance to seek state protection is insufficient to rebut the above presumption.

[27] Mexico is considered an emerging, not a full-fledged democracy which is plagued by major problems, such as crime, corruption in police and governmental agencies, drug-trafficking gangs etc., but since the government presided by President Fox and followed by President Calderon, measures have been implemented to combat these problems. Countries cannot guarantee perfect state protection; what is required is adequate protection which is not necessarily effective (Blanco v. Minister of Citizenship and Immigration, 2005 FC 1487, at paragraph 10; Canada (M.E.I.) v. Villafranca, [1992] F.C.J. No. 1189 (C.A.) (QL); Mendez v. Minister of Citizenship and Immigration, 2008 FC 584). It is recognized in documentary evidence that Mexico still has extensive problems such as state and police corruption, prevalent crime and drug trafficking but it is making efforts to cope with them (De Leon v. Minister of Citizenship and Immigration, 2007 FC 1307; Zepeda v. Minister of Citizenship and Immigration, 2008 FC 491; J.C.M.G. et al. v. Minister of Citizenship and Immigration, 2009 FC 610). However, its citizens must first claim state protection in Mexico before they can seek refuge in another country.
A. Adequate v. effective protection

[28] As mentioned before the preponderant case-law supports the test of an “adequate” state protection rather than an “effective or perfect” state protection. The applicants in the present case rely upon the decision of Garcia v. Canada (Minister of Citizenship and Immigration), [2007] 4 F.C.R. 385, at paragraph 16, to argue that the test should be “[t]hat is, are the police capable of accepting and acting on her complaint in a credible and earnest manner?”

[29] The applicants submit that the Board in the present case did not refer to or meet this test. With all due respect, this test resembles unequivocally the “effective” test which the case-law has not accepted, preferring the “adequacy” test (see also Minister of Citizenship and Immigration v. Carrillo, 2008 FCA 94, at paragraph 38).

[30] In the present case, as the Board found, the applicants have not sought state protection and have not presented sufficient reasons to rebut the presumption of state protection. For the two serious criminal acts in 2007, the applicants have not sought state protection.
B. Internal flight alternative

[31] During the hearing before the Board the principal applicant was asked why they had not considered moving away, for example, to Mexico City or Tijuana. The applicant replied they feared the gang could track them down with their police connections and database information.

[32] The respondent answers that this allegation is purely speculative with no evidentiary basis.

[33] In principle an applicant must first seek safety in another part of his or her country before coming to Canada or establishing why this would be unreasonable (Thirunavukkarasu v. Canada (Minister of Employment and Immigration), [1994] 1 F.C. 589 (C.A.)).

[34] The leading case on IFA, Rasaratnam v. Canada (Minister of Employment and Immigration), [1992] 1 F.C. 706 (C.A.), proposes a two-pronged test for a potential IFA: (a) the Board must be satisfied that there is no serious persecution or danger in the city where the IFA is located; and (b) the Board must consider whether the claimant can reasonably, without undue hardship, seek refuge in that city.

[35] The Board in this case has analyzed the applicants’ reasons in their opposition to the IFA and the evidence which is quasi-totally speculative, concluding an IFA was open to the applicants.

[36] In my view, both findings of the Board on the state protection and the IFA issue are reasonable and fall within the range of acceptable outcomes based upon the facts and the law (Dunsmuir, supra).


## 21912:2 · paragraphs 37-38

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `54e26a4d17586b2d7b94d35f516aadecea19a41868cd825edc1083b2e9e14ddc`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21912:2:subtheme:1 · paragraphs 37-38

- Raw key terms: `application, conclude, conclusion, dismissed, reasons`
- Display key terms: `conclude, conclusion, dismissed`
- Argument roles: `disposition, reasoning_application`
- Explanation: Observed roles: disposition, reasoning_application Display terms: conclude, conclusion, dismissed Application context: [37] For these reasons I must conclude that the application must be dismissed. Operative outcome context: [37] For these reasons I must conclude that the application must be dismissed. Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `conclude` at chunk `5027632` offsets `30-38`; context: [37] For these reasons I must conclude that the application must be dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `5027632` offsets `68-77`; context: [37] For these reasons I must conclude that the application must be dismissed.

#### Section text

IX. Conclusion

[37] For these reasons I must conclude that the application must be dismissed.


## 21912:3 · paragraphs 39-40

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `440c1432eae4084c0885c0991babc30b795d233b79fc4ada133a71e878a88722`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21912:3:subtheme:1 · paragraphs 39-40

- Raw key terms: `applicants, deputy, frenette, immigration, judge, judgment, orville, record`
- Display key terms: `deputy, frenette, judge, orville`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: deputy, frenette, judge, orville No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 39-40. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
The application for judicial review pursuant to section 72 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27, (the “Act”) of a decision of the Refugee Protection Division of the Immigration and Refugee Board rendered on December 31, 2008, determining that the applicants were not Convention refugees nor persons in need of protection pursuant to sections 96 and 97 of the Act, is dismissed.
No questions are certified.
“Orville Frenette”
Deputy Judge
FEDERAL COURT
NAME OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-232-09

STYLE OF CAUSE: ARTEMIO VALERIO CUETO, MARIA LUISA MEYA
CASTILLO, DAVID SANTIAGO CUETO, LEONARDO SANTIAGO CUETO v. THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: July 15, 2009
REASONS FOR JUDGMENT
AND JUDGMENT: The Honourable Orville Frenette, Deputy Judge
DATED: August 10, 2009
APPEARANCES:
Mr. Luis Antonio Monroy FOR THE APPLICANTS
Mr. David Joseph FOR THE RESPONDENT
SOLICITORS OF RECORD:
Luis Antonio Monroy FOR THE APPLICANTS
Toronto, Ontario
John H. Sims, Q.C. FOR THE RESPONDENT
Deputy Attorney General of Canada
