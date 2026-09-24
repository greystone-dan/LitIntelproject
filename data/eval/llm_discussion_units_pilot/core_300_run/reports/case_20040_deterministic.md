# Discussion Units: case 20040

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **33**
- Continuity pairs: **32**
- Discussion Units: **4**
- Paragraph source hashes: **33**
- Sub-themes: **10**

## 20040:1 · paragraphs 0-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2acc5c75a0bd791fc436729c9ab24a28e6efbde68bc63be9cdc7ff067b1f6308`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20040:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `applicant, canada, decision, april, arrival, arrived, because, china`
- Display key terms: `april, arrival, arrived, because, china`
- Argument roles: `governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, party_position, reasoning_application Display terms: april, arrival, arrived, because, china Position/evidence statements: The applicant claimed refugee protection on the basis that he fears persecution in Fujian on religious grounds because he is a practicing Christian. Rule/authority context: [1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board), dated September 23, 2010, concluding that the applicant is not a Conventio | Decision under review Application context: 27 (the Act) because the applicant was not credible and did not face a serious possibility of persecution or a risk to his life or of cruel and unusual treatment or punishment in his hometown in China. | The applicant claimed refugee protection on the basis that he fears persecution in Fujian on religious grounds because he is a practicing Christian. Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4947820` offsets `262-273`; context: [1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board), dated September 23, 2010, concluding that the applicant is not a Convention refugee or person in need of protection pursuant to sections 96 or 97 of the Immigration and Refugee Protection Act, S.
- Evidence: `reasoning_application` cue `because` at chunk `4947820` offsets `365-372`; context: 27 (the Act) because the applicant was not credible and did not face a serious possibility of persecution or a risk to his life or of cruel and unusual treatment or punishment in his hometown in China.
- Evidence: `party_position` cue `claimed` at chunk `4947821` offsets `126-133`; context: The applicant claimed refugee protection on the basis that he fears persecution in Fujian on religious grounds because he is a practicing Christian.
- Evidence: `reasoning_application` cue `because` at chunk `4947821` offsets `223-230`; context: The applicant claimed refugee protection on the basis that he fears persecution in Fujian on religious grounds because he is a practicing Christian.
- Evidence: `governing_rule` cue `under` at chunk `4947824` offsets `274-279`; context: Decision under review

#### 20040:1:subtheme:2 · paragraphs 6-13

