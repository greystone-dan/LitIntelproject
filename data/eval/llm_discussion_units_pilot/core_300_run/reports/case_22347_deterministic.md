# Discussion Units: case 22347

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **100**
- Continuity pairs: **99**
- Discussion Units: **5**
- Paragraph source hashes: **100**
- Sub-themes: **30**

## 22347:1 · paragraphs 0-12

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9759fd309dcd9977595088625463e92222fd0f3aefd79d0eb19af570dccc6e6a`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22347:1:subtheme:1 · paragraphs 0-6

- Raw key terms: `innocent, canada, decision, montr, philomena, resident, applicant, applied`
- Display key terms: `innocent, montr, philomena, resident, applied`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, reasoning_application Display terms: innocent, montr, philomena, resident, applied Application context: Innocent arrived in Canada on October 11, 2005, travelling on a temporary resident visa that was granted after she applied to visit her daughter in Canada on a temporary basis. | Following this refusal, the applicant applied for refugee status in Canada. Operative outcome context: Innocent arrived in Canada on October 11, 2005, travelling on a temporary resident visa that was granted after she applied to visit her daughter in Canada on a temporary basis. | Justice Lemieux granted leave on June 17, 2009. Evidence spans paragraphs 0-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `5049101` offsets `123-130`; context: Innocent arrived in Canada on October 11, 2005, travelling on a temporary resident visa that was granted after she applied to visit her daughter in Canada on a temporary basis.
- Evidence: `disposition` cue `granted` at chunk `5049101` offsets `105-112`; context: Innocent arrived in Canada on October 11, 2005, travelling on a temporary resident visa that was granted after she applied to visit her daughter in Canada on a temporary basis.
- Evidence: `reasoning_application` cue `applied` at chunk `5049102` offsets `200-207`; context: Following this refusal, the applicant applied for refugee status in Canada.
- Evidence: `counterargument_limitation` cue `However` at chunk `5049102` offsets `84-91`; context: However, in January 2007, an additional request for an extension was refused.
- Evidence: `evidence_fact` cue `determined that` at chunk `5049103` offsets `178-193`; context: [4] A hearing took place on December 1, 2008, before a panel of the Immigration and Refugee Board (the panel) and, in a decision dated January 14, 2009 (the decision), the panel determined that Ms.
- Evidence: `disposition` cue `granted` at chunk `5049104` offsets `112-119`; context: Justice Lemieux granted leave on June 17, 2009.

#### 22347:1:subtheme:2 · paragraphs 7-11

- Raw key terms: `panel, allegedly, claimant, decision, innocent, neighbourhood, september, testified`
- Display key terms: `allegedly, innocent, neighbourhood, september, testified`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: allegedly, innocent, neighbourhood, september, testified Application context: In about September or October 2005, the authorities allegedly ordered the citizens to leave the neighbourhood because the gangs were invading it. Evidence spans paragraphs 7-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049106` offsets `22-30`; context: [7] The panel did not question Ms.
- Evidence: `reasoning_application` cue `because` at chunk `5049110` offsets `194-201`; context: In about September or October 2005, the authorities allegedly ordered the citizens to leave the neighbourhood because the gangs were invading it.

#### 22347:1:subtheme:3 · paragraphs 12-12

- Raw key terms: `accepted, claimant, decision, facts, generalized, panel, para, personalized`
- Display key terms: `accepted, facts, generalized, para, personalized`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: accepted, facts, generalized, para, personalized Evidence spans paragraphs 12-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049111` offsets `61-69`; context: [10] The panel accepted these facts as true and had only one question, i.

#### Section text

Innocent v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2009-10-08
Neutral citation
2009 FC 1019
File numbers
IMM-541-09
Notes
Digest
Decision Content
Date: 20091008
Docket: IMM‑541‑09
Citation: 2009 FC 1019
Montréal, Quebec, October 8, 2009
PRESENT: The Honourable Mr. Justice Mainville
BETWEEN:
PHILOMENA INNOCENT
Applicant
and
MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT
Introduction

[1] Ms. Philomena Innocent is a septuagenarian citizen of Haiti who currently lives in Laval, a suburb of Montréal, with her daughter, who is a permanent resident of Canada.

[2] Ms. Innocent arrived in Canada on October 11, 2005, travelling on a temporary resident visa that was granted after she applied to visit her daughter in Canada on a temporary basis.

[3] The temporary resident authorization was renewed or extended a number of times. However, in January 2007, an additional request for an extension was refused. Following this refusal, the applicant applied for refugee status in Canada.

[4] A hearing took place on December 1, 2008, before a panel of the Immigration and Refugee Board (the panel) and, in a decision dated January 14, 2009 (the decision), the panel determined that Ms. Philomena Innocent was neither a “Convention refugee” nor “person in need of protection” (decision para. 20).

[5] Ms. Innocent brought an application for leave and judicial review of that decision, and Mr. Justice Lemieux granted leave on June 17, 2009.

[6] The judicial review hearing took place before the undersigned at Montréal on September 15, 2009.
Decision submitted for judicial review

[7] The panel did not question Ms. Innocent’s credibility and concluded as follows on this point: “Despite some inconsistencies and evasive responses, the panel takes into account Maldonado, which reads in part as follows: ‘When an applicant swears to the truth of certain allegations, this creates a presumption that those allegations are true unless there be reason to doubt their truthfulness’, and gives [Ms. Innocent] the benefit of the doubt.” (decision, para. 12).

[8] The panel accepted Ms. Innocent’s narrative as true, and the Minister did not challenge it before the Court.

[9] The panel considered the following facts, as summarized by the panel in its decision:

[7] The claimant testified that she lived in Port‑au‑Prince, in the Bel Air neighbourhood, and had a small business in her house. Starting in September 2005, she was allegedly attacked on three occasions. Some people went to her home to rob her, demanding the money that she received from her daughter who lives in Canada.

[8] The claimant testified that the police were afraid to go to that neighbourhood. In about September or October 2005, the authorities allegedly ordered the citizens to leave the neighbourhood because the gangs were invading it. The claimant testified that she had nowhere else to go, since her children live in the provinces. . . .

[10] The panel accepted these facts as true and had only one question, i.e., “whether the risk to which the claimant could be subject is personalized or generalized” (decision, para. 13).

## 22347:2 · paragraphs 13-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `96ae67821bb82ce272f44aee047dda00b9022f56bff341c3a5b3c2fbcf4bbdbd`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22347:2:subtheme:1 · paragraphs 13-19

- Raw key terms: `entire, evidence, haiti, insecurity, panel, population, documentary, violence`
- Display key terms: `entire, haiti, insecurity, population, documentary, violence`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: entire, haiti, insecurity, population, documentary, violence Application context: However, the claimant also testified that the police were afraid to go to the neighbourhood where she lived because the gangs had invaded it. Evidence spans paragraphs 13-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049112` offsets `32-40`; context: [11] The tribunal answered this question in a few paragraphs:
- Evidence: `evidence_fact` cue `evidence` at chunk `5049113` offsets `27-35`; context: The documentary evidence has established that a state of violence and insecurity prevails in Haiti and affects the entire population.
- Evidence: `evidence_fact` cue `evidence` at chunk `5049114` offsets `275-283`; context: [14] In reaching this conclusion, the panel relies on the recent case law, which establishes in particular that, although being perceived as rich or returning from abroad puts a person at greater risk of being subject to criminal acts, this risk is generalized when there is evidence establishing that the entire population faces the same risk.
- Evidence: `evidence_fact` cue `evidence` at chunk `5049115` offsets `21-29`; context: [15] The documentary evidence also indicates that insecurity, violence and impunity are present in Haiti and particularly the capital, Port‑au‑Prince.
- Evidence: `reasoning_application` cue `because` at chunk `5049116` offsets `254-261`; context: However, the claimant also testified that the police were afraid to go to the neighbourhood where she lived because the gangs had invaded it.
- Evidence: `counterargument_limitation` cue `However` at chunk `5049116` offsets `146-153`; context: However, the claimant also testified that the police were afraid to go to the neighbourhood where she lived because the gangs had invaded it.
- Evidence: `evidence_fact` cue `evidence` at chunk `5049118` offsets `56-64`; context: [18] The panel is of the opinion that, according to the evidence adduced before it, the risk to which the claimant could be subjected is a generalized risk affecting the entire population of the country and not a personalized risk, which means that paragraph 97(1)(b) is not applicable.

#### 22347:2:subtheme:2 · paragraphs 20-22

- Raw key terms: `panel, applicant, finding, paragraph, accordingly, affects, alternative, although`
- Display key terms: `finding, paragraph, accordingly, affects, alternative, although`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: finding, paragraph, accordingly, affects, alternative, although Application context: Accordingly, the application for judicial review applies only to the panel’s findings on the application of paragraph 97(1)(b) of the Act, which is reproduced below. Evidence spans paragraphs 20-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5049119` offsets `35-42`; context: [12] The tribunal did not consider whether there was an internal flight alternative in Haiti although some of the evidence may suggest that this solution was available to Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `5049119` offsets `114-122`; context: [12] The tribunal did not consider whether there was an internal flight alternative in Haiti although some of the evidence may suggest that this solution was available to Ms.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5049120` offsets `181-192`; context: Accordingly, the application for judicial review applies only to the panel’s findings on the application of paragraph 97(1)(b) of the Act, which is reproduced below.

#### 22347:2:subtheme:3 · paragraphs 23-26

