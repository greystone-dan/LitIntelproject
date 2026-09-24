# Discussion Units: case 19540

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **84**
- Continuity pairs: **83**
- Discussion Units: **4**
- Paragraph source hashes: **84**
- Sub-themes: **21**

## 19540:1 · paragraphs 0-63

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `86e6831675e2907a2ddff0bcf0a525a5bcd8874211a8f5075df91c73d85219d5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 19540:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `court, decision, immigration, mercado, angel, applicants, asking, baptista`
- Display key terms: `mercado, angel, asking, baptista`
- Argument roles: `governing_rule`
- Explanation: Observed roles: governing_rule Display terms: mercado, angel, asking, baptista Rule/authority context: Mercado is asking the Court to review the decision by the Refugee Protection Division of the Immigration and Refugee Board (RPD) dismissing his refugee claim and that of his family members under sections 96 and 97 of the Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4926154` offsets `197-202`; context: Mercado is asking the Court to review the decision by the Refugee Protection Division of the Immigration and Refugee Board (RPD) dismissing his refugee claim and that of his family members under sections 96 and 97 of the Immigration and Refugee Protection Act, S.

#### 19540:1:subtheme:2 · paragraphs 2-6

- Raw key terms: `mercado, venezuela, despite, family, states, united, american, applicant`
- Display key terms: `mercado, venezuela, despite, family, states, united, american`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, party_position Display terms: mercado, venezuela, despite, family, states, united, american Position/evidence statements: He claimed that he consulted a lawyer about his problems in September 2007; the lawyer advised him to leave Venezuela. Rule/authority context: [2] Inter alia, the applicant alleges a variety of circumstances—the failure to send the initial screening form, the existence of a document of unknown origin in counsel’s file indicating that the date of issuance of his Operative outcome context: For the following reasons, the Court cannot concur with this approach and, despite the vigorous efforts of his counsel, the application is dismissed. Evidence spans paragraphs 2-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4926155` offsets `719-725`; context: Background and issues
- Evidence: `governing_rule` cue `principles` at chunk `4926155` offsets `438-448`; context: [2] Inter alia, the applicant alleges a variety of circumstances—the failure to send the initial screening form, the existence of a document of unknown origin in counsel’s file indicating that the date of issuance of his American driver’s licence cast doubt on the credibility of his story, the uncertainty about the place and date of the RPD hearing—that were not raised before the RPD, to support his argument that the RPD breached the principles of fundamental justice and to obtain another chance to establish the merits of his claim before the RPD.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4926155` offsets `591-597`; context: For the following reasons, the Court cannot concur with this approach and, despite the vigorous efforts of his counsel, the application is dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `4926155` offsets `693-702`; context: For the following reasons, the Court cannot concur with this approach and, despite the vigorous efforts of his counsel, the application is dismissed.
- Evidence: `party_position` cue `claimed` at chunk `4926159` offsets `71-78`; context: He claimed that he consulted a lawyer about his problems in September 2007; the lawyer advised him to leave Venezuela.

#### 19540:1:subtheme:3 · paragraphs 7-9

- Raw key terms: `applicant, copy, documents, family, file, filed, identity, immigration`
- Display key terms: `copy, documents, family, file, filed, identity`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: copy, documents, family, file, filed, identity Application context: He also said that he attempted to file a police report about his assailants but that the police clearly indicated that a complaint would be futile because they were members of the secret police. Evidence spans paragraphs 7-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4926160` offsets `379-386`; context: He also said that he attempted to file a police report about his assailants but that the police clearly indicated that a complaint would be futile because they were members of the secret police.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926161` offsets `26-34`; context: [8] Before discussing the evidence that was before the RPD, it is worth noting that the applicant and his spouse did not have their passports.

#### 19540:1:subtheme:4 · paragraphs 10-12

- Raw key terms: `applicant, hearing, place, calgary, card, copy, counsel, documentary`
- Display key terms: `hearing, place, calgary, card, copy, documentary`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: hearing, place, calgary, card, copy, documentary Position/evidence statements: [11] It should also be noted here that the applicant argues that there was much uncertainty about the place and date of the RPD hearing. Evidence spans paragraphs 10-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4926163` offsets `231-238`; context: [7] Later, when the applicant was questioned as to whether he had documentary evidence confirming that he had, in fact, worked at the ministry during the period indicated, his counsel filed a copy of a work identity card that the applicant had sent by fax the day before.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926163` offsets `258-266`; context: [7] Later, when the applicant was questioned as to whether he had documentary evidence confirming that he had, in fact, worked at the ministry during the period indicated, his counsel filed a copy of a work identity card that the applicant had sent by fax the day before.
- Evidence: `party_position` cue `argues` at chunk `4926164` offsets `53-59`; context: [11] It should also be noted here that the applicant argues that there was much uncertainty about the place and date of the RPD hearing.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926164` offsets `400-408`; context: He also maintains that this uncertainty was a factor that should have been considered when he requested more time to provide documentary evidence after the hearing; this request for more time will be discussed in the second part of these reasons.
- Evidence: `evidence_fact` cue `record` at chunk `4926165` offsets `30-36`; context: [12] It is true that, in this record, the applicant received three notices of hearing.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4926165` offsets `423-431`; context: Although this does not appear in the record, it is clear that counsel for the applicants contacted the RPD to advise them that the applicant and his family could not afford to travel to Montréal.

#### 19540:1:subtheme:5 · paragraphs 13-15

- Raw key terms: `mercado, because, claim, decision, evidence, hearing, issued, venezuela`
- Display key terms: `mercado, because, hearing, issued, venezuela`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: mercado, because, hearing, issued, venezuela Application context: Mercado testified that he did not have the original of this document in Calgary because it was in Venezuela. | Mercado’s claim was dismissed because the RPD found that the applicant was not credible. Operative outcome context: Mercado’s claim was dismissed because the RPD found that the applicant was not credible. Evidence spans paragraphs 13-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4926166` offsets `15-20`; context: [13] As to the issue of a better copy of the work card, the Court notes that Mr.
- Evidence: `reasoning_application` cue `because` at chunk `4926166` offsets `161-168`; context: Mercado testified that he did not have the original of this document in Calgary because it was in Venezuela.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926167` offsets `87-95`; context: Mercado asked for more time to provide additional documentary evidence to support his claim, but the request was refused.
- Evidence: `counterargument_limitation` cue `but` at chunk `4926167` offsets `118-121`; context: Mercado asked for more time to provide additional documentary evidence to support his claim, but the request was refused.
- Evidence: `evidence_fact` cue `found that` at chunk `4926168` offsets `68-78`; context: Mercado’s claim was dismissed because the RPD found that the applicant was not credible.
- Evidence: `reasoning_application` cue `because` at chunk `4926168` offsets `52-59`; context: Mercado’s claim was dismissed because the RPD found that the applicant was not credible.
- Evidence: `counterargument_limitation` cue `but` at chunk `4926168` offsets `477-480`; context: In its decision, the RPD also noted that the driver’s licence was issued by the state of Georgia on January 8 but the applicant stated that he was in Venezuela on that date.
- Evidence: `disposition` cue `dismissed` at chunk `4926168` offsets `42-51`; context: Mercado’s claim was dismissed because the RPD found that the applicant was not credible.

#### 19540:1:subtheme:6 · paragraphs 16-20

