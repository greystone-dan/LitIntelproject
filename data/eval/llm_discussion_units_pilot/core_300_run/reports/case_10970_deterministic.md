# Discussion Units: case 10970

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **47**
- Continuity pairs: **46**
- Discussion Units: **6**
- Paragraph source hashes: **47**
- Sub-themes: **15**

## 10970:1 · paragraphs 0-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4a9df1a1fca825f6abfd5a13f949b83e96d8e412efb88d6c61feb2dc46d6e4f1`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10970:1:subtheme:1 · paragraphs 0-9

- Raw key terms: `applicant, claim, refugee, states, canada, claims, ghana, decision`
- Display key terms: `refugee, states, claims, ghana`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: refugee, states, claims, ghana Position/evidence statements: He contends before this Court that he ﬂed Ghana on July 23, 2014. | [4] The Applicant claims he has been attracted to members of the same sex since the age of 11. Rule/authority context: [1] The Applicant brings an application, pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S. Application context: I offer the limiting words “before this Court” because there is evidence he stated on at least one other occasion that he left Ghana on a different date. | During the interview, the reporter asked about the basis of his claim, to which he answered that he is in danger in Ghana because he is gay. Operative outcome context: He states the intervention of a stranger allowed him to escape. Evidence spans paragraphs 0-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4553039` offsets `41-52`; context: [1] The Applicant brings an application, pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `party_position` cue `contends` at chunk `4553040` offsets `44-52`; context: He contends before this Court that he ﬂed Ghana on July 23, 2014.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553040` offsets `171-179`; context: I offer the limiting words “before this Court” because there is evidence he stated on at least one other occasion that he left Ghana on a different date.
- Evidence: `reasoning_application` cue `because` at chunk `4553040` offsets `154-161`; context: I offer the limiting words “before this Court” because there is evidence he stated on at least one other occasion that he left Ghana on a different date.
- Evidence: `party_position` cue `claims` at chunk `4553042` offsets `18-24`; context: [4] The Applicant claims he has been attracted to members of the same sex since the age of 11.
- Evidence: `party_position` cue `claims` at chunk `4553043` offsets `18-24`; context: [5] The Applicant claims his uncle wanted the property he had inherited from his parents.
- Evidence: `counterargument_limitation` cue `however` at chunk `4553043` offsets `551-558`; context: The Applicant states he and his sister reported the crimes to the police following his release from the hospital; however, the police took no action due to his inability or refusal to pay money.
- Evidence: `party_position` cue `contends` at chunk `4553044` offsets `18-26`; context: [6] The Applicant contends that several months after the attack, his uncle reported him to community leaders, whereby he was “outed”.
- Evidence: `disposition` cue `allowed` at chunk `4553044` offsets `282-289`; context: He states the intervention of a stranger allowed him to escape.
- Evidence: `party_position` cue `claims` at chunk `4553045` offsets `51-57`; context: [7] Upon entering the United States, the Applicant claims he was not given the opportunity to provide full details of his asylum claim.
- Evidence: `reasoning_application` cue `because` at chunk `4553046` offsets `214-221`; context: During the interview, the reporter asked about the basis of his claim, to which he answered that he is in danger in Ghana because he is gay.

#### 10970:1:subtheme:2 · paragraphs 10-13

- Raw key terms: `applicant, american, claim, ghana, information, noted, officials, orientation`
- Display key terms: `american, ghana, information, noted, officials, orientation`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: american, ghana, information, noted, officials, orientation Position/evidence statements: The RPD also noted that a letter from the Applicant’s sister, submitted to the American authorities in support of the Applicant’s claim, failed to mention his sexual orientation. Evidence spans paragraphs 10-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4553048` offsets `23-28`; context: [10] The determinative issue for the RPD was credibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553048` offsets `623-631`; context: ); (3) Inconsistencies in the dates of key events, such as the sale of land, the dispute with his uncle, the first attack and subsequent hospitalization; and; (4) Contradictory evidence relating to his father’s death.
- Evidence: `evidence_fact` cue `record` at chunk `4553049` offsets `756-762`; context: Furthermore, the RPD considered it implausible that the Applicant would not have had an opportunity to discuss his personal circumstances in private given that the United States has a strong human rights record, American officials provided the Applicant with information regarding free legal counsel and the Applicant had assistance in the preparation of his asylum claim.
- Evidence: `party_position` cue `submitted` at chunk `4553050` offsets `270-279`; context: The RPD also noted that a letter from the Applicant’s sister, submitted to the American authorities in support of the Applicant’s claim, failed to mention his sexual orientation.
- Evidence: `counterargument_limitation` cue `however` at chunk `4553051` offsets `230-237`; context: For example, the Applicant had initially indicated he was hospitalized after being beaten in 2012; however, the doctor’s letter states that the Applicant was treated in October 2013.

#### 10970:1:subtheme:3 · paragraphs 14-17

- Raw key terms: `applicant, concluded, ghana, during, against, authorities, claim, considered`
- Display key terms: `concluded, ghana, during, against, authorities, considered`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: concluded, ghana, during, against, authorities, considered Evidence spans paragraphs 14-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4553052` offsets `73-80`; context: [14] The RPD considered other documentary evidence in order to determine whether, disregarding the Applicant’s lack of credibility, other sufﬁcient credible evidence existed to allow the claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553052` offsets `42-50`; context: [14] The RPD considered other documentary evidence in order to determine whether, disregarding the Applicant’s lack of credibility, other sufﬁcient credible evidence existed to allow the claim.

#### 10970:1:subtheme:4 · paragraphs 18-20

