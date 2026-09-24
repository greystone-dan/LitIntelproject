# Discussion Units: case 12076

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **35**
- Continuity pairs: **34**
- Discussion Units: **3**
- Paragraph source hashes: **35**
- Sub-themes: **9**

## 12076:1 · paragraphs 0-11

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3bfd2f8e2a1be714924b43fc275b5ad56112b999329d56e7ac50ade3f4004cf6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12076:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `applicant, court, dated, application, august, china, counsel, date`
- Display key terms: `dated, august, china, date`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: dated, august, china, date Position/evidence statements: [5] The Applicant claims that in August 2012 he was introduced to Christianity by his friend as well as his father’s friend. Rule/authority context: [1] This is a judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board [the Board] dated September 23, 2014, wherein it was determined that the Applicant is not a Convention R | His previous counsel was removed as Solicitor of Record for the Applicant by Order of Prothonotary Aalto dated August 25, 2015 pursuant to Rule 125 of the Federal Court Rules, SOR/98-106 [Rules]. Application context: I am satisfied that this requirement is met, as the Order dated June 30, 2015 granting leave in this matter and setting the hearing date was sent by facsimile on June 30 to the Applicant’s then solicitor of record, which Operative outcome context: [1] For the reasons that follow, this application is dismissed. Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `4604402` offsets `169-184`; context: [1] This is a judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board [the Board] dated September 23, 2014, wherein it was determined that the Applicant is not a Convention Refugee pursuant to section 96 of the Immigration and Refugee Protection Act 2001 c 27 [IRPA] and is not a person in need of protection under section 97 of the IRPA.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4604402` offsets `227-238`; context: [1] This is a judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board [the Board] dated September 23, 2014, wherein it was determined that the Applicant is not a Convention Refugee pursuant to section 96 of the Immigration and Refugee Protection Act 2001 c 27 [IRPA] and is not a person in need of protection under section 97 of the IRPA.
- Evidence: `evidence_fact` cue `Record` at chunk `4604403` offsets `278-284`; context: His previous counsel was removed as Solicitor of Record for the Applicant by Order of Prothonotary Aalto dated August 25, 2015 pursuant to Rule 125 of the Federal Court Rules, SOR/98-106 [Rules].
- Evidence: `governing_rule` cue `pursuant to` at chunk `4604403` offsets `356-367`; context: His previous counsel was removed as Solicitor of Record for the Applicant by Order of Prothonotary Aalto dated August 25, 2015 pursuant to Rule 125 of the Federal Court Rules, SOR/98-106 [Rules].
- Evidence: `disposition` cue `dismissed` at chunk `4604403` offsets `53-62`; context: [1] For the reasons that follow, this application is dismissed.
- Evidence: `evidence_fact` cue `record` at chunk `4604404` offsets `963-969`; context: I am satisfied that this requirement is met, as the Order dated June 30, 2015 granting leave in this matter and setting the hearing date was sent by facsimile on June 30 to the Applicant’s then solicitor of record, which represents effective service upon the Applicant and therefore notice in accordance with the Rules.
- Evidence: `reasoning_application` cue `therefore` at chunk `4604404` offsets `1029-1038`; context: I am satisfied that this requirement is met, as the Order dated June 30, 2015 granting leave in this matter and setting the hearing date was sent by facsimile on June 30 to the Applicant’s then solicitor of record, which represents effective service upon the Applicant and therefore notice in accordance with the Rules.
- Evidence: `party_position` cue `claims` at chunk `4604405` offsets `18-24`; context: [5] The Applicant claims that in August 2012 he was introduced to Christianity by his friend as well as his father’s friend.

#### 12076:1:subtheme:2 · paragraphs 5-8

- Raw key terms: `applicant, board, christian, church, identity, alleged, attended, baptism`
- Display key terms: `christian, church, identity, alleged, attended, baptism`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: christian, church, identity, alleged, attended, baptism Application context: However, based on his testimony, it did not believe that he is a Pentecostal Christian, because he exhibited a very limited knowledge of the religion and was unable to answer very basic questions concerning his faith. Evidence spans paragraphs 5-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4604406` offsets `249-254`; context: Impugned Decision [7] The Board’s decision reflects that the determinative issue was the Applicant’s credibility as it directly related to his identity as a Christian.
- Evidence: `evidence_fact` cue `testimony` at chunk `4604407` offsets `94-103`; context: However, based on his testimony, it did not believe that he is a Pentecostal Christian, because he exhibited a very limited knowledge of the religion and was unable to answer very basic questions concerning his faith.
- Evidence: `reasoning_application` cue `because` at chunk `4604407` offsets `160-167`; context: However, based on his testimony, it did not believe that he is a Pentecostal Christian, because he exhibited a very limited knowledge of the religion and was unable to answer very basic questions concerning his faith.
- Evidence: `counterargument_limitation` cue `However` at chunk `4604407` offsets `72-79`; context: However, based on his testimony, it did not believe that he is a Pentecostal Christian, because he exhibited a very limited knowledge of the religion and was unable to answer very basic questions concerning his faith.
- Evidence: `evidence_fact` cue `found that` at chunk `4604408` offsets `456-466`; context: The Board found that, if he were a true Pentecostal, he would have been able to provide a more detailed description of Pentecost and would have been able to recall the date on which it occurs;
C.
- Evidence: `counterargument_limitation` cue `but` at chunk `4604408` offsets `340-343`; context: The Applicant stated that Pentecost was a date to commemorate Jesus, but he did not know when Pentecost occurred and stated that it was not an important date to Pentecostals.

