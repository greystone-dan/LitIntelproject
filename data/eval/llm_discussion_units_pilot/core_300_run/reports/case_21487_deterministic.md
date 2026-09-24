# Discussion Units: case 21487

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **33**
- Continuity pairs: **32**
- Discussion Units: **4**
- Paragraph source hashes: **33**
- Sub-themes: **9**

## 21487:1 · paragraphs 0-10

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `364f40e06366dad1812a25ae9e61d8554e2be6229fca3072c067e2ea71cb4e49`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21487:1:subtheme:1 · paragraphs 0-10

- Raw key terms: `applicant, board, immigration, indicated, protection, alleged, asylum, cited`
- Display key terms: `indicated, protection, alleged, asylum, cited`
- Argument roles: `evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position, reasoning_application Display terms: indicated, protection, alleged, asylum, cited Position/evidence statements: [2] The applicant, a 32 year-old citizen of Haiti, claims to have been the target of gang violence on multiple occasions between September 2000 and June 2004, the date on which he left the country for the United States i | [4] The applicant asserts that he was targeted because he was a known businessman, operating the company “Indice Communications” and as such he was perceived to be wealthy. Rule/authority context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S. Application context: [4] The applicant asserts that he was targeted because he was a known businessman, operating the company “Indice Communications” and as such he was perceived to be wealthy. | [10] Finally, the Board cited a document submitted by the applicant, which indicated that the national police in Haiti were “making progress”, in order to conclude that state protection exists. Evidence spans paragraphs 0-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `5009219` offsets `314-329`; context: 27 (the “Act” or “IRPA”), for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the “IRB” or the "Board") dated July 5, 2006, wherein the Board determined that the applicant was not a Convention refugee according to Section 96 of the Act, nor a "person in need of protection" according to Section 97 of the Act.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5009219` offsets `27-38`; context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `party_position` cue `claims` at chunk `5009220` offsets `51-57`; context: [2] The applicant, a 32 year-old citizen of Haiti, claims to have been the target of gang violence on multiple occasions between September 2000 and June 2004, the date on which he left the country for the United States in possession of an American visa.
- Evidence: `party_position` cue `asserts` at chunk `5009222` offsets `18-25`; context: [4] The applicant asserts that he was targeted because he was a known businessman, operating the company “Indice Communications” and as such he was perceived to be wealthy.
- Evidence: `reasoning_application` cue `because` at chunk `5009222` offsets `47-54`; context: [4] The applicant asserts that he was targeted because he was a known businessman, operating the company “Indice Communications” and as such he was perceived to be wealthy.
- Evidence: `evidence_fact` cue `determined that` at chunk `5009225` offsets `21-36`; context: [7] First, the Board determined that the applicant’s fear of persecution had no nexus with any of the five grounds contained in the definition of Convention refugee.
- Evidence: `reasoning_application` cue `conclude` at chunk `5009228` offsets `155-163`; context: [10] Finally, the Board cited a document submitted by the applicant, which indicated that the national police in Haiti were “making progress”, in order to conclude that state protection exists.

#### Section text

Prophète v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2008-03-12
Neutral citation
2008 FC 331
File numbers
IMM-3077-07
Decision Content
Date: 20080312
Docket: IMM-3077-07
Citation: 2008 FC 331
Ottawa, Ontario, March 12, 2008
PRESENT: The Honourable Madam Justice Tremblay-Lamer
BETWEEN:
RALPH PROPHÈTE
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (the “Act” or “IRPA”), for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the “IRB” or the "Board") dated July 5, 2006, wherein the Board determined that the applicant was not a Convention refugee according to Section 96 of the Act, nor a "person in need of protection" according to Section 97 of the Act.
I . Background

[2] The applicant, a 32 year-old citizen of Haiti, claims to have been the target of gang violence on multiple occasions between September 2000 and June 2004, the date on which he left the country for the United States in possession of an American visa.

[3] During this time, the acts of alleged persecution were in the form of vandalism, extortion, and threats of kidnapping.

[4] The applicant asserts that he was targeted because he was a known businessman, operating the company “Indice Communications” and as such he was perceived to be wealthy.

[5] The applicant remained in the United States from 20 February 2004 until the 19 October 2005. He subsequently arrived in New Brunswick with a valid six-month Canadian visitor’s visa before finally claiming asylum in Montreal on 22 April 2006.

[6] The IRB found the applicant to be credible and generally accepted the facts as alleged.

