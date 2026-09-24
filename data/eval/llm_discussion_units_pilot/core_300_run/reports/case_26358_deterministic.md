# Discussion Units: case 26358

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **42**
- Continuity pairs: **41**
- Discussion Units: **4**
- Paragraph source hashes: **42**
- Sub-themes: **10**

## 26358:1 · paragraphs 0-20

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4f3617a551ed835d0a9817a54999adae0d16c554ff79e8f4cb16953393fe9fd7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26358:1:subtheme:1 · paragraphs 0-10

- Raw key terms: `applicant, applicants, male, allegedly, made, authorities, female, pirata`
- Display key terms: `male, allegedly, made, authorities, female, pirata`
- Argument roles: `governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, party_position, reasoning_application Display terms: male, allegedly, made, authorities, female, pirata Position/evidence statements: [4] The male applicant claimed that on May 22, 2009, he was accosted by El Pirata near his home. Rule/authority context: [1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the panel) made under subsection 72(1) of the Immigration and Refugee Protection Act,  | They were allegedly again told that their neighbourhood would be under police surveillance. Application context: The panel rejected their claim because state protection was available in Mexico and there was an internal flight alternative [IFA]. Evidence spans paragraphs 0-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5239398` offsets `150-155`; context: [1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the panel) made under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 (the Act).
- Evidence: `party_position` cue `claimed` at chunk `5239401` offsets `23-30`; context: [4] The male applicant claimed that on May 22, 2009, he was accosted by El Pirata near his home.
- Evidence: `governing_rule` cue `under` at chunk `5239405` offsets `191-196`; context: They were allegedly again told that their neighbourhood would be under police surveillance.
- Evidence: `governing_rule` cue `UNDER` at chunk `5239407` offsets `232-237`; context: DECISION UNDER APPEAL
- Evidence: `reasoning_application` cue `because` at chunk `5239407` offsets `122-129`; context: The panel rejected their claim because state protection was available in Mexico and there was an internal flight alternative [IFA].

#### 26358:1:subtheme:2 · paragraphs 11-13

