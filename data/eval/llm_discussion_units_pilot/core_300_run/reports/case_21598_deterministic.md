# Discussion Units: case 21598

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **28**
- Continuity pairs: **27**
- Discussion Units: **1**
- Paragraph source hashes: **28**
- Sub-themes: **7**

## 21598:1 · paragraphs 0-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `465ca97c9704209fd86476b1594f88983201f0601f25c302ae325be06e2b1fcb`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21598:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `applicant, applicants, board, elmi, principle, sahra, shukri, adam`
- Display key terms: `elmi, principle, sahra, shukri, adam`
- Argument roles: `evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, reasoning_application Display terms: elmi, principle, sahra, shukri, adam Rule/authority context: [1] This is an application pursuant to section 72(1) of the Immigration and Refugee Protection Act, S. Application context: The Board relied on a number of inconsistencies in their testimony to find the evidence not credible and, therefore, based on a complete failure to establish identity, the Board found the Applicants not to be from Somali | [3] Although the Board also voiced a number of other overwhelming credibility concerns and found the Principle Applicant did not demonstrate that she had a genuine subjective fear of persecution, the Board clearly stated Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `5013660` offsets `347-362`; context: The Board determined that the Applicants, Sahra Shukri Elmi (the Principle Applicant) and her two children are not Convention refugees nor are they persons in need of protection within the meaning of sections 96 and 97 of IRPA.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5013660` offsets `27-38`; context: [1] This is an application pursuant to section 72(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `evidence_fact` cue `evidence` at chunk `5013661` offsets `278-286`; context: Elmi proffered no documentary evidence indicating she is Somali and claimed to be unable to attain any such evidence.
- Evidence: `reasoning_application` cue `therefore` at chunk `5013661` offsets `726-735`; context: The Board relied on a number of inconsistencies in their testimony to find the evidence not credible and, therefore, based on a complete failure to establish identity, the Board found the Applicants not to be from Somalia.
- Evidence: `reasoning_application` cue `because` at chunk `5013662` offsets `267-274`; context: [3] Although the Board also voiced a number of other overwhelming credibility concerns and found the Principle Applicant did not demonstrate that she had a genuine subjective fear of persecution, the Board clearly stated, twice, that the claim was rejected primarily because the Principle Applicant was unable to establish her identity.

#### 21598:1:subtheme:2 · paragraphs 4-6

- Raw key terms: `applicants, assessment, board, canada, fear, persecution, protection, refugee`
- Display key terms: `assessment, fear, persecution, protection, refugee`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: assessment, fear, persecution, protection, refugee Application context: It follows that where a Board errs in assessing a claimant’s identity and therefore does not undertake an objective risk assessment, that error alone may constitute sufficient grounds for having an applicant’s refugee cl Evidence spans paragraphs 4-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5013663` offsets `1321-1326`; context: Because establishing identity is so fundamental to properly assessing a claim for protection, and because the Board’s reasons clearly state identity to have been the determinative issue, there is no need to consider the Board’s other credibility findings, which may or may not have been reasonably open to the Board.
- Evidence: `reasoning_application` cue `therefore` at chunk `5013663` offsets `671-680`; context: It follows that where a Board errs in assessing a claimant’s identity and therefore does not undertake an objective risk assessment, that error alone may constitute sufficient grounds for having an applicant’s refugee claim reassessed.

#### 21598:1:subtheme:3 · paragraphs 7-13

- Raw key terms: `elmi, adan, house, board, hearing, somalia, clay, family`
- Display key terms: `elmi, adan, house, hearing, somalia, clay, family`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: elmi, adan, house, hearing, somalia, clay, family Application context: Elmi testified that she did not leave Somalia at that time because there was not enough money for her to leave. Evidence spans paragraphs 7-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5013666` offsets `840-847`; context: Similarly, she has had no contact with her parents, does not know whether they returned to Somalia or not, and does not know how to contact them.
- Evidence: `reasoning_application` cue `because` at chunk `5013666` offsets `572-579`; context: Elmi testified that she did not leave Somalia at that time because there was not enough money for her to leave.
- Evidence: `evidence_fact` cue `testimony` at chunk `5013667` offsets `137-146`; context: Elmi presented no documents confirming her identity or citizenship; her counsel made clear to the Board that the testimony of Mr.
- Evidence: `evidence_fact` cue `testimony` at chunk `5013669` offsets `16-25`; context: Adan’s testimony largely confirmed the facts as presented by Ms.
- Evidence: `counterargument_limitation` cue `however` at chunk `5013672` offsets `80-87`; context: Elmi’s house was made out of brick; however, the transcript of the hearing suggests there may have been trouble with the translation as Mr.

#### 21598:1:subtheme:4 · paragraphs 14-16

- Raw key terms: `adan, elmi, respect, testified, accept, acceptable, accidentally, accordance`
- Display key terms: `adan, elmi, respect, testified, accept, acceptable, accidentally, accordance`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: adan, elmi, respect, testified, accept, acceptable, accidentally, accordance Rule/authority context: DECISION UNDER REVIEW Evidence spans paragraphs 14-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5013673` offsets `80-87`; context: Adan said that he was uncertain whether his house was bigger than Ms.
- Evidence: `governing_rule` cue `UNDER` at chunk `5013674` offsets `102-107`; context: DECISION UNDER REVIEW
- Evidence: `evidence_fact` cue `evidence` at chunk `5013675` offsets `1067-1075`; context: While I can accept that Somalia may not be issuing any formal documents, no documentary evidence of her existence in Somalia for 26 years was provided.

#### 21598:1:subtheme:5 · paragraphs 17-22

- Raw key terms: `court, credibility, standard, analysis, board, canada, clear, decision`
- Display key terms: `credibility, standard, analysis, clear`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: credibility, standard, analysis, clear Rule/authority context: I have other reasons to doubt the credibility of the principal claimant thereby adding to my findings them not to be refugees under the IRPA. | ANALYSIS Standard of Review Application context: Elmi were never neighbours in Somalia: I find the testimony of the witness and the principal claimant inconsistent as the principal claimant testified her house in Somalia was green and the witness testified it was blue. | (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subj Operative outcome context: To put it simply, this application for judicial review will be granted only if the Board’s conclusion was not open to it as a matter of fact or law. Evidence spans paragraphs 17-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5013676` offsets `98-103`; context: [17] At the hearing, the Board Member made clear that, among other things, identity was a primary issue to be addressed.
- Evidence: `evidence_fact` cue `evidence` at chunk `5013676` offsets `210-218`; context: However, very little was said to the Principle Applicant about the dearth of documentary evidence; both the Board Member and counsel appeared to be in agreement that Ms.
- Evidence: `governing_rule` cue `under` at chunk `5013676` offsets `1306-1311`; context: I have other reasons to doubt the credibility of the principal claimant thereby adding to my findings them not to be refugees under the IRPA.
- Evidence: `reasoning_application` cue `I find` at chunk `5013676` offsets `537-543`; context: Elmi were never neighbours in Somalia:
I find the testimony of the witness and the principal claimant inconsistent as the principal claimant testified her house in Somalia was green and the witness testified it was blue.
- Evidence: `counterargument_limitation` cue `However` at chunk `5013676` offsets `121-128`; context: However, very little was said to the Principle Applicant about the dearth of documentary evidence; both the Board Member and counsel appeared to be in agreement that Ms.
- Evidence: `issue` cue `whether` at chunk `5013677` offsets `1726-1733`; context: The Refugee Protection Division must take into account, with respect to the credibility of a claimant, whether the claimant possesses acceptable documentation establishing identity, and if not, whether they have provided a reasonable explanation for the lack of documentation or have taken reasonable steps to obtain the documentation.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `5013677` offsets `3873-3891`; context: ANALYSIS
Standard of Review
- Evidence: `reasoning_application` cue `because` at chunk `5013677` offsets `1147-1154`; context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
- Evidence: `governing_rule` cue `standard of review` at chunk `5013679` offsets `168-186`; context: [20] In light of the Supreme Court’s decision in Dunsmuir, it is clear that the standard of patent unreasonableness has now been abandoned and that courts conducting a standard of review analysis must now focus on two standards, those of correctness and reasonableness.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5013680` offsets `9-22`; context: [21] The jurisprudence is clear in stating that the Board's credibility analysis is central to its role as trier of fact and that, accordingly, its findings in this regard should be given significant deference.
- Evidence: `reasoning_application` cue `accordingly` at chunk `5013680` offsets `131-142`; context: [21] The jurisprudence is clear in stating that the Board's credibility analysis is central to its role as trier of fact and that, accordingly, its findings in this regard should be given significant deference.
- Evidence: `disposition` cue `granted` at chunk `5013680` offsets `706-713`; context: To put it simply, this application for judicial review will be granted only if the Board’s conclusion was not open to it as a matter of fact or law.
- Evidence: `evidence_fact` cue `evidence` at chunk `5013681` offsets `225-233`; context: Further, the Board reasonably determined there to be insufficient documentary evidence to affirm the national identity of the Applicants.
- Evidence: `counterargument_limitation` cue `However` at chunk `5013681` offsets `285-292`; context: However, this Court has held in the past that section 106 of the IRPA recognizes the difficulty in proving national identity with the usual documentation from countries, such as Somalia, that have unstable civil administration (Shafi v.

#### 21598:1:subtheme:6 · paragraphs 23-25

- Raw key terms: `board, evidence, adan, elmi, forward, immigration, inconsistencies, microscopic`
- Display key terms: `adan, elmi, forward, inconsistencies, microscopic`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: adan, elmi, forward, inconsistencies, microscopic Application context: [25] After extensively reviewing the record before the Board and the transcript of the hearing and after hearing the oral submissions, I find the Board’s treatment of the testimonial evidence of Ms. Evidence spans paragraphs 23-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5013682` offsets `425-433`; context: The question, then, is whether the evidence proffered reasonably supports the Board’s decision.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5013682` offsets `71-80`; context: [23] In the cases cited above, immigration officers erred by rejecting affidavit evidence put forward to affirm a claimant’s national identity.
- Evidence: `evidence_fact` cue `evidence` at chunk `5013683` offsets `180-188`; context: [24] It is well settled that while the Board’s task is a difficult one, it should not be over-vigilant in searching out inconsistencies or be microscopic in its examination of the evidence, particularly where persons testify through an interpreter; the Board will often slip into error if it overzealously seeks out instances of contradiction in an applicant’s testimony (Attakora v.
- Evidence: `evidence_fact` cue `record` at chunk `5013684` offsets `37-43`; context: [25] After extensively reviewing the record before the Board and the transcript of the hearing and after hearing the oral submissions, I find the Board’s treatment of the testimonial evidence of Ms.
- Evidence: `reasoning_application` cue `I find` at chunk `5013684` offsets `135-141`; context: [25] After extensively reviewing the record before the Board and the transcript of the hearing and after hearing the oral submissions, I find the Board’s treatment of the testimonial evidence of Ms.

#### 21598:1:subtheme:7 · paragraphs 26-27

- Raw key terms: `applicants, dated, deputy, judgment, reasons, teitelbaum, adam, adjudges`
- Display key terms: `dated, deputy, teitelbaum, adam, adjudges`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: dated, deputy, teitelbaum, adam, adjudges Application context: In effect, this conclusion, which I find was reached in error, influenced the remainder of the Board’s analysis and inquiry and also precluded the Board from conducting an objective risk assessment. Operative outcome context: JUDGMENT THIS COURT ORDERS AND ADJUDGES that this application for judicial review is allowed. Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5013685` offsets `19-26`; context: [26] Regardless of whether the remaining credibility concerns were open to the Board, the Board’s reasons clearly indicate that identity was largely determinative in rejecting the Applicants’ claims.
- Evidence: `reasoning_application` cue `I find` at chunk `5013685` offsets `234-240`; context: In effect, this conclusion, which I find was reached in error, influenced the remainder of the Board’s analysis and inquiry and also precluded the Board from conducting an objective risk assessment.
- Evidence: `disposition` cue `allowed` at chunk `5013685` offsets `609-616`; context: JUDGMENT
THIS COURT ORDERS AND ADJUDGES that this application for judicial review is allowed.

#### Section text

Elmi v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2008-06-24
Neutral citation
2008 FC 773
File numbers
IMM-4956-07
Decision Content
Date: 20080624
Docket: IMM-4956-07
Citation: 2008 FC 773
Ottawa, Ontario, June 24, 2008
PRESENT: The Honourable Max M. Teitelbaum
BETWEEN:
SAHRA SHUKRI ELMI
AMRAN HUSSEIN ADAM
SAID HUSSEIN ADAM
Applicants
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application pursuant to section 72(1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 ("IRPA") for judicial review, pursuant to section 18.1 of the Federal Courts Act, R.S.C. 1985, c. F-7, of a decision of the Immigration and Refugee Board, Refugee Protection Division (the Board), dated October 29, 2007. The Board determined that the Applicants, Sahra Shukri Elmi (the Principle Applicant) and her two children are not Convention refugees nor are they persons in need of protection within the meaning of sections 96 and 97 of IRPA.

[2] The Principle Applicant, 28-year-old Sahra Shukri Elmi (Ms. Elmi), her eight-year-old daughter Amran Hussein Adam, and her six-year-old son, Said Hussein Adam, all claim to be members of the Madiban tribe in the Medina district of Somalia. Ms. Elmi proffered no documentary evidence indicating she is Somali and claimed to be unable to attain any such evidence. Instead, she sought to convince the Board that she was genuinely from Somalia through the testimonial evidence of a witness, Mr. Adan, who was allegedly her neighbour in Medina. The two gave testimony describing their neighbourhood and homes in Somalia. The Board relied on a number of inconsistencies in their testimony to find the evidence not credible and, therefore, based on a complete failure to establish identity, the Board found the Applicants not to be from Somalia.

[3] Although the Board also voiced a number of other overwhelming credibility concerns and found the Principle Applicant did not demonstrate that she had a genuine subjective fear of persecution, the Board clearly stated, twice, that the claim was rejected primarily because the Principle Applicant was unable to establish her identity.

[4] Identity is of central importance to a refugee claim and failure to prove identity is fatal to a claim (Najam v. Canada (Minister of Citizenship and Immigration), [2004] F.C.J. No. 516 [hereinafter Najam]; Hussein v. Canada (Minister of Citizenship and Immigration), 2005 FC 1237 [hereinafter Hussein]). Where the Board finds a refugee claimant fails to prove their national identity, their analysis need not go any further (Najam, supra). That is, there is no need to assess subjective fear of persecution and clearly no basis upon which to assess a claimant’s objective risk or persecution. It follows that where a Board errs in assessing a claimant’s identity and therefore does not undertake an objective risk assessment, that error alone may constitute sufficient grounds for having an applicant’s refugee claim reassessed. I find this to have been the case here. For the reasons that follow, I find the Board’s conclusion that the Applicants are not from Somalia was not reasonably open to it as a matter of fact and law and must, therefore, order that the Applicants’ claim be sent back to be decided by a different Board member. Because establishing identity is so fundamental to properly assessing a claim for protection, and because the Board’s reasons clearly state identity to have been the determinative issue, there is no need to consider the Board’s other credibility findings, which may or may not have been reasonably open to the Board.
ISSUE

[5] Did the Board err in its assessment of the Applicants’ identities?
BACKGROUND

[6] On December 30, 2005, Ms. Elmi and her children arrived in Canada via Syria and France. They immediately sought refugee protection. All three claimed to be from the Medina district in Somalia and to fear persecution if returned to Somalia. Upon arrival, the interviewing officer noted that the Applicants were not the rightful holders of the German passports they used to travel to Canada.

[7] Civil war erupted in Somalia in early 1991. Ms. Elmi claims the war had a considerable and devastating effect on her family. A translation of Ms. Elmi’s written statement given to the Port of Entry (POE) officer indicates that Ms. Elmi feared being attacked by other tribes in Somalia. She also indicated that her father was paralyzed after being “sprayed with bullets,” that four of her brothers were killed and her sister was raped. Many of Ms. Elmi’s remaining family members fled to Ethiopia in 2003. Ms. Elmi testified that she did not leave Somalia at that time because there was not enough money for her to leave. She waited for an uncle in Dubai to arrange for her exit in 2005. Ms. Elmi has not spoken with her uncle since and does not know how to contact him. Similarly, she has had no contact with her parents, does not know whether they returned to Somalia or not, and does not know how to contact them.

[8] At the hearing, Ms. Elmi presented no documents confirming her identity or citizenship; her counsel made clear to the Board that the testimony of Mr. Adan, Ms. Elmi’s former neighbour in Somalia, would be presented in order to corroborate Ms. Elmi’s claim to be from Somalia.

[9] According to both Mr. Adan and Ms. Elmi, the two had not seen each other since 1991. As chance would have it, they met again when Mr. Adan recognized Ms. Elmi at a restaurant in Toronto.

[10] Mr. Adan’s testimony largely confirmed the facts as presented by Ms. Elmi at the hearing; the two were neighbours in Medina, their neighbourhood was near the Medina market and many mosques, Ms. Elmi’s family belonged to the Madiban tribe, her father was a shoe-maker and her mother used to cook for Mr. Adan’s family. Mr. Adan was able to remember Ms. Elmi’s parents, and Ms. Elmi was able to accurately state the names of Mr. Adan’s siblings. There are only three apparent inconsistencies in their testimony, all of which relate to their descriptions of Ms. Elmi’s house in Medina. On the basis of these inconsistencies, the Board determined that Ms. Elmi was not from Somalia.

[11] Ms. Elmi described her home in Medina as a green house built out of clay and cement with a flat corrugated metal roof. She said the house was “much smaller” than Mr. Adan’s house.

[12] Mr. Adan stated that Ms. Elmi lived in a blue house, though he later stated that he confuses the colours blue and green.

[13] Mr. Adan appears to have said that Ms. Elmi’s house was made out of brick; however, the transcript of the hearing suggests there may have been trouble with the translation as Mr. Adan struggled for the correct word to describe the materials used to build the house. Later, when the Board questioned Mr. Adan about this inconsistency, he explained that those who could not afford to use bricks would use a mixture of bricks and clay.

[14] With respect to the size of the house, Mr. Adan said that he was uncertain whether his house was bigger than Ms. Elmi’s; he stated that while the homes in the neighborhood were constructed by the same builder, some were taller or shorter than others.

[15] Both Ms. Elmi and Mr. Adan testified that Ms. Elmi’s roof was made of corrugated metal.
DECISION UNDER REVIEW

[16] The Board Member’s conclusion indicates there were two grounds for rejecting the Applicants’ claim, namely identity and credibility. With respect to identity, the relevant portion of the Board’s reasons reads as follows:
The claimants have failed to establish their identity as citizens of Somalia. The claimants produced no genuine identity documents whatsoever. The principal claimant produced a witness named Mohamed Jama Adan (witness) who accidentally met her at a restaurant in Toronto and recognized her from 15 years ago. She testified she last saw him 15 years ago, when the war started in 1991, when she was twelve and he was 30.
In accordance with section 106 of the IRPA, the claimants must provide acceptable documentation establishing identity. Failing that the claimants must provide reasonable explanation for the lack of documentation. Neither any documentation nor a reasonable explanation was provided. I was told that no documents are issued in Somalia. While I can accept that Somalia may not be issuing any formal documents, no documentary evidence of her existence in Somalia for 26 years was provided. No evidence of the children’s presence in Somalia was provided. No documentary evidence of her and her children’s departure from Somalia to Syria and then to France was provided. Only copies of fraudulent documents were provided. For these reasons I am unable to establish the identities of the claimants.

[17] At the hearing, the Board Member made clear that, among other things, identity was a primary issue to be addressed. However, very little was said to the Principle Applicant about the dearth of documentary evidence; both the Board Member and counsel appeared to be in agreement that Ms. Elmi’s claim to be from Somalia would be corroborated through her testimony and the testimony of Mr. Adan. The Board’s assessment of this testimony makes clear that the Board concluded that Mr. Adan and Ms. Elmi were never neighbours in Somalia:
I find the testimony of the witness and the principal claimant inconsistent as the principal claimant testified her house in Somalia was green and the witness testified it was blue. She testified her house was made of clay and cement but the witness testified it was made of brick. She testified her house was much smaller than that of the neighbour. The witness who was allegedly her neighbour in Somalia testified all houses were generally the same size in the neighbourhood. Even though some of this evidence matched, based on serious inconsistencies in their descriptions of the surroundings, I am not persuaded that they were neighbours. I have other reasons to doubt the credibility of the principal claimant thereby adding to my findings them not to be refugees under the IRPA.
RELEVANT STATUTORY PROVISIONS

[18] The following provisions of the IRPA are applicable in this application for judicial review:
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
106. The Refugee Protection Division must take into account, with respect to the credibility of a claimant, whether the claimant possesses acceptable documentation establishing identity, and if not, whether they have provided a reasonable explanation for the lack of documentation or have taken reasonable steps to obtain the documentation.
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
106. La Section de la protection des réfugiés prend en compte, s’agissant de crédibilité, le fait que, n’étant pas muni de papiers d’identité acceptables, le demandeur ne peut raisonnablement en justifier la raison et n’a pas pris les mesures voulues pour s’en procurer.
ANALYSIS
Standard of Review

[19] Prior to the Supreme Court of Canada’s recent decision in Dunsmuir v. New Brunswick, 2008 SCC 9 [hereinafter Dunsmuir], it was trite law that facts and credibility findings were reviewable on the now defunct patent unreasonableness standard (Nyirasuku v. Minister of Citizenship and Immigration, 2006 FC 803 at para. 28, citing Chowdhury v. Canada (Minister of Citizenship and Immigration) (2006), 287 F.T.R. 1, 2006 FC 139 at para. 12; Thavarathinam v. Canada (Minister of Citizenship and Immigration), 2003 FC 1469 (F.C.A.) at para. 10; Aguebor v. Canada (Minister of Citizenship and Immigration) (1993), 160 N.R. 315, [1993] F.C.J. No. 732 (F.C.A.) at para. 4).

[20] In light of the Supreme Court’s decision in Dunsmuir, it is clear that the standard of patent unreasonableness has now been abandoned and that courts conducting a standard of review analysis must now focus on two standards, those of correctness and reasonableness.

[21] The jurisprudence is clear in stating that the Board's credibility analysis is central to its role as trier of fact and that, accordingly, its findings in this regard should be given significant deference. This grant of deference supports a reasonableness standard of review and implies, as the Court held at paragraph 49 of Dunsmuir, that courts will give "due consideration to the determinations of decision makers" when reaching a conclusion. Accordingly, the Board’s decision will be reviewed on the standard of reasonableness with considerable deference being afforded to the Board’s factual findings and credibility determinations. To put it simply, this application for judicial review will be granted only if the Board’s conclusion was not open to it as a matter of fact or law.
Conclusion

[22] The Board correctly interpreted section 106 of IRPA as requiring refugee claimants to provide acceptable documentation establishing identity. Further, the Board reasonably determined there to be insufficient documentary evidence to affirm the national identity of the Applicants. However, this Court has held in the past that section 106 of the IRPA recognizes the difficulty in proving national identity with the usual documentation from countries, such as Somalia, that have unstable civil administration (Shafi v. Canada (Minister of Citizenship and Immigration) (2005), [2006] 1 F.C.R. 129, 2005 FC 714 at para. 27; Hussein, supra).

[23] In the cases cited above, immigration officers erred by rejecting affidavit evidence put forward to affirm a claimant’s national identity. Here, in admitting Mr. Adan’s testimony relating to Ms. Elmi’s identity, the Board implicitly (and correctly) recognized the principle that refugee claimants from countries with unstable civil administration ought to be afforded other means of proving their national identity. The question, then, is whether the evidence proffered reasonably supports the Board’s decision.

[24] It is well settled that while the Board’s task is a difficult one, it should not be over-vigilant in searching out inconsistencies or be microscopic in its examination of the evidence, particularly where persons testify through an interpreter; the Board will often slip into error if it overzealously seeks out instances of contradiction in an applicant’s testimony (Attakora v. Canada (Minister of Employment and Immigration) (1989), 99 N.R. 168, [1989] F.C.J. No. 444 (F.C.A.)).

[25] After extensively reviewing the record before the Board and the transcript of the hearing and after hearing the oral submissions, I find the Board’s treatment of the testimonial evidence of Ms. Elmi and Mr. Adan indicated an impermissibly microscopic assessment of the evidence. That is, in light of the amount of evidence put forward indicating that Ms. Elmi and Mr. Adan were in fact neighbours in Somalia, and in light of the fact that the inconsistencies noted by the Board were arguably not inconsistencies, or in any event, were comparably minor inconsistencies, I find the Board’s conclusion with regards to the national identities of the Applicants was not open to it as a matter of fact.

[26] Regardless of whether the remaining credibility concerns were open to the Board, the Board’s reasons clearly indicate that identity was largely determinative in rejecting the Applicants’ claims. In effect, this conclusion, which I find was reached in error, influenced the remainder of the Board’s analysis and inquiry and also precluded the Board from conducting an objective risk assessment. The error, therefore, was fundamental to the Board’s decision. Therefore, I must grant this application for judicial review.
JUDGMENT
THIS COURT ORDERS AND ADJUDGES that this application for judicial review is allowed. The decision of the Board, dated October 29, 2007, is set aside and the claim for refugee protection is referred to a differently constituted Board for re-determination. No question was submitted for certification.
"Max M. Teitelbaum"
Deputy Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-4956-07
STYLE OF CAUSE: Sahra Shukri Elmi, Amran Hussein Adam,
Said Hussein Adam v. The Minister of Citizenship and Immigration
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: June 11, 2008
REASONS FOR JUDGMENT
AND JUDGMENT: TEITELBAUM D.J.
DATED: June 24, 2008
APPEARANCES:
David P. Yerzy
FOR THE APPLICANTS
Gordon Lee
FOR THE RESPONDENT
SOLICITORS OF RECORD:
David P. Yerzy
Barrister & Solicitor
Toronto, Ontrio
FOR THE APPLICANTS
John H. Sims, Q.C.
Deputy Attorney General of Canada
FOR THE RESPONDENT