- Raw key terms: `evidence, submissions, admissibility, appeal, applicant, canada, citizenship, considered`
- Display key terms: `submissions, admissibility, considered`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: submissions, admissibility, considered Application context: It then applied a standard of correctness in accordance with the decision in Canada (Minister of Citizenship and Immigration) v. | The RAD also noted that, if the new evidence meets one of the legislative requirements set out in subsection 110(4), the second step of the analysis is for the RAD to apply the modified Raza factors endorsed in Canada (M Evidence spans paragraphs 18-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4553056` offsets `524-531`; context: The RAD then conducted a re-assessment of the record in order to determine whether the RPD erred on the grounds advanced by the Applicant.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553056` offsets `79-87`; context: [18] The RAD first considered submissions relating to the admissibility of new evidence (two affidavits from Ghana, four support letters from Canada, a copy of the Applicant’s Brazilian visa, and photos taken in Canada), as well as a request for an oral hearing.
- Evidence: `reasoning_application` cue `applied` at chunk `4553056` offsets `271-278`; context: It then applied a standard of correctness in accordance with the decision in Canada (Minister of Citizenship and Immigration) v.
- Evidence: `issue` cue `question` at chunk `4553057` offsets `12-20`; context: [19] On the question of the admissibility of new evidence, the RAD considered subsection 110(4) of the IRPA, which provides that appellants may present only evidence that arose after the rejection of their claims or that was not reasonably available, or that they could not reasonably have been expected in the circumstances to have presented, at the time of the rejection.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553057` offsets `49-57`; context: [19] On the question of the admissibility of new evidence, the RAD considered subsection 110(4) of the IRPA, which provides that appellants may present only evidence that arose after the rejection of their claims or that was not reasonably available, or that they could not reasonably have been expected in the circumstances to have presented, at the time of the rejection.
- Evidence: `reasoning_application` cue `apply` at chunk `4553057` offsets `817-822`; context: The RAD also noted that, if the new evidence meets one of the legislative requirements set out in subsection 110(4), the second step of the analysis is for the RAD to apply the modified Raza factors endorsed in Canada (Minister of Citizenship and Immigration) v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553058` offsets `93-101`; context: [20] The RAD noted that the Applicant had provided no submissions about how the proposed new evidence meets the requirements of 110(4) or the modified Raza factors.

#### 10970:1:subtheme:5 · paragraphs 21-22

- Raw key terms: `applicant, date, decision, however, reasonably, support, whether, affidavits`
- Display key terms: `date, however, reasonably, support, whether, affidavits`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: date, however, reasonably, support, whether, affidavits Position/evidence statements: The Applicant had nearly two months between the date of the hearing and the decision to submit post-hearing evidence in support of his claim. Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4553059` offsets `388-395`; context: The RAD was unable to determine whether the information communicated in the letters arose after the RPD’s decision, or that the Applicant could not reasonably have been expected, in the circumstances, to have presented this information to the RPD before it rendered its decision.
- Evidence: `evidence_fact` cue `record` at chunk `4553059` offsets `120-126`; context: [21] The two affidavits from Ghana post-dated the RPD’s decision, but largely reiterated information already in the RPD record.
- Evidence: `counterargument_limitation` cue `but` at chunk `4553059` offsets `66-69`; context: [21] The two affidavits from Ghana post-dated the RPD’s decision, but largely reiterated information already in the RPD record.
- Evidence: `issue` cue `whether` at chunk `4553060` offsets `330-337`; context: It was unclear whether any of the photos were available, or could reasonably have been available, prior to the RPD’s decision in May 2017.
- Evidence: `party_position` cue `submit` at chunk `4553060` offsets `261-267`; context: The Applicant had nearly two months between the date of the hearing and the decision to submit post-hearing evidence in support of his claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553060` offsets `281-289`; context: The Applicant had nearly two months between the date of the hearing and the decision to submit post-hearing evidence in support of his claim.
- Evidence: `counterargument_limitation` cue `However` at chunk `4553060` offsets `99-106`; context: However, the fact that they were taken after the hearing is not the test.

#### 10970:1:subtheme:6 · paragraphs 23-27

- Raw key terms: `applicant, appeal, concluded, credibility, decision, evidence, refugee, accepted`
- Display key terms: `concluded, credibility, refugee, accepted`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: concluded, credibility, refugee, accepted Rule/authority context: Under the circumstances, the RAD found the Applicant had not met these requirements, there being no evidence from the Minister, and no new admissible evidence from the Applicant. | The RAD noted the submissions relating to these alleged errors were extremely brief and essentially only articulated general principles about credibility. Application context: Accordingly, the RAD dismissed the Applicant’s request for an oral hearing. Operative outcome context: Accordingly, the RAD dismissed the Applicant’s request for an oral hearing. | The RAD concluded the Applicant is neither a Convention refugee nor a person in need of protection, and dismissed the appeal. Evidence spans paragraphs 23-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4553061` offsets `204-209`; context: [23] Concerning the request for an oral hearing, the RAD noted it may hold a hearing if, in its opinion, there is documentary evidence as described in subsection 110(3) of the IRPA that: raises a serious issue relating to the credibility of the person who is the subject of the appeal; is central to the decision with respect to the refugee protection claim; and; if accepted, would justify allowing or rejecting the claim (subsection 110(6) of the IRPA).
- Evidence: `evidence_fact` cue `evidence` at chunk `4553061` offsets `126-134`; context: [23] Concerning the request for an oral hearing, the RAD noted it may hold a hearing if, in its opinion, there is documentary evidence as described in subsection 110(3) of the IRPA that: raises a serious issue relating to the credibility of the person who is the subject of the appeal; is central to the decision with respect to the refugee protection claim; and; if accepted, would justify allowing or rejecting the claim (subsection 110(6) of the IRPA).
- Evidence: `governing_rule` cue `Under` at chunk `4553061` offsets `456-461`; context: Under the circumstances, the RAD found the Applicant had not met these requirements, there being no evidence from the Minister, and no new admissible evidence from the Applicant.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4553061` offsets `635-646`; context: Accordingly, the RAD dismissed the Applicant’s request for an oral hearing.
- Evidence: `disposition` cue `dismissed` at chunk `4553061` offsets `656-665`; context: Accordingly, the RAD dismissed the Applicant’s request for an oral hearing.
- Evidence: `issue` cue `whether` at chunk `4553062` offsets `173-180`; context: [24] In its analysis of the merits, the RAD first identified the two alleged errors advanced by the Applicant, namely: (a) that the RPD failed to make a determination as to whether the Applicant is a Convention refugee based on the evidence accepted as credible; and; (b) that the RPD erred in ignoring the reasonable explanations of the Applicant, which, rather than being inconsistent, complemented one another.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553062` offsets `232-240`; context: [24] In its analysis of the merits, the RAD first identified the two alleged errors advanced by the Applicant, namely: (a) that the RPD failed to make a determination as to whether the Applicant is a Convention refugee based on the evidence accepted as credible; and; (b) that the RPD erred in ignoring the reasonable explanations of the Applicant, which, rather than being inconsistent, complemented one another.
- Evidence: `governing_rule` cue `principles` at chunk `4553062` offsets `539-549`; context: The RAD noted the submissions relating to these alleged errors were extremely brief and essentially only articulated general principles about credibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553063` offsets `48-56`; context: [25] Following an independent assessment of the evidence, the RAD concluded the RPD had carried out a thorough credibility analysis that was clear, intelligible and based upon contradictions and omissions not reasonably explained.
- Evidence: `disposition` cue `dismissed` at chunk `4553064` offsets `292-301`; context: The RAD concluded the Applicant is neither a Convention refugee nor a person in need of protection, and dismissed the appeal.

#### Section text

Ilias v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2018-06-27
Neutral citation
2018 FC 661
File numbers
IMM-5152-17
Decision Content
Date: 20180627
Docket: IMM-5152-17
Citation: 2018 FC 661
Ottawa, Ontario, June 27, 2018
PRESENT: The Honourable Mr. Justice Bell
Docket: IMM-5152-17
BETWEEN:
MOHAMMED KAMAL DEEN ILIAS
Applicant
and
MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Nature of the Proceedings

[1] The Applicant brings an application, pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 [IRPA], by which he seeks judicial review of a decision of the Immigration and Refugee Board, Refugee Appeal Division [RAD], rendered on November 3, 2017 [Decision]. The RAD confirmed an earlier decision of the Refugee Protection Division [RPD] that the Applicant is neither a Convention refugee nor a person in need of protection pursuant to section 96 and subsection 97(1) of the IRPA.
II. Background

[2] The Applicant is a citizen of Ghana. He contends before this Court that he ﬂed Ghana on July 23, 2014. I offer the limiting words “before this Court” because there is evidence he stated on at least one other occasion that he left Ghana on a different date. The Applicant contends he travelled to Brazil on a visa. From Brazil, he travelled through South and Central America, eventually arriving in the United States of America, where, on April 11, 2015, he made a refugee claim based on his political opinion. Notably, that claim made no mention of persecution based upon sexual orientation. The claim was ultimately rejected. Faced with deportation from the United States, the Applicant fled to Canada by crossing the border near Emerson, Manitoba.

[3] On December 3, 2016, Canada Border Services Agency officers arrested the Applicant. In making his claim for refugee protection in Canada, the Applicant alleged a fear of persecution in Ghana due to his sexual orientation as a homosexual man and due to a land dispute with his uncle. The Applicant made no mention of political opinion as a potential ground of persecution in his claim for refugee status in Canada.

[4] The Applicant claims he has been attracted to members of the same sex since the age of 11. He says he engaged in his first homosexual activity while selling goods on the streets. This resulted in a relationship with a man who he says was his protector and a financial support for him and his sister.

[5] The Applicant claims his uncle wanted the property he had inherited from his parents. The uncle used the Applicant’s homosexuality to pressure him into giving him the property. When the Applicant refused, the uncle obtained the assistance of a local gang, who began to threaten the Applicant. The Applicant says he was eventually taken to the bush, beaten and cut with knives, resulting in injuries which required medical attention. The Applicant states he and his sister reported the crimes to the police following his release from the hospital; however, the police took no action due to his inability or refusal to pay money.

[6] The Applicant contends that several months after the attack, his uncle reported him to community leaders, whereby he was “outed”. He claims he was again attacked, stripped to his underwear, tied, and threatened to be burned with petrol. He states the intervention of a stranger allowed him to escape. After the latest attack, he states he called his partner who arranged his travel to Tamale, in northern Ghana, where he stayed with a family member. When this family member learned the Applicant was gay, he had to leave Tamale. The Applicant went Accra, where he stayed with a childhood friend until that friend was threatened due to the Applicant’s alleged homosexuality. The friend contacted the Applicant’s partner who provided him (the Applicant) with a passport and visa to Brazil.

[7] Upon entering the United States, the Applicant claims he was not given the opportunity to provide full details of his asylum claim. He states that due to his detention, he was unable to meet in private with a lawyer or volunteer worker. He states his hearing was not held in private as he was questioned in front of other detainees. He claims he was fearful of what the other detainees might do to him if they discovered he was gay. For that reason he never disclosed his homosexuality to immigration authorities in the United States.

[8] Following his arrival in Canada, the Applicant states he was interviewed by a reporter. During the interview, the reporter asked about the basis of his claim, to which he answered that he is in danger in Ghana because he is gay. This interview was aired on CTV News. He states he received a copy of the video of the interview from a friend who saw it in Ghana. Based upon the diffusion of the video in Ghana, he claimed he was entitled to make a sur place refugee claim.

[9] The Applicant’s Canadian refugee hearing took place before the RPD on February 6 and March 7, 2017. In a written decision rendered on May 5, 2017, the RPD rejected his claim. The Applicant appealed the RPD decision, which was confirmed by the RAD. That RAD Decision is the subject of this judicial review.
III. RPD Decision

[10] The determinative issue for the RPD was credibility. The RPD found the Applicant lacking credibility for a number of reasons, namely: (1) the complete absence of any mention of his sexual orientation, or persecution he suffered due to his sexual orientation, in the application for asylum made in the United States; (2) inconsistencies in the information provided vis-à-vis the Applicant’s travel from Ghana (dates, travel destinations, etc.); (3) Inconsistencies in the dates of key events, such as the sale of land, the dispute with his uncle, the first attack and subsequent hospitalization; and; (4) Contradictory evidence relating to his father’s death.

[11] With respect to the omissions regarding his sexual orientation in the American political asylum claim, the RPD rejected the Applicant’s explanations regarding lack of privacy and fear. The RPD noted the Applicant had at least three opportunities to inform American ofﬁcials about the persecution he suffered in Ghana due to his sexual orientation: (1) in the Application for Asylum and Withholding of Removal form; (2) in his written declaration; and; (3) to the Department of Homeland Security when he ﬁrst arrived at the American port of entry. Furthermore, the RPD considered it implausible that the Applicant would not have had an opportunity to discuss his personal circumstances in private given that the United States has a strong human rights record, American officials provided the Applicant with information regarding free legal counsel and the Applicant had assistance in the preparation of his asylum claim.

[12] Additionally, the RPD noted the Applicant failed to mention to American officials, in writing or otherwise, the traumatic event during which he was tied up and threatened to be burned alive with petrol. The RPD also noted that a letter from the Applicant’s sister, submitted to the American authorities in support of the Applicant’s claim, failed to mention his sexual orientation. These omissions were never explained.

[13] Other inconsistencies were explained away by the Applicant as errors or delays with respect to the registration of documents. For example, the Applicant had initially indicated he was hospitalized after being beaten in 2012; however, the doctor’s letter states that the Applicant was treated in October 2013. The Applicant provided no explanation for this discrepancy, other than to suggest the doctor had made a mistake. In handwritten declarations and information provided to American officials, the Applicant stated he travelled from Ghana to Ecuador on January 23, 2015; however, in the information he provided to Canadian authorities and in his Canadian refugee claim, he asserts that he travelled from Ghana to Brazil on July 23, 2014. Again, the Applicant states this inconsistency is the result of errors by the American authorities. Another major inconsistency concerned his departure from his hometown of Kumasi. He stated he fled Kumasi in April 2014; however, a signed land sale agreement placed him in Kumasi in June 2014. The RPD noted the Applicant’s explanations for many of the discrepancies were “convoluted and confusing”, or “vague and evasive”. It did not assist the Applicant that discrepancies were found in multiple documents by different authors.

[14] The RPD considered other documentary evidence in order to determine whether, disregarding the Applicant’s lack of credibility, other sufﬁcient credible evidence existed to allow the claim. With respect to letters of support from Canada, the RPD concluded the letters, in large measure, simply relayed information already conveyed by the Applicant, whose credibility was seriously damaged. The panel also concluded supporting letters from Ghana, pictures of wanted posters depicting the Applicant, and pictures from the second attack were likely not legitimate, and could not outweigh the myriad of credibility issues raised by the other evidence.

[15] The letters from Ghana were all unsworn and appeared to be written in close to the same format and style, despite purporting to be written by three different people. A letter from the Applicant’s sister failed to explain why she had not mentioned her brother’s sexual orientation in her letter to American authorities. Concerning the “wanted posters” depicting the Applicant’s image, the RPD noted the posters contained spelling mistakes and appeared unusually set against the backgrounds on which they had been posted. The RPD stated the posters appeared to have been photo-shopped. With respect to the images of him being tied up, the Applicant stated they were taken by a friend who was apparently observing the assault as it was unfolding. The Applicant stated that at the time of the assault he was unaware his friend was present and only subsequently learned of his presence. The RPD concluded the apparent proximity of the photographer to the Applicant made this explanation unlikely. The RPD was skeptical that a friend would be in a position to take such images and not offer assistance during the struggle, that the Applicant would not have noticed his friend, or that the images would only come to light following the Canadian application for asylum. Crucially, the RPD determined the pictures of the Applicant being tied up were staged.

[16] During the course of the RPD’s questioning of the Applicant, his counsel advanced arguments for a sur place refugee claim. Counsel argued that, since the Applicant had identiﬁed himself as a homosexual man from Ghana on a televised news program, he would automatically face persecution in Ghana due to the existence of laws that criminalized homosexual acts. The RPD concluded there was no basis for a sur place refugee claim. The RPD considered it was speculative to suggest the authorities in Ghana would consider the information contained in the report serious enough to alert border ofﬁcials about the Applicant’s pending arrival in Ghana.

[17] The RPD noted there have been no reported cases of police or government violence against LGBT individuals during the year, and there are no reports suggesting Ghana’s anti-gay provisions are currently enforced. The RPD concluded the Applicant is neither a Convention refugee nor a person in need of protection as contemplated by sections 96 and subsection 97(1) of the IRPA.
IV. RAD Decision

[18] The RAD first considered submissions relating to the admissibility of new evidence (two affidavits from Ghana, four support letters from Canada, a copy of the Applicant’s Brazilian visa, and photos taken in Canada), as well as a request for an oral hearing. It then applied a standard of correctness in accordance with the decision in Canada (Minister of Citizenship and Immigration) v. Huruglica, 2016 FCA 93, [2016] 4 F.C.R. 157 [Huruglica]. The RAD then conducted a re-assessment of the record in order to determine whether the RPD erred on the grounds advanced by the Applicant.

[19] On the question of the admissibility of new evidence, the RAD considered subsection 110(4) of the IRPA, which provides that appellants may present only evidence that arose after the rejection of their claims or that was not reasonably available, or that they could not reasonably have been expected in the circumstances to have presented, at the time of the rejection. The RAD noted it is incumbent upon appellants to make full submissions regarding the means by which any proposed new evidence meets those requirements and how that evidence relates to them. See Rule 3(3)(g)(iii) of the Refugee Appeal Division Rules, SOR/2012-257 [RAD Rules]. The RAD also noted that, if the new evidence meets one of the legislative requirements set out in subsection 110(4), the second step of the analysis is for the RAD to apply the modified Raza factors endorsed in Canada (Minister of Citizenship and Immigration) v. Singh, 2016 FCA 96, [2016] 4 FCR 230 [Singh], namely, to assess the admissibility of the new evidence for its credibility, relevance and newness.

[20] The RAD noted that the Applicant had provided no submissions about how the proposed new evidence meets the requirements of 110(4) or the modified Raza factors. The Applicant stated only that the documents supported his appeal and that the photos were taken after his refugee hearing. Below, I briefly set out the reasons offered by the RAD for rejecting each piece of proposed new evidence.

[21] The two affidavits from Ghana post-dated the RPD’s decision, but largely reiterated information already in the RPD record. Where the information in the affidavits differed from information already in the RPD record, no date was provided to support the contention that it post-dated the RPD decision. This was also true of support letters from Canada. The RAD was unable to determine whether the information communicated in the letters arose after the RPD’s decision, or that the Applicant could not reasonably have been expected, in the circumstances, to have presented this information to the RPD before it rendered its decision. Conversely, the Brazilian visa, dated July 2014, pre-dated the RPD’s decision. However, the Applicant offered no credible explanation as to why it could not have been provided before the RPD rendered its decision.

[22] With respect to the “new” photos, the Applicant stated they were taken after his RPD hearing. However, the fact that they were taken after the hearing is not the test. The Applicant had nearly two months between the date of the hearing and the decision to submit post-hearing evidence in support of his claim. It was unclear whether any of the photos were available, or could reasonably have been available, prior to the RPD’s decision in May 2017.

[23] Concerning the request for an oral hearing, the RAD noted it may hold a hearing if, in its opinion, there is documentary evidence as described in subsection 110(3) of the IRPA that: raises a serious issue relating to the credibility of the person who is the subject of the appeal; is central to the decision with respect to the refugee protection claim; and; if accepted, would justify allowing or rejecting the claim (subsection 110(6) of the IRPA). Under the circumstances, the RAD found the Applicant had not met these requirements, there being no evidence from the Minister, and no new admissible evidence from the Applicant. Accordingly, the RAD dismissed the Applicant’s request for an oral hearing.

[24] In its analysis of the merits, the RAD first identified the two alleged errors advanced by the Applicant, namely: (a) that the RPD failed to make a determination as to whether the Applicant is a Convention refugee based on the evidence accepted as credible; and; (b) that the RPD erred in ignoring the reasonable explanations of the Applicant, which, rather than being inconsistent, complemented one another. The RAD noted the submissions relating to these alleged errors were extremely brief and essentially only articulated general principles about credibility. The RAD concluded they were not full and detailed submissions regarding the alleged errors which formed the basis of the appeal, nor did they set out where the errors were to be found in the reasons for decision, as required by Rules 3(3)(g)(i) and (ii) of the RAD Rules.

[25] Following an independent assessment of the evidence, the RAD concluded the RPD had carried out a thorough credibility analysis that was clear, intelligible and based upon contradictions and omissions not reasonably explained. The RAD concluded the RPD was correct to ﬁnd the Applicant lacked credibility and decided the RPD’s ﬁndings were sufﬁcient to maintain its determination that the Applicant failed to prove, on a balance of probabilities, that he is homosexual.

[26] Finally, the RAD observed that the Applicant did not contest the RPD’s sur place ﬁndings. For this reason, the RAD deemed it unnecessary to address that aspect of the RPD’s decision. The RAD concluded the Applicant is neither a Convention refugee nor a person in need of protection, and dismissed the appeal.
V. Relevant Provisions

[27] The relevant provisions of the IRPA are ss. 96, 97(1), 110(3), 110(4), 110(6) and 111. Rules 3(3)(g)(i),(ii) and (iii) of the RAD Rules are also relevant. These provisions are set out in Annex A attached to these reasons.


## 10970:2 · paragraphs 28-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e6bc3473e263288c5c89fc509a2ee1684cb3155a55042d3b202568cf26a17206`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10970:2:subtheme:1 · paragraphs 28-28

- Raw key terms: `issues`
- Display key terms: `issues`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: issues No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 28-28. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

VI. Issues

## 10970:3 · paragraphs 29-41

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `043c785d50c9f62e0a97e3d63edcc50f232cbc548cfd3ac893ce66a34f2d3d94`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10970:3:subtheme:1 · paragraphs 29-30

- Raw key terms: `evidence, irpa, issues, place, review, standard, subsection, admissibility`
- Display key terms: `irpa, issues, place, review, standard, subsection, admissibility`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: irpa, issues, place, review, standard, subsection, admissibility Position/evidence statements: Did the RAD err in refusing to assess the Applicant’s sur place claim? Rule/authority context: [28] The Applicant raises the following issues: Did the RAD err in its assessment of the admissibility of new evidence pursuant to subsection 110(4) of the IRPA? | Where a tribunal is interpreting its home statute or rules enacted thereunder, there is a presumption that the reasonableness standard of review applies to that interpretation (Dunsmuir v. Application context: Where a tribunal is interpreting its home statute or rules enacted thereunder, there is a presumption that the reasonableness standard of review applies to that interpretation (Dunsmuir v. Evidence spans paragraphs 29-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4553066` offsets `40-46`; context: [28] The Applicant raises the following issues:
Did the RAD err in its assessment of the admissibility of new evidence pursuant to subsection 110(4) of the IRPA?
- Evidence: `party_position` cue `claim` at chunk `4553066` offsets `321-326`; context: Did the RAD err in refusing to assess the Applicant’s sur place claim?
- Evidence: `evidence_fact` cue `evidence` at chunk `4553066` offsets `110-118`; context: [28] The Applicant raises the following issues:
Did the RAD err in its assessment of the admissibility of new evidence pursuant to subsection 110(4) of the IRPA?
- Evidence: `governing_rule` cue `pursuant to` at chunk `4553066` offsets `119-130`; context: [28] The Applicant raises the following issues:
Did the RAD err in its assessment of the admissibility of new evidence pursuant to subsection 110(4) of the IRPA?
- Evidence: `issue` cue `issues` at chunk `4553067` offsets `51-57`; context: [29] In considering the new evidence and sur place issues, the RAD was interpreting its home statute, as well as the rules enacted thereunder.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553067` offsets `28-36`; context: [29] In considering the new evidence and sur place issues, the RAD was interpreting its home statute, as well as the rules enacted thereunder.
- Evidence: `governing_rule` cue `standard of review` at chunk `4553067` offsets `389-407`; context: Where a tribunal is interpreting its home statute or rules enacted thereunder, there is a presumption that the reasonableness standard of review applies to that interpretation (Dunsmuir v.
- Evidence: `reasoning_application` cue `applies` at chunk `4553067` offsets `408-415`; context: Where a tribunal is interpreting its home statute or rules enacted thereunder, there is a presumption that the reasonableness standard of review applies to that interpretation (Dunsmuir v.

#### 10970:3:subtheme:2 · paragraphs 31-33

- Raw key terms: `evidence, admissibility, court, para, reasonableness, acceptable, accepted, accordingly`
- Display key terms: `admissibility, para, reasonableness, acceptable, accepted, accordingly`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: admissibility, para, reasonableness, acceptable, accepted, accordingly Position/evidence statements: [32] The Applicant submits the new evidence presented to the RAD should have been admitted. Application context: Accordingly, all three issues must be reviewed on a standard of reasonableness. | For the reasons set out below, I conclude the RAD reasonably decided the requirements of subsection 110(4) of the IRPA were not met. Evidence spans paragraphs 31-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4553068` offsets `87-94`; context: [30] Moreover, this Court has stated that the role of the Court is not to re-determine whether new evidence should have been accepted, but to determine whether the RAD’s ﬁndings on the admissibility of new evidence are reasonable (Walite v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553068` offsets `99-107`; context: [30] Moreover, this Court has stated that the role of the Court is not to re-determine whether new evidence should have been accepted, but to determine whether the RAD’s ﬁndings on the admissibility of new evidence are reasonable (Walite v.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4553068` offsets `774-785`; context: Accordingly, all three issues must be reviewed on a standard of reasonableness.
- Evidence: `counterargument_limitation` cue `but` at chunk `4553068` offsets `135-138`; context: [30] Moreover, this Court has stated that the role of the Court is not to re-determine whether new evidence should have been accepted, but to determine whether the RAD’s ﬁndings on the admissibility of new evidence are reasonable (Walite v.
- Evidence: `issue` cue `issue` at chunk `4553069` offsets `14-19`; context: [31] Where an issue attracts a reasonableness review, the Court must give due consideration to the justification, transparency and intelligibility of the decision-making process, and intervene only if the decision falls outside “a range of possible, acceptable outcomes which are defensible in respect of the facts and the law” (Dunsmuir at para.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553069` offsets `417-425`; context: Did the RAD err in its assessment of the admissibility of new evidence?
- Evidence: `party_position` cue `submits` at chunk `4553070` offsets `19-26`; context: [32] The Applicant submits the new evidence presented to the RAD should have been admitted.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553070` offsets `35-43`; context: [32] The Applicant submits the new evidence presented to the RAD should have been admitted.
- Evidence: `reasoning_application` cue `conclude` at chunk `4553070` offsets `304-312`; context: For the reasons set out below, I conclude the RAD reasonably decided the requirements of subsection 110(4) of the IRPA were not met.

#### 10970:3:subtheme:3 · paragraphs 34-37

- Raw key terms: `applicant, evidence, decision, relation, admissibility, available, canada, citizenship`
- Display key terms: `relation, admissibility, available`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: relation, admissibility, available Rule/authority context: An appellant may present only evidence that arose, was not reasonably available or could not have been reasonably expected under the circumstances until, after the rejection of the claim. Application context: It was reasonable for the RAD to conclude the documents were not new, even where they post-dated the decision, because the information contained therein either pre-dated the RPD’s decision or contained information that c Evidence spans paragraphs 34-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4553071` offsets `847-854`; context: Without further information regarding dates on which the evidence became available to the Applicant, how it came to his attention, or why it was not available until after the rejection of his claim, it was impossible for the RAD to determine whether the requirements of subsection 110(4) were met.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4553071` offsets `54-63`; context: [33] The RAD considered statements in the Applicant’s affidavit that some of the new evidence was not available until after the RPD hearing.
- Evidence: `governing_rule` cue `under` at chunk `4553071` offsets `321-326`; context: An appellant may present only evidence that arose, was not reasonably available or could not have been reasonably expected under the circumstances until, after the rejection of the claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553072` offsets `87-95`; context: [34] Other arguments advanced by the Applicant in relation to the admissibility of new evidence are made for the first time before this Court.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4553072` offsets `176-182`; context: The Respondent says an applicant cannot advance new grounds, which were not before the RAD, in an attempt to bootstrap the admissibility of that new evidence (Lalonde v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4553073` offsets `134-142`; context: [35] Regardless, I am satisfied the RAD reasonably found it could not consider the eight documents tendered by the Applicant as “new” evidence.
- Evidence: `reasoning_application` cue `conclude` at chunk `4553073` offsets `473-481`; context: It was reasonable for the RAD to conclude the documents were not new, even where they post-dated the decision, because the information contained therein either pre-dated the RPD’s decision or contained information that could not be confirmed as post-dating the decision (Jadallah v.
- Evidence: `evidence_fact` cue `testimony` at chunk `4553074` offsets `144-153`; context: However, he states he has provided credible testimony on every central aspect of his claim.
- Evidence: `counterargument_limitation` cue `However` at chunk `4553074` offsets `100-107`; context: However, he states he has provided credible testimony on every central aspect of his claim.

#### 10970:3:subtheme:4 · paragraphs 38-40

- Raw key terms: `applicant, canada, citizenship, claim, immigration, minister, para, considered`
- Display key terms: `para, considered`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: para, considered Position/evidence statements: [37] Effectively, the Applicant contends the RAD should have assessed his credibility in relation to his sexual orientation in a vacuum, separate and apart from the remainder of his testimony. | [38] The RAD was entitled to draw negative inferences with respect to the Applicant's credibility from the omission of an element that is central to and forms the basis of his Canadian claim (i. Application context: I find the RAD’s credibility assessment was justifiable, transparent and intelligible, and fell within the range of possible, acceptable outcomes. Evidence spans paragraphs 38-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4553075` offsets `318-325`; context: That is to say, the RAD should only have considered the testimony related to his romantic and sexual preferences in deciding whether the Applicant is, on a balance of probabilities, homosexual.
- Evidence: `party_position` cue `contends` at chunk `4553075` offsets `32-40`; context: [37] Effectively, the Applicant contends the RAD should have assessed his credibility in relation to his sexual orientation in a vacuum, separate and apart from the remainder of his testimony.
- Evidence: `evidence_fact` cue `testimony` at chunk `4553075` offsets `182-191`; context: [37] Effectively, the Applicant contends the RAD should have assessed his credibility in relation to his sexual orientation in a vacuum, separate and apart from the remainder of his testimony.
- Evidence: `party_position` cue `claim` at chunk `4553076` offsets `185-190`; context: [38] The RAD was entitled to draw negative inferences with respect to the Applicant's credibility from the omission of an element that is central to and forms the basis of his Canadian claim (i.
- Evidence: `reasoning_application` cue `I find` at chunk `4553076` offsets `926-932`; context: I find the RAD’s credibility assessment was justifiable, transparent and intelligible, and fell within the range of possible, acceptable outcomes.
- Evidence: `party_position` cue `claim` at chunk `4553077` offsets `86-91`; context: [39] I reject the Applicant’s contention the RAD should have considered the sur place claim.

#### 10970:3:subtheme:5 · paragraphs 41-41

- Raw key terms: `acceptable, claim, consider, decision, fell, intelligible, issue, justifiable`
- Display key terms: `acceptable, consider, fell, intelligible, justifiable`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: acceptable, consider, fell, intelligible, justifiable Evidence spans paragraphs 41-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4553078` offsets `203-208`; context: [40] I am of the view the RAD’s decision not to consider the sur place claim was justifiable, transparent and intelligible, and fell within the range of possible, acceptable outcomes in relation to that issue.

#### Section text

[28] The Applicant raises the following issues:
Did the RAD err in its assessment of the admissibility of new evidence pursuant to subsection 110(4) of the IRPA?
Did the RAD err in its assessment of the evidence with respect to the Applicant’s credibility?
Did the RAD err in refusing to assess the Applicant’s sur place claim?
VII. Analysis
A. Standard of Review

[29] In considering the new evidence and sur place issues, the RAD was interpreting its home statute, as well as the rules enacted thereunder. Specifically, it was interpreting subsection 110(4) of the IRPA, as well as Rules 3(3)(g)(i) and (ii) of the RAD Rules. Where a tribunal is interpreting its home statute or rules enacted thereunder, there is a presumption that the reasonableness standard of review applies to that interpretation (Dunsmuir v. New Brunswick, 2008 SCC 9, [2008] 1 S.C.R. 190 at para. 54 [Dunsmuir]; Huruglica at paras 30-33; Singh at para. 23; Deng v. Canada (Minister of Citizenship and Immigration), 2016 FC 887, [2016] F.C.J. No. 843 at para. 7; Warraich v. Choudhry, 2018 ONSC 1275, [2018] O.J. No. 1071 at para. 11).

[30] Moreover, this Court has stated that the role of the Court is not to re-determine whether new evidence should have been accepted, but to determine whether the RAD’s ﬁndings on the admissibility of new evidence are reasonable (Walite v. Canada (Minister of Citizenship and Immigration), 2017 FC 49, [2017] F.C.J. No. 31 at para. 30; Canada (Minister of Citizenship and Immigration) v. Ali, 2016 FC 709, [2016] F.C.J. No. 711 at paras 29, 48). It has also recognized that the RAD’s credibility findings are reviewable on a reasonableness standard (Deng v. Canada (Minister of Citizenship and Immigration), 2016 FC 887, [2016] F.C.J. No. 843 at paras 6-7; Diedhiou v. Canada (Minister of Citizenship and Immigration), 2016 FC 1198, [2016] F.C.J. No. 1181 at paras 34-35). Accordingly, all three issues must be reviewed on a standard of reasonableness.

[31] Where an issue attracts a reasonableness review, the Court must give due consideration to the justification, transparency and intelligibility of the decision-making process, and intervene only if the decision falls outside “a range of possible, acceptable outcomes which are defensible in respect of the facts and the law” (Dunsmuir at para. 47).
B. Did the RAD err in its assessment of the admissibility of new evidence?

[32] The Applicant submits the new evidence presented to the RAD should have been admitted. The Applicant contends it is clear from his afﬁdavit in support of the appeal and from the new evidence that he met the requirements of subsection 110(4) of the IRPA. I disagree. For the reasons set out below, I conclude the RAD reasonably decided the requirements of subsection 110(4) of the IRPA were not met.

[33] The RAD considered statements in the Applicant’s affidavit that some of the new evidence was not available until after the RPD hearing. The RAD correctly noted this was not the test to be met. An appellant may present only evidence that arose, was not reasonably available or could not have been reasonably expected under the circumstances until, after the rejection of the claim. The Applicant does not explain how the proposed new evidence met this test. Instead, the Applicant’s submissions serve largely to explain the importance of the evidence, and how it was only available after the hearing. Without further information regarding dates on which the evidence became available to the Applicant, how it came to his attention, or why it was not available until after the rejection of his claim, it was impossible for the RAD to determine whether the requirements of subsection 110(4) were met.

[34] Other arguments advanced by the Applicant in relation to the admissibility of new evidence are made for the first time before this Court. The Respondent says an applicant cannot advance new grounds, which were not before the RAD, in an attempt to bootstrap the admissibility of that new evidence (Lalonde v. Canada (Canada Revenue Agency), 2008 FC 183, [2008] F.C.J. No. 316 at para. 66; Jakhu v. Canada (Minister of Citizenship and Immigration), 2009 FC 159, [2009] F.C.J. No. 203 at para. 18). I agree. In addition, an applicant cannot offer new evidence “every time he or she is surprised by the RPD’s decision” (Marin v. Canada (Minister of Citizenship and Immigration), 2016 FC 847, [2016] F.C.J. No. 830 at para. 27; Canada (Minister of Citizenship and Immigration) v. Desalegn, 2016 FC 12, [2016] F.C.J. No. 11 at para. 23; Ozomba v. Canada (Minister of Citizenship and Immigration), 2016 FC 1418, [2016] F.C.J. No. 1442 at para. 18).

[35] Regardless, I am satisfied the RAD reasonably found it could not consider the eight documents tendered by the Applicant as “new” evidence. The documents did not meet the criteria for admissibility set out in subsection 110(4) of the IRPA and in accordance with the decision in Singh. Singh is clear. The requirements of subsection 110(4) leave no room for discretion on the part of the RAD and must be narrowly interpreted (para. 35). It was reasonable for the RAD to conclude the documents were not new, even where they post-dated the decision, because the information contained therein either pre-dated the RPD’s decision or contained information that could not be confirmed as post-dating the decision (Jadallah v. Canada (Minister of Citizenship and Immigration), 2016 FC 1240, [2016] F.C.J. No. 1276 at para. 34). There was also nothing to suggest the documents were not reasonably available or could not reasonably be expected to be available prior to the RPD decision. The RAD’s decision in relation to the admissibility of new evidence was justified, transparent and intelligible, and fell within the range of possible, acceptable outcomes.
C. Did the RAD err in its credibility assessment?

[36] The Applicant acknowledges he has made incomplete statements in relation to some of the facts. However, he states he has provided credible testimony on every central aspect of his claim. The Applicant contends the RAD based its decision with respect to his sexual orientation on speculation and conjecture rather than the evidence.

[37] Effectively, the Applicant contends the RAD should have assessed his credibility in relation to his sexual orientation in a vacuum, separate and apart from the remainder of his testimony. That is to say, the RAD should only have considered the testimony related to his romantic and sexual preferences in deciding whether the Applicant is, on a balance of probabilities, homosexual. He cites Tshibola Kabongo v. Canada (Minister of Citizenship and Immigration), 2012 FC 313, [2012] F.C.J. No. 367 [Tshibola] (para. 7) in support of this contention. The paragraph cited by the Applicant informs us that the RPD is entitled to make findings of implausibility based on rationality and common sense. The Court must intervene where the findings are based on inferences not drawn from the evidence. The negative credibility findings in this case were, in my view, clearly drawn from the evidence. Those credibility findings touch all aspects of the Applicant’s evidence, including his claim of homosexuality.

[38] The RAD was entitled to draw negative inferences with respect to the Applicant's credibility from the omission of an element that is central to and forms the basis of his Canadian claim (i.e., his homosexuality) in his earlier American asylum claim, as well as from the inconsistencies regarding other important elements of his claim (Arabalidoosti v. Canada (Minister of Citizenship and Immigration), 2006 FC 440, [2006] F.C.J. No. 552 at para. 1; Osman v. Canada (Minister of Citizenship and Immigration), 2008 FC 921, [2008] F.C.J. No. 1134 at paras 36, 38 and 39; Kumar v. Canada (Minister of Citizenship and Immigration), 2009 FC 1063, [2009] F.C.J. No. 1457 at paras 6, 8 and 14; Gabriel v. Canada (Minister of Citizenship and Immigration), 2009 FC 232, [2009] F.C.J. No. 247 at paras 5, 10-11 and 13; Bikoko v. Canada (Minister of Citizenship and Immigration), 2015 FC 1313, [2015] F.C.J. No. 1370 at paras 9-10). I find the RAD’s credibility assessment was justifiable, transparent and intelligible, and fell within the range of possible, acceptable outcomes.
D. Did the RAD err in refusing to assess the Applicant’s sur place claim?

[39] I reject the Applicant’s contention the RAD should have considered the sur place claim. The Applicant did not challenge, in accordance with Rules 3(3)(g)(i) and (ii) of the RAD Rules, the RPD’s finding in this regard. The responsibility rests with the appellant to raise any potential grounds of appeal that arise from the RPD decision. The RAD has no responsibility to consider other grounds (Dhillon v. Canada (Minister of Citizenship and Immigration), 2015 FC 321, [2015] F.C.J. No. 286 [Dhillon] at paras 18-20; Huruglica at para. 103; Ghauri v. Canada (Minister of Citizenship and Immigration), 2016 FC 548, [2016] F.C.J. No. 529 [Ghauri] at paras 33-34; Murugesu v. Canada (Minister of Citizenship and Immigration), 2016 FC 819, [2016] F.C.J. No. 885 [Murugesu] at paras 25-27; Dakpokpo v. Canada (Minister of Citizenship and Immigration), 2017 FC 580, [2017] F.C.J. No. 632 at para. 14; Liu v. Canada (Minister of Citizenship and Immigration), 2017 FC 736, [2017] F.C.J. No. 768 at para. 25).

[40] I am of the view the RAD’s decision not to consider the sur place claim was justifiable, transparent and intelligible, and fell within the range of possible, acceptable outcomes in relation to that issue.


## 10970:4 · paragraphs 42-43

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ed92cc79614fe8d0aad4ac0562c2b813b7fa60824dadf935549846befa14c15f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10970:4:subtheme:1 · paragraphs 42-43

- Raw key terms: `appeal, applicant, application, certified, conclusion, consideration, costs, court`
- Display key terms: `certified, conclusion, consideration, costs`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: certified, conclusion, consideration, costs Operative outcome context: [41] For the foregoing reasons, the Applicant’s application for judicial review is dismissed without costs. Evidence spans paragraphs 42-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4553079` offsets `111-119`; context: No question is certified for consideration by the Federal Court of Appeal.
- Evidence: `disposition` cue `dismissed` at chunk `4553079` offsets `83-92`; context: [41] For the foregoing reasons, the Applicant’s application for judicial review is dismissed without costs.

#### Section text

VIII. Conclusion

[41] For the foregoing reasons, the Applicant’s application for judicial review is dismissed without costs. No question is certified for consideration by the Federal Court of Appeal.


## 10970:5 · paragraphs 44-45

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7168ea1da6f1580fde17ca3bf53bdf1d5ae32ea6bcbcaaf0fde2692bac63f837`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10970:5:subtheme:1 · paragraphs 44-45

- Raw key terms: `cause, hearing, imm-5152-17, immigration, minister, reasons, record, accept`
- Display key terms: `hearing, imm-5152-17, accept`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: hearing, imm-5152-17, accept No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 44-45. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT in IMM-5152-17
THIS COURT’S JUDGMENT is that the Application for Judicial Review is dismissed without costs. No question of general importance is certified for consideration by the Federal Court of Appeal.
“B. Richard Bell”
Judge
ANNEX A
Immigration and Refugee Protection Act, S.C. 2001, c. 27
Loi sur l’immigration et la protection des réfugiés, L.C. 2001, ch. 27
Convention refugee
96 A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
Définition de réfugié
96 A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
[…]
[…]
Person in need of protection
97 (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
Personne à protéger
97 (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
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
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
[…]
[…]
Procedure
110 (3) Subject to subsections (3.1), (4) and (6), the Refugee Appeal Division must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division, and may accept documentary evidence and written submissions from the Minister and the person who is the subject of the appeal and, in the case of a matter that is conducted before a panel of three members, written submissions from a representative or agent of the United Nations High Commissioner for Refugees and any other person described in the rules of the Board.
Fonctionnement
110 (3) Sous réserve des paragraphes (3.1), (4) et (6), la section procède sans tenir d’audience en se fondant sur le dossier de la Section de la protection des réfugiés, mais peut recevoir des éléments de preuve documentaire et des observations écrites du ministre et de la personne en cause ainsi que, s’agissant d’une affaire tenue devant un tribunal constitué de trois commissaires, des observations écrites du représentant ou mandataire du Haut-Commissariat des Nations Unies pour les réfugiés et de toute autre personne visée par les règles de la Commission.
[…]
[…]
Evidence that may be presented
110 (4) On appeal, the person who is the subject of the appeal may present only evidence that arose after the rejection of their claim or that was not reasonably available, or that the person could not reasonably have been expected in the circumstances to have presented, at the time of the rejection.
Éléments de preuve admissibles
110 (4) Dans le cadre de l’appel, la personne en cause ne peut présenter que des éléments de preuve survenus depuis le rejet de sa demande ou qui n’étaient alors pas normalement accessibles ou, s’ils l’étaient, qu’elle n’aurait pas normalement présentés, dans les circonstances, au moment du rejet.
[…]
[…]
Hearing
110 (6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
Audience
110(6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause;
(b) that is central to the decision with respect to the refugee protection claim; and
b) sont essentiels pour la prise de la décision relative à la demande d’asile;
(c) that, if accepted, would justify allowing or rejecting the refugee protection claim.
c) à supposer qu’ils soient admis, justifieraient que la demande d’asile soit accordée ou refusée, selon le cas.
[…]
[…]
Decision
111 (1) After considering the appeal, the Refugee Appeal Division shall make one of the following decisions:
Décision
111 (1) La Section d’appel des réfugiés confirme la décision attaquée, casse la décision et y substitue la décision qui aurait dû être rendue ou renvoie, conformément à ses instructions, l’affaire à la Section de la protection des réfugiés.
(a) confirm the determination of the Refugee Protection Division;
EN BLANC
(b) set aside the determination and substitute a determination that, in its opinion, should have been made; or
EN BLANC
(c) refer the matter to the Refugee Protection Division for re-determination, giving the directions to the Refugee Protection Division that it considers appropriate.
EN BLANC
Referrals
111 (2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
Renvoi
111 (2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
b) qu’elle ne peut confirmer la décision attaquée ou casser la décision et y substituer la décision qui aurait dû être rendue sans tenir une nouvelle audience en vue du réexamen des éléments de preuve qui ont été présentés à la Section de la protection des réfugiés.
Refugee Appeal Division Rules, SOR/2012-257
Règles de la Section d’appel des réfugiés, DORS/2012-257
Content of appellant’s record
3 (3) The appellant’s record must contain the following documents, on consecutively numbered pages, in the following order:
Contenu du dossier de l’appelant
3 (3) Le dossier de l’appelant comporte les documents ci-après, sur des pages numérotées consécutivement, dans l’ordre qui suit :
[…]
[…]
(g) a memorandum that includes full and detailed submissions regarding
g) un mémoire qui inclut des observations complètes et détaillées concernant :
(i) the errors that are the grounds of the appeal,
(i) les erreurs commises qui constituent les motifs d’appel,
(ii) where the errors are located in the written reasons for the Refugee Protection Division’s decision that the appellant is appealing or in the transcript or in any audio or other electronic recording of the Refugee Protection Division hearing,
(ii) l’endroit où se trouvent ces erreurs dans les motifs écrits de la décision de la Section de la protection des réfugiés portée en appel ou dans la transcription ou dans tout enregistrement audio ou électronique de l’audience tenue devant cette dernière,
(iii) how any documentary evidence referred to in paragraph (e) meets the requirements of subsection 110(4) of the Act and how that evidence relates to the appellant,
(iii) la façon dont les éléments de preuve documentaire visés à l’alinéa e) sont conformes aux exigences du paragraphe 110(4) de la Loi et la façon dont ils sont liés à l’appelant,
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-5152-17
STYLE OF CAUSE:
MOHAMMED KAMAL DEEN ILIAS v MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Montréal, Quebec
DATE OF HEARING:
JUNE 4, 2018
REASONS FOR 

## 10970:6 · paragraphs 46-46

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `cbf7e08833c162c0d2e7c97a674b34d69ad3a88500e632e1cb0adfcf0936e497`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10970:6:subtheme:1 · paragraphs 46-46

- Raw key terms: `anne, anne-ren, appearances, applicant, attorney, bell, camille, canada`
- Display key terms: `anne, anne-ren, bell, camille`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: anne, anne-ren, bell, camille No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 46-46. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND JUDGMENT:
BELL J.
DATED:
June 27, 2018
APPEARANCES:
Me Camille Larouche
For The Applicant
Me Anne-Renée Touchette
For The Respondent
SOLICITORS OF RECORD:
Me Anne Castagner
Étude Légale Stewart Istvanffy
Montreal, Quebec
For The Applicant
Attorney General of Canada
Montreal, Quebec
For The Respondent