- Raw key terms: `mexico, panel, protection, adequate, applicants, concluded, decision, evidence`
- Display key terms: `mexico, protection, adequate, concluded`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: mexico, protection, adequate, concluded Rule/authority context: [11] It its decision dated December 19, 2011, the panel correctly pointed out that the ground of persecution alleged by the applicants does not fall under section 96 of the Act, and so the applicants are not Convention r Application context: The panel instead analyzed the applicants’ refugee protection claim under paragraph 97(1)(b) of the Act, and had to determine whether they are persons in need of protection because they would be subject to the risks list Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5239408` offsets `355-362`; context: The panel instead analyzed the applicants’ refugee protection claim under paragraph 97(1)(b) of the Act, and had to determine whether they are persons in need of protection because they would be subject to the risks listed in that paragraph if they had to return to Mexico.
- Evidence: `governing_rule` cue `under` at chunk `5239408` offsets `149-154`; context: [11] It its decision dated December 19, 2011, the panel correctly pointed out that the ground of persecution alleged by the applicants does not fall under section 96 of the Act, and so the applicants are not Convention refugees.
- Evidence: `reasoning_application` cue `because` at chunk `5239408` offsets `402-409`; context: The panel instead analyzed the applicants’ refugee protection claim under paragraph 97(1)(b) of the Act, and had to determine whether they are persons in need of protection because they would be subject to the risks listed in that paragraph if they had to return to Mexico.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239409` offsets `159-167`; context: [12] The panel concluded that the applicants had not succeeded in rebutting the presumption of state protection, as they had not provided clear and convincing evidence of Mexico’s inability to offer them adequate protection (see Canada (Attorney General) v Ward, [1993] 2 SCR 689 [Ward]).
- Evidence: `counterargument_limitation` cue `Although` at chunk `5239409` offsets `289-297`; context: Although the situation in Mexico is not ideal at present, the decisions of the Board and of this Court recognize that there is state protection in Mexico.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239410` offsets `419-427`; context: The documentary evidence before the panel shows that those organizations also offer recourses for individuals who wish to file complaints against officials who do not do their jobs.

#### 26358:1:subtheme:3 · paragraphs 14-19

- Raw key terms: `mexico, applicants, panel, evidence, applicant, authorities, cities, city`
- Display key terms: `mexico, authorities, cities, city`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: mexico, authorities, cities, city Position/evidence statements: Although the male applicant claimed he could be found anywhere in Mexico and there is still corruption, there is no concrete evidence to that effect. Application context: [14] Accordingly, the documentary evidence confirms that there are various mechanisms in Mexico by which victims of crime can file complaints, whether against the criminals, against the authorities who fail to investigat Evidence spans paragraphs 14-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5239411` offsets `143-150`; context: [14] Accordingly, the documentary evidence confirms that there are various mechanisms in Mexico by which victims of crime can file complaints, whether against the criminals, against the authorities who fail to investigate or against corrupt elements.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239411` offsets `34-42`; context: [14] Accordingly, the documentary evidence confirms that there are various mechanisms in Mexico by which victims of crime can file complaints, whether against the criminals, against the authorities who fail to investigate or against corrupt elements.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5239411` offsets `5-16`; context: [14] Accordingly, the documentary evidence confirms that there are various mechanisms in Mexico by which victims of crime can file complaints, whether against the criminals, against the authorities who fail to investigate or against corrupt elements.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239413` offsets `40-48`; context: [16] The panel had regard to all of the evidence in the record and concluded that the applicants had failed to establish, by clear and convincing evidence, that Mexico was unable to offer them adequate protection.
- Evidence: `party_position` cue `claimed` at chunk `5239415` offsets `358-365`; context: Although the male applicant claimed he could be found anywhere in Mexico and there is still corruption, there is no concrete evidence to that effect.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239415` offsets `125-133`; context: There is no evidence that El Pirata made any effort to find the applicants after July 15, 2009, and neither the male applicant’s friend nor the applicants’ family members suffered any reprisals after their departure.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5239415` offsets `330-338`; context: Although the male applicant claimed he could be found anywhere in Mexico and there is still corruption, there is no concrete evidence to that effect.

#### 26358:1:subtheme:4 · paragraphs 20-20

- Raw key terms: `applicants, claim, concluded, issues, meaning, need, panel, persons`
- Display key terms: `concluded, issues, meaning, need, persons`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: concluded, issues, meaning, need, persons Application context: Their refugee protection claim was therefore rejected. Evidence spans paragraphs 20-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `5239417` offsets `201-207`; context: ISSUES
- Evidence: `reasoning_application` cue `therefore` at chunk `5239417` offsets `181-190`; context: Their refugee protection claim was therefore rejected.

#### Section text

Mayorga Gonzalez v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2012-08-13
Neutral citation
2012 FC 987
File numbers
IMM-548-12
Decision Content
Date: 20120813
Docket: IMM-548-12
Citation: 2012 FC 987
[UNREVISED ENGLISH CERTIFIED TRANSLATION]
Ottawa, Ontario, August 13, 2012
PRESENT: The Honourable Madam Justice Gagné
BETWEEN:
ANUAR EDUARDO MAYORGA GONZALEZ & NATIVIDAD ACUNA LARA
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the panel) made under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 (the Act). The panel rejected the applicants’ refugee protection claim, concluding that they were not refugees or persons in need of protection within the meaning of the Act.
FACTS

[2] Anuar Eduardo Mayorga Gonzalez (the male applicant) and his wife Natividad Acuna Lara (the female applicant) (together, the applicants) are citizens of Mexico. The male applicant comes from Guadalajara, Jalisco, and the female applicant from Villahermosa, Tabasco.

[3] The male applicant stated that on May 13, 2009, while he was driving in his neighbourhood, Santa Elena, in Villahermosa, he witnessed a transaction among a group of individuals that he suspected of being a drug deal. He stated that looks were then exchanged between him and the person directly involved in the transaction. A few days later, while the male applicant was driving with a friend in the La Selva neighbourhood (acknowledged by the male applicant to be a dangerous part of Villahermosa), he again encountered the individual involved in the transaction on May 13. The male applicant recounted the event to his friend, who informed him that the man was known as “El Pirata” and was a well known drug trafficker in La Selva, and that he made a practice of being armed.

[4] The male applicant claimed that on May 22, 2009, he was accosted by El Pirata near his home. El Pirata allegedly became aggressive, blaming the applicant for a recent drug seizure by the police authorities and for the resulting financial loss.

[5] On May 27, 2009, the male applicant allegedly made a complaint to the Mexican police authorities. After his deposition was taken, he was informed that the police service was going to send units to do surveillance in his neighbourhood, and they had him meet with a psychologist to make sure he was not affected too much by the events.

[6] On May 31, 2009, while the applicants were driving in La Selva, El Pirata allegedly blocked their way, banged on their car windows and told them he was aware of the report made about him. He allegedly threatened the male applicant and made obscene gestures at the female applicant, and then told them he was a member of a criminal group known as the Zetas and the male applicant’s days were numbered.

[7] On June 5, 2009, the applicants left their home and went to live with a friend in another part of Villahermosa.

[8] On June 15, 2009, the applicants gave another deposition to the police authorities, to report the events of May 31, 2009. They were allegedly again told that their neighbourhood would be under police surveillance. On the same day, the male applicant allegedly received a call from El Pirata, who threatened to rape the female applicant and kill the male applicant.

[9] The male applicant left for Canada on June 18, 2009, and the female applicant remained in Mexico to liquidate his business assets. From June 18 to July 15, 2009, the date when the female applicant joined the male applicant in Canada, she allegedly received two telephone calls in which attempts were made to extort money from her by threats. The female applicant did not complain to the authorities following those events.

[10] The applicants’ refugee protection claim was heard by the panel on November 17, 2011. The panel rejected their claim because state protection was available in Mexico and there was an internal flight alternative [IFA].
DECISION UNDER APPEAL

[11] It its decision dated December 19, 2011, the panel correctly pointed out that the ground of persecution alleged by the applicants does not fall under section 96 of the Act, and so the applicants are not Convention refugees. The panel instead analyzed the applicants’ refugee protection claim under paragraph 97(1)(b) of the Act, and had to determine whether they are persons in need of protection because they would be subject to the risks listed in that paragraph if they had to return to Mexico.

[12] The panel concluded that the applicants had not succeeded in rebutting the presumption of state protection, as they had not provided clear and convincing evidence of Mexico’s inability to offer them adequate protection (see Canada (Attorney General) v Ward, [1993] 2 SCR 689 [Ward]). Although the situation in Mexico is not ideal at present, the decisions of the Board and of this Court recognize that there is state protection in Mexico. While those decisions are not, in principle, binding on the panel, the decision of the panel on state protection in TA6-07453, [2007] RPDD No. 253 has been recognized as persuasive by Justice Zinn (see Mendoza v Canada (Minister of Employment and Immigration), 2010 FC 648, [2010] FCJ 788 [Mendoza]) and the panel did not believe it justified to depart from it in this case.

[13] In the panel’s view, it cannot be concluded from the failure of the authorities to provide adequate protection in certain circumstances that the state is unable to provide its citizens with protection. The panel noted that there are several organizations in Mexico to help individuals seek protection, such as the National Human Rights Commission or the Commission for the Defence of Human Rights. The documentary evidence before the panel shows that those organizations also offer recourses for individuals who wish to file complaints against officials who do not do their jobs.

[14] Accordingly, the documentary evidence confirms that there are various mechanisms in Mexico by which victims of crime can file complaints, whether against the criminals, against the authorities who fail to investigate or against corrupt elements. The Mexican government, in the Board’s view, is making serious efforts to tackle the problem of corruption.

[15] The male applicant complained to the authorities on May 27, 2009, and the authorities took his complaint seriously, as illustrated by Exhibit P-3. They promised him heightened surveillance in his neighbourhood and offered him psychological support.

[16] The panel had regard to all of the evidence in the record and concluded that the applicants had failed to establish, by clear and convincing evidence, that Mexico was unable to offer them adequate protection.

[17] The panel was also of the opinion that the applicants had an IFA in Mexico, more specifically in the locations identified as being safe. The panel was thinking of Mérida and Mexico City, in particular.

[18] Those cities are located far from the applicants’ home and the panel believed they could live there safely. There is no evidence that El Pirata made any effort to find the applicants after July 15, 2009, and neither the male applicant’s friend nor the applicants’ family members suffered any reprisals after their departure. Although the male applicant claimed he could be found anywhere in Mexico and there is still corruption, there is no concrete evidence to that effect. The applicants did not prove that their assailant had the means or the ability to find them everywhere in Mexico. Their problem seems to have been relatively localized and the documentary evidence shows that it is difficult to find someone in Mexico using government databases; information about individuals is not easily accessible.

[19] The panel ultimately concluded that the applicants had not established that it would be unreasonable for them to relocate to Mérida or Mexico City, or that those cities were inaccessible to them.

[20] For those reasons, the panel concluded that the applicants were not refugees or persons in need of protection within the meaning of the Act. Their refugee protection claim was therefore rejected.
ISSUES

## 26358:2 · paragraphs 21-38

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9c88c5b06b171836ae41fb3006d5dd7915e8bce78bea2181e487577f4e651ff7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26358:2:subtheme:1 · paragraphs 21-23

- Raw key terms: `review, available, canada, citizenship, conclusion, fact, immigration, mexico`
- Display key terms: `review, available, conclusion, fact, mexico`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: review, available, conclusion, fact, mexico Rule/authority context: [23] The same standard of review applies to the panel’s conclusion regarding the existence of an IFA in Mexico (see Rahal v Canada (Minister of Citizenship and Immigration), 2012 FC 319 at paragraph 22 [Rahal]; Velasquez Application context: [23] The same standard of review applies to the panel’s conclusion regarding the existence of an IFA in Mexico (see Rahal v Canada (Minister of Citizenship and Immigration), 2012 FC 319 at paragraph 22 [Rahal]; Velasquez Evidence spans paragraphs 21-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5239418` offsets `63-69`; context: [21] This application for judicial review raises the following issues:
(1) Did the panel err in concluding that state protection was available in Mexico, basing its conclusion on erroneous findings of fact that it made capriciously or without regard for all of the evidence?
- Evidence: `evidence_fact` cue `evidence` at chunk `5239418` offsets `265-273`; context: [21] This application for judicial review raises the following issues:
(1) Did the panel err in concluding that state protection was available in Mexico, basing its conclusion on erroneous findings of fact that it made capriciously or without regard for all of the evidence?
- Evidence: `issue` cue `whether` at chunk `5239419` offsets `37-44`; context: [22] The panel's determination as to whether state protection is available is a question of mixed fact and law subject to review against the standard of reasonableness (see Mendoza v Canada (Minister of Citizenship and Immigration), 2010 FC 119 at paragraph 26; Soto v Canada (Minister of Citizenship and Immigration), 2010 FC 1183 at paragraph 26; Burgos v Canada (Minister of Citizenship and Immigration), 2006 FC 1537 at paragraph 17; Velasquez v Canada (Minister of Citizenship and Immigration), 2009 FC 109 at paragraphs 12-13 [Velasquez]; Leon v Canada (Minister of Citizenship and Immigration), 2011 FC 34 at paragraph 12, [2011] FCJ 57 [Leon]).
- Evidence: `governing_rule` cue `standard of review` at chunk `5239420` offsets `14-32`; context: [23] The same standard of review applies to the panel’s conclusion regarding the existence of an IFA in Mexico (see Rahal v Canada (Minister of Citizenship and Immigration), 2012 FC 319 at paragraph 22 [Rahal]; Velasquez, above at paragraph 12).
- Evidence: `reasoning_application` cue `applies` at chunk `5239420` offsets `33-40`; context: [23] The same standard of review applies to the panel’s conclusion regarding the existence of an IFA in Mexico (see Rahal v Canada (Minister of Citizenship and Immigration), 2012 FC 319 at paragraph 22 [Rahal]; Velasquez, above at paragraph 12).

