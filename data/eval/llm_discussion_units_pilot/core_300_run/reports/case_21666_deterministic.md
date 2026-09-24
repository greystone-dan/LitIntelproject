# Discussion Units: case 21666

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **53**
- Continuity pairs: **52**
- Discussion Units: **7**
- Paragraph source hashes: **53**
- Sub-themes: **18**

## 21666:1 · paragraphs 0-7

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `218dfd78688c3bc2adc450a6aa3fcc86e92ae9197fa21f3424f077c0fd955315`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21666:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `applicant, canada, decision, application, reasons, applicant's, approximately, arch`
- Display key terms: `applicant's, approximately, arch`
- Argument roles: `evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, reasoning_application Display terms: applicant's, approximately, arch Rule/authority context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S. | Upon discovering that the Applicant had entered Canada, the items were seized and a warrant was issued for the Applicant's arrest on the grounds that she was inadmissible for misrepresentation pursuant to section 40(1)(a Application context: After conducting a search of the Applicant's vehicle together with another officer, Officer Emmott concluded that the Applicant would not leave Canada at the end of her stay because she was unemployed and did not have pr | This is because section 22(2) of the Act permits a person to have a dual intent when coming to Canada. Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5016969` offsets `27-38`; context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `reasoning_application` cue `because` at chunk `5016970` offsets `554-561`; context: After conducting a search of the Applicant's vehicle together with another officer, Officer Emmott concluded that the Applicant would not leave Canada at the end of her stay because she was unemployed and did not have proof of funds to support herself during her stay in Canada.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5016972` offsets `852-863`; context: Upon discovering that the Applicant had entered Canada, the items were seized and a warrant was issued for the Applicant's arrest on the grounds that she was inadmissible for misrepresentation pursuant to section 40(1)(a) of the Act.
- Evidence: `evidence_fact` cue `record` at chunk `5016973` offsets `511-517`; context: Further, the Board noted that the Applicant had a record of complying with the Act, having held student and work visas in the past and not having stayed beyond her authorized periods in the past.
- Evidence: `reasoning_application` cue `because` at chunk `5016973` offsets `366-373`; context: This is because section 22(2) of the Act permits a person to have a dual intent when coming to Canada.

#### 21666:1:subtheme:2 · paragraphs 6-7

- Raw key terms: `applicant, board, conflicting, evidence, literature, noted, officer, political`
- Display key terms: `conflicting, literature, noted, officer, political`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: conflicting, literature, noted, officer, political Application context: The Board stated as follows: Because these are items that Officer Dempsey personally inspected and seized, I prefer his statutory declaration over Ms. Evidence spans paragraphs 6-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5016974` offsets `489-496`; context: The Board noted that there was conflicting evidence from the Applicant and Officer Emmott regarding whether Officer Emmott even saw the anti-war literature.
- Evidence: `evidence_fact` cue `evidence` at chunk `5016974` offsets `432-440`; context: The Board noted that there was conflicting evidence from the Applicant and Officer Emmott regarding whether Officer Emmott even saw the anti-war literature.
- Evidence: `evidence_fact` cue `evidence` at chunk `5016975` offsets `52-60`; context: [7] The Board noted that there was also conflicting evidence between the Applicant’s oral testimony regarding the contents that were transferred to Mr.
- Evidence: `reasoning_application` cue `Because` at chunk `5016975` offsets `313-320`; context: The Board stated as follows:
Because these are items that Officer Dempsey personally inspected and seized, I prefer his statutory declaration over Ms.

#### Section text

Bodine v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2008-07-09
Neutral citation
2008 FC 848
File numbers
IMM-4736-07
Decision Content
Date: 20080709
Docket: IMM-4736-07
Citation: 2008 FC 848
Ottawa, Ontario, July 9, 2008
PRESENT: The Honourable Mr. Justice Russell
BETWEEN:
ALISON COLETTE BODINE
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT

[1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (Act) for judicial review of a decision of a member of the Immigration and Refugee Board (Board) dated October 31, 2007 (Decision) in which Ms. Bodine (the Applicant) was found inadmissible to Canada for misrepresentation.
BACKGROUND

[2] On September 10, 2007, at approximately 2:00 a.m., the Applicant, a citizen of the United States of America, attempted to enter Canada at the Peace Arch border-crossing. The Applicant stated that she was seeking entry as a visitor to stay with a friend in Canada for two or three months. The Applicant was refused entry by Canada Border Services Agency (CBSA) Officer Emmott. After conducting a search of the Applicant's vehicle together with another officer, Officer Emmott concluded that the Applicant would not leave Canada at the end of her stay because she was unemployed and did not have proof of funds to support herself during her stay in Canada. Also, she did not have documents proving her ties to the United States or proof of an address in the United States to which she would return. Further the number and nature of the items in her vehicle suggested that the Applicant was coming to Canada to live. These items included personal documents (pay stubs, journals, and old mail), sheets of return address stickers with a Vancouver address, a wooden chest, a bicycle and bicycle rack, and several bags of personal goods. Officer Emmott advised the Applicant of the reasons for her refusal into Canada and the Applicant stated that she understood the reasons provided to her. Officer Emmott also advised the Applicant that, if she wished to enter Canada as a visitor, she should have proof indicating that she would leave by the end of her authorized stay. This might include such things as proof of funds and residence in the United States, as well as goods and belongings commensurate with her trip as a visitor. The Applicant did not protest Officer Emmott's decision and agreed to voluntarily withdraw her application for entry into Canada. The Applicant returned to the United States.

[3] Later on the same morning, the Applicant's boyfriend, Mr. Andrew Barry, a Canadian citizen, met with the Applicant in the parking lot of a gas station in Blaine, Washington. The Applicant transferred a number of articles from her car to the vehicle driven by Mr. Barry. She also obtained an ATM receipt as proof of the funds in her bank account and a bank statement showing her home address in Colorado. The Applicant then proceeded to the Peace Arch border-crossing and was admitted into Canada at approximately 11:50 a.m. without being referred to secondary examination. The Officer who admitted the Applicant into Canada was not aware that the Applicant had voluntarily withdrawn her application earlier that morning or of the reasons for that withdrawal.

[4] At approximately 12:15 p.m., Mr. Barry attempted to re-enter Canada and was referred to secondary examination. A number of articles were found in his car, including: a bicycle and bicycle rack; a wooden chest containing anitwar and cannabis literature; personal file folders filled with personal information and artwork; photo albums; old letters; old bills; unopened letters; several notebooks; old books; women's clothing and shoes; a certificate of achievement for a course that was completed; and the Applicant's expired passport and expired driver's license. Some of these items were distributed amongst two black bags, two red bags and a beige bag. Upon discovering that the Applicant had entered Canada, the items were seized and a warrant was issued for the Applicant's arrest on the grounds that she was inadmissible for misrepresentation pursuant to section 40(1)(a) of the Act. On September 13, 2007, the Applicant returned to the Peace Arch border-crossing to collect the belongings that had been seized, whereupon she was arrested. Inadmissibility hearings pertaining to this case were held on September 17, 2007 and October 31, 2007. The Board issued its Decision on inadmissibility on October 31, 2007. This is the Decision under review in this application.
DECISION UNDER REVIEW

[5] In its reasons, the Board was clear that its Decision did not involve Officer Emmett's decision to deny the Applicant entry into Canada, although the Board did state that it did not agree with that decision. The Board said it would not be improper of the Applicant to have been considering permanently living in Canada even though entering as a visitor. This is because section 22(2) of the Act permits a person to have a dual intent when coming to Canada. Further, the Board noted that the Applicant had a record of complying with the Act, having held student and work visas in the past and not having stayed beyond her authorized periods in the past.

[6] The Board also noted that the hearing was not about the Applicant's political opinion or affiliations. The Applicant was of the view that Officer Emmott's decision to deny her entry was influenced by the antiwar literature found in her car. The Board noted that this was the Applicant's impression of her interaction with Officer Emmott; it was not the Officer's recall of the events. The Board noted that there was conflicting evidence from the Applicant and Officer Emmott regarding whether Officer Emmott even saw the anti-war literature.

[7] The Board noted that there was also conflicting evidence between the Applicant’s oral testimony regarding the contents that were transferred to Mr. Barry's car and the items listed in the Statutory Declaration given by CBSA Officer Dempsey, who had inspected Mr. Barry's vehicle. The Board stated as follows:
Because these are items that Officer Dempsey personally inspected and seized, I prefer his statutory declaration over Ms. Bodine's oral testimony. Ms. Bodine attempted to minimize the significance of the transfer to Mr. Barry's car. She testified that only Mr. Barry's belongings and the political literature were moved. But in fact Mr. Barry's trunk contained many of Ms. Bodine's own possessions, including clothing and personal documents, and these were not just inadvertently in the chest but also in one of the backpacks.

## 21666:2 · paragraphs 8-8

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f6f1491dd96bd278a821706b8cf58541d21a3a8c782a4990383af2069c74dceb`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21666:2:subtheme:1 · paragraphs 8-8