- Raw key terms: `board, applicant, found, persecution, evidence, fujian, province, although`
- Display key terms: `persecution, fujian, province, although`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: persecution, fujian, province, although Application context: Although the documentary evidence is mixed, it is reasonable to conclude that the authorities have concluded some investigation which gives rise to them stating that he was identified as a member of an underground church | [10] The Board held, however, that because evidence of persecution incidents in areas more remote than Fujian province was available, the absence of such information regarding persecution in Fujian province indicating th Operative outcome context: The Board found that the treatment of such underground churches is varied, with many urban underground churches limiting the size of their membership to avoid harassment, while those in rural areas could be quite large. Evidence spans paragraphs 6-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4947825` offsets `171-177`; context: There were credibility issues with respect to the unregistered service being raided and whether the authorities are interested in the claimant.
- Evidence: `evidence_fact` cue `found that` at chunk `4947826` offsets `29-39`; context: [7] In particular, the Board found that the fact that the applicant was unable to produce any documentary evidence that the police were searching for him was fatal to his claim.
- Evidence: `reasoning_application` cue `conclude` at chunk `4947826` offsets `524-532`; context: Although the documentary evidence is mixed, it is reasonable to conclude that the authorities have concluded some investigation which gives rise to them stating that he was identified as a member of an underground church.
- Evidence: `counterargument_limitation` cue `but` at chunk `4947826` offsets `305-308`; context: The Board recognized that the documentary evidence revealed that summons or arrest warrants were not always left for suspects, but found that the weight of the documentary evidence indicated that the police were likely to have left some sort of summons at the applicant’s home:
¶7.
- Evidence: `evidence_fact` cue `found that` at chunk `4947827` offsets `27-37`; context: [8] In addition, the Board found that the applicant failed to show that any persecution of underground churches was occurring in the applicant’s home province of Fujian.
- Evidence: `counterargument_limitation` cue `although` at chunk `4947827` offsets `353-361`; context: The Board found that although smaller “house churches” like the one attended by the applicant do not officially need to register with the government, local officials nevertheless do disrupt home worship meetings.
- Evidence: `disposition` cue `varied` at chunk `4947827` offsets `612-618`; context: The Board found that the treatment of such underground churches is varied, with many urban underground churches limiting the size of their membership to avoid harassment, while those in rural areas could be quite large.
- Evidence: `evidence_fact` cue `found that` at chunk `4947828` offsets `65-75`; context: [9] With regard to the applicant’s province of Fujian, the Board found that the evidence revealed that east coast provinces like Fujian have fewer reported incidents of persecution, but that this could indicate either that they are “more open” or that there are simply fewer reports made of the incidents that occur.
- Evidence: `counterargument_limitation` cue `but` at chunk `4947828` offsets `182-185`; context: [9] With regard to the applicant’s province of Fujian, the Board found that the evidence revealed that east coast provinces like Fujian have fewer reported incidents of persecution, but that this could indicate either that they are “more open” or that there are simply fewer reports made of the incidents that occur.
- Evidence: `evidence_fact` cue `evidence` at chunk `4947829` offsets `43-51`; context: [10] The Board held, however, that because evidence of persecution incidents in areas more remote than Fujian province was available, the absence of such information regarding persecution in Fujian province indicating that such persecution was not occurring in that province:
¶11.
- Evidence: `reasoning_application` cue `because` at chunk `4947829` offsets `35-42`; context: [10] The Board held, however, that because evidence of persecution incidents in areas more remote than Fujian province was available, the absence of such information regarding persecution in Fujian province indicating that such persecution was not occurring in that province:
¶11.
- Evidence: `evidence_fact` cue `found that` at chunk `4947830` offsets `15-25`; context: [11] The Board found that the documentation revealed that increasing numbers of Chinese, between 50 and 70 million individuals, belong to non-state-sanctioned churches, and that such underground churches are increasingly operating publicly without being bothered.
- Evidence: `evidence_fact` cue `found that` at chunk `4947831` offsets `97-107`; context: [12] Thus, while the Board accepted the applicant’s claim that he was a practicing Christian, it found that he did not face persecution for that reason in Fujian province of China.

#### 20040:1:subtheme:3 · paragraphs 14-14

- Raw key terms: `accepted, adequate, against, alors, article, autres, avail, avait`
- Display key terms: `accepted, adequate, against, alors, article, autres, avail, avait`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: accepted, adequate, against, alors, article, autres, avail, avait Application context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subj Evidence spans paragraphs 14-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `4947833` offsets `2227-2233`; context: ISSUES
- Evidence: `reasoning_application` cue `because` at chunk `4947833` offsets `707-714`; context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.

#### Section text

Zhang v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2011-06-08
Neutral citation
2011 FC 654
File numbers
IMM-6200-10
Decision Content
Federal Court
Cour fédérale
Date: 20110608
Docket: IMM-6200-10
Citation: 2011 FC 654
Ottawa, Ontario, June 8, 2011
PRESENT: The Honourable Mr. Justice Kelen
BETWEEN:
XI SHUN ZHANG
Applicant
and
THE MINISTER OF
CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board), dated September 23, 2010, concluding that the applicant is not a Convention refugee or person in need of protection pursuant to sections 96 or 97 of the Immigration and Refugee Protection Act, S.C. 2001, c.27 (the Act) because the applicant was not credible and did not face a serious possibility of persecution or a risk to his life or of cruel and unusual treatment or punishment in his hometown in China.
FACTS
Background

[2] The applicant is a 57-year-old citizen of China from Fujian Province. He arrived in Canada on May 13, 2009. The applicant claimed refugee protection on the basis that he fears persecution in Fujian on religious grounds because he is a practicing Christian.

[3] The applicant stated that he first attended a church service at the suggestion of his childhood friend, Jun Lin, as a means of overcoming depression and drinking problems that he developed following a failed attempt to start a business. He first attended a service on April 6, 2008, and stated that he immediately became enthralled. Thereafter, he attended services every week. The applicant stated that the church was “underground” with practices not sanctioned by the Chinese government. As a result, the church took numerous precautions in order to ensure its secrecy and the safety of its attendees.

[4] On April 19, 2009, officers from the Public Security Bureau (PSB) raided the church service that the applicant was attending. He escaped before their arrival, “thanks” to a warning from a lookout. The applicant fled to a relative’s home, afraid to return to his own home. As he hid, his wife informed him that PSB officers had visited his home looking for him. The applicant stated that the officers continued to visit his home and tell his wife that he had to face the consequences of having violated the law. As a result, the applicant and his wife decided that he could not return home. He decided to flee the country.

[5] The applicant managed to borrow $46,000 from relatives in order to pay a smuggler to get him a fake passport and fly to Canada, where he arrived in May 13, 2009. Since his arrival, his wife reports that Chinese authorities continue to look for him at his home.
Decision under review

[6] On September 23, 2010, the Board rejected the applicant’s claim. The Board summarized its principal finding at paragraph 4 of its decision:
¶4. There were credibility issues with respect to the unregistered service being raided and whether the authorities are interested in the claimant.

[7] In particular, the Board found that the fact that the applicant was unable to produce any documentary evidence that the police were searching for him was fatal to his claim. The Board recognized that the documentary evidence revealed that summons or arrest warrants were not always left for suspects, but found that the weight of the documentary evidence indicated that the police were likely to have left some sort of summons at the applicant’s home:
¶7. Although the documentary evidence is mixed, it is reasonable to conclude that the authorities have concluded some investigation which gives rise to them stating that he was identified as a member of an underground church. Further, given that the authorities have allegedly continue [sic] to inquire about the claimant, it is reasonable to expect, given the documentary evidence, that an arrest warrant or summons would have been left with the claimant’s family.

[8] In addition, the Board found that the applicant failed to show that any persecution of underground churches was occurring in the applicant’s home province of Fujian. The Board reviewed the documentary evidence regarding the persecution of the estimated 50 to 70 million Christians associated with underground churches in China. The Board found that although smaller “house churches” like the one attended by the applicant do not officially need to register with the government, local officials nevertheless do disrupt home worship meetings. The Board found that the treatment of such underground churches is varied, with many urban underground churches limiting the size of their membership to avoid harassment, while those in rural areas could be quite large. The Board found that the police are more likely to target larger underground churches with stronger community and international connections. The Board recognized that the documentation indicates that members of unregistered churches face harassment and harsh punishment, including mistreatment and torture in custody, in some parts of China.

[9] With regard to the applicant’s province of Fujian, the Board found that the evidence revealed that east coast provinces like Fujian have fewer reported incidents of persecution, but that this could indicate either that they are “more open” or that there are simply fewer reports made of the incidents that occur. The Board recognized that in 2006 a church in Fujian province was demolished, although there is no evidence as to why.

[10] The Board held, however, that because evidence of persecution incidents in areas more remote than Fujian province was available, the absence of such information regarding persecution in Fujian province indicating that such persecution was not occurring in that province:
¶11. The panel is mindful of the caveat that the number of persecution incidents is likely to be much higher because of censorship in communications and even considered the possibility that not all information is available to commentators. Considering all these factors, the panel concludes that since there is a significant amount of information detailing very specific examples from areas much more remote and difficult to access than Fujian, which includes not only egregious examples of persecution such as arrests but also other forms of persecution such as fines, short term detentions, confiscation of materials, etc., that it is reasonable for the panel to expect to see persuasive evidence that groups such as the claimant’s, which are small and not required to register, are being raided and individuals being jailed or facing other forms of persecution in Fujian province. The documentary evidence persuades the panel, based on a balance of probabilities, that the claimant’s unregistered house church was not raided and further supports the determination that the authorities are not seeking the claimant.

[11] The Board found that the documentation revealed that increasing numbers of Chinese, between 50 and 70 million individuals, belong to non-state-sanctioned churches, and that such underground churches are increasingly operating publicly without being bothered.

[12] Thus, while the Board accepted the applicant’s claim that he was a practicing Christian, it found that he did not face persecution for that reason in Fujian province of China.
LEGISLATION

[13] Section 96 of the Act, grants protection to Convention refugees:
96. A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country
96. A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.

[14] Section 97 of the Act grants protection to persons whose removal would subject them personally to a danger of torture, or to a risk to life, or to a risk of cruel and unusual treatment or punishment:
97. (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
97. (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
ISSUES

## 20040:2 · paragraphs 15-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c14a036a337b62d32fbadad553293edf7c7f1310c4dffec19f1020ce879e4975`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20040:2:subtheme:1 · paragraphs 15-17

