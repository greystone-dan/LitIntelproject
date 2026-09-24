# Discussion Units: case 20525

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **47**
- Continuity pairs: **46**
- Discussion Units: **3**
- Paragraph source hashes: **47**
- Sub-themes: **16**

## 20525:1 · paragraphs 0-43

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a863ae3ec5ef7b228712e759267914abd83c947c193867904d09374bfc9cead2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20525:1:subtheme:1 · paragraphs 0-6

- Raw key terms: `applicant, based, board, decision, gang, haiti, rejected, alleged`
- Display key terms: `based, gang, haiti, rejected, alleged`
- Argument roles: `counterargument_limitation, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, party_position, reasoning_application Display terms: based, gang, haiti, rejected, alleged Position/evidence statements: [6] The Board found that the gang which the applicant claimed to fear was an organized criminal entity. Application context: She also feared to go back because there is sexual abuse and violence against women in Haiti and the state is not protecting them. Evidence spans paragraphs 0-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4969045` offsets `324-331`; context: She also feared to go back because there is sexual abuse and violence against women in Haiti and the state is not protecting them.
- Evidence: `evidence_fact` cue `determined that` at chunk `4969046` offsets `14-29`; context: [5] The Board determined that the applicant was not credible regarding her description of the alleged gang attacks on her father in 2004 and 2005.
- Evidence: `party_position` cue `claimed` at chunk `4969047` offsets `54-61`; context: [6] The Board found that the gang which the applicant claimed to fear was an organized criminal entity.
- Evidence: `evidence_fact` cue `found that` at chunk `4969047` offsets `14-24`; context: [6] The Board found that the gang which the applicant claimed to fear was an organized criminal entity.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4969047` offsets `104-112`; context: Although the evidence showed that in Haiti organized criminal entities were, at one point in history, very closed affiliated with political parties or the military, they no longer have political affiliations.

#### 20525:1:subtheme:2 · paragraphs 7-10

- Raw key terms: `board, political, applicant, because, constitute, evidence, fact, group`
- Display key terms: `political, because, constitute, fact, group`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, reasoning_application Display terms: political, because, constitute, fact, group Rule/authority context: The standard of review for questions of fact and questions of mixed fact and law is reasonableness (Dunsmuir v. Application context: [7] Finally, the Board accepted that Haitian women do constitute a particular social group, but they do not face persecution because of their membership therein. | [10] This brings us to the applicant’s claim for protection because of her membership in a particular social group, here Haitian women. Evidence spans paragraphs 7-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4969048` offsets `125-132`; context: [7] Finally, the Board accepted that Haitian women do constitute a particular social group, but they do not face persecution because of their membership therein.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969049` offsets `188-196`; context: However, she strongly contests the correctness of the Board’s legal approach and reasonableness of its analysis of the evidence regarding the political nature of gang violence in Haiti and the gender-targeted nature of rape in Haiti.
- Evidence: `governing_rule` cue `standard of review` at chunk `4969049` offsets `307-325`; context: The standard of review for questions of fact and questions of mixed fact and law is reasonableness (Dunsmuir v.
- Evidence: `counterargument_limitation` cue `However` at chunk `4969049` offsets `69-76`; context: However, she strongly contests the correctness of the Board’s legal approach and reasonableness of its analysis of the evidence regarding the political nature of gang violence in Haiti and the gender-targeted nature of rape in Haiti.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969050` offsets `224-232`; context: Even if one accepts that political motive can coexist with non-Convention grounds, the evidence before the Board was highly speculative and virtually untied to political involvement (or leading to an inference that political motive could constitute a secondary ground).
- Evidence: `reasoning_application` cue `because` at chunk `4969051` offsets `60-67`; context: [10] This brings us to the applicant’s claim for protection because of her membership in a particular social group, here Haitian women.

#### 20525:1:subtheme:3 · paragraphs 11-13

- Raw key terms: `soimin, above, claimant, country, court, haiti, kidnapped, legal`
- Display key terms: `soimin, above, country, haiti, kidnapped, legal`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: soimin, above, country, haiti, kidnapped, legal Position/evidence statements: Moreover, there was no analysis by the Court of relevant legal principles or case law with respect to gender-related claims under section 96 of the Act. Rule/authority context: Moreover, there was no analysis by the Court of relevant legal principles or case law with respect to gender-related claims under section 96 of the Act. Application context: [12] The claimant in Soimin, above, feared that she would be kidnapped, raped and tortured should she return to Haiti because of the general crime and violence in her country of origin, since she had travelled abroad and Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4969052` offsets `563-570`; context: In this regard, the Court has cautioned the Board not to import into the definition of a Convention refugee, legal requirements which are specific to section 97 when the Board is assessing whether the fear of persecution is based on a Convention ground in light of section 96 of the Act.
- Evidence: `reasoning_application` cue `because` at chunk `4969053` offsets `118-125`; context: [12] The claimant in Soimin, above, feared that she would be kidnapped, raped and tortured should she return to Haiti because of the general crime and violence in her country of origin, since she had travelled abroad and would therefore be perceived as being wealthy.
- Evidence: `party_position` cue `claims` at chunk `4969054` offsets `530-536`; context: Moreover, there was no analysis by the Court of relevant legal principles or case law with respect to gender-related claims under section 96 of the Act.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969054` offsets `403-411`; context: Apparently, her risk of being kidnapped and raped was no different from that faced by other individuals from her country, but in the Court’s decision, there was no specific mention or analysis of the documentary evidence.
- Evidence: `governing_rule` cue `principles` at chunk `4969054` offsets `476-486`; context: Moreover, there was no analysis by the Court of relevant legal principles or case law with respect to gender-related claims under section 96 of the Act.