- Raw key terms: `account, address, admission, balance, board, bodine, border, bringing`
- Display key terms: `account, address, admission, balance, bodine, border, bringing`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: account, address, admission, balance, bodine, border, bringing No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 8-8. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

[8] This led the Board to the following conclusions:
I draw two conclusions: First, that Ms. Bodine unburdened herself of the bulk of the items from her car to create the impression to border officials that she was bringing into Canada no more than what she would need for a short sojourn in Canada, once again, in order to address Officer Emmett's [sic] concerns. [The Board also noted that [i]n order to address two of Officer Emmett's [sic] concerns, Ms. Bodine obtained an ATM receipt showing her account balance and a statement showing her home address in Colorado.] Second, at this hearing Ms. Bodine wanted to create the impression that transferring the bulk of the items was not a calculated act; at least, it was only calculated in respect of the political literature that she felt had hindered her admission previously.

## 21666:3 · paragraphs 9-13

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2e16e8ea5dcf6fa06e44e9f20c6f273fb677ba91281b7cf9b02a4746f70975cb`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21666:3:subtheme:1 · paragraphs 9-10

- Raw key terms: `board, misrepresentation, officer, words, actually, applicant, argument, asked`
- Display key terms: `misrepresentation, officer, words, actually, argument, asked`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: misrepresentation, officer, words, actually, argument, asked Application context: because she was displaying only a minimum of personal effects. Evidence spans paragraphs 9-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5016977` offsets `29-36`; context: [9] The Board then turned to whether there was a misrepresentation in law and noted that “[t]here was considerable argument about whether and to what degree Ms.
- Evidence: `evidence_fact` cue `found that` at chunk `5016978` offsets `15-25`; context: [10] The Board found that the Applicant had indirectly withheld information or made a direct misrepresentation, noting that when she entered Canada she “was not asked.
- Evidence: `reasoning_application` cue `because` at chunk `5016978` offsets `233-240`; context: because she was displaying only a minimum of personal effects.

#### 21666:3:subtheme:2 · paragraphs 11-13

