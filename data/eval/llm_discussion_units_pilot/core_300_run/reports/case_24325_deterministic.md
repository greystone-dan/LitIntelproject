# Discussion Units: case 24325

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **53**
- Continuity pairs: **52**
- Discussion Units: **5**
- Paragraph source hashes: **53**
- Sub-themes: **16**

## 24325:1 · paragraphs 0-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c5cda6072779e83f6bd335deded50d85dbe2b9092169bc53c8e6b878a3e85853`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24325:1:subtheme:1 · paragraphs 0-11

- Raw key terms: `applicant, applicants, female, decision, irpa, protection, refugee, section`
- Display key terms: `female, irpa, protection, refugee, section`
- Argument roles: `evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position, reasoning_application Display terms: female, irpa, protection, refugee, section Position/evidence statements: [7] La female applicant submitted that in February 2000 investigators from the Criminal Investigation Directorate apparently came to intercept her at her home to answer for certain offences before the court. | The applicants never claimed refugee protection during their stay in the United States. Rule/authority context: [1] This is an application for judicial review under section 18. | [11] The RPD said it was satisfied with the identity of the applicants and found that they are not Convention refugees for the purposes of section 96 of the IRPA or persons in need of protection under section 97 of the I Application context: [8] On March 5, 2000, the female applicant allegedly left the country for the United States to flee the criminals who were looking for her because of the reports. | [9] The applicant left the United States for Guatemala to request a work visa but he had to leave the country shortly after because the threatening calls resumed. Evidence spans paragraphs 0-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `5144133` offsets `280-290`; context: 1 of the Federal Courts Act, RSC 1985, c F-7 against the decision rendered on January 7, 2013, by a member of the Refugee Protection Division (the RPD) of the Immigration and Refugee Board (the IRB), in which it was found that the applicants are neither Convention refugees for the purposes of section 96 of the Immigration and Refugee Protection Act, SC 2001, c 27 (the IRPA), or persons in need of protection under section 97 of the IRPA.
- Evidence: `governing_rule` cue `under` at chunk `5144133` offsets `47-52`; context: [1] This is an application for judicial review under section 18.
- Evidence: `party_position` cue `submitted` at chunk `5144139` offsets `24-33`; context: [7] La female applicant submitted that in February 2000 investigators from the Criminal Investigation Directorate apparently came to intercept her at her home to answer for certain offences before the court.
- Evidence: `party_position` cue `claimed` at chunk `5144140` offsets `242-249`; context: The applicants never claimed refugee protection during their stay in the United States.
- Evidence: `reasoning_application` cue `because` at chunk `5144140` offsets `139-146`; context: [8] On March 5, 2000, the female applicant allegedly left the country for the United States to flee the criminals who were looking for her because of the reports.
- Evidence: `reasoning_application` cue `because` at chunk `5144141` offsets `124-131`; context: [9] The applicant left the United States for Guatemala to request a work visa but he had to leave the country shortly after because the threatening calls resumed.
- Evidence: `evidence_fact` cue `found that` at chunk `5144143` offsets `75-85`; context: [11] The RPD said it was satisfied with the identity of the applicants and found that they are not Convention refugees for the purposes of section 96 of the IRPA or persons in need of protection under section 97 of the IRPA.
- Evidence: `governing_rule` cue `under` at chunk `5144143` offsets `195-200`; context: [11] The RPD said it was satisfied with the identity of the applicants and found that they are not Convention refugees for the purposes of section 96 of the IRPA or persons in need of protection under section 97 of the IRPA.

#### 24325:1:subtheme:2 · paragraphs 12-14

- Raw key terms: `applicant, female, another, stated, testimony, translation, vendors, actions`
- Display key terms: `female, another, stated, testimony, translation, vendors, actions`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: female, another, stated, testimony, translation, vendors, actions Evidence spans paragraphs 12-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5144144` offsets `793-801`; context: She added that the dates in question were not written in the female applicant’s Personal Information Form (the PIF).
- Evidence: `evidence_fact` cue `testimony` at chunk `5144144` offsets `71-80`; context: [12] The RPD stated that the female applicant did not provide credible testimony and noted some contradictions that slipped into the different versions of the facts.
- Evidence: `counterargument_limitation` cue `however` at chunk `5144144` offsets `453-460`; context: The RPD stated that it thought it was normal and understandable for the female applicant to have been mistaken the two dates, given that the events took place 12 years earlier, however, it did not understand why facts provided by the female applicant as to the number of calls and the times that the calls were received could be so precise one moment and much less clear at another.
- Evidence: `evidence_fact` cue `found that` at chunk `5144145` offsets `73-83`; context: It found that it was implausible to claim that the female applicant had mobilized the merchants who have stores by asking them not to pay the people extorting them.
- Evidence: `evidence_fact` cue `testimony` at chunk `5144146` offsets `88-97`; context: [14] The RPD also confronted the female applicant about another discrepancy between her testimony and the content of her PIF.

#### 24325:1:subtheme:3 · paragraphs 15-16