[7] First, the Board determined that the applicant’s fear of persecution had no nexus with any of the five grounds contained in the definition of Convention refugee.

[8] Second, the Board indicated that to fall within the category of “person in need of protection” as contemplated by s. 97(1)(b), the applicant must demonstrate that he would be subject to danger or to a risk to his life or cruel or unusual treatment owing to his personal circumstances or those of similarly situated individuals.

[9] The Board indicated that the risk feared by the applicant is a generalized risk. In support of this contention the Board cited information given by the applicant to an immigration officer during his asylum claim of 16 May 2006:
Ceux qui avaient des entreprises étaient des cibles et j’étais une cible, étant considéré comme riche car j’avais du succès” […] Les gens d’affaires font leurs déplacements en secret car il est dit que si tu te déplaces, tu as de l’argent, et si tu as de l’argent, tu te fais voler et kidnapper.”
The Board concluded that the applicant was not more at risk than any other Haitian.

[10] Finally, the Board cited a document submitted by the applicant, which indicated that the national police in Haiti were “making progress”, in order to conclude that state protection exists.


## 21487:2 · paragraphs 11-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9c004adbe17334b83e732b48b5d36b84ca06e142ff9d794d2b0a382a5e9e28b0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21487:2:subtheme:1 · paragraphs 11-15