- Raw key terms: `applicant, hearing, alleges, court, decision, file, paragraph, story`
- Display key terms: `hearing, alleges, file, paragraph, story`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: hearing, alleges, file, paragraph, story Position/evidence statements: First, he alleges that the RPD erred when it wrote at paragraph 12 of the decision: “the Claimant did not submit any document confirming his presence in his country. | [18] He also submits that the RPD breached the principles of natural justice by refusing to grant him more time after the hearing to permit him to file his income tax return or something from [translation] “someone who c Rule/authority context: [18] He also submits that the RPD breached the principles of natural justice by refusing to grant him more time after the hearing to permit him to file his income tax return or something from [translation] “someone who c Application context: Accordingly, there is no need to discuss this issue further in these reasons. | He also alleges that he was judged more severely when he asked for more time to file evidence because he was represented by experienced counsel. Evidence spans paragraphs 16-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4926169` offsets `394-399`; context: Accordingly, there is no need to discuss this issue further in these reasons.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4926169` offsets `348-359`; context: Accordingly, there is no need to discuss this issue further in these reasons.
- Evidence: `party_position` cue `submit` at chunk `4926170` offsets `197-203`; context: First, he alleges that the RPD erred when it wrote at paragraph 12 of the decision: “the Claimant did not submit any document confirming his presence in his country.
- Evidence: `counterargument_limitation` cue `However` at chunk `4926170` offsets `263-270`; context: However, he had no document showing that he worked for the Ministry of the Interior, such as a tax document, registration with the municipality, a pay stub from his employer or any other document.
- Evidence: `party_position` cue `submits` at chunk `4926171` offsets `13-20`; context: [18] He also submits that the RPD breached the principles of natural justice by refusing to grant him more time after the hearing to permit him to file his income tax return or something from [translation] “someone who could place him at his workplace.
- Evidence: `governing_rule` cue `principles` at chunk `4926171` offsets `47-57`; context: [18] He also submits that the RPD breached the principles of natural justice by refusing to grant him more time after the hearing to permit him to file his income tax return or something from [translation] “someone who could place him at his workplace.
- Evidence: `party_position` cue `submits` at chunk `4926172` offsets `19-26`; context: [19] The applicant submits that the RPD imposed too heavy a burden by requiring him to file official proof.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926172` offsets `193-201`; context: He also alleges that he was judged more severely when he asked for more time to file evidence because he was represented by experienced counsel.
- Evidence: `reasoning_application` cue `because` at chunk `4926172` offsets `202-209`; context: He also alleges that he was judged more severely when he asked for more time to file evidence because he was represented by experienced counsel.
- Evidence: `party_position` cue `argues` at chunk `4926173` offsets `101-107`; context: [20] Finally, referring to an unsigned, undated note whose origin remains nebulous,[9] the applicant argues that he should have been informed at or before the hearing that the Refugee Protection Officer (RPO) and the RPD doubted his story and the [translation] “medical report” filed, given the clear contradiction between the date his driver’s licence was issued and his story that he was in Venezuela in January 2007.

#### 19540:1:subtheme:7 · paragraphs 21-31

- Raw key terms: `applicant, court, evidence, hearing, panel, paragraph, canada, counsel`
- Display key terms: `hearing, paragraph`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: hearing, paragraph Position/evidence statements: [21] Counsel for the applicant submits that this is especially serious considering that the applicant did not receive the screening form that is in the certified record, which states that, as of January 13, 2009, the iss | [22] It is settled law that the reasonableness standard of review applies to the assessment of a refugee claimant’s credibility and the evidentiary weight of the documentation submitted by the claimant: Dunsmuir v. Rule/authority context: [22] It is settled law that the reasonableness standard of review applies to the assessment of a refugee claimant’s credibility and the evidentiary weight of the documentation submitted by the claimant: Dunsmuir v. Application context: [22] It is settled law that the reasonableness standard of review applies to the assessment of a refugee claimant’s credibility and the evidentiary weight of the documentation submitted by the claimant: Dunsmuir v. | In addition to specific questions and comments during the hearing about these documents, a simple review of this nine‑page decision is sufficient to conclude that the RPD examined this evidence properly. Operative outcome context: The Court allowed the parties to file supplementary representations after the hearing on this issue. Evidence spans paragraphs 21-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4926174` offsets `217-223`; context: [21] Counsel for the applicant submits that this is especially serious considering that the applicant did not receive the screening form that is in the certified record, which states that, as of January 13, 2009, the issues included his credibility.
- Evidence: `party_position` cue `submits` at chunk `4926174` offsets `31-38`; context: [21] Counsel for the applicant submits that this is especially serious considering that the applicant did not receive the screening form that is in the certified record, which states that, as of January 13, 2009, the issues included his credibility.
- Evidence: `evidence_fact` cue `record` at chunk `4926174` offsets `162-168`; context: [21] Counsel for the applicant submits that this is especially serious considering that the applicant did not receive the screening form that is in the certified record, which states that, as of January 13, 2009, the issues included his credibility.
- Evidence: `disposition` cue `allowed` at chunk `4926174` offsets `260-267`; context: The Court allowed the parties to file supplementary representations after the hearing on this issue.
- Evidence: `party_position` cue `submitted` at chunk `4926175` offsets `176-185`; context: [22] It is settled law that the reasonableness standard of review applies to the assessment of a refugee claimant’s credibility and the evidentiary weight of the documentation submitted by the claimant: Dunsmuir v.
- Evidence: `governing_rule` cue `standard of review` at chunk `4926175` offsets `47-65`; context: [22] It is settled law that the reasonableness standard of review applies to the assessment of a refugee claimant’s credibility and the evidentiary weight of the documentation submitted by the claimant: Dunsmuir v.
- Evidence: `reasoning_application` cue `applies` at chunk `4926175` offsets `66-73`; context: [22] It is settled law that the reasonableness standard of review applies to the assessment of a refugee claimant’s credibility and the evidentiary weight of the documentation submitted by the claimant: Dunsmuir v.
- Evidence: `party_position` cue `submitted` at chunk `4926177` offsets `147-156`; context: [24] The Court cannot accept the applicant’s position that paragraph 12 of the decision indicates that the panel did not consider the documents he submitted.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926177` offsets `343-351`; context: In addition to specific questions and comments during the hearing about these documents, a simple review of this nine‑page decision is sufficient to conclude that the RPD examined this evidence properly.
- Evidence: `reasoning_application` cue `conclude` at chunk `4926177` offsets `307-315`; context: In addition to specific questions and comments during the hearing about these documents, a simple review of this nine‑page decision is sufficient to conclude that the RPD examined this evidence properly.
- Evidence: `party_position` cue `assert` at chunk `4926178` offsets `464-470`; context: In the Court’s view, the panel’s reasoning with respect to the evidence before it was sufficiently developed to enable the principal applicant to assert his rights on a judicial review: Via Rail Canada Inc.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926178` offsets `381-389`; context: In the Court’s view, the panel’s reasoning with respect to the evidence before it was sufficiently developed to enable the principal applicant to assert his rights on a judicial review: Via Rail Canada Inc.
- Evidence: `counterargument_limitation` cue `However` at chunk `4926178` offsets `142-149`; context: However, paragraph 12 of the decision must be read in its context, and, having done so, the Court is satisfied that the ambiguity results solely from a literal interpretation.
- Evidence: `party_position` cue `submit` at chunk `4926180` offsets `68-74`; context: [27] First, contrary to the applicable rules, the applicant did not submit the original of his work identity card and provided no explanation for failing to do so.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926180` offsets `348-356`; context: It should also be noted that counsel for the applicant only decided to submit this copy of poor quality near the end of the hearing when the panel commented on the lack of documentary evidence to establish that the applicant, in fact, had worked for the Ministry of the Interior.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926181` offsets `416-424`; context: At that point, the applicant should have had in hand all the documents in support of his claim, which necessarily includes the available documentary evidence to establish that he was indeed in Venezuela during the relevant period (March 2006 to October 1, 2007) and that he was working there.
- Evidence: `reasoning_application` cue `because` at chunk `4926181` offsets `81-88`; context: [28] The Court cannot accept that the applicant did not have the time to prepare because he did not know where or when his hearing would take place or that he did not know he could request the original.
- Evidence: `evidence_fact` cue `testimony` at chunk `4926182` offsets `260-269`; context: That document does not corroborate the applicant’s testimony on a key element of the story, i.