#### 20525:1:subtheme:4 · paragraphs 14-15

- Raw key terms: `above, claim, court, frejuste, noted, perceived, returnee, risk`
- Display key terms: `above, frejuste, noted, perceived, returnee, risk`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: above, frejuste, noted, perceived, returnee, risk Position/evidence statements: The Court further noted that there were two separate categories of risk underlying the claimant’s section 97 claim: the risk associated with being a returnee who has spent time in North America and is therefore perceived Application context: The Court further noted that there were two separate categories of risk underlying the claimant’s section 97 claim: the risk associated with being a returnee who has spent time in North America and is therefore perceived | [15] In allowing the judicial review application, the Court noted in Frejuste, above, that the Board had addressed the gender issue and the returnee issue simultaneously and that “this case may have been obscured by the  Evidence spans paragraphs 14-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4969055` offsets `181-188`; context: [14] In contrast, the Court stated in Frejuste, above, that “as the documentary evidence reveals, the risk of sexual violence is one widely faced by women in Haiti, irrespective of whether or not they are returnees” (Frejuste, above, at paragraph 34).
- Evidence: `party_position` cue `claim` at chunk `4969055` offsets `361-366`; context: The Court further noted that there were two separate categories of risk underlying the claimant’s section 97 claim: the risk associated with being a returnee who has spent time in North America and is therefore perceived as a person of wealth, and the risk of being a single woman in Haiti.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969055` offsets `80-88`; context: [14] In contrast, the Court stated in Frejuste, above, that “as the documentary evidence reveals, the risk of sexual violence is one widely faced by women in Haiti, irrespective of whether or not they are returnees” (Frejuste, above, at paragraph 34).
- Evidence: `reasoning_application` cue `therefore` at chunk `4969055` offsets `453-462`; context: The Court further noted that there were two separate categories of risk underlying the claimant’s section 97 claim: the risk associated with being a returnee who has spent time in North America and is therefore perceived as a person of wealth, and the risk of being a single woman in Haiti.
- Evidence: `issue` cue `issue` at chunk `4969056` offsets `126-131`; context: [15] In allowing the judicial review application, the Court noted in Frejuste, above, that the Board had addressed the gender issue and the returnee issue simultaneously and that “this case may have been obscured by the applicant’s emphasis on a risk as a returnee who might be targeted because of her perceived wealth”.
- Evidence: `reasoning_application` cue `because` at chunk `4969056` offsets `287-294`; context: [15] In allowing the judicial review application, the Court noted in Frejuste, above, that the Board had addressed the gender issue and the returnee issue simultaneously and that “this case may have been obscured by the applicant’s emphasis on a risk as a returnee who might be targeted because of her perceived wealth”.

#### 20525:1:subtheme:5 · paragraphs 16-19

- Raw key terms: `basis, board, cannot, case, claim, evidence, haiti, woman`
- Display key terms: `basis, cannot, case, haiti, woman`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: basis, cannot, case, haiti, woman Application context: Canada (Minister of Citizenship and Immigration), 2010 FC 1100, the Court was tasked with evaluating whether the Board’s conclusion that fear of sexual assault cannot give rise to refugee protection because it amounts to Operative outcome context: Justice O’Reilly of this Court dismissed the application, but explicitly stated at paragraph 11 that: … while the issues raised in this case are difficult and merit, in appropriate circumstances, serious scrutiny both by | [19] That being said, in Dezameau, above, it appears that the Board had dismissed the claim on the basis that the Prime Minister of Haiti was a woman and half of Haiti’s population were women. Evidence spans paragraphs 16-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4969057` offsets `121-128`; context: Canada (Minister of Citizenship and Immigration), 2010 FC 1100, the Court was tasked with evaluating whether the Board’s conclusion that fear of sexual assault cannot give rise to refugee protection because it amounts to a general fear of crime which affects the entire population of Haiti, and not a particular social group, was reasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969057` offsets `842-850`; context: Accordingly, the evidence before the Board was not as extensive as one might otherwise have expected, and the submissions on the point were not as detailed as they might have been in a case in which the issue was central to the claim.
- Evidence: `reasoning_application` cue `because` at chunk `4969057` offsets `219-226`; context: Canada (Minister of Citizenship and Immigration), 2010 FC 1100, the Court was tasked with evaluating whether the Board’s conclusion that fear of sexual assault cannot give rise to refugee protection because it amounts to a general fear of crime which affects the entire population of Haiti, and not a particular social group, was reasonable.
- Evidence: `disposition` cue `dismissed` at chunk `4969057` offsets `393-402`; context: Justice O’Reilly of this Court dismissed the application, but explicitly stated at paragraph 11 that:
… while the issues raised in this case are difficult and merit, in appropriate circumstances, serious scrutiny both by the Board and this Court, this is not an apt case to analyze them thoroughly.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969058` offsets `134-142`; context: [17] The same cannot be said for the present case, in which the claim based on gender was expressly made and is well-supported by the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969059` offsets `384-392`; context: With regard to the second ground, the Court acknowledged that the Board’s failure to include a gender-based analysis in its assessment of the evidence of violence directed at women in Haiti constitutes a reviewable error.
- Evidence: `counterargument_limitation` cue `but` at chunk `4969060` offsets `263-266`; context: The Board’s conclusion was that the risk of rape is not due to gender but, rather, a risk that all Haitians face as a result of generalized crime and as such, it cannot support a refugee claim.
- Evidence: `disposition` cue `dismissed` at chunk `4969060` offsets `72-81`; context: [19] That being said, in Dezameau, above, it appears that the Board had dismissed the claim on the basis that the Prime Minister of Haiti was a woman and half of Haiti’s population were women.