- Raw key terms: `risk, applicant, general, canada, citizenship, decision, faced, fact`
- Display key terms: `risk, faced, fact`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: risk, faced, fact Position/evidence statements: [12] The applicant submits that kidnapping is rampant in Haiti, but businessmen are especially at risk because the goal of kidnapping for ransom is to obtain money. Rule/authority context: concluded that, the standard of correctness was applicable when reviewing a decision regarding whether or not the perception of wealth constitutes a particularized risk under section 97. Application context: [12] The applicant submits that kidnapping is rampant in Haiti, but businessmen are especially at risk because the goal of kidnapping for ransom is to obtain money. | For the Board, the weakness in the applicant’s claim stemmed from the fact that the risk he faced was also faced by the general Haitian population and therefore was not personalized. Evidence spans paragraphs 11-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5009229` offsets `196-203`; context: concluded that, the standard of correctness was applicable when reviewing a decision regarding whether or not the perception of wealth constitutes a particularized risk under section 97.
- Evidence: `governing_rule` cue `under` at chunk `5009229` offsets `270-275`; context: concluded that, the standard of correctness was applicable when reviewing a decision regarding whether or not the perception of wealth constitutes a particularized risk under section 97.
- Evidence: `party_position` cue `submits` at chunk `5009230` offsets `19-26`; context: [12] The applicant submits that kidnapping is rampant in Haiti, but businessmen are especially at risk because the goal of kidnapping for ransom is to obtain money.
- Evidence: `reasoning_application` cue `because` at chunk `5009230` offsets `103-110`; context: [12] The applicant submits that kidnapping is rampant in Haiti, but businessmen are especially at risk because the goal of kidnapping for ransom is to obtain money.
- Evidence: `counterargument_limitation` cue `but` at chunk `5009230` offsets `64-67`; context: [12] The applicant submits that kidnapping is rampant in Haiti, but businessmen are especially at risk because the goal of kidnapping for ransom is to obtain money.
- Evidence: `evidence_fact` cue `evidence` at chunk `5009232` offsets `106-114`; context: 97 claim, a claimant must provide “persuasive evidence (i.
- Evidence: `reasoning_application` cue `therefore` at chunk `5009232` offsets `763-772`; context: For the Board, the weakness in the applicant’s claim stemmed from the fact that the risk he faced was also faced by the general Haitian population and therefore was not personalized.

#### 21487:2:subtheme:2 · paragraphs 16-18

- Raw key terms: `canada, ahmad, applicant, citizenship, country, general, immigration, issue`
- Display key terms: `ahmad, country`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: ahmad, country Rule/authority context: [16] The test under s. Application context: 97 “requires the Board to apply a different criterion pertaining to the issue of whether the applicant’s removal may or may not expose him personally to the risks and dangers referred to in paragraphs 97(1)(a) and (b) of | [17] Accordingly, documentary evidence which illustrates the systematic and generalized violation of human rights in a given country will not be sufficient to ground a section 97 claim absent proof that might link this g Evidence spans paragraphs 16-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5009233` offsets `39-44`; context: [15] Thus, the present case raises the issue of the interpretation of the meaning of the terms “personally” and “generally” as contained in s.
- Evidence: `issue` cue `issue` at chunk `5009234` offsets `292-297`; context: 97 “requires the Board to apply a different criterion pertaining to the issue of whether the applicant’s removal may or may not expose him personally to the risks and dangers referred to in paragraphs 97(1)(a) and (b) of the Act” and must be assessed with reference to the personal situation of the applicant.
- Evidence: `governing_rule` cue `under` at chunk `5009234` offsets `14-19`; context: [16] The test under s.
- Evidence: `reasoning_application` cue `apply` at chunk `5009234` offsets `246-251`; context: 97 “requires the Board to apply a different criterion pertaining to the issue of whether the applicant’s removal may or may not expose him personally to the risks and dangers referred to in paragraphs 97(1)(a) and (b) of the Act” and must be assessed with reference to the personal situation of the applicant.
- Evidence: `evidence_fact` cue `evidence` at chunk `5009235` offsets `30-38`; context: [17] Accordingly, documentary evidence which illustrates the systematic and generalized violation of human rights in a given country will not be sufficient to ground a section 97 claim absent proof that might link this general documentary evidence to the applicant’s specific circumstances (Ould v.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5009235` offsets `5-16`; context: [17] Accordingly, documentary evidence which illustrates the systematic and generalized violation of human rights in a given country will not be sufficient to ground a section 97 claim absent proof that might link this general documentary evidence to the applicant’s specific circumstances (Ould v.

#### 21487:2:subtheme:3 · paragraphs 19-21

- Raw key terms: `applicant, larger, population, analyzing, asserted, because, born, canada`
- Display key terms: `larger, population, analyzing, asserted, because, born`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: larger, population, analyzing, asserted, because, born Rule/authority context: Under these circumstances, the Court may be faced with applicant who has been targeted in the past and who may be targeted in the future but whose risk situation is similar to a segment of the larger population. Application context: In that case, the applicant asserted that if he and his young Canadian born son were returned to Colombia it would constitute indirect cruel and unusual treatment/punishment because of the psychological stress that he wo Evidence spans paragraphs 19-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `Under` at chunk `5009236` offsets `237-242`; context: Under these circumstances, the Court may be faced with applicant who has been targeted in the past and who may be targeted in the future but whose risk situation is similar to a segment of the larger population.
- Evidence: `reasoning_application` cue `because` at chunk `5009237` offsets `453-460`; context: In that case, the applicant asserted that if he and his young Canadian born son were returned to Colombia it would constitute indirect cruel and unusual treatment/punishment because of the psychological stress that he would experience as a parent worrying about his child’s welfare in that country.

#### 21487:2:subtheme:4 · paragraphs 22-25

- Raw key terms: `applicant, board, faced, further, group, risk, beaudry, case`
- Display key terms: `faced, further, group, risk, beaudry, case`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue Display terms: faced, further, group, risk, beaudry, case Operative outcome context: dismissed the application indicating, at para. Evidence spans paragraphs 22-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5009239` offsets `320-325`; context: 97(1)(b)(ii), thereby leaving to the Board the issue of deciding whether a particular group meets the definition.
- Evidence: `evidence_fact` cue `evidence` at chunk `5009241` offsets `691-699`; context: The documentary evidence submitted in support of this case indicates that there is a serious risk to the personal safety of all in Haiti.
- Evidence: `counterargument_limitation` cue `However` at chunk `5009241` offsets `535-542`; context: […] However, as discussed above, the risk faced by the applicant is generalized.
- Evidence: `counterargument_limitation` cue `however` at chunk `5009242` offsets `415-422`; context: In that particular case, the Board accepted that the applicants had been the victims of violence, however, O’Keefe J.
- Evidence: `disposition` cue `dismissed` at chunk `5009242` offsets `435-444`; context: dismissed the application indicating, at para.

#### 21487:2:subtheme:5 · paragraphs 26-27

- Raw key terms: `applicant, application, based, because, becoming, board, court, criminality`
- Display key terms: `based, because, becoming, criminality`
- Argument roles: `disposition, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, reasoning_application Display terms: based, because, becoming, criminality Rule/authority context: [23] Based on the recent jurisprudence of this Court, I am of the view that the applicant does not face a personalized risk that is not faced generally by other individuals in or from Haiti. Application context: While a specific number of individuals may be targeted more frequently because of their wealth, all Haitians are at risk of becoming the victims of violence. Operative outcome context: [24] For these reasons, the application for judicial review of the Immigration and Refugee Board decision is dismissed. Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5009243` offsets `25-38`; context: [23] Based on the recent jurisprudence of this Court, I am of the view that the applicant does not face a personalized risk that is not faced generally by other individuals in or from Haiti.
- Evidence: `reasoning_application` cue `because` at chunk `5009243` offsets `336-343`; context: While a specific number of individuals may be targeted more frequently because of their wealth, all Haitians are at risk of becoming the victims of violence.
- Evidence: `disposition` cue `dismissed` at chunk `5009244` offsets `109-118`; context: [24] For these reasons, the application for judicial review of the Immigration and Refugee Board decision is dismissed.

#### Section text

II. Standard of Review

[11] In Cius v. Canada (Minister of Citizenship and Immigration), 2008 FC 1, at para. 22, Beaudry J. concluded that, the standard of correctness was applicable when reviewing a decision regarding whether or not the perception of wealth constitutes a particularized risk under section 97. I agree. The interpretation of this provision is a question of pure law and thus will be afforded no deference.
III. Analysis

[12] The applicant submits that kidnapping is rampant in Haiti, but businessmen are especially at risk because the goal of kidnapping for ransom is to obtain money. Given the fact that in Haiti most of the population is poor, those with money or those perceived to have money are at greater risk than the general population. Section 97 of the Act is to be interpreted as indicating that there can be a sub-group within a generalized group that faces an even more acute risk than the larger group.

[13] For the respondent, the risk of crime faced by the applicant was general rather than personal, as it was prevalent throughout the entire country. While the perception of the applicant as wealthy could increase his chances of being victimized, it does not mean that the risk is no longer generalized.

[14] I note at the outset, that in order to succeed on a s. 97 claim, a claimant must provide “persuasive evidence (i.e. a balance of probabilities) establishing the facts” on which he relies (Li v. Canada (Minister of Citizenship and Immigration), 2003 FC 1514, [2003] F.C.J. No. 1934 (QL), at para. 50, aff’d 2005 FCA 1). In the present case, the alleged facts were generally accepted by the Board. My reading of the decision reveals that he applicant’s status as a victim of gang violence and extortion in the past was uncontested, nor does the Board appear to rule out that he may be a victim in the future. For the Board, the weakness in the applicant’s claim stemmed from the fact that the risk he faced was also faced by the general Haitian population and therefore was not personalized.

[15] Thus, the present case raises the issue of the interpretation of the meaning of the terms “personally” and “generally” as contained in s. 97(1) of the Act:
A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally […]
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if […]
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country […] [Emphasis added]
[…]
A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée : […]
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant : […]
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas, […]
[je souligne]

[16] The test under s. 97 of the Act is distinct from the test under section 96. As Rouleau J. noted in Ahmad v. Canada (Minister of Citizenship and Immigration), 2004 FC 808, [2004] F.C.J. No. 995 (QL), at para. 21, s. 97 “requires the Board to apply a different criterion pertaining to the issue of whether the applicant’s removal may or may not expose him personally to the risks and dangers referred to in paragraphs 97(1)(a) and (b) of the Act” and must be assessed with reference to the personal situation of the applicant. Moreover, he indicated that the “assessment of the applicant’s fear must be made in concreto, and not from an abstract and general perspective” (at para. 22).

[17] Accordingly, documentary evidence which illustrates the systematic and generalized violation of human rights in a given country will not be sufficient to ground a section 97 claim absent proof that might link this general documentary evidence to the applicant’s specific circumstances (Ould v. Canada (Minister of Citizenship and Immigration), 2007 FC 83, [2007] F.C.J. No. 103 (QL), at para. 21; Jarada v. Canada (Minster of Citizenship and Immigration), 2005 FC 409, [2005] F.C.J. No. 506 (QL), at para. 28; Ahmad, supra, at para. 22).

[18] The difficulty in analyzing personalized risk in situations of generalized human rights violations, civil war, and failed states lies in determining the dividing line between a risk that is “personalized” and one that is “general”. Under these circumstances, the Court may be faced with applicant who has been targeted in the past and who may be targeted in the future but whose risk situation is similar to a segment of the larger population. Thus, the Court is faced with an individual who may have a personalized risk, but one that is shared by many other individuals.

[19] Recently, the term “generally” was interpreted in a manner that may include segments of the larger population, as well as all residents or citizens of a given country. In Osorio v. Canada (Minister of Citizenship and Immigration), 2005 FC 1459, [2005] F.C.J. No. 1792 (QL). In that case, the applicant asserted that if he and his young Canadian born son were returned to Colombia it would constitute indirect cruel and unusual treatment/punishment because of the psychological stress that he would experience as a parent worrying about his child’s welfare in that country. At paras, 24 and 26 Snider J. stated:

[24] It seems to me that common sense must determine the meaning of s. 97(1)(b)(ii) […]

[26] Further, I can see nothing in s. 97(1)(b)(ii) that requires the Board to interpret "generally" as applying to all citizens. The word "generally" is commonly used to mean "prevalent" or "wide-spread". Parliament deliberately chose to include the word "generally" in s. 97(1)(b)(ii), thereby leaving to the Board the issue of deciding whether a particular group meets the definition. Provided that its conclusion is reasonable, as it is here, I see no need to intervene. [Emphasis added]
Snider J. concluded that the Board had not erred in its determination given that the risk described by the applicant was one faced by all Colombians who have or will have children.

[20] Recently in Cius, supra, Justice Michel Beaudry, dealt with an individual situated similarly to the present applicant: a Haitian man who alleged a fear of, among other things, armed gangs in Haiti who target Haitians who have been abroad, foreigners, and anyone who they perceive to have wealth.

[21] In his analysis of the claim, Beaudry J. noted, at para. 18, that the applicant was the subject of general violence, which was the fallout of criminal activity and that “[as] a group, people who are perceived to be wealthy are not marginalized in Haiti; rather they are more frequent targets of criminal activity.” Further, at para. 23, in the context of the s. 97 analysis, Beaudry J. asserted:
It is my opinion that the Board did not err by determining that the applicant did not face a particularized risk upon his return. […] However, as discussed above, the risk faced by the applicant is generalized. The risk of violence is one which every person in Haiti faces. The documentary evidence submitted in support of this case indicates that there is a serious risk to the personal safety of all in Haiti. The United Nations High Commissioner for Refugees (UNHCR) has recommended the suspension of forced returns to Haiti.

[22] In the recent case of Carias v Canada (Minister of Citizenship and Immigration), 2007 FC 602, [2007] F.C.J. No. 817 (QL), at paras. 23 and 25, O’Keefe J. concluded that the applicants faced a generalized risk of economic crime which was experienced by many other Hondurans, including those perceived as wealthy. In that particular case, the Board accepted that the applicants had been the victims of violence, however, O’Keefe J. dismissed the application indicating, at para. 25, that “[t]he applicants are members of a large group of people who may be targeted for economic crimes in Honduras on basis of their perceived wealth.” Further, he held that “[g]iven the wording of subparagraph 97(1)(b)(ii) of the IRPA, the applicants had to satisfy the Board that they would be personally subjected to a risk that was not generally faced by others in Honduras.”

[23] Based on the recent jurisprudence of this Court, I am of the view that the applicant does not face a personalized risk that is not faced generally by other individuals in or from Haiti. The risk of all forms of criminality is general and felt by all Haitians. While a specific number of individuals may be targeted more frequently because of their wealth, all Haitians are at risk of becoming the victims of violence.

[24] For these reasons, the application for judicial review of the Immigration and Refugee Board decision is dismissed.

## 21487:3 · paragraphs 28-31

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9e6c89a694d5c2aad9f70de7417ff280b2a626ddf03bb9f33439879ef73a792b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21487:3:subtheme:1 · paragraphs 28-29

- Raw key terms: `applicant, question, appeal, application, apply, broad, canada, certification`
- Display key terms: `question, apply, broad, certification`
- Argument roles: `issue, party_position, reasoning_application`
- Explanation: Observed roles: issue, party_position, reasoning_application Display terms: question, apply, broad, certification Position/evidence statements: [25] The applicant submits the following question for certification: Where the population of a country faces a generalized risk of crime, does the limitation of section 97 (1)(b)(ii) of the IRPA apply to a subgroup of in Application context: [25] The applicant submits the following question for certification: Where the population of a country faces a generalized risk of crime, does the limitation of section 97 (1)(b)(ii) of the IRPA apply to a subgroup of in | In my view, the question posed by the applicant’s satisfies this test and therefore shall be certified. Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5009245` offsets `41-49`; context: [25] The applicant submits the following question for certification:
Where the population of a country faces a generalized risk of crime, does the limitation of section 97 (1)(b)(ii) of the IRPA apply to a subgroup of individuals who face a significantly heightened risk of such crime?
- Evidence: `party_position` cue `submits` at chunk `5009245` offsets `19-26`; context: [25] The applicant submits the following question for certification:
Where the population of a country faces a generalized risk of crime, does the limitation of section 97 (1)(b)(ii) of the IRPA apply to a subgroup of individuals who face a significantly heightened risk of such crime?
- Evidence: `reasoning_application` cue `apply` at chunk `5009245` offsets `195-200`; context: [25] The applicant submits the following question for certification:
Where the population of a country faces a generalized risk of crime, does the limitation of section 97 (1)(b)(ii) of the IRPA apply to a subgroup of individuals who face a significantly heightened risk of such crime?
- Evidence: `issue` cue `question` at chunk `5009246` offsets `26-34`; context: [26] To be certified, the question must be one which transcends the interests of the immediate parties to the litigation, contemplates issues of broad significance or general application, and be one that is determinative of the appeal (Canada (Minister of Citizenship and Immigration) v.
- Evidence: `reasoning_application` cue `therefore` at chunk `5009246` offsets `422-431`; context: In my view, the question posed by the applicant’s satisfies this test and therefore shall be certified.

#### 21487:3:subtheme:2 · paragraphs 30-31

- Raw key terms: `immigration, application, apply, board, cause, certified, citizenship, country`
- Display key terms: `apply, certified, country`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: apply, certified, country Application context: The following question is certified: Where the population of a country faces a generalized risk of crime, does the limitation of section 97 (1)(b)(ii) of the IRPA apply to a subgroup of individuals who face a significant Operative outcome context: The application for judicial review of the Immigration and Refugee Board decision is dismissed. Evidence spans paragraphs 30-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5009247` offsets `144-152`; context: The following question is certified:
Where the population of a country faces a generalized risk of crime, does the limitation of section 97 (1)(b)(ii) of the IRPA apply to a subgroup of individuals who face a significantly heightened risk of such crime?
- Evidence: `reasoning_application` cue `apply` at chunk `5009247` offsets `293-298`; context: The following question is certified:
Where the population of a country faces a generalized risk of crime, does the limitation of section 97 (1)(b)(ii) of the IRPA apply to a subgroup of individuals who face a significantly heightened risk of such crime?
- Evidence: `disposition` cue `dismissed` at chunk `5009247` offsets `116-125`; context: The application for judicial review of the Immigration and Refugee Board decision is dismissed.

#### Section text

[25] The applicant submits the following question for certification:
Where the population of a country faces a generalized risk of crime, does the limitation of section 97 (1)(b)(ii) of the IRPA apply to a subgroup of individuals who face a significantly heightened risk of such crime?

[26] To be certified, the question must be one which transcends the interests of the immediate parties to the litigation, contemplates issues of broad significance or general application, and be one that is determinative of the appeal (Canada (Minister of Citizenship and Immigration) v. Liyanagamage (F.C.A.), [1994] F.C.J. No. 1637, at para. 4). In my view, the question posed by the applicant’s satisfies this test and therefore shall be certified.
JUDGMENT

[27] THIS COURT ORDERS that
1. The application for judicial review of the Immigration and Refugee Board decision is dismissed.
2. The following question is certified:
Where the population of a country faces a generalized risk of crime, does the limitation of section 97 (1)(b)(ii) of the IRPA apply to a subgroup of individuals who face a significantly heightened risk of such crime?
“Danièle Tremblay-Lamer”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-3077-07
STYLE OF CAUSE: RALPH PROPHÈTE
v.
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Montreal (Quebec)
DATE OF HEARING: February 28, 2008
REASONS FOR 

## 21487:4 · paragraphs 32-32

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fdf96c09253bd1a37036195ee2ade1b56700d4435dc488e1af2381204eb3fd77`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21487:4:subtheme:1 · paragraphs 32-32

- Raw key terms: `appearances, applicant, attorney, avocats, canada, dated, deputy, general`
- Display key terms: `avocats, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: avocats, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 32-32. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: TREMBLAY-LAMER J.
DATED: March 12, 2008
APPEARANCES:
Mr. Peter Shams
FOR THE APPLICANT
Mrs. Michèle Joubert
FOR THE RESPONDENT
SOLICITORS OF RECORD:
SAINT-PIERRE, GRENIER AVOCATS INC.
Montreal, Quebec
FOR THE APPLICANT
JOHN H. SIMS, Q.C.
Deputy Attorney General of Canada
FOR THE RESPONDENT