#### 26358:2:subtheme:2 · paragraphs 24-32

- Raw key terms: `applicants, evidence, panel, mexico, protection, made, state, conclusion`
- Display key terms: `mexico, protection, made, state, conclusion`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: mexico, protection, made, state, conclusion Position/evidence statements: [25] The applicants submit that the panel erred in its state protection analysis. | [26] The respondent submits that the panel’s decision is reasonable. Application context: [24] This Court must therefore determine whether the decision and conclusions of the panel are justified, transparent and intelligible, and fall “within a range of possible, acceptable outcomes which are defensible in re | The panel’s conclusion that the applicants had not succeeded in rebutting the presumption of state protection is therefore reasonable. Evidence spans paragraphs 24-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5239421` offsets `41-48`; context: [24] This Court must therefore determine whether the decision and conclusions of the panel are justified, transparent and intelligible, and fall “within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir v New Brunswick, 2008 SCC 9 at paragraph 47 [Dunsmuir]).
- Evidence: `evidence_fact` cue `evidence` at chunk `5239421` offsets `518-526`; context: ANALYSIS
(1) Did the panel err in concluding that state protection was available in Mexico, basing its conclusion on erroneous findings of fact that it made capriciously or without regard for all of the evidence?
- Evidence: `reasoning_application` cue `therefore` at chunk `5239421` offsets `21-30`; context: [24] This Court must therefore determine whether the decision and conclusions of the panel are justified, transparent and intelligible, and fall “within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir v New Brunswick, 2008 SCC 9 at paragraph 47 [Dunsmuir]).
- Evidence: `party_position` cue `submit` at chunk `5239422` offsets `20-26`; context: [25] The applicants submit that the panel erred in its state protection analysis.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239422` offsets `372-380`; context: The applicants argue that the evidence clearly establishes that they were threatened for complaining to the police authorities.
- Evidence: `party_position` cue `submits` at chunk `5239423` offsets `20-27`; context: [26] The respondent submits that the panel’s decision is reasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239423` offsets `174-182`; context: The applicants had the burden of rebutting the presumption of state protection with clear and convincing evidence (see Ward, above), which they did not do.
- Evidence: `reasoning_application` cue `therefore` at chunk `5239423` offsets `1263-1272`; context: The panel’s conclusion that the applicants had not succeeded in rebutting the presumption of state protection is therefore reasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239424` offsets `186-194`; context: [27] This Court may intervene only if the applicants establish that the panel’s findings regarding state protection were made in a perverse or capricious manner or without regard to the evidence before it (Leon, above at paragraph 13).
- Evidence: `party_position` cue `contend` at chunk `5239425` offsets `483-490`; context: The applicants contend that it was unreasonable for them to make further efforts to seek the protection of the Mexican authorities, their lives being in danger because of the reprisals to which they were subject after filing their two complaints.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239425` offsets `332-340`; context: [28] Although the applicants were not required to put their lives at risk to show that they tried to get protection from their country before seeking international protection (see Villasenor v Canada (Minister of Citizenship and Immigration), 2006 FC 1080 at paragraph 19, [2006] FCJ 1359), they had to present clear and convincing evidence of their country’s inability to protect them, and it is up to the panel to assess that evidence (Leon, above at paragraph 28).
- Evidence: `reasoning_application` cue `because` at chunk `5239425` offsets `628-635`; context: The applicants contend that it was unreasonable for them to make further efforts to seek the protection of the Mexican authorities, their lives being in danger because of the reprisals to which they were subject after filing their two complaints.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239426` offsets `88-96`; context: [29] The panel’s conclusion regarding state protection in Mexico takes into account the evidence in the record: the panel considered the efforts made by the applicants, the situation in Mexico and their relationship with the Mexican authorities.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239427` offsets `26-34`; context: [30] Having regard to the evidence in the record, it was reasonable for the panel to conclude that state protection was available in Mexico, the applicants having failed to provide clear and convincing evidence to rebut the presumption in that respect.
- Evidence: `reasoning_application` cue `conclude` at chunk `5239427` offsets `85-93`; context: [30] Having regard to the evidence in the record, it was reasonable for the panel to conclude that state protection was available in Mexico, the applicants having failed to provide clear and convincing evidence to rebut the presumption in that respect.
- Evidence: `party_position` cue `assert` at chunk `5239428` offsets `20-26`; context: [31] The applicants assert that there is no IFA, since their agent of persecution has the means and motivation to find them everywhere in the country, the criminal group to which he belongs having infiltrated Mexico’s various institutions and organizations.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239428` offsets `302-310`; context: They contend that the panel disregarded the evidence in the record.
- Evidence: `party_position` cue `contends` at chunk `5239429` offsets `20-28`; context: [32] The respondent contends that the panel’s conclusion regarding the existence of an IFA is also reasonable, since the applicants failed to show that they could not settle safely in either of the cities suggested.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239429` offsets `387-395`; context: It was possible to conclude from the documentary evidence in the record that the personal information of Mexican citizens is protected and is difficult to access.
- Evidence: `reasoning_application` cue `conclude` at chunk `5239429` offsets `357-365`; context: It was possible to conclude from the documentary evidence in the record that the personal information of Mexican citizens is protected and is difficult to access.

#### 26358:2:subtheme:3 · paragraphs 33-37

- Raw key terms: `applicants, panel, above, evidence, paragraph, actual, concrete, court`
- Display key terms: `above, paragraph, actual, concrete`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: above, paragraph, actual, concrete Application context: [37] I am therefore of the opinion that the applicants have not established that an error was made by the panel that would justify intervention by this Court, nor have they identified evidence that was disregarded by the Operative outcome context: The existence of an IFA is conclusive and is sufficient in itself for the applicants’ application for judicial review to be dismissed (see Villasenor, above at paragraph 20). Evidence spans paragraphs 33-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5239430` offsets `283-290`; context: The panel had to analyze (i) whether the applicants could live safely in Mexico, in the locations identified as safe, and (ii) whether those locations were reasonable and accessible to the applicants.
- Evidence: `issue` cue `whether` at chunk `5239431` offsets `38-45`; context: [34] The panel first had to determine whether, having regard to the persecution the applicants had suffered in their city, and in fact their neighbourhood, it is “objectively reasonable to expect [them] to seek safety in a different part of that country before seeking a haven in Canada or elsewhere”.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239431` offsets `771-779`; context: In addition, it requires actual and concrete evidence of such conditions.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239432` offsets `212-220`; context: That is not sufficient, and it does not constitute actual, concrete evidence of the circumstances that would put their lives or safety in peril.
- Evidence: `evidence_fact` cue `evidence` at chunk `5239433` offsets `88-96`; context: [36] Having regard to the fact that the applicants did not produce any actual, concrete evidence showing that Mérida and Mexico City were unreasonable IFAs or that those cities were inaccessible to them, the panel’s conclusion was reasonable.
- Evidence: `disposition` cue `dismissed` at chunk `5239433` offsets `367-376`; context: The existence of an IFA is conclusive and is sufficient in itself for the applicants’ application for judicial review to be dismissed (see Villasenor, above at paragraph 20).
- Evidence: `evidence_fact` cue `evidence` at chunk `5239434` offsets `184-192`; context: [37] I am therefore of the opinion that the applicants have not established that an error was made by the panel that would justify intervention by this Court, nor have they identified evidence that was disregarded by the panel.
- Evidence: `reasoning_application` cue `therefore` at chunk `5239434` offsets `10-19`; context: [37] I am therefore of the opinion that the applicants have not established that an error was made by the panel that would justify intervention by this Court, nor have they identified evidence that was disregarded by the panel.