- Raw key terms: `applicant, counsel, applied, court, decisions, first, notes, paragraph`
- Display key terms: `applied, decisions, first, notes, paragraph`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: applied, decisions, first, notes, paragraph Position/evidence statements: Consequently, counsel for the Minister contends that only the reasonableness standard of review applies to the entire decision submitted for this judicial review. Rule/authority context: [15] Counsel for the applicant suggests that the Court should apply the correctness standard of review to the first question and the reasonableness standard of review to the second. | Consequently, counsel for the Minister contends that only the reasonableness standard of review applies to the entire decision submitted for this judicial review. Application context: [15] Counsel for the applicant suggests that the Court should apply the correctness standard of review to the first question and the reasonableness standard of review to the second. | [16] Counsel for the Minister notes the two questions raised by the applicant but maintains that the interpretation of paragraph 97(1)(b) is not at issue in this case since the panel simply applied the statutory provisio Evidence spans paragraphs 23-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049122` offsets `116-124`; context: [15] Counsel for the applicant suggests that the Court should apply the correctness standard of review to the first question and the reasonableness standard of review to the second.
- Evidence: `governing_rule` cue `standard of review` at chunk `5049122` offsets `84-102`; context: [15] Counsel for the applicant suggests that the Court should apply the correctness standard of review to the first question and the reasonableness standard of review to the second.
- Evidence: `reasoning_application` cue `apply` at chunk `5049122` offsets `62-67`; context: [15] Counsel for the applicant suggests that the Court should apply the correctness standard of review to the first question and the reasonableness standard of review to the second.
- Evidence: `issue` cue `issue` at chunk `5049123` offsets `148-153`; context: [16] Counsel for the Minister notes the two questions raised by the applicant but maintains that the interpretation of paragraph 97(1)(b) is not at issue in this case since the panel simply applied the statutory provision to the facts of the case.
- Evidence: `party_position` cue `contends` at chunk `5049123` offsets `287-295`; context: Consequently, counsel for the Minister contends that only the reasonableness standard of review applies to the entire decision submitted for this judicial review.
- Evidence: `governing_rule` cue `standard of review` at chunk `5049123` offsets `325-343`; context: Consequently, counsel for the Minister contends that only the reasonableness standard of review applies to the entire decision submitted for this judicial review.
- Evidence: `reasoning_application` cue `applied` at chunk `5049123` offsets `190-197`; context: [16] Counsel for the Minister notes the two questions raised by the applicant but maintains that the interpretation of paragraph 97(1)(b) is not at issue in this case since the panel simply applied the statutory provision to the facts of the case.
- Evidence: `governing_rule` cue `under` at chunk `5049124` offsets `433-438`; context: (d) ensures that decisions taken under this Act are consistent with the Canadian Charter of Rights and Freedoms, including its principles of equality and freedom from discrimination and of the equality of English and French as the official languages of Canada;
.
- Evidence: `reasoning_application` cue `applied` at chunk `5049124` offsets `369-376`; context: 3(3) This Act is to be construed and applied in a manner that
.

#### 22347:2:subtheme:4 · paragraphs 27-28

- Raw key terms: `generalized, need, person, population, protection, risk, status, according`
- Display key terms: `generalized, need, person, population, protection, risk, status, according`
- Argument roles: `counterargument_limitation, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue Display terms: generalized, need, person, population, protection, risk, status, according Rule/authority context: [19] According to the first school of jurisprudence, this provision of the Act should be interpreted as not conferring the status of person in need of protection on applicants who face a risk similar to the risk faced by Evidence spans paragraphs 27-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049126` offsets `276-284`; context: [19] According to the first school of jurisprudence, this provision of the Act should be interpreted as not conferring the status of person in need of protection on applicants who face a risk similar to the risk faced by a significant part of the population of the country in question, despite the fact that these applicants may be members of subgroups who face more significant risk than this generalized risk.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5049126` offsets `38-51`; context: [19] According to the first school of jurisprudence, this provision of the Act should be interpreted as not conferring the status of person in need of protection on applicants who face a risk similar to the risk faced by a significant part of the population of the country in question, despite the fact that these applicants may be members of subgroups who face more significant risk than this generalized risk.
- Evidence: `counterargument_limitation` cue `although` at chunk `5049127` offsets `294-302`; context: Canada (Citizenship and Immigration), 2008 FC 331, a Haitian businessman sought person in need of protection status on the ground that wealthy people or those perceived as such in Haiti are more at risk of criminal violence than the entire population of Haiti, although criminal violence is generalized in Haiti.

#### Section text

[11] The tribunal answered this question in a few paragraphs:

[13] . . . The documentary evidence has established that a state of violence and insecurity prevails in Haiti and affects the entire population. That said, the panel is of the opinion that business persons are not a particular social group as defined in Ward. [Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689].

[14] In reaching this conclusion, the panel relies on the recent case law, which establishes in particular that, although being perceived as rich or returning from abroad puts a person at greater risk of being subject to criminal acts, this risk is generalized when there is evidence establishing that the entire population faces the same risk. The reliable and objective documentary evidence adduced and cited above confirms that the insecurity prevailing in Haiti is generalized and thus affects all social classes.

[15] The documentary evidence also indicates that insecurity, violence and impunity are present in Haiti and particularly the capital, Port‑au‑Prince. The Port‑au‑Prince gangs are centred in Cité Soleil and the neighbourhoods to its immediate the north and east, including Cité Militaire, Bel Air, Solino and Delmas. . . .

[16] In short, the entire population of Haiti is victimized by the risks resulting from the violence, insecurity and crime that persist in Haiti. However, the claimant also testified that the police were afraid to go to the neighbourhood where she lived because the gangs had invaded it. The government even asked the citizens to leave the neighbourhood, which the claimant did not do.

[17] Consequently, the panel cannot establish a nexus between the fear of persecution and one of the five grounds set out in section 96 of the Act.

[18] The panel is of the opinion that, according to the evidence adduced before it, the risk to which the claimant could be subjected is a generalized risk affecting the entire population of the country and not a personalized risk, which means that paragraph 97(1)(b) is not applicable.

[12] The tribunal did not consider whether there was an internal flight alternative in Haiti although some of the evidence may suggest that this solution was available to Ms. Innocent. In fact, she testified that some of her children lived in the provinces in Haiti and that the Haitian police were encouraging the residents of her neighbourhood to leave voluntarily. It is not clear whether the failure to examine an internal flight alternative stemmed from the panel’s position that the state of violence and insecurity that prevails in Haiti affects the entire country or whether the panel did not believe it was necessary to deal with this issue, given its finding on the lack of a personalized risk.
Issues

[13] We note at the outset that the applicant is not disputing the panel’s finding that she does not fall within section 96 of the Immigration and Refugee Protection Act (the Act). Accordingly, the application for judicial review applies only to the panel’s findings on the application of paragraph 97(1)(b) of the Act, which is reproduced below.

[14] In this regard, counsel for the applicant raised two questions in oral argument before the Court:
a. Did the panel err in interpreting paragraph 97(1)(b) of the Act?
b. Did the panel err in applying paragraph 97(1)(b) of the Act to the facts of this case?

[15] Counsel for the applicant suggests that the Court should apply the correctness standard of review to the first question and the reasonableness standard of review to the second.

[16] Counsel for the Minister notes the two questions raised by the applicant but maintains that the interpretation of paragraph 97(1)(b) is not at issue in this case since the panel simply applied the statutory provision to the facts of the case. Consequently, counsel for the Minister contends that only the reasonableness standard of review applies to the entire decision submitted for this judicial review.
Relevant statutory provisions

