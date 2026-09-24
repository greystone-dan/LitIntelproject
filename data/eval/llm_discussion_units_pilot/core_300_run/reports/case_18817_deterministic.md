# Discussion Units: case 18817

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **50**
- Continuity pairs: **49**
- Discussion Units: **4**
- Paragraph source hashes: **50**
- Sub-themes: **15**

## 18817:1 · paragraphs 0-16

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f8cf9ccfb10f3461214e49894e94a4f80d4d03c1393f5643fe96d9c73eaf7d0e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 18817:1:subtheme:1 · paragraphs 0-7

- Raw key terms: `gabor, applicants, attack, gaborova, police, able, attacked, attended`
- Display key terms: `gabor, attack, gaborova, police, able, attacked, attended`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, reasoning_application Display terms: gabor, attack, gaborova, police, able, attacked, attended Rule/authority context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S. Application context: The doctor examined him and gave him painkillers, but was unwilling to confirm the attack sustained by the Applicant because he stated that “it’s you gypsies who are always making up stories. | Gaborova has also experienced persecution because of her ethnicity. Evidence spans paragraphs 0-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `4892660` offsets `277-292`; context: 27 (Act) for judicial review of a decision of the Refugee Protection Division (RPD) of the Immigration and Refugee Board, dated June 19, 2009, (Decision) which determined that the Applicants are not Convention refugees or persons in need of protection pursuant to sections 96 and 97 of the Act.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4892660` offsets `27-38`; context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `counterargument_limitation` cue `However` at chunk `4892662` offsets `229-236`; context: However, as a self-employed painter he was only able to acquire occasional and seasonal work.
- Evidence: `reasoning_application` cue `because` at chunk `4892664` offsets `481-488`; context: The doctor examined him and gave him painkillers, but was unwilling to confirm the attack sustained by the Applicant because he stated that “it’s you gypsies who are always making up stories.
- Evidence: `reasoning_application` cue `because` at chunk `4892666` offsets `50-57`; context: Gaborova has also experienced persecution because of her ethnicity.

#### 18817:1:subtheme:2 · paragraphs 8-9

- Raw key terms: `applicants, claim, arrived, began, canada, considered, country, czech`
- Display key terms: `arrived, began, considered, country, czech`
- Argument roles: `evidence_fact, governing_rule`
- Explanation: Observed roles: evidence_fact, governing_rule Display terms: arrived, began, considered, country, czech Rule/authority context: DECISION UNDER REVIEW Evidence spans paragraphs 8-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `UNDER` at chunk `4892667` offsets `103-108`; context: DECISION UNDER REVIEW
- Evidence: `evidence_fact` cue `found that` at chunk `4892668` offsets `100-110`; context: [9] The RPD considered both the Czech Republic and the Slovak Republic in the Applicants’ claim and found that the Applicants did not have a well-founded fear of persecution if they were returned to either country.

#### 18817:1:subtheme:3 · paragraphs 10-15

- Raw key terms: `discrimination, found, basic, evidence, human, persecution, rights, state`
- Display key terms: `discrimination, basic, human, persecution, rights, state`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: discrimination, basic, human, persecution, rights, state Application context: [11] The RPD found that the discrimination faced by the Applicants did not rise to the level of persecution because there had been no threat to the Applicants’ basic human rights. | Gabor was able to obtain work because he worked as a self-employed painter. Evidence spans paragraphs 10-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4892669` offsets `225-232`; context: In order to determine whether a particular mistreatment would qualify as “serious”, one must examine what interest of the claimant might be harmed; and to what extent the subsistence, enjoyment, expression or exercise of that interest might be compromised.
- Evidence: `evidence_fact` cue `found that` at chunk `4892670` offsets `13-23`; context: [11] The RPD found that the discrimination faced by the Applicants did not rise to the level of persecution because there had been no threat to the Applicants’ basic human rights.
- Evidence: `reasoning_application` cue `because` at chunk `4892670` offsets `108-115`; context: [11] The RPD found that the discrimination faced by the Applicants did not rise to the level of persecution because there had been no threat to the Applicants’ basic human rights.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892671` offsets `35-43`; context: Gabor did not provide any evidence as to “specific experiences” of discrimination he had faced during school.
- Evidence: `reasoning_application` cue `because` at chunk `4892671` offsets `283-290`; context: Gabor was able to obtain work because he worked as a self-employed painter.
- Evidence: `evidence_fact` cue `found that` at chunk `4892673` offsets `97-107`; context: It found that no corroborating evidence was adduced to support this allegation and that she had never sought redress or compensation.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892674` offsets `52-60`; context: [15] The RPD gave greater weight to the documentary evidence than Ms.

#### 18817:1:subtheme:4 · paragraphs 16-16

