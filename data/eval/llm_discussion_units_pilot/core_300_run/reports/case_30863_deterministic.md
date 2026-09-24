# Discussion Units: case 30863

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **42**
- Continuity pairs: **41**
- Discussion Units: **3**
- Paragraph source hashes: **42**
- Sub-themes: **16**

## 30863:1 · paragraphs 0-38

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fe1d1dcb65f3e7dced21601516795084631df7d87837be34de479bd56b335c45`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 30863:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, decision, immigration, acts, agent, alleged, antonio, apparently`
- Display key terms: `acts, agent, alleged, antonio, apparently`
- Argument roles: `disposition, party_position`
- Explanation: Observed roles: disposition, party_position Display terms: acts, agent, alleged, antonio, apparently Position/evidence statements: He claimed that the authorities in his country could not protect him from the persecution which he fears primarily from one José Antonio Lemus (the persecuting agent) for whom he worked in the local office of the Institu Operative outcome context: [2] The applicant’s refugee claim was dismissed by the Refugee Protection Division of the Immigration and Refugee Board (the Board); hence this application for judicial review. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claimed` at chunk `5436418` offsets `45-52`; context: He claimed that the authorities in his country could not protect him from the persecution which he fears primarily from one José Antonio Lemus (the persecuting agent) for whom he worked in the local office of the Institutional Revolutionary Party (IRP) in Mexico when he was studying industrial engineering.
- Evidence: `disposition` cue `dismissed` at chunk `5436419` offsets `38-47`; context: [2] The applicant’s refugee claim was dismissed by the Refugee Protection Division of the Immigration and Refugee Board (the Board); hence this application for judicial review.

#### 30863:1:subtheme:2 · paragraphs 3-6

- Raw key terms: `applicant, board, protection, agent, case, concluded, convention, government`
- Display key terms: `protection, agent, case, concluded, convention, government`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: protection, agent, case, concluded, convention, government Application context: In view of the fact that, in the Board’s opinion, the death threats made against the applicant were prompted by personal revenge on the part of the persecuting agent (and not related to the alleged political opinions of  | [5] Therefore, the Board concluded that the applicant was neither a “Convention refugee” nor a “person in need of protection” within the meaning of sections 96 and 97 of the Act. Evidence spans paragraphs 3-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5436420` offsets `99-107`; context: [3] In the very succinct reasons (two and a half pages) provided in this matter, the Board did not question the applicant’s credibility and concluded that he had [translation] “definitely been the victim of personal revenge”.
- Evidence: `reasoning_application` cue `therefore` at chunk `5436420` offsets `646-655`; context: In view of the fact that, in the Board’s opinion, the death threats made against the applicant were prompted by personal revenge on the part of the persecuting agent (and not related to the alleged political opinions of the applicant), therefore, there had been no “persecution” within the meaning of section 96 of the Immigration and Refugee Protection Act, S.
- Evidence: `counterargument_limitation` cue `However` at chunk `5436420` offsets `226-233`; context: However, in order to be recognized as a “Convention refugee”, a person must show that he reasonably feared persecution in relation to one of the five grounds listed in the definition.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436421` offsets `217-225`; context: [4] The Board also considered that “the claimant has not discharged the burden of proof on him to rebut the presumption that the authorities in his country are unable to protect him, by providing clear and convincing evidence in this respect” (emphasis added).
- Evidence: `reasoning_application` cue `Therefore` at chunk `5436422` offsets `4-13`; context: [5] Therefore, the Board concluded that the applicant was neither a “Convention refugee” nor a “person in need of protection” within the meaning of sections 96 and 97 of the Act.

#### 30863:1:subtheme:3 · paragraphs 7-8

- Raw key terms: `applicant, board, evidence, whole, account, allow, application, approached`
- Display key terms: `whole, account, allow, approached`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: whole, account, allow, approached Position/evidence statements: The applicant argued that he had good reason not to want to seek protection in his country because of the degree of corruption existing there at all levels and the reprisals to which he would have been exposed if he had  Application context: The applicant argued that he had good reason not to want to seek protection in his country because of the degree of corruption existing there at all levels and the reprisals to which he would have been exposed if he had  Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5436424` offsets `135-142`; context: [7] The applicant challenged, first, the sufficiency of the reasons given in this matter, as they did not allow the Court to determine whether the Board derived its general finding from the evidence in the record as a whole, while taking the applicant’s personal situation into account.
- Evidence: `party_position` cue `argued` at chunk `5436424` offsets `301-307`; context: The applicant argued that he had good reason not to want to seek protection in his country because of the degree of corruption existing there at all levels and the reprisals to which he would have been exposed if he had filed a complaint with the Mexican authorities.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436424` offsets `190-198`; context: [7] The applicant challenged, first, the sufficiency of the reasons given in this matter, as they did not allow the Court to determine whether the Board derived its general finding from the evidence in the record as a whole, while taking the applicant’s personal situation into account.
- Evidence: `reasoning_application` cue `because` at chunk `5436424` offsets `378-385`; context: The applicant argued that he had good reason not to want to seek protection in his country because of the degree of corruption existing there at all levels and the reprisals to which he would have been exposed if he had filed a complaint with the Mexican authorities.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436425` offsets `58-66`; context: [8] The applicant noted that the Board must weigh all the evidence as a whole, not examine each part in isolation: Owusu v.

#### 30863:1:subtheme:4 · paragraphs 9-12

