# Discussion Units: case 10214

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **31**
- Continuity pairs: **30**
- Discussion Units: **1**
- Paragraph source hashes: **31**
- Sub-themes: **11**

## 10214:1 · paragraphs 0-30

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a73677232abf341921d10f2da39446f16784eecb84a1fd817cca6816cc7ff7b9`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10214:1:subtheme:1 · paragraphs 0-9

- Raw key terms: `applicant, canada, findings, refugee, appeal, brazil, claim, credibility`
- Display key terms: `findings, refugee, brazil, credibility`
- Argument roles: `counterargument_limitation, disposition, governing_rule, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, party_position Display terms: findings, refugee, brazil, credibility Position/evidence statements: ], where he claimed asylum. Rule/authority context: [1] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c-27 [Act or IRPA], of an Immigration and Refugee Board of Canada Appeal Division’s [RAD or Bo Operative outcome context: [6] The Applicant appealed to the RAD, which dismissed the appeal on July 6, 2016, for reasons (as will be discussed below) nearly identical to the RPD’s. Evidence spans paragraphs 0-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4514521` offsets `47-52`; context: [1] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c-27 [Act or IRPA], of an Immigration and Refugee Board of Canada Appeal Division’s [RAD or Board] July 6, 2016 negative decision [Decision] confirming the Refugee Protection Division [RPD]’s findings.
- Evidence: `party_position` cue `claimed` at chunk `4514524` offsets `275-282`; context: ], where he claimed asylum.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4514524` offsets `291-299`; context: Although his application was found credible in a very early stage of the U.
- Evidence: `disposition` cue `dismissed` at chunk `4514526` offsets `45-54`; context: [6] The Applicant appealed to the RAD, which dismissed the appeal on July 6, 2016, for reasons (as will be discussed below) nearly identical to the RPD’s.

#### 10214:1:subtheme:2 · paragraphs 10-11

- Raw key terms: `american, applicant, army, authorities, fact, held, lankan, noted`
- Display key terms: `american, army, authorities, fact, lankan, noted`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: american, army, authorities, fact, lankan, noted Position/evidence statements: [10] Second, the RAD noted the discrepancies between the Applicant’s American and Canadian claims, noting that the Applicant told Canadian authorities that he had been detained by the Sri Lankan military in 2011 and 2014 | [11] The RAD further noted an important omission from the Applicant’s Basis of Claim [BOC], which was included in the American application: the Applicant failed to disclose shrapnel scarring on his ankle, which was used  Evidence spans paragraphs 10-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4514530` offsets `379-385`; context: The Applicant explained that the discrepancies were due to interpretation issues and the fact that the U.
- Evidence: `party_position` cue `claims` at chunk `4514530` offsets `91-97`; context: [10] Second, the RAD noted the discrepancies between the Applicant’s American and Canadian claims, noting that the Applicant told Canadian authorities that he had been detained by the Sri Lankan military in 2011 and 2014, while informing American officials that he had last been hurt by the army in 2008.
- Evidence: `counterargument_limitation` cue `However` at chunk `4514530` offsets `443-450`; context: However, the RAD rejected these reasons and held that while they may explain minor inconsistencies, they did not explain major ones.
- Evidence: `party_position` cue `Claim` at chunk `4514531` offsets `79-84`; context: [11] The RAD further noted an important omission from the Applicant’s Basis of Claim [BOC], which was included in the American application: the Applicant failed to disclose shrapnel scarring on his ankle, which was used by Sri Lankan authorities as a means to identify possible LTTE members.
- Evidence: `evidence_fact` cue `testimony` at chunk `4514531` offsets `400-409`; context: Given the importance of this fact, the RAD said the omission cast doubts on the veracity of the Applicant’s testimony.

#### 10214:1:subtheme:3 · paragraphs 12-13

- Raw key terms: `advantage, correctness, credibility, enjoys, evidence, findings, issue, particular`
- Display key terms: `advantage, correctness, credibility, enjoys, findings, particular`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: advantage, correctness, credibility, enjoys, findings, particular Position/evidence statements: In other words, the Applicant contends that the RAD -- while purporting to conduct a correctness review and deferring to the RDP in matters of credibility where the RPD enjoys a particular advantage -- did not independen Application context: The RAD may choose to show deference with respect to the RDP’s credibility findings where the RPD enjoys a particular advantage, but should apply a correctness standard review when reviewing the RPD’s findings of fact or Evidence spans paragraphs 12-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4514532` offsets `38-43`; context: [12] The Applicant raises one central issue in this judicial review: the RAD failed to conduct an independent assessment of the evidence, likening its role to that of a judicial review body.
- Evidence: `party_position` cue `contends` at chunk `4514532` offsets `221-229`; context: In other words, the Applicant contends that the RAD -- while purporting to conduct a correctness review and deferring to the RDP in matters of credibility where the RPD enjoys a particular advantage -- did not independently assess the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4514532` offsets `128-136`; context: [12] The Applicant raises one central issue in this judicial review: the RAD failed to conduct an independent assessment of the evidence, likening its role to that of a judicial review body.
- Evidence: `issue` cue `issue` at chunk `4514533` offsets `396-401`; context: The RAD may choose to show deference with respect to the RDP’s credibility findings where the RPD enjoys a particular advantage, but should apply a correctness standard review when reviewing the RPD’s findings of fact or of mixed fact and law, “which do not involve an issue of the credibility of oral evidence alone” (Sinnaraja v Canada (Citizenship and Immigration), 2016 FC 778 at para 24 [Sinnaraja]).
- Evidence: `evidence_fact` cue `evidence` at chunk `4514533` offsets `429-437`; context: The RAD may choose to show deference with respect to the RDP’s credibility findings where the RPD enjoys a particular advantage, but should apply a correctness standard review when reviewing the RPD’s findings of fact or of mixed fact and law, “which do not involve an issue of the credibility of oral evidence alone” (Sinnaraja v Canada (Citizenship and Immigration), 2016 FC 778 at para 24 [Sinnaraja]).
- Evidence: `reasoning_application` cue `apply` at chunk `4514533` offsets `267-272`; context: The RAD may choose to show deference with respect to the RDP’s credibility findings where the RPD enjoys a particular advantage, but should apply a correctness standard review when reviewing the RPD’s findings of fact or of mixed fact and law, “which do not involve an issue of the credibility of oral evidence alone” (Sinnaraja v Canada (Citizenship and Immigration), 2016 FC 778 at para 24 [Sinnaraja]).
- Evidence: `counterargument_limitation` cue `but` at chunk `4514533` offsets `256-259`; context: The RAD may choose to show deference with respect to the RDP’s credibility findings where the RPD enjoys a particular advantage, but should apply a correctness standard review when reviewing the RPD’s findings of fact or of mixed fact and law, “which do not involve an issue of the credibility of oral evidence alone” (Sinnaraja v Canada (Citizenship and Immigration), 2016 FC 778 at para 24 [Sinnaraja]).

#### 10214:1:subtheme:4 · paragraphs 14-16

- Raw key terms: `fear, subjective, applicant, case, claim, decision, finding, abandonment`
- Display key terms: `fear, subjective, case, finding, abandonment`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: fear, subjective, case, finding, abandonment Position/evidence statements: [15] Rather, the RAD’s ‘independent analysis’ in the area of the subjective fear (relating to the third country claims) consisted of assessing the jurisprudence brought to its attention by the Applicant’s RAD counsel (wh Rule/authority context: [15] Rather, the RAD’s ‘independent analysis’ in the area of the subjective fear (relating to the third country claims) consisted of assessing the jurisprudence brought to its attention by the Applicant’s RAD counsel (wh Evidence spans paragraphs 14-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4514534` offsets `177-182`; context: This part of the proceedings did not involve an issue of the credibility of oral evidence alone.
- Evidence: `evidence_fact` cue `evidence` at chunk `4514534` offsets `210-218`; context: This part of the proceedings did not involve an issue of the credibility of oral evidence alone.
- Evidence: `issue` cue `whether` at chunk `4514535` offsets `503-510`; context: This fell short of the exercise required: a contextual and independent analysis – since it was in no worse a position than the RPD – in arriving at its own determination whether the Applicant indeed lacked subjective fear, by failing to claim in the U.
- Evidence: `party_position` cue `claims` at chunk `4514535` offsets `112-118`; context: [15] Rather, the RAD’s ‘independent analysis’ in the area of the subjective fear (relating to the third country claims) consisted of assessing the jurisprudence brought to its attention by the Applicant’s RAD counsel (which it uniformly distinguished), and pointing to other case law (upon which it relied): Decision at paras 25-35.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4514535` offsets `147-160`; context: [15] Rather, the RAD’s ‘independent analysis’ in the area of the subjective fear (relating to the third country claims) consisted of assessing the jurisprudence brought to its attention by the Applicant’s RAD counsel (which it uniformly distinguished), and pointing to other case law (upon which it relied): Decision at paras 25-35.

#### 10214:1:subtheme:5 · paragraphs 17-18

- Raw key terms: `argued, findings, huruglica, para, principles, references, advantage, agents`
- Display key terms: `findings, huruglica, para, principles, references, advantage, agents`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: findings, huruglica, para, principles, references, advantage, agents Position/evidence statements: The Applicant argued that 69 references to or points of reliance placed on RPD findings, failed to demonstrate an independent review. | [18] In response he Respondent argued, that that many of the references were simply reporting what the RPD had stated or found: the fact that the RAD concurred with the RPD’s findings does not in and of itself mean that  Rule/authority context: At the outset of its Decision, the RAD reiterated the correct guiding principles for its appeal (at para 18 of its Decision): “the RAD will review all of the evidence in the RPD’s record and come to its own independent a | [18] In response he Respondent argued, that that many of the references were simply reporting what the RPD had stated or found: the fact that the RAD concurred with the RPD’s findings does not in and of itself mean that  Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4514537` offsets `343-350`; context: At the outset of its Decision, the RAD reiterated the correct guiding principles for its appeal (at para 18 of its Decision): “the RAD will review all of the evidence in the RPD’s record and come to its own independent assessment of whether the Appellant is Convention refugee or a person in need of protection.
- Evidence: `party_position` cue `argued` at chunk `4514537` offsets `567-573`; context: The Applicant argued that 69 references to or points of reliance placed on RPD findings, failed to demonstrate an independent review.
- Evidence: `evidence_fact` cue `evidence` at chunk `4514537` offsets `268-276`; context: At the outset of its Decision, the RAD reiterated the correct guiding principles for its appeal (at para 18 of its Decision): “the RAD will review all of the evidence in the RPD’s record and come to its own independent assessment of whether the Appellant is Convention refugee or a person in need of protection.
- Evidence: `governing_rule` cue `principles` at chunk `4514537` offsets `180-190`; context: At the outset of its Decision, the RAD reiterated the correct guiding principles for its appeal (at para 18 of its Decision): “the RAD will review all of the evidence in the RPD’s record and come to its own independent assessment of whether the Appellant is Convention refugee or a person in need of protection.
- Evidence: `party_position` cue `argued` at chunk `4514538` offsets `31-37`; context: [18] In response he Respondent argued, that that many of the references were simply reporting what the RPD had stated or found: the fact that the RAD concurred with the RPD’s findings does not in and of itself mean that the principles established in Huruglica were not respected (Anel v Canada (Citizenship and Immigration), 2016 FC 759 at para 26).
- Evidence: `governing_rule` cue `principles` at chunk `4514538` offsets `224-234`; context: [18] In response he Respondent argued, that that many of the references were simply reporting what the RPD had stated or found: the fact that the RAD concurred with the RPD’s findings does not in and of itself mean that the principles established in Huruglica were not respected (Anel v Canada (Citizenship and Immigration), 2016 FC 759 at para 26).

#### 10214:1:subtheme:6 · paragraphs 19-20

- Raw key terms: `analysis, deference, findings, independent, para, acknowledged, added, appeal`
- Display key terms: `analysis, deference, findings, independent, para, acknowledged, added`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: analysis, deference, findings, independent, para, acknowledged, added Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4514539` offsets `276-284`; context: An overly obsequious support for and reinforcement of all RPD findings can bring into question the independence of the RAD’s analysis.

#### 10214:1:subtheme:7 · paragraphs 21-22

- Raw key terms: `applicant, assessment, however, independent, required, review, whether, accordingly`
- Display key terms: `assessment, however, independent, required, review, whether, accordingly`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: assessment, however, independent, required, review, whether, accordingly Application context: [21] While I am mindful that in Khachatourian, the RAD explicitly stated that it had applied a reasonableness standard (at para 14), which the RAD did not expressly do in the case at bar, I am of the view that the RAD’s  | Accordingly, this judicial review is granted. Operative outcome context: Accordingly, this judicial review is granted. Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4514541` offsets `739-746`; context: I can do no better than to repeat Justice Fothergill’s words in HAK v Canada (Citizenship and Immigration), 2015 FC 1172 at para 18 [HAK]:
[…] the RAD stated its intention to conduct its own assessment of the evidence and to determine independently whether the Applicant is a Convention refugee or a person in need of protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `4514541` offsets `699-707`; context: I can do no better than to repeat Justice Fothergill’s words in HAK v Canada (Citizenship and Immigration), 2015 FC 1172 at para 18 [HAK]:
[…] the RAD stated its intention to conduct its own assessment of the evidence and to determine independently whether the Applicant is a Convention refugee or a person in need of protection.
- Evidence: `reasoning_application` cue `applied` at chunk `4514541` offsets `85-92`; context: [21] While I am mindful that in Khachatourian, the RAD explicitly stated that it had applied a reasonableness standard (at para 14), which the RAD did not expressly do in the case at bar, I am of the view that the RAD’s language mirrors that of Khachatourian.
- Evidence: `counterargument_limitation` cue `However` at chunk `4514541` offsets `820-827`; context: However, it is not apparent from a review of the RAD’s decision that this approach was followed in practice.
- Evidence: `issue` cue `whether` at chunk `4514542` offsets `37-44`; context: [22] Like in HAK, I am unable to say whether an independent assessment of the Applicant’s claim would have changed the outcome of the appeal before the RAD.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4514542` offsets `269-280`; context: Accordingly, this judicial review is granted.
- Evidence: `counterargument_limitation` cue `However` at chunk `4514542` offsets `157-164`; context: However, an independent assessment is required, and for the reasons provided, I am not satisfied that occurred.
- Evidence: `disposition` cue `granted` at chunk `4514542` offsets `306-313`; context: Accordingly, this judicial review is granted.

#### 10214:1:subtheme:8 · paragraphs 23-24

- Raw key terms: `credibility, deference, question, appeal, applicant, appropriate, arise, case`
- Display key terms: `credibility, deference, question, appropriate, arise, case`
- Argument roles: `governing_rule, issue, party_position`
- Explanation: Observed roles: governing_rule, issue, party_position Display terms: credibility, deference, question, appropriate, arise, case Position/evidence statements: [23] Applicant’s counsel submits the same question for certification as he did in Sinnaraja, namely: Does the RAD owe any degree of deference to the RPD’s finding on credibility? Rule/authority context: The RAD should be given the opportunity to develop its own jurisprudence in that respect; there is thus no need for me to pigeon-hole the RAD to the level of deference owed in each case. Evidence spans paragraphs 23-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4514543` offsets `42-50`; context: [23] Applicant’s counsel submits the same question for certification as he did in Sinnaraja, namely:
Does the RAD owe any degree of deference to the RPD’s finding on credibility?
- Evidence: `party_position` cue `submits` at chunk `4514543` offsets `25-32`; context: [23] Applicant’s counsel submits the same question for certification as he did in Sinnaraja, namely:
Does the RAD owe any degree of deference to the RPD’s finding on credibility?
- Evidence: `issue` cue `question` at chunk `4514544` offsets `36-44`; context: [24] There are two reasons why this question need not be certified.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4514544` offsets `369-382`; context: The RAD should be given the opportunity to develop its own jurisprudence in that respect; there is thus no need for me to pigeon-hole the RAD to the level of deference owed in each case.

#### 10214:1:subtheme:9 · paragraphs 25-26

- Raw key terms: `appeal, conducted, file, issue, members, notice, panel, three`
- Display key terms: `conducted, file, members, notice, three`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: conducted, file, members, notice, three Rule/authority context: [26] After citing the above-referenced paragraph 74 of Huruglica, the RAD writes in this Notice: In the interest of developing a coherent national jurisprudence, the Chairperson of the IRB has ordered that the appeal bef Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4514545` offsets `69-74`; context: [25] As counsel pointed out, the RAD has committed to addressing the issue, as noted in its “Notice - Proceeding to be conducted before a Panel of three Members of the Refugee Appeal Division” regarding File #TB6‑03419/20/21/22 (see: http://www.
- Evidence: `issue` cue `issue` at chunk `4514546` offsets `421-426`; context: [26] After citing the above-referenced paragraph 74 of Huruglica, the RAD writes in this Notice:
In the interest of developing a coherent national jurisprudence, the Chairperson of the IRB has ordered that the appeal before the RAD in this file be conducted before a panel of three members of the RAD so that the RAD may determine its role in an appeal where the RPD’s findings of fact (or mixed fact and law) involve an issue of credibility, including determining what level of deference, if any, is owed to the credibility findings made by the RPD.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4514546` offsets `147-160`; context: [26] After citing the above-referenced paragraph 74 of Huruglica, the RAD writes in this Notice:
In the interest of developing a coherent national jurisprudence, the Chairperson of the IRB has ordered that the appeal before the RAD in this file be conducted before a panel of three members of the RAD so that the RAD may determine its role in an appeal where the RPD’s findings of fact (or mixed fact and law) involve an issue of credibility, including determining what level of deference, if any, is owed to the credibility findings made by the RPD.

#### 10214:1:subtheme:10 · paragraphs 27-28

- Raw key terms: `question, above, certify, developments, dispositive, equally, erred, explained`
- Display key terms: `question, above, certify, developments, dispositive, equally, erred, explained`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: question, above, certify, developments, dispositive, equally, erred, explained Rule/authority context: [28] Second, and equally important, the proposed question is not dispositive of the outcome of this matter: I have found that the RAD erred on points which, as explained above, the jurisprudence (including post-Huruglica Evidence spans paragraphs 27-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4514547` offsets `94-102`; context: [27] Given these developments, it would be premature and indeed inappropriate to certify this question.
- Evidence: `issue` cue `question` at chunk `4514548` offsets `49-57`; context: [28] Second, and equally important, the proposed question is not dispositive of the outcome of this matter: I have found that the RAD erred on points which, as explained above, the jurisprudence (including post-Huruglica) has settled.
- Evidence: `evidence_fact` cue `found that` at chunk `4514548` offsets `115-125`; context: [28] Second, and equally important, the proposed question is not dispositive of the outcome of this matter: I have found that the RAD erred on points which, as explained above, the jurisprudence (including post-Huruglica) has settled.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4514548` offsets `181-194`; context: [28] Second, and equally important, the proposed question is not dispositive of the outcome of this matter: I have found that the RAD erred on points which, as explained above, the jurisprudence (including post-Huruglica) has settled.

#### 10214:1:subtheme:11 · paragraphs 29-30

- Raw key terms: `applicant, canada, citizenship, diner, immigration, judgment, reasons, above`
- Display key terms: `diner, above`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: diner, above Application context: [29] The Applicant has therefore failed to established the test for certification set out in Zhang v Canada (Citizenship and Immigration), 2013 FCA 168 at para 9. Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that: The application for judicial review is granted. Evidence spans paragraphs 29-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4514549` offsets `180-188`; context: Accordingly, the question proposed by the Applicant cannot be certified.
- Evidence: `reasoning_application` cue `therefore` at chunk `4514549` offsets `23-32`; context: [29] The Applicant has therefore failed to established the test for certification set out in Zhang v Canada (Citizenship and Immigration), 2013 FCA 168 at para 9.
- Evidence: `disposition` cue `granted` at chunk `4514549` offsets `315-322`; context: JUDGMENT
THIS COURT’S JUDGMENT is that:
The application for judicial review is granted.

#### Section text

Jeyaseelan v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2017-03-15
Neutral citation
2017 FC 278
File numbers
IMM-3294-16
Notes
Decision Content
Date: 20170315
Docket: IMM-3294-16
Citation: 2017 FC 278
Ottawa, Ontario, March 15, 2017
PRESENT: The Honourable Mr. Justice Diner
BETWEEN:
ANESHKUMAR JEYASEELAN
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Background

[1] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c-27 [Act or IRPA], of an Immigration and Refugee Board of Canada Appeal Division’s [RAD or Board] July 6, 2016 negative decision [Decision] confirming the Refugee Protection Division [RPD]’s findings.

[2] The Applicant is a twenty-four year-old male citizen from Sri Lanka, who says that his father and two uncles were either accused or suspected of having ties to the Liberation Tigers of Tamil Eelam [LTTE], a militant organization fighting for the independence of the northeastern region of the country.

[3] The Applicant says he was assaulted in 2011. The Applicant further alleges that in 2012, men came looking for him at his home. He also says that in 2014 he was arrested, assaulted, beaten and warned that if re-arrested, he may be killed.

[4] The Applicant first fled to his grandmother’s house, and then fled the country in February 2015 with the help of a smuggler, travelling through the United Arab Emirates, Ecuador, Brazil, Panama, Peru, Colombia, Mexico, and finally into the United States [U.S.], where he claimed asylum. Although his application was found credible in a very early stage of the U.S. process, he abandoned the claim when released from immigration-based detention, and made his way to Canada on June 24, 2015. He claimed refugee status based on ethnicity, nationality, political opinion, and membership in a particular social group grounds.

[5] The RPD rejected the claim on February 12, 2016, drawing negative credibility findings based on:
the Applicant’s failure to claim in Brazil and Ecuador (which are Convention signatory countries);
the Applicant’s election to abandon his U.S. claim;
discrepancies between his U.S. and Canadian claims regarding the agents of persecution and events in Sri Lanka; and
his profile that would not put him at risk upon return.

[6] The Applicant appealed to the RAD, which dismissed the appeal on July 6, 2016, for reasons (as will be discussed below) nearly identical to the RPD’s.

[7] The RAD reviewed the Federal Court of Appeal’s decision in Canada (Citizenship and Immigration) v Huruglica, 2016 FCA 93 [Huruglica], explaining that a hybrid appeal is not a classic de novo appeal: it must intervene when the RPD is wrong in fact, law and questions of mixed fact and law, and deference is not owed, save with respect to certain findings of credibility. In other words, the RAD does not start the refugee determination anew; the RPD decision is not ignored.

[8] The RAD made a number of findings, which resulted in adverse inferences made against the Applicant’s credibility. Again, these mirrored those of the RPD.

[9] First, the RAD drew a negative inference against the Applicant for not claiming refugee status in Convention signatory countries, specifically Brazil and Ecuador, and for abandoning his claim in the U.S.

[10] Second, the RAD noted the discrepancies between the Applicant’s American and Canadian claims, noting that the Applicant told Canadian authorities that he had been detained by the Sri Lankan military in 2011 and 2014, while informing American officials that he had last been hurt by the army in 2008. The Applicant explained that the discrepancies were due to interpretation issues and the fact that the U.S. transcripts are not verbatim. However, the RAD rejected these reasons and held that while they may explain minor inconsistencies, they did not explain major ones.

[11] The RAD further noted an important omission from the Applicant’s Basis of Claim [BOC], which was included in the American application: the Applicant failed to disclose shrapnel scarring on his ankle, which was used by Sri Lankan authorities as a means to identify possible LTTE members. Given the importance of this fact, the RAD said the omission cast doubts on the veracity of the Applicant’s testimony. Furthermore, the RAD noted that the Applicant told American authorities that in 2012, the army came looking for him, and he thus fled his home to live with his grandmother, a fact not included in his BOC. The RAD noted that even if the 2011 and 2014 arrests were true, there was a three year gap with no arrests. Moreover, the RAD held that if the Applicant was wanted by the State, it is doubtful that he would have been able to pass checkpoints, since that he would likely have been on a watch list, and would not have been able to leave the country using his passport. Given the foregoing, also all noted by the RPD, the RAD rejected the claim.
II. Analysis

[12] The Applicant raises one central issue in this judicial review: the RAD failed to conduct an independent assessment of the evidence, likening its role to that of a judicial review body. In other words, the Applicant contends that the RAD -- while purporting to conduct a correctness review and deferring to the RDP in matters of credibility where the RPD enjoys a particular advantage -- did not independently assess the evidence. Rather, he contends that the RAD simply endorsed the RPD’s findings.

[13] The parties agree, as do I, that the RAD’s Decision is reviewable on a standard of reasonableness (Huruglica at para 35). The RAD may choose to show deference with respect to the RDP’s credibility findings where the RPD enjoys a particular advantage, but should apply a correctness standard review when reviewing the RPD’s findings of fact or of mixed fact and law, “which do not involve an issue of the credibility of oral evidence alone” (Sinnaraja v Canada (Citizenship and Immigration), 2016 FC 778 at para 24 [Sinnaraja]).

[14] In this case, the RAD concurred with the RPD’s finding with respect to the Applicant’s abandonment of his claim in the U.S. This part of the proceedings did not involve an issue of the credibility of oral evidence alone. In other words, the RAD should have independently assessed the subjective fear component of the claim.

[15] Rather, the RAD’s ‘independent analysis’ in the area of the subjective fear (relating to the third country claims) consisted of assessing the jurisprudence brought to its attention by the Applicant’s RAD counsel (which it uniformly distinguished), and pointing to other case law (upon which it relied): Decision at paras 25-35. This fell short of the exercise required: a contextual and independent analysis – since it was in no worse a position than the RPD – in arriving at its own determination whether the Applicant indeed lacked subjective fear, by failing to claim in the U.S. and any other Convention signatory countries he transited through.

[16] Subjective fear was a key finding in the Decision, which the RAD placed before all others. It could thus well have tainted the other findings. The Board needs to reconsider this point of subjective fear to properly conduct its hybrid appeal.

[17] More broadly, I am not satisfied that the RAD followed the hybrid appeal approach required by Huruglica. At the outset of its Decision, the RAD reiterated the correct guiding principles for its appeal (at para 18 of its Decision): “the RAD will review all of the evidence in the RPD’s record and come to its own independent assessment of whether the Appellant is Convention refugee or a person in need of protection.” It appears to me, looking at the totality of the Decision, that the RAD did not truly follow through with this guiding principle. The Applicant argued that 69 references to or points of reliance placed on RPD findings, failed to demonstrate an independent review. Some other places where the RAD did not enjoy any advantage (other than the subjective fear analysis) included the RAD’s agreement on all RPD findings with respect to persecution versus discrimination, the agents thereof, and conclusions drawn from comparisons between evidence from the RPD hearing, U.S. documentation, and BOC.

[18] In response he Respondent argued, that that many of the references were simply reporting what the RPD had stated or found: the fact that the RAD concurred with the RPD’s findings does not in and of itself mean that the principles established in Huruglica were not respected (Anel v Canada (Citizenship and Immigration), 2016 FC 759 at para 26).

[19] However, the Court has held that there must be a point at which one can discern where deference to the RPD stops and where the RAD’s independent analysis begins (Sinnaraja at para 27). An overly obsequious support for and reinforcement of all RPD findings can bring into question the independence of the RAD’s analysis.

[20] The line between deference and independent analysis can indeed be difficult to demarcate. Justice Noël had the following to say about where that line was crossed, in Khachatourian v Canada (Citizenship and Immigration), 2015 FC 182 at para 33 [Khachatourian]:
Throughout the decision, the RAD wrote “the RPD found” (para 36), “the Member found” (paras 36, 42, 46, 49, 53, 60), “the RPD determination” (para 37), “the Member’s review” (para 37), the “Member refers” (para 38), the “Member notes” (para 38), “the Member carefully reviewed” (para 39), “the Member discusses” (para 40), “the Member drew the following conclusions” (para 43), “the conclusions drawn by the RPD Member” (para 44), “the Member acknowledged” (para 46),“the Member provided” (Ibid), “the Member placed” (Ibid), “inconsistencies found by the Member” (para 47), “the Member reviewed” (Ibid), “the Member concluded” (para 49), “the Member lists” (Ibid), “the Member noted” (para 52), “the Member commented” (para 54), “the Member also stated” (Ibid) and “the Member’s findings” (para 61). This enunciation of the references to the reliance the RAD was showing towards the RPD is by itself a clear indication of a high degree of deference. It does not disclose the analysis that an appeal board should be doing in such a situation. [Emphasis added]

[21] While I am mindful that in Khachatourian, the RAD explicitly stated that it had applied a reasonableness standard (at para 14), which the RAD did not expressly do in the case at bar, I am of the view that the RAD’s language mirrors that of Khachatourian. Such language, when repeatedly employed by the RAD throughout its analysis of legal, factual or mixed questions, does not reflect an independent assessment as required by Huruglica, which, in turn, constitutes a reviewable error. I can do no better than to repeat Justice Fothergill’s words in HAK v Canada (Citizenship and Immigration), 2015 FC 1172 at para 18 [HAK]:
[…] the RAD stated its intention to conduct its own assessment of the evidence and to determine independently whether the Applicant is a Convention refugee or a person in need of protection. However, it is not apparent from a review of the RAD’s decision that this approach was followed in practice. Rather, it appears that the RAD applied the standard of reasonableness to its review of many aspects of the RPD’s analysis [...]

[22] Like in HAK, I am unable to say whether an independent assessment of the Applicant’s claim would have changed the outcome of the appeal before the RAD. However, an independent assessment is required, and for the reasons provided, I am not satisfied that occurred. Accordingly, this judicial review is granted.
III. Certification

[23] Applicant’s counsel submits the same question for certification as he did in Sinnaraja, namely:
Does the RAD owe any degree of deference to the RPD’s finding on credibility? If so, what degree of deference?

[24] There are two reasons why this question need not be certified. First, the Court of Appeal has spoken on the issue of deference regarding credibility in Huruglica, stating at paragraph 74:
That said, it is not appropriate to say more about the various scenarios that may arise, for they are not before us. The RAD should be given the opportunity to develop its own jurisprudence in that respect; there is thus no need for me to pigeon-hole the RAD to the level of deference owed in each case.

[25] As counsel pointed out, the RAD has committed to addressing the issue, as noted in its “Notice - Proceeding to be conducted before a Panel of three Members of the Refugee Appeal Division” regarding File #TB6‑03419/20/21/22 (see: http://www.irb-cisr.gc.ca/Eng/RefApp/Pages/notice3mempan.aspx) [Notice].

[26] After citing the above-referenced paragraph 74 of Huruglica, the RAD writes in this Notice:
In the interest of developing a coherent national jurisprudence, the Chairperson of the IRB has ordered that the appeal before the RAD in this file be conducted before a panel of three members of the RAD so that the RAD may determine its role in an appeal where the RPD’s findings of fact (or mixed fact and law) involve an issue of credibility, including determining what level of deference, if any, is owed to the credibility findings made by the RPD.

[27] Given these developments, it would be premature and indeed inappropriate to certify this question.

[28] Second, and equally important, the proposed question is not dispositive of the outcome of this matter: I have found that the RAD erred on points which, as explained above, the jurisprudence (including post-Huruglica) has settled.

[29] The Applicant has therefore failed to established the test for certification set out in Zhang v Canada (Citizenship and Immigration), 2013 FCA 168 at para 9. Accordingly, the question proposed by the Applicant cannot be certified.
JUDGMENT
THIS COURT’S JUDGMENT is that:
The application for judicial review is granted.
No question will be certified for the reasons explained above.
No costs will be ordered.
"Alan S. Diner"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-3294-16
STYLE OF CAUSE:
ANESHKUMAR JEYASEELAN v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
February 1, 2017
judgment and REASONS:
DINER J.
DATED:
March 15, 2017
APPEARANCES:
Robert I. Blanshay
For The Applicant
Daniel Engel
For The Respondent
SOLICITORS OF RECORD:
Robert Israel Blanshay Professional Corporation
Barrister and Solicitor
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