[17] The relevant provisions of the Act are paragraph 3(2)(a), paragraph 3(3)(d), subsection 97(1) and subsection 107(1):
3(2) The objectives of this Act with respect to refugees are
(a) to recognize that the refugee program is in the first instance about saving lives and offering protection to the displaced and persecuted;
. . .
3(3) This Act is to be construed and applied in a manner that
. . .
(d) ensures that decisions taken under this Act are consistent with the Canadian Charter of Rights and Freedoms, including its principles of equality and freedom from discrimination and of the equality of English and French as the official languages of Canada;
. . .
97(1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
107(1) The Refugee Protection Division shall accept a claim for refugee protection if it determines that the claimant is a Convention refugee or person in need of protection, and shall otherwise reject the claim.
3(2) S’agissant des réfugiés, la présente loi a pour objet :
a) de reconnaître que le programme pour les réfugiés vise avant tout à sauver des vies et à protéger les personnes de la persécution;
…
3(3) L’interprétation et la mise en oeuvre de la présente loi doivent avoir pour effet :
...
d) d’assurer que les décisions prises en vertu de la présente loi sont conformes à la Charte canadienne des droits et libertés, notamment en ce qui touche les principes, d’une part, d’égalité et de protection contre la discrimination et, d’autre part, d’égalité du français et de l’anglais à titre de langues officielles du Canada;
...
97(1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles‑ci ou occasionnés par elles,
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
107(1) La Section de la protection des réfugiés accepte ou rejette la demande d’asile selon que le demandeur a ou non la qualité de réfugié ou de personne à protéger.
Applicant’s position

[18] Counsel for the applicant notes a debate in the Court’s decisions on interpreting subparagraph 97(1)(b)(ii) of the Act.

[19] According to the first school of jurisprudence, this provision of the Act should be interpreted as not conferring the status of person in need of protection on applicants who face a risk similar to the risk faced by a significant part of the population of the country in question, despite the fact that these applicants may be members of subgroups who face more significant risk than this generalized risk.

[20] For example, in Prophète v. Canada (Citizenship and Immigration), 2008 FC 331, a Haitian businessman sought person in need of protection status on the ground that wealthy people or those perceived as such in Haiti are more at risk of criminal violence than the entire population of Haiti, although criminal violence is generalized in Haiti. Madam Justice Tremblay‑Lamer refused to grant person in need of protection status in such a case on the following grounds:

## 22347:3 · paragraphs 29-37

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `32af52a1fd5ef726b9d2607da06703b8a8530a5954844e1394beb3d25a4f9116`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22347:3:subtheme:1 · paragraphs 29-31

- Raw key terms: `applicant, larger, population, analyzing, asserted, because, born, canada`
- Display key terms: `larger, population, analyzing, asserted, because, born`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: larger, population, analyzing, asserted, because, born Rule/authority context: Under these circumstances, the Court may be faced with an applicant who has been targeted in the past and who may be targeted in the future but whose risk situation is similar to a segment of the larger population. Application context: In that case, the applicant asserted that if he and his young Canadian born son were returned to Colombia it would constitute indirect cruel and unusual treatment/punishment because of the psychological stress that he wo Evidence spans paragraphs 29-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `Under` at chunk `5049128` offsets `237-242`; context: Under these circumstances, the Court may be faced with an applicant who has been targeted in the past and who may be targeted in the future but whose risk situation is similar to a segment of the larger population.
- Evidence: `reasoning_application` cue `because` at chunk `5049129` offsets `450-457`; context: In that case, the applicant asserted that if he and his young Canadian born son were returned to Colombia it would constitute indirect cruel and unusual treatment/punishment because of the psychological stress that he would experience as a parent worrying about his child’s welfare in that country.

#### 22347:3:subtheme:2 · paragraphs 32-37

- Raw key terms: `jurisprudence, applicant, because, canada, counsel, court, generally, group`
- Display key terms: `jurisprudence, because, generally, group`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: jurisprudence, because, generally, group Position/evidence statements: [24] Counsel for the applicant submits that this is the approach taken by the second school of jurisprudence of the Court, which includes, inter alia, the decisions in Surajnarain v. Rule/authority context: [23] Based on the recent jurisprudence of this Court, I am of the view that the applicant does not face a personalized risk that is not faced generally by other individuals in or from Haiti. | [21] Other than the Prophète decision, above, this first school of jurisprudence includes Ventura De Parada v. Application context: While a specific number of individuals may be targeted more frequently because of their wealth, all Haitians are at risk of becoming the victims of violence. | [22] In the view of counsel for the applicant, the interpretation given to 97(1)(b)(ii) of the Act by this school of jurisprudence is erroneous because it would lead to arbitrary results. Evidence spans paragraphs 32-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5049131` offsets `320-325`; context: 97(1)(b)(ii), thereby leaving to the Board the issue of deciding whether a particular group meets the definition.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5049132` offsets `25-38`; context: [23] Based on the recent jurisprudence of this Court, I am of the view that the applicant does not face a personalized risk that is not faced generally by other individuals in or from Haiti.
- Evidence: `reasoning_application` cue `because` at chunk `5049132` offsets `336-343`; context: While a specific number of individuals may be targeted more frequently because of their wealth, all Haitians are at risk of becoming the victims of violence.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5049133` offsets `67-80`; context: [21] Other than the Prophète decision, above, this first school of jurisprudence includes Ventura De Parada v.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5049134` offsets `117-130`; context: [22] In the view of counsel for the applicant, the interpretation given to 97(1)(b)(ii) of the Act by this school of jurisprudence is erroneous because it would lead to arbitrary results.
- Evidence: `reasoning_application` cue `because` at chunk `5049134` offsets `144-151`; context: [22] In the view of counsel for the applicant, the interpretation given to 97(1)(b)(ii) of the Act by this school of jurisprudence is erroneous because it would lead to arbitrary results.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5049135` offsets `441-454`; context: This reasoning requires disregarding the jurisprudence cited above and favouring an approach that establishes a personalized risk by reason of membership in an at-risk group, in this case, the group of persons who may be perceived as more affluent and, therefore, more likely to be victims of generalized violence.
- Evidence: `reasoning_application` cue `because` at chunk `5049135` offsets `162-169`; context: [23] The applicant notes that she is at greater risk than the rest of the Haitian population of being subject to the generalized crime that is prevalent in Haiti because she is part of a group of persons who are perceived as more affluent.
- Evidence: `party_position` cue `submits` at chunk `5049136` offsets `31-38`; context: [24] Counsel for the applicant submits that this is the approach taken by the second school of jurisprudence of the Court, which includes, inter alia, the decisions in Surajnarain v.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5049136` offsets `95-108`; context: [24] Counsel for the applicant submits that this is the approach taken by the second school of jurisprudence of the Court, which includes, inter alia, the decisions in Surajnarain v.

#### Section text

[18] The difficulty in analyzing personalized risk in situations of generalized human rights violations, civil war, and failed states lies in determining the dividing line between a risk that is “personalized” and one that is “general”. Under these circumstances, the Court may be faced with an applicant who has been targeted in the past and who may be targeted in the future but whose risk situation is similar to a segment of the larger population. Thus, the Court is faced with an individual who may have a personalized risk, but one that is shared by many other individuals.

[19] Recently, the term “generally” was interpreted in a manner that may include segments of the larger population, as well as all residents or citizens of a given country: Osorio v. Canada (Minister of Citizenship and Immigration), 2005 FC 1459, [2005] F.C.J. No. 1792 (QL). In that case, the applicant asserted that if he and his young Canadian born son were returned to Colombia it would constitute indirect cruel and unusual treatment/punishment because of the psychological stress that he would experience as a parent worrying about his child’s welfare in that country. At paras. 24 and 26 Snider J. stated:

[24] It seems to me that common sense must determine the meaning of s. 97(1)(b)(ii) …

[26] Further, I can see nothing in s. 97(1)(b)(ii) that requires the Board to interpret “generally” as applying to all citizens. The word “generally” is commonly used to mean “prevalent” or “wide‑spread”. Parliament deliberately chose to include the word “generally” in s. 97(1)(b)(ii), thereby leaving to the Board the issue of deciding whether a particular group meets the definition. Provided that its conclusion is reasonable, as it is here, I see no need to intervene. [Not underlined in the original.]
. . .

[23] Based on the recent jurisprudence of this Court, I am of the view that the applicant does not face a personalized risk that is not faced generally by other individuals in or from Haiti. The risk of all forms of criminality is general and felt by all Haitians. While a specific number of individuals may be targeted more frequently because of their wealth, all Haitians are at risk of becoming the victims of violence.

[21] Other than the Prophète decision, above, this first school of jurisprudence includes Ventura De Parada v. Canada (Citizenship and Immigration), 2009 FC 845 (Mr. Justice Zinn), Acosta v. Canada (Citizenship and Immigration), 2009 FC 213 (Madam Justice Gauthier), Cius v. Canada (Citizenship and Immigration), 2008 FC 1 (Mr. Justice Beaudry), Étienne v. Canada (Citizenship and Immigration), 2007 FC 64 (Mr. Justice Shore), and Osorio v. Canada (Minister of Citizenship and Immigration), 2005 FC 1459 (Madam Justice Snider). A number of other decisions could be added to this list, including Jeudy v. Canada (Minister of Citizenship and Immigration), 2005 FC 1124 (Mr. Justice Lemieux).

[22] In the view of counsel for the applicant, the interpretation given to 97(1)(b)(ii) of the Act by this school of jurisprudence is erroneous because it would lead to arbitrary results. In fact, this interpretation is based on a prior determination of the existence of an at-risk group sufficiently large to come under the word “generally” used in that subparagraph. In what circumstances is a threatened group large enough for a threatened person to lose Canada’s protection? Is this not a purely arbitrary and subjective determination?

[23] The applicant notes that she is at greater risk than the rest of the Haitian population of being subject to the generalized crime that is prevalent in Haiti because she is part of a group of persons who are perceived as more affluent. Her counsel therefore asks the Court to set aside the panel’s decision on the ground that it erred in law in interpreting subparagraph 97(1)(b)(ii) of the Act. This reasoning requires disregarding the jurisprudence cited above and favouring an approach that establishes a personalized risk by reason of membership in an at-risk group, in this case, the group of persons who may be perceived as more affluent and, therefore, more likely to be victims of generalized violence.

[24] Counsel for the applicant submits that this is the approach taken by the second school of jurisprudence of the Court, which includes, inter alia, the decisions in Surajnarain v. Canada (Citizenship and Immigration), 2008 FC 1165 (Madam Justice Dawson) and Sinnappu v. Canada (Minister of Citizenship and Immigration), [1997] 2 FC 791 (Mr. Justice McGillis).

## 22347:4 · paragraphs 38-97

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a74661100e2f4cf85c4e9f4de3a23d7880eab192e1006e33cecb29794aa290b9`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22347:4:subtheme:1 · paragraphs 38-39

- Raw key terms: `above, applicant, apply, approach, claimant, clearly, counsel, country`
- Display key terms: `above, apply, approach, clearly, country`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: above, apply, approach, clearly, country Rule/authority context: [25] In the view of counsel for the applicant, Justice Dawson clearly explained the approach of this second school of jurisprudence in obiter dictum in Surajnarain, above: Application context: [16] Of relevance was the requirement that a claimant must establish that his removal would subject him to “an objectively identifiable risk, which risk would apply in every part of that country and would not be faced ge Evidence spans paragraphs 38-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5049137` offsets `118-131`; context: [25] In the view of counsel for the applicant, Justice Dawson clearly explained the approach of this second school of jurisprudence in obiter dictum in Surajnarain, above:
- Evidence: `reasoning_application` cue `apply` at chunk `5049138` offsets `159-164`; context: [16] Of relevance was the requirement that a claimant must establish that his removal would subject him to “an objectively identifiable risk, which risk would apply in every part of that country and would not be faced generally by other individuals in or from that country.

#### 22347:4:subtheme:2 · paragraphs 40-41

- Raw key terms: `apply, citizens, class, country, faced, generally, guidelines, individual`
- Display key terms: `apply, citizens, class, country, faced, generally, guidelines, individual`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: apply, citizens, class, country, faced, generally, guidelines, individual Rule/authority context: Any risk that would apply to all residents or citizens of the country of origin cannot result in a positive decision under this Regulation. Application context: would not be faced generally by other individuals in or from that country” applies. | Indeed, during his cross‑examination, Gilbert Troutet, a specialist in PDRCC class applications, stated that the exclusion would apply only “in extreme situations such as a generalized disaster of some sort that would in Evidence spans paragraphs 40-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `5049139` offsets `650-657`; context: Whether or not the risk is associated with a “Convention” ground, a person may fall within the scope of this definition.
- Evidence: `governing_rule` cue `under` at chunk `5049139` offsets `1072-1077`; context: Any risk that would apply to all residents or citizens of the country of origin cannot result in a positive decision under this Regulation.
- Evidence: `reasoning_application` cue `applies` at chunk `5049139` offsets `946-953`; context: would not be faced generally by other individuals in or from that country” applies.
- Evidence: `counterargument_limitation` cue `Notwithstanding` at chunk `5049139` offsets `771-786`; context: Notwithstanding this, the limitation imposed by the PDRCC definition in the phrase “which risk .
- Evidence: `reasoning_application` cue `apply` at chunk `5049140` offsets `720-725`; context: Indeed, during his cross‑examination, Gilbert Troutet, a specialist in PDRCC class applications, stated that the exclusion would apply only “in extreme situations such as a generalized disaster of some sort that would involve all of the inhabitants of a given country.

#### 22347:4:subtheme:3 · paragraphs 42-43

- Raw key terms: `subparagraph, appeal, applicant, application, based, board, canada, citizenship`
- Display key terms: `subparagraph, based`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: subparagraph, based Rule/authority context: [19] Thus, the Board should consider whether application of the principles set out in Salibian and Sinnappu lead to the conclusion that a claimant may only be denied protection under subparagraph 97(1)(b)(ii) of the Act  Application context: Based on that, he concludes that the state of the law on this point is far from satisfactory. Operative outcome context: [19] Thus, the Board should consider whether application of the principles set out in Salibian and Sinnappu lead to the conclusion that a claimant may only be denied protection under subparagraph 97(1)(b)(ii) of the Act  Evidence spans paragraphs 42-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5049141` offsets `37-44`; context: [19] Thus, the Board should consider whether application of the principles set out in Salibian and Sinnappu lead to the conclusion that a claimant may only be denied protection under subparagraph 97(1)(b)(ii) of the Act if the risk is faced generally by all of the other persons in the country.
- Evidence: `governing_rule` cue `principles` at chunk `5049141` offsets `64-74`; context: [19] Thus, the Board should consider whether application of the principles set out in Salibian and Sinnappu lead to the conclusion that a claimant may only be denied protection under subparagraph 97(1)(b)(ii) of the Act if the risk is faced generally by all of the other persons in the country.
- Evidence: `disposition` cue `denied` at chunk `5049141` offsets `159-165`; context: [19] Thus, the Board should consider whether application of the principles set out in Salibian and Sinnappu lead to the conclusion that a claimant may only be denied protection under subparagraph 97(1)(b)(ii) of the Act if the risk is faced generally by all of the other persons in the country.
- Evidence: `reasoning_application` cue `concludes` at chunk `5049142` offsets `233-242`; context: Based on that, he concludes that the state of the law on this point is far from satisfactory.

#### 22347:4:subtheme:4 · paragraphs 44-46

- Raw key terms: `application, applicant, case, decision, gang, justice, montigny, number`
- Display key terms: `case, gang, justice, montigny, number`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: case, gang, justice, montigny, number Rule/authority context: [27] Counsel for the applicant adds as an alternative argument that, even if the Court agrees with the first school of jurisprudence in its interpretation of subparagraph 97(1)(b)(ii) of the Act, the panel’s decision sho | Canada (Citizenship and Immigration), 2007 FC 365 where he allowed an application for judicial review of a decision refusing person in need of protection status under subsection 97(1)(b) of the Act to a Salvadorean citiz Application context: [27] Counsel for the applicant adds as an alternative argument that, even if the Court agrees with the first school of jurisprudence in its interpretation of subparagraph 97(1)(b)(ii) of the Act, the panel’s decision sho | [28] In fact, we are not dealing solely with the case of a person who fears violence by reason of his or her membership in a particular group and who is therefore more at risk than the entire population. Operative outcome context: Canada (Citizenship and Immigration), 2007 FC 365 where he allowed an application for judicial review of a decision refusing person in need of protection status under subsection 97(1)(b) of the Act to a Salvadorean citiz | Pineda’s application was therefore denied by the panel on the ground that the risk faced by the applicant was no different from that faced by the Salvadorean population in general. Evidence spans paragraphs 44-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049143` offsets `339-347`; context: [27] Counsel for the applicant adds as an alternative argument that, even if the Court agrees with the first school of jurisprudence in its interpretation of subparagraph 97(1)(b)(ii) of the Act, the panel’s decision should nonetheless be set aside because the application of that subparagraph, as interpreted in this way, to the facts in question is not reasonable.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5049143` offsets `119-132`; context: [27] Counsel for the applicant adds as an alternative argument that, even if the Court agrees with the first school of jurisprudence in its interpretation of subparagraph 97(1)(b)(ii) of the Act, the panel’s decision should nonetheless be set aside because the application of that subparagraph, as interpreted in this way, to the facts in question is not reasonable.
- Evidence: `reasoning_application` cue `because` at chunk `5049143` offsets `249-256`; context: [27] Counsel for the applicant adds as an alternative argument that, even if the Court agrees with the first school of jurisprudence in its interpretation of subparagraph 97(1)(b)(ii) of the Act, the panel’s decision should nonetheless be set aside because the application of that subparagraph, as interpreted in this way, to the facts in question is not reasonable.
- Evidence: `governing_rule` cue `under` at chunk `5049144` offsets `576-581`; context: Canada (Citizenship and Immigration), 2007 FC 365 where he allowed an application for judicial review of a decision refusing person in need of protection status under subsection 97(1)(b) of the Act to a Salvadorean citizen.
- Evidence: `reasoning_application` cue `therefore` at chunk `5049144` offsets `153-162`; context: [28] In fact, we are not dealing solely with the case of a person who fears violence by reason of his or her membership in a particular group and who is therefore more at risk than the entire population.
- Evidence: `disposition` cue `allowed` at chunk `5049144` offsets `474-481`; context: Canada (Citizenship and Immigration), 2007 FC 365 where he allowed an application for judicial review of a decision refusing person in need of protection status under subsection 97(1)(b) of the Act to a Salvadorean citizen.
- Evidence: `evidence_fact` cue `Evidence` at chunk `5049145` offsets `133-141`; context: Evidence was adduced that street gangs recruited across the country; Mr.
- Evidence: `reasoning_application` cue `therefore` at chunk `5049145` offsets `231-240`; context: Pineda’s application was therefore denied by the panel on the ground that the risk faced by the applicant was no different from that faced by the Salvadorean population in general.
- Evidence: `disposition` cue `denied` at chunk `5049145` offsets `241-247`; context: Pineda’s application was therefore denied by the panel on the ground that the risk faced by the applicant was no different from that faced by the Salvadorean population in general.

#### 22347:4:subtheme:5 · paragraphs 47-47

- Raw key terms: `above, alleged, amounts, applicant, application, based, case, circumstances`
- Display key terms: `above, alleged, amounts, based, case, circumstances`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: above, alleged, amounts, based, case, circumstances Operative outcome context: If such were the case, the application would have to be dismissed for the same reasons that led the Court to confirm the RPD decisions in the two matters mentioned above [Jeudy and Osorio, above]. Evidence spans paragraphs 47-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049146` offsets `527-535`; context: Unless we question the truthfulness of his story, which the RPD did not do, we have no doubt that he will be personally in danger if he were to return to El Salvador.
- Evidence: `disposition` cue `dismissed` at chunk `5049146` offsets `226-235`; context: If such were the case, the application would have to be dismissed for the same reasons that led the Court to confirm the RPD decisions in the two matters mentioned above [Jeudy and Osorio, above].

#### 22347:4:subtheme:6 · paragraphs 48-53

- Raw key terms: `court, above, decision, jurisprudence, standard, appropriate, canada, case`
- Display key terms: `above, jurisprudence, standard, appropriate, case`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application Display terms: above, jurisprudence, standard, appropriate, case Rule/authority context: [30] Counsel for the Minister maintains that the panel’s decision does not deal with the interpretation of subsection 97(1)(b)(ii) of the Act but is limited to the application of the provision to the facts of the case in | [32] He adds that the Court’s recent jurisprudence is clear on the principles to be applied in such cases. Application context: [32] He adds that the Court’s recent jurisprudence is clear on the principles to be applied in such cases. Operative outcome context: Consequently, the decision of Justice Tremblay‑Lamer in Prophète, above, is determinative, especially because the Federal Court of Appeal upheld the judge’s findings in this matter. Evidence spans paragraphs 48-53. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5049147` offsets `264-277`; context: [30] Counsel for the Minister maintains that the panel’s decision does not deal with the interpretation of subsection 97(1)(b)(ii) of the Act but is limited to the application of the provision to the facts of the case in light of the clear majority of the Court’s jurisprudence concerning the scope of the provision.
- Evidence: `counterargument_limitation` cue `but` at chunk `5049147` offsets `142-145`; context: [30] Counsel for the Minister maintains that the panel’s decision does not deal with the interpretation of subsection 97(1)(b)(ii) of the Act but is limited to the application of the provision to the facts of the case in light of the clear majority of the Court’s jurisprudence concerning the scope of the provision.
- Evidence: `evidence_fact` cue `evidence` at chunk `5049148` offsets `340-348`; context: Each case turns on its own facts, and it is incumbent on the panel to determine the facts in light of the evidence adduced before it.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5049149` offsets `37-50`; context: [32] He adds that the Court’s recent jurisprudence is clear on the principles to be applied in such cases.
- Evidence: `reasoning_application` cue `applied` at chunk `5049149` offsets `84-91`; context: [32] He adds that the Court’s recent jurisprudence is clear on the principles to be applied in such cases.
- Evidence: `disposition` cue `upheld` at chunk `5049149` offsets `245-251`; context: Consequently, the decision of Justice Tremblay‑Lamer in Prophète, above, is determinative, especially because the Federal Court of Appeal upheld the judge’s findings in this matter.
- Evidence: `counterargument_limitation` cue `but` at chunk `5049150` offsets `115-118`; context: [33] Counsel for the Minister acknowledges the recent discordant decision by Justice Dawson in Surajnarain, above, but notes that her comment was obiter dictum, which does not bind the Court and which is essentially based on the Sinnappu decision, above, which dates from 1997 and was made in a different statutory and regulatory context from that of today.
- Evidence: `governing_rule` cue `standard of review` at chunk `5049151` offsets `373-391`; context: To establish the appropriate standard in each case, “[a]n exhaustive review is not required in every case to determine the proper standard of review.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5049152` offsets `317-330`; context: 54), the relevant jurisprudence generally indicates that questions of law relating to refugee status (and, by implication, person in need of protection status) under the Immigration and Refugee Protection Act are reviewable on a standard of correctness: Pushpanathan v.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5049152` offsets `102-110`; context: Although a certain deference may be appropriate where a specialized administrative tribunal is interpreting its own statute or statutes closely connected to its function (Dunsmuir, above, at para.

#### 22347:4:subtheme:7 · paragraphs 54-56

- Raw key terms: `application, case, correctness, fact, interpretation, reasonableness, section, standard`
- Display key terms: `case, correctness, fact, interpretation, reasonableness, section, standard`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: case, correctness, fact, interpretation, reasonableness, section, standard Rule/authority context: [38] The Court is of the view that consideration of an application for protected person status under subsection 97(1)(b)(ii) of the Act requires an individualized assessment in the context of existing and prospective ris Application context: As I explain below, I agree that this standard applies to judicial review of decisions about the application of this subparagraph. | [37] Accordingly, I will apply the correctness standard to the section 97 interpretation and the reasonableness standard to the panel’s findings of fact. Evidence spans paragraphs 54-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049153` offsets `226-234`; context: Canada (Citizenship and Immigration), 2009 FC 886, maintain that the application of subparagraph 97(1)(b)(ii) of the Act is a question of fact reviewable on a standard of reasonableness.
- Evidence: `reasoning_application` cue `applies` at chunk `5049153` offsets `334-341`; context: As I explain below, I agree that this standard applies to judicial review of decisions about the application of this subparagraph.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5049154` offsets `5-16`; context: [37] Accordingly, I will apply the correctness standard to the section 97 interpretation and the reasonableness standard to the panel’s findings of fact.
- Evidence: `governing_rule` cue `under` at chunk `5049155` offsets `95-100`; context: [38] The Court is of the view that consideration of an application for protected person status under subsection 97(1)(b)(ii) of the Act requires an individualized assessment in the context of existing and prospective risks faced by the applicant.

#### 22347:4:subtheme:8 · paragraphs 57-62

- Raw key terms: `analysis, court, analyses, based, particular, textual, above, approach`
- Display key terms: `analysis, analyses, based, particular, textual, above, approach`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: analysis, analyses, based, particular, textual, above, approach Rule/authority context: [42] For the Court, the analysis required under subsection 97(1)(b)(ii) of the Act primarily entails a case-by-case determination of a real and particularized threat directed at an individual. | [44] The Supreme Court of Canada recently reiterated the modern principles of statutory interpretation in Canada Trustco Mortgage Co. Application context: This approach is consistent with the very objectives of the Act, in particular, paragraph 3(2)(a), reproduced above, which recognizes that the refugee program is, in the first instance, about saving lives and offering pr Evidence spans paragraphs 57-62. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049156` offsets `106-114`; context: [39] The requisite analysis includes not only an analysis of the personalized risk faced by the person in question, but also a separate analysis of the risk faced by other individuals from the country in question.
- Evidence: `evidence_fact` cue `evidence` at chunk `5049156` offsets `301-309`; context: The objective of these analyses is to determine, in each particular case, based on the evidence available, whether the personalized risk faced by the applicant exists “in every part of that country and is not faced generally by other individuals in or from that country”.
- Evidence: `issue` cue `question` at chunk `5049157` offsets `241-249`; context: [40] The Court is also of the view that a textual analysis of subparagraph 97(1)(b)(ii) and a pragmatic and functional approach to applying this subparagraph shows that the analysis of the risk faced by other individuals from the country in question is not necessarily limited to an analysis of the risk faced by the entire population but may also include an analysis of the risk faced by only one segment of the population, to the extent that the particular circumstances of each case justify this approach in light of the objectives of the Act and its section 97.
- Evidence: `governing_rule` cue `under` at chunk `5049159` offsets `42-47`; context: [42] For the Court, the analysis required under subsection 97(1)(b)(ii) of the Act primarily entails a case-by-case determination of a real and particularized threat directed at an individual.
- Evidence: `reasoning_application` cue `applied` at chunk `5049159` offsets `552-559`; context: This approach is consistent with the very objectives of the Act, in particular, paragraph 3(2)(a), reproduced above, which recognizes that the refugee program is, in the first instance, about saving lives and offering protection to the displaced and persecuted, and paragraph 3(3)(d), also reproduced above, which provides that the Act is to be construed and applied in a manner that ensures that decisions taken under the Act are consistent with the Canadian Charter of Rights and Freedoms.
- Evidence: `governing_rule` cue `principles` at chunk `5049161` offsets `64-74`; context: [44] The Supreme Court of Canada recently reiterated the modern principles of statutory interpretation in Canada Trustco Mortgage Co.

#### 22347:4:subtheme:9 · paragraphs 63-65

- Raw key terms: `country, risk, faced, french, individuals, pays, subparagraph, alternative`
- Display key terms: `country, risk, faced, french, individuals, pays, subparagraph, alternative`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: country, risk, faced, french, individuals, pays, subparagraph, alternative Evidence spans paragraphs 63-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049162` offsets `170-178`; context: [45] A textual analysis of subparagraph 97(1)(b)(ii) demonstrates that the provision does not require that the risk be faced by all other individuals from the country in question.

#### 22347:4:subtheme:10 · paragraphs 66-69

- Raw key terms: `individuals, risk, country, faced, analysis, canada, certain, determination`
- Display key terms: `individuals, risk, country, faced, analysis, certain, determination`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: individuals, risk, country, faced, analysis, certain, determination Rule/authority context: [49] Thus, in cases such as this one, where the general population faces a risk of criminality, the fact that certain individuals are more likely to face this risk, either because they live in more dangerous areas, or be | The post‑determination refugee claimants in Canada class (the PDRCC class) was formally established under the Immigration Regulations, 1978 — Amendment SOR/93‑44, which provided that the following definition should be in Application context: [49] Thus, in cases such as this one, where the general population faces a risk of criminality, the fact that certain individuals are more likely to face this risk, either because they live in more dangerous areas, or be | A similar provision appeared for the first time in the Regulations in 1993 in order to add a prior review process with respect to individuals to whom the definition of Convention refugee did not apply but who should none Evidence spans paragraphs 66-69. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049165` offsets `22-30`; context: [48] The provision in question does not require that “all other individuals from that country” face the risk, but that the risk is not faced generally “by other individuals in or from that country”.
- Evidence: `governing_rule` cue `under` at chunk `5049166` offsets `350-355`; context: [49] Thus, in cases such as this one, where the general population faces a risk of criminality, the fact that certain individuals are more likely to face this risk, either because they live in more dangerous areas, or because they are perceived as being more affluent, does not necessarily make those individuals eligible for protected person status under subparagraph 97(1)(b)(ii).
- Evidence: `reasoning_application` cue `because` at chunk `5049166` offsets `172-179`; context: [49] Thus, in cases such as this one, where the general population faces a risk of criminality, the fact that certain individuals are more likely to face this risk, either because they live in more dangerous areas, or because they are perceived as being more affluent, does not necessarily make those individuals eligible for protected person status under subparagraph 97(1)(b)(ii).
- Evidence: `governing_rule` cue `under` at chunk `5049167` offsets `471-476`; context: The post‑determination refugee claimants in Canada class (the PDRCC class) was formally established under the Immigration Regulations, 1978 — Amendment SOR/93‑44, which provided that the following definition should be inserted into subsection 2(1) of the Regulations:
“member of the post‑determination refugee claimants in Canada class” means an immigrant in Canada
(a) who the Refugee Division has determined on or after February 1, 1993 is not a Convention refugee .
- Evidence: `reasoning_application` cue `apply` at chunk `5049167` offsets `280-285`; context: A similar provision appeared for the first time in the Regulations in 1993 in order to add a prior review process with respect to individuals to whom the definition of Convention refugee did not apply but who should nonetheless not be returned, since they were at serious risk of harm.

#### 22347:4:subtheme:11 · paragraphs 70-75

- Raw key terms: `class, immigration, pdrcc, refugee, added, canada, country, criteria`
- Display key terms: `class, pdrcc, refugee, added, country, criteria`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: class, pdrcc, refugee, added, country, criteria Rule/authority context: (PDRCC class guidelines) to assist officers reviewing applications for landing under the PDRCC class in interpreting the criteria in the Regulations. | 117 Under the Minister's discretionary power to create classes of persons to single out for special treatment, a class of persons called the Post‑Determination Refugee Claimants in Canada Class was created by regulation  Application context: would not be faced generally by other individuals in or from that country” applies. | Therefore, individuals who face a serious and credible risk may not be able to benefit from protection under s. Evidence spans paragraphs 70-75. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049169` offsets `419-427`; context: Following the review, a recommendation was made to broaden the definition in subsection 2(1) of the Regulations by including factors of generalized risk facing the person upon removal to the country in question.
- Evidence: `governing_rule` cue `under` at chunk `5049169` offsets `785-790`; context: (PDRCC class guidelines) to assist officers reviewing applications for landing under the PDRCC class in interpreting the criteria in the Regulations.
- Evidence: `reasoning_application` cue `applies` at chunk `5049169` offsets `1648-1655`; context: would not be faced generally by other individuals in or from that country” applies.
- Evidence: `governing_rule` cue `Under` at chunk `5049171` offsets `1039-1044`; context: 117 Under the Minister's discretionary power to create classes of persons to single out for special treatment, a class of persons called the Post‑Determination Refugee Claimants in Canada Class was created by regulation in 1993.
- Evidence: `governing_rule` cue `under` at chunk `5049173` offsets `291-296`; context: Specifically, we now have a statutory scheme (not regulatory), the decision on the “person in need of protection” status under section 97 is made at the same time as the decision on the “refugee” status under section 96, and both these decisions are made by the Refugee Protection Division of the Immigration and Refugee Board when applications are submitted in Canada.
- Evidence: `evidence_fact` cue `evidence` at chunk `5049174` offsets `1384-1392`; context: In a civil war situation a claimant would be required to adduce some evidence that the risk faced is not an indiscriminate risk faced generally in that country, but linked to a particular characteristic or status.
- Evidence: `governing_rule` cue `under` at chunk `5049174` offsets `236-241`; context: [57] In this regard, the Immigration and Refugee Board’s legal services produced a document entitled Consolidated Grounds in the Immigration and Refugee Protection Act dated May 15, 2002, which describes the conditions that must be met under paragraph 97(1)(b) of the Act (as of the date of this judgement, this document is on the Board’s website).
- Evidence: `reasoning_application` cue `Therefore` at chunk `5049174` offsets `2271-2280`; context: Therefore, individuals who face a serious and credible risk may not be able to benefit from protection under s.
- Evidence: `counterargument_limitation` cue `However` at chunk `5049174` offsets `1117-1124`; context: However, claims based on personal threats, vendettas, etc.

#### 22347:4:subtheme:12 · paragraphs 76-79

- Raw key terms: `risk, analysis, canada, case, citizenship, establish, immigration, particularized`
- Display key terms: `risk, analysis, case, establish, particularized`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: risk, analysis, case, establish, particularized Operative outcome context: Their applications were properly dismissed since a personalized risk must target an individual in a particularized way. Evidence spans paragraphs 76-79. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5049175` offsets `71-78`; context: [58] The decisions of this Court on paragraph 97(1)(b) are grounded on whether or not there is a personalized risk in each case, which is established on the basis of a factual analysis appropriate to the circumstances in each case.
- Evidence: `disposition` cue `dismissed` at chunk `5049176` offsets `458-467`; context: Their applications were properly dismissed since a personalized risk must target an individual in a particularized way.

#### 22347:4:subtheme:13 · paragraphs 80-81

- Raw key terms: `appeal, court, federal, justice, lamer, madam, proph, question`
- Display key terms: `federal, justice, lamer, madam, proph, question`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: federal, justice, lamer, madam, proph, question Application context: [62] Madam Justice Tremblay‑Lamer invited the Federal Court of Appeal to rule on the issue raised here by counsel for the applicant by certifying the following question in the Prophète case, above: Where the population o | Nonetheless, the Court noted that there was evidence before Madam Justice Tremblay‑Lamer allowing her to conclude as she did: Evidence spans paragraphs 80-81. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5049179` offsets `85-90`; context: [62] Madam Justice Tremblay‑Lamer invited the Federal Court of Appeal to rule on the issue raised here by counsel for the applicant by certifying the following question in the Prophète case, above:
Where the population of a country faces a generalized risk of crime, does the limitation of section 97(1)(b)(ii) of the IRPA apply to a subgroup of individuals who face a significantly heightened risk of such crime?
- Evidence: `reasoning_application` cue `apply` at chunk `5049179` offsets `323-328`; context: [62] Madam Justice Tremblay‑Lamer invited the Federal Court of Appeal to rule on the issue raised here by counsel for the applicant by certifying the following question in the Prophète case, above:
Where the population of a country faces a generalized risk of crime, does the limitation of section 97(1)(b)(ii) of the IRPA apply to a subgroup of individuals who face a significantly heightened risk of such crime?
- Evidence: `issue` cue `question` at chunk `5049180` offsets `208-216`; context: Canada (Citizenship and Immigration), 2009 FCA 31, the Federal Court of Appeal declined to deal with this subject, noting that the certified question was too broad.
- Evidence: `evidence_fact` cue `evidence` at chunk `5049180` offsets `276-284`; context: Nonetheless, the Court noted that there was evidence before Madam Justice Tremblay‑Lamer allowing her to conclude as she did:
- Evidence: `reasoning_application` cue `conclude` at chunk `5049180` offsets `337-345`; context: Nonetheless, the Court noted that there was evidence before Madam Justice Tremblay‑Lamer allowing her to conclude as she did:

#### 22347:4:subtheme:14 · paragraphs 82-83

- Raw key terms: `certified, question, adduced, answering, basis, broad, broader, canada`
- Display key terms: `certified, question, adduced, answering, basis, broad, broader`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: certified, question, adduced, answering, basis, broad, broader Rule/authority context: [7] The examination of a claim under subsection 97(1) of the Act necessitates an individualized inquiry, which is to be conducted on the basis of the evidence adduced by a claimant “in the context of a present or prospec Evidence spans paragraphs 82-83. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049181` offsets `384-392`; context: As drafted, the certified question is too broad.
- Evidence: `evidence_fact` cue `evidence` at chunk `5049181` offsets `150-158`; context: [7] The examination of a claim under subsection 97(1) of the Act necessitates an individualized inquiry, which is to be conducted on the basis of the evidence adduced by a claimant “in the context of a present or prospective risk” for him (Sanchez v.
- Evidence: `governing_rule` cue `under` at chunk `5049181` offsets `31-36`; context: [7] The examination of a claim under subsection 97(1) of the Act necessitates an individualized inquiry, which is to be conducted on the basis of the evidence adduced by a claimant “in the context of a present or prospective risk” for him (Sanchez v.
- Evidence: `issue` cue `question` at chunk `5049182` offsets `112-120`; context: [8] Taking into consideration the broader federal scheme of which section 97 is a part, answering the certified question in a factual vacuum would, depending on the circumstances of each case, result in unduly narrowing or widening the scope of subparagraph 97(1)(b)(ii) of the Act.

#### 22347:4:subtheme:15 · paragraphs 84-86

- Raw key terms: `allowing, answer, applicant, applications, because, becoming, canada, case`
- Display key terms: `allowing, answer, applications, because, becoming, case`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: allowing, answer, applications, because, becoming, case Application context: Canada (Citizenship and Immigration), 2008 FC 331), there was evidence on record allowing the Applications Judge to conclude: | While a specific number of individuals may be targeted more frequently because of their wealth, all Haitians are at risk of becoming the victims of violence. Evidence spans paragraphs 84-86. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049183` offsets `58-66`; context: [9] For these reasons, we decline to answer the certified question.
- Evidence: `evidence_fact` cue `evidence` at chunk `5049184` offsets `99-107`; context: Canada (Citizenship and Immigration), 2008 FC 331), there was evidence on record allowing the Applications Judge to conclude:
- Evidence: `reasoning_application` cue `conclude` at chunk `5049184` offsets `153-161`; context: Canada (Citizenship and Immigration), 2008 FC 331), there was evidence on record allowing the Applications Judge to conclude:
- Evidence: `reasoning_application` cue `because` at chunk `5049185` offsets `276-283`; context: While a specific number of individuals may be targeted more frequently because of their wealth, all Haitians are at risk of becoming the victims of violence.

