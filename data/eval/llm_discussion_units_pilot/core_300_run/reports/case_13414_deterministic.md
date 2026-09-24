# Discussion Units: case 13414

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **19**
- Continuity pairs: **18**
- Discussion Units: **2**
- Paragraph source hashes: **19**
- Sub-themes: **6**

## 13414:1 · paragraphs 0-17

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ce1c4fa665ed245b210a9fbe9f7d1612fbd09fa79b78dabcbace59c8ce50852d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13414:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, canada, ibrahim, somalia, southern, yusra, al-shabaab, animals`
- Display key terms: `ibrahim, somalia, southern, yusra, al-shabaab, animals`
- Argument roles: `party_position`
- Explanation: Observed roles: party_position Display terms: ibrahim, somalia, southern, yusra, al-shabaab, animals Position/evidence statements: [1] Yusra Mohamed Ibrahim, the Applicant, claims to be a 21 year old Sufi-Sunni woman who is a member of the Garre clan in Somalia. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `4660971` offsets `42-48`; context: [1] Yusra Mohamed Ibrahim, the Applicant, claims to be a 21 year old Sufi-Sunni woman who is a member of the Garre clan in Somalia.

#### 13414:1:subtheme:2 · paragraphs 3-6

- Raw key terms: `applicant, appeal, evidence, money, somalia, canada, considered, credibility`
- Display key terms: `money, somalia, considered, credibility`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position Display terms: money, somalia, considered, credibility Position/evidence statements: [5] After noting its role, the RAD considered the new evidence submitted by the Applicant pursuant to subsection 110(4) of the Act, namely: (1) two Ottawa Hospital documents; (2) an affidavit from the interpreter at the  Rule/authority context: The Applicant now asks this Court, pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act], to set aside the RAD’s decision and return the matter to a different member of the RAD f | [5] After noting its role, the RAD considered the new evidence submitted by the Applicant pursuant to subsection 110(4) of the Act, namely: (1) two Ottawa Hospital documents; (2) an affidavit from the interpreter at the  Operative outcome context: The Applicant’s appeal of the RPD’s decision to the Refugee Appeal Division [RAD] of the Board was dismissed by the RAD in a decision dated April 9, 2015. Evidence spans paragraphs 3-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4660973` offsets `944-951`; context: The RAD’s Decision [4] The RAD adopted this Court’s decision in Huruglica v Canada (Citizenship and Immigration), 2014 FC 799 (at paras 54-55), [2014] 4 FCR 811, to frame its role in reviewing the RPD’s decision, stating that it would conduct its own, independent assessment of whether the Applicant was a Convention refugee or person in need of protection under section 97 of the Act, and that it also would respect the credibility or other findings of the RPD where the RPD had a particular advantage in reaching its conclusions.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4660973` offsets `457-468`; context: The Applicant now asks this Court, pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act], to set aside the RAD’s decision and return the matter to a different member of the RAD for re-determination.
- Evidence: `disposition` cue `dismissed` at chunk `4660973` offsets `366-375`; context: The Applicant’s appeal of the RPD’s decision to the Refugee Appeal Division [RAD] of the Board was dismissed by the RAD in a decision dated April 9, 2015.
- Evidence: `party_position` cue `submitted` at chunk `4660974` offsets `63-72`; context: [5] After noting its role, the RAD considered the new evidence submitted by the Applicant pursuant to subsection 110(4) of the Act, namely: (1) two Ottawa Hospital documents; (2) an affidavit from the interpreter at the Applicant’s RPD hearing confirming that “bessa” means money in Garreh; and (3) an internet article about Somalian currency.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660974` offsets `54-62`; context: [5] After noting its role, the RAD considered the new evidence submitted by the Applicant pursuant to subsection 110(4) of the Act, namely: (1) two Ottawa Hospital documents; (2) an affidavit from the interpreter at the Applicant’s RPD hearing confirming that “bessa” means money in Garreh; and (3) an internet article about Somalian currency.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4660974` offsets `90-101`; context: [5] After noting its role, the RAD considered the new evidence submitted by the Applicant pursuant to subsection 110(4) of the Act, namely: (1) two Ottawa Hospital documents; (2) an affidavit from the interpreter at the Applicant’s RPD hearing confirming that “bessa” means money in Garreh; and (3) an internet article about Somalian currency.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660975` offsets `138-146`; context: [6] Turning next to the merits of the appeal, the RAD considered the RPD’s finding that the Applicant had failed to produce any secondary evidence such as money transfers, bills of sale, or affidavits to establish her identity.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4660975` offsets `228-236`; context: Although the RPD acknowledged the lack and unavailability of documents in Somalia, given the country conditions, it nevertheless determined the Applicant could have made efforts to find secondary sources to identify herself, including contacting her mother in Nairobi or uncle in Somalia.
- Evidence: `evidence_fact` cue `found that` at chunk `4660976` offsets `12-22`; context: [7] The RAD found that, since the Applicant had spent four months in Nairobi and communicated during that time with her family in Somalia, she could have asked her Somalian relatives to provide evidence, especially as she was planning to come to Canada to seek protection.

#### 13414:1:subtheme:3 · paragraphs 7-10

- Raw key terms: `evidence, identity, personal, testimony, weight, witness, appellant, applicant`
- Display key terms: `identity, personal, testimony, weight, witness, appellant`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: identity, personal, testimony, weight, witness, appellant Evidence spans paragraphs 7-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4660977` offsets `612-619`; context: This letter did not: (a) give details of who was consulted; (b) indicate what checks and balances were undertaken to ensure the accuracy of the information; (c) confirm her personal identity, although it stated the Applicant is a member of the Garre clan; and (d) state whether the Garre members who were consulted were from Jubaland.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660977` offsets `32-40`; context: [8] The RAD then considered the evidence from the Somali Immigrant Aid Organization [SIAO].
- Evidence: `counterargument_limitation` cue `although` at chunk `4660977` offsets `534-542`; context: This letter did not: (a) give details of who was consulted; (b) indicate what checks and balances were undertaken to ensure the accuracy of the information; (c) confirm her personal identity, although it stated the Applicant is a member of the Garre clan; and (d) state whether the Garre members who were consulted were from Jubaland.
- Evidence: `evidence_fact` cue `testimony` at chunk `4660978` offsets `45-54`; context: [9] The RAD also placed little weight on the testimony of the witness, the Applicant’s great aunt, noting that the “RPD found the connection between the Applicant and the witness was ‘peripheral, tenuous and minor at best’.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660979` offsets `46-54`; context: [26] The RAD finds that, even if the witness’ evidence was found to be credible, this evidence can only establish the Appellant’s personal identity and affiliation with the Garre clan.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4660979` offsets `208-214`; context: The witness’ testimony cannot and does not establish the Appellant’s nationality at the time the witness knew the Appellant or any time after.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660980` offsets `87-95`; context: [27] Given the credibility concerns highlighted above, the RAD finds that the witness’ evidence is of little probative value in establishing the personal identity and nationality of the Appellant.