- Raw key terms: `applicant, application, board, information, judicial, administration, admissible, admitted`
- Display key terms: `information, judicial, administration, admissible, admitted`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: information, judicial, administration, admissible, admitted Position/evidence statements: [12] As part of her Application Record, the Applicant has submitted a personal affidavit that contains information that was not part of the record before the Board. Application context: Because the information contained in the Applicant’s affidavit was not before the Board, it does not properly form part of the record on this judicial review and, as such, will not be considered on this application. Operative outcome context: That application was dismissed by this Court in a decision dated November 16, 2007. Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5016979` offsets `218-225`; context: [11] Finally, the Board concluded that the misrepresentation induced, or could have induced, an error in the administration of the Act, stating that “[i]f one withholds or misrepresents information that is relevant to whether or not one is admitted to Canada, then it creates the potential for an error in the administration of the Act; that is, the potential for admitting someone who may not be admissible.
- Evidence: `disposition` cue `dismissed` at chunk `5016979` offsets `662-671`; context: That application was dismissed by this Court in a decision dated November 16, 2007.
- Evidence: `issue` cue `ISSUES` at chunk `5016980` offsets `5-11`; context: [11]
ISSUES
Preliminary Issue
- Evidence: `party_position` cue `submitted` at chunk `5016981` offsets `58-67`; context: [12] As part of her Application Record, the Applicant has submitted a personal affidavit that contains information that was not part of the record before the Board.
- Evidence: `evidence_fact` cue `Record` at chunk `5016981` offsets `32-38`; context: [12] As part of her Application Record, the Applicant has submitted a personal affidavit that contains information that was not part of the record before the Board.
- Evidence: `reasoning_application` cue `Because` at chunk `5016981` offsets `382-389`; context: Because the information contained in the Applicant’s affidavit was not before the Board, it does not properly form part of the record on this judicial review and, as such, will not be considered on this application.

#### Section text

[9] The Board then turned to whether there was a misrepresentation in law and noted that “[t]here was considerable argument about whether and to what degree Ms. Bodine owed a duty of candour, in other words, a duty to spontaneously disclose to the border officer that she had been refused entry earlier that day.” The Board concluded that it was unnecessary to make a determination on that point.

[10] The Board found that the Applicant had indirectly withheld information or made a direct misrepresentation, noting that when she entered Canada she “was not asked...about the quantity of belongings she was bringing into Canada...because she was displaying only a minimum of personal effects.” Thus, the Applicant “was not asked because...she had transferred most of her belongings to Mr. Barry's car.” The Board held that “[t]he purpose of doing so was unquestionably to mislead the examining officer into believing she was bringing into Canada less than she actually was.” The Board found that this misrepresentation was material because, “[b]y removing the bulk of the belongings, [the Applicant] foreclosed or averted further inquiries, or in other words, she cut off an avenue of investigation for the officer.”

[11] Finally, the Board concluded that the misrepresentation induced, or could have induced, an error in the administration of the Act, stating that “[i]f one withholds or misrepresents information that is relevant to whether or not one is admitted to Canada, then it creates the potential for an error in the administration of the Act; that is, the potential for admitting someone who may not be admissible.” Thus, the Board held that all of the elements of misrepresentation had been established and, consequently, an exclusion order was issued against the Applicant. The Applicant sought a judicial stay of the removal order against her. That application was dismissed by this Court in a decision dated November 16, 2007.

[11]
ISSUES
Preliminary Issue

[12] As part of her Application Record, the Applicant has submitted a personal affidavit that contains information that was not part of the record before the Board. It is a well-recognized principle that, apart from a few recognized exceptions that are not present in this case, an application for judicial review involves a review of the record before the original decision-maker. Because the information contained in the Applicant’s affidavit was not before the Board, it does not properly form part of the record on this judicial review and, as such, will not be considered on this application.

## 21666:4 · paragraphs 14-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4646c462c1950d9b8160647e9f967e9b657d5033f2c39f2ef0b8226680600bf2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21666:4:subtheme:1 · paragraphs 14-14

- Raw key terms: `applicant, applicant's, barry's, board, brought, canada, coming, consideration`
- Display key terms: `applicant's, barry's, brought, coming, consideration`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: applicant's, barry's, brought, coming, consideration No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 14-14. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

[13] The Applicant poses the following questions for consideration by the Court:
1. Was the Board’s decision patently unreasonable?
2. Did the Applicant have a positive obligation to spontaneously inform an officer at the port of entry about all the goods coming into Canada for the purposes of her visit?
3. If such an obligation exists, did the Member make a finding that the goods in Mr. Barry's vehicle were being brought into Canada for the purposes of the Applicant's visit?
STATUTORY FRAMEWORK

## 21666:5 · paragraphs 15-21

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `079c3ebfd34eae0879e14b9dbab28190b73a1e7d45e2918bca47af94049402ad`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21666:5:subtheme:1 · paragraphs 15-16

- Raw key terms: `canada, having, review, accueilli, administration, alin, allow, although`
- Display key terms: `having, review, accueilli, administration, alin, allow, although`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, reasoning_application Display terms: having, review, accueilli, administration, alin, allow, although Rule/authority context: (1) Every foreign national, other than a foreign national referred to in section 19, who seeks to enter or remain in Canada must establish, (a) to become a permanent resident, that they hold the visa or other document re Application context: New Brunswick, 2008 SCC 9, the Supreme Court of Canada recognized that, although the reasonableness simpliciter and patent unreasonableness standards are theoretically different, “the analytical problems that arise in tr Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5016983` offsets `245-253`; context: (1) A person who makes an application must answer truthfully all questions put to them for the purpose of the examination and must produce a visa and all relevant evidence and documents that the officer reasonably requires.
- Evidence: `governing_rule` cue `under` at chunk `5016983` offsets `537-542`; context: (1) Every foreign national, other than a foreign national referred to in section 19, who seeks to enter or remain in Canada must establish,
(a) to become a permanent resident, that they hold the visa or other document required under the regulations and have come to Canada in order to establish permanent residence; and
(b) to become a temporary resident, that they hold the visa or other document required under the regulations and will leave Canada by the end of the period authorized for their stay.
- Evidence: `reasoning_application` cue `apply` at chunk `5016984` offsets `258-263`; context: New Brunswick, 2008 SCC 9, the Supreme Court of Canada recognized that, although the reasonableness simpliciter and patent unreasonableness standards are theoretically different, “the analytical problems that arise in trying to apply the different standards undercut any conceptual usefulness created by the inherently greater flexibility of having multiple standards of review” (para.
- Evidence: `counterargument_limitation` cue `although` at chunk `5016984` offsets `102-110`; context: New Brunswick, 2008 SCC 9, the Supreme Court of Canada recognized that, although the reasonableness simpliciter and patent unreasonableness standards are theoretically different, “the analytical problems that arise in trying to apply the different standards undercut any conceptual usefulness created by the inherently greater flexibility of having multiple standards of review” (para.

#### 21666:5:subtheme:2 · paragraphs 17-18

- Raw key terms: `analysis, dunsmuir, standard, well-settled, acceptable, adopt, applicable, applicant`
- Display key terms: `analysis, dunsmuir, standard, well-settled, acceptable, adopt, applicable`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: analysis, dunsmuir, standard, well-settled, acceptable, adopt, applicable Rule/authority context: [16] The Supreme Court of Canada in Dunsmuir also held that a standard of review analysis need not be conducted in every instance. Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5016985` offsets `198-206`; context: Instead, where the standard of review applicable to the particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review.
- Evidence: `governing_rule` cue `standard of review` at chunk `5016985` offsets `62-80`; context: [16] The Supreme Court of Canada in Dunsmuir also held that a standard of review analysis need not be conducted in every instance.
- Evidence: `issue` cue `whether` at chunk `5016986` offsets `614-621`; context: In light of Dunsmuir, my analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process” and also with whether the Decision “falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law”(Dunsmuir at para.
- Evidence: `evidence_fact` cue `evidence` at chunk `5016986` offsets `97-105`; context: [17] In the case before me, the Applicant challenges the Board’s Decision on the ground that the evidence was not sufficient to support an inference either that the majority of the items in Mr.

#### 21666:5:subtheme:3 · paragraphs 19-21

- Raw key terms: `board, applicant, barry, belongings, items, second, transferred, according`
- Display key terms: `barry, belongings, items, second, transferred, according`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: barry, belongings, items, second, transferred, according Position/evidence statements: [19] The Applicant argues that there was insufficient evidence to support the inference that the majority of the items transferred to Mr. Rule/authority context: Did the Board err in concluding that the Applicant made either a direct or indirect misrepresentation so that she was inadmissible pursuant to section 40 of the Act? Application context: Because these are items that Officer Dempsey personally inspected and seized, I prefer his statutory declaration over Ms. Evidence spans paragraphs 19-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5016987` offsets `16-21`; context: [18] The second issue raised by the Applicant regarding the obligation of candour is, in my view, a question of pure law.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5016987` offsets `455-466`; context: Did the Board err in concluding that the Applicant made either a direct or indirect misrepresentation so that she was inadmissible pursuant to section 40 of the Act?
- Evidence: `party_position` cue `argues` at chunk `5016988` offsets `19-25`; context: [19] The Applicant argues that there was insufficient evidence to support the inference that the majority of the items transferred to Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5016988` offsets `54-62`; context: [19] The Applicant argues that there was insufficient evidence to support the inference that the majority of the items transferred to Mr.
- Evidence: `evidence_fact` cue `testimony` at chunk `5016989` offsets `343-352`; context: According to her testimony, she transferred to Mr.
- Evidence: `reasoning_application` cue `Because` at chunk `5016989` offsets `1602-1609`; context: Because these are items that Officer Dempsey personally inspected and seized, I prefer his statutory declaration over Ms.

#### Section text

[14] The following provisions of the Act are applicable in these proceedings:
16. (1) A person who makes an application must answer truthfully all questions put to them for the purpose of the examination and must produce a visa and all relevant evidence and documents that the officer reasonably requires.
20. (1) Every foreign national, other than a foreign national referred to in section 19, who seeks to enter or remain in Canada must establish,
(a) to become a permanent resident, that they hold the visa or other document required under the regulations and have come to Canada in order to establish permanent residence; and
(b) to become a temporary resident, that they hold the visa or other document required under the regulations and will leave Canada by the end of the period authorized for their stay.
40. (1) A permanent resident or a foreign national is inadmissible for misrepresentation
(a) for directly or indirectly misrepresenting or withholding material facts relating to a relevant matter that induces or could induce an error in the administration of this Act;
(b) for being or having been sponsored by a person who is determined to be inadmissible for misrepresentation;
(c) on a final determination to vacate a decision to allow the claim for refugee protection by the permanent resident or the foreign national; or
(d) on ceasing to be a citizen under paragraph 10(1)(a) of the Citizenship Act, in the circumstances set out in subsection 10(2) of that Act.
16. (1) L’auteur d’une demande au titre de la présente loi doit répondre véridiquement aux questions qui lui sont posées lors du contrôle, donner les renseignements et tous éléments de preuve pertinents et présenter les visa et documents requis.
20. (1) L’étranger non visé à l’article 19 qui cherche à entrer au Canada ou à y séjourner est tenu de prouver :
a) pour devenir un résident permanent, qu’il détient les visa ou autres documents réglementaires et vient s’y établir en permanence;
b) pour devenir un résident temporaire, qu’il détient les visa ou autres documents requis par règlement et aura quitté le Canada à la fin de la période de séjour autorisée.
40. (1) Emportent interdiction de territoire pour fausses déclarations les faits suivants :
a) directement ou indirectement, faire une présentation erronée sur un fait important quant à un objet pertinent, ou une réticence sur ce fait, ce qui entraîne ou risque d’entraîner une erreur dans l’application de la présente loi;
b) être ou avoir été parrainé par un répondant dont il a été statué qu’il est interdit de territoire pour fausses déclarations;
c) l’annulation en dernier ressort de la décision ayant accueilli la demande d’asile;
d) la perte de la citoyenneté au titre de l’alinéa 10(1)a) de la Loi sur la citoyenneté dans le cas visé au paragraphe 10(2) de cette loi.
ANALYSIS
Standard of Review