- Raw key terms: `board, decision, protection, referred, according, applicant, canada, directorate`
- Display key terms: `protection, referred, according, directorate`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: protection, referred, according, directorate Position/evidence statements: [10] The applicant further argued that a majority of crimes are not reported in Mexico simply because people do not trust the police and fear reprisals if they report criminals. | In this regard, the applicant submitted that the Board picked and chose in the documentary evidence. Rule/authority context: Further, the courts continue to admit in evidence statements obtained under torture. | Thus, in one of the documents not mentioned by the Board in its decision, the crime rate for crimes under the law of the several Mexican states is said to have diminished by 1% while federal crimes allegedly increased by Application context: [9] Therefore, the applicant reproached the Board for not having mentioned or discussed in its decision the evidence that did corroborate his testimony that corruption is widespread in Mexico and that in such a case it i | [10] The applicant further argued that a majority of crimes are not reported in Mexico simply because people do not trust the police and fear reprisals if they report criminals. Evidence spans paragraphs 9-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5436426` offsets `266-271`; context: What is at issue here is the reporting of crimes committed by an influential political figure and by the henchmen in his pay.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436426` offsets `108-116`; context: [9] Therefore, the applicant reproached the Board for not having mentioned or discussed in its decision the evidence that did corroborate his testimony that corruption is widespread in Mexico and that in such a case it is pointless to contact the police.
- Evidence: `governing_rule` cue `under` at chunk `5436426` offsets `1279-1284`; context: Further, the courts continue to admit in evidence statements obtained under torture.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5436426` offsets `4-13`; context: [9] Therefore, the applicant reproached the Board for not having mentioned or discussed in its decision the evidence that did corroborate his testimony that corruption is widespread in Mexico and that in such a case it is pointless to contact the police.
- Evidence: `issue` cue `whether` at chunk `5436427` offsets `285-292`; context: The applicant submitted that this was a factor the Board should have taken into account when it determined whether the claimant’s refusal to file a complaint with the police was reasonable in the circumstances.
- Evidence: `party_position` cue `argued` at chunk `5436427` offsets `27-33`; context: [10] The applicant further argued that a majority of crimes are not reported in Mexico simply because people do not trust the police and fear reprisals if they report criminals.
- Evidence: `governing_rule` cue `under` at chunk `5436427` offsets `489-494`; context: Thus, in one of the documents not mentioned by the Board in its decision, the crime rate for crimes under the law of the several Mexican states is said to have diminished by 1% while federal crimes allegedly increased by 1%.
- Evidence: `reasoning_application` cue `because` at chunk `5436427` offsets `94-101`; context: [10] The applicant further argued that a majority of crimes are not reported in Mexico simply because people do not trust the police and fear reprisals if they report criminals.
- Evidence: `counterargument_limitation` cue `However` at chunk `5436427` offsets `614-621`; context: However, several information sources claim that the official statistics do not reflect the reality as many persons are hesitant to report crimes.
- Evidence: `party_position` cue `submitted` at chunk `5436428` offsets `310-319`; context: In this regard, the applicant submitted that the Board picked and chose in the documentary evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436428` offsets `371-379`; context: In this regard, the applicant submitted that the Board picked and chose in the documentary evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436429` offsets `190-198`; context: [12] For example, the Center for Public Integrity (CPI) recently noted that, in some cases, corruption in the public service continued to occur with impunity [translation] “due to a lack of evidence and an ineffective judicial system”.

#### 30863:1:subtheme:5 · paragraphs 13-15

- Raw key terms: `mexico, protection, state, account, applicant, cases, corruption, december`
- Display key terms: `mexico, protection, state, account, cases, corruption, december`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: mexico, protection, state, account, cases, corruption, december Position/evidence statements: [13] Further, although human rights commissions have a general mandate to investigate complaints against public service employees and “issue non-binding recommendations to the public prosecution or any other public insti | [15] Accordingly, the applicant submitted that the documentary evidence in the record is “clear and convincing” and demonstrates the scope of corruption in Mexico both in political and judicial institutions and in the po Application context: [15] Accordingly, the applicant submitted that the documentary evidence in the record is “clear and convincing” and demonstrates the scope of corruption in Mexico both in political and judicial institutions and in the po Evidence spans paragraphs 13-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5436430` offsets `135-140`; context: [13] Further, although human rights commissions have a general mandate to investigate complaints against public service employees and “issue non-binding recommendations to the public prosecution or any other public institution whose public servants were allegedly involved in the violation”, the applicant submitted that the latter [translation] “do not have the necessary authority to prosecute persons for crimes”: see MEX43164.
- Evidence: `party_position` cue `submitted` at chunk `5436430` offsets `306-315`; context: [13] Further, although human rights commissions have a general mandate to investigate complaints against public service employees and “issue non-binding recommendations to the public prosecution or any other public institution whose public servants were allegedly involved in the violation”, the applicant submitted that the latter [translation] “do not have the necessary authority to prosecute persons for crimes”: see MEX43164.
- Evidence: `party_position` cue `submitted` at chunk `5436432` offsets `32-41`; context: [15] Accordingly, the applicant submitted that the documentary evidence in the record is “clear and convincing” and demonstrates the scope of corruption in Mexico both in political and judicial institutions and in the police.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436432` offsets `63-71`; context: [15] Accordingly, the applicant submitted that the documentary evidence in the record is “clear and convincing” and demonstrates the scope of corruption in Mexico both in political and judicial institutions and in the police.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5436432` offsets `5-16`; context: [15] Accordingly, the applicant submitted that the documentary evidence in the record is “clear and convincing” and demonstrates the scope of corruption in Mexico both in political and judicial institutions and in the police.

#### 30863:1:subtheme:6 · paragraphs 16-21

