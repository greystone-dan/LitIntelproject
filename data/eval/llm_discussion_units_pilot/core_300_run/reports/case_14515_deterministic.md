# Discussion Units: case 14515

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **29**
- Continuity pairs: **28**
- Discussion Units: **2**
- Paragraph source hashes: **29**
- Sub-themes: **8**

## 14515:1 · paragraphs 0-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fd72f56106b856353cbbbff54e12a3272b4589b705b1366519289b597956dff0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 14515:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `applicant, canada, applicant's, decision, father, immigration, order, persecution`
- Display key terms: `applicant's, father, order, persecution`
- Argument roles: `governing_rule`
- Explanation: Observed roles: governing_rule Display terms: applicant's, father, order, persecution Rule/authority context: The applicant's family and especially her brother were under police surveillance in Punjab for a few years, due to their association with suspected Sikh militants. Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4708969` offsets `145-150`; context: The applicant's family and especially her brother were under police surveillance in Punjab for a few years, due to their association with suspected Sikh militants.

#### 14515:1:subtheme:2 · paragraphs 5-10

- Raw key terms: `applicant, board, canada, evidence, credibility, immigration, minister, para`
- Display key terms: `credibility, para`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: credibility, para Position/evidence statements: [6] The applicant contends that the Board's negative credibility findings were made in a perverse or capricious manner or without regard to the evidence. Application context: [9] Normally, the Board is entitled to conclude that an applicant is not credible because of implausibilities in his or her evidence as long as its inferences are not unreasonable and its reasons are set out in "clear an Evidence spans paragraphs 5-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4708971` offsets `121-126`; context: [5] The Board determined that the applicant was not a Convention refugee, stating that credibility was the determinative issue in her claim.
- Evidence: `evidence_fact` cue `determined that` at chunk `4708971` offsets `14-29`; context: [5] The Board determined that the applicant was not a Convention refugee, stating that credibility was the determinative issue in her claim.
- Evidence: `issue` cue `whether` at chunk `4708972` offsets `167-174`; context: To determine whether that is the case, the Court has to examine the Board's decision in light of the extensive jurisprudential guidelines pertaining to CRDD credibility assessments.
- Evidence: `party_position` cue `contends` at chunk `4708972` offsets `18-26`; context: [6] The applicant contends that the Board's negative credibility findings were made in a perverse or capricious manner or without regard to the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4708972` offsets `144-152`; context: [6] The applicant contends that the Board's negative credibility findings were made in a perverse or capricious manner or without regard to the evidence.
- Evidence: `evidence_fact` cue `found that` at chunk `4708973` offsets `113-123`; context: This Court has found that the Board has well-established expertise in the determination of questions of fact, particularly in the evaluation of the credibility and the subjective fear of persecution of an applicant: see Rahaman v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4708974` offsets `103-111`; context: [8] Moreover, it has been recognized and confirmed that, with respect to credibility and assessment of evidence, this Court may not substitute its decision for that of the Board when the applicant has failed to prove that the Board's decision was based on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it: see Akinlolu v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4708975` offsets `124-132`; context: [9] Normally, the Board is entitled to conclude that an applicant is not credible because of implausibilities in his or her evidence as long as its inferences are not unreasonable and its reasons are set out in "clear and unmistakable terms": see Hilo v.
- Evidence: `reasoning_application` cue `conclude` at chunk `4708975` offsets `39-47`; context: [9] Normally, the Board is entitled to conclude that an applicant is not credible because of implausibilities in his or her evidence as long as its inferences are not unreasonable and its reasons are set out in "clear and unmistakable terms": see Hilo v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4708976` offsets `305-313`; context: The Board may reject uncontradicted evidence if it is not consistent with the probabilities affecting the case as a whole, or where inconsistencies are found in the evidence: see Akinlolu, supra, at para.

#### 14515:1:subtheme:3 · paragraphs 11-17

- Raw key terms: `board, canada, applicant's, employment, evidence, general, immigration, minister`
- Display key terms: `applicant's, employment`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: applicant's, employment Rule/authority context: [15] I will now turn to the particular facts of the case under review. Application context: [12] Furthermore, the Board should not be quick to apply the North American logic and reasoning to the claimant's behaviour: consideration should be given to the claimant's age, cultural background and previous social ex | [13] A person's first story is usually the most genuine and, therefore, the one to be most believed. Evidence spans paragraphs 11-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4708977` offsets `270-276`; context: It would not be proper for the Board to base its findings on extensive "microscopic" examination of issues irrelevant or peripheral to the applicant's claim: see Attakora v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4708977` offsets `83-91`; context: [11] However, not every kind of inconsistency or implausibility in the applicant's evidence will reasonably support the Board's negative findings on overall credibility.
- Evidence: `evidence_fact` cue `testimony` at chunk `4708978` offsets `485-494`; context: Likewise, a lack of coherency or consistency in the claimant's testimony should be viewed in light of the claimant's psychological condition, especially where it has been medically documented: see Reyes v.
- Evidence: `reasoning_application` cue `apply` at chunk `4708978` offsets `51-56`; context: [12] Furthermore, the Board should not be quick to apply the North American logic and reasoning to the claimant's behaviour: consideration should be given to the claimant's age, cultural background and previous social experiences: see Rahnema v.
- Evidence: `reasoning_application` cue `therefore` at chunk `4708979` offsets `61-70`; context: [13] A person's first story is usually the most genuine and, therefore, the one to be most believed.
- Evidence: `counterargument_limitation` cue `although` at chunk `4708979` offsets `118-126`; context: That being said, although the failure to report a fact can be a cause for concern, it should not always be so.
- Evidence: `evidence_fact` cue `testimony` at chunk `4708980` offsets `66-75`; context: [14] Finally, the applicant's credibility and the plausibility of testimony should be assessed in the context of her country's conditions and other documentary evidence available to the Board.
- Evidence: `evidence_fact` cue `evidence` at chunk `4708981` offsets `298-306`; context: In light of the particular circumstances of this case, taking into account the evidence on record and considering the impugned decision as a whole, I find that the Board's general conclusion is patently unreasonable.
- Evidence: `governing_rule` cue `under` at chunk `4708981` offsets `57-62`; context: [15] I will now turn to the particular facts of the case under review.
- Evidence: `reasoning_application` cue `I find` at chunk `4708981` offsets `367-373`; context: In light of the particular circumstances of this case, taking into account the evidence on record and considering the impugned decision as a whole, I find that the Board's general conclusion is patently unreasonable.
- Evidence: `counterargument_limitation` cue `however` at chunk `4708981` offsets `189-196`; context: No decision-maker, however, can act arbitrarily.
- Evidence: `counterargument_limitation` cue `however` at chunk `4708982` offsets `816-823`; context: She, however, remained vague in her responses" (page 4, paragraph 1), and finally, that "[s]he was asked why there is no mention of her arrests, for example, in December 1999" [at her Port of Entry Statement] - for which the Board continues: "Her explanation that the interpreter had told her to write few words [sic] what had happened to her in India is not accepted by the panel" (page 4, paragraph 2).
- Evidence: `evidence_fact` cue `evidence` at chunk `4708983` offsets `335-343`; context: According to the psychological report, which was in evidence and remained uncontroverted, it caused the applicant tremendous stress to discuss her experiences relevant to the claim.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `4708983` offsets `694-706`; context: The Board, nevertheless, in the impugned decision, "noticed no problems in her manner of testifying, finding her to be alert and aware" - omitting to mention the important fact that the applicant once broke down while testifying and had to be taken to hospital.