#### 12076:1:subtheme:3 · paragraphs 9-11

- Raw key terms: `review, standard, applicable, applicant, evidence, fairness, knowledge, made`
- Display key terms: `review, standard, applicable, fairness, knowledge, made`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: review, standard, applicable, fairness, knowledge, made Position/evidence statements: With respect to the procedural fairness issue, the Applicant submits that the applicable standard of review is correctness. Rule/authority context: [11] The Board concluded by determining that the Applicant is not a Convention Refugee and is not a person in need of protection under section 96 or 97 of IRPA. | [13] The parties agree that the applicable standard of review is reasonableness for assessing evidence including credibility and genuineness of faith (Hou v Canada (MCI), 2012 FC 993 [Hou] at para 8 and 15). Application context: In view of its finding that the Applicant was not a Christian as alleged, the Board also found pursuant to section 107(2) of IRPA that there was no credible or trustworthy evidence upon which a favourable decision could  Evidence spans paragraphs 9-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4604410` offsets `464-470`; context: Issues and Standard of Review [12] In my view, the Applicant’s arguments (canvassed below) amount to a consideration of whether there was a breach of procedural fairness by the Board (by failing to alert the Applicant to the use of specialized knowledge about Pentecostal Christianity) and whether the Board’s decision was reasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4604410` offsets `333-341`; context: In view of its finding that the Applicant was not a Christian as alleged, the Board also found pursuant to section 107(2) of IRPA that there was no credible or trustworthy evidence upon which a favourable decision could have been made and, therefore, that there was no credible basis for the claim.
- Evidence: `governing_rule` cue `under` at chunk `4604410` offsets `129-134`; context: [11] The Board concluded by determining that the Applicant is not a Convention Refugee and is not a person in need of protection under section 96 or 97 of IRPA.
- Evidence: `reasoning_application` cue `therefore` at chunk `4604410` offsets `401-410`; context: In view of its finding that the Applicant was not a Christian as alleged, the Board also found pursuant to section 107(2) of IRPA that there was no credible or trustworthy evidence upon which a favourable decision could have been made and, therefore, that there was no credible basis for the claim.
- Evidence: `issue` cue `issue` at chunk `4604411` offsets `248-253`; context: With respect to the procedural fairness issue, the Applicant submits that the applicable standard of review is correctness.
- Evidence: `party_position` cue `submits` at chunk `4604411` offsets `269-276`; context: With respect to the procedural fairness issue, the Applicant submits that the applicable standard of review is correctness.
- Evidence: `evidence_fact` cue `evidence` at chunk `4604411` offsets `94-102`; context: [13] The parties agree that the applicable standard of review is reasonableness for assessing evidence including credibility and genuineness of faith (Hou v Canada (MCI), 2012 FC 993 [Hou] at para 8 and 15).
- Evidence: `governing_rule` cue `standard of review` at chunk `4604411` offsets `43-61`; context: [13] The parties agree that the applicable standard of review is reasonableness for assessing evidence including credibility and genuineness of faith (Hou v Canada (MCI), 2012 FC 993 [Hou] at para 8 and 15).
- Evidence: `governing_rule` cue `standard of review` at chunk `4604412` offsets `58-76`; context: [14] I accept the parties’ articulation of the applicable standard of review.

#### Section text

Gao v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2015-10-06
Neutral citation
2015 FC 1139
File numbers
IMM-7310-14
Decision Content
Date: 20151006
Docket: IMM-7310-14
Citation: 2015 FC 1139
Ottawa, Ontario, October 6, 2015
PRESENT: The Honourable Mr. Justice Southcott
BETWEEN:
MENGMENG GAO
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] This is a judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board [the Board] dated September 23, 2014, wherein it was determined that the Applicant is not a Convention Refugee pursuant to section 96 of the Immigration and Refugee Protection Act 2001 c 27 [IRPA] and is not a person in need of protection under section 97 of the IRPA.