#### 20525:1:subtheme:6 · paragraphs 20-21

- Raw key terms: `above, board, court, dezameau, fact, paragraph, rape, risk`
- Display key terms: `above, dezameau, fact, paragraph, rape, risk`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: above, dezameau, fact, paragraph, rape, risk Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4969061` offsets `167-175`; context: [20] Disagreeing with the respondent’s assertion that the judgment in Soimin, above, was determinative, the Court stated in Dezameau, above, at paragraph 22, that the question “is whether the Board’s finding that the applicant faced a risk of general criminality such that there is no nexus between her risk and her social group is defensible in law or in fact”.
- Evidence: `issue` cue `whether` at chunk `4969062` offsets `351-358`; context: [21] The Court in Dezameau, above, at paragraph 24, referred expressly to the Chairperson’s Guideline 4, Women Refugee Claimants Fearing Gender-Related Persecution, Immigration and Refugee Board of Canada (Guideline 4):
The fact that violence, including sexual violence and domestic violence, against women is universal is irrelevant when determining whether rape, and other gender-specific crimes constitute forms of persecution.

#### 20525:1:subtheme:7 · paragraphs 22-25

- Raw key terms: `above, court, dezameau, assaults, canada, canadian, cannot, claim`
- Display key terms: `above, dezameau, assaults, canadian, cannot`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: above, dezameau, assaults, canadian, cannot Rule/authority context: In other words, a finding that a risk is universally experienced by a social group does not foreclose the inquiry under section 96. | [25] Canadian jurisprudence is also emphatic on the point. Application context: [22] Indeed, a gender-specific claim cannot be rejected simply because the group in question or its members face general oppression and the claimant’s fear of persecution is not supported by an individualized set of fact Evidence spans paragraphs 22-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4969063` offsets `84-92`; context: [22] Indeed, a gender-specific claim cannot be rejected simply because the group in question or its members face general oppression and the claimant’s fear of persecution is not supported by an individualized set of facts.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969063` offsets `346-354`; context: Where the claimant has not, himself or herself, experienced the type of persecution, he or she fears, the claimant can use evidence of similarly-situated persons to demonstrate the risk and the unwillingness or inability of the state to protect (Dezameau, above, at paragraph 26; Salibian v.
- Evidence: `reasoning_application` cue `because` at chunk `4969063` offsets `63-70`; context: [22] Indeed, a gender-specific claim cannot be rejected simply because the group in question or its members face general oppression and the claimant’s fear of persecution is not supported by an individualized set of facts.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4969063` offsets `37-43`; context: [22] Indeed, a gender-specific claim cannot be rejected simply because the group in question or its members face general oppression and the claimant’s fear of persecution is not supported by an individualized set of facts.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969064` offsets `250-258`; context: The evidence provided by the applicant must still satisfy the Board that there is a risk of harm that is sufficiently serious and whose occurrence is “more than a mere possibility”.
- Evidence: `governing_rule` cue `under` at chunk `4969064` offsets `659-664`; context: In other words, a finding that a risk is universally experienced by a social group does not foreclose the inquiry under section 96.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4969066` offsets `14-27`; context: [25] Canadian jurisprudence is also emphatic on the point.

#### 20525:1:subtheme:8 · paragraphs 26-30