#### 14515:1:subtheme:4 · paragraphs 18-20

- Raw key terms: `claim, credibility, finding, negative, alleged, applicant, applicant's, authorities`
- Display key terms: `credibility, finding, negative, alleged, applicant's, authorities`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: credibility, finding, negative, alleged, applicant's, authorities Application context: Therefore, it is natural to expect that the applicant would not be very clear in her recollection of making a refugee claim. Evidence spans paragraphs 18-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4708984` offsets `82-87`; context: [18] Third, a major difficulty with the impugned decision is that, except for the issue of the applicant's election card, where the Board finds that "she .
- Evidence: `evidence_fact` cue `evidence` at chunk `4708984` offsets `321-329`; context: In light of evidence on record, I cannot accept the position of counsel for the respondent that any of these findings, individually or cumulatively, can reasonably sustain the general conclusion reached by the Board, and in particular as follows:
(a) In view of the specific circumstances of this case, I am ready to accept that the applicant's alleged maltreatment by the police in India would have made her suspicious and afraid of any official functionaries and would have made her communication with Canadian immigration authorities inherently stressful.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4708984` offsets `868-877`; context: Therefore, it is natural to expect that the applicant would not be very clear in her recollection of making a refugee claim.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4708984` offsets `343-349`; context: In light of evidence on record, I cannot accept the position of counsel for the respondent that any of these findings, individually or cumulatively, can reasonably sustain the general conclusion reached by the Board, and in particular as follows:
(a) In view of the specific circumstances of this case, I am ready to accept that the applicant's alleged maltreatment by the police in India would have made her suspicious and afraid of any official functionaries and would have made her communication with Canadian immigration authorities inherently stressful.
- Evidence: `evidence_fact` cue `testimony` at chunk `4708986` offsets `209-218`; context: [20] There is no doubt that a failure to mention the key events on which the refugee claim is based in a written statement to immigration authorities, or an inconsistency between such statement and subsequent testimony, are very serious matters that can potentially sustain a negative credibility finding.
- Evidence: `counterargument_limitation` cue `However` at chunk `4708986` offsets `306-313`; context: However, the omission or inconsistency must be real: see Rajaratnam v.