[1] For the reasons that follow, this application is dismissed.
I. Preliminary Matter [2] As a preliminary matter, I note that the Applicant did not appear at the hearing of this application, either in person or through counsel. His previous counsel was removed as Solicitor of Record for the Applicant by Order of Prothonotary Aalto dated August 25, 2015 pursuant to Rule 125 of the Federal Court Rules, SOR/98-106 [Rules]. That Order was issued upon motion by the Applicant’s former counsel, supported by evidence that his counsel has been unable to reach the Applicant or obtain instructions from him and that correspondence to the Applicant at his last known address had been returned with an indication that the intended recipient had moved.

[3] The Respondent took the position that the Court should consider dismissing the application on the basis that it had been abandoned by the Applicant. With the Court’s permission, the Respondent has filed submissions on abandonment and, after considering same, I am of the view that the better approach is to proceed to decide the application based on the written materials, including a Memorandum of Fact and Law previously filed by the Applicant’s counsel on his behalf, and the Respondent’s oral submissions. In doing so, I note that the Respondent has correctly referred to Rule 38 as permitting the Court to proceed in the absence of a party if the Court is satisfied that notice of the hearing was given to that party in accordance with the Rules. I am satisfied that this requirement is met, as the Order dated June 30, 2015 granting leave in this matter and setting the hearing date was sent by facsimile on June 30 to the Applicant’s then solicitor of record, which represents effective service upon the Applicant and therefore notice in accordance with the Rules.
II. Background [4] The twenty-two year old Applicant is a citizen of the People’s Republic of China. He alleges that he faces persecution in China due to his religious activities as a Pentecostal Christian.

[5] The Applicant claims that in August 2012 he was introduced to Christianity by his friend as well as his father’s friend. After some conversations, the Applicant decided to attend their house church. In January 2013, he accepted his parents’ plan for him to work abroad and on March 4, 2013 obtained a passport. The Applicant continued to attend services regularly every Sunday. On March 10, 2013, the Applicant’s house church was discovered by the state authorities. He subsequently went into hiding and left China through a smuggler on September 26, 2013.

[6] After arriving in Canada, the Applicant made his claim for refugee protection and joined a church in Toronto. He was baptized and continued to attend services here.
III. Impugned Decision [7] The Board’s decision reflects that the determinative issue was the Applicant’s credibility as it directly related to his identity as a Christian.

[8] The Board accepted the Applicant’s identity as a national of China. However, based on his testimony, it did not believe that he is a Pentecostal Christian, because he exhibited a very limited knowledge of the religion and was unable to answer very basic questions concerning his faith. Considering that the Applicant alleged that he was practising Pentecostalism for a year, read the Bible every day, attended church every Sunday, volunteered with the church in Canada and has been baptised, the Board expected him to have knowledge of basic beliefs of his religion. However, the Board concluded that he did not.

[9] Specifically, the Board’s conclusions were as follows:
A. The Board drew a negative inference from the Applicant’s lack of knowledge as to why attending church on Sunday is important to Christians and found this to be an indication he was not a genuine Christian;
B. The Applicant stated that Pentecost was a date to commemorate Jesus, but he did not know when Pentecost occurred and stated that it was not an important date to Pentecostals. The Board found that, if he were a true Pentecostal, he would have been able to provide a more detailed description of Pentecost and would have been able to recall the date on which it occurs;
C. The Applicant stated there were no prayers recited by Pentecostals other than the Lord’s Prayer and referred to discussion of the Ten Commandments. The Board noted that the Ten Commandments are commandments to be obeyed, not prayers to be recited;
D. The Applicant stated that baptism and communion are the only rites performed by Pentecostals and could not explain why communion is taken; and,
E. The Applicant could not recall a date besides December 25 which is important to his faith. The Board concluded as a result that he had not attended church every Sunday as alleged and was not a genuine Christian.

[10] The Board did not give any weight to a Certificate of Baptism issued by his Canadian church. Neither the baptism nor a letter from his church overcame the credibility concerns about the Applicant’s Christian identity.

[11] The Board concluded by determining that the Applicant is not a Convention Refugee and is not a person in need of protection under section 96 or 97 of IRPA. In view of its finding that the Applicant was not a Christian as alleged, the Board also found pursuant to section 107(2) of IRPA that there was no credible or trustworthy evidence upon which a favourable decision could have been made and, therefore, that there was no credible basis for the claim.
IV. Issues and Standard of Review [12] In my view, the Applicant’s arguments (canvassed below) amount to a consideration of whether there was a breach of procedural fairness by the Board (by failing to alert the Applicant to the use of specialized knowledge about Pentecostal Christianity) and whether the Board’s decision was reasonable.

[13] The parties agree that the applicable standard of review is reasonableness for assessing evidence including credibility and genuineness of faith (Hou v Canada (MCI), 2012 FC 993 [Hou] at para 8 and 15). With respect to the procedural fairness issue, the Applicant submits that the applicable standard of review is correctness. The Respondent agrees, referring in particular to the taking of judicial notice of “specialized knowledge” , without prior notification to the parties, as being reviewable under the standard of correctness, but notes that the use made of the “specialized knowledge” is reviewable under the standard of reasonableness (Toma v Canada (MCI), 2014 FC 121 at paras 3 and 7).