- Raw key terms: `standard, analysis, board, canada, citizenship, immigration, paragraph, review`
- Display key terms: `standard, analysis, paragraph, review`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: standard, analysis, paragraph, review Position/evidence statements: [15] The applicant submits the following two issues: a. Rule/authority context: STANDARD OF REVIEW | 190, the Supreme Court of Canada held at paragraph 62 that the first step in conducting a standard of review analysis is to “ascertain whether the jurisprudence has already determined in a satisfactory manner the degree  Application context: Was the Board’s finding that the applicant was not being sought by Chinese authorities unreasonable because he was unable to provide a warrant or summons documenting that interest? Evidence spans paragraphs 15-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4947834` offsets `45-51`; context: [15] The applicant submits the following two issues:
a.
- Evidence: `party_position` cue `submits` at chunk `4947834` offsets `19-26`; context: [15] The applicant submits the following two issues:
a.
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `4947834` offsets `391-409`; context: STANDARD OF REVIEW
- Evidence: `reasoning_application` cue `because` at chunk `4947834` offsets `156-163`; context: Was the Board’s finding that the applicant was not being sought by Chinese authorities unreasonable because he was unable to provide a warrant or summons documenting that interest?
- Evidence: `issue` cue `whether` at chunk `4947835` offsets `198-205`; context: 190, the Supreme Court of Canada held at paragraph 62 that the first step in conducting a standard of review analysis is to “ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of (deference) to be accorded with regard to a particular category of question”: see also Canada (Citizenship and Immigration) v.
- Evidence: `governing_rule` cue `standard of review` at chunk `4947835` offsets `153-171`; context: 190, the Supreme Court of Canada held at paragraph 62 that the first step in conducting a standard of review analysis is to “ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of (deference) to be accorded with regard to a particular category of question”: see also Canada (Citizenship and Immigration) v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4947836` offsets `82-90`; context: [17] Credibility and plausibility determinations, and the Board’s analysis of the evidence are questions of fact or mixed fact and law and reviewable on a standard of reasonableness: Wu v.