- Raw key terms: `acts, applicant, extortion, extortionists, female, found, help, identify`
- Display key terms: `acts, extortion, extortionists, female, help, identify`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: acts, extortion, extortionists, female, help, identify Application context: Having carefully reviewed documentary evidence, the RPD stated that gangs of extortionists were indeed demanding money from the entire population, but it characterized the female applicant’s claim that she was targeted b Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5144147` offsets `45-50`; context: [15] Turning to a hypothetical review of the issue, the RPD found that even if one were to assume that the story was credible, the violence to which the female applicant could be exposed would be generalized.
- Evidence: `evidence_fact` cue `found that` at chunk `5144147` offsets `60-70`; context: [15] Turning to a hypothetical review of the issue, the RPD found that even if one were to assume that the story was credible, the violence to which the female applicant could be exposed would be generalized.
- Evidence: `reasoning_application` cue `because` at chunk `5144147` offsets `457-464`; context: Having carefully reviewed documentary evidence, the RPD stated that gangs of extortionists were indeed demanding money from the entire population, but it characterized the female applicant’s claim that she was targeted by the police or these gangs because she allegedly reported them as very general and not credible.
- Evidence: `counterargument_limitation` cue `but` at chunk `5144147` offsets `356-359`; context: Having carefully reviewed documentary evidence, the RPD stated that gangs of extortionists were indeed demanding money from the entire population, but it characterized the female applicant’s claim that she was targeted by the police or these gangs because she allegedly reported them as very general and not credible.
- Evidence: `evidence_fact` cue `found that` at chunk `5144148` offsets `148-158`; context: [16] In its decision, the RPD also took interest in the documentation provided by the female applicant who reported the extortion and it once again found that the documents could not result in any acts of vengeance since they did not help identify anyone.

#### 24325:1:subtheme:4 · paragraphs 17-18

- Raw key terms: `applicants, claim, decision, evidence, raised, refugee, stated, states`
- Display key terms: `raised, refugee, stated, states`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: raised, refugee, stated, states Position/evidence statements: [17] Finally, the RPD stated that the applicants stayed in the United States for 10 years and, having entered illegally into this country, they did not submit any refugee claim. | [18] The applicants stated that the RPD came to the conclusion that the female applicant was not a Convention refugee or a person in need of protection because it believed that she was not credible, that she was a victim Application context: To conclude, the RPD added that the son’s designated representative, the mother, did not submit any evidence against the United States, his country of citizenship. | [18] The applicants stated that the RPD came to the conclusion that the female applicant was not a Convention refugee or a person in need of protection because it believed that she was not credible, that she was a victim Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5144149` offsets `642-650`; context: In this respect, no fear of returning to the United States was raised and the finding concerning him is not called into question.
- Evidence: `party_position` cue `submit` at chunk `5144149` offsets `152-158`; context: [17] Finally, the RPD stated that the applicants stayed in the United States for 10 years and, having entered illegally into this country, they did not submit any refugee claim.
- Evidence: `evidence_fact` cue `found that` at chunk `5144149` offsets `276-286`; context: The RPD found that the applicants did not discharge their burden of proof in this regard.
- Evidence: `reasoning_application` cue `conclude` at chunk `5144149` offsets `361-369`; context: To conclude, the RPD added that the son’s designated representative, the mother, did not submit any evidence against the United States, his country of citizenship.
- Evidence: `issue` cue `issue` at chunk `5144150` offsets `544-549`; context: The applicants are of the view that the decision is not reasonable since the RPD failed to conduct a separate analysis on section 96, that it had not informed the female applicant of the fact that the issue of generalized risk was raised and that it did not correctly assess the evidence on the record, leading to declare the female applicant not credible.
- Evidence: `party_position` cue `claim` at chunk `5144150` offsets `271-276`; context: [18] The applicants stated that the RPD came to the conclusion that the female applicant was not a Convention refugee or a person in need of protection because it believed that she was not credible, that she was a victim of generalized violence and that she neglected to claim refugee protection in the United States when she had that option.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144150` offsets `622-630`; context: The applicants are of the view that the decision is not reasonable since the RPD failed to conduct a separate analysis on section 96, that it had not informed the female applicant of the fact that the issue of generalized risk was raised and that it did not correctly assess the evidence on the record, leading to declare the female applicant not credible.
- Evidence: `reasoning_application` cue `because` at chunk `5144150` offsets `152-159`; context: [18] The applicants stated that the RPD came to the conclusion that the female applicant was not a Convention refugee or a person in need of protection because it believed that she was not credible, that she was a victim of generalized violence and that she neglected to claim refugee protection in the United States when she had that option.

#### 24325:1:subtheme:5 · paragraphs 19-20

- Raw key terms: `applicant, applicants, burden, claim, erred, female, guatemala, opinions`
- Display key terms: `burden, erred, female, guatemala, opinions`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: burden, erred, female, guatemala, opinions Position/evidence statements: They claimed that the RPD limited its analysis to the credibility of the female applicant, to the notion of generalized risk and the female applicant’s failure to claim refugee protection in the United States, without qu Rule/authority context: Further, the RPD did not rule on the existence or the lack of a link between refugee claim and the grounds established under section 96 of the IRPA, unlike what procedural fairness dictates. Application context: [19] First, the applicants are of the view that the RPD erred by neglecting to conduct a separate analysis relating to section 96, a provision raised by the female applicant who stated that she fears being persecuted bec | Since the burdens of proof were different, it is not even possible to know whether the RPD applied the burden of proof of section 96 or of section 97. Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5144151` offsets `1057-1065`; context: They added that the RPD did not at all state that it rejected the female applicant’s claims in this respect and that it merely stated that the female applicant did not discharge her burden of proof, without specifying what burden of proof was in question.
- Evidence: `party_position` cue `claimed` at chunk `5144151` offsets `405-412`; context: They claimed that the RPD limited its analysis to the credibility of the female applicant, to the notion of generalized risk and the female applicant’s failure to claim refugee protection in the United States, without questioning the female applicant’s political opinions.
- Evidence: `reasoning_application` cue `because` at chunk `5144151` offsets `217-224`; context: [19] First, the applicants are of the view that the RPD erred by neglecting to conduct a separate analysis relating to section 96, a provision raised by the female applicant who stated that she fears being persecuted because of her membership in a particular social group, i.
- Evidence: `issue` cue `whether` at chunk `5144152` offsets `900-907`; context: Since the burdens of proof were different, it is not even possible to know whether the RPD applied the burden of proof of section 96 or of section 97.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144152` offsets `32-40`; context: [20] Since there was sufficient evidence to support a claim based on political opinions, the RPD should have assessed this ground of the application more carefully.
- Evidence: `governing_rule` cue `under` at chunk `5144152` offsets `433-438`; context: Further, the RPD did not rule on the existence or the lack of a link between refugee claim and the grounds established under section 96 of the IRPA, unlike what procedural fairness dictates.
- Evidence: `reasoning_application` cue `applied` at chunk `5144152` offsets `916-923`; context: Since the burdens of proof were different, it is not even possible to know whether the RPD applied the burden of proof of section 96 or of section 97.
- Evidence: `counterargument_limitation` cue `although` at chunk `5144152` offsets `265-273`; context: Relying on case law, the applicants believed that the RPD erred since it did not analyze the risks, although evidence was submitted in this respect.

#### 24325:1:subtheme:6 · paragraphs 21-22

- Raw key terms: `applicant, applicants, female, able, activism, added, amounts, characterized`
- Display key terms: `female, able, activism, added, amounts, characterized`
- Argument roles: `issue, party_position`
- Explanation: Observed roles: issue, party_position Display terms: female, able, activism, added, amounts, characterized Position/evidence statements: [22] Third, as regards credibility, the applicants submit that it was unreasonable for the RPD to find that it was implausible that the female applicant, as a merchant working on the street, could have mobilized merchant Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5144153` offsets `23-28`; context: [21] Second, as to the issue of generalized risk, the applicants were of the view that the female applicant was never informed of the fact that the RPD was concerned by this issue and it was not able to provide the necessary details.
- Evidence: `party_position` cue `submit` at chunk `5144154` offsets `51-57`; context: [22] Third, as regards credibility, the applicants submit that it was unreasonable for the RPD to find that it was implausible that the female applicant, as a merchant working on the street, could have mobilized merchants with stores.