#### 22347:4:subtheme:16 · paragraphs 87-90

- Raw key terms: `case, applicant, argument, counsel, crime, perceived, reasons, risk`
- Display key terms: `case, argument, crime, perceived, risk`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: case, argument, crime, perceived, risk Rule/authority context: [67] A person victimized by crime is not, based on that fact alone, a person in need of protection under section 97 of the Act. Application context: [65] The primary argument of counsel for the applicant that she is more at risk of the generalized crime prevalent in Haiti than the rest of the population because she is perceived to be a member of a group that is more  Evidence spans paragraphs 87-90. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049186` offsets `65-73`; context: [64] Although the Federal Court of Appeal declined to answer the question, its reasons on this point are consistent with the section 97 analysis that is being carried out here.
- Evidence: `reasoning_application` cue `because` at chunk `5049187` offsets `156-163`; context: [65] The primary argument of counsel for the applicant that she is more at risk of the generalized crime prevalent in Haiti than the rest of the population because she is perceived to be a member of a group that is more affluent, cannot therefore succeed, and this argument fails for the reasons set out at length below.
- Evidence: `governing_rule` cue `under` at chunk `5049189` offsets `99-104`; context: [67] A person victimized by crime is not, based on that fact alone, a person in need of protection under section 97 of the Act.

#### 22347:4:subtheme:17 · paragraphs 91-92

- Raw key terms: `court, decision, acceptable, according, added, adduced, administrative, affecting`
- Display key terms: `acceptable, according, added, adduced, administrative, affecting`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: acceptable, according, added, adduced, administrative, affecting Evidence spans paragraphs 91-92. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049190` offsets `239-247`; context: In the circumstances of this case, it is unlikely that the applicant will be subject to a personalized risk by the same band of thugs almost 4 years after the incidents in question.
- Evidence: `evidence_fact` cue `found that` at chunk `5049190` offsets `352-362`; context: The panel found that “according to the evidence adduced before it, the risk to which the claimant could be subjected is a generalized risk affecting the entire population of the country and not a personalized risk .
- Evidence: `counterargument_limitation` cue `However` at chunk `5049190` offsets `249-256`; context: However, it is not the Court’s task to carry out this prospective analysis, but the panel’s.
- Evidence: `issue` cue `whether` at chunk `5049191` offsets `921-928`; context: But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.
- Evidence: `counterargument_limitation` cue `But` at chunk `5049191` offsets `891-894`; context: But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.

