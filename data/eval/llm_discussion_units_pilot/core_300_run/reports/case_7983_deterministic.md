# Discussion Units: case 7983

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **54**
- Continuity pairs: **53**
- Discussion Units: **4**
- Paragraph source hashes: **54**
- Sub-themes: **10**

## 7983:1 · paragraphs 0-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `feca9b5487a17619a2f9c239428037ce4f9963d6ddfa3fdd1b8d85e69a2d1089`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7983:1:subtheme:1 · paragraphs 0-21

- Raw key terms: `claimant, benefits, parental, application, commission, extended, return, standard`
- Display key terms: `benefits, parental, commission, extended, return, standard`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application Display terms: benefits, parental, commission, extended, return, standard Rule/authority context: Karval) failed attempt to amend a claim for parental benefits payable under the Employment Insurance Act, SC 1996, c 23. | The Tribunal declined to grant leave to appeal, finding that she had not established under s 58 of the Department of Employment and Social Development Act, SC 2005, c 34 that her proposed appeal had a reasonable chance o Application context: The Canada Employment Insurance Commission [Commission] refused to amend the claim because s 23(1. | [9] I find, on a balance of probabilities, that the Claimant elected to receive extended parental benefits. Operative outcome context: The General Division denied her appeal on the following basis: Evidence spans paragraphs 0-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4420486` offsets `121-126`; context: Karval) failed attempt to amend a claim for parental benefits payable under the Employment Insurance Act, SC 1996, c 23.
- Evidence: `reasoning_application` cue `because` at chunk `4420486` offsets `422-429`; context: The Canada Employment Insurance Commission [Commission] refused to amend the claim because s 23(1.
- Evidence: `counterargument_limitation` cue `but` at chunk `4420486` offsets `257-260`; context: Karval filed her claim, she chose the option of receiving extended benefits but, later, she sought to receive benefits under the standard option of 35 weeks.
- Evidence: `disposition` cue `denied` at chunk `4420486` offsets `678-684`; context: The General Division denied her appeal on the following basis:
- Evidence: `reasoning_application` cue `I find` at chunk `4420487` offsets `4-10`; context: [9] I find, on a balance of probabilities, that the Claimant elected to receive extended parental benefits.
- Evidence: `evidence_fact` cue `evidence` at chunk `4420488` offsets `9-17`; context: [10] The evidence about which kind of parental benefits the Claimant chose is ambiguous.
- Evidence: `evidence_fact` cue `evidence` at chunk `4420489` offsets `14-22`; context: [11] When the evidence is not clear one way or another, I have to decide what is most likely.
- Evidence: `evidence_fact` cue `Record` at chunk `4420490` offsets `157-163`; context: The Record of Employment (ROE) also said that the Claimant’s return to work date was unknown.
- Evidence: `reasoning_application` cue `because` at chunk `4420496` offsets `239-246`; context: She said that she asked for 61 weeks of parental benefits because she thought she was asking for 61 total weeks of leave.
- Evidence: `reasoning_application` cue `because` at chunk `4420499` offsets `127-134`; context: [21] At the hearing, the Claimant said that she did not contact the Commission about the change in her rate of weekly benefits because she assumed that the Commission had correctly calculated the rate.
- Evidence: `reasoning_application` cue `because` at chunk `4420500` offsets `264-271`; context: I think that the Claimant did not ask the Commission about the change to her benefit rate because she expected the benefit rate to change.
- Evidence: `evidence_fact` cue `evidence` at chunk `4420503` offsets `356-364`; context: I think of the Claimant’s statements at the hearing have less weight than the other evidence.
- Evidence: `reasoning_application` cue `applied` at chunk `4420503` offsets `207-214`; context: However, the Claimant made these statements more than a year after she applied for employment insurance benefits and made her election.
- Evidence: `counterargument_limitation` cue `However` at chunk `4420503` offsets `136-143`; context: However, the Claimant made these statements more than a year after she applied for employment insurance benefits and made her election.
- Evidence: `governing_rule` cue `under` at chunk `4420506` offsets `182-187`; context: The Tribunal declined to grant leave to appeal, finding that she had not established under s 58 of the Department of Employment and Social Development Act, SC 2005, c 34 that her proposed appeal had a reasonable chance of success.

#### 7983:1:subtheme:2 · paragraphs 22-24

- Raw key terms: `application, court, evidence, like, review, tribunal, accept, account`
- Display key terms: `like, review, accept, account`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: like, review, accept, account Rule/authority context: Standard of Review | [4] An application in this Court to review an evidence-based decision of a specialized decision-maker like the Tribunal can only succeed if the decision under consideration can be seen to be unreasonable. Application context: In other words, the decision will not be set aside simply because another outcome could have been possible. | [5] In Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65, [2019] SCJ No 65, the Supreme Court of Canada described the level of deference that a reviewing court is required to apply in cases like thi Evidence spans paragraphs 22-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4420507` offsets `950-955`; context: Karval’s original Record of Employment [ROE] from the Commission after the close of the hearing; and
(e) the Tribunal acted unfairly by refusing to take account of new evidence in the form of a letter from her employer dealing with the issue of Ms.
- Evidence: `evidence_fact` cue `Record` at chunk `4420507` offsets `732-738`; context: Karval’s original Record of Employment [ROE] from the Commission after the close of the hearing; and
(e) the Tribunal acted unfairly by refusing to take account of new evidence in the form of a letter from her employer dealing with the issue of Ms.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4420507` offsets `1005-1023`; context: Standard of Review
- Evidence: `issue` cue `question` at chunk `4420508` offsets `411-419`; context: The question before the Court is whether the Tribunal’s decision in this case was defensible in the assessment of the facts and the law.
- Evidence: `evidence_fact` cue `evidence` at chunk `4420508` offsets `46-54`; context: [4] An application in this Court to review an evidence-based decision of a specialized decision-maker like the Tribunal can only succeed if the decision under consideration can be seen to be unreasonable.
- Evidence: `governing_rule` cue `under` at chunk `4420508` offsets `153-158`; context: [4] An application in this Court to review an evidence-based decision of a specialized decision-maker like the Tribunal can only succeed if the decision under consideration can be seen to be unreasonable.
- Evidence: `reasoning_application` cue `because` at chunk `4420508` offsets `263-270`; context: In other words, the decision will not be set aside simply because another outcome could have been possible.
- Evidence: `reasoning_application` cue `apply` at chunk `4420509` offsets `197-202`; context: [5] In Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65, [2019] SCJ No 65, the Supreme Court of Canada described the level of deference that a reviewing court is required to apply in cases like this one:

#### 7983:1:subtheme:3 · paragraphs 25-26

- Raw key terms: `administrative, court, decision, maker, para, process, rationale, reasonableness`
- Display key terms: `administrative, maker, para, process, rationale, reasonableness`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: administrative, maker, para, process, rationale, reasonableness Application context: Accordingly, a court applying the reasonableness standard does not ask what decision it would have made in place of that of the administrative decision maker, attempt to ascertain the “range” of possible conclusions that Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4420510` offsets `315-320`; context: The role of courts in these circumstances is to review, and they are, at least as a general rule, to refrain from deciding the issue themselves.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4420510` offsets `333-344`; context: Accordingly, a court applying the reasonableness standard does not ask what decision it would have made in place of that of the administrative decision maker, attempt to ascertain the “range” of possible conclusions that would have been open to the decision maker, conduct a de novo analysis or seek to determine the “correct” solution to the problem.

#### 7983:1:subtheme:4 · paragraphs 27-29

- Raw key terms: `court, reviewing, standard, administrative, analysis, appeal, applied, assess`
- Display key terms: `reviewing, standard, administrative, analysis, applied, assess`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: reviewing, standard, administrative, analysis, applied, assess Application context: [6] In previous decisions of this Court reviewing the Tribunal’s leave to appeal decisions, the level of deference to be applied has been described as “substantial” or “high”: see Hideq v Canada, 2017 FC 439, [2017] FCJ  Evidence spans paragraphs 27-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4420512` offsets `126-133`; context: [85] Developing an understanding of the reasoning that led to the administrative decision enables a reviewing court to assess whether the decision as a whole is reasonable.
- Evidence: `reasoning_application` cue `applied` at chunk `4420513` offsets `121-128`; context: [6] In previous decisions of this Court reviewing the Tribunal’s leave to appeal decisions, the level of deference to be applied has been described as “substantial” or “high”: see Hideq v Canada, 2017 FC 439, [2017] FCJ No 438 at para 8, and Canada v O’Keefe, 2016 FC 503, [2016] FCJ No 796 at para 17.

#### Section text

Karval v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2021-05-05
Neutral citation
2021 FC 395
File numbers
T-1396-20
Decision Content
Date: 20210505
Docket: T-1396-20
Citation: 2021 FC 395
Ottawa, Ontario, May 5, 2021
PRESENT: The Honourable Mr. Justice Barnes
BETWEEN:
PREETIKA KARVAL
Applicant
and
THE ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS

[1] This application involves the Applicant’s (Ms. Karval) failed attempt to amend a claim for parental benefits payable under the Employment Insurance Act, SC 1996, c 23. When Ms. Karval filed her claim, she chose the option of receiving extended benefits but, later, she sought to receive benefits under the standard option of 35 weeks. The Canada Employment Insurance Commission [Commission] refused to amend the claim because s 23(1.2) of the Act states that such an election is irrevocable once payments have commenced. Ms. Karval appealed the Commission’s decision to the General Division of the Social Security Tribunal of Canada [General Division]. The General Division denied her appeal on the following basis:

[9] I find, on a balance of probabilities, that the Claimant elected to receive extended parental benefits. She cannot change her election to standard parental benefits because she asked for a change after she already received parental benefits.

[10] The evidence about which kind of parental benefits the Claimant chose is ambiguous. There is some evidence suggesting that the Claimant elected to receive extended parental benefits. There is also evidence suggesting that she elected to receive standard parental benefits.

[11] When the evidence is not clear one way or another, I have to decide what is most likely. I have to consider all of the evidence and make a decision on the balance of probabilities. I have to ask myself: is it more likely [than] not that the Claimant elected to receive extended parental benefits?

[12] The Claimant’s last day of work was May 10, 2019. On her application, the Claimant said that she did not know when she was going to return to work. The Record of Employment (ROE) also said that the Claimant’s return to work date was unknown.

[13] During the reconsideration process, the Claimant told the Commission that she expected to be off work for about a year. At the hearing, she said that she did not arrange a return to work date. She said that she expected to be off work for about a year.

[14] The ROE and the application both say that the Claimant did not arrange a return to work date. Several months after she stopped working, the Claimant told the Commission that she had originally planned to take a year off work. She said the same thing at the hearing. She returned to work with a new employer in March 2020. She was actually off work for about ten months.

[15] I think the earliest statements are more reliable. I give more weight to the application and the ROE. I think it is likely that the Claimant did not arrange a return to work date. The Claimant has not proven that she made an agreement with her employer to return to work after a year.

[16] On her application, the Claimant had the choice between standard parental benefits and extended parental benefits. She chose extended parental benefits. In the field asking how many weeks of parental benefits she wanted, the Claimant asked for 61 weeks of parental benefits. This is the maximum number of weeks of extended parental benefits. This means that the Claimant asked for a total of 76 weeks of benefits – 15 weeks of maternity and 61 weeks of parental benefits.

[17] There is no obvious contradiction on the application form. The Claimant said that she did not know when she was going to return to work. She asked for the maximum number of weeks of parental benefits. These statements do not contradict each other.

[18] At the hearing, the Claimant said that she did not understand the difference between maternity and parental benefits. She said that she thought it was all one type of benefit. She said that she asked for 61 weeks of parental benefits because she thought she was asking for 61 total weeks of leave. She said that she wanted the option that would give her a year of benefits. I do not think this is a credible explanation. 61 weeks is nine weeks more than a year. I do not think it is likely that the Claimant expected to return to work after about a year, but asked the Commission to pay her benefits for 14 or 15 months. I think it is more likely that the Claimant asked for 61 weeks of parental benefits because she wanted to receive benefits for longer than a year.

[19] The application form explains that the rate of weekly benefits is different, depending on which kind of parental benefits you choose. The application says that people who ask for standard parental benefits will get 55% of their normal weekly earnings. People who ask for extended parental benefits will get 33% of their normal weekly earnings.

[20] The Claimant’s benefit rate dropped to 33% of her normal weekly earnings in the week beginning September 1, 2019. The Claimant collected parental benefits at the reduced rate for nearly six months, but she did not contact the Commission to ask for an explanation. She only contacted the Commission at the end of February 2020.

[21] At the hearing, the Claimant said that she did not contact the Commission about the change in her rate of weekly benefits because she assumed that the Commission had correctly calculated the rate.

[22] I do not think the explanation is credible. I think it is more likely that she read and understood the information on the application about the rate of weekly benefits. I think that the Claimant did not ask the Commission about the change to her benefit rate because she expected the benefit rate to change. I think that the Claimant understood that she had chosen the type of parental benefits that paid 33% of her normal weekly earnings.

[23] In the letter she included with her reconsideration request, the Claimant said that she did not know that there was a deadline to change her parental benefit election. She said that the Commission did not tell her that she could change her election. The Claimant did not say that the Commission made a mistake about her election. She did not say that she meant to ask for standard parental benefits from the beginning. I think it is likely that the Claimant would have said that there was a mistake if she thought the Commission had interpreted her election incorrectly.

[24] The Claimant did not arrange to return to work after a year of leave. She chose the extended parental benefit option on her application. She asked the Commission for 61 weeks of parental benefits. This is more than a year of benefits, and it is the maximum number of extended parental benefit weeks. There are no obvious contradictions on her application about her return to work date and the number of weeks of benefits. She did not contact the Commission when her benefit rate dropped. She collected benefits at the reduced rate for nearly six months without asking the Commission for an explanation. On her reconsideration request, she said that she did not know that she could change her election. She did not say that there was a mistake about the kind of parental benefits she really meant to elect. I think all of these factors suggest that the Claimant elected to receive extended parental benefits when she completed her application.

[25] I acknowledge that, at the hearing, the Claimant said that she was confused. She said that she only meant to take a year of leave. However, the Claimant made these statements more than a year after she applied for employment insurance benefits and made her election. I think of the Claimant’s statements at the hearing have less weight than the other evidence.

[26] When I consider all of the circumstances, I think it is more likely that the Claimant elected extended parental benefits when she completed her application. I do not think it is likely that the Claimant really meant to elect standard parental benefits.

[27] The Claimant asked the Commission to change the parental benefit type after she had already collected several weeks of parental benefits. The law does not allow the Claimant to change her election after she has already received parental benefits. The Claimant cannot change her election.
[Footnotes omitted.]

[2] Ms. Karval sought to appeal the General Division decision to the Appeal Division [Tribunal]. The Tribunal declined to grant leave to appeal, finding that she had not established under s 58 of the Department of Employment and Social Development Act, SC 2005, c 34 that her proposed appeal had a reasonable chance of success. It is from this finding that this application arises.

[3] Ms. Karval’s arguments on this application largely mirror those that she has unsuccessfully advanced to the Commission, the General Division and the Tribunal. These can be summarized as follows:
(a) the Commission failed to disclose to her that there was a deadline to amend an election for parental benefits;
(b) the Commission erred by failing to find that her claim to extended parental benefits was made in error and resulted from a confusing and misleading online application;
(c) the Commission should require that claimants declare an exact return-to-work date and it should have refused to accept her statement that her return date was unknown;
(d) the General Division acted unfairly by obtaining Ms. Karval’s original Record of Employment [ROE] from the Commission after the close of the hearing; and
(e) the Tribunal acted unfairly by refusing to take account of new evidence in the form of a letter from her employer dealing with the issue of Ms. Karval’s expected return-to-work date.
I. Standard of Review

[4] An application in this Court to review an evidence-based decision of a specialized decision-maker like the Tribunal can only succeed if the decision under consideration can be seen to be unreasonable. In other words, the decision will not be set aside simply because another outcome could have been possible. This is so even where the Court might have reached a different decision on the same evidence. The question before the Court is whether the Tribunal’s decision in this case was defensible in the assessment of the facts and the law.

[5] In Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65, [2019] SCJ No 65, the Supreme Court of Canada described the level of deference that a reviewing court is required to apply in cases like this one:

[83] It follows that the focus of reasonableness review must be on the decision actually made by the decision maker, including both the decision maker’s reasoning process and the outcome. The role of courts in these circumstances is to review, and they are, at least as a general rule, to refrain from deciding the issue themselves. Accordingly, a court applying the reasonableness standard does not ask what decision it would have made in place of that of the administrative decision maker, attempt to ascertain the “range” of possible conclusions that would have been open to the decision maker, conduct a de novo analysis or seek to determine the “correct” solution to the problem. The Federal Court of Appeal noted in Delios v. Canada (Attorney General), 2015 FCA 117, 472 N.R. 171, that, “as reviewing judges, we do not make our own yardstick and then use that yardstick to measure what the administrator did”: at para. 28; see also Ryan, at paras. 50-51. Instead, the reviewing court must consider only whether the decision made by the administrative decision maker — including both the rationale for the decision and the outcome to which it led — was unreasonable.

[84] As explained above, where the administrative decision maker has provided written reasons, those reasons are the means by which the decision maker communicates the rationale for its decision. A principled approach to reasonableness review is one which puts those reasons first. A reviewing court must begin its inquiry into the reasonableness of a decision by examining the reasons provided with “respectful attention” and seeking to understand the reasoning process followed by the decision maker to arrive at its conclusion: see Dunsmuir, at para. 48, quoting D. Dyzenhaus, “The Politics of Deference: Judicial Review and Democracy”, in M. Taggart, ed., The Province of Administrative Law (1997), 279, at p. 286.

[85] Developing an understanding of the reasoning that led to the administrative decision enables a reviewing court to assess whether the decision as a whole is reasonable. As we will explain in greater detail below, a reasonable decision is one that is based on an internally coherent and rational chain of analysis and that is justified in relation to the facts and law that constrain the decision maker. The reasonableness standard requires that a reviewing court defer to such a decision.

[6] In previous decisions of this Court reviewing the Tribunal’s leave to appeal decisions, the level of deference to be applied has been described as “substantial” or “high”: see Hideq v Canada, 2017 FC 439, [2017] FCJ No 438 at para 8, and Canada v O’Keefe, 2016 FC 503, [2016] FCJ No 796 at para 17.

[7] Ms. Karval’s complaints about procedural unfairness will be considered on the standard of correctness.


## 7983:2 · paragraphs 30-50

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `21a4fa215ab7e4d442fdf8d54b883b19564099002f0ddf430caf7d0527392c0d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7983:2:subtheme:1 · paragraphs 30-37

- Raw key terms: `benefits, extended, karval, once, option, parental, claim, information`
- Display key terms: `benefits, extended, karval, once, option, parental, information`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, reasoning_application Display terms: benefits, extended, karval, once, option, parental, information Rule/authority context: 2) of the Employment Insurance Act, SC 1996, c 23, prohibits such a change once benefits have been paid under the initial election. | Indeed, the online application form clearly states that benefits under the standard option will be calculated at 55% of weekly insurable earnings and, if the extended option is chosen, at the reduced rate of 33%. Application context: Unfortunately, this is not an available option because s 23(1. Evidence spans paragraphs 30-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4420515` offsets `223-231`; context: Indeed, the Tribunal’s decision is fair, sound and in conformity with the evidence.
- Evidence: `governing_rule` cue `under` at chunk `4420515` offsets `952-957`; context: 2) of the Employment Insurance Act, SC 1996, c 23, prohibits such a change once benefits have been paid under the initial election.
- Evidence: `reasoning_application` cue `because` at chunk `4420515` offsets `833-840`; context: Unfortunately, this is not an available option because s 23(1.
- Evidence: `governing_rule` cue `under` at chunk `4420516` offsets `247-252`; context: Indeed, the online application form clearly states that benefits under the standard option will be calculated at 55% of weekly insurable earnings and, if the extended option is chosen, at the reduced rate of 33%.
- Evidence: `counterargument_limitation` cue `but` at chunk `4420516` offsets `106-109`; context: Karval was apparently unaware of this statutory limitation (see para 29 of the Tribunal decision) but that lack of knowledge is not indicative of an error by the Commission.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4420518` offsets `883-889`; context: Once the election is made and payments commence, it cannot be changed.
- Evidence: `governing_rule` cue `under` at chunk `4420520` offsets `155-160`; context: She then received parental benefits under that option for six (6) months before seeking to convert the claim to the standard option.
- Evidence: `governing_rule` cue `under` at chunk `4420521` offsets `556-561`; context: Where a claimant is actually misled by relying on official and incorrect information, certain legal recourse may be available under the doctrine of reasonable expectations.

#### 7983:2:subtheme:2 · paragraphs 38-43

- Raw key terms: `employer, application, claimant, date, division, evidence, general, return-to-work`
- Display key terms: `employer, date, division, return-to-work`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: employer, date, division, return-to-work Position/evidence statements: She argues that the Tribunal ought to have seen from the evidence that she had always intended to return to work after one (1) year and that the Commission erred in accepting her application for extended benefits at face | [34] The Claimant has tried to submit the employer letter to this appeal, but the Appeal Division told her that it could not consider new evidence that was not before the General Division when it made its decision. Evidence spans paragraphs 38-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4420522` offsets `426-431`; context: She also argues that the Tribunal erred by refusing to receive into evidence a letter from her employer clarifying the issue of when she would be returning to work.
- Evidence: `party_position` cue `argues` at chunk `4420522` offsets `83-89`; context: She argues that the Tribunal ought to have seen from the evidence that she had always intended to return to work after one (1) year and that the Commission erred in accepting her application for extended benefits at face value.
- Evidence: `evidence_fact` cue `evidence` at chunk `4420522` offsets `136-144`; context: She argues that the Tribunal ought to have seen from the evidence that she had always intended to return to work after one (1) year and that the Commission erred in accepting her application for extended benefits at face value.
- Evidence: `counterargument_limitation` cue `However` at chunk `4420523` offsets `207-214`; context: However, the General Division did not accept that it could rescind or amend based on the letter.
- Evidence: `party_position` cue `submit` at chunk `4420524` offsets `31-37`; context: [34] The Claimant has tried to submit the employer letter to this appeal, but the Appeal Division told her that it could not consider new evidence that was not before the General Division when it made its decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `4420524` offsets `138-146`; context: [34] The Claimant has tried to submit the employer letter to this appeal, but the Appeal Division told her that it could not consider new evidence that was not before the General Division when it made its decision.
- Evidence: `counterargument_limitation` cue `but` at chunk `4420524` offsets `74-77`; context: [34] The Claimant has tried to submit the employer letter to this appeal, but the Appeal Division told her that it could not consider new evidence that was not before the General Division when it made its decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `4420525` offsets `18-26`; context: [35] There was no evidence before the General Division that could have supported a finding that the Claimant had made an agreement with her employer to return to work after a year.
- Evidence: `evidence_fact` cue `evidence` at chunk `4420527` offsets `75-83`; context: [39] The General Division was entitled to consider the application form as evidence that the Claimant did not know when she would be returning to work.

#### 7983:2:subtheme:3 · paragraphs 44-45

- Raw key terms: `application, commission, date, decision, division, employer, error, even`
- Display key terms: `commission, date, division, employer, error, even`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: commission, date, division, employer, error, even Position/evidence statements: This means that the Claimant had to find and submit evidence to show the General Division that the Commission decision was wrong. Rule/authority context: Karval made a clear election to receive extended benefits, gave the Commission no indication she was confused, made no timely inquiries of her own to clarify her options, received extended benefits in a reduced amount fo Evidence spans paragraphs 44-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `4420528` offsets `302-309`; context: Whether or not that would be appropriate, neither the Claimant nor the employer identified a return-to-work date in this case.
- Evidence: `party_position` cue `submit` at chunk `4420528` offsets `112-118`; context: This means that the Claimant had to find and submit evidence to show the General Division that the Commission decision was wrong.
- Evidence: `evidence_fact` cue `evidence` at chunk `4420528` offsets `119-127`; context: This means that the Claimant had to find and submit evidence to show the General Division that the Commission decision was wrong.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4420528` offsets `515-521`; context: The Claimant cannot show that the General Division made an error by not considering evidence that was not even before it.
- Evidence: `evidence_fact` cue `evidence` at chunk `4420529` offsets `74-82`; context: [16] There is nothing unreasonable about the Tribunal’s assessment of the evidence as stated above.
- Evidence: `governing_rule` cue `under` at chunk `4420529` offsets `1466-1471`; context: Karval made a clear election to receive extended benefits, gave the Commission no indication she was confused, made no timely inquiries of her own to clarify her options, received extended benefits in a reduced amount for six (6) months and, under s 23(1.

#### 7983:2:subtheme:4 · paragraphs 46-50

- Raw key terms: `date, declared, karval, return-to-work, application, breach, commission, division`
- Display key terms: `date, declared, karval, return-to-work, breach, commission, division`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue Display terms: date, declared, karval, return-to-work, breach, commission, division Operative outcome context: [20] For the foregoing reasons, this application is dismissed. Evidence spans paragraphs 46-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4420530` offsets `463-468`; context: Karval took no issue with this approach and she made no further submissions about the significance of this document to her appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `4420531` offsets `174-182`; context: However, when asked, she was unable to say how its acceptance into evidence could have made a difference to the outcome.
- Evidence: `counterargument_limitation` cue `However` at chunk `4420531` offsets `107-114`; context: However, when asked, she was unable to say how its acceptance into evidence could have made a difference to the outcome.
- Evidence: `disposition` cue `dismissed` at chunk `4420533` offsets `52-61`; context: [20] For the foregoing reasons, this application is dismissed.

#### Section text

II. Analysis

[8] Having considered the Tribunal’s decision in this case against the standards of review described above, I can identify no basis to set it aside. Indeed, the Tribunal’s decision is fair, sound and in conformity with the evidence. While Ms. Karval alleges errors on the part of the Commission, the General Division and the Tribunal, their respective refusals to provide relief were justified, particularly in the face of information she provided and the choices she made. What seems to have occurred is that Ms. Karval elected to receive extended parental and maternity benefits based on her uncertain return-to-work date. Then, after receiving reduced benefits for six (6) months, she had second thoughts. She sought to reduce the claim period in order to recover enhanced benefits. Unfortunately, this is not an available option because s 23(1.2) of the Employment Insurance Act, SC 1996, c 23, prohibits such a change once benefits have been paid under the initial election.

[9] Ms. Karval was apparently unaware of this statutory limitation (see para 29 of the Tribunal decision) but that lack of knowledge is not indicative of an error by the Commission. Indeed, the online application form clearly states that benefits under the standard option will be calculated at 55% of weekly insurable earnings and, if the extended option is chosen, at the reduced rate of 33%. The application also includes the following information:
Once parental benefits have been paid on the claim, the choice between standard and extended parental benefits is irrevocable.

[10] Ms. Karval chose the extended option and cannot complain that the Commission somehow misled her or should have told her again that she could not change her election once benefits had been paid.

[11] There are also problems with Ms. Karval’s assertion that the application for benefits is bereft of necessary information and is otherwise confusing, all of which led her astray. One problem is that the questions Ms. Karval now says were confusing are not objectively so and the explanations provided to claimants are not particularly lacking in information. This program itself is not overly complicated to understand. Maternity benefits are payable for 15 weeks followed by parental benefits which can be claimed by either or both parents. Parental benefits can be claimed in one of two ways. A claim to standard benefits allows for payments at the rate of 55% of weekly insurable earnings payable over 35 weeks. A claim to extended benefits allows for reduced payments (33%) payable over an extended term of up to 61 weeks. Once the election is made and payments commence, it cannot be changed.

[12] The online application describes the parental benefit program in the following way:
Parental Information
Answers to fields and questions with an asterisk (*) are mandatory.
Parental benefits are payable only to the biological, adoptive, or legally recognized parents while they are caring for their newborn or newly adopted child.
In order to be considered a legal parent for the purposes of receiving EI parental benefits, when not the birth or adoptive parent, an individual has to be recognized as such by their province or territory on the birth registration and have taken leave from work to care for the child or children.
Standard option:
 The benefit rate is 55% of your weekly insurable earnings up to a maximum amount.
 Up to 35 weeks of benefits payable to one parent.
 If parental benefits are shared, up to a combined total of 40 weeks payable if the child was born or placed for the purpose of adoption on or after March 17, 2019.
Extended option:
 The benefit rate is 33% of your weekly insurable earnings up to a maximum amount.
 Up to 61 weeks of benefits payable to one parent.
 If parental benefits are shared, up to a combined total of 69 weeks payable if the child was born or placed for the purpose of adoption on or after March 17, 2019.
If parental benefits are being shared, the parental benefit option selected by the parent who first makes a claim is binding on the other parent(s).
You must choose the same option as the other parent(s) to avoid delays or incorrect payments of benefits.
Once parental benefits have been paid on the claim, the choice between standard and extended parental benefits is irrevocable.
* Select the type of parental benefits you are applying for:
¡ Standard option
¤ Extended option
[Emphasis added.]

[13] In answer to the questions posed above, Ms. Karval unequivocally chose the extended option payable over 61 weeks. She then received parental benefits under that option for six (6) months before seeking to convert the claim to the standard option.

[14] While it may well be that Ms. Karval was uncertain about the maternity and parental leave program, it cannot fairly be said that her clear choices resulted from being misled by the Commission. It is undoubtedly the case that many government benefit programs will have complex features and strict eligibility requirements. More information, clearer language and better explanations can almost always be proposed in hindsight. Where a claimant is actually misled by relying on official and incorrect information, certain legal recourse may be available under the doctrine of reasonable expectations. However, where a claimant like Ms. Karval is not misled but merely lacks the knowledge necessary to accurately answer unambiguous questions, no legal remedies are available. Fundamentally it is the responsibility of a claimant to carefully read and attempt to understand their entitlement options and, if still in doubt, to ask the necessary questions. Ms. Karval deliberately selected the extended benefit option and, had she read the application, she would have understood that the parental payments would be reduced. She would also have appreciated that once parental benefits were paid her election was irrevocable. These things are clearly stated on the application and were at the heart of the General Division’s dismissal of her appeal and the Tribunal’s decision to deny leave to further appeal.

[15] Ms. Karval also complains about the treatment of her return-to-work date. She argues that the Tribunal ought to have seen from the evidence that she had always intended to return to work after one (1) year and that the Commission erred in accepting her application for extended benefits at face value. She also argues that the Tribunal erred by refusing to receive into evidence a letter from her employer clarifying the issue of when she would be returning to work. The Tribunal’s treatment of these issues is set out in the following paragraphs from its decision:

[33] I note that the Claimant sent the General Division a letter from her employer with her rescind or amend application. In the letter, the employer wrote about the Claimant’s expected return-to-work date. However, the General Division did not accept that it could rescind or amend based on the letter. The Claimant appealed that refusal to the Appeal Division (AD-20-778) as a separate matter from this appeal.

[34] The Claimant has tried to submit the employer letter to this appeal, but the Appeal Division told her that it could not consider new evidence that was not before the General Division when it made its decision. The General Division did not have the letter from the Claimant’s employer when it made the June 18, 2020, decision that is on appeal here.

[35] There was no evidence before the General Division that could have supported a finding that the Claimant had made an agreement with her employer to return to work after a year. The General Division noted that the Claimant herself testified that she had not arranged a return-to-work date with her employer. It considered that the Claimant said she did not know when she would return to work in her application for benefits. It also considered the original ROE, in which her employer wrote that her return to work date was “unknown”.
…

[38] Neither the Claimant, nor the employer gave the Commission an expected date of return. The benefit application form allows an applicant to indicate an expected date of return to work. The application form asks claimants if they know the date they will be returning to work. If a claimant answers “yes”, the form asks for the expected date of return. The Claimant stated that she did not know when she would be returning to work. The ROE document allows an employer to indicate the expected date of return to be completed. It has a section in which it asks for the expected date of recall to work, but it allows the employer to tick off a box for “unknown.” The employer ticked off the “unknown” box.

[39] The General Division was entitled to consider the application form as evidence that the Claimant did not know when she would be returning to work. It was also entitled to consider the original ROE as evidence that the employer did not know her return-to-work date. The General Division must make a decision on all the evidence that is before it, and it is entitled to weigh that evidence as it sees fit.

[40] The Claimant had the burden of proof at the General Division. This means that the Claimant had to find and submit evidence to show the General Division that the Commission decision was wrong. The Claimant thinks that the application form and the ROE should require a specific return-to-work date. Whether or not that would be appropriate, neither the Claimant nor the employer identified a return-to-work date in this case. The General Division needed to decide based on the evidence that it had. The Claimant cannot show that the General Division made an error by not considering evidence that was not even before it.
[Footnotes omitted.]

[16] There is nothing unreasonable about the Tribunal’s assessment of the evidence as stated above. Ms. Karval did not establish that an error was made in identifying her expected return-to-work date. Her application clearly stated that she did not know when she would be returning to work. If she had a known date of return, she had the option of declaring it on her application. Instead she elected to receive extended benefits payable over 61 weeks even though she could have chosen other options (see Tribunal decision at para 46). Both the original and the amended ROE provided by her employer stated that her return-to-work date was “unknown”. She also testified to the General Division that a firm date of return had not been arranged with her employer. On this record, there is no basis for Ms. Karval’s argument that the Commission owed her some heightened obligation to seek more information from her than what she had already provided. There is also nothing very confusing about the application completed by Ms. Karval. If she found it perplexing, she could have called the Commission instead of providing answers that, she now says, were inconsistent with her true intentions. Reduced to its simplest terms, Ms. Karval made a clear election to receive extended benefits, gave the Commission no indication she was confused, made no timely inquiries of her own to clarify her options, received extended benefits in a reduced amount for six (6) months and, under s 23(1.2) of the Employment Insurance Act, above, was precluded from changing her election. In these circumstances, the Tribunal’s decision that Ms. Karval’s appeal had no reasonable chance of success was, itself, reasonable.

[17] As the Tribunal found, there was no breach of fairness from the General Division’s post-hearing request to the Commission for a copy of Ms. Karval’s original ROE. The General Division made this request to see if it disclosed a different return-to-work date than the one declared in the amended ROE. The General Division told Ms. Karval it would make this request, copied her on the request and emailed the ROE to her when it was received. Ms. Karval took no issue with this approach and she made no further submissions about the significance of this document to her appeal.

[18] Ms. Karval now says that she did not know that she could have made further submissions about the ROE. However, when asked, she was unable to say how its acceptance into evidence could have made a difference to the outcome. In the end, both ROEs declared the same thing — that Ms. Karval’s return-to-work date was then unknown. The original ROE added nothing new and was not material to the outcome of the case. In these circumstances, it was not a breach of fairness to have obtained it from the Commission after the hearing.

[19] Ms. Karval also says that it was unfair and inconsistent for the Tribunal to reject a letter from her employer which also concerned her return-to-work date. The letter was not put to the General Division and the Tribunal rejected it on that basis. It is of equal significance that the letter did not contradict what the employer had recorded in the ROEs or what Ms. Karval had declared in her application. The letter simply stated that as of November 07, 2019 it was “anticipated that she will return from leave in May 2020”. This is fully consistent with the General Division’s conclusion that when she filed her application in May 2019 her return-to-work date was unknown and this only changed after the date of election irrevocability. In short, the employer’s letter is not corroborative of Ms. Karval’s contention that she always intended to return to work after one year of leave and the Tribunal’s refusal to receive it was neither material to the decision nor unfair.

[20] For the foregoing reasons, this application is dismissed.

[21] No costs are sought and none are ordered.


## 7983:3 · paragraphs 51-52

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7f961b258d4d7c54cbe6b55ef02c749ebe0dceaa5a8afcdb4457f4f379207fce`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7983:3:subtheme:1 · paragraphs 51-52

- Raw key terms: `t-1396-20, alberta, april, attorney, barnes, calgary, canada, cause`
- Display key terms: `t-1396-20, alberta, april, barnes, calgary`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: t-1396-20, alberta, april, barnes, calgary Operative outcome context: JUDGMENT IN T-1396-20 THIS COURT’S JUDGMENT is that this judicial review is dismissed. Evidence spans paragraphs 51-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4420534` offsets `123-132`; context: JUDGMENT IN T-1396-20
THIS COURT’S JUDGMENT is that this judicial review is dismissed.

#### Section text

JUDGMENT IN T-1396-20
THIS COURT’S JUDGMENT is that this judicial review is dismissed.
"R.L. Barnes"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
Docket:
T-1396-20
STYLE OF CAUSE:
PREETIKA KARVAL v THE ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
Ottawa, Ontario
CALGARY, ALBERTA
EDMONTON, ALBERTA
DATE OF HEARING:
April 15, 2021
REASONS FOR 

## 7983:4 · paragraphs 53-53

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b7e38608450575cc772e2973472561afcc2a000f6b07f37e8a0a0a1ae2a3fa9f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7983:4:subtheme:1 · paragraphs 53-53

- Raw key terms: `appearances, applicant, attorney, barnes, behalf, canada, chao, dated`
- Display key terms: `barnes, behalf, chao, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barnes, behalf, chao, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 53-53. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND JUDGMENT:
BARNES J.
DATED:
May 5, 2021
APPEARANCES:
Preetika Karval
For The Applicant
(ON HER OWN BEHALF)
Matthew Chao
For The Respondent
SOLICITORS OF RECORD:
N/A
For The Applicant
Attorney General of Canada
Edmonton, AB
For The Respondent