#### 24325:1:subtheme:7 · paragraphs 23-27

- Raw key terms: `applicants, respondent, alleged, applicant, fear, behaviour, calls, certain`
- Display key terms: `alleged, fear, behaviour, calls, certain`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: alleged, fear, behaviour, calls, certain Position/evidence statements: [23] Fourth, the applicants claimed that the RPD neglected to consider and include in its decision a series of evidence that support the female applicant’s claims. | [25] First, the respondent argued that it was up to the applicants to establish a subjective fear of persecution and an objective basis to this fear. Rule/authority context: Therefore, the applicants are not persons in need of protection under section 97 of the IRPA since they did not establish how a possible return to Guatemala would expose them personally to a risk of torture or a risk to  Application context: Therefore, the applicants are not persons in need of protection under section 97 of the IRPA since they did not establish how a possible return to Guatemala would expose them personally to a risk of torture or a risk to  Evidence spans paragraphs 23-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5144155` offsets `608-613`; context: They also added that as the evidence went against the RPD’s finding on a central issue, it was up to the RPD to analyze the evidence and explain why it would prefer other elements.
- Evidence: `party_position` cue `claimed` at chunk `5144155` offsets `28-35`; context: [23] Fourth, the applicants claimed that the RPD neglected to consider and include in its decision a series of evidence that support the female applicant’s claims.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144155` offsets `111-119`; context: [23] Fourth, the applicants claimed that the RPD neglected to consider and include in its decision a series of evidence that support the female applicant’s claims.
- Evidence: `party_position` cue `argued` at chunk `5144157` offsets `27-33`; context: [25] First, the respondent argued that it was up to the applicants to establish a subjective fear of persecution and an objective basis to this fear.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144157` offsets `475-483`; context: Such behaviour may lead the RPD to draw negative inferences as to the subjective component of the fear alleged by an applicant and the absence of evidence relating to this subjective component is a fatal error for an application.
- Evidence: `evidence_fact` cue `record` at chunk `5144158` offsets `185-191`; context: In support of his claims, the respondent recalls certain essential elements on record that were raised by the RPD, in particular the fact that the female applicant delivered inconsistent versions of the threatening calls, that she could not identify her alleged persecutors and that she did not mention her report or her fear of the police officers during her point of entry declaration in Canada.
- Evidence: `governing_rule` cue `under` at chunk `5144159` offsets `711-716`; context: Therefore, the applicants are not persons in need of protection under section 97 of the IRPA since they did not establish how a possible return to Guatemala would expose them personally to a risk of torture or a risk to their lives or to a risk of cruel and unusual treatment or punishment.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5144159` offsets `647-656`; context: Therefore, the applicants are not persons in need of protection under section 97 of the IRPA since they did not establish how a possible return to Guatemala would expose them personally to a risk of torture or a risk to their lives or to a risk of cruel and unusual treatment or punishment.

#### 24325:1:subtheme:8 · paragraphs 28-28