- Raw key terms: `adversely, affected, allegations, ambulance, basic, because, claim, concluded`
- Display key terms: `adversely, affected, allegations, ambulance, basic, because, concluded`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: adversely, affected, allegations, ambulance, basic, because, concluded Application context: Gaborova’s allegations about the refusal of treatment, the RPD found that “there were no specific details given for this claim and no evidence that [she] had been adversely affected because of lack of ambulance service. Evidence spans paragraphs 16-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `4892675` offsets `437-443`; context: ISSUES
- Evidence: `evidence_fact` cue `found that` at chunk `4892675` offsets `83-93`; context: Gaborova’s allegations about the refusal of treatment, the RPD found that “there were no specific details given for this claim and no evidence that [she] had been adversely affected because of lack of ambulance service.
- Evidence: `reasoning_application` cue `because` at chunk `4892675` offsets `202-209`; context: Gaborova’s allegations about the refusal of treatment, the RPD found that “there were no specific details given for this claim and no evidence that [she] had been adversely affected because of lack of ambulance service.

#### Section text

Gabor v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2010-04-12
Neutral citation
2010 FC 383
File numbers
IMM-3466-09
Decision Content
Federal Court
Cour fédérale
Date: 20100412
Docket: IMM-3466-09
Citation: 2010 FC 383
Ottawa, Ontario, April 12, 2010
PRESENT: The Honourable Mr. Justice Russell
BETWEEN:
GABOR MIROSLAV
GABOROVA MAGDALENA
GABOROVA MAGDALENA JR
GABOROVA BIANKA
Applicants
and
THE MINISTER OF
CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (Act) for judicial review of a decision of the Refugee Protection Division (RPD) of the Immigration and Refugee Board, dated June 19, 2009, (Decision) which determined that the Applicants are not Convention refugees or persons in need of protection pursuant to sections 96 and 97 of the Act.
BACKGROUND

[2] The Applicants are Mr. Miroslav Gabor, his wife Ms. Magdalena Gaborova, and their two daughters, Magdalena Gaborova Jr. and Bianka Gaborova. Mr. Gabor is a citizen of the Czech Republic, while the other three Applicants are citizens of the Slovak Republic. The Applicants allege persecution in their home countries based on their ethnicity.

[3] Mr. Gabor reports having been subjected to differential treatment and verbal and physical abuse while in school. He faced further discrimination in seeking employment, which resulted in his being forced into self-employment. However, as a self-employed painter he was only able to acquire occasional and seasonal work.

[4] In 1991, Mr. Gabor was subjected to a racially motivated attack while waiting at a bus station in Czechoslovakia. He was verbally attacked by a group of skinheads and hit in the back with a chain. He did not report this attack to the police.

[5] Mr. Gabor was attacked again by a group of skinheads in 2007. While waiting for a train, he was verbally attacked, pushed to the ground, and kicked repeatedly. The attack only stopped when an onlooker shouted that s/he had contacted the police. Mr. Gabor attended the emergency department of a hospital as a result of the injuries he sustained in this attack. The doctor examined him and gave him painkillers, but was unwilling to confirm the attack sustained by the Applicant because he stated that “it’s you gypsies who are always making up stories.”

[6] Mr. Gabor attempted to report this attack to the police, but the police were unwilling to talk to him. The police would not let him into the station and told him they had more serious matters to attend to.

[7] Ms. Gaborova has also experienced persecution because of her ethnicity. She maintains that she has not been able to receive proper treatment in her home country for her epilepsy because of her ethnicity. Ambulances have refused to come to her aid because the Applicants lived in a gypsy settlement. Furthermore, Ms. Gaborova alleges that she was involuntarily sterilized when she attended the hospital to have a cyst removed. When asked why he sterilized her, the doctor allegedly stated “you already have two kids, you do not need anymore, and we have enough gypsies in the country.”

[8] The Applicants arrived in Canada in June, 2008 and began their refugee claim immediately.
DECISION UNDER REVIEW

[9] The RPD considered both the Czech Republic and the Slovak Republic in the Applicants’ claim and found that the Applicants did not have a well-founded fear of persecution if they were returned to either country.

[10] The RPD focussed its analysis on the distinction between discrimination and persecution and found as follows:
To be considered persecution, the mistreatment suffered or anticipated must be serious. In order to determine whether a particular mistreatment would qualify as “serious”, one must examine what interest of the claimant might be harmed; and to what extent the subsistence, enjoyment, expression or exercise of that interest might be compromised. “Persecution”, for example, undefined in the Convention, has been ascribed the meaning of sustained or systemic violation of basic human rights demonstrative of a failure of state protection [footnotes omitted].

[11] The RPD found that the discrimination faced by the Applicants did not rise to the level of persecution because there had been no threat to the Applicants’ basic human rights. See Chan v. Canada (Minister of Employment and Immigration), [1995] 3 S.C.R. 593, 187 N.R. 321.