- Raw key terms: `canada, board, immigration, state, citizenship, court, decision, evidence`
- Display key terms: `state`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: state Position/evidence statements: [16] The respondent submitted that state protection is essentially a question of fact. | [17] The respondent submitted that the Board’s decision should not be set aside, since it was based on the evidence in the record and was reasonable. Application context: The respondent submitted that the applicant has not shown that the Board’s conclusion was patently unreasonable, or alternatively if it is the standard of reasonableness simpliciter which applies, that the intervention o | It is true that in the impugned decision the expression of the test in Ward leaves something to be desired, but what is important is that, concretely, the Court be satisfied that the Board fully understood and applied th Evidence spans paragraphs 16-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5436433` offsets `69-77`; context: [16] The respondent submitted that state protection is essentially a question of fact.
- Evidence: `party_position` cue `submitted` at chunk `5436433` offsets `20-29`; context: [16] The respondent submitted that state protection is essentially a question of fact.
- Evidence: `reasoning_application` cue `applies` at chunk `5436433` offsets `357-364`; context: The respondent submitted that the applicant has not shown that the Board’s conclusion was patently unreasonable, or alternatively if it is the standard of reasonableness simpliciter which applies, that the intervention of the Court is warranted in this case: see Mendoza v.
- Evidence: `party_position` cue `submitted` at chunk `5436434` offsets `20-29`; context: [17] The respondent submitted that the Board’s decision should not be set aside, since it was based on the evidence in the record and was reasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436434` offsets `107-115`; context: [17] The respondent submitted that the Board’s decision should not be set aside, since it was based on the evidence in the record and was reasonable.
- Evidence: `reasoning_application` cue `applied` at chunk `5436434` offsets `491-498`; context: It is true that in the impugned decision the expression of the test in Ward leaves something to be desired, but what is important is that, concretely, the Court be satisfied that the Board fully understood and applied the test.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5436434` offsets `150-158`; context: Although the reasons in support of the decision are not extensive, those given in this case can stand up to a careful examination.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436435` offsets `44-52`; context: [18] From its assessment of the documentary evidence, the Board could reasonably find that a legal framework existed that was capable of protecting Mexican nationals.
- Evidence: `party_position` cue `argued` at chunk `5436436` offsets `20-26`; context: [19] The respondent argued it was not reasonable for a refugee protection claimant seeking to rebut the presumption of state protection to say that no approach had been made to the police simply because corruption existed.
- Evidence: `reasoning_application` cue `because` at chunk `5436436` offsets `195-202`; context: [19] The respondent argued it was not reasonable for a refugee protection claimant seeking to rebut the presumption of state protection to say that no approach had been made to the police simply because corruption existed.
- Evidence: `party_position` cue `submitted` at chunk `5436437` offsets `259-268`; context: It therefore does not have to specify in its decision all the points of documentary evidence it may have considered before finding, as it did, that the applicant had not submitted “clear and convincing evidence” that the Mexican government was unable to protect him.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436437` offsets `69-77`; context: [20] Further, it must be assumed that the Board has reviewed all the evidence of record.
- Evidence: `reasoning_application` cue `therefore` at chunk `5436437` offsets `92-101`; context: It therefore does not have to specify in its decision all the points of documentary evidence it may have considered before finding, as it did, that the applicant had not submitted “clear and convincing evidence” that the Mexican government was unable to protect him.
- Evidence: `reasoning_application` cue `because` at chunk `5436438` offsets `2204-2211`; context: (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
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

#### 30863:1:subtheme:7 · paragraphs 22-23

- Raw key terms: `according, board, case, protection, review, state, therefore, accomplice`
- Display key terms: `according, case, protection, review, state, therefore, accomplice`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: according, case, protection, review, state, therefore, accomplice Position/evidence statements: In this case, the applicant argued it was reasonable not to file charges with the police because of the reprisals he would probably suffer, especially as [translation] “everything is corrupt in Mexico” and “the authoriti Rule/authority context: ) (QL), Madam Justice Danièle Tremblay-Lamer held, after making an exhaustive review of the case law and of the pragmatic and functional tests, that the standard of review applicable to questions relating to state protec Application context: The only point really at issue in this case, therefore, is that of state protection in a situation where it is not the persecuting agent nor an accomplice in the crimes allegedly committed by the persecuting agent, accor | Therefore, if any of the reasons for dismissing the protection application can stand up to a somewhat probing examination, then the decision is not unreasonable and this Court should not intervene in the case: see Law So Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5436439` offsets `345-350`; context: The only point really at issue in this case, therefore, is that of state protection in a situation where it is not the persecuting agent nor an accomplice in the crimes allegedly committed by the persecuting agent, according to the applicant.
- Evidence: `party_position` cue `argued` at chunk `5436439` offsets `591-597`; context: In this case, the applicant argued it was reasonable not to file charges with the police because of the reprisals he would probably suffer, especially as [translation] “everything is corrupt in Mexico” and “the authorities [in Mexico] do not protect people who have political connections and are against them” (applicant’s testimony, hearing transcripts of May 31, 2005, certified record, at pages 237 et seq.
- Evidence: `evidence_fact` cue `testimony` at chunk `5436439` offsets `886-895`; context: In this case, the applicant argued it was reasonable not to file charges with the police because of the reprisals he would probably suffer, especially as [translation] “everything is corrupt in Mexico” and “the authorities [in Mexico] do not protect people who have political connections and are against them” (applicant’s testimony, hearing transcripts of May 31, 2005, certified record, at pages 237 et seq.
- Evidence: `reasoning_application` cue `therefore` at chunk `5436439` offsets `365-374`; context: The only point really at issue in this case, therefore, is that of state protection in a situation where it is not the persecuting agent nor an accomplice in the crimes allegedly committed by the persecuting agent, according to the applicant.
- Evidence: `issue` cue `question` at chunk `5436440` offsets `888-896`; context: Further, the particular interpretation given by the Board of law and precedent raises a question of law which, of course, must be considered according to the correctness standard: paragraph 18.
- Evidence: `governing_rule` cue `standard of review` at chunk `5436440` offsets `281-299`; context: ) (QL), Madam Justice Danièle Tremblay-Lamer held, after making an exhaustive review of the case law and of the pragmatic and functional tests, that the standard of review applicable to questions relating to state protection is that of reasonableness simpliciter.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5436440` offsets `510-519`; context: Therefore, if any of the reasons for dismissing the protection application can stand up to a somewhat probing examination, then the decision is not unreasonable and this Court should not intervene in the case: see Law Society of New Brunswick v.

#### 30863:1:subtheme:8 · paragraphs 24-25

- Raw key terms: `added, country, emphasis, protection, refugee, additional, address, adopts`
- Display key terms: `added, country, emphasis, protection, refugee, additional, address, adopts`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: added, country, emphasis, protection, refugee, additional, address, adopts Rule/authority context: [24] The general principles governing state protection developed by the courts in applying the old Immigration Act, R. Application context: Nevertheless, in his testimony, in response to a question from the refugee protection officer about attempts by him to live elsewhere in Mexico, the applicant answered in the negative: [translation] “If I had lived in an Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5436441` offsets `230-237`; context: I‑2, as amended and subsequently repealed (the old Act), continue to be applicable in determining whether a person is a “Convention refugee” under section 96 of the Act.
- Evidence: `governing_rule` cue `principles` at chunk `5436441` offsets `17-27`; context: [24] The general principles governing state protection developed by the courts in applying the old Immigration Act, R.
- Evidence: `issue` cue `question` at chunk `5436442` offsets `267-275`; context: Nevertheless, in his testimony, in response to a question from the refugee protection officer about attempts by him to live elsewhere in Mexico, the applicant answered in the negative: [translation] “If I had lived in another town and had asked for protection, it would have been the same thing, it was not worth the trouble of filing charges, because in my country there is no democracy or protection for people who oppose the country’s policies” (emphasis added).
- Evidence: `evidence_fact` cue `testimony` at chunk `5436442` offsets `239-248`; context: Nevertheless, in his testimony, in response to a question from the refugee protection officer about attempts by him to live elsewhere in Mexico, the applicant answered in the negative: [translation] “If I had lived in another town and had asked for protection, it would have been the same thing, it was not worth the trouble of filing charges, because in my country there is no democracy or protection for people who oppose the country’s policies” (emphasis added).
- Evidence: `reasoning_application` cue `because` at chunk `5436442` offsets `562-569`; context: Nevertheless, in his testimony, in response to a question from the refugee protection officer about attempts by him to live elsewhere in Mexico, the applicant answered in the negative: [translation] “If I had lived in another town and had asked for protection, it would have been the same thing, it was not worth the trouble of filing charges, because in my country there is no democracy or protection for people who oppose the country’s policies” (emphasis added).
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `5436442` offsets `218-230`; context: Nevertheless, in his testimony, in response to a question from the refugee protection officer about attempts by him to live elsewhere in Mexico, the applicant answered in the negative: [translation] “If I had lived in another town and had asked for protection, it would have been the same thing, it was not worth the trouble of filing charges, because in my country there is no democracy or protection for people who oppose the country’s policies” (emphasis added).

#### 30863:1:subtheme:9 · paragraphs 26-27

- Raw key terms: `board, claimant, country, order, paragraphs, protection, refugee, risk`
- Display key terms: `country, order, paragraphs, protection, refugee, risk`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: country, order, paragraphs, protection, refugee, risk Position/evidence statements: [27] In order to determine whether a refugee protection claimant has discharged his burden of proof, the Board must undertake a proper analysis of the situation in the country and the particular reasons why the protectio Application context: [27] In order to determine whether a refugee protection claimant has discharged his burden of proof, the Board must undertake a proper analysis of the situation in the country and the particular reasons why the protectio Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5436443` offsets `12-20`; context: [26] On the question of government protection, the Ward test expressly requires careful review of the fear of persecution from the standpoint of the refugee protection claimant and the objective conditions of the country in question.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436443` offsets `509-517`; context: The risk that this presumption will be too broad in its application is limited by the requirement of clear and convincing evidence that the state is unable to provide protection.
- Evidence: `issue` cue `whether` at chunk `5436444` offsets `27-34`; context: [27] In order to determine whether a refugee protection claimant has discharged his burden of proof, the Board must undertake a proper analysis of the situation in the country and the particular reasons why the protection claimant submits that he is “unable or, because of that risk, unwilling to avail [himself] of the protection” of his country of nationality or habitual residence (paragraphs 96(a) and (b) and subparagraph 97(1)(b)(i) of the Act).
- Evidence: `party_position` cue `submits` at chunk `5436444` offsets `231-238`; context: [27] In order to determine whether a refugee protection claimant has discharged his burden of proof, the Board must undertake a proper analysis of the situation in the country and the particular reasons why the protection claimant submits that he is “unable or, because of that risk, unwilling to avail [himself] of the protection” of his country of nationality or habitual residence (paragraphs 96(a) and (b) and subparagraph 97(1)(b)(i) of the Act).
- Evidence: `reasoning_application` cue `because` at chunk `5436444` offsets `262-269`; context: [27] In order to determine whether a refugee protection claimant has discharged his burden of proof, the Board must undertake a proper analysis of the situation in the country and the particular reasons why the protection claimant submits that he is “unable or, because of that risk, unwilling to avail [himself] of the protection” of his country of nationality or habitual residence (paragraphs 96(a) and (b) and subparagraph 97(1)(b)(i) of the Act).

#### 30863:1:subtheme:10 · paragraphs 28-30

- Raw key terms: `nationals, protect, protection, state, supra, able, agent, applicant`
- Display key terms: `nationals, protect, protection, state, supra, able, agent`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: nationals, protect, protection, state, supra, able, agent Rule/authority context: When, as in this case, the applicant fears the persecution of a person who is not an agent of the state, the Board must inter alia examine the motivation of the persecuting agent and his ability to go after the applicant Application context: Therefore, it will not suffice for the applicant to show that his government was not always able to protect persons in his position (Villafranca, supra, at paragraph 7). | [29] Accordingly, when the government is not the persecuting agent, and even when it is a democratic state, it is still open to an applicant to adduce evidence showing clearly and convincingly that it is unable or does n Evidence spans paragraphs 28-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5436445` offsets `772-780`; context: In my opinion, this is a question of fact which does not have to be answered in absolute terms.
- Evidence: `governing_rule` cue `under` at chunk `5436445` offsets `1559-1564`; context: When, as in this case, the applicant fears the persecution of a person who is not an agent of the state, the Board must inter alia examine the motivation of the persecuting agent and his ability to go after the applicant locally or throughout the country, which may raise the question of the existence of internal refuge and its reasonableness (at least in connection with the analysis conducted under section 96 of the Act).
- Evidence: `reasoning_application` cue `Therefore` at chunk `5436445` offsets `156-165`; context: Therefore, it will not suffice for the applicant to show that his government was not always able to protect persons in his position (Villafranca, supra, at paragraph 7).
- Evidence: `evidence_fact` cue `evidence` at chunk `5436446` offsets `151-159`; context: [29] Accordingly, when the government is not the persecuting agent, and even when it is a democratic state, it is still open to an applicant to adduce evidence showing clearly and convincingly that it is unable or does not really wish to protect its nationals in certain types of situation: see Annan v.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5436446` offsets `5-16`; context: [29] Accordingly, when the government is not the persecuting agent, and even when it is a democratic state, it is still open to an applicant to adduce evidence showing clearly and convincingly that it is unable or does not really wish to protect its nationals in certain types of situation: see Annan v.
- Evidence: `counterargument_limitation` cue `although` at chunk `5436446` offsets `777-785`; context: It should be borne in mind that most countries might be prepared to try to provide protection, although an objective assessment could establish that they are not in fact able to do so in practice.
- Evidence: `evidence_fact` cue `found that` at chunk `5436447` offsets `81-91`; context: [30] At the same time, Kadenko, supra, indicates that it cannot be automatically found that a state is unable to protect one of its nationals when he has sought police protection and certain police officers refused to intervene to help him.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5436447` offsets `794-803`; context: Therefore, it would be an error of law to adopt a “systemic” approach as to the protection offered to the nationals of a given country.

#### 30863:1:subtheme:11 · paragraphs 31-33

- Raw key terms: `applicant, board, canada, cannot, circumstances, citizenship, criminal, decision`
- Display key terms: `cannot, circumstances, criminal`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: cannot, circumstances, criminal Rule/authority context: For example, although the Board held that section 96 of the Act did not apply in the case at bar, it is not clear from reading its reasons that it actually analyzed the personal risk the applicant would face if he were r Application context: Therefore, the degree to which a state tolerates corruption in the political or judicial apparatus correspondingly diminishes its degree of democracy. | Further, because of the laconic nature of the reasons for dismissal contained in the decision, it cannot stand up to somewhat probing examination. Evidence spans paragraphs 31-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `5436448` offsets `5-12`; context: [31] Whether the issue be the best interest of the democratic state in question and of civil society in general, or the individual interest of the victim or perpetrator of an alleged criminal offence, the payment of a monetary or other benefit of any kind to a police or law officer is illegal.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436448` offsets `1309-1317`; context: That being said, I do not have to decide here whether the documentary evidence established, as the applicant vigorously claimed, such a degree of corruption that it can be said it was not unreasonable in the circumstances for the applicant not to approach the police of his country before seeking international protection.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5436448` offsets `1088-1097`; context: Therefore, the degree to which a state tolerates corruption in the political or judicial apparatus correspondingly diminishes its degree of democracy.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436449` offsets `243-251`; context: It is not sufficient for the Board to indicate in its decision that it considered all the documentary evidence.
- Evidence: `governing_rule` cue `under` at chunk `5436449` offsets `1006-1011`; context: For example, although the Board held that section 96 of the Act did not apply in the case at bar, it is not clear from reading its reasons that it actually analyzed the personal risk the applicant would face if he were returned to Mexico in terms of each of the specific tests and of the burden of proof applicable under section 97 of the Act: see Li, supra; Kandiah v.
- Evidence: `reasoning_application` cue `because` at chunk `5436449` offsets `553-560`; context: Further, because of the laconic nature of the reasons for dismissal contained in the decision, it cannot stand up to somewhat probing examination.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5436449` offsets `642-648`; context: Further, because of the laconic nature of the reasons for dismissal contained in the decision, it cannot stand up to somewhat probing examination.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5436450` offsets `299-308`; context: Therefore, the Board could not simply state that if the claimant’s appeal to the police were made in vain, he could have appealed to the CNDH and the CEDH, two organizations concerned with human rights.

#### 30863:1:subtheme:12 · paragraphs 34-35

- Raw key terms: `board, case, decision, evidence, fact, finding, given, government`
- Display key terms: `case, fact, finding, given, government`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: case, fact, finding, given, government Application context: The Board simply noted cryptically that the applicant “stated that he did not want to file a complaint because it was unnecessary, given that all those organizations are garbage and that everything in Mexico is corrupt”. | The same applies to a host of other relevant documents which were part of the National Documentation Package on Mexico that were not considered by the Board. Evidence spans paragraphs 34-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5436451` offsets `154-162`; context: Now, the question is not so much whether remedies exist against corrupt public servants in Mexico, but is to determine whether in practice those remedies are useful in the circumstances.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436451` offsets `843-851`; context: In addition, the Board ignored the fact that the applicant did not want to file any complaint with the authorities of his country for fear of reprisals and that his persecuting agent was a political organizer linked to the PRI, which might give rise to doubts as to the “incriminating” nature of evidence regarding the persecuting agent.
- Evidence: `reasoning_application` cue `because` at chunk `5436451` offsets `988-995`; context: The Board simply noted cryptically that the applicant “stated that he did not want to file a complaint because it was unnecessary, given that all those organizations are garbage and that everything in Mexico is corrupt”.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436452` offsets `99-107`; context: [35] The Board’s role was to make findings of fact and arrive at a reasonable finding based on the evidence, even if conflicting.
- Evidence: `reasoning_application` cue `applies` at chunk `5436452` offsets `1002-1009`; context: The same applies to a host of other relevant documents which were part of the National Documentation Package on Mexico that were not considered by the Board.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5436452` offsets `223-229`; context: The Board cannot, without giving reasonable grounds, ignore or dismiss the content of a document dealing expressly with state protection in a given region (Renteria et al.

#### 30863:1:subtheme:13 · paragraphs 36-37

- Raw key terms: `applicant, board, decision, make, another, arbitrarily, arguments, back`
- Display key terms: `make, another, arbitrarily, arguments, back`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: make, another, arbitrarily, arguments, back Application context: [37] All these errors make the decision unreasonable; therefore, it should be quashed by this Court, and the applicant’s case should be referred back to the Board for re-hearing and re-determination by another member. Operative outcome context: [37] All these errors make the decision unreasonable; therefore, it should be quashed by this Court, and the applicant’s case should be referred back to the Board for re-hearing and re-determination by another member. Evidence spans paragraphs 36-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5436453` offsets `34-41`; context: [36] I do not have to decide here whether Mexico is capable of protecting its nationals.
- Evidence: `evidence_fact` cue `evidence` at chunk `5436453` offsets `193-201`; context: I do not have to substitute my judgment for that of the Board and make specific findings of fact on the evidence as a whole.
- Evidence: `reasoning_application` cue `therefore` at chunk `5436454` offsets `54-63`; context: [37] All these errors make the decision unreasonable; therefore, it should be quashed by this Court, and the applicant’s case should be referred back to the Board for re-hearing and re-determination by another member.
- Evidence: `disposition` cue `quashed` at chunk `5436454` offsets `78-85`; context: [37] All these errors make the decision unreasonable; therefore, it should be quashed by this Court, and the applicant’s case should be referred back to the Board for re-hearing and re-determination by another member.

#### 30863:1:subtheme:14 · paragraphs 38-38

- Raw key terms: `allowed, application, certification, counsel, general, importance, question, suggested`
- Display key terms: `allowed, certification, importance, question, suggested`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: allowed, certification, importance, question, suggested Application context: [38] This application must therefore be allowed. Operative outcome context: [38] This application must therefore be allowed. Evidence spans paragraphs 38-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5436455` offsets `70-78`; context: Counsel suggested no question of general importance for certification.
- Evidence: `reasoning_application` cue `therefore` at chunk `5436455` offsets `27-36`; context: [38] This application must therefore be allowed.
- Evidence: `disposition` cue `allowed` at chunk `5436455` offsets `40-47`; context: [38] This application must therefore be allowed.

#### Section text

Vigueras Avila v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2006-03-20
Neutral citation
2006 FC 359
File numbers
IMM-4106-05
Notes
Digest
Decision Content
Date: 20060320
Docket: IMM-4106-05
Citation: 2006 FC 359
Ottawa, Ontario, the 20th day of March 2006
PRESENT: THE HONOURABLE MR. JUSTICE MARTINEAU
BETWEEN:
CRISTIAN MARCEL VIGUERAS AVILA
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR ORDER AND ORDER

[1] The applicant is a citizen of Mexico. He claimed that the authorities in his country could not protect him from the persecution which he fears primarily from one José Antonio Lemus (the persecuting agent) for whom he worked in the local office of the Institutional Revolutionary Party (IRP) in Mexico when he was studying industrial engineering. The applicant alleged that the persecuting agent threatened him with death and that ruffians working for him tried to extort money from him and kidnapped him and beat him, and an attempt was made to set fire to the family house where he lived after he had discovered that the persecuting agent was directly involved in the illegal financing of the democratic organization of technical students (DOTS), suspected of committing acts of sabotage and vandalism for the IRP. The applicant made the persecuting agent aware that he knew about these illegal payments and wished to take his distance from the latter. Before ceasing working for the persecuting agent, the applicant made copies of certain documents which apparently incriminated the latter.

[2] The applicant’s refugee claim was dismissed by the Refugee Protection Division of the Immigration and Refugee Board (the Board); hence this application for judicial review.
BOARD’S DECISION

[3] In the very succinct reasons (two and a half pages) provided in this matter, the Board did not question the applicant’s credibility and concluded that he had [translation] “definitely been the victim of personal revenge”. However, in order to be recognized as a “Convention refugee”, a person must show that he reasonably feared persecution in relation to one of the five grounds listed in the definition. In view of the fact that, in the Board’s opinion, the death threats made against the applicant were prompted by personal revenge on the part of the persecuting agent (and not related to the alleged political opinions of the applicant), therefore, there had been no “persecution” within the meaning of section 96 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (the Act).

[4] The Board also considered that “the claimant has not discharged the burden of proof on him to rebut the presumption that the authorities in his country are unable to protect him, by providing clear and convincing evidence in this respect” (emphasis added). In this case, since the Mexican government is not the persecuting agent, the applicant should have exhausted all existing remedies before claiming protection in Canada: “if he had no success [with the police], he could have appealed to the CNDH [National Human Rights Commission] and the CEDH [Government Human Rights Commission], which investigate complaints”. The Board based its decision on Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689, and Kadenko v. Canada (Minister of Citizenship and Immigration), (1996) D.L.R. (4th) 532 (F.C.A.), [1996] F.C.J. No. 1376 (QL).

[5] Therefore, the Board concluded that the applicant was neither a “Convention refugee” nor a “person in need of protection” within the meaning of sections 96 and 97 of the Act.
APPLICANT’S ARGUMENTS

[6] In this case, the applicant objected primarily to the finding of the Board as to the Mexican government’s ability to protect him.

[7] The applicant challenged, first, the sufficiency of the reasons given in this matter, as they did not allow the Court to determine whether the Board derived its general finding from the evidence in the record as a whole, while taking the applicant’s personal situation into account. The applicant argued that he had good reason not to want to seek protection in his country because of the degree of corruption existing there at all levels and the reprisals to which he would have been exposed if he had filed a complaint with the Mexican authorities. The Board arbitrarily rejected the applicant’s explanations without taking all the documentary evidence and his testimony into account. Further, as to the application and scope of the test pertaining to government protection, the applicant submitted that the Board misunderstood and misapplied Ward and Kadenko. In the circumstances of this case, the Board’s finding that the applicant should have first approached the police is said to be unreasonable.

[8] The applicant noted that the Board must weigh all the evidence as a whole, not examine each part in isolation: Owusu v. Canada (Minister of Employment and Immigration), [1989] F.C.J. No. 33 (F.C.A.) (QL); Lai v. Canada (Minister of Employment and Immigration) (1989), 8 Imm. L.R. (2d) 245 (F.C.A.); and Hilo v. Canada (Minister of Employment and Immigration) (1991), 15 Imm. L.R. (2d) 199 (F.C.A.).

[9] Therefore, the applicant reproached the Board for not having mentioned or discussed in its decision the evidence that did corroborate his testimony that corruption is widespread in Mexico and that in such a case it is pointless to contact the police. What is at issue here is the reporting of crimes committed by an influential political figure and by the henchmen in his pay. In particular, the applicant drew this Court’s attention to the U.S. Country Reports on Human Rights Practices dealing with Mexico, which were not referred to in the decision. Certain portions of the 2004 report are very critical of the Mexican government. In particular, it is indicated that corruption is widespread in the Mexican police and exists to a lesser extent in the army. Murders and kidnappings of individuals are common and are a real problem; according to an unofficial figure, 3,000 kidnappings occur annually. Further, the police is at times involved in kidnappings, armed robberies, acts of extortion and the protection of criminals and drug traffickers. Several suspects are not charged or are released after paying bribes. The Mexican police are also reproached with torturing suspects to obtain confessions. Further, the courts continue to admit in evidence statements obtained under torture. Even though the Mexican government has taken punitive measures against the police or members of the army, impunity remains a problem. Despite the reforms undertaken in the judiciary, the long delays, the absence of due process, judicial incompetence and corruption persist. Indeed, because of these problems, many victims fear filing complaints against the police. The fact is that police officers suspected of corruption are not often prosecuted. In short, a number of individuals have no confidence in the legal system and are very hesitant to file official complaints: see U.S., U.S. Department of State, Bureau of Democracy, Human Rights and Labor, Country Reports on Human Rights Practices 2004: Mexico (February 28, 2005).

[10] The applicant further argued that a majority of crimes are not reported in Mexico simply because people do not trust the police and fear reprisals if they report criminals. The applicant submitted that this was a factor the Board should have taken into account when it determined whether the claimant’s refusal to file a complaint with the police was reasonable in the circumstances. Thus, in one of the documents not mentioned by the Board in its decision, the crime rate for crimes under the law of the several Mexican states is said to have diminished by 1% while federal crimes allegedly increased by 1%. However, several information sources claim that the official statistics do not reflect the reality as many persons are hesitant to report crimes. According to various estimates, the proportion of unreported crimes, sometimes referred to as the [translation] “black number” (la cifra negra) is between 75% and 80%, which would mean that only one crime in four or five is reported to the police: see Canada, Research Directorate, Immigration and Refugee Board, Mexico: State Protection (December 2003 - March 2005), Ottawa, 2005, at pages 22-23.

[11] The applicant also challenged the reasonableness of the finding by the Board that “if he had no success [with the police], he could have appealed to the CNDH [National Human Rights Commission] and the CEDH [Government Human Rights Commission], which investigate complaints”. In this regard, the applicant submitted that the Board picked and chose in the documentary evidence. In the impugned decision, the Board only referred to the following two documents: Canada, Research Directorate, Immigration and Refugee Board, MEX36332.EF, Procedure to file a complaint with the Federal Prosecutor Office and to obtain copies of a filed complaint, Ottawa, March 26, 2001, and Canada, Research Branch, Immigration and Refugee Board, MEX43164.EF, List of government-funded institutions that assist those having difficulty obtaining state protection, Ottawa, November 18, 2004.

[12] For example, the Center for Public Integrity (CPI) recently noted that, in some cases, corruption in the public service continued to occur with impunity [translation] “due to a lack of evidence and an ineffective judicial system”. Thus, according to the documentary evidence not referred to by the Board in its decision, it appeared that, by October 2004, the Government of Mexico had not yet provided information on public service employees who had actually served a term of imprisonment between December 2000 and 2003 for convictions on charges of corruption: see Canada, Research Directorate, Immigration and Refugee Board, MEX42663.EF, Possible recourse for victims of bribery demands/corruption by government officials federally, in the Federal District and in the states of Guanajuato, Jalisco, Mexico, Michoacan, Puebla, Queretaro, Veracruz and Yucatan, including agencies to which such corruption can be reported and protection available (2003 - September 2004), Ottawa, October 1, 2004.

[13] Further, although human rights commissions have a general mandate to investigate complaints against public service employees and “issue non-binding recommendations to the public prosecution or any other public institution whose public servants were allegedly involved in the violation”, the applicant submitted that the latter [translation] “do not have the necessary authority to prosecute persons for crimes”: see MEX43164.EF, supra. Similarly, an OECD report mentions that while the federal government has made efforts to make the people aware of corruption and prevent it, the same cannot be said with respect to the implementation of the law and the bringing of prosecutions. Persons responsible for applying the law in Mexico admit that they encounter difficulty to press charges in corruption cases on account of problems of detection (caused in part by a lack of resources and training) and investigation: see OECD, Mexico: Phase 2. Report on the Application of the Convention on Combating Bribery of Foreign Public Officials in International Business Transactions and the 1997 Recommendations on Combating Bribery in International Business Transactions (September 2, 2004), mentioned in Mexico: State Protection (December 2003 - March 2005), supra, at page 26.

[14] Also in 2004, the media and human rights advocates noted the following regularly recurring problems: police misconduct, arbitrary detention and vigilante justice carried out by private individuals who do not trust the police: see Mexico: State Protection (December 2003 - March 2005), supra, at pages 8-9.

[15] Accordingly, the applicant submitted that the documentary evidence in the record is “clear and convincing” and demonstrates the scope of corruption in Mexico both in political and judicial institutions and in the police. From an objective standpoint, such corruption affects the ability of the state institutions to provide protection for nationals in cases such as his own. Here, the persecuting agent was a political organizer for the PRI, the party which was in power in Mexico for 70 years. The applicant was already threatened, kidnapped and beaten by members of the DOTS. The applicant stated that attempts were also made to set the family home on fire: two neighbours saw two young people he rightly suspected of being thugs employed by the persecuting agent throw a cracker at the wall of the family home. In the event of possible reprisals, the Mexican police could do nothing to protect him. The applicant’s fear of persecution should be assessed prospectively. If the applicant were to return to Mexico, he would be at risk everywhere in that country. In this case, the Board simply failed to take all the evidence into account and this makes its decision unreasonable.
RESPONDENT’S ARGUMENTS

[16] The respondent submitted that state protection is essentially a question of fact. In this case, the applicant just did not agree with the Board’s findings of fact. The respondent submitted that the applicant has not shown that the Board’s conclusion was patently unreasonable, or alternatively if it is the standard of reasonableness simpliciter which applies, that the intervention of the Court is warranted in this case: see Mendoza v. Canada (Minister of Citizenship and Immigration), 2005 FC 634, [2005] F.C.J. No. 772 (F.C.) (QL).

[17] The respondent submitted that the Board’s decision should not be set aside, since it was based on the evidence in the record and was reasonable. Although the reasons in support of the decision are not extensive, those given in this case can stand up to a careful examination. It is true that in the impugned decision the expression of the test in Ward leaves something to be desired, but what is important is that, concretely, the Court be satisfied that the Board fully understood and applied the test. In all countries, individuals are victims of various types of crime everyday. Kidnappings and acts of extortion also occur in Canada. This is why various countries have taken steps to ensure that offenders will be tracked down by the police and punished by the courts. As the Board noted in its decision, Mexico is a democratic country. In these circumstances, where the state has not completely collapsed, it must be assumed that the Mexican government is in a position to protect its nationals (Canada (Department of Employment and Immigration) v. Villafranca, [1992] F.C.J. No. 1189 (F.C.A.) (QL); Ward, supra; Kadenko, supra).

[18] From its assessment of the documentary evidence, the Board could reasonably find that a legal framework existed that was capable of protecting Mexican nationals. In this respect, the Board noted in its decision the existence of a federal preventive police force, state and municipal police forces, a federal investigation agency, a federal attorney general, courts and an army.

[19] The respondent argued it was not reasonable for a refugee protection claimant seeking to rebut the presumption of state protection to say that no approach had been made to the police simply because corruption existed. Moreover, several judgments of this Court indicate that the government of Mexico is able to protect its nationals: Velazquez v. Canada (Minister of Citizenship and Immigration), [1999] F.C.J. No. 934 (F.C.T.D.) (QL); Garcia v. Canada (Minister of Citizenship and Immigration), 2004 FC 1699, [2004] F.C.J. No. 2058 (F.C.) (QL); Urgel v. Canada (Minister of Citizenship and Immigration), 2004 FC 1777, [2004] F.C.J. No. 2171 (F.C.) (QL); Valdes v. Canada (Minister of Citizenship and Immigration), 2005 FC 93, [2005] F.C.J. No. 123 (F.C.) (QL); Balderas v. Canada (Minister of Citizenship and Immigration), 2005 FC 157, [2005] F.C.J. No. 225 (F.C.) (QL); B.O.T. v. Canada (Minister of Citizenship and Immigration), 2005 FC 284, [2005] F.C.J. No. 343 (F.C.) (QL).

[20] Further, it must be assumed that the Board has reviewed all the evidence of record. It therefore does not have to specify in its decision all the points of documentary evidence it may have considered before finding, as it did, that the applicant had not submitted “clear and convincing evidence” that the Mexican government was unable to protect him. It will suffice if the record contains evidence to support the Board’s general finding. Further, the Board could prefer some documentary evidence to the applicant’s testimony (Zhou v. Canada (Minister of Employment and Immigration), [1994] F.C.J. No. 1087 (F.C.A.) (QL); Bustamante v. Canada (Minister of Citizenship and Immigration), 2002 FCTD 499, [2002] F.C.J. No. 643 (F.C.T.D.) (QL); Ortiz Vergara v. Canada (Minister of Employment and Immigration), [1994] F.C.J. No. 1164 (F.C.T.D.) (QL)).
APPLICABLE LEGISLATION

[21] Sections 96 and 97 of the Act read as follows:
96. A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
96. A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
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
(iv) the risk is not caused by the inability of that coun

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 30863:2 · paragraphs 39-40

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `143fcc2c32f5f2744c740adece744c5fabd9469ff21f0cd091a93ab7492a6140`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 30863:2:subtheme:1 · paragraphs 39-40

- Raw key terms: `allows, another, applicant, application, aside, avila, back, board`
- Display key terms: `allows, another, aside, avila, back`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: allows, another, aside, avila, back No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 39-40. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
THE COURT ALLOWS the application for judicial review, sets aside the decision of June 8, 2005 and refers the applicant’s case back to the Board for re-hearing and re-determination by another member. No question of general importance will be certified by the Court.
“Luc Martineau”
Judge
Certified true translation
François Brunet, LLB, BCL
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-4106-05
STYLE OF CAUSE: CRISTIAN MARCEL VIGUERAS AVILA
v.
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Montréal, Quebec
DATE OF HEARING: February 14, 2006
REASONS FOR 

## 30863:3 · paragraphs 41-41

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e9af434e2995592f6f90fb0097f80ce85b62e823046acb1196d952e75490dbb9`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 30863:3:subtheme:1 · paragraphs 41-41

- Raw key terms: `appearances, applicant, attorney, bell, canada, dated, deputy, eveline`
- Display key terms: `bell, dated, deputy, eveline`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: bell, dated, deputy, eveline No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 41-41. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
AND ORDER BY: The Honourable Mr. Justice Martineau
DATED: March 20, 2006
APPEARANCES:
Evelyne Fiset
FOR THE APPLICANT
Steve Bell
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Eveline Fiset
Montréal, Quebec
FOR THE APPLICANT
John H. Sims, Q.C.
Deputy Attorney General of Canada
Montréal, Quebec
FOR THE RESPONDENT