[14] I accept the parties’ articulation of the applicable standard of review.


## 12076:2 · paragraphs 12-33

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f1723548859549ae3d8cbfd08ecd6bdbedd2021b5accbe369d0367375bf05b52`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12076:2:subtheme:1 · paragraphs 12-14

- Raw key terms: `applicant, board, knowledge, argues, pentecostalism, actually, address, alert`
- Display key terms: `knowledge, argues, pentecostalism, actually, address, alert`
- Argument roles: `counterargument_limitation, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, party_position, reasoning_application Display terms: knowledge, argues, pentecostalism, actually, address, alert Position/evidence statements: The Applicant’s Position [15] The Applicant argues that the Board failed to alert him to its reliance on specialized knowledge about Pentecostalism. | [16] The Applicant also argues that the Board’s overall assessment of the Applicant’s Christian identity was unreasonable. Application context: It chose to rely on the Applicant’s testimony instead of other evidence and its questions did not address basic knowledge but rather applied too high a threshold of required religious knowledge, which has been found to r Evidence spans paragraphs 12-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `argues` at chunk `4604412` offsets `155-161`; context: The Applicant’s Position [15] The Applicant argues that the Board failed to alert him to its reliance on specialized knowledge about Pentecostalism.
- Evidence: `party_position` cue `argues` at chunk `4604413` offsets `24-30`; context: [16] The Applicant also argues that the Board’s overall assessment of the Applicant’s Christian identity was unreasonable.
- Evidence: `evidence_fact` cue `testimony` at chunk `4604413` offsets `159-168`; context: It chose to rely on the Applicant’s testimony instead of other evidence and its questions did not address basic knowledge but rather applied too high a threshold of required religious knowledge, which has been found to represent a reviewable error.
- Evidence: `reasoning_application` cue `applied` at chunk `4604413` offsets `256-263`; context: It chose to rely on the Applicant’s testimony instead of other evidence and its questions did not address basic knowledge but rather applied too high a threshold of required religious knowledge, which has been found to represent a reviewable error.
- Evidence: `counterargument_limitation` cue `but` at chunk `4604413` offsets `245-248`; context: It chose to rely on the Applicant’s testimony instead of other evidence and its questions did not address basic knowledge but rather applied too high a threshold of required religious knowledge, which has been found to represent a reviewable error.
- Evidence: `party_position` cue `submits` at chunk `4604414` offsets `27-34`; context: [17] The Applicant further submits that the Board itself lacked knowledge and understanding of Pentecostalism.

#### 12076:2:subtheme:2 · paragraphs 15-21

- Raw key terms: `applicant, board, decision, justice, religious, respondent, assessing, faith`
- Display key terms: `justice, religious, assessing, faith`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: justice, religious, assessing, faith Position/evidence statements: [18] Finally, the Applicant submits that the Board misapplied the test for a “no credible basis” finding. | [20] On the substantive issue, the Respondent submits that the Board reasonably assessed the genuineness of the Applicant’s religious faith. Application context: The case law is clear that the Board may not simply extend its credibility findings to the entirety of the evidence and on that basis conclude that there is no credible basis. | In Wang the applicant was determined not to be a Christian because the RPD found he incorrectly answered questions about “transubstantiation”. Evidence spans paragraphs 15-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4604415` offsets `477-482`; context: Respondent’s Position [19] On the procedural fairness issue, the Respondent submits that the Board did not make use of specialized knowledge in assessing the genuineness of the Applicant’s religious faith.
- Evidence: `party_position` cue `submits` at chunk `4604415` offsets `28-35`; context: [18] Finally, the Applicant submits that the Board misapplied the test for a “no credible basis” finding.
- Evidence: `evidence_fact` cue `evidence` at chunk `4604415` offsets `213-221`; context: The case law is clear that the Board may not simply extend its credibility findings to the entirety of the evidence and on that basis conclude that there is no credible basis.
- Evidence: `reasoning_application` cue `conclude` at chunk `4604415` offsets `240-248`; context: The case law is clear that the Board may not simply extend its credibility findings to the entirety of the evidence and on that basis conclude that there is no credible basis.
- Evidence: `issue` cue `issue` at chunk `4604416` offsets `24-29`; context: [20] On the substantive issue, the Respondent submits that the Board reasonably assessed the genuineness of the Applicant’s religious faith.
- Evidence: `party_position` cue `submits` at chunk `4604416` offsets `46-53`; context: [20] On the substantive issue, the Respondent submits that the Board reasonably assessed the genuineness of the Applicant’s religious faith.
- Evidence: `party_position` cue `argues` at chunk `4604417` offsets `20-26`; context: [21] The Respondent argues that the Board reasonably assessed the probative value of evidence and reasonably determined that the claim had no credible basis.
- Evidence: `evidence_fact` cue `evidence` at chunk `4604417` offsets `85-93`; context: [21] The Respondent argues that the Board reasonably assessed the probative value of evidence and reasonably determined that the claim had no credible basis.
- Evidence: `evidence_fact` cue `found that` at chunk `4604418` offsets `924-934`; context: Indeed, in Penghui Wu v Minister of Citizenship and Immigration, 2009 FC 929, Justice Kelen found that assessing a genuine Christian by way of “trivia” is contrary to law.
- Evidence: `reasoning_application` cue `because` at chunk `4604418` offsets `1284-1291`; context: In Wang the applicant was determined not to be a Christian because the RPD found he incorrectly answered questions about “transubstantiation”.
- Evidence: `party_position` cue `submits` at chunk `4604420` offsets `1623-1630`; context: As the Respondent submits, testimony lacking in detail that would reasonably be expected of a person in the claimant’s position is a basis for rejecting claims as non-credible even if the Applicant was able to answer some other questions, and with great detail.
- Evidence: `evidence_fact` cue `evidence` at chunk `4604420` offsets `1194-1202`; context: Absent a showing of disregard for the evidence, or a misapprehension of the facts, I am unwilling to disturb the Board’s conclusion in this regard – again deference is warranted.

#### 12076:2:subtheme:3 · paragraphs 22-24

- Raw key terms: `applicant, assessing, board, canada, citizenship, genuine, immigration, justice`
- Display key terms: `assessing, genuine, justice`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: assessing, genuine, justice Evidence spans paragraphs 22-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4604422` offsets `497-504`; context: The questions asked by the Board were not to gage the correctness of his beliefs, but rather to determine whether the applicant understood the basic tenants of Christianity.