- Raw key terms: `allege, applicable, applicant, applicants, application, because, challenge, citizenship`
- Display key terms: `allege, applicable, because, challenge`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: allege, applicable, because, challenge Application context: [28] In closing, the respondent stated that the refugee claim concerning the female applicant’s son was dismissed because the applicants did not allege any risk for him in his country of citizenship, the United States. Operative outcome context: [28] In closing, the respondent stated that the refugee claim concerning the female applicant’s son was dismissed because the applicants did not allege any risk for him in his country of citizenship, the United States. Evidence spans paragraphs 28-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5144160` offsets `361-367`; context: Issues
- Evidence: `reasoning_application` cue `because` at chunk `5144160` offsets `114-121`; context: [28] In closing, the respondent stated that the refugee claim concerning the female applicant’s son was dismissed because the applicants did not allege any risk for him in his country of citizenship, the United States.
- Evidence: `disposition` cue `dismissed` at chunk `5144160` offsets `104-113`; context: [28] In closing, the respondent stated that the refugee claim concerning the female applicant’s son was dismissed because the applicants did not allege any risk for him in his country of citizenship, the United States.

#### Section text

Garcia Arreaga v Canada ( Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2013-09-25
Neutral citation
2013 FC 977
File numbers
IMM-996-13
Decision Content
Date: 20130925
Docket: IMM-996-13
Citation: 2013 FC 977
[UNREVISED ENGLISH CERTIFIED TRANSLATION]
Montréal, Quebec, September 25, 2013
PRESENT: The Honourable Mr. Justice Simon Noël
BETWEEN:
YANIRA JEANETH GARCIA ARREAGA
JONATHAN ABDIEL IMUL
JONATHAN IMUL MEJIA
Applicants
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review under section 18.1 of the Federal Courts Act, RSC 1985, c F-7 against the decision rendered on January 7, 2013, by a member of the Refugee Protection Division (the RPD) of the Immigration and Refugee Board (the IRB), in which it was found that the applicants are neither Convention refugees for the purposes of section 96 of the Immigration and Refugee Protection Act, SC 2001, c 27 (the IRPA), or persons in need of protection under section 97 of the IRPA.
I. Facts

[2] Yanira Jeaneth Garcia Arreaga (the female applicant), her spouse Jonathan Imul Mejia (the applicant), citizens of Guatemala, and their son Jonathan Abdiel Imul, citizen of the United States, (together, the applicants) based their request on section 96 and subsection 97(1) of the IRPA. The female applicant is the designated representative of her son.

[3] The female applicant was a street merchant and she stated that she was a victim of extortion, i.e. that she had to pay to stay in business. The acts of extortion occurred in person and on the telephone. All citizens who are merchants faced this extortion. The female applicant stated that police officers, political officials and customs officers were involved.

[4] The female applicant informed the police officers of the situation by telephone, asking them to watch the suspects, but the police officers did not come. The applicant reported the crimes against the female applicant to the public prosecutor so that the authorities could investigate and the Ministry asked the applicants to report the suspects at the time when the wrongdoing was occurring. It was impossible for the authorities to protect the female applicant at all times.

[5] The female applicant collected signatures and documents in an attempt to put pressure on the authorities. She collected three lists: the people who agreed to pay, those who did not agree to pay and those who were undecided. The female applicant also made a last report in which she accused the authorities of complicity and identified them as responsible for her situation that she was facing.

[6] To continue her activities, the female applicant moved to another area.

[7] La female applicant submitted that in February 2000 investigators from the Criminal Investigation Directorate apparently came to intercept her at her home to answer for certain offences before the court. The female applicant is of the view that the Criminal Investigation Directorate wished to make an example of her case.

[8] On March 5, 2000, the female applicant allegedly left the country for the United States to flee the criminals who were looking for her because of the reports. The female applicant’s son was born in the United States. The applicants never claimed refugee protection during their stay in the United States.

[9] The applicant left the United States for Guatemala to request a work visa but he had to leave the country shortly after because the threatening calls resumed. The extortion calls continued after the applicant left.

[10] The applicants entered Canada and filed a refugee claim on June 22, 2011.
II. Impugned decision

[11] The RPD said it was satisfied with the identity of the applicants and found that they are not Convention refugees for the purposes of section 96 of the IRPA or persons in need of protection under section 97 of the IRPA.

[12] The RPD stated that the female applicant did not provide credible testimony and noted some contradictions that slipped into the different versions of the facts. These contradictions related to the number of calls received and to the times when these calls were received. The RPD stated that it thought it was normal and understandable for the female applicant to have been mistaken the two dates, given that the events took place 12 years earlier, however, it did not understand why facts provided by the female applicant as to the number of calls and the times that the calls were received could be so precise one moment and much less clear at another. Finally, the RPD rejected the dates provided by the female applicant as being [translation] “fabricated”. She added that the dates in question were not written in the female applicant’s Personal Information Form (the PIF).

[13] Then, the RPD considered the female applicant’s activist status. It found that it was implausible to claim that the female applicant had mobilized the merchants who have stores by asking them not to pay the people extorting them. In the view of the RPD, it was more plausible that the female applicant’s actions were limited to mobilizing vendors at her level, i.e. vendors on the street or in the market, but not merchants owning stores.

[14] The RPD also confronted the female applicant about another discrepancy between her testimony and the content of her PIF. In fact, in her testimony, the female applicant stated that she worked alone, whereas her PIF used the pronoun [translation] “we”, which gives the impression that a group of vendors worked with her.

[15] Turning to a hypothetical review of the issue, the RPD found that even if one were to assume that the story was credible, the violence to which the female applicant could be exposed would be generalized. Having carefully reviewed documentary evidence, the RPD stated that gangs of extortionists were indeed demanding money from the entire population, but it characterized the female applicant’s claim that she was targeted by the police or these gangs because she allegedly reported them as very general and not credible. The RPD was of the view that the alleged extortionists and the [translation] “shady police officers” did not have any way to find the female applicant since she did not provide any information to the authorities that would help to identify the individuals who carried out the acts of extortion. Therefore, since the reports did not contain any names, the RPD did not believe the female applicant with respect to officers of the Criminal Investigation Directorate allegedly coming to get her to answer to certain offences.

[16] In its decision, the RPD also took interest in the documentation provided by the female applicant who reported the extortion and it once again found that the documents could not result in any acts of vengeance since they did not help identify anyone. Confronted with why she had not mentioned reporting the extortionists and the police officers in the form that she filled out when she entered Canada, the female applicant stated that she did not have enough space to do so. This explanation was rejected by the RPD.

[17] Finally, the RPD stated that the applicants stayed in the United States for 10 years and, having entered illegally into this country, they did not submit any refugee claim. The authorized timeframe for submitting such a request for the United States has expired. The RPD found that the applicants did not discharge their burden of proof in this regard. To conclude, the RPD added that the son’s designated representative, the mother, did not submit any evidence against the United States, his country of citizenship. In this respect, no fear of returning to the United States was raised and the finding concerning him is not called into question. Therefore, the RPD decision is valid.
III. Position of the applicants

[18] The applicants stated that the RPD came to the conclusion that the female applicant was not a Convention refugee or a person in need of protection because it believed that she was not credible, that she was a victim of generalized violence and that she neglected to claim refugee protection in the United States when she had that option. The applicants are of the view that the decision is not reasonable since the RPD failed to conduct a separate analysis on section 96, that it had not informed the female applicant of the fact that the issue of generalized risk was raised and that it did not correctly assess the evidence on the record, leading to declare the female applicant not credible.

[19] First, the applicants are of the view that the RPD erred by neglecting to conduct a separate analysis relating to section 96, a provision raised by the female applicant who stated that she fears being persecuted because of her membership in a particular social group, i.e. a group of human rights advocates, or her political opinions, which were opposite to those of the government authorities. They claimed that the RPD limited its analysis to the credibility of the female applicant, to the notion of generalized risk and the female applicant’s failure to claim refugee protection in the United States, without questioning the female applicant’s political opinions. They also argued that, if she had to return to Guatemala, the female applicant would risk a great deal because of her political opinions. They added that the RPD did not at all state that it rejected the female applicant’s claims in this respect and that it merely stated that the female applicant did not discharge her burden of proof, without specifying what burden of proof was in question.

[20] Since there was sufficient evidence to support a claim based on political opinions, the RPD should have assessed this ground of the application more carefully. Relying on case law, the applicants believed that the RPD erred since it did not analyze the risks, although evidence was submitted in this respect. Further, the RPD did not rule on the existence or the lack of a link between refugee claim and the grounds established under section 96 of the IRPA, unlike what procedural fairness dictates. The RPD’s findings did not indicate that the female applicant had not succeeded in establishing a serious possibility of persecution in connection with one of the Convention grounds or that the risk she would allegedly face if she were to return to Guatemala would be different from what her fellow citizens would face. Since the burdens of proof were different, it is not even possible to know whether the RPD applied the burden of proof of section 96 or of section 97.

[21] Second, as to the issue of generalized risk, the applicants were of the view that the female applicant was never informed of the fact that the RPD was concerned by this issue and it was not able to provide the necessary details.

[22] Third, as regards credibility, the applicants submit that it was unreasonable for the RPD to find that it was implausible that the female applicant, as a merchant working on the street, could have mobilized merchants with stores. They characterized this conclusion as insulting since it amounts to saying that the female applicant is inferior to the other vendors. They added that the social ranking or wealth of the female applicant have nothing to do with her activism.

[23] Fourth, the applicants claimed that the RPD neglected to consider and include in its decision a series of evidence that support the female applicant’s claims. They stated that the fact of taking into evidence the documentation without challenging their probative value led to the conclusion that the evidence proves their content. The applicants argue that the RPD erred in insisting that some contradictions with regard to the calls, while the evidence—that she did not mention—showed the female applicant’s allegations. They also added that as the evidence went against the RPD’s finding on a central issue, it was up to the RPD to analyze the evidence and explain why it would prefer other elements.
IV. Position of the respondent

[24] The respondent characterized the RPD’s decision as reasonable given that the applicants have adopted behaviour that undermines their credibility, that they delivered an inconsistent and contradictory story and that they allege a generalized and random risk.

[25] First, the respondent argued that it was up to the applicants to establish a subjective fear of persecution and an objective basis to this fear. Further, the applicants lived for 10 years without status in the United States, a country that is a signatory of the Convention, without taking steps to claim refugee protection. Such behaviour may lead the RPD to draw negative inferences as to the subjective component of the fear alleged by an applicant and the absence of evidence relating to this subjective component is a fatal error for an application. It was open to the RPD to assess the behaviour of the applicants and they did not provide sufficient explanations as to why they did not claim refugee protection during this 10-year period.

[26] Second, the respondent is of the view that the applicants’ story was inconsistent and contradictory. In support of his claims, the respondent recalls certain essential elements on record that were raised by the RPD, in particular the fact that the female applicant delivered inconsistent versions of the threatening calls, that she could not identify her alleged persecutors and that she did not mention her report or her fear of the police officers during her point of entry declaration in Canada. The applicants did not provide all the details that could reasonably be expected in this matter and the inconsistencies and contradictions in the applicants’ stories properly support the finding of the applicants’ lack of credibility.

[27] Third, the respondent stated that the risk alleged by the applicants is generalized and random since the fear raised by the applicants relates to the actions of a gang of criminals that target the general public. Thus, the applicants are not exposed to a personalized risk and they fall outside of the definition of Convention refugee for the purposes of section 96 of the IRPA. Further, the respondent stated that even if the applicants were members of a sub-group of persons that is likely to be targeted by certain types of widespread crimes, the risk would still be generalized for the purposes of sub-paragraph 97(1)(b)(ii) of the IRPA. Therefore, the applicants are not persons in need of protection under section 97 of the IRPA since they did not establish how a possible return to Guatemala would expose them personally to a risk of torture or a risk to their lives or to a risk of cruel and unusual treatment or punishment.

[28] In closing, the respondent stated that the refugee claim concerning the female applicant’s son was dismissed because the applicants did not allege any risk for him in his country of citizenship, the United States. Since the applicants do not challenge this finding, the application for judicial review applicable to the son must therefore be dismissed.
V. Issues

## 24325:2 · paragraphs 29-32

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c3ec5e057c235c8d8e232c82cfda04ef26ba22b2c1c964f31bf67c61e5122c1f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24325:2:subtheme:1 · paragraphs 29-30

- Raw key terms: `applicable, applicants, credibility, finding, standard, aguebor, allegation, applicant`
- Display key terms: `applicable, credibility, finding, standard, aguebor, allegation`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: applicable, credibility, finding, standard, aguebor, allegation Rule/authority context: Standard of review Evidence spans paragraphs 29-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5144161` offsets `19-25`; context: [29] The following issues arise from this judicial review:
1.
- Evidence: `governing_rule` cue `Standard of review` at chunk `5144161` offsets `564-582`; context: Standard of review
- Evidence: `issue` cue `question` at chunk `5144162` offsets `128-136`; context: the first question, since it is a question of fact and it was within the RPD’s purview to assess the applicants’ allegation of subjective fear (Pinon v Canada (Minister of Citizenship and Immigration), 2010 FC 413, at para 10, [2010] FCJ No 500, see also Aguebor v Canada (Minister of Employment and Immigration) (1993), 160 NR 315, at para 4, 1993 CarswellNat 303 (FCA)).