#### 26358:2:subtheme:4 · paragraphs 38-38

- Raw key terms: `agree, case, certification, court, parties, question, raise, view`
- Display key terms: `agree, case, certification, question, raise, view`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: agree, case, certification, question, raise, view Evidence spans paragraphs 38-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5239435` offsets `57-65`; context: [38] The parties agree that this case does not raise any question for certification.

#### Section text

[21] This application for judicial review raises the following issues:
(1) Did the panel err in concluding that state protection was available in Mexico, basing its conclusion on erroneous findings of fact that it made capriciously or without regard for all of the evidence?
(2) Did the panel err in concluding that the applicants had an internal flight alternative?

[22] The panel's determination as to whether state protection is available is a question of mixed fact and law subject to review against the standard of reasonableness (see Mendoza v Canada (Minister of Citizenship and Immigration), 2010 FC 119 at paragraph 26; Soto v Canada (Minister of Citizenship and Immigration), 2010 FC 1183 at paragraph 26; Burgos v Canada (Minister of Citizenship and Immigration), 2006 FC 1537 at paragraph 17; Velasquez v Canada (Minister of Citizenship and Immigration), 2009 FC 109 at paragraphs 12-13 [Velasquez]; Leon v Canada (Minister of Citizenship and Immigration), 2011 FC 34 at paragraph 12, [2011] FCJ 57 [Leon]).

[23] The same standard of review applies to the panel’s conclusion regarding the existence of an IFA in Mexico (see Rahal v Canada (Minister of Citizenship and Immigration), 2012 FC 319 at paragraph 22 [Rahal]; Velasquez, above at paragraph 12).

[24] This Court must therefore determine whether the decision and conclusions of the panel are justified, transparent and intelligible, and fall “within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir v New Brunswick, 2008 SCC 9 at paragraph 47 [Dunsmuir]).
ANALYSIS
(1) Did the panel err in concluding that state protection was available in Mexico, basing its conclusion on erroneous findings of fact that it made capriciously or without regard for all of the evidence?
Position of the Applicants

[25] The applicants submit that the panel erred in its state protection analysis. They contend that the panel failed to have regard to the efforts made by the applicants and the reprisals they allegedly suffered after filing their complaints. They state that they had no further recourses available in Mexico without endangering their lives. The applicants argue that the evidence clearly establishes that they were threatened for complaining to the police authorities. In addition, it is not the role of the various organizations listed by the panel to provide protection, and they are unable to protect the applicants. In view of the threats and the corruption on the part of the Mexican authorities, they had no obligation to do more to seek the protection of the authorities in Mexico, as any other efforts would put their lives in peril.
Position of the Respondent

[26] The respondent submits that the panel’s decision is reasonable. The applicants had the burden of rebutting the presumption of state protection with clear and convincing evidence (see Ward, above), which they did not do. The agent of the applicants’ persecution was not a state agent, it was a criminal. The evidence cited by the panel indicates that Mexico offers a number of mechanisms for victims of crime, in spite of the existence of corruption. The applicants’ testimony confirmed that the Mexican authorities responded to the complaints made, and not only opened an investigation, but promised heightened surveillance and offered the male applicant psychological help. As it was required to do, the panel had regard to the general situation in Mexico, the efforts made by the applicants and their relationship with the authorities (see Leon, above). The respondent added that even if the authorities had been unable to offer the applicants effective protection, that is insufficient to support their refugee protection claim (Canada (Minister of Employment and Immigration) v Villafranca [1992] FCJ 1189, (1992) 150 NR 232 [Villafranca]). The panel’s conclusion that the applicants had not succeeded in rebutting the presumption of state protection is therefore reasonable.
Analysis

[27] This Court may intervene only if the applicants establish that the panel’s findings regarding state protection were made in a perverse or capricious manner or without regard to the evidence before it (Leon, above at paragraph 13).

[28] Although the applicants were not required to put their lives at risk to show that they tried to get protection from their country before seeking international protection (see Villasenor v Canada (Minister of Citizenship and Immigration), 2006 FC 1080 at paragraph 19, [2006] FCJ 1359), they had to present clear and convincing evidence of their country’s inability to protect them, and it is up to the panel to assess that evidence (Leon, above at paragraph 28). The applicants contend that it was unreasonable for them to make further efforts to seek the protection of the Mexican authorities, their lives being in danger because of the reprisals to which they were subject after filing their two complaints. The applicants’ main argument is based on the fact that those reprisals suggested a direct link between the police authorities and El Pirata. However, El Pirata associated the male applicant with the drug seizure following the transaction of May 13, 2009, even before the male applicant had reported the events to the authorities for the first time. The male applicant left Mexico shortly afterward and the female applicant did not seek police protection after the threats made against her between June 18 and July 15, 2009.

[29] The panel’s conclusion regarding state protection in Mexico takes into account the evidence in the record: the panel considered the efforts made by the applicants, the situation in Mexico and their relationship with the Mexican authorities. The action taken by the authorities in response to the reports filed by the applicants shows the ability and willingness of the state to protect them: the police opened an investigation, promised heightened surveillance in their neighbourhood and offered the male applicant psychological help. El Pirata was plainly known to the authorities, since he had been the subject of a drug seizure even before the male applicant reported the events of May 13, 2009. It was not sufficient for the applicants to allege that there is corruption in Mexico or that the government has not always been able to protect its citizens, to rebut the presumption operating against them. As Justice Hugessen stated in Villafranca, above at paragraph 7:
[W]here a state is in effective control of its territory . . . and makes serious efforts to protect its citizens, the mere fact it is not always successful at doing so will not be enough to justify a claim that the victims are unable to avail themselves of protection.

[30] Having regard to the evidence in the record, it was reasonable for the panel to conclude that state protection was available in Mexico, the applicants having failed to provide clear and convincing evidence to rebut the presumption in that respect. Accordingly, the panel’s conclusion is supported by the evidence in the record and is transparent, intelligible and justified within the meaning of Dunsmuir.
(2) Did the panel err in concluding that the applicants had an internal flight alternative?
Position of the Applicants

[31] The applicants assert that there is no IFA, since their agent of persecution has the means and motivation to find them everywhere in the country, the criminal group to which he belongs having infiltrated Mexico’s various institutions and organizations. They contend that the panel disregarded the evidence in the record.
Position of the Respondent

[32] The respondent contends that the panel’s conclusion regarding the existence of an IFA is also reasonable, since the applicants failed to show that they could not settle safely in either of the cities suggested. A mere assertion of corruption in Mexico is insufficient to establish that an IFA is not reasonable or is not accessible. It was possible to conclude from the documentary evidence in the record that the personal information of Mexican citizens is protected and is difficult to access. The applicants failed to establish that actual conditions would put their lives and safety in peril in Mérida and Mexico City, or that their lives would be in danger everywhere in Mexico.
Analysis

[33] The panel was required to consider the two aspects of an IFA analysis, which it did (see Ranganathan v Canada (Minister of Citizenship and Immigration), [2001] 2 FC 164, [2000] FCJ No 2118 at paragraph 13 [Ranganathan] and Thirunavukkarasu, above). The panel had to analyze (i) whether the applicants could live safely in Mexico, in the locations identified as safe, and (ii) whether those locations were reasonable and accessible to the applicants.

[34] The panel first had to determine whether, having regard to the persecution the applicants had suffered in their city, and in fact their neighbourhood, it is “objectively reasonable to expect [them] to seek safety in a different part of that country before seeking a haven in Canada or elsewhere”. The burden of convincing the panel of the contrary rested on the applicants, as this Court noted in Ranganathan, (above at paragraph 15; see also Perez v Canada (Minister of Citizenship and Immigration), 2011 FC 8 at paragraph 15, [2011] FCJ 16):
. . . It requires nothing less than the existence of conditions which would jeopardize the life and safety of a claimant in travelling or temporarily relocating to a safe area. In addition, it requires actual and concrete evidence of such conditions.

[35] The applicants simply asserted that corruption was present throughout Mexico and that their agent of persecution could find them anywhere. That is not sufficient, and it does not constitute actual, concrete evidence of the circumstances that would put their lives or safety in peril. The applicants presented no evidence that their agent of persecution had the desire and/or the ability to find them, nor were they able to identify for this Court the evidence showing such a desire or ability that was disregarded by the panel.

[36] Having regard to the fact that the applicants did not produce any actual, concrete evidence showing that Mérida and Mexico City were unreasonable IFAs or that those cities were inaccessible to them, the panel’s conclusion was reasonable. The existence of an IFA is conclusive and is sufficient in itself for the applicants’ application for judicial review to be dismissed (see Villasenor, above at paragraph 20).
CONCLUSION

[37] I am therefore of the opinion that the applicants have not established that an error was made by the panel that would justify intervention by this Court, nor have they identified evidence that was disregarded by the panel. The panel’s decision falls “within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, above at paragraph 47). Intervention by the Court is not warranted.

[38] The parties agree that this case does not raise any question for certification. The Court is also of that view.


## 26358:3 · paragraphs 39-40

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1c21581d5db6e9f405befed8b3c8c48e59644947f00e1797bcd35f51676a8fe6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26358:3:subtheme:1 · paragraphs 39-40

- Raw key terms: `acuna, anuar, application, case, cause, certification, certified, chamberlain`
- Display key terms: `acuna, anuar, case, certification, certified, chamberlain`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: acuna, anuar, case, certification, certified, chamberlain No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 39-40. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THE COURT ORDERS THAT:
1. the application for judicial review is dismissed.
2. the case raises no question for certification.
“Jocelyne Gagné”
Judge
Certified true translation
Monica F. Chamberlain
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-548-12
STYLE OF CAUSE: Anuar Eduardo Mayorga Gonzalez &
Natividad Acuna Lara
and MCI
PLACE OF HEARING: Montréal, Quebec
DATE OF HEARING: July 25, 2012
REASONS FOR 

## 26358:4 · paragraphs 41-41

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `54f3db234a654a5a478700c54872545bc70ffe6c77d7ef749172de634b5970b0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26358:4:subtheme:1 · paragraphs 41-41

- Raw key terms: `appearances, applicants, attorney, august, bell, canada, complexe, date`
- Display key terms: `august, bell, complexe, date`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: august, bell, complexe, date No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 41-41. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT &
JUDGMENT: GAGNÉ J.
DATE OF REASONS: August 13, 2012
APPEARANCES:
Odette Desjardins
FOR THE APPLICANTS
Steve Bell
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Odette Desjardins
Montréal, Quebec
FOR THE APPLICANTS
Deputy Attorney General of Canada
Complexe Guy Favreau
Montréal, Quebec
FOR THE RESPONDENT