#### 12076:2:subtheme:4 · paragraphs 25-31

- Raw key terms: `applicant, board, claim, conclusion, canada, citizenship, evidence, genuineness`
- Display key terms: `conclusion, genuineness`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: conclusion, genuineness Position/evidence statements: The applicant submits that the member should have accorded deference to the Pastor’s opinion and taken the baptismal certificate at face value. Rule/authority context: [26] My reading of the jurisprudence is that it is not improper for the Board to engage in religious questioning in an effort to gauge the genuineness of a claimant’s beliefs, but that such questioning and resulting anal | However, its conclusion that he is not a genuine Christian, based on his lack of overall knowledge of the Christian religion, is reasonable and consistent with the jurisprudence. Application context: [28] Turning to the Applicant’s submissions on procedural fairness, I cannot conclude this argument to have merit. Evidence spans paragraphs 25-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4604425` offsets `287-294`; context: [26] My reading of the jurisprudence is that it is not improper for the Board to engage in religious questioning in an effort to gauge the genuineness of a claimant’s beliefs, but that such questioning and resulting analysis must indeed focus on the genuineness of those beliefs and not whether they are theologically correct.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4604425` offsets `23-36`; context: [26] My reading of the jurisprudence is that it is not improper for the Board to engage in religious questioning in an effort to gauge the genuineness of a claimant’s beliefs, but that such questioning and resulting analysis must indeed focus on the genuineness of those beliefs and not whether they are theologically correct.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4604426` offsets `773-786`; context: However, its conclusion that he is not a genuine Christian, based on his lack of overall knowledge of the Christian religion, is reasonable and consistent with the jurisprudence.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4604427` offsets `420-433`; context: Given my conclusion that this questioning and the resulting analysis were within the boundaries contemplated by the jurisprudence, I do not consider this to be reliance on specialized knowledge.
- Evidence: `reasoning_application` cue `conclude` at chunk `4604427` offsets `77-85`; context: [28] Turning to the Applicant’s submissions on procedural fairness, I cannot conclude this argument to have merit.
- Evidence: `governing_rule` cue `under` at chunk `4604428` offsets `57-62`; context: [29] Finally, I can find no fault in the Board`s finding under section 107(2) of IRPA that there was no credible basis for the Applicant’s claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4604429` offsets `242-250`; context: summarised his understanding of the law as follows:
In my view, what Sheikh, tells us is that when the only evidence linking the applicant to the harm he or she alleges is found in the claimant's own testimony and the claimant is found to be not credible, the Refugee Division may, after examining the documentary evidence make a general finding that there is no credible basis for the claim.
- Evidence: `counterargument_limitation` cue `however` at chunk `4604429` offsets `598-605`; context: In cases where there is independent and credible documentary evidence, however, the panel may not make a no credible basis finding.
- Evidence: `evidence_fact` cue `evidence` at chunk `4604430` offsets `68-76`; context: [30] The Applicant’s submissions note that he had filed documentary evidence in support of his claim, including a baptismal certificate and church letters.
- Evidence: `counterargument_limitation` cue `However` at chunk `4604430` offsets `156-163`; context: However, the Board asked the Applicant how his pastor was able to determine that he was a Christian.
- Evidence: `party_position` cue `submits` at chunk `4604431` offsets `261-268`; context: The applicant submits that the member should have accorded deference to the Pastor’s opinion and taken the baptismal certificate at face value.
- Evidence: `evidence_fact` cue `evidence` at chunk `4604431` offsets `136-144`; context: [28] It is clear from the member’s reasons that he arrived at the conclusion that the applicant’s faith was not genuine in spite of the evidence that the applicant had been in regular attendance at a church in Toronto and had been baptized there.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4604431` offsets `573-579`; context: Taken as a whole, the decision cannot be said to be irrational or unsupported by the evidence.

#### 12076:2:subtheme:5 · paragraphs 32-33

- Raw key terms: `appeal, applicant, application, board, capable, cause, certified, circumstance`
- Display key terms: `capable, certified, circumstance`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: capable, certified, circumstance Rule/authority context: The Board’s subsequent finding under section 107(2) of IRPA is permissible in a circumstance where there is no independent and credible documentary evidence capable of supporting a positive determination of the Applicant Application context: [31] Similarly, I find the Board’s treatment of this evidence to be reasonable. Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that this application is dismissed. Evidence spans paragraphs 32-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4604432` offsets `383-391`; context: No question of general importance is certified for appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `4604432` offsets `53-61`; context: [31] Similarly, I find the Board’s treatment of this evidence to be reasonable.
- Evidence: `governing_rule` cue `under` at chunk `4604432` offsets `111-116`; context: The Board’s subsequent finding under section 107(2) of IRPA is permissible in a circumstance where there is no independent and credible documentary evidence capable of supporting a positive determination of the Applicant’s claim.
- Evidence: `reasoning_application` cue `I find` at chunk `4604432` offsets `16-22`; context: [31] Similarly, I find the Board’s treatment of this evidence to be reasonable.
- Evidence: `disposition` cue `dismissed` at chunk `4604432` offsets `369-378`; context: JUDGMENT
THIS COURT’S JUDGMENT is that this application is dismissed.