[15] Recently, in Dunsmuir v. New Brunswick, 2008 SCC 9, the Supreme Court of Canada recognized that, although the reasonableness simpliciter and patent unreasonableness standards are theoretically different, “the analytical problems that arise in trying to apply the different standards undercut any conceptual usefulness created by the inherently greater flexibility of having multiple standards of review” (para. 44). Consequently, the Supreme Court of Canada collapsed the standards of patent unreasonableness and reasonableness simpliciter into a single form of “reasonableness” review.

[16] The Supreme Court of Canada in Dunsmuir also held that a standard of review analysis need not be conducted in every instance. Instead, where the standard of review applicable to the particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review. Only where this search proves fruitless must a reviewing court undertake a consideration of the four factors comprising the standard of review analysis.

[17] In the case before me, the Applicant challenges the Board’s Decision on the ground that the evidence was not sufficient to support an inference either that the majority of the items in Mr. Barry's vehicle belonged to the Applicant, nor that the items transferred represented the "bulk" of her belongings. Prior to Dunsmuir, it was well-settled that the Board's findings of fact should be reviewed on a patent unreasonableness standard. In light of Dunsmuir, my analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process” and also with whether the Decision “falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law”(Dunsmuir at para. 47).

[18] The second issue raised by the Applicant regarding the obligation of candour is, in my view, a question of pure law. Following Dunsmuir, this issue is reviewable on a standard of correctness. Further, as the Applicant suggests, this question is one of general importance, which also suggests a correctness standard.
1. Did the Board err in concluding that the Applicant made either a direct or indirect misrepresentation so that she was inadmissible pursuant to section 40 of the Act?

[19] The Applicant argues that there was insufficient evidence to support the inference that the majority of the items transferred to Mr. Barry’s vehicle belonged to her, or that the items transferred represented the “bulk” of her belongings. Thus, the Applicant argues that the Board’s findings to this effect were unreasonable.

[20] The pertinent passages of the Board’s Decision occur at pages 4 and 5:
…According to Ms. Bodine, she gave Mr. Barry his belongings that had been in her car, including the bicycle. She also gave him the chest that primarily contained the antiwar literature that Ms. Bodine felt caused her to be turned away at the border. According to her testimony, she transferred to Mr. Barry’s car only things belonging to him and that when she approached the border the second time, she had with her only her belongings, her personal belongings, including a backpack and some other bags. She admitted that she inadvertently left a folder full of personal documents in the chest.
The Minister presented in a post-hearing letter a receipt for the seized goods, those seized from Mr. Barry’s car, indicating that seized from Mr. Barry was a bike, a bike rack, helmet, wooden chest, two black bags, two red bags and a beige bag. Officer Dempsey, who inspected Mr. Barry’s car, stated in a statutory declaration that the trunk of Mr. Barry’s car contained several backpacks and a chest.
The trunk contained several backpacks and a large chest that contained goods such as several photo albums, old letters, old bills, unopened letters, several notebooks with notes, many old books, women’s clothing, women’s shoes, a certificate of achievement for a course that was completed, personal file folders filled with personal information, artwork. Political and cannabis literature was found within the contents. Inside of the of the backpacks was an expired passport of a woman, as well as other picture identification.
Because these are items that Officer Dempsey personally inspected and seized, I prefer his statutory declaration over Ms. Bodine’s oral testimony. Ms. Bodine attempted to minimize the significance of the transfer to Mr. Barry’s car. She testified that only Mr. Barry’s belongings and the political literature were moved. But in fact Mr. Barry’s trunk contained many of Ms. Bodine’s own possessions, including clothing and personal documents, and these were not just inadvertently in the chest but also in one of the backpacks.

## 21666:6 · paragraphs 22-51

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `cc1be404efaf602d0ad27ad18ef1233c3229bd9cdcc8e80a2dc3640a0b731b62`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21666:6:subtheme:1 · paragraphs 22-23

- Raw key terms: `applicant, barry's, board, dempsey, evidence, inspected, items, officer`
- Display key terms: `barry's, dempsey, inspected, items, officer`
- Argument roles: `evidence_fact`
- Explanation: Observed roles: evidence_fact Display terms: barry's, dempsey, inspected, items, officer Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5016990` offsets `18-26`; context: [21] Based on the evidence before the Board, I am satisfied that the Board’s findings were not unreasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `5016991` offsets `59-67`; context: [22] In my view, the Board carefully considered all of the evidence before finding that the Applicant had transferred most of the belongings from her car to Mr.

#### 21666:6:subtheme:2 · paragraphs 24-33