#### 14515:1:subtheme:5 · paragraphs 21-23

- Raw key terms: `insulted, police, applicant, applicant's, board, decision, entry, evidence`
- Display key terms: `insulted, police, applicant's, entry`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: insulted, police, applicant's, entry Application context: The police insulted me because my brother had left the house and gone away. Evidence spans paragraphs 21-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4708987` offsets `236-243`; context: The police insulted me because my brother had left the house and gone away.
- Evidence: `evidence_fact` cue `evidence` at chunk `4708988` offsets `727-735`; context: Considering the evidence on record and the Board's expert knowledge, making this unauthorized inference constituted a reviewable error.
- Evidence: `evidence_fact` cue `evidence` at chunk `4708989` offsets `183-191`; context: This particular view is confirmed by the documentary evidence which was before the Board and which seems to have been completely overlooked in the impugned decision.

#### 14515:1:subtheme:6 · paragraphs 24-25

- Raw key terms: `amount, applicant, arrest, entry, port, reasons, record, statement`
- Display key terms: `amount, arrest, entry, port, statement`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: amount, arrest, entry, port, statement Rule/authority context: In Lives Under Threat: A Study of Sikhs Coming to the UK from the Punjab (certified record, at page 213), it is noted as follows: There are many reasons why an applicant, having arrived in the UK, may not present his cas | The Board was, of course, under no obligation to accept any of this evidence, but the Board's decision fails to establish that the evidence received sufficient attention and consideration. Application context: I find her explanation totally reasonable in the particular circumstances of this case. | For those reasons, I conclude that the Board's general negative credibility finding is patently unreasonable, and that the Board's decision was based on findings of fact made in a perverse or capricious manner or without Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4708990` offsets `168-176`; context: [24] When asked at the hearing about her failure to mention her arrest in the Port of Entry Statement, the applicant replied that the amount of space allocated to that question in the form, as well as the interpreter's instructions, prompted her to make her statement brief.
- Evidence: `evidence_fact` cue `record` at chunk `4708990` offsets `447-453`; context: In Lives Under Threat: A Study of Sikhs Coming to the UK from the Punjab (certified record, at page 213), it is noted as follows:
There are many reasons why an applicant, having arrived in the UK, may not present his case for asylum to the best advantage.
- Evidence: `governing_rule` cue `Under` at chunk `4708990` offsets `372-377`; context: In Lives Under Threat: A Study of Sikhs Coming to the UK from the Punjab (certified record, at page 213), it is noted as follows:
There are many reasons why an applicant, having arrived in the UK, may not present his case for asylum to the best advantage.
- Evidence: `reasoning_application` cue `I find` at chunk `4708990` offsets `275-281`; context: I find her explanation totally reasonable in the particular circumstances of this case.
- Evidence: `issue` cue `issues` at chunk `4708991` offsets `759-765`; context: Furthermore, in its zealous pursuit of inconsistencies, the Board placed too much importance on peripheral elements and failed to focus on the real issues that were before it: the applicant's subjective fear of persecution and the objective basis for such fear.
- Evidence: `evidence_fact` cue `evidence` at chunk `4708991` offsets `75-83`; context: [25] In summary, most of the problems the Board finds with the applicant's evidence are either imaginary or irrelevant to her claim.
- Evidence: `governing_rule` cue `under` at chunk `4708991` offsets `1360-1365`; context: The Board was, of course, under no obligation to accept any of this evidence, but the Board's decision fails to establish that the evidence received sufficient attention and consideration.
- Evidence: `reasoning_application` cue `conclude` at chunk `4708991` offsets `1544-1552`; context: For those reasons, I conclude that the Board's general negative credibility finding is patently unreasonable, and that the Board's decision was based on findings of fact made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `counterargument_limitation` cue `but` at chunk `4708991` offsets `1412-1415`; context: The Board was, of course, under no obligation to accept any of this evidence, but the Board's decision fails to establish that the evidence received sufficient attention and consideration.