#### 19540:1:subtheme:8 · paragraphs 32-33

- Raw key terms: `paragraph, able, affirm, another, applicant, applicant's, assessment, board`
- Display key terms: `paragraph, able, affirm, another, applicant's, assessment`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: paragraph, able, affirm, another, applicant's, assessment Rule/authority context: [32] The jurisprudence is clear that failing to file supporting documentation that it is reasonable to expect may have an impact on an applicant’s credibility: A. Evidence spans paragraphs 32-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4926185` offsets `878-886`; context: ) (QL) at paragraph 20:
Once a Board, as the present Board did, comes to the conclusion that an applicant is not credible, in most cases, it will necessarily follow that the Board will not give that applicant's documents much probative value, unless the applicant has been able to prove satisfactorily that the documents in question are truly genuine.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4926185` offsets `9-22`; context: [32] The jurisprudence is clear that failing to file supporting documentation that it is reasonable to expect may have an impact on an applicant’s credibility: A.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926186` offsets `83-91`; context: [33] In the circumstances, the RPD’s assessment of the testimonial and documentary evidence[11] is within the parameters of reasonability and is “defensible in respect of the facts and law”: Dunsmuir at paragraph 47.

#### 19540:1:subtheme:9 · paragraphs 34-36

- Raw key terms: `applicant, effort, failure, hearing, lack, probative, rules, value`
- Display key terms: `effort, failure, hearing, lack, probative, rules, value`
- Argument roles: `disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue Display terms: effort, failure, hearing, lack, probative, rules, value Rule/authority context: [34] I must now determine whether the RPD breached the principles of procedural fairness. | [35] Under Rules 29 and 36,[12] the applicant was required to file a copy of the documents in support of his claim 20 days before the hearing and provide the original of the documents no later than the day of the hearing Operative outcome context: [36] The RPD denied the applicant’s oral request at the hearing. Evidence spans paragraphs 34-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4926187` offsets `26-33`; context: [34] I must now determine whether the RPD breached the principles of procedural fairness.
- Evidence: `governing_rule` cue `principles` at chunk `4926187` offsets `55-65`; context: [34] I must now determine whether the RPD breached the principles of procedural fairness.
- Evidence: `issue` cue `whether` at chunk `4926188` offsets `667-674`; context: The factors that the RPD must consider in exercising this discretion are the same in both Rules: (a) the relevance and probative value of the document, (b) any new evidence it brings to the proceedings, and (c) whether the party, with reasonable effort, could have complied with the deadlines in Rule 29.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926188` offsets `422-430`; context: Rules 30 and 37 give discretion to the RPD to admit new evidence at or after the hearing.
- Evidence: `governing_rule` cue `Under` at chunk `4926188` offsets `5-10`; context: [35] Under Rules 29 and 36,[12] the applicant was required to file a copy of the documents in support of his claim 20 days before the hearing and provide the original of the documents no later than the day of the hearing.
- Evidence: `disposition` cue `denied` at chunk `4926189` offsets `13-19`; context: [36] The RPD denied the applicant’s oral request at the hearing.

#### 19540:1:subtheme:10 · paragraphs 37-38

- Raw key terms: `applicant, considered, counsel, document, fact, income, official, panel`
- Display key terms: `considered, document, fact, income, official`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: considered, document, fact, income, official Rule/authority context: In accordance with the principle articulated in the jurisprudence cited above at paragraph 32, it was open to the panel to find that filing an unofficial document would not have mitigated the problem of the applicant’s c Application context: [37] After meticulously reviewing the transcript and the reasons, the Court is satisfied that the panel properly applied the test set out in the Rules. | Contrary to the applicant’s argument, the RPD did not impose a heavier burden on him simply because he was represented by this counsel. Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4926190` offsets `238-245`; context: It specifically asked the applicant why he had not provided his income tax return and whether in fact it was available.
- Evidence: `reasoning_application` cue `applied` at chunk `4926190` offsets `113-120`; context: [37] After meticulously reviewing the transcript and the reasons, the Court is satisfied that the panel properly applied the test set out in the Rules.
- Evidence: `issue` cue `question` at chunk `4926191` offsets `1018-1026`; context: In accordance with the principle articulated in the jurisprudence cited above at paragraph 32, it was open to the panel to find that filing an unofficial document would not have mitigated the problem of the applicant’s credibility, considering the fact that the applicant’s credibility was already in question.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926191` offsets `698-706`; context: It is clear from the panel’s comments that it considered the probative value (lack of official stamp) of this document if it had been adduced as part of the evidence it heard.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4926191` offsets `769-782`; context: In accordance with the principle articulated in the jurisprudence cited above at paragraph 32, it was open to the panel to find that filing an unofficial document would not have mitigated the problem of the applicant’s credibility, considering the fact that the applicant’s credibility was already in question.
- Evidence: `reasoning_application` cue `because` at chunk `4926191` offsets `232-239`; context: Contrary to the applicant’s argument, the RPD did not impose a heavier burden on him simply because he was represented by this counsel.

#### 19540:1:subtheme:11 · paragraphs 39-42

- Raw key terms: `applicant, venezuela, because, court, documents, obtain, access, account`
- Display key terms: `venezuela, because, documents, obtain, access, account`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: venezuela, because, documents, obtain, access, account Application context: [40] Similarly, the RPD also considered that the applicant had more than two years to obtain this documentation and that it should have been easy to access because the principal applicant seemed to indicate that the tax  | [41] The applicant noted that the RPD should have taken into account that a refugee claimant is often without resources and that, in this case, it was difficult for him to obtain evidence from his employer because it was Evidence spans paragraphs 39-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4926192` offsets `96-103`; context: [39] There is no doubt that the presence of counsel on a file is a relevant factor in assessing whether the applicant should have known that he had to file documents to prove that he was in Venezuela and that he worked for the Ministry of the Interior.
- Evidence: `reasoning_application` cue `because` at chunk `4926193` offsets `156-163`; context: [40] Similarly, the RPD also considered that the applicant had more than two years to obtain this documentation and that it should have been easy to access because the principal applicant seemed to indicate that the tax return was in his father’s possession in Venezuela.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926194` offsets `179-187`; context: [41] The applicant noted that the RPD should have taken into account that a refugee claimant is often without resources and that, in this case, it was difficult for him to obtain evidence from his employer because it was at the very heart of his fear of persecution.
- Evidence: `reasoning_application` cue `because` at chunk `4926194` offsets `206-213`; context: [41] The applicant noted that the RPD should have taken into account that a refugee claimant is often without resources and that, in this case, it was difficult for him to obtain evidence from his employer because it was at the very heart of his fear of persecution.

#### 19540:1:subtheme:12 · paragraphs 43-45