- Raw key terms: `applicant, canada, board, items, barry's, days, attempt, barry`
- Display key terms: `items, barry's, days, attempt, barry`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: items, barry's, days, attempt, barry Position/evidence statements: [27] The Applicant also submits that the Board focused on the fact that the Applicant moved some items from her vehicle into Mr. | [28] Although the Applicant submits that the Board made no comment with respect to the change in the Applicant's reasons for coming to Canada, the Applicant herself notes that, in its reasons, the Board stated as follows Application context: The statutory declaration provided by Officer Dempsey states that “Barry said that these goods belonged to his partner and it would be easier for him to bring her goods across because she has a station wagon and all the  | Yes, because there was a warrant for your arrest after -- the Department believed you misrepresented yourself, so after the release and those events that you've already detailed, you went to get your items and they were  Operative outcome context: She also denied that any of her clothing was with Mr. | Barry's vehicle, but made no comment on the fact that the Applicant's purpose for entering Canada was different from her purpose when she was denied entry on her first attempt. Evidence spans paragraphs 24-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5016992` offsets `21-28`; context: [23] With respect to whether the items in Mr.
- Evidence: `disposition` cue `denied` at chunk `5016992` offsets `231-237`; context: She also denied that any of her clothing was with Mr.
- Evidence: `reasoning_application` cue `because` at chunk `5016993` offsets `323-330`; context: The statutory declaration provided by Officer Dempsey states that “Barry said that these goods belonged to his partner and it would be easier for him to bring her goods across because she has a station wagon and all the goods would be visible.
- Evidence: `reasoning_application` cue `because` at chunk `5016994` offsets `719-726`; context: Yes, because there was a warrant for your arrest after -- the Department believed you misrepresented yourself, so after the release and those events that you've already detailed, you went to get your items and they were released to you, correct?
- Evidence: `evidence_fact` cue `evidence` at chunk `5016995` offsets `39-47`; context: [26] I am satisfied that, based on the evidence before it, it was open to the Board to conclude that the majority of the items in Mr.
- Evidence: `reasoning_application` cue `conclude` at chunk `5016995` offsets `87-95`; context: [26] I am satisfied that, based on the evidence before it, it was open to the Board to conclude that the majority of the items in Mr.
- Evidence: `party_position` cue `submits` at chunk `5016996` offsets `24-31`; context: [27] The Applicant also submits that the Board focused on the fact that the Applicant moved some items from her vehicle into Mr.
- Evidence: `counterargument_limitation` cue `but` at chunk `5016996` offsets `146-149`; context: Barry's vehicle, but made no comment on the fact that the Applicant's purpose for entering Canada was different from her purpose when she was denied entry on her first attempt.
- Evidence: `disposition` cue `denied` at chunk `5016996` offsets `271-277`; context: Barry's vehicle, but made no comment on the fact that the Applicant's purpose for entering Canada was different from her purpose when she was denied entry on her first attempt.
- Evidence: `party_position` cue `submits` at chunk `5016997` offsets `28-35`; context: [28] Although the Applicant submits that the Board made no comment with respect to the change in the Applicant's reasons for coming to Canada, the Applicant herself notes that, in its reasons, the Board stated as follows:
In the morning, she received a call from Simon Fraser University about a teaching assistant position she had applied for.
- Evidence: `reasoning_application` cue `applied` at chunk `5016997` offsets `331-338`; context: [28] Although the Applicant submits that the Board made no comment with respect to the change in the Applicant's reasons for coming to Canada, the Applicant herself notes that, in its reasons, the Board stated as follows:
In the morning, she received a call from Simon Fraser University about a teaching assistant position she had applied for.
- Evidence: `evidence_fact` cue `evidence` at chunk `5017000` offsets `66-74`; context: [31] In my view, the Board seems to have accepted the Applicant’s evidence that her purpose for entering Canada was different on her second attempt.
- Evidence: `counterargument_limitation` cue `However` at chunk `5017000` offsets `300-307`; context: However, in my view, the lack of such a finding is not fatal to the Board’s logic.
- Evidence: `reasoning_application` cue `because` at chunk `5017001` offsets `13-20`; context: [32] This is because the Board found, and based its Decision upon the fact, that the Applicant misrepresented the amount of goods she was bringing into Canada and that this misrepresentation was material and induced, or could have induced, an error in the administration of the Act.
- Evidence: `disposition` cue `denied` at chunk `5017001` offsets `1296-1302`; context: She knew that she had been denied admission to Canada because, among other concerns, reasonable or not, she had had with her too much stuff.

#### 21666:6:subtheme:3 · paragraphs 34-36

- Raw key terms: `applicant, canada, entry, finding, obligation, positive, because, board`
- Display key terms: `entry, finding, obligation, positive, because`
- Argument roles: `issue, party_position, reasoning_application`
- Explanation: Observed roles: issue, party_position, reasoning_application Display terms: entry, finding, obligation, positive, because Position/evidence statements: [34] The Applicant argues that the Board’s finding that she had the intention to mislead the Officer was irrelevant because she did not have a positive obligation to spontaneously inform an officer at the port of entry a Application context: She withheld and/or misrepresented the personal effects she was bringing into Canada and that misrepresentation or withholding clearly could have induced an error in the administration of the Act because it deprived the  | [34] The Applicant argues that the Board’s finding that she had the intention to mislead the Officer was irrelevant because she did not have a positive obligation to spontaneously inform an officer at the port of entry a Evidence spans paragraphs 34-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5017002` offsets `891-898`; context: She withheld and/or misrepresented the personal effects she was bringing into Canada and that misrepresentation or withholding clearly could have induced an error in the administration of the Act because it deprived the officer of material facts he needed to gauge whether she would leave when she said she would.
- Evidence: `reasoning_application` cue `because` at chunk `5017002` offsets `822-829`; context: She withheld and/or misrepresented the personal effects she was bringing into Canada and that misrepresentation or withholding clearly could have induced an error in the administration of the Act because it deprived the officer of material facts he needed to gauge whether she would leave when she said she would.
- Evidence: `issue` cue `question` at chunk `5017003` offsets `450-458`; context: The Applicant argues that there was no such obligation to inform and submits that, even if there was an obligation, the Board member did not put his mind to the question of whether the items in Mr.
- Evidence: `party_position` cue `argues` at chunk `5017003` offsets `19-25`; context: [34] The Applicant argues that the Board’s finding that she had the intention to mislead the Officer was irrelevant because she did not have a positive obligation to spontaneously inform an officer at the port of entry about all the goods coming into Canada for the purposes of her visit.
- Evidence: `reasoning_application` cue `because` at chunk `5017003` offsets `116-123`; context: [34] The Applicant argues that the Board’s finding that she had the intention to mislead the Officer was irrelevant because she did not have a positive obligation to spontaneously inform an officer at the port of entry about all the goods coming into Canada for the purposes of her visit.

#### 21666:6:subtheme:4 · paragraphs 37-41

- Raw key terms: `applicant, bringing, canada, barry, border, because, belongings, either`
- Display key terms: `bringing, barry, border, because, belongings, either`
- Argument roles: `counterargument_limitation, disposition, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, issue, party_position, reasoning_application Display terms: bringing, barry, border, because, belongings, either Position/evidence statements: [36] The Respondent argues that the Applicant’s purpose in bringing her belongings into Canada and, more generally, her intentions when entering Canada, were exactly what the border services officers had to determine. | [38] Further, the Applicant argues that, on her second attempt, she neither misrepresented her intentions for entering Canada nor did she misrepresent the items she was bringing into Canada for the purpose of her visit. Application context: According to the Respondent, the Applicant cannot reasonably argue that she was entitled to cut off a possible line of investigation by border services officers because she intended to stay in Canada for only a few days. | The facts are that the Applicant was earlier denied entry (and allowed to withdraw her application) because Officer Emmott was not convinced that she would leave Canada after her authorized period of stay. Operative outcome context: The facts are that the Applicant was earlier denied entry (and allowed to withdraw her application) because Officer Emmott was not convinced that she would leave Canada after her authorized period of stay. | She knew that she had been denied admission to Canada because, among other concerns, reasonable or not, she had had with her too much stuff. Evidence spans paragraphs 37-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5017005` offsets `997-1004`; context: In order to make that determination properly, the officers needed to know the type and amount of all of the belongings that the Applicant was bringing into Canada, whether in her own car or in Mr.
- Evidence: `party_position` cue `argues` at chunk `5017005` offsets `20-26`; context: [36] The Respondent argues that the Applicant’s purpose in bringing her belongings into Canada and, more generally, her intentions when entering Canada, were exactly what the border services officers had to determine.
- Evidence: `reasoning_application` cue `because` at chunk `5017005` offsets `571-578`; context: According to the Respondent, the Applicant cannot reasonably argue that she was entitled to cut off a possible line of investigation by border services officers because she intended to stay in Canada for only a few days.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5017005` offsets `453-459`; context: According to the Respondent, the Applicant cannot reasonably argue that she was entitled to cut off a possible line of investigation by border services officers because she intended to stay in Canada for only a few days.
- Evidence: `issue` cue `whether` at chunk `5017006` offsets `702-709`; context: A border services officer’s duty entails making an assessment on whether or not a person is admissible to Canada as a visitor.
- Evidence: `party_position` cue `argues` at chunk `5017007` offsets `28-34`; context: [38] Further, the Applicant argues that, on her second attempt, she neither misrepresented her intentions for entering Canada nor did she misrepresent the items she was bringing into Canada for the purpose of her visit.
- Evidence: `reasoning_application` cue `because` at chunk `5017008` offsets `212-219`; context: The facts are that the Applicant was earlier denied entry (and allowed to withdraw her application) because Officer Emmott was not convinced that she would leave Canada after her authorized period of stay.
- Evidence: `disposition` cue `denied` at chunk `5017008` offsets `157-163`; context: The facts are that the Applicant was earlier denied entry (and allowed to withdraw her application) because Officer Emmott was not convinced that she would leave Canada after her authorized period of stay.
- Evidence: `reasoning_application` cue `because` at chunk `5017009` offsets `343-350`; context: She was not asked because she was displaying only a minimum of personal effects.
- Evidence: `disposition` cue `denied` at chunk `5017009` offsets `1348-1354`; context: She knew that she had been denied admission to Canada because, among other concerns, reasonable or not, she had had with her too much stuff.