#### 14515:1:subtheme:7 · paragraphs 26-27

- Raw key terms: `accordance, allowed, applicant, applicant's, application, aside, back, canada`
- Display key terms: `accordance, allowed, applicant's, aside, back`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: accordance, allowed, applicant's, aside, back Operative outcome context: [26] As a result, this application for judicial review will be allowed, the negative CRDD decision quashed, and the matter sent back for reconsideration by a differently constituted panel. Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4708992` offsets `192-200`; context: No question of general importance is raised by counsel and no such question will be certified by the Court.
- Evidence: `evidence_fact` cue `determined that` at chunk `4708992` offsets `470-485`; context: The decision of the Refugee Division, dated June 12, 2002, wherein the Convention Refugee Determination Division determined that the applicant was not a Convention refugee, is set aside.
- Evidence: `disposition` cue `allowed` at chunk `4708992` offsets `63-70`; context: [26] As a result, this application for judicial review will be allowed, the negative CRDD decision quashed, and the matter sent back for reconsideration by a differently constituted panel.

#### Section text

Lubana v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2003-02-03
Neutral citation
2003 FCT 116
File numbers
IMM-2936-02
Decision Content
Date: 20030203
Docket: IMM-2936-02
Neutral citation: 2003 FCT 116
OTTAWA, ONTARIO, THIS 3rd DAY OF FEBRUARY 2003
PRESENT: THE HONOURABLE MR. JUSTICE LUC MARTINEAU
BETWEEN:
RAJWANT KAUR LUBANA
Applicant
- and -
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR ORDER AND ORDER

[1] This is an application for judicial review of a decision of the Convention Refugee Determination Division, Immigration and Refugee Board of Canada ("CRDD" or the "Board"), rendered on June 12, 2002, wherein the applicant was found not to be a Convention refugee as defined in subsection 2(1) of the Immigration Act, R.S.C. 1985, c. I-2 (the "Act").

[2] The applicant is a woman from rural India who has never worked and has attended school for ten years. She alleges a well-founded fear of persecution by police authorities in her native Punjab on the grounds of her imputed political opinion and membership in a particular social group as a Sikh woman.

[3] The applicant's allegations of past persecution can be briefly summarized as follows. The applicant's family and especially her brother were under police surveillance in Punjab for a few years, due to their association with suspected Sikh militants. The applicant's brother was arrested twice, subjected to cruel treatment, and required to report to the police. When he went into hiding, the police repeatedly raided the applicant's house in search for him. The police brutality grew from visit to visit and culminated in the arrest of the applicant and her father in December 1999. In detention, the applicant was physically and sexually assaulted, and her father was tortured.