- Raw key terms: `applicant, court, evidence, last, mercado, question, absence, additional`
- Display key terms: `last, mercado, question, absence, additional`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: last, mercado, question, absence, additional Application context: [43] Before addressing the last question or the second aspect of this issue of breaching the rules of procedural fairness, the Court would like to mention that it is not discussing the driver’s licence in this analysis o | [45] Can the Court consider the new factors (absence of screening form and the so‑called [translation] “compromising evidence”) relied on by the applicant to conclude that there was a denial of justice? Evidence spans paragraphs 43-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4926196` offsets `32-40`; context: [43] Before addressing the last question or the second aspect of this issue of breaching the rules of procedural fairness, the Court would like to mention that it is not discussing the driver’s licence in this analysis of the request for additional time that was made at the RPD hearing because it has nothing to do with the issue of obtaining the driver’s licence.
- Evidence: `evidence_fact` cue `testimony` at chunk `4926196` offsets `466-475`; context: Mercado if he had any documents to support his testimony that he obtained this renewal on the Internet, the applicant did not suggest any additional evidence on this point.
- Evidence: `reasoning_application` cue `because` at chunk `4926196` offsets `287-294`; context: [43] Before addressing the last question or the second aspect of this issue of breaching the rules of procedural fairness, the Court would like to mention that it is not discussing the driver’s licence in this analysis of the request for additional time that was made at the RPD hearing because it has nothing to do with the issue of obtaining the driver’s licence.
- Evidence: `issue` cue `question` at chunk `4926197` offsets `32-40`; context: [44] This brings us to the last question which, Mr.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4926197` offsets `116-125`; context: Mercado says, is an essential question (see paragraph 15 of his affidavit).
- Evidence: `evidence_fact` cue `evidence` at chunk `4926198` offsets `117-125`; context: [45] Can the Court consider the new factors (absence of screening form and the so‑called [translation] “compromising evidence”) relied on by the applicant to conclude that there was a denial of justice?
- Evidence: `reasoning_application` cue `conclude` at chunk `4926198` offsets `158-166`; context: [45] Can the Court consider the new factors (absence of screening form and the so‑called [translation] “compromising evidence”) relied on by the applicant to conclude that there was a denial of justice?

#### 19540:1:subtheme:13 · paragraphs 46-47