- Raw key terms: `women, convention, group, indeed, above, approach, board, constitute`
- Display key terms: `women, convention, group, indeed, above, approach, constitute`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: women, convention, group, indeed, above, approach, constitute Application context: [29] Indeed, Canadian scholar and practitioner, Lorne Waldman holds that women, at large, should be recognized as a particular social group, provided that the evidence proves that they are subject to severe violations of Evidence spans paragraphs 26-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4969067` offsets `269-276`; context: The latter specifically categorizes rape as a gender-specific crime:
The fact that violence, including sexual and domestic violence, against women is universal is irrelevant when determining whether rape, and other gender-specific crimes constitute forms of persecution.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969070` offsets `159-167`; context: [29] Indeed, Canadian scholar and practitioner, Lorne Waldman holds that women, at large, should be recognized as a particular social group, provided that the evidence proves that they are subject to severe violations of their fundamental human rights because of their gender (Lorne Waldman, The Definition of Convention Refugee (Buttersworth: Markham, Ontario, 2001) at §8.
- Evidence: `reasoning_application` cue `because` at chunk `4969070` offsets `252-259`; context: [29] Indeed, Canadian scholar and practitioner, Lorne Waldman holds that women, at large, should be recognized as a particular social group, provided that the evidence proves that they are subject to severe violations of their fundamental human rights because of their gender (Lorne Waldman, The Definition of Convention Refugee (Buttersworth: Markham, Ontario, 2001) at §8.

#### 20525:1:subtheme:9 · paragraphs 31-33

- Raw key terms: `board, haiti, rape, sexual, violence, women, boys, conclusion`
- Display key terms: `haiti, rape, sexual, violence, women, boys, conclusion`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: haiti, rape, sexual, violence, women, boys, conclusion Rule/authority context: [33] Thus, the Board’s findings and general conclusion that nexus has not been established is unreasonable, as it goes directly against the legal principles already discussed above and is not based on the documentary evi Application context: In the case at hand, the Board has generally found that Haitian women do not face persecution in the form of violence and sexual abuse because of their membership in that group: “Women in Haiti are not targeted qua women Evidence spans paragraphs 31-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4969072` offsets `28-35`; context: [31] Thus, the real test is whether the claimant is subject to persecution by reason of his or her membership in that particular social group.
- Evidence: `evidence_fact` cue `found that` at chunk `4969072` offsets `188-198`; context: In the case at hand, the Board has generally found that Haitian women do not face persecution in the form of violence and sexual abuse because of their membership in that group: “Women in Haiti are not targeted qua women.
- Evidence: `reasoning_application` cue `because` at chunk `4969072` offsets `278-285`; context: In the case at hand, the Board has generally found that Haitian women do not face persecution in the form of violence and sexual abuse because of their membership in that group: “Women in Haiti are not targeted qua women.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969073` offsets `286-294`; context: In addition, the documentary evidence before the Board clearly demonstrates that women and girls in Haiti face an elevated risk of violence and rape, a risk that is not similarly experienced by men and boys, even though men and boys can also be victims of rape.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969074` offsets `217-225`; context: [33] Thus, the Board’s findings and general conclusion that nexus has not been established is unreasonable, as it goes directly against the legal principles already discussed above and is not based on the documentary evidence.
- Evidence: `governing_rule` cue `principles` at chunk `4969074` offsets `146-156`; context: [33] Thus, the Board’s findings and general conclusion that nexus has not been established is unreasonable, as it goes directly against the legal principles already discussed above and is not based on the documentary evidence.

#### 20525:1:subtheme:10 · paragraphs 34-35

- Raw key terms: `board, fact, haiti, raped, reasonableness, violence, women, young`
- Display key terms: `fact, haiti, raped, reasonableness, violence, women, young`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: fact, haiti, raped, reasonableness, violence, women, young Rule/authority context: [35] The fact that the applicant “is a married 30 year old not an under 18 year old, single female” has strongly influenced the dismissal of this claim. Application context: [34] Therefore, the suggestion made by the Board that women are randomly raped in Haiti by criminals is not supported by the evidence; while women are targeted for kidnapping just like men, they are raped because they ar Evidence spans paragraphs 34-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4969075` offsets `520-525`; context: Again, the real issue is whether such violence is a serious violation of a fundamental human right for a Convention ground and the Board’s analysis in this regard is perfunctory and biased.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969075` offsets `125-133`; context: [34] Therefore, the suggestion made by the Board that women are randomly raped in Haiti by criminals is not supported by the evidence; while women are targeted for kidnapping just like men, they are raped because they are women.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4969075` offsets `5-14`; context: [34] Therefore, the suggestion made by the Board that women are randomly raped in Haiti by criminals is not supported by the evidence; while women are targeted for kidnapping just like men, they are raped because they are women.
- Evidence: `governing_rule` cue `under` at chunk `4969076` offsets `66-71`; context: [35] The fact that the applicant “is a married 30 year old not an under 18 year old, single female” has strongly influenced the dismissal of this claim.

#### 20525:1:subtheme:11 · paragraphs 36-38

- Raw key terms: `adequate, applicant, board, case, court, decision, fear, haiti`
- Display key terms: `adequate, case, fear, haiti`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: adequate, case, fear, haiti Application context: [36] In light of Canadian law and the evidence before the Board, the conclusion that as a Haitian woman, the applicant does not have reasonable fear of persecution because of her membership in that group is unreasonable. Operative outcome context: [37] The application is allowed and the impugned decision is set aside. Evidence spans paragraphs 36-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4969077` offsets `396-403`; context: Had the Board accepted that a risk of rape is grounded in the applicant’s membership in a particular social group, then the inquiry should have resulted in a determination of whether there is “more than a mere possibility” that the applicant risks suffering this harm in Haiti.
- Evidence: `evidence_fact` cue `evidence` at chunk `4969077` offsets `38-46`; context: [36] In light of Canadian law and the evidence before the Board, the conclusion that as a Haitian woman, the applicant does not have reasonable fear of persecution because of her membership in that group is unreasonable.
- Evidence: `reasoning_application` cue `because` at chunk `4969077` offsets `164-171`; context: [36] In light of Canadian law and the evidence before the Board, the conclusion that as a Haitian woman, the applicant does not have reasonable fear of persecution because of her membership in that group is unreasonable.
- Evidence: `disposition` cue `allowed` at chunk `4969078` offsets `24-31`; context: [37] The application is allowed and the impugned decision is set aside.

#### 20525:1:subtheme:12 · paragraphs 39-40

- Raw key terms: `absence, accompanied, account, adequate, affected, against, analyzed, applicant`
- Display key terms: `absence, accompanied, account, adequate, affected, against, analyzed`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: absence, accompanied, account, adequate, affected, against, analyzed Evidence spans paragraphs 39-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4969080` offsets `53-60`; context: [39] In particular, the Board should notably examine whether there is a rape epidemic in Haiti and whether there are serious violations of fundamental human rights against women for a Convention ground, taking into account these present reasons for judgment, the present political turmoil in Haiti and the climate of ongoing violence by different groups following the legislative elections and the first round of the presidential election of November 28, 2010.
- Evidence: `issue` cue `question` at chunk `4969081` offsets `49-57`; context: [40] The respondent has not proposed any general question of importance for certification.

#### 20525:1:subtheme:13 · paragraphs 41-42

- Raw key terms: `against, made, respect, respondent, above, appeal, applied, assumption`
- Display key terms: `against, made, respect, above, applied, assumption`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: against, made, respect, above, applied, assumption Application context: Incidentally, the following question was certified in Dezameau, above: Can an assumption that rape is not a crime predicated on gender and reflecting gender imbalances be applied in an evidentiary vacuum, without regard  Evidence spans paragraphs 41-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4969082` offsets `226-234`; context: Incidentally, the following question was certified in Dezameau, above:
Can an assumption that rape is not a crime predicated on gender and reflecting gender imbalances be applied in an evidentiary vacuum, without regard to evidence demonstrating the contrary with respect to conditions in a refugee claimant’s country of nationality?
- Evidence: `evidence_fact` cue `evidence` at chunk `4969082` offsets `421-429`; context: Incidentally, the following question was certified in Dezameau, above:
Can an assumption that rape is not a crime predicated on gender and reflecting gender imbalances be applied in an evidentiary vacuum, without regard to evidence demonstrating the contrary with respect to conditions in a refugee claimant’s country of nationality?
- Evidence: `reasoning_application` cue `applied` at chunk `4969082` offsets `369-376`; context: Incidentally, the following question was certified in Dezameau, above:
Can an assumption that rape is not a crime predicated on gender and reflecting gender imbalances be applied in an evidentiary vacuum, without regard to evidence demonstrating the contrary with respect to conditions in a refugee claimant’s country of nationality?

#### 20525:1:subtheme:14 · paragraphs 43-43

- Raw key terms: `accordingly, certified, court, question`
- Display key terms: `accordingly, certified, question`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: accordingly, certified, question Application context: [43] Accordingly, no question is certified by this Court. Evidence spans paragraphs 43-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4969084` offsets `21-29`; context: [43] Accordingly, no question is certified by this Court.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4969084` offsets `5-16`; context: [43] Accordingly, no question is certified by this Court.

#### Section text

Josile v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2011-01-17
Neutral citation
2011 FC 39
File numbers
IMM-3623-10
Decision Content
Federal Court
Cour fédérale
Date: 20110117
Docket: IMM-3623-10
Citation: 2011 FC 39
Ottawa, Ontario, January 17, 2011
PRESENT: The Honourable Mr. Justice Martineau
BETWEEN:
DULEINE JOSILE
Applicant
and
MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is a judicial review of a decision made by the Immigration and Refugee Board, Refugee Protection Division (the Board), dated May 25, 2010, wherein the applicant was determined to be neither a Convention refugee nor a person in need of protection within the meaning of sections 96 and 97 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (the Act).

[2] The factual background leading to the impugned decision is not challenged.

[3] The applicant is a female Haitian national born in 1980. She left Haiti in 2005 and had her refugee claim rejected by the United States the same year. In 2007, she made her Canadian refugee claim based on political opinion and membership in a particular social group (Haitian women) or other social group (family).

[4] The applicant alleged that her father, a minor government official in a small village in Haiti, was beaten by gang members in 2004 and threatened again by armed men in 2005 as a result of his providing information to the police about the identities of the murderers of a local pastor in 2003. She also feared to go back because there is sexual abuse and violence against women in Haiti and the state is not protecting them.

[5] The Board determined that the applicant was not credible regarding her description of the alleged gang attacks on her father in 2004 and 2005. The applicant’s argument based on membership in a social group (family) was rejected.

[6] The Board found that the gang which the applicant claimed to fear was an organized criminal entity. Although the evidence showed that in Haiti organized criminal entities were, at one point in history, very closed affiliated with political parties or the military, they no longer have political affiliations. The applicant’s claim based on political opinion was thus rejected.

[7] Finally, the Board accepted that Haitian women do constitute a particular social group, but they do not face persecution because of their membership therein. While Haitian women face violence and rape, these dangers are generally faced by the population, men and women alike. Moreover, the Board noted that perpetrators of rape in Haiti are mostly poor, young, uneducated males who are not pursuing a political agenda.

[8] The applicant does not contest the Board’s credibility findings. However, she strongly contests the correctness of the Board’s legal approach and reasonableness of its analysis of the evidence regarding the political nature of gang violence in Haiti and the gender-targeted nature of rape in Haiti. The standard of review for questions of fact and questions of mixed fact and law is reasonableness (Dunsmuir v. New Brunswick, 2008 SCC 9, at paragraph 51). However, the Board’s legal interpretation of sections 96 and 97 of the Act, including key elements inherent in the Refugee definition (i.e. persecution and nexus), is reviewable under a correctness standard.

[9] First, the Court finds that the Board’s conclusions of fact as to the apolitical nature of organized criminal groups are reasonable. Even if one accepts that political motive can coexist with non-Convention grounds, the evidence before the Board was highly speculative and virtually untied to political involvement (or leading to an inference that political motive could constitute a secondary ground). This part of the Board’s decision is entirely supported by the evidence and thus the Court has no grounds to interfere.

[10] This brings us to the applicant’s claim for protection because of her membership in a particular social group, here Haitian women.

[11] The situation of sexual abuse and violence against women in Haiti has recently come to the attention of the Federal Court: Soimin v. Canada (Minister of Citizenship and Immigration), 2009 FC 218 (Soimin); Frejuste v. Canada (Citizenship and Immigration), 2009 FC 586 (Frejuste); and Dezameau v. Canada (Minister of Citizenship and Immigration), 2010 FC 559 (Dezameau). In this regard, the Court has cautioned the Board not to import into the definition of a Convention refugee, legal requirements which are specific to section 97 when the Board is assessing whether the fear of persecution is based on a Convention ground in light of section 96 of the Act.

[12] The claimant in Soimin, above, feared that she would be kidnapped, raped and tortured should she return to Haiti because of the general crime and violence in her country of origin, since she had travelled abroad and would therefore be perceived as being wealthy. The finding that “[t]he violence feared by the applicant arises from general criminal activity in Haiti, and not the discriminatory targeting of women in particular” (Soimin, above, at paragraph 14) was not seriously challenged by the claimant.

[13] In dismissing the judicial review application, the Court in Soimin, above, simply accepted that in light of section 97 of the Act, the claimant was not a “person in need of protection”. Apparently, her risk of being kidnapped and raped was no different from that faced by other individuals from her country, but in the Court’s decision, there was no specific mention or analysis of the documentary evidence. Moreover, there was no analysis by the Court of relevant legal principles or case law with respect to gender-related claims under section 96 of the Act.

[14] In contrast, the Court stated in Frejuste, above, that “as the documentary evidence reveals, the risk of sexual violence is one widely faced by women in Haiti, irrespective of whether or not they are returnees” (Frejuste, above, at paragraph 34). The Court further noted that there were two separate categories of risk underlying the claimant’s section 97 claim: the risk associated with being a returnee who has spent time in North America and is therefore perceived as a person of wealth, and the risk of being a single woman in Haiti.

[15] In allowing the judicial review application, the Court noted in Frejuste, above, that the Board had addressed the gender issue and the returnee issue simultaneously and that “this case may have been obscured by the applicant’s emphasis on a risk as a returnee who might be targeted because of her perceived wealth”. That being said, there was no discussion regarding the application of section 96 of the Act in the context of a gender-related claim.

[16] In Frederic v. Canada (Minister of Citizenship and Immigration), 2010 FC 1100, the Court was tasked with evaluating whether the Board’s conclusion that fear of sexual assault cannot give rise to refugee protection because it amounts to a general fear of crime which affects the entire population of Haiti, and not a particular social group, was reasonable. Justice O’Reilly of this Court dismissed the application, but explicitly stated at paragraph 11 that:
… while the issues raised in this case are difficult and merit, in appropriate circumstances, serious scrutiny both by the Board and this Court, this is not an apt case to analyze them thoroughly. As mentioned, the proposition that a woman’s fear of sexual violence could form the basis of a refugee claim was not the main thrust of Ms. Frederic’s application. Accordingly, the evidence before the Board was not as extensive as one might otherwise have expected, and the submissions on the point were not as detailed as they might have been in a case in which the issue was central to the claim.

[17] The same cannot be said for the present case, in which the claim based on gender was expressly made and is well-supported by the evidence.

[18] Even more telling is Dezameau, above, a case very similar to the present one. There, the claimant was a Haitian woman fearing persecution on the basis of her political opinion, as well as her membership in a social group, Haitian women. With regard to the second ground, the Court acknowledged that the Board’s failure to include a gender-based analysis in its assessment of the evidence of violence directed at women in Haiti constitutes a reviewable error.

[19] That being said, in Dezameau, above, it appears that the Board had dismissed the claim on the basis that the Prime Minister of Haiti was a woman and half of Haiti’s population were women. The Board’s conclusion was that the risk of rape is not due to gender but, rather, a risk that all Haitians face as a result of generalized crime and as such, it cannot support a refugee claim.

[20] Disagreeing with the respondent’s assertion that the judgment in Soimin, above, was determinative, the Court stated in Dezameau, above, at paragraph 22, that the question “is whether the Board’s finding that the applicant faced a risk of general criminality such that there is no nexus between her risk and her social group is defensible in law or in fact”. In allowing the judicial review application, the Court concluded that “the error of the Board was to use its finding of widespread risk of violence to rebut the assertion that there is a nexus between the applicant’s social group and the risk of rape” (Dezameau, above, at paragraph 23).

[21] The Court in Dezameau, above, at paragraph 24, referred expressly to the Chairperson’s Guideline 4, Women Refugee Claimants Fearing Gender-Related Persecution, Immigration and Refugee Board of Canada (Guideline 4):
The fact that violence, including sexual violence and domestic violence, against women is universal is irrelevant when determining whether rape, and other gender-specific crimes constitute forms of persecution. The real issues are whether the violence – experienced or feared – is a serious violation of a fundamental human right for a Convention ground and in what circumstances can the risk of that violence be said to result from a failure of state protection.
(Emphasis in original.)

[22] Indeed, a gender-specific claim cannot be rejected simply because the group in question or its members face general oppression and the claimant’s fear of persecution is not supported by an individualized set of facts. Where the claimant has not, himself or herself, experienced the type of persecution, he or she fears, the claimant can use evidence of similarly-situated persons to demonstrate the risk and the unwillingness or inability of the state to protect (Dezameau, above, at paragraph 26; Salibian v. Canada (Minister of Employment and Immigration), [1990] 3 F.C. 250 at pages 258 and 259).

[23] My colleague Justice Pinard, who rendered the judgment of the Court in Dezameau, above, also noted at paragraphs 29 and 31:
This is not to say that membership in a particular social group is sufficient to result in a finding of persecution. The evidence provided by the applicant must still satisfy the Board that there is a risk of harm that is sufficiently serious and whose occurrence is “more than a mere possibility”.
…
As mentioned before, a general risk faced by a particular social group does not preclude a finding of persecution. In other words, a finding that a risk is universally experienced by a social group does not foreclose the inquiry under section 96. The Board foreclosed a proper inquiry into this claim by making an erroneous finding that the risk of violence, specifically rape, is a risk of generalized criminality that all Haitians face.

[24] With respect to the establishment of nexus, the Court in Dezameau, above, at paragraphs 34 and 35, notes that “it is well established in Canadian law that rape, and other forms of sexual assaults, are grounded in the status of women in society”, and adds to this effect that “[t]he notion that rape can be merely motivated by common criminal intent or desire, without regard to gender or the status of females in a society is wrong according to Canadian law”.

[25] Canadian jurisprudence is also emphatic on the point. For example, in R. v. Osolin, [1993] 4 S.C.R. 595, Justice Cory for the majority of the Supreme Court of Canada stated that “it cannot be forgotten that a sexual assault is very different from other assaults. It is true that it, like all the other forms of assault, is an act of violence. Yet it is something more than a simple act of violence. Sexual assault is in the vast majority of cases gender based. It is an assault upon human dignity and constitutes a denial of any concept of equality for women” (Osolin, above, at paragraph 165).

[26] Indeed, rape is referred to as a “gender-specific” crime in Guideline 4. The latter specifically categorizes rape as a gender-specific crime:
The fact that violence, including sexual and domestic violence, against women is universal is irrelevant when determining whether rape, and other gender-specific crimes constitute forms of persecution.
(My emphasis.)

[27] Consequently, I entirely agree with the approach taken by the Court in Dezameau, above.

[28] The Board, as well as the parties before the Court, accept that Haitian women can constitute a particular social group for the purpose of applying section 96 of the Act. Indeed, the Supreme Court of Canada has already recognized that the definition of a Convention refugee embraces “individuals fearing persecution on such bases as gender …” (Ward v. Canada (Attorney General), [1993] 2 S.C.R. 689, at page 739 (Ward)).

[29] Indeed, Canadian scholar and practitioner, Lorne Waldman holds that women, at large, should be recognized as a particular social group, provided that the evidence proves that they are subject to severe violations of their fundamental human rights because of their gender (Lorne Waldman, The Definition of Convention Refugee (Buttersworth: Markham, Ontario, 2001) at §8.288). In my opinion, such an approach is the correct one and flows from Ward, above.

[30] This conclusion is also in accordance with the human rights purpose of the Convention and is in line with other decisions of the Board, where women without male protection and adequate state protection who are persecuted in certain countries (e.g. Pakistan and Somalia) were found to be Convention refugees by reason of their membership in that group (G.L.U. (Re), [2000] C.R.D.D. No. 69; E.U.C. (Re), [2001] C.R.D.D. No. 253).

[31] Thus, the real test is whether the claimant is subject to persecution by reason of his or her membership in that particular social group. In the case at hand, the Board has generally found that Haitian women do not face persecution in the form of violence and sexual abuse because of their membership in that group: “Women in Haiti are not targeted qua women. They, like all others in Haiti, including men and boys are subject to endemic violence and as a result all kinds including rape. They are victims, as is everyone else, of chronic state breakdown and ubiquitous crime and violence”. This conclusion is untenable in this case.

[32] The applicant cited Professor Lise Gotell, a professor in the Women’s Studies Programme at the University of Alberta as stating that rape is never a genderless crime. This assertion was discarded by the Board, but it is amply supported by Guideline 4. In addition, the documentary evidence before the Board clearly demonstrates that women and girls in Haiti face an elevated risk of violence and rape, a risk that is not similarly experienced by men and boys, even though men and boys can also be victims of rape. Moreover, the number of women raped in Haiti has constantly been increasing over the past months. Many of the victims are single women. Most sexual attacks are committed by men. Moreover, almost half of the women kidnapped are raped. While nearly 50 percent of cases involve minors less than 18 years of age, the Doctors Without Borders Clinic in Port-au-Prince reported that of their 500 rape victims, over half were between 19 and 45 years old.

[33] Thus, the Board’s findings and general conclusion that nexus has not been established is unreasonable, as it goes directly against the legal principles already discussed above and is not based on the documentary evidence. More particularly, the Board erred or otherwise acted unreasonably in finding that rape is not a gender-related risk in Haiti or that only “some female Haitians under the age of 18 may be at risk of gender-related persecution”. The fact that much of the sexual violence against girls, and women in general, in Haiti occurs in a domestic or family context does not excuse or lift the persecutory nature of gender-related abuses against women in Haiti who are kidnapped by gangs or raped in camps since the earthquake of January 12, 2010.

[34] Therefore, the suggestion made by the Board that women are randomly raped in Haiti by criminals is not supported by the evidence; while women are targeted for kidnapping just like men, they are raped because they are women. Likewise, young boys may be abused because they are part of a vulnerable social group. The fact that there has been “horrific sexual abuse of young boys by UN peace keeping forces from Sri Lanka” does not help to sustain the reasonableness of the Board’s general conclusion. Again, the real issue is whether such violence is a serious violation of a fundamental human right for a Convention ground and the Board’s analysis in this regard is perfunctory and biased.

[35] The fact that the applicant “is a married 30 year old not an under 18 year old, single female” has strongly influenced the dismissal of this claim. The Court is also appalled by certain gratuitous statements of the Board, such as “rape is not the motive for criminal violence against women”, “[g]ender is not a variable in such a calculation” (in the case of kidnapped women who are raped), ““genderless” is a rather meaningless word”, and “the perpetrators of rape in Haiti…[are] mostly poor, young, uneducated, males”. Such a stereotypical view further confirms that the Board member did not have an open mind or otherwise suggests a pernicious form of bias which severely taints the reasonableness of the result.

[36] In light of Canadian law and the evidence before the Board, the conclusion that as a Haitian woman, the applicant does not have reasonable fear of persecution because of her membership in that group is unreasonable. Had the Board accepted that a risk of rape is grounded in the applicant’s membership in a particular social group, then the inquiry should have resulted in a determination of whether there is “more than a mere possibility” that the applicant risks suffering this harm in Haiti. The particular circumstances and situation of the applicant in the case of return to Haiti have not been thoroughly considered and analyzed. The next step of the failed analysis would have been to determine whether in the alleged absence of male protection in her particular case, adequate state protection is available to the applicant.

[37] The application is allowed and the impugned decision is set aside. There should be a new hearing and redetermination by a different panel of the Board in accordance with the guidance given by the Court and the following directions.

[38] The impugned decision was made on May 25, 2010, that is only four months after the earthquake of January 12, 2010 in Haiti. Before this Court, the applicant alleges that “[t]here is a rape epidemic in Haiti, exacerbated by the earthquake”. It would appear that since the earthquake, some 1.5 million persons have been displaced and are living in close proximity in camps or elsewhere in extreme conditions and without adequate protection, as the case may be. Considering that fear of persecution is forward-looking, the Court expects that there will be a complete and objective evaluation of the most up-t

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 20525:2 · paragraphs 44-45

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `165e36d5baee37826251043052025609d0feaafdbe1540e13ee7ddebe1d830f8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20525:2:subtheme:1 · paragraphs 44-45

- Raw key terms: `hearing, reasons, accordance, adjuges, applicant, application, aside, back`
- Display key terms: `hearing, accordance, adjuges, aside, back`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: hearing, accordance, adjuges, aside, back Operative outcome context: The application for judicial review is granted. Evidence spans paragraphs 44-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4969084` offsets `425-433`; context: No question is certified.
- Evidence: `disposition` cue `granted` at chunk `4969084` offsets `139-146`; context: The application for judicial review is granted.

#### Section text

JUDGMENT
THE COURT ADJUGES AND ORDERS:
1. The application for judicial review is granted.
2. The decision made on May 25, 2010 by the Board is set aside and the applicant’s claim is referred back for a new hearing and redetermination by a different panel of the Board, in accordance with the reasons for judgment and the directions issued by the Court in same.
3. No question is certified.
“Luc Martineau”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-3623-10
STYLE OF CAUSE: DULEINE JOSILE v. MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Ottawa, Ontario
DATE OF HEARING: December 8, 2010
REASONS FOR 

## 20525:3 · paragraphs 46-46

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4673bf003af54c53b7670d426fcc9097b77a1bcdf6d81b70fcab6344487d7f5d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20525:3:subtheme:1 · paragraphs 46-46

- Raw key terms: `appearances, applicant, attorney, canada, dated, deputy, general, helene`
- Display key terms: `dated, deputy, helene`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: dated, deputy, helene No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 46-46. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT: MARTINEAU J.
DATED: January 17, 2011
APPEARANCES:
Russell L. Kaplan
FOR THE APPLICANT
Helene Robertson
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Kaplan Immigration Law Office
Ottawa, Ontario
FOR THE APPLICANT
Myles J. Kirvan
Deputy Attorney General of Canada
Ottawa, Ontario
FOR THE RESPONDENT