[4] Upon release, the applicant and her father sought the assistance of an agent in Bombay in order to leave the country. The agent arranged false travel documents for the applicant and sent her to Canada, where she made her refugee claim immediately upon arrival. The applicant's father was supposedly sent to Moscow, and his present whereabouts are unknown.

[5] The Board determined that the applicant was not a Convention refugee, stating that credibility was the determinative issue in her claim. The Board simply disbelieved the applicant's story, observing that she "was not straightforward in answering certain questions" and noting the following problems with her evidence:
1. While testifying, the applicant stated that she did not remember much about making her refugee claim. She was not clear or consistent about whether the agent had instructed her to claim refugee status upon arrival.
2. At the port of entry, the applicant stated that she was travelling on her own genuine passport. In the Personal Information Form (PIF), she stated that she had travelled on a false passport. At the hearing, she confirmed the PIF version, explaining that the false passport had been provided by her agent and that her statement at the port of entry was prompted by the agent's instruction.
3. The applicant testified that she had travelled to Canada from Bombay via Korea and the United States, and that the agent had accompanied her all the way except the very last flight, held her documents and did all the talking while crossing border controls. The applicant did not remember the exact place of transit in the United States and could not explain how the agent could have escorted her to the plane destined for Vancouver without being a passenger.
4. The applicant's testimony with regard to her election card, one of the few identity documents presented, appeared inconsistent. The applicant was unclear about when the card was issued in India and how she came to possess it in Canada.
5. The applicant's written statement at the port of entry did not mention her arrest in December 1999. The latter was "an important event, which allegedly had happened to her prompting [her] to leave India. It does not take much to say that she had been detained then".

[6] The applicant contends that the Board's negative credibility findings were made in a perverse or capricious manner or without regard to the evidence. To determine whether that is the case, the Court has to examine the Board's decision in light of the extensive jurisprudential guidelines pertaining to CRDD credibility assessments.
THE LAW: CRDD CREDIBILITY FINDINGS

[7] The determination of an applicant's credibility is the heartland of the Board's jurisdiction. This Court has found that the Board has well-established expertise in the determination of questions of fact, particularly in the evaluation of the credibility and the subjective fear of persecution of an applicant: see Rahaman v. Canada (Minister of Citizenship and Immigration), [2000] F.C.J. No. 1800 at para. 38 (QL) (T.D.); and Cepeda-Gutierrez v. Canada (Minister of Citizenship and Immigration) (1998), 157 F.T.R. 35 at para. 14.

[8] Moreover, it has been recognized and confirmed that, with respect to credibility and assessment of evidence, this Court may not substitute its decision for that of the Board when the applicant has failed to prove that the Board's decision was based on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it: see Akinlolu v. Canada (Minister of Citizenship and Immigration), [1997] F.C.J. No. 296 at para. 14 (QL) (T.D.) ("Akinlolu"); Kanyai v. Canada (Minister of Citizenship and Immigration), [2002] F.C.J. No. 1124 at para. 9 (QL) (T.D.) ("Kanyai"); and the grounds for review set out in paragraph 18.1(4)(d) of the Federal Court Act.

[9] Normally, the Board is entitled to conclude that an applicant is not credible because of implausibilities in his or her evidence as long as its inferences are not unreasonable and its reasons are set out in "clear and unmistakable terms": see Hilo v. Canada (Minister of Employment and Immigration) (1991), 130 N.R. 236 (F.C.A.); Aguebor v. Canada (Minister of Employment and Immigration) (1993), 160 N.R. 315 (F.C.A.) ("Aguebor"); Zhou v. Canada (Minister of Citizenship and Immigration), [1994] F.C.J. No. 1087 (QL) (C.A.); and Kanyai, supra, at para. 10.