#### 24325:2:subtheme:2 · paragraphs 31-32

- Raw key terms: `dunsmuir, para, question, standard, above, acosta, addressed, application`
- Display key terms: `dunsmuir, para, question, standard, above, acosta, addressed`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: dunsmuir, para, question, standard, above, acosta, addressed Rule/authority context: [32] The standard of review on the third issue is correctness since it is a question of law (Dunsmuir, above, at para 59). Evidence spans paragraphs 31-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5144163` offsets `48-56`; context: [31] The RPD’s findings addressed by the second question and relating to the application of section 97 of the IRPA consist in mixed questions of fact and law that must be reviewed on the standard of reasonableness (see Acosta v Canada (Minister of Citizenship and Immigration), 2009 FC 213, at paras 11 to 15, [2009] FCJ No 270; Dunsmuir v New Brunswick, 2008 SCC 9, at para 53, (2008), 329 NBR (2d) 1 (Dunsmuir)).
- Evidence: `issue` cue `issue` at chunk `5144164` offsets `41-46`; context: [32] The standard of review on the third issue is correctness since it is a question of law (Dunsmuir, above, at para 59).
- Evidence: `governing_rule` cue `standard of review` at chunk `5144164` offsets `9-27`; context: [32] The standard of review on the third issue is correctness since it is a question of law (Dunsmuir, above, at para 59).

#### Section text

[29] The following issues arise from this judicial review:
1. Did the RPD err in its assessment of the applicants’ credibility and, as applicable, was the rejection by the RPD of the claim for Convention refugee status for the purposes of section 96 of the IRPA reasonable?
2. Did the RPD err in finding that the applicants faced a generalized risk and not a personalized risk in Guatemala for the purposes of section 97 of the IRPA?
3. Did the RPD err by ignoring one of the grounds supporting the application, i.e. the female applicant’s political opinions?
VI. Standard of review

[30] The reasonableness standard is applicable to the RPD’s finding regarding the credibility of the applicants, i.e. the first question, since it is a question of fact and it was within the RPD’s purview to assess the applicants’ allegation of subjective fear (Pinon v Canada (Minister of Citizenship and Immigration), 2010 FC 413, at para 10, [2010] FCJ No 500, see also Aguebor v Canada (Minister of Employment and Immigration) (1993), 160 NR 315, at para 4, 1993 CarswellNat 303 (FCA)).

[31] The RPD’s findings addressed by the second question and relating to the application of section 97 of the IRPA consist in mixed questions of fact and law that must be reviewed on the standard of reasonableness (see Acosta v Canada (Minister of Citizenship and Immigration), 2009 FC 213, at paras 11 to 15, [2009] FCJ No 270; Dunsmuir v New Brunswick, 2008 SCC 9, at para 53, (2008), 329 NBR (2d) 1 (Dunsmuir)).

[32] The standard of review on the third issue is correctness since it is a question of law (Dunsmuir, above, at para 59).


## 24325:3 · paragraphs 33-49

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0f092678e7dcd010a20a439f8d8805b49a4b6d46daf68a120219bf2776c4685c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24325:3:subtheme:1 · paragraphs 33-41

- Raw key terms: `applicants, credibility, reasonable, applicant, canada, fear, female, irpa`
- Display key terms: `credibility, reasonable, fear, female, irpa`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: credibility, reasonable, fear, female, irpa Position/evidence statements: [36] Other findings with respect to the use of [translation] “we” in the PIF compared to [translation] “I” during her testimony in explaining her role and the minimization to a mere vendor not being able to influence the Application context: The female applicant did not specify any of these dates in her PIF, rather, she merely stated that she was forced to move because of calls and fears. | [40] Therefore, it was up to the applicants to establish a subjective fear of persecution in Guatemala and the objective basis of this fear (Ward, above, and see also Adjei, above). Evidence spans paragraphs 33-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `5144165` offsets `365-372`; context: Whether it is for section 96 or 97 of the IRPA, the applicants’ claims were not such that they could justify one of these findings (Adjei v Canada (Minister of Employment and Immigration), [1989] 2 FC 680, at para 5, 7 Imm LR (2d) 169) (Adjei); Chan v Canada (Minister of Employment and Immigration), [1995] 3 SCR 593, at para 120, [1995] SCJ No 78).
- Evidence: `evidence_fact` cue `testimony` at chunk `5144165` offsets `166-175`; context: [33] The RPD’s findings regarding the lack of credibility of the applicants are reasonable since, as the RPD pointed out in its conclusion, the female applicant gave testimony that was not credible in several ways.
- Evidence: `evidence_fact` cue `testimony` at chunk `5144166` offsets `124-133`; context: [34] First, a simple reading of the hearing transcript and the female applicant’s PIF helps see that the female applicant’s testimony shows various elements likely to undermine her credibility.
- Evidence: `reasoning_application` cue `because` at chunk `5144166` offsets `493-500`; context: The female applicant did not specify any of these dates in her PIF, rather, she merely stated that she was forced to move because of calls and fears.
- Evidence: `party_position` cue `submitted` at chunk `5144168` offsets `347-356`; context: [36] Other findings with respect to the use of [translation] “we” in the PIF compared to [translation] “I” during her testimony in explaining her role and the minimization to a mere vendor not being able to influence the rich merchants are a little less persuasive, but they remain within the limits of reasonableness if the entirety of the facts submitted are considered.
- Evidence: `evidence_fact` cue `testimony` at chunk `5144168` offsets `118-127`; context: [36] Other findings with respect to the use of [translation] “we” in the PIF compared to [translation] “I” during her testimony in explaining her role and the minimization to a mere vendor not being able to influence the rich merchants are a little less persuasive, but they remain within the limits of reasonableness if the entirety of the facts submitted are considered.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5144172` offsets `5-14`; context: [40] Therefore, it was up to the applicants to establish a subjective fear of persecution in Guatemala and the objective basis of this fear (Ward, above, and see also Adjei, above).