#### 21666:6:subtheme:5 · paragraphs 42-43

- Raw key terms: `applicant, candour, circumstances, disclose, duty, information, officer, person`
- Display key terms: `candour, circumstances, disclose, duty, information, officer, person`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: candour, circumstances, disclose, duty, information, officer, person Rule/authority context: Instead, to determine whether the withholding of information constitutes a misrepresentation under the Act, it is necessary to consider the surrounding circumstances in each instance. Evidence spans paragraphs 42-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5017010` offsets `1745-1752`; context: One must look at the surrounding circumstances to decide whether the applicant has failed to comply with s.
- Evidence: `evidence_fact` cue `evidence` at chunk `5017010` offsets `113-121`; context: [41] Although the Act, or section 40 specifically, does not require spontaneous disclosure of all information or evidence, there may be an obligation to disclose information or to produce relevant evidence in certain circumstances.
- Evidence: `issue` cue `question` at chunk `5017011` offsets `187-195`; context: This case presents the question of the extent to which an applicant must disclose information when not expressly asked for that information by an examining officer.
- Evidence: `governing_rule` cue `under` at chunk `5017011` offsets `556-561`; context: Instead, to determine whether the withholding of information constitutes a misrepresentation under the Act, it is necessary to consider the surrounding circumstances in each instance.

#### 21666:6:subtheme:6 · paragraphs 44-46

- Raw key terms: `applicant, bringing, canada, entry, items, officer, transferred, address`
- Display key terms: `bringing, entry, items, officer, transferred, address`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: bringing, entry, items, officer, transferred, address Position/evidence statements: [45] The Applicant argues that the goods transferred to Mr. Rule/authority context: [43] Here, the Applicant knew or ought to have known that the amount and the kind of goods she was bringing into Canada was a relevant fact that the examining border services officer would need to know in order to assess Application context: The Applicant knew that, because of the goods she had previously attempted to bring into Canada, together with the lack of proof of funds and proof of an address in the United States, Officer Emmott had not been satisfie | Barry’s car were not brought into Canada for the purposes of her visit to Canada and, therefore, there was no obligation on her part to spontaneously disclose that Mr. Evidence spans paragraphs 44-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5017012` offsets `221-228`; context: [43] Here, the Applicant knew or ought to have known that the amount and the kind of goods she was bringing into Canada was a relevant fact that the examining border services officer would need to know in order to assess whether she was admissible under the Act.
- Evidence: `governing_rule` cue `under` at chunk `5017012` offsets `248-253`; context: [43] Here, the Applicant knew or ought to have known that the amount and the kind of goods she was bringing into Canada was a relevant fact that the examining border services officer would need to know in order to assess whether she was admissible under the Act.
- Evidence: `reasoning_application` cue `because` at chunk `5017012` offsets `288-295`; context: The Applicant knew that, because of the goods she had previously attempted to bring into Canada, together with the lack of proof of funds and proof of an address in the United States, Officer Emmott had not been satisfied that she would leave Canada at the end of the period of her authorized stay.
- Evidence: `party_position` cue `argues` at chunk `5017014` offsets `19-25`; context: [45] The Applicant argues that the goods transferred to Mr.
- Evidence: `reasoning_application` cue `therefore` at chunk `5017014` offsets `146-155`; context: Barry’s car were not brought into Canada for the purposes of her visit to Canada and, therefore, there was no obligation on her part to spontaneously disclose that Mr.

#### 21666:6:subtheme:7 · paragraphs 47-49

- Raw key terms: `applicant, canada, items, accurately, articles, barry, because, bring`
- Display key terms: `items, accurately, articles, barry, because, bring`
- Argument roles: `counterargument_limitation, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, reasoning_application Display terms: items, accurately, articles, barry, because, bring Application context: [47] On the specific facts of this case, I find there was an obligation on the part of the Applicant to fully disclose the number of articles she was bringing to Canada, since only a few hours earlier the Applicant, to h | This is indeed unfortunate because it could impact the Applicant’s life in significant ways. Evidence spans paragraphs 47-49. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5017015` offsets `757-764`; context: It is clear that the number and type of articles that the Applicant was bringing into Canada, either directly or indirectly, was a relevant fact that the examining officer needed to know in order to make a determination of whether or not the Applicant was admissible to Canada.
- Evidence: `issue` cue `whether` at chunk `5017016` offsets `421-428`; context: Only if this disclosure was made could the examining officer have properly determined whether the goods being transported by the Applicant were for the purpose of her visit, and whether or not the Applicant would leave Canada at the end of her stay.
- Evidence: `reasoning_application` cue `I find` at chunk `5017016` offsets `41-47`; context: [47] On the specific facts of this case, I find there was an obligation on the part of the Applicant to fully disclose the number of articles she was bringing to Canada, since only a few hours earlier the Applicant, to her knowledge, was refused entry because of, inter alia, the quantity and nature of the articles in her possession.
- Evidence: `reasoning_application` cue `because` at chunk `5017017` offsets `401-408`; context: This is indeed unfortunate because it could impact the Applicant’s life in significant ways.
- Evidence: `counterargument_limitation` cue `But` at chunk `5017017` offsets `467-470`; context: But the choice was the Applicant’s.

#### 21666:6:subtheme:8 · paragraphs 50-51