#### 13414:1:subtheme:4 · paragraphs 11-15

- Raw key terms: `applicant, evidence, canada, identity, nationality, paragraph, stated, another`
- Display key terms: `identity, nationality, paragraph, stated, another`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: identity, nationality, paragraph, stated, another Position/evidence statements: The Respondent argues that the RAD must have meant to cite another RIR which is in the record (SOM103613. | [20] What appear to be additional typographical errors are found in paragraph 4 of the decision, where the panel member writes that the “Appellant, his wife and his mother fled to Ethiopia,” and again in paragraph 14 whe Rule/authority context: Standard of Review [12] The RAD’s decision in this case is to be reviewed on a standard of reasonableness (see: Sisman v. Application context: Accordingly, the RAD's decision should not be disturbed so long as it is justifiable, intelligible, and transparent, and defensible in respect of the facts and the law (Dunsmuir at paragraph 47). | [15] Because the RAD did not regard this letter as establishing the Applicant’s identity or nationality, the RAD found the Applicant “could reasonably be a member of the Garre clan but not a citizen of Somalia, as member Evidence spans paragraphs 11-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4660981` offsets `557-563`; context: Issues [11] This application for judicial review raises one primary issue: was the RAD’s decision as to the Applicant’s identity reasonable?
- Evidence: `evidence_fact` cue `evidence` at chunk `4660981` offsets `60-68`; context: [10] In view of the Applicant’s failure to obtain secondary evidence and her unreasonable explanations for not doing so, the low weight given to the SIAO letter, the Applicant’s inconsistent answers about Somalian currency and the neighbourhood she lived in, the tenuous connection with the witness, and a lack of evidence beyond the Applicant’s own testimony, the RAD concluded that it “concurs with the RPD that the Applicant has failed to provide sufficient credible or trustworthy evidence to establish his [sic] personal identity and nationality.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4660981` offsets `904-922`; context: Standard of Review [12] The RAD’s decision in this case is to be reviewed on a standard of reasonableness (see: Sisman v.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4660981` offsets `1385-1396`; context: Accordingly, the RAD's decision should not be disturbed so long as it is justifiable, intelligible, and transparent, and defensible in respect of the facts and the law (Dunsmuir at paragraph 47).
- Evidence: `party_position` cue `argues` at chunk `4660982` offsets `525-531`; context: The Respondent argues that the RAD must have meant to cite another RIR which is in the record (SOM103613.
- Evidence: `evidence_fact` cue `record` at chunk `4660982` offsets `502-508`; context: However, this RIR cannot be found in the certified tribunal record.
- Evidence: `reasoning_application` cue `Because` at chunk `4660982` offsets `5-12`; context: [15] Because the RAD did not regard this letter as establishing the Applicant’s identity or nationality, the RAD found the Applicant “could reasonably be a member of the Garre clan but not a citizen of Somalia, as members of the Garre clan are scattered all over Somalia and all over the Muslim world.
- Evidence: `counterargument_limitation` cue `but` at chunk `4660982` offsets `181-184`; context: [15] Because the RAD did not regard this letter as establishing the Applicant’s identity or nationality, the RAD found the Applicant “could reasonably be a member of the Garre clan but not a citizen of Somalia, as members of the Garre clan are scattered all over Somalia and all over the Muslim world.
- Evidence: `evidence_fact` cue `testimony` at chunk `4660983` offsets `44-53`; context: [17] Furthermore, in assessing the witness’ testimony, the RAD stated it did not establish the Applicant’s nationality at the time the witness knew Ms.
- Evidence: `evidence_fact` cue `record` at chunk `4660984` offsets `274-280`; context: The record is devoid of any evidence that a farm had been sold to pay for the smuggler’s services.
- Evidence: `party_position` cue `submitted` at chunk `4660985` offsets `348-357`; context: [20] What appear to be additional typographical errors are found in paragraph 4 of the decision, where the panel member writes that the “Appellant, his wife and his mother fled to Ethiopia,” and again in paragraph 14 where it states the interpreter’s affidavit “is admissible as new evidence;”, this is despite paragraph 15 where all the documents submitted as new evidence (including this affidavit) are stated to be “not admissible as new evidence.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4660985` offsets `251-260`; context: [20] What appear to be additional typographical errors are found in paragraph 4 of the decision, where the panel member writes that the “Appellant, his wife and his mother fled to Ethiopia,” and again in paragraph 14 where it states the interpreter’s affidavit “is admissible as new evidence;”, this is despite paragraph 15 where all the documents submitted as new evidence (including this affidavit) are stated to be “not admissible as new evidence.

#### 13414:1:subtheme:5 · paragraphs 16-17

- Raw key terms: `above, actually, allowed, appeal, applicant, application, aside, assessment`
- Display key terms: `above, actually, allowed, aside, assessment`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: above, actually, allowed, aside, assessment Operative outcome context: Conclusion [22] In view of the foregoing reasons, the Applicant’s application for judicial review is granted, the RAD's decision is set aside, and the matter returned to the RAD for a new determination by a different pan Evidence spans paragraphs 16-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4660986` offsets `509-517`; context: No question of general importance is certified.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660986` offsets `160-168`; context: [21] One is thus left to wonder, despite the RAD’s statements as to its role in reviewing the RPD’s decision, just how much of an independent assessment of the evidence the RAD actually conducted in this case given the numerous typographical and other errors noted above.
- Evidence: `disposition` cue `granted` at chunk `4660986` offsets `376-383`; context: Conclusion [22] In view of the foregoing reasons, the Applicant’s application for judicial review is granted, the RAD's decision is set aside, and the matter returned to the RAD for a new determination by a different panel member.

#### Section text

Ibrahim v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2016-01-06
Neutral citation
2016 FC 11
File numbers
IMM-2025-15
Decision Content
Date: 20160106
Docket: IMM-2025-15
Citation: 2016 FC 11
Ottawa, Ontario, January 6, 2016
PRESENT: The Honourable Mr. Justice Boswell
BETWEEN:
YUSRA IBRAHIM
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] Yusra Mohamed Ibrahim, the Applicant, claims to be a 21 year old Sufi-Sunni woman who is a member of the Garre clan in Somalia. The Garre is a minority nomadic clan in southern Somalia who herd goats, camels, and sheep.

[2] During the evening on July 22, 2013, members of Al-Shabaab came to the hut where the Applicant lived with her family on the outskirts of the town of El-Wak in southern Somalia. They demanded the Applicant’s father stop practicing Sufism and make her two older brothers join Al-Shabaab; they also wanted to take the Applicant to become the wife of one of the members. When the Applicant heard this, she fled out the back of the hut with her two younger siblings to the safety of her aunt’s hut. Later that night, the Applicant’s mother came to the aunt’s hut and informed the Applicant her father and two brothers had been killed. The next day, the Applicant, her mother, and her two younger siblings left on foot for Kenya to seek refuge. After they arrived in Nairobi, the Applicant’s uncle sold some animals and sent the money to the Applicant’s mother who found a smuggler to take the Applicant to Canada using a Swedish passport. The Applicant arrived in Canada on November 11, 2013, and sought Canada’s protection on November 27, 2013.

[3] On October 10, 2014, the Refugee Protection Division [RPD] of the Immigration and Refugee Protection Board [the Board] rejected the Applicant’s refugee claim, finding that she had failed to establish her personal identity and nationality as a citizen of Somalia. The Applicant’s appeal of the RPD’s decision to the Refugee Appeal Division [RAD] of the Board was dismissed by the RAD in a decision dated April 9, 2015. The Applicant now asks this Court, pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act], to set aside the RAD’s decision and return the matter to a different member of the RAD for re-determination.
I. The RAD’s Decision [4] The RAD adopted this Court’s decision in Huruglica v Canada (Citizenship and Immigration), 2014 FC 799 (at paras 54-55), [2014] 4 FCR 811, to frame its role in reviewing the RPD’s decision, stating that it would conduct its own, independent assessment of whether the Applicant was a Convention refugee or person in need of protection under section 97 of the Act, and that it also would respect the credibility or other findings of the RPD where the RPD had a particular advantage in reaching its conclusions.

[5] After noting its role, the RAD considered the new evidence submitted by the Applicant pursuant to subsection 110(4) of the Act, namely: (1) two Ottawa Hospital documents; (2) an affidavit from the interpreter at the Applicant’s RPD hearing confirming that “bessa” means money in Garreh; and (3) an internet article about Somalian currency. The RAD noted there were no explanations for the relevance of any of these documents or why they were not available earlier and, consequently, found them not admissible as new evidence for purposes of the appeal.

[6] Turning next to the merits of the appeal, the RAD considered the RPD’s finding that the Applicant had failed to produce any secondary evidence such as money transfers, bills of sale, or affidavits to establish her identity. Although the RPD acknowledged the lack and unavailability of documents in Somalia, given the country conditions, it nevertheless determined the Applicant could have made efforts to find secondary sources to identify herself, including contacting her mother in Nairobi or uncle in Somalia. The RAD also determined the Applicant could have contacted authorities such as the Jubaland administration, the Somali Police Force, or the National Army, concerning the murders of her father and brothers and establishing her identity.

[7] The RAD found that, since the Applicant had spent four months in Nairobi and communicated during that time with her family in Somalia, she could have asked her Somalian relatives to provide evidence, especially as she was planning to come to Canada to seek protection. The RAD also thought it would have been reasonable for there to be some documentation of money transfers from Somalia to Kenya or to the smuggler. Thus, the RAD concurred with the RPD that the Applicant’s failure to make any efforts to obtain secondary evidence undermined her overall credibility.

[8] The RAD then considered the evidence from the Somali Immigrant Aid Organization [SIAO]. Based on a response to information request [RIR], the RAD noted that Somali associations in Canada employed different methods to assist applicants in establishing their identity as a Somalian. The RAD expressed several concerns with the SIAO letter. This letter did not: (a) give details of who was consulted; (b) indicate what checks and balances were undertaken to ensure the accuracy of the information; (c) confirm her personal identity, although it stated the Applicant is a member of the Garre clan; and (d) state whether the Garre members who were consulted were from Jubaland. Given these concerns, the RAD concluded it could not place significant weight on this letter.

[9] The RAD also placed little weight on the testimony of the witness, the Applicant’s great aunt, noting that the “RPD found the connection between the Applicant and the witness was ‘peripheral, tenuous and minor at best’.” After assessing this evidence, the RAD “arrived at the same conclusion as the RPD did,” and concluded as follows:

[26] The RAD finds that, even if the witness’ evidence was found to be credible, this evidence can only establish the Appellant’s personal identity and affiliation with the Garre clan. The witness’ testimony cannot and does not establish the Appellant’s nationality at the time the witness knew the Appellant or any time after. For example, the Appellant and her family could have left Somalia and obtained permanent residence or citizenship in another country after she was last seen by the witness. The Appellant could have been living in El-Wak and have citizenship in another country as well as Somalia.

[27] Given the credibility concerns highlighted above, the RAD finds that the witness’ evidence is of little probative value in establishing the personal identity and nationality of the Appellant. Even if the RAD placed significant weight on the witness’ testimony and evidence, it does not establish the Appellant’s nationality or country of reference. This is of little value in establishing the Appellant’s nationality in the year 2014.

[10] In view of the Applicant’s failure to obtain secondary evidence and her unreasonable explanations for not doing so, the low weight given to the SIAO letter, the Applicant’s inconsistent answers about Somalian currency and the neighbourhood she lived in, the tenuous connection with the witness, and a lack of evidence beyond the Applicant’s own testimony, the RAD concluded that it “concurs with the RPD that the Applicant has failed to provide sufficient credible or trustworthy evidence to establish his [sic] personal identity and nationality.”
II. Issues [11] This application for judicial review raises one primary issue: was the RAD’s decision as to the Applicant’s identity reasonable? For the reasons stated below, the RAD’s decision in this case is not reasonable and the matter must be returned to the RAD for redetermination by another panel member in accordance with these reasons.
III. Standard of Review [12] The RAD’s decision in this case is to be reviewed on a standard of reasonableness (see: Sisman v. Canada (Citizenship and Immigration), 2015 FC 930). Its assessment of the evidence before it is entitled to deference (see: Dunsmuir v New Brunswick, 2008 SCC 9 at paragraph 53, [2008] 1 SCR 190 [Dunsmuir]; Yin v Canada (Citizenship and Immigration), 2014 FC 1209 at paragraph 34; Mojahed v Canada (Citizenship and Immigration), 2015 FC 690 at paragraph 14). Accordingly, the RAD's decision should not be disturbed so long as it is justifiable, intelligible, and transparent, and defensible in respect of the facts and the law (Dunsmuir at paragraph 47). Those criteria are met if “the reasons allow the reviewing court to understand why the tribunal made its decision and permit it to determine whether the conclusion is within the range of acceptable outcomes” (Newfoundland and Labrador Nurses' Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at paragraph 16, [2011] 3 SCR 708).
IV. Analysis [13] The RAD’s reasons for its decision in this case are replete with mistakes and errors that cumulatively render the decision unreliable as a whole and unintelligible in parts and, consequently, unreasonable and not defensible in respect of the facts and the law.
A. The SIAO Letter [14] The RAD prefaces its assessment of the SIAO letter by stating that other Somalian aid organizations in Canada utilize various practices to verify the identity of individuals, such as the use of statutory declarations or requiring a certain number of witnesses. This mindset of the RAD as to the practices of other organizations negatively colours the RAD’s analysis and assessment of this letter which states: “we have confirmed with Garre clan member that Yusra Mohamed Ibrahim is a Garre from Somalia.” In the RIR about Somali organizations in Canada, there are several statements as to how difficult it is to establish the identities of younger Somali individuals such as the Applicant. The RAD ignores this information, and proceeds to selectively and unjustifiably use the practices of other Somalian organizations to discount and discredit the letter the Applicant did proffer to establish her identity.

[15] Because the RAD did not regard this letter as establishing the Applicant’s identity or nationality, the RAD found the Applicant “could reasonably be a member of the Garre clan but not a citizen of Somalia, as members of the Garre clan are scattered all over Somalia and all over the Muslim world.” The RAD references a RIR (SOM104613.E) to support its finding that the Garre are scattered all over Somalia and all over the Muslim world. However, this RIR cannot be found in the certified tribunal record. The Respondent argues that the RAD must have meant to cite another RIR which is in the record (SOM103613.E) [emphasis added]; this RIR states that the Ashraf clan lives across Somalia and all over the Muslin world. This argument is not convincing. Even if the RAD had this document in mind when expressing its concern that the Applicant might not be a citizen of Somalia, the RIR about the Ashraf clan makes no mention whatsoever of the Garre clan being a subgroup of the Ashraf clan.
B. The Identity Witness [16] In this case, the Applicant brought forward an identity witness to establish her identity as a Garre from Somalia, thus taking the same step as followed by at least one of the organizations identified in the RIR about Somali organizations in Canada. In concluding that the witness’ testimony and evidence had “little probative value” to establish the Applicant’s personal identity, the RAD stated that the RPD had found the connection between the Applicant and the witness was “peripheral, tenuous and minor at best.” However, the RPD made no such finding and made no such statement. This is plainly wrong. The RAD misapprehended and misstated the RPD’s assessment of the connection between the Applicant and the witness. What the RPD actually found was that the Applicant’s evidence as to how she connected with the witness in Canada was “questionable and unlikely given the many other credibility findings related to her identity.”

[17] Furthermore, in assessing the witness’ testimony, the RAD stated it did not establish the Applicant’s nationality at the time the witness knew Ms. Ibrahim or at any time after. While that may well be so, it was not reasonable for the RAD to then speculate from this determination that the Applicant could have obtained citizenship in another country after she was last seen by the witness. There is no evidence in the record for any such speculation by the RAD. On the contrary, the witness in this case (unlike the identity witness in Elmi v Canada (Citizenship and Immigration), 2008 FC 773 at para 2, 168 ACWS (3d) 832, who was a former neighbour of Ms. Elmi in Somalia) was a blood relative of the Applicant and the witness’ identity as a Somalian national was not questioned.
C. The Typographical Errors [18] By themselves, the six typographical errors where the RAD writes (in paragraph 21 of its reasons) “Ethiopia” rather than “Kenya” are not mistakes that render the decision unintelligible. Reading the decision as a whole, it does not appear that the RAD was confused to the point of suggesting that the Applicant was Ethiopian, or that the RAD based any specific outcome on the country to which the Applicant fled as being Ethiopia rather than her actual destination, Kenya. As a result, these typographical errors in this one paragraph could be characterized as a slip of the tongue, since the RAD correctly identifies that the Applicant had fled to Nairobi.

[19] What cannot be so characterized, however, is the reference in this same paragraph to the Applicant being aware, while in Kenya, that “the farm and the animals had been sold” and that the money raised from “the sale of the farm” had been used to pay for a smuggler. The record is devoid of any evidence that a farm had been sold to pay for the smuggler’s services. A similar misapprehension of the evidence about what was sold to fund the Applicant’s travel to Canada also occurs in paragraph 18 of the reasons, where the RAD refers to the RPD noting the Applicant’s lack of efforts to provide a “bill of sale for the family farm and or animals,” as secondary evidence to support her identity and nationality. Again, the RAD here misconstrues and misstates what the RPD determined. Although the RPD did find it unreasonable for the Applicant not to have some paper evidence of the sale of the animals, it made no reference to the sale of any farm. Indeed, the Garre being a nomadic clan, it belies the definition of the word nomadic that there would even be a farm to sell.

[20] What appear to be additional typographical errors are found in paragraph 4 of the decision, where the panel member writes that the “Appellant, his wife and his mother fled to Ethiopia,” and again in paragraph 14 where it states the interpreter’s affidavit “is admissible as new evidence;”, this is despite paragraph 15 where all the documents submitted as new evidence (including this affidavit) are stated to be “not admissible as new evidence.” The Applicant is also referred to as male by the use of the word “his” in paragraphs 16 and 29.

[21] One is thus left to wonder, despite the RAD’s statements as to its role in reviewing the RPD’s decision, just how much of an independent assessment of the evidence the RAD actually conducted in this case given the numerous typographical and other errors noted above.
V. Conclusion [22] In view of the foregoing reasons, the Applicant’s application for judicial review is granted, the RAD's decision is set aside, and the matter returned to the RAD for a new determination by a different panel member. No question of general importance is certified.
JUDGMENT
THIS COURT’S JUDGMENT is that: the application for judicial review is allowed; the matter is returned to the Refugee Appeal Division for redetermination by a different panel member; and no question of general importance is certified.
"Keith M. Boswell"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-2025-15
STYLE OF CAUSE:
YUSRA IBRAHIM v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
December 2, 2015


## 13414:2 · paragraphs 18-18

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c449faacfbe5f066e02da0e15971eef981a8366e1a3f304ffb4fac11dfef8614`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13414:2:subtheme:1 · paragraphs 18-18

- Raw key terms: `appearances, applicant, attorney, barrister, boswell, canada, crane, dated`
- Display key terms: `barrister, boswell, crane, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, boswell, crane, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 18-18. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
BOSWELL J.
DATED:
january 6, 2016
APPEARANCES:
Micheal Crane
For The Applicant
Teresa Ramnarine
For The Respondent
SOLICITORS OF RECORD:
Micheal Crane
Barrister and Solicitor
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