#### Section text

V. Submissions of the Parties A. The Applicant’s Position [15] The Applicant argues that the Board failed to alert him to its reliance on specialized knowledge about Pentecostalism.

[16] The Applicant also argues that the Board’s overall assessment of the Applicant’s Christian identity was unreasonable. It chose to rely on the Applicant’s testimony instead of other evidence and its questions did not address basic knowledge but rather applied too high a threshold of required religious knowledge, which has been found to represent a reviewable error. The Board also appeared to ignore the knowledge that the Applicant actually possessed and ought to have indicated what the correct answers to its questions were or why the Applicant’s answers were incorrect.

[17] The Applicant further submits that the Board itself lacked knowledge and understanding of Pentecostalism.

[18] Finally, the Applicant submits that the Board misapplied the test for a “no credible basis” finding. The case law is clear that the Board may not simply extend its credibility findings to the entirety of the evidence and on that basis conclude that there is no credible basis. Such a conclusion may only be made where there is no trustworthy or credible evidence that could potentially support a positive decision.
B. Respondent’s Position [19] On the procedural fairness issue, the Respondent submits that the Board did not make use of specialized knowledge in assessing the genuineness of the Applicant’s religious faith. Rather, it asked simple questions on topics of which the Applicant claimed knowledge.

[20] On the substantive issue, the Respondent submits that the Board reasonably assessed the genuineness of the Applicant’s religious faith. Given the Applicant’s alleged level of study, the information sought from him regarding knowledge and understanding of his faith was appropriate. The Respondent notes that the topic of the Pentecost, about which the Board questioned the Applicant, was the subject of the church service that the Applicant said he had most recently attended.

[21] The Respondent argues that the Board reasonably assessed the probative value of evidence and reasonably determined that the claim had no credible basis. The burden is on the Applicant to satisfy the decision maker with “clear, convincing and cogent” “clear, evidence, and the Applicant failed to meet his onus. The Board is not obligated to defer to a pastor’s opinion and take a baptismal certificate at face value.
VI. Analysis [22] This Court has expressed in past decisions the concerns that can arise in connection with assessing the genuineness of religious belief based on questioning as to religious knowledge. In Zhang v Canada (Minister of Citizenship and Immigration), 2012 FC 503, Justice Campbell expressed this concern as follows at paragraph 12:

[12] The Court has recognized the potential unfairness of RPD religious knowledge testing and has attempted to limit the stringency of this inquiry. In Dong v Canada (Minister of Citizenship & Immigration), 2010 FC 55, at paragraph 20, Justice Kelen found as follows:
In assessing a claimant’s knowledge of Christianity, the Board should not adopt an unrealistically high standard of knowledge or focus on a “few points of error or misunderstandings to a level which reached the microscopic analysis”: Attakora v. Canada (Minister of Employment and Immigration) (F.C.A.), (1989), 99 N.R. 168, [1989] F.C.J. No. 444 (QL), and subsequent cases: Huang v. Canada (MCI), 2008 FC 346, 69 Imm. L.R. (3d) 286, per Justice Mosley at paragraph 10; Chen v. Canada (MCI), 2007 FC 270, 155 A.C.W.S. (3d) 929, per Justice Barnes at paragraph 16.
Indeed, in Penghui Wu v Minister of Citizenship and Immigration, 2009 FC 929, Justice Kelen found that assessing a genuine Christian by way of “trivia” is contrary to law. In Wang v Minister of Citizenship and Immigration, 2011 FC 1030, Justice Beaudry determined that a decision of the RPD can be set aside where the claimant was held to an unreasonably high standard of religious knowledge. In Wang the applicant was determined not to be a Christian because the RPD found he incorrectly answered questions about “transubstantiation”. At paragraph 13, Justice Beaudry has this to say about such a determination:
The Board erroneously determined the applicant's knowledge of the Catholic faith by way of "trivia". In assessing the applicant's knowledge of Christianity, the Board "erroneously expected the answers of the applicant to questions about his religion to be equivalent to the Board's own knowledge of that religion" Ullah v. Canada (Minister of Citizenship and Immigration), 2000 FCJ No 1918, para 11.

[23] On the other hand, the Respondent relies on the decision in Hou, in which Justice Gleason stated as follows at paragraph 55:

[55] Indeed, in all cases – and especially in cases like the present where the applicant’s credibility is found to be wanting – the Court should not be too hasty to substitute its opinion for that of the RPD, which has developed expertise regarding the dictates of a number of religions. As Justice Near noted in Wang (cited above at para 8), assessing the genuineness of the claimant’s religious beliefs is a difficult task and “this challenging job has been delegated to the Board as the finder of fact and this Court cannot, on judicial review, decide to, in effect, reweigh the results of what can look like a round of Bible trivia” (at para 18). In my view, in Wang at para 20, Justice Near set out the proper approach to be adopted by this Court in assessing the reasonableness of the RPD’s assessment of the genuineness of a claimant’s religious beliefs. After reviewing an awkward set of questions the Board had posed regarding what Jesus was like, he stated:
… this line of questioning illustrates the difficulty of the assessment the Board is required to make. It does not represent an error for which the Board’s decision should be over-turned. Absent a showing of disregard for the evidence, or a misapprehension of the facts, I am unwilling to disturb the Board’s conclusion in this regard – again deference is warranted. The Board did not make the determination of the genuineness of the Applicant’s faith based solely on the Applicant’s inability to attribute some human characteristics to Jesus. Answers to other questions regarding the Pentecostal faith were vague and lacking in detail. As the Respondent submits, testimony lacking in detail that would reasonably be expected of a person in the claimant’s position is a basis for rejecting claims as non-credible even if the Applicant was able to answer some other questions, and with great detail.

[24] Similarly, Justice Pinard held as follows in Jin v Canada (Minister of Citizenship and Immigration), 2012 FC 595 at paragraph 15:

[15] Amselem, above, deals with freedom of religion and the subjectivity of religious beliefs. Thus, the Supreme Court of Canada held that it is not the objectivity of the religious beliefs that matters, nor their validity, but rather the sincerity of the applicant’s religious beliefs (at para 43). Here, the Board needed to assess the genuineness of the applicant’s religious convictions. The questions asked by the Board were not to gage the correctness of his beliefs, but rather to determine whether the applicant understood the basic tenants of Christianity. Unlike in Zhu v. Minister of Citizenship and Immigration, 2008 FC 1066 [Zhu], the Court was not assessing the sophistication of the applicant’s belief: the Board did not accept that the applicant was a genuine Christian (at para 13). Moreover, Mr. Justice Russell Zinn in Zhu specifically stated that the sincerity of the applicant’s religious conviction can be assessed with regards to his familiarity with the dogma or creed invoked (at para 17).

[25] I believe that Justice Rennie succinctly captured the applicable principle at paragraph 9 of Wang v Canada (Minister of Citizenship and Immigration), 2012 FC 346:

[9] The Board is tasked with assessing the applicant’s credibility and not the soundness of his theology. A claimant may have a poor understanding of the minutiae of the religious doctrine but that does not, necessarily, mean his faith is not genuine. While there is a logical correlation between the depth of religious knowledge and the credibility of a claim of persecution, here, the deviations from doctrine were, at best, minor and cannot safely sustain the finding that the applicant was not a genuine adherent.