[12] Mr. Gabor did not provide any evidence as to “specific experiences” of discrimination he had faced during school. He also failed to provide any corroborating evidence that he had been discriminated against when seeking employment. Furthermore, Mr. Gabor was able to obtain work because he worked as a self-employed painter. The RPD found that Mr. Gabor had provided “no persuasive evidence that he could not earn a living for himself and his family.”

[13] The RPD noted that the two racially motivated attacks which Mr. Gabor suffered were 16 years apart, and it was only on the second occasion that Mr. Gabor attempted to obtain state protection. The RPD concluded that Mr. Gabor’s basic human rights had not been affected in a fundamental way and the discrimination he experienced did not rise to the level of persecution.

[14] The RPD did not give much weight to Ms. Gaborova’s allegation of a forced sterilization. It found that no corroborating evidence was adduced to support this allegation and that she had never sought redress or compensation. Furthermore, the documentary evidence showed that sterilizations without informed consent were illegal in both the Slovak and Czech Republic at the material time and that victims were entitled to compensation.

[15] The RPD gave greater weight to the documentary evidence than Ms. Gaborova’s testimony and determined that “there was no forced sterilization without informed consent.” In concluding that Ms. Gaborova was not sterilized before giving her informed consent the RPD pointed out the following:
Surgeons who practice in the area of women’s operations would certainly be aware of the law. It is implausible that a surgeon would make a statement suggesting that they performed a sterilization of a woman without informed consent and then state that there were already enough gypsies in the country and risk criminal charges.

[16] As regards Ms. Gaborova’s allegations about the refusal of treatment, the RPD found that “there were no specific details given for this claim and no evidence that [she] had been adversely affected because of lack of ambulance service.” As such, the RPD concluded that the discrimination experienced by Ms. Gaborova did not rise to the level of persecution and that her basic human rights had not been affected in a fundamental way.
ISSUES

## 18817:2 · paragraphs 17-17

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c85b48e3de0ffb982a1547928b4a6f3933e3f5daa4d9ff0bf9270ef6fed0ce3f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 18817:2:subtheme:1 · paragraphs 17-17

- Raw key terms: `application, base, conclusion, decision, erroneous, evidence, fact, findings`
- Display key terms: `base, conclusion, erroneous, fact, findings`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: base, conclusion, erroneous, fact, findings Evidence spans paragraphs 17-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4892676` offsets `9-15`; context: [17] The issues on the application can be summarized as follows:
1.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892676` offsets `188-196`; context: Did the RPD err, ignore, misconstrue, and/or misapply the evidence before it?

#### Section text

[17] The issues on the application can be summarized as follows:
1. Did the RPD err in its application of the section 96 test?
2. Did the RPD err, ignore, misconstrue, and/or misapply the evidence before it?
3. Did the RPD base its decision on erroneous findings of fact?
4. Was the RPD’s conclusion reasonable?
STATUTORY PROVISIONS

## 18817:3 · paragraphs 18-47

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `81d054b80ac830a5708ca380f60fd9dcab9b9390afe2370767e2d2b66e6ca321`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 18817:3:subtheme:1 · paragraphs 18-19

- Raw key terms: `applicable, canada, every, need, particular, review, standard, accepted`
- Display key terms: `applicable, every, need, particular, review, standard, accepted`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: applicable, every, need, particular, review, standard, accepted Rule/authority context: STANDARD OF REVIEW | 190 held that a standard of review analysis need not be conducted in every instance. Application context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subj Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `4892677` offsets `3726-3744`; context: STANDARD OF REVIEW
- Evidence: `reasoning_application` cue `because` at chunk `4892677` offsets `1175-1182`; context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
- Evidence: `issue` cue `question` at chunk `4892678` offsets `243-251`; context: Instead, where the standard of review applicable to the particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review.
- Evidence: `governing_rule` cue `standard of review` at chunk `4892678` offsets `107-125`; context: 190 held that a standard of review analysis need not be conducted in every instance.

#### 18817:3:subtheme:2 · paragraphs 20-21