[10] Furthermore, the Board is entitled to make reasonable findings based on implausibilities, common sense and rationality: see Shahamati v. Canada (Minister of Employment and Immigration), [1994] F.C.J. No. 415 at para. 2 (QL) (C.A.); and Aguebor, supra, at para. 4. The Board may reject uncontradicted evidence if it is not consistent with the probabilities affecting the case as a whole, or where inconsistencies are found in the evidence: see Akinlolu, supra, at para. 13; and Kanyai, supra, at para. 11.

[11] However, not every kind of inconsistency or implausibility in the applicant's evidence will reasonably support the Board's negative findings on overall credibility. It would not be proper for the Board to base its findings on extensive "microscopic" examination of issues irrelevant or peripheral to the applicant's claim: see Attakora v. Canada (Minister of Employment and Immigration), (1989), 99 N.R. 168 at para. 9 (F.C.A.) ("Attakora"); and Owusu-Ansah v. Canada (Minister of Employment and Immigration), [1989] F.C.J. No. 442 (QL) (C.A.) ("Owusu-Ansah"). In particular, where a claimant travels on false documents, destroys travel documents or lies about them upon arrival following an agent's instructions, it has been held to be peripheral and of very limited value to a determination of general credibility: see Attakora, supra; and Takhar v. Canada (Minister of Citizenship and Immigration), [1999] F.C.J. No. 240 at para. 14 (QL) (T.D.) ("Takhar").

[12] Furthermore, the Board should not be quick to apply the North American logic and reasoning to the claimant's behaviour: consideration should be given to the claimant's age, cultural background and previous social experiences: see Rahnema v. Canada (Solicitor General), [1993] F.C.J. No. 1431 at para. 20 (QL) (T.D.); and El-Naem v. Canada (Minister of Citizenship and Immigration), [1997] F.C.J. No. 185 (QL) (T.D.). Likewise, a lack of coherency or consistency in the claimant's testimony should be viewed in light of the claimant's psychological condition, especially where it has been medically documented: see Reyes v. Canada (Minister of Employment and Immigration), [1993] F.C.J. No. 282 (QL) (C.A.); Sanghera v. Canada (Minister of Employment and Immigration) (1994), 73 F.T.R. No. 155; and Luttra Nievas v. Canada (Minister of Citizenship and Immigration), [1998] F.C.J. No. 34 (QL) (T.D.).

[13] A person's first story is usually the most genuine and, therefore, the one to be most believed. That being said, although the failure to report a fact can be a cause for concern, it should not always be so. That, again depends on all the circumstances: see Fajardo v. Canada (Minister of Employment and Immigration), [1993] F.C.J. No. 915 at para. 5 (QL) (C.A.); Owusu-Ansah, supra; and Sheikh v. Canada (Minister of Citizenship and Immigration), [2000] F.C.J. No. 568 (QL) (T.D.). In evaluating the applicant's first encounters with Canadian immigration authorities or referring to the applicant's Port of Entry Statements, the Board should also be mindful of the fact that "most refugees have lived experiences in their country of origin which give them good reason to distrust persons in authority": see Prof. James C. Hathaway, The Law of Refugee Status, (Toronto: Butterworth, 1991) at 84-85; Attakora, supra; and Takhar,supra.

[14] Finally, the applicant's credibility and the plausibility of testimony should be assessed in the context of her country's conditions and other documentary evidence available to the Board. Minor or peripheral inconsistencies in the applicant's evidence should not lead to a finding of general lack of credibility where documentary evidence supports the plausibility of the applicant's story: see Attakora, supra; and Frimpong v. Canada (Minister of Employment and Immigration), [1989] F.C.J. No. 441 (QL) (C.A.).
APPLICATION TO THE CASE AT BAR

[15] I will now turn to the particular facts of the case under review. I am fully aware of the Board's great expertise and discretion in the appreciation of credibility. No decision-maker, however, can act arbitrarily. In light of the particular circumstances of this case, taking into account the evidence on record and considering the impugned decision as a whole, I find that the Board's general conclusion is patently unreasonable.