#### 24325:3:subtheme:2 · paragraphs 42-45

- Raw key terms: `applicants, found, reasonable, risk, applicant, application, convention, extortionists`
- Display key terms: `reasonable, risk, convention, extortionists`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: reasonable, risk, convention, extortionists Position/evidence statements: [41] It is important to recall that the applicants in this case lived in the United States for 10 years without status and without taking steps to claim refugee protection in that country, which is a signatory of the Con Rule/authority context: [42] For the foregoing reasons, I am of the view that the RPD reasonably found that the applicants are not Convention refugees under section 96 of the IRPA and, therefore, the application was dismissed. Application context: was determining a similar question and found, at paragraph 22, that “it was reasonable for the Board to conclude that a five-year stay in the United States without making a claim indicates a lack of subjective fear”. | [42] For the foregoing reasons, I am of the view that the RPD reasonably found that the applicants are not Convention refugees under section 96 of the IRPA and, therefore, the application was dismissed. Operative outcome context: [42] For the foregoing reasons, I am of the view that the RPD reasonably found that the applicants are not Convention refugees under section 96 of the IRPA and, therefore, the application was dismissed. Evidence spans paragraphs 42-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5144173` offsets `712-720`; context: was determining a similar question and found, at paragraph 22, that “it was reasonable for the Board to conclude that a five-year stay in the United States without making a claim indicates a lack of subjective fear”.
- Evidence: `party_position` cue `claim` at chunk `5144173` offsets `147-152`; context: [41] It is important to recall that the applicants in this case lived in the United States for 10 years without status and without taking steps to claim refugee protection in that country, which is a signatory of the Convention.
- Evidence: `evidence_fact` cue `record` at chunk `5144173` offsets `1260-1266`; context: On reading the record, it appears that the explanations provided by the female applicant as to the fact that the applicants had not claimed refugee status in the United States are insufficient.
- Evidence: `reasoning_application` cue `conclude` at chunk `5144173` offsets `790-798`; context: was determining a similar question and found, at paragraph 22, that “it was reasonable for the Board to conclude that a five-year stay in the United States without making a claim indicates a lack of subjective fear”.
- Evidence: `evidence_fact` cue `found that` at chunk `5144174` offsets `73-83`; context: [42] For the foregoing reasons, I am of the view that the RPD reasonably found that the applicants are not Convention refugees under section 96 of the IRPA and, therefore, the application was dismissed.
- Evidence: `governing_rule` cue `under` at chunk `5144174` offsets `127-132`; context: [42] For the foregoing reasons, I am of the view that the RPD reasonably found that the applicants are not Convention refugees under section 96 of the IRPA and, therefore, the application was dismissed.
- Evidence: `reasoning_application` cue `therefore` at chunk `5144174` offsets `161-170`; context: [42] For the foregoing reasons, I am of the view that the RPD reasonably found that the applicants are not Convention refugees under section 96 of the IRPA and, therefore, the application was dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `5144174` offsets `192-201`; context: [42] For the foregoing reasons, I am of the view that the RPD reasonably found that the applicants are not Convention refugees under section 96 of the IRPA and, therefore, the application was dismissed.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144175` offsets `184-192`; context: The RPD reviewed the documentary evidence and found that the extortionists in Guatemala have victimized many in the entire population.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5144175` offsets `286-295`; context: Therefore, the applicants are not specifically targeted by the criminal acts.

#### 24325:3:subtheme:3 · paragraphs 46-48

- Raw key terms: `facts, applicant, application, considering, decision, female, grounds, irpa`
- Display key terms: `facts, considering, female, grounds, irpa`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: facts, considering, female, grounds, irpa Position/evidence statements: in this matter A decision-maker cannot be criticized for not considering it when the female applicant did not raise or submit it during her testimony. Rule/authority context: It is clear that the facts submitted could not have been recognized as credible and, therefore, the applicants did not meet their burden under sections 96 and 97 of the IRPA. Application context: [46] Therefore, the RPD did not err with respect to the grounds in support of the application. Evidence spans paragraphs 46-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5144177` offsets `188-196`; context: In response to question 28 of the PIF, the female applicant instead indicated that she was requesting refugee protection on the basis of membership in a particular social group; however, there was never a question of political opinions.
- Evidence: `party_position` cue `submit` at chunk `5144177` offsets `841-847`; context: in this matter A decision-maker cannot be criticized for not considering it when the female applicant did not raise or submit it during her testimony.
- Evidence: `evidence_fact` cue `testimony` at chunk `5144177` offsets `862-871`; context: in this matter A decision-maker cannot be criticized for not considering it when the female applicant did not raise or submit it during her testimony.
- Evidence: `counterargument_limitation` cue `however` at chunk `5144177` offsets `351-358`; context: In response to question 28 of the PIF, the female applicant instead indicated that she was requesting refugee protection on the basis of membership in a particular social group; however, there was never a question of political opinions.
- Evidence: `evidence_fact` cue `testimony` at chunk `5144178` offsets `179-188`; context: On the whole, it is a decision that gives full importance to the female applicant’s testimony.
- Evidence: `governing_rule` cue `under` at chunk `5144178` offsets `371-376`; context: It is clear that the facts submitted could not have been recognized as credible and, therefore, the applicants did not meet their burden under sections 96 and 97 of the IRPA.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5144178` offsets `5-14`; context: [46] Therefore, the RPD did not err with respect to the grounds in support of the application.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144179` offsets `208-216`; context: [47] I would add that while the RPD did not specifically identify its analysis for the purposes of sections 96 and 97 of the IRPA, a careful reading of the decision reveals that the RPD analyzed the facts in evidence, considering the above-noted sections.
- Evidence: `counterargument_limitation` cue `but` at chunk `5144179` offsets `302-305`; context: Of course, it could have been better written, but this is not a reason to say that it is incorrect or unreasonable.