- Raw key terms: `above, case, dunsmuir, fact, paragraph, reasonableness, standard, according`
- Display key terms: `above, case, dunsmuir, fact, paragraph, reasonableness, standard, according`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: above, case, dunsmuir, fact, paragraph, reasonableness, standard, according Position/evidence statements: [20] The Applicants submit that the RPD erred when it applied the section 96 test to the case at hand. Rule/authority context: The application of a legal test to the facts of the case is an issue of mixed fact and law that is to be reviewed on a standard of reasonableness. | According to Dunsmuir, above, at paragraph 51, the appropriate standard of review for these issues is reasonableness. Application context: [20] The Applicants submit that the RPD erred when it applied the section 96 test to the case at hand. Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4892679` offsets `166-171`; context: The application of a legal test to the facts of the case is an issue of mixed fact and law that is to be reviewed on a standard of reasonableness.
- Evidence: `party_position` cue `submit` at chunk `4892679` offsets `20-26`; context: [20] The Applicants submit that the RPD erred when it applied the section 96 test to the case at hand.
- Evidence: `governing_rule` cue `legal test` at chunk `4892679` offsets `124-134`; context: The application of a legal test to the facts of the case is an issue of mixed fact and law that is to be reviewed on a standard of reasonableness.
- Evidence: `reasoning_application` cue `applied` at chunk `4892679` offsets `54-61`; context: [20] The Applicants submit that the RPD erred when it applied the section 96 test to the case at hand.
- Evidence: `issue` cue `issues` at chunk `4892680` offsets `21-27`; context: [21] The final three issues in this case all concern issues of evidence and fact.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892680` offsets `63-71`; context: [21] The final three issues in this case all concern issues of evidence and fact.
- Evidence: `governing_rule` cue `standard of review` at chunk `4892680` offsets `145-163`; context: According to Dunsmuir, above, at paragraph 51, the appropriate standard of review for these issues is reasonableness.

#### 18817:3:subtheme:3 · paragraphs 22-23

- Raw key terms: `applicants, acceptable, allegation, allegations, analysis, another, applicant, arguments`
- Display key terms: `acceptable, allegation, allegations, analysis, another, arguments`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: acceptable, allegation, allegations, analysis, another, arguments Position/evidence statements: Moreover, the Applicants submit that sworn testimony that is not “inherently unbelievable” cannot simply be “ignored or rejected out-of-hand. Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4892681` offsets `219-226`; context: [22] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law”: Dunsmuir at paragraph 47.
- Evidence: `party_position` cue `submit` at chunk `4892682` offsets `309-315`; context: Moreover, the Applicants submit that sworn testimony that is not “inherently unbelievable” cannot simply be “ignored or rejected out-of-hand.
- Evidence: `evidence_fact` cue `testimony` at chunk `4892682` offsets `327-336`; context: Moreover, the Applicants submit that sworn testimony that is not “inherently unbelievable” cannot simply be “ignored or rejected out-of-hand.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4892682` offsets `375-381`; context: Moreover, the Applicants submit that sworn testimony that is not “inherently unbelievable” cannot simply be “ignored or rejected out-of-hand.

#### 18817:3:subtheme:4 · paragraphs 24-31

- Raw key terms: `erred, evidence, applicants, based, canada, consider, fact, immigration`
- Display key terms: `erred, based, consider, fact`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: erred, based, consider, fact Position/evidence statements: They contend that the RPD erred in concluding that they are required to show that they have been persecuted in the past in order to establish a well-founded fear of persecution in the future. | The Applicants submit that the unwillingness of the police to provide help to Mr. Evidence spans paragraphs 24-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4892683` offsets `410-417`; context: Rather, what matters is whether the Applicants will objectively be at risk if they are returned to their country of origin.
- Evidence: `party_position` cue `contend` at chunk `4892683` offsets `199-206`; context: They contend that the RPD erred in concluding that they are required to show that they have been persecuted in the past in order to establish a well-founded fear of persecution in the future.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892683` offsets `38-46`; context: [24] The Applicants say they provided evidence in both their Personal Information Form (PIF) and orally at their hearing with regard to the persecution they had suffered due to their ethnicity.
- Evidence: `counterargument_limitation` cue `but` at chunk `4892683` offsets `713-716`; context: The Applicants’ claim can be established by not only the evidence of the Applicants themselves, but also by the evidence of those similarly situated to the Applicants.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892684` offsets `182-190`; context: However, the RPD ignored the evidence given by the Applicants’ relatives who have previously been accepted as Convention refugees.
- Evidence: `counterargument_limitation` cue `However` at chunk `4892684` offsets `153-160`; context: However, the RPD ignored the evidence given by the Applicants’ relatives who have previously been accepted as Convention refugees.
- Evidence: `party_position` cue `submit` at chunk `4892685` offsets `230-236`; context: The Applicants submit that the unwillingness of the police to provide help to Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892685` offsets `118-126`; context: Gabor’s evidence spoke of an attempt to seek state protection that the police were unwilling to provide.
- Evidence: `party_position` cue `submit` at chunk `4892686` offsets `20-26`; context: [27] The Applicants submit that the RPD’s conclusion with regard to forced sterilization was based on an erroneous finding of fact.
- Evidence: `evidence_fact` cue `found that` at chunk `4892686` offsets `146-156`; context: While the RPD found that sterilization was a criminal offence as of 2005, the Applicants submit that it was considered a criminal offence sooner than 2005, but that the practice continued nonetheless.
- Evidence: `counterargument_limitation` cue `but` at chunk `4892686` offsets `288-291`; context: While the RPD found that sterilization was a criminal offence as of 2005, the Applicants submit that it was considered a criminal offence sooner than 2005, but that the practice continued nonetheless.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892688` offsets `31-39`; context: [29] The RPD must consider all evidence that it has not found untrustworthy.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892689` offsets `69-77`; context: [30] A conclusion that is made without regard to the totality of the evidence can be characterized as being based on an erroneous finding of fact.
- Evidence: `party_position` cue `submits` at chunk `4892690` offsets `20-27`; context: [31] The Respondent submits that the RPD is entitled to consider past discrimination in a refugee claim.