[26] My reading of the jurisprudence is that it is not improper for the Board to engage in religious questioning in an effort to gauge the genuineness of a claimant’s beliefs, but that such questioning and resulting analysis must indeed focus on the genuineness of those beliefs and not whether they are theologically correct. This can be a difficult task for the Board, as it is entitled to consider whether the claimant holds a level of religious knowledge that would be expected of someone in the claimant’s position but should not reach an adverse conclusion based on minutiae or holding the claimant to an unreasonably high standard of religious knowledge.

[27] My conclusion is that the Board approached this task in a defensible manner. The Board was neither subjecting him to a test on religious trivia nor reaching its conclusions based on an assessment of the theological soundness of his responses. Rather, it was posing relatively basic questions and, for the most part, based its conclusion as to the lack of genuinely held belief not upon an assessment of the correctness of the Applicant’s answers but rather upon the Applicant’s failure to provide answers or answers of any detail. The Board acknowledged that the Applicant provided some correct answers. However, its conclusion that he is not a genuine Christian, based on his lack of overall knowledge of the Christian religion, is reasonable and consistent with the jurisprudence.

[28] Turning to the Applicant’s submissions on procedural fairness, I cannot conclude this argument to have merit. It cannot be unexpected for the Applicant to have to answer questions posed by the Board on the religion he professes to follow, so that the Board can assess the genuineness of his belief. Given my conclusion that this questioning and the resulting analysis were within the boundaries contemplated by the jurisprudence, I do not consider this to be reliance on specialized knowledge.

[29] Finally, I can find no fault in the Board`s finding under section 107(2) of IRPA that there was no credible basis for the Applicant’s claim. The Respondent refers to the decision of the Federal Court of Appeal in Rahaman v Canada (Minister of Citizenship and Immigration), 2002 FCA 89 as summarizing the applicable law at paragraph 19:

[19] … In this case ([Foyet v. Canada (Minister of Citizenship and Immigration) (2000), 187 F.T.R. 181], at paragraph 19), Denault J. summarised his understanding of the law as follows:
In my view, what Sheikh, tells us is that when the only evidence linking the applicant to the harm he or she alleges is found in the claimant's own testimony and the claimant is found to be not credible, the Refugee Division may, after examining the documentary evidence make a general finding that there is no credible basis for the claim. In cases where there is independent and credible documentary evidence, however, the panel may not make a no credible basis finding.
In my view, this is an accurate statement of the law as it has been understood to date, subject to one qualification: in order to preclude a "no credible basis" finding, the "independent and credible documentary evidence" to which Denault J. refers must have been capable of supporting a positive determination of the refugee claim.

[30] The Applicant’s submissions note that he had filed documentary evidence in support of his claim, including a baptismal certificate and church letters. However, the Board asked the Applicant how his pastor was able to determine that he was a Christian. The Board considered the Applicant’s responses and concluded that the pastor had asked very simple questions and expected very little in return. The Board did not give any weight to this evidence. This is consistent with the reasoning approved by the Court in Cao v Canada (Minister of Citizenship and Immigration), 2008 FC 1174 at paragraph 28:

[28] It is clear from the member’s reasons that he arrived at the conclusion that the applicant’s faith was not genuine in spite of the evidence that the applicant had been in regular attendance at a church in Toronto and had been baptized there. The applicant submits that the member should have accorded deference to the Pastor’s opinion and taken the baptismal certificate at face value. To do so would, in effect, substitute the Pastor’s assessment of the genuineness of the claim of faith for that which the member was required to make. Taken as a whole, the decision cannot be said to be irrational or unsupported by the evidence.

[31] Similarly, I find the Board’s treatment of this evidence to be reasonable. The Board’s subsequent finding under section 107(2) of IRPA is permissible in a circumstance where there is no independent and credible documentary evidence capable of supporting a positive determination of the Applicant’s claim.
JUDGMENT
THIS COURT’S JUDGMENT is that this application is dismissed. No question of general importance is certified for appeal.
“Richard F. Southcott”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-7310-14
STYLE OF CAUSE:
MENGMENG GAO v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
TORONTO, ONTARIO
DATE OF HEARING:
SEPTEMBER 22, 2015


## 12076:3 · paragraphs 34-34

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `71d14a15fba3ef5a08a41741bd5402d260eb9a842fb774f21c791b7bf09b5529`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12076:3:subtheme:1 · paragraphs 34-34

- Raw key terms: `appearances, applicants, associates, attorney, barrister, canada, catherine, dated`
- Display key terms: `associates, barrister, catherine, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: associates, barrister, catherine, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 34-34. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
southcott, J.
DATED:
october 6, 2015
APPEARANCES:
Matthew Oh
For The ApplicantS
Catherine Vasilaros
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Matthew Oh
Barrister & Solicitor
Lewis & Associates
Toronto, Ontario
For The ApplicantS
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
FOR THE RESPONDENT