- Raw key terms: `form, impact, manner, screening, timely, affirmed, applicant, because`
- Display key terms: `form, impact, manner, screening, timely, affirmed, because`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: form, impact, manner, screening, timely, affirmed, because Application context: [47] In this case, the failure to object in a timely manner is of little consequence because, as I indicate below, the screening form did not contain any information that could have had an impact. Evidence spans paragraphs 46-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4926199` offsets `336-341`; context: For the system to function, it is essential that counsel review their files before the hearing and raise with the RPD in a timely manner any issue that could have an impact on their client’s right to a fair hearing: Benitez v.
- Evidence: `reasoning_application` cue `because` at chunk `4926200` offsets `85-92`; context: [47] In this case, the failure to object in a timely manner is of little consequence because, as I indicate below, the screening form did not contain any information that could have had an impact.

#### 19540:1:subtheme:14 · paragraphs 48-49

- Raw key terms: `applicant, form, accept, according, accordingly, addition, addressed, application`
- Display key terms: `form, accept, according, accordingly, addition, addressed`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: form, accept, according, accordingly, addition, addressed Application context: Accordingly, the RPD was unable, on the initial review, to determine whether the reliability of the documents would be an important element at the hearing. | According to the applicant, this was not sufficient because the “consistency” box should also have been checked. Evidence spans paragraphs 48-49. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4926201` offsets `386-393`; context: Accordingly, the RPD was unable, on the initial review, to determine whether the reliability of the documents would be an important element at the hearing.
- Evidence: `evidence_fact` cue `record` at chunk `4926201` offsets `41-47`; context: [48] The screening form in the certified record is dated January 13, 2009.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4926201` offsets `317-328`; context: Accordingly, the RPD was unable, on the initial review, to determine whether the reliability of the documents would be an important element at the hearing.
- Evidence: `issue` cue `issues` at chunk `4926202` offsets `70-76`; context: [49] In addition, various boxes are checked off on this form as being issues, including the “credibility” box.
- Evidence: `evidence_fact` cue `determined that` at chunk `4926202` offsets `374-389`; context: 124 (QL), the Court determined that where the main box is checked but none of the subordinate boxes are checked, the applicant should know that all parts of the category should be addressed in his or her application.
- Evidence: `reasoning_application` cue `because` at chunk `4926202` offsets `163-170`; context: According to the applicant, this was not sufficient because the “consistency” box should also have been checked.

#### 19540:1:subtheme:15 · paragraphs 50-51

- Raw key terms: `issue, able, additional, alia, always, applicant, argument, aside`
- Display key terms: `able, additional, alia, always, argument, aside`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: able, additional, alia, always, argument, aside Evidence spans paragraphs 50-51. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4926203` offsets `64-69`; context: [50] In any event, it is clear that credibility is always a key issue in refugee claims (see, inter alia, Talukder v.
- Evidence: `issue` cue `issue` at chunk `4926204` offsets `24-29`; context: [51] The only remaining issue to be determined is the impact of the unsigned, undated note that is in the applicant’s file and not in the certified record.
- Evidence: `evidence_fact` cue `record` at chunk `4926204` offsets `148-154`; context: [51] The only remaining issue to be determined is the impact of the unsigned, undated note that is in the applicant’s file and not in the certified record.

#### 19540:1:subtheme:16 · paragraphs 52-56

- Raw key terms: `applicant, fact, although, anyone, argument, because, cannot, counsel`
- Display key terms: `fact, although, anyone, argument, because, cannot`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: fact, although, anyone, argument, because, cannot Rule/authority context: [56] The applicant did not provide any jurisprudence supporting his position that he should have been advised of the contents of this note. Application context: [53] Although it appears from the five memoranda filed by the parties that the applicant attributes this note to the RPO and that his counsel obtained it prior to the hearing, the Court cannot accept the theory that the  | [55] In fact, since these comments are simple and quite factual, anyone reading the record before the hearing (because the lawyer’s letter does not contain any reference) could have written it. Evidence spans paragraphs 52-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4926205` offsets `34-41`; context: [52] It is difficult to determine whether this argument should have been raised before the RPD given that the Court cannot, in fact, determine exactly when this document was prepared, by whom and when counsel for the applicant obtained it.
- Evidence: `reasoning_application` cue `because` at chunk `4926206` offsets `264-271`; context: [53] Although it appears from the five memoranda filed by the parties that the applicant attributes this note to the RPO and that his counsel obtained it prior to the hearing, the Court cannot accept the theory that the note was among the documents sent on July 7 because, at that time, the medical report had not yet been filed.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926207` offsets `74-82`; context: [54] The parties agree that the following is the relevant passage:[15]
No evidence that the claimant went to his country in 2005 and stayed until July 2007 with the exception of the very succinct medical report that could have been written by anyone and that is dated June 2006 whereas nothing happened to the applicant before July 2006.
- Evidence: `evidence_fact` cue `record` at chunk `4926208` offsets `84-90`; context: [55] In fact, since these comments are simple and quite factual, anyone reading the record before the hearing (because the lawyer’s letter does not contain any reference) could have written it.
- Evidence: `reasoning_application` cue `because` at chunk `4926208` offsets `111-118`; context: [55] In fact, since these comments are simple and quite factual, anyone reading the record before the hearing (because the lawyer’s letter does not contain any reference) could have written it.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4926209` offsets `39-52`; context: [56] The applicant did not provide any jurisprudence supporting his position that he should have been advised of the contents of this note.

#### 19540:1:subtheme:17 · paragraphs 57-63

- Raw key terms: `applicant, document, hearing, information, knowledge, licence, opinion, rule`
- Display key terms: `document, hearing, information, knowledge, licence, opinion, rule`
- Argument roles: `counterargument_limitation, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, party_position, reasoning_application Display terms: document, hearing, information, knowledge, licence, opinion, rule Position/evidence statements: [58] It is certainly clear that the applicant cannot argue that the RPD did not inform him at the hearing about its concerns, which included those described above in the note at paragraph 54. Application context: [57] In his first memorandum, the applicant referred to Rule 18 which, he says, applies in this case. | By invoking this new argument, he cannot now attempt after the fact to apply Rule 18 to the RPD’s rejection of his explanation. Evidence spans paragraphs 57-63. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926210` offsets `358-366`; context: This rule states that, before using any information or opinion that is within its specialized knowledge, the Division must notify claimants and give them a chance to make representations on the reliability and use of the information or opinion and to give evidence in support of their representations.
- Evidence: `reasoning_application` cue `applies` at chunk `4926210` offsets `80-87`; context: [57] In his first memorandum, the applicant referred to Rule 18 which, he says, applies in this case.
- Evidence: `party_position` cue `argue` at chunk `4926211` offsets `53-58`; context: [58] It is certainly clear that the applicant cannot argue that the RPD did not inform him at the hearing about its concerns, which included those described above in the note at paragraph 54.
- Evidence: `evidence_fact` cue `record` at chunk `4926212` offsets `203-209`; context: Moreover, the authenticity of the driver’s licence, the only official document in the record, was not challenged.
- Evidence: `counterargument_limitation` cue `although` at chunk `4926215` offsets `438-446`; context: In this regard, the Court notes that, strangely, when questioned about the available documentation to confirm his identity at the beginning of the hearing, he referred to his American licence and described it as expired[17] although it is valid until 2017.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926216` offsets `81-89`; context: [63] As I said earlier, the applicant did not ask for additional time to provide evidence that he had obtained his licence on the Internet.
- Evidence: `reasoning_application` cue `apply` at chunk `4926216` offsets `211-216`; context: By invoking this new argument, he cannot now attempt after the fact to apply Rule 18 to the RPD’s rejection of his explanation.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4926216` offsets `174-180`; context: By invoking this new argument, he cannot now attempt after the fact to apply Rule 18 to the RPD’s rejection of his explanation.

#### Section text

Mercado v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2010-03-12
Neutral citation
2010 FC 289
File numbers
IMM-4493-09
Decision Content
Date: 20100312
Docket: IMM-4493-09
Citation: 2010 FC 289
Ottawa, Ontario, March 12, 2010
PRESENT: Madam Justice Johanne Gauthier
BETWEEN:
WILFREDO JOSE MERCADO,
YADIRA BAPTISTA,
WILLIE JOSE MERCADO,
YANIRA MERCADO
and JESUS ANGEL MERCADO BAPTISTA
Applicants
and
MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR ORDER AND ORDER

[1] Mr. Mercado is asking the Court to review the decision by the Refugee Protection Division of the Immigration and Refugee Board (RPD) dismissing his refugee claim and that of his family members under sections 96 and 97 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (the Act).

[2] Inter alia, the applicant alleges a variety of circumstances—the failure to send the initial screening form, the existence of a document of unknown origin in counsel’s file indicating that the date of issuance of his American driver’s licence cast doubt on the credibility of his story, the uncertainty about the place and date of the RPD hearing—that were not raised before the RPD, to support his argument that the RPD breached the principles of fundamental justice and to obtain another chance to establish the merits of his claim before the RPD. For the following reasons, the Court cannot concur with this approach and, despite the vigorous efforts of his counsel, the application is dismissed.
Background and issues

[3] Mr. Mercado, a citizen of Venezuela, arrived in Canada with his family on October 18, 2007, and claimed refugee status three days later. His spouse Yadira Baptista and their oldest son Jesus Angel Mercado Baptista are also Venezuelan citizens while their two other children, Willie Jose Mercado and Yanira Mercado, are American citizens. Ms. Mercado’s claim and that of the children were based entirely on Mr. Mercado’s claim; he says he fears the secret police in his country and his former employer, the Ministry of the Interior.[1]

[4] In his Personal Information Form (PIF), Mr. Mercado stated that, after spending a number of years in the United States,[2] he returned to Venezuela in March 2005 but his family remained in the United States. He then obtained a position as a computer maintenance technician in certain state offices. In the course of his work, he said he discovered blacklists[3] of the Circulos Bolivarianos [Bolivarian Circles] that named members of his family (including his brother) and some close friends. The government authorities knew that he had told his relatives about the situation and ordered an investigation.

[5] In his PIF, Mr. Mercado described the persecution he suffered as follows:
[TRANSLATION] 6. In July 2006, I was subjected to all types of threats [sic] persecution, even psychological and physical torture.
7. In the same month of July and during the following months, I was subjected to verbal threats and abuse at my workplace.
8. Persecution by certain elements of the Circulos Bolivarianos consisted of continual monitoring; [sic] my daily activities, including my private activities.
9. Death threats against me and against my family both in Venezuela and the United States by elements of the Circulos Bolovarianos [sic] consisted in persecution and the physical disappearance of my children and my spouse who, despite being alone in the United States. . . . [[4]]
[Footnote added.]

[6] Despite this, the applicant continued to work for the ministry. He claimed that he consulted a lawyer about his problems in September 2007; the lawyer advised him to leave Venezuela. Mr. Mercado states that he left Venezuela on October 1, 2007, for Colombia, and from there he went to Mexico, then to the United States on October 10, 2007. He stayed there for eight days.

[7] At the hearing, the applicant stated that his problems began in early June 2006.[5] He testified that he was beaten and required a visit to the hospital around the [translation] “20th or so”,[6] then specifically June 21, 2006. He also said that he attempted to file a police report about his assailants but that the police clearly indicated that a complaint would be futile because they were members of the secret police. He added that, before he left Venezuela, his brother was also attacked.

[8] Before discussing the evidence that was before the RPD, it is worth noting that the applicant and his spouse did not have their passports. Mr. Mercado, whose passport could have established the date he entered Venezuela, was forced to give his to his smuggler, and Ms. Mercado lost hers when her purse was stolen. Only their oldest son had a Venezuelan passport issued in 2007; a copy of it was included in the immigration documents. The four other family members filed their birth certificates. Ms. Mercado also filed her official identity card.

[9] On or about July 7, the RPD officer filed with the RPD a copy of the applicants’ immigration file containing an American driver’s licence in Mr. Mercado’s name dated January 8, 2007 (valid until 2017). A little later, on August 4, the principal applicant filed a photocopy of a medical report dated June 21, 2006, along with his PIF and the family’s identity documents.

[10] At the beginning of the hearing that took place in Montréal and by videoconference in Calgary, counsel for the applicant filed a letter from a lawyer dated September 27, 2007.[7] Later, when the applicant was questioned as to whether he had documentary evidence confirming that he had, in fact, worked at the ministry during the period indicated, his counsel filed a copy of a work identity card that the applicant had sent by fax the day before.

[11] It should also be noted here that the applicant argues that there was much uncertainty about the place and date of the RPD hearing. According to him, this explains in part his lack of preparation and why he was unable to file a better copy of his work card. He also maintains that this uncertainty was a factor that should have been considered when he requested more time to provide documentary evidence after the hearing; this request for more time will be discussed in the second part of these reasons.

[12] It is true that, in this record, the applicant received three notices of hearing. The first was sent on July 7, 2009, and indicated that the hearing would be held on August 17, 2009, in Montréal. A few weeks later, the applicant and his family moved to Alberta, and the RPD was notified. On August 5, a new notice of hearing was sent changing only the time of the hearing to 1:30 p.m. on August 17, 2009, in Montréal. Although this does not appear in the record, it is clear that counsel for the applicants contacted the RPD to advise them that the applicant and his family could not afford to travel to Montréal. On August 14, a third notice of hearing indicated that it would take place at 11:30 a.m., Calgary time, and that it would be held by videoconference between Calgary and Montréal. Nothing indicates that the applicant requested that the hearing be adjourned.

[13] As to the issue of a better copy of the work card, the Court notes that Mr. Mercado testified that he did not have the original of this document in Calgary because it was in Venezuela.

[14] At the hearing, Mr. Mercado asked for more time to provide additional documentary evidence to support his claim, but the request was refused. The RPD issued its decision on the merits the following day.

[15] Essentially, Mr. Mercado’s claim was dismissed because the RPD found that the applicant was not credible. This finding was based on contradictions and omissions between the PIF and the evidence adduced at the hearing, including the medical report (presumably, this was an excerpt from the hospital record in Venezuela whose name the applicant could not recall). In its decision, the RPD also noted that the driver’s licence was issued by the state of Georgia on January 8 but the applicant stated that he was in Venezuela on that date. The panel also rejected his explanation that the licence was renewed on the Internet.

[16] Contrary to what was briefly argued in one of the applicant’s three memoranda, the omissions and contradictions noted in the decision do not deal with peripheral facts. As mentioned at the hearing, the Court is satisfied that, as the RPD indicated, they involve facts that are at the very heart of Mr. Mercado’s story (see paragraph 7 above). Accordingly, there is no need to discuss this issue further in these reasons.

[17] This is the context in which the applicant asks the Court to set aside this decision. First, he alleges that the RPD erred when it wrote at paragraph 12 of the decision: “the Claimant did not submit any document confirming his presence in his country. . . . However, he had no document showing that he worked for the Ministry of the Interior, such as a tax document, registration with the municipality, a pay stub from his employer or any other document.”

[18] He also submits that the RPD breached the principles of natural justice by refusing to grant him more time after the hearing to permit him to file his income tax return or something from [translation] “someone who could place him at his workplace.”[8]

[19] The applicant submits that the RPD imposed too heavy a burden by requiring him to file official proof. He also alleges that he was judged more severely when he asked for more time to file evidence because he was represented by experienced counsel.

[20] Finally, referring to an unsigned, undated note whose origin remains nebulous,[9] the applicant argues that he should have been informed at or before the hearing that the Refugee Protection Officer (RPO) and the RPD doubted his story and the [translation] “medical report” filed, given the clear contradiction between the date his driver’s licence was issued and his story that he was in Venezuela in January 2007.

[21] Counsel for the applicant submits that this is especially serious considering that the applicant did not receive the screening form that is in the certified record, which states that, as of January 13, 2009, the issues included his credibility. The Court allowed the parties to file supplementary representations after the hearing on this issue.
Analysis

[22] It is settled law that the reasonableness standard of review applies to the assessment of a refugee claimant’s credibility and the evidentiary weight of the documentation submitted by the claimant: Dunsmuir v. New Brunswick, 2008 SCC 9, [2008] 1 S.C.R. 190 (Dunsmuir) at paragraphs 47, 53, Cadet v. Canada (Minister of Citizenship and Immigration), 2009 FC 723, [2009] F.C.J. No. 864 (QL) at paragraph 12.

[23] With respect to the breaches of procedural fairness raised by the applicant, these questions are reviewable against the standard of correctness: Canada (Citizenship and Immigration) v. Khosa, 2009 SCC 12, [2009] 1 S.C.R. 339 at paragraph 111 and Sketchley v. Canada (A.G.), 2005 FCA 404, [2005] F.C.J. No. 2056, (QL) at paragraphs 52 to 55.

[24] The Court cannot accept the applicant’s position that paragraph 12 of the decision indicates that the panel did not consider the documents he submitted. In addition to specific questions and comments during the hearing about these documents, a simple review of this nine‑page decision is sufficient to conclude that the RPD examined this evidence properly. Indeed, it refers to each of the documents, and its comments indicate that it assigned very little probative value to them and that it did not accept the applicant’s explanations.

[25] It is obvious that the decision could have been written better and that the RPD would benefit from expressing its thoughts more clearly. However, paragraph 12 of the decision must be read in its context, and, having done so, the Court is satisfied that the ambiguity results solely from a literal interpretation. In the Court’s view, the panel’s reasoning with respect to the evidence before it was sufficiently developed to enable the principal applicant to assert his rights on a judicial review: Via Rail Canada Inc. v. National Transportation Agency, [2001] 2 F.C. 25, [2000] F.C.J. No. 1685 (QL), at paragraphs 19, 24.

[26] The Court is also satisfied that the RPD’s decision to assign little probative value to the documents was reasonable.

[27] First, contrary to the applicable rules, the applicant did not submit the original of his work identity card and provided no explanation for failing to do so. It should also be noted that counsel for the applicant only decided to submit this copy of poor quality near the end of the hearing when the panel commented on the lack of documentary evidence to establish that the applicant, in fact, had worked for the Ministry of the Interior.

[28] The Court cannot accept that the applicant did not have the time to prepare because he did not know where or when his hearing would take place or that he did not know he could request the original. Counsel for the applicant requested a hearing date in May 2009. At that point, the applicant should have had in hand all the documents in support of his claim, which necessarily includes the available documentary evidence to establish that he was indeed in Venezuela during the relevant period (March 2006 to October 1, 2007) and that he was working there.

[29] The lawyer’s letter does not indicate the date of the meeting and refers to an immigration consultation whereas the applicant says he consulted a lawyer about his problems with the Circulos Bolivarianos. That document does not corroborate the applicant’s testimony on a key element of the story, i.e. the persecution that commenced in June/July 2006. As the RPD noted, it could have been written by anyone. It is not on letterhead and does not indicate the lawyer’s coordinates. In fact, the consultation it refers to could also have taken place by telephone rather than in person. Both this document and the medical report refer to the number of the applicant’s official identity card, a document that was not entered into evidence.

[30] As the RPD indicated at the hearing, since the applicant worked in Venezuela for nearly 18 months, the panel could reasonably expect that he would file pay stubs, copies of pay cheques, a tax return or a document showing that he had filed a tax return.

[31] As to the medical report, again, it is a photocopy dated prior to the events described very generally in the PIF. Not only did the applicant fail to mention any prosecution in June[10] in his PIF but, even more important, he did not mention the attack and the visit to the hospital. When he testified, Mr. Mercado was vague about this and did not describe the attack.

[32] The jurisprudence is clear that failing to file supporting documentation that it is reasonable to expect may have an impact on an applicant’s credibility: A.M. v. Canada (Minister of Citizenship and Immigration), 2005 FC 579, [2005] F.C.J. No. 709 (QL) at paragraph 20 and Nechifor v. Canada (Minister of Citizenship and Immigration), 2003 FC 1004, [2003] F.C.J. No. 1278 (QL) at paragraph 6. Moreover, as Justice Marc Nadon noted in Hamid v. Canada (Minister of Employment and Immigration) (1995), 58 A.C.W.S. (3d) 469, [1995] F.C.J. No. 1293 (F.C.) (QL) at paragraph 20:
Once a Board, as the present Board did, comes to the conclusion that an applicant is not credible, in most cases, it will necessarily follow that the Board will not give that applicant's documents much probative value, unless the applicant has been able to prove satisfactorily that the documents in question are truly genuine. In the present case, the Board was not satisfied with the applicant's proof and refused to give the documents at issue any probative value. Put another way, where the Board is of the view, like here, that the applicant is not credible, it will not be sufficient for the applicant to file a document and affirm that it is genuine and that the information contained therein is true. Some form of corroboration or independent proof will be required to "offset" the Board's negative conclusion on credibility.
See also Singh v. Canada (Minister of Citizenship and Immigration), 2006 FC 756, [2006] F.C.J. No. 1054 (QL) at paragraph 17, Zaloshnja v. Canada (Minister of Citizenship and Immigration), 2003 FCT 206, [2003] F.C.J. No. 272 at paragraph 9.

[33] In the circumstances, the RPD’s assessment of the testimonial and documentary evidence[11] is within the parameters of reasonability and is “defensible in respect of the facts and law”: Dunsmuir at paragraph 47.

[34] I must now determine whether the RPD breached the principles of procedural fairness. Since the applicant’s arguments based on the absence of the screening form, the RPD’s failure to advise him in a timely manner of its doubts about the date his licence was issued and the lack of probative value of his medical report were not made before the RPD, I believe it is necessary to first examine the legality of the RPD’s refusal based simply on the Refugee Protection Division Rules, SOR/2002‑228 (the Rules).

[35] Under Rules 29 and 36,[12] the applicant was required to file a copy of the documents in support of his claim 20 days before the hearing and provide the original of the documents no later than the day of the hearing. If he was unable to comply with those deadlines, he had to provide a reasonable explanation for his failure to do so in accordance with Rule 7. Rules 30 and 37 give discretion to the RPD to admit new evidence at or after the hearing. The factors that the RPD must consider in exercising this discretion are the same in both Rules: (a) the relevance and probative value of the document, (b) any new evidence it brings to the proceedings, and (c) whether the party, with reasonable effort, could have complied with the deadlines in Rule 29.

[36] The RPD denied the applicant’s oral request at the hearing. It also referred to this request in its decision and noted that the applicant’s lack of effort undermined his credibility.

[37] After meticulously reviewing the transcript and the reasons, the Court is satisfied that the panel properly applied the test set out in the Rules. It specifically asked the applicant why he had not provided his income tax return and whether in fact it was available. It considered the fact that the applicant worked for at least 18 months for the Ministry of the Interior. It also took into account that, in response to a question from his counsel as to whether he had payment receipts or some other official document from his employer, Mr. Mercado simply indicated that he could obtain a document from [translation] “someone who could place him at his workplace.” In addition, when his counsel expressly requested more time to produce his income tax return, Mr. Mercado indicated [translation] “I’m not sure that it’s available”.

[38] The panel clearly took into consideration the fact that the applicant was educated and that he was represented by experienced counsel. Contrary to the applicant’s argument, the RPD did not impose a heavier burden on him simply because he was represented by this counsel. That was simply a part of the facts relevant to assessing the reasonable efforts that could objectively be expected on the part of a person in the applicant’s position. The panel also assessed the explanation given for his failure to provide his income tax return. It is clear from the panel’s comments that it considered the probative value (lack of official stamp) of this document if it had been adduced as part of the evidence it heard. In accordance with the principle articulated in the jurisprudence cited above at paragraph 32, it was open to the panel to find that filing an unofficial document would not have mitigated the problem of the applicant’s credibility, considering the fact that the applicant’s credibility was already in question.

[39] There is no doub

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 19540:2 · paragraphs 64-65

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b41fc51ab8e8896a5cd512c50b5b7db5cbb7d8b5d59e5dbebe373f26fc38ee8e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 19540:2:subtheme:1 · paragraphs 64-65

- Raw key terms: `application, case, certification, court, dismissed, facts, finds, foregoing`
- Display key terms: `case, certification, dismissed, facts, finds, foregoing`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: case, certification, dismissed, facts, finds, foregoing Operative outcome context: [64] In light of the foregoing, the application is dismissed. Evidence spans paragraphs 64-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4926217` offsets `51-60`; context: [64] In light of the foregoing, the application is dismissed.
- Evidence: `issue` cue `question` at chunk `4926218` offsets `37-45`; context: [65] The parties did not propose any question for certification, and the Court finds that the outcome of this case turns on its own facts.

#### Section text

[64] In light of the foregoing, the application is dismissed.

[65] The parties did not propose any question for certification, and the Court finds that the outcome of this case turns on its own facts.


## 19540:3 · paragraphs 66-71

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `98e98cd00a0ecfabc2ed6e230f5a6a12cd5c2c0f3064b95b035de28e54e50737`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 19540:3:subtheme:1 · paragraphs 66-71

- Raw key terms: `beginning, canada, certified, lists, record, acceptable, acceptables, additional`
- Display key terms: `beginning, certified, lists, acceptable, acceptables, additional`
- Argument roles: `evidence_fact`
- Explanation: Observed roles: evidence_fact Display terms: beginning, certified, lists, acceptable, acceptables, additional Evidence spans paragraphs 66-71. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `record` at chunk `4926223` offsets `39-45`; context: [5] See also page 249 of the certified record where he said he discovered these lists in July 2009, and page 243 of the certified record where he indicated that his problems occurred in June/July 2006.

#### Section text

ORDER
THE COURT ORDERS that
The application for judicial review is dismissed.
“Johanne Gauthier”
Judge
Certified true translation
Mary Jo Egan, LLB
ANNEX A
Refugee Protection Division Rules, SOR/2002‑228
Documents establishing identity and other elements of the claim
7. The claimant must provide acceptable documents establishing identity and other elements of the claim. A claimant who does not provide acceptable documents must explain why they were not provided and what steps were taken to obtain them.
18. Before using any information or opinion that is within its specialized knowledge, the Division must notify the claimant or protected person, and the Minister if the Minister is present at the hearing, and give them a chance to
(a) make representations on the reliability and use of the information or opinion;
And
(b) give evidence in support of their representations.
29. (1) If a party wants to use a document at a hearing, the party must provide one copy to any other party and two copies to the Division, unless these Rules require a different number of copies.
Disclosure of documents by the Division
(2) If the Division wants to use a document at a hearing, the Division must provide a copy to each party.
Proof that document was provided
(3) Together with the copies provided to the Division, the party must provide a written statement of how and when a copy was provided to any other party.
Time limit
(4) Documents provided under this rule must be received by the Division or a party, as the case may be, no later than
(a) 20 days before the hearing; or
(b) five days before the hearing if the document is provided to respond to another document provided by a party or the Division.
Use of undisclosed documents
30. A party who does not provide a document as required by rule 29 may not use the document at the hearing unless allowed by the Division. In deciding whether to allow its use, the Division must consider any relevant factors, including
(a) the document’s relevance and probative value;
(b) any new evidence it brings to the hearing; and
(c) whether the party, with reasonable effort, could have provided the document as required by rule 29.
Original documents
36. (1) A party who has provided a copy of a document to the Division must provide the original document to the Division
(a) without delay, on the request in writing of the Division; or
(b) if the Division does not make a request, no later than the beginning of the proceeding at which the document will be used.
Documents mentioned in paragraph 3(2)(c)
(2) On the request in writing of the Division, the Minister must without delay provide to the Division the original of any document mentioned in paragraph 3(2)(c) that is in the possession of an officer.
Additional documents after the hearing has ended
37. (1) A party who wants to provide a document as evidence after a hearing must make an application to the Division.
Written application
(2) The party must attach a copy of the document to the application. The application must be made under rule 44, but the party is not required to give evidence in an affidavit or statutory declaration.
Factors
(3) In deciding the application, the Division must consider any relevant factors, including:
(a) the document’s relevance and probative value;
(b) any new evidence it brings to the proceedings; and
(c) whether the party, with reasonable effort, could have provided the document as required by rule 29.
Documents d’identité et autres éléments de la demande
7. Le demandeur d’asile transmet à la Section des documents acceptables pour établir son identité et les autres éléments de sa demande. S’il ne peut le faire, il en donne la raison et indique quelles mesures il a prises pour s’en procurer.
18. Avant d’utiliser un renseignement ou ne opinion qui est du ressort de sa spécialisation, la Section en avise le demandeur d’asile ou la personne protégée et le ministre — si celui-ci est présent à l’audience et leur donne la possibilité de :
a) faire des observations sur la fiabilité et l’utilisation du renseignement ou de l’opinion;
b) fournir des éléments de preuve à l’appui de leurs observations.
29. (1) Pour utiliser un document à l’audience, la partie en transmet une copie à l’autre partie, le cas échéant, et deux copies à la Section, sauf si les présentes règles exigent un nombre différent de copies.
Communication de documents par la Section
(2) Pour utiliser un document à l’audience, la Section en transmet une copie aux parties.
Preuve de transmission
(3) En même temps qu’elle transmet les copies à la Section, la partie lui transmet également une déclaration écrite indiquant à quel moment et de quelle façon elle en a transmis une copie à l’autre partie, le cas échéant.
Délai
(4) Tout document transmis selon la présente règle doit être reçu par son destinataire au plus tard:
a) soit vingt jours avant l’audience;
b) soit, dans le cas où il s’agit d’un document transmis en réponse à un document reçu de l’autre partie ou de la Section, cinq jours avant l’audience.
Utilisation d’un document non communiqué
30. La partie qui ne transmet pas un document selon la règle 29 ne peut utiliser celui-ci à l’audience, sauf autorisation de la Section. Pour décider si elle autorise l’utilisation du document à l’audience, la Section prend en considération tout élément pertinent. Elle examine notamment:
a) la pertinence et la valeur probante du document;
b) toute preuve nouvelle qu’il apporte;
c) si la partie aurait pu, en faisant des efforts raisonnables, le transmettre selon la règle 29.
Documents originaux
36. (1) La partie transmet à la Section l’original de tout document dont elle lui a transmis copie:
a) sans délai, si la Section le lui demande par écrit;
b) sinon, au plus tard au début de la procédure au cours de laquelle le document sera utilisé.
Documents mentionnés à l’alinéa 3(2)c)
(2) Sur demande écrite de la Section, le ministre transmet à celle-ci, sans délai, l’original de tout document mentionné à l’alinéa 3(2)c) qui est en la possession de l’agent.
Documents supplémentaires après l’audience
37. (1) Pour transmettre, après l’audience, un document à la Section pour qu’elle l’admette en preuve, la partie en fait la demande à la Section.
Forme de la demande
(2) La partie fait sa demande selon la règle 44 et y joint une copie du document, mais elle n’a pas à y joindre d’affidavit ou de déclaration solennelle.
Éléments à considérer
(3) Pour statuer sur la demande, la Section prend en considération tout élément pertinent. Elle examine notamment:
a) la pertinence et la valeur probante du document;
b) toute preuve nouvelle qu’il apporte;
c) si la partie aurait pu, en faisant des efforts raisonnables, le transmettre selon la règle 29.
FEDERAL COURT
SOLICITORS OF RECORD
DOCKET: IMM-4493-09
STYLE OF CAUSE: WILFREDO JOSE MERCADO, YADIRA BAPTISTA, WILLIE JOSE MERCADO, YANIRA MERCADO and JESUS ANGEL MERCADO BAPTISTA v. MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Montréal, Quebec
DATE OF HEARING: February 23, 2010
REASONS FOR ORDER
AND ORDER BY: MADAM JUSTICE GAUTHIER
DATED: March 12, 2010
APPEARANCES:
Michel Le Brun
FOR THE APPLICANTS
Evan Liosis
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Michel Le Brun, lawyer
Lasalle, Quebec
FOR THE APPLICANTS
John H. Sims, Q.C.
Deputy Attorney General of Canada
Montréal, Quebec
FOR THE RESPONDENT