- Raw key terms: `reasons, alison, bodine, cause, certification, colette, counsel, court`
- Display key terms: `alison, bodine, certification, colette`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: alison, bodine, certification, colette Evidence spans paragraphs 50-51. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5017018` offsets `96-104`; context: [49] Counsel are requested to serve and file any submissions with respect to certification of a question of general importance within seven days of receipt of these Reasons for Judgment.

#### Section text

[21] Based on the evidence before the Board, I am satisfied that the Board’s findings were not unreasonable. Officer Emmott testified that, when the Applicant attempted to enter Canada the first time, she had a large wooden chest, four or five bags and a bicycle in or on her car. The Applicant testified that when she entered Canada on her second attempt, she had only one backpack, one other bag and some artwork in her car. Meanwhile, when Mr. Barry re-entered Canada shortly after the Applicant had entered, Officer Dempsey, who inspected Mr. Barry's car, found that Mr. Barry had a bicycle and bicycle rack on his car and that the trunk held several backpacks and a large chest that contained, among other things, women's clothing and shoes, identification documents in the Applicant’s name and other documents. The Applicant did not dispute the fact that she transferred several items from her car to Mr. Barry's vehicle.

[22] In my view, the Board carefully considered all of the evidence before finding that the Applicant had transferred most of the belongings from her car to Mr. Barry's car. The Board preferred the evidence provided by the Officers who had inspected the Applicant’s and Mr. Barry's vehicles and was entitled to prefer that evidence, including the statutory declaration of Officer Dempsey, over the testimonial evidence of the Applicant. In my view, the Board's conclusion that the Applicant transferred the bulk of the items in her car to Mr. Barry's vehicle is reasonable and should not be disturbed by this Court.

[23] With respect to whether the items in Mr. Barry's car belonged to the Applicant, the Applicant did not contest that the documents belonged to her, but testified that the bicycle and bicycle rack belonged to Mr. Barry. She also denied that any of her clothing was with Mr. Barry when he entered Canada.

[24] The Board’s conclusion on this point, however, is supported by Mr. Barry's statement to Officer Dempsey when he attempted to re-enter Canada. The statutory declaration provided by Officer Dempsey states that “Barry said that these goods belonged to his partner and it would be easier for him to bring her goods across because she has a station wagon and all the goods would be visible. Further questioning about the visibility of the goods resulted in Barry stating that it would be faster if he transported her goods into Canada... .”

[25] Further, when testifying about the difficulties she encountered in attempting to retrieve the items that had been seized from Mr. Barry's vehicle, the Applicant indicated that they belonged to her:
Q Mr. Barry couldn't enter Canada with your possessions and he was told that only you could come and get them?
A Yeah, he was told that he couldn't take these things into Canada with him and so they were left there at the border.
Q And they would only be released to you, which is why you had to come to receive them, correct?
A According to the receipt he was given, yes.
Q And when you did go to receive your items, they were returned to you?
A No, when I went to go receive my items, I was arrested.
Q Okay. Yes, because there was a warrant for your arrest after -- the Department believed you misrepresented yourself, so after the release and those events that you've already detailed, you went to get your items and they were released to you, correct?
A They were release to me, yeah, a week and some odd days later.
[...]
Q Okay. So the belongings were never prevented from being returned to you. Whatever could be returned to you was returned to you and the only prevention the Department did with respect to your belongings was preventing Mr. Barry from coming into Canada with it, correct?
A In my opinion, they were prevented, because I was not given any information by anyone within the CBSA of how to get my things back to me, anyone with Immigration. I was only informed and given a seizure document for my passport. I wasn't told, when I asked or attempted to contact a number of different Immigration phone numbers, that I could go get these things or how about I would get them. [emphasis added]
[Hearing Transcript, pages 62-64].

[26] I am satisfied that, based on the evidence before it, it was open to the Board to conclude that the majority of the items in Mr. Barry’s vehicle belonged to the Applicant. This finding, in my view, was not unreasonable.

[27] The Applicant also submits that the Board focused on the fact that the Applicant moved some items from her vehicle into Mr. Barry's vehicle, but made no comment on the fact that the Applicant's purpose for entering Canada was different from her purpose when she was denied entry on her first attempt. The Applicant submits that, when she entered Canada on her second attempt, she was not seeking entry for two to three months as she had been upon her initial request for entry, but that her intention was to enter Canada long enough to complete a job interview at Simon Fraser University and then return to the United States.

[28] Although the Applicant submits that the Board made no comment with respect to the change in the Applicant's reasons for coming to Canada, the Applicant herself notes that, in its reasons, the Board stated as follows:
In the morning, she received a call from Simon Fraser University about a teaching assistant position she had applied for. She decided then that she would attempt to come into Canada for a couple of days to see about the job. In order to address two of Officer Emmett's [sic] concerns, Ms. Bodine obtained an ATM receipt showing her account balance and a statement showing her home address in Colorado.

[29] The Applicant also notes that the Board said that “Ms. Bodine testified that she told the border officer that she was seeking to enter Canada for two or three days” as well as the following conclusions reached by the Board:
I draw two conclusions: First, that Ms. Bodine unburdened herself of the bulk of the items from her car to create the impression to border officials that she was bringing into Canada no more than what she would need for a short sojourn in Canada, once again, in order to address Officer Emmett's [sic] concerns.

[30] It is obvious from reading the Board’s Decision that, contrary to the Applicant's submission, the Board did make reference to the fact that the Applicant’s stated purpose for entering Canada on her second attempt was different from the first attempt. The Applicant is really saying that the Board did not make a finding that she did not intend to stay in Canada for only two or three days. The failure to make such a finding, argues the Applicant, was fatal to the Board’s logic, as the Applicant was only bringing with her the goods she required for her short sojourn in Canada, and any other items were either things that did not belong to her, or items she might use upon her return to Canada at sometime in the future.

[31] In my view, the Board seems to have accepted the Applicant’s evidence that her purpose for entering Canada was different on her second attempt. I think the Applicant is correct that the Board did not make a finding that the Applicant did not intend to stay in Canada for only two or three days. However, in my view, the lack of such a finding is not fatal to the Board’s logic.

[32] This is because the Board found, and based its Decision upon the fact, that the Applicant misrepresented the amount of goods she was bringing into Canada and that this misrepresentation was material and induced, or could have induced, an error in the administration of the Act. The Board’s findings on this point are contained in the following passages of the Board’s Decision at page 6:
Clearly in this case Ms. Bodine was not asked by the officer about the quantity of belongings she was bringing into Canada. She was not asked because she was displaying only a minimum of personal effects. She was not asked because, as I have found in fact, she had transferred most of her belongings to Mr. Barry's car. The purpose of doing so was unquestionably to mislead the examining officer into believing she was brining into Canada less than she actually was. I characterize this as either indirectly withholding information or directly misrepresenting....
[...]
In this case, seeing only a few things in Ms. Bodine's car, the border officer's interest was not piqued. This is precisely what makes Ms. Bodine's misrepresentation material. She knew that a car full of possessions would attract unwanted attention, as it had when she tried to enter earlier the same day. She knew that she had been denied admission to Canada because, among other concerns, reasonable or not, she had had with her too much stuff. By removing the bulk of the belongings, she foreclosed or averted further inquiries, or in other words, she cut off an avenue of investigation for the officer.

[33] The fact that the Applicant says she intended to stay for only a few days does not change the fact that, by transferring most of her belongings into Mr. Barry’s car, she represented to the border services officer that she was bringing in less than she actually was. Thus, regardless of any changed intention for entering Canada, and her stated change in the intended length of stay, the elements that led the Board to its finding that the Applicant made a material misrepresentation remain the same. The Applicant was found inadmissible for misrepresentation and withholding material facts relating to a relevant matter. She withheld and/or misrepresented the personal effects she was bringing into Canada and that misrepresentation or withholding clearly could have induced an error in the administration of the Act because it deprived the officer of material facts he needed to gauge whether she would leave when she said she would.
2. Did the Applicant have a positive obligation to spontaneously inform an officer at the port of entry about all the goods coming into Canada for the purposes of her visit?

[34] The Applicant argues that the Board’s finding that she had the intention to mislead the Officer was irrelevant because she did not have a positive obligation to spontaneously inform an officer at the port of entry about all the goods coming into Canada for the purposes of her visit. The Applicant argues that there was no such obligation to inform and submits that, even if there was an obligation, the Board member did not put his mind to the question of whether the items in Mr. Barry's possession were for the purposes of the Applicant's visit at the time of her applications to enter Canada. A decision on this issue, the Applicant submits, could only be made in a new hearing.

[35] The Applicant states that no such positive obligation is explicitly mentioned in the Act; nor are there any instructions or directions to that effect provided to persons seeking entry into Canada at a land border. According to the Applicant, to make a finding that there is such an obligation would require a liberal and broad interpretation of section 40 of the Act which, in view of the consequences, would be inappropriate.

[36] The Respondent argues that the Applicant’s purpose in bringing her belongings into Canada and, more generally, her intentions when entering Canada, were exactly what the border services officers had to determine. By misrepresenting how much she was bringing into Canada, argues the Respondent, the Applicant forestalled officers from asking her relevant questions about her intentions on entering Canada. According to the Respondent, the Applicant cannot reasonably argue that she was entitled to cut off a possible line of investigation by border services officers because she intended to stay in Canada for only a few days. The determination of how long the Applicant might intend to stay in Canada, argues the Respondent, was a determination that had to be made by border services officers rather than the Applicant herself. In order to make that determination properly, the officers needed to know the type and amount of all of the belongings that the Applicant was bringing into Canada, whether in her own car or in Mr. Barry’s car.

[37] With respect to the Applicant's claim that the Board failed to consider that the items in Mr. Barry’s vehicle were ones that she might use upon her return to Canada in the future, I do not find that this changes in any way the fact that the Applicant misrepresented the number of items she was bringing into Canada either for her short sojourn in Canada or for future use. Regardless of when the Applicant intended to use the items, the fact remains that, by transferring most of her belongings into Mr. Barry’s car, the Applicant represented to Canadian border services offices that she was bringing in less than she actually was. A border services officer’s duty entails making an assessment on whether or not a person is admissible to Canada as a visitor. This assessment is conducted with a view to factors such as the amount of funds the person has available to them, their ties to their home country including proof of residence, and the number and kind of goods they are transporting. The number and kind of goods the Applicant intended to bring into Canada, directly in her own car, and indirectly through the use of Mr. Barry’s car, was a material fact that the Officers needed to know in order to properly determine whether the Applicant would leave the country at the end of her authorized period of stay.

[38] Further, the Applicant argues that, on her second attempt, she neither misrepresented her intentions for entering Canada nor did she misrepresent the items she was bringing into Canada for the purpose of her visit. She states that “[e]ven if one were to accept the Member’s finding that Mr. Barry was bringing in items belonging to the Applicant, the conclusion that there was an obligation to disclose items in the possession of someone else which were not being brought in for the purposes of the visit is simply untenable.”

[39] In my view, the Applicant is asking this Court to ignore the reality of the situation in the present case. The facts are that the Applicant was earlier denied entry (and allowed to withdraw her application) because Officer Emmott was not convinced that she would leave Canada after her authorized period of stay. Some of the factors behind Officer Emmott’s refusal to admit the Applicant were the number and kinds of goods the Applicant was attempting to bring into Canada. After having been refused entry, the Applicant, either calculatedly or not, transferred her items into Mr. Barry’s vehicle so it would appear that she was bringing in fewer articles. She did so in an attempt to mitigate the examining officer’s concerns. This is clear from Mr. Barry’s statement to CBSA Officer Marcotte as recorded in Officer Marcott’s Report (Subsection 44(1) Report). According to that Report, Mr. Barry stated that “the reason the goods were transferred to his vehicle was to make it easier for Ms. Bodine to cross the border into Canada.”

[40] I agree with the Board's conclusion that, on this particular set of facts, the Applicant’s actions constitute a material misrepresentation in law. The Board, in this regard, concluded as follows:
Clearly in this case Ms. Bodine was not asked by the officer about the quantity of belongings she was bringing into Canada. She was not asked because she was displaying only a minimum of personal effects. She was not asked because, as I have found in fact, she had transferred most of her belongings to Mr. Barry's car. The purpose of doing so was unquestionably to mislead the examining officer into believing she was brining into Canada less than she actually was. I characterize this as either indirectly withholding information or directly misrepresenting....
A misrepresentation must be of a material fact. “Material” means in context relevant to that person's admission to Canada and it's very case-specific. “Material” also relates to what a person objectively knows to be relevant to the border officials.
In this case, seeing only a few things in Ms. Bodine’s car, the border officer’s interest was not piqued. This is precisely what makes Ms. Bodine’s misrepresentation material. She knew that a car full of possessions would attract unwanted attention, as it had when she tried to enter earlier the same day. She knew that she had been denied admission to Canada because, among other concerns, reasonable or not, she had had with her too much stuff. By removing the bulk of the belongings, she foreclosed or averted further inquiries, or in other words, she cut off an avenue of investigation for the officer.

[41] Although the Act, or section 40 specifically, does not require spontaneous disclosure of all information or evidence, there may be an obligation to disclose information or to produce relevant evidence in certain circumstances. Section 16(1) of the Act provides that “[a] person who makes an application must answer truthfully all questions put to them for the purpose of the examination and must answer truthfully all questions put to them for the purpose of the examination and must produce a visa and all relevant evidence and documents that the officer reasonably requires.” In Baro v. Canada (Minister of Citizenship and Immigration), 2007 FC 1299 at para. 15, the Court recognized that a foreign national seeking to enter Canada has a “duty of candour” which requires disclosure of material facts. The Court went on to state at paragraphs 15-17:
15 …Even an innocent failure to provide material information can result in a finding of inadmissibility; for example, an applicant who fails to include all of her children in her application may be inadmissible: Bickin v. Canada (Minister of Citizenship and Immigration), [2000] F.C.J. No. 1495(F.C.T.D.) (QL). An exception arises where applicants can show that they honestly and reasonably believed that they were not withholding material information: Medel v. Canada (Minister of Employment and Immigration), [1990] 2 F.C. 345, [1990] F.C.J. No. 318 (F.C.A.) (QL).
[…]
17 Of course, applicants cannot be expected to anticipate the kinds of information that immigration officials might be interested in receiving. As the IAD noted here, "there is no onus on the person to disclose all information that might possibly be relevant". One must look at the surrounding circumstances to decide whether the applicant has failed to comply with s. 40(1)(a).

[42] It is clear that a duty of candour exists and that the surrounding circumstances are important for deciding what that duty entails in any particular instance. This case presents the question of the extent to which an applicant must disclose information when not expressly asked for that information by an examining officer. I do not find that section 40 of the Act requires that a person must spontaneously disclose any fact that could possibly be relevant. Instead, to determine whether the withholding of information constitutes a misrepresentation under the Act, it is necessary to consider the surrounding circumstances in each instance.

[43] Here, the Applicant knew or ought to have known that the amount and the kind of goods she was bringing into Canada was a relevant fact that the examining border services officer would need to know in order to assess whether she was admissible under the Act. The Applicant knew that, because of the goods she had previously attempted to bring into Canada, together with the lack of proof of funds and proof of an address in the United States, Officer Emmott had not been satisfied that she would leave Canada at the end of the period of her authorized stay. Thus, she knew that the number and type of goods she was transporting were material to the determination of whether or not she was admissible to Canada. That concern had been raised with her at her first attempt at entry and, to ensure it would not be raised as a concern on her second attempt, she transferred items to Mr. Barr

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 21666:7 · paragraphs 52-52

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `91fa28f2f94c498ec7aa79b08e968d492c3dc94817d0349bf0e1f48593290b62`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21666:7:subtheme:1 · paragraphs 52-52

- Raw key terms: `appearances, applicant, attorney, canada, dated, deputy, edelmann, general`
- Display key terms: `dated, deputy, edelmann`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: dated, deputy, edelmann No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 52-52. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT: Russell, J.
DATED: July 9, 2008
APPEARANCES:
Peter Edelmann
Keith Reimer
FOR THE APPLICANT
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Peter Edelmann
Solicitor
Vancouver, B.C.
John H. Sims, Q.C.
Deputy Attorney General of Canada
FOR THE APPLICANT
FOR THE RESPONDENT