#### 22347:4:subtheme:18 · paragraphs 93-94

- Raw key terms: `question, applicant, application, apply, certification, certified, claimant, counsel`
- Display key terms: `question, apply, certification, certified`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: question, apply, certification, certified Application context: [71] Counsel for the applicant has proposed that the following question be certified for purposes of paragraph 74(d) of the Act: “Does the exclusionary provision found in subparagraph 97(1)(b)(ii) of the Act apply when t Operative outcome context: [70] For these reasons, the application for judicial review is dismissed. Evidence spans paragraphs 93-94. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049192` offsets `91-99`; context: Certification of question
- Evidence: `disposition` cue `dismissed` at chunk `5049192` offsets `63-72`; context: [70] For these reasons, the application for judicial review is dismissed.
- Evidence: `issue` cue `question` at chunk `5049193` offsets `63-71`; context: [71] Counsel for the applicant has proposed that the following question be certified for purposes of paragraph 74(d) of the Act: “Does the exclusionary provision found in subparagraph 97(1)(b)(ii) of the Act apply when the subgroup of which the claimant is a member faces the risk in question or only when the entire population faces the same risk?
- Evidence: `reasoning_application` cue `apply` at chunk `5049193` offsets `208-213`; context: [71] Counsel for the applicant has proposed that the following question be certified for purposes of paragraph 74(d) of the Act: “Does the exclusionary provision found in subparagraph 97(1)(b)(ii) of the Act apply when the subgroup of which the claimant is a member faces the risk in question or only when the entire population faces the same risk?

#### 22347:4:subtheme:19 · paragraphs 95-96

- Raw key terms: `question, above, affluent, answer, appeal, because, broad, canada`
- Display key terms: `question, above, affluent, answer, because, broad`
- Argument roles: `counterargument_limitation, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, reasoning_application Display terms: question, above, affluent, answer, because, broad Application context: [72] Counsel for the Minister is opposed to the question and notes, first, that subparagraph 97(1)(b)(ii) does not contain a restriction but an implementation measure and second, that the question is too broad because it Evidence spans paragraphs 95-96. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049194` offsets `48-56`; context: [72] Counsel for the Minister is opposed to the question and notes, first, that subparagraph 97(1)(b)(ii) does not contain a restriction but an implementation measure and second, that the question is too broad because it deals with all subgroups, not just the subgroup of individuals who are affluent or are perceived as such.
- Evidence: `reasoning_application` cue `because` at chunk `5049194` offsets `210-217`; context: [72] Counsel for the Minister is opposed to the question and notes, first, that subparagraph 97(1)(b)(ii) does not contain a restriction but an implementation measure and second, that the question is too broad because it deals with all subgroups, not just the subgroup of individuals who are affluent or are perceived as such.
- Evidence: `issue` cue `question` at chunk `5049195` offsets `21-29`; context: [73] In my view, the question is improperly framed.
- Evidence: `counterargument_limitation` cue `However` at chunk `5049195` offsets `52-59`; context: However, I will not reframe the question since I am also of the view that the very subject of this question is identical to the subject of the question framed by Madam Justice Tremblay‑Lamer in Prophète, above, the wording of which is reproduced above and which the Federal Court of Appeal declined to answer in Prophète v.

#### 22347:4:subtheme:20 · paragraphs 97-97

- Raw key terms: `answer, appeal, certified, clearly, court, federal, framing, indicated`
- Display key terms: `answer, certified, clearly, federal, framing, indicated`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: answer, certified, clearly, federal, framing, indicated Application context: Therefore, no question will be certified for purposes of paragraph 74(d) of the Act. Evidence spans paragraphs 97-97. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5049196` offsets `33-41`; context: [74] I see no point in framing a question that the Federal Court of Appeal has clearly indicated it will not answer.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5049196` offsets `117-126`; context: Therefore, no question will be certified for purposes of paragraph 74(d) of the Act.

#### Section text

[25] In the view of counsel for the applicant, Justice Dawson clearly explained the approach of this second school of jurisprudence in obiter dictum in Surajnarain, above:

[16] Of relevance was the requirement that a claimant must establish that his removal would subject him to “an objectively identifiable risk, which risk would apply in every part of that country and would not be faced generally by other individuals in or from that country.”

[17] The Department of Citizenship and Immigration published guidelines [in 1994] to assist officers in the interpretation of the various elements contained in the definition of the PDRCC class. With respect to the requirement that the risk “would not be faced generally by other individuals” the guidelines instructed officers that:
The threat is not restricted to a risk personalized to an individual; it includes risks faced by individuals that may be shared by others who are similarly situated. Neither are risks restricted by ethnic, political, religious or social factors as the concept of persecution is in the Convention refugee definition. Whether or not the risk is associated with a “Convention” ground, a person may fall within the scope of this definition. Notwithstanding this, the limitation imposed by the PDRCC definition in the phrase “which risk . . .would not be faced generally by other individuals in or from that country” applies. Any risk that would apply to all residents or citizens of the country of origin cannot result in a positive decision under this Regulation. [Not underlined in original.]

[18] Justice McGillis had the occasion to consider the guidelines in Sinnappu, referred to above. At paragraph 37, Justice McGillis wrote:
In particular, the PDRCC class guidelines emphasize that the criteria in subsection 2(1) of the Regulations are not only restricted to “a risk personalized to an individual”, but also include a risk faced by others similarly situated. Furthermore, the guidelines interpret the exclusionary phrase in the Regulations that the risk must not be “faced generally by other individuals”, as meaning a risk faced by all residents or citizens of that country. Indeed, during his cross‑examination, Gilbert Troutet, a specialist in PDRCC class applications, stated that the exclusion would apply only “in extreme situations such as a generalized disaster of some sort that would involve all of the inhabitants of a given country. And if such a situation does occur, the [respondent] has specific programs to cover such situations.” [Not underlined in original and footnote omitted.]

[19] Thus, the Board should consider whether application of the principles set out in Salibian and Sinnappu lead to the conclusion that a claimant may only be denied protection under subparagraph 97(1)(b)(ii) of the Act if the risk is faced generally by all of the other persons in the country.

[26] Counsel for the applicant notes that the Federal Court of Appeal declined to rule on the interpretation of subparagraph 97(1)(b)(ii) of the Act in Prophète v. Canada (Citizenship and Immigration), 2009 FCA 31. Based on that, he concludes that the state of the law on this point is far from satisfactory.

[27] Counsel for the applicant adds as an alternative argument that, even if the Court agrees with the first school of jurisprudence in its interpretation of subparagraph 97(1)(b)(ii) of the Act, the panel’s decision should nonetheless be set aside because the application of that subparagraph, as interpreted in this way, to the facts in question is not reasonable.

[28] In fact, we are not dealing solely with the case of a person who fears violence by reason of his or her membership in a particular group and who is therefore more at risk than the entire population. In that case, Ms. Prophète was personally targeted by a gang of thugs who attacked her on a number of occasions. The case at bar is analogous to the one examined by Mr. Justice de Montigny in Martinez Pineda v. Canada (Citizenship and Immigration), 2007 FC 365 where he allowed an application for judicial review of a decision refusing person in need of protection status under subsection 97(1)(b) of the Act to a Salvadorean citizen.

[29] In that case, Mr. Pineda had been threatened a number of times by members of a street gang after he refused to become a member. Evidence was adduced that street gangs recruited across the country; Mr. Pineda’s application was therefore denied by the panel on the ground that the risk faced by the applicant was no different from that faced by the Salvadorean population in general. On this point, Mr. Justice de Montigny noted the following:

[17] . . . The applicant was not claiming to be subject to a risk to his life or his safety based only on the fact that he was a student, young or from a wealthy family. If such were the case, the application would have to be dismissed for the same reasons that led the Court to confirm the RPD decisions in the two matters mentioned above [Jeudy and Osorio, above]. But this is not the case. The applicant alleged that he had been personally targeted on more than one occasion, and over quite a long period of time. Unless we question the truthfulness of his story, which the RPD did not do, we have no doubt that he will be personally in danger if he were to return to El Salvador. In the particular circumstances of this matter, to find the opposite amounts to a patently unreasonable error.
Minister’s position

[30] Counsel for the Minister maintains that the panel’s decision does not deal with the interpretation of subsection 97(1)(b)(ii) of the Act but is limited to the application of the provision to the facts of the case in light of the clear majority of the Court’s jurisprudence concerning the scope of the provision.

[31] In this regard, he notes that even where a person is a direct victim of violence resulting from generalized crime, this does not mean that the risk faced by that person is different from the risk faced by the general population. Each case turns on its own facts, and it is incumbent on the panel to determine the facts in light of the evidence adduced before it. Unless the panel’s decision contravenes the deferential standard of reasonableness, the Court should not intervene.

[32] He adds that the Court’s recent jurisprudence is clear on the principles to be applied in such cases. Consequently, the decision of Justice Tremblay‑Lamer in Prophète, above, is determinative, especially because the Federal Court of Appeal upheld the judge’s findings in this matter. The Prophète decision has largely been followed subsequently, in particular, in Lebrun Charles v. Canada (Citizenship and Immigration), 2009 FC 233 (Mr. Justice Martineau), Octave v. Canada (Citizenship and Immigration), 2009 FC 403 (Mr. Justice Harrington) and Ventura de Parada, above (Mr. Justice Zinn).

[33] Counsel for the Minister acknowledges the recent discordant decision by Justice Dawson in Surajnarain, above, but notes that her comment was obiter dictum, which does not bind the Court and which is essentially based on the Sinnappu decision, above, which dates from 1997 and was made in a different statutory and regulatory context from that of today.
Analysis
Appropriate standard

[34] In light of the Supreme Court of Canada decisions in Dunsmuir v. New Brunswick, [2008] 1 S.C.R. 190, and Canada (Citizenship and Immigration) v. Khosa, 2009 SCC 12, the two standards of judicial review are correctness and reasonableness. To establish the appropriate standard in each case, “[a]n exhaustive review is not required in every case to determine the proper standard of review. Here again, existing jurisprudence may be helpful in identifying some of the questions that generally fall to be determined according to the correctness standard (Cartaway Resources Corp. (Re), [2004] 1 S.C.R. 672, 2004 SCC 26). This simply means that the analysis required is already deemed to have been performed and need not be repeated.” (Dunsmuir, above, at para. 57).

[35] Errors of law are generally reviewable on a correctness standard: Khosa, above, at paragraph 44. Although a certain deference may be appropriate where a specialized administrative tribunal is interpreting its own statute or statutes closely connected to its function (Dunsmuir, above, at para. 54), the relevant jurisprudence generally indicates that questions of law relating to refugee status (and, by implication, person in need of protection status) under the Immigration and Refugee Protection Act are reviewable on a standard of correctness: Pushpanathan v. Canada (Minister of Citizenship and Immigration), [1998] 1 S.C.R. 982, at paragraphs 42 to 50, Mugesera v. Canada (Minister of Citizenship and Immigration), [2005] 2 S.C.R. 100, at paragraph 37.

[36] The recent judgements in Acosta v. Canada (Citizenship and Immigration), above, and Michaud v. Canada (Citizenship and Immigration), 2009 FC 886, maintain that the application of subparagraph 97(1)(b)(ii) of the Act is a question of fact reviewable on a standard of reasonableness. As I explain below, I agree that this standard applies to judicial review of decisions about the application of this subparagraph. Nonetheless, to arrive at this conclusion, it is necessary in this case to interpret the scope of section 97 of the Act, and this interpretation involves a question of law, which is subject to the correctness standard.

[37] Accordingly, I will apply the correctness standard to the section 97 interpretation and the reasonableness standard to the panel’s findings of fact.
Summary

[38] The Court is of the view that consideration of an application for protected person status under subsection 97(1)(b)(ii) of the Act requires an individualized assessment in the context of existing and prospective risks faced by the applicant. This assessment is based on the particular facts of each case.

[39] The requisite analysis includes not only an analysis of the personalized risk faced by the person in question, but also a separate analysis of the risk faced by other individuals from the country in question. The objective of these analyses is to determine, in each particular case, based on the evidence available, whether the personalized risk faced by the applicant exists “in every part of that country and is not faced generally by other individuals in or from that country”.

[40] The Court is also of the view that a textual analysis of subparagraph 97(1)(b)(ii) and a pragmatic and functional approach to applying this subparagraph shows that the analysis of the risk faced by other individuals from the country in question is not necessarily limited to an analysis of the risk faced by the entire population but may also include an analysis of the risk faced by only one segment of the population, to the extent that the particular circumstances of each case justify this approach in light of the objectives of the Act and its section 97.

[41] These various analyses are essentially factual and must be carried out on a case-by-case basis. To the extent that these analyses and the conclusions based thereon are reasonable, the Court will not intervene on judicial review of such a decision by the Refugee Protection Division of the Immigration and Refugee Board. In this regard, see Acosta v. Canada (Citizenship and Immigration), above, and Michaud v. Canada (Citizenship and Immigration), above.

[42] For the Court, the analysis required under subsection 97(1)(b)(ii) of the Act primarily entails a case-by-case determination of a real and particularized threat directed at an individual. This approach is consistent with the very objectives of the Act, in particular, paragraph 3(2)(a), reproduced above, which recognizes that the refugee program is, in the first instance, about saving lives and offering protection to the displaced and persecuted, and paragraph 3(3)(d), also reproduced above, which provides that the Act is to be construed and applied in a manner that ensures that decisions taken under the Act are consistent with the Canadian Charter of Rights and Freedoms.

[43] These findings are based on the following analyses.
Textual analysis

[44] The Supreme Court of Canada recently reiterated the modern principles of statutory interpretation in Canada Trustco Mortgage Co. v. Canada, [2005] 2 S.C.R. 601, 2005 SCC 54, at paragraph 10:
It has been long established as a matter of statutory interpretation that “the words of an Act are to be read in their entire context and in their grammatical and ordinary sense harmoniously with the scheme of the Act, the object of the Act, and the intention of Parliament”: see 65302 British Columbia Ltd. v. Canada, [1999] 3 S.C.R. 804, at para. 50. The interpretation of a statutory provision must be made according to a textual, contextual and purposive analysis to find a meaning that is harmonious with the Act as a whole. When the words of a provision are precise and unequivocal, the ordinary meaning of the words play a dominant role in the interpretive process. On the other hand, where the words can support more than one reasonable meaning, the ordinary meaning of the words plays a lesser role. The relative effects of ordinary meaning, context and purpose on the interpretive process may vary, but in all cases the court must seek to read the provisions of an Act as a harmonious whole.

[45] A textual analysis of subparagraph 97(1)(b)(ii) demonstrates that the provision does not require that the risk be faced by all other individuals from the country in question.

[46] In fact, the subparagraph requires that the person concerned face the risk “in every part of the country” (in French, “en tout lieu de ce pays”), thus giving first priority to an internal flight alternative.

[47] Furthermore, the legislation provides that the risk faced by the applicant must not be a risk faced by other individuals from that country (“is not faced generally by other individuals in or from that country”; in French “que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas”).

[48] The provision in question does not require that “all other individuals from that country” face the risk, but that the risk is not faced generally “by other individuals in or from that country”. The use of the indefinite article in this context makes the wording clear. In fact, as Grevisse notes, [translation] “[the] indefinite article indicates that the person or the object designated by the noun is presented as a certain person or a certain object separate from other persons or objects particular to the type, but whose individualization remains undetermined” (Le Bon Usage, 11th edition, pages 347 and 348). A grammatical analysis of the English wording of the provision leads to the same result.

[49] Thus, in cases such as this one, where the general population faces a risk of criminality, the fact that certain individuals are more likely to face this risk, either because they live in more dangerous areas, or because they are perceived as being more affluent, does not necessarily make those individuals eligible for protected person status under subparagraph 97(1)(b)(ii). In the first case, the availability of an internal flight alternative would exclude this status and in the other case, the generalized risk would have the same effect.
Legislative history

[50] This textual analysis is also supported by the provision’s legislative history. A similar provision appeared for the first time in the Regulations in 1993 in order to add a prior review process with respect to individuals to whom the definition of Convention refugee did not apply but who should nonetheless not be returned, since they were at serious risk of harm. The post‑determination refugee claimants in Canada class (the PDRCC class) was formally established under the Immigration Regulations, 1978 — Amendment SOR/93‑44, which provided that the following definition should be inserted into subsection 2(1) of the Regulations:
“member of the post‑determination refugee claimants in Canada class” means an immigrant in Canada
(a) who the Refugee Division has determined on or after February 1, 1993 is not a Convention refugee . . .
(c) who if removed to a country to which the immigrant could be removed would be subjected to an objectively identifiable risk, which risk would apply in every part of that country and would not be faced generally by other individuals in or from that country,
(i) to the immigrant’s life, other than a risk to the immigrant’s life that is caused by the inability of that country to provide adequate health or medical care,
(ii) of extreme sanctions against the immigrant, or
(iii) of inhumane treatment of the immigrant;
« demandeur non reconnu du statut de réfugié au Canada »
Immigrant au Canada :
a) à l’égard duquel la section du statut a décidé, le 1er février 1993 ou après cette date, de ne pas reconnaître le statut de réfugié au sens de la Convention, ...
c) dont le renvoi vers un pays dans lequel il peut être renvoyé l’expose personnellement, en tout lieu de ce pays, à l’un des risques suivants, objectivement identifiable, auquel ne sont pas généralement exposés d’autres individus provenant de ce pays ou s’y trouvant :
(i) sa vie est menacée pour des raisons autres que l’incapacité de ce pays de fournir des soins médicaux ou de santé adéquats,
(ii) des sanctions excessives peuvent être exercées contre lui,
(iii) un traitement inhumain peut lui être infligé.

[51] In this regard, the Regulatory Impact Statement accompanying these Regulations (but not a part of them) explicitly states that the risk faced by the applicant must be personalized: “The claimant must be subject to an identifiable risk if forced to leave Canada. The risk must be compelling, consisting of a threat to life, excessive sanctions or inhumane treatment. It must be personal, that is, directed at the individual rather than being based on generalized situations of risk faced by other individuals in the country of return . . . The criteria are intended to be narrowly drawn [in French, “circonscrits”] to avoid creating an admissions system on top of the refugee determination system.” (Canada Gazette, Part II, Vol. 127, No. 3, page 655; emphasis added.)

[52] However, in 1994, a review of the PDRCC class procedures was initiated. Madam Justice McGillis explained the result of this review in her judgement in Sinnappu v. Canada, above, at paragraph 36 as follows:
. . . Following the review, a recommendation was made to broaden the definition in subsection 2(1) of the Regulations by including factors of generalized risk facing the person upon removal to the country in question. Although that recommendation was not accepted, a decision was made to develop guidelines in order to assist officers in interpreting the regulatory criteria. In July 1994, the Department of Citizenship and Immigration (Department) issued guidelines entitled What is the PDRCC? (PDRCC class guidelines) to assist officers reviewing applications for landing under the PDRCC class in interpreting the criteria in the Regulations. For the purposes of the present case, the following are the relevant portions of the PDRCC class guidelines:
. . .
· “. . .would not be faced generally by other individuals . . .” The threat is not restricted to a risk personalized to an individual; it includes risks faced by individuals that may be shared by others who are similarly situated. Neither are risks restricted by ethnic, political, religious or social factors as the concept of persecution is in the Convention refugee definition. Whether or not the risk is associated with a “Convention” ground, a person may fall within the scope of this definition. Notwithstanding this, the limitation imposed by the PDRCC definition in the phrase “which risk. . . would not be faced generally by other individuals in or from that country” applies. Any risk that would apply to all residents or citizens of the countr

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 22347:5 · paragraphs 98-99

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e17a9df4b36d3bc61c4145a3bd38c743768daaf354dd380e29a7e93823e98f0b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22347:5:subtheme:1 · paragraphs 98-99

- Raw key terms: `mainville, adjudges, alexandre, appearances, applicant, application, attorney, barrister`
- Display key terms: `mainville, adjudges, alexandre, barrister`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: mainville, adjudges, alexandre, barrister No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 98-99. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THE COURT ORDERS AND ADJUDGES that the application for judicial review is dismissed.
“Robert M. Mainville”
Judge
Certified true translation
Mary Jo Egan, LLB
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM‑541‑09
STYLE OF CAUSE: PHILOMENA INNOCENT v.
MINISTER OF CITIZENSHIP
AND IMMIGRATION
PLACE OF HEARING: Montréal, Quebec
DATE OF HEARING: September 15, 2009
REASONS FOR JUDGEMENT
AND JUDGEMENT BY: Mr. Justice Mainville
DATED: October 8, 2009
APPEARANCES:
Jared Will
FOR THE APPLICANT
Alexandre Tavadian
FOR THE RESPONDENT
SOLICITORS OF RECORD:
JARED WILL
Barrister and Solicitor
Montréal, Quebec
FOR THE APPLICANT
JOHN H. SIMS, Q.C.
Deputy Attorney General of Canada
FOR THE RESPONDENT