[1] Also referred to as the Ministry of Internal Relations.

[2] He lived illegally in the United States beginning in 1989.

[3] These lists are well known and their existence is well documented.

[4] The other paragraphs primarily describe his trip from Venezuela to Canada.

[5] See also page 249 of the certified record where he said he discovered these lists in July 2009, and page 243 of the certified record where he indicated that his problems occurred in June/July 2006.

## 19540:4 · paragraphs 72-83

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3f107011a0a653b741249d7f02dd821cc3ef421e3f29d19d10e07b04f2449959`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 19540:4:subtheme:1 · paragraphs 72-76

- Raw key terms: `certified, record, applicant, page, amend, arrival, attack, began`
- Display key terms: `certified, page, amend, arrival, attack, began`
- Argument roles: `evidence_fact`
- Explanation: Observed roles: evidence_fact Display terms: certified, page, amend, arrival, attack, began Evidence spans paragraphs 72-76. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `record` at chunk `4926224` offsets `34-40`; context: [6] See page 254 of the certified record.
- Evidence: `evidence_fact` cue `record` at chunk `4926225` offsets `108-114`; context: [7] This is the document that the panel and counsel for the applicant refer to at page 271 of the certified record when they discuss [translation] “the lawyer’s letter”.
- Evidence: `evidence_fact` cue `record` at chunk `4926226` offsets `22-28`; context: [8] See the certified record at pages 271 to 274.

#### 19540:4:subtheme:2 · paragraphs 77-83

- Raw key terms: `document, applicant, counsel, licence, american, annex, asked, assistant`
- Display key terms: `document, licence, american, annex, asked, assistant`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: document, licence, american, annex, asked, assistant Evidence spans paragraphs 77-83. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4926229` offsets `9-14`; context: [11] The issue of the American driver’s licence is examined later.
- Evidence: `evidence_fact` cue `evidence` at chunk `4926231` offsets `176-184`; context: Mercado’s licence was included in the documents photocopied by the immigration authorities in November 2007, there is no evidence that this document was in the RPD’s file before it was filed in July.
- Evidence: `evidence_fact` cue `record` at chunk `4926235` offsets `33-39`; context: 240 of the certified record.

#### Section text

[6] See page 254 of the certified record.

[7] This is the document that the panel and counsel for the applicant refer to at page 271 of the certified record when they discuss [translation] “the lawyer’s letter”.

[8] See the certified record at pages 271 to 274.

[9] See paragraph 48 and following.

[10] The only explanation provided by the applicant on this point was that he did not know he could amend his PIF. He did not indicate how, on his arrival in Canada in 2007, he could have forgotten the attack in June 2006 or made a mistake as to the time when his problems began.

[11] The issue of the American driver’s licence is examined later.

[12] The relevant Rules are reproduced in Annex A.

[13] Even if, as counsel for the applicant stated, Mr. Mercado’s licence was included in the documents photocopied by the immigration authorities in November 2007, there is no evidence that this document was in the RPD’s file before it was filed in July.

[14] In a letter dated January 6, 2010, the RPD’s Assistant Deputy Chairperson asked counsel for the applicant to explain the source of this document.

[15] The beginning of the document summarizes other facts in the PIF.

[16] October 10, 2007.

[17] See p. 240 of the certified record.