#### 24325:3:subtheme:4 · paragraphs 49-49

- Raw key terms: `certification, invited, none, parties, proposed, question, submit`
- Display key terms: `certification, invited, none, proposed, question, submit`
- Argument roles: `counterargument_limitation, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, issue, party_position Display terms: certification, invited, none, proposed, question, submit Position/evidence statements: [48] The parties were invited to submit a question for certification, but none was proposed. Evidence spans paragraphs 49-49. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5144180` offsets `42-50`; context: [48] The parties were invited to submit a question for certification, but none was proposed.
- Evidence: `party_position` cue `submit` at chunk `5144180` offsets `33-39`; context: [48] The parties were invited to submit a question for certification, but none was proposed.
- Evidence: `counterargument_limitation` cue `but` at chunk `5144180` offsets `70-73`; context: [48] The parties were invited to submit a question for certification, but none was proposed.

#### Section text

VII. Analysis
A. Did the RPD err in its assessment of the applicants’ credibility and, as applicable, was the rejection by the RPD of the claim for Convention refugee status for the purposes of section 96 of the IRPA reasonable?

[33] The RPD’s findings regarding the lack of credibility of the applicants are reasonable since, as the RPD pointed out in its conclusion, the female applicant gave testimony that was not credible in several ways. She had the burden of proving a factual foundation justifying a finding that the applicants are Convention refugees or persons in need of protection. Whether it is for section 96 or 97 of the IRPA, the applicants’ claims were not such that they could justify one of these findings (Adjei v Canada (Minister of Employment and Immigration), [1989] 2 FC 680, at para 5, 7 Imm LR (2d) 169) (Adjei); Chan v Canada (Minister of Employment and Immigration), [1995] 3 SCR 593, at para 120, [1995] SCJ No 78).

[34] First, a simple reading of the hearing transcript and the female applicant’s PIF helps see that the female applicant’s testimony shows various elements likely to undermine her credibility. Initially, the female applicant provided very specific memories as to the number of calls received and the time that those calls were received, both the dates and times of day. The female applicant did not specify any of these dates in her PIF, rather, she merely stated that she was forced to move because of calls and fears. Given the number of details omitted in the PIF, it was reasonable for the RPD to support a determination of lack of credibility for this omission. In addition, the female applicant did not provide any details that would help identify the alleged extortionists and corrupt police officers and, further, when she arrived in Canada, she did not mention her reports or her fear of the police officers to the responsible authorities.

[35] In addition, with respect to the assessment of the female applicant’s credibility, it is important to identify, as did the RPD, that the applicants lived in the United States illegally for 10 years without ever claiming refugee protection before filing their application in Canada. The RPD was correct in pointing out the length of this delay, which inevitably undermines the applicants’ credibility.

[36] Other findings with respect to the use of [translation] “we” in the PIF compared to [translation] “I” during her testimony in explaining her role and the minimization to a mere vendor not being able to influence the rich merchants are a little less persuasive, but they remain within the limits of reasonableness if the entirety of the facts submitted are considered. Again, the reading of the testimony of the female applicant and the applicant shows uncertainty, vagueness and, on occasion, contradictions. With such testimony, it is difficult for the applicants to meet their burden. This has an impact on the entire application.