#### 20040:2:subtheme:2 · paragraphs 18-21

- Raw key terms: `applicant, authorities, board, submits, summons, warrant, arrest, court`
- Display key terms: `authorities, submits, summons, warrant, arrest`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: authorities, submits, summons, warrant, arrest Position/evidence statements: [19] The applicant submits that the Board was unreasonable in relying upon the documentary evidence that it cited to find that an arrest warrant or summons would have been left with the applicant’s family if the authorit | [20] As a result, the applicant submits that his testimony that no arrest warrant or summons was left with his family is not refuted by the evidence. Application context: ANALYSIS Issue 1: Was the Board’s finding that the applicant was not being sought by Chinese authorities unreasonable because he was unable to provide a warrant or summons documenting that interest? | In this case, the applicant submits that the documentary evidence is entirely consistent with his testimony and, therefore, could easily have occurred as he described it. Evidence spans paragraphs 18-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4947837` offsets `206-213`; context: [18] In reviewing the Board's decision using a standard of reasonableness, the Court will consider “the existence of justification, transparency and intelligibility within the decision-making process” and “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law”: Dunsmuir, supra, at paragraph 47; Khosa, supra, at paragraph 59.
- Evidence: `reasoning_application` cue `because` at chunk `4947837` offsets `519-526`; context: ANALYSIS
Issue 1: Was the Board’s finding that the applicant was not being sought by Chinese authorities unreasonable because he was unable to provide a warrant or summons documenting that interest?
- Evidence: `party_position` cue `submits` at chunk `4947838` offsets `19-26`; context: [19] The applicant submits that the Board was unreasonable in relying upon the documentary evidence that it cited to find that an arrest warrant or summons would have been left with the applicant’s family if the authorities were truly searching for the applicant.
- Evidence: `evidence_fact` cue `evidence` at chunk `4947838` offsets `91-99`; context: [19] The applicant submits that the Board was unreasonable in relying upon the documentary evidence that it cited to find that an arrest warrant or summons would have been left with the applicant’s family if the authorities were truly searching for the applicant.
- Evidence: `counterargument_limitation` cue `although` at chunk `4947838` offsets `354-362`; context: The applicant submits that the documentary evidence cited by the Board itself states that although court documents, summonses, or notices may be received by an adult member of the suspect’s household, due to discrepancies between legislation and its implementation in China, this is not always the procedure chosen by the authorities themselves.
- Evidence: `party_position` cue `submits` at chunk `4947839` offsets `32-39`; context: [20] As a result, the applicant submits that his testimony that no arrest warrant or summons was left with his family is not refuted by the evidence.
- Evidence: `evidence_fact` cue `testimony` at chunk `4947839` offsets `49-58`; context: [20] As a result, the applicant submits that his testimony that no arrest warrant or summons was left with his family is not refuted by the evidence.
- Evidence: `reasoning_application` cue `therefore` at chunk `4947839` offsets `263-272`; context: In this case, the applicant submits that the documentary evidence is entirely consistent with his testimony and, therefore, could easily have occurred as he described it.
- Evidence: `party_position` cue `submits` at chunk `4947840` offsets `20-27`; context: [21] The respondent submits that the Board considered the authorities referred to by the applicant but decided that the balance of probabilities was that the applicant was not being sought by authorities.
- Evidence: `counterargument_limitation` cue `but` at chunk `4947840` offsets `99-102`; context: [21] The respondent submits that the Board considered the authorities referred to by the applicant but decided that the balance of probabilities was that the applicant was not being sought by authorities.

#### 20040:2:subtheme:3 · paragraphs 22-25

- Raw key terms: `applicant, board, documentary, evidence, china, finding, practice, always`
- Display key terms: `documentary, china, finding, practice, always`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: documentary, china, finding, practice, always Position/evidence statements: [24] The applicant submits that the panel erred in finding that the applicant’s church had not been raided and that the applicant could practice in an underground church in China. Evidence spans paragraphs 22-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4947841` offsets `839-846`; context: The evidence before the Board stated:
RESPONSES TO INFORMATION REQUESTS (RIRs)
1 June 2004
China: Circumstances and authorities responsible for issuing summonses/subpoenas; procedural law; whether summonses are given to individuals or households; format and appearance; whether legality can be challenged; punishment for failure to comply with a summons (1998-2004)
Research Directorate, Immigration and Refugee Board, Ottawa”
…
Furthermore, a Human Rights in China (HRIC) representative, who is based in New York, provided the following information that she received from a colleague who is based in Hong Kong and who works as a lawyer specializing in Chinese law, on a) the service of subpoenas, b) the refusal of service and c) on witness appearance at trials:
a) Article 81 of the Criminal Procedure Law (CPL) governs service of process on witnesses.
- Evidence: `evidence_fact` cue `evidence` at chunk `4947841` offsets `64-72`; context: [22] The Board specifically referred to reliable and verifiable evidence in support of its finding that the applicant was not being sought by Chinese authorities.
- Evidence: `counterargument_limitation` cue `however` at chunk `4947841` offsets `455-462`; context: The Board found, however, that given the number of times the applicant had alleged that his house was visited, the documentary evidence indicated that the police were likely to have left something at some point.
- Evidence: `issue` cue `Issue` at chunk `4947842` offsets `178-183`; context: Issue 2: Was the Board’s finding that the applicant could practice his faith in China without facing more than a serious possibility of persecution, reasonable?
- Evidence: `evidence_fact` cue `evidence` at chunk `4947842` offsets `37-45`; context: [23] The Board may weigh documentary evidence against the applicant’s testimony, and find that the documentary evidence supports a finding contrary to the applicant’s testimony.
- Evidence: `party_position` cue `submits` at chunk `4947843` offsets `19-26`; context: [24] The applicant submits that the panel erred in finding that the applicant’s church had not been raided and that the applicant could practice in an underground church in China.
- Evidence: `evidence_fact` cue `evidence` at chunk `4947843` offsets `223-231`; context: The applicant submits that the documentary evidence reviewed by the Board demonstrates that underground churches and their members are regularly persecuted by Chinese authorities.
- Evidence: `evidence_fact` cue `evidence` at chunk `4947844` offsets `109-117`; context: [25] The Court finds that the Board was reasonable in concluding, on a balance of probabilities based on the evidence that the applicant’s church was not raided and the applicant can continue to practice his religion in an underground church in Fujian Province.