[16] First, I note that the Board never points to any distinct or articulable contradiction. It always describes its difficulties in ambivalent terms. It says that "the claimant was not straightforward" (page 2, last paragraph), that "she did not remember ..." (page 3, paragraph 1), that "[s]he failed to provide the date ..." (page 3, paragraph 1), that "the agent might have told her ..." (ibid), that "[s]he explained that the agent had advised her to do so. He had told her to lie, she said" (page 3, paragraph 2), that "[s]he did not know where she transited in the USA" (page 3, paragraph 3), that "the agent did all the talking" (ibid) - for which the Board "questions the plausibility of it in absence of a reasonable explanation" (ibid), that "[s]he had taken long pauses to answer certain questions. She, however, remained vague in her responses" (page 4, paragraph 1), and finally, that "[s]he was asked why there is no mention of her arrests, for example, in December 1999" [at her Port of Entry Statement] - for which the Board continues: "Her explanation that the interpreter had told her to write few words [sic] what had happened to her in India is not accepted by the panel" (page 4, paragraph 2).

[17] Second, one must not forget the applicant's background - a woman from rural India - and her psychological condition. In the case at bar, the applicant underwent a psychological evaluation in Canada, was diagnosed with post-traumatic stress disorder (PTSD) and received therapy. According to the psychological report, which was in evidence and remained uncontroverted, it caused the applicant tremendous stress to discuss her experiences relevant to the claim. E. Kornacki, M.Ed., psychotherapist, in her report, expressly recommended that care be taken when questioning her and noted that "formal questioning may trigger memories of past traumatic events involving the police". The Board, nevertheless, in the impugned decision, "noticed no problems in her manner of testifying, finding her to be alert and aware" - omitting to mention the important fact that the applicant once broke down while testifying and had to be taken to hospital. In fact, the Board decided to resume the September 6, 2001 hearing and to postpone it on medical grounds, the presiding member noting that the applicant "had to go for medical attention ... it's advisable to her in this condition not to continue. She's crying and sobbing and can't breathe properly" (transcript, certified record, at page 519).

[18] Third, a major difficulty with the impugned decision is that, except for the issue of the applicant's election card, where the Board finds that "she ... remained vague in her responses", the Board's negative credibility finding is based chiefly on matters related to the agent who brought her to Canada. In light of evidence on record, I cannot accept the position of counsel for the respondent that any of these findings, individually or cumulatively, can reasonably sustain the general conclusion reached by the Board, and in particular as follows:
(a) In view of the specific circumstances of this case, I am ready to accept that the applicant's alleged maltreatment by the police in India would have made her suspicious and afraid of any official functionaries and would have made her communication with Canadian immigration authorities inherently stressful. Therefore, it is natural to expect that the applicant would not be very clear in her recollection of making a refugee claim.
(b) Nor do I see any serious problem in the applicant's narrative of her journey to Canada. The applicant comes from rural India and had never travelled to a Western country before. It is quite common for agents who "arrange" passports for refugee claimants to accompany the claimants, hold their documents, and deal with border controls for them. That the applicant could not remember the point of transit or explain how the agent managed to escort her to her seat on the plane without being a passenger is by no means implausible in view of the applicant's psychological condition. In any event, I do not see how the applicant's inability to present a smooth and coherent travel story can serve as reasonable grounds to disbelieve her allegations of persecution in India.
(c) Likewise, the fact that the applicant travelled on a false passport and claimed at the port of entry that it was genuine can hardly support a general negative credibility finding. As Evans J. puts it in Takhar, supra, at paragraph 14, "whether a person has told the truth about his or her travel documents has little direct bearing on whether the person is indeed a refugee". Nor is this a case where the identity of the claimant has been questioned by the Board or where the absence of a valid passport has proven to be problematic, as e.g. in Elazi v. Canada (Minister of Citizenship and Immigration), (2000) 191 F.T.R. 205 at paragraph 17.
(d) With regard to the election card, I tend to accept the counsel's explanation that the contradiction in the testimony was illusory, caused by the Board's confusion of the concepts of "issuance" and "possession". More importantly, I find it difficult to understand the Board's disproportionate amount of attention to the history of that particular document. The election card was not the only document attesting to the applicant's identity. Her true identity was never questioned by the Board. Speaking in the language of Attakora, supra (at paragraph 8), the Board seems to have engaged in microscopic examination of a document that "could not have had any conceivable relevance to any issue which the Board had to decide".