[37] Considering the above, I am of the view that the analysis conducted by the RPD before pronouncing the applicants not credible was reasonable. There is no reason for the Court to intervene on this ground.
Section 96 of the IRPA and the subjective fear of persecution

[38] The RPD’s analysis of credibility being otherwise reasonable, it would now be appropriate to review the reasonableness of the decision-maker’s finding that the applicants are not Convention refugees for the purposes of section 96 of the IRPA.

[39] It was established in Ward v Canada (Attorney General), [1993] 2 SCR 689, 103 DLR (4th) 1) (Ward) that assessing the fear of persecution has two components: (1) the claimant must subjectively fear persecution; and (2) this fear must be well-founded in an objective sense. At paragraph 14 of its decision Rajudeen v Canada (Minister of Employment and Immigration) (1984), 55 NR 129 (FCA), the Federal Court of Appeal interpreted this criterion as follows: “The subjective component relates to the existence of the fear of persecution in the mind of the refugee. The objective component requires that the refugee’s fear be evaluated objectively to determine if there is a valid basis for that fear”. We must point out that the assessment of subjective fear of persecution is intimately related to the credibility of the person or persons that argue a fear of persecution.

[40] Therefore, it was up to the applicants to establish a subjective fear of persecution in Guatemala and the objective basis of this fear (Ward, above, and see also Adjei, above).

[41] It is important to recall that the applicants in this case lived in the United States for 10 years without status and without taking steps to claim refugee protection in that country, which is a signatory of the Convention. As the respondent alleges, it was open to the RPD to draw negative inferences with respect to the subjective fear of applicants if they neglect to claim refugee status in a country that is a party to the Convention (see Ilie v Canada (Minister of Citizenship and Immigration), [1994] FCA No 1758, 51 ACWS (3d) 1349). Moreover, at paragraphs 22 to 25 of Herrera v Canada (Minister of Citizenship and Immigration), 2007 FC 979, [2007] FCJ No 1297, Beaudry J. was determining a similar question and found, at paragraph 22, that “it was reasonable for the Board to conclude that a five-year stay in the United States without making a claim indicates a lack of subjective fear”. In addition, case law established that the lack of subjective fear can be “a fatal flaw which in and of itself warrants dismissal of the claim, since both elements of the refugee definition—subjective and objective—must be met” (see Kamana v Canada (Minister of Citizenship and Immigration), [1999] FCJ No 1695 at para 10, 94 ACWS (3d) 338). On reading the record, it appears that the explanations provided by the female applicant as to the fact that the applicants had not claimed refugee status in the United States are insufficient.

[42] For the foregoing reasons, I am of the view that the RPD reasonably found that the applicants are not Convention refugees under section 96 of the IRPA and, therefore, the application was dismissed.
B. Did the RPD err in finding that the applicants faced a generalized risk and not a personalized risk in Guatemala for the purposes of section 97 of the IRPA?

[43] The RPD’s finding that the applicants face a generalized risk for the purposes of section 97 of the IRPA is reasonable for the following reasons. The RPD reviewed the documentary evidence and found that the extortionists in Guatemala have victimized many in the entire population. Therefore, the applicants are not specifically targeted by the criminal acts.

[44] Further, while she reported the extortion of which she was a victim, the female applicant never gave details that would help identify the alleged extortionists and corrupt police officers. For this reason, it was perfectly reasonable for the RPD to find that the applicants face no personalized risk of revenge since the female applicant did not identify any person in her reports.
C. Did the RPD err by ignoring one of the grounds supporting the application, i.e. the female applicant’s political opinions?

[45] Contrary to what she states in her memorandum, during the hearing, the female applicant never raised the “political opinions” as grounds in support of her application. In response to question 28 of the PIF, the female applicant instead indicated that she was requesting refugee protection on the basis of membership in a particular social group; however, there was never a question of political opinions. The point was also not raised during the hearing. Further, in determining an application for refugee status, it was up to the female applicant to establish, on a balance of probabilities, the facts on which she based her application, which the female applicant did not do with respect to the political opinions. in this matter A decision-maker cannot be criticized for not considering it when the female applicant did not raise or submit it during her testimony. No person is bound to the impossible. Moreover, I also note that during the arguments, the topic was not brought up.

[46] Therefore, the RPD did not err with respect to the grounds in support of the application. On the whole, it is a decision that gives full importance to the female applicant’s testimony. The decision was adjusted to the testimony. It is clear that the facts submitted could not have been recognized as credible and, therefore, the applicants did not meet their burden under sections 96 and 97 of the IRPA.

[47] I would add that while the RPD did not specifically identify its analysis for the purposes of sections 96 and 97 of the IRPA, a careful reading of the decision reveals that the RPD analyzed the facts in evidence, considering the above-noted sections. Of course, it could have been better written, but this is not a reason to say that it is incorrect or unreasonable.

[48] The parties were invited to submit a question for certification, but none was proposed.


## 24325:4 · paragraphs 50-51

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `008cab91637e432397c9e8cdafc49ff40d23bcf36da73727cb0b1cb3fddb45b9`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24325:4:subtheme:1 · paragraphs 50-51

- Raw key terms: `adjudges, application, arreaga, catherine, cause, certified, citizenship, court`
- Display key terms: `adjudges, arreaga, catherine, certified`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: adjudges, arreaga, catherine, certified No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 50-51. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THIS COURT ORDERS AND ADJUDGES that this application for judicial review is dismissed and no question is certified.
“Simon Noël”
Judge
Certified true translation
Catherine Jones, Translator
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-996-13
STYLE OF CAUSE: YANIRA JEANETH GARCIA ARREAGA ET AL v
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Montréal, Quebec
DATE OF HEARING: September 23, 2013
REASONS FOR 

## 24325:5 · paragraphs 52-52

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `609b50006a28f78459fa50139b24f5c91d6aefaeb5038aed396b26f4db7825c7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24325:5:subtheme:1 · paragraphs 52-52

- Raw key terms: `angelica, appearances, applicants, attorney, baum, canada, counsel, daniel`
- Display key terms: `angelica, baum, daniel`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: angelica, baum, daniel No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 52-52. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND JUDGMENT: MR. JUSTICE SIMON NOËL
DATED: September 25, 2013
APPEARANCES:
Angelica Pantiru
FOR THE APPLICANTS
Daniel Baum
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Angelica Pantiru
Counsel
Montréal, Quebec
FOR THE APPLICANTS
William F. Pentney
Deputy Attorney General of Canada
FOR THE RESPONDENT