#### 20040:2:subtheme:4 · paragraphs 26-27

- Raw key terms: `based, board, case, court, evidence, open, accept, accepted`
- Display key terms: `based, case, open, accept, accepted`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: based, case, open, accept, accepted Position/evidence statements: [26] The Federal Court has dealt with a number of claims similar to those of the applicant. Rule/authority context: From this it follows that if the Board has reasons to doubt the overall truthfulness of a claimant’s evidence it is “under a duty to give its reasons for casting doubt upon the appellant's credibility in clear and unmist Application context: That is hardly surprising as one is unlikely to find a report that something has not happened because it is events, not non-events, that are reported. Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4947845` offsets `332-340`; context: I agree with his comments on the question applicable to the case at bar.
- Evidence: `party_position` cue `claims` at chunk `4947845` offsets `50-56`; context: [26] The Federal Court has dealt with a number of claims similar to those of the applicant.
- Evidence: `evidence_fact` cue `evidence` at chunk `4947845` offsets `289-297`; context: Canada (Citizenship and Immigration), 2010 FC 310, Justice Zinn considered the interaction between the presumption of an applicant’s truthfulness and corroborating documentary evidence.
- Evidence: `governing_rule` cue `under` at chunk `4947845` offsets `978-983`; context: From this it follows that if the Board has reasons to doubt the overall truthfulness of a claimant’s evidence it is “under a duty to give its reasons for casting doubt upon the appellant's credibility in clear and unmistakable terms:”Hilo v.
- Evidence: `reasoning_application` cue `because` at chunk `4947845` offsets `2419-2426`; context: That is hardly surprising as one is unlikely to find a report that something has not happened because it is events, not non-events, that are reported.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4947845` offsets `1880-1888`; context: Although he had otherwise been found credible, in that the Board accepted his evidence that he was a Christian and attended a house church in Fujian, there was other evidence before the Board that brought his evidence of the raid into question.
- Evidence: `evidence_fact` cue `evidence` at chunk `4947846` offsets `61-69`; context: [27] The Court finds that the Board in this case weighed the evidence that was before it.

#### 20040:2:subtheme:5 · paragraphs 28-29

- Raw key terms: `certified, court, question, advised, agrees, appeal, application, based`
- Display key terms: `certified, question, advised, agrees, based`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue Display terms: certified, question, advised, agrees, based Operative outcome context: The application for judicial review is dismissed. Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `QUESTION` at chunk `4947847` offsets `236-244`; context: CERTIFIED QUESTION
- Evidence: `evidence_fact` cue `evidence` at chunk `4947847` offsets `67-75`; context: [28] The Board’s conclusion was reasonably open to it based on the evidence.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4947847` offsets `158-164`; context: This Court cannot intervene.
- Evidence: `disposition` cue `dismissed` at chunk `4947847` offsets `215-224`; context: The application for judicial review is dismissed.
- Evidence: `issue` cue `question` at chunk `4947848` offsets `76-84`; context: [29] Both parties advised the Court that this case does not raise a serious question of general importance which ought to be certified for an appeal.