#### 18817:3:subtheme:5 · paragraphs 32-37

- Raw key terms: `persecution, applicants, discrimination, evidence, face, canada, considered, corroborating`
- Display key terms: `persecution, discrimination, face, considered, corroborating`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: persecution, discrimination, face, considered, corroborating Position/evidence statements: [33] The Respondent contends that the difference between persecution and discrimination is the “greater degree of seriousness of the harm or mistreatment involved” with the former. Application context: [34] The Applicants’ reliance on Salibian, above, is not helpful because the RPD determined that the discrimination faced by the Applicants in the past – as well as the discrimination they may face in the future – did no Evidence spans paragraphs 32-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4892691` offsets `43-48`; context: [32] The RPD stated that the determinative issue was whether the Applicants will face persecution if removed from Canada.
- Evidence: `issue` cue `whether` at chunk `4892692` offsets `222-229`; context: It is the RPD’s prerogative to determine whether mistreatment is discrimination or whether it rises to the level of persecution.
- Evidence: `party_position` cue `contends` at chunk `4892692` offsets `20-28`; context: [33] The Respondent contends that the difference between persecution and discrimination is the “greater degree of seriousness of the harm or mistreatment involved” with the former.
- Evidence: `evidence_fact` cue `determined that` at chunk `4892693` offsets `81-96`; context: [34] The Applicants’ reliance on Salibian, above, is not helpful because the RPD determined that the discrimination faced by the Applicants in the past – as well as the discrimination they may face in the future – did not amount to persecution.
- Evidence: `reasoning_application` cue `because` at chunk `4892693` offsets `65-72`; context: [34] The Applicants’ reliance on Salibian, above, is not helpful because the RPD determined that the discrimination faced by the Applicants in the past – as well as the discrimination they may face in the future – did not amount to persecution.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892694` offsets `39-47`; context: [35] The RPD must assign weight to the evidence before it.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892695` offsets `115-123`; context: Gaborova’s alleged forced sterilization was also made with regard to the evidence before it.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892696` offsets `97-105`; context: Gaborova’s sterilization, the RPD considered evidence from both the Czech Republic and the Slovak Republic, including the 2009 U.

#### 18817:3:subtheme:6 · paragraphs 38-41

- Raw key terms: `evidence, applicants, canada, considered, each, furthermore, immigration, minister`
- Display key terms: `considered, each, furthermore`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: considered, each, furthermore Application context: Rather, each claim must be considered on its own merits: “the RPD is not bound by the result in another claim, even if it is the claim of a relative, because refugee status is determined on a case by case basis. Evidence spans paragraphs 38-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4892697` offsets `258-263`; context: Furthermore, while the Applicants allege that the RPD’s consideration of this issue is based on speculation and assumptions, they have failed to specify what exactly has been speculated or assumed.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892698` offsets `66-74`; context: [39] Moreover, another refugee claim cannot be used as conclusive evidence of persecution.
- Evidence: `reasoning_application` cue `because` at chunk `4892698` offsets `241-248`; context: Rather, each claim must be considered on its own merits: “the RPD is not bound by the result in another claim, even if it is the claim of a relative, because refugee status is determined on a case by case basis.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4892698` offsets `37-43`; context: [39] Moreover, another refugee claim cannot be used as conclusive evidence of persecution.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892699` offsets `68-76`; context: [40] Furthermore, the RPD is presumed to have considered all of the evidence before it, unless the contrary is shown.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892700` offsets `76-84`; context: Gabor submitted his brother’s successful refugee decision as evidence before the RPD, the Respondent notes that there are discrepancies between Mr.

#### 18817:3:subtheme:7 · paragraphs 42-42

- Raw key terms: `applicants, decision, error, examined, issues, material, raised, review`
- Display key terms: `error, examined, issues, material, raised, review`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: error, examined, issues, material, raised, review Evidence spans paragraphs 42-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4892701` offsets `40-46`; context: [42] The Applicants have raised several issues for review, all of which I have examined, but in my view there is only one material error in the Decision.

#### 18817:3:subtheme:8 · paragraphs 43-44