[19] As we can see, the only problem that directly relates to the essence of the applicant's claim is the alleged omission of the central persecutory events in her Port of Entry Statement. The respondent's counsel submits that this ground alone may be invoked to justify the general negative credibility finding made by the Board.

[20] There is no doubt that a failure to mention the key events on which the refugee claim is based in a written statement to immigration authorities, or an inconsistency between such statement and subsequent testimony, are very serious matters that can potentially sustain a negative credibility finding. However, the omission or inconsistency must be real: see Rajaratnam v. Canada (Minister of Employment and Immigration), [1991] F.C.J. 1271 (QL) (C.A.). Besides, explanations given by the applicant which are not obviously implausible must be taken into account: see Owusu-Ansah, supra.

[21] The applicant's Port of Entry Statement, written in Punjabi, was translated into English as follows:
One day the terrorists had a meal at our house and left and for this reason the police began to harass me. The police insulted me because my brother had left the house and gone away.

[22] Although the applicant did write what possibly amounts to a somewhat undetailed description of her problems, I, nevertheless, find that her description is a reasonably accurate one. In that statement, the applicant clearly identified the agents of persecution - the police. She also identified the reasons why the police targeted her. She did not mention that she was arrested or detained, but she stated something which in her mind was undoubtedly more essential: that she was "insulted" by the police. A close reading of the impugned decision shows that the Board implicitly understood that by being "insulted" the applicant meant that the police used rude language. This is certainly not the case here. Considering the evidence on record and the Board's expert knowledge, making this unauthorized inference constituted a reviewable error.

[23] Apparently, the applicant's native culture discourages an open discussion of rape and prompts her to use euphemisms instead. This particular view is confirmed by the documentary evidence which was before the Board and which seems to have been completely overlooked in the impugned decision. At the port of entry, the applicant wrote that she had been "insulted." In her PIF narrative, she stated that the drunken police inspector had "used" her "for his lust." At one point in her oral testimony, the applicant stated she had been "humiliated" by the police. In my view, the use of these expressions tends to indicate the authenticity of the applicant's story, rather than to undermine her credibility. It should not be forgotten that "there are police custodial rapes" and that "[t]here exists a silence that shrouds sexual violence in a society that places a lot of stress on female virtue and chastity ... Indeed, the sorrow, bewilderment, anger and trauma of the victim is aggravated by a sense of shame and self-contempt, which could even lead to attempts at suicide and self-destruction": see Shame, Arndhika Sekhon, The Tribune, March 13, 1999, certified record, at page 291.

[24] When asked at the hearing about her failure to mention her arrest in the Port of Entry Statement, the applicant replied that the amount of space allocated to that question in the form, as well as the interpreter's instructions, prompted her to make her statement brief. I find her explanation totally reasonable in the particular circumstances of this case. In Lives Under Threat: A Study of Sikhs Coming to the UK from the Punjab (certified record, at page 213), it is noted as follows:
There are many reasons why

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 14515:2 · paragraphs 28-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `113315a4b5e714ff734c1f218393ec689a4bc4404c3327aa72579922ee8c9f5d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 14515:2:subtheme:1 · paragraphs 28-28

- Raw key terms: `appearances, applicant, attorney, bernardfor, bertrand, bertrandfor, canada, christine`
- Display key terms: `bernardfor, bertrand, bertrandfor, christine`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: bernardfor, bertrand, bertrandfor, christine No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 28-28. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER THE HONOURABLE MR. JUSTICE
AND ORDER: MARTINEAU
DATED: February 3, 2003
APPEARANCES:
Mr. Jean-François Bertrand FOR THE APPLICANT
Ms. Christine BernardFOR THE RESPONDENT
SOLICITORS ON THE RECORD:
Mr. Jean-François BertrandFOR THE APPLICANT
Montreal, Quebec
Mr. Morris RosenbergFOR THE RESPONDENT
Deputy Attorney General Of Canada