#### Section text

[15] The applicant submits the following two issues:
a. Was the Board’s finding that the applicant was not being sought by Chinese authorities unreasonable because he was unable to provide a warrant or summons documenting that interest?
b. Was the Board’s finding that the applicant could practice his faith in China without facing more than a serious possibility of persecution reasonable?
STANDARD OF REVIEW

[16] In Dunsmuir v. New Brunswick, 2008 SCC 9, [2008] 1 S.C.R. 190, the Supreme Court of Canada held at paragraph 62 that the first step in conducting a standard of review analysis is to “ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of (deference) to be accorded with regard to a particular category of question”: see also Canada (Citizenship and Immigration) v. Khosa, 2009 SCC 12, [2009] 1 S.C.R. 339, per Justice Binnie at paragraph 53.

[17] Credibility and plausibility determinations, and the Board’s analysis of the evidence are questions of fact or mixed fact and law and reviewable on a standard of reasonableness: Wu v. Canada (Citizenship and Immigration), 2009 FC 929, at paragraph 17; Khokhar v. Canada (Citizenship and Immigration), 2008 FC 449 at paras. 17-20, and Dong v. Canada (Citizenship and Immigration), 2010 FC 55, at paragraph 17.

[18] In reviewing the Board's decision using a standard of reasonableness, the Court will consider “the existence of justification, transparency and intelligibility within the decision-making process” and “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law”: Dunsmuir, supra, at paragraph 47; Khosa, supra, at paragraph 59.
ANALYSIS
Issue 1: Was the Board’s finding that the applicant was not being sought by Chinese authorities unreasonable because he was unable to provide a warrant or summons documenting that interest?

[19] The applicant submits that the Board was unreasonable in relying upon the documentary evidence that it cited to find that an arrest warrant or summons would have been left with the applicant’s family if the authorities were truly searching for the applicant. The applicant submits that the documentary evidence cited by the Board itself states that although court documents, summonses, or notices may be received by an adult member of the suspect’s household, due to discrepancies between legislation and its implementation in China, this is not always the procedure chosen by the authorities themselves. The same documentary evidence indicated that China does not comply with rule of law standards, and that police do not always comply with the law.

[20] As a result, the applicant submits that his testimony that no arrest warrant or summons was left with his family is not refuted by the evidence. In this case, the applicant submits that the documentary evidence is entirely consistent with his testimony and, therefore, could easily have occurred as he described it.