- Raw key terms: `applicant, female, significant, sterilization, against, alleged, attempts, available`
- Display key terms: `female, significant, sterilization, against, alleged, attempts, available`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: female, significant, sterilization, against, alleged, attempts, available Application context: [43] At paragraphs 24 and 25 of the Decision the RPD makes a significant negative credibility finding against the Female Applicant and concludes that “there was no forced sterilization without consent. Evidence spans paragraphs 43-44. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `concludes` at chunk `4892702` offsets `135-144`; context: [43] At paragraphs 24 and 25 of the Decision the RPD makes a significant negative credibility finding against the Female Applicant and concludes that “there was no forced sterilization without consent.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892703` offsets `116-124`; context: [44] A significant portion of the RPD’s reasons for not believing the Female Applicant on this point was based upon evidence which suggested that redress was available for victims of involuntary sterilization and that the Female Applicant “did not make any attempts to seek compensation or redress in any manner as a result of the alleged sterilization.

#### 18817:3:subtheme:9 · paragraphs 45-47

- Raw key terms: `decision, issue, above, accepted, advised, anywhere, applicant, applicants`
- Display key terms: `above, accepted, advised, anywhere`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: above, accepted, advised, anywhere Application context: This is important because the sterilization issue was one of the major aspects of the Applicants’ claim that they had faced persecution in the past and would face it again in the future. Evidence spans paragraphs 45-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4892704` offsets `164-169`; context: [45] As the Tribunal Record shows, and as the Respondent conceded at the hearing, the Female Applicant testified that she did go to a lawyer to explore the redress issue and was advised that there was no chance “to take them anywhere or to complain or to get anywhere with this issue.
- Evidence: `evidence_fact` cue `Record` at chunk `4892704` offsets `21-27`; context: [45] As the Tribunal Record shows, and as the Respondent conceded at the hearing, the Female Applicant testified that she did go to a lawyer to explore the redress issue and was advised that there was no chance “to take them anywhere or to complain or to get anywhere with this issue.
- Evidence: `issue` cue `issue` at chunk `4892705` offsets `131-136`; context: This is important because the sterilization issue was one of the major aspects of the Applicants’ claim that they had faced persecution in the past and would face it again in the future.
- Evidence: `evidence_fact` cue `evidence` at chunk `4892705` offsets `77-85`; context: [46] The RPD has obviously made a serious mistake concerning highly material evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4892705` offsets `105-112`; context: This is important because the sterilization issue was one of the major aspects of the Applicants’ claim that they had faced persecution in the past and would face it again in the future.

#### Section text

[18] The following provisions of the Act are applicable in these proceedings:
Convention refugee
96. A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
Person in need of protection
97. (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
Person in need of protection
(2) A person in Canada who is a member of a class of persons prescribed by the regulations as being in need of protection is also a person in need of protection.
Définition de « réfugié »
96. A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
Personne à protéger
97. (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
Personne à protéger
(2) A également qualité de personne à protéger la personne qui se trouve au Canada et fait partie d’une catégorie de personnes auxquelles est reconnu par règlement le besoin de protection.
STANDARD OF REVIEW

[19] The Supreme Court of Canada in Dunsmuir v. New Brunswick, 2008 SCC 9, [2008] 1 S.C.R. 190 held that a standard of review analysis need not be conducted in every instance. Instead, where the standard of review applicable to the particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review. Only where this search proves fruitless must the reviewing court undertake a consideration of the four factors comprising the standard of review analysis.

[20] The Applicants submit that the RPD erred when it applied the section 96 test to the case at hand. The application of a legal test to the facts of the case is an issue of mixed fact and law that is to be reviewed on a standard of reasonableness. See Dunsmuir, above, at paragraph 164.

[21] The final three issues in this case all concern issues of evidence and fact. According to Dunsmuir, above, at paragraph 51, the appropriate standard of review for these issues is reasonableness. As such, these issues will attract a standard of reasonableness upon review.

[22] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law”: Dunsmuir at paragraph 47. Put another way, the Court should only intervene if the Decision was unreasonable in the sense that it falls outside the “range of possible, acceptable outcomes which are defensible in respect of the facts and law.”
ARGUMENTS
The Applicants

[23] There is a presumption of truth when an applicant swears to the truth of an allegation. As a result, allegations are presumed to be true unless there is reason to believe otherwise. See Maldonado v. Canada (Minister of Employment and Immigration), [1980] 2 F.C. 302, 31 N.R. 34. Moreover, the Applicants submit that sworn testimony that is not “inherently unbelievable” cannot simply be “ignored or rejected out-of-hand.”

[24] The Applicants say they provided evidence in both their Personal Information Form (PIF) and orally at their hearing with regard to the persecution they had suffered due to their ethnicity. They contend that the RPD erred in concluding that they are required to show that they have been persecuted in the past in order to establish a well-founded fear of persecution in the future. Rather, what matters is whether the Applicants will objectively be at risk if they are returned to their country of origin. See Salibian v. Canada (Minister of Employment and Immigration), [1990] 3 F.C. 250, [1990] F.C.J. No. 454. The Applicants’ claim can be established by not only the evidence of the Applicants themselves, but also by the evidence of those similarly situated to the Applicants. This may include family members, friends, or members of the same ethnic group: see Salibian, above.

[25] The Applicants have suffered first-hand abuses of their human rights, and so have those similarly situated to them, including their family members. However, the RPD ignored the evidence given by the Applicants’ relatives who have previously been accepted as Convention refugees.

[26] The RPD erred in determining that the Applicants’ rights had not been affected in a fundamental way. Mr. Gabor’s evidence spoke of an attempt to seek state protection that the police were unwilling to provide. The Applicants submit that the unwillingness of the police to provide help to Mr. Gabor is “a violation of the basic human rights of the citizen for state protection.”

[27] The Applicants submit that the RPD’s conclusion with regard to forced sterilization was based on an erroneous finding of fact. While the RPD found that sterilization was a criminal offence as of 2005, the Applicants submit that it was considered a criminal offence sooner than 2005, but that the practice continued nonetheless. Furthermore, the RPD’s conclusion was based on documents and facts from the Czech Republic even though the sterilization took place in the Slovak Republic. Since the laws in these countries differ, the RPD’s findings with regard to forced sterilization cannot be reasonable. Moreover, the RPD erred in giving greater weight to the documentary evidence than to the testimony of the Applicants.

[28] The RPD further erred in its consideration of Ms. Gaborova’s epilepsy. In this case, the RPD failed to consider that a denial of health care – including access to ambulance service – is tantamount to persecution. Rather, it made a determination based on its speculation and its own assumption of the facts.

[29] The RPD must consider all evidence that it has not found untrustworthy. The RPD erred in failing to give proper weight to the testimony of Ms. Gaborova’s brother and sister.

[30] A conclusion that is made without regard to the totality of the evidence can be characterized as being based on an erroneous finding of fact. See Owusu-Ansah v. Canada (Minister of Employment and Immigration), 98 N.R. 312, 8 Imm. L.R. (2d) 106 (FCA). In this case, the RPD erred by making assertions of fact that were not based on the evidentiary record before it. Rather, the Decision was based on the RPD’s own speculation.
The Respondent

[31] The Respondent submits that the RPD is entitled to consider past discrimination in a refugee claim. In fact, the Applicants’ claim for refugee protection was based on discrimination they had previously faced. The RPD did not err in considering the seriousness of the past incidents to determine if it could justify making an inference of future persecution. See, for example, Natynczyk v. Canada (Minister of Citizenship and Immigration), 2004 FC 914, [2004] F.C.J. No. 1118 at paragraph 71; Asaipillai v. Canada (Minister of Citizenship and Immigration), [1995] F.C.J. No. 1777 at paragraph 7.

[32] The RPD stated that the determinative issue was whether the Applicants will face persecution if removed from Canada. The RPD’s language makes it clear that it acknowledged that the test for persecution is forward-looking.

[33] The Respondent contends that the difference between persecution and discrimination is the “greater degree of seriousness of the harm or mistreatment involved” with the former. It is the RPD’s prerogative to determine whether mistreatment is discrimination or whether it rises to the level of persecution. See, for example, Kwiatkowsky v. Canada (Minister of Employment and Immigration), [1982] 2 S.C.R. 856; Sagharichi v. Canada (Minister of Employment and Immigration), 182 N.R. 398, [1993] F.C.J. No. 796 at paragraph 3.

[34] The Applicants’ reliance on Salibian, above, is not helpful because the RPD determined that the discrimination faced by the Applicants in the past – as well as the discrimination they may face in the future – did not amount to persecution.

[35] The RPD must assign weight to the evidence before it. In this case, the RPD examined the evidence before it thoroughly and determined that Mr. Gabor had not faced persecution in the past and would not face persecution in the future. The RPD’s conclusions were based upon the following:
1. Mr. Gabor’s failure to provide specific examples of discrimination he faced at school;
2. Mr. Gabor’s failure to provide corroborating evidence for discrimination he experienced in finding employment;
3. Mr. Gabor’s failure to prove that he would not be able to resume employment as a self-employed painter;
4. Mr. Gabor’s minimal effort to obtain state protection; and
5. The level of discrimination faced by Mr. Gabor that did not rise to the level of persecution.

[36] The RPD’s finding with regard to Ms. Gaborova’s alleged forced sterilization was also made with regard to the evidence before it. In reaching its conclusion, the RPD considered the following:
1. Ms. Gaborova’s failure to provide persuasive evidence that she approached the police after the illegal procedure;
2. Ms. Gaborova’s failure to consult a lawyer or seek compensation;
3. The implausibility of the doctor’s admission to Ms. Gaborova; and
4. Ms. Gaborova’s failure to provide any corroborating evidence.

[37] In making its determination with regard to Ms. Gaborova’s sterilization, the RPD considered evidence from both the Czech Republic and the Slovak Republic, including the 2009 U.S. Department of State Reports for both countries. Furthermore, the Applicants testified to the similarity of country conditions for Roma people within both countries. As such, the RPD’s consideration of the documentary evidence of forced sterilizations in both countries is not unreasonable.

[38] Ms. Gaborova was unable to provide the RPD with details of the denial of ambulance services. She was also unable to provide details of how this denial adversely affected her. Furthermore, while the Applicants allege that the RPD’s consideration of this issue is based on speculation and assumptions, they have failed to specify what exactly has been speculated or assumed.

[39] Moreover, another refugee claim cannot be used as conclusive evidence of persecution. Rather, each claim must be considered on its own merits: “the RPD is not bound by the result in another claim, even if it is the claim of a relative, because refugee status is determined on a case by case basis.” See, for example, Noha v. Canada (Minister of Citizenship and Immigration), 2009 FC 683, [2009] F.C.J. No. 850 at paragraphs 102-103.

[40] Furthermore, the RPD is presumed to have considered all of the evidence before it, unless the contrary is shown. The fact that the RPD does not refer to each piece of evidence does not mean that it ignored the evidence, if the reasons suggest that the RPD considered all of the evidence. See Florea v. Canada (Minister of Employment and Immigration), [1993] F.C.J. No. 598.

[41] While Mr. Gabor submitted his brother’s successful refugee decision as evidence before the RPD, the Respondent notes that there are discrepancies between Mr. Gabor’s brother’s decision and Mr. Gabor’s testimony as to what sort of school he attended: a “regular school” or one for Roma children. Moreover, the Applicants’ family members did not provide any specific examples of persecution they faced. It was not unreasonable for the RPD to come to a different conclusion from that reached in the claims made by the Applicants’ other family members.
ANALYSIS

[42] The Applicants have raised several issues for review, all of which I have examined, but in my view there is only one material error in the Decision.

[43] At paragraphs 24 and 25 of the Decision the RPD makes a significant negative credibility finding against the Female Applicant and concludes that “there was no forced sterilization without consent.”

[44] A significant portion of the RPD’s reasons for not believing the Female Applicant on this point was based upon evidence which suggested that redress was available for victims of involuntary sterilization and that the Female Applicant “did not make any attempts to seek compensation or redress in any manner as a result of the alleged sterilization. She also did not speak to a lawyer in regard to the matter even though she was aware of the compensation given to other women.”

[45] As the Tribunal Record shows, and as the Respondent conceded at the hearing, the Female Applicant testified that she did go to a lawyer to explore the redress issue and was advised that there was no chance “to take them anywhere or to complain or to get anywhere with this issue.”

[46] The RPD has obviously made a serious mistake concerning highly material evidence. This is important because the sterilization issue was one of the major aspects of the Applicants’ claim that they had faced persecution in the past and would face it again in the future. Had the RPD not overlooked this crucial piece of evidence, and had it accepted that forced sterilization had occurred, its Decision concerning persecution – as opposed to discrimination – could well have been different.

[47] This error renders the Decision unreasonable. Consequently, the matter must be returned for reconsideration. See Dunsmuir, above, at paragraph 47.


## 18817:4 · paragraphs 48-49

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e3dc39b20cccbe0954fafb34e6f1efc7e95eb2d983828dc301dca06eae21a187`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 18817:4:subtheme:1 · paragraphs 48-49

- Raw key terms: `record, russell, solicitors, adjudges, allowed, appearances, applicants, application`
- Display key terms: `russell, solicitors, adjudges, allowed`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: russell, solicitors, adjudges, allowed No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 48-49. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THIS COURT ORDERS AND ADJUDGES that
1. The application is allowed. The Decision is set aside and this matter is returned for reconsideration by a differently constituted RPD.
2. There is no question for certification.
“James Russell”
Judge
FEDERAL COURT
NAME OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-3466-09

STYLE OF CAUSE: GABOR MIROSLAV, GABOROVA
MAGDALENA, GABOROVA
MAGDALENA JR., GABOROVA BIANKA
APPLICANTS
- and -
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
RESPONDENT
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: MARCH 2, 2010
REASONS FOR : HON. MR. JUSTICE RUSSELL
DATED: April 12, 2010
APPEARANCES:
Mr. Hart Kaminker APPLICANTS
Ms. Monmi Goswami RESPONDENT
SOLICITORS OF RECORD:
Hart A. Kaminker
Toronto, Ontario APPLICANTS
John H. Sims, Q.C.
Deputy Attorney General of Canada RESPONDENT