[21] The respondent submits that the Board considered the authorities referred to by the applicant but decided that the balance of probabilities was that the applicant was not being sought by authorities. The respondent submits that this finding was reasonably open to the Board.

[22] The Board specifically referred to reliable and verifiable evidence in support of its finding that the applicant was not being sought by Chinese authorities. This conclusion did not rest on the Board’s assumptions about rational behaviour. The Board also fully considered evidence that potentially refuted its ultimate conclusions. The Board recognized that the police do not always leave summonses or arrest warrants with families. The Board found, however, that given the number of times the applicant had alleged that his house was visited, the documentary evidence indicated that the police were likely to have left something at some point. The evidence before the Board stated:
RESPONSES TO INFORMATION REQUESTS (RIRs)
1 June 2004
China: Circumstances and authorities responsible for issuing summonses/subpoenas; procedural law; whether summonses are given to individuals or households; format and appearance; whether legality can be challenged; punishment for failure to comply with a summons (1998-2004)
Research Directorate, Immigration and Refugee Board, Ottawa”
…
Furthermore, a Human Rights in China (HRIC) representative, who is based in New York, provided the following information that she received from a colleague who is based in Hong Kong and who works as a lawyer specializing in Chinese law, on a) the service of subpoenas, b) the refusal of service and c) on witness appearance at trials:
a) Article 81 of the Criminal Procedure Law (CPL) governs service of process on witnesses. The service of subpoenas, notices and other procedural documents shall be made upon the addressee himself. If the addressee is not in, delivery may be made on his behalf to an adult member of his family or a responsible person of his unit.
…
… it is very common in China for the police authorities to leave a summons or subpoena with family members (or possibly close friends, though that is probably less common), instructing them to pass it along to the person named on the summons. The person accepting the summons would be expected to sign an acknowledgement of receipt.

[23] The Board may weigh documentary evidence against the applicant’s testimony, and find that the documentary evidence supports a finding contrary to the applicant’s testimony.
Issue 2: Was the Board’s finding that the applicant could practice his faith in China without facing more than a serious possibility of persecution, reasonable?

[24] The applicant submits that the panel erred in finding that the applicant’s church had not been raided and that the applicant could practice in an underground church in China. The applicant submits that the documentary evidence reviewed by the Board demonstrates that underground churches and their members are regularly persecuted by Chinese authorities. The applicant cites, in particular, a Response to Information Request relied on by the Board, in a section not quoted by the Board, which states:
With specific reference to the provinces Fujian and Guangdong, it is absolutely incorrect to find that there is religious freedom in these provinces. […] [T]he persecution may come and go and not be totally predictable, but it is always present. Even the very threat of a government crackdown is a method of persecution. The house churches in Fujian and Guangdong, like all of China, face the constant and fearful risk of being closed and its members punished. Certainly, these provinces do not enjoy religious freedom while all other parts of China do not.

[25] The Court finds that the Board was reasonable in concluding, on a balance of probabilities based on the evidence that the applicant’s church was not raided and the applicant can continue to practice his religion in an underground church in Fujian Province. The evidence that the Board balanced was the applicant’s testimony regarding the raid and police visits to his home, and the documentary evidence indicating the frequency and likelihood of police raids on underground churches in the applicant’s home province of Fujian. Based on a review of this evidence, the Board found that certain churches were more likely to be raided than others. In particular, churches in certain areas of the country, churches that are larger, churches that have international connections, and churches that evangelize. The Board found no evidence of targeting of churches in Fujian Province.

[26] The Federal Court has dealt with a number of claims similar to those of the applicant. In the case of Yu v. Canada (Citizenship and Immigration), 2010 FC 310, Justice Zinn considered the interaction between the presumption of an applicant’s truthfulness and corroborating documentary evidence. I agree with his comments on the question applicable to the case at bar. Justice Zinn states that there is nothing unreasonable in a Board’s decision to prefer documentary evidence to an applicant’s testimony after a careful weighing of the evidence:
¶26. The applicant is correct in asserting that “when an applicant swears to the truth of certain allegations, this creates a presumption that those allegations are true unless there be reason to doubt their truthfulness:” Maldonado v. Canada (Minister of Employment and Immigration), [1980] 2 F.C. 302 (C.A.). From this it follows that if the Board has reasons to doubt the overall truthfulness of a claimant’s evidence it is “under a duty to give its reasons for casting doubt upon the appellant's credibility in clear and unmistakable terms:”Hilo v. Canada (Minister of Employment and Immigration) (1991), 15 Imm. L.R. (2d) 199 (F.C.A.). (emphasis added)
¶27. In this case, the applicant correctly notes that the Board made no explicit negative credibility finding regarding his testimony. Rather, he submits, the Board preferred the documentary evidence and concluded “based on a balance of probabilities, that the authorities did not raid the gathering.” He submits that this finding was only open to the Board if it first provided reasons for finding his evidence to be not credible. I do not accept the applicant’s submission.
…
¶31. In this case, the only evidence that was provided to the Board that the applicant’s house church was raided was his own testimony. There was no corroborative evidence of any sort provided. Although he had otherwise been found credible, in that the Board accepted his evidence that he was a Christian and attended a house church in Fujian, there was other evidence before the Board that brought his evidence of the raid into question.
¶32. The other evidence was documentary evidence. It was not directly contradictory of the applicant’s testimony in that it did not say that no house churches had ever been raided in Fujian Province. That is hardly surprising as one is unlikely to find a report that something has not happened because it is events, not non-events, that are reported. Nonetheless, the documentary evidence does lead to an inference that no such raid occurred. It leads to this inference, as the Board noted, for many reasons, including the following:
1. There is a large discrepancy in the treatment of house churches in China. In some parts of the country house churches with large memberships meet openly with no objection, while in other areas, house churches with small memberships are targeted by the authorities.
2. Protestant Christians who attempt to meet in large groups, or who travel within China and outside China for religious meetings are more likely to be targeted by authorities.
3. There is documentary information of religious persecution of house churches and their adherents from many areas of China, including many remote areas, but there is little such evidence of such persecution in Fujian Province.
4. The evidence of religious persecution in Fujian Province that exists relates to the Catholic Church.
¶33. In this case, the Board chose to accept the independent documentary evidence over the applicant’s testimony. It is evident from a reading of the decision as a whole that it did so because it preferred the evidence from “a large number of different commentators … none of whom have a personal interest in the pursuit of an individual claim for protection” to the applicant’s evidence in support of his own claim for protection. Its weighing of the evidence on this basis cannot be said to be unreasonable. Having formed the view that the documentary evidence was stronger and was to be preferred, it did not need to make any explicit finding that the applicant’s evidence on this point was not credible; it did so indirectly.
(underlining added)
The underlined parts of Justice Zinn’s reasons are directly applicable to the case at bar. Justice Zinn thoroughly assesses the likelihood of a raid on an underground church in Fujian Province.

[27] The Court finds that the Board in this case weighed the evidence that was before it. This Court is not to interfere where the Board’s conclusions are reasonably open to the Board based on the evidence.
CONCLUSION

[28] The Board’s conclusion was reasonably open to it based on the evidence. The Board could have also reasonably come to the opposite conclusion. This Court cannot intervene. The application for judicial review is dismissed.
CERTIFIED QUESTION

[29] Both parties advised the Court that this case does not raise a serious question of general importance which ought to be certified for an appeal. The Court agrees.


## 20040:3 · paragraphs 30-31

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `38347fb5b2a5a6546774b47f52d73cd5f867c43a9bb1d8d4ffc762b85b8feaad`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20040:3:subtheme:1 · paragraphs 30-31

- Raw key terms: `application, cause, citizenship, court, date, dismissed, docket, federal`
- Display key terms: `date, dismissed, federal`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: date, dismissed, federal Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that: This application for judicial review is dismissed. Evidence spans paragraphs 30-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4947848` offsets `248-257`; context: JUDGMENT
THIS COURT’S JUDGMENT is that:
This application for judicial review is dismissed.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that:
This application for judicial review is dismissed.
“Michael A. Kelen”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-6200-10
STYLE OF CAUSE: Xi Shun Zhang v. The Minister of Citizenship and Immigration
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: May 24, 2011
REASONS FOR 

## 20040:4 · paragraphs 32-32

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e39fa5b6cf0f33881734144a7de26b9d724dca4aff41e76682aa6c00e8f044cf`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20040:4:subtheme:1 · paragraphs 32-32

- Raw key terms: `appearances, applicant, attorney, barrister, canada, dated, deputy, general`
- Display key terms: `barrister, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 32-32. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: KELEN J.
DATED: June 8, 2011
APPEARANCES:
Hart A. Kaminker
FOR THE APPLICANT
Lorne McClenaghan
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Hart A. Kaminker,
Barrister & Solicitor
Toronto, Ontario
FOR THE APPLICANT
Myles J. Kirvan,
Deputy Attorney General of Canada
Toronto, Ontario
FOR THE RESPONDENT
